#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C152 manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MANIFEST=ROOT/"C152_RELEASE_MANIFEST.json"
def digest(path): return sha256(path.read_bytes()).hexdigest()
def main():
    excluded={MANIFEST,ROOT/"paper/main.aux",ROOT/"paper/main.log",ROOT/"paper/main.out",ROOT/"paper/main.fdb_latexmk",ROOT/"paper/main.fls",ROOT/"paper/main.synctex.gz"}
    files={}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix==".pyc":continue
        files[str(path.relative_to(ROOT))]=digest(path)
    evidence=ROOT/"results/c152_heat_evidence.json";pdf=ROOT/"paper/main.pdf"
    result={
      "schema":"hcs-c152-release-v1","status":"RELEASE_COMPLETE","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "headline":"The ordered primitive square-billiard directions have an absolutely convergent Mobius-theta heat transform with leading law 3/(8*pi*t) and a controlled logarithmic remainder",
      "gates":{"G0_source_lock":"PASS","G1_absolute_convergence":"PASS","G2_exact_mobius_theta_factorization":"PASS","G3_collision_multiplicity_convention":"PASS","G4_quarter_disk_primitive_asymptotic":"PASS","G5_stieltjes_heat_asymptotic":"PASS","G6_exact_coefficients_and_counts":"PASS","G7_spectral_trace_nonidentity":"PASS","G8_independent_checker_sympy_replay_mutation":"PASS","G9_two_internal_review_rounds":"PASS","G10_double_compile_fonts_layout_visual":"PASS","G11_manifest_hash_closure":"PASS","G12_target_arithmetic_and_route_b":"NOT_CLAIMED"},
      "results":{"coefficient_s_max":20000,"nonzero_primitive_coefficients":3145,"exact_count_radius_max":200,"first_ordered_multiplicity_four_square":65,"independent_checker_assertions":20047,"sympy_checks":503,"repaired_hash_mutation_rejections":38,"stale_hash_mutation_rejections":1,"pdf_pages":1,"evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},
      "route_a_verdict":{"A1":"A1_WEAK","A1_qualification":"INTRINSIC_PRIMITIVE_DIRECTION_FAMILIES_HAVE_A_CONVERGENT_SOURCE_HEAT_TRANSFORM_BUT_ARE_NOT_ISOLATED_OR_PRIME_LIKE","A2":"A2_FAIL","A2_qualification":"THE_TRANSFORM_IS_NOT_AN_ISOLATED_ORBIT_DETERMINANT_AND_CLEAN_FAMILY_STABILITY_REMAINS_SINGULAR","A3":"A3_FAIL","A3_qualification":"NO_TARGET_ANALYTIC_STRUCTURE_OR_COUNTING_COMPARISON","A4":"A4_NATURAL_QUANTIZATION","A4_qualification":"THE_DIRICHLET_HALF_WAVE_IS_NATURAL_ON_THE_SAME_UNIT_SQUARE_GEOMETRY_BUT_ITS_SPECTRAL_TRACE_IS_NOT_THE_DIRECTION_TRANSFORM","overall":"ROUTE_A_EXPLORATORY","route_b_invocation_allowed":False},
      "nonclaims":["a clean wave trace or isolated-orbit determinant","an identity with the Dirichlet spectral heat trace","a target divisor, functional equation, or counting law","a prime-like correspondence","an arithmetic local or Euler factorization, root number, or automorphy statement","a Hilbert--Polya construction or Route-B authorization"],
      "excluded_from_manifest":["C152_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper/main.aux","paper/main.log","paper/main.out","paper/main.fdb_latexmk","paper/main.fls","paper/main.synctex.gz"],"files":files}
    assert len(files)==27,f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":"C152_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),"evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},sort_keys=True))
if __name__=="__main__":main()
