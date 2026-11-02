from pathlib import Path
import re, shutil, os
root=Path('/tmp/velwork')
html='''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><meta name="description" content="Velocity Rewards MVP case study presented as a responsive web slide deck."/><title>Velocity Rewards MVP | Stanslous Nhau</title><link href="stan-logo.svg" rel="icon" type="image/svg+xml"/><link href="styles.css?v=velocity-deck-01" rel="stylesheet"/></head>
<body class="case-page velocity-case velocity-deck-page"><div aria-hidden="true" class="cursor-glow"></div>
<header class="site-nav"><div class="wrap nav-inner"><a class="brand" href="index.html">STAN<span>.</span></a><nav aria-label="Primary" class="nav-links"><a href="index.html#work">Work</a><a href="index.html#about">About</a><a href="index.html#contact">Contact</a><a class="nav-cv" download="" href="assets/Stanslous_Nhau_CV.pdf">Download CV</a></nav><button aria-expanded="false" aria-label="Open navigation" class="menu-btn">☰</button></div></header>
<main>
<section class="velocity-deck-intro"><div class="wrap"><a class="back-link" href="index.html#work">← Selected work</a><div class="eyebrow">Case Study 03 · UX Designer</div><h1>Velocity Rewards MVP</h1><p>Designing a petrol-retail rewards experience around the real rhythm of a fuel stop.</p><div class="velocity-deck-meta"><span>Individual concept</span><span>Competitor audit</span><span>Product strategy + UI</span><span>Johannesburg pilot concept</span></div><div class="velocity-deck-tools"><span>Original presentation, rebuilt as a responsive web case study</span><a href="#slide-1">Start the case study ↓</a></div></div></section>
<section class="velocity-deck-wrap" aria-label="Velocity case study presentation">
<div class="velocity-deck-topline"><span>VELOCITY REWARDS MVP</span><span id="velocity-slide-count">01 / 24</span></div>
<div class="velocity-slide-list">
'''
slides=[
(1,'Shell Velocity Rewards MVP. Designing a petrol-retail rewards experience around the real rhythm of a fuel stop.'),
(2,'Contents: project framing; research and competitor signal; behavioural archetypes; hypotheses and MVP definition; success model; journey and interaction design; final UI and next iteration.'),
(3,'Opening story about Lindiwe, a regular Shell customer who cannot see or use the rewards she has earned.'),
(4,'The problem and opportunity: card-bound rewards are difficult to see and use, with no easy digital way to tip fuel attendants.'),
(5,'Research method: audit of fuel-retail and adjacent high-frequency loyalty models. Scope and constraints of self-directed concept research.'),
(6,'Full competitive audit, part one: Sasol Rewards, BP Rewards and Engen 1App.'),
(7,'Full competitive audit, part two: eBucks, Discovery Vitality and Tappy.'),
(8,'Market audit synthesis: visibility, usable value, tipping integration and redemption flexibility.'),
(9,'Lindiwe Sibanda persona: balance- and value-conscious parent. Hypothesis archetype based on market patterns, not user interviews.'),
(11,'Jabulani Dube persona: regular, generous loyalist. Hypothesis archetype based on market patterns, not user interviews.'),
(12,'What the archetypes point to: customer control over payment method, redemption and generosity.'),
(13,'Four hypotheses to validate first: visibility, card-agnostic earning, cash-out and digital tipping.'),
(14,'MVP definition: see it, use it now, pay my way and thank clearly.'),
(15,'Core MVP success matrix: repeat engagement is the primary measure, with sign-up and redemption as supporting signals.'),
(16,'The digital flow mirrors the physical station journey: launch, sign-in, dashboard, fuel payment, rewards, tipping and wallet.'),
]
# Add actual web-native slide cards. Source deck slides are retained visually at presentation fidelity.
for i,alt in slides:
    html+=f'''<article class="velocity-slide" id="slide-{i}" data-slide="{i}"><div class="velocity-slide-frame"><img src="assets/velocity-web-slides/slide-{i:02d}.webp" alt="{alt}" loading="{'eager' if i==1 else 'lazy'}"/><span class="velocity-slide-index">{i:02d}</span></div></article>\n'''
# Replace the removed 32-screen inventory slide with the two actual exploration artefacts already selected for the portfolio.
html+='''<article class="velocity-slide velocity-artifact-slide" id="slide-ui-lowfi" data-slide="17"><div class="velocity-artifact-frame"><div class="velocity-artifact-heading"><span>DESIGN EXPLORATION</span><h2>From flow structure to interface exploration.</h2><p>Low-fidelity screens explore the core tasks before the visual design is applied.</p></div><img src="assets/case-velocity/velocity-low-fidelity-exploration.png" alt="Low-fidelity Velocity screens exploring attendant identification, payment, rewards, withdrawal and redemption." loading="lazy"/><span class="velocity-slide-index">17</span></div></article>
<article class="velocity-slide velocity-artifact-slide" id="slide-ui-highfi" data-slide="18"><div class="velocity-artifact-frame"><div class="velocity-artifact-heading"><span>HIGH-FIDELITY UI</span><h2>Make rewards and service actions tangible.</h2><p>The interface exploration brings balance visibility, redemption, payment freedom and digital tipping into one experience.</p></div><img src="assets/case-velocity/velocity-high-fidelity-screens.png" alt="High-fidelity Velocity mobile screens for rewards, redemption, pay it forward tipping, attendant scanning and withdrawal." loading="lazy"/><span class="velocity-slide-index">18</span></div></article>
'''
for i,alt in [(18,'Design decision: one unified balance, not separate wallets.'),(19,'Design decision: real-time visibility and control over point usage.'),(20,'Design decision: preserve customer freedom with card-agnostic earning.'),(21,'Design decision: bring the human service layer into the ecosystem through explicit tipping.')]:
    html+=f'''<article class="velocity-slide" id="slide-{i+2}" data-slide="{i+2}"><div class="velocity-slide-frame"><img src="assets/velocity-web-slides/slide-{i:02d}.webp" alt="{alt}" loading="lazy"/><span class="velocity-slide-index">{i+2:02d}</span></div></article>\n'''
# Actual PDF pages 22-24 become web sequence 23-25.
for i,alt in [(22,'Velocity visual design system: colour, typography, interface components and visual language.'),(23,'The next test belongs at the station: research and pilot activities.'),(24,'Thank you. A rewards experience designed around the real rhythm of the fuel stop.')]:
    html+=f'''<article class="velocity-slide" id="slide-{i+1}" data-slide="{i+1}"><div class="velocity-slide-frame"><img src="assets/velocity-web-slides/slide-{i:02d}.webp" alt="{alt}" loading="lazy"/><span class="velocity-slide-index">{i+1:02d}</span></div></article>\n'''
html+='''</div>
<div class="velocity-deck-controls"><button type="button" id="velocity-prev" aria-label="Previous slide">← Previous</button><div class="velocity-deck-progress"><span id="velocity-progress-fill"></span></div><button type="button" id="velocity-next" aria-label="Next slide">Next →</button></div>
<p class="velocity-deck-hint">Scroll or swipe through the slides. Use the arrows to move one slide at a time. On smaller screens, open a slide to zoom in.</p>
</section>
<section class="velocity-deck-notes"><div class="wrap"><div><span class="eyebrow">Scope and evidence</span><p>This is a self-directed concept informed by a competitor and market audit. The archetypes are hypotheses, not interview-based personas. The concept and proposed success measures require customer, commercial and station-operations validation.</p></div><a class="btn" href="index.html#work">Back to selected work ↑</a></div></section>
<nav aria-label="Case study navigation" class="case-pager"><div class="case-pager-inner"><div class="case-pager-top"><span>KEEP EXPLORING</span><span>03 / 03</span></div><div class="case-pager-links"><a class="case-pager-link previous" href="rise.html"><span>← PREVIOUS</span><strong>RISE Financial Wellbeing</strong></a><a class="case-pager-link next" href="index.html#work"><span>NEXT →</span><strong>Back to selected work</strong></a></div></div></nav>
</main><footer class="footer"><div class="wrap footer-grid"><div><a class="brand" href="index.html">STAN<span>.</span></a><p>UX design grounded in research and evidence.</p></div><div class="footer-links"><a href="mailto:smnhau03@gmail.com">Email</a><a href="https://www.linkedin.com/in/stanslous-nhau-3b56a53a6/" rel="noreferrer" target="_blank">LinkedIn</a><a download="" href="assets/Stanslous_Nhau_CV.pdf">CV</a></div></div><div class="wrap copyright">© <span data-year=""></span> Stanslous Nhau · UX Designer</div></footer>
<script src="script.js"></script><script>
(()=>{const slides=[...document.querySelectorAll('.velocity-slide')];if(!slides.length)return;const count=document.getElementById('velocity-slide-count'),fill=document.getElementById('velocity-progress-fill'),prev=document.getElementById('velocity-prev'),next=document.getElementById('velocity-next');let active=0;const update=()=>{const s=slides[active];count.textContent=String(active+1).padStart(2,'0')+' / '+String(slides.length).padStart(2,'0');fill.style.width=((active+1)/slides.length*100)+'%';prev.disabled=active===0;next.disabled=active===slides.length-1;};const go=(n)=>{active=Math.max(0,Math.min(slides.length-1,n));slides[active].scrollIntoView({behavior:'smooth',block:'center'});update();};prev.addEventListener('click',()=>go(active-1));next.addEventListener('click',()=>go(active+1));const obs=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){active=slides.indexOf(e.target);update();}}},{threshold:.55});slides.forEach(s=>obs.observe(s));document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')go(active+1);if(e.key==='ArrowLeft')go(active-1);});slides.forEach(s=>{const img=s.querySelector('img');img?.addEventListener('click',()=>{s.classList.toggle('is-zoomed');});});update();})();
</script></body></html>'''
(root/'velocity.html').write_text(html)
