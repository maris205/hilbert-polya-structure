# Final builds and all-page PDF inspection: C409–C413

Status: **FIVE_FINAL_PDFS_VERIFIED**, 59 pages in total.
Actual build/inspection session clock: 2026-09-06 UTC. The client calendar
rolled to 2026-09-07 during this work; the frozen reproducibility epoch was
not changed. This report records the actual coordinator-run final builds,
not the earlier author builds or the later payload-sealing check.

## Final artifacts

Both clean builds of each paper produced the same SHA-256 and passed `cmp`.
The delivered `main.pdf` was copied from pass a and separately compared
byte-for-byte with that output. These are the current PDF hashes; earlier
author/review hashes remain historical snapshots.

| Paper | Pages | Bytes | SHA-256 of both final builds and delivered PDF |
|---|---:|---:|---|
| [C409](papers/C409_wild_fad/main.pdf) | 11 | 326878 | `94d0432495a8a38fbf159b316b462e28c40c7f5b6da65d8ace91d53b6fb5ccf4` |
| [C410](papers/C410_wild_cubic/main.pdf) | 13 | 408234 | `6b0ceb67ed7cb9db9f2a1bc35921f90c3534672efe5dd317262dd53db50c45ba` |
| [C411](papers/C411_two_clock/main.pdf) | 11 | 318511 | `881fa8f8d1a1d8ad71cfc1ecded18d3241a5d23e0ff4b0d3d120d5aabe329638` |
| [C412](papers/C412_integer_henon/main.pdf) | 14 | 367848 | `66788e384cc8016240b17695decac08962f9289fef40a6782eeb108bd3ab699a` |
| [C413](papers/C413_integral_trace/main.pdf) | 10 | 353053 | `60d9b0289b163216db7a217aeb06e8967053b00bc4f75ff7231eb3fa79ade552` |

All are unencrypted, letter-size PDF 1.5 documents. They contain complete
manuscripts and references, not placeholders. No journal or conference has
been selected; the page totals are descriptive, not compliance with a
particular venue's format or page cap.

## Inputs and two genuinely clean build directories

The 50 actual source inputs (45 TeX files and five bibliographies) are fixed
in [FINAL_SOURCE_SHA256SUMS](FINAL_SOURCE_SHA256SUMS), whose SHA-256 is
`3b94393fd4558ca18466a55efe003b08591b59e5645bc315038726300022b51d`.
Each current input was also compared with its copies in both clean build
directories; all 100 source-copy comparisons passed. No source was changed
after these final builds or to make this report.

A fresh container directory was created with `mktemp -d`, giving the actual
root `/tmp/c409-c413-final.InOw0Z`. Each paper then had two previously absent
source/build directories beneath it, named `<paper>/a` and `<paper>/b`.
Only that paper's `main.tex`, `references.bib`, `sections/`, and, where used,
`math_commands.tex` were copied in. No `.aux`, `.bbl`, prior PDF, or author
build cache was used as an input. The temporary paths are execution provenance,
not dependencies of the delivered package; a new reproduction should create
its own fresh directories.

In each of the ten directories the actual command was:

```bash
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Its ordinary console output was retained. All ten invocations exited 0
after Latexmk's necessary reference/BibTeX passes. All five `cmp` comparisons
between the two resulting PDFs exited 0; there was no final-build failure
or typography repair requiring a third final attempt. This does not erase
the earlier author failures that are explicitly retained in their reports.

Environment actually checked:

- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
- Latexmk 4.76 (20 November 2021);
- BibTeX 0.99d;
- Poppler `pdftoppm` 22.02.0;
- local PDF-info display timezone CST +0800; the chosen source epoch is
  2026-09-06 00:00:00 UTC, displayed as 08:00:00 CST where dates are present.

C410's preamble suppresses creation/modification dates and trailer IDs;
the other four retain reproducibly pinned PDF dates. All five byte comparisons
passed with their existing preambles: the coordinator did not add a warning
suppression or change a mathematical source to obtain equality.

## Retained final-run evidence

Each paper's `final_build/` contains the two final TeX logs
(`pass_a.log`, `pass_b.log`), both full console logs, `bibliography.blg`,
`pdfinfo.txt`, `fonts.txt`, and the inspected `pdftotext -layout` extraction
`main.txt`. The console logs include ordinary first-pass unresolved references;
these disappear after reference resolution. The **final** TeX logs and
BibTeX logs, not a selectively truncated console, determine the clean result.

The actual final-log searches found zero matches for `Warning`, `Overfull`,
`Underfull`, `undefined`, `Missing character`, and `multiply defined`, for
both builds of every paper. The extracted final texts had no `??`, `[?]`,
`[VERIFY]`, TODO, TBD or FIXME placeholder matches. The final bibliography
and cross-reference numbering were also visible in the page inspection.

| Paper | Font-object rows | Embedding/type result | Main argument and references |
|---|---:|---|---|
| C409 | 18 | All embedded subset Type 1; no Type 3 | Conclusion and references share p. 11 |
| C410 | 26 | All embedded subset Type 1; no Type 3 | Conclusion p. 12; references p. 13 |
| C411 | 18 | All embedded subset Type 1; no Type 3 | Conclusion and references begin p. 10; references finish p. 11 |
| C412 | 21 | All embedded subset Type 1; no Type 3 | Main argument ends p. 12; Appendix A p. 13–14; references p. 14 |
| C413 | 21 | All embedded subset Type 1; no Type 3 | Conclusion p. 9; references p. 10 |

## Every final page actually viewed

The coordinator rendered each final pass-a PDF with
`pdftoppm -r 100 -png main.pdf page` inside its temporary build directory
and individually displayed **all 59 pages**, in the following complete groups:

- C412: 1–4, 5–9, 10–14;
- C413: 1–5, 6–10;
- C409: 1–4, 5–8, 9–11;
- C411: 1–4, 5–8, 9–11;
- C410: 1–4, 5–9, 10–13.

The inspection found no clipped equation, overlapping text, missing glyph,
unreadable table, wholly blank page, or unresolved reference. In particular,
C412's two classification tables and both appendix certificate tables fit;
C413's orbit tables, all-level zeta and corrected finite-check paragraph fit;
C410's nested powers, class quotients and different/genus formulas fit;
C409/C411's long formulas and reference URLs fit. Ordinary statements and
proofs continuing across pages were retained. The space at the bottom of
C412 p. 12 is the explicit appendix page break, not missing text.

The 17 PNGs retained in author-build locations are earlier author-stage
inspection artifacts, not asserted to be these final renders. The final
temporary render set is not a new scientific figure collection and is not
required to reproduce the manuscript; the pinned PDF determines its pages.

## Closing the review-dependent PDF gates

C409's supported-conductor and citation revisions, C410's three-root
distinctness paragraph, and C413's whole-cycle-in-cube clarification are
present in these final source copies and final PDFs. Their non-author
affected-passage confirmations are linked from
[the review adjudication](REVIEW_ADJUDICATION.md). This closes the requested
stale-PDF rebuild gate, including C413 review item R2. There is no remaining
requested mathematical/source repair from the five manuscript reviews.

No frozen mathematical experiment was rerun for this build check. Existing
author working auxiliaries and cited logs are preserved as historical
evidence; final `main.pdf`, this report and `FINAL_SOURCE_SHA256SUMS` identify
the deliverable, not a timestamp guess. Payload integrity/sealing and Git
synchronization are separate subsequent steps. Successful typesetting and
byte identity do not prove mathematical correctness, worldwide priority,
target Euler factors, root numbers, zero/divisor correspondence or a
Hilbert–Pólya construction.
