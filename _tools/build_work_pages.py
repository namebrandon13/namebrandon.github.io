"""Generates the case-study pages in work/ from the PAGES data below.

Every fact here comes from Brandon's CV (data/build_master_cv.py, Brandon Rodrigues Games.pdf) or his own
itch.io pages. Edit the text here, then run:  python _tools/build_work_pages.py
Jekyll ignores folders starting with "_", so this script is not published on GitHub Pages.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://namebrandon13.github.io/namebrandon.github.io/"

# body: list of (heading, [paragraph or ("ul", [items])])
PAGES = [
    {
        "slug": "coach-number-11",
        "title": "Coach Number 11",
        "lede": "An observation-horror puzzle on a train. Every coach looks the same, until one doesn't.",
        "spec": [("engine", "Unreal Engine"), ("genre", "Horror puzzle"), ("platform", "Windows"),
                 ("status", "Prototype, still in development"),
                 ("play", '<a href="https://name-brandon.itch.io/coach-number-11" target="_blank" rel="noopener">name-brandon.itch.io/coach-number-11 ↗</a>')],
        "body": [
            ("The idea", [
                "You're trying to reach coach number 11. In each coach you look around carefully and decide: is this "
                "the same coach as the last one, or has something changed? Get it right and you move forward.",
                "It's inspired by P.T., Observation Duty and The Exit 8, games where the scare comes from noticing "
                "something small is wrong, rather than from something jumping out at you.",
            ]),
            ("What's in the build", [
                ("ul", [
                    "Sleeper-coach interiors in Unreal Engine (screenshots below)",
                    "The same-or-changed loop: inspect a coach, make the call, move on",
                    "A playable Windows build on itch.io",
                ]),
            ]),
            ("What's next", [
                "It's a prototype and I'm still working on it. Next up are new anomalies (defects), more features and "
                "more gameplay elements.",
            ]),
        ],
        "gallery": [("coach1", "the sleeper coach"), ("coach2", "the doorway between coaches"), ("coach3", "down the aisle")],
        "side": "it's free on itch: go and see if you can spot the changes",
    },
    {
        "slug": "vr-rage-room",
        "title": "VR Rage Room",
        "lede": "My MSc dissertation: a room full of things to smash, in VR or on a flat screen, built to study how people respond.",
        "spec": [("engine", "Unity"), ("platform", "VR headset and flatscreen (dual mode)"),
                 ("context", "MSc Computer Games Technology dissertation, City St George's, University of London"),
                 ("year", "2024")],
        "body": [
            ("The idea", [
                "A rage room simulation you can play in VR or on a normal screen. The point wasn't only to make breaking "
                "things feel good: it was a research tool for analysing people's emotional responses, so the same "
                "experience had to work in both modes and record what players did.",
            ]),
            ("What I built", [
                ("ul", [
                    "Real-time destruction: procedural destruction plus soft-body physics, so objects deform and break",
                    "A VR input loop that responds to the player's real-time motion, with physics-based feedback",
                    "A flatscreen mode running the same simulation, for comparison",
                    "A UX testing framework, with gameplay-data analysis of each session",
                ]),
            ]),
            ("The hard part: frame rate", [
                "Physics-heavy scenes and VR don't get along. Dropped frames in a headset are uncomfortable, so the target "
                "was a stable 90 FPS. I got there on mid-tier hardware through custom collision mesh design.",
            ]),
            ("How it turned out", [
                "The project was part of an MSc I finished with a Distinction (71.53%). Holding VR scenes at 90 FPS is now "
                "part of my job at Candela.",
            ]),
        ],
        "gallery": [],
        "side": "screenshots and a capture of this are on my list to add",
    },
    {
        "slug": "cosmic-chaos",
        "title": "Cosmic Chaos",
        "lede": "A fast arcade space game: dodge, weave, grab the energy cores, survive the next wave.",
        "spec": [("engine", "Unity"), ("genre", "Arcade shooter"), ("platform", "Windows and Linux"),
                 ("context", "Academic project"), ("status", "Released"),
                 ("play", '<a href="https://name-brandon.itch.io/cosmic-chaos" target="_blank" rel="noopener">name-brandon.itch.io/cosmic-chaos ↗</a>')],
        "body": [
            ("The idea", [
                "A short, replayable arcade game about tight movement and quick reactions. You fly through an "
                "obstacle-filled patch of space, avoid enemies and collect energy cores.",
            ]),
            ("What I built", [
                ("ul", [
                    "Real-time physics for movement and collisions",
                    "Wave-based enemy spawners that set the pace of each run",
                    "Object pooling, so spawning lots of enemies and hazards doesn't cause hitches",
                    "Procedurally generated hazards, so each run plays out differently",
                    "A HUD with a timer and energy bar, and a pause menu",
                ]),
            ]),
            ("What I focused on", [
                "System design, tuning the player feedback, gameplay pacing through the wave-based enemy logic, "
                "and performance.",
            ]),
        ],
        "gallery": [("cosmic1", "gameplay"), ("cosmic2", "a busier moment"), ("cosmic3", "pause menu")],
        "side": "it's free on itch for Windows and Linux",
        "honest": "The itch.io page marks this game as AI-assisted for code.",
    },
    {
        "slug": "one-more-lesson",
        "title": "One More Lesson",
        "lede": "A friendly 1994 tutor program that teaches you the command line, and won't let you leave.",
        "spec": [("engine", "Godot 4"), ("genre", "Text-based, fourth-wall-breaking horror mystery"), ("platform", "Windows"),
                 ("status", "Prototype / proof of concept"), ("released", "2026"),
                 ("play", '<a href="https://name-brandon.itch.io/one-more-lesson" target="_blank" rel="noopener">name-brandon.itch.io/one-more-lesson ↗</a>')],
        "body": [
            ("The idea", [
                "TUTOR.EXE is a cheerful program called Shellby that teaches you the command line using real commands, "
                "in real folders on your PC. It was built to keep students engaged. It never let the last four leave.",
                "Their logs are still on the disk, half erased. You find out what happened to them, and use everything "
                "Shellby taught you to get out.",
            ]),
            ("What's in it", [
                ("ul", [
                    "Notepad and File Explorer open on their own, and the window and your mouse fight back",
                    "A tutor that notices when you look away",
                    "You actually learn the command line while playing",
                    "It only touches its own folder next to the .exe",
                ]),
            ]),
            ("How I made it", [
                "This one was an experiment in a different way of working: I built it with Claude as an AI pair "
                "programmer in Godot 4. It's a proof of concept and I'd welcome feedback. The itch.io page discloses "
                "AI assistance for code, graphics, sounds and text.",
            ]),
        ],
        "gallery": [("oml", "title screen")],
        "side": "heads-up: it reopens itself if you close it. Task Manager gets you out",
    },
]

HEAD = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Brandon Rodrigues</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#f3eee3">
<link rel="canonical" href="{site}work/{slug}.html">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<meta property="og:type" content="article">
<meta property="og:title" content="{title} · Brandon Rodrigues">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}work/{slug}.html">
<meta property="og:image" content="{site}{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,700;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/notebook.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap top__inner">
    <a class="sig" href="../">brandon rodrigues</a>
    <nav aria-label="Main">
      <a href="../#work">work</a>
      <a class="hide-sm" href="../#experience">experience</a>
      <a href="../#contact">contact</a>
      <a class="cv" href="../assets/cv/Brandon_Rodrigues_CV.pdf" target="_blank" rel="noopener">CV</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="foot">
  <div class="wrap"><span>© <span class="year">2026</span> Brandon Rodrigues</span><span><a href="mailto:brandon13111998@gmail.com">brandon13111998@gmail.com</a></span></div>
</footer>
<dialog class="lightbox" aria-label="Image viewer">
  <button class="lightbox__close" aria-label="Close">✕</button>
  <button class="lightbox__nav lightbox__prev" aria-label="Previous">‹</button>
  <figure class="lightbox__stage"></figure>
  <button class="lightbox__nav lightbox__next" aria-label="Next">›</button>
</dialog>
<script src="../assets/js/main.js" defer></script>
</body>
</html>
"""

RAGE_SKETCH = (ROOT / "index.html").read_text(encoding="utf-8").split('<div class="sketch">', 1)[1].split("</div>", 1)[0]


def render_block(block):
    if isinstance(block, tuple) and block[0] == "ul":
        return "<ul>" + "".join(f"<li>{escape(i)}</li>" for i in block[1]) + "</ul>"
    return f"<p>{escape(block)}</p>"


def build(i, page):
    prev_p = PAGES[i - 1]
    next_p = PAGES[(i + 1) % len(PAGES)]
    og = f"assets/img/{page['gallery'][0][0]}.webp" if page["gallery"] else "assets/img/og.jpg"
    out = [HEAD.format(title=escape(page["title"]), desc=escape(page["lede"]), site=SITE, slug=page["slug"], og=og)]
    out.append('<div class="wrap">')
    out.append('<header class="cs-head"><a class="back" href="../#work">← all work</a>')
    out.append(f"<h1>{escape(page['title'])}</h1><p class='lede'>{escape(page['lede'])}</p>")
    out.append("<dl class='spec'>" + "".join(f"<dt>{escape(k)}</dt><dd>{v}</dd>" for k, v in page["spec"]) + "</dl></header>")

    out.append("<div class='cs-body'><article>")
    for heading, blocks in page["body"]:
        out.append(f"<h2>{escape(heading)}</h2>" + "".join(render_block(b) for b in blocks))
    if page.get("honest"):
        out.append(f"<p class='honest'>{escape(page['honest'])}</p>")
    out.append("</article><aside class='cs-side'>")
    out.append(f"<p class='hand'>{escape(page['side'])}</p>")
    if page["gallery"]:
        key, cap = page["gallery"][0]
        out.append(f"<button class='entry__media' data-lb='g' data-src='../assets/img/{key}.webp' data-caption='{escape(cap)}'>"
                   f"<figure class='taped tilt-r'><img src='../assets/img/{key}-sm.webp' alt='{escape(page['title'])}: {escape(cap)}' loading='lazy'>"
                   f"<figcaption>{escape(cap)}</figcaption></figure></button>")
    else:
        out.append(f"<figure class='taped tilt-r'><div class='sketch'>{RAGE_SKETCH}</div><figcaption>how it fits together</figcaption></figure>")
    out.append("</aside></div>")

    if len(page["gallery"]) > 1:
        out.append("<h2 class='label' style='margin-top:30px'>screenshots</h2><div class='cs-gallery'>")
        for n, (key, cap) in enumerate(page["gallery"][1:], start=1):
            tilt = "tilt-l" if n % 2 else "tilt-r"
            out.append(f"<button data-lb='g' data-src='../assets/img/{key}.webp' data-caption='{escape(cap)}'>"
                       f"<figure class='taped {tilt}'><img src='../assets/img/{key}-sm.webp' alt='{escape(page['title'])}: {escape(cap)}' loading='lazy'>"
                       f"<figcaption>{escape(cap)}</figcaption></figure></button>")
        out.append("</div>")

    out.append(f"<nav class='cs-next' aria-label='More projects'><a href='{prev_p['slug']}.html'>← {escape(prev_p['title'])}</a>"
               f"<a href='{next_p['slug']}.html'>{escape(next_p['title'])} →</a></nav>")
    out.append("</div>")
    out.append(FOOT)
    (ROOT / "work" / f"{page['slug']}.html").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "work").mkdir(exist_ok=True)
    for i, p in enumerate(PAGES):
        build(i, p)
        print("work/" + p["slug"] + ".html")
