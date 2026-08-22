#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MAN=ROOT/"C113_PREFREEZE_MANIFEST.json"
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    files={}
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p!=MAN and '__pycache__' not in p.parts and p.suffix not in {'.aux','.log','.out','.fls','.fdb_latexmk'}:
            files[str(p.relative_to(ROOT))]=h(p)
    ev=ROOT/"results/c113_memory_evidence.json"; pdf=ROOT/"paper/main.pdf"
    d={"schema":"hcs-c113-third-order-memory-prefreeze-v1","status":"PREFREEZE_COMPLETE_NOT_RELEASED",
       "scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","headline":"Third-order memory Hénon map and exact low-period monodromy prefix",
       "route_a_verdict":{"A1":"A1_WEAK","A2":"A2_CERTIFIED_PREFIX","A3":"A3_NOT_ADDRESSED","A4":"A4_FAIL"},
       "results":{"fixed_count":2,"period_two_count":1,"evidence_sha256":h(ev),"pdf_sha256":h(pdf) if pdf.exists() else "","pdf_pages":1,"mutation_rejections":5},
       "nonclaims":["complete primitive-orbit atlas","analytic Fredholm determinant","arithmetic data","Route B"],"files":files}
    MAN.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n"); print(h(MAN))
if __name__=='__main__': main()
