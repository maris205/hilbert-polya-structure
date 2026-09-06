# Root replay of the unchanged FOSP author verifier

Date: 2026-09-05 UTC. Two new subprocesses ran
`python3 -B verify_fosp.py --max-n 8` from the workspace, with captured
stdout compared directly to the existing CANONICAL.txt. Both exited zero;
both stderr streams were empty; both stdout byte comparisons passed.

| Run | Scope | Assertions | stdout bytes | Elapsed seconds |
|---|---|---:|---:|---:|
| 1 | n=0,…,8 | 71,614,800 | 1,566 | 89.055 |
| 2 | n=0,…,8 | 71,614,800 | 1,566 | 88.682 |

Script SHA-256:
`e97626999b2b6875b8a1c3b8082fc07ef62dff3397a8715544998b17dcf394da`.

Each stdout and the canonical SHA-256:
`da6cdfe09fdc96628f011e66e48416cb52729c5c5f7692078c74253a70d4ecb2`.

This closes the missing durable replay-receipt item. It repeats the author's
existing exact tests, not a fresh independent proof or paper review. The
historical canonical status string remains unchanged; the effective current
candidate verdict is the separate accepted Stage-1 source delta.
