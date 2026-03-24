#!/usr/bin/env python3
import os
import glob
import requests
import yaml

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


def update_album_file(filepath: str) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Separa front matter e body
    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"  ⚠️  {filepath}: front matter non trovato, skip.")
        return False

    fm = yaml.safe_load(parts[1])
    body = parts[2]

    if not fm or "cloudinary_folder" not in fm:
        print(f"  ⏭️  {filepath}: nessun cloudinary_folder, skip.")
        return False

    folder = fm["cloudinary_folder"]
    title  = fm.get("title", "Foto")
    print(f"  📁 {filepath}: sincronizo cartella '{folder}'...")

    try:
        resources = cloudinary_search(folder)
    except requests.HTTPError as e:
        print(f"  ❌ Errore Cloudinary: {e}")
        return False

    print(f"  ✅ Trovate {len(resources)} foto.")

    # Aggiorna il front matter
    fm["foto_count"] = len(resources)
    fm["foto"] = [{"url": r["secure_url"], "alt": title} for r in resources]

    # Riscrivi il file manualmente (non con yaml.dump per preservare la formattazione)
    lines = ["---"]
    # Campi semplici nell'ordine originale
    simple_keys = ["layout", "title", "permalink", "cloudinary_folder", 
                   "data", "anno", "categoria", "descrizione", "cover", "og_image"]
    for key in simple_keys:
        if key in fm:
            val = fm[key]
            if isinstance(val, str):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")

    lines.append(f"foto_count: {len(resources)}")
    lines.append("foto:")
    for foto in fm["foto"]:
        lines.append(f'  - url: "{foto["url"]}"')
        lines.append(f'    alt: "{foto["alt"]}"')
    lines.append("---")
    lines.append(body.lstrip("\n"))

    new_content = "\n".join(lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  💾 Scritte {len(resources)} foto in {filepath}.")
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


if __name__ == "__main__":
    main()