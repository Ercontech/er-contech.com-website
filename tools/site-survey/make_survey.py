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

section('Sketches', 'optional; photos work just as well')
sh = y - 54                         # sketch box height down to footer
bw = (CW - 14) / 2
for i, t in enumerate(['Cross section', 'Exposure']):
    x = M + i * (bw + 14)
    c.setStrokeColor(HAZE); c.setLineWidth(.8); c.setFillColor(FIELD)
    c.rect(x, 54, bw, sh, stroke=1, fill=1)
    c.setFillColor(GRAPHITE); c.setFont('Helvetica-Bold', LAB); c.drawString(x + 8, 54 + sh - 13, t.upper() + ' SKETCH')
    # light grid
    c.setStrokeColor(HexColor('#ECEBEA')); c.setLineWidth(.4)
    gx = x + 18
    while gx < x + bw - 4:
        c.line(gx, 58, gx, 54 + sh - 20); gx += 18
    gy = 58 + 18
    while gy < 54 + sh - 20:
        c.line(x + 4, gy, x + bw - 4, gy); gy += 18
footer(); c.showPage()
c.save()
print('ok')
