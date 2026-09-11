# P188 Review B — replay receipt

Replays executed on `2026-09-04` UTC from repository root with
`PYTHONDONTWRITEBYTECODE=1`.

## Pinned upstream package checks

- Author verifier:
  `python3 papers/188-self-cardinality-truncation/verify_p188.py`
  matched `papers/188-self-cardinality-truncation/CANONICAL.txt` byte for
  byte (`5` lines / `149` bytes).
- Formal Review-A verifier:
  `python3 docs/papers187_191_sequence/reviews/p188_a/verify_review_a_p188.py`
  matched `docs/papers187_191_sequence/reviews/p188_a/CANONICAL.txt` byte for
  byte (`13` lines / `443` bytes).

## Review-B verifier checks

- Replay 1:
  `python3 docs/papers187_191_sequence/reviews/p188_b/verify_review_b_p188.py`
  produced byte-identical stdout in a fresh process.
- Replay 2:
  `python3 docs/papers187_191_sequence/reviews/p188_b/verify_review_b_p188.py`
  matched Replay 1 byte for byte in a second fresh process.
- Reviewer verifier SHA-256:
  `3b58baf3090487528cde5f1f0865ce0605e84752ca81889113a8348f00ec27a5`
- Canonical stdout SHA-256:
  `573f4e578060c8cfa2f4319c353662b54e281bfba00afd13f5494191501f3a12`
- Canonical stdout size: `30` lines / `2539` bytes.

The replay receipts certify package integrity only. They do not upgrade the
mathematics to proof-by-exhaustion or the bounded source audit to ownership
clearance or external release.
