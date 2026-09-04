# P190 Review B — replay receipt

Replays executed on `2026-09-04` UTC from repository root with
`PYTHONDONTWRITEBYTECODE=1`.

## Pinned upstream package checks

- Author verifier:
  `python3 papers/190-brandt-sandwich-erosion/code/verify_p190.py`
  matched `papers/190-brandt-sandwich-erosion/code/CANONICAL.txt` byte for
  byte (`32` lines / `4693` bytes).
- Formal Review-A verifier:
  `python3 docs/papers187_191_sequence/reviews/p190_a/verify_p190_review_a.py`
  matched `docs/papers187_191_sequence/reviews/p190_a/CANONICAL.txt` byte for
  byte (`51` lines / `5618` bytes).

## Review-B verifier checks

- Replay 1:
  `python3 docs/papers187_191_sequence/reviews/p190_b/verify_review_b_p190.py`
  produced byte-identical stdout in a fresh process.
- Replay 2:
  `python3 docs/papers187_191_sequence/reviews/p190_b/verify_review_b_p190.py`
  matched Replay 1 byte for byte in a second fresh process.
- Reviewer verifier SHA-256:
  `f25dbcf9c6314d77ec068d989047df77012aa7233071ec3edf4bd1b9b419dca3`
- Canonical stdout SHA-256:
  `7dc48384c76202e4b9737ff27ff73811879176e613a08b9d010af1b80a03a2cb`
- Canonical stdout size: `46` lines / `5386` bytes.

The two Review-B replays are package-integrity receipts only; they do not
convert finite computation into proof or bounded owner search into novelty.
