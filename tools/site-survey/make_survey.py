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
    c.drawRightString(W - M, H - 60, f'Page {page} of 3')
    c.setStrokeColor(SIGNAL); c.setLineWidth(2); c.line(M, H - 82, W - M, H - 82)

def footer():
    c.setStrokeColor(HAZE); c.setLineWidth(.6); c.line(M, 40, W - M, 40)
    c.setFillColor(GRAPHITE); c.setFont('Helvetica', 7.5)
    c.drawString(M, 27, 'Er-Con Technologies  ·  6715 Theall Road, Houston, TX 77066')
    c.drawRightString(W - M, 27, '+1 (713) 460-4601  ·  info@er-contech.com')

def section(title, note=None):
    global y
    y -= 22
    c.setFillColor(SIGNAL); c.setFont('Helvetica-Bold', 8.5)
    c.drawString(M, y, title.upper())
    if note:
        c.setFillColor(GRAPHITE); c.setFont('Helvetica-Oblique', 7.5)
        c.drawString(M + c.stringWidth(title.upper(), 'Helvetica-Bold', 8.5) + 8, y, note)
    c.setStrokeColor(NAVY); c.setLineWidth(1.2); c.line(M, y - 5, W - M, y - 5)
    y -= 12

def text(label, x, w, h=FH, multiline=False):
    """label above, field below; returns nothing. caller manages row y."""
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB)
    c.drawString(x, y - LAB, label.upper())
    form.textfield(name=fid(label), tooltip=label, x=x, y=y - LAB - 3 - h, width=w, height=h,
                   borderColor=HAZE, fillColor=FIELD, textColor=NAVY, borderWidth=.8,
                   fontName='Helvetica', fontSize=0 if multiline else 9,
                   fieldFlags='multiline' if multiline else '')

def row(*cols, h=FH, gap=12, multiline=False):
    """cols: (label, fraction)"""
    global y
    total = sum(f for _, f in cols); avail = CW - gap * (len(cols) - 1); x = M
    for label, f in cols:
        w = avail * f / total; text(label, x, w, h, multiline); x += w + gap
    y -= LAB + 3 + h + 6

def box(label, x, yy):
    form.checkbox(name=fid(label), tooltip=label, x=x, y=yy - 1, size=10, buttonStyle='check',
                  borderColor=GRAPHITE, fillColor=white, textColor=NAVY, borderWidth=.8)
    c.setFillColor(NAVY); c.setFont('Helvetica', 8.5); c.drawString(x + 14, yy + 1, label)
    return x + 14 + c.stringWidth(label, 'Helvetica', 8.5) + 16

def checks(label, options, x=M, prefix=''):
    """one line: LABEL  [] a  [] b ..."""
    global y
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(x, y - LAB, label.upper())
    yy = y - LAB - 16; cx = x
    for o in options:
        cx = box(o if not prefix else o, cx, yy) if not prefix else _pbox(prefix, o, cx, yy)
    y -= LAB + 26

def _pbox(prefix, o, x, yy):
    form.checkbox(name=fid(f'{prefix} {o}'), tooltip=f'{prefix}: {o}', x=x, y=yy - 1, size=10, buttonStyle='check',
                  borderColor=GRAPHITE, fillColor=white, textColor=NAVY, borderWidth=.8)
    c.setFillColor(NAVY); c.setFont('Helvetica', 8.5); c.drawString(x + 14, yy + 1, o)
    return x + 14 + c.stringWidth(o, 'Helvetica', 8.5) + 16

def yesno(question, follow=None, follow_w=None):
    """QUESTION ............ [] Yes [] No   [follow-up field]"""
    global y
    qw = 210
    c.setFillColor(NAVY); c.setFont('Helvetica', 9); c.drawString(M, y - 12, question)
    x = M + qw
    x = _pbox(question, 'Yes', x, y - 13)
    x = _pbox(question, 'No', x, y - 13)
    if follow:
        fx = M + qw + 100
        c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(fx, y - 4, follow.upper())
        form.textfield(name=fid(follow), tooltip=follow, x=fx, y=y - 22, width=W - M - fx, height=15,
                       borderColor=HAZE, fillColor=FIELD, textColor=NAVY, borderWidth=.8, fontName='Helvetica', fontSize=9)
    c.setStrokeColor(MIST); c.setLineWidth(.6); c.line(M, y - 27, W - M, y - 27)
    y -= 31

# ------------------------------------------------------------------ page 1
header(1); y = H - 92
c.setFillColor(GRAPHITE); c.setFont('Helvetica', 9)
c.drawString(M, y - 10, 'Fill in what you know and leave the rest blank. Save the completed form and email it, with any photos,')
c.drawString(M, y - 22, 'to info@er-contech.com. Photos of the site are the most helpful thing you can send.')
y -= 26

section('Contact')
row(('Company', 3), ('Date', 1))
row(('Site contact', 2), ('Title', 2))
row(('Office phone', 1), ('Cell phone', 1), ('Email', 2))
row(('Address', 1))

section('Site')
row(('Project name', 2), ('Body of water', 2))
row(('City', 2), ('County', 2), ('State', 1))
row(('Latitude', 1), ('Longitude', 1))

section('The erosion')
checks('Erosion type', ['Degradation', 'Head cutting', 'Lateral migration', 'Other'], prefix='Erosion type')
row(('If other, describe', 3), ('Nominal depth of flow', 1))
for lab, x0 in (('Bed material', M), ('Bank material', M + CW / 2 + 6)):
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(x0, y - LAB, (lab + ' (check all that apply)').upper())
    cx = x0
    for o in ['Clay', 'Rock', 'Gravel', 'Sand']:
        cx = _pbox(lab, o, cx, y - LAB - 16)
y -= LAB + 26

section('Pipeline', 'if a pipeline is involved')
row(('Pipeline company', 2), ('Line name / number', 2))
row(('Milepost / station', 1), ('Pipelines in right-of-way', 1), ('Pipeline diameter(s)', 1))
row(('Length of exposure', 1), ('Length of free span', 1))
# two yes/no questions on one line
c.setFillColor(NAVY); c.setFont('Helvetica', 9)
c.drawString(M, y - 12, 'Is the pipeline visible?')
x = _pbox('Is the pipeline visible?', 'Yes', M + 130, y - 13); _pbox('Is the pipeline visible?', 'No', x, y - 13)
c.setFillColor(NAVY); c.setFont('Helvetica', 9)
c.drawString(M + CW / 2 + 6, y - 12, 'Is recoating needed?')
x = _pbox('Is recoating needed?', 'Yes', M + CW / 2 + 130, y - 13); _pbox('Is recoating needed?', 'No', x, y - 13)
y -= 24
assert y > 52, y
footer(); c.showPage()

# ------------------------------------------------------------------ page 2
header(2); y = H - 92
section('Access and construction')
yesno('Weather sensitive?', 'If yes, explain')
yesno('Is the right-of-way cleared?')
yesno('Walk to site?', 'If yes, distance walked')
yesno('Tree removal needed?', 'Number of trees / size')
yesno('Other pipelines or utilities in the ROW?', 'Company name(s)')
yesno('Road or bridge limits?', 'If yes, weight limits')
yesno('Overhead power lines?')
y -= 4
checks('Additional equipment / material for access or construction',
       ['Excavator', 'Pumps', 'Dozer', 'Loader', 'Culvert', 'Rock', 'Timber mats', 'Forklift'], prefix='Equipment')

section('Comments')
row(('Anything else we should know', 1), h=62, multiline=True)

footer(); c.showPage()

# ------------------------------------------------------------------ page 3: sketches with reference examples
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
    xs = [x + w * f for f in (.32, .48, .64, .84)]
    names = ['HIGH BANK', 'TOE', 'TOE', 'HIGH BANK']
    top, bot = y + h - 6, y + 36
    def py(px):  # pipeline centreline
        return (y + h - 18) - (px - (x + 8)) * .55
    # bank lines (gentle curves)
    c.setStrokeColor(NAVY); c.setLineWidth(1.1)
    for i, bx in enumerate(xs):
        k = 5 if i in (1, 2) else 3
        sgn = -1 if i < 2 else 1
        pth = c.beginPath(); pth.moveTo(bx - sgn * 2, top); pth.curveTo(bx + sgn * k, top - 30, bx + sgn * k, bot + 30, bx - sgn * 3, bot)
        c.drawPath(pth, stroke=1, fill=0)
        lab(bx + 2, y + 6, names[i], size=5.5, rot=90, anchor='l')
    # pipeline band
    x0, x1 = x + 8, x + w - 6
    c.setFillColor(SIG_L); c.setStrokeColor(SIGNAL); c.setLineWidth(.8)
    pth = c.beginPath(); pth.moveTo(x0, py(x0) + 4); pth.lineTo(x1, py(x1) + 4); pth.lineTo(x1, py(x1) - 4); pth.lineTo(x0, py(x0) - 4); pth.close()
    c.drawPath(pth, stroke=1, fill=1)
    lab(x1 - 4, py(x1) + 10, 'PL', size=6.5, color=SIGNAL, anchor='r')
    # skew D2: horizontal dashed from left high bank to where PL meets right high bank
    yd = py(xs[3])
    c.setStrokeColor(NAVY); c.setLineWidth(.8); c.setDash(3, 2); c.line(xs[0], yd, xs[3], yd); c.line(xs[0], yd, xs[0], py(xs[0])); c.setDash()
    lab((xs[1] + xs[2]) / 2, yd - 10, 'SKEW (D2)', bg=True)
    # skew D1: vertical at left high bank
    brace_v(xs[0] - 4, yd, py(xs[0]), left=True, t='SKEW (D1)')
    # exposure along the pipe between the toes
    c.setStrokeColor(GRAPHITE); c.setLineWidth(.6)
    ax, bx2 = xs[1], xs[2]
    c.line(ax, py(ax) + 7, bx2, py(bx2) + 7); c.line(ax, py(ax) + 5, ax, py(ax) + 9); c.line(bx2, py(bx2) + 5, bx2, py(bx2) + 9)
    mx = (ax + bx2) / 2
    lab(mx + 5, py(mx) + 14, 'EXPOSURE', rot=-28.8, bg=True)

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

header(3); y = H - 92
section('Sketches', 'optional; photos work just as well')
y -= 2
rows3 = [('Plan view', 'Show the crossing from above: high banks, toes, the pipeline and its skew.', ex_plan),
         ('Cross section', 'Show the channel across the flow: bank-to-bank width, bottom width, depth, pipeline.', ex_xsec),
         ('Exposure', 'Show where the pipeline sits relative to the bed, and the flow direction.', ex_exposure)]
rh = (y - 52 - 2 * 10) / 3
ew = 205; gap = 12; gw = CW - ew - gap
for t, hint, fn in rows3:
    top = y; bot = y - rh
    # example panel
    c.setFillColor(MIST); c.setStrokeColor(HAZE); c.setLineWidth(.8); c.rect(M, bot, ew, rh, stroke=1, fill=1)
    c.setFillColor(SIGNAL); c.setFont('Helvetica-Bold', LAB); c.drawString(M + 8, top - 13, 'EXAMPLE')
    c.setFillColor(NAVY); c.setFont('Helvetica-Bold', 9); c.drawString(M + 8 + c.stringWidth('EXAMPLE', 'Helvetica-Bold', LAB) + 6, top - 13, t)
    c.setFillColor(white); c.rect(M + 6, bot + 6, ew - 12, rh - 26, stroke=0, fill=1)
    fn(M + 6, bot + 6, ew - 12, rh - 26)
    # sketch area with grid
    gx0 = M + ew + gap
    c.setFillColor(FIELD); c.setStrokeColor(HAZE); c.rect(gx0, bot, gw, rh, stroke=1, fill=1)
    c.setStrokeColor(HexColor('#ECEBEA')); c.setLineWidth(.4)
    gx = gx0 + 14
    while gx < gx0 + gw - 3: c.line(gx, bot + 3, gx, top - 32); gx += 14
    gy = bot + 14
    while gy < top - 32: c.line(gx0 + 3, gy, gx0 + gw - 3, gy); gy += 14
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(gx0 + 8, top - 13, (t + ' sketch').upper())
    c.setFont('Helvetica', 7); c.drawString(gx0 + 8, top - 24, hint)
    y = bot - 10
footer(); c.showPage()
c.save()
print('ok')
