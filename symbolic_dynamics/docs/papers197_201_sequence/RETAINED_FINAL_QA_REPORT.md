# Three retained papers: individual terminal completion

2026-09-05 UTC. P197/P199/P200 have each completed their two actual
manuscript reviews, accepted deltas, physical Round2 freezes, two final
source-only builds, root viewing of every final page, exact double
author/A/B replay and complete package manifests.

The full retained-subset audit actually passed twice. The first exact
stdout is qa/RETAINED_TERMINAL_AUDIT_1.txt. The three mutable manuscript
recovery companions were then refreshed from terminal-pending to
individual-terminal-PASS, and only their current manifest entries changed.
No main source, bibliography, verifier, canonical, PDF, accepted review or
frozen source changed. A second full audit re-executed every author/A/B
verifier twice again and validated the refreshed complete packages. Its
actual stdout is qa/RETAINED_TERMINAL_AUDIT.txt: 4,083 mechanical assertions.

| Paper | Pages | Author assertions/run | Review A/run | Review B/run |
|---|---:|---:|---:|---:|
| P197 TCSD | 4 | 3,998,247 | 4,814,623 | 4,833,354 |
| P199 FOSP | 4 | 1,496,779 | 1,926,465 | 1,026,386 |
| P200 LFAS | 4 | 3,595,488 | 3,823,696 | 4,026,047 |

These verifier counts measure executed checks, not numbers of proofs,
subclasses, external reviews or novelty. Six actual terminal cold builds
and twelve actual final 180-dpi page views are documented in the paper
FINAL_QA.md files and qa_final/ directories. Each final cold PDF is byte
identical to the corresponding accepted main_round2.pdf. The full batch
auditor's five-paper requirement has not been disabled: a separate explicit
subset command reports SUBSET_PASS_NOT_BATCH_COMPLETE.

This is **three individually completed papers, not a completed five-paper
batch**. P198/P201 remain rejected drafts; P202 has its own manuscript
rounds to finish and one candidate seat remains open. The latest completed
batch stays P192--P196. OWNER_AMBER / HOLD_EXTERNAL remains binding for
each retained paper; no public release, external submission or specialist
endorsement is inferred. Future exact owner evidence can reopen acceptance.
