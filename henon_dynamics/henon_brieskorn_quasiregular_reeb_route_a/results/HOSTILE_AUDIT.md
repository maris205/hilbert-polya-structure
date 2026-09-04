# Hostile audit

The hostile suite first confirms that the unmodified evidence and YAML pass.
It then repairs every declared section and payload hash after semantic
mutations, preventing a stale digest from being the reason for rejection.

## Rejected attacks

- 46 repaired-hash evidence attacks covering identity, baseline, epoch,
  evaluator, YAML binding, parameter domain, contact normalization, Reeb
  speed, determinant and trivialization conventions, theorem contracts,
  collision ownership, references, flags, tuple, Route B, exact scales, pair
  rows, orbit types, rotations, degeneracies, and RS indices;
- 1 stale-hash control;
- 2 malformed JSON controls: duplicate key and nonfinite constant;
- 12 YAML controls: duplicate key, merge, non-string key, anchor/alias,
  implicit date, unknown field, type mutation, authority, status, artifact,
  tuple, and Route-B changes.

Result: `61/61` killed.

## Reviewer attacks closed in prose

1. The common-period index is not inferred from the finite sign table. The
   theorem and paper derive it from the ambient diagonal Maslov contribution
   minus the defining-polynomial normal winding, under a named Milnor-fiber
   capping trivialization and primary citation.
2. Three exceptional circles are not advertised as the complete primitive
   ledger: the two-dimensional principal quotient is explicit.
3. The pre-degeneracy CZ formula is not applied at the first degenerate cover.
4. No contact-homology result is inferred from fixed strata or indices.
5. Integer source weights are not relabeled as rational primes or prime powers.
