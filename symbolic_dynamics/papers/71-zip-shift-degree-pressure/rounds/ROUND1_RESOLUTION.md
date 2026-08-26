# Round 1 resolution

**Review provenance:** independent cross-agent review; requested GPT-5.4
child unavailable because of the structural thread cap.  External release is
**HOLD**.

## Issue ledger

| Review issue | Severity | Resolution |
|---|---:|---|
| M1 Bowen versus capacity entropy | MAJOR | Fixed an explicit product metric; proved the exact `(n,2^-M)` Bowen-ball cylinder identity; supplied variable-length Carathéodory type covers and a Bernoulli local-entropy lower bound. |
| m1 natural-extension entropy bridge | MINOR | Added finite-dimensional inverse-limit distributions, uniqueness/affinity, and a generating-partition entropy argument. |
| m2 periodic alignment | MINOR | Added exact positive and negative coordinate formulae and listed the actual cyclic order of degrees. |
| m3 endpoint wording | MINOR | Restated the formula for `k_min` and `k_max`, including all `m_k` extremal fibres and the uniform coincidence. |
| m4 direct-owner version | MINOR | Added arXiv:2407.01828 to the published Martins--Mattos--Varão bibliography entry. |

## Verification

- `python3 code/verify_degree_pressure.py`: `ALL CHECKS PASS`.
- Full build: three total `pdflatex` runs---one before BibTeX and two after
  BibTeX; all exits zero.
- Log scan: zero undefined references/citations, overfull/underfull boxes, or
  package/LaTeX warnings.
- `main_round1.pdf`: 9 A4 pages; SHA-256
  `2610aac081aba4ff9032f66a6e821a819b004f04503545ad748742b72b3b6c64`.
- Preserved `main_round0_original.pdf`: SHA-256
  `7f51cb14af412305849f1929f0a4bfec0c7a72a48fbd5082b4d7429446b939b2`.

Round 1 is resolved.  Round 2 must audit the precise Bowen-cylinder equality,
countable-stability/Carathéodory step, local-entropy lower bound, endpoint
limit, and every index in the periodic coordinate formula.
