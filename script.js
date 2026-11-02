const nav=document.querySelector('.site-nav');const menu=document.querySelector('.menu-btn');const links=document.querySelector('.nav-links');menu?.addEventListener('click',()=>{const o=links.classList.toggle('open');menu.setAttribute('aria-expanded',o)});links?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));window.addEventListener('scroll',()=>nav?.classList.toggle('scrolled',scrollY>20),{passive:true});document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){const d=e.target.dataset.delay||0;e.target.style.transitionDelay=d+'ms';e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -50px'});document.querySelectorAll('.reveal').forEach(el=>io.observe(el));const glow=document.querySelector('.cursor-glow');if(glow&&matchMedia('(pointer:fine)').matches){window.addEventListener('mousemove',e=>{glow.style.opacity='1';glow.style.transform=`translate(${e.clientX-210}px,${e.clientY-210}px)`})}document.querySelectorAll('.tilt').forEach(card=>{if(!matchMedia('(pointer:fine)').matches)return;card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5;const y=(e.clientY-r.top)/r.height-.5;card.style.transform=`perspective(1200px) rotateX(${y*-2.5}deg) rotateY(${x*3.5}deg) translateY(-2px)`});card.addEventListener('mouseleave',()=>card.style.transform='')});document.querySelectorAll('.magnetic').forEach(btn=>{if(!matchMedia('(pointer:fine)').matches)return;btn.addEventListener('mousemove',e=>{const r=btn.getBoundingClientRect();btn.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.08}px,${(e.clientY-r.top-r.height/2)*.08}px)`});btn.addEventListener('mouseleave',()=>btn.style.transform='')});
// Case-study section index: lets readers jump directly to the parts they need.
(()=>{
  const content=document.querySelector('#case-content');
  if(!content)return;
  const sections=[...content.querySelectorAll('section.case-section')];
  if(!sections.length)return;
  const tidy=s=>s.replace(/\s+/g,' ').trim();
  const labelFor=section=>{
    const eyebrow=section.querySelector('.eyebrow');
    let label=tidy(eyebrow?.textContent||section.querySelector('h2')?.textContent||'Section');
    const aliases={
      'Summary':'Overview','Issue tree':'Problem framing','Protocol design':'Research approach',
      'Discovery process':'Research approach','Research synthesis':'Key insights',
      'Proposed target-state journey':'User journey','From sketches to high-fidelity design':'Interface design',
      'Key decisions and trade-offs':'Design decisions','Outcome / learnings':'Outcome and learnings',
      'Who this concept is for':'Target users','How might we':'Research goal',
      'Competitor analysis':'Competitor audit','Information architecture':'Information architecture',
      'Proposed user journey':'User journey','Success metrics':'Measuring success'
    };
    return aliases[label]||label;
  };
  const used=new Set();
  sections.forEach((section,i)=>{
    if(!section.id)section.id=`case-section-${i+1}`;
    let label=labelFor(section),candidate=label,n=2;
    while(used.has(candidate)){candidate=`${label} ${n++}`;}
    used.add(candidate);section.dataset.sectionLabel=candidate;
  });
  const aside=document.createElement('aside');
  aside.className='case-section-index';
  aside.setAttribute('aria-label','Case study section navigation');
  const title=document.createElement('span');title.textContent='ON THIS PAGE';
  const list=document.createElement('nav');list.setAttribute('aria-label','Jump to section');
  const links=[];
  sections.forEach(section=>{
    const a=document.createElement('a');a.href=`#${section.id}`;a.textContent=section.dataset.sectionLabel;
    a.addEventListener('click',()=>{mobilePanel?.classList.remove('is-open');toggle?.setAttribute('aria-expanded','false');});
    list.append(a);links.push(a);
  });
  aside.append(title,list);document.body.append(aside);
  const toggle=document.createElement('button');toggle.className='case-section-toggle';toggle.type='button';toggle.textContent='Jump to section';toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-controls','case-section-index-panel');
  const mobilePanel=document.createElement('div');mobilePanel.className='case-section-mobile-panel';mobilePanel.id='case-section-index-panel';
  const mobileList=list.cloneNode(true);
  mobileList.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{mobilePanel.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');}));
  mobilePanel.append(mobileList);document.body.append(toggle,mobilePanel);
  toggle.addEventListener('click',()=>{const open=mobilePanel.classList.toggle('is-open');toggle.setAttribute('aria-expanded',String(open));});
  const observer=new IntersectionObserver(entries=>{
    entries.forEach(entry=>{
      if(!entry.isIntersecting)return;
      const index=sections.indexOf(entry.target);
      links.forEach((a,i)=>i===index?a.setAttribute('aria-current','location'):a.removeAttribute('aria-current'));
      mobileList.querySelectorAll('a').forEach((a,i)=>i===index?a.setAttribute('aria-current','location'):a.removeAttribute('aria-current'));
    });
  },{rootMargin:'-18% 0px -65% 0px',threshold:0});
  sections.forEach(section=>observer.observe(section));
})();
