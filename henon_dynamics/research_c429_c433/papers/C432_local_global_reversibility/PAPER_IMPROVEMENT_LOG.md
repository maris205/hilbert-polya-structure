# C432 manuscript review and preservation log

Latest lifecycle checkpoint observed: 2026-09-09 21:30:04 UTC.
Current status: **review_loop_completed_pending_final_build_and_release**.
Review-loop status: **completed**; both actual same-thread nonauthor
manuscript passes were accepted with no required author changes.

## Historical round 1 checkpoint

Checkpoint observed: 2026-09-09 21:12:35 UTC.
Status: **round1_accepted_pending_second_review**.

## Round 1 disposition

The coordinator has read and accepted the actual first manuscript review
and the separate citation audit. Both report zero required author changes.
The author has now read both complete raw reports and checked their actual
hashes. No source, bibliography, table, PDF, baseline, or build input was
edited in response to this pass. No changed manuscript or improvement in
quality is inferred merely from completing the review.

Exactly **one actual nonauthor manuscript pass** is complete. The citation
audit is a separate source check, not the second manuscript pass. The
coordinator will activate the required second actual manuscript pass in
the same reviewer thread; two distinct reviewers are not required by this
workflow. No second-pass outcome is claimed here.

## Full raw reports, retained unchanged

These links point to the complete original reports, not summaries or
replacement author responses. Their existing files are frozen and must
not be appended to or overwritten. Any later report belongs at a new path.

| Record | Actual extent | SHA256 |
| --- | --- | --- |
| [Round 1 manuscript review](reviews/round1/REVIEW.md) | 347 lines; zero required repairs | `5d1b198e0828571f57991abb8b2d74e008c5eb3dbc916ae212964d340f520c45` |
| [Separate citation audit](reviews/citations/REPORT.md) | 258 lines; zero citation must-fixes | `80b1dbf06d648de9c4ae51590a707d1dcf81e79c60b602eb246a27400cb25223` |

The citation audit's limitations remain in force: live retraction/Crossmark
verification is incomplete; the two IOP landing pages were inaccessible;
published Song Wang full text was not obtained; and the ARS structural PDF
preflight was unavailable because pypdf is absent. These are not converted
into verified clean-status or structural-PASS claims. The audit's actual
primary-source accesses are its reviewer's work, not new author accesses
performed during this bookkeeping task.

## Actual round artifacts

The pre-review [baseline](baseline/) remains untouched. At this checkpoint
the following new archives were made from its actual bytes:

- [main_round0_original.pdf](main_round0_original.pdf) is an exact copy of
  baseline/main.pdf. This filename was created now, from the preserved
  original baseline; it is not assigned an invented earlier creation event.
- [main_round1.pdf](main_round1.pdf) is another exact copy of that same PDF.
  It records acceptance without an author change, not a revised build.
- [Round 1 source snapshot](snapshots/round1/source/) contains the actual
  unchanged main source, bibliography, seven sections, sole table,
  PAPER_PLAN.md, and SOURCES.md. It contains ten compilation inputs and
  two supporting records, not a new mathematical or editorial version.

All five PDFs below were compared byte for byte and share SHA256
`d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa`:

- [Current PDF](main.pdf).
- [Frozen baseline PDF](baseline/main.pdf).
- [First author build PDF](build/attempt_01/main.pdf).
- [Preserved original PDF](main_round0_original.pdf).
- [Round 1 PDF](main_round1.pdf).

Each remains the original eight-page, 341,782-byte article. The source
paths in the following table have identical bytes at the current paper
root, under baseline/, and under snapshots/round1/source/. Direct file
comparisons and recursive section/table comparisons found no differences.

| Relative source/support path | Actual SHA256 in all three locations |
| --- | --- |
| main.tex | `e83ee44b45b9a4be1e98a150ec05514a3f47fcbc3f87342da90cfed55d3201c8` |
| references.bib | `a4ce6daf2a069c51bece1a08c45ad8f241c8cfca74b20fede1d6e5cac8b564b7` |
| sections/00_abstract.tex | `ef3ccceef4dedb08c052bf56563f6976100ac9d38b8a87419c71c543760d3ed8` |
| sections/01_introduction.tex | `68852fd93b21c6c7322bd9230170db19f142281d3d7d6dd4c5419d51b80dafc9` |
| sections/02_axis.tex | `f49282b52048a15046c3bb2be8644f252ef77e8f6e0df3b48f6e5eac41acecb0` |
| sections/03_centralizer.tex | `a5eb22a9144d4893e896aae6f222e917d5f337a2315a5d7b8f2a4af99f0fad56` |
| sections/04_descent.tex | `15e6b2f06402a64c62e4c2bb7cd787b47f4acb4a80cb26f4c92a9a85da1cb930` |
| sections/05_places.tex | `da4035fc48b59bad0e1a4f64f9c79bab2f05400f5e85496449f15c800eaf7ed7` |
| sections/06_control.tex | `7bc226b0cfab97680f02b82e5e26efa648ce1d2ee3f4c4ae98e2fa3b2beca21f` |
| figures/TABLE_local_places.tex | `102a0dac97aff1519c20e53122b731543ff0380f9a9ffa7568a42c33a1bcc7fb` |
| PAPER_PLAN.md | `30f3364801b0b7dbab2bd56c94eb45b7d93f62e45558452332011246618856ae` |
| SOURCES.md | `04813dc535c7d6fc4d10140f7bd5f3a4483db05dbd240c2609422239128ef5d1` |

## No unnecessary build or fictional revision

There was **no compilation in this round-1 bookkeeping task**: no
compilation input changed and the accepted first-build PDF is retained.
The only completed author build remains the actual latexmk invocation
recorded in [BUILD_RECORD.md](BUILD_RECORD.md), with raw outputs at
[build/attempt_01/](build/attempt_01/). Its preliminary internal TeX passes
are not counted as new review rounds or final reproducibility builds.
BUILD_RECORD.md remains the unchanged historical first-draft receipt,
SHA256 `343d6c01c11989d514c0bb760aca7dfbc840afc3418dc66bc0a8acfb0ee1f0dc`;
its then-pending reviews are not retroactively rewritten.

The auto-paper-improvement-loop skill supplied version preservation and
complete-review retention. The explicit current assignment governs this
no-change disposition, PAPER_IMPROVEMENT_STATE.json filename, linked immutable raw reports,
current-team review, and absence of a redundant rebuild. Its legacy
external-model, scoring, ML-venue, and notification examples are not
executed. No new reviewer was activated by the author.

## Freeze and next gate

The baseline, current manuscript inputs/PDF, two raw reports, round-0 and
round-1 PDFs, and round-1 source snapshot are frozen for the next review.
This log and [PAPER_IMPROVEMENT_STATE.json](PAPER_IMPROVEMENT_STATE.json) record this actual checkpoint; only
a separately authorized later lifecycle task may extend their state.
All links are relative to this paper's real hilbert-polya-structure tree.

The second actual nonauthor manuscript pass and the separate two clean
deterministic final builds remain pending. No final release, publication,
peer-review acceptance, formal evaluation, or completed-paper status is
claimed. Only the new archive copies, this log, and PAPER_IMPROVEMENT_STATE.json were written
in the allocated paper tree. No existing author file, raw review, baseline,
build output, shared index, old proof, evaluator, Git object, release seal,
or other stream was changed. No mathematical program or external-model
operation was performed.

## Round 2 lifecycle checkpoint

Checkpoint observed: 2026-09-09 21:30:04 UTC. The coordinator has fully
read and accepted the actual second manuscript pass. The author then
read its entire 255-line report and recomputed its supplied hash.
Required manuscript changes: **0**. Author source changes: **0**.
Additional author compilations: **0**. There is no fabricated revision
or inferred quality improvement from rereading the unchanged manuscript.

### Preserve the records actually read in pass 2

Before any extension of this live log or state, their exact previous
bytes were copied into the new frozen
[round1_records snapshot](snapshots/round1_records/). Direct byte
comparisons passed before the live records were changed.

| Preserved record | SHA256 personally bound by the second reviewer and retained here |
| --- | --- |
| [Round 1 log](snapshots/round1_records/PAPER_IMPROVEMENT_LOG.md) | `d0cf47a68f64f0da1f8db4d9203f86368ac7b0c563f21cca2e66498bde4af824` |
| [Round 1 state](snapshots/round1_records/PAPER_IMPROVEMENT_STATE.json) | `9521819d11f3a18278e0cd493c67d907d53619a7d9b8076d23234fdd5aaafc9e` |

These are historical records, not competing live state files. Their
content, old checkpoint status, and original paper-root-relative links
are retained verbatim; no links inside the frozen copies were rewritten.
The sole live state remains PAPER_IMPROVEMENT_STATE.json at the paper root.

### Second raw review and completed review loop

The complete [actual pass 2 report](reviews/round2/REVIEW.md), 255 lines,
is retained unchanged at its existing immutable path, SHA256
`2c08408b70fb92760ca225692054145220bf1999608bfce62545e0a835838b04`.
It is not replaced by this lifecycle summary. The first raw review and
the separate citation audit retain the exact hashes recorded above.

There are now **two actual manuscript passes by the same nonauthor in
the same reviewer thread**. Both have zero required repairs and have
been accepted by the coordinator. This is not evidence from two
independent manuscript reviewers. The citation audit remains a separate
record and was never counted as either manuscript pass. The selected
auto-paper-improvement-loop's review-preservation and same-thread gates
are satisfied; no external-model, scoring, or unnecessary rebuild example
is imported into this explicitly authorized no-change lifecycle.

All citation-access and retraction-status limitations stated in the
historical checkpoint and complete citation report remain unchanged.
This lifecycle update makes no new primary-source access, clean-status,
structural PDF-PASS, or independent all-page visual-inspection claim.

### Actual round 2 PDF and explicit source alias

[main_round2.pdf](main_round2.pdf) was actually copied from main_round1.pdf
at this checkpoint. It is byte-identical to the current PDF and the
previously bound original, baseline, round-1, and first-build PDFs:
SHA256 `d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa`,
eight pages and 341,782 bytes. It is an archive of unchanged reviewed
bytes, not the output of an invented second-round compilation.

The **round 2 source snapshot is an explicit logical alias** to
[snapshots/round1/source/](snapshots/round1/source/). No new physical
source copy or filesystem symlink is implied. The same twelve-file
snapshot, its ten compilation inputs and two supporting records, and
all twelve hashes in the source-identity table remain frozen. The live
state records this alias explicitly. No source revision occurred in
either review round.

### Final-build ownership and freeze

The author review loop is complete; final-build verification and release
remain pending in this lifecycle record. Root separately assigns B3 the
two clean deterministic final builds, with exclusive write ownership of
the new final_builds directory and FINAL_BUILD_REPORT.md. This author
task did not compile, create those paths, edit that report, or infer any
outcome for B3. Its actual receipt and root's acceptance will govern the
subsequent build gate; this log is not that receipt.

The current source/PDF, existing baseline and source snapshot, three raw
reviews, all round PDFs, and the newly preserved round-1 records remain
frozen. In this round-2 task, only the new round-1 record copies,
main_round2.pdf, and the two authorized live lifecycle records were
written. No mathematical program, Git action, shared-index change,
release operation, or external-model call was performed. No completed
paper, publication acceptance, or release status follows solely from
completion of these two internal manuscript passes.
