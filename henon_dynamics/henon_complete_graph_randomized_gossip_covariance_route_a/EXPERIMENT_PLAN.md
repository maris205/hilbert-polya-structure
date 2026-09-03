# Exact evidence plan

## Analytic objects

1. Reconstruct every pair matrix over exact rational arithmetic.
2. Verify pathwise mean preservation and the complete-graph Laplacian sum.
3. Construct the three explicit projectors on centered symmetric matrices.
4. Verify dimensions, orthogonality, completeness, transfer eigenvalues, and
   the distinction between positive-relaxation eigenspaces and the merged
   identity eigenspace at `eta=0`.
5. Compare the closed second moment with exhaustive edge-word averaging.
6. Audit `N=1,2,3` and `eta=0,1/2,1` separately.

## Evidence grid

- `N=1,...,9`;
- `eta` in `0,1/4,1/3,1/2,2/3,3/4,1` for `N>=2`;
- exact projector receipts for `N=3,...,8`;
- exhaustive words through time three for `N=2,...,5` and
  `eta=1/3,1/2,2/3`.

All stored rationals use canonical numerator/denominator strings.  Decimal
tolerance is unnecessary.

## Independent lanes

- the checker does not import the producer;
- SymPy proves the symbolic polynomial identities and checks exact finite
  representations;
- replay runs the producer twice in isolated temporary paths and compares raw
  bytes;
- hostile mutation recomputes the self-hash after semantic attacks;
- every Python entry point explicitly refuses optimized execution;
- the release gate rebuilds each revision twice in fresh directories.

## Claim boundary

The evidence tests the source stochastic dynamics only.  It cannot establish
prime ownership, an orbit zeta, a target determinant, a functional equation,
a target zero match, or a Hilbert--Polya operator.
