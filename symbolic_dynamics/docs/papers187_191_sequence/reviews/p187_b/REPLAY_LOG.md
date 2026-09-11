# P187 Review B — replay receipt

Replays executed on `2026-09-04` UTC from repository root with
`PYTHONDONTWRITEBYTECODE=1`.

## Pinned upstream package checks

- Author verifier:
  `python3 papers/187-cyclic-divisor-quotient/code/verify_p187.py`
  matched `papers/187-cyclic-divisor-quotient/code/CANONICAL.txt` byte for
  byte (`6` lines / `196` bytes).
- Formal Review-A verifier:
  `python3 docs/papers187_191_sequence/reviews/p187_a/verify_review_a_p187.py`
  matched `docs/papers187_191_sequence/reviews/p187_a/CANONICAL.txt` byte for
  byte (`13` lines / `424` bytes).

## Review-B verifier checks

- Replay 1:
  `python3 docs/papers187_191_sequence/reviews/p187_b/verify_review_b_p187.py`
  produced byte-identical stdout in a fresh process.
- Replay 2:
  `python3 docs/papers187_191_sequence/reviews/p187_b/verify_review_b_p187.py`
  matched Replay 1 byte for byte in a second fresh process.
- Reviewer verifier SHA-256:
  `cd9b1d0db12f5821d2b20f6b04225ca6938b7cf4b85cd5a2b533c2cf40ff29c3`
- Canonical stdout SHA-256:
  `92c8e6cf6a5fa324029e4ec52b9ec68a0e5511b50b01686e706657f33014e9e2`
- Canonical stdout size: `67` lines / `8459` bytes.

The replay receipts certify package integrity only. They do not upgrade the
mathematics to proof-by-exhaustion or the bounded source audit to ownership
clearance or external release.
