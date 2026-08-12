# Experiment Tracker

No Stage-02 numerical run has been executed.

| ID | Milestone | Purpose | Object / variant | Cutoff | Exact outputs | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| `S2-T000` | M0 | strict-extension obstruction | graded infinite wheel tail shift | all levels | proof | MUST | DONE | extension branch closed |
| `S2-T001` | M0 | bisimulation/clock obstructions | finite DAG class; level-labelled wheel; finite local decoder | scoped theorem classes | proofs and counter-boundaries | MUST | DONE | does not exclude every infinite recoding |
| `S2-D001` | M1 | freeze one infinite recoding | factor or observational recoding | infinite object | completed source lock and rule hash | MUST | TODO | current blocker; no candidate ID |
| `S2-R001` | M2 | validate exact implementation | hand DAG + cyclic stationary toy | tiny; periods 1–12 | partitions, SCCs, fixed/primitive counts | MUST | BLOCKED | requires D001 |
| `S2-R002` | M3 | first main audit | source-locked canonical recoding | K=5; periods 1–12 | full joint signature | MUST | BLOCKED | rule frozen before run |
| `S2-R003` | M3 | cutoff extension | unchanged main recoding | K=6,7; periods 1–12 | consistency and full joint signature | MUST | BLOCKED | no rule edits |
| `S2-R004` | M4 | clock ablation | source-locked clock-erased recoding | K=5,6,7 | partition coarsening, SCC/cycle counts, lost labels | MUST | BLOCKED | zero cycles is allowed |
| `S2-R005` | M4 | deterministic controls | fixed + cyclic deletion | K=5,6,7 | full joint signature | MUST | BLOCKED | matched convention required |
| `S2-R006` | M4 | random controls | five frozen seeds | K=5,6,7 | every seed's full signature | MUST | BLOCKED | no best-seed selection |
| `S2-R007` | M5 | final certificate audit | all preceding artifacts | all | hashes, completeness, one outcome | MUST | BLOCKED | no determinant stage |

`BLOCKED` here is a tracker dependency state, not a Route-A evidence label and
not a project-level blocked verdict.  Completing `S2-D001` is the only action
that unlocks implementation.
