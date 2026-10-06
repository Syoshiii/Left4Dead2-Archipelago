# Left 4 Dead 2 – Archipelago

Intégration [Archipelago](https://archipelago.gg) pour Left 4 Dead 2 (monde non officiel).

Ce projet reprend le travail de **YufiiEvershade** ([dépôt d'origine](https://github.com/yufiievershade/Left-4-Dead-2-Archipelago)).
L'objectif est d'avoir une version stable et maintenue. Le système de traps est volontairement retiré pour l'instant.

## Contenu du dépôt

| Dossier | Rôle |
|---|---|
| `apworld/L4D2/` | Le monde Archipelago : items, locations, options, logique |
| `client/` | Client compagnon qui fait le lien entre le serveur AP et le jeu |
| `sourcemod/scripting/` | Sources des plugins SourceMod, qui tournent dans le jeu |
| `addon/l4d2_ap_mod/` | Contenu de l'addon `.vpk` : mutation « Archipelago », scripts, missions |
| `tools/` | Scripts de build (`.apworld`, `.vpk`) |

## Fonctionnement

```
Serveur AP  <--websocket-->  client/ap_companion.py  <--fichiers-->  plugins SourceMod (jeu)
```

Le client et les plugins échangent par des fichiers dans `left4dead2/addons/sourcemod/data/` :

- `archipelago_status.json` (client → jeu) : campagnes et items débloqués
- `archipelago/mod_data/location_check.txt` (jeu → client) : ID d'une location validée
- `archipelago/mod_data/starting_items.txt` (client → jeu) : équipement de départ

## Build

```bash
python tools/build_apworld.py     # -> dist/L4D2.apworld
pip install vpk
python tools/build_vpk.py         # -> dist/l4d2_ap_mod.vpk
pip install -r client/requirements.txt pyinstaller
pyinstaller client/ap_companion.spec   # -> dist/ap_companion.exe
```

Plugins : compiler chaque `.sp` avec `spcomp` (fourni avec SourceMod, dossier `addons/sourcemod/scripting/`).

## Installation (jeu)

1. Installer [Metamod:Source](https://www.sourcemm.net/downloads.php?branch=stable) et [SourceMod](https://www.sourcemod.net/downloads.php?branch=stable).
2. Copier les `.smx` dans `left4dead2/addons/sourcemod/plugins/`.
3. Copier `l4d2_ap_mod.vpk` dans `left4dead2/addons/`.
4. Copier `L4D2.apworld` dans le dossier `custom_worlds` d'Archipelago.
5. Lancer le jeu en mode `-insecure`, choisir la mutation **Archipelago**, puis lancer le client.

## Crédits

- YufiiEvershade : auteur original du monde, du client et des plugins
- NaotoADB (ADBsArt), DaftValac : co-auteurs de l'addon
- Nep : template APSkeleton ayant servi de base au monde (voir `LICENSE`)
