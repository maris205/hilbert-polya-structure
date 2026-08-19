# C74 test report

```text
producer: PREFREEZE_G3_PASS
independent finite-group checker: PASS
matrix/image cross-check: GROUP_CROSSCHECK_PASS
clean-process replay: REPLAY_PASS
hostile mutation test: PASS, 28/28 rejected
Python syntax compilation: PASS
```

The producer and checker independently enumerate the 54-point group and all
5832 affine maps.  The cross-check separately verifies the 243 odd-part,
486 full-endomorphism, and 108 automorphism counts.
