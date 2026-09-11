# Two actual P202 B fresh processes

Root executed two independent fresh Python processes of the unchanged B
program in parallel, capturing stdout and stderr separately. These are
two executions of one B implementation, not two different reviews.
Command from the workspace root:

    python3 -B docs/papers197_201_sequence/reviews/p202_b/verify_flux_powers.py

| Execution | Actual start UTC | Actual finish UTC | Duration seconds | Exit |
|---|---|---|---:|---:|
| Replay 1 | 2026-09-05 07:26:36.060037 | 2026-09-05 07:27:09.460690 | 33.400667 | 0 |
| Replay 2 | 2026-09-05 07:26:36.040261 | 2026-09-05 07:27:09.350360 | 33.310114 | 0 |

Both stderr strings were empty. The captured complete stdout strings were
compared directly and were byte-identical, then saved with apply_patch as
REPLAY1.txt, REPLAY2.txt and CANONICAL.txt. Subsequent physical cmp checks
also passed. Each has8456463 assertions, all797160 words n=1..12,
8708 parking configurations, and sharp witnesses n=3..210.

Verifier SHA-256:
6f2e146854b12e2490d9b383bab1d1e55686619457d8e7a5d7affe57c34f5835.
Canonical/replay SHA-256:
34f6f11dfbfdd6918b7f43c30e332ade205aa632cc5c303c8bfb63683938ea8d.

An earlier unchanged-code development execution also passed, but is not
counted as either fresh final replay. No author/A verifier source was
read or imported to build the B implementation. No theorem or novelty
claim is established by the number of checks or by reproducibility.
The reviewer is root itself, not an invented additional external referee.
