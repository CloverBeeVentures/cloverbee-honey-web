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

    /* Click-grown white clover */
    .clover-flower{position:absolute;left:0;top:0;width:70px;height:82px;transform:translate(-50%,-58%) scale(.58);opacity:0;pointer-events:none;z-index:9;filter:drop-shadow(0 7px 10px rgba(20,45,28,.16));transition:opacity .16s ease,transform .2s cubic-bezier(.2,.8,.2,1)}
    .clover-flower.show{opacity:1;transform:translate(-50%,-58%) scale(1)}
    .clover-flower.fade{opacity:0;transform:translate(-50%,-58%) scale(.88)}
    .clover-flower svg{display:block;width:100%;height:100%;overflow:visible}
    .clover-stem{fill:none;stroke:#456f4e;stroke-width:2.3;stroke-linecap:round}
    .clover-leaf{fill:#789d75;stroke:#486c4b;stroke-width:1.1}
    .clover-leaf-mark{fill:none;stroke:#d9e3d3;stroke-width:1;stroke-linecap:round;opacity:.8}
    .clover-floret{fill:#faf9ef;stroke:#798879;stroke-width:.8}
    .clover-floret-shadow{fill:#e8eadf;stroke:#798879;stroke-width:.7}
    .clover-core{fill:#dfe4d5;stroke:#718071;stroke-width:.8}

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
<g clip-path="url(#bodyClip)" opacity=".96"><path d="M27 27C22 40 23 60 31 73" fill="none" stroke="#2a2118" stroke-width="9"/><path d="M44 26C38 40 39 64 46 76" fill="none" stroke="#2a2118" stroke-width="9"/><path d="M61 29C56 42 57 62 65 72" fill="none" stroke="#2a2118" stroke-width="8"/></g>
<circle cx="78" cy="40" r="22" fill="url(#face)" stroke="#6b3c16" stroke-width="1.8"/>
<ellipse cx="73" cy="36" rx="8.2" ry="10.2" fill="white" stroke="#714315" stroke-width="1"/><ellipse cx="73" cy="37" rx="5.6" ry="7.6" fill="url(#eye)"/><circle cx="70.8" cy="33.7" r="2" fill="white"/>
<ellipse cx="89.5" cy="37" rx="7.2" ry="9.2" fill="white" stroke="#714315" stroke-width="1"/><ellipse cx="89.7" cy="38" rx="4.8" ry="6.7" fill="url(#eye)"/><circle cx="87.9" cy="35" r="1.8" fill="white"/>
<path d="M76 50c4.5 4.7 10.5 4.6 14.5-.2" fill="none" stroke="#6c351a" stroke-width="2" stroke-linecap="round"/>
<path d="M72 19C68 9 65 6 59 4M85 19C88 8 94 4 100 5" fill="none" stroke="#2b1c13" stroke-width="2.5" stroke-linecap="round"/><circle cx="58.5" cy="4" r="3.2" fill="#2b1c13"/><circle cx="101" cy="5" r="3.2" fill="#2b1c13"/>
<path d="M43 69c-2 8-8 12-13 14M54 71c0 7-4 12-9 15M65 67c3 7 1 12-3 16" fill="none" stroke="#2b1c13" stroke-width="3.2" stroke-linecap="round"/><path d="M16 53l-8 3 7 4" fill="#2b1c13"/>
</svg>'''

# White clover head: many overlapping small florets on a slim stem, with trifoliate leaves.
clover_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 78 94" aria-hidden="true">
  <path class="clover-stem" d="M39 43 C38 57, 40 73, 36 93"/>
  <g transform="translate(37 72) rotate(-9)">
    <path class="clover-leaf" d="M0 0 C-3-12-17-13-21-5 C-23 2-12 8 0 4 Z"/>
    <path class="clover-leaf-mark" d="M-2 2 C-9 1-14-2-18-5"/>
    <path class="clover-leaf" d="M2 1 C7-12 21-11 24-2 C26 5 14 9 2 5 Z"/>
    <path class="clover-leaf-mark" d="M4 3 C11 2 17 0 21-2"/>
    <path class="clover-leaf" d="M1 1 C0-12 7-20 14-17 C21-13 17-2 5 5 Z"/>
    <path class="clover-leaf-mark" d="M4 2 C7-5 10-10 13-14"/>
  </g>
  <g transform="translate(39 29)">
    <ellipse class="clover-floret-shadow" cx="-19" cy="4" rx="8" ry="5" transform="rotate(-45 -19 4)"/>
    <ellipse class="clover-floret-shadow" cx="-13" cy="-8" rx="8.2" ry="5.2" transform="rotate(-62 -13 -8)"/>
    <ellipse class="clover-floret-shadow" cx="-2" cy="-14" rx="8.3" ry="5" transform="rotate(-82 -2 -14)"/>
    <ellipse class="clover-floret-shadow" cx="10" cy="-12" rx="8" ry="5" transform="rotate(-104 10 -12)"/>
    <ellipse class="clover-floret-shadow" cx="19" cy="-3" rx="8" ry="5" transform="rotate(-126 19 -3)"/>
    <ellipse class="clover-floret" cx="-20" cy="12" rx="8.2" ry="5.1" transform="rotate(-28 -20 12)"/>
    <ellipse class="clover-floret" cx="-13" cy="3" rx="8.6" ry="5" transform="rotate(-48 -13 3)"/>
    <ellipse class="clover-floret" cx="-8" cy="-7" rx="8.5" ry="5.2" transform="rotate(-68 -8 -7)"/>
    <ellipse class="clover-floret" cx="2" cy="-8" rx="9" ry="5.2" transform="rotate(-87 2 -8)"/>
    <ellipse class="clover-floret" cx="12" cy="-5" rx="8.5" ry="5.2" transform="rotate(-108 12 -5)"/>
    <ellipse class="clover-floret" cx="19" cy="5" rx="8.4" ry="5" transform="rotate(-133 19 5)"/>
    <ellipse class="clover-floret" cx="17" cy="14" rx="8" ry="5" transform="rotate(-154 17 14)"/>
    <ellipse class="clover-floret" cx="7" cy="17" rx="8.6" ry="5.2" transform="rotate(170 7 17)"/>
    <ellipse class="clover-floret" cx="-4" cy="18" rx="8.8" ry="5.2" transform="rotate(157 -4 18)"/>
    <ellipse class="clover-floret" cx="-14" cy="15" rx="8.4" ry="5" transform="rotate(145 -14 15)"/>
    <ellipse class="clover-floret" cx="-4" cy="5" rx="8.5" ry="5" transform="rotate(-56 -4 5)"/>
    <ellipse class="clover-floret" cx="6" cy="4" rx="8.5" ry="5" transform="rotate(-106 6 4)"/>
    <ellipse class="clover-floret" cx="1" cy="12" rx="8.8" ry="5.1" transform="rotate(172 1 12)"/>
    <circle class="clover-core" cx="0" cy="8" r="4.2"/>
  </g>
</svg>'''

new_bees = f'''    <!-- Option 4: verified inline cinematic/cartoon bees; no external image files -->
    <div class="bee bee1">{bee_svg}</div>
    <div class="bee bee2">{bee_svg}</div>
    <div class="bee bee3">{bee_svg}</div>
    <div class="clover-flower" id="cloverFlower">{clover_svg}</div>'''
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

# Add flower attraction interaction to the existing bee controller.
needle = "    const trailEls = [...document.querySelectorAll('.bee-trail')];\n"
if needle not in html:
    raise SystemExit("bee trail declaration not found")
html = html.replace(needle, needle + "    const flowerEl = document.getElementById('cloverFlower');\n", 1)

sync_block = '''    function syncLayer(){
      const h = pageHeight();
      layer.style.height = `${h}px`;
      trailSvg.setAttribute('viewBox',`0 0 ${window.innerWidth} ${h}`);
      trailSvg.setAttribute('width',window.innerWidth);
      trailSvg.setAttribute('height',h);
    }
'''
if sync_block not in html:
    raise SystemExit("syncLayer block not found")
html = html.replace(sync_block, sync_block + '''
    const attractor={active:false,x:0,y:0,until:0,fadeTimer:null,hideTimer:null,serial:0};
''', 1)

bees_block = '''    const h = pageHeight();
    const bees = [
      makeBee(beeEls[0],trailEls[0],{x:170,y:165,speed:.020,wobble:10}),
      makeBee(beeEls[1],trailEls[1],{x:Math.max(240,window.innerWidth-180),y:440,speed:.016,wobble:13}),
      makeBee(beeEls[2],trailEls[2],{x:210,y:Math.min(h-120,860),speed:.018,wobble:11})
    ];
'''
if bees_block not in html:
    raise SystemExit("bees block not found")
interaction = '''
    function placeFlower(x,y){
      const serial=++attractor.serial;
      if(attractor.fadeTimer) clearTimeout(attractor.fadeTimer);
      if(attractor.hideTimer) clearTimeout(attractor.hideTimer);

      const reveal=()=>{
        if(serial!==attractor.serial) return;
        attractor.active=true;
        attractor.x=clamp(x,38,window.innerWidth-38);
        attractor.y=clamp(y,92,pageHeight()-42);
        attractor.until=performance.now()+2000;
        flowerEl.style.left=`${attractor.x}px`;
        flowerEl.style.top=`${attractor.y}px`;
        flowerEl.classList.remove('fade');
        flowerEl.classList.add('show');
        bees.forEach((bee,i)=>{
          bee.tx=clamp(attractor.x+rand(-26,26)+(i-1)*4,38,window.innerWidth-38);
          bee.ty=clamp(attractor.y-12+rand(-22,22),92,pageHeight()-42);
          bee.targetAge=0;
        });
        attractor.fadeTimer=setTimeout(()=>{
          if(serial===attractor.serial) flowerEl.classList.add('fade');
        },1680);
        attractor.hideTimer=setTimeout(()=>{
          if(serial!==attractor.serial) return;
          flowerEl.classList.remove('show','fade');
          attractor.active=false;
        },2000);
      };

      if(flowerEl.classList.contains('show')){
        flowerEl.classList.add('fade');
        attractor.active=false;
        setTimeout(reveal,120);
      } else {
        reveal();
      }
    }

    document.addEventListener('click',(event)=>{
      if(event.target.closest('a,button,input,textarea,select,label,summary,[role="button"]')) return;
      placeFlower(event.pageX,event.pageY);
    },{passive:true});
'''
html = html.replace(bees_block, bees_block + interaction, 1)

wander_block = '''        let dx=bee.tx-bee.x, dy=bee.ty-bee.y;
        const dist=Math.hypot(dx,dy);
        if(dist<30 || bee.targetAge>rand(2800,6200) || Math.random()<.0012){
          chooseTarget(bee);
          dx=bee.tx-bee.x; dy=bee.ty-bee.y;
        }
'''
if wander_block not in html:
    raise SystemExit("bee wander block not found")
attract_block = '''        let dx=bee.tx-bee.x, dy=bee.ty-bee.y;
        const dist=Math.hypot(dx,dy);
        if(attractor.active){
          if(performance.now()>attractor.until){
            attractor.active=false;
          } else if(dist<24 || bee.targetAge>500 || Math.random()<.01){
            bee.tx=clamp(attractor.x+rand(-30,30),38,window.innerWidth-38);
            bee.ty=clamp(attractor.y-12+rand(-26,24),92,pageHeight()-42);
            bee.targetAge=0;
            dx=bee.tx-bee.x; dy=bee.ty-bee.y;
          }
        } else if(dist<30 || bee.targetAge>rand(2800,6200) || Math.random()<.0012){
          chooseTarget(bee);
          dx=bee.tx-bee.x; dy=bee.ty-bee.y;
        }
'''
html = html.replace(wander_block, attract_block, 1)

html = html.replace('.bee{width:44px;height:44px}', '.bee{width:64px;height:64px}')
html = html.replace('.bee{width:56px;height:56px}', '.bee{width:64px;height:64px}')
html = html.replace('.bee{width:62px;height:62px}', '.bee{width:64px;height:64px}')

index_path.write_text(html, encoding="utf-8")
print(f"Patched inline cinematic bees, interactive white clover, and upright motion into {index_path}")