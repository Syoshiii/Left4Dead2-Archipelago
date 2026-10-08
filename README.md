# Left 4 Dead 2 – Archipelago

An [Archipelago](https://archipelago.gg) integration for Left 4 Dead 2 (unofficial world).

This project is a continuation, led by **Syoshi**, of the work of **YufiiEvershade** ([original repository](https://github.com/yufiievershade/Left-4-Dead-2-Archipelago)). The goal is a stable, maintained version of the world with new options to customize it the way you want.

## Status

Early alpha, in progress. The first milestone is a minimal, stable version: locked campaigns, one check per safe room, an optional melee-only mode, no traps. Targets Archipelago 0.6.8.

## Repository contents

| Folder | Purpose |
|---|---|
| `apworld/L4D2/` | The Archipelago world: items, locations, options, logic |
| `client/` | Companion client bridging the AP server and the game |
| `addon/l4d2_ap_mod/` | Content of the `.vpk` addon: "Archipelago" mutation, scripts, missions |
| `tools/` | Build scripts (`.apworld`, `.vpk`, `.smx`) |

The SourceMod plugins run in game. Their sources are not published in this repository: the compiled `.smx` files are provided with each [release](../../releases).

## How it works

```
AP server  <--websocket-->  client/ap_companion.py  <--files-->  SourceMod plugins (game)
```

The client and the plugins communicate through files in `left4dead2/addons/sourcemod/data/`:

- `archipelago_status.json` (client → game): unlocked campaigns and items
- `archipelago/mod_data/location_check.txt` (game → client): queue of completed locations, one `seed|ID` line each
- `archipelago/mod_data/starting_items.txt` (client → game): starting equipment (including the melee-only starting weapon)

## Build

```bash
python tools/build_apworld.py     # -> dist/L4D2.apworld
pip install vpk
python tools/build_vpk.py         # -> dist/l4d2_ap_mod.vpk
pip install -r client/requirements.txt pyinstaller
pyinstaller client/ap_companion.spec   # -> dist/ap_companion.exe
```

## Installation (game)

1. Install [Metamod:Source](https://www.sourcemm.net/downloads.php?branch=stable) and [SourceMod](https://www.sourcemod.net/downloads.php?branch=stable).
2. Copy the `.smx` files from the release into `left4dead2/addons/sourcemod/plugins/`.
3. Copy `l4d2_ap_mod.vpk` into `left4dead2/addons/`.
4. Copy `L4D2.apworld` into Archipelago's `custom_worlds` folder.
5. Launch the game with `-insecure`, pick the **Archipelago** mutation, then start the client.

## Contributing

Contributions are welcome. All changes go through pull requests: fork the repository, work on a branch, and open a PR against `main`. Direct pushes to `main` are not allowed. If you would like to get more involved, feel free to ask.

## Credits

- **YufiiEvershade**: Original Author of the world, the client and the plugins
- **Syoshi**: Project Lead, current Developer and Maintainer
- **NaotoADB** (ADBsArt), **DaftValac**: Co-Authors of the original addon
- **Nep**: APSkeleton Template used as the base of the world (see `LICENSE`)

## Thanks

A huge thank you to **Yufii**, who created this world, the client and the plugins, and generously gave their blessing, advice and access to the original sources so the project could live on. None of this would exist without Yufii's work.
