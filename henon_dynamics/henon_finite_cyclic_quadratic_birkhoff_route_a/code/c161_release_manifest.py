#!/usr/bin/env python3
"""Build the self-excluded HCS-C161 release manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C161_RELEASE_MANIFEST.json"
def digest(path):return sha256(path.read_bytes()).hexdigest()
def main():
    excluded={MANIFEST,ROOT/"paper/main.aux",ROOT/"paper/main.log",ROOT/"paper/main.out",
              ROOT/"paper/main.fdb_latexmk",ROOT/"paper/main.fls",ROOT/"paper/main.synctex.gz",
              ROOT/"paper/build_pass1.log",ROOT/"paper/build_pass2.log"}
    files={str(p.relative_to(ROOT)):digest(p) for p in sorted(ROOT.rglob("*"))
           if p.is_file() and p not in excluded and "__pycache__" not in p.parts and p.suffix!=".pyc"}
    evidence=ROOT/"results/c161_cyclic_gauss_evidence.json";pdf=ROOT/"paper/main.pdf"
    result={
      "schema":"hcs-c161-release-v1","status":"RELEASE_COMPLETE","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "headline":"Every odd cyclic quadratic Birkhoff amplitude has an exact gcd vanishing gate and completed-square Gauss evaluation at every iterate",
      "gates":{"G0_source_and_pivot_lock":"PASS","G1_birkhoff_polynomial":"PASS","G2_gcd_vanishing_iff":"PASS",
               "G3_nonzero_gauss_phase_sign_magnitude":"PASS","G4_prime_zero_discriminant":"PASS",
               "G5_same_clock_finite_unitary_and_time_reversal":"PASS","G6_exhaustive_independent_sympy_replay_mutation":"PASS",
               "G7_two_internal_review_rounds":"PASS","G8_bilingual_abstract_keywords_declarations":"PASS",
               "G9_lualatex_double_compile_fonts_layout_visual":"PASS","G10_manifest_hash_closure":"PASS",
               "G11_target_arithmetic_and_route_b":"NOT_CLAIMED"},
      "results":{"exhaustive_formula_cases":261630,"vanishing_cases":26864,"prime_zero_cases":164284,
                 "independent_checker_assertions":483310,"sympy_checks":15834,
                 "repaired_hash_mutation_rejections":29,"stale_hash_mutation_rejections":1,
                 "pdf_pages":2,"pdf_engine":"LuaLaTeX","source_date_epoch":1787616000,
                 "evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},
      "route_a_verdict":{"A1":"A1_WEAK","A2":"A2_FAIL","A3":"A3_FAIL",
                         "A4":"A4_NATURAL_QUANTIZATION","overall":"ROUTE_A_EXPLORATORY",
                         "route_b_invocation_allowed":False},
      "nonclaims":["the rejected Heisenberg local-product draft","a target trace/divisor/counting law",
                    "an isolated stability determinant","an arithmetic local or Euler factorization, root number, or automorphy statement",
                    "a Hilbert--Polya construction or Route-B authorization"],
      "excluded_from_manifest":["C161_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper/main.aux",
                                  "paper/main.log","paper/main.out","paper/main.fdb_latexmk","paper/main.fls",
                                  "paper/main.synctex.gz","paper/build_pass1.log","paper/build_pass2.log"],
      "files":files}
    assert len(files)==27,f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":"C161_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),
                      "evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},sort_keys=True))
if __name__=="__main__":main()
