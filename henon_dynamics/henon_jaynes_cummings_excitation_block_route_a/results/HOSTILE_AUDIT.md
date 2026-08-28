# Hostile audit

## Failure modes tested

- replacing `sqrt(n)` by `n`, shifting the block index or reversing detuning
  is caught by exact block extraction;
- the zero-frequency block is handled by a continuous limit rather than a
  `0/0` evaluation;
- `g` and `-g` are gauge-equivalent but their off-diagonal amplitudes are not
  silently identified entry by entry;
- population revival is not promoted to state-vector revival without center,
  parity and vacuum phase alignment;
- a finite Fock block trace/determinant is never promoted to an ordinary
  infinite-dimensional trace or Fredholm determinant;
- source, evaluator, scope, citation, Route tuple, unknown-key and stale-hash
  corruptions are rejected after hash repair where applicable.

## Integrity conclusion

No target table, external data, fitted clock or Route-B input appears.  The
source is naturally quantum, but A0--A3 fail and the overall verdict remains
`ROUTE_A_REJECTED`.  Internal review is not external peer review.
