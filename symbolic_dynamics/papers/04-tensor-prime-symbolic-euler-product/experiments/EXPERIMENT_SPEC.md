# Experiment Spec — Opaque Tensor-Atom Recovery

## Claim under test

Within the tensor monoid of finite full shifts, tensor indecomposability,
topological entropy, and the reciprocal Artin--Mazur determinant should be
sufficient to recover the rational-prime Euler ledger without exposing an
integer label or prime table to the recovery algorithm.

## Frozen main registry

- Objects: full shifts `F_1,...,F_N`, exposed through opaque hashed IDs.
- Unit: registered `F_1` ID.
- Operation: the partial table induced by actual Cartesian product
  `F_m tensor F_n = F_mn` whenever `mn <= N`.
- Intrinsic clock: topological entropy `h(F_n)=log(n)`.
- Registered determinant: reciprocal AM polynomial `D_n(z)=1-nz`.
- Consistency observable: fixed-point counts `#Fix(sigma^r)=n^r`, `1<=r<=4`.
- Cutoffs: `N=32,64,128,256`.
- Forbidden candidate inputs: integer labels, prime tables, Riemann zeros,
  fitted phases, and fitted clocks.

The independent verifier may factor integers or test primality only after the
opaque recovery is complete.

## Exact outputs

1. tensor atoms and unique tensor factorizations;
2. coefficients of `prod_a (1-a^-s)^-1`;
3. coefficients of `prod_a (1-a^-s)`;
4. coefficients of `-Z'/Z`;
5. entropy/determinant/fixed-point compatibility errors.

For mass at most `N`, these are exact finite-prefix tests, not estimates: all
proper factors of any registered `n` are themselves registered.

## Controls

1. **Additive alphabet law:** `F_m boxplus F_n = F_(m+n)` with formal unit
   `F_0`.  This has a unique additive atom but fails the entropy norm and its
   sole atom has zero clock.
2. **Matched random atom sets:** 64 deterministic seeds at each cutoff with
   exactly the main system's atom count.
3. **Shifted multiplication:** `m star n=(m-1)(n-1)+1`.  It is a UFD after
   conjugating labels by `n -> n-1`, but is incompatible with the intrinsic
   full-shift entropy, AM determinant, and fixed counts.
4. **Post-hoc shifted clock:** replacing `log n` by `log(n-1)` recovers the
   target exactly and is therefore the explicit `PROVES_TOO_MUCH` witness.
5. **Positive free-mixing grammar:** for each of 28 pairs among the first
   eight atoms, compare isolated self-loops with the freely mixing two-symbol
   full shift.  The latter must produce a spurious mixed term at mass `pq`.

## Pass conditions

- opaque atoms equal all verifier primes through every cutoff;
- unique factorization fraction is one;
- zeta, Möbius, and von Mangoldt prefix coefficients are exact;
- tensor entropy additivity, determinant-norm multiplicativity, and fixed-count
  identities pass;
- random, additive, and intrinsic shifted controls separate;
- every positive free-mixing pair produces coefficient two in `Z` and a
  positive `log(pq)` coefficient in `-Z'/Z`, while isolated atom loops give
  one and zero respectively.

## Reproduction

From the Paper04 project directory:

```bash
python code/exact_tensor_atom_experiment.py --output results
python -m unittest discover -s code -p 'test_*.py' -v
```

The experiment uses only the Python standard library.  Large opaque registry
JSON files are not stored by default; add `--save-registries` for a diagnostic
run outside the shareable result package.
