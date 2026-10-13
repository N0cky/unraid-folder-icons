"""Generate the animated folder icons for Unraid FolderView3.

Each icon is a self-contained SVG: a colored rounded tile with a white
glyph (based on Tabler Icons, MIT) and a subtle CSS animation embedded in
the file, so it animates when used as a plain <img>.

Usage: python build.py   -> writes icons/*.svg
"""

from pathlib import Path

OUT = Path(__file__).parent / "icons"


def mix(hex_color: str, target: str, amount: float) -> str:
    a = [int(hex_color[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(target[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * amount):02x}" for x, y in zip(a, b))


def svg(color: str, body: str, css: str = "", overlay: str = "") -> str:
    top = mix(color, "#ffffff", 0.16)
    bottom = mix(color, "#000000", 0.08)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs>
<style>
.g{{fill:none;stroke:#fff;stroke-width:1.75;stroke-linecap:round;stroke-linejoin:round}}
.f{{fill:#fff}}
.ns{{stroke:none}}
.fb{{transform-box:fill-box;transform-origin:center}}
{css.strip()}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect width="128" height="128" rx="30" fill="url(#bg)"/>
<rect x="1" y="1" width="126" height="126" rx="29" fill="none" stroke="#fff" stroke-opacity=".14" stroke-width="2"/>
{overlay}<g class="g" transform="translate(26 26) scale(3.1667)">
{body.strip()}
</g>
</svg>
"""


ICONS = {
    # Datenbanken: database stack with two blinking activity LEDs
    "datenbanken": ("#475569", """
<path d="M12 6m-8 0a8 3 0 1 0 16 0a8 3 0 1 0 -16 0"/>
<path d="M4 6v6a8 3 0 0 0 16 0v-6"/>
<path d="M4 12v6a8 3 0 0 0 16 0v-6"/>
<circle class="f ns led l1" cx="16.6" cy="11.3" r=".8"/>
<circle class="f ns led l2" cx="16.6" cy="17.3" r=".8"/>
""", """
.led{animation:led 2.8s ease-in-out infinite}
.l2{animation-duration:2.1s;animation-delay:-.9s}
@keyframes led{0%,22%,48%,100%{opacity:1}10%,60%{opacity:.25}}
"""),

    # Netzwerk & Zugriff: globe on a network line, data pulses travel along the lines
    "netzwerk": ("#4F46E5", """
<path d="M6 9a6 6 0 1 0 12 0a6 6 0 0 0 -12 0"/>
<path d="M12 3c1.333 .333 2 2.333 2 6s-.667 5.667 -2 6"/>
<path d="M12 3c-1.333 .333 -2 2.333 -2 6s.667 5.667 2 6"/>
<path d="M6 9h12"/>
<path d="M10 20a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"/>
<path d="M3 20h7M14 20h7M12 15v3" stroke-opacity=".45"/>
<path class="pk p1" d="M3 20h7" pathLength="100"/>
<path class="pk p2" d="M14 20h7" pathLength="100"/>
<path class="pk p3" d="M12 15v3" pathLength="100"/>
""", """
.pk{stroke-dasharray:28 172;stroke-dashoffset:28;animation:pk 3s linear infinite}
.p2{animation-delay:-1.5s}.p3{animation-duration:2s;animation-delay:-.6s}
@keyframes pk{to{stroke-dashoffset:-100}}
"""),

    # Plex & Medien: play button with a soft expanding ring
    "medien": ("#D97706", """
<circle cx="12" cy="12" r="9.25"/>
<circle class="ring fb" cx="12" cy="12" r="9.25"/>
<path class="f fb tri" d="M10.1 8.4v7.2l6 -3.6z" stroke="#fff" stroke-width="1.2"/>
""", """
.ring{animation:ring 3.2s ease-out infinite}
.tri{animation:tri 3.2s ease-in-out infinite}
@keyframes ring{0%{transform:scale(1);opacity:.7}70%,100%{transform:scale(1.22);opacity:0}}
@keyframes tri{0%,100%{transform:scale(1)}15%{transform:scale(1.08)}35%{transform:scale(1)}}
"""),

    # Downloads & Arr: arrow drops into the tray
    "downloads": ("#0D9488", """
<path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"/>
<g class="arr"><path d="M7 11l5 5l5 -5"/><path d="M12 4l0 12"/></g>
""", """
.arr{animation:arr 2.6s ease-in-out infinite}
@keyframes arr{0%,100%{transform:translateY(-1.2px)}45%{transform:translateY(1.4px)}55%{transform:translateY(1.1px)}}
"""),

    # YouTube: player with a progress bar that fills up
    "youtube": ("#DC2626", """
<path d="M2 8a4 4 0 0 1 4 -4h12a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-12a4 4 0 0 1 -4 -4v-8z"/>
<path class="f" d="M10.2 8.4l5 3l-5 3z" stroke="#fff" stroke-width="1.2"/>
<path d="M5.5 17h13" stroke-width="1.2" stroke-opacity=".35"/>
<path class="bar" d="M5.5 17h13" stroke-width="1.2" pathLength="100"/>
""", """
.bar{stroke-dasharray:100 100;stroke-dashoffset:100;animation:bar 6s linear infinite}
@keyframes bar{0%{stroke-dashoffset:100;opacity:1}88%{stroke-dashoffset:0;opacity:1}100%{stroke-dashoffset:0;opacity:0}}
"""),

    # Buecher & Hoerbuecher: open book, a page turns now and then
    "buecher": ("#DB2777", """
<path d="M3 19a9 9 0 0 1 9 0a9 9 0 0 1 9 0"/>
<path d="M3 6a9 9 0 0 1 9 0a9 9 0 0 1 9 0"/>
<path d="M3 6l0 13M12 6l0 13M21 6l0 13"/>
<path class="page" d="M12 6a9 9 0 0 1 9 0v13a9 9 0 0 0 -9 0z" fill="#fff" fill-opacity=".22"/>
""", """
.page{transform-box:fill-box;transform-origin:0% 50%;animation:page 6s ease-in-out infinite}
@keyframes page{0%,50%{transform:scaleX(1);opacity:0}58%{transform:scaleX(1);opacity:1}78%{transform:scaleX(-1);opacity:1}90%,100%{transform:scaleX(-1);opacity:0}}
"""),

    # Nextcloud: floating cloud with the three-ring logo hint
    "nextcloud": ("#0284C7", """
<g class="cloud">
<path d="M6.657 18c-2.572 0 -4.657 -2.007 -4.657 -4.483c0 -2.475 2.085 -4.482 4.657 -4.482c.393 -1.762 1.794 -3.2 3.675 -3.773c1.88 -.572 3.956 -.193 5.444 1c1.488 1.19 2.162 3.007 1.77 4.769h.99c1.913 0 3.464 1.56 3.464 3.486c0 1.927 -1.551 3.487 -3.465 3.487h-11.878"/>
<circle class="r r1" cx="8.2" cy="13.7" r="1.3" stroke-width="1.35"/>
<circle class="r r2" cx="12" cy="13.7" r="2.05" stroke-width="1.35"/>
<circle class="r r3" cx="15.8" cy="13.7" r="1.3" stroke-width="1.35"/>
</g>
""", """
.cloud{animation:cloud 4.5s ease-in-out infinite}
.r{animation:r 3s ease-in-out infinite}.r2{animation-delay:.25s}.r3{animation-delay:.5s}
@keyframes cloud{50%{transform:translateY(-.9px)}}
@keyframes r{0%,60%,100%{opacity:1}30%{opacity:.4}}
"""),

    # Buero & Finanzen: briefcase gives a little wiggle
    "buero": ("#EA580C", """
<g class="case">
<path d="M3 7m0 2a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v9a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2z"/>
<path d="M8 7v-2a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v2"/>
<path d="M12 12l0 .01"/>
<path d="M3 13a20 20 0 0 0 18 0"/>
</g>
""", """
.case{transform-box:fill-box;transform-origin:50% 0%;animation:case 6s ease-in-out infinite}
@keyframes case{0%,72%,100%{transform:rotate(0)}77%{transform:rotate(-5deg)}83%{transform:rotate(4deg)}89%{transform:rotate(-2deg)}94%{transform:rotate(0)}}
"""),

    # Monitoring & Dashboards: heartbeat line keeps drawing itself
    "monitoring": ("#7C3AED", """
<path d="M3 12h4l3 8l4 -16l3 8h4" stroke-opacity=".5"/>
<path class="line" d="M3 12h4l3 8l4 -16l3 8h4" pathLength="100"/>
""", """
.line{stroke-dasharray:100 100;stroke-dashoffset:100;animation:line 3.6s ease-in-out infinite}
@keyframes line{0%{stroke-dashoffset:100}50%{stroke-dashoffset:0}100%{stroke-dashoffset:-100}}
"""),

    # Bunk Media: camera with a soft, short flash
    "bunk-media": ("#18181B", """
<path d="M5 7h1a2 2 0 0 0 2 -2a1 1 0 0 1 1 -1h6a1 1 0 0 1 1 1a2 2 0 0 0 2 2h1a2 2 0 0 1 2 2v9a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-9a2 2 0 0 1 2 -2"/>
<path d="M9 13a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"/>
<circle class="f ns glint" cx="12" cy="13" r="1.4"/>
<path class="f spark" d="M19.4 1.6l.45 1.25l1.25 .45l-1.25 .45l-.45 1.25l-.45 -1.25l-1.25 -.45l1.25 -.45z" stroke="#fff" stroke-width=".5"/>
""", """
.flash{animation:flash 6s ease-out infinite}
.glint{animation:glint 6s ease-out infinite}
.spark{transform-box:fill-box;transform-origin:center;animation:spark 6s ease-out infinite}
@keyframes flash{0%,84%,100%{opacity:0}87%{opacity:.13}}
@keyframes glint{0%,84%,100%{opacity:.15}87%{opacity:.9}}
@keyframes spark{0%,83%,100%{opacity:0;transform:scale(.4)}87%{opacity:1;transform:scale(1.1)}95%{opacity:0;transform:scale(.8)}}
""", '<rect class="flash" width="128" height="128" rx="30" fill="#fff" opacity="0"/>\n'),

    # Weitara: Lumi the firefly, glowing belly and a short wing flutter
    "weitara": ("#1F6B45", """
<g class="bug">
<g fill="#fff" fill-opacity=".26" stroke-width="1.4">
<g class="wing wl"><ellipse cx="7.2" cy="11.6" rx="3.7" ry="1.9" transform="rotate(28 7.2 11.6)"/></g>
<g class="wing wr"><ellipse cx="16.8" cy="11.6" rx="3.7" ry="1.9" transform="rotate(-28 16.8 11.6)"/></g>
<g class="wing wl"><ellipse cx="8.1" cy="16.7" rx="2.5" ry="1.3" transform="rotate(-28 8.1 16.7)"/></g>
<g class="wing wr"><ellipse cx="15.9" cy="16.7" rx="2.5" ry="1.3" transform="rotate(28 15.9 16.7)"/></g>
</g>
<circle class="halo ns" cx="12" cy="16.7" r="5.4" fill="#FDE047"/>
<circle class="belly" cx="12" cy="16.7" r="3.6" fill="#FDE68A"/>
<path d="M10.6 5.7c-.4 -1.3 -1.1 -2.2 -2.1 -2.8M13.4 5.7c.4 -1.3 1.1 -2.2 2.1 -2.8"/>
<circle class="f ns" cx="8.3" cy="2.8" r=".9"/>
<circle class="f ns" cx="15.7" cy="2.8" r=".9"/>
<circle cx="12" cy="8.7" r="3.3"/>
<circle class="f ns" cx="10.75" cy="8.5" r=".6"/>
<circle class="f ns" cx="13.25" cy="8.5" r=".6"/>
<path d="M11.1 10.1q.9 .7 1.8 0" stroke-width=".9"/>
</g>
""", """
.bug{animation:bug 4.4s ease-in-out infinite}
.halo{transform-box:fill-box;transform-origin:center;animation:halo 2.8s ease-in-out infinite}
.belly{animation:belly 2.8s ease-in-out infinite}
.wing{transform-box:fill-box;animation:wing 4.4s ease-in-out infinite}
.wl{transform-origin:100% 50%}.wr{transform-origin:0% 50%}
@keyframes bug{50%{transform:translateY(-.6px)}}
@keyframes halo{0%,100%{transform:scale(.85);opacity:.12}50%{transform:scale(1.08);opacity:.42}}
@keyframes belly{0%,100%{fill:#FDE68A}50%{fill:#FEF3C7}}
@keyframes wing{0%,60%,72%,84%,100%{transform:scaleY(1)}66%,78%{transform:scaleY(.7)}}
"""),

    # Smart Home & Kameras: house with a pulsing wifi signal
    "smart-home": ("#65A30D", """
<path d="M19 8.71l-5.333 -4.148a2.666 2.666 0 0 0 -3.274 0l-5.334 4.148a2.665 2.665 0 0 0 -1.029 2.105v7.2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-7.2c0 -.823 -.38 -1.6 -1.03 -2.105"/>
<circle class="f ns" cx="12" cy="16.4" r=".95"/>
<path class="w w1" d="M10.16 14.56a2.6 2.6 0 0 1 3.68 0"/>
<path class="w w2" d="M8.46 12.86a5 5 0 0 1 7.08 0"/>
""", """
.w{animation:w 2.6s ease-in-out infinite}.w2{animation-delay:.35s}
@keyframes w{0%,100%{opacity:.25}35%,60%{opacity:1}}
"""),

    # Gaming: gamepad rocks gently, buttons blink
    "gaming": ("#C026D3", """
<g class="pad">
<path d="M12 5h3.5a5 5 0 0 1 0 10h-5.5l-4.015 4.227a2.3 2.3 0 0 1 -3.923 -2.035l1.634 -8.173a5 5 0 0 1 4.904 -4.019h3.4z"/>
<path d="M14 15l4.07 4.284a2.3 2.3 0 0 0 3.925 -2.023l-1.6 -8.232"/>
<path d="M8 9v2M7 10h2"/>
<circle class="f ns btn b1" cx="15.1" cy="9.2" r=".8"/>
<circle class="f ns btn b2" cx="16.9" cy="11" r=".8"/>
</g>
""", """
.pad{transform-box:fill-box;transform-origin:center;animation:pad 4.5s ease-in-out infinite}
.btn{animation:btn 1.8s steps(1) infinite}.b2{animation-delay:-.9s}
@keyframes pad{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
@keyframes btn{0%{opacity:1}50%{opacity:.3}}
"""),

    # Backup: server units with blinking LEDs, the sync badge turns once and pauses
    "backup": ("#0D9488", """
<path d="M5.5 3h11a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1 -2.5 2.5h-11a2.5 2.5 0 0 1 -2.5 -2.5v-2a2.5 2.5 0 0 1 2.5 -2.5z"/>
<path d="M12.5 19h-7a2.5 2.5 0 0 1 -2.5 -2.5v-2a2.5 2.5 0 0 1 2.5 -2.5h11a2.5 2.5 0 0 1 2.4 1.8"/>
<circle class="f ns led l1" cx="6.5" cy="6.5" r=".9"/>
<circle class="f ns led l2" cx="6.5" cy="15.5" r=".9"/>
<path d="M10 6.5h5.5" stroke-opacity=".55"/>
<g transform="translate(18 18) scale(.45) translate(-12 -12)" stroke-width="3.6">
<g class="sync">
<path d="M20 11a8.1 8.1 0 0 0 -15.5 -2m-.5 -4v4h4"/>
<path d="M4 13a8.1 8.1 0 0 0 15.5 2m.5 4v-4h-4"/>
</g>
</g>
""", """
.led{animation:led 2.8s ease-in-out infinite}
.l2{animation-duration:2.1s;animation-delay:-.9s}
.sync{transform-box:fill-box;transform-origin:center;animation:sync 5s ease-in-out infinite}
@keyframes led{0%,22%,48%,100%{opacity:1}10%,60%{opacity:.25}}
@keyframes sync{0%{transform:rotate(0)}40%,100%{transform:rotate(360deg)}}
"""),
}


# Static app icons for containers that have no usable logo anywhere.
# Unraid caches container icons as PNG, so render these with render_apps.sh.
APPS = {
    # parse-dmarc: envelope with a small shield badge
    "parse-dmarc": ("#2563EB", """
<path d="M11 19h-6a2 2 0 0 1 -2 -2v-10a2 2 0 0 1 2 -2h14a2 2 0 0 1 2 2v5"/>
<path d="M3 7l9 6l9 -6"/>
<path d="M17.5 12.6c1.2 1 2.6 1.5 4 1.5c.2 3.3 -1.3 5.9 -4 7c-2.7 -1.1 -4.2 -3.7 -4 -7c1.4 0 2.8 -.5 4 -1.5z" stroke-width="1.5"/>
<path d="M15.9 17.1l1.1 1.1l2.1 -2.1" stroke-width="1.4"/>
"""),

    # nas-backup: two server units with a circular-arrow badge (ntfy/Kuma backup alerts)
    "nas-backup": ("#0D9488", """
<path d="M5.5 3h11a2.5 2.5 0 0 1 2.5 2.5v2a2.5 2.5 0 0 1 -2.5 2.5h-11a2.5 2.5 0 0 1 -2.5 -2.5v-2a2.5 2.5 0 0 1 2.5 -2.5z"/>
<path d="M12.5 19h-7a2.5 2.5 0 0 1 -2.5 -2.5v-2a2.5 2.5 0 0 1 2.5 -2.5h11a2.5 2.5 0 0 1 2.4 1.8"/>
<circle class="f ns" cx="6.5" cy="6.5" r=".9"/>
<circle class="f ns" cx="6.5" cy="15.5" r=".9"/>
<path d="M10 6.5h5.5" stroke-opacity=".55"/>
<g transform="translate(18 18) scale(.45) translate(-12 -12)" stroke-width="3.6">
<path d="M20 11a8.1 8.1 0 0 0 -15.5 -2m-.5 -4v4h4"/>
<path d="M4 13a8.1 8.1 0 0 0 15.5 2m.5 4v-4h-4"/>
</g>
"""),
}


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name, (color, body, css, *rest) in ICONS.items():
        overlay = rest[0] if rest else ""
        (OUT / f"{name}.svg").write_text(svg(color, body, css, overlay), encoding="utf-8")
    apps = Path(__file__).parent / "apps"
    apps.mkdir(exist_ok=True)
    for name, (color, body) in APPS.items():
        (apps / f"{name}.svg").write_text(svg(color, body), encoding="utf-8")
    print(f"{len(ICONS)} folder icons and {len(APPS)} app icons written")


if __name__ == "__main__":
    main()
