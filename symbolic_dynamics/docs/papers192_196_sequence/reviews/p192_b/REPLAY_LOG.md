# P192 Review-B replay receipt

All replays ran on 2026-09-04 UTC from repository root.

## Pinned upstream controls

- author Python control:
  `PYTHONDONTWRITEBYTECODE=1 python3 papers/192-first-collision-hurwitz/code/verify.py`
  matched its canonical transcript byte for byte (`13` lines / `864` bytes);
- accepted Review-A control:
  `PYTHONDONTWRITEBYTECODE=1 python3 docs/papers192_196_sequence/reviews/p192_a/verify_review_a_p192.py`
  matched its canonical transcript byte for byte (`27` lines / `1223` bytes);
- author `n=9` control was freshly compiled with `g++ -O2 -std=c++17` and
  matched `CANONICAL_N9.txt` byte for byte (`132` lines / `4643` bytes).

## Review-B fresh-process replays

- replay 1 ran
  `PYTHONDONTWRITEBYTECODE=1 python3 docs/papers192_196_sequence/reviews/p192_b/verify_review_b_p192.py`;
- replay 2 ran the same command in a second fresh process;
- replay 1 and replay 2 are byte-identical;
- both match `CANONICAL.txt` byte for byte (`33` lines / `1945` bytes).

```text
states=280392
transitions=280392
targets=280392
assertions=4606117
record_digest=5343319ee0915bf342877ea2511e14201fa9c99c0822804ae914f94550b2ba5f
history_law_status=CONJECTURE_ONLY_FINITE_N_LE_8_PLUS_PINNED_N9
open_critical=0 open_major=0 open_minor=0
status=PASS
```

Replay certifies deterministic integrity, not proof by exhaustion, novelty, or
owner clearance.
