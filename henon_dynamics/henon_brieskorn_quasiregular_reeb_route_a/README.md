# HCS-C370: Brieskorn quasiregular Reeb dynamics

This package proves the complete normalized Reeb period, fixed-set,
Morse--Bott, transverse-rotation, exceptional CZ, Seifert quotient, and
principal RS-index atlas for pairwise-coprime links (Sigma(2,p,q)).

## Main artifacts

- `THEOREM_PACKAGE.md`: assumptions, theorems, proofs, limitations, references,
  and scope.
- `paper/main.pdf`: final theorem paper; `main_round0_original.pdf`,
  `main_round1.pdf`, and `main_round2.pdf` retain the three revision stages.
- `results/c370_brieskorn_reeb_evidence.json`: canonical exact receipt.
- `evaluations/route_a/HCS-C370/2026-09-04.yaml`: strict Route-A record.
- `SOURCE_AUDIT.md`: literature ownership and nearest-workspace collision audit.
- `ASSUMPTIONS.md`, `CLAIMS.md`, `SCOPE.md`, `LIMITATIONS.md`, and
  `REFERENCES.md`: explicit research boundary and source ledger.
- `REPRODUCIBILITY.md`, `requirements.txt`, and `tests/test_c370_smoke.py`:
  environment and smoke-test contract.
- `EXPERIMENT_PLAN.md` and `results/TEST_REPORT.md`: reproducibility contract.
- `C370_RELEASE_MANIFEST.json`: self-excluded manifest for exactly 35 payloads
  and 36 physical files.

## Reproduce

```bash
python code/c370_brieskorn_reeb_producer.py
python code/c370_brieskorn_reeb_checker.py
python code/c370_brieskorn_reeb_sympy_crosscheck.py
python code/c370_brieskorn_reeb_replay.py
python code/c370_brieskorn_reeb_mutation.py
python code/c370_release_manifest.py
```

Dependencies and command roles are listed in `code/README.md`. The release
script refuses optimized Python. For a clean PDF rebuild use
`python code/c370_release_manifest.py --build-pdfs`; after updating the compile
report, use `--write` once to regenerate the manifest.

## Claims and limitations

The general theorem is analytic. The (q\le101) grid verifies serialization,
formulas, branch counts, and boundary handling only. The package does not
compute contact homology and does not discretize the principal orbit continuum.
It asserts no target arithmetic or target spectral result.

Route-A tuple:

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
```

Overall: `ROUTE_A_EXPLORATORY`. Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
