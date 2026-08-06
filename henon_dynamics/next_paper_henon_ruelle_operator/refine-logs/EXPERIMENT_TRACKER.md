# Experiment tracker

This file records the proposed execution order. `PLANNED` does not mean that a
result exists.

| Run | Milestone | Purpose | Mandatory | Status | Gate opened |
|---|---|---|---|---|---|
| G000 | G0 | primary-source theorem-delta and novelty audit | yes | OPEN / BLOCKING | `G000_THEOREM_DELTA.md` + source ledger authorize implementation |
| R000 | M0 | theorem-aware feasibility pilot | yes | BLOCKED_BY_G000 | draft resources only |
| R001 | M0 | freeze conventions, hashes, domains, metrics, and stops | yes | BLOCKED_BY_R000 | T0 |
| R010 | M1 | inherited geometry/coding interface re-check | yes | BLOCKED_BY_R001 | inherited base accepted |
| R015 | M1 | local-basic-set and dimension-theorem applicability preflight | yes | BLOCKED_BY_R010 | dimension route authorized |
| R020 | M1 | interval unstable bundle, adapted-roof variation, and Euclidean gauge bridge | yes | BLOCKED_BY_R015 | T1 |
| R030 | M2 | effective one-sided cohomology and periodic-sum check | yes | BLOCKED_BY_R020 | T2 |
| R040 | M2 | constant- and finite-memory known-truth controls | yes | BLOCKED_BY_R001 | operator implementation accepted |
| R050 | M3 | Hénon finite-memory transfer matrices | yes | BLOCKED_BY_R030_R040 | T3--T4 evidence |
| R060 | M4 | certified real pressure root | yes | BLOCKED_BY_R050 | T5 |
| R065 | M4 | stable/unstable and Hausdorff-dimension certificate consuming R015/R020 | yes | BLOCKED_BY_R060_R020_R015 | T5 geometric conclusion |
| R070 | M4 | independent cycle/matrix and orientation audit | yes | BLOCKED_BY_R050 | cross-check |
| R080 | M5 | flat/random/shuffled/precision controls | yes | BLOCKED_BY_R050 | mechanism audit |
| R090 | M6 | optional fixed-contour determinant certification | no | BLOCKED_BY_T6_THEOREM | T6 |
| R100 | M7 | independent reproduction and Route-A evaluation | yes | BLOCKED_BY_R065_AND_REQUIRED_RUNS | release |

## Current verdict

- No production experiment has been run in this project.
- No pressure root or complex resonance is currently claimed.
- No Hausdorff-dimension interval is currently claimed.
- The quantum Hénon candidate is separately deferred pending its own novelty
  and operator-definition audit.
- Immediate next action: G000. If it passes, R000 is restricted to feasibility
  and known-truth controls.

## Status vocabulary

- `PLANNED`: designed but not started.
- `BLOCKED_BY_*`: intentionally gated by an earlier theorem or run.
- `RUNNING`: command and immutable config exist.
- `DONE_POSITIVE`: all prespecified checks passed.
- `DONE_NEGATIVE`: a prespecified falsifier was reached.
- `NOT_CERTIFIED`: numerical evidence exists but the mathematical gate failed.
- `ABORTED_PROTOCOL_VIOLATION`: frozen protocol was violated; results cannot be
  confirmatory.
