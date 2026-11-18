"""Builds assets/cv/Brandon_Rodrigues_CV.pdf: the generic games + data/QA CV linked from the site.

Facts are copied from data/build_master_cv.py (the master CV) and Brandon's itch.io pages; nothing new is
invented. Phone number and street address are deliberately left out because this PDF is public.
Run:  python _tools/build_cv.py   (needs Microsoft Edge or Chrome installed for the HTML -> PDF step)
Jekyll ignores folders starting with "_", so this script is not published on GitHub Pages.
"""
import html
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "cv" / "Brandon_Rodrigues_CV.pdf"

NAME = "Brandon Rodrigues"
HEADLINE = "Game Developer · Real-Time 3D & VR · Data / QA Engineer"
CONTACT = [
    ("London, UK", None),
    ("brandon13111998@gmail.com", "mailto:brandon13111998@gmail.com"),
    ("linkedin.com/in/brandon-rodrigues-935762180", "https://www.linkedin.com/in/brandon-rodrigues-935762180"),
    ("Portfolio: namebrandon13.github.io/namebrandon.github.io", "https://namebrandon13.github.io/namebrandon.github.io/"),
    ("itch.io/name-brandon", "https://name-brandon.itch.io/"),
]

SUMMARY = (
    "Creative and technically skilled Game Developer with hands-on experience in Unity, Unreal, and Blender, "
    "and an MSc in Computer Games Technology (Distinction). "
    "Data QA Engineer with over two and a half years of enterprise experience in data pipeline validation, "
    "ETL testing, and UAT management."
)

SKILLS = [
    ("Game Engines", "Unreal Engine 5, Unity, MonoGame"),
    ("Programming", "C++, C#, C, Python, Java, JavaScript, SQL, HTML, CSS"),
    ("Graphics & Systems", "OpenGL, Custom Shaders, Memory Management, Level Streaming, VR/AR Development, Physics Simulation"),
    ("3D & Art", "Blender, Substance Painter, Maya, Photoshop, Marmoset Toolbag"),
    ("QA & Testing", "Jira, Confluence, Postman, Playwright, UAT, Unit Testing, Bug Tracking"),
    ("Data & Cloud", "Snowflake, SAP HANA, Teradata, BigQuery, Azure, GCP, Power BI, React JS"),
    ("Version Control", "Git, GitHub"),
]

ROLES = [
    ("Software Engineer (Contract)", "Candela, London", "Mar 2026 – Present", [
        "Held Unity scenes at a stable 90 FPS VR target, using GPU profiling to isolate draw-call and overdraw bottlenecks.",
        "Reduced triangle counts by up to 40% with no visual loss, through LOD chains and texture atlasing.",
    ]),
    ("3D Generalist (Contract)", "404 Gaming Ltd, London", "Mar 2026 – Present", [
        "Prototyped 20+ modular environment assets to 100% pipeline compliance in Blender, working strictly to level design specs.",
        "Cut asset rejection rates by 35% via a pre-submission checklist covering naming conventions, pivots, and LODs.",
    ]),
    ("Game Developer and Software QA Tester (Part-time)", "Knowbotics AI, London", "Oct 2025 – Present", [
        "Architected core systems for a neurodiverse-learner simulation, implementing mechanics and edge cases in Unreal Engine 5.",
        "Accelerated bug-to-resolution time by 30% through structured QA passes and behaviour logs feeding stakeholder review.",
    ]),
    ("Freelance 3D Generalist and Game Developer", "Upwork, Remote", "Mar 2025 – Present", [
        "Created and shipped VR-ready game environment and prop kits, optimised for Quest 2 and PC-based headsets.",
        "Implemented 3D content into Unreal, Unity, and MonoGame engines for independent teams.",
        "Balanced aesthetic quality with technical constraints (polycount, UV unwrapping, PBR workflows).",
    ]),
    ("VR Support Technician (Part-time)", "Nobody's Listening, London", "Nov 2023 – Jul 2024", [
        "Operated and maintained Meta Quest 2 VR headsets, proactively resolving hardware/software issues and improving session flow by 30%.",
    ]),
    ("Quality Engineer", "LTIMindtree, Mumbai, India", "Jun 2023 – Aug 2023", [
        "Developed automated validation workflows in SQL & Python for Siemens' migration pipeline, improving data integrity by 30%.",
        "Performed root-cause analysis on UAT issues, decreasing QA-to-resolution cycle time by 40%.",
        "Served as point of contact between QA, development, and client-side teams to orchestrate go-live testing and sign-off.",
    ]),
    ("Data Engineer", "LTIMindtree, Mumbai, India", "Jan 2021 – Jun 2023", [
        "Led the migration of more than 5 TB of data across platforms (SAP HANA, JCI servers, Teradata) to Snowflake, Azure, and GCP with 100% client SLA compliance.",
        "Created and supported ETL scripts with SQL and Python, automating major processes that enhanced team throughput by 30%.",
        "Performed performance benchmarking and optimised query logic to decrease data processing time by up to 25%.",
        "Developed and optimised internal migration applications using Python, JavaScript, and React JS within a GCP and Teradata environment.",
    ]),
    ("Freelance 3D Generalist", "Upwork, Remote", "Nov 2020 – Sep 2023", [
        "Finished 150+ projects in gaming, architecture, and product design with a 4.9/5 Upwork rating and several repeat clients.",
        "Automated repetitive tasks through Python scripting, cutting asset turnaround time by 30%.",
    ]),
]

PROJECTS = [
    ("VR Rage Room (Unity, MSc dissertation)", "Procedural destruction and soft-body physics, optimised to a stable 90 FPS on mid-tier hardware through custom collision mesh design."),
    ("Coach Number 11 (Unreal Engine)", "Observation-horror puzzle prototype set on a train; playable on itch.io."),
    ("Cosmic Chaos (Unity)", "Arcade space game with real-time physics, object pooling and wave-based enemy spawners; released on itch.io."),
    ("Delivery Challenge (Unreal)", "Semi-open-world delivery simulation using pathfinding and modular urban assets."),
    ("Space Tracks (C++)", "Framebuffer objects and dynamic shading techniques, built without an engine."),
]

EDUCATION = [
    "MSc Computer Games Technology, City St George's, University of London, Sep 2023 – Oct 2024, Distinction (71.53%)",
    "BEng Computer Engineering, St. John College of Engineering and Management, Jul 2016 – Nov 2020, CGPA 7.69/10",
]
CERTS = ["Microsoft Azure Fundamentals (AZ-900)", "Agile/DevOps/Testing Fundamentals (Pluralsight)"]

CSS = """
@page { size: A4; margin: 13mm 15mm; }
body { font-family: Calibri, Arial, Helvetica, sans-serif; font-size: 10.2pt; line-height: 1.32; color: #111; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 1pt; }
.headline { font-size: 11.5pt; font-weight: bold; margin: 0 0 3pt; }
.contact { font-size: 9.3pt; margin: 0 0 6pt; }
.contact a { color: #111; text-decoration: none; }
h2 { font-size: 11pt; text-transform: uppercase; letter-spacing: .5pt; border-bottom: 1px solid #444; margin: 9pt 0 4pt; padding-bottom: 1pt; }
.role { margin: 0 0 5pt; page-break-inside: avoid; }
.rt { font-weight: bold; margin: 0; }
.rm { margin: 0 0 1pt; font-size: 9.8pt; }
ul { margin: 1pt 0 0 14pt; padding: 0; }
li { margin: 0 0 1.2pt; }
p { margin: 0 0 3pt; }
.sk { display: grid; grid-template-columns: 118pt 1fr; }
"""


def e(s: str) -> str:
    return html.escape(s, quote=True)


def build_html() -> str:
    contact = " | ".join(f'<a href="{e(u)}">{e(t)}</a>' if u else e(t) for t, u in CONTACT)
    parts = [f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{NAME} - CV</title><style>{CSS}</style></head><body>",
             f"<h1>{NAME}</h1><p class='headline'>{e(HEADLINE)}</p><p class='contact'>{contact}</p>",
             f"<h2>Professional Summary</h2><p>{e(SUMMARY)}</p>",
             "<h2>Skills</h2>" + "".join(f"<p class='sk'><b>{e(k)}:</b> {e(v)}</p>" for k, v in SKILLS),
             "<h2>Professional Experience</h2>"]
    for title, org, when, bullets in ROLES:
        lis = "".join(f"<li>{e(b)}</li>" for b in bullets)
        parts.append(f"<div class='role'><p class='rt'>{e(title)}</p><p class='rm'>{e(org)} | {e(when)}</p><ul>{lis}</ul></div>")
    parts.append("<h2>Projects</h2><ul>" + "".join(f"<li><b>{e(t)}:</b> {e(d)}</li>" for t, d in PROJECTS) + "</ul>")
    parts.append("<h2>Education</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in EDUCATION) + "</ul>")
    parts.append("<h2>Certifications</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in CERTS) + "</ul>")
    parts.append("</body></html>")
    return "".join(parts)


def find_browser() -> str:
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"):
        if Path(p).exists():
            return p
    for name in ("msedge", "chrome", "chromium", "google-chrome"):
        if shutil.which(name):
            return shutil.which(name)
    raise SystemExit("Edge or Chrome is needed to print the PDF")


def main() -> Path:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "cv.html"
        src.write_text(build_html(), encoding="utf-8")
        (ROOT / "_tools" / "cv_preview.html").write_text(build_html(), encoding="utf-8")
        subprocess.run([find_browser(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--user-data-dir={Path(tmp) / 'profile'}",
                        f"--print-to-pdf={OUT}", src.as_uri()], check=True, timeout=120)
    print(OUT)
    return OUT


if __name__ == "__main__":
    main()
