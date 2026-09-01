# P140 improvement log

## Round A — 2026-09-01 UTC

**Review input:** `HOSTILE_REVIEW_A.md`.  **Initial disposition:** `REPAIR`.
**Closure:** `REPAIRED / GO_INTERNAL / HOLD_EXTERNAL`.

### Finding disposition

| finding | severity | disposition | exact closure |
|---|---|---|---|
| `M-A-01` | major | closed | State `tau_1=0` almost surely; treat both embedded vectors as empty at `n=1`; retain the empty-product Laplace and empty-sum moment boundary; restrict `Beta(1/2,m)` to `n=2m+1>=3`, `m>=1`; state the Gamma limit along odd lengths with `m -> infinity`. |

The proof status is **PROVABLE AFTER SCOPE CORRECTION**. The invalid symbol
`Beta(1/2,0)` was an allowed-boundary statement defect, not a counterexample
to the nondegenerate clock law.

### Reader-facing changes

- `main.tex`: abstract, Theorem 4.1 boundary, theorem proof, paragraph before
  Corollary 4.2, Corollary 4.2 scope, and Theorem 4.3 limit scope.
- `README.md`, `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`,
  `CLAIMS_EVIDENCE.md`, `BUILD.md`, and `FINAL_QA.md`: synchronized Round-A
  status and boundary language.

### Deliberate nonchanges

- The two-run kernel, endpoint/history laws, marked cross-count law, and
  one-cross coefficient are unchanged.
- The nondegenerate Laplace, Beta, moment, and Gamma formulas are unchanged.
- `references.bib`, `code/verify.py`, and canonical verifier stdout are
  byte-unchanged.
- `main_round0_original.pdf` is preserved byte for byte.

### Artifact delta

| artifact | Round 0 SHA-256 | Round 1 SHA-256 |
|---|---|---|
| `main.tex` | `0479c29f34d7ab4362074df3ab71719ac81041a6068fd3f0a498545b25e947c9` | `1e10db2a0bedadc9c35df6265867264813bf165298b83c16cc60434dcb158473` |
| `main.pdf` | `2b151d0916d8d43d26988f3f70a25885fdf8e71255657dc1486bc300e070aa99` | `a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18` |

`main_round0_original.pdf` retains the Round-0 hash. `main_round1.pdf` is
byte-identical to the repaired current PDF. Canonical replay remains
190,740/190,740 assertions passing.

## Round B — 2026-09-01 UTC

**Review input:** `HOSTILE_REVIEW_B.md`.  **Disposition:**
`PASS / GO_INTERNAL / HOLD_EXTERNAL`.

The second independent reviewer reconstructed the repaired `n=1` boundary,
the complete two-run and crossing laws, and the whole-history clock
separation.  Its standalone checks contributed 818 hostile conditions without
importing the paper-local verifier.  It returned zero critical, major, and
minor repair items; no further source change was justified.

`main_round2.pdf` is therefore the unchanged sign-off copy of the repaired
Round-1 manuscript.  Both have SHA-256
`a04683cd14c2ac0ecea73ae6baf98f17ef1a0c947ba712f25529b0087d839c18`.
