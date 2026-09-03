# P176 Hostile Review A — independent exact control

This directory is the executable evidence for the non-author Review A of
`papers/176-first-frequency-rotation/`.

## Independence boundary

`verify_review_a.py` imports no paper-author or scouting module.  It was
implemented from the literal update using integer bitmasks, explicit cyclic
bit rotation, a fresh functional-graph traversal, and independently written
component/fibre/Möbius predictions.  The author control uses tuple words; the
representations and graph engines are distinct.

## Exact box

- every binary orientation for component lengths `1..18` (`524,286`
  profiles);
- every binary word for `1<=n<=19`;
- every pointed necklace and generator component in that box;
- every target inverse set, layer histogram, period, preperiod, deepest
  state, primitive block, and fixed state.

The canonical run reports `14,407,195` assertions and passes all requested
claims while preserving `AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`.

## Replay

From this directory, run:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 verify_review_a.py
```

The output must match `CANONICAL.txt` byte for byte.  During Review A, two
fresh processes matched exactly.

```text
verify_review_a.py  b8fc75bf73ded06a682b4e94474cc4f9301ef35970793b98c3d14b8551ca99be
CANONICAL.txt       b8a02e64afb86c4dc642ba477ac1e4c9afa18cffc66950094e4641cfb42e38ff
```

Finite enumeration is a falsifier and regression control.  The uniform
proof audit is in the paper-local `HOSTILE_REVIEW_A.md`.
