# HCS-P73 proof package

## 1. Frozen input and full complex divisor

Put

    Phi(x) = 2x/(1-2x^2),
    c_m = (1/m) product_(p|m, p odd) (1-p),
    L(t) = sum_(m>=2) c_m Phi(t^m).

P72 proves, on compact subsets of the unit disk avoiding its poles,

    log C_rel(t) = H_rel(1-sqrt(2)t) - L(t),

where

    H_rel(u) = -(1/2)log(2-u)-3(2u-3)/[4(u-2)].

For `m>=2` define

    rho_m = 2^(-1/(2m)),
    alpha_(m,k) = rho_m exp(pi i k/m),  0<=k<2m,
    b_(m,k) = c_m (-1)^k/(sqrt(2)m).

The points `alpha_(m,k)` are precisely the roots of `1-2t^(2m)`.  Different
levels have different moduli because `rho_m` is strictly increasing, so no
pole belongs to two levels.

## 2. Exact partial fractions

For every `m>=2`,

    c_m Phi(t^m)
      = sum_(k=0)^(2m-1) b_(m,k)/(1-t/alpha_(m,k)).       (2.1)

Indeed, at `alpha=alpha_(m,k)` the local coordinate `v=1-t/alpha`
gives

    Phi(t^m) = (-1)^k/[sqrt(2)m v] + O(1).

Thus both sides of (2.1) have the same simple principal parts.  Their
difference is entire on the Riemann sphere and vanishes at infinity, hence is
zero.  Equivalently, expansion at zero uses

    sum_(k=0)^(2m-1) exp(pi i (m-j)k/m) = 0

unless `j` is congruent to `m` modulo `2m`, reproducing exactly the
coefficients `c_m 2^(ell+1)` in degrees `m(2ell+1)`.

## 3. The raw pole family fails

Before levelwise grouping, the absolute mass of the raw right side of (2.1)
at `t=0` is

    sum_(k=0)^(2m-1) |b_(m,k)| = sqrt(2)|c_m|.

For every odd prime `p`, `|c_p|=(p-1)/p>=2/3`.  Since there are infinitely
many odd primes, the double series of raw pole terms is not absolutely
summable even at the origin.  It may be summed only after imposing the
channel grouping, so arbitrary pole ordering is invalid.

## 4. Genus `m-1` regularization

Define the regularized pole term

    R_(m,k)(t) = b_(m,k) [ 1/(1-t/alpha_(m,k))
                          - sum_(j=0)^(m-1)(t/alpha_(m,k))^j ]
                = b_(m,k) (t/alpha_(m,k))^m
                  /(1-t/alpha_(m,k)).                    (4.1)

This is the logarithm of the genus-`m-1` exponential pole factor.  For every
`0<=j<m`, root orthogonality gives

    sum_(k=0)^(2m-1) b_(m,k) alpha_(m,k)^(-j) = 0.

Consequently the subtracted polynomials cancel levelwise and

    sum_(k=0)^(2m-1) R_(m,k)(t) = c_m Phi(t^m).           (4.2)

Let `K` be a compact subset of the unit disk with all `alpha_(m,k)` removed.
Choose `r<q<1` with `|t|<=r` on `K`.  Since `rho_m` increases to one, for all
large `m` one has `|t/alpha_(m,k)|<=q` uniformly on `K`.  From (4.1),

    sum_k |R_(m,k)(t)|
      <= sqrt(2)|c_m| q^m/(1-q)
      <= sqrt(2) q^m/(1-q).

The geometric majorant is summable.  The finitely many earlier levels are
bounded on `K`, proving absolute normal convergence of

    sum_(m>=2) sum_(k=0)^(2m-1) R_(m,k)(t).

It follows from (4.2) that this double sum equals `L(t)`.  Absolute normal
convergence also proves independence under every enumeration of the
individual complex poles, not merely permutations of whole channels.

## 5. Exact normalized all-channel counterterm

Write

    w = 1+sqrt(2)t = 2-u.

The P72 regular part becomes

    H_rel(u) = 3/(4w) - (1/2)log w - 3/2.                (5.1)

On any simply connected slit subdomain carrying compatible square-root and
logarithm branches, define

    K_all(t) = exp(3/2) w^(1/2) exp(-3/(4w))
               product_(m>=2) product_(k=0)^(2m-1)
               exp(R_(m,k)(t)).                          (5.2)

The product in (5.2) is well defined, locally uniform, nonzero, and
independent of the ordering of its pole factors.  Sections 4 and 5.1 give

    log K_all(t) = 3/2 + (1/2)log w - 3/(4w) + L(t).

Combining this identity with P72 proves

    K_all(t) C_rel(t) = 1.                               (5.3)

The source factor in (5.2) is indispensable: P71 cancels the positive
first-channel boundary, but (5.1) retains an exponential and square-root
singularity at the negative point `w=0`.  The factor `exp(3/2)` fixes the
base-point normalization; indeed `K_all(0)=exp(3/4)` and
`C_rel(0)=exp(-3/4)`.

## 6. Claim boundary

**PROVED:** the full complex pole divisor; exact partial fractions; failure
of the raw unordered pole family; genus-`m-1` regularization; absolute normal
convergence; arbitrary pole-order independence; and exact normalized
all-channel cancellation.

**NOT CLAIMED:** a transfer operator, a self-adjoint operator, rational-prime
or prime-power semantics, a von-Mangoldt amplitude, or an explicit formula.
The counterterm copies the complete scalar-channel ledger it cancels.  Route
B remains unauthorized.
