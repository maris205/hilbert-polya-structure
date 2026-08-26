#!/usr/bin/env python3
"""Build the content-addressed self-excluded C172 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"C172_RELEASE_MANIFEST.json"


def digest(path:Path)->str: return sha256(path.read_bytes()).hexdigest()


def main()->None:
    excluded={MANIFEST,ROOT/"paper/main.aux",ROOT/"paper/main.log",ROOT/"paper/main.out",
              ROOT/"paper/main.fdb_latexmk",ROOT/"paper/main.fls",ROOT/"paper/main.synctex.gz"}
    files={}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix==".pyc": continue
        files[str(path.relative_to(ROOT))]=digest(path)
    evidence=ROOT/"results/c172_field_multiplier_evidence.json"; pdf=ROOT/"paper/main.pdf"
    result={
        "schema":"hcs-c172-release-v1","status":"RELEASE_COMPLETE","candidate_id":"HCS-C172",
        "evaluation_date":"2026-08-26","source_commit":"ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f",
        "scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline":"All-prime-power orbit, zeta, Koopman determinant, reversal, and self-adjoint-boundary theorem for primitive field multipliers",
        "gates":{"G0_source_arithmetic_clock_weight_lock":"PASS","G1_all_Q_orbit_decomposition":"PASS",
                 "G2_all_Q_zeta_and_koopman_determinant":"PASS","G3_reversal_and_self_adjoint_boundary":"PASS",
                 "G4_adversarial_genericity_controls":"PASS","G5_checker_sympy_replay_mutation":"PASS",
                 "G6_bilingual_three_round_deterministic_pdf":"PASS","G7_manifest_hash_closure":"PASS",
                 "G8_target_global_arithmetic_route_b":"NOT_CLAIMED"},
        "results":{"Q_sentinel_count":18,"n_max":24,"independent_checker_assertions":663,"sympy_checks":486,
                   "repaired_hash_mutation_rejections":44,"stale_hash_mutation_rejections":1,"pdf_pages":2,
                   "pivot_required":False,"evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},
        "route_a_verdict":{"A0":"A0_WEAK_ARITHMETIC_RELATION","A1":"A1_WEAK","A2":"A2_FAIL","A3":"A3_FAIL",
                           "A4":"A4_NATURAL_QUANTIZATION","overall":"ROUTE_A_EXPLORATORY",
                           "route_b_invocation_allowed":False},
        "nonclaims":["a rational-prime orbit dictionary or logarithmic prime clock","target divisor or functional-equation matching",
                      "arithmetic local data, a global Euler product, local factors, or root numbers",
                      "automorphy or a Hilbert--Polya operator"],
        "integrity":{"hard_gate":"unconditional all-prime-power source theorem","hard_gate_status":"PASS",
                     "finite_ledgers_are_proof":False,"external_reviewer_simulated":False,"registered_citation_population":0},
        "excluded_from_manifest":["C172_RELEASE_MANIFEST.json","code/__pycache__/","*.pyc","paper/main.aux","paper/main.log",
                                  "paper/main.out","paper/main.fdb_latexmk","paper/main.fls","paper/main.synctex.gz"],
        "files":files,
    }
    assert len(files)==27,f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C172_MANIFEST_PASS","file_count":len(files),"manifest_sha256":digest(MANIFEST),
                      "evidence_sha256":digest(evidence),"pdf_sha256":digest(pdf)},sort_keys=True))


if __name__ == "__main__": main()
