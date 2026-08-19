# C69 test report

```text
producer: PREFREEZE_G3_PASS
structural checker: PASS
SymPy Smith cross-check: SNF_CROSSCHECK_PASS
source replay checker: REPLAY_PASS
hostile mutation test: PASS, 23/23 mutations rejected
```

The producer and checker separately reconstruct the retraction, lattice basis,
integral presentation, Smith factors, and `Hom` count.  The SymPy path repeats
the central matrix and Smith calculations.
