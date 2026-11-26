"""Compose the README hero and GitHub social preview from the AI illustration.

The illustration (hero-art.png) has no text by design; all text is set here in
real type so it stays sharp and correct. Scores are real output of
src/model (all-MiniLM-L6-v2) for the README example, measured 2026-11-26.

Run from the repo root:  python docs/assets/tools/compose_hero.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ASSETS = Path("docs/assets")
FONT = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf"
W, H = 1280, 640

# Point centres measured on hero-art.png (1774x887), scaled to 1280x640 below.
QUERY, RICH, HAPPY, SAD = (1150, 480), (1422, 371), (1422, 160), (1580, 623)
SENTENCE = '"feeling like a million bucks"'
SCORES = {"rich": 0.353, "happy": 0.238, "sad": 0.205}

TEAL, GREEN, VIOLET, AMBER = "#5EEAD4", "#34D399", "#C4B5FD", "#FCD34D"
WHITE, MUTED = "#F1F5F9", "#94A3B8"


def font(weight, size):
    try:
        return ImageFont.truetype(FONT.format(weight), size)
    except OSError:
        return ImageFont.load_default()


def scale(p, src):
    return (p[0] * W / src[0], p[1] * H / src[1])


def label(d, xy, text, fill, size=22, dx=22, dy=-14, anchor="la"):
    d.text((xy[0] + dx, xy[1] + dy), text, font=font("SemiBold", size), fill=fill, anchor=anchor)


def compose(title_lines, tagline, out):
    art = Image.open(ASSETS / "hero-art.png").convert("RGB")
    src = art.size
    img = art.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(img)

    q, r, h, s = (scale(p, src) for p in (QUERY, RICH, HAPPY, SAD))
    label(d, q, SENTENCE, WHITE, size=21, dx=0, dy=44, anchor="ma")
    label(d, r, f"rich  {SCORES['rich']:.3f}", GREEN, size=26, dx=20, dy=-16)
    label(d, h, f"happy  {SCORES['happy']:.3f}", VIOLET, dx=-20, dy=-12, anchor="ra")
    label(d, s, f"sad  {SCORES['sad']:.3f}", AMBER, dx=-20, dy=8, anchor="ra")

    y = 150
    for line in title_lines:
        d.text((64, y), line, font=font("Bold", 54), fill=WHITE)
        y += 66
    y += 18
    for line in tagline:
        d.text((64, y), line, font=font("Regular", 26), fill=MUTED)
        y += 36
    d.text((64, H - 70), "all-MiniLM-L6-v2 · FastAPI · Docker · Kubernetes · AWS Fargate",
           font=ImageFont.truetype(MONO, 18), fill=TEAL)
    img.save(ASSETS / out, optimize=True)
    print("wrote", ASSETS / out)


if __name__ == "__main__":
    tag = ["Zero-shot text classification:", "send a sentence and any labels,", "the nearest label by meaning wins."]
    compose(["Semantic", "classification API"], tag, "hero.png")
    compose(["semantic-", "classification-api"], tag, "social-preview.png")
