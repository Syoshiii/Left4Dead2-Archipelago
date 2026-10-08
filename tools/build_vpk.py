"""Build dist/l4d2_ap_mod.vpk from the addon/l4d2_ap_mod folder.

Requires: pip install vpk
Usage: python tools/build_vpk.py
"""
from pathlib import Path

import vpk

ROOT = Path(__file__).resolve().parent.parent
ADDON_DIR = ROOT / "addon" / "l4d2_ap_mod"
OUTPUT = ROOT / "dist" / "l4d2_ap_mod.vpk"

OUTPUT.parent.mkdir(exist_ok=True)
pak = vpk.new(str(ADDON_DIR))
pak.version = 1  # Left 4 Dead 2 only reads VPK version 1 ("Unknown version 2 for vpk")
pak.save(str(OUTPUT))
print(f"Created: {OUTPUT}")
