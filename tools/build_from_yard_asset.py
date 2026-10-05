#!/usr/bin/env python3
import base64
import hashlib
import sys
from pathlib import Path

EXPECTED_SHA256 = "c2c3b7eb55600c8509caf9f4132f9a76b075cb8cc741de0d0529c8a40d998440"
ROOT = Path(__file__).resolve().parents[1]

if len(sys.argv) != 2:
    raise SystemExit("usage: build_from_yard_asset.py <asset-directory>")

payload = "".join(
    (ROOT / "assets" / f"from-yard.b64.part{i}").read_text(encoding="ascii").strip()
    for i in range(5)
)
raw = base64.b64decode(payload, validate=True)

if hashlib.sha256(raw).hexdigest() != EXPECTED_SHA256:
    raise SystemExit("From the yard image payload checksum mismatch")
if not raw.startswith(b"\xff\xd8") or not raw.endswith(b"\xff\xd9"):
    raise SystemExit("From the yard image is not a complete JPEG")

destination = Path(sys.argv[1])
destination.mkdir(parents=True, exist_ok=True)
(destination / "from-yard.jpg").write_bytes(raw)
svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" '
    'preserveAspectRatio="xMidYMid slice"><image '
    'href="data:image/jpeg;base64,' + payload + '" width="640" height="360" '
    'preserveAspectRatio="xMidYMid slice"/></svg>\n'
)
(destination / "from-yard.svg").write_text(svg, encoding="utf-8")
