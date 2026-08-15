# Compilation report — Paper 36 / SD-C38

Status: **SUCCESS**

Build date: 2026-08-15 UTC
Manuscript: *Fill the Relations, Lose the Clock: Chain Quotients of an Affine
Symbolic Shift*

## Clean build

The manuscript was compiled from a clean output state with

    pdflatex → bibtex → pdflatex × 3

The four TeX passes stabilized all citations, cross-references, tables, and
TikZ figures. Rebuildable LaTeX and BibTeX auxiliaries are not retained in
the authority directory.

## Output

| Check | Result |
|---|---|
| PDF | `main.pdf` |
| pages | 11 |
| page geometry | A4, 595.276 × 841.890 pt |
| file size | 389,058 bytes |
| PDF version | 1.5 |
| fonts | 24/24 Type 1 fonts embedded and subset |
| raster images | 0 |
| vector figures | 3/3 pure TikZ |

All 11 pages were inspected at rendered-page resolution. The audit covered
the title and abstract, the three source/chain firewalls, the affine relation
cell, the Cayley-chain quadrilemma, the trace-class Hashimoto calculation,
the generic all-orders supercancellation control, both exact-audit tables,
the Route decision, the bibliography, and both appendices. No clipping,
overlap, illegible label, malformed page, or blank page was found.

## Log and source audit

- TeX errors: 0.
- Undefined citations: 0.
- Undefined cross-references: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Stale rerun warnings after the fourth TeX pass: 0.
- Section modules included/present: 12/12.
- Figure inputs included/present: 3/3.
- Bibliography entries cited/present: 10/10, with no orphan or missing key.
- Draft markers (`TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, `??`, `[?]`): 0.
- Route tuple in the PDF:
  `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL,
  A4_FAIL)`.
- Overall verdict: `ROUTE_A_REJECTED`; Route B: `LOCKED`.
- Branch decision: `CLOSE_COMPLETE_AFFINE_CHAIN_QUOTIENT_BRANCH`.

The final source layer passes 33/33 internal checks; the independent evaluator
reproduces 33/33 prototype semantic checks and passes 35/35 authority
integration checks; and the authority suite passes 53/53 tests. Fresh A/B and
cache-free cold C reproduce all 19 scientific payloads and all six captured
stage stdout streams byte-identically. The final package contains 27 result
files, passes 71/71 strict integrity checks, and has a sorted 44-entry
code/result ledger whose 44/44 entries verify. All 48 sampled scalar chain-lift
powers vanish exactly; the all-orders statement is proved independently.

## Final fingerprints

| Artifact | SHA-256 |
|---|---|
| `main.pdf` | `be20604aff65d580a94b852b59fb03fdd07767192bdac02c2a20084b17691c75` |
| canonical code/result ledger | `6458284dfd8f8e18100571ca695e3a8d5815e92588975d53a8201595344a213f` |
| scientific aggregate | `58a5d3b404d85163edfe74bea45b077da07ac6ff4f0794aff0bf9f1fbcf6ea9e` |
| research lock | `c5834fb3b95a652f09300b6153265392e179fac9e71649a8849093a2118d082b` |
| environment lock | `67f4e67f32637886b7877f28d076dfefa45fa473d37d4e78153167c69e12f736` |
| dependency lock | `b92d875c3ccebc87fd0037af3eb7566df2bcbbcea45688f9f28675085f8d1fbd` |
| integrity audit | `2954f8eaf40bd88f6a81b8ba04f43faf1c298642df8c99b9b9806b816419309d` |
| idempotence certificate | `1ae54c221801ad1aaf53e869014a6f3bd6362a93d3d14f38c43078926ecf49d3` |
| experiment report | `b888140a7cd5a45a7fdb00091272667c2e1477e3233877ffe0fdc1f6957e9513` |
| Route-A v0.2 YAML | `a9342f1d99cadef9073ce14ddfe05fcf4263b294a0981f1d89699990ec9d0b60` |

## Review boundary

No peer-review or LLM review loop was run, following the explicit project
instruction. The checks above are deterministic compilation, citation,
artifact, typography, and visual-QA checks only.
