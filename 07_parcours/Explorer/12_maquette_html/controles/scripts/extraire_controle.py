"""Extrait le résultat de contrôle réellement exécuté dans Edge headless."""
import html
import json
import re
import sys
from pathlib import Path

here = Path(__file__).resolve().parents[1]
kind = sys.argv[1] if len(sys.argv) > 1 else "desktop"
assert kind in ("desktop", "mobile")
content = (here / "traces" / f"controle-{kind}.dom.html").read_text(encoding="utf-8-sig")
match = re.search(r'<pre id="verification-result"[^>]*>(.*?)</pre>', content, re.S)
result = json.loads(html.unescape(match[1])) if match else {"missing": True, "bytes": len(content)}
(here / "resultats" / f"CONTROLE_{kind.upper()}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(1 if result.get("missing") or result.get("failed") else 0)
