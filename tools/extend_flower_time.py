#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: extend_flower_time.py INDEX_HTML")

p = Path(sys.argv[1])
html = p.read_text(encoding="utf-8")

replacements = {
    "attractor.until=performance.now()+2000;": "attractor.until=performance.now()+3000;",
    "},1680);": "},2680);",
    "},2000);": "},3000);",
}

for old, new in replacements.items():
    if old not in html:
        raise SystemExit(f"expected timing token not found: {old}")
    html = html.replace(old, new, 1)

p.write_text(html, encoding="utf-8")
print(f"Extended clover flower lifetime to 3 seconds in {p}")
