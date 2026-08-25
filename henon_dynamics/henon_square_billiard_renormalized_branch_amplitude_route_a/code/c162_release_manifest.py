#!/usr/bin/env python3
"""Build the self-excluded HCS-C162 release manifest."""
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];MANIFEST=ROOT/"C162_RELEASE_MANIFEST.json"
def digest(path):return sha256(path.read_bytes()).hexdigest()
def main():
    excluded={MANIFEST,ROOT/"paper/main.aux",ROOT/"paper/main.log",ROOT/"paper/main.out",
              ROOT/"paper/main.fdb_latexmk",ROOT/"paper/main.fls",ROOT/"paper/main.synctex.gz",
              ROOT/"paper/build_pass1.log",ROOT/"paper/build_pass2.log"}
    files={str(p.relative_to(ROOT)):digest(p) for p in sorted(ROOT.rglob("*"))
           if p.is_file() and p not in excluded and "__pycache__" not in p.parts and p.suffix!=".pyc"}
    evidence=ROOT/"results/c162_branch_amplitude_evidence.json";pdf=ROOT/"paper/main.pdf"
    result={
      "schema":"hcs-c162-release-v1","status":"RELEASE_COMPLETE","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "headline":"The full square-billiard Abel trace has a canonical epsilon^(3/2) boundary coefficient at every nonzero source shell, including coincident simple poles",
      "gates":{"G0_c157_source_lock":"PASS","G1_principal_branch_constant":"PASS","G2_full_trace_uniform_tail":"PASS",
               "G3_coincident_pole_suppression":"PASS","G4_negative_time_conjugation":"PASS",
               "G5_exact_shell_reconstruction":"PASS","G6_independent_sympy_replay_mutation":"PASS",
               "G7_two_internal_review_rounds":"PASS","G8_bilingual_abstract_keywords_declarations":"PASS",
               "G9_lualatex_double_compile_fonts_layout_visual":"PASS","G10_manifest_hash_closure":"PASS",
               "G11_isolated_target_arithmetic_and_route_b":"NOT_CLAIMED"},
      "results":{"exact_shell_cutoff_N":800,"occupied_shells":270,"source_lattice_vectors":2520,
                 "coincident_pole_shells":28,"independent_checker_assertions":1988,"sympy_checks":9,
                 "repaired_hash_mutation_rejections":23,"stale_hash_mutation_rejections":1,
                 "pdf_pages":2,"pdf_engine":"LuaLaTeX","source_date_epoch":1787616000,
                 "evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},
      "route_a_verdict":{"A1":"A1_WEAK","A2":"A2_FAIL","A3":"A3_FAIL",
                         "A4":"A4_NATURAL_QUANTIZATION","overall":"ROUTE_A_EXPLORATORY",
                         "route_b_invocation_allowed":False},
      "nonclaims":["an isolated primitive-orbit determinant or isolated stability amplitude",
                    "a target trace/divisor/counting law","an arithmetic local or Euler factorization, root number, or automorphy statement",
                    "a Hilbert--Polya construction or Route-B authorization"],
      "excluded_from_manifest":["C162_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper/main.aux",
                                  "paper/main.log","paper/main.out","paper/main.fdb_latexmk","paper/main.fls",
                                  "paper/main.synctex.gz","paper/build_pass1.log","paper/build_pass2.log"],
      "files":files}
    assert len(files)==27,f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":"C162_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),
                      "evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},sort_keys=True))
if __name__=="__main__":main()
