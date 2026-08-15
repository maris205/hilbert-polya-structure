# Compilation report — Paper 35 / SD-C37

Status: **SUCCESS**

Build date: 2026-08-15 UTC
Manuscript: *Acyclicity, Backtracks, and Relation Cycles in an Affine
Semigroup Benchmark*

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
| file size | 398,125 bytes |
| PDF version | 1.5 |
| fonts | 24/24 Type 1 fonts embedded and subset |
| raster images | 0 |
| vector figures | 3/3 pure TikZ |

All 11 pages were inspected at rendered-page resolution. The audit covered
the title and abstract, all three object-firewall diagrams, the affine
relation cycle, whole-operator ownership, congruence quotients, the exact
census table, the Route decision, the bibliography, and both appendices. No
clipping, overlap, illegible label, malformed page, or blank page was found.

## Log and source audit

- TeX errors: 0.
- Undefined citations: 0.
- Undefined cross-references: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Stale rerun warnings after the fourth TeX pass: 0.
- Section modules included/present: 12/12.
- Figure inputs included/present: 3/3.
- Bibliography entries cited/present: 16/16, with no orphan or missing key.
- Draft markers (`TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, `??`, `[?]`): 0.
- Route tuple in the PDF:
  `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL,
  A4_FAIL)`.
- Overall verdict: `ROUTE_A_REJECTED`; Route B: `LOCKED`.
- Branch decision: `CLOSE_AFFINE_SEMIGROUP_PARTITION_IDENTIFICATION_BRANCH`.

The canonical exact audit passes 84/84 tests and 10/10 independent evaluator
gates. Fresh A/B and cache-free cold C runs reproduce 23 scientific payloads
byte-identically. The final package records 520 positive height rows, 520
symmetric backtracks, 699,040 frozen words, 126,553 admissible words, 88
primitive cyclically nonbacktracking classes, eight affine relation witnesses,
and 48 quotient rows. Metadata-seal, dependency, idempotence, UTF-8/LF, exact
one-terminal-newline, and no-cache checks all pass.

## Final fingerprints

| Artifact | SHA-256 |
|---|---|
| `main.pdf` | `306be2b35072e94a81e2fc5268888d9738ac64328b956cd16ea9b59a09ba36a2` |
| canonical code/result ledger | `8ca89e858fadd9069916eeba3584aeae005ba0f1189dc7ec7c51c6cdde6b7e36` |
| scientific aggregate | `94df5a68ef2a3a9a05bedddea2b6f210e437622a3d77cb1f9ec4aff351a55fed` |
| research lock | `92364bd4e9dd8cae1775e3831c135994b2d8a5f6bddb8e75ef2750a22f0fd805` |
| integrity audit | `b37a01fcbe32018b96689e4a60d61eb094110c420d1b5328ab5e1427b53a5707` |
| Route-A v0.2 YAML | `d67c1fd276b1065a0504866cb758dea9a6940994d77be2c04d50d82785844d9c` |

## Review boundary

No peer-review or LLM review loop was run, following the explicit project
instruction. The checks above are deterministic compilation, citation,
artifact, typography, and visual-QA checks only.
