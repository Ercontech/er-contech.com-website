import re, glob, os, sys
sys.path.insert(0, '/home/claude/site')
from content import SERVICES, SYSTEMS, SHORT, INDUSTRIES, DISCIPLINES, PAIRS, EVIDENCE, GALLERY, GALLERY_ORDER, GALLERY_FIRST, GALLERY_LEAD

D = '/home/claude/site/dist'
os.chdir(D)

def read(f): return open(f, encoding='utf-8').read()
def write(f, s): open(f, 'w', encoding='utf-8').write(s)

PRODUCTS = ['palisade.html', 'fcr.html', 'ercoform.html', 'eco-flex.html', 'system-21.html', 'pipeline-supports.html']
JOBS = ['civil-designer.html', 'field-construction-technician.html', 'project-manager.html', 'regional-account-manager.html']

# ---------------------------------------------------------------- nav
def nav(current):
    cur = lambda k: ' aria-current="page"' if current == k else ''
    subs = ''.join(
        f'<a href="{i["slug"]}.html"{cur(i["slug"])}>{i["name"]}</a>' for i in INDUSTRIES)
    ind_cur = ' aria-current="page"' if current in [i['slug'] for i in INDUSTRIES] else ''
    return ('<nav id="main-nav" class="main-nav" aria-label="Main navigation">\n'
            f'        <div class="nav-group"><a class="nav-top" href="index.html#industries"{ind_cur}>Industries</a><div class="nav-sub">{subs}</div></div>'
            f'<a href="services.html"{cur("services")}>Services</a><a href="about.html"{cur("about")}>About</a>'
            f'<a href="safety.html"{cur("safety")}>Safety</a>'
            f'<a href="careers.html"{cur("careers")}>Careers</a><a href="contact.html"{cur("contact")}>Contact</a>\n'
            '      </nav>')

NAV_RE = re.compile(r'<nav id="main-nav".*?</nav>', re.S)

def page_key(f):
    if f == 'index.html': return 'home'
    if f in PRODUCTS or f == 'services.html': return 'services'
    if f in JOBS or f == 'careers.html': return 'careers'
    return f[:-5]

# ---------------------------------------------------------------- shared blocks
def contact_card(btn='Start a Conversation'):
    return ('<div class="contact-card"><a href="tel:+17134604601">+1 (713) 460-4601</a>'
            '<a href="mailto:info@er-contech.com">info@er-contech.com</a>'
            '<p>6715 Theall Road<br>Houston, TX 77066</p>'
            f'<a class="btn primary" href="contact.html">{btn}</a></div>')

def industry_tiles():
    # Quiet tiles (Ron, 2026-10-05, layout A): one photo and the industry name each,
    # one row of five, a plain "Not sure where you fit?" line beneath the grid.
    out = []
    for i in INDUSTRIES:
        out.append(
            f'<a class="industry-tile" href="{i["slug"]}.html">'
            f'<div class="industry-tile-photo"><img src="{i["tile_img"]}" alt="{i["tile_alt"]}">'
            + (f'<img class="tile-before" src="{i["tile_before"]}" alt="" aria-hidden="true"><span class="tile-before-tag">Before</span>' if i.get("tile_before") else '') + '</div>'
            + f'<div class="industry-tile-body"><h3>{i["name"]}</h3></div></a>')
    return '\n          '.join(out)

INDUSTRY_ASK = '<p class="industry-ask">Not sure where you fit? <a href="contact.html">Tell us what you\'re seeing →</a></p>'

def investigation(heading_tag='h2'):
    cols = ''.join(f'<article class="discipline"><h3>{n}</h3><p>{d}</p></article>' for n, d in DISCIPLINES)
    return f'''<section class="investigation" id="site-investigation" aria-labelledby="investigation-title">
      <div class="investigation-inner">
        <div class="investigation-heading">
          <div class="investigation-row"><{heading_tag} id="investigation-title">We are water<br>experts.</{heading_tag}><p>Every project starts with a site investigation. Before we design anything, we study how water reaches the site, what it does there and where it goes.</p></div>
        </div>
        <div class="discipline-grid">{cols}</div>
      </div>
    </section>'''

def solution_card(k):
    href, name, typ, desc, img, alt, link = SYSTEMS[k]
    return (f'<a class="solution-card" href="{href}"><div class="solution-card-body"><p class="solution-type">{typ}</p>'
            f'<h3>{name}</h3><p>{desc}</p></div><img class="solution-card-image" src="{img}" alt="{alt}">'
            f'<span class="solution-link">{link}</span></a>')

# ---------------------------------------------------------------- 1. nav on every existing page
for f in sorted(glob.glob('*.html')):
    s = read(f)
    s = NAV_RE.sub(nav(page_key(f)), s, count=1)
    write(f, s)

# ---------------------------------------------------------------- 2. home page
s = read('index.html')
s = s.replace('engineering, permitting and installation services across', 'engineering, permitting and construction services across')
s = s.replace('from field investigation and permitting through installation', 'from site investigation and permitting through construction')
# The hero is a flat navy block: no photograph. The industry tiles below are the
# first photography on the page, so they are not competing with a hero image.
s = s.replace('<section class="hero">', '<section class="hero hero-compact hero-navy">')
s = re.sub(r'\s*<div class="hero-overlay"></div>', '', s)
assert 'hero-overlay' not in s
# Slim hero (Ron, 2026-10-05): title and statement only - no eyebrow, no accent line, sentence case
s = s.replace('<h1>Engineered Erosion Mitigation &<br>Bank Stabilization</h1>', '<h1>Engineered erosion mitigation <br>and bank stabilization.</h1>')
s = re.sub(r'\s*<p class="eyebrow">Backed by more than 50 years of field experience</p>', '', s)
s = re.sub(r'\s*<span class="accent-line"></span>', '', s, count=1)
assert 'erosion mitigation <br>' in s and 'Backed by more' not in s
# The statement replaces the old lead, inside the navy hero under the accent line
s = re.sub(r'\s*<p class="lead">.*?</p>', '', s, flags=re.S)
s = s.replace('<h1>Engineered erosion mitigation <br>and bank stabilization.</h1>', '<h1>Engineered erosion mitigation <br>and bank stabilization.</h1>\n          <p class="hero-statement">Protecting and preserving critical infrastructure and assets: pipelines, roads and rail, public works, utilities, and commercial and private property.</p>', 1)
assert 'hero-statement' in s
# no hero buttons: the industry tiles sit directly below and are the call to action
s = re.sub(r'\s*<div class="hero-actions">.*?</div>', '', s, flags=re.S)
assert 'hero-actions' not in s

industries_section = f'''<section class="industry-picker" id="industries" aria-labelledby="industries-title">
      <div class="industry-picker-inner">
        <div class="industry-picker-heading">
          <h2 id="industries-title">Industry<br>Applications</h2>
        </div>
        <div class="industry-grid">
          {industry_tiles()}
        </div>
        {INDUSTRY_ASK}
      </div>
    </section>'''

# stats move below the picker; the product-led "critical applications" block is replaced
stats = re.search(r'\s*<section class="stats".*?</section>', s, re.S).group(0)
s = s.replace(stats, '')
s = re.sub(r'<section class="section intro" id="about">.*?</section>', industries_section + '\n\n    ' + investigation(), s, flags=re.S)
# stats sit between the engineering callout and local partnerships, so the two navy bands never touch
s = s.replace('\n\n    <section class="local-partnerships">', stats + '\n\n    <section class="local-partnerships">', 1)
assert 'class="stats"' in s

svc_cards = '\n        '.join(
    f'<article class="service-card"><h3>{n}</h3><p>{d}</p></article>' for k, n, d in SERVICES)
s = re.sub(r'<section class="services section dark" id="services">.*?</section>',
           f'''<section class="services section dark" id="services">
      <div class="section-heading light"><p class="eyebrow">How we work</p><h2>One team, from site investigation through construction.</h2><p>Whatever the industry, every project follows the same six steps, and our own people carry it through each one. Nothing is handed off to another firm along the way.</p></div>
      <div class="service-grid">
        {svc_cards}
      </div>
      <div class="services-more"><a class="btn primary" href="services.html">See Our Services</a></div>
    </section>''', s, flags=re.S)
write('index.html', s)

# ---------------------------------------------------------------- 3. services page
s = read('services.html')
s = s.replace('<title>Erosion Mitigation Solutions | Er-Con Technologies</title>',
              '<title>Services | Er-Con Technologies</title>')
svc_list = '\n          '.join(
    f'<article class="service-item" id="{k}"><h3>{n}</h3><p>{d}</p></article>' for k, n, d in SERVICES)
services_section = f'''<section class="section service-detail" aria-labelledby="services-title">
      <div class="service-detail-heading">
        <h2 id="services-title">One team, from site investigation through construction.</h2>
        <p>Every Er-Con project runs through the same in-house teams. The work is not handed from a consultant to a supplier to a contractor, so the people who define the problem are the ones who solve it.</p>
      </div>
      <div class="service-list">
          {svc_list}
      </div>
    </section>

    '''
s = s.replace('<section class="solutions-section">', investigation() + '\n\n    ' + services_section + '<section class="solutions-section" id="systems">', 1)
# No product talk (Ron, 2026-09-28): the systems section and "Additional capabilities" come out
s = re.sub(r'<section class="solutions-section" id="systems">.*?</section>\s*', '', s, count=1, flags=re.S)
s = re.sub(r'<section class="section supporting-methods">.*?</section>\s*', '', s, count=1, flags=re.S)
assert 'solution-card' not in s and 'supporting-methods' not in s
s = s.replace('before recommending the right system or combination of systems.', 'before recommending the right solution.')
s = s.replace('<article class="framework-step"><h3>Install</h3><p>Complete the work in the field.</p></article>', '<article class="framework-step"><h3>Build</h3><p>Construct the solution in the field.</p></article>')
assert '<h3>Install</h3>' not in s
assert 'combination of systems' not in s
s = s.replace('<p class="eyebrow blue">Core erosion-control solutions</p>', '<p class="eyebrow blue">The systems behind our services</p>')
industries_strip = f'''<section class="industry-picker industry-picker-compact" aria-labelledby="serve-title">
      <div class="industry-picker-inner">
        <div class="industry-picker-heading">
          <h2 id="serve-title">Industry<br>Applications</h2>
        </div>
        <div class="industry-grid">
          {industry_tiles()}
        </div>
        {INDUSTRY_ASK}
      </div>
    </section>

    '''
s = s.replace('<section class="cta">', industries_strip + '<section class="cta">', 1)
write('services.html', s)

# ---------------------------------------------------------------- 4. product pages: back to services
for f in PRODUCTS:
    s = read(f)
    s = s.replace('<a class="back-link" href="services.html">← Back to Solutions</a>',
                  '<a class="back-link" href="services.html">← Back to Services</a>')
    write(f, s)

# ---------------------------------------------------------------- 5. industry pages
head_tpl = read('palisade.html').split('<main>')[0]
foot_tpl = '</main>' + read('palisade.html').split('</main>')[1]

def switcher(cur):
    AC = ' aria-current="page"'
    return ''.join(f'<a href="{i["slug"]}.html"{AC if i["slug"] == cur else ""}>{i["short"]}</a>' for i in INDUSTRIES)

for i in INDUSTRIES:
    head = head_tpl
    plain = i['name'].replace('&amp;', '&')
    head = re.sub(r'<title>.*?</title>', f'<title>{i["name"]} | Er-Con Technologies</title>', head)
    head = re.sub(r'<meta name="description" content=".*?">',
                  f'<meta name="description" content="Erosion problems Er-Con solves for {plain.lower()}, and the engineering, permitting and construction services that solve them.">', head)
    head = NAV_RE.sub(nav(i['slug']), head)

    rows = []
    for n, (title, see, cause, solve, systems) in enumerate(i['problems'], 1):
        rows.append(f'''<article class="problem-row">
            <div class="problem-cell problem-see"><span class="problem-label">What you're seeing</span><h3>{title}</h3><p>{see}</p></div>
            <div class="problem-cell problem-cause"><span class="problem-label">What's driving it</span><p>{cause}</p></div>
            <div class="problem-cell problem-solve"><span class="problem-label">How we solve it</span><p>{solve}</p></div>
          </article>''')
    rows = '\n          '.join(rows)

    steps = ''.join(f'<li><a href="services.html#{k}">{n}</a></li>' for k, n, d in SERVICES)
    first = GALLERY_FIRST.get(i['slug'], [])
    order = first + [k for k in GALLERY_ORDER if k not in first]
    gcards = []
    for k in order:
        b_, balt, a_, aalt, story = GALLERY[k][:5]
        t1, t2 = GALLERY[k][5] if len(GALLERY[k]) > 5 else ("Before", "After")
        gcards.append(f'''<article class="g-card">
            <div class="evidence-pair">
              <figure><div class="evidence-photo"><img src="{b_}" alt="{t1}: {balt}" loading="lazy"><span class="ba-tag">{t1}</span></div></figure>
              <figure><div class="evidence-photo"><img src="{a_}" alt="{t2}: {aalt}" loading="lazy"><span class="ba-tag">{t2}</span></div></figure>
            </div>
            <p class="evidence-story">{story}</p>
          </article>''')
    cases = '\n          '.join(gcards)
    eyebrow = 'Industries' + (f' · {i["sub"]}' if i.get('sub') else '')
    lower = i['name'].lower()

    body = f'''<main>
    <section class="product-hero industry-hero industry-hero-{i["slug"]}">
      <div class="product-hero-overlay"></div>
      <div class="product-hero-inner">
        <a class="back-link" href="index.html#industries">← All Industries</a>
        <p class="eyebrow">{eyebrow}</p>
        <h1>{i["name"]}</h1>
        <p class="product-hero-statement">{i["statement"]}</p>
        <p class="product-hero-lead">{i["lead"]}</p>
        <a class="btn primary" href="contact.html">Discuss Your Site</a>
      </div>
    </section>

    <nav class="industry-switch" aria-label="Industries">
      <div class="industry-switch-inner">{switcher(i["slug"])}</div>
    </nav>

    <section class="section problems" aria-labelledby="problems-title">
      <div class="problems-heading">
        <div class="problems-row"><h2 id="problems-title">What we see in {lower}.</h2></div>
      </div>
      <div class="problem-table">
        <div class="problem-head" aria-hidden="true"><span>What you're seeing</span><span>What's driving it</span><span>How we solve it</span></div>
          {rows}
      </div>
    </section>

    <section class="evidence" aria-labelledby="evidence-title">
      <div class="evidence-inner">
        <div class="g-head">
          <p class="eyebrow blue" id="evidence-title">In the field</p>
          <div class="g-nav"><span class="g-count" aria-live="polite"></span><button class="g-btn" type="button" data-d="-1" aria-label="Previous projects">←</button><button class="g-btn" type="button" data-d="1" aria-label="Next projects">→</button></div>
        </div>
        <div class="g-viewport"><div class="g-track">
          {cases}
        </div></div>
      </div>
    </section>

    <section class="service-band" aria-labelledby="band-title">
      <div class="service-band-inner">
        <div class="service-band-copy">
          <p class="eyebrow">How we work</p>
          <h2 id="band-title">One team, from site investigation through construction.</h2>
          <p>Whatever the industry, every project follows the same six steps, and our own people carry it through each one. Nothing is handed off to another firm along the way.</p>
        </div>
        <ol class="service-band-steps">{steps}</ol>
      </div>
    </section>

    <section class="cta">
      <div><p class="eyebrow">{i["cta_eyebrow"]}</p><h2>Tell us what you're seeing.</h2><p>Send us the location, what concerns you and any photos, surveys or history you have. We'll help determine the right path forward.</p></div>
      {contact_card()}
    </section>
  '''
    write(f'{i["slug"]}.html', head + body + foot_tpl)

# ---------------------------------------------------------------- 5b. safety page (v0.78)
from content import SAFETY_GROUPS
_t = read('services.html')
s_head, s_foot = _t[:_t.index('<main>')], _t[_t.index('</main>') + 7:]
s_head = re.sub(r'<title>.*?</title>', '<title>Safety | Er-Con Technologies</title>', s_head, flags=re.S)
s_head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Moments Matter. How Er-Con keeps its crews safe before, during and after every job.">', s_head)
s_head = NAV_RE.sub(nav('safety'), s_head, count=1)
rows = ''
for g, items in SAFETY_GROUPS:
    cells = ''.join(f'<div class="sp-item"><h3>{t}</h3><p>{d}</p></div>' for t, d in items)
    rows += f'\n        <div class="sp-row"><h3 class="sp-group">{g}</h3><div class="sp-items">{cells}</div></div>'
s_main = f"""<main>
    <section class="hero hero-compact hero-navy safety-hero">
      <div class="hero-inner"><div class="hero-copy">
        <h1>Moments Matter<span class="sp-dot">.</span></h1>
        <p class="hero-statement">A job is made of small moments: where to stand, what to watch and, most importantly, when to say stop. Our safety program is built so every person on our crews gets those moments right, and goes home the way they arrived.</p>
      </div></div>
    </section>

    <section class="section sp-intro" aria-labelledby="sp-title">
      <div class="sp-intro-row">
        <h2 id="sp-title">Safety starts<br>before the work does.</h2>
        <p>Before a crew sets foot on site, they know its hazards, the client's requirements and the plan for the day. On site, the plan is checked every morning, and anyone can stop the work when something isn't right.</p>
      </div>
      <div class="sp-table">{rows}
      </div>
    </section>

    <section class="sp-stop" aria-label="Stop Work Authority">
      <div class="sp-stop-inner">
        <p class="sp-stop-label">Stop Work Authority</p>
        <p class="sp-stop-quote">The most important moment on any job is the one where someone says stop.</p>
        <p class="sp-stop-body">On an Er-Con site, a new hire has the same right to stop the job as the person running it. If something doesn't feel right, we want to hear it, and nobody gets grief for speaking up. Work starts again when it's safe to proceed, not a moment before.</p>
      </div>
    </section>

    <section class="cta">
      <div><p class="eyebrow">Prequalifying a contractor?</p><h2>Ask for our safety program.</h2><p>Send us your prequalification requirements. We'll provide our safety program, our record and our certifications.</p></div>
      {contact_card()}
    </section>
  </main>"""
write('safety.html', s_head + s_main + s_foot)

# ---------------------------------------------------------------- 5c. new photos + gallery script (v0.83)
import shutil
shutil.copytree('/home/claude/site/newassets', 'assets', dirs_exist_ok=True)
_js = read('script.js')
if 'g-track' not in _js:
    _js += """
// v0.83 In the field gallery: step through before/after jobs, no autoplay
document.querySelectorAll('.g-evidence, .evidence').forEach(function (sec) {
  var track = sec.querySelector('.g-track'); if (!track) return;
  var cards = Array.prototype.slice.call(track.children), btns = sec.querySelectorAll('.g-btn'), count = sec.querySelector('.g-count'), i = 0;
  function per() { return window.matchMedia('(max-width: 900px)').matches ? 1 : 2; }
  function go() {
    var p = per(), max = Math.max(0, cards.length - p); i = Math.max(0, Math.min(i, max));
    var w = cards[0].getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 0);
    track.style.transform = 'translateX(' + (-i * w) + 'px)';
    btns[0].disabled = i === 0; btns[1].disabled = i >= max;
    count.textContent = p === 1 ? (i + 1) + ' of ' + cards.length : (i + 1) + '–' + (i + p) + ' of ' + cards.length;
    cards.forEach(function (c, n) { c.setAttribute('aria-hidden', n < i || n >= i + p ? 'true' : 'false'); });
  }
  btns.forEach(function (b) { b.addEventListener('click', function () { i += (+b.dataset.d) * per(); go(); }); });
  window.addEventListener('resize', go); go();
});
"""
    write('script.js', _js)

# ---------------------------------------------------------------- 5d. contact form = web site survey (v0.96)
import sys as _sys
_sys.path.insert(0, '/home/claude/site')
from survey_form import survey_form, ASIDE as SV_ASIDE, JS as SV_JS
_c = read('contact.html')
_c, _n1 = re.subn(r'<form class="project-form".*?</form>', lambda m: survey_form(), _c, count=1, flags=re.S)
_c, _n2 = re.subn(r'<aside class="contact-details">.*?</aside>', lambda m: SV_ASIDE, _c, count=1, flags=re.S)
assert _n1 == 1 and _n2 == 1
write('contact.html', _c)
# thank-you page, from the contact page shell
_t = re.sub(r'<title>.*?</title>', '<title>Thank You | Er-Con Technologies</title>', _c, flags=re.S)
_t = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="robots" content="noindex">', _t)
_t = _t[:_t.index('<main>')] + """<main>
    <section class="contact-hero thanks-hero">
      <div class="contact-hero-inner">
        <h1>Thanks. We have <span>your site details.</span></h1>
        <p>Someone from our team will be in touch. If it's urgent, call us at <a href="tel:+17134604601">+1 (713) 460-4601</a>.</p>
      </div>
    </section>
    <section class="section"><p><a class="btn primary" href="index.html">Back to the Home Page</a></p></section>
  </main>""" + _t[_t.index('</main>') + 7:]
_t = NAV_RE.sub(nav('contact'), _t, count=1)
write('thank-you.html', _t)
import shutil as _sh
for _f in os.listdir('/home/claude/site/newassets_root'):
    _sh.copy('/home/claude/site/newassets_root/' + _f, _f)
_js = read('script.js')
if 'data-survey-form' not in _js:
    write('script.js', _js + SV_JS)

# ---------------------------------------------------------------- 6. css
css = read('styles.css')
marker = '/* ===== v0.50 Industry-first structure ===== */'
css = css.split(marker)[0].rstrip() + '\n\n' + marker + '\n' + read('/home/claude/site/add.css')
bg = '\n'.join(f'.industry-hero-{i["slug"]}{{background-image:url(\'{i["img"]}\');background-position:{i["pos"]}}}' for i in INDUSTRIES)
write('styles.css', css + '\n' + bg + '\n')
print('built')
exec(open('/home/claude/site/copypass.py').read())
