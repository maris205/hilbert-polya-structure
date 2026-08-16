# Compilation report — Paper 37 / SD-C39

Status: **SUCCESS**

Build date: 2026-08-15 UTC
Manuscript: *Cancel the Relator, Lose the Ledger: Local-Coefficient Saturation
on an Affine Hashimoto Shift*

## Clean build

The manuscript was compiled from a clean output state with

    pdflatex → bibtex → pdflatex × 3

The four TeX passes stabilized all citations, cross-references, tables, and
TikZ figures. Rebuildable LaTeX and BibTeX auxiliaries are not retained in the
authority directory.

## Output

| Check | Result |
|---|---|
| PDF | `main.pdf` |
| pages | 13 |
| page geometry | A4, 595.276 × 841.890 pt |
| file size | 400,769 bytes |
| PDF version | 1.5 |
| fonts | 24/24 Type 1 fonts embedded and subset |
| raster images | 0 |
| vector figures | 3/3 pure TikZ |

All 13 pages were inspected at rendered-page resolution. The audit covered
the title, abstract and status box; the finite-coefficient fork; the primary
literature boundary; the uniformly bounded matrix Fredholm model; the
saturation theorem; the ordinary-factor obstruction; the shear path and
mixed-leak figure; the normal-closure funnel; both exact-audit tables; the
Route decision; the complete bibliography; and both appendices. No clipping,
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
- Bibliography entries cited/present: 8/8, with no orphan or missing key.
- Draft-marker scan: 0 matches.
- Route tuple in the PDF:
  `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL,
  A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`.
- Overall verdict: `ROUTE_A_REJECTED`; Route B: `LOCKED`.
- Branch decision: `CLOSE_LOCAL_COEFFICIENT_SATURATION_BRANCH`.

The independent authority layer reproduces 131/131 source/evaluator
assertions and passes 32/32 integration tests. Fresh A/B and isolated cold C
reproduce all scientific, source-packet, and Route bytes; the temporary copy
is removed. Four metadata states, two manifest states, and the second primary
materialization preserve the scientific bytes. The exact result set contains
26 files. All 82/82 full-integrity checks and all 39/39 immutable-ledger
entries pass; the managed integration layer contains 41 canonical text files.
The pre-seal Route YAML is schema-audited separately and excluded from the
immutable ledger so its paired provenance can be bound metadata-only.

## Final fingerprints

| Artifact | SHA-256 |
|---|---|
| `main.pdf` | `e3cc72f2fd10d0ab878fe0aa2874767d372cd507fe6f7a07e87c9033b99dbc6a` |
| scientific aggregate | `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e` |
| 39-entry immutable ledger | `8f47abf523451e1fdb84363d7a1b85b1009bc6e619700389959f4b39f01b8b6e` |
| full integrity audit | `ff2f805c91d4b393e8d09d31dc260bbda528d70b54b970547f285e6470430432` |
| research lock | `c67960f0534a5646bedca2349db408c87e66c32252b6d11c586f9a129b15a015` |
| dependency lock | `93bb9c1aa95c1621862820cdf2c803188154b8acdbf87050e6b8102e0d00bd9b` |
| idempotence certificate | `f685ac3e57af13a9430c9bd719ac7495517693726cac9813fca7106412851bc3` |
| exact result-set declaration | `3f5f78f6584c0256481af0fcaaea34b3f22c51321f9ccd1b3c5dc7d82f82e588` |
| integration test results | `bf7722a67e44e7dec6617dba094f6977c50e885eb93ce2b240d877ef703fb0f5` |
| experiment report | `99dfbe9dc1e4eb772e93bfd25741589bf7aae61ae5d9a725079618402825c888` |
| independent Route evaluation | `c45b419d445d365eb2d13ee4e471dd40bf8407540cfbd466be2d3a47d39b66cd` |
| pre-seal Route-A v0.2 YAML | `a74c63544aaf6cbe398de2516fc5b03cec11ef5290a768de30aeae553c83bcdb` |

## Review boundary

No peer-review or LLM review loop was run, following the explicit project
instruction. The checks above are deterministic mathematical, primary-source,
compilation, citation, provenance, artifact, and visual-QA checks only.
