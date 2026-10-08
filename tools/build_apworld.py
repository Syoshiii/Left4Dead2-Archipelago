"""Build dist/L4D2.apworld from the apworld/L4D2 folder.

An .apworld is a zip containing the world folder and its archipelago.json manifest.
Like Archipelago's "Build APWorlds" component, the packaged manifest gets the
container "version" and "compatible_version" fields added (never written in the source).
Usage: python tools/build_apworld.py
"""
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORLD_DIR = ROOT / "apworld" / "L4D2"
MANIFEST = WORLD_DIR / "archipelago.json"
OUTPUT = ROOT / "dist" / "L4D2.apworld"

# Container format of Archipelago 0.6.8 (worlds/Files.py)
CONTAINER_VERSION = 7

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
manifest.update({"version": CONTAINER_VERSION, "compatible_version": CONTAINER_VERSION})

OUTPUT.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(WORLD_DIR.rglob("*")):
        if path.is_file() and path != MANIFEST and "__pycache__" not in path.parts:
            archive.write(path, path.relative_to(WORLD_DIR.parent))
    archive.writestr(f"{WORLD_DIR.name}/archipelago.json", json.dumps(manifest, indent=4))

print(f"Created: {OUTPUT} (world version {manifest['world_version']})")
