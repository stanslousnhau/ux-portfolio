from pathlib import Path
p=Path('/mnt/data/attrjourney/assets')
(p/'rise-web-slides').mkdir(parents=True,exist_ok=True)
(p/'velocity-web-slides').mkdir(parents=True,exist_ok=True)

def svg_start(title,sub):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f7f8fc"/><stop offset="1" stop-color="#eef2fb"/></linearGradient><style>text{{font-family:Inter,Arial,sans-serif;fill:#14213d}}.eyebrow{{font-size:24px;font-weight:700;letter-spacing:4px;fill:#3268f5}}.title{{font-size:62px;font-weight:800;letter-spacing:-1.5px}}.sub{{font-size:27px;fill:#52617b}}.head{{font-size:26px;font-weight:800}}.body{{font-size:23px;fill:#43516a}}.small{{font-size:20px;fill:#596780}}.label{{font-size:19px;font-weight:800;letter-spacing:1.5px;fill:#3268f5}}.line{{stroke:#cbd5e8;stroke-width:3}}.blue{{fill:#3268f5}}.white{{fill:#fff}}.muted{{fill:#64728b}}</style></defs><rect width="1920" height="1080" fill="url(#bg)"/><text x="100" y="95" class="eyebrow">{title.upper()}</text><text x="100" y="180" class="title">{sub}</text>'''

# Rise attribute continuum
s=svg_start('RISE · RESEARCH SYNTHESIS','From recurring behaviours to the “Cautious Provider”')
s+='''<text x="100" y="235" class="sub">A working archetype built by clustering the pressures, priorities and decision patterns surfaced in secondary research.</text>
<rect x="100" y="285" width="1720" height="610" rx="28" fill="#fff" stroke="#dce3f0" stroke-width="2"/>
<text x="150" y="345" class="label">ATTRIBUTE CONTINUUM</text><text x="150" y="390" class="small">The synthesis moves from short-term coping towards careful, security-seeking financial behaviour.</text>
'''
rows=[
 ('TIME HORIZON','Immediate decisions','Plans around payday and upcoming commitments',0.78),
 ('RISK RESPONSE','Uses money when it is available','Protects a small reserve against surprises',0.84),
 ('DECISION STYLE','Acts with limited visibility','Wants clear information before committing',0.80),
 ('SUPPORT NEED','Relies on trial and error','Values reassurance and practical guidance',0.74),
 ('MOTIVATION','Wants to get through today','Wants to provide reliably and stay in control',0.88),
]
y=465
for label,left,right,pos in rows:
 s+=f'<text x="150" y="{y}" class="label">{label}</text><text x="430" y="{y}" class="body">{left}</text><text x="1490" y="{y}" text-anchor="end" class="body">{right}</text>'
 x1,x2=455,1450; yy=y+34; xx=x1+(x2-x1)*pos
 s+=f'<line x1="{x1}" y1="{yy}" x2="{x2}" y2="{yy}" class="line"/><circle cx="{xx}" cy="{yy}" r="13" fill="#3268f5" stroke="#dce7ff" stroke-width="8"/><text x="{x1}" y="{yy+34}" class="small">COPING</text><text x="{x2}" y="{yy+34}" text-anchor="end" class="small">CAUTIOUS / PREPARED</text>'
 y+=96
s+='''<rect x="150" y="825" width="1620" height="1" fill="#e4e9f2"/><text x="150" y="865" class="head">Archetype name: The Cautious Provider</text><text x="650" y="865" class="body">A first-job earner who wants to meet responsibilities, protect a modest buffer and feel confident before spending.</text>
<text x="100" y="970" class="small">Interpretation, not a measured segmentation: positions show the design hypothesis used to guide the concept and should be validated with first-job earners.</text></svg>'''
(p/'rise-web-slides/attribute-continuum.svg').write_text(s)

# Velocity journey
s=svg_start('VELOCITY · TARGET-STATE EXPERIENCE','A rewards journey built around a real fuel stop')
s+='''<text x="100" y="235" class="sub">The intended experience: make rewards visible, usable in the moment and flexible enough to include a thank-you to the attendant.</text>
'''
cols=[
 ('01 · ARRIVE','Arrive at station','Open the app; check nearby station and current rewards balance.','App home · station signage','Can I quickly understand what I have and what I can do here?','🙂','Oriented'),
 ('02 · PREPARE','Get ready to pay','Choose fuel amount and preferred payment method; present app or scan code.','App payment · pump · attendant','Does payment work with the method I prefer, without extra friction?','😐','Focused'),
 ('03 · EARN','Complete fuel purchase','Confirm transaction and see points/rewards update.','POS · app transaction receipt','Are my rewards credited accurately and immediately?','🙂','Reassured'),
 ('04 · USE VALUE','Choose how to use rewards','Review balance; redeem, save or cash out where eligible.','Rewards wallet · redemption options','Can I use value in a way that suits my needs right now?','😊','In control'),
 ('05 · THANK','Tip attendant & finish','Choose a tip amount, confirm, and receive a clear confirmation.','Pay-it-forward flow · attendant confirmation','Did my thank-you reach the right person, and is it clear that it did?','🥰','Appreciative'),
]
# grid cards
x0=100; gap=22; w=326; y0=310; h=565
for i,(num,name,act,tp,mot,emo,feel) in enumerate(cols):
 x=x0+i*(w+gap)
 s+=f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" rx="22" fill="#fff" stroke="#dbe3f0" stroke-width="2"/><rect x="{x}" y="{y0}" width="{w}" height="74" rx="22" fill="#132b61"/><rect x="{x}" y="{y0+52}" width="{w}" height="22" fill="#132b61"/><text x="{x+24}" y="{y0+47}" font-size="20" font-weight="800" fill="#fff">{num}</text><text x="{x+24}" y="{y0+122}" class="head">{name}</text>'
 s+=f'<text x="{x+24}" y="{y0+170}" class="label">USER ACTIONS</text><foreignObject x="{x+24}" y="{y0+184}" width="278" height="105"><div xmlns="http://www.w3.org/1999/xhtml" style="font:21px Arial,sans-serif;color:#43516a;line-height:1.35">{act}</div></foreignObject>'
 s+=f'<text x="{x+24}" y="{y0+320}" class="label">TOUCHPOINTS</text><foreignObject x="{x+24}" y="{y0+334}" width="278" height="66"><div xmlns="http://www.w3.org/1999/xhtml" style="font:20px Arial,sans-serif;color:#43516a;line-height:1.3">{tp}</div></foreignObject>'
 s+=f'<text x="{x+24}" y="{y0+420}" class="label">MOMENT OF TRUTH</text><foreignObject x="{x+24}" y="{y0+434}" width="278" height="72"><div xmlns="http://www.w3.org/1999/xhtml" style="font:19px Arial,sans-serif;color:#43516a;line-height:1.28">{mot}</div></foreignObject>'
 s+=f'<text x="{x+24}" y="{y0+535}" font-size="34">{emo}</text><text x="{x+80}" y="{y0+532}" class="head">{feel}</text>'
s+='''<rect x="100" y="915" width="1720" height="85" rx="18" fill="#e4ebff"/><text x="130" y="968" class="head">Experience principle</text><text x="440" y="968" class="body">Every step should reduce uncertainty and give customers visible control over their rewards and choices.</text><text x="100" y="1040" class="small">Target-state hypothesis for design exploration; validate task completion, payment compatibility, reward timing and tipping operations in station-based research.</text></svg>'''
(p/'velocity-web-slides/target-state-journey.svg').write_text(s)
