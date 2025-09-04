# scripts/dedup_thebe.py
import re, pathlib
root = pathlib.Path("docs/notebooks")
block = re.compile(r'<script>const THEBE_JS_URL\b.*?</script>', re.DOTALL)
changed = 0
for p in root.rglob("*.html"):
    s = p.read_text(encoding="utf-8")
    matches = list(block.finditer(s))
    if len(matches) > 1:
        ss = s
        for m in matches[1:][::-1]:
            ss = ss[:m.start()] + ss[m.end():]
        p.write_text(ss, encoding="utf-8")
        print(f"- {p}: {len(matches)} -> 1")
        changed += 1
print(f"Fichiers corrigés: {changed}")
