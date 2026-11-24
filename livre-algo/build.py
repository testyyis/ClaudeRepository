# -*- coding: utf-8 -*-
"""Génère « Algo'Aventures » : livre d'algorithmique illustré pour collégiens (HTML -> PDF)."""
import base64, html, math, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
FS = os.path.join(HERE, "node_modules", "@fontsource")


def font_face(family, folder, weight):
    p = os.path.join(FS, folder, "files", f"{folder}-latin-{weight}-normal.woff2")
    data = base64.b64encode(open(p, "rb").read()).decode()
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:normal;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');}}\n")


FONTS = "".join(font_face("Fredoka", "fredoka", w) for w in (400, 500, 600, 700))
FONTS += "".join(font_face("Nunito", "nunito", w) for w in (400, 600, 700, 800, 900))
FONTS += "".join(font_face("JetBrains Mono", "jetbrains-mono", w) for w in (400, 700))

INK = "#1e1b4b"
esc = html.escape

# ------------------------------------------------------------------ illustrations

def robot(main="#3B82F6", accent="#FACC15", pose="wave", mood="happy", w=110, flip=False):
    out = INK
    arm_l = f'<path d="M34 96 Q18 104 14 118" stroke="{out}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="14" cy="120" r="7" fill="{accent}" stroke="{out}" stroke-width="3"/>'
    if pose == "wave":
        arm_r = f'<path d="M86 94 Q104 84 106 64" stroke="{out}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="106" cy="60" r="7" fill="{accent}" stroke="{out}" stroke-width="3"/>'
    elif pose == "point":
        arm_r = f'<path d="M86 96 Q104 96 116 88" stroke="{out}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="117" cy="87" r="7" fill="{accent}" stroke="{out}" stroke-width="3"/>'
    elif pose == "think":
        arm_r = f'<path d="M86 98 Q96 92 84 74" stroke="{out}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="83" cy="72" r="7" fill="{accent}" stroke="{out}" stroke-width="3"/>'
    else:  # cheer
        arm_r = f'<path d="M86 94 Q104 84 106 64" stroke="{out}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="106" cy="60" r="7" fill="{accent}" stroke="{out}" stroke-width="3"/>'
        arm_l = f'<path d="M34 94 Q16 84 14 64" stroke="{out}" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="14" cy="60" r="7" fill="{accent}" stroke="{out}" stroke-width="3"/>'
    if mood == "happy":
        mouth = f'<path d="M50 58 Q60 67 70 58" stroke="{out}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    elif mood == "wow":
        mouth = f'<ellipse cx="60" cy="61" rx="5" ry="6" fill="{out}"/>'
    else:
        mouth = f'<path d="M52 61 L68 59" stroke="{out}" stroke-width="3.5" stroke-linecap="round"/>'
    eyes = "".join(f'<circle cx="{x}" cy="45" r="7" fill="{out}"/><circle cx="{x+2.5}" cy="42.5" r="2.4" fill="#fff"/>' for x in (47, 73))
    tr = ' transform="translate(120,0) scale(-1,1)"' if flip else ""
    return f'''<svg viewBox="-4 -2 128 154" width="{w}" xmlns="http://www.w3.org/2000/svg"><g{tr}>
<line x1="60" y1="22" x2="60" y2="9" stroke="{out}" stroke-width="4"/><circle cx="60" cy="7" r="6" fill="{accent}" stroke="{out}" stroke-width="3"/>
<rect x="11" y="38" width="10" height="20" rx="4" fill="{accent}" stroke="{out}" stroke-width="3"/>
<rect x="99" y="38" width="10" height="20" rx="4" fill="{accent}" stroke="{out}" stroke-width="3"/>
{arm_l}{arm_r}
<rect x="30" y="80" width="60" height="46" rx="14" fill="{main}" stroke="{out}" stroke-width="4"/>
<circle cx="60" cy="102" r="10" fill="{accent}" stroke="{out}" stroke-width="3"/>
<path d="M56 100 a3 3 0 0 1 4 -2 a3 3 0 0 1 4 2 q0 3 -4 6 q-4 -3 -4 -6z" fill="#ef4444"/>
<rect x="38" y="126" width="16" height="14" rx="5" fill="{out}"/><rect x="66" y="126" width="16" height="14" rx="5" fill="{out}"/>
<rect x="18" y="20" width="84" height="60" rx="20" fill="{main}" stroke="{out}" stroke-width="4"/>
<rect x="27" y="29" width="66" height="42" rx="14" fill="#F0F9FF" stroke="{out}" stroke-width="3"/>
{eyes}<circle cx="37" cy="58" r="4" fill="#fda4af"/><circle cx="83" cy="58" r="4" fill="#fda4af"/>{mouth}
</g></svg>'''


def bitou(**k):
    return robot("#3B82F6", "#FACC15", **k)


def nova(**k):
    return robot("#F97316", "#A7F3D0", **k)


def drone(w=90, col="#6366F1"):
    rot = "".join(f'<ellipse cx="{x}" cy="{y}" rx="18" ry="5" fill="#cbd5e1" stroke="{INK}" stroke-width="2.5"/>'
                  f'<line x1="{x}" y1="{y}" x2="{60 + (x-60)*0.4}" y2="{40}" stroke="{INK}" stroke-width="4"/>' for x, y in ((20, 18), (100, 18)))
    return f'''<svg viewBox="0 0 120 80" width="{w}"><line x1="20" y1="18" x2="100" y2="18" stroke="{INK}" stroke-width="5"/>{rot}
<rect x="38" y="30" width="44" height="22" rx="10" fill="{col}" stroke="{INK}" stroke-width="3"/>
<circle cx="60" cy="41" r="6" fill="#F0F9FF" stroke="{INK}" stroke-width="2"/><circle cx="60" cy="41" r="2.5" fill="{INK}"/>
<line x1="60" y1="52" x2="60" y2="60" stroke="{INK}" stroke-width="2.5"/>
<rect x="49" y="60" width="22" height="16" rx="3" fill="#D97706" stroke="{INK}" stroke-width="2.5"/><line x1="60" y1="60" x2="60" y2="76" stroke="#92400e" stroke-width="2"/></svg>'''


def rocket(w=80):
    return f'''<svg viewBox="0 0 80 140" width="{w}">
<path d="M40 4 C62 26 64 64 58 100 L22 100 C16 64 18 26 40 4Z" fill="#F8FAFC" stroke="{INK}" stroke-width="4"/>
<path d="M40 4 C50 14 55 24 57 34 L23 34 C25 24 30 14 40 4Z" fill="#EF4444" stroke="{INK}" stroke-width="4"/>
<circle cx="40" cy="56" r="10" fill="#7DD3FC" stroke="{INK}" stroke-width="4"/>
<path d="M22 78 L6 104 L22 100Z M58 78 L74 104 L58 100Z" fill="#EF4444" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
<path d="M28 102 Q40 140 52 102Z" fill="#FACC15" stroke="#F97316" stroke-width="3"/></svg>'''


def football(w=60):
    return f'''<svg viewBox="0 0 60 60" width="{w}"><circle cx="30" cy="30" r="27" fill="#fff" stroke="{INK}" stroke-width="3.5"/>
<path d="M30 19 L40 26 L36 38 L24 38 L20 26Z" fill="{INK}"/>
<path d="M30 19 L30 4 M40 26 L54 21 M36 38 L45 51 M24 38 L15 51 M20 26 L6 21" stroke="{INK}" stroke-width="2.5"/>
<path d="M22 4.5 L30 4 L38 4.5 L34 0Z M55 28 L54 21 L57 30Z" fill="{INK}"/></svg>'''


def turtle_path(steps, size=60, pad=8):
    x = y = 0.0; ang = 0.0; pts = [(0.0, 0.0)]
    for kind, v in steps:
        if kind == "f":
            x += v * math.cos(math.radians(ang)); y -= v * math.sin(math.radians(ang)); pts.append((x, y))
        else:
            ang += v
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    mnx, mny, w, h = min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)
    s = (size - 2 * pad) / max(w, h, 1)
    ox = (size - w * s) / 2 - mnx * s; oy = (size - h * s) / 2 - mny * s
    d = "M" + " L".join(f"{p[0]*s+ox:.1f} {p[1]*s+oy:.1f}" for p in pts)
    return d, (pts[0][0] * s + ox, pts[0][1] * s + oy)


def shape_svg(n, turn, color, w=120):
    d, (sx, sy) = turtle_path([x for _ in range(n) for x in (("f", 100), ("t", turn))], 100)
    dots = ''
    return (f'<svg viewBox="0 0 100 100" width="{w}"><rect width="100" height="100" rx="14" fill="#1e1b4b"/>{dots}'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3.5" stroke-linejoin="round" stroke-dasharray="0.1 6" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-opacity=".35" stroke-width="1.5"/>'
            f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4" fill="#fff"/></svg>')


def scooter(w=150):
    return f'''<svg viewBox="0 0 160 110" width="{w}">
<circle cx="30" cy="88" r="16" fill="#334155" stroke="{INK}" stroke-width="4"/><circle cx="30" cy="88" r="6" fill="#cbd5e1"/>
<circle cx="130" cy="88" r="16" fill="#334155" stroke="{INK}" stroke-width="4"/><circle cx="130" cy="88" r="6" fill="#cbd5e1"/>
<path d="M30 88 L46 80 L118 80 L130 88" fill="none" stroke="{INK}" stroke-width="5"/>
<rect x="44" y="72" width="76" height="12" rx="5" fill="#10B981" stroke="{INK}" stroke-width="3.5"/>
<path d="M118 78 L108 14" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
<path d="M96 14 L122 12" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>
<rect x="56" y="58" width="44" height="14" rx="4" fill="#fff" stroke="{INK}" stroke-width="3"/>
<rect x="59" y="61" width="26" height="8" rx="2" fill="#22c55e"/><rect x="100" y="62" width="4" height="6" fill="{INK}"/>
<path d="M66 50 l6 -10 l-2 7 l6 0 l-6 10 l2 -7z" fill="#FACC15" stroke="{INK}" stroke-width="1.5"/></svg>'''


def moon_scene(w=260):
    craters = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#94a3b8" opacity=".6"/>' for x, y, r in ((40, 120, 8), (120, 128, 5), (200, 118, 10), (230, 134, 4)))
    stars = "".join(f'<circle cx="{(i*53)%260}" cy="{(i*37)%80+4}" r="{1+(i%3)*0.6}" fill="#fff"/>' for i in range(22))
    return f'''<svg viewBox="0 0 260 150" width="{w}"><rect width="260" height="150" rx="16" fill="#0f172a"/>{stars}
<circle cx="215" cy="38" r="22" fill="#3b82f6"/><path d="M200 30 q8 -6 14 2 q6 8 14 2 M206 48 q6 -4 12 2" stroke="#22c55e" stroke-width="5" fill="none"/>
<path d="M0 110 Q60 96 130 108 T260 104 L260 150 L0 150Z" fill="#cbd5e1"/>{craters}
<g transform="translate(70,78)"><rect x="0" y="10" width="54" height="20" rx="6" fill="#F97316" stroke="{INK}" stroke-width="3"/>
<rect x="8" y="0" width="22" height="12" rx="3" fill="#FACC15" stroke="{INK}" stroke-width="2.5"/>
<line x1="40" y1="10" x2="46" y2="-8" stroke="{INK}" stroke-width="3"/><circle cx="46" cy="-10" r="4" fill="#A7F3D0" stroke="{INK}" stroke-width="2"/>
<circle cx="10" cy="34" r="7" fill="#334155" stroke="{INK}" stroke-width="2.5"/><circle cx="27" cy="34" r="7" fill="#334155" stroke="{INK}" stroke-width="2.5"/><circle cx="44" cy="34" r="7" fill="#334155" stroke="{INK}" stroke-width="2.5"/></g>
</svg>'''


def bins_svg():
    data = [("#16a34a", "VERRE"), ("#eab308", "EMBALLAGES"), ("#92400e", "BIODÉCHETS"), ("#6b7280", "ORDURES")]
    g = ""
    for i, (c, t) in enumerate(data):
        x = 6 + i * 92
        g += (f'<g transform="translate({x},0)"><rect x="6" y="14" width="70" height="10" rx="3" fill="{c}" stroke="{INK}" stroke-width="3"/>'
              f'<path d="M10 24 L72 24 L66 96 L16 96Z" fill="{c}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'
              f'<rect x="31" y="8" width="20" height="7" rx="3" fill="{INK}"/>'
              f'<text x="41" y="62" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="{8 if len(t)>7 else 10.5}" fill="#fff">{t}</text>'
              f'<circle cx="24" cy="102" r="5" fill="{INK}"/><circle cx="58" cy="102" r="5" fill="{INK}"/></g>')
    return f'<svg viewBox="0 0 376 110" width="62%" style="display:block;margin:0 auto">{g}</svg>'


def thermo_svg(w=90):
    levels = [("#22c55e", "<30"), ("#facc15", "30"), ("#f97316", "35"), ("#ef4444", "40")]
    seg = "".join(f'<rect x="26" y="{126-i*28}" width="18" height="28" fill="{c}"/><text x="52" y="{126-i*28+18}" font-family="Fredoka" font-size="12" fill="{INK}">{t}°</text>' for i, (c, t) in enumerate(levels))
    return f'''<svg viewBox="0 0 90 180" width="{w}">{seg}<rect x="24" y="12" width="22" height="144" rx="11" fill="none" stroke="{INK}" stroke-width="4"/>
<circle cx="35" cy="160" r="16" fill="#ef4444" stroke="{INK}" stroke-width="4"/><rect x="26" y="12" width="18" height="30" fill="#fff"/><rect x="24" y="12" width="22" height="144" rx="11" fill="none" stroke="{INK}" stroke-width="4"/></svg>'''


def sun(w=70):
    rays = "".join(f'<line x1="{35+20*math.cos(a)}" y1="{35+20*math.sin(a)}" x2="{35+31*math.cos(a)}" y2="{35+31*math.sin(a)}" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>' for a in [i*math.pi/4 for i in range(8)])
    return f'<svg viewBox="0 0 70 70" width="{w}">{rays}<circle cx="35" cy="35" r="16" fill="#fde047" stroke="#f59e0b" stroke-width="4"/><circle cx="30" cy="33" r="2" fill="{INK}"/><circle cx="40" cy="33" r="2" fill="{INK}"/><path d="M29 39 q6 5 12 0" stroke="{INK}" stroke-width="2" fill="none"/></svg>'


def phone_playlist(titles, w=200, hl=None):
    rows = ""
    for i, t in enumerate(titles):
        y = 62 + i * 30
        bg = "#fce7f3" if hl == i else "#fff"
        rows += (f'<rect x="16" y="{y}" width="148" height="25" rx="7" fill="{bg}" stroke="#f9a8d4" stroke-width="1.5"/>'
                 f'<rect x="21" y="{y+4}" width="17" height="17" rx="4" fill="#EC4899"/><text x="29.5" y="{y+17}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="11" fill="#fff">{i+1}</text>'
                 f'<text x="44" y="{y+17}" font-family="Nunito" font-weight="700" font-size="11" fill="{INK}">{esc(t)}</text>')
    h = 62 + len(titles) * 30 + 40
    return f'''<svg viewBox="0 0 180 {h}" width="{w}"><rect x="4" y="4" width="172" height="{h-8}" rx="22" fill="{INK}"/>
<rect x="10" y="16" width="160" height="{h-30}" rx="14" fill="#fdf2f8"/><rect x="70" y="8" width="40" height="5" rx="2.5" fill="#475569"/>
<text x="90" y="42" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="14" fill="#BE185D">♫ Ma playlist</text>{rows}
<g transform="translate(90,{h-30})"><circle r="11" fill="#EC4899"/><path d="M-3 -6 L6 0 L-3 6Z" fill="#fff"/></g></svg>'''


def temp_bars(vals, days, w="100%"):
    mx = 45; g = ""
    for i, (v, d) in enumerate(zip(vals, days)):
        h = v / mx * 120; x = 18 + i * 52
        c = "#ef4444" if v >= 40 else "#f97316" if v >= 35 else "#facc15" if v >= 30 else "#22c55e"
        g += (f'<rect x="{x}" y="{140-h}" width="34" height="{h}" rx="6" fill="{c}" stroke="{INK}" stroke-width="2.5"/>'
              f'<text x="{x+17}" y="{134-h}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="13" fill="{INK}">{v}°</text>'
              f'<text x="{x+17}" y="158" text-anchor="middle" font-family="Nunito" font-weight="700" font-size="11" fill="#475569">{d}</text>')
    return f'<svg viewBox="0 0 380 165" width="{w}"><line x1="10" y1="140" x2="372" y2="140" stroke="{INK}" stroke-width="2.5"/>{g}</svg>'


def bars_row(vals, hi=(), done=0, w=260, label=None):
    g = ""
    for i, v in enumerate(vals):
        x = 8 + i * 48; h = v * 9
        c = "#a78bfa" if i >= done else "#22c55e"
        if i in hi:
            c = "#facc15"
        g += (f'<rect x="{x}" y="{92-h}" width="38" height="{h}" rx="6" fill="{c}" stroke="{INK}" stroke-width="2.5"/>'
              f'<text x="{x+19}" y="{88-h}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="15" fill="{INK}">{v}</text>')
    return f'<svg viewBox="0 -14 250 112" width="{w}">{g}</svg>'


def caesar(s, k):
    return "".join(chr((ord(c) - 65 + k) % 26 + 65) if "A" <= c <= "Z" else c for c in s)


def caesar_wheel(k=3, w=230):
    g = ""
    for i in range(26):
        a = math.radians(i * 360 / 26 - 90)
        L = chr(65 + i); C = chr(65 + (i + k) % 26)
        for r, ch, col, fs in ((92, L, INK, 13), (64, C, "#F8FAFC", 12)):
            g += f'<text x="{100+r*math.cos(a):.1f}" y="{100+r*math.sin(a)+4.5:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="{fs}" fill="{col}">{ch}</text>'
        g += f'<line x1="{100+78*math.cos(a+math.pi/26):.1f}" y1="{100+78*math.sin(a+math.pi/26):.1f}" x2="{100+104*math.cos(a+math.pi/26):.1f}" y2="{100+104*math.sin(a+math.pi/26):.1f}" stroke="#94a3b8" stroke-width="1"/>'
    return f'''<svg viewBox="-8 -8 216 216" width="{w}"><circle cx="100" cy="100" r="104" fill="#e2e8f0" stroke="{INK}" stroke-width="4"/>
<circle cx="100" cy="100" r="78" fill="#334155" stroke="{INK}" stroke-width="3"/>{g}<circle cx="100" cy="100" r="44" fill="#FACC15" stroke="{INK}" stroke-width="3"/>
<text x="100" y="96" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="14" fill="{INK}">CLÉ</text>
<text x="100" y="118" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="22" fill="{INK}">+{k}</text>
<path d="M100 -6 L94 -16 L106 -16Z" fill="#ef4444"/></svg>'''


def padlock(w=80, col="#334155"):
    return f'''<svg viewBox="0 0 80 100" width="{w}"><path d="M20 44 V28 a20 20 0 0 1 40 0 V44" fill="none" stroke="{INK}" stroke-width="8"/>
<rect x="8" y="42" width="64" height="52" rx="10" fill="{col}" stroke="{INK}" stroke-width="4"/>
<circle cx="40" cy="62" r="7" fill="#FACC15"/><rect x="37" y="64" width="6" height="16" rx="2" fill="#FACC15"/></svg>'''


def chest(w=160):
    return f'''<svg viewBox="0 0 160 130" width="{w}">
<path d="M14 54 Q80 6 146 54Z" fill="#b45309" stroke="{INK}" stroke-width="4"/>
<rect x="14" y="54" width="132" height="66" rx="6" fill="#d97706" stroke="{INK}" stroke-width="4"/>
<rect x="14" y="54" width="132" height="12" fill="#92400e" stroke="{INK}" stroke-width="3"/>
<rect x="32" y="54" width="12" height="66" fill="#fbbf24" stroke="{INK}" stroke-width="2.5"/><rect x="116" y="54" width="12" height="66" fill="#fbbf24" stroke="{INK}" stroke-width="2.5"/>
<rect x="60" y="70" width="40" height="34" rx="5" fill="#fde047" stroke="{INK}" stroke-width="3"/>
{"".join(f'<rect x="{64+i*8.5}" y="80" width="7" height="12" rx="1.5" fill="#fff" stroke="{INK}" stroke-width="1.5"/><text x="{67.5+i*8.5}" y="90" text-anchor="middle" font-family="Fredoka" font-size="9" font-weight="700" fill="{INK}">?</text>' for i in range(4))}
<path d="M40 30 l3 -8 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3z M120 22 l2 -6 l2 6 l6 2 l-6 2 l-2 6 l-2 -6 l-6 -2z" fill="#fde047"/></svg>'''


def medal(w=120):
    return f'''<svg viewBox="0 0 120 150" width="{w}"><path d="M30 0 L52 60 L68 60 L46 0Z" fill="#3B82F6" stroke="{INK}" stroke-width="3"/><path d="M90 0 L68 60 L52 60 L74 0Z" fill="#F97316" stroke="{INK}" stroke-width="3"/>
<circle cx="60" cy="96" r="42" fill="#FACC15" stroke="{INK}" stroke-width="4"/><circle cx="60" cy="96" r="31" fill="#FDE047" stroke="#CA8A04" stroke-width="3"/>
<path d="M60 74 l7 14 l15 2 l-11 10 l3 15 l-14 -7 l-14 7 l3 -15 l-11 -10 l15 -2z" fill="#F59E0B" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/></svg>'''


def graph_svg(nodes, edges, w="100%", vb="0 0 400 230", node_col="#0891B2", r=24, weights=True, hl_edges=(), fs=12, labels_full=None):
    g = ""
    for a, b, *wt in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        hot = (a, b) in hl_edges or (b, a) in hl_edges
        g += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{"#f59e0b" if hot else "#94a3b8"}" stroke-width="{7 if hot else 4}" stroke-linecap="round"/>'
        if weights and wt:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            g += (f'<rect x="{mx-15}" y="{my-11}" width="30" height="22" rx="11" fill="#fff" stroke="{INK}" stroke-width="2"/>'
                  f'<text x="{mx}" y="{my+5}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="12.5" fill="{INK}">{wt[0]} min</text>' if False else
                  f'<rect x="{mx-13}" y="{my-11}" width="26" height="22" rx="11" fill="#fff" stroke="{INK}" stroke-width="2"/>'
                  f'<text x="{mx}" y="{my+5}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="13" fill="{INK}">{wt[0]}</text>')
    for k, (x, y) in nodes.items():
        col = node_col(k) if callable(node_col) else node_col
        g += (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="{INK}" stroke-width="3"/>'
              f'<text x="{x}" y="{y+fs*0.36}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="{fs}" fill="#fff">{k}</text>')
        if labels_full:
            g += f'<text x="{x}" y="{y+r+15}" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="11.5" fill="{INK}">{labels_full[k]}</text>'
    return f'<svg viewBox="{vb}" width="{w}">{g}</svg>'


def drone_grid():
    obs = {(4, 1), (3, 1), (1, 1), (2, 3), (3, 3), (0, 2), (4, 4), (2, 5), (1, 3)}
    c = 44; ox = 30; oy = 8; g = ""
    for r in range(6):
        g += f'<text x="{ox-14}" y="{oy+r*c+c/2+6}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="16" fill="{INK}">{6-r}</text>'
        for col in range(6):
            x, y = ox + col * c, oy + r * c
            fill = "#e0e7ff" if (r + col) % 2 else "#eef2ff"
            g += f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{fill}" stroke="#a5b4fc" stroke-width="1.5"/>'
            if (r, col) in obs:
                g += (f'<rect x="{x+4}" y="{y+4}" width="{c-8}" height="{c-8}" rx="6" fill="#fecaca" stroke="#ef4444" stroke-width="2.5"/>'
                      f'<circle cx="{x+c/2}" cy="{y+c/2}" r="11" fill="none" stroke="#ef4444" stroke-width="3.5"/><line x1="{x+c/2-8}" y1="{y+c/2+8}" x2="{x+c/2+8}" y2="{y+c/2-8}" stroke="#ef4444" stroke-width="3.5"/>')
    for col in range(6):
        g += f'<text x="{ox+col*c+c/2}" y="{oy+6*c+20}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="16" fill="{INK}">{"ABCDEF"[col]}</text>'
    # start drone (A1) & house (F6)
    sx, sy = ox + 0 * c, oy + 5 * c
    g += f'<g transform="translate({sx+3},{sy+7}) scale(0.32)">{drone_inner()}</g>'
    hx, hy = ox + 5 * c, oy
    g += (f'<path d="M{hx+8} {hy+22} L{hx+22} {hy+8} L{hx+36} {hy+22} V{hy+38} H{hx+8}Z" fill="#fde68a" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>'
          f'<rect x="{hx+18}" y="{hy+27}" width="8" height="11" fill="#b45309"/>')
    g += f'<rect x="{ox}" y="{oy}" width="{6*c}" height="{6*c}" fill="none" stroke="{INK}" stroke-width="3" rx="4"/>'
    return f'<svg viewBox="0 0 310 300" width="100%">{g}</svg>'


def drone_inner():
    s = drone(120)
    return s[s.index(">") + 1: s.rindex("</svg>")]


def video_card(title, tags, color, emoji):
    t = "".join(f'<span class="tag">#{x}</span>' for x in tags)
    return f'<div class="vcard"><div class="vthumb" style="background:{color}"><span>{emoji}</span><i>▶</i></div><b>{title}</b><div>{t}</div></div>'


def flow_sort():
    def box(x, y, w, h, txt, fill, diamond=False):
        if diamond:
            return (f'<path d="M{x+w/2} {y} L{x+w} {y+h/2} L{x+w/2} {y+h} L{x} {y+h/2}Z" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
                    f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="11" fill="{INK}">{txt}</text>')
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
                f'<text x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="11.5" fill="#fff">{txt}</text>')
    g = ""
    qs = ["En verre ?", "Emballage ?", "Reste de repas ?"]
    outs = [("Bac VERT", "#16a34a"), ("Bac JAUNE", "#ca8a04"), ("Bac MARRON", "#92400e")]
    for i, q in enumerate(qs):
        y = 6 + i * 64
        g += box(10, y, 140, 50, q, "#d1fae5", True)
        g += f'<line x1="150" y1="{y+25}" x2="210" y2="{y+25}" stroke="{INK}" stroke-width="2.5" marker-end="url(#ar)"/><text x="166" y="{y+19}" font-family="Fredoka" font-weight="600" font-size="11" fill="#16a34a">OUI</text>'
        g += box(214, y + 8, 110, 34, outs[i][0], outs[i][1])
        g += f'<line x1="80" y1="{y+50}" x2="80" y2="{y+64}" stroke="{INK}" stroke-width="2.5" marker-end="url(#ar)"/><text x="86" y="{y+61}" font-family="Fredoka" font-weight="600" font-size="10" fill="#dc2626">NON</text>'
    g += box(25, 198, 110, 34, "Bac GRIS", "#6b7280")
    return (f'<svg viewBox="0 0 330 236" width="100%"><defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
            f'<path d="M0 0 L8 4 L0 8Z" fill="{INK}"/></marker></defs>{g}</svg>')


def decision_tree():
    def node(x, y, t, fill, w=124, h=40, col=INK):
        return (f'<rect x="{x-w/2}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
                f'<text x="{x}" y="{y+h/2+4.5}" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="12" fill="{col}">{t}</text>')
    def edge(x1, y1, x2, y2, t, c):
        return (f'<path d="M{x1} {y1} C{x1} {(y1+y2)/2} {x2} {(y1+y2)/2} {x2} {y2}" stroke="{INK}" stroke-width="2.5" fill="none"/>'
                f'<text x="{(x1+x2)/2 + (8 if x2 > x1 else -8)}" y="{(y1+y2)/2}" text-anchor="{"start" if x2 > x1 else "end"}" font-family="Fredoka" font-weight="700" font-size="11" fill="{c}">{t}</text>')
    g = node(200, 4, "Expéditeur inconnu ?", "#f5d0fe")
    g += edge(200, 44, 100, 82, "OUI", "#16a34a") + edge(200, 44, 300, 82, "NON", "#dc2626")
    g += node(100, 82, "Lien bizarre ?", "#f5d0fe")
    g += node(300, 82, "✅ Message normal", "#bbf7d0", 140)
    g += edge(100, 122, 50, 162, "OUI", "#16a34a") + edge(100, 122, 160, 162, "NON", "#dc2626")
    g += node(50, 162, "🚫 SPAM", "#fecaca", 92)
    g += node(160, 162, "⚠️ À vérifier", "#fde68a", 110)
    return f'<svg viewBox="0 0 400 206" width="100%">{g}</svg>'


def bracket_svg():
    g = ""; cols = [8, 4, 2, 1]; x0 = 6; colw = 74
    for ci, n in enumerate(cols):
        gap = 200 / n
        for i in range(n):
            y = gap * i + gap / 2
            x = x0 + ci * colw
            col = "#FACC15" if n == 1 else "#fff"
            g += f'<rect x="{x}" y="{y-9}" width="56" height="18" rx="9" fill="{col}" stroke="{INK}" stroke-width="2"/>'
            if n == 1:
                g += f'<text x="{x+28}" y="{y+4.5}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="10" fill="{INK}">CHAMPION</text>'
            if ci < 3:
                ny = (200 / (n // 2)) * (i // 2) + (200 / (n // 2)) / 2
                g += f'<path d="M{x+56} {y} H{x+65} V{ny} H{x+74}" fill="none" stroke="#94a3b8" stroke-width="2"/>'
    labels = ["8 équipes", "Demies", "Finale", ""]
    for ci, l in enumerate(labels):
        g += f'<text x="{x0+ci*colw+28}" y="215" text-anchor="middle" font-family="Nunito" font-weight="800" font-size="10" fill="#475569">{l}</text>'
    return f'<svg viewBox="0 0 290 220" width="100%">{g}</svg>'


# ------------------------------------------------------------------ text helpers

KW = ["Tant que", "Sinon si", "Répéter", "Pour chaque", "Pour", "Si", "Sinon", "Alors", "Fin", "Afficher", "Fonction", "Retourner",
      "faire", "fois", "alors", "de", "à", "dans", "ET", "OU", "NON", "Demander"]


def code(src, title=None):
    lines = []
    for ln in src.strip("\n").split("\n"):
        e = esc(ln, quote=False)
        e = re.sub(r"(#.*)$", r'<span class="cm">\1</span>', e)
        e = re.sub(r'(".*?")', r'<span class="st">\1</span>', e)
        for k in KW:
            e = re.sub(r"(?<![\w>])(" + re.escape(k) + r")(?![\w])", r'<span class="kw">\1</span>', e) if k in ("Tant que", "Sinon si", "Pour chaque", "Répéter", "Afficher", "Fonction", "Retourner", "Demander") else \
                re.sub(r"(?<![\wÀ-ÿ&;>])(" + re.escape(k) + r")(?![\wÀ-ÿ])(?![^<]*</span>)", r'<span class="kw">\1</span>', e)
        e = e.replace("←", '<span class="ar">←</span>')
        lines.append(e if e.strip() else "&nbsp;")
    t = f'<div class="code-title">{title}</div>' if title else ""
    return f'<div class="code">{t}<pre>{"<br>".join(lines)}</pre></div>'


def py(src, title="🐍 Coin Python"):
    e = esc(src.strip("\n"), quote=False)
    e = re.sub(r"(#.*)$", r'<span class="cm">\1</span>', e, flags=re.M)
    e = re.sub(r"\b(for|in|range|while|if|elif|else|def|return|print|and|or|not|import|input|int|len|max|append)\b", r'<span class="kw">\1</span>', e)
    return f'<div class="py"><div class="py-title">{title}</div><pre>{e}</pre></div>'


def box(kind, title, body, extra=""):
    return f'<div class="box {kind}" {extra}><div class="box-t">{title}</div>{body}</div>'


def defi(n, title, stars, body, color):
    st = "★" * stars + '<span class="off">' + "★" * (3 - stars) + "</span>"
    return f'<div class="defi" style="--c:{color}"><div class="defi-h"><span class="defi-n">DÉFI {n}</span><span class="defi-title">{title}</span><span class="stars">{st}</span></div><div class="defi-b">{body}</div></div>'


def ans(label="Ta réponse", lines=1):
    return "".join(f'<div class="ans"><span>{label if i == 0 else ""}</span></div>' for i in range(lines))


def blocks(items):
    """items: list of (cat, text) or (cat, text, [children])"""
    out = ""
    for it in items:
        cat, txt = it[0], it[1]
        if len(it) > 2:
            out += f'<div class="blk c-{cat} cblock"><div class="blk-top">{txt}</div><div class="blk-in">{blocks(it[2])}</div><div class="blk-bot"></div></div>'
        else:
            out += f'<div class="blk c-{cat}">{txt}</div>'
    return out


def scratch(items, title="🧩 Version blocs"):
    return f'<div class="scratch"><div class="scratch-t">{title}</div>{blocks(items)}</div>'


def trace_table(headers, rows, empty_rows=0):
    h = "".join(f"<th>{x}</th>" for x in headers)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    b += "".join("<tr>" + "".join("<td>&nbsp;</td>" for _ in headers) + "</tr>" for _ in range(empty_rows))
    return f'<table class="trace"><tr>{h}</tr>{b}</table>'


# ------------------------------------------------------------------ pages

PAGES = []
CH = {}


def add(body, chapter=None, color="#6366F1", cls="", footer=True):
    PAGES.append(dict(body=body, chapter=chapter, color=color, cls=cls, footer=footer))
    return len(PAGES)


def chap_banner(n, title, sub, color, art):
    return (f'<div class="banner" style="--c:{color}"><div class="banner-txt"><div class="banner-n">CHAPITRE {n}</div>'
            f'<h1>{title}</h1><div class="banner-sub">{sub}</div></div><div class="banner-art">{art}</div></div>')


def bubble(who, text, side="left"):
    art = bitou(w=70, pose="point") if who == "bitou" else nova(w=70, pose="wave", flip=True)
    name = "Bitou" if who == "bitou" else "Nova"
    if side == "left":
        return f'<div class="say"><div class="say-art">{art}</div><div class="say-b left"><b>{name} :</b> {text}</div></div>'
    return f'<div class="say right"><div class="say-b right"><b>{name} :</b> {text}</div><div class="say-art">{art}</div></div>'


C = {1: "#6366F1", 2: "#0EA5E9", 3: "#10B981", 4: "#F59E0B", 5: "#EF4444", 6: "#EC4899", 7: "#8B5CF6",
     8: "#14B8A6", 9: "#F97316", 10: "#0891B2", 11: "#334155", 12: "#C026D3", 13: "#EAB308"}
TITLES = {1: "Un algorithme, c'est quoi ?", 2: "Les variables", 3: "Les conditions", 4: "Les boucles « Répéter »",
          5: "Les boucles « Tant que »", 6: "Les listes", 7: "Trier, c'est gagner", 8: "Chercher plus vite",
          9: "Les fonctions", 10: "Les graphes et les chemins", 11: "Codes secrets", 12: "Dans la tête d'une IA",
          13: "Le grand défi final"}

# ---- 1 COUVERTURE
stars_bg = "".join(f'<circle cx="{(i*97)%600}" cy="{(i*61)%840}" r="{0.8+(i%4)*0.6}" fill="#fff" opacity="{0.3+(i%5)*0.12}"/>' for i in range(90))
cover = f'''
<svg class="cover-bg" viewBox="0 0 600 840" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="cg" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#312e81"/><stop offset=".55" stop-color="#6d28d9"/><stop offset="1" stop-color="#db2777"/></linearGradient></defs>
<rect width="600" height="840" fill="url(#cg)"/>{stars_bg}
<path d="M0 700 Q150 640 300 690 T600 670 L600 840 L0 840Z" fill="#1e1b4b" opacity=".55"/>
<g stroke="#a5b4fc" stroke-width="2" fill="none" opacity=".35"><path d="M20 300 H120 V360 H200"/><circle cx="200" cy="360" r="5"/><path d="M580 260 H480 V320 H430"/><circle cx="430" cy="320" r="5"/><path d="M40 560 H110 V600"/><circle cx="110" cy="600" r="5"/></g>
<circle cx="548" cy="52" r="30" fill="#fde68a" opacity=".9"/><circle cx="540" cy="45" r="6" fill="#fcd34d"/><circle cx="558" cy="62" r="4" fill="#fcd34d"/>
</svg>
<div class="cover">
  <div class="cover-top">COLLÈGE · 11-15 ANS · SCRATCH &amp; PYTHON</div>
  <div class="cover-title">Algo<span>'</span>Aventures</div>
  <div class="cover-sub">27 défis fun pour devenir un as de l'algorithmique</div>
  <div class="cover-chips"><span>⚽ Coupe du monde</span><span>🚀 Mission Lune</span><span>🤖 Intelligence artificielle</span><span>🛸 Drones</span><span>🔐 Codes secrets</span><span>🌡️ Climat</span></div>
  <div class="cover-art">
    <div class="ca-drone">{drone(150, "#22d3ee")}</div>
    <div class="ca-rocket">{rocket(105)}</div>
    <div class="ca-bitou">{bitou(w=270, pose="cheer")}</div>
    <div class="ca-nova">{nova(w=225, pose="wave", flip=True)}</div>
    <div class="ca-ball">{football(70)}</div>
    <div class="ca-code">si&nbsp;défi&nbsp;=&nbsp;réussi&nbsp;alors<br>&nbsp;&nbsp;score&nbsp;←&nbsp;score&nbsp;+&nbsp;1</div>
  </div>
  <div class="cover-bottom"><b>Avec Bitou &amp; Nova</b>, les robots qui adorent les énigmes · Corrigés inclus · Diplôme à la fin</div>
</div>'''
add(cover, cls="cover-page", footer=False)

# ---- 2 PAGE DE TITRE / MENTIONS
add(f'''<div class="titlepage">
<div class="tp-robots">{bitou(w=120, pose="wave")}{nova(w=120, pose="wave", flip=True)}</div>
<h1 class="tp-title">Algo'Aventures</h1>
<div class="tp-sub">27 défis fun pour devenir un as de l'algorithmique</div>
<div class="tp-lvl">Cycle 4 · 6<sup>e</sup> – 5<sup>e</sup> – 4<sup>e</sup> – 3<sup>e</sup></div>
<div class="tp-author">Texte : <span class="ph">[Nom de l'auteur·e]</span><br>Illustrations : <span class="ph">[Nom de l'illustrateur·rice]</span></div>
<div class="legal">
<p><b><span class="ph">[Nom de la maison d'édition]</span></b> — <span class="ph">[Adresse]</span></p>
<p>© <span class="ph">[Année]</span> <span class="ph">[Titulaire des droits]</span>. Tous droits réservés.</p>
<p>ISBN : <span class="ph">[978-X-XXXX-XXXX-X]</span> — Dépôt légal : <span class="ph">[mois année]</span></p>
<p>Le Code de la propriété intellectuelle interdit les copies ou reproductions destinées à une utilisation collective. Toute représentation ou reproduction intégrale ou partielle faite par quelque procédé que ce soit, sans le consentement de l'auteur ou de ses ayants cause, est illicite (art. L.122-4 et suivants du CPI). Les pages d'exercices peuvent être photocopiées pour un usage strictement personnel.</p>
<p>Loi n° 49-956 du 16 juillet 1949 sur les publications destinées à la jeunesse.</p>
<p>Les situations, chiffres « inventés pour l'exercice », noms de chansons, de vidéos et de personnages sont fictifs. Les marques et noms de services ne sont pas cités volontairement : ce livre n'est affilié à aucune entreprise.</p>
<p>Imprimé en <span class="ph">[pays]</span> par <span class="ph">[imprimeur]</span>.</p>
</div></div>''', footer=False)

# ---- 3 SOMMAIRE (rempli après)
SOMMAIRE_IDX = add("__SOMMAIRE__", footer=True, color="#6366F1")

# ---- 4 BIENVENUE
add(f'''<h1 class="ptitle">Bienvenue, futur·e as de l'algo !</h1>
<div class="welcome">
<div class="w-intro">
<p class="lead">Chaque jour, tu utilises des <b>algorithmes</b> sans le savoir : quand ton GPS calcule un trajet, quand une appli te propose une vidéo, quand une IA répond à une question, ou quand un drone livre un colis.</p>
<p>Dans ce livre, tu vas apprendre à <b>penser comme un·e informaticien·ne</b> : découper un problème, donner des instructions précises, répéter, décider, trier, chercher… et même fabriquer des codes secrets !</p>
<p><b>Pas besoin d'ordinateur</b> : un crayon et ta tête suffisent. Mais si tu en as un, les encadrés <b>Scratch</b> et <b>Python</b> te permettront de programmer tes solutions.</p>
</div>
<div class="duo">
 <div class="card-perso"><div>{bitou(w=110, pose="wave")}</div><div><h3 style="color:#3B82F6">Bitou</h3><p>Robot livreur un peu tête en l'air. Il exécute <b>exactement</b> ce qu'on lui dit… même quand c'est une bêtise !</p></div></div>
 <div class="card-perso"><div>{nova(w=110, pose="think")}</div><div><h3 style="color:#F97316">Nova</h3><p>Robot exploratrice, fan d'espace et de foot. Elle cherche toujours la solution <b>la plus rapide</b>.</p></div></div>
</div>
</div>
<h2 class="h2">Comment utiliser ce livre ?</h2>
<div class="legend">
<div><span class="lg" style="background:#e0e7ff">📘</span><b>Je comprends</b><br>La leçon, expliquée simplement avec un exemple.</div>
<div><span class="lg" style="background:#fef3c7">🎯</span><b>Défis</b><br>À toi de jouer ! De ★ (facile) à ★★★ (expert).</div>
<div><span class="lg" style="background:#dcfce7">💡</span><b>Astuce</b><br>Un conseil pour ne pas tomber dans le piège.</div>
<div><span class="lg" style="background:#1e1b4b;color:#fff">🐍</span><b>Coin Python</b><br>Le même algorithme en vrai langage.</div>
<div><span class="lg" style="background:#fce7f3">🧩</span><b>Blocs</b><br>La version façon Scratch, comme en cours de techno et de maths.</div>
<div><span class="lg" style="background:#ede9fe">🧠</span><b>Le savais-tu ?</b><br>Des anecdotes pour briller en classe.</div>
</div>
{box("tip", "💡 Le conseil de Nova", "<p>Ne regarde pas les corrigés trop vite ! Un défi qui résiste, c'est ton cerveau qui fait de la muscu. Les solutions sont à la fin du livre, page <b>__CORR__</b>.</p>")}
''', color="#6366F1")

# ================= CHAPITRE 1
CH[1] = add(f'''{chap_banner(1, TITLES[1], "Des instructions précises pour résoudre un problème", C[1], bitou(w=120, pose="think", mood="wow"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Un <b>algorithme</b>, c'est une <b>suite d'instructions précises</b>, dans un <b>ordre</b> donné, qui permet de résoudre un problème.</p>
<p>Une recette de cuisine, l'itinéraire d'un GPS ou la notice d'un meuble sont des algorithmes ! Un <b>programme</b>, c'est un algorithme écrit dans un langage que l'ordinateur comprend (Scratch, Python…).</p>
{box("warn", "⚠️ Un ordinateur ne devine rien", "<p>Si tu dis à Bitou « fais des crêpes », il ne bouge pas. Il faut tout détailler : prendre un bol, verser 250 g de farine, casser 4 œufs…</p>")}
</div>
<div>
{box("know", "🧠 Le savais-tu ?", "<p>Le mot <b>algorithme</b> vient du nom d'<b>Al-Khwârizmî</b>, un savant qui vivait à Bagdad il y a plus de 1 200 ans. Ses livres ont appris à l'Europe à calculer avec les chiffres que l'on utilise aujourd'hui.</p><p>Et le tout premier programme informatique a été écrit en <b>1843</b> par une femme : <b>Ada Lovelace</b> !</p>")}
<h3 class="h3">Les algorithmes autour de toi</h3>
<ul class="chips"><li>🗺️ Le GPS qui trouve le trajet le plus court</li><li>🎬 L'appli qui te recommande des vidéos</li><li>🤖 Les IA qui répondent à tes questions</li><li>🚦 Les feux tricolores synchronisés</li></ul>
</div></div>
{defi(1, "Le smoothie de l'été", 1, '''<p>Bitou veut préparer un smoothie, mais ses instructions sont dans le désordre ! Numérote-les de 1 à 6 pour obtenir un algorithme qui fonctionne.</p>
<div class="order">
<div><span class="num"></span>Appuyer sur le bouton du mixeur pendant 30 secondes.</div>
<div><span class="num"></span>Éplucher la banane et la couper en morceaux.</div>
<div><span class="num"></span>Verser le smoothie dans un verre.</div>
<div><span class="num"></span>Mettre la banane, les fraises et le lait dans le mixeur.</div>
<div><span class="num"></span>Laver les fraises.</div>
<div><span class="num"></span>Fermer le couvercle du mixeur.</div>
</div><p class="small">🤔 Question bonus : peut-on inverser certaines étapes sans problème ? Lesquelles ?</p>''', C[1])}
''', chapter=1, color=C[1])

add(f'''{defi(2, "Le drone livreur", 2, f"""
<div class="cols2 ac">
<div>{drone_grid()}</div>
<div>
<p>Le drone de Bitou part de la case <b>A1</b> pour livrer un colis à la maison en <b>F6</b>. Les cases rouges sont des <b>zones interdites</b> (hôpital, aéroport…) : s'il y entre, la mission échoue !</p>
<p>Le drone comprend 4 instructions, qui le déplacent d'une case :</p>
<div class="arrows"><span>↑</span> haut <span>↓</span> bas <span>→</span> droite <span>←</span> gauche</div>
</div></div>
<p><b>a)</b> Le drone exécute : <span class="mono big">→ → ↑ ↑ ↑ ↑</span>. Sur quelle case arrive-t-il ?</p>{ans()}
<p><b>b)</b> Nova propose : <span class="mono big">↑ ↑ ↑ ↑ ↑ → → → → →</span>. Que se passe-t-il ? Sur quelle case ?</p>{ans()}
<p><b>c)</b> Écris le programme <b>le plus court</b> pour livrer le colis. Combien d'instructions contient-il ?</p>{ans(lines=2)}
""", C[1])}
<div class="cols2">
{box("tip", "💡 Astuce de pro", "<p>Quand une même instruction se répète, on peut la regrouper : <span class='mono'>→ → → → →</span> s'écrit <b>« Répéter 5 fois → »</b>. Tu en sauras plus au chapitre 4 !</p><p><b>d)</b> Réécris ton programme de la question c) avec des « Répéter ».</p>" + ans())}
{box("know", "🧠 Le savais-tu ?", "<p>Dans plusieurs pays, des drones livrent déjà des médicaments ou des repas. Leur ordinateur de bord calcule un trajet qui évite les <b>zones interdites de survol</b>, comme les aéroports. C'est exactement ce que tu viens de faire !</p>")}
</div>''', chapter=1, color=C[1])

# ================= CHAPITRE 2
CH[2] = add(f'''{chap_banner(2, TITLES[2], "Des boîtes pour garder des informations en mémoire", C[2], nova(w=120, pose="point"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Une <b>variable</b>, c'est comme une <b>boîte avec une étiquette</b>. On range une valeur dedans, et on peut la changer quand on veut.</p>
<svg viewBox="0 0 300 120" width="100%"><g font-family="Fredoka" font-weight="600">
<path d="M20 40 L140 40 L140 110 L20 110Z" fill="#7dd3fc" stroke="{INK}" stroke-width="3.5"/><path d="M20 40 L40 20 L160 20 L140 40Z" fill="#bae6fd" stroke="{INK}" stroke-width="3.5"/><path d="M140 40 L160 20 L160 90 L140 110Z" fill="#38bdf8" stroke="{INK}" stroke-width="3.5"/>
<rect x="34" y="56" width="92" height="24" rx="6" fill="#fff" stroke="{INK}" stroke-width="2.5"/><text x="80" y="73" text-anchor="middle" font-size="14" fill="{INK}">score</text>
<text x="80" y="100" text-anchor="middle" font-size="18" fill="{INK}">120</text>
<text x="230" y="50" text-anchor="middle" font-size="13" fill="#0369a1">le NOM</text><path d="M196 54 L130 66" stroke="#0369a1" stroke-width="2" marker-end="url(#a2)"/>
<text x="230" y="100" text-anchor="middle" font-size="13" fill="#0369a1">la VALEUR</text><path d="M190 96 L102 96" stroke="#0369a1" stroke-width="2" marker-end="url(#a2)"/>
<defs><marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#0369a1"/></marker></defs></g></svg>
<p>La flèche <b>←</b> veut dire « <b>reçoit</b> ». On lit <span class="mono">score ← 120</span> : « score reçoit 120 ».</p>
</div>
<div>
{code("""score ← 120
score ← score + 35
score ← score × 2
Afficher score""", "Exemple : le score d'un jeu vidéo")}
<p>À chaque ligne, on remplace la valeur. Pour suivre un algorithme, on fait un <b>tableau de suivi</b> :</p>
{trace_table(["Ligne", "score"], [["1", "120"], ["2", "120 + 35 = 155"], ["3", "155 × 2 = 310"], ["4", "affiche <b>310</b>"]])}
</div></div>
{box("warn", "⚠️ Piège classique", "<p><span class='mono'>score ← score + 35</span> n'est pas une équation de maths ! On calcule d'abord la partie droite avec l'<b>ancienne</b> valeur, puis on range le résultat dans la boîte.</p>")}
<div class="cols2">
{scratch([("var", "mettre <i>score</i> à <u>120</u>"), ("var", "ajouter <u>35</u> à <i>score</i>"), ("var", "mettre <i>score</i> à <i>score</i> × <u>2</u>"), ("look", "dire <i>score</i>")])}
{py("""score = 120
score = score + 35
score = score * 2
print(score)   # affiche 310""")}
</div>''', chapter=2, color=C[2])

add(f'''{defi(3, "La cagnotte du voyage de classe", 1, f"""
<div class="cols2"><div>
<p>La classe de 4<sup>e</sup>B organise des actions pour financer un voyage. Le trésorier a écrit cet algorithme :</p>
{code('''cagnotte ← 0
cagnotte ← cagnotte + 84       # gâteaux
cagnotte ← cagnotte + 126      # vélos
cagnotte ← cagnotte - 30       # matériel
tickets ← 45
cagnotte ← cagnotte + 2 × tickets   # tombola
Afficher cagnotte''')}
</div><div>
<p><b>a)</b> Complète le tableau de suivi.</p>
{trace_table(["Ligne", "tickets", "cagnotte"], [["1", "—", "0"]], 6)}
<p><b>b)</b> Le voyage coûte 12 € par élève et ils sont 25. Combien manque-t-il ?</p>{ans()}
</div></div>""", C[2])}
{defi(4, "L'échange impossible ?", 2, f"""
<div class="cols2"><div>
<p>Dans un jeu, Bitou veut <b>échanger</b> le contenu de deux variables : <span class="mono">a</span> (son nombre de pièces) et <span class="mono">b</span> (celui de Nova). Il écrit :</p>
{code('''a ← 5
b ← 8
a ← b
b ← a''')}
<p><b>a)</b> Que valent <span class="mono">a</span> et <span class="mono">b</span> à la fin ?</p>{ans()}
</div><div>
<p><b>b)</b> Ça ne marche pas ! Imagine deux verres : un de jus d'orange, un de lait. Comment les échanger ? Il faut un… <b>troisième verre</b> ! Écris l'algorithme correct avec une variable <span class="mono">temp</span>.</p>
{ans(lines=4)}
<div class="mini-art">{bitou(w=80, pose="think", mood="wow")}</div>
</div></div>""", C[2])}
{box("know", "🧠 Le savais-tu ?", "<p>Les compteurs d'abonnés, de « j'aime » ou de vues sur les réseaux sociaux sont des variables stockées sur d'immenses serveurs. Une vidéo très populaire peut voir sa variable « vues » augmenter de plusieurs milliers de fois… par seconde !</p>")}''', chapter=2, color=C[2])

# ================= CHAPITRE 3
CH[3] = add(f'''{chap_banner(3, TITLES[3], "Si… alors… sinon : apprendre à décider", C[3], bitou(w=120, pose="point"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Une <b>condition</b> permet à un programme de <b>choisir</b> quoi faire selon la situation. On teste quelque chose qui est soit <b>VRAI</b>, soit <b>FAUX</b>.</p>
{code('''Si il pleut alors
    prendre un parapluie
Sinon
    prendre une casquette
Fin Si''')}
<p>On peut enchaîner plusieurs tests avec <b>Sinon si</b>. Dès qu'un test est vrai, on exécute son bloc et on <b>ignore la suite</b>.</p>
<h3 class="h3">Exemple : le tri sélectif automatique</h3>
<p>Une start-up fabrique une poubelle intelligente qui reconnaît les déchets avec une caméra. Voici son algorithme :</p>
</div>
<div>{flow_sort()}</div>
</div>
{bins_svg()}
{defi(5, "Trie comme un robot", 1, f"""
<div class="cols2"><div><p>Suis l'organigramme pour chaque déchet. Écris la couleur du bac.</p>
<table class="trace wide"><tr><th>Déchet</th><th>Bac</th></tr>
<tr><td>🧴 Bouteille d'eau en plastique</td><td></td></tr><tr><td>🫙 Pot de confiture en verre</td><td></td></tr>
<tr><td>🍌 Peau de banane</td><td></td></tr><tr><td>🥫 Canette de soda</td><td></td></tr><tr><td>🪥 Vieille brosse à dents</td><td></td></tr></table></div>
<div><p><b>Le piège 🔋 :</b> Nova jette une <b>pile usagée</b>. Selon l'algorithme, où va-t-elle ? Est-ce une bonne idée ?</p>{ans(lines=2)}
<p>Propose une condition à ajouter <b>au début</b> pour corriger l'algorithme.</p>{ans(lines=2)}</div></div>""", C[3])}''', chapter=3, color=C[3])

add(f'''{defi(6, "Alerte canicule !", 2, f"""
<div class="cols-t"><div>{thermo_svg(85)}</div><div>
<p>Les étés sont de plus en plus chauds. Une appli météo affiche une couleur d'alerte selon la température <span class="mono">t</span> prévue <i>(seuils inventés pour l'exercice)</i> :</p>
{code('''Si t ≥ 40 alors
    Afficher "ROUGE : restez au frais !"
Sinon si t ≥ 35 alors
    Afficher "ORANGE : buvez beaucoup d'eau"
Sinon si t ≥ 30 alors
    Afficher "JAUNE : attention au soleil"
Sinon
    Afficher "VERT : tout va bien"
Fin Si''')}
</div></div>
<p><b>a)</b> Quelle couleur s'affiche pour : t = 28 → ........ t = 36 → ........ t = 41 → ........ t = 35 → ........ t = 30 → ........</p>
<div class="cols2"><div>
<p><b>b)</b> Un stagiaire a écrit les tests <b>dans l'autre sens</b> : d'abord <span class="mono">t ≥ 30</span>, puis <span class="mono">t ≥ 35</span>, puis <span class="mono">t ≥ 40</span>. Quelle couleur s'affiche alors pour t = 41 ? Pourquoi est-ce un <b>bug</b> ?</p>{ans(lines=2)}
</div><div>{box("tip", "💡 Astuce", "<p>Avec des « Sinon si », l'<b>ordre des tests</b> compte : on teste du plus précis au plus général.</p>")}</div></div>""", C[3])}
{defi(7, "ET, OU : la piscine est-elle ouverte ?", 2, f"""
<div class="cols2"><div>
<p>On peut combiner des conditions :</p>
<ul class="tight"><li><b>A ET B</b> est vrai si <b>les deux</b> sont vrais.</li><li><b>A OU B</b> est vrai si <b>au moins un</b> des deux est vrai.</li></ul>
{code('''Si t ≥ 25 ET orage = non alors
    Afficher "Piscine ouverte"
Sinon
    Afficher "Piscine fermée"
Fin Si''')}
</div><div>
<table class="trace wide"><tr><th>t</th><th>orage</th><th>Ouverte ?</th></tr>
<tr><td>30</td><td>non</td><td></td></tr><tr><td>30</td><td>oui</td><td></td></tr><tr><td>20</td><td>non</td><td></td></tr><tr><td>20</td><td>oui</td><td></td></tr></table>
<p class="small"><b>Bonus :</b> si on remplace <b>ET</b> par <b>OU</b>, quelles réponses changent ?</p>
</div></div>""", C[3])}
<div class="cols2">{scratch([("ctrl", "si <span class='op'>t ≥ 40</span> alors", [("look", "dire <u>ROUGE</u>")]), ("ctrl", "sinon", [("look", "dire <u>…</u>")])])}
{py("""t = int(input("Température ? "))
if t >= 40:
    print("ROUGE")
elif t >= 35:
    print("ORANGE")
elif t >= 30:
    print("JAUNE")
else:
    print("VERT")""")}</div>''', chapter=3, color=C[3])

# ================= CHAPITRE 4
shapes = (f'<div class="shapes"><figure>{shape_svg(4, 90, "#facc15", 110)}<figcaption>Répéter <b>4</b> fois<br>avancer · tourner <b>90°</b></figcaption></figure>'
          f'<figure>{shape_svg(3, 120, "#22d3ee", 110)}<figcaption>Répéter <b>3</b> fois<br>avancer · tourner <b>120°</b></figcaption></figure>'
          f'<figure>{shape_svg(5, 144, "#f472b6", 110)}<figcaption>Répéter <b>5</b> fois<br>avancer · tourner <b>144°</b></figcaption></figure>'
          f'<figure>{shape_svg(6, 60, "#a3e635", 110)}<figcaption>Répéter <b>?</b> fois<br>avancer · tourner <b>?°</b></figcaption></figure></div>')
CH[4] = add(f'''{chap_banner(4, TITLES[4], "Ne plus jamais écrire 100 fois la même chose", C[4], drone(140, "#F59E0B"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Quand une action doit être faite plusieurs fois, on utilise une <b>boucle</b>. Au lieu d'écrire 4 fois la même chose, on écrit :</p>
{code('''Répéter 4 fois
    avancer de 50
    tourner de 90°
Fin Répéter''')}
<p>Le drone dessine un <b>carré</b> ! Les instructions <b>à l'intérieur</b> de la boucle (décalées vers la droite) sont répétées.</p>
</div>
<div>
{scratch([("event", "quand le drapeau est cliqué"), ("pen", "stylo en position d'écriture"), ("ctrl", "répéter <u>4</u> fois", [("motion", "avancer de <u>50</u> pas"), ("motion", "tourner ↻ de <u>90</u> degrés")])])}
{py("""import turtle
for i in range(4):
    turtle.forward(50)
    turtle.right(90)""")}
</div></div>
{defi(8, "Le spectacle de drones", 2, f"""
<p>Pour les grandes fêtes, des centaines de drones lumineux dessinent des formes dans le ciel. Chaque drone suit un algorithme avec une boucle !</p>
{shapes}
<div class="cols2"><div>
<p><b>a)</b> Quelle figure dessine le 4<sup>e</sup> drone ? Complète son programme.</p>{ans()}
<p><b>b)</b> Observe les trois premiers : combien de degrés le drone tourne-t-il <b>au total</b> pour le carré ? pour le triangle ?</p>{ans()}
</div><div>
<p><b>c)</b> Trouve la règle : pour un polygone à <b>n</b> côtés, l'angle vaut <b>360 ÷ n</b>. Quel programme dessine un octogone (8 côtés) ?</p>{ans()}
<p><b>d) Expert :</b> l'étoile fait 2 tours complets. Vérifie : 5 × 144 = ........ = 2 × 360.</p>
</div></div>""", C[4])}''', chapter=4, color=C[4])

add(f'''{defi(9, "La Coupe du monde 2026", 3, f"""
<div class="cols-t"><div>{football(70)}</div><div>
<p>En 2026, la Coupe du monde de football s'est jouée aux <b>États-Unis</b>, au <b>Canada</b> et au <b>Mexique</b>, avec pour la première fois <b>48 équipes</b> ! Elles sont réparties en <b>12 groupes de 4</b>. Dans un groupe, chaque équipe affronte une fois chacune des 3 autres.</p></div></div>
<div class="cols2"><div>
<p><b>a)</b> Dans un groupe A, B, C, D, écris la liste de tous les matchs. Combien y en a-t-il ?</p>
<p class="mono">A–B, A–C, ........................................</p>{ans()}
<p><b>b)</b> Complète l'algorithme qui compte les matchs de la phase de groupes, puis exécute-le.</p>
{code('''total ← 0
Pour groupe de 1 à 12 faire
    total ← total + .....
Fin Pour
Afficher total''')}{ans()}
</div><div>
<p><b>c)</b> 32 équipes se qualifient pour la phase finale. À chaque match, le perdant est éliminé. Exécute cet algorithme :</p>
{code('''équipes ← 32
matchs ← 0
Tant que équipes > 1 faire
    matchs ← matchs + équipes ÷ 2
    équipes ← équipes ÷ 2
Fin Tant que
Afficher matchs''')}
{trace_table(["Tour", "équipes", "matchs"], [["début", "32", "0"]], 5)}
</div></div>
<p><b>d)</b> On ajoute le match pour la 3<sup>e</sup> place. Combien de matchs en tout dans cette Coupe du monde ?</p>{ans()}
""", C[4])}
<div class="cols2">{box("know", "🧠 Le savais-tu ?", "<p>Les organisateurs utilisent des algorithmes très complexes pour fabriquer le <b>calendrier</b> des matchs : il faut tenir compte des stades, des voyages, des fuseaux horaires et du repos des joueurs !</p>")}
<div>{bracket_svg()}</div></div>''', chapter=4, color=C[4])

# ================= CHAPITRE 5
CH[5] = add(f'''{chap_banner(5, TITLES[5], "Répéter tant qu'une condition est vraie", C[5], scooter(170))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Parfois, on ne sait pas <b>à l'avance</b> combien de fois répéter. On utilise alors une boucle <b>Tant que</b> : on répète <b>tant que</b> la condition est vraie, et on s'arrête dès qu'elle devient fausse.</p>
{code('''Tant que mon assiette n'est pas vide faire
    manger une bouchée
Fin Tant que''')}
{box("warn", "⚠️ La boucle infinie", "<p>Si la condition ne devient <b>jamais</b> fausse, le programme tourne pour toujours ! Il faut que quelque chose change à chaque tour.</p>")}
</div>
<div>
{defi(10, "La trottinette électrique", 2, f"""<p>Nova loue une trottinette en libre-service. Elle s'arrête quand la batterie descend à 20 % ou moins, pour pouvoir rejoindre une borne.</p>
{code('''batterie ← 100
km ← 0
Tant que batterie > 20 faire
    km ← km + 1
    batterie ← batterie - 8
Fin Tant que
Afficher km''')}
<p><b>a)</b> Combien de km Nova parcourt-elle ? Quelle est la batterie à la fin ?</p>{ans()}
<p><b>b)</b> Avec un modèle plus économe qui consomme 6 % par km ?</p>{ans()}""", C[5])}
</div></div>
<div class="cols2">
{trace_table(["Tour", "km", "batterie", "batterie > 20 ?"], [["début", "0", "100", "oui"], ["1", "1", "92", "oui"], ["2", "", "", ""]], 4)}
<div>
{py("""batterie = 100
km = 0
while batterie > 20:
    km = km + 1
    batterie = batterie - 8
print(km, batterie)""")}
{box("tip", "💡 Astuce", "<p>Au lieu de tout calculer de tête, remplis un tableau de suivi ligne par ligne. Les vrais programmeurs font pareil pour trouver leurs bugs !</p>")}
</div></div>''', chapter=5, color=C[5])

add(f'''<div class="moon-head">{moon_scene(560)}</div>
<p class="lead">Avec le programme <b>Artemis</b>, des astronautes repartent vers la Lune, plus de 50 ans après les missions Apollo. Nova et Bitou font partie de l'équipe au sol !</p>
<div class="cols2">
{defi(11, "Le compte à rebours", 1, f"""
{code('''n ← 10
Tant que n > 0 faire
    Afficher n
    n ← n - 1
Fin Tant que
Afficher "Décollage !"''')}
<p><b>a)</b> Quel est le dernier nombre affiché avant « Décollage ! » ?</p>{ans()}
<p><b>b)</b> Bitou a tapé <span class="mono">n ← n + 1</span> au lieu de <span class="mono">n ← n - 1</span>. Que se passe-t-il ?</p>{ans(lines=2)}""", C[5])}
{defi(12, "Le rover ramasseur", 2, f"""
<p>Sur la Lune, le rover ramasse des échantillons de roche. Chaque échantillon lui coûte 12 unités d'énergie.</p>
{code('''énergie ← 50
échantillons ← 0
Tant que énergie ≥ 12 faire
    échantillons ← échantillons + 1
    énergie ← énergie - 12
Fin Tant que''')}
<p><b>a)</b> Combien d'échantillons rapporte-t-il ? Combien d'énergie lui reste-t-il ?</p>{ans()}
<p><b>b)</b> Quelle opération de maths fait en réalité cet algorithme ?</p>{ans()}""", C[5])}
</div>
{box("know", "🧠 Le savais-tu ?", "<div class='cols-t'><div>" + rocket(46) + "</div><div><p>En 1969, le code qui a guidé Apollo 11 jusqu'à la Lune a été dirigé par <b>Margaret Hamilton</b>. Son équipe avait prévu qu'en cas de surcharge, l'ordinateur abandonne les tâches les moins importantes. Grâce à cela, l'alunissage a pu continuer malgré des alarmes !</p></div></div>")}''', chapter=5, color=C[5])

# ================= CHAPITRE 6
songs = ["Soleil de minuit", "Pixel Love", "Mars Express", "Vague électrique", "Danse des drones"]
CH[6] = add(f'''{chap_banner(6, TITLES[6], "Ranger plein de valeurs dans une seule variable", C[6], nova(w=120, pose="wave"))}
<div class="cols-pl">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Une <b>liste</b> (on dit aussi <b>tableau</b>) est une variable qui contient <b>plusieurs valeurs</b> rangées dans l'ordre. Chaque valeur a une <b>position</b> (son numéro).</p>
{code('''playlist ← ["Soleil de minuit", "Pixel Love",
             "Mars Express", "Vague électrique",
             "Danse des drones"]''')}
<table class="trace wide"><tr><th>Instruction</th><th>Résultat</th></tr>
<tr><td class="mono">longueur(playlist)</td><td>5</td></tr>
<tr><td class="mono">playlist[2]</td><td>"Pixel Love"</td></tr>
<tr><td class="mono">ajouter "Lune" à playlist</td><td>la liste a 6 titres</td></tr>
<tr><td class="mono">supprimer playlist[1]</td><td>les autres remontent d'un cran</td></tr></table>
</div>
<div class="center">{phone_playlist(songs, 205, hl=1)}</div>
</div>
{box("warn", "⚠️ Attention en Python !", "<p>Dans ce livre et dans Scratch, les positions commencent à <b>1</b>. Mais en Python, elles commencent à <b>0</b> ! <span class='mono'>playlist[0]</span> vaut donc « Soleil de minuit ».</p>")}
{defi(13, "Ma playlist de l'été", 1, f"""
<div class="cols2"><div>
<p>On part de la playlist ci-dessus (5 titres) et on exécute :</p>
{code('''ajouter "Lune rousse" à playlist
supprimer playlist[3]
ajouter "Retour sur Terre" à playlist
Afficher longueur(playlist)
Afficher playlist[3]''')}
</div><div>
<p><b>a)</b> Combien de titres s'affichent ?</p>{ans()}
<p><b>b)</b> Quel est le titre n°3 à la fin ?</p>{ans()}
<p><b>c)</b> Écris la liste complète finale.</p>{ans(lines=2)}
</div></div>""", C[6])}''', chapter=6, color=C[6])

temps = [31, 34, 38, 41, 36, 29, 33]
days = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
add(f'''{defi(14, "La semaine de records", 2, f"""
<p>Voici les températures maximales relevées pendant une semaine de canicule dans une ville <i>(valeurs inventées pour l'exercice)</i> :</p>
{temp_bars(temps, days)}
<p class="mono center big">températures ← [31, 34, 38, 41, 36, 29, 33]</p>
<div class="cols2"><div>
<p>Pour trouver la <b>plus grande</b> valeur d'une liste, on utilise cet algorithme célèbre :</p>
{code('''max ← températures[1]
Pour chaque t dans températures faire
    Si t > max alors
        max ← t
    Fin Si
Fin Pour
Afficher max''')}
</div><div>
<p><b>a)</b> Suis l'algorithme : écris les valeurs successives de <span class="mono">max</span>.</p>{ans()}
<p><b>b)</b> Modifie l'algorithme pour trouver la température <b>la plus basse</b>.</p>{ans(lines=2)}
</div></div>
<div class="cols2"><div>
<p><b>c)</b> Écris un algorithme qui compte les jours où il a fait <b>35° ou plus</b>. Combien y en a-t-il ?</p>{ans(lines=3)}
</div><div>
<p><b>d)</b> Calcule la <b>moyenne</b> de la semaine (arrondie au dixième). Indice : additionne tout avec une boucle, puis divise par la longueur de la liste.</p>{ans(lines=2)}
</div></div>""", C[6])}
<div class="cols2">{py("""temperatures = [31, 34, 38, 41, 36, 29, 33]
maxi = temperatures[0]
for t in temperatures:
    if t > maxi:
        maxi = t
print(maxi)""")}
{box("know", "🧠 Le savais-tu ?", "<p>Les climatologues analysent des listes de <b>millions</b> de températures mesurées partout sur la planète depuis plus de 150 ans. Sans algorithmes, impossible de repérer les records et le réchauffement climatique !</p>")}</div>''', chapter=6, color=C[6])

# ================= CHAPITRE 7
sel = [[7, 2, 9, 4, 1], [1, 2, 9, 4, 7], [1, 2, 9, 4, 7], [1, 2, 4, 9, 7], [1, 2, 4, 7, 9]]
sel_hi = [(0, 4), (), (2, 3), (3, 4), ()]
sel_txt = ["Départ : le plus petit est 1 → on l'échange avec la 1<sup>re</sup> case.", "Étape 1 : 1 est bien rangé. Le plus petit du reste est 2 : déjà à sa place !",
           "Étape 2 : le plus petit du reste est 4 → on l'échange avec 9.", "Étape 3 : le plus petit du reste est 7 → on l'échange avec 9.", "Terminé : la liste est triée ! 🎉"]
sel_html = "".join(f'<div class="selrow">{bars_row(v, sel_hi[i], i, 200)}<p>{sel_txt[i]}</p></div>' for i, v in enumerate(sel))
CH[7] = add(f'''{chap_banner(7, TITLES[7], "Mettre de l'ordre dans le chaos", C[7], bitou(w=120, pose="cheer"))}
<h2 class="h2">📘 Je comprends : le tri par sélection</h2>
<p>Les ordinateurs passent leur temps à <b>trier</b> : les classements de jeux, les résultats de recherche, les prix du moins cher au plus cher… Voici une méthode simple : <b>on cherche le plus petit, on le met devant, et on recommence avec le reste</b>.</p>
<div class="selgrid">{sel_html}</div>
{code('''Pour i de 1 à longueur(liste) - 1 faire
    chercher la position p du plus petit élément entre i et la fin
    échanger liste[i] et liste[p]
Fin Pour''', "Le tri par sélection")}
{box("tip", "💡 Joue avec des cartes !", "<p>Prends 6 cartes à jouer mélangées et trie-les avec cette méthode, en comptant le nombre d'échanges. Puis essaie avec un·e ami·e : qui trie le plus vite en suivant <b>exactement</b> l'algorithme ?</p>")}''', chapter=7, color=C[7])

add(f'''{defi(15, "Le tri à bulles du tournoi d'e-sport", 2, f"""
<p>Une autre méthode célèbre : le <b>tri à bulles</b>. On compare les éléments <b>deux par deux, côte à côte</b>, de gauche à droite. S'ils sont dans le mauvais ordre, on les échange. On refait des passages jusqu'à ce qu'il n'y ait plus aucun échange. Les grands nombres « remontent » vers la fin comme des bulles !</p>
<div class="cols2"><div>
<p>Exemple, premier passage sur <span class="mono">[5, 3, 8, 1]</span> :</p>
<div class="bubble-steps">
<div><span class="mono"><b class="hl">5 3</b> 8 1</span> → échange → <span class="mono">3 5 8 1</span></div>
<div><span class="mono">3 <b class="hl">5 8</b> 1</span> → OK → <span class="mono">3 5 8 1</span></div>
<div><span class="mono">3 5 <b class="hl">8 1</b></span> → échange → <span class="mono">3 5 1 8</span></div></div>
<p><b>a)</b> Termine le tri : écris la liste après chaque passage.</p>
<p>Passage 2 : {ans("")}</p><p>Passage 3 : {ans("")}</p>
<p><b>b)</b> Combien d'échanges en tout ?</p>{ans()}
</div><div>
<p><b>c)</b> Au tournoi du collège, voici les scores des équipes. Trie-les du <b>plus grand au plus petit</b> avec le tri à bulles (attention : on change le sens de la comparaison !).</p>
<table class="trace wide"><tr><th>Équipe</th><th>Score</th></tr><tr><td>🐉 Les Dragons</td><td>42</td></tr><tr><td>🦊 Les Renards</td><td>57</td></tr><tr><td>🐙 Les Krakens</td><td>38</td></tr><tr><td>🦅 Les Aigles</td><td>61</td></tr></table>
<p>Classement final :</p>{ans("1.")}{ans("2.")}{ans("3.")}{ans("4.")}
</div></div>""", C[7])}
<div class="cols2">{py("""scores = [42, 57, 38, 61]
n = len(scores)
for passage in range(n - 1):
    for i in range(n - 1):
        if scores[i] < scores[i + 1]:
            scores[i], scores[i + 1] = scores[i + 1], scores[i]
print(scores)""")}
{box("know", "🧠 Le savais-tu ?", "<p>Le tri à bulles est facile à comprendre, mais il est <b>lent</b> pour de grandes listes. Les ordinateurs utilisent des méthodes plus malines, comme le <b>tri fusion</b> : ils trient un million de nombres en une fraction de seconde !</p>")}</div>''', chapter=7, color=C[7])

# ================= CHAPITRE 8
iv = [(1, 100, 50, "plus"), (51, 100, 75, "moins"), (51, 74, 62, "plus"), (63, 74, 68, "plus"), (69, 74, 71, "plus"), (72, 74, 73, "gagné !")]
ivs = ""
for i, (a, b, m, r) in enumerate(iv):
    x1 = 10 + (a - 1) * 3.4; x2 = 10 + b * 3.4
    xm = 10 + (m - 0.5) * 3.4; y = 8 + i * 28
    ivs += (f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="18" rx="9" fill="#99f6e4" stroke="{INK}" stroke-width="2"/>'
            f'<circle cx="{xm}" cy="{y+9}" r="7" fill="#14B8A6" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{x1-4}" y="{y+13}" text-anchor="end" font-family="Fredoka" font-size="10" fill="{INK}">{a}</text>'
            f'<text x="{x2+4}" y="{y+13}" font-family="Fredoka" font-size="10" fill="{INK}">{b}</text>'
            f'<text x="372" y="{y+13}" font-family="Nunito" font-weight="800" font-size="11" fill="#0f766e">{m} ? {r}</text>')
dicho_svg = f'<svg viewBox="-10 0 470 176" width="100%">{ivs}</svg>'
CH[8] = add(f'''{chap_banner(8, TITLES[8], "La recherche dichotomique, l'arme secrète", C[8], nova(w=120, pose="think"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Jeu : Bitou pense à un nombre entre <b>1 et 100</b>. Tu proposes un nombre, il répond « plus grand », « plus petit » ou « gagné ».</p>
<p>❌ Méthode lente : 1 ? 2 ? 3 ? … jusqu'à 100 essais !</p>
<p>✅ Méthode maline : toujours proposer le <b>milieu</b>. À chaque question, on élimine <b>la moitié</b> des possibilités. C'est la <b>recherche dichotomique</b> (« couper en deux »).</p>
</div>
<div>{box("know", "🧠 Le savais-tu ?", "<p>Tu utilises déjà la dichotomie quand tu cherches un mot dans un dictionnaire papier : tu l'ouvres au milieu, puis tu choisis la bonne moitié… Ça ne marche que parce que les mots sont <b>triés</b> !</p>")}</div>
</div>
<h3 class="h3">Exemple : le nombre secret est 73</h3>
{dicho_svg}
<p class="center">Seulement <b>6 questions</b> au lieu de 73 ! 🎉</p>
{code('''bas ← 1
haut ← 100
Répéter
    milieu ← partie entière de (bas + haut) ÷ 2
    Si milieu < secret alors bas ← milieu + 1
    Sinon si milieu > secret alors haut ← milieu - 1
Jusqu'à milieu = secret''', "Recherche dichotomique")}''', chapter=8, color=C[8])

add(f'''{defi(16, "Le prix mystère", 2, f"""
<div class="cols2"><div>
<p>Dans un jeu télé, il faut deviner le prix d'une nouvelle console de jeux, entre <b>100 €</b> et <b>600 €</b>. Le prix secret est <b>437 €</b>. Applique la méthode du milieu (arrondi à l'unité inférieure) et complète :</p>
</div><div class="center">{padlock(46, "#14B8A6")}</div></div>
{trace_table(["Question", "bas", "haut", "milieu proposé", "Réponse"], [["1", "100", "600", "350", "plus grand"], ["2", "351", "600", "", ""]], 6)}
<p><b>Combien de questions</b> a-t-il fallu ?</p>{ans()}""", C[8])}
{defi(17, "La puissance du « couper en deux »", 3, f"""
<div class="cols2"><div>
<p>À chaque question, le nombre de possibilités est divisé par 2. Complète :</p>
<table class="trace wide"><tr><th>Questions</th><th>Possibilités traitées</th></tr>
<tr><td>1</td><td>2</td></tr><tr><td>2</td><td>4</td></tr><tr><td>3</td><td>8</td></tr><tr><td>…</td><td>…</td></tr><tr><td>7</td><td></td></tr><tr><td>10</td><td></td></tr></table>
</div><div>
<p><b>a)</b> Combien de questions au maximum pour un nombre entre 1 et 100 ?</p>{ans()}
<p><b>b)</b> Entre 1 et 1 000 000 ? <i>(Indice : 2<sup>20</sup> = 1 048 576)</i></p>{ans()}
<p><b>c) Défi ultime :</b> il y a environ 8 milliards d'humains. Si on les rangeait dans l'ordre alphabétique, combien de questions « oui/non » suffiraient pour retrouver n'importe qui ?</p>{ans()}
</div></div>""", C[8])}
<div class="cols2">
<div>{bubble("bitou", "Moi j'avais commencé par 100, 101, 102… J'aurais trouvé en 338 questions. 😅")}</div><div>{bubble("nova", "Avec la dichotomie, 8 questions suffisent. Travailler malin, c'est mieux que travailler beaucoup !", "right")}</div></div>''', chapter=8, color=C[8])

# ================= CHAPITRE 9
CH[9] = add(f'''{chap_banner(9, TITLES[9], "Créer ses propres blocs et les réutiliser", C[9], bitou(w=120, pose="wave"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Une <b>fonction</b> est un petit algorithme auquel on donne un <b>nom</b>. On peut ensuite l'<b>appeler</b> autant de fois qu'on veut, comme un nouveau bloc. Elle peut recevoir des <b>paramètres</b> (des valeurs d'entrée) et <b>retourner</b> un résultat.</p>
{code('''Fonction carré(taille)
    Répéter 4 fois
        avancer de taille
        tourner de 90°
    Fin Répéter
Fin Fonction

carré(30)
carré(60)
carré(90)''')}
<p>3 carrés de tailles différentes avec seulement 3 lignes !</p>
</div>
<div>
<svg viewBox="0 0 200 200" width="80%" style="display:block;margin:0 auto"><rect width="200" height="200" rx="16" fill="#fff7ed"/>
<rect x="20" y="20" width="160" height="160" fill="none" stroke="#F97316" stroke-width="4"/><rect x="20" y="73" width="107" height="107" fill="none" stroke="#FB923C" stroke-width="4"/><rect x="20" y="127" width="53" height="53" fill="none" stroke="#FDBA74" stroke-width="4"/><circle cx="20" cy="180" r="6" fill="{INK}"/></svg>
{scratch([("myb", "définir <b>carré</b> (taille)"), ("ctrl", "répéter <u>4</u> fois", [("motion", "avancer de <i>taille</i>"), ("motion", "tourner ↻ de <u>90</u> degrés")])], "🧩 « Créer un bloc » dans Scratch")}
</div></div>
{box("tip", "💡 Pourquoi c'est génial ?", "<p>Les fonctions évitent de recopier du code, rendent le programme plus <b>lisible</b> et permettent de travailler en équipe : chacun programme ses fonctions, puis on les assemble. Une appli de ton téléphone contient des <b>milliers</b> de fonctions !</p>")}''', chapter=9, color=C[9])

add(f'''{defi(18, "Sortie au cinéma", 2, f"""
<div class="cols2"><div>
<p>Le cinéma du quartier a créé une fonction pour calculer le prix d'un billet selon l'âge <i>(tarifs inventés)</i> :</p>
{code('''Fonction prix_billet(âge)
    Si âge < 12 alors
        Retourner 6
    Sinon si âge ≥ 65 alors
        Retourner 7
    Sinon
        Retourner 10
    Fin Si
Fin Fonction''')}
</div><div>
<p><b>a)</b> Que retournent :</p>
<p class="mono">prix_billet(8) = ........<br>prix_billet(12) = ........<br>prix_billet(70) = ........</p>
<p><b>b)</b> La famille de Nova va voir le dernier film de science-fiction : sa petite sœur (10 ans), Nova (14 ans), sa mère (42 ans) et son grand-père (68 ans). Combien paient-ils ?</p>{ans()}
</div></div>
<p><b>c)</b> Le mercredi, tous les billets ont <b>2 € de réduction</b>. Écris une fonction <span class="mono">prix_mercredi(âge)</span> qui <b>utilise</b> <span class="mono">prix_billet</span>.</p>{ans(lines=3)}""", C[9])}
{defi(19, "La fonction mystère", 3, f"""
<div class="cols2"><div>
{code('''Fonction mystère(n)
    résultat ← 0
    Pour i de 1 à n faire
        résultat ← résultat + i
    Fin Pour
    Retourner résultat
Fin Fonction''')}
</div><div>
<p><b>a)</b> Calcule <span class="mono">mystère(3)</span>, puis <span class="mono">mystère(5)</span>.</p>{ans()}
<p><b>b)</b> Que calcule cette fonction ? Donne-lui un meilleur nom !</p>{ans()}
<p><b>c)</b> Le savant Gauss aurait trouvé <span class="mono">mystère(100)</span> de tête à 9 ans. Et toi ? <i>(Indice : 1+100, 2+99, 3+98…)</i></p>{ans()}
</div></div>""", C[9])}''', chapter=9, color=C[9])

# ================= CHAPITRE 10
nodes = {"M": (40, 120), "G": (150, 40), "P": (165, 160), "S": (300, 172), "C": (370, 50)}
edges = [("M", "G", 4), ("M", "P", 7), ("G", "P", 2), ("G", "S", 8), ("P", "S", 3), ("P", "C", 9), ("S", "C", 2), ("G", "C", 12)]
full = {"M": "Maison", "G": "Gare", "P": "Parc", "S": "Stade", "C": "Collège"}
CH[10] = add(f'''{chap_banner(10, TITLES[10], "Comment ton GPS trouve le chemin le plus court", C[10], drone(130, "#0891B2"))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Un <b>graphe</b>, c'est un ensemble de <b>points</b> (appelés <b>sommets</b>) reliés par des <b>traits</b> (appelés <b>arêtes</b>). On peut s'en servir pour représenter une carte : les sommets sont des lieux, les arêtes des routes, et le nombre sur chaque arête est la durée du trajet.</p>
</div>
<div>{box("know", "🧠 Le savais-tu ?", "<p>En 1956, l'informaticien néerlandais <b>Edsger Dijkstra</b> a inventé en une vingtaine de minutes, à la terrasse d'un café, l'algorithme du plus court chemin. Il est encore utilisé dans les GPS et sur Internet !</p>")}</div>
</div>
<h3 class="h3">La carte des pistes cyclables de la ville (durées en minutes)</h3>
{graph_svg(nodes, edges, w="92%", labels_full=full, vb="0 0 410 222")}
{defi(20, "À vélo jusqu'au collège", 2, f"""
<div class="cols2"><div>
<p><b>a)</b> Bitou passe par la gare : M → G → C. Combien de minutes ?</p>{ans()}
<p><b>b)</b> Nova passe par le parc : M → P → C. Combien de minutes ?</p>{ans()}
</div><div>
<p><b>c)</b> Trouve le chemin le <b>plus rapide</b> de la Maison au Collège. Combien de minutes ?</p>{ans(lines=2)}
<p class="small">💡 Méthode de Dijkstra : note à côté de chaque lieu le temps le plus court pour l'atteindre, en partant des plus proches.</p>
</div></div>""", C[10])}''', chapter=10, color=C[10])

snodes = {"Léa": (50, 60), "Tom": (150, 30), "Inès": (110, 150), "Yanis": (260, 50), "Malo": (230, 170), "Zoé": (340, 120), "Adam": (430, 60), "Sarah": (380, 210)}
sedges = [("Léa", "Tom"), ("Léa", "Inès"), ("Tom", "Inès"), ("Tom", "Yanis"), ("Inès", "Malo"), ("Yanis", "Zoé"), ("Malo", "Zoé"), ("Zoé", "Adam"), ("Malo", "Sarah"), ("Zoé", "Sarah")]
pal = {"Léa": "#ec4899", "Tom": "#3b82f6", "Inès": "#10b981", "Yanis": "#f59e0b", "Malo": "#8b5cf6", "Zoé": "#ef4444", "Adam": "#0891b2", "Sarah": "#84cc16"}
add(f'''{defi(21, "La rumeur qui se propage", 3, f"""
<p>Sur un réseau social, deux élèves sont reliés s'ils sont amis. Voici le graphe d'une petite partie du collège :</p>
{graph_svg(snodes, [(a, b) for a, b in sedges], weights=False, node_col=lambda k: pal[k], r=30, fs=11.5, vb="0 0 480 250")}
<div class="cols2"><div>
<p><b>a)</b> Le <b>degré</b> d'un sommet, c'est son nombre d'amis. Qui a le plus d'amis ?</p>{ans()}
<p><b>b)</b> Quel est le plus court chemin entre Léa et Adam ? Combien d'arêtes ?</p>{ans()}
</div><div>
<p><b>c)</b> Léa lance une fausse information. Chaque heure, toute personne qui la connaît la transmet à <b>tous</b> ses amis. Au bout de combien d'heures tout le monde la connaît-il ?</p>
{trace_table(["Heure", "Qui vient de l'apprendre ?"], [["0", "Léa"], ["1", ""], ["2", ""]], 2)}
</div></div>""", C[10])}
{box("know", "🧠 Fausses infos : un vrai problème de graphe !", "<p>Des études ont montré que les fausses informations se propagent souvent <b>plus vite</b> que les vraies sur les réseaux sociaux, car elles sont plus surprenantes. Avant de partager : <b>vérifie la source</b>, la date, et cherche si d'autres médias fiables en parlent. Tu peux être celui ou celle qui <b>casse la chaîne</b> ! ⛓️‍💥</p>")}''', chapter=10, color=C[10])

# ================= CHAPITRE 11
msg1 = caesar("BRAVO AGENT TU AS TROUVE", 3)
msg2 = caesar("RENDEZ VOUS AU CDI A MIDI", 5)
CH[11] = add(f'''{chap_banner(11, TITLES[11], "Le chiffrement : protéger ses secrets", C[11], padlock(90, "#64748B"))}
<div class="cols-cz">
<div>
<h2 class="h2">📘 Je comprends : le code de César</h2>
<p>Il y a plus de 2 000 ans, Jules César envoyait des messages secrets à ses généraux. Son algorithme : <b>décaler chaque lettre de 3 rangs</b> dans l'alphabet.</p>
<p class="mono big center">A → D &nbsp; B → E &nbsp; C → F … X → A &nbsp; Y → B &nbsp; Z → C</p>
<p>Le nombre 3 est la <b>clé</b>. Pour <b>chiffrer</b>, on avance de 3. Pour <b>déchiffrer</b>, on recule de 3.</p>
<p>Exemple : <span class="mono">ALGO</span> devient <span class="mono">DOJR</span>.</p>
{box("tip", "✂️ Bricolage", "<p>Fabrique ta roue : découpe deux disques en carton, écris l'alphabet sur chacun et attache-les au centre avec une attache parisienne. Tourne pour changer de clé !</p>")}
</div>
<div class="center">{caesar_wheel(3, 240)}<p class="small">Lettre normale à l'extérieur, lettre chiffrée à l'intérieur.</p></div>
</div>
{defi(22, "Messages d'agents secrets", 2, f"""
<p><b>a)</b> Déchiffre ce message codé avec la clé 3 :</p>
<p class="mono big secret">{msg1}</p>{ans()}
<p><b>b)</b> Celui-ci a été codé avec la clé <b>5</b> :</p>
<p class="mono big secret">{msg2}</p>{ans()}
<p><b>c)</b> Chiffre ton prénom avec la clé 7 :</p>{ans()}
<p><b>d) Expert :</b> un espion intercepte <span class="mono">KHOOR</span> sans connaître la clé. Combien de clés différentes doit-il essayer au maximum ? Pourquoi ce code n'est-il <b>pas sûr</b> aujourd'hui ?</p>{ans(lines=2)}""", C[11])}''', chapter=11, color=C[11])

add(f'''{defi(23, "Ton mot de passe est-il costaud ?", 2, f"""
<div class="cols2"><div>
<p>Un site vérifie les mots de passe avec cet algorithme :</p>
{code('''force ← 0
Si longueur(mdp) ≥ 12 alors force ← force + 1
Si mdp contient un chiffre alors force ← force + 1
Si mdp contient une majuscule alors force ← force + 1
Si mdp contient un symbole (! ? - …) alors force ← force + 1

Si force = 4 alors Afficher "Fort 💪"
Sinon si force ≥ 2 alors Afficher "Moyen 😐"
Sinon Afficher "Faible 😱"''')}
</div><div>
<table class="trace wide"><tr><th>Mot de passe</th><th>force</th><th>Résultat</th></tr>
<tr><td class="mono">soleil</td><td></td><td></td></tr>
<tr><td class="mono">Soleil2026</td><td></td><td></td></tr>
<tr><td class="mono">jaimelefootetlespizzas</td><td></td><td></td></tr>
<tr><td class="mono">Tortue-Volante-42!</td><td></td><td></td></tr></table>
<p class="small">💡 Les longues <b>phrases de passe</b> faciles à retenir sont souvent plus sûres qu'un mot court et compliqué.</p>
</div></div>""", C[11])}
{defi(24, "L'attaque du robot pirate", 3, f"""
<div class="cols-t"><div>{robot("#475569", "#ef4444", pose="point", mood="flat", w=95)}</div><div>
<p>Un robot pirate essaie <b>toutes les combinaisons</b> possibles, à la vitesse d'<b>un milliard d'essais par seconde</b>. C'est une « attaque par force brute ».</p>
<p><b>a)</b> Un code PIN de 4 chiffres : combien de combinaisons ? <i>(10 × 10 × 10 × 10)</i></p>{ans()}
<p><b>b)</b> Un mot de 8 lettres minuscules : 26<sup>8</sup> ≈ 209 milliards de combinaisons. Combien de temps pour tout tester ?</p>{ans()}
<p><b>c)</b> Avec 12 caractères pris parmi 90 (lettres, chiffres, symboles), il y a environ 2,8 × 10<sup>23</sup> combinaisons. Il faudrait environ <b>9 millions d'années</b> ! Que peux-tu en conclure ?</p>{ans(lines=2)}
</div></div>""", C[11])}
{box("warn", "🛡️ Les 4 règles d'or de la cybersécurité", "<ol class='tight'><li>Un mot de passe <b>long</b> et <b>différent</b> pour chaque compte.</li><li>Ne jamais le donner, même à un·e ami·e, ni par message.</li><li>Méfie-toi des messages qui te pressent : « Clique vite, tu as gagné ! » (c'est de l'<b>hameçonnage</b>).</li><li>Active la <b>double authentification</b> quand c'est possible, avec l'aide d'un adulte.</li></ol>")}''', chapter=11, color=C[11])

# ================= CHAPITRE 12
CH[12] = add(f'''{chap_banner(12, TITLES[12], "Comment une machine apprend avec des exemples", C[12], robot("#C026D3", "#FDE047", pose="think", w=120))}
<div class="cols2">
<div>
<h2 class="h2">📘 Je comprends</h2>
<p>Avec un algorithme classique, c'est le programmeur qui écrit toutes les règles. Avec l'<b>apprentissage automatique</b>, on donne à la machine <b>des milliers d'exemples</b>, et c'est elle qui <b>trouve les règles</b> toute seule.</p>
<p>Par exemple, pour reconnaître un chat sur une photo, on lui montre des milliers de photos étiquetées « chat » ou « pas chat ». Elle repère peu à peu ce qui les distingue.</p>
{box("know", "🧠 Et les IA qui discutent ?", "<p>Les IA conversationnelles (les « chatbots ») ont lu d'énormes quantités de textes. Leur talent : <b>prédire le mot suivant</b> le plus probable, encore et encore. Essaie : « Il était une … » Tu as pensé « fois » ? Bravo, tu viens de faire comme une IA !</p>")}
</div>
<div>
<h3 class="h3">Un arbre de décision anti-spam</h3>
<p>Une IA simple apprend des questions à poser, sous forme d'<b>arbre</b> :</p>
{decision_tree()}
{box("warn", "⚠️ Une IA peut se tromper", "<p>Une IA n'est pas magique : si on lui donne de <b>mauvais exemples</b>, elle apprend de mauvaises règles (on parle de <b>biais</b>). Elle peut aussi inventer des réponses fausses avec beaucoup d'assurance. Garde toujours ton <b>esprit critique</b> !</p>")}
</div></div>
{defi(25, "Entraîne ton IA à reconnaître les fruits", 2, f"""
<div class="cols2"><div>
<table class="trace wide"><tr><th>Exemple</th><th>Couleur</th><th>Forme</th><th>Taille</th><th>Fruit</th></tr>
<tr><td>1</td><td>jaune</td><td>allongée</td><td>moyenne</td><td>🍌 banane</td></tr>
<tr><td>2</td><td>jaune</td><td>ronde</td><td>petite</td><td>🍋 citron</td></tr>
<tr><td>3</td><td>rouge</td><td>ronde</td><td>petite</td><td>🍒 cerise</td></tr>
<tr><td>4</td><td>rouge</td><td>ronde</td><td>moyenne</td><td>🍎 pomme</td></tr>
<tr><td>5</td><td>verte</td><td>ronde</td><td>grosse</td><td>🍉 pastèque</td></tr></table>
</div><div>
<p><b>a)</b> Dessine un arbre de décision qui reconnaît ces 5 fruits avec le <b>moins de questions</b> possible.</p>
<div class="drawbox"></div>
<p><b>b)</b> Que répond ton arbre pour un fruit <b>jaune, rond et gros</b> (un melon) ? Pourquoi se trompe-t-il ?</p>{ans()}
</div></div>""", C[12])}''', chapter=12, color=C[12])

add(f'''{defi(26, "Fabrique un algorithme de recommandation", 2, f"""
<p>Quand tu regardes des vidéos, un algorithme choisit la suivante pour te garder le plus longtemps possible. Voici une version simplifiée : chaque vidéo a des <b>mots-clés</b>. Le <b>score</b> d'une vidéo = le nombre de mots-clés <b>en commun</b> avec ce que tu as aimé.</p>
<p class="center">Tu as aimé des vidéos sur : <span class="tag big">#foot</span> <span class="tag big">#humour</span> <span class="tag big">#science</span></p>
<div class="vgrid">
{video_card("V1 · Le geste technique du siècle", ["foot", "cuisine"], "#22c55e", "⚽")}
{video_card("V2 · 10 expériences qui explosent", ["science", "espace", "humour"], "#8b5cf6", "🧪")}
{video_card("V3 · Chorégraphie de l'été", ["danse", "musique"], "#ec4899", "💃")}
{video_card("V4 · Les robots footballeurs", ["foot", "humour", "science"], "#0ea5e9", "🤖")}
{video_card("V5 · Voyage vers Mars", ["espace", "science"], "#f97316", "🚀")}
</div>
<div class="cols2"><div>
<p><b>a)</b> Calcule le score de chaque vidéo :</p>
<p class="mono">V1 : .... V2 : .... V3 : .... V4 : .... V5 : ....</p>
<p><b>b)</b> Dans quel ordre l'algorithme va-t-il te les proposer ?</p>{ans()}
</div><div>
<p><b>c)</b> Quelle vidéo ne te sera <b>jamais</b> proposée ? Si l'algorithme fait toujours ça, que risque-t-il de se passer ? <i>(On appelle ça une « bulle de filtres ».)</i></p>{ans(lines=2)}
</div></div>
<p><b>d)</b> Invente une règle pour que l'algorithme te fasse aussi découvrir des choses nouvelles :</p>{ans(lines=2)}""", C[12])}
<div class="cols2">
{box("know", "🧠 Le savais-tu ?", "<p>Les vrais algorithmes de recommandation utilisent des centaines d'indices : le temps que tu passes sur une vidéo, si tu la regardes jusqu'au bout, l'heure, ce que regardent des personnes qui te ressemblent… Ils sont conçus pour capter ton attention. À toi de garder le contrôle de ton <b>temps d'écran</b> ! ⏱️</p>")}
<div>{bubble("nova", "Le meilleur algorithme anti-ennui ? Poser le téléphone et aller jouer au foot !", "right")}</div>
</div>''', chapter=12, color=C[12])

# ================= GRAND DÉFI FINAL
CH[13] = add(f'''<div class="final-head">{chest(150)}<div><div class="banner-n" style="color:#a16207">GRAND DÉFI FINAL</div><h1 class="ptitle" style="margin:0">Escape game : le coffre de Nova</h1>
<p class="lead">Nova a caché sa clé USB dans un coffre à <b>4 chiffres</b>. Chaque énigme te donne un chiffre. Utilise tout ce que tu as appris !</p></div></div>
<div class="escape">
<div class="eg"><div class="eg-n">1</div><div><b>Variables</b>
{code('''x ← 3
x ← x × 4
x ← x - 5
Afficher x''')}<p>1<sup>er</sup> chiffre : <span class="digit"></span></p></div></div>
<div class="eg"><div class="eg-n">2</div><div><b>Boucles imbriquées</b>
{code('''compteur ← 0
Répéter 3 fois
    Répéter 2 fois
        compteur ← compteur + 1
    Fin Répéter
Fin Répéter
Afficher compteur''')}<p>2<sup>e</sup> chiffre : <span class="digit"></span></p></div></div>
<div class="eg"><div class="eg-n">3</div><div><b>Conditions</b>
{code('''n ← 21
Si n est pair alors d ← 2
Sinon si n est un multiple de 5 alors d ← 5
Sinon d ← 9
Afficher d''')}<p>3<sup>e</sup> chiffre : <span class="digit"></span></p></div></div>
<div class="eg"><div class="eg-n">4</div><div><b>Code secret</b><p>Déchiffre ce mot avec la clé de César <b>3</b>. C'est un nombre écrit en lettres !</p>
<p class="mono big secret">{caesar("TROIS", 3)}</p><p>4<sup>e</sup> chiffre : <span class="digit"></span></p></div></div>
</div>
<div class="finalcode"><span>CODE DU COFFRE :</span><span class="digit big"></span><span class="digit big"></span><span class="digit big"></span><span class="digit big"></span></div>
<div class="cols2">
{box("tip", "🏆 Énigme bonus pour les champions", "<p>Trie les 4 chiffres du code dans l'ordre <b>croissant</b> avec le tri à bulles. Combien d'échanges faut-il ?</p>" + ans())}
<div class="center">{bitou(w=90, pose="cheer")}{nova(w=90, pose="cheer", flip=True)}</div>
</div>''', chapter=13, color=C[13])

# ================= CORRIGÉS
CORR_START = len(PAGES) + 1


def sol(n, title, body):
    return f'<div class="sol"><div class="sol-h"><span>Défi {n}</span> {title}</div>{body}</div>'


add(f'''<h1 class="ptitle">✅ Corrigés</h1><p class="small">Il existe parfois plusieurs bonnes réponses : si ton algorithme fonctionne, il est juste !</p>
<div class="solcols">
{sol(1, "Le smoothie", "<p>Ordre : 5 – 2 – 1 – 3 – 6 – 4 → laver les fraises ; éplucher et couper la banane ; tout mettre dans le mixeur ; fermer le couvercle ; mixer 30 s ; verser dans un verre.</p><p><b>Bonus :</b> on peut laver les fraises et éplucher la banane dans n'importe quel ordre. Mais on ne peut pas mixer avant de fermer le couvercle… sauf si on aime repeindre la cuisine !</p>")}
{sol(2, "Le drone livreur", "<p><b>a)</b> Le drone arrive en <b>C5</b>.</p><p><b>b)</b> Il monte jusqu'en A6, puis en allant à droite il entre dans la zone interdite <b>C6</b> : mission échouée !</p><p><b>c)</b> 12 instructions : <span class='mono'>→→→→→ ↑↑ ← ↑↑↑ →</span> (A1 → F1 → F3 → E3 → E6 → F6).</p><p><b>d)</b> Répéter 5 fois → ; Répéter 2 fois ↑ ; ← ; Répéter 3 fois ↑ ; →.</p>")}
{sol(3, "La cagnotte", "<p><b>a)</b> 0 → 84 → 210 → 180 → (tickets = 45) → 180 + 90 = <b>270 €</b>.</p><p><b>b)</b> 12 × 25 = 300 €, il manque <b>30 €</b>.</p>")}
{sol(4, "L'échange", "<p><b>a)</b> a = 8 et b = 8 : la valeur 5 a été écrasée !</p><p><b>b)</b> <span class='mono'>temp ← a ; a ← b ; b ← temp</span>. On obtient a = 8 et b = 5.</p>")}
{sol(5, "Le tri", "<p>Bouteille → jaune ; pot en verre → vert ; peau de banane → marron ; canette → jaune ; brosse à dents → gris.</p><p><b>Pile :</b> l'algorithme l'envoie au bac gris, mais c'est dangereux pour l'environnement ! On ajoute au début : <i>Si c'est une pile ou un objet électronique alors → point de collecte (en magasin ou à la déchetterie)</i>.</p>")}
{sol(6, "Alerte canicule", "<p><b>a)</b> 28 → vert ; 36 → orange ; 41 → rouge ; 35 → orange ; 30 → jaune.</p><p><b>b)</b> Pour 41, le premier test <span class='mono'>t ≥ 30</span> est déjà vrai : on affiche <b>JAUNE</b> et les autres tests ne sont jamais regardés. Il faut tester du plus grand seuil au plus petit.</p>")}
{sol(7, "La piscine", "<p>30/non → ouverte ; 30/oui → fermée ; 20/non → fermée ; 20/oui → fermée.</p><p><b>Bonus</b> avec OU : 30/oui et 20/non deviennent « ouverte » (seul 20/oui reste fermé).</p>")}
{sol(8, "Les drones", "<p><b>a)</b> Un hexagone : Répéter <b>6</b> fois, avancer, tourner de <b>60°</b>.</p><p><b>b)</b> 4 × 90 = 360° et 3 × 120 = 360° : un tour complet.</p><p><b>c)</b> Répéter 8 fois : avancer, tourner de 360 ÷ 8 = <b>45°</b>.</p><p><b>d)</b> 5 × 144 = <b>720</b> = 2 × 360.</p>")}
</div>''', chapter=None, color="#16a34a")

add(f'''<h1 class="ptitle">✅ Corrigés (suite)</h1>
<div class="solcols">
{sol(9, "Coupe du monde 2026", "<p><b>a)</b> A–B, A–C, A–D, B–C, B–D, C–D : <b>6 matchs</b>.</p><p><b>b)</b> On ajoute 6 à chaque tour : 12 × 6 = <b>72 matchs</b>.</p><p><b>c)</b> 32 → 16 (16 matchs) → 8 (+8 = 24) → 4 (+4 = 28) → 2 (+2 = 30) → 1 (+1 = <b>31</b>).</p><p><b>d)</b> 72 + 31 + 1 = <b>104 matchs</b>.</p>")}
{sol(10, "La trottinette", "<p><b>a)</b> La batterie passe par 92, 84, 76, 68, 60, 52, 44, 36, 28, 20. À 20, la condition « &gt; 20 » est fausse : <b>10 km</b>, il reste <b>20 %</b>.</p><p><b>b)</b> 100, 94, 88… après 13 km il reste 22 % (on continue), après 14 km : 16 %. Réponse : <b>14 km</b>.</p>")}
{sol(11, "Compte à rebours", "<p><b>a)</b> Le dernier nombre est <b>1</b> (quand n vaut 0, on sort de la boucle).</p><p><b>b)</b> n vaut 11, 12, 13… il reste toujours &gt; 0 : c'est une <b>boucle infinie</b>, la fusée ne décolle jamais !</p>")}
{sol(12, "Le rover", "<p><b>a)</b> 50 → 38 → 26 → 14 → 2 : <b>4 échantillons</b>, il reste <b>2</b> unités.</p><p><b>b)</b> Une <b>division euclidienne</b> : 50 = 4 × 12 + 2 (quotient 4, reste 2).</p>")}
{sol(13, "La playlist", "<p>Après ajout : 6 titres. On supprime le n°3 (« Mars Express »). Puis on ajoute un titre.</p><p><b>a)</b> <b>6</b> titres. <b>b)</b> « Vague électrique ».</p><p><b>c)</b> Soleil de minuit, Pixel Love, Vague électrique, Danse des drones, Lune rousse, Retour sur Terre.</p>")}
{sol(14, "Les records", "<p><b>a)</b> max vaut 31, puis 34, 38, <b>41</b> (et ne change plus).</p><p><b>b)</b> On écrit <span class='mono'>Si t &lt; min</span> : le minimum est <b>29</b> (samedi).</p><p><b>c)</b> compteur ← 0 ; Pour chaque t : Si t ≥ 35 alors compteur ← compteur + 1. Résultat : <b>3 jours</b> (38, 41, 36).</p><p><b>d)</b> 242 ÷ 7 ≈ <b>34,6°</b>.</p>")}
{sol(15, "Tri à bulles", "<p><b>a)</b> Passage 2 : 3 1 5 8 — Passage 3 : 1 3 5 8 (un 4<sup>e</sup> passage confirme : aucun échange).</p><p><b>b)</b> 2 + 1 + 1 = <b>4 échanges</b>.</p><p><b>c)</b> 1. Aigles (61) — 2. Renards (57) — 3. Dragons (42) — 4. Krakens (38).</p>")}
{sol(16, "Le prix mystère", "<p>Milieux proposés : 350 (plus), 475 (moins), 412 (plus), 443 (moins), 427 (plus), 435 (plus), 439 (moins), <b>437</b> (gagné). <b>8 questions</b>.</p>")}
{sol(17, "Couper en deux", "<p>7 questions → 128 ; 10 questions → 1 024.</p><p><b>a)</b> <b>7</b> questions (2<sup>7</sup> = 128 ≥ 100). <b>b)</b> <b>20</b> questions. <b>c)</b> <b>33</b> questions (2<sup>33</sup> ≈ 8,6 milliards).</p>")}
</div>''', chapter=None, color="#16a34a")

add(f'''<h1 class="ptitle">✅ Corrigés (fin)</h1>
<div class="solcols">
{sol(18, "Le cinéma", "<p><b>a)</b> 6 € ; 10 € (12 n'est pas &lt; 12) ; 7 €.</p><p><b>b)</b> 6 + 10 + 10 + 7 = <b>33 €</b>.</p><p><b>c)</b> <span class='mono'>Fonction prix_mercredi(âge) : Retourner prix_billet(âge) - 2</span>.</p>")}
{sol(19, "La fonction mystère", "<p><b>a)</b> mystère(3) = 1+2+3 = <b>6</b> ; mystère(5) = <b>15</b>.</p><p><b>b)</b> Elle calcule la somme des entiers de 1 à n : on peut l'appeler <span class='mono'>somme_jusqu_a(n)</span>.</p><p><b>c)</b> 50 paires qui valent 101 : 50 × 101 = <b>5 050</b>.</p>")}
{sol(20, "À vélo", "<p><b>a)</b> 4 + 12 = <b>16 min</b>. <b>b)</b> 7 + 9 = <b>16 min</b>.</p><p><b>c)</b> M → G → P → S → C : 4 + 2 + 3 + 2 = <b>11 min</b>. Le chemin le plus court n'est pas toujours celui qui a le moins d'étapes !</p>")}
{sol(21, "La rumeur", "<p><b>a)</b> <b>Zoé</b> (4 amis : Yanis, Malo, Adam, Sarah).</p><p><b>b)</b> Par exemple Léa → Tom → Yanis → Zoé → Adam : <b>4 arêtes</b>.</p><p><b>c)</b> H1 : Tom, Inès — H2 : Yanis, Malo — H3 : Zoé, Sarah — H4 : Adam. <b>4 heures</b>.</p>")}
{sol(22, "Agents secrets", "<p><b>a)</b> BRAVO AGENT TU AS TROUVE.</p><p><b>b)</b> RENDEZ VOUS AU CDI A MIDI.</p><p><b>d)</b> 25 clés au maximum (la clé 26 redonne le message). Un ordinateur les teste en une fraction de seconde. (KHOOR = HELLO, clé 3.)</p>")}
{sol(23, "Mots de passe", "<p>soleil : 0 → Faible. Soleil2026 : 2 (chiffre, majuscule) → Moyen. jaimelefootetlespizzas : 1 (longueur) → Faible. Tortue-Volante-42! : 4 → <b>Fort</b>.</p><p class='small'>Remarque : une phrase de passe très longue reste difficile à deviner ; les règles des sites ne sont pas parfaites !</p>")}
{sol(24, "Force brute", "<p><b>a)</b> 10 000 combinaisons : trouvées en 0,00001 seconde !</p><p><b>b)</b> 209 secondes, soit environ <b>3 minutes 30</b>.</p><p><b>c)</b> Chaque caractère en plus multiplie le travail du pirate : la <b>longueur</b> et la variété des caractères sont nos meilleures armes.</p>")}
{sol(25, "Les fruits", "<p><b>a)</b> Par exemple : <i>Couleur ?</i> → verte : pastèque. Jaune → <i>Allongée ?</i> oui : banane, non : citron. Rouge → <i>Petite ?</i> oui : cerise, non : pomme.</p><p><b>b)</b> Il répond « citron » : il n'a jamais vu de melon dans ses exemples. Une IA ne connaît que ce qu'elle a appris !</p>")}
{sol(26, "Recommandation", "<p><b>a)</b> V1 : 1 — V2 : 2 — V3 : 0 — V4 : 3 — V5 : 1.</p><p><b>b)</b> V4, V2, puis V1 et V5 (égalité), puis V3.</p><p><b>c)</b> V3 : on ne voit plus que ce qu'on aime déjà, on s'enferme dans une « bulle ». <b>d)</b> Ex. : 1 vidéo sur 5 est choisie au hasard parmi d'autres thèmes.</p>")}
{sol("final", "Escape game", "<p>1 : 3 × 4 − 5 = <b>7</b>. 2 : 3 × 2 = <b>6</b>. 3 : 21 est impair et pas multiple de 5 → <b>9</b>. 4 : WURLV → TROIS → <b>3</b>.</p><p>Code : <b>7 6 9 3</b>. Bonus : passage 1 : 7 6 9 3 → 6 7 3 9 (2 échanges) ; passage 2 : → 6 3 7 9 (1) ; passage 3 : → 3 6 7 9 (1). <b>4 échanges</b>.</p>")}
</div>''', chapter=None, color="#16a34a")

# ---- DIPLÔME
add(f'''<div class="diploma"><div class="dip-in">
<div class="dip-top">{medal(110)}</div>
<div class="dip-t">DIPLÔME</div>
<div class="dip-s">de Maître·sse des Algorithmes</div>
<p>Ce diplôme est décerné à</p>
<div class="dip-name"></div>
<p>pour avoir relevé les défis d'<b>Algo'Aventures</b> avec logique, persévérance et créativité.</p>
<div class="dip-skills"><span>✔ Variables</span><span>✔ Conditions</span><span>✔ Boucles</span><span>✔ Listes</span><span>✔ Tris</span><span>✔ Dichotomie</span><span>✔ Fonctions</span><span>✔ Graphes</span><span>✔ Cryptographie</span><span>✔ IA</span></div>
<div class="dip-foot"><div>Date : ......................</div><div class="dip-robots">{bitou(w=70, pose="cheer")}{nova(w=70, pose="cheer", flip=True)}</div><div>Signé : Bitou &amp; Nova</div></div>
<p class="small">Mon score de défis réussis : ........ / 27</p>
</div></div>''', footer=False)

# ---- GLOSSAIRE
gl = [("Algorithme", "Suite d'instructions précises et ordonnées pour résoudre un problème."), ("Programme", "Algorithme écrit dans un langage informatique (Scratch, Python…)."),
      ("Variable", "« Boîte » qui porte un nom et contient une valeur qui peut changer."), ("Affectation (←)", "Instruction qui range une valeur dans une variable."),
      ("Condition", "Test qui est vrai ou faux et permet de choisir (Si… alors… sinon)."), ("Boucle", "Structure qui répète des instructions (Répéter, Pour, Tant que)."),
      ("Boucle infinie", "Boucle qui ne s'arrête jamais : c'est un bug !"), ("Liste", "Variable contenant plusieurs valeurs rangées par position."),
      ("Tri", "Ranger des éléments dans un ordre (croissant, alphabétique…)."), ("Dichotomie", "Méthode de recherche qui coupe en deux à chaque étape. Il faut une liste triée."),
      ("Fonction", "Morceau de programme nommé, réutilisable, avec des paramètres."), ("Paramètre", "Valeur donnée à une fonction quand on l'appelle."),
      ("Graphe", "Ensemble de sommets reliés par des arêtes."), ("Chiffrement", "Transformer un message pour qu'il soit illisible sans la clé."),
      ("Force brute", "Attaque qui essaie toutes les possibilités une par une."), ("Bug", "Erreur dans un programme. Le débogage, c'est la chasse aux bugs !"),
      ("Intelligence artificielle", "Programmes capables d'apprendre à partir d'exemples pour accomplir des tâches."), ("Biais", "Erreur d'une IA due à des exemples incomplets ou déséquilibrés.")]
add(f'''<h1 class="ptitle">📖 Petit dictionnaire de l'algo</h1>
<div class="gloss">{"".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in gl)}</div>
<div class="cols2">
{box("tip", "🚀 Pour aller plus loin", "<ul class='tight'><li><b>Scratch</b> : gratuit, en ligne, pour programmer avec des blocs.</li><li><b>Python</b> : installe-le avec un adulte, ou utilise un éditeur en ligne.</li><li>Participe aux concours d'informatique pour collégiens, comme le <b>concours Castor</b> et l'<b>Algoréa</b>.</li><li>Inscris-toi au club informatique ou de robotique de ton collège !</li></ul>")}
<div class="center">{bitou(w=100, pose="wave")}<p class="small"><b>Bitou :</b> « À bientôt pour de nouvelles aventures ! »</p></div>
</div>''', color="#6366F1")

# ---- 4e DE COUVERTURE
add(f'''<svg class="cover-bg" viewBox="0 0 600 840" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="cg2" x1="0" y1="1" x2="0.4" y2="0"><stop offset="0" stop-color="#312e81"/><stop offset=".55" stop-color="#6d28d9"/><stop offset="1" stop-color="#db2777"/></linearGradient></defs><rect width="600" height="840" fill="url(#cg2)"/>{stars_bg}</svg>
<div class="back">
<div class="back-title">Deviens un as de l'algorithmique… en t'amusant !</div>
<p class="back-lead">Comment un GPS trouve-t-il le chemin le plus court ? Comment une IA apprend-elle ? Combien de matchs compte la Coupe du monde 2026 ? Ton mot de passe résisterait-il à un robot pirate ?</p>
<p>Avec <b>Bitou</b> et <b>Nova</b>, deux robots attachants, découvre pas à pas toutes les notions d'algorithmique du collège grâce à <b>27 défis</b> inspirés de l'actualité : drones livreurs, canicules, trottinettes électriques, mission vers la Lune, réseaux sociaux, cybersécurité…</p>
<div class="back-grid">
<div>✔ 12 chapitres progressifs</div><div>✔ Leçons claires et illustrées</div><div>✔ Versions Scratch &amp; Python</div><div>✔ Corrigés détaillés</div><div>✔ Escape game final</div><div>✔ Diplôme à compléter</div></div>
<div class="back-art">{bitou(w=130, pose="wave")}{nova(w=130, pose="point", flip=True)}</div>
<div class="back-foot"><div class="age">11-15<br><small>ANS</small></div><div class="isbn"><div class="barcode">{"".join(f'<i style="width:{1+(i*7)%3}px"></i>' for i in range(46))}</div>ISBN <span class="ph2">[978-X-XXXX-XXXX-X]</span></div><div class="price">Prix : <span class="ph2">[XX,XX €]</span><br><small><span class="ph2">[Maison d'édition]</span></small></div></div>
</div>''', cls="cover-page", footer=False)

# ------------------------------------------------------------------ sommaire
som_items = "".join(f'<a class="som-it" style="--c:{C[n]}"><span class="som-n">{n if n < 13 else "★"}</span><span class="som-t">{TITLES[n]}</span><span class="som-dots"></span><span class="som-p">{CH[n]}</span></a>' for n in range(1, 14))
som_items += f'<a class="som-it" style="--c:#16a34a"><span class="som-n">✓</span><span class="som-t">Corrigés</span><span class="som-dots"></span><span class="som-p">{CORR_START}</span></a>'
som_items += f'<a class="som-it" style="--c:#EAB308"><span class="som-n">🏅</span><span class="som-t">Diplôme · Petit dictionnaire</span><span class="som-dots"></span><span class="som-p">{CORR_START+3}</span></a>'
themes = [("🛸", "Drones"), ("⚽", "Coupe du monde 2026"), ("🌡️", "Canicules"), ("♻️", "Tri des déchets"), ("🛴", "Trottinettes"), ("🌙", "Mission Lune"), ("🎧", "Playlists"), ("🎮", "E-sport"), ("🎬", "Cinéma"), ("🚲", "Vélo en ville"), ("📱", "Réseaux sociaux"), ("🔐", "Cybersécurité"), ("🤖", "IA"), ("📺", "Recommandations")]
PAGES[SOMMAIRE_IDX - 1]["body"] = f'''<h1 class="ptitle">Sommaire</h1>
<div class="som">{som_items}</div>
<h2 class="h2">Les thèmes d'actualité du livre</h2>
<div class="themes">{"".join(f"<span>{e} {t}</span>" for e, t in themes)}</div>
<div class="som-art">{drone(110)}{bitou(w=95, pose="point")}</div>'''
for p in PAGES:
    p["body"] = p["body"].replace("__CORR__", str(CORR_START))

# ------------------------------------------------------------------ CSS & assemble
CSS = FONTS + r"""
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#e5e7eb}
body{font-family:'Nunito',sans-serif;color:#1e1b4b;font-size:10.4pt;line-height:1.4}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff;page-break-after:always;break-after:page;margin:0 auto}
@media screen{.page{margin:10mm auto;box-shadow:0 4px 20px rgba(0,0,0,.15)}}
.content{position:absolute;inset:13mm 14mm 16mm 14mm;overflow:hidden}
.edge{position:absolute;top:0;bottom:0;width:5mm;background:var(--pc)}
.page.odd .edge{right:0}.page.even .edge{left:0}
.foot{position:absolute;bottom:6mm;left:14mm;right:14mm;display:flex;justify-content:space-between;align-items:center;font-family:Fredoka;font-size:9pt;color:#64748b}
.foot .pn{background:var(--pc);color:#fff;border-radius:99px;min-width:9mm;height:9mm;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:10.5pt}
.page.odd .foot{flex-direction:row-reverse}
p{margin:0 0 2.2mm}
h1,h2,h3{font-family:Fredoka;font-weight:600;margin:0}
.ptitle{font-size:24pt;color:#1e1b4b;margin-bottom:4mm}
.h2{font-size:14pt;color:var(--pc);margin:1mm 0 2mm}
.h3{font-size:12pt;margin:2mm 0 1.5mm;color:#334155}
.lead{font-size:11.5pt}
.small{font-size:9pt;color:#475569}
.center{text-align:center}
.mono{font-family:'JetBrains Mono',monospace;font-size:9.5pt;background:#f1f5f9;padding:0 1mm;border-radius:3px}
.big{font-size:11.5pt}
p.mono{background:none}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:5mm;align-items:start}
.cols2.ac{align-items:center}
.cols-t{display:grid;grid-template-columns:auto 1fr;gap:4mm;align-items:center}
.cols-pl{display:grid;grid-template-columns:1.35fr 1fr;gap:5mm;align-items:center}
.cols-cz{display:grid;grid-template-columns:1.15fr 1fr;gap:5mm;align-items:center}
ul.tight,ol.tight{margin:1mm 0 2mm;padding-left:5mm}
ul.tight li,ol.tight li{margin-bottom:.8mm}
/* banner */
.banner{display:flex;align-items:center;justify-content:space-between;background:var(--c);color:#fff;border-radius:6mm;padding:4mm 6mm;margin-bottom:4mm;position:relative;overflow:hidden;min-height:38mm}
.banner:before{content:"";position:absolute;right:-20mm;top:-25mm;width:70mm;height:70mm;border-radius:50%;background:rgba(255,255,255,.15)}
.banner:after{content:"";position:absolute;left:35%;bottom:-18mm;width:40mm;height:40mm;border-radius:50%;background:rgba(255,255,255,.1)}
.banner-n{font-family:Fredoka;font-weight:600;letter-spacing:2px;font-size:10pt;opacity:.9}
.banner h1{font-size:24pt;line-height:1.1;margin:1mm 0}
.banner-sub{font-size:11pt;font-weight:700;opacity:.95}
.banner-art{position:relative;z-index:1;flex-shrink:0;background:#fff;border-radius:50%;width:36mm;height:36mm;display:flex;align-items:center;justify-content:center;border:3px solid #1e1b4b}
.banner-art svg{max-width:30mm;max-height:31mm}
.banner-txt{position:relative;z-index:1}
/* boxes */
.box{border-radius:4mm;padding:3mm 4mm;margin:2mm 0 3mm;border:2px solid}
.box-t{font-family:Fredoka;font-weight:600;font-size:11pt;margin-bottom:1.2mm}
.box p:last-child{margin-bottom:0}
.box.tip{background:#f0fdf4;border-color:#86efac}.box.tip .box-t{color:#15803d}
.box.warn{background:#fff7ed;border-color:#fdba74}.box.warn .box-t{color:#c2410c}
.box.know{background:#f5f3ff;border-color:#c4b5fd}.box.know .box-t{color:#6d28d9}
.defi{border:2.5px solid var(--c);border-radius:5mm;margin:2mm 0 3mm;overflow:hidden;background:#fff}
.defi-h{background:var(--c);color:#fff;display:flex;align-items:center;gap:3mm;padding:1.8mm 4mm}
.defi-n{background:#fff;color:var(--c);font-family:Fredoka;font-weight:700;border-radius:99px;padding:.3mm 3mm;font-size:9.5pt}
.defi-title{font-family:Fredoka;font-weight:600;font-size:13pt;flex:1}
.stars{color:#fde047;font-size:13pt;letter-spacing:1px}.stars .off{color:rgba(255,255,255,.35)}
.defi-b{padding:3mm 4mm 2mm}
/* code */
.code{background:#0f172a;border-radius:3mm;margin:1.5mm 0 2.5mm;overflow:hidden;border-left:4px solid var(--pc)}
.code-title{background:#1e293b;color:#cbd5e1;font-family:Fredoka;font-size:9pt;padding:1mm 3mm}
.code pre{margin:0;padding:2.4mm 3.5mm;font-family:'JetBrains Mono',monospace;font-size:8.7pt;line-height:1.55;color:#e2e8f0;white-space:pre-wrap}
.code .kw{color:#f472b6;font-weight:700}.code .ar{color:#facc15;font-weight:700}.code .cm{color:#64748b;font-style:italic}.code .st{color:#86efac}
.py{background:#1e1b4b;border-radius:3mm;margin:1.5mm 0 2.5mm;overflow:hidden}
.py-title{background:#facc15;color:#1e1b4b;font-family:Fredoka;font-weight:600;font-size:9.5pt;padding:1mm 3mm}
.py pre{margin:0;padding:2.4mm 3.5mm;font-family:'JetBrains Mono',monospace;font-size:8.5pt;line-height:1.5;color:#e0e7ff;white-space:pre-wrap}
.py .kw{color:#7dd3fc;font-weight:700}.py .cm{color:#a5b4fc;font-style:italic}
/* scratch blocks */
.scratch{background:#f8fafc;border:2px dashed #cbd5e1;border-radius:3mm;padding:2mm 3mm 3mm;margin:1.5mm 0 2.5mm}
.scratch-t{font-family:Fredoka;font-weight:600;font-size:9.5pt;color:#64748b;margin-bottom:1.5mm}
.blk{display:inline-block;clear:both;float:left;color:#fff;font-weight:800;font-size:9pt;padding:1.3mm 3mm;border-radius:2mm;margin-bottom:.6mm;min-width:38mm;border:1.5px solid rgba(0,0,0,.2)}
.scratch:after{content:"";display:block;clear:both}
.blk u,.blk i{text-decoration:none;font-style:normal;background:#fff;color:#1e1b4b;border-radius:99px;padding:0 2mm;margin:0 .5mm}
.blk .op{background:rgba(0,0,0,.18);border-radius:99px;padding:0 2mm}
.cblock{padding:0;background:none!important;border:none}
.cblock .blk-top{padding:1.3mm 3mm;border-radius:2mm 2mm 2mm 0;border:1.5px solid rgba(0,0,0,.2)}
.cblock .blk-in{border-left:4mm solid;padding:.6mm 0 .1mm 0}
.cblock .blk-in:after{content:"";display:block;clear:both}
.cblock .blk-bot{height:3mm;border-radius:0 2mm 2mm 2mm;border:1.5px solid rgba(0,0,0,.2);border-top:none;width:20mm}
.c-ctrl .blk-top,.c-ctrl .blk-bot{background:#FFAB19}.c-ctrl .blk-in{border-color:#FFAB19}
.c-motion{background:#4C97FF}.c-look{background:#9966FF}.c-var{background:#FF8C1A}.c-event{background:#FFBF00;color:#1e1b4b;border-radius:5mm 5mm 2mm 2mm}
.c-pen{background:#0fBD8C}.c-myb{background:#FF6680;border-radius:5mm 5mm 2mm 2mm}
/* answers */
.ans{border-bottom:2px dotted #94a3b8;height:7mm;margin:0 0 1.5mm;display:flex;align-items:flex-end}
.ans span{font-size:8.5pt;color:#94a3b8;font-weight:700;padding-bottom:.6mm}
p .ans{display:inline-flex;width:70%;vertical-align:bottom;margin:0}
.trace{border-collapse:collapse;width:100%;margin:1mm 0 2.5mm;font-size:9.5pt}
.trace th{background:var(--pc);color:#fff;font-family:Fredoka;font-weight:500;padding:1.2mm 2mm;border:1.5px solid var(--pc)}
.trace td{border:1.5px solid #cbd5e1;padding:1.2mm 2mm;height:7mm;text-align:center}
.trace.wide td:first-child{text-align:left}
/* chapter 1 */
.chips{list-style:none;padding:0;margin:0;display:grid;gap:1.5mm}
.chips li{background:#eef2ff;border-radius:99px;padding:1.3mm 3.5mm;font-weight:700;font-size:9.5pt}
.order{display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin:2mm 0}
.order div{display:flex;align-items:center;gap:2.5mm;background:#eef2ff;border-radius:3mm;padding:2mm 3mm;font-weight:600;font-size:9.8pt}
.num{flex-shrink:0;width:8mm;height:8mm;border:2px dashed #6366f1;border-radius:50%;background:#fff}
.arrows{font-family:Fredoka;font-size:11pt;margin:2mm 0}
.arrows span{display:inline-flex;width:8mm;height:8mm;align-items:center;justify-content:center;background:#6366f1;color:#fff;border-radius:2mm;font-weight:700;margin:0 1mm 0 2mm}
.mini-art{text-align:right}
/* welcome */
.welcome{display:grid;grid-template-columns:1.1fr 1fr;gap:5mm;align-items:start}
.duo{display:grid;gap:3mm}
.card-perso{display:grid;grid-template-columns:auto 1fr;gap:3mm;align-items:center;background:#f8fafc;border-radius:4mm;padding:2.5mm 3mm;border:2px solid #e2e8f0}
.card-perso h3{font-size:15pt}.card-perso p{font-size:9.6pt;margin:0}
.legend{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3mm;margin-bottom:3mm}
.legend div{font-size:9.5pt;background:#f8fafc;border-radius:3mm;padding:2.5mm 3mm;border:1.5px solid #e2e8f0}
.lg{display:inline-flex;width:9mm;height:9mm;border-radius:2.5mm;align-items:center;justify-content:center;margin-right:2mm;font-size:12pt;vertical-align:middle;margin-bottom:1mm}
/* shapes */
.shapes{display:flex;justify-content:space-between;gap:2mm;margin:2mm 0}
.shapes figure{margin:0;text-align:center}
.shapes figcaption{font-size:8.6pt;margin-top:1mm;line-height:1.3}
/* moon */
.moon-head{text-align:center;margin-bottom:2mm}
.moon-head svg{width:100%;height:auto;max-height:62mm}
/* sorting */
.selgrid{display:grid;grid-template-columns:1fr;gap:1mm;margin:2mm 0}
.selrow{display:grid;grid-template-columns:56mm 1fr;gap:4mm;align-items:center;background:#f5f3ff;border-radius:3mm;padding:1.5mm 3mm}
.selrow svg{height:20mm;width:auto}
.selrow p{margin:0;font-weight:700;font-size:10pt}
.bubble-steps div{margin-bottom:1.2mm;font-size:9.8pt}
.bubble-steps .hl{background:#fde047;border-radius:2px;padding:0 1mm}
/* say bubble */
.say{display:flex;align-items:center;gap:2mm;margin:2mm 0}
.say.right{justify-content:flex-end}
.say-b{background:#f1f5f9;border-radius:4mm;padding:2.5mm 3.5mm;font-size:9.8pt;position:relative;max-width:62mm;border:2px solid #cbd5e1}
/* crypto */
.secret{background:#0f172a!important;color:#4ade80;padding:2mm 3mm!important;border-radius:2mm;letter-spacing:2px;text-align:center}
/* IA */
.drawbox{height:34mm;border:2px dashed #d8b4fe;border-radius:3mm;margin-bottom:2mm;background:repeating-linear-gradient(0deg,#fff,#fff 4.8mm,#faf5ff 4.8mm,#faf5ff 5mm)}
.vgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm;margin:3mm 0}
.vcard{background:#f8fafc;border-radius:3mm;border:1.5px solid #e2e8f0;overflow:hidden;font-size:8.6pt;padding-bottom:1.5mm}
.vcard b{display:block;padding:1.2mm 2mm .6mm;line-height:1.2}
.vcard>div:last-child{padding:0 1.5mm}
.vthumb{height:18mm;display:flex;align-items:center;justify-content:center;position:relative;font-size:20pt}
.vthumb i{position:absolute;right:1.5mm;bottom:1mm;font-style:normal;color:#fff;font-size:9pt;background:rgba(0,0,0,.4);border-radius:99px;padding:0 1.5mm}
.tag{display:inline-block;background:#fae8ff;color:#a21caf;border-radius:99px;padding:0 1.6mm;font-weight:800;font-size:8pt;margin:.4mm .4mm 0 0}
.tag.big{font-size:10pt;padding:.4mm 2.5mm}
/* final */
.final-head{display:grid;grid-template-columns:auto 1fr;gap:5mm;align-items:center;background:linear-gradient(135deg,#fef9c3,#fde68a);border-radius:5mm;padding:4mm 5mm;margin-bottom:4mm;border:2.5px solid #eab308}
.escape{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}
.eg{display:grid;grid-template-columns:auto 1fr;gap:3mm;border:2.5px solid #eab308;border-radius:4mm;padding:3mm;background:#fffbeb}
.eg-n{width:10mm;height:10mm;border-radius:50%;background:#eab308;color:#fff;font-family:Fredoka;font-weight:700;font-size:15pt;display:flex;align-items:center;justify-content:center}
.eg p{margin:1mm 0 0}
.digit{display:inline-block;width:9mm;height:11mm;border:2.5px solid #1e1b4b;border-radius:2mm;background:#fff;vertical-align:middle}
.digit.big{width:14mm;height:17mm;margin:0 1.5mm;border-width:3px}
.finalcode{display:flex;align-items:center;justify-content:center;background:#1e1b4b;color:#fde047;font-family:Fredoka;font-weight:700;font-size:16pt;border-radius:5mm;padding:4mm;margin:4mm 0 2mm;gap:2mm}
.finalcode span:first-child{margin-right:4mm}
/* solutions */
.solcols{column-count:2;column-gap:5mm}
.sol{break-inside:avoid;border:1.5px solid #bbf7d0;background:#f0fdf4;border-radius:3mm;padding:2.2mm 3mm;margin-bottom:3mm;font-size:9.4pt}
.sol p{margin-bottom:1.2mm}.sol p:last-child{margin-bottom:0}
.sol-h{font-family:Fredoka;font-weight:600;font-size:11pt;color:#15803d;margin-bottom:1mm}
.sol-h span{background:#16a34a;color:#fff;border-radius:99px;padding:0 2.5mm;font-size:9pt;margin-right:1mm}
/* sommaire */
.som{display:grid;gap:2mm;margin-bottom:5mm}
.som-it{display:flex;align-items:center;gap:3mm;font-size:12.5pt;font-weight:700}
.som-n{width:10mm;height:10mm;border-radius:3mm;background:var(--c);color:#fff;display:flex;align-items:center;justify-content:center;font-family:Fredoka;font-weight:600;font-size:12pt;flex-shrink:0}
.som-dots{flex:1;border-bottom:2.5px dotted #cbd5e1;margin:0 1mm 1.5mm}
.som-p{font-family:Fredoka;font-weight:600;color:var(--c);font-size:13pt;min-width:8mm;text-align:right}
.themes{display:flex;flex-wrap:wrap;gap:2mm}
.themes span{background:#eef2ff;border-radius:99px;padding:1.2mm 3.5mm;font-weight:700;font-size:9.8pt}
.som-art{position:absolute;bottom:0;right:0;display:flex;align-items:flex-end;gap:4mm}
/* glossaire */
.gloss{display:grid;grid-template-columns:1fr 1fr;gap:2mm 5mm;margin-bottom:4mm}
.gloss div{border-left:4px solid #6366f1;padding:1mm 0 1mm 3mm;font-size:9.6pt}
.gloss b{display:block;font-family:Fredoka;font-weight:600;font-size:11pt;color:#4338ca}
/* title page */
.titlepage{text-align:center;padding-top:10mm}
.tp-robots{display:flex;justify-content:center;gap:8mm;margin-bottom:4mm}
.tp-title{font-size:40pt;color:#4338ca}
.tp-sub{font-size:14pt;font-weight:700;color:#475569;margin:2mm 0 4mm}
.tp-lvl{display:inline-block;background:#eef2ff;border-radius:99px;padding:1.5mm 6mm;font-family:Fredoka;font-weight:500;color:#4338ca;margin-bottom:8mm}
.tp-author{font-size:11pt;margin-bottom:22mm}
.legal{text-align:left;font-size:8.4pt;color:#475569;border-top:1.5px solid #e2e8f0;padding-top:4mm}
.legal p{margin-bottom:1.6mm}
.ph{background:#fef08a;padding:0 1mm;border-radius:2px;color:#713f12}
.ph2{background:rgba(254,240,138,.25);padding:0 1mm;border-radius:2px}
/* cover */
.cover-page .content{inset:0}
.cover-bg{position:absolute;inset:0;width:100%;height:100%}
.cover{position:absolute;inset:0;padding:16mm 14mm;color:#fff;text-align:center}
.cover-top{display:inline-block;font-family:Fredoka;font-weight:600;letter-spacing:2px;font-size:10.5pt;background:rgba(255,255,255,.15);border:1.5px solid rgba(255,255,255,.4);border-radius:99px;padding:1.5mm 5mm}
.cover-title{font-family:Fredoka;font-weight:700;font-size:64pt;line-height:1;margin-top:9mm;text-shadow:0 1.5mm 0 #1e1b4b;color:#fde047;letter-spacing:-1px}
.cover-title span{color:#f472b6}
.cover-sub{font-family:Fredoka;font-weight:500;font-size:17pt;margin-top:4mm}
.cover-chips{display:flex;flex-wrap:wrap;justify-content:center;gap:2mm;margin:6mm 8mm 0}
.cover-chips span{background:#fff;color:#1e1b4b;border-radius:99px;padding:1.2mm 3.5mm;font-weight:800;font-size:9.5pt}
.cover-art{position:absolute;left:0;right:0;bottom:28mm;height:150mm}
.ca-bitou{position:absolute;left:22mm;bottom:0}
.ca-nova{position:absolute;right:18mm;bottom:0}
.ca-drone{position:absolute;left:16mm;top:6mm;transform:rotate(-8deg)}
.ca-rocket{position:absolute;right:26mm;top:-2mm;transform:rotate(14deg)}
.ca-ball{position:absolute;left:100mm;bottom:4mm}
.ca-code{position:absolute;left:76mm;top:22mm;font-family:'JetBrains Mono';font-size:9pt;text-align:left;background:#0f172a;color:#4ade80;border-radius:3mm;padding:2mm 3mm;border:2px solid #fde047;transform:rotate(-4deg)}
.cover-bottom{position:absolute;left:14mm;right:14mm;bottom:12mm;font-size:11pt;background:rgba(15,23,42,.55);border-radius:4mm;padding:3mm 4mm}
/* back cover */
.back{position:absolute;inset:0;padding:20mm 18mm;color:#fff}
.back-title{font-family:Fredoka;font-weight:700;font-size:24pt;color:#fde047;line-height:1.15;margin-bottom:5mm}
.back-lead{font-size:13pt;font-weight:700;margin-bottom:4mm}
.back p{font-size:11.5pt}
.back-grid{display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin:5mm 0}
.back-grid div{background:rgba(255,255,255,.14);border-radius:3mm;padding:2mm 3mm;font-weight:800}
.back-art{display:flex;justify-content:center;gap:10mm}
.back-foot{position:absolute;left:18mm;right:18mm;bottom:16mm;display:flex;justify-content:space-between;align-items:flex-end}
.age{background:#fde047;color:#1e1b4b;border-radius:50%;width:22mm;height:22mm;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Fredoka;font-weight:700;font-size:14pt;line-height:1}
.age small{font-size:8pt}
.isbn{background:#fff;color:#1e1b4b;padding:3mm 4mm 2mm;border-radius:2mm;font-size:8pt;text-align:center;font-family:'JetBrains Mono'}
.barcode{display:flex;gap:1.2px;height:16mm;margin-bottom:1mm;justify-content:center}
.barcode i{background:#1e1b4b;display:block}
.price{text-align:right;font-weight:800}
/* diploma */
.diploma{position:absolute;inset:0;padding:6mm;background:linear-gradient(135deg,#fef3c7,#fde68a)}
.dip-in{height:100%;border:3mm double #b45309;border-radius:6mm;background:#fffbeb;text-align:center;padding:10mm 16mm;position:relative}
.dip-t{font-family:Fredoka;font-weight:700;font-size:46pt;color:#b45309;letter-spacing:6px;margin-top:2mm}
.dip-s{font-family:Fredoka;font-weight:500;font-size:19pt;color:#4338ca;margin-bottom:8mm}
.diploma p{font-size:12.5pt}
.dip-name{border-bottom:2.5px dashed #b45309;width:70%;height:16mm;margin:2mm auto 6mm}
.dip-skills{display:flex;flex-wrap:wrap;gap:2mm;justify-content:center;margin:8mm 6mm}
.dip-skills span{background:#fff;border:2px solid #fbbf24;border-radius:99px;padding:1mm 3.5mm;font-weight:800;font-size:10pt;color:#92400e}
.dip-foot{display:flex;justify-content:space-between;align-items:flex-end;margin:10mm 4mm 6mm;font-weight:700}
.dip-robots{display:flex;gap:2mm}
"""

out = []
for i, p in enumerate(PAGES, 1):
    side = "odd" if i % 2 else "even"
    ch = p["chapter"]
    foot = ""
    if p["footer"]:
        label = f"Chapitre {ch} · {TITLES[ch]}" if ch and ch < 13 else (TITLES[13] if ch == 13 else "Algo'Aventures")
        foot = f'<div class="foot"><span class="pn">{i}</span><span>{label}</span></div>'
    edge = '<div class="edge"></div>' if p["footer"] else ""
    out.append(f'<section class="page {side} {p["cls"]}" style="--pc:{p["color"]}">{edge}<div class="content">{p["body"]}</div>{foot}</section>')

doc = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Algo'Aventures</title><style>{CSS}</style></head><body>{"".join(out)}</body></html>'''
open(os.path.join(HERE, "algo-aventures.html"), "w", encoding="utf-8").write(doc)
print("pages:", len(PAGES), "corr:", CORR_START, "chapters:", CH)
