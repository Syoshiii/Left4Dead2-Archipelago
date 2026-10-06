"""Construit dist/l4d2_ap_mod.vpk à partir du dossier addon/l4d2_ap_mod.

Nécessite : pip install vpk
Usage : python tools/build_vpk.py
"""
from pathlib import Path

import vpk

ROOT = Path(__file__).resolve().parent.parent
ADDON_DIR = ROOT / "addon" / "l4d2_ap_mod"
OUTPUT = ROOT / "dist" / "l4d2_ap_mod.vpk"

OUTPUT.parent.mkdir(exist_ok=True)
vpk.new(str(ADDON_DIR)).save(str(OUTPUT))
print(f"Créé : {OUTPUT}")
