# C139 hostile and boundary audit

The mutation suite contains 48 registered semantic corruptions whose payload
hash is repaired before checking, plus one stale-hash control.  Coverage
includes the roof and marker locks, state order, transition rule, determinant
and receipt, specialization, clock basis, all-period formula fields, every
period row, memory witness, residual collision, totals, Route-A tuple, scope
flags, nonclaims, and closed schemas.  All 49 are rejected.

The registered set is not claimed to enumerate every possible corruption.  It
demonstrates semantic rejection rather than reliance on a stale hash.

Failure-mode findings retained in the release:

- minimal memory is relative to the frozen forward coding, not cohomology or
  recoding invariant;
- the four-block marker does not give primitive-orbit injectivity;
- the first retained collision occurs at period seven;
- the fixed-`z=1` qualification is required for the imaginary-period control;
- the primitive product is symbolic-dynamical, not arithmetic;
- target matching, global target structure, natural quantization,
  Hilbert--Polya, and Route B remain nonclaims.

Verdict: PASS within `NO_BAD_EULER_OR_ROOT_NUMBER`.
