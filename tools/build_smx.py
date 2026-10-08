"""Compile the SourceMod plugins (sourcemod/scripting/*.sp) into dist/plugins/.

The .sp sources come from the private repo Left4Dead2-Archipelago-Dev, cloned into sourcemod/.
The compiler is the spcomp shipped with SourceMod (1.12 recommended).

spcomp is looked up in this order:
  1. the --spcomp PATH option
  2. the SPCOMP environment variable
  3. the SourceMod folder of Left 4 Dead 2 (Steam registry + common install paths)

Usage: python tools/build_smx.py [--spcomp PATH] [--install]
  --install: also copy the .smx files into the game's left4dead2/addons/sourcemod/plugins/
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTING_DIR = ROOT / "sourcemod" / "scripting"
OUTPUT_DIR = ROOT / "dist" / "plugins"

SPCOMP_NAME = "spcomp.exe" if os.name == "nt" else "spcomp"
SOURCEMOD_SUBDIR = Path("left4dead2") / "addons" / "sourcemod"

COMMON_L4D2_PATHS = [
    r"C:\Program Files (x86)\Steam\steamapps\common\Left 4 Dead 2",
    r"C:\Program Files\Steam\steamapps\common\Left 4 Dead 2",
    r"D:\Steam\steamapps\common\Left 4 Dead 2",
    r"D:\SteamLibrary\steamapps\common\Left 4 Dead 2",
    r"E:\SteamLibrary\steamapps\common\Left 4 Dead 2",
    r"F:\SteamLibrary\steamapps\common\Left 4 Dead 2",
]


def find_l4d2_paths():
    # Return the Left 4 Dead 2 install folders found on this machine.
    paths = []
    if os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam") as key:
                steam_path = winreg.QueryValueEx(key, "InstallPath")[0]
            paths.append(Path(steam_path) / "steamapps" / "common" / "Left 4 Dead 2")
        except OSError:
            pass
    paths += [Path(p) for p in COMMON_L4D2_PATHS]

    found = []
    for path in paths:
        if path.is_dir() and path not in found:
            found.append(path)
    return found


def find_spcomp(cli_path):
    # Return the path of spcomp, or None.
    if cli_path:
        return Path(cli_path)
    if os.environ.get("SPCOMP"):
        return Path(os.environ["SPCOMP"])
    for l4d2 in find_l4d2_paths():
        candidate = l4d2 / SOURCEMOD_SUBDIR / "scripting" / SPCOMP_NAME
        if candidate.is_file():
            return candidate
    return None


def main():
    parser = argparse.ArgumentParser(description="Compile the SourceMod plugins into dist/plugins/.")
    parser.add_argument("--spcomp", help="path to spcomp (spcomp.exe on Windows)")
    parser.add_argument("--install", action="store_true",
                        help="also copy the .smx files into the game's SourceMod plugins folder")
    args = parser.parse_args()

    sources = sorted(SCRIPTING_DIR.glob("*.sp"))
    if not sources:
        sys.exit(f"No .sp file found in {SCRIPTING_DIR} (is the Dev repo cloned into sourcemod/?)")

    spcomp = find_spcomp(args.spcomp)
    if spcomp is None or not spcomp.is_file():
        sys.exit("spcomp not found. Install SourceMod in the game, "
                 "or pass --spcomp PATH or set the SPCOMP variable.")
    include_dir = spcomp.parent / "include"

    print(f"Compiler: {spcomp}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    failed = []
    for source in sources:
        output = OUTPUT_DIR / f"{source.stem}.smx"
        result = subprocess.run(
            [str(spcomp), str(source), f"-i{include_dir}", f"-o{output}"],
            capture_output=True, text=True,
        )
        messages = [line for line in (result.stdout + result.stderr).splitlines()
                    if "error" in line.lower() or "warning" in line.lower()]
        if result.returncode != 0 or not output.is_file():
            failed.append(source.name)
            print(f"FAILED {source.name}")
        else:
            print(f"OK     {source.name}")
        for line in messages:
            print(f"       {line}")

    if failed:
        sys.exit(f"{len(failed)} plugin(s) failed: {', '.join(failed)}")
    print(f"Created: {OUTPUT_DIR}")

    if args.install:
        plugins_dir = spcomp.parent.parent / "plugins"
        if not plugins_dir.is_dir():
            sys.exit(f"Plugins folder not found: {plugins_dir}")
        for smx in sorted(OUTPUT_DIR.glob("*.smx")):
            shutil.copy2(smx, plugins_dir / smx.name)
        print(f"Copied to: {plugins_dir}")


if __name__ == "__main__":
    main()
