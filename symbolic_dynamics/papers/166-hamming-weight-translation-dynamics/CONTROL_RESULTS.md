# P166 exact control results

Lifecycle: `ROUND2_INTERNAL_ACCEPT / REVIEWS A-B COMPLETE / HOLD_EXTERNAL`.

## Frozen author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
assertions: 17,017,929
result: PASS
fresh byte-identical replays: 2/2
canonical SHA-256: 7ef213d9334acc39c835f9c9da4b52f4581b423e76de82406d65ece73c55cc06
verifier SHA-256: bf3d58ffddc3ff41381e08b8eaeaca7bde865733b431c2f35d2e63765ab30038
```

The program is deterministic, standard-library only, and imports no scout,
gate, or paper code.  It uses no network, clock, floating point, or
unseeded randomness.

## Exhaustive literal boxes

| `n` | states | image | exact-depth distribution `d:count` | maximum fibre |
|---:|---:|---:|---|---:|
| 2 | 4 | 4 | `0:4` | 1 |
| 3 | 27 | 21 | `0:21,1:6` | 3 |
| 4 | 256 | 180 | `0:156,1:64,2:36` | 3 |
| 5 | 3,125 | 2,175 | `0:1565,1:780,2:540,3:240` | 3 |
| 6 | 46,656 | 32,398 | `0:20308,1:11528,2:8100,3:4920,4:1800` | 4 |
| 7 | 823,543 | 571,886 | `0:327229,1:201810,2:139944,3:90720,4:48720,5:15120` | 4 |

For every target in these boxes, the literal one-step indegree equals the
closed target formula.  For every time `0<=t<=2n`, the directly powered
literal map and independently powered phase map give the same target
indegree.

## Structural boxes

- Every weak composition of `n` into `n` parts was checked for `2<=n<=10`
  (130,475 profiles in total).
- Cycle uniqueness, mass exhaustion, gap support, tail cap, maximum-tail
  shape, and maximum-tail phases were checked profile by profile.
- The exact max-fibre equality classification was checked for every profile
  through `n=10`.
- The explicit max-fibre witness and nonhit-bin repair were checked for
  every `3<=n<=128`, including every triangular boundary.
- 6,000 fixed-seed extension profiles were checked at
  `n=8,9,10,11,12,15,16,20,27,31,48,64`, including composite moduli.

## Boundary controls

The transcript explicitly covers `n=2`, `t=0`, integer weights zero and
`n`, the all-zero target, targets with no zero coordinate, empty one-step
fibres, prime and composite `n`, triangular remainders, and the last
transient shell.

The executable controls are falsification evidence only; the manuscript's
proofs are self-contained.

## Independent Review-A control

Hostile Review A used a separate implementation and reported `11,795,304`
assertions, `PASS`, and two byte-identical replays.  It returned
`0 Critical / 0 Major / 0 minor`; no author control or canonical transcript
changed for Round 1.

## Independent Review-B control

Fresh Hostile Review B used another independent standard-library
implementation.  It reports `14,005,344` assertions, `PASS`, and two
byte-identical process replays; it also replayed the author verifier twice
against the frozen author canonical.  The verdict was `ACCEPT_INTERNAL` with
`0 Critical / 0 Major / 0 minor`.  No author control changed for Round 2.
