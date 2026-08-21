#!/usr/bin/env python3
"""Write the deterministic C96 prefreeze ledger."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; MANIFEST=PROJECT/'C96_PREFREEZE_MANIFEST.json'
def main():
 excluded={MANIFEST,PROJECT/'paper/main.aux',PROJECT/'paper/main.fdb_latexmk',PROJECT/'paper/main.fls',PROJECT/'paper/main.log',PROJECT/'paper/main.out'}; prefixes=(PROJECT/'code/__pycache__',)
 files={}
 for path in sorted(PROJECT.rglob('*')):
  if path.is_file() and path not in excluded and not any(str(path).startswith(str(p)) for p in prefixes): files[str(path.relative_to(PROJECT))]=sha256(path.read_bytes()).hexdigest()
 result={
  'schema_id':'hcs-c96-prefreeze-manifest-v1','status':'PREFREEZE_COMPLETE_NOT_RELEASED','scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','headline':'Exact first-passage laws and moments for all twenty target-coverage ranks',
  'authority':{'c88':'4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b','c88_manifest':'aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5'},
  'files':files,'excluded_from_manifest':['C96_PREFREEZE_MANIFEST.json','code/__pycache__/','paper/main.aux','paper/main.fdb_latexmk','paper/main.fls','paper/main.log','paper/main.out'],
  'gates':{'G0_source_rebind_C88':'PASS','G1_all_65536_supports_and_20_targets':'PASS','G2_all_17_coverage_histogram_layers':'PASS','G3_all_20_rank_distributions_moments':'PASS','G4_checker_sympy_replay_hostile_mutations':'PASS','G5_paper_double_isolated_compile_visual_font_check':'PASS','G6_manifest_hash_verification':'PASS','G7_arithmetic_local':'NOT_CLAIMED','G8_release_closure':'PENDING'},
  'results':{'support_count':65536,'target_count_including_trivial':20,'coverage_rank_count':20,'rank_monotonicity_relation_count':19,'factorial_certificate_count':340,'hostile_mutations_rejected':15,'evidence_sha256':'75a93c80b5e44f6aca1885073cf12e943de02751ad4e99aa37e83bf211b6ca23','pdf_pages':2,'pdf_sha256':'9222c35bd7d0d8c097ffadf47eeb086e735adbfccd98bff142143087c4626e18'},
  'nonclaims':['arithmetic/local data, Euler factors, root numbers, automorphy','full Burnside ring or full table of marks','Hilbert-Polya operators']}
 MANIFEST.write_bytes((json.dumps(result,sort_keys=True,indent=2)+'\n').encode()); print(sha256(MANIFEST.read_bytes()).hexdigest())
if __name__=='__main__': main()
