# Round 10 Papers 29–33 — Stage 1 Phase 5 reviewer configuration

Configured: **2026-09-02T10:28:16Z**  
Input freeze: `BATCH_ROUND10_STAGE1_PHASE5_INPUT_FREEZE.json`

## Seats

| Seat | Role | Scope | Output | Calibration |
|---|---|---|---|---|
| `R10-P5-EIC` | Editor-in-Chief | originality/contribution, method, evidence, coherence, writing | categorical editorial verdict and actionable findings for each paper | `NOT_CALIBRATED` |
| `R10-P5-ETH` | Ethics and research integrity | AI disclosure, attribution, dual use, representation, data, conflicts, human-subject boundary | `CLEARED`, `CONDITIONAL`, or integrity-only `BLOCKED` for each paper | `NOT_CALIBRATED` |
| `R10-P5-CIT` | Citation integrity | exact marker/list/inventory closure, manifest constraints, frozen verification coverage, locator status | structural and claim-faithfulness status for each paper | deterministic checks plus `NOT_CALIBRATED` semantic review |
| `R10-P5-DA` | independent Devil's Advocate, Checkpoint 3 | strongest counterargument, overreach, alternatives, limitations, significance | `PASS` or `REVISE` for each paper | `NOT_CALIBRATED` |
| `R10-P5-SYN` | role-preserving synthesis | combines but does not overwrite the four seat records | categorical integrated disposition and revision roadmap | `NOT_CALIBRATED` |

## Independence and model disclosure

The EIC, Ethics, and DA seats are separately dispatched and are blind to one
another's findings during first-pass review. The citation-integrity seat is a
separate closed-corpus pass, and synthesis begins only after all role outputs
are frozen. All seats use the current Codex model family; no external provider
or cross-model transfer is authorized. Separation is procedural independence,
not proof of statistically independent errors. The review is therefore
recorded as single-family and `NOT_CALIBRATED`.

## Categorical judgment rule

No reviewer score, weighted score, hidden scalar, acceptance probability, or
numerical ranking is permitted. Dimension judgments use only `STRONG`,
`ADEQUATE`, `NEEDS_REVISION`, `INADEQUATE`, or `NOT_APPLICABLE`, with written
evidence. Editorial verdicts remain `ACCEPT`, `MINOR_REVISION`,
`MAJOR_REVISION`, or `REJECT`.

## Blind inputs

Each seat receives the exact five Phase-4 reports, their Phase-4 manifests,
their Phase-2 verification records, the Phase-4 checkpoint, the two frozen
roadmaps, this configuration, and the Phase-5 contract. No seat may edit an
input, retrieve new material, inspect another seat's first-pass output, or
write a Phase-6 deliverable.

## Decision preservation

Every finding receives a stable paper/seat identifier. The synthesis must map
each finding to `required_before_delivery`, `required_before_scientific_run`,
`advisory`, or `no_action`. A `CRITICAL` DA issue or integrity-only `BLOCKED`
ethics issue cannot be diluted. An unresolved EIC major issue, ethics
condition, citation-integrity non-clearance, or DA `REVISE` verdict requires a
recorded revision disposition even when no core scientific conclusion is
invalidated.
