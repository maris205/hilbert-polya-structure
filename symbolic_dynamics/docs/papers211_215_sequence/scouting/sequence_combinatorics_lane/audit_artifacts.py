"""Read-only integrity audit. No scientific or historical code is executed."""
from pathlib import Path
import hashlib
import json
import re
import sys
base=Path(__file__).resolve().parent
workspace=base.parents[3]
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted(p for p in base.rglob("*") if p.is_file())
assert not any(p.is_symlink() for p in base.rglob("*"))
assert sum(p.stat().st_size for p in files)<2_000_000
hist=[]
for line in (base/"HISTORY_INPUTS.sha256").read_text().splitlines():
    h,p=line.split("  ",1)
    assert digest(workspace/p)==h,p
    hist.append(p)
assert len(hist)==len(set(hist))==12
links=[]
for p in base.glob("*.md"):
    for t in re.findall(r"\[[^\]]*\]\(([^)]+)\)",p.read_text()):
        if t.startswith(("https://","http://","#")):
            continue
        assert (p.parent/t.split("#",1)[0]).exists(),(p,t)
        links.append(t)
json_count=0
for p in base.rglob("*.json"):
    json.loads(p.read_text())
    json_count+=1
seal=None
if "--check-seal" in sys.argv:
    rows=[]
    for line in (base/"MANIFEST.sha256").read_text().splitlines():
        h,p=line.split("  ",1)
        assert p!="MANIFEST.sha256" and digest(base/p)==h,p
        rows.append(p)
    actual={str(p.relative_to(base)) for p in files if p.name!="MANIFEST.sha256"}
    assert len(rows)==len(set(rows)) and set(rows)==actual
    seal=len(rows)
print(json.dumps({"status":"PASS_ARTIFACT_ONLY","scientific_runs":0,
"historical_pins":len(hist),"local_links":len(links),"json_files":json_count,
"files":len(files),"bytes":sum(p.stat().st_size for p in files),
"nonself_seal_entries":seal,"python":sys.version,
"limits":"Post-read identity and artifact checks only; not a mathematical review or hermetic execution."},indent=2))
