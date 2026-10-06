"""Construit dist/L4D2.apworld à partir du dossier apworld/L4D2.

Un .apworld est simplement un zip contenant le dossier du monde.
Usage : python tools/build_apworld.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORLD_DIR = ROOT / "apworld" / "L4D2"
OUTPUT = ROOT / "dist" / "L4D2.apworld"

OUTPUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(WORLD_DIR.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            archive.write(path, path.relative_to(WORLD_DIR.parent))

print(f"Créé : {OUTPUT}")
