# Proof Package — HCS-C302

## Claim

For classical single-pivot Quicksort on a uniformly random permutation of
`n` distinct keys, let `X_n` be the number of key comparisons, with
`X_0=X_1=0`.  The cost distribution has an exact probability-generating
polynomial recurrence at every `n`, exact closed mean and variance, and a
centered normalized `L^2` limit.  The limit is the unique centered
finite-variance solution of the Quicksort contraction equation, and its exact
positive third moment proves that it is not Gaussian.

## Status

**PROVABLE AS STATED.**  Frozen obstruction record: `HEN-O286`.

## Frozen model

- The input is a uniformly random permutation of `n` distinct keys.
- The pivot rule is fixed independently of key values, so its rank is uniform
  on `{1,...,n}`.  Equivalently, choose the first key as pivot.
- Partitioning compares the pivot with each of the other `n-1` keys exactly
  once.  Only key comparisons are counted.
- Conditional on pivot rank, the relative orders in the two subarrays are
  independent uniform permutations.

With `I_n` uniform on `{0,...,n-1}` and independent recursive copies,

`X_n = X_(I_n) + X'_(n-1-I_n) + n-1`.                    (1)

## Finite distribution and moments

Let `G_n(z)=E[z^(X_n)]`.  Then `G_0=G_1=1` and, for `n>=2`,

`G_n(z)=z^(n-1)/n sum_(j=0)^(n-1) G_j(z)G_(n-1-j)(z)`.   (2)

Thus every finite law is an exactly computable polynomial with nonnegative
rational coefficients and value one at `z=1`.

Write `H_n=sum_(k=1)^n 1/k` and
`H_n^(2)=sum_(k=1)^n 1/k^2`, with both sums zero at `n=0`.  Then

`mu_n=E X_n=2(n+1)H_n-4n`,                              (3)

`v_n=Var X_n=7n^2-4(n+1)^2 H_n^(2)-2(n+1)H_n+13n`.      (4)

The formulas include `n=0,1`.

## Limiting theorem

Set

`Y_n=(X_n-mu_n)/(n+1)`

and let `U,Y_1,Y_2` be independent, with `U` uniform on `[0,1]` and
`Y_1,Y_2` copies of `Y`.  Then `Y_n` converges in `L^2` (under a suitable
coupling, equivalently in the quadratic Wasserstein metric) and hence in
distribution to the unique centered finite-second-moment solution of

`Y = UY_1+(1-U)Y_2+C(U)`,                                (5)

where

`C(u)=1+2u log u+2(1-u)log(1-u)`,                        (6)

with `0 log 0=0`.  Its first three centered moments are

`E Y=0`,

`E Y^2=7-2 pi^2/3`,

`E Y^3=16 zeta(3)-19>0`.                                 (7)

Consequently the limiting distribution is nondegenerate and non-Gaussian.

## Proof

### 1. Recursive independence and PGFs

Condition on `I_n=j` in (1).  The pivot contributes `n-1`; standardization
of the random permutation makes the two induced relative orders independent
uniform permutations of sizes `j` and `n-1-j`.  Taking `z`-transforms and
averaging the `n` possible ranks proves (2).  Induction proves that each
`G_n` is a probability polynomial.

### 2. Mean and variance

Differentiating (2) at one, or taking expectations in (1), gives

`mu_n=n-1+(2/n)sum_(j=0)^(n-1)mu_j`.                     (8)

Subtract the equation at `n-1` after multiplying by the appropriate index;
the resulting first-order recurrence is solved by (3).  Substitution back
into (8) verifies the boundary cases and closes the induction.

For the variance, the law of total variance gives

`v_n=(2/n)sum_(j=0)^(n-1)v_j
     + Var(mu_(I_n)+mu_(n-1-I_n))`.                       (9)

Insert (3), use the harmonic identities

`sum_(k=1)^n H_k=(n+1)H_n-n`

and their first- and second-order weighted analogues, and subtract
successive versions of (9).  The unique solution with `v_0=v_1=0` is (4).
An independent symbolic lane verifies the unsimplified recurrence through
`n=80`, while the harmonic-sum induction above proves it for every `n`; exact
finite rows verify the endpoint conventions.

### 3. Centered recurrence and contraction

Center (1) using (3), divide by `n+1`, and put
`A_n=(I_n+1)/(n+1)`, `B_n=1-A_n`.  Exactly,

`Y_n=A_n Y_(I_n)+B_n Y'_(n-1-I_n)+C_n(I_n)`,

where

`C_n(j)=[n-1+mu_j+mu_(n-1-j)-mu_n]/(n+1)`.

Couple `I_n=floor(nU)` with one uniform `U`.  Then `A_n->U` uniformly.
The elementary bounds `H_k=log k+gamma+O(1/k)` (with the endpoints evaluated
directly) give `C_n(floor(nU))->C(U)` in `L^2`; also the exact mean recurrence
gives `n^{-1}sum_j C_n(j)=0`.  Thus `E C(U)=0`.

On centered finite-second-moment laws, couple two inputs optimally and use
independent copies in the two branches.  Cross terms vanish, so the
quadratic Wasserstein distance obeys

`d_2(T nu,T nu')^2 <= E[U^2+(1-U)^2] d_2(nu,nu')^2
                    = (2/3)d_2(nu,nu')^2`.               (10)

Hence `T` is a strict contraction and has one fixed centered law `Y`.  On an
iid-uniform binary tree, let `L_v` be the product of branch weights to node
`v` and `Delta_r=sum_(|v|=r)L_v C(U_v)`.  The levels are orthogonal and
`E Delta_r^2=E[C(U)^2](2/3)^r`, so their series converges in `L2`; its root
split realizes the unique fixed law.  On that same tree construct `Yhat_n` by
setting `I_m=floor(m U_v)` at every node of current size `m`; then `Yhat_n`
has the law of `Y_n`.  With
`e_n=||Yhat_n-Y||_2`, subtree centering and Minkowski give

`e_n <= sqrt(Q_n)+delta_n`,

`Q_n=(2/n)sum_(j=0)^(n-1)((j+1)/(n+1))^2 e_j^2`,

where `delta_n->0` is the coefficient/grid-toll error.  Indeed the coefficient
error is `O(1/n)` and the harmonic remainder controls the toll uniformly up to
the continuous modulus of `x log x`.  Formula (4) bounds `Var(Y_n)` uniformly,
so `(e_n)` is bounded.  Put `M_N=sup_(j>=N)e_j`; then
`M_N` decreases to `D=limsup e_n`.  The finitely many `j<N` terms in `Q_n`
have total weighted contribution `O(n^-3)`, while

`(2/n)sum_(j=0)^(n-1)((j+1)/(n+1))^2=(2n+1)/(3(n+1))->2/3`.

Taking the limsup gives `D<=sqrt(2/3)M_N`; then `N->infinity` gives
`D<=sqrt(2/3)D`, forcing `D=0`.  This proves an explicit same-tree `L^2`
coupling and therefore
quadratic-Wasserstein convergence.  Formula (4) also gives the limiting
positive variance in (7).

### 4. Exact moments and non-Gaussianity

Before cubing (5), a third-moment license is required.  On an independent
binary tree put `L_empty=1`, `L_(v0)=L_v U_v`,
`L_(v1)=L_v(1-U_v)`, and

`Delta_r=sum_(|v|=r) L_v C(U_v)`.

The toll `C` is bounded and centered.  Conditional Rosenthal inequality for
the independent centered summands at level `r`, together with

`E sum_(|v|=r)L_v^2=(2/3)^r`,

`E sum_(|v|=r)L_v^3=(1/2)^r`,

and `sum_v L_v^2<=1`, gives

`||Delta_r||_3 <= K[(2/3)^(r/3)+(1/2)^(r/3)]`.

The right side is summable.  Therefore
`sum_r Delta_r` converges in `L^3`, splits at the root to satisfy (5), and is
centered with finite variance.  By `L^2` uniqueness it is the same fixed law
`Y`.  Hence taking its third moment is legitimate.

Square (5), use independence and centering, and evaluate the elementary
integrals of (6).  This gives `E Y^2=7-2pi^2/3`.  Cubing now gives

`m_3=(1/2)m_3
     +3 m_2 integral_0^1 C(u)(u^2+(1-u)^2)du
     +integral_0^1 C(u)^3du`.                             (11)

Beta-function differentiation gives

`integral C(u)(u^2+(1-u)^2)du=1/18`,

`integral C(u)^3du=-32/3+pi^2/9+8 zeta(3)`,

and hence `m_3=16 zeta(3)-19`.  Finally
`zeta(3)>sum_(k=1)^6 k^(-3)=28567/24000` implies
`m_3>67/1500>0`.  A centered Gaussian has third moment zero, so the fixed law
cannot be Gaussian.

## Boundary and collision atlas

- `n=0,1` have zero cost; `n=2` has deterministic cost one.
- Extreme pivots give one empty subproblem and are included in (1)--(2).
- Repeated keys, randomized pivot sampling, three-way partitioning, swaps,
  assignments, recursion depth and wall-clock time are different models.
- The normalization is `n+1`.  Replacing it by `n` for `n>=1` has the same
  weak limit but is not the finite recurrence frozen here.
- C291 also uses a first-event convolution, but its states are jammed dimer
  configurations on paths/cycles; it has no recursive permutation split or
  contraction fixed point.  The C289 idea ledger explicitly reserved
  Quicksort after collision screening.

## Route-A boundary

The strict tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the overall verdict is
`ROUTE_A_REJECTED`.  Input size is not an intrinsic dynamical clock, the
recursion is not a primitive periodic-orbit ledger, finite PGFs are not
target determinants, and the distributional contraction has no same-clock
self-adjoint lift.  No target arithmetic or spectral claim and no Route-B
authorization is made under `NO_BAD_EULER_OR_ROOT_NUMBER`.

Finite coefficient tables, moments and integral identities in the evidence
artifact are exact regression certificates.  The all-`n` recurrence and
limit theorem are analytic.
