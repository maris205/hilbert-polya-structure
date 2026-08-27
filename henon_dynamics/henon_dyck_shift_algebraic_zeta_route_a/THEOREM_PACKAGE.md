# Theorem package

Let `D_N^E` be the edge-type Dyck shift of the graph with one vertex and `N`
loop edges, and let `F_N(n)=|Fix(sigma^n)|` count origin-marked periodic
sequences.  Put `s_N(z)=sqrt(1-4Nz^2)`.

## Main theorem

For every `N>=1`, the context-free circular-code series is the small solution
of `g_N=Nz^2/(1-g_N)`, namely
`g_N=(1-sqrt(1-4Nz^2))/2`, and the source specialization
`zeta_N=(1-g_N)/(1-Nz-g_N)^2` gives

`zeta_N(z)=2(1+s_N(z))/(1+s_N(z)-2Nz)^2`.

For odd `n`,

`F_N(n)=2((N+1)^n-sum_{j=0}^{(n-1)/2} binom(n,j)N^j)`;

for even `n`,

`F_N(n)=2((N+1)^n-sum_{j=0}^{n/2} binom(n,j)N^j)
          +binom(n,n/2)N^(n/2)`.

The least-period point and orbit counts are
`P_N(n)=sum_{d|n}mu(n/d)F_N(d)` and `C_N(n)=P_N(n)/n`.

When `N=1`, `zeta_1(z)=1/(1-2z)` and `F_1(n)=2^n`.  When `N>1`, the unique
dominant positive singularity is a double pole at `1/(N+1)`; the quadratic
branchpoints are `+-1/(2sqrt(N))`, the zeta function is nonrational, and

`F_N(n)=2(N+1)^n+O((2sqrt(N))^n/sqrt(n))`,
`C_N(n)~2(N+1)^n/n`.

For every `N>=1`, `h_top(D_N^E)=log(N+1)`.  Here the entropy identification is
source-locked to Krieger--Matsumoto Proposition 3.1 for Markov-Dyck shifts;
the fixed-count asymptotic supplies the periodic growth rate.

## Proof ledger

The Krieger--Matsumoto circular-code theorem is specialized to the one-vertex
`N`-loop graph; solving its quadratic code equation and substituting gives the
displayed closed zeta.  This is a source specialization, not a priority claim.
Exact coefficient extraction of its logarithmic derivative
gives the parity formulas.  Möbius inversion gives primitive points and orbit
division gives cycles.  Direct substitution proves the `N=1` cancellation.
For `N>1`, the denominator has a simple zero at `1/(N+1)` and is squared,
while its numerator is nonzero.  The inequality `N+1>2sqrt(N)` makes this pole
dominant.  Quadratic conjugation changes the zeta, proving nonrationality; a
geometrically bounded binomial tail proves the stated asymptotics.

Krieger--Matsumoto Proposition 3.1 identifies Markov-Dyck topological entropy
with the exponential rate of periodic points.  Therefore the already-proved
limit `log(F_N(n))/n -> log(N+1)` yields the entropy formula.  No general
periodic-growth-equals-entropy principle is assumed.

For the direct audit, reduce one period to normal form `B A`.  In repeated
periods, only the interface `A B` can create zero.  A mismatch appears at the
first interface; if it does not, unequal lengths produce monotone excess and
equal lengths cancel periodically.  Therefore a forbidden periodic factor
always has a forbidden cyclic subfactor of length at most `2n`.

The registered route record is exactly `overall=ROUTE_A_REJECTED` with
`route_b_invocation_allowed=false`.
