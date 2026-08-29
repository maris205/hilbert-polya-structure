# Final QA report — Papers 107–111

Checkpoint: 2026-08-29 UTC

Result: **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | exact control | independent gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P107 | 4 | 271,211 | 212,843 | `GO_INTERNAL` | 23/23 | 4/4 |
| P108 | 3 | 269,786 | 67,475,970 | `GO_INTERNAL` | 21/21 | 3/3 |
| P109 | 5 | 302,089 | 515,379 | `GO_INTERNAL` | 22/22 | 5/5 |
| P110 | 5 | 321,838 | 1,916,206 | `GO_INTERNAL` | 25/25 | 5/5 |
| P111 | 7 | 316,032 | 421,285 | `GO_INTERNAL` | 21/21 | 7/7 |
| **total** | **24** | **1,480,956** | **70,541,683** | **5/5** | **112/112** | **24/24** |

The assertion total is heterogeneous finite-control evidence, not an
independent proof count or quality score.

## Control and build replay

After hostile-review repairs, each canonical verifier was run from its final
paper tree and its stdout compared byte for byte with the stored result.  All
five comparisons passed.  The frozen counts are 212,843; 67,475,970;
515,379; 1,916,206; and 421,285 assertions.

Every manuscript was built in the order
`pdflatex -> bibtex -> pdflatex -> pdflatex`; all 20 required stages exited
zero.  Deterministic rebuild checks reproduced each final PDF SHA-256.  The
final `main.log` and `main.blg` scans found zero emitted LaTeX/package
warnings, undefined citations/references/control sequences, multiply-defined
labels, overfull/underfull boxes, fatal errors, emergency stops, or actionable
rerun requests.

## Bibliography and PDF gates

The bibliography audit found **26 paper-local entries**, all 26 cited and
resolved, with zero missing citation key and zero uncited entry.  The per-
paper closures are 5/5, 4/4, 7/7, 4/4, and 6/6.

For every artifact, `pdfinfo` reports A4, PDF 1.5, rotation zero, no
encryption, no JavaScript, no form, and an empty Author metadata field.  All
112 font records are embedded, subsetted, and Unicode-mapped.  The PDFs have
**86,944 bytes** of nonempty searchable layout text in 1,298 lines.  Exact
scans found no unresolved-reference marker, placeholder token, or stray
literal `qquad`.

## Visual gate

All 24 final pages were rendered at 120 or 150 dpi and inspected page by
page.  Titles, abstracts, theorem statements, boxed formulas, proof endings,
owner/collision boundaries, conclusions, and all references are legible.
No page is clipped, overlapped, accidentally blank, malformed, or missing
content.  Short reference endings leave only benign lower-page white space.

## Integrity gate

The five paper-local manifests cover **68 evidence files** and pass
`sha256sum -c` entry by entry.  The five canonical PDF digests are frozen in
[`CANONICAL_PDF_MANIFEST.sha256`](CANONICAL_PDF_MANIFEST.sha256), which also
passes in full.

This report certifies internal consistency, reproducibility, and final
artifact mechanics only.  It does not grant novelty, priority, authorship,
venue fit, public release, submission, or specialist contact clearance;
those actions remain **HOLD**.
