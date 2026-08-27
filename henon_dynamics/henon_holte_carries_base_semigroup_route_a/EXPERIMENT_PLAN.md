# C194 exact regression plan

## Purpose

Finite calculations test two independent implementations of the classical
all-parameter theorem.  They are not used to infer its infinite quantifiers.

## Frozen census

- `1<=n<=8`, `2<=b<=10`: 72 complete transition matrices and 1,836 cells.
- Every case: Eulerian stationary row, simple spectral list, characteristic
  polynomial, `det(I-zP_b)`, powers `0..6`, and five exact convergence rows.
- `1<=n<=8`, `2<=a,b<=8`: 392 semigroup tuples and 9,996 cell equalities.
- 96 independent `P_b^r=P_(b^r)` sentinels and 2,448 cell equalities.
- Prime-base cases: 32; composite-base cases: 40.

## Independent algorithms

1. Producer: convolution of the `n` digit-sum polynomials.
2. Checker: the `(n+1)`-variable slack coefficient evaluated by
   inclusion--exclusion; Eulerian numbers are enumerated from permutations;
   characteristic coefficients use Faddeev--LeVerrier.
3. SymPy: direct matrix characteristic polynomials, determinants, ranks,
   stationary equations, power traces and low-base semigroup products.
4. Replay: isolated producer execution and byte equality.
5. Mutation: repaired canonical hashes for semantic attacks plus one stale-hash
   attack.

## Gates

- Exact source/evaluator/scope maps must match, not merely contain expected
  substrings.
- Every transition row must sum to one.
- All stationary, trace, determinant, semigroup, power and convergence rows
  must reconstruct independently.
- Prime/composite tags cannot change the theorem.
- Every forbidden-claim flag remains false.
- Three substantive paper rounds must have distinct PDF hashes, and the final
  must be a deterministic fixed-epoch XeLaTeX build with embedded fonts and a
  clean log.

Any failure blocks release rather than weakening the theorem to selected
examples.
