# Build and QA record — P148

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**

## Historical artifacts

- Engine: pdfTeX 1.40.22 / LaTeX2e, BibTeX 0.99d.
- Build sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- `main_round0_original.pdf`: pre-review baseline, 4 A4 pages, 351,696
  bytes, SHA-256
  `b32439d6be070d10bd54ff05a60b9920db176dcaf81c6a6a96fc939dd8db88d2`.
- The pre-hostile then-current build was 4 pages and 352,411 bytes, SHA-256
  `ac3aea38bc4ed0580a37cfef9f02fa91699d91b1f8a23e3e1f6cf1baa1f2c8f0`.

## Accepted round-2 artifact

- `main.pdf`: 5 A4 pages, 357,397 bytes.
- `main_round1.pdf`: byte-identical retained copy of the accepted artifact.
- SHA-256 of both files:
  `5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957`.
- Bibliography: 5/5 cited primary entries resolve.
- Settled log: no unresolved citation/reference, rerun request, build error,
  overfull box, or underfull box.
- Fonts: all embedded and subsetted.
- Metadata: anonymous presentation; blank title/author metadata; PDF 1.5 and
  unencrypted.
- Text extraction prints `Christian Höner zu Siederdissen` correctly.
- Visual inspection: 5/5 pages accepted with no clipping, overlap, malformed
  formula, or broken bibliography entry.

## Exact control

- Canonical replay is byte-identical to `verification_output.txt`.
- Assertions: 216,905.
- Coverage: all 23,714 plane trees through 11 vertices; labelled iterate
  skeletons, pointwise clocks, every target/source-size fibre, local factor
  coefficients, exact image sets, and algebraic image coefficients.
- Finite enumeration is counterexample pressure, not proof or novelty
  evidence.

## Reproducibility

- Two consecutive deterministic builds are byte-identical.
- A clean isolated directory containing only `main.tex` and
  `references.bib`, built by the frozen sequence, produces a PDF
  byte-identical to current `main.pdf` at the accepted SHA-256 above.
- Volatile PDF dates and trailer IDs are suppressed.

## Review and repair history

Hostile Review A returned **1 Critical / 0 Major / 2 Minor**.  It identified
the omitted direct outward-contraction owner, compressed exposition of the
recursive global inverse, and the Höner/year bibliography defect.  The
repair build:

- states `For(E(T)) ≅ OutContr(For(T),root(T))` and cites
  Soo--Khoussainov--Linz Definition 6.6;
- assigns the direct-owned unordered rule and bare height compression zero
  credit;
- exposes `F_U=A_d product_j F_{U_j}` and its reversible bijection; and
- corrects Höner spelling and the version-of-record year 2021.

The owner gate was reopened.  Independent Hostile Review B then rederived
the equivalence, proofs, boundary cases, and strict credit boundary; cold-ran
the verifier; performed the isolated build; and inspected all five pages.
It returned **0 Critical / 0 Major / 0 Minor, ACCEPT**.

Round-2 closure applies a still stricter scoring boundary: the unordered
one-step rule and all cheap unordered all-rank depth/clock consequences
receive zero contribution credit.  The sole residual conjunction is

```text
ordered every-target size-refined inverse
+ exact-layer image criterion
+ algebraic image series.
```

`PROOF_PACKAGE.md` remains **PROVABLE AS STATED**.  Review acceptance does not
authorize novelty, priority, submission, posting, specialist contact,
external release, or Git action.  Status remains `HOLD_EXTERNAL`.
