# C140 hostile and boundary audit

The mutation suite contains 53 registered semantic corruptions whose payload
hash is repaired before checking, plus one stale-hash control.  Coverage
includes the language and roof locks, graph states/transitions, cover matrix,
cover versus intrinsic determinant fields, strict-sofic and Fischer-cover
claims, all-period correction, each finite row, totals, fixed-count sequences,
exceptional periods, Route-A tuple, scope flags, nonclaims, and closed schemas.
All 54 are rejected.

The registered set is not claimed to enumerate every possible corruption.  It
demonstrates semantic rejection rather than reliance on a stale hash.

Failure-mode findings retained in the release:

- the all-zero label point has three cover lifts but counts once intrinsically;
- `D_cov` is not silently substituted for `D_140`;
- no natural Fredholm owner is constructed for the corrected rational factor;
- the fixed-`z=1` qualification is required for the imaginary-period control;
- the primitive product is symbolic-dynamical, not arithmetic;
- target matching, global target structure, natural quantization,
  Hilbert--Polya, and Route B remain nonclaims.

Verdict: PASS within `NO_BAD_EULER_OR_ROOT_NUMBER`.
