# P215 Review B canonical adoption

2026-09-11 UTC. After the complete initial DATA root reception, root verified
that `reviews/p215_b/CANONICAL.txt` did not exist, copied only the actual
initial-run stdout without clobbering, and compared the complete raw bytes.
The adopted canonical is 1,739 bytes with SHA-256
`8c20881098141820fbc67fcce89879a634ea590501ed1909986228d7d69970a8`.

The initial producer did not read a canonical. Each later strict run must bind
this exact file in its complete PRE/POST input set. This adoption is not a
strict replay, final B verdict, manuscript edit, build or Round2 freeze.
