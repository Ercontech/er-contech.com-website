"""Web version of the Er-Con Site Survey (contact page form). Imported by build.py."""

def _f(name, label, typ='text', req=False, full=False, ph='', auto=''):
    r = ' <span class="required">*</span>' if req else ''
    a = f' autocomplete="{auto}"' if auto else ''
    p = f' placeholder="{ph}"' if ph else ''
    rq = ' required' if req else ''
    cls = 'form-field full' if full else 'form-field'
    return (f'<div class="{cls}"><label for="{name}">{label}{r}</label>'
            f'<input id="{name}" name="{name}" type="{typ}"{a}{p}{rq}></div>')

def _checks(name, legend, opts):
    boxes = ''.join(f'<label class="sv-check"><input type="checkbox" name="{name}[]" value="{o}"><span>{o}</span></label>' for o in opts)
    return f'<fieldset class="sv-checks"><legend>{legend}</legend><div>{boxes}</div></fieldset>'

def _yn(name, q, follow=None):
    fl = (f'<input class="sv-follow" name="{name}_detail" type="text" placeholder="{follow}" aria-label="{follow}">'
          if follow else '')
    return (f'<div class="sv-yn"><span class="sv-q">{q}</span>'
            f'<label class="sv-check"><input type="radio" name="{name}" value="Yes"><span>Yes</span></label>'
            f'<label class="sv-check"><input type="radio" name="{name}" value="No"><span>No</span></label>{fl}</div>')

INDUSTRIES = ['Pipelines &amp; Energy', 'Transportation', 'Utilities',
              'Commercial &amp; Private Property', 'Other']

def survey_form():
    ind = ''.join(f'<option>{i}</option>' for i in INDUSTRIES)
    return f'''<form id="form" class="project-form sv-form" action="send.php" method="post" enctype="multipart/form-data" data-survey-form>
        <p class="sv-error" hidden data-missing="Please fill in your name, email, site location and what you're seeing, then send again." data-verify="We couldn't confirm the form was sent by a person. Please wait for the check above the Send button to finish, then send again.">Please fill in your name, email, site location and what you're seeing, then send again.</p>
        <input type="text" name="website" class="sv-hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <h2 class="sv-h">About you</h2>
        <div class="form-grid">
          {_f('name', 'Name', req=True, auto='name')}
          {_f('company', 'Company', auto='organization')}
          {_f('email', 'Email', 'email', req=True, auto='email')}
          {_f('phone', 'Phone', 'tel', auto='tel')}
        </div>

        <h2 class="sv-h">The site</h2>
        <div class="form-grid">
          {_f('location', 'Site location', req=True, ph='City and state, or coordinates')}
          <div class="form-field"><label for="industry">Industry</label><select id="industry" name="industry"><option value="">Choose one</option>{ind}</select></div>
          <div class="form-field full"><label for="details">What are you seeing? <span class="required">*</span></label><textarea id="details" name="details" required placeholder="What's happening at the site, what's at risk and any timing we should know about."></textarea></div>
          <div class="form-field full"><label for="photos">Photos</label>
            <label class="sv-drop" for="photos"><input id="photos" name="photos[]" type="file" accept="image/*,.pdf" multiple><span class="sv-drop-main">Add photos of the site</span><span class="sv-drop-sub">Up to 10 files, 25 MB total. Photos are the most helpful thing you can send.</span></label>
            <ul class="sv-files" aria-live="polite"></ul></div>
        </div>

        <details class="sv-more">
          <summary><span>Add site details</span><small>Optional. Fill in what you know, skip the rest.</small></summary>
          <div class="sv-more-body">
            <h3 class="sv-h3">Site</h3>
            <div class="form-grid sv-grid3">
              {_f('water', 'Body of water')}
              {_f('county', 'County')}
              {_f('project', 'Project name')}
              {_f('lat', 'Latitude')}
              {_f('long', 'Longitude')}
            </div>

            <h3 class="sv-h3">The erosion</h3>
            {_checks('erosion_type', 'Erosion type', ['Degradation', 'Head cutting', 'Lateral migration', 'Other'])}
            <div class="form-grid">{_f('flow_depth', 'Nominal depth of flow')}</div>
            <div class="sv-pair">
              {_checks('bed', 'Bed material', ['Clay', 'Rock', 'Gravel', 'Sand'])}
              {_checks('bank', 'Bank material', ['Clay', 'Rock', 'Gravel', 'Sand'])}
            </div>

            <h3 class="sv-h3">Pipeline</h3>
            {_yn('pipeline', 'Is a pipeline involved?')}
            <div class="sv-pipe" hidden>
              <div class="form-grid sv-grid3">
                {_f('pipe_company', 'Pipeline company')}
                {_f('line', 'Line name / number')}
                {_f('milepost', 'Milepost / station')}
                {_f('lines_row', 'Pipelines in right-of-way')}
                {_f('diameter', 'Pipeline diameter(s)')}
                {_f('exposure', 'Length of exposure')}
                {_f('span', 'Length of free span')}
              </div>
              {_yn('pipe_visible', 'Is the pipeline visible?')}
            </div>

            <h3 class="sv-h3">Access</h3>
            {_yn('row_cleared', 'Is the right-of-way cleared?')}
            {_yn('walk', 'Walk to site?', 'Distance walked')}
            {_yn('trees', 'Tree removal needed?', 'Number of trees / size')}
            {_yn('utilities', 'Other pipelines or utilities in the ROW?', 'Company name(s)')}
            {_yn('road_limits', 'Road or bridge weight limits?', 'Weight limits')}
            {_yn('power', 'Overhead power lines?')}
            {_yn('weather', 'Weather sensitive?', 'Explain')}
          </div>
        </details>

        <div class="sv-turnstile" hidden></div>
        <div class="form-actions"><button class="btn primary" type="submit">Send Site Details</button><p class="form-note">Your details go straight to our team.</p></div>
      </form>
      <script src="form-config.php"></script>'''

ASIDE = '''<aside class="contact-details">
        <h2>Talk with Er-Con.</h2>
        <a href="tel:+17134604601">+1 (713) 460-4601</a>
        <a href="mailto:info@er-contech.com">info@er-contech.com</a>
        <p>6715 Theall Road<br>Houston, TX 77066</p>
        <div class="photo-note"><strong>Prefer a form you can print?</strong><p>Download our site survey, fill it in on your computer or by hand, and email it back with your photos.</p>
        <a class="sv-pdf" href="assets/Er-Con-Site-Survey.pdf" download>Download the site survey (PDF)</a></div>
      </aside>'''

CSS = '''/* v0.96 site survey form */
.sv-error{margin:0 0 20px;padding:12px 16px;background:#fff3d6;border-left:4px solid var(--amber);color:var(--ink)}
.thanks-hero .contact-hero-inner p:last-child a{color:#fff;text-decoration:underline}
.sv-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.sv-h{color:var(--navy);font-size:20px;margin:0 0 16px}
.sv-form .form-grid+.sv-h,.sv-form .form-grid+details{margin-top:30px}
.sv-form select{width:100%;border:1px solid var(--fog);border-radius:3px;background:#fff;color:var(--ink);font:inherit;font-size:16px;padding:12px 14px}
.sv-form textarea{min-height:140px}
.sv-drop{position:relative;display:flex;flex-direction:column;gap:4px;border:2px dashed var(--haze);border-radius:4px;padding:22px;text-align:center;cursor:pointer;background:var(--mist)}
.sv-drop:hover{border-color:var(--signal)}
.sv-drop input{position:absolute;inset:0;opacity:0;cursor:pointer}
.sv-drop-main{color:var(--signal);font-weight:800}
.sv-drop-sub{color:var(--graphite);font-size:13px}
.sv-files{list-style:none;margin:8px 0 0;padding:0;color:var(--graphite);font-size:14px}
.sv-more{margin-top:30px;border-top:4px solid var(--navy);border-bottom:1px solid var(--haze)}
.sv-more summary{cursor:pointer;list-style:none;display:flex;align-items:baseline;gap:14px;padding:18px 0;flex-wrap:wrap}
.sv-more summary::-webkit-details-marker{display:none}
.sv-more summary span{color:var(--navy);font-size:20px;font-weight:800}
.sv-more summary span::before{content:"+";display:inline-block;width:22px;color:var(--signal)}
.sv-more[open] summary span::before{content:"\\2212"}
.sv-more summary small{color:var(--graphite);font-size:14px}
.sv-more-body{padding:4px 0 26px}
.sv-h3{color:var(--signal);font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;margin:24px 0 12px}
.sv-grid3{grid-template-columns:repeat(3,1fr)}
.sv-checks{border:0;margin:0 0 16px;padding:0}
.sv-checks legend{color:var(--navy);font-weight:800;font-size:14px;margin-bottom:8px;padding:0}
.sv-checks>div{display:flex;flex-wrap:wrap;gap:8px 20px}
.sv-check{display:inline-flex;align-items:center;gap:7px;color:var(--ink);font-size:15px;cursor:pointer}
.sv-check input{width:17px;height:17px;accent-color:var(--signal);margin:0}
.sv-pair{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:16px}
.sv-yn{display:flex;align-items:center;gap:8px 20px;flex-wrap:wrap;padding:10px 0;border-bottom:1px solid var(--mist)}
.sv-q{flex:0 0 300px;color:var(--ink);font-size:15px}
.sv-follow{flex:1 1 200px;border:1px solid var(--fog);border-radius:3px;font:inherit;font-size:15px;padding:8px 10px}
.sv-pipe .form-grid{margin:10px 0 6px}
.sv-turnstile{margin:26px 0 0;min-height:65px}
.sv-pdf{display:inline-block;margin-top:12px;color:var(--signal);font-weight:800}
.sv-pdf::before{content:"\\2193  "}
@media (max-width:900px){.sv-grid3,.sv-pair{grid-template-columns:1fr}.sv-q{flex-basis:100%}}
'''

JS = '''
// v0.96 site survey form: pipeline fields on demand, file list
(function () {
  var f = document.querySelector('[data-survey-form]'); if (!f) return;
  var err = f.querySelector('.sv-error'), m = location.search.match(/[?&]error=(\\w+)/);
  if (m) { err.textContent = err.getAttribute(m[1] === 'verify' ? 'data-verify' : 'data-missing'); err.hidden = false; }
  // v1.36 Cloudflare Turnstile: dormant until the site key is set on the server (form-config.php)
  var tsKey = window.ER_TURNSTILE_SITE_KEY, tsBox = f.querySelector('.sv-turnstile'), tsWaiting = false;
  if (tsKey && tsBox) {
    tsBox.hidden = false;
    window.erTurnstileReady = function () {
      turnstile.render(tsBox, { sitekey: tsKey, action: 'site-survey',
        callback: function () { if (tsWaiting) { tsWaiting = false; f.requestSubmit ? f.requestSubmit() : f.submit(); } } });
    };
    var ts = document.createElement('script');
    ts.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=erTurnstileReady';
    ts.async = true; ts.defer = true; document.head.appendChild(ts);
    f.addEventListener('submit', function (e) {
      var tok = f.querySelector('[name="cf-turnstile-response"]');
      if (window.turnstile && !(tok && tok.value)) { e.preventDefault(); tsWaiting = true; }
    });
  }
  var pipe = f.querySelector('.sv-pipe'), ind = f.querySelector('#industry');
  function syncPipe() {
    var yes = (f.querySelector('input[name="pipeline"]:checked') || {}).value === 'Yes';
    pipe.hidden = !(yes || (ind && ind.value.indexOf('Pipelines') === 0));
  }
  f.querySelectorAll('input[name="pipeline"]').forEach(function (r) { r.addEventListener('change', syncPipe); });
  if (ind) ind.addEventListener('change', syncPipe);
  var input = f.querySelector('#photos'), list = f.querySelector('.sv-files');
  if (input) input.addEventListener('change', function () {
    list.innerHTML = '';
    Array.prototype.forEach.call(input.files, function (file) {
      var li = document.createElement('li'); li.textContent = file.name + ' (' + Math.round(file.size / 1024) + ' KB)'; list.appendChild(li);
    });
  });
})();
'''
