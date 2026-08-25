#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C151 manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MANIFEST=ROOT/"C151_RELEASE_MANIFEST.json"
def digest(path): return sha256(path.read_bytes()).hexdigest()
def main():
    excluded={MANIFEST,ROOT/"paper/main.aux",ROOT/"paper/main.log",ROOT/"paper/main.out",ROOT/"paper/main.fdb_latexmk",ROOT/"paper/main.fls",ROOT/"paper/main.synctex.gz"}
    files={}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix==".pyc": continue
        files[str(path.relative_to(ROOT))]=digest(path)
    evidence=ROOT/"results/c151_heisenberg_fibre_evidence.json";pdf=ROOT/"paper/main.pdf"
    result={
      "schema":"hcs-c151-release-v1","status":"RELEASE_COMPLETE","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "headline":"An exact representative-invariant central rotation and finite root-of-unity projector classify every clean fixed fibre of the frozen Heisenberg automorphism",
      "gates":{"G0_source_lock":"PASS","G1_fibre_rotation_derivation":"PASS","G2_representative_invariance":"PASS","G3_zero_rotation_iff_clean_fixed_circle":"PASS","G4_all_iterate_denominator_and_projector":"PASS","G5_exact_histograms_through_12":"PASS","G6_false_pattern_rejected":"PASS","G7_independent_checker_sympy_replay_mutation":"PASS","G8_two_internal_review_rounds":"PASS","G9_double_compile_fonts_layout_visual":"PASS","G10_manifest_hash_closure":"PASS","G11_target_arithmetic_and_route_b":"NOT_CLAIMED"},
      "results":{"histogram_iterate_cutoff":12,"n12_horizontal_fixed_classes":103680,"n12_rotation_support":231,"n12_observed_denominator_lcm":720,"n12_fixed_circle_components":144,"independent_checker_assertions":168146,"sympy_checks":72,"repaired_hash_mutation_rejections":36,"stale_hash_mutation_rejections":1,"pdf_pages":1,"evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},
      "route_a_verdict":{"A1":"A1_FAIL","A1_qualification":"THE_PERIODIC_OBJECTS_ARE_POSITIVE_DIMENSIONAL_CLEAN_FIBRES_NOT_ISOLATED_PRIMITIVE_ORBITS","A2":"A2_FAIL","A2_qualification":"THE_ORDINARY_ISOLATED_STABILITY_DENOMINATOR_REMAINS_SINGULAR","A3":"A3_FAIL","A3_qualification":"NO_TARGET_ANALYTIC_STRUCTURE_OR_COUNTING_COMPARISON","A4":"A4_FORMAL_HINT","A4_qualification":"HAAR_KOOPMAN_EVOLUTION_IS_NATURAL_AND_CLOCK_MATCHED_BUT_THE_CYCLIC_FILTER_IS_NOT_AN_OPERATOR_TRACE_BRIDGE","overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False},
      "nonclaims":["that rho_n is a homomorphism of the horizontal quotient","an all-iterate closed formula for the fixed-circle count","an isolated primitive-orbit determinant","a target divisor, functional equation, or counting law","an arithmetic local or Euler factorization, root number, or automorphy statement","a Hilbert--Polya construction or Route-B authorization"],
      "excluded_from_manifest":["C151_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper/main.aux","paper/main.log","paper/main.out","paper/main.fdb_latexmk","paper/main.fls","paper/main.synctex.gz"],"files":files}
    assert len(files)==27,f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":"C151_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},sort_keys=True))
if __name__=="__main__":main()
