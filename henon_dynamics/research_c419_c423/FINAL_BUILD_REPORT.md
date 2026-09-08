# C419–C423 final manuscript production gate

2026-09-08 UTC. **Five actual final PDFs, 67 pages total; all five fresh
same-input build pairs compare byte-for-byte equal. Every final page was
actually inspected.** This report closes manuscript production, not the
later exact-member seal or Git synchronization.

## Final artifacts

| Article | Pages | PDF bytes | Exact successful pair | Complete receipt |
| --- | --- | --- | --- | --- |
| [C419](papers/C419_positive_trace_words/main.pdf) | 11 | 346075 | builds/final1 and builds/final2 | [C419 report](papers/C419_positive_trace_words/FINAL_BUILD_REPORT.md) |
| [C420](papers/C420_scattering_commutativity/main.pdf) | 18 | 428401 | builds/final1 and builds/final2 | [C420 report](papers/C420_scattering_commutativity/FINAL_BUILD_REPORT.md) |
| [C421](papers/C421_integral_return/main.pdf) | 18 | 473595 | build_final_stable1 and build_final_stable2 | [C421 report](papers/C421_integral_return/FINAL_BUILD_REPORT.md) |
| [C422](papers/C422_painleve_bound/main.pdf) | 14 | 352289 | build_final1 and build_final2 | [C422 report](papers/C422_painleve_bound/FINAL_BUILD_REPORT.md) |
| [C423](papers/C423_two_cycle_preperiodicity/main.pdf) | 6 | 317347 | builds/final1 and builds/final2 | [C423 report](papers/C423_two_cycle_preperiodicity/FINAL_BUILD_REPORT.md) |

All paths in the pair column are relative to that paper directory. C420's
builds directory is a sibling of paper/, not inside it. Root main.pdf
entries have the following SHA256 values, independently measured by the
coordinator after all five handoffs:

```text
C419 8089cac2f3826f5813a7153038d217ff744af3a159ec4d288dd098f411ef2723
C420 9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512
C421 13fece76ec21d56eacbdcb43303f3acef017e9f9b7f1e0e228f5438cd6761d0c
C422 83691c4b0f36d28373642ed8a6a1c290db29333986de601aaf914b08120c3079
C423 03ab70bcbcac190c9592c55337dba2d6a124fb8574039ff00e5f5b23ec86f9bb
```

The five final entry PDFs total 1,917,707 bytes. This sum excludes preserved
duplicates, old PDFs and all other payload; it is not a batch-ledger total.

## Actual build history and unchanged reviewed content

Both final builds per paper used new directories without inherited auxiliary
files, the installed latexmk 4.76/pdfTeX 1.40.22/TeX Live 2022-dev toolchain,
and SOURCE_DATE_EPOCH=1788825600, FORCE_SOURCE_DATE=1, TZ=UTC, LC_ALL=C.
Each successful build converged with three pdfLaTeX and two BibTeX passes.
No production TeX/Bib input changed after the accepted second reviews.

C421 first compiled a fresh pair successfully but its exact PDF comparison
failed solely because of the automatic trailer ID. Those two outputs and
logs are preserved. After an explicitly approved build-only ID omission,
two additional fresh directories produced its final equal pair. Thus there
were **12 actual final-stage builds, including two compile-successful but
comparison-failing initial C421 outputs**, not an invented clean ten-build
history. Other papers had no failed final pair. C420 already suppressed
dates/ID in its reviewed source; the other final commands suppress only the
volatile ID through a compiler option, with no reviewed-source change.

C420's final PDF is exactly its reviewed PDF. For C419/C421/C422/C423,
read-only comparison proves that the only difference from the reviewed PDF
is omission of 75 trailer-ID characters, retaining the newline. No PDF was
edited by that diagnostic and no layout/content stream was changed. All
five bibliography outputs and same-option text comparisons pass.

## Coordinator adjudication and final checks

The coordinator read all five complete final reports, including C420's
282-line report, C421's 214-line report and C422's 179-line report, and
accepts their recorded commands, failures, fixes and scope. The coordinator
also independently compared every final alias to its successful first
build, compared all five successful PDF pairs, and checked the recorded
TeX/Bib manifests from their correct individual paper working directories:
14+13+17+17+10 = **71 recorded input entries, all OK**, every command exit 0.
The first C420 manifest invocation was mistakenly run from the batch root,
so its paper/-relative paths could not resolve; the correctly located
read-only check passed all 13. This was not a source or build failure.

Every final engine/BibTeX log is free of actual errors, unresolved
citations/references, rerun requests and overfull/underfull boxes. Early
convergence warnings remain in console logs. Fonts are embedded Type 1
with Unicode mappings (19/27/24/19/20 entries respectively); no Type 3 or
unembedded-font claim is hidden by successful compilation.

All 67 distinct final pages were newly rendered and actually opened:
the coordinator viewed all C419 and C423 pages; the recurrence-lane agent
viewed all C421 and C422 pages; the characteristic-p agent viewed all C420
pages, also opening the second byte-identical C420 copy. The latter duplicate
18 views do not increase the distinct final-page count. The per-paper
receipts identify what was inspected. No clipping, overlap, missing glyph,
unresolved marker or omitted proof was found. C420's sparse bibliography
page and C422's theorem-preserving whitespace are accepted layout choices.

The sources are anonymous English mathematical articles, not a claimed
named-venue template. Proof length, tables and the C421 code appendix follow
the complete arguments, with no artificial page quota or fabricated plot.
The actual two manuscript-review passes are adjudicated in
[REVIEW_ADJUDICATION.md](REVIEW_ADJUDICATION.md). Review, production and
byte integrity are distinct from human peer review or worldwide priority.

All original versions and disclosed failures remain available. No old
mathematical program was rerun during final production. The C421 proof
certificates remain historical exact evidence, not new final-build tests.
The paper-compile and batch skills supplied convergence/diagnostic checks,
deterministic fresh pairs and all-page verification. After these gates
passed, no further build was requested without changed inputs or a concrete
failure. Exact payload sealing and synchronization have separate receipts.
