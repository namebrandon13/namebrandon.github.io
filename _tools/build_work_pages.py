"""Generates the case-study pages in work/ from the PAGES data below.

Every fact here comes from Brandon's CV (data/build_master_cv.py, Brandon Rodrigues Games.pdf) or his own
itch.io pages. Edit the text here, then run:  python _tools/build_work_pages.py
Jekyll ignores folders starting with "_", so this script is not published on GitHub Pages.
"""
import hashlib
import re
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
        "spec": [("my role", "Solo: concept, design, level layout, programming and every 3D model (made in Blender)"),
                 ("engine", "Unreal Engine"), ("genre", "Horror puzzle"), ("platform", "Windows"),
                 ("status", "Prototype, still in development"),
                 ("play", '<a href="https://name-brandon.itch.io/coach-number-11" target="_blank" rel="noopener">name-brandon.itch.io/coach-number-11 ↗</a>')],
        "body": [
            ("The idea", [
                "You're trying to reach coach number 11. In each coach you look around carefully and decide: is this "
                "the same coach as the last one, or has something changed? Get it right and you move forward.",
                "The concept came from Shinkansen 0 and The Exit 8, games where the scare comes from noticing "
                "something small is wrong, rather than from something jumping out at you. I set mine in an Indian "
                "railway sleeper coach.",
            ]),
            ("What I built", [
                ("ul", [
                    "Every 3D model in the game, made in Blender: the coaches, bunks, fittings and props",
                    "The level layout, and the same-or-changed loop: inspect a coach, make the call, move on",
                    "AI behaviour and the gameplay code in Unreal Engine",
                    "A playable Windows build on itch.io",
                ]),
            ]),
            ("The hardest part", [
                "The anomalies. I was designing them while I was building the game, so every new idea meant going back "
                "into code I'd already written. There was a lot of back and forth.",
            ]),
            ("What I'd do differently", [
                "Design the full list of anomalies before writing any code. Knowing every change the game needs to make "
                "up front would let me build the systems for them once, and keep development smooth.",
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
        "lede": "My MSc dissertation: a room full of things to smash, in VR or on a flat screen, built to compare how people feel after each.",
        "spec": [("my role", "Solo: design, programming, testing and every 3D model (made in Blender)"),
                 ("engine", "Unity, with the XR Interaction Toolkit"), ("platform", "VR headset and flatscreen (dual mode)"),
                 ("context", "MSc Computer Games Technology dissertation, City St George's, University of London"),
                 ("playtest", "8 players, each played both versions"),
                 ("year", "2024")],
        "body": [
            ("The idea", [
                "A rage room simulation you can play in VR or on a normal screen. The point wasn't only to make breaking "
                "things feel good: it was a research tool. The question was whether VR changes how people feel after "
                "letting off steam, and whether better physics makes a difference, so the same room had to work in both modes.",
                "Before building anything I looked at how real rage rooms are set up: what people smash, what they smash it "
                "with, and the axe-throwing lanes that often sit next door. That turned into a hand-drawn floor plan with six zones.",
            ]),
            ("The room", [
                ("ul", [
                    "Break Zone: pick up plates and glasses and throw them onto the spiked mat, or smash them with a hammer",
                    "Punching bag: a soft-body bag in the middle of the room that dents when you hit it",
                    "Knockdown: throw balls at a stack of breakable boxes",
                    "Axe Throw: aim for the bullseye",
                    "Ice Sculpting: slice things in two with a sword, or trim the edges with a chipper",
                    "Chaos zone: breakable and soft-body objects all together, to do as you please",
                ]),
                "Before the main room there's a small demo room for learning the controls. When you're ready, you slot a cube "
                "into the 'Provide Key' socket and the wall opens.",
            ]),
            ("What I built", [
                ("ul", [
                    "Slicing: the sword cuts an object in two along the line of your swing. I added a minimum-volume check so "
                    "pieces can't be cut forever, and wrote the chipper, which only trims small slivers when you move slowly",
                    "Soft bodies: the punching bag, plus a sloped object that acts like a trampoline when you toss plates onto it. "
                    "I added impact sound that gets louder and changes pitch the harder it's dented",
                    "Fracture: plates, glasses and blocks break into chunks when they're hit hard enough",
                    "A flat-screen version of the same room, with keyboard and mouse controls and swing animations for the hammer and sword",
                    "Every 3D model in the room, kept low-poly and made in Blender",
                    "The playtest: questionnaires and screen recordings for both versions",
                ]),
            ]),
            ("The hardest part: getting the physics right", [
                "Making things deform and break convincingly was the hardest part, and it all had to run in VR. Dropped "
                "frames in a headset are uncomfortable, so the target was a stable 90 FPS. I got there on mid-tier "
                "hardware through custom collision mesh design.",
                "Lighting mattered too. I swapped 14 real-time point lights for over 20 baked area lights, tuned Unity's "
                "physics settings and put objects on collision layers so things only collide with what they should.",
            ]),
            ("What I'd do differently", [
                "Split it into different rooms, each built around a different kind of physics, instead of having one "
                "room handle everything. Each room could then be tuned on its own.",
                "I'd also merge the physics scripts. Slicing, soft bodies and fracture are three separate systems, so a "
                "sliced object can't then shatter. Players noticed the game could still stutter when lots of things broke "
                "at once, and one asked to be able to smash plates against each other.",
            ]),
            ("How it turned out", [
                "Eight people played both versions. VR scored 4.38 out of 5 overall, ahead of the flat screen, and seven "
                "of the eight spent longer in VR. Slicing was the favourite. The axe throw turned out too hard: one player "
                "kept fetching the axes for another go.",
                "The project was part of an MSc I finished with a Distinction (71.53%). Holding VR scenes at 90 FPS is now "
                "part of my job at Candela.",
            ]),
        ],
        "honest": "The slicing, soft-body and fracture code started from open-source work (the EzySlice library and a "
                  "Valem tutorial, Unity-SoftBody-physics, and Unity Libre Fracture). My part was adapting and extending "
                  "it and building the game around it.",
        "gallery": [("vr-final3", "the punching bag, with the Chaos zone behind"),
                    ("vr-final2", "Knockdown"),
                    ("vr-final4", "the Break Zone, from the Chaos zone"),
                    ("vr-final5", "Axe Throw"),
                    ("vr-final1", "the demo room")],
        "process": [
            ("1 · on paper", [("vr-sketch-plan", "the first floor plan: six zones"),
                              ("vr-sketch-3d", "the same room, sketched in 3D")]),
            ("2 · Blender blockout", [("vr-blockout1", "Knockdown, still an empty table"),
                                      ("vr-blockout2", "the punching bag, with the Chaos zone behind"),
                                      ("vr-blockout3", "the Break Zone mat and Ice Sculpting"),
                                      ("vr-blockout4", "the way to Axe Throw")]),
            ("3 · final build in Unity", [("vr-final3", "the punching bag, now pink and squishy"),
                                          ("vr-final4", "Break Zone and the Chaos zone, filled in")]),
        ],
        "side": "it started as a pencil floor plan. the whole journey from sketch to build is further down",
    },
    {
        "slug": "cosmic-chaos",
        "title": "Cosmic Chaos",
        "lede": "A fast arcade space game: dodge, weave, grab the energy cores, survive the next wave.",
        "spec": [("my role", "Solo"), ("engine", "Unity"), ("genre", "Arcade shooter"), ("platform", "Windows and Linux"),
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
        "spec": [("my role", "Solo, with Claude as an AI pair programmer"), ("engine", "Godot 4"), ("genre", "Text-based, fourth-wall-breaking horror mystery"), ("platform", "Windows"),
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
<link rel="stylesheet" href="../assets/css/notebook.css?v={css_v}">
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
<script src="../assets/js/main.js?v={js_v}" defer></script>
</body>
</html>
"""

def _short_hash(path):
    return hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]


# Cache-busting: ?v=<hash of the file> changes whenever the CSS/JS changes, so browsers never mix old and new files
CSS_V = _short_hash("assets/css/notebook.css")
JS_V = _short_hash("assets/js/main.js")


def stamp_index():
    idx = ROOT / "index.html"
    t = idx.read_text(encoding="utf-8")
    t = re.sub(r'assets/css/notebook\.css(\?v=[0-9a-f]+)?"', f'assets/css/notebook.css?v={CSS_V}"', t)
    t = re.sub(r'assets/js/main\.js(\?v=[0-9a-f]+)?"', f'assets/js/main.js?v={JS_V}"', t)
    idx.write_text(t, encoding="utf-8")




def render_block(block):
    if isinstance(block, tuple) and block[0] == "ul":
        return "<ul>" + "".join(f"<li>{escape(i)}</li>" for i in block[1]) + "</ul>"
    return f"<p>{escape(block)}</p>"


def build(i, page):
    prev_p = PAGES[i - 1]
    next_p = PAGES[(i + 1) % len(PAGES)]
    og = f"assets/img/{page['gallery'][0][0]}.webp" if page["gallery"] else "assets/img/og.jpg"
    out = [HEAD.format(css_v=CSS_V, title=escape(page["title"]), desc=escape(page["lede"]), site=SITE, slug=page["slug"], og=og)]
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
    out.append("</aside></div>")

    if len(page["gallery"]) > 1:
        out.append("<h2 class='label' style='margin-top:30px'>screenshots</h2><div class='cs-gallery'>")
        for n, (key, cap) in enumerate(page["gallery"][1:], start=1):
            tilt = "tilt-l" if n % 2 else "tilt-r"
            out.append(f"<button data-lb='g' data-src='../assets/img/{key}.webp' data-caption='{escape(cap)}'>"
                       f"<figure class='taped {tilt}'><img src='../assets/img/{key}-sm.webp' alt='{escape(page['title'])}: {escape(cap)}' loading='lazy'>"
                       f"<figcaption>{escape(cap)}</figcaption></figure></button>")
        out.append("</div>")

    if page.get("process"):
        out.append("<section class='cs-process' aria-labelledby='process-h'><h2 class='label' id='process-h'>from sketch to build</h2>")
        for stage, shots in page["process"]:
            out.append(f"<h3 class='hand'>{escape(stage)}</h3><div class='cs-gallery'>")
            for n, (key, cap) in enumerate(shots):
                tilt = "tilt-l" if n % 2 == 0 else "tilt-r"
                out.append(f"<button data-lb='p' data-src='../assets/img/{key}.webp' data-caption='{escape(cap)}'>"
                           f"<figure class='taped {tilt}'><img src='../assets/img/{key}-sm.webp' alt='{escape(page['title'])}: {escape(cap)}' loading='lazy'>"
                           f"<figcaption>{escape(cap)}</figcaption></figure></button>")
            out.append("</div>")
        out.append("</section>")

    out.append(f"<nav class='cs-next' aria-label='More projects'><a href='{prev_p['slug']}.html'>← {escape(prev_p['title'])}</a>"
               f"<a href='{next_p['slug']}.html'>{escape(next_p['title'])} →</a></nav>")
    out.append("</div>")
    out.append(FOOT.format(js_v=JS_V))
    (ROOT / "work" / f"{page['slug']}.html").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "work").mkdir(exist_ok=True)
    stamp_index()
    print("index.html: css", CSS_V, "js", JS_V)
    for i, p in enumerate(PAGES):
        build(i, p)
        print("work/" + p["slug"] + ".html")
