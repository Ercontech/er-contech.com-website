const btn=document.querySelector('.menu-btn');const nav=document.querySelector('.main-nav');btn?.addEventListener('click',()=>{const open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open)});nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');btn?.setAttribute('aria-expanded','false')}));

const featuredProject=document.querySelector('[data-project-featured]');
const projectSelectors=document.querySelectorAll('[data-project-selector]');

const readProject=card=>({
  src:card.querySelector('img').getAttribute('src'),
  alt:card.querySelector('img').getAttribute('alt'),
  category:card.querySelector('.project-caption span').textContent,
  title:card.querySelector('.project-caption strong').textContent
});

const writeProject=(card,project)=>{
  const image=card.querySelector('img');
  image.setAttribute('src',project.src);
  image.setAttribute('alt',project.alt);
  card.querySelector('.project-caption span').textContent=project.category;
  card.querySelector('.project-caption strong').textContent=project.title;
};

projectSelectors.forEach(selector=>selector.addEventListener('click',()=>{
  if(!featuredProject)return;
  const featured=readProject(featuredProject);
  const selected=readProject(selector);
  writeProject(featuredProject,selected);
  writeProject(selector,featured);
  selector.setAttribute('aria-label',`Show ${featured.title} as the featured project`);
  [featuredProject,selector].forEach(card=>{
    card.classList.remove('is-changing');
    void card.offsetWidth;
    card.classList.add('is-changing');
  });
}));

const projectForm=document.querySelector('[data-project-form]');
projectForm?.addEventListener('submit',event=>{
  event.preventDefault();
  const data=new FormData(projectForm);
  const name=[data.get('first-name'),data.get('last-name')].filter(Boolean).join(' ');
  const subject=`Project inquiry${data.get('project-location')?` - ${data.get('project-location')}`:''}`;
  const body=[
    `Name: ${name}`,
    `Company: ${data.get('company')||'Not provided'}`,
    `Email: ${data.get('email')}`,
    `Phone: ${data.get('phone')||'Not provided'}`,
    `Project location: ${data.get('project-location')||'Not provided'}`,
    '',
    'Project details:',
    data.get('project-details')
  ].join('\n');
  window.location.href=`mailto:info@er-contech.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
});

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

// v0.96 site survey form: pipeline fields on demand, file list
(function () {
  var f = document.querySelector('[data-survey-form]'); if (!f) return;
  if (/[?&]error=/.test(location.search)) f.querySelector('.sv-error').hidden = false;
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
