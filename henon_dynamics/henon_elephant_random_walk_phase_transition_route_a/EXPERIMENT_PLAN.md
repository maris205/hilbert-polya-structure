# Experiment plan

## Claims under test

1. The position is a sufficient state for the next-step kernel even though the increment process has full memory.
2. The first and second moments agree with the product formulas, including the harmonic critical branch.
3. The normalized drift is exactly martingale-zero, with a separate `p=0` normalization.
4. Direct enumeration of histories agrees with position dynamic programming.
5. The recorded superdiffusive moment constants agree with independent symbolic simplification.

## Frozen grid

- `p = 0,1/4,1/2,2/3,3/4,4/5,1` and `q = 0,1/4,1/2,3/4,1`.
- Every position law from `n=1` through `n=14`.
- Martingale identities through `n=10` on every parity-compatible state.
- Four direct history enumerations through `n=8`.
- Limit moments at `p=4/5,7/8,1` and `q=0,1/2,1`.

## Acceptance gates

The producer must replay byte-for-byte. The independent checker must not import producer code and must reconstruct every fixed row. JSON and YAML reject duplicates, nonfinite values, aliases, and unauthorized semantics. SymPy checks a disjoint identity basis. Repaired-hash mutations and optimized Python must fail. Three manuscript rounds must build twice identically, without warnings, with embedded subset fonts.
