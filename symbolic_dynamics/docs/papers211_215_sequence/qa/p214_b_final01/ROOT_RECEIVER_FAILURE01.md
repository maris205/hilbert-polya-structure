# P214 final B root receiver failure 01

2026-09-11 UTC. Root's first combined read-only receipt command exited 1.
It incorrectly checked the directory-relative `FINAL_SHA256SUMS` from the
workspace root, addressed the live paper below `docs/papers211_215_sequence`
instead of workspace-root `papers/`, and attempted unavailable `jq`.

The independently workspace-relative `FINAL_INPUT_PINS.sha256` portion did
pass before the command reached those receiver errors. The reported 171-file
count was observational only. This failed invocation receives no acceptance
credit and did not modify any scientific, review, build or frozen artifact.
