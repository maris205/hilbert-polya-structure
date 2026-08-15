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
| file size | 389,045 bytes |
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
files, passes 74/74 strict integrity checks, and has a sorted 43-entry
immutable code/result ledger whose 43/43 entries verify. The Route card is
schema-audited separately so its paired provenance can be sealed metadata-only.
All 48 sampled scalar chain-lift
powers vanish exactly; the all-orders statement is proved independently.

## Final fingerprints

| Artifact | SHA-256 |
|---|---|
| `main.pdf` | `d163715c5b324dd24bffe780c9cbe71a66c8f9eb1bcde97c640ef3b275fc6d72` |
| canonical code/result ledger | `2874181eb08de0c9b8a0a35a5627ddc4dac1c865457bcf134c508d84669983b2` |
| scientific aggregate | `58a5d3b404d85163edfe74bea45b077da07ac6ff4f0794aff0bf9f1fbcf6ea9e` |
| research lock | `1f1f5ef49f09cf234063e23d6e12464cc24592bfb66648a6dcbb7e695f16051c` |
| environment lock | `67f4e67f32637886b7877f28d076dfefa45fa473d37d4e78153167c69e12f736` |
| dependency lock | `b92d875c3ccebc87fd0037af3eb7566df2bcbbcea45688f9f28675085f8d1fbd` |
| integrity audit | `903229d0e823a48b0575ee7078c16aecc654a288f04f5517c5f1bbb4c30e9195` |
| idempotence certificate | `9b896c40e0260e7551397c65cff008f3e2cd29c55a4a93e69f173d9cea65c253` |
| experiment report | `8727a613806ad9dfe6e05ef59a06225c4e6274eafb48e7ecddcb6dccf3a50b95` |
| Route-A v0.2 YAML | schema/provenance audited separately; excluded from Stage-1 ledger |

## Review boundary

No peer-review or LLM review loop was run, following the explicit project
instruction. The checks above are deterministic compilation, citation,
artifact, typography, and visual-QA checks only.
