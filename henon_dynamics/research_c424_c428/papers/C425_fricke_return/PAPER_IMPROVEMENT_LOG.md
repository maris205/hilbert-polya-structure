# C425 manuscript improvement log

2026-09-09 UTC. Current status: **two manuscript rounds adjudicated;
final build gate passed; AUTHOR STOP-WRITE; pending coordinator seal**.
The coordinator adopted the sole P1 finding from the actual first
nonauthor manuscript review. This log records the resulting author
revision, not an author-issued manuscript acceptance or formal evaluation.

## Review and revision progression

| Stage | Actual result | Author action |
| --- | --- | --- |
| Original first draft | Stable 12-page baseline; no author-assigned score | Preserved as `baseline.pdf`, `main_round0_original.pdf` and `baseline_source/` |
| Nonauthor round 1 | 0 mathematical and 0 source/evidence must-fixes; one minor P1 correction | Coordinator adopted P1; precise abstract containment wording implemented |
| Author revision 1 | One successful fresh-directory build, 12 pages; complete PDF inspection | Frozen for the assigned nonauthor second pass |
| Nonauthor round 2 | PASS; P1 closed; 0 mathematical/source must-fixes and 0 new minor findings | Coordinator explicitly adopted the full report; no further source changes |
| Author round 2 | No-change round | `main_round2.pdf` is an explicitly labelled byte-identical alias of `main_round1.pdf`, not a fabricated revised build |

The batch's assigned current-team nonauthor review supersedes the
improvement skill's external-model/ML-venue defaults. No external GPT
thread, human external review, fabricated numerical score, mathematical
execution or additional experiment is represented here.

## Full raw round-1 review

The complete, unedited first manuscript review is preserved in
[ROUND1_REVIEW_RAW.md](ROUND1_REVIEW_RAW.md), copied byte-for-byte from
[the assigned review](../../manuscript_reviews/round1/C425_REVIEW.md).
Its SHA-256 is
`e7e8a2cf840d37d52dc1dad9120342d60e711684a627e64dad6f8a61e5adb81e`.
The full review file, not an excerpt or this summary, is the raw record.

## P1 resolution and complete source-diff boundary

P1 observes that identifying a finite periodic orbit with a whole
infinite line is imprecise, and also suggests containment in one line
although the proved orbit may pass between different lines.

The exact replacement in `sections/00_abstract.tex` is:

> maps then place every large periodic orbit in a finite union of whole
> periodic lines.

This matches Theorem 1.1, Proposition 5.3 and the explicit explanation
immediately after that proposition. No theorem, proof, bound, citation,
period label, execution claim or source-ownership statement was changed.

All thirteen reproducibility inputs were individually compared against
the preserved original source: `main.tex`, `math_commands.tex`,
`references.bib`, `build.sh` and all nine active section files. Exactly
the two-line abstract substitution differs; the other twelve files are
byte-identical. [ROUND1_SOURCE_DIFF.patch](ROUND1_SOURCE_DIFF.patch)
contains the complete content diff (timestamp fields omitted).
[ROUND1_INPUT_MANIFEST.sha256](ROUND1_INPUT_MANIFEST.sha256) records all
thirteen current input hashes. The actual revised build's source copies
are retained in `build_round1_01/source_snapshot/`.

The `auto-paper-improvement-loop` skill guided baseline preservation,
full review retention, minimal adopted-finding correction and an honest
pending-second-review state. The `paper-compile` skill guided the real
build, log/font/text and every-page visual checks. The ARS abstract
claims-consistency guidance was applied only to match this sentence to
the existing theorem; it did not launch a full paper-generation pipeline
or change the research scope.

## Actual revision build and PDF checks

Command: `bash build.sh build_round1_01`; actual terminal exit code 0.
The unique directory was newly created; no old build was cleaned or
overwritten. The saved `compile.log` includes the normal unresolved
references/citations from early passes of the fresh build. They are
resolved in the final engine log. Do not count early-pass messages as
remaining warnings, or the internal LaTeX passes as separate reviews.

Current output: `main.pdf`, `main_round1.pdf` and
`build_round1_01/main.pdf`, all byte-identical: 12 pages, 378223 bytes,
SHA-256 `e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb`.

The final `main.log` and `main.blg` have zero warning/error,
undefined-reference/citation or over/underfull-box matches. All 23
reported Type 1 font resources are embedded. Metadata remains anonymous,
with no creation/modification dates, and the PDF is not encrypted.
The full 614 lines of `build_round1_01/pdf_text.txt` were read. Each
of the twelve 1400-pixel page renderings in `build_round1_01/pdf_pages/`
was separately viewed; this includes every table, proof continuation,
the finite output procedure, level formulas and all six bibliography
entries. The new abstract sentence is visible and correct. No clipping,
collision, missing glyph or unresolved cross-reference was observed.
Pages 1–11 contain the article; page 12 contains references. No venue
page-limit compliance certification is claimed because no target venue
was assigned.

The original `baseline.pdf`, `main_round0_original.pdf` and
`build_initial_04/main.pdf` retain SHA-256
`aa6c4ee4bbc6f55bcf2934caccc927bf36aef872bf230466541c0f3de7b2f207`.
`DRAFT_HANDOFF.md` and `BUILD_REPORT.md` are unchanged historical
first-draft records; their current-PDF phrases refer to that earlier
handoff, not this revision. This log and `ROUND1_HANDOFF.md` are the
current revision receipts. All original failed/intermediate build
evidence remains preserved.

## Historical round-1 handoff boundary

The author has completed the sole adopted first-round fix and has
stopped writing. The assigned second nonauthor review, its coordinator
adjudication, any newly authorized correction, the final fresh identical-
input build gate, formal evaluation and release remain separate and
pending. No mathematical program or old certificate was run. No file
outside this C425 paper directory and no Git state was changed by this
author revision.

## Round-2 adjudication and no-change closure

The coordinator explicitly adopted the second actual nonauthor review
on 2026-09-09 UTC: **PASS, P1 closed, zero new findings, zero requested
manuscript changes**. The author freshly read all 203 lines of this
report and the complete first-round report before closure. The complete
second report is preserved byte-for-byte in
[ROUND2_REVIEW_RAW.md](ROUND2_REVIEW_RAW.md), identical by actual `cmp`
to [the assigned report](../../manuscript_reviews/round2/C425_REVIEW.md).
Its SHA-256 is
`c5f8224db870115d6e11e0ebbaba341c176c09717510f70b7349eeb583d8d202`.

This closes both scheduled internal manuscript-review rounds, with one
minor correction in round 1 and no correction in round 2. No additional
review, external-model thread, numerical score, mathematical execution
or artificial second revision is claimed. `main_round2.pdf` was copied
from and actually byte-compared with `main_round1.pdf`; both retain
SHA-256 `e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb`.
All thirteen active inputs still pass `ROUND1_INPUT_MANIFEST.sha256`.

The coordinator separately authorized exactly two fresh final builds
using those unchanged inputs. A read-only startup check found neither
final-build directory, final report nor round-2 alias, and no live C425
build process; the earlier authorization had not actually been executed.
The output directories are `build_final_01/` and `build_final_02/`.
Both real commands completed with exit 0; no further final build was
attempted. Their completion and final quality evidence are recorded in
[FINAL_BUILD_REPORT.md](FINAL_BUILD_REPORT.md): the 13 identical inputs,
two 12-page 378223-byte PDFs equal to the reviewed version, clean final
logs, 23 embedded Type 1 resources, complete 614-line text reread and
all 12 freshly rendered final pages individually viewed. The final
input manifest equals `ROUND1_INPUT_MANIFEST.sha256`; no round-2 or
finalization source changes occurred.

The author now stops writing. Sealing, formal-evaluation disposition,
shared batch records and Git remain coordinator-owned, not certified
by this author receipt. The local handoff is **pending coordinator seal**.
