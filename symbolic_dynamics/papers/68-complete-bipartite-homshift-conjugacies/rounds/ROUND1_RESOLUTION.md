# Round 1 resolution

**Review provenance:** independent cross-agent review; requested GPT-5.4
child unavailable because of the structural thread cap.  External release is
**HOLD**.

## Issue ledger

| Review issue | Severity | Resolution |
|---|---:|---|
| C1 false component-wise finite-shape count | CRITICAL | Replaced by the single-global-phase formula, including `N(empty)=1`; rewrote proof and all dependent ledgers. |
| C1 semantically invalid control | CRITICAL | Split globally extendible restrictions from locally admissible patterns; added remote even and remote even--odd counterexamples. |
| M1 fixed-pair dimer wording | MAJOR | The theorem now gives memory set `{-e_1,0,e_1}` and explains the symbol-selected neighbour. |
| m1 dimension range | MINOR | Abstract now states the proved range `d>=1`. |
| m2 Gibbs equality chain | MINOR | Added arbitrary joint dimer marginal, within-dimer equality, and across-dimer entropy-rate equality. |
| m3 factor-pair corollary | MINOR | Made the distinct-factor-pair clause conditional and retained the `(2,6)`/`(3,4)` witness. |

The key repaired formula for nonempty `F` is

```text
N(F)=m^|F cap E| n^|F cap O| + n^|F cap E| m^|F cap O|.
```

For `(m,n)=(2,3)`, the control now distinguishes two remote even sites
(`13` extendible versus `25` locally admissible) and a remote even--odd pair
(`12` versus `25`).

## Verification

- `python3 code/verify_complete_bipartite.py`: `ALL CHECKS PASS`.
- Full build: three total `pdflatex` runs---one before BibTeX and two after
  BibTeX; all exits zero.
- Log scan: zero undefined references/citations, overfull/underfull boxes, or
  package/LaTeX warnings.
- `main_round1.pdf`: 7 A4 pages; SHA-256
  `b96ac6118ad81839eb796ad5640357ce710ff9e1372411bfa7931883dd3ac7c6`.
- Preserved `main_round0_original.pdf`: SHA-256
  `e072cc764f80e28accb3a3a586246a6e82219e1e3bf9f7f1ec494221dbe84479`.

Round 1 is resolved.  Round 2 must independently re-audit the corrected
global restriction formula and every theorem that uses the entropy value.
