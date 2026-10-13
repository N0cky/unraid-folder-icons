# Unraid Folder Icons

Animierte Ordner-Icons für [FolderView3](https://forums.unraid.net/topic/197223-plugin-folderview3/) auf Unraid.
Farbige Kacheln mit weißem Symbol und einer dezenten Animation, die direkt in der SVG steckt.
Sie funktionieren deshalb als ganz normales Bild-URL im Icon-Feld eines Ordners.

| | | | | | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| <img src="icons/datenbanken.svg" width="64"><br>`datenbanken` | <img src="icons/netzwerk.svg" width="64"><br>`netzwerk` | <img src="icons/medien.svg" width="64"><br>`medien` | <img src="icons/downloads.svg" width="64"><br>`downloads` | <img src="icons/youtube.svg" width="64"><br>`youtube` | <img src="icons/buecher.svg" width="64"><br>`buecher` | <img src="icons/nextcloud.svg" width="64"><br>`nextcloud` |
| <img src="icons/buero.svg" width="64"><br>`buero` | <img src="icons/monitoring.svg" width="64"><br>`monitoring` | <img src="icons/bunk-media.svg" width="64"><br>`bunk-media` | <img src="icons/weitara.svg" width="64"><br>`weitara` | <img src="icons/smart-home.svg" width="64"><br>`smart-home` | <img src="icons/gaming.svg" width="64"><br>`gaming` | <img src="icons/backup.svg" width="64"><br>`backup` |

## Verwendung

In FolderView3 beim Ordner als Icon eintragen (feste Version, damit sich nichts unbemerkt ändert):

```
https://cdn.jsdelivr.net/gh/N0cky/unraid-folder-icons@v1.3.0/icons/<name>.svg
```

Wer `prefers-reduced-motion` aktiviert hat, bekommt die Icons ohne Animation.

## App-Icons

Für Container ohne brauchbares Logo und für Benachrichtigungen (z. B. ntfy) liegen statische
App-Icons in [`apps/`](apps/) (SVG + 256 px PNG, da Unraid Container-Icons als PNG cached):

| | |
|:-:|:-:|
| <img src="apps/parse-dmarc.png" width="64"><br>`parse-dmarc` | <img src="apps/nas-backup.png" width="64"><br>`nas-backup` |

```
https://cdn.jsdelivr.net/gh/N0cky/unraid-folder-icons@v1.2.0/apps/<name>.png
```

PNGs neu rendern: `CHROME=/pfad/zu/chrome ./render_apps.sh`

## Anpassen

Farben, Symbole und Animationen stehen in [`build.py`](build.py). Nach Änderungen neu erzeugen:

```
python build.py
```

`preview.html` zeigt alle Icons in FolderView3-Größe im hellen und dunklen Unraid-Theme
(z. B. mit `python -m http.server` im Repo-Ordner öffnen).

## Credits

- Symbole basieren auf [Tabler Icons](https://tabler.io/icons) (MIT-Lizenz).
- Idee der animierten Ordner-Icons: [hernandito](https://github.com/hernandito/unRAID-Docker-Folder-Animated-Icons---Alternate-Colors).
