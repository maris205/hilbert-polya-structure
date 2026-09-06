# Two fresh deterministic replay receipts

Date: 2026-09-05 UTC. Both runs were actual separate Python process launches,
not copies of an inherited transcript. The initial exploratory execution is
not counted as either of the two final replays below.

Command, run from `/root/autodl-tmp/symbolic_dynamics`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/papers197_201_sequence/scouting/final_seat_tree_lane_20260905/verify_lgb_reentry.py
```

## Replay 1

- Execution receipt chunk: `71a6c2`.
- Exit code: `0`; tool-reported elapsed time: `0.87854729` seconds.
- States: `18,249`; assertions: `164,277`.
- Final line: `PASS_MATHEMATICS / RECOMMEND_KILL_VALUE_THIN / NO_PAPER_NUMBER`.

## Replay 2

- Execution receipt chunk: `f48652`.
- Exit code: `0`; tool-reported elapsed time: `0.892037162` seconds.
- States: `18,249`; assertions: `164,277`.
- Same final line as Replay 1.

## Byte equality and frozen pins

The complete stdout strings returned by the two process launches were
compared directly and were **byte-identical** (ASCII throughout). The exact
text, including its final newline, was written through `apply_patch` as
`CANONICAL.txt`. No timestamps, randomness, absolute paths or process IDs
are emitted by the verifier.

```text
verify_lgb_reentry.py
0e694c1c9e3d218553d1e00b1655b69ab684ef38c7f29251d86cfaed1899334f
CANONICAL.txt
b53dd33990292abf685de6ff85ff25b987dda97f62d71007fa7f443cdb55b010
PINNED_INPUTS_SHA256SUMS
68235079c612f8b05854de6c064243df8ee452efa219da06e9d7247df3494a7d
```

`PINNED_INPUTS_SHA256SUMS` records ten historical inputs, with paths relative
to the repository root. The final `SHA256SUMS` records every top-level file
in this lane except itself, with paths relative to this lane. All historical
inputs remained unchanged. No PDF/manuscript build was called for this
negative scouting package, and no paper-review completion is claimed.

These are author-side repeatability checks. Independent representation from
the old pilot is supplied by parent-tuple enumeration and the compressed
inverse, but no claim of a separate reviewer or another model follows from
running a program twice. External state remains `HOLD_EXTERNAL`.
