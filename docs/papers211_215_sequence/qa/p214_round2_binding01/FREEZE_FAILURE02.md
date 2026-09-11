# P214 Round2 freeze attempt 02 failed after payload copies

2026-09-11 UTC. Actual chunk `2575cb` exited 1 with no session. All six bound
inputs passed. The recipe created frozen_round2 and copied/compared all 30
intended payloads, then encountered a real trailing blank record in FILES.tsv
as a 31st mapping and stopped at the nonempty-source guard. It did not create
SHA256SUMS and receives no freeze credit. The complete partial tree is retained
without modification as `frozen_round2_failed_attempt02`; it will not be
reused or completed.

