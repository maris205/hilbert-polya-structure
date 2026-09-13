---
name: route-a-evaluator
description: Assess explicit Riemann dynamical-determinant or arithmetic-orbit claims with Route A gates. Use for formal Route A scoring or a requested scoped gate audit, not routine symplectic theorems or PDF fixes.
---

# Route A evaluator

Identify the claimed arithmetic object and the requested evaluation scope. A purely structural symplectic result need not pass Route A; explain non-applicability when relevant and continue the user's actual task.

For a formal evaluation, read [the rubric and schema](references/rubric.md) in full. Preserve its scientific thresholds, verdict enums, same-object/clock/normalization requirements, signed cancellations, and prohibition on target-data fitting. Numerical agreement is not a theorem or RH proof.

For a scoped gate question, use the same rubric to answer only that question. Missing evidence limits the verdict; it does not require inventing experiments or completing unrequested later gates. A failed arithmetic gate can yield a useful scoped obstruction or structural paper without advancing Route A.

Use candidate artifacts and relevant registry entries first. Read prior-work indexes or specific papers when needed for a claim, not the whole archive. Verify the exact source of any literature benchmark before relying on it; optional Weil-compression examples are not universal gates.

Bind available inputs to existing locks or relevant file hashes. In a non-Git workspace, set commit fields to `null` with a reason; do not create a repository to fill a report field. Distinguish an absent test split in a fitted-zero claim from a proof-only scoped audit.

Report the requested verdict, evidence, limitations, and next useful test. Use the full v0.2.0 YAML schema when formally scoring; a limited answer need not fabricate a full report. Do not award Route B readiness without the rubric's conditions; a user-requested limited Route B audit remains limited.

For unassessed fields use `null` or empty evidence lists and explain why. Put evaluation testability in `claim_boundary`; a known decisive A0 failure may still support `ROUTE_A_REJECTED` when other gates are unassessable. If no overall verdict is justified, use `null` with `NOT_TESTABLE` in that explanation, not an invented verdict enum. Retain the rubric's evidence-status vocabulary in formal reports.

When the task includes saving a formal evaluation, create a new timestamped file under `evaluations/route_a/<candidate_id>/` and update only genuinely changed registry entries. A review-only request does not authorize running experiments or changing records. Record cross-family clues and stop that branch, not unrelated authorized work.

User instructions take precedence over skill workflow guidance; scientific claims must still match the evidence. If this skill itself requires pausing the task, identify the relevant instruction and concrete missing input or authority.
