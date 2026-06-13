#!/usr/bin/env python3
"""Generate the printable Rec-League Swing Scorecard PDF (scorecard.pdf).

Content mirrors swing-scorecard.md and scorecard.html. Run from this folder:
    pip install reportlab
    python3 build-scorecard-pdf.py
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

ACCENT = colors.HexColor("#1d4e89")
MUTED = colors.HexColor("#555555")
LINE = colors.HexColor("#bbbbbb")
INK = colors.HexColor("#1a1a1a")
HEADBG = colors.HexColor("#eef2f8")
NOTEBG = colors.HexColor("#f7f9fc")
NOTEBD = colors.HexColor("#dfe7f2")

PAGE_W, PAGE_H = letter
M = 0.55 * inch
CW = PAGE_W - 2 * M

KILLERS = [
    ("1. Lunging / drifting", "Face-on",
     "Head & weight slide toward the pitcher early. More than ~a head's-width of forward drift = problem."),
    ("2. Casting / bat drag", "Behind",
     "Hands push out wide instead of knob-to-the-ball. Cast-first = problem. (“Always late on the fastball.”)"),
    ("3. Pulling off / flying open", "Face-on",
     "Front shoulder & head bail toward the dugout early. Shoulder already open at launch = problem."),
    ("4. No load / no separation", "Face-on",
     "Starts dead-still and arms the ball. No gather/coil, no hands-back as the foot lands = problem."),
    ("5. Stepping in the bucket", "Behind",
     "Stride foot lands toward the dugout, not the pitcher. Pointing at the dugout = problem."),
    ("6. Steep / long bat path", "Behind",
     "Barrel chops steeply down or loops way uphill instead of matching the pitch plane. Steep either way = problem."),
]

REFERENCE = [
    ("1. Lunging / drifting", "Face-on",
     "“Stay back — let it come to you. Turn, don’t lunge.”",
     "Fence/wall stride-and-hold · tee work with weight held back · one-handed top-hand tee."),
    ("2. Casting / bat drag", "Behind",
     "“Knob to the ball. Keep your hands inside.”",
     "Towel/connection-ball pinned under lead armpit · inside-pitch tee · two-tee drill (don’t clip the outer tee)."),
    ("3. Pulling off / flying open", "Face-on",
     "“Stay closed, see it deep, hit it back up the middle.”",
     "Opposite-field tee/soft-toss · contact point set deeper · “show the logo” — chest closed until the hands go."),
    ("4. No load / no separation", "Face-on",
     "“Get a rhythm, gather, then go. Hips lead, hands follow.”",
     "Toe-tap / small leg-kick timing · “hands back as foot goes down” reps · hip-turn-first dry swings."),
    ("5. Stepping in the bucket", "Behind / Face-on",
     "“Stride to the pitcher, not away from it.”",
     "Stride into a bat laid on the ground · closed-toe stride vs. a wall · slow walk-up swings toward the mound."),
    ("6. Steep / long bat path", "Behind",
     "“Match the plane. Stay through the zone, not down or up at it.”",
     "Two-tee path drill (low back, higher front) · high-tee/low-tee mix · bottom-hand-only path reps."),
]

c = canvas.Canvas("scorecard.pdf", pagesize=letter)


def wrap(text, font, size, width):
    return simpleSplit(text, font, size, width)


def note_box(x, y, w, lines_data, pad=8, lh=12.5, fs=8.5):
    """Draw a tinted note box; lines_data is list of (text,bold) segments per line already wrapped."""
    height = pad * 2 + lh * len(lines_data)
    c.setFillColor(NOTEBG)
    c.setStrokeColor(NOTEBD)
    c.roundRect(x, y - height, w, height, 4, stroke=1, fill=1)
    ty = y - pad - 9
    for seg in lines_data:
        tx = x + pad
        for txt, bold in seg:
            c.setFont("Helvetica-Bold" if bold else "Helvetica", fs)
            c.setFillColor(ACCENT if bold else colors.HexColor("#33455e"))
            c.drawString(tx, ty, txt)
            tx += c.stringWidth(txt, "Helvetica-Bold" if bold else "Helvetica", fs)
        ty -= lh
    return height


# ---------------- PAGE 1 ----------------
y = PAGE_H - M

# Title
c.setFont("Helvetica-Bold", 21)
c.setFillColor(ACCENT)
c.drawString(M, y - 16, "Rec-League Swing Scorecard")
# tag
tag = "v0 · MANUAL"
c.setFont("Helvetica-Bold", 8)
tw = c.stringWidth(tag, "Helvetica-Bold", 8) + 12
c.setFillColor(ACCENT)
c.roundRect(M + c.stringWidth("Rec-League Swing Scorecard", "Helvetica-Bold", 21) + 10,
            y - 16, tw, 14, 3, fill=1, stroke=0)
c.setFillColor(colors.white)
c.drawString(M + c.stringWidth("Rec-League Swing Scorecard", "Helvetica-Bold", 21) + 16, y - 13, tag)
y -= 30
c.setFont("Helvetica", 10)
c.setFillColor(MUTED)
c.drawString(M, y, "Watch the swing video, mark what you see, then hand the hitter 1–3 things to work on.")
y -= 22

# Meta fields
field_w = (CW - 2 * 16) / 3
labels = ["HITTER", "DATE", "FILMED / SCORED BY"]
for i, lab in enumerate(labels):
    fx = M + i * (field_w + 16)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(MUTED)
    c.drawString(fx, y, lab)
    c.setStrokeColor(LINE)
    c.line(fx, y - 16, fx + field_w, y - 16)
y -= 30

# Film note
seg = [
    [("Film it right first. ", True), ("Two angles if you can — ", False), ("face-on ", True),
     ("(phone ~15 ft to the side, hip height) and ", False), ("behind ", True), ("(catcher’s view).", False)],
    [("Whole body + bat in frame, slow-mo ON. If the body and bat aren’t clearly visible, don’t score it — refilm.", False)],
]
h = note_box(M, y, CW, seg)
y -= h + 16

# Table
col_killer = CW * 0.40
col_angle = CW * 0.13
col_score = CW * 0.22
col_notes = CW * 0.25
x0 = M
x1 = x0 + col_killer
x2 = x1 + col_angle
x3 = x2 + col_score
x4 = x3 + col_notes

# header
hh = 18
c.setFillColor(HEADBG)
c.rect(x0, y - hh, CW, hh, fill=1, stroke=0)
c.setFillColor(colors.HexColor("#33455e"))
c.setFont("Helvetica-Bold", 8)
c.drawString(x0 + 5, y - 12, "SWING-KILLER & WHAT TO LOOK FOR")
c.drawString(x1 + 5, y - 12, "ANGLE")
c.drawString(x2 + 5, y - 12, "SCORE")
c.drawString(x3 + 5, y - 12, "NOTES")
ytop = y
y -= hh

# rows
for name, angle, look in KILLERS:
    name_lines = wrap(name, "Helvetica-Bold", 9.5, col_killer - 10)
    look_lines = wrap(look, "Helvetica", 8, col_killer - 10)
    content_h = 4 + len(name_lines) * 11 + 2 + len(look_lines) * 9.5 + 6
    row_h = max(content_h, 44)
    ry = y
    # killer text
    ty = ry - 13
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(INK)
    for ln in name_lines:
        c.drawString(x0 + 5, ty, ln)
        ty -= 11
    ty -= 2
    c.setFont("Helvetica", 8)
    c.setFillColor(MUTED)
    for ln in look_lines:
        c.drawString(x0 + 5, ty, ln)
        ty -= 9.5
    # angle
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ACCENT)
    c.drawString(x1 + 5, ry - 14, angle)
    # score checkboxes
    sy = ry - 13
    for opt in ("OK", "Minor", "Major"):
        c.setStrokeColor(colors.HexColor("#666666"))
        c.setLineWidth(1.2)
        c.rect(x2 + 6, sy - 9, 10, 10, fill=0, stroke=1)
        c.setFont("Helvetica", 9)
        c.setFillColor(INK)
        c.drawString(x2 + 21, sy - 8, opt)
        sy -= 14
    y -= row_h

# grid lines
c.setStrokeColor(LINE)
c.setLineWidth(0.8)
# verticals
for xx in (x0, x1, x2, x3, x4):
    c.line(xx, ytop, xx, y)
# top + bottom + row separators
c.line(x0, ytop, x4, ytop)
yy = ytop - hh
c.line(x0, yy, x4, yy)
# recompute row separators
ycur = ytop - hh
for name, angle, look in KILLERS:
    name_lines = wrap(name, "Helvetica-Bold", 9.5, col_killer - 10)
    look_lines = wrap(look, "Helvetica", 8, col_killer - 10)
    content_h = 4 + len(name_lines) * 11 + 2 + len(look_lines) * 9.5 + 6
    row_h = max(content_h, 44)
    ycur -= row_h
    c.line(x0, ycur, x4, ycur)

y = ycur - 22

# Summary
def summary_block(label, hint, y, n_lines=2, maxw=CW):
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(INK)
    c.drawString(M, y, label)
    if hint:
        w = c.stringWidth(label + " ", "Helvetica-Bold", 10)
        c.setFont("Helvetica", 8)
        c.setFillColor(MUTED)
        c.drawString(M + w, y, hint)
    yy = y - 16
    c.setStrokeColor(LINE)
    for _ in range(n_lines):
        c.line(M, yy, M + maxw, yy)
        yy -= 16
    return yy - 6

y = summary_block("Top 1–3 to work on", "(only the biggest Majors — don’t dump all six)", y)
y = summary_block("Drills assigned", "", y)
y = summary_block("Refilm by", "", y, n_lines=1, maxw=2.6 * inch)

c.showPage()

# ---------------- PAGE 2: REFERENCE ----------------
y = PAGE_H - M
c.setFont("Helvetica-Bold", 21)
c.setFillColor(ACCENT)
c.drawString(M, y - 16, "Coaching reference")
y -= 30
c.setFont("Helvetica", 10)
c.setFillColor(MUTED)
c.drawString(M, y, "The cue to say and a drill or two for each killer. Give one thing at a time.")
y -= 24

for name, angle, cue, drills in REFERENCE:
    c.setFont("Helvetica-Bold", 11.5)
    c.setFillColor(INK)
    c.drawString(M, y, name)
    w = c.stringWidth(name + "  ", "Helvetica-Bold", 11.5)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ACCENT)
    c.drawString(M + w, y, "· " + angle)
    y -= 14
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(ACCENT)
    for ln in wrap(cue, "Helvetica-Oblique", 10, CW):
        c.drawString(M, y, ln)
        y -= 13
    c.setFont("Helvetica", 9)
    c.setFillColor(MUTED)
    for ln in wrap("Drills: " + drills, "Helvetica", 9, CW):
        c.drawString(M, y, ln)
        y -= 11.5
    y -= 8

# How-to note
y -= 4
seg = [
    [("How to use it:  ", True), ("score each killer OK / Minor / Major → pick the top 1–3 Majors only → tell the hitter", False)],
    [("what you saw + the cue + one drill → refilm in 2–3 weeks and re-score. Did it move? That’s your proof.", False)],
    [("Honest caveat: these are rough, widely-taught fundamentals, not gospel — trust your eyes and catch the big stuff.", False)],
]
note_box(M, y, CW, seg)

c.setFont("Helvetica", 8)
c.setFillColor(colors.HexColor("#888888"))
c.drawCentredString(PAGE_W / 2, M - 6, "Rec-League Swing Scorecard · manual v0 · catch the big, obvious swing-killers")

c.showPage()
c.save()
print("wrote scorecard.pdf")
