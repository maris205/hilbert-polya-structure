# Paper 15 manuscript package

This directory contains the user-authorized Stage-2 research draft of
*Wieferich--Ulm Signatures and the Classification of Compact Arithmetic Packet
Bases*.

## Status and claim boundary

- Article type: theoretical full paper.
- Status: `STAGE_2_5_INTEGRITY_PASS_AWAITING_STAGE_3_CHECKPOINT`.
- The primary-structure and topological-classification theorems are claims of
  the manuscript; the local proof ledger and a fresh semantic re-review found
  no remaining mathematical blocker.
- This package has passed the separate Stage-2.5 claim--citation--source
  integrity gate with zero open issues after one bounded correction round.
  Stage 3 simulated peer review has not started and requires explicit user
  confirmation. External peer review, release, and submission gates remain
  unpassed.
- The paper assigns no Route-A coordinate or overall verdict. Its Route-A
  required-input screen is `NOT_TESTABLE`.
- Route-B advancement is unauthorized and its exact overall status for this
  object is `ROUTE_B_NOT_TESTABLE`.
- The MG11 appendix is nonnormative conformance documentation only; it is not
  theorem evidence or an executed result.

## Retained artifact tuple

| Path | Bytes | SHA-256 |
|---|---:|---|
| `manuscript.tex` | 47,451 | `aff441ee124f0042470dd21270626028b3fca09423a6fdd4beb924c5d5ae195f` |
| `references.bib` | 4,266 | `f4f1ac49a5cd47481d54fe7bc7da7cf14dac2a75b78844d2570eefb5fed06297` |
| `figures/classification_pipeline.tex` | 1,748 | `cc6d75e797c7ca4ad5893864bd74f5b57c364dfcba599f0c5a6749d56c406375` |
| `claim_intent_manifest.json` | 3,658 | `08dcdd66b1ce23718111b063ba3afe3814ea85c365a699e16275d51cf4325a21` |
| `paper.pdf` | 167,484 | `7d30302714e63209766e554e6fa685208789c400e791bb04bf5cf7fe6b2fbfe8` |

This README deliberately does not self-record its own digest.

## Clean build

From this directory:

```sh
build_dir=$(mktemp -d)
latexmk -xelatex -bibtex -jobname=paper \
  -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$build_dir" manuscript.tex
cp "$build_dir/paper.pdf" paper.pdf
```

The retained PDF was rebuilt from the current sources in a fresh temporary
directory using XeLaTeX, BibTeX, and `latexmk`.

## Stage-2.5 rebuild and inspection receipt

- Output: 14 A4 pages, PDF 1.5, 167,484 bytes.
- Extracted text: 6,282 whitespace-delimited words.
- Abstracts: English abstract approximately 182 prose words; Simplified
  Chinese abstract body 329 Han characters, within the 300--500 target.
- LaTeX log: zero warnings or errors, zero overfull/underfull boxes, zero
  missing characters, zero undefined citations/references, and zero duplicate
  labels.
- Citation graph: 10 unique cited keys and 10 bibliography records, with zero
  missing and zero unused keys.
- Fonts: all seven PDF font subsets are embedded and Unicode mapped.
- Ghostscript null-page parse: PASS.
- Visual inspection: pages 1, 11, and 14 were inspected from the final
  Stage-2.5 rebuild at original detail; there is no clipping, overlap, blank
  page, malformed source/owner table, orphaned reference page, or bad URL
  wrapping. The bilingual abstract crosses the page-1/page-2 boundary cleanly.
- Manifest: `claim_intent_manifest.json` parses as valid JSON and remains the
  one-shot pre-composition record.
- Only source assets and the retained PDF are stored here; auxiliary build
  files remain outside the workspace.

The integrity report and machine handoffs are retained in
[`../notes/stage2_5_integrity_report_v1.md`](../notes/stage2_5_integrity_report_v1.md),
[`../notes/stage2_5_integrity_report_v1.json`](../notes/stage2_5_integrity_report_v1.json),
and [`../notes/stage2_5_material_passport_v1.json`](../notes/stage2_5_material_passport_v1.json).

## Roadmap interpretation

The manuscript follows the exact vocabulary of the repository evaluators:

- [`../../../skills/route-a-evaluator.md`](../../../skills/route-a-evaluator.md)
  uses `NOT_TESTABLE` for a missing-input screen, but does not define an overall
  `ROUTE_A_NOT_TESTABLE` verdict. The manuscript therefore assigns neither an
  A0--A4 tuple nor an overall Route-A status.
- [`../../../skills/route-b-evaluator.md`](../../../skills/route-b-evaluator.md)
  defines `ROUTE_B_NOT_TESTABLE`. That is the exact status used because the
  paper has no common-object Hilbert-space/operator/trace/determinant chain.

These local protocol labels are governance metadata, not scientific claims.

## Remaining pre-submission work

1. Obtain explicit user confirmation to enter Stage 3 simulated peer review.
2. Conduct the manuscript-level peer review and resolve any report.
3. Confirm funding wording, author contributions, conflicts, acknowledgments,
   repository coordinates, license, venue format, and final AI disclosure.
4. Rebuild and run a release audit before any public synchronization or
   submission.

No publication, runtime execution, Route advancement, or release authority is
claimed by this package. Stage-2.5 PASS is an integrity result, not an external
peer-review or release verdict.
