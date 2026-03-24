#!/usr/bin/env python3
"""
Sync Cloudinary photos into Jekyll album .md files.

Legge tutti i file _pages/album-*.md, controlla se hanno
il campo `cloudinary_folder`, e aggiorna la lista `foto:`
con tutti gli asset trovati in quella cartella su Cloudinary.
"""

import os
import re
import glob
import json
import requests
import hashlib
import hmac
import time
from urllib.parse import urlencode

CLOUD_NAME  = os.environ["CLOUDINARY_CLOUD_NAME"]
API_KEY     = os.environ["CLOUDINARY_API_KEY"]
API_SECRET  = os.environ["CLOUDINARY_API_SECRET"]


def cloudinary_search(folder: str) -> list[dict]:
    """Recupera tutti gli asset in una cartella Cloudinary via Search API."""
    url = f"https://api.cloudinary.com/v1_1/{CLOUD_NAME}/resources/search"
    
    expression = f'folder="{folder}"'
    payload = {
        "expression": expression,
        "max_results": 500,
        "sort_by": [{"public_id": "asc"}],
        "fields": ["secure_url", "public_id", "format"]
    }
    
    resp = requests.post(
        url,
        json=payload,
        auth=(API_KEY, API_SECRET),
        timeout=30
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("resources", [])


def build_foto_yaml(resources: list[dict], title: str) -> str:
    """Costruisce il blocco YAML della lista foto."""
    if not resources:
        return "foto: []\n"
    
    lines = ["foto:"]
    for r in resources:
        url = r["secure_url"]
        lines.append(f'  - url: "{url}"')
        lines.append(f'    alt: "{title}"')
    return "\n".join(lines) + "\n"


def update_album_file(filepath: str) -> bool:
    """
    Aggiorna un file album .md con le foto da Cloudinary.
    Ritorna True se il file è stato modificato.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Estrai il front matter
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        print(f"  ⚠️  {filepath}: nessun front matter trovato, skip.")
        return False

    front_matter = fm_match.group(1)

    # Controlla se ha cloudinary_folder
    folder_match = re.search(r'^cloudinary_folder:\s*["\']?(.+?)["\']?\s*$', front_matter, re.MULTILINE)
    if not folder_match:
        print(f"  ⏭️  {filepath}: nessun cloudinary_folder, skip.")
        return False

    folder = folder_match.group(1).strip()
    print(f"  📁 {filepath}: sincronizo cartella '{folder}'...")

    # Estrai il titolo per l'alt text
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', front_matter, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Foto"

    # Recupera foto da Cloudinary
    try:
        resources = cloudinary_search(folder)
    except requests.HTTPError as e:
        print(f"  ❌ Errore Cloudinary per '{folder}': {e}")
        return False

    print(f"  ✅ Trovate {len(resources)} foto.")

    # Costruisci il nuovo blocco foto
    new_foto_block = build_foto_yaml(resources, title)

    # Sostituisci o aggiungi il blocco foto nel front matter
    if re.search(r'^foto:', front_matter, re.MULTILINE):
        # Rimuovi il blocco foto esistente (multi-riga)
        new_fm = re.sub(
            r'^foto:.*?(?=^\w|\Z)',
            new_foto_block,
            front_matter,
            flags=re.MULTILINE | re.DOTALL
        )
    else:
        # Aggiungi alla fine del front matter
        new_fm = front_matter.rstrip() + "\n\n" + new_foto_block

    # Aggiorna anche foto_count
    count = len(resources)
    if re.search(r'^foto_count:', new_fm, re.MULTILINE):
        new_fm = re.sub(r'^foto_count:\s*\d+', f'foto_count: {count}', new_fm, flags=re.MULTILINE)
    else:
        new_fm = new_fm.rstrip() + f"\nfoto_count: {count}\n"

    # Ricostruisci il file
    new_content = f"---\n{new_fm}---\n"
    
    # Scrivi solo se cambiato
    if new_content == content:
        print(f"  ✨ Nessuna modifica necessaria.")
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"  💾 File aggiornato con {count} foto.")
    return True


def main():
    pattern = "_pages/album-*.md"
    files = glob.glob(pattern)
    
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