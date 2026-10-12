"""Er-Con Site Survey: fillable 2-page PDF, rebranded from the Ecodyne,CIM General Survey Form."""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white

NAVY = HexColor('#0B2D5B'); SIGNAL = HexColor('#0067D0'); GRAPHITE = HexColor('#4A4949')
HAZE = HexColor('#D8D7D6'); MIST = HexColor('#F4F4F3'); FIELD = HexColor('#FAFAF9')
W, H = letter
M = 42                      # side margin
CW = W - 2 * M              # content width
LAB = 7                     # label size
FH = 18                     # field height

c = canvas.Canvas('/home/claude/survey/Er-Con-Site-Survey.pdf', pagesize=letter)
c.setTitle('Er-Con Site Survey'); c.setAuthor('Er-Con Technologies'); c.setSubject('Site survey form')
form = c.acroForm
y = 0
names = set()

def fid(label):
    base = ''.join(ch for ch in label.title() if ch.isalnum())[:40] or 'Field'
    n, i = base, 2
    while n in names:
        n = f'{base}{i}'; i += 1
    names.add(n); return n

def header(page):
    c.setFillColor(NAVY); c.rect(0, H - 6, W, 6, stroke=0, fill=1)
    c.drawImage('/home/claude/survey/logo.png', M, H - 70, width=137, height=49.6, mask='auto')
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 22)
    c.drawRightString(W - M, H - 46, 'Site Survey')
    c.setFillColor(GRAPHITE); c.setFont('Helvetica', 8.5)
    c.drawRightString(W - M, H - 60, f'Page {page} of 2')
    c.setStrokeColor(SIGNAL); c.setLineWidth(2); c.line(M, H - 82, W - M, H - 82)

def footer():
    c.setStrokeColor(HAZE); c.setLineWidth(.6); c.line(M, 40, W - M, 40)
    c.setFillColor(GRAPHITE); c.setFont('Helvetica', 7.5)
    c.drawString(M, 27, 'Er-Con Technologies  ·  6715 Theall Road, Houston, TX 77066')
    c.drawRightString(W - M, 27, '+1 (713) 460-4601  ·  info@er-contech.com')


GAP = 18
COLW = (CW - GAP) / 2
LX, RX = M, M + COLW + GAP
FH2 = 16

def section_at(x, w, title, note=None):
    global y
    y -= 18
    c.setFillColor(SIGNAL); c.setFont('Helvetica-Bold', 8.5); c.drawString(x, y, title.upper())
    if note:
        c.setFillColor(GRAPHITE); c.setFont('Helvetica-Oblique', 7.5)
        c.drawString(x + c.stringWidth(title.upper(), 'Helvetica-Bold', 8.5) + 8, y, note)
    c.setStrokeColor(NAVY); c.setLineWidth(1.2); c.line(x, y - 5, x + w, y - 5)
    y -= 10

def tfield(label, x, w, h=FH2, multiline=False, top=None):
    t = y if top is None else top
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(x, t - LAB, label.upper())
    form.textfield(name=fid(label), tooltip=label, x=x, y=t - LAB - 3 - h, width=w, height=h,
                   borderColor=HAZE, fillColor=FIELD, textColor=NAVY, borderWidth=.8,
                   fontName='Helvetica', fontSize=0 if multiline else 9, fieldFlags='multiline' if multiline else '')

def frow(x, w, *cols, h=FH2, gap=10, multiline=False):
    global y
    total = sum(f for _, f in cols); avail = w - gap * (len(cols) - 1); cx = x
    for label, f in cols:
        cw = avail * f / total; tfield(label, cx, cw, h, multiline); cx += cw + gap
    y -= LAB + 3 + h + 7

def cb(prefix, o, x, yy, size=8.5):
    form.checkbox(name=fid(f'{prefix} {o}'), tooltip=f'{prefix}: {o}', x=x, y=yy - 1, size=9.5, buttonStyle='check',
                  borderColor=GRAPHITE, fillColor=white, textColor=NAVY, borderWidth=.8)
    c.setFillColor(NAVY); c.setFont('Helvetica', size); c.drawString(x + 13, yy + 1, o)
    return x + 13 + c.stringWidth(o, 'Helvetica', size) + 12

def cbgroup(x, w, label, prefix, opts):
    """label then options, wrapping inside width w"""
    global y
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(x, y - LAB, label.upper())
    yy = y - LAB - 15; cx = x
    for o in opts:
        need = 13 + c.stringWidth(o, 'Helvetica', 8.5) + 12
        if cx + need > x + w + 12: cx = x; yy -= 15
        cx = cb(prefix, o, cx, yy)
    y = yy - 9

def yn(x, w, q, follow=None):
    """question, Yes/No at right; optional follow-up field on the next line"""
    global y
    c.setFillColor(NAVY); c.setFont('Helvetica', 8.5); c.drawString(x, y - 11, q)
    bx = x + w - 78
    nx = cb(q, 'Yes', bx, y - 12); cb(q, 'No', nx, y - 12)
    y -= 17
    if follow:
        c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', 6.5); c.drawString(x + 10, y - 9, follow.upper())
        fx = x + 10 + c.stringWidth(follow.upper(), 'Helvetica-Bold', 6.5) + 6
        form.textfield(name=fid(follow), tooltip=follow, x=fx, y=y - 13, width=x + w - fx, height=13,
                       borderColor=HAZE, fillColor=FIELD, textColor=NAVY, borderWidth=.8, fontName='Helvetica', fontSize=8)
        y -= 17
    c.setStrokeColor(MIST); c.setLineWidth(.6); c.line(x, y - 2, x + w, y - 2)
    y -= 5

import math
SIG_L = HexColor('#DCE9F8')
def lab(x, y, t, size=6.5, bold=True, color=None, anchor='c', rot=0, bg=False):
    c.saveState(); f = 'Helvetica-Bold' if bold else 'Helvetica'
    c.translate(x, y); c.rotate(rot)
    if bg:
        tw = c.stringWidth(t, f, size); x0 = {'c': -tw / 2, 'l': 0, 'r': -tw}[anchor]
        c.setFillColor(white); c.rect(x0 - 2, -2, tw + 4, size + 2.5, stroke=0, fill=1)
    c.setFillColor(color or NAVY); c.setFont(f, size)
    {'c': c.drawCentredString, 'l': c.drawString, 'r': c.drawRightString}[anchor](0, 0, t)
    c.restoreState()

def arrowhead(x, y, ang, size=3.2):
    p = c.beginPath(); p.moveTo(x, y)
    p.lineTo(x - size * math.cos(ang - .45), y - size * math.sin(ang - .45))
    p.lineTo(x - size * math.cos(ang + .45), y - size * math.sin(ang + .45)); p.close()
    c.drawPath(p, stroke=0, fill=1)

def dim(x1, y1, x2, y2, dashed=True, both=True):
    c.saveState(); c.setStrokeColor(NAVY); c.setFillColor(NAVY); c.setLineWidth(.7)
    if dashed: c.setDash(2.5, 1.8)
    c.line(x1, y1, x2, y2); c.setDash()
    ang = math.atan2(y2 - y1, x2 - x1)
    arrowhead(x2, y2, ang)
    if both: arrowhead(x1, y1, ang + math.pi)
    c.restoreState()

def brace_h(x1, x2, y, up=True, t='', ty=None):
    d = 4 if up else -4
    c.setStrokeColor(GRAPHITE); c.setLineWidth(.6)
    c.line(x1, y, x1, y + d); c.line(x2, y, x2, y + d); c.line(x1, y + d, x2, y + d)
    m = (x1 + x2) / 2; c.line(m, y + d, m, y + 2 * d)
    if t: lab(m, ty if ty is not None else (y + 2 * d + (2 if up else -7)), t)

def brace_v(x, y1, y2, left=True, t=''):
    d = -4 if left else 4
    c.setStrokeColor(GRAPHITE); c.setLineWidth(.6)
    c.line(x, y1, x + d, y1); c.line(x, y2, x + d, y2); c.line(x + d, y1, x + d, y2)
    m = (y1 + y2) / 2; c.line(x + d, m, x + 2 * d, m)
    if t: lab(x + 2 * d + (-3 if left else 3), m - 2, t, anchor='r' if left else 'l')

def ex_plan(x, y, w, h):
    """Plan view of a crossing: pipeline band across high banks and toes, skew D1/D2, exposure."""
    xs = [x + w * f for f in (.30, .46, .62, .80)]
    names = ['HIGH BANK', 'TOE', 'TOE', 'HIGH BANK']
    top, bot = y + h - 2, y + 14
    x0, x1 = x + 10, x + w - 6
    ya, yb = y + h - 12, y + 30
    slope = (yb - ya) / (x1 - x0)
    def py(px): return ya + (px - x0) * slope
    ang = math.degrees(math.atan(slope))
    c.setStrokeColor(NAVY); c.setLineWidth(1.1)
    for i, bx in enumerate(xs):
        k = 4 if i in (1, 2) else 2.5
        sgn = -1 if i < 2 else 1
        pth = c.beginPath(); pth.moveTo(bx - sgn * 2, top); pth.curveTo(bx + sgn * k, top - (top - bot) * .3, bx + sgn * k, bot + (top - bot) * .3, bx - sgn * 2, bot)
        c.drawPath(pth, stroke=1, fill=0)
        lab(bx - sgn * 2, y + 4, names[i], size=5.5)
    c.setFillColor(SIG_L); c.setStrokeColor(SIGNAL); c.setLineWidth(.8)
    pth = c.beginPath(); pth.moveTo(x0, py(x0) + 3.5); pth.lineTo(x1, py(x1) + 3.5); pth.lineTo(x1, py(x1) - 3.5); pth.lineTo(x0, py(x0) - 3.5); pth.close()
    c.drawPath(pth, stroke=1, fill=1)
    lab(x1 - 2, py(x1) + 8, 'PL', size=6.5, color=SIGNAL, anchor='r')
    # skew D2: horizontal dashed from left high bank to where the PL meets the right high bank
    yd = py(xs[3])
    c.setStrokeColor(NAVY); c.setLineWidth(.8); c.setDash(3, 2); c.line(xs[0], yd, xs[3], yd); c.line(xs[0], yd, xs[0], py(xs[0])); c.setDash()
    lab((xs[1] + xs[2]) / 2, yd - 9, 'SKEW (D2)', bg=True)
    brace_v(xs[0] - 4, yd, py(xs[0]), left=True, t='SKEW (D1)')
    # exposure along the pipe between the toes
    c.setStrokeColor(GRAPHITE); c.setLineWidth(.6)
    ax, bx2 = xs[1], xs[2]
    c.line(ax, py(ax) + 6, bx2, py(bx2) + 6); c.line(ax, py(ax) + 4, ax, py(ax) + 8); c.line(bx2, py(bx2) + 4, bx2, py(bx2) + 8)
    mx = (ax + bx2) / 2
    lab(mx, py(mx) + 10, 'EXPOSURE', rot=ang, bg=True)

def ex_xsec(x, y, w, h):
    """Cross section: channel with pipeline, high bank width, bottom width, depth."""
    gtop = y + h - 26; gbot = y + 34
    l1, l2 = x + w * .42, x + w * .53
    r2, r1 = x + w * .70, x + w * .82
    c.setStrokeColor(NAVY); c.setLineWidth(1.3)
    pth = c.beginPath(); pth.moveTo(x + w * .28, gtop); pth.lineTo(l1, gtop); pth.lineTo(l2, gbot); pth.lineTo(r2, gbot); pth.lineTo(r1, gtop); pth.lineTo(x + w - 4, gtop)
    c.drawPath(pth, stroke=1, fill=0)
    # pipeline band (exposed across the channel)
    py0 = gbot + (gtop - gbot) * .42
    c.setFillColor(SIG_L); c.setStrokeColor(SIGNAL); c.setLineWidth(.8)
    c.rect(x + w * .30, py0 - 3.5, w * .67, 7, stroke=1, fill=1)
    lab(x + w * .93, py0 - 2.3, 'PL', color=SIGNAL)
    # dashed channel-bottom reference back to the depth brace
    c.setStrokeColor(NAVY); c.setLineWidth(.7); c.setDash(3, 2); c.line(x + w * .28, gbot, l2, gbot); c.setDash()
    brace_h(l1, r1, gtop + 6, up=True, t='HIGH BANK (HB)')
    brace_h(l2, r2, gbot - 6, up=False, t='BOTTOM WIDTH (BW)')
    brace_v(x + w * .27, gbot, gtop, left=True, t='DEPTH (D)')

def ex_exposure(x, y, w, h):
    """Exposure: pipeline positions relative to the bed, height and distances, flow direction."""
    # flow arrow
    fy = y + h - 16
    c.setStrokeColor(NAVY); c.setFillColor(NAVY); c.setLineWidth(.8)
    c.line(x + 14, fy, x + w * .55, fy); arrowhead(x + 14, fy, math.pi); arrowhead(x + w * .55, fy, 0)
    c.setFillColor(MIST if False else white); c.rect(x + w * .2, fy - 5, w * .16, 10, stroke=0, fill=1)
    lab(x + w * .28, fy - 2.3, 'FLOW', size=6.5)
    lab(x + w * .28, fy - 11, '(circle direction)', size=5.5, bold=False, color=GRAPHITE)
    # bed line
    by0, by1 = y + h * .52, y + h * .46
    c.setStrokeColor(NAVY); c.setLineWidth(1.1); c.line(x + w * .12, by0, x + w - 8, by1)
    def bed(px): return by0 + (by1 - by0) * (px - (x + w * .12)) / (w - 8 - w * .12)
    cx = x + w * .58
    def pipe(px, py, r):
        c.setFillColor(NAVY); c.setStrokeColor(SIGNAL); c.setLineWidth(1); c.circle(px, py, r, stroke=1, fill=1)
    # pipe above the bed: height
    ph = bed(cx) + 22
    pipe(cx, ph, 5.5); lab(cx, ph + 9, 'PL', color=SIGNAL)
    brace_v(cx + 9, bed(cx), ph, left=False, t='HEIGHT (H)')
    # centre reference
    c.setStrokeColor(NAVY); c.setLineWidth(.7); c.setDash(2, 2); c.line(cx, ph - 6, cx, y + 30); c.setDash()
    # pipe left, below: distance D1
    lx, ly = x + w * .24, bed(x + w * .24) - 16
    pipe(lx, ly, 7.5); lab(lx - 12, ly + 6, 'PL', color=SIGNAL, anchor='r')
    dim(lx + 10, ly, cx - 2, ly)
    brace_h(lx, cx, ly - 12, up=False, t='DISTANCE (D1)')
    # pipe right, on the bed: distance D2
    rx = x + w * .86; ry = bed(rx)
    pipe(rx, ry, 5.5); lab(rx + 8, ry + 5, 'PL', color=SIGNAL, anchor='l')
    dim(cx + 2, ry - 4, rx - 8, ry - 4)
    brace_h(cx, rx, ry - 12, up=False, t='DISTANCE (D2)', ty=ry - 30)


def grid(x, yb, w, h, title=None):
    c.setFillColor(FIELD); c.setStrokeColor(HAZE); c.setLineWidth(.8); c.rect(x, yb, w, h, stroke=1, fill=1)
    c.setStrokeColor(HexColor('#ECEBEA')); c.setLineWidth(.4)
    top = yb + h - (18 if title else 3)
    gx = x + 13
    while gx < x + w - 2: c.line(gx, yb + 3, gx, top); gx += 13
    gy = yb + 13
    while gy < top: c.line(x + 3, gy, x + w - 3, gy); gy += 13
    if title:
        c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(x + 8, yb + h - 12, title.upper())

def example(x, yb, w, h, title, fn):
    c.setFillColor(white); c.setStrokeColor(HAZE); c.setLineWidth(.8); c.rect(x, yb, w, h, stroke=1, fill=1)
    c.setFillColor(SIGNAL); c.setFont('Helvetica-Bold', LAB); c.drawString(x + 8, yb + h - 12, 'EXAMPLE')
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 8); c.drawString(x + 48, yb + h - 12, title)
    fn(x + 4, yb + 3, w - 8, h - 18)

# ================================================================== page 1
header(1); y = H - 92
c.setFillColor(GRAPHITE); c.setFont('Helvetica', 8.5)
c.drawString(M, y - 10, 'Fill in what you know and leave the rest blank. Save the completed form and email it, with any photos, to')
c.drawString(M, y - 21, 'info@er-contech.com. Photos of the site are the most helpful thing you can send.')
y -= 22

section_at(M, CW, 'Contact')
frow(M, CW, ('Company', 3), ('Date', 1))
frow(M, CW, ('Site contact', 2), ('Title', 2))
frow(M, CW, ('Office phone', 1), ('Cell phone', 1), ('Email', 2))
frow(M, CW, ('Address', 1))
ystart = y

# left column: site, erosion, pipeline
section_at(LX, COLW, 'Site')
frow(LX, COLW, ('Body of water', 2), ('State', 1))
frow(LX, COLW, ('City', 1), ('County', 1))
frow(LX, COLW, ('Latitude', 1), ('Longitude', 1))
section_at(LX, COLW, 'The erosion')
cbgroup(LX, COLW, 'Erosion type', 'Erosion type', ['Degradation', 'Head cutting', 'Lateral migration', 'Other'])
frow(LX, COLW, ('If other, describe', 3), ('Depth of flow', 2))
cbgroup(LX, COLW, 'Bed material (check all that apply)', 'Bed material', ['Clay', 'Rock', 'Gravel', 'Sand'])
cbgroup(LX, COLW, 'Bank material (check all that apply)', 'Bank material', ['Clay', 'Rock', 'Gravel', 'Sand'])
section_at(LX, COLW, 'Pipeline', 'if a pipeline is involved')
frow(LX, COLW, ('Line name / number', 1), ('Milepost / station', 1))
frow(LX, COLW, ('Pipelines in ROW', 1), ('Diameter(s)', 1))
frow(LX, COLW, ('Length of exposure', 1), ('Length of free span', 1))
yn(LX, COLW, 'Is the pipeline visible?')
yn(LX, COLW, 'Is recoating needed?')
yleft = y

# right column: access and construction
y = ystart
section_at(RX, COLW, 'Access and construction')
yn(RX, COLW, 'Weather sensitive?', 'If yes, explain')
yn(RX, COLW, 'Is the right-of-way cleared?')
yn(RX, COLW, 'Walk to site?', 'Distance walked')
yn(RX, COLW, 'Tree removal needed?', 'Number of trees / size')
yn(RX, COLW, 'Other pipelines or utilities in ROW?', 'Company name(s)')
yn(RX, COLW, 'Road or bridge limits?', 'Weight limits')
yn(RX, COLW, 'Overhead power lines?')
y -= 4
cbgroup(RX, COLW, 'Additional equipment / material needed', 'Equipment',
        ['Excavator', 'Pumps', 'Dozer', 'Loader', 'Culvert', 'Rock', 'Timber mats', 'Forklift'])
assert min(yleft, y) > 50, (yleft, y)
print('page1 bottoms', round(yleft), round(y))
footer(); c.showPage()

# ================================================================== page 2
header(2); y = H - 92
y -= 4
frow(M, CW, ('Project name', 1), ('Pipeline company', 1), gap=GAP)
# comments + plan example
rowh = 140
top = y
tfield('Comments', LX, COLW, h=rowh - 13, multiline=True, top=top)
example(RX, top - rowh, COLW, rowh, 'Plan view', ex_plan)
y = top - rowh - 10
# shared plan-view sketch grid
bottom = 52
exh = 118; gap = 10
sk2 = (y - bottom - exh - 2 * gap) * .5
plan_h = y - bottom - exh - 2 * gap - sk2
grid(M, y - plan_h, CW, plan_h, 'Plan view sketch')
y -= plan_h + gap
example(LX, y - exh, COLW, exh, 'Cross section', ex_xsec)
example(RX, y - exh, COLW, exh, 'Exposure', ex_exposure)
y -= exh + gap
grid(LX, bottom, COLW, y - bottom, 'Cross section sketch')
grid(RX, bottom, COLW, y - bottom, 'Exposure sketch')
footer(); c.showPage()
c.save()
print('ok')
