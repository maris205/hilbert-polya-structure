# HCS-C307 theorem package

## Frozen process

Let the `K=binom(n,2)` edges of the complete graph be uniformly randomly
permuted.  `G_m` contains the first `m` edges, so it is exactly uniform on the
fixed-size slice `G(n,m)`.  Connectivity is monotone under edge addition and
is therefore absorbing.  Set

`tau_conn=min{m:G_m is connected}`, with `tau_conn=0` for `n=1`.

## Exact finite theorem

Let `C(n,m)` count connected labeled `n`-vertex graphs with `m` edges, set
`C(1,0)=1`, and set all out-of-range counts/binomials to zero.  For `n>=2`,

`C(n,m)=binom(K,m)-sum_{s=1}^{n-1} binom(n-1,s-1)
          sum_j C(s,j)binom(binom(n-s,2),m-j)`.

A disconnected graph is counted exactly once by the component of vertex 1,
which proves the recurrence.  Its support/endpoints are

- `C(n,m)=0` for `m<n-1`;
- `C(n,n-1)=n^(n-2)` by the Prüfer tree code;
- `C(n,K)=1`.

Uniform prefixes and monotonicity give

`F_n(m)=P(tau_conn<=m)=C(n,m)/binom(K,m)`,

`P(tau_conn=m)=F_n(m)-F_n(m-1)` with `F_n(-1)=0`, and

`P(tau_conn>m)=1-F_n(m)`.

For every integer `r>=1`, telescoping each nonnegative integer lifetime gives

`E[tau_conn^r]=sum_{m=0}^{K-1}((m+1)^r-m^r)P(tau_conn>m)`.

A disconnected graph has at most `binom(n-1,2)` edges, so for `n>=2`,

`n-1<=tau_conn<=binom(n-1,2)+1`.

## Gumbel theorem

For fixed real `c`, define

`m_n(c)=floor((n/2)(log n+c))`.

Then

`P(2 tau_conn/n-log n<=c) -> exp(-exp(-c))`.

### Isolated vertices

If `I_n` counts isolated vertices at `m=m_n(c)`, then for every fixed `r`,

write `(x)_{r↓}=x(x-1)...(x-r+1)` for the falling factorial. Then

`E[(I_n)_{r↓}]=(n)_{r↓} binom(binom(n-r,2),m)/binom(K,m)`.

With `D_r=K-binom(n-r,2)=rn-r(r+1)/2`, logarithmic expansion of the ratio
gives `-r(log n+c)+o(1)`.  Hence all fixed factorial moments tend to
`exp(-rc)`, proving `I_n => Poisson(exp(-c))`.

### All other components

Let `X_s` count components of size `s`.  For a fixed `s`-set to be a
component, at least one of its `s^(s-2)` spanning trees must be present and all
`s(n-s)` crossing edges absent.  Exact sampling without replacement yields

`E X_s <= binom(n,s)s^(s-2)(m/K)^(s-1)
 exp{-s(n-s)(m-s+1)/(K-s+1)}`.

For `2<=s<=n/log n`, the exponent is at least
`s(log n-O_c(1))`; after `binom(n,s)<=(en/s)^s`, the geometric ratio is
`O(log n/n)` and its sum from `s=2` is `O_c(log^2 n/n)`.  For
`n/log n<=s<=n/2`, the exponent is at least `s log n/8`, and the remaining
factor is at most `n(C log n)^s`; that geometric tail also vanishes.  Thus a
disconnected graph with no isolated vertex has probability `o(1)`.

It follows that connectivity at `m_n(c)` has probability
`P(I_n=0)+o(1)->exp(-exp(-c))`.  Since the lifetime is integer, its normalized
event is exactly the prefix event at the displayed floor.

## Boundary and nonclaims

- `n=1`: `tau_conn=0`; `n=2`: `tau_conn=1`.
- `m=0` and `m=K` are included in the exact CDF.
- For fixed `c`, the window index is in `[0,K]` for all sufficiently large
  `n`; clipping is only a finite software convention.
- The finite process is without replacement.  `G(n,p)` is not substituted.
- No equality with the last-isolated stopping time is claimed.
- The Gumbel conclusion is weak convergence; unbounded-moment convergence is
  not claimed.

The evidence covers all 298 exact cells through `n=12`, four moments per row,
33,867 exhaustive masks through `n=6`, and 60 isolated-factorial diagnostics.
It is regression evidence only.

## Repository collision boundary

- C301 is a parallel fair-bit partition-refinement birthday process, whereas
  C307 grows a simple graph without replacement and stops at connectivity.
- C291 is random greedy dimer adsorption on finite paths and cycles, whereas
  C307 adds unused complete-graph edges and has an absorbing connectivity
  upper set.
- C276 samples a whole uniform random mapping and studies its functional
  graph, whereas C307 evolves simple graphs one edge at a time and closes exact
  connected-graph counts.

Thus none of C301, C291, or C276 owns C307's edge-reveal clock, exact
connectivity-hitting law, or Gumbel connectivity window.

Route-A tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
rejected; Route B is false.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER` with every
target-arithmetic flag false.
