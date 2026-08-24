# C115 test report

Expected successful commands:

```text
C115_CHECK_PASS 66
C115_SYMPY_PASS 23
C115_REPLAY_PASS <evidence-sha256>
C115_MUTATION_PASS 12/12
```

The checker independently recomputes inverse identities, reversibility,
Jacobian determinant, invariant preservation, fixed and second-iterate
elimination, domain exclusions, the real two-cycle, monodromy, and the
fixed-origin control.  It imports no producer functions.

The PDF closure additionally requires a fixed-date double isolated build,
identical hashes, embedded fonts, exact page count, and a clean final log.
