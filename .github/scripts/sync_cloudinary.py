#!/usr/bin/env python3
"""
Sync Cloudinary photos into Jekyll album .md files.
"""

import os
import re
import glob
import requests

CLOUD_NAME = os.environ["CLOUDINARY_CLOUD_NAME"]
API_KEY    = os.environ["CLOUDINARY_API_KEY"]
API_SECRET = os.environ["CLOUDINARY_API_SECRET"]


def cloudinary_search(folder: str) -> list:
    url = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/resources/search"
    payload = {
        "expression": f'folder="{folder}"',
        "max_results": 500,
        "sort_by": [{"public_id": "asc"}],
        "fields": ["secure_url", "public_id", "format"]
    }
    resp = requests.post(url, json=payload, auth=(API_KEY, API_SECRET), timeout=30)
    resp.raise_for_status()
    return resp.json().get("resources", [])


def parse_front_matter(content: str):
    match = re.match(r"^---\n(.*?)\n---\s*\n?(.*)", content, re.DOTALL)
    if not match:
        return None, content
    return match.group(1), match.group(2)


def update_album_file(filepath: str) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_front_matter(content)
    if fm is None:
        print(f"  ⚠️  {filepath}: nessun front matter, skip.")
        return False

    # Cerca cloudinary_folder
    folder_match = re.search(r'^cloudinary_folder:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    if not folder_match:
        print(f"  ⏭️  {filepath}: nessun cloudinary_folder, skip.")
        return False

    folder = folder_match.group(1).strip()
    print(f"  📁 {filepath}: sincronizo cartella '{folder}'...")

    # Titolo per alt text
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Foto"

    # Fetch foto
    try:
        resources = cloudinary_search(folder)
    except requests.HTTPError as e:
        print(f"  ❌ Errore Cloudinary: {e}")
        return False

    print(f"  ✅ Trovate {len(resources)} foto.")

    # Rimuovi blocchi foto: e foto_count: esistenti
    fm_clean = re.sub(r'^foto_count:.*$\n?', '', fm, flags=re.MULTILINE)
    fm_clean = re.sub(r'^foto:.*?(?=^\w|\Z)', '', fm_clean, flags=re.MULTILINE | re.DOTALL)
    fm_clean = fm_clean.rstrip()

    # Costruisci nuovo blocco foto
    foto_lines = [f"foto_count: {len(resources)}", "foto:"]
    for r in resources:
        foto_lines.append(f'  - url: "{r["secure_url"]}"')
        foto_lines.append(f'    alt: "{title}"')

    new_fm = fm_clean + "\n" + "\n".join(foto_lines)
    new_content = f"---\n{new_fm}\n---\n{body}"

    if new_content == content:
        print(f"  ✨ Nessuna modifica necessaria.")
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  💾 File aggiornato con {len(resources)} foto.")
    return True


def main():
    files = glob.glob("_pages/album-*.md")
    if not files:
        print("Nessun file album trovato.")
        return

    print(f"🔍 Trovati {len(files)} file album:\n")
    changed = 0
    for fp in sorted(files):
        if update_album_file(fp):
            changed += 1

    print(f"\n✅ Completato. {changed}/{len(files)} file aggiornati.")
    
    with open(filepath, "r", encoding="utf-8") as f:
        preview = f.read(500)
    print(f"  🔍 Preview:\n{preview[:500]}")


if __name__ == "__main__":
    main()