#!/usr/bin/env bash
# Render apps/*.svg to 256 px PNGs with headless Chrome (Unraid caches container icons as PNG).
# Usage: CHROME=/path/to/chrome ./render_apps.sh
set -euo pipefail
cd "$(dirname "$0")/apps"
CHROME="${CHROME:-chrome}"
abs() { command -v cygpath >/dev/null && cygpath -m "$PWD/$1" || echo "$PWD/$1"; }
for svg in *.svg; do
  name="${svg%.svg}"
  printf '<html><body style="margin:0;background:transparent"><img src="%s" width="256" height="256"></body></html>' "$svg" > "_render.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --default-background-color=00000000 \
    --window-size=256,256 --screenshot="$(abs "$name.png")" "file:///$(abs _render.html)" >/dev/null 2>&1
  echo "apps/$name.png"
done
rm -f _render.html
