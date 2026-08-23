#!/usr/bin/env python3
from pathlib import Path
import base64
import sys

if len(sys.argv) != 4:
    raise SystemExit("usage: patch_cinematic_bees.py INDEX_HTML B64_SOURCE PNG_TARGET")

index_path = Path(sys.argv[1])
b64_path = Path(sys.argv[2])
png_path = Path(sys.argv[3])

png_path.write_bytes(base64.b64decode(b64_path.read_text().strip()))

html = index_path.read_text()

css_start_marker = "    /* Page-relative cinematic bees */"
css_end_marker = "    @media(max-width:900px){"
css_start = html.index(css_start_marker)
css_end = html.index(css_end_marker, css_start)

new_css = '''    /* Page-relative cinematic bees */
    .bee-layer{position:absolute;inset:0;pointer-events:none;z-index:8;overflow:hidden}
    .bee-trails{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
    .bee-trail{fill:none;stroke:rgba(235,178,60,.48);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:2 10}
    .bee{position:absolute;width:68px;height:68px;transform:translate(-50%,-50%);filter:drop-shadow(0 7px 14px rgba(0,0,0,.18));opacity:.98;will-change:left,top,transform}
    .bee-art{display:block;width:100%;height:100%;background:url('/bee-cinematic.png') center/contain no-repeat;animation:beeBob .72s infinite alternate ease-in-out}
    .bee2 .bee-art{animation-duration:.64s;animation-delay:-.18s}
    .bee3 .bee-art{animation-duration:.80s;animation-delay:-.31s}
    @keyframes beeBob{from{transform:translateY(-2px) rotate(-1.5deg)}to{transform:translateY(2px) rotate(1.5deg)}}

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

index_path.write_text(html)
print(f"Patched cinematic bee artwork into {index_path}")
