# Compilation report — Paper 34 / SD-C36

Status: **SUCCESS**

Build date: 2026-08-15 UTC
Manuscript: *Recognition Before Recurrence: A Positive Compiler Quadrilemma
for Arithmetic Markov Shifts*

## Clean build

The manuscript was compiled from a clean output state with

    pdflatex → bibtex → pdflatex × 3

The four TeX passes stabilized all citations, cross-references, tables, and
TikZ figures.  Rebuildable LaTeX and BibTeX auxiliaries are not retained in
the authority directory.

## Output

| Check | Result |
|---|---|
| PDF | `main.pdf` |
| pages | 11 |
| page geometry | A4, 595.276 × 841.890 pt |
| file size | 387,547 bytes |
| PDF version | 1.5 |
| fonts | 24/24 Type 1 fonts embedded and subset |
| raster images | 0 |
| vector figures | 3/3 pure TikZ |

All 11 pages were inspected at rendered-page resolution.  The audit covered
the title and abstract, all three diagrams, the repaired connector lemma, the
operator-pruning argument, the Kraft-clock and marker firewalls, the exact
census table, the Route decision, the bibliography, and both appendices.  No
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
- Bibliography entries cited/present: 19/19, with no orphan or missing key.
- Draft markers (`TODO`, `FIXME`, `TBD`, `PLACEHOLDER`, `??`, `[?]`): 0.
- Route tuple in the PDF:
  `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL,
  A4_FAIL)`.
- Overall verdict: `ROUTE_A_REJECTED`; Route B: `LOCKED`.
- Branch decision: `CLOSE_POSITIVE_RECOGNITION_COMPILER_BRANCH`.

The canonical exact audit was synchronized after integration: 76/76 tests
pass; the repaired connector statement passes 844,544/844,544 constructions
with no true failure; the deliberately preserved preregistration overclaim
has 18,272 exact counterexamples; 85/85 integrity checks and 20/20 scientific
checks pass; and fresh, cold-start, metadata-seal, and idempotence runs are
byte-stable.  The final code/result ledger contains 41 entries.

## Final fingerprints

| Artifact | SHA-256 |
|---|---|
| `main.pdf` | `ff07ac0090822894a94912321b8429cfdc96fc8f5a61fa363ea2845259219642` |
| canonical code/result ledger | `6ffbbee5ce1e2a20f0fb00839b89981293c25a8eca2a0995ed384e7448dc7591` |
| scientific aggregate | `ae0aa6d1767bb207d0096df149224995bfb40aba674367a2f300668bfdd88c02` |
| research lock | `6878be90bd1e213e8a186309abedd1b04b949e3d220b29d01afebc9bce5bb8eb` |
| environment lock | `b2e06f43020927370dab245ad648535f5705d6cd441c8da2b7167ceb024f3329` |
| integrity audit | `178a6c0f565e4076b19f3b5485ce59ffcd860e88622bedcf6ba18074422db61d` |
| Route-A v0.2 YAML | `e089975ac903ecc3da4cc1a510c6153e950a41280f0a6272268f7ae6d1605897` |

## Review boundary

No peer-review or LLM review loop was run, following the explicit project
instruction.  The checks above are deterministic compilation, citation,
artifact, typography, and visual-QA checks only.
