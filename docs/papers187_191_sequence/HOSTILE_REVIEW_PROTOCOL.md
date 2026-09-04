# Dual hostile-review protocol — P187–P191

Every paper receives two process-separated hostile reviews.  Each review
contains a proof/claim/source audit and an independently written exact control
with canonical stdout and a checksum manifest under this batch directory.

Reviewers attack carrier closure, every theorem quantifier and exceptional
parameter, labelled-target and fibre formulae, recurrence/period/tail/spectrum
claims, asymptotic-to-finite inference, P1–P186 proof transfer, direct-owner
subtraction, verifier independence, anonymity, and lifecycle wording.

Reviewer controls bind the immutable theorem source, reviewed PDF, author
verifier, and author canonical transcript.  They do not bind mutable terminal
paper manifests or post-review lifecycle notes; the terminal audit owns those
checks.  This avoids circular review receipts while preserving hard-fail
coverage of all final rows.

Findings use stable IDs and `Critical`, `Major`, or `Minor` severity.  Every
finding requires a written disposition, a repaired manuscript round, and a
delta verification.  Delta decisions contain a standalone machine-readable
`PASS` or `ACCEPTED` token.  A zero-finding review still records a no-change
rationale and preserves a byte-identical PDF round.  Review B reopens all live
kill switches and does not inherit Review A's semantic conclusions.

Completion requires two `PROVABLE AS STATED` or repaired-and-accepted verdicts
per paper, zero open findings, fresh author and reviewer replays, immutable
Round-0/1/2 PDFs, two source-only cold builds, complete manifests,
integrity/failure-mode audit, and unchanged `HOLD_EXTERNAL`.
