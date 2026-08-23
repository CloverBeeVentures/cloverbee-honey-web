#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch_cinematic_bees.py INDEX_HTML")

index_path = Path(sys.argv[1])
html = index_path.read_text(encoding="utf-8")

css_start_marker = "    /* Page-relative cinematic bees */"
css_end_marker = "    @media(max-width:900px){"
css_start = html.index(css_start_marker)
css_end = html.index(css_end_marker, css_start)

new_css = '''    /* Page-relative cinematic bees */
    .bee-layer{position:absolute;inset:0;pointer-events:none;z-index:8;overflow:hidden}
    .bee-trails{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
    .bee-trail{fill:none;stroke:rgba(235,178,60,.48);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:2 10}
    .bee{position:absolute;width:82px;height:82px;transform:translate(-50%,-50%);filter:drop-shadow(0 7px 13px rgba(0,0,0,.18));opacity:.98;will-change:left,top,transform}
    .bee-art{display:block!important;width:82px!important;height:82px!important;max-width:none!important;visibility:visible!important;opacity:1!important;animation:beeBob .72s infinite alternate ease-in-out}
    .bee2 .bee-art{animation-duration:.64s;animation-delay:-.18s}
    .bee3 .bee-art{animation-duration:.80s;animation-delay:-.31s}
    @keyframes beeBob{from{transform:translateY(-2px)}to{transform:translateY(2px)}}

'''
html = html[:css_start] + new_css + html[css_end:]

bee_start_marker = "    <!-- Option 4: cinematic/cartoon side-profile bees -->"
bee_end_marker = "\n  </div>\n\n  <header>"
bee_start = html.index(bee_start_marker)
bee_end = html.index(bee_end_marker, bee_start)

bee_svg = '''<svg class="bee-art" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 90" aria-hidden="true">
<defs>
  <linearGradient id="fur" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd75f"/><stop offset=".5" stop-color="#f4aa25"/><stop offset="1" stop-color="#c97517"/></linearGradient>
  <radialGradient id="face" cx="35%" cy="28%"><stop offset="0" stop-color="#ffd967"/><stop offset=".7" stop-color="#f2aa29"/><stop offset="1" stop-color="#c77817"/></radialGradient>
  <linearGradient id="wing" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity=".88"/><stop offset="1" stop-color="#d9eef4" stop-opacity=".36"/></linearGradient>
  <radialGradient id="eye" cx="35%" cy="25%"><stop offset="0" stop-color="#57472d"/><stop offset=".3" stop-color="#1f1b16"/><stop offset="1" stop-color="#050505"/></radialGradient>
  <clipPath id="bodyClip"><ellipse cx="49" cy="51" rx="33" ry="22"/></clipPath>
</defs>
<path d="M28 37C11 24 10 8 24 6c14-2 25 12 27 27" fill="url(#wing)" stroke="#a8cbd1" stroke-width="1.5"/>
<path d="M43 35C34 15 43 4 55 8c12 4 12 18 6 31" fill="url(#wing)" stroke="#a8cbd1" stroke-width="1.5"/>
<ellipse cx="49" cy="51" rx="33" ry="22" fill="url(#fur)" stroke="#5b3516" stroke-width="1.8"/>
<g clip-path="url(#bodyClip)" opacity=".96">
  <path d="M27 27C22 40 23 60 31 73" fill="none" stroke="#2a2118" stroke-width="9"/>
  <path d="M44 26C38 40 39 64 46 76" fill="none" stroke="#2a2118" stroke-width="9"/>
  <path d="M61 29C56 42 57 62 65 72" fill="none" stroke="#2a2118" stroke-width="8"/>
</g>
<g stroke="#d68c1f" stroke-width="1.2" stroke-linecap="round" opacity=".8">
  <path d="M19 40l-5-3M18 47l-6-1M18 55l-6 2M21 63l-5 4M27 69l-3 5M35 73l-1 5M54 73l1 5M63 70l3 5"/>
</g>
<circle cx="78" cy="40" r="22" fill="url(#face)" stroke="#6b3c16" stroke-width="1.8"/>
<g stroke="#5f391c" stroke-width="1" stroke-linecap="round" opacity=".72">
  <path d="M66 21l-2-4M72 19l-1-5M80 18l1-5M87 21l3-4M94 27l4-2M97 35l5-1M98 43l5 2M94 52l4 3M88 58l2 4M70 59l-2 4M63 55l-4 3"/>
</g>
<ellipse cx="73" cy="36" rx="8.2" ry="10.2" fill="white" stroke="#714315" stroke-width="1"/>
<ellipse cx="73" cy="37" rx="5.6" ry="7.6" fill="url(#eye)"/>
<circle cx="70.8" cy="33.7" r="2" fill="white"/><circle cx="75.2" cy="39" r=".9" fill="#fff" opacity=".7"/>
<ellipse cx="89.5" cy="37" rx="7.2" ry="9.2" fill="white" stroke="#714315" stroke-width="1"/>
<ellipse cx="89.7" cy="38" rx="4.8" ry="6.7" fill="url(#eye)"/>
<circle cx="87.9" cy="35" r="1.8" fill="white"/>
<path d="M76 50c4.5 4.7 10.5 4.6 14.5-.2" fill="none" stroke="#6c351a" stroke-width="2" stroke-linecap="round"/>
<circle cx="74" cy="49" r="1.3" fill="#9d4c25"/><circle cx="93" cy="48" r="1.1" fill="#9d4c25"/>
<path d="M72 19C68 9 65 6 59 4M85 19C88 8 94 4 100 5" fill="none" stroke="#2b1c13" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="58.5" cy="4" r="3.2" fill="#2b1c13"/><circle cx="101" cy="5" r="3.2" fill="#2b1c13"/>
<path d="M43 69c-2 8-8 12-13 14M54 71c0 7-4 12-9 15M65 67c3 7 1 12-3 16" fill="none" stroke="#2b1c13" stroke-width="3.2" stroke-linecap="round"/>
<path d="M16 53l-8 3 7 4" fill="#2b1c13"/>
</svg>'''

new_bees = f'''    <!-- Option 4: verified inline cinematic/cartoon bees; no external image files -->
    <div class="bee bee1">{bee_svg}</div>
    <div class="bee bee2">{bee_svg}</div>
    <div class="bee bee3">{bee_svg}</div>'''
html = html[:bee_start] + new_bees + html[bee_end:]

# Keep bees upright. Face left/right and bank only slightly; never rotate with flight angle.
old_motion = '''        const rot=angle*180/Math.PI + Math.sin(bee.t*6+i)*7;
        const flip=dx<0?-1:1;
        bee.el.style.left=`${bee.x}px`;
        bee.el.style.top=`${bee.y}px`;
        bee.el.style.transform=`translate(-50%,-50%) rotate(${rot}deg) scaleX(${flip})`;
'''
new_motion = '''        const facing=dx<0?-1:1;
        const bank=Math.max(-8,Math.min(8,dy*0.045 + Math.sin(bee.t*6+i)*3));
        bee.el.style.left=`${bee.x}px`;
        bee.el.style.top=`${bee.y}px`;
        bee.el.style.transform=`translate(-50%,-50%) scaleX(${facing}) rotate(${bank}deg)`;
'''
if old_motion in html:
    html = html.replace(old_motion, new_motion, 1)
elif new_motion not in html:
    raise SystemExit("expected bee motion block not found")

html = html.replace('.bee{width:44px;height:44px}', '.bee{width:64px;height:64px}')
html = html.replace('.bee{width:56px;height:56px}', '.bee{width:64px;height:64px}')
html = html.replace('.bee{width:62px;height:62px}', '.bee{width:64px;height:64px}')

index_path.write_text(html, encoding="utf-8")
print(f"Patched verified inline cinematic bees and upright motion into {index_path}")
