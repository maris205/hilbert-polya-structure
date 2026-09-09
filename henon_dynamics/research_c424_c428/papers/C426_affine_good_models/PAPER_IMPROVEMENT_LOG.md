# C426 manuscript improvement log

Status: `manuscript_reviews_complete_pending_final_release`. 2026-09-09 UTC.

This log records actual nonauthor manuscript review and actual source
revisions. The earlier GR5 proof-admission and outline reviews are
not manuscript rounds. No external reviewer service, invented score,
human peer-review claim or mathematical execution is involved.

## Round 1: actual review and coordinator decision

The coordinator, who is not the C426 manuscript or GR5 proof author,
read the complete actual source/PDF and evidence, viewed all ten pages,
and performed the bounded primary-source checks stated in the full
report. The untouched complete report is preserved at
`reviews/round1/REVIEW.md` (SHA-256
`e1be3cd670d5a5cc8536020c0b3352c133a3e4faa91fc0d9bea4b0b5eb07511c`),
a byte copy of the batch's `manuscript_reviews/round1/C426_REVIEW.md`.
Its verdict is zero critical/major mathematical or source/evidence
defects and three minor presentation corrections, all adopted by the
coordinator. No numerical journal score was assigned.

| Review ID | Adopted change | Verification |
| --- | --- | --- |
| P1 | Abstract: `uses no mathematical computation` became `requires no computer-assisted certificate`. | Revised PDF text contains the precise certificate distinction; explicit hand calculations remain. |
| P2 | Introduction: the split `arbitrary-class-` / `group` was replaced by `statement for arbitrary class groups`. | Revised PDF has ordinary spaces and no spurious hyphen-space. |
| P3 | GR5 bibliography description retains `8 September`; `year={2026}` supplies the year once. | Reference [3] now has `8 September, 2026`; unpublished AI-assisted/internal and source link remain. |

The exact three-file diff is `reviews/round1/source_changes.diff`.
The full baseline source was extracted, without modifying its archive,
to `builds/round1_revised/baseline_source/`. All seven other editable
TeX inputs were byte-compared unchanged; no theorem, proof, scope,
table or mathematical-execution count changed.

## Round 1: actual revised build

One fresh local latexmk invocation in `builds/round1_revised/` ran
three pdfLaTeX and two BibTeX passes, exit 0. Fixed settings were the
same as the initial ledger. The final log has no warnings, over/underfull
boxes or unresolved items. `pdfinfo` reports 10 pages, 343725 bytes,
empty author and no dates. All 20 fonts are embedded Type 1 resources.
Real PDF text was inspected for all three requested changes, and all
ten rendered revised pages were actually viewed without clipping or
overlap. Transcript, engine log, extracted text and page PNGs persist.

The first attempted copy of the review used an incorrect relative
path and returned `cannot stat`; the corrected in-batch path succeeded
immediately, and its SHA-256 was checked. This harmless file-copy
error was not a compile failure or a mathematical execution. No
latexmk invocation failed, and no prior certificate was rerun.

Baseline PDF `main_round0_original.pdf` SHA-256:
`85677da439f31f1c2faea804430c8f395a2aaa235a0d20696e0a97a8ca08ed38`.
Revised PDF `main_round1.pdf` and current `main.pdf` SHA-256:
`d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db`.
The original source archive and all initial builds remain intact.
`builds/round1_revised/source.tar` preserves the actual revised source,
audit, ledger, README, full review, diff, improvement log and state.

## Round 2 and final release

The coordinator completed and read back the second actual nonauthor
pass at `../../manuscript_reviews/round2/C426_REVIEW.md`, SHA-256
`30db2f60462771ff47a3347ce0a02755e9fcd7d2d11c68f7287d681475afa605`.
P1/P2/P3 are closed, with zero must-fix or new optional findings.
The complete revised PDF text and all ten pages were freshly inspected;
all ten source/archive members and the exact three-hunk diff were checked.
Theorem quantifiers, wild/quadratic centres, CRT support and principal-square
sufficiency received a new regression check. No further source edit was
needed. `main_round2.pdf` is a no-change byte alias, not a new build.
Formal evaluation and the two fresh deterministic final builds remain open;
the revision build is not either final build. The local
`auto-paper-improvement-loop` skill supplied the preserve/revise/build/
log workflow; the batch plan replaces its external-model, ML score,
venue-cap and notification defaults.
