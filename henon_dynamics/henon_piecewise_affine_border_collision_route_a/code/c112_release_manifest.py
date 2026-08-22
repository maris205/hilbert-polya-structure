#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MAN=ROOT/"C112_PREFREEZE_MANIFEST.json"
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    files={}
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p!=MAN and '__pycache__' not in p.parts and p.suffix not in {'.aux','.log','.out','.fls','.fdb_latexmk'}: files[str(p.relative_to(ROOT))]=h(p)
    ev=ROOT/"results/c112_border_evidence.json"; pdf=ROOT/"paper/main.pdf"
    d={"schema":"hcs-c112-piecewise-affine-border-prefreeze-v1","status":"PREFREEZE_COMPLETE_NOT_RELEASED","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","headline":"Piecewise-affine border-collision Hénon branch and weighted transfer prefix","route_a_verdict":{"A1":"A1_PARTIAL_CERTIFIED","A2":"A2_CERTIFIED_PREFIX","A3":"A3_NOT_ADDRESSED","A4":"A4_FAIL"},"results":{"max_period":8,"primitive_necklaces":71,"evidence_sha256":h(ev),"pdf_sha256":h(pdf) if pdf.exists() else "","pdf_pages":1,"mutation_rejections":6},"nonclaims":["complete border-collision repeller","analytic Fredholm determinant","arithmetic data","Route B"],"files":files}
    MAN.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n"); print(h(MAN))
if __name__=='__main__': main()
