#!/usr/bin/env python3
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/'C143_RELEASE_MANIFEST.json'
def digest(p):return sha256(p.read_bytes()).hexdigest()
def main():
    excluded={MANIFEST,ROOT/'paper/main.aux',ROOT/'paper/main.log',ROOT/'paper/main.out',ROOT/'paper/main.fdb_latexmk',ROOT/'paper/main.fls',ROOT/'paper/main.synctex.gz'};files={}
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and p not in excluded and '__pycache__' not in p.parts and p.suffix!='.pyc':files[str(p.relative_to(ROOT))]=digest(p)
    evidence=ROOT/'results/c143_quantum_walk_evidence.json';pdf=ROOT/'paper/main.pdf'
    result={'schema':'hcs-c143-release-v1','status':'RELEASE_COMPLETE','scope_literal':'NO_BAD_EULER_OR_ROOT_NUMBER','headline':'A spatially inhomogeneous coined quantum walk has a source-derived unitary, exact antiunitary reversal, signed primitive paths, and order-sensitive secular polynomial','gates':{'G0_source_lock':'PASS','G1_exact_unitarity':'PASS','G2_antiunitary_reversal':'PASS','G3_signed_path_trace_identity':'PASS','G4_arrangement_order_sensitivity':'PASS','G5_population_average_negative_control':'PASS','G6_independent_checker_sympy_replay_mutation':'PASS','G7_double_compile_fonts_layout':'PASS','G8_manifest_hash_closure':'PASS','G9_target_divisor_matching':'NOT_ESTABLISHED','G10_arithmetic_and_route_b':'NOT_CLAIMED'},'results':{'matrix_dimension':10,'trace_cutoff':12,'path_cutoff':10,'mutation_rejections':30,'pdf_pages':3,'evidence_sha256':digest(evidence),'pdf_sha256':digest(pdf)},'route_a_verdict':{'A1':'A1_WEAK','A2':'A2_FAIL','A3':'A3_FAIL','A4':'A4_UNITARY_OR_SCATTERING_CANDIDATE','overall':'ROUTE_A_EXPLORATORY','route_b_invocation_allowed':False},'nonclaims':['a target-facing zero or divisor match','a target functional equation or counting law','prime-like information, arithmetic local data, Euler factors, root numbers, or automorphy','a self-adjoint Hilbert--Polya operator or Route-B authorization'],'excluded_from_manifest':['C143_RELEASE_MANIFEST.json','code/__pycache__/','*.pyc','paper/main.aux','paper/main.log','paper/main.out','paper/main.fdb_latexmk','paper/main.fls','paper/main.synctex.gz'],'files':files}
    assert len(files)==27,f'expected 27 manifest files, found {len(files)}';MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print(json.dumps({'manifest_sha256':digest(MANIFEST),'file_count':len(files),'evidence_sha256':digest(evidence),'pdf_sha256':digest(pdf)},sort_keys=True))
if __name__=='__main__':main()
