# Paper 11 post-run analyzer

This directory is a validator-only tree.  It has no authority to execute or
rerun the registered candidate.  The registered execution remains bound to the
immutable execution tree
`5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb`.

The first manifest command was attempted once after the independent result
review.  It stopped before creating `results/result_manifest.json` with
`CONTROLS_NOT_EXACT_RECOMPUTED_TRUE`.  The sole cause was a post-run analyzer
type error: JSON serializes a singleton Python tuple as an array, and strict
JSON loading correctly returns a list, while the old K005 recomputation
compared that list with a tuple.

This analyzer repairs only that boundary.  It requires a singleton JSON list,
reproduces the historical list-versus-tuple failure, preserves every immutable
execution/result/report byte, binds an independent analyzer tree and JUnit,
and implements exact pre-write and final result inventories.  Its manifest
writer is exclusive and one-shot; its existing-manifest validator is read-only.

Before a real manifest write, the analyzer tree and analyzer JUnit must be
frozen and an independent reviewer must add exactly one canonical
`EQUIVARIANT_CLOCK_POSTRUN_ANALYZER_REVIEW_V1` authority line to
`results/POSTRUN_ANALYZER_REVIEW.md`.
