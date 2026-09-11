# P191 Review B — replay receipt

Replays executed on `2026-09-04` UTC from repository root with
`PYTHONDONTWRITEBYTECODE=1`.

## Pinned upstream package checks

- Author verifier:
  `python3 papers/191-prefix-divisibility-cuts/code/verify.py`
  matched `papers/191-prefix-divisibility-cuts/code/CANONICAL.txt` byte for
  byte (`24` lines / `1439` bytes).
- Formal Review-A verifier:
  `python3 papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a/verify_review_a.py`
  matched
  `papers/191-prefix-divisibility-cuts/reviews/round1/reviewer_a/CANONICAL.txt`
  byte for byte (`35` lines / `3639` bytes).

## Review-B verifier checks

- Replay 1:
  `python3 docs/papers187_191_sequence/reviews/p191_b/verify_review_b_p191.py`
  produced byte-identical stdout in a fresh process.
- Replay 2:
  `python3 docs/papers187_191_sequence/reviews/p191_b/verify_review_b_p191.py`
  matched Replay 1 byte for byte in a second fresh process.
- Reviewer verifier SHA-256:
  `bfeb20310d850a5d07e9510ec9076a7a7f913ed340f574044e2e94aaa54071d4`
- Canonical stdout SHA-256:
  `ddd6326fa2312a82046a2d95749915a589b4694551f42f89511253477e4b7214`
- Canonical stdout size: `35` lines / `3460` bytes.

The two Review-B replays are package-integrity receipts only; they do not
convert finite computation into proof or bounded owner search into novelty.
