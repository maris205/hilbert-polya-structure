# Scout35 initial-document recovery

Scope: this directory only. The original sealed Scout35 package is unchanged.

Status:
**LATER_RECONSTRUCTION_FROM_ACTUAL_HISTORY_AND_MATCHING_OLD_PIN**.

The initial 27-payload manifest recorded older REPORT.md and
SOURCE_AND_HISTORY.md bytes that were not retained as physical copies
inside the final 31-payload package. Root identified this documentary
preservation gap. It is not a scientific defect, and the original seal
must not be described as having preserved those two pre-edit files.

This supplement reconstructs exactly those two old documents by reversing
the two-document portion of the actual correction, then requiring the
complete SHA-256 digests from the immutable initial manifest. The original
added text also matches the original creation/correction sequence. The
proof package and all scientific source/output files are outside this task.

The historical forward delta is recorded as ORIGINAL_DOCUMENT_EDIT.patch
for provenance only. Do not apply it to the sealed scout. Current-source
captures live under inputs/ and are explicitly later captures, not
pre-edit snapshots. Exact reconstructed bytes live under
reconstructed_initial/; their text is intentionally not annotated because
an annotation would invalidate the old hashes. This document supplies
their provenance label.

The read-only reconstruction script prints full input/output evidence.
File creation is separately performed with apply_patch. Subsequent
comparisons check the physical reconstructed files against the initial
manifest's two exact roles and compare each actual current-source capture
against the sealed source. No old or modified old checker is run.

An initial orchestration attempt had an unescaped Markdown backtick in a
JavaScript template literal. It failed at parse time before any nested tool
call or file creation; RECOVERY_PREPARATION_FAILURE_01.actual.json retains
that actual failure and its no-execution boundary.
