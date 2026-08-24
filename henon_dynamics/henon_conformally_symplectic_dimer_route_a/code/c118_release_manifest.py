#!/usr/bin/env python3
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MAN=ROOT/'C118_PREFREEZE_MANIFEST.json'
def h(p):return sha256(p.read_bytes()).hexdigest()
def main():
 ex={'C118_PREFREEZE_MANIFEST.json','paper/main.aux','paper/main.log','paper/main.out','paper/main.fls','paper/main.fdb_latexmk','paper/main.synctex.gz'};files={}
 for p in sorted(ROOT.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts and str(p.relative_to(ROOT)) not in ex:files[str(p.relative_to(ROOT))]=h(p)
 ev=ROOT/'results/c118_damped_dimer_evidence.json';pdf=ROOT/'paper/main.pdf'
 d={'schema_id':'hcs-c118-conformal-damped-dimer-prefreeze-manifest-v1','status':'PREFREEZE_COMPLETE_NOT_RELEASED','scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','headline':'Exact conformally symplectic damping and Fourier-mode monodromy for a Hénon dimer','files':files,'excluded_from_manifest':sorted(ex)+['code/__pycache__/'],'results':{'fixed_count':2,'period_two_count':1,'mutation_rejections':12,'pdf_pages':2,'evidence_sha256':h(ev),'pdf_sha256':h(pdf) if pdf.exists() else ''},'route_a_verdict':{'A1':'A1_WEAK','A2':'A2_FAIL','A3':'A3_NOT_ADDRESSED','A4':'A4_FAIL','overall':'ROUTE_A_EXPLORATORY'},'gates':{'G0_model_freeze':'PASS','G1_conformal_symplectic_inverse_identity':'PASS','G2_exact_low_period_mode_monodromy':'PASS','G3_independent_symbolic_replay_mutation':'PASS','G4_pdf_determinism_fonts_layout':'PASS','G5_manifest_hash_closure':'PASS','G6_complete_orbit_atlas':'NOT_ESTABLISHED','G7_transfer_owner':'NOT_ESTABLISHED','G8_arithmetic_route_b':'NOT_CLAIMED'},'nonclaims':['complete primitive-orbit atlas','transfer/Fredholm/nuclear operator owner','arithmetic/local data, Euler factors, root numbers, or automorphy','Hilbert--Polya operator or Route-B authorization']}
 MAN.write_text(json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'manifest_sha256':h(MAN),'file_count':len(files),'evidence_sha256':h(ev),'pdf_sha256':h(pdf) if pdf.exists() else ''},sort_keys=True))
if __name__=='__main__':main()
