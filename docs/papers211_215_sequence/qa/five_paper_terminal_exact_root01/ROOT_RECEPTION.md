# P211-P215 exact-five terminal root reception

2026-09-11 UTC. Root independently accepts the successful preparation05 run.
The isolated read-only auditor exited zero, emitted 338,038 bytes with SHA-256
`b1a5359e694823e51c2c8df33be8f1e6ccb2706b81c321712557df63a7f4f6f2`,
and had empty stderr. The forbidden reader-cache path remained absent.

Root parsed the complete JSON and verified exactly P211--P215, 15 accepted
author/A/B replay pairs, 15 physical Round manifests, 10 terminal builds and
five final page-view receipts. All ten A/B current finding records are zero;
both central indexes carry 5 retained / 5 complete and `HOLD_EXTERNAL`.
The output pins 1,687 distinct physical inputs and records 246 preserved
failed/HOLD/rejected files. It performed 1,959 bounded physical-file checks,
1,939 stable whole-byte rereads, 1,610 strict manifest-row/digest checks and
all exact cardinality checks.

Preparation02/run01, preparation03/run02 and preparation04/run03 failures are
preserved. They exposed only old P211/P213 naming conventions; preparation05
uses explicit pinned naming adapters, and the auditor logic is unchanged.
Root changes the emitted pending flags only by this separate receipt: the
exact-five gate is accepted and the batch is internally complete. Private Git
synchronization remains separate. `HOLD_EXTERNAL`.
