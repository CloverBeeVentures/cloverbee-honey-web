#!/usr/bin/env python3
from pathlib import Path
import re
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: patch_cinematic_bees.py INDEX_HTML B64_SOURCE")

index_path = Path(sys.argv[1])
b64_path = Path(sys.argv[2])
html = index_path.read_text(encoding="utf-8")
bee_b64 = b64_path.read_text(encoding="utf-8").strip()

css_start_marker = "    /* Page-relative cinematic bees */"
css_end_marker = "    @media(max-width:900px){"
css_start = html.index(css_start_marker)
css_end = html.index(css_end_marker, css_start)

new_css = f'''    /* Page-relative cinematic bees */
    .bee-layer{{position:absolute;inset:0;pointer-events:none;z-index:8;overflow:hidden}}
    .bee-trails{{position:absolute;inset:0;width:100%;height:100%;overflow:visible}}
    .bee-trail{{fill:none;stroke:rgba(235,178,60,.48);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:2 10}}
    .bee{{position:absolute;width:78px;height:78px;transform:translate(-50%,-50%);filter:drop-shadow(0 7px 14px rgba(0,0,0,.18));opacity:.98;will-change:left,top,transform}}
    .bee-art{{display:block;width:100%;height:100%;background:url("data:image/png;base64,{bee_b64}") center/contain no-repeat;animation:beeBob .72s infinite alternate ease-in-out}}
    .bee2 .bee-art{{animation-duration:.64s;animation-delay:-.18s}}
    .bee3 .bee-art{{animation-duration:.80s;animation-delay:-.31s}}
    @keyframes beeBob{{from{{transform:translateY(-2px) rotate(-1.5deg)}}to{{transform:translateY(2px) rotate(1.5deg)}}}}

'''
html = html[:css_start] + new_css + html[css_end:]

bee_start_marker = "    <!-- Option 4: cinematic/cartoon side-profile bees -->"
bee_end_marker = "\n  </div>\n\n  <header>"
bee_start = html.index(bee_start_marker)
bee_end = html.index(bee_end_marker, bee_start)

new_bees = '''    <!-- Option 4 selected: approved fluffy 3D/cinematic bee -->
    <div class="bee bee1"><span class="bee-art"></span></div>
    <div class="bee bee2"><span class="bee-art"></span></div>
    <div class="bee bee3"><span class="bee-art"></span></div>'''
html = html[:bee_start] + new_bees + html[bee_end:]

# Keep bees upright. They may bank slightly, but never rotate with the full flight angle.
old_motion = '''        const rot=angle*180/Math.PI + Math.sin(bee.t*6+i)*7;
        const flip=dx<0?-1:1;
        bee.el.style.left=`${bee.x}px`;
        bee.el.style.top=`${bee.y}px`;
        bee.el.style.transform=`translate(-50%,-50%) rotate(${rot}deg) scaleX(${flip})`;
'''
new_motion = '''        const facing=dx<0?-1:1;
        const bank=Math.max(-12,Math.min(12,dy*0.06 + Math.sin(bee.t*6+i)*4));
        bee.el.style.left=`${bee.x}px`;
        bee.el.style.top=`${bee.y}px`;
        bee.el.style.transform=`translate(-50%,-50%) scaleX(${facing}) rotate(${bank}deg)`;
'''
if old_motion not in html:
    raise SystemExit("expected bee motion block not found")
html = html.replace(old_motion, new_motion, 1)

# Mobile bee size.
html = html.replace('.bee{width:44px;height:44px}', '.bee{width:62px;height:62px}')

index_path.write_text(html, encoding="utf-8")
print(f"Patched visible cinematic bees and upright motion into {index_path}")
