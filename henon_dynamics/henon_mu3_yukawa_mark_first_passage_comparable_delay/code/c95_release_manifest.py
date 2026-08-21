#!/usr/bin/env python3
"""Write the deterministic C95 prefreeze ledger."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; MANIFEST=PROJECT/'C95_PREFREEZE_MANIFEST.json'
def main():
 excluded={MANIFEST,PROJECT/'paper/main.aux',PROJECT/'paper/main.fdb_latexmk',PROJECT/'paper/main.fls',PROJECT/'paper/main.log',PROJECT/'paper/main.out'}; prefixes=(PROJECT/'code/__pycache__',)
 files={}
 for path in sorted(PROJECT.rglob('*')):
  if path.is_file() and path not in excluded and not any(str(path).startswith(str(p)) for p in prefixes): files[str(path.relative_to(PROJECT))]=sha256(path.read_bytes()).hexdigest()
 result={
  'schema_id':'hcs-c95-prefreeze-manifest-v1','status':'PREFREEZE_COMPLETE_NOT_RELEASED','scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','headline':'Exact conditional first-passage delay laws for all 102 comparable C88 target pairs',
  'authority':{'c88':'4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b','c88_manifest':'aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5','c90':'c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978','c90_manifest':'4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737'},
  'files':files,'excluded_from_manifest':['C95_PREFREEZE_MANIFEST.json','code/__pycache__/','paper/main.aux','paper/main.fdb_latexmk','paper/main.fls','paper/main.log','paper/main.out'],
  'gates':{'G0_source_rebind_C88_C90':'PASS','G1_all_102_comparable_pairs':'PASS','G2_all_29478_joint_pmf_cells':'PASS','G3_order_delay_conditionals_marginals':'PASS','G4_checker_sympy_replay_hostile_mutations':'PASS','G5_paper_double_isolated_compile_visual_font_check':'PASS','G6_manifest_hash_verification':'PASS','G7_arithmetic_local':'NOT_CLAIMED','G8_release_closure':'PENDING'},
  'results':{'comparable_ordered_pair_count_including_reflexive':102,'joint_pmf_cell_count':29478,'positive_mass_conditional_row_count':1041,'hostile_mutations_rejected':17,'evidence_sha256':'53e5c9a1dbda2fa7e01af34ce6fc161ac102a312b003e1c86402ae7ec7373a3c','pdf_pages':2,'pdf_sha256':'60caec178a32d3d33d459cd0103c922fb5e967d25e06830fcd4011705ac3698c'},
  'nonclaims':['arithmetic/local data, Euler factors, root numbers, automorphy','full Burnside ring or full table of marks','Hilbert-Polya operators']}
 MANIFEST.write_bytes((json.dumps(result,sort_keys=True,indent=2)+'\n').encode()); print(sha256(MANIFEST.read_bytes()).hexdigest())
if __name__=='__main__': main()
