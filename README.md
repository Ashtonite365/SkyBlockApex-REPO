# SkyBlockApex-REPO

Item and recipe data for SkyBlock Apex, in NEU-REPO JSON format, shipped as one lossless bundle.

- `repo.json.zst`: zstd-compressed JSON `{"format":"apex-repo-bundle","version":1,"files":{"<path>":"<file text>"}}`. Unpacking gives a folder (`items/`, `constants/`) that neurepoparser 1.11.0 loads with `NEURepository.of(path)`.
- `manifest.json`: bundle version, sha256, item and recipe counts, build date.
- `tools/unpack.py`: `python3 tools/unpack.py repo.json.zst out/ manifest.json`

Data comes from the Hypixel API, hypixelskyblock.minecraft.wiki and Fandom. Licence: MIT (see LICENSE).
