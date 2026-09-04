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
