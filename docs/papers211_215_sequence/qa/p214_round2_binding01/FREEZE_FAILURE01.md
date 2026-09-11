# P214 Round2 freeze attempt 01 failed before copy

2026-09-11 UTC. Actual invocation chunk `29e866` exited 1 with no session.
All six named content pins printed `OK`, then `sha256sum --strict` rejected the
trailing blank line in `INPUTS.sha256` as one improperly formatted line. The
recipe stopped before its destination-absence check and before `mkdir`; the
Round2 tree remained absent. This attempt receives no freeze credit and is not
retried under its consumed grant.

