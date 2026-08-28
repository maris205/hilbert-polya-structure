# Deterministic control results

Command:

```bash
python3 code/verify_fredkin.py
```

Status: **PASS**.

- `299,592` states across `m=1,...,6` were exhaustively evaluated.
- The instrumented run executed **1,878,811 actual control assertions**.
- Every aligned and shifted layer was checked as an involution on every
  state.
- The explicit inverse, reversing identity, Hamming-weight conservation,
  and global bijectivity all passed.
- For every state, the literal update's fixed predicate agreed with the
  independent nearest-neighbor SFT predicate.
- The displayed transfer matrix was checked against all `8 x 8 = 64`
  ordered block pairs.
- Matrix rank, the first twelve traces, and the fixed-count recurrence passed.

## Full finite cycle census

The notation `period:count` gives the number of cycles, not the number of
states, at that period.

```text
m=1 states=8 fixed=5 max_period=3
  {1:5, 3:1}
m=2 states=64 fixed=19 max_period=4
  {1:19, 2:9, 3:5, 4:3}
m=3 states=512 fixed=80 max_period=8
  {1:80, 2:75, 3:46, 4:15, 6:6, 8:6}
m=4 states=4096 fixed=343 max_period=18
  {1:343, 2:537, 3:321, 4:149, 6:108, 8:24, 10:2, 12:2,
   14:2, 16:4, 18:8}
m=5 states=32768 fixed=1475 max_period=32
  {1:1475, 2:3600, 3:2101, 4:1200, 6:1240, 8:230, 10:5,
   12:75, 16:35, 18:105, 30:5, 32:5}
m=6 states=262144 fixed=6346 max_period=74
  {1:6346, 2:23433, 3:13432, 4:9273, 6:12078, 8:1872, 10:3,
   12:1314, 16:336, 18:966, 24:96, 30:6, 32:48, 54:24, 74:3}
```

The fixed counts are

```text
5, 19, 80, 343, 1475, 6346,
```

matching both `tr(M^m)` and `f_m=5f_{m-1}-3f_{m-2}`.  These controls are
exact over the displayed finite range, but they are neither the proof of the
all-`m` formulas nor a novelty claim.  The temporal maximum-period sequence
`3,4,8,18,32,74` is reported without extrapolation.
