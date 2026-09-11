# P195 Review-B replay receipt

Replays ran on 2026-09-04 UTC from repository root with
`PYTHONDONTWRITEBYTECODE=1`.

## Pinned upstream replays

- author: `python3 papers/195-odd-side-least-neighbor-trees/code/verify.py`
  matched its canonical transcript byte for byte (`13` lines / `876` bytes);
- Review A:
  `python3 docs/papers192_196_sequence/reviews/p195_a/verify_review_a_p195.py`
  matched its canonical transcript byte for byte (`19` lines / `1113` bytes).

## Review-B replays

- replay 1 ran
  `python3 docs/papers192_196_sequence/reviews/p195_b/verify_review_b_p195.py`
  in a fresh process;
- replay 2 ran the same command in a second fresh process;
- replay 1 and replay 2 are byte-identical;
- both match `CANONICAL.txt` byte for byte (`18` lines / `1068` bytes).

```text
transitions=2223278
assertions=9390311
record_digest=4126ec772a597e46c2b387681c46df7bf96b83c1774b9f3436d515c03361b354
open_critical=0 open_major=0 open_minor=0
status=PASS
```

The receipt verifies deterministic replay only.  Exact enumeration remains
bounded falsification pressure and does not clear external ownership.
