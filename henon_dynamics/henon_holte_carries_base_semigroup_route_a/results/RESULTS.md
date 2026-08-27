# C194 results

Status: `RELEASE_COMPLETE` after manifest closure.

## Mathematical result

For every `n>=1` and `b>=2`, the base-`b` carry chain on
`{0,...,n-1}` has Holte's exact transition window, satisfies
`P_aP_b=P_ab`, and is diagonalizable in a base-independent eigenbasis with
spectrum `1,b^-1,...,b^{-(n-1)}`.  Its stationary row is the normalized
Eulerian row.  Therefore all powers, traces and the finite Markov determinant
are explicit, and common spectral projectors give an exact convergence
expansion.

The result is classical and source-attributed.  This package contributes the
scoped theorem/evidence/release certificate, not a novelty claim.

## Exact evidence

- 72 complete `(n,b)` cases for `1<=n<=8`, `2<=b<=10`.
- 1,836 transition cells.
- 504 power-trace rows and 360 convergence rows.
- 392 semigroup tuples and 9,996 semigroup cell equalities.
- 96 power-identity tuples and 2,448 power-identity cell equalities.
- 32 prime-base cases and 40 composite-base controls.
- Independent checker: 24,602 assertions.
- SymPy oracle: 14,248 exact checks.
- Mutation suite: 159 repaired-hash and 1 stale-hash rejection.
- Evidence payload SHA-256:
  `15c02c5b83f6314fef0e3c786f7bdad09feeb1d7a557b7df7bd88db30eb3106f`.
- Evidence-file SHA-256:
  `b165dd9ae0b60009db7c9489d969a6910500bb5aec72fea1ec226cf147e43b18`.

## Route-A result

`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
overall `ROUTE_A_REJECTED`; Route B false.

Positional addition is intrinsic arithmetic, but prime and composite bases
obey the same theorem and provide no rational-prime primitive carrier.  No
target tables, arithmetic local data, Euler factors, root numbers, automorphy,
target divisor, functional equation, counting law or Hilbert--Polya operator is
claimed.
