# C76 pilot report

Status: **PREFREEZE_G3_PASS**.

The source-bound producer and independent checker agree on the complete
finite support computation.  The effective label group has order 1920 and
acts on all 65536 masks.  The atlas contains 3024 support orbits with size
spectrum

```text
1:128, 2:256, 4:416, 5:128, 8:192,
10:384, 16:16, 20:672, 40:608, 80:208, 160:16.
```

The closure-minimal filter retains 98 supports in 34 orbits.  The full-core
filter retains 25 supports in seven orbits, and every one is a triple.

The result is source-bound to the C75 evidence and manifest hashes listed in
`SOURCE_AUDIT.md`.  The C6 ambient kernel is recorded but excluded from the
effective label action.  GAP, clean replay, and hostile mutation results are
reported in `results/TEST_REPORT.md` and `results/HOSTILE_AUDIT.md`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
