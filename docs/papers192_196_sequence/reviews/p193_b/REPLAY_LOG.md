# P193 Review-B replay receipt

Replays ran on 2026-09-04 UTC from repository root with
`PYTHONDONTWRITEBYTECODE=1`.

## Pinned upstream replays

- author: `python3 papers/193-mutual-best-block-refinement/code/verify.py`
  matched its canonical transcript byte for byte (`16` lines / `989` bytes);
- Review A:
  `python3 docs/papers192_196_sequence/reviews/p193_a/verify_review_a_p193.py`
  matched its canonical transcript byte for byte (`19` lines / `1096` bytes).

## Review-B replays

- replay 1 ran
  `python3 docs/papers192_196_sequence/reviews/p193_b/verify_review_b_p193.py`
  in a fresh process;
- replay 2 ran the same command in a second fresh process;
- replay 1 and replay 2 are byte-identical;
- both match `CANONICAL.txt` byte for byte (`16` lines / `1063` bytes).

```text
transitions=46233
assertions=1170066
record_digest=d4d9d2f86f2b0e2e5b54fc62b8e80e4cf5f58ada010a5cfe21dc3b7c2d46c586
open_critical=0 open_major=0 open_minor=0
status=PASS
```

The receipt verifies deterministic package replay only.  It does not convert
bounded computation or search into proof, novelty, or ownership clearance.
