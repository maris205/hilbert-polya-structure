# C68 test report

```text
producer: PREFREEZE_G3_PASS
structural checker: PASS
SymPy Smith cross-check: SNF_CROSSCHECK_PASS
source replay checker: REPLAY_PASS
hostile mutation test: PASS, 17/17 mutations rejected
```

The producer and checker use separate exact Smith reductions.  The row-side
quotient is computed from an explicit integral basis of the congruence lattice,
and the SymPy path reproduces both quotient Smith forms.
