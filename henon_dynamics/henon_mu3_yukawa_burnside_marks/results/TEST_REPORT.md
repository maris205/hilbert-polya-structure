# C64 test report

The following gates pass on the canonical evidence:

```text
producer: PREFREEZE_G3_PASS
structural checker: PASS
source replay checker: REPLAY_PASS
hostile mutation test: PASS, 10/10 mutations rejected
```

The checker recomputes all 256 marks from the C61/C62 source arrays in a
separate Python process and verifies canonical bytes, source hashes, rank,
determinant, and the (R_4) witness.
