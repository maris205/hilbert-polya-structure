# P214 final B root receiver failure 02

2026-09-11 UTC. Root's second combined seal command also exited 1. The four
review-directory-relative entries in `FINAL_SHA256SUMS` passed, but the
workspace-relative entries in `FINAL_INPUT_PINS.sha256` were then incorrectly
evaluated from the reviewer directory and failed path resolution.

This is a receiver cwd error only. It receives no whole-command PASS credit,
does not invalidate the four explicitly printed successful final-file checks,
and made no scientific, review, build or frozen-artifact mutation. The two
manifests are rerun separately from their declared base directories.
