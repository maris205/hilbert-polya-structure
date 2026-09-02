# Build and review-artifact record — P158

**Date:** 2026-09-02 UTC.  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Toolchain and settled command

- Engine: pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Bibliography: BibTeX 0.99d with `plainnat`.
- Class: anonymous `amsart`, 10 pt, A4, 27 mm margins.
- Settled sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Round‑0 artifact

| Check | Value |
|---|---|
| Immutable author freeze | `main_round0_original.pdf` |
| Pages / format | 4 / A4 |
| Size | 352,360 bytes |
| PDF SHA-256 | `bbe961298aa62adc54d34f15cc546ff3f14d7d4d29fd90dee2dcc6e2fff2e892` |
| Freeze integrity | preserved unchanged after Review A |
| References | 3/3 cited and resolved |
| Encryption / forms / JavaScript | none / none / none |
| Identifying metadata | title, author, subject, and keywords blank |

All 27 font rows reported by `pdffonts` are embedded, subsetted, and Unicode
mapped.  The settled `main.log` and `main.blg` contain zero unresolved
citation/reference, rerun request, build error, BibTeX warning, overfull box,
underfull box, or multiply defined label.  The pdfTeX console emits one benign
font-expansion ordering notice when the monospaced hash font is first used;
it does not affect layout, references, reproducibility, or PDF validity.

## Deterministic source-only reproduction

Two independent temporary directories were populated only with `main.tex`
and `references.bib`.  Each ran the four-command sequence above.  Both PDFs
were 4 pages and 352,360 bytes and were byte-identical to each other, to
`main.pdf`, and to `main_round0_original.pdf`, all at the recorded SHA-256.

## Exact control

- Frozen assertions: 35,278, all exact integer checks.
- Fresh stdout matched `verification_output.txt` byte for byte.
- Transcript SHA-256:
  `728c32e557e920c46022f3fe8d24fce1e5e303a3d43d823b6d22ae20d7a85fe8`.
- The every-target lane includes all zero fibres and the mandatory
  `n=5,t=2`, `r=R=2,z=1` nonimage.
- No bytecode cache was generated during the frozen replay.

Enumeration is finite counterexample pressure, not proof, source ownership,
novelty, priority, or clearance.

## Visual and round boundary

All four pages were rasterized at 120 dpi and inspected.  No clipping,
overlap, broken equation, unresolved marker, malformed glyph, or illegible
reference was found.  The theorem domain explicitly limits the displayed
fibre formula to `r<=R`; targets with `r>R` are separately assigned fibre
zero.  The `r=R,z>0` condition and two-edges-plus-isolate counterexample are
visible beside the theorem.

No hostile review, improvement log, Round‑1 PDF, Round‑2 PDF, or external
action is part of this author freeze.

## Review-A repair and Round-1 artifact

Review A found zero Critical, zero Major, and two Minor items.  The boundary
display's comma was replaced by a multiplication space.  The verifier gained
an independent literal successive-cut lane, adding 42,252 assertions; the
new total is 77,530 and the transcript SHA-256 is
`3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d`.
Microtype expansion was disabled while protrusion was retained, eliminating
the disclosed font-expansion notice.

| Check | Value |
|---|---|
| Current / Round-1 PDFs | `main.pdf` / `main_round1.pdf` |
| Pages / format | 4 / A4 |
| Size | 371,703 bytes |
| PDF SHA-256 | `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5` |
| Current versus Round 1 | byte-identical |
| Current versus Round 0 | intentionally different; Round 0 preserved |
| References | 3/3 cited and resolved |

The retained Round-1 logs are `build_round1_pdflatex_1.log`,
`build_round1_bibtex.log`, `build_round1_pdflatex_2.log`, and
`build_round1_pdflatex_3.log`.  The settled log has zero selected warning,
bad-box, undefined-reference, or rerun lines.  All 28 font rows are embedded,
subsetted, and Unicode mapped; all four pages passed raster inspection.

## Review-B acceptance and Round-2 freeze

Review B returned zero Critical, zero Major, and zero Minor findings.  Its two
source-only builds and two verifier replays matched the Round-1 package
exactly.  No further source repair was necessary.  `main.pdf`,
`main_round1.pdf`, and `main_round2.pdf` are byte-identical at 371,703 bytes
with SHA-256
`2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5`.
The Round-0 pre-review freeze remains distinct and unchanged.
