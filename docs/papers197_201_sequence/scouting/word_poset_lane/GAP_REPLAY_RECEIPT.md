# Supplementary TCSD gap-product check

2026-09-05 UTC. `verify_gap_supplement.py` directly enumerates all original
ternary inputs through n=10, counts their literal sign-derivative outputs,
and separately parses every possible target into cyclic runs. It imports
none of the earlier verifier. The exact gap product agrees on every target,
including empty fibres and small all-zero ties: 88,582 assertions per run.

Two fresh captured subprocess outputs were byte-identical and stderr-free.
Their 431 bytes are preserved in GAP_CANONICAL.txt.

- Script SHA-256: `273b6492ee8d20eb73d8721ee772cfee011a6e4e9f3650564e30d4c75cec3189`.
- stdout SHA-256: `1435f17ea41e686d624b7c3290a22fe7b312dd6ef88b869910a262a2fcbf9dad`.

This is root's supplemental finite control, not another process-separated
reviewer. The all-size argument is in TCSD_EXACT_GAP_PROOF.md. No assertion
count is a count of newly proved systems or papers.
