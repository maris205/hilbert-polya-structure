# P214 Review B root artifact checker failure 01

2026-09-11 UTC. The first read-only root checker invocation exited nonzero at
the exit-role count. It counted 15 supervised child statuses plus the
controller, while its expected total mistakenly remained 15. The exact failed
source is preserved as `check.failed01.cjs`, SHA256
`334b4aebe5793dc6de0fdd57f9085cbc0a4fd2017c671387b7aef86d865bb02c`.

The expected total is corrected to 16. No build artifact, reviewer evidence or
failed invocation was changed, and this failure is not a PASS.
