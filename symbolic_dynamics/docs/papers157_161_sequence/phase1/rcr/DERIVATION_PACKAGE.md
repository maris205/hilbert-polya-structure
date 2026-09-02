# RCR focused derivation package

**Candidate:** random anchored-rectangle contraction (`RCR`)  
**Mathematical status:** `PROVABLE AS STATED`  
**Owner status:** `OWNER_AMBER / SPECIALIST CHECK REQUIRED`  
**External status:** `HOLD_EXTERNAL`

No paper number is assigned here.  This is a theorem/proof freeze candidate,
not a manuscript or a release decision.

## 1. Target statement

For integers `a,b>=1`, start from the anchored lattice rectangle
`[1,a] x [1,b]`.  From the current state `(x,y)`, choose `I` uniformly in
`[1,x]` and `J` independently and uniformly in `[1,y]`, and replace the state
by `(I,J)`.  The target package is:

1. a boundary-complete exact law for the one-coordinate absorption time,
   including its PGF, independent-geometric representation, distribution,
   mean, variance, and sharp tail;
2. a boundary-complete exact law for the rectangle absorption time, including
   its CDF, finite rational PGF, first two moments, support, and sharp tail;
3. independently of the absorption clock, an every-time/every-target
   transition atlas and an every-target discounted potential, Green kernel,
   visit probability, and first-hit transform.

All infinite statements below are deductive.  The exact program is only
finite counterexample pressure.

## 2. Status

The formulas in Sections 7--12 have complete derivations and boundary cases.
The owner audit found a direct owner for the **strict embedded one-dimensional
descent chain**, so the earlier scouting label `OWNER_THIN` is tightened to
`OWNER_AMBER`.  The literal rectangle update was not found in the bounded
search, but that non-hit is not novelty, priority, ownership, or release
clearance.

## 3. Invariant object

The decisive invariant object is the lower-triangular resolvent of the
one-coordinate chain.  Its diagonal eigenvalues are `1,1/2,...,1/m`, and its
entries admit an explicit partial-fraction basis.  The two-dimensional chain
is the literal tensor product of two such coordinate kernels because a
uniform cell has independent uniform coordinates.

This one object supports two genuinely different observables:

- the absorption clock, obtained from the `(1,1)` coordinate; and
- the spatial occupation atlas, obtained from every target `(i,j)`.

The second observable is not recoverable merely from the law of the clock.

## 4. Assumptions

- All rectangle side lengths and coordinate states are positive integers.
- The two coordinates selected at each epoch are independent conditional on
  the current rectangle; selections at different epochs use fresh randomness.
- Time starts at zero.  Thus a chain started at its absorbing state has
  absorption time zero.
- Visits count the state occupied at integer times, including time zero.
- A Green count is stopped before rectangle absorption.  For a transient
  target this equals its unrestricted total occupation; the absorbing target
  is handled separately.
- `Geom0(p)` denotes the number of failures before the first success:
  `P(Z=q)=p(1-p)^q`, `q>=0`.

## 5. Notation

Let `X_0=m` and

```text
P(X_(t+1)=k | X_t=x) = 1/x,       1<=k<=x.
```

Write

```text
H_m = inf{t>=0 : X_t=1},
g_m(z) = E_m[z^H_m],
h_n = sum_(q=1)^n 1/q,
h_n^(2) = sum_(q=1)^n 1/q^2.
```

The lower-case `h_n` is reserved for harmonic numbers; it removes the
scouting ambiguity in which `H` denoted both a hitting time and a harmonic
number.

For `m>=2` and `2<=r<=m`, put

```text
A_(m,r) = (-1)^(r-2) binom(m-1,r-1).
```

For `1<=k<=r<=m`, put

```text
C_(m,k;r)
 = (-1)^(r-k) (m-1)! / [(k-1)!(r-k)!(m-r)!].       (5.1)
```

Empty sums are zero and empty products are one.  In particular, every
formula below has an explicit `m=1`, `a=1`, or `b=1` interpretation.

## 6. Derivation strategy

1. Solve the one-step PGF equation by introducing the cumulative sum
   `S_m=sum_(j<=m)g_j`.
2. Read the independent-geometric representation from the product PGF and
   take partial fractions to obtain the exact CDF and PMF.
3. Solve the full one-coordinate resolvent, then extract its transition
   coefficients `C_(m,k;r)`.
4. Use pathwise coordinate independence to identify rectangle absorption as
   a maximum and multiply the coordinate CDFs.
5. Sum the finite exponential tail for the rectangle PGF and moments.
6. Tensor the one-coordinate transition atlas and sum over time for every
   spatial target.  A no-return dwell argument converts occupation into visit
   probability.

## 7. Derivation map

| target | input | transformation | output | independent check |
|---|---|---|---|---|
| one-dimensional clock | first-step equation | cumulative-product recursion | exact rational PGF | direct Bellman solve |
| distribution | product PGF | partial fractions / tail difference | exact CDF and PMF | literal finite law |
| geometric representation | factored PGF | uniqueness of PGFs | independent `Geom0` sum | exact convolution |
| rectangle clock | conditional coordinate independence | product CDF / tail inclusion-exclusion | CDF, PGF, moments, tail | literal 2D kernel |
| target atlas | one-coordinate resolvent | partial fractions and tensor product | all `t,(i,j)` transitions | literal 2D kernel |
| Green/visit law | target atlas | geometric series and target dwell | every-target potential and hit transform | independent Bellman resolvent |

## 8. Scouting-formula audit

The four mathematical assertions printed in the frozen stochastic scouting
package were rederived before extending them.

| scouting assertion | focused verdict | clarification |
|---|---|---|
| `g_m(z)=z(m-1)!/prod_(r=2)^m(r-z)` | correct for `m>=2` | `g_1(z)=1`; expectation is analytic for `|z|<2`, with rational continuation away from poles |
| one positive geometric plus `m-2` zero-based geometrics | correct | the convention-free form is `H_m =_d 1+sum_(r=2)^m Z_r` with `Z_r~Geom0((r-1)/r)` independent |
| `E H_m=1+H_(m-1)` | correct | the harmonic number is renamed `h_(m-1)` to avoid collision with the hitting-time symbol |
| one-dimensional Green row `0,k/(k-1),1/(k-1)` | correct for transient `k>=2` | target `1` has visit probability one, killed-before-hit Green zero, and infinite ordinary occupation |
| rectangle clock is `max(H_a,H_b)` | correct pathwise under the coordinate construction | `H_a,H_b` are independent and `H_1=0` |
| transition atlas factorizes | correct | the full coefficients and all boundary cases are supplied below |

The pilot values also recheck exactly:

```text
P_(4,3)(T<=4) = 3360875/4478976,
E H_5 = 37/12,
(G(5,k):2<=k<=5) = (1,1/2,1/3,5/4).
```

No frozen scouting file is edited.

## 9. One-dimensional clock

### 9.1 PGF

First-step conditioning gives `g_1(z)=1` and, for `m>=2`,

```text
g_m(z) = (z/m) sum_(j=1)^m g_j(z).
```

With `S_m=sum_(j=1)^m g_j`, isolate the self term:

```text
g_m(z) = z S_(m-1)/(m-z),
S_m     = m S_(m-1)/(m-z),
S_1     = 1.
```

Therefore

```text
g_m(z) = z (m-1)! / prod_(r=2)^m (r-z),       m>=2.     (9.1)
```

This is an identity of formal power series and a probability transform for
`|z|<2`.  Its displayed quotient is the meromorphic continuation.

### 9.2 Independent-geometric representation

For independent variables

```text
Z_r ~ Geom0((r-1)/r),
P(Z_r=q)=(r-1)/r^(q+1),
E[z^Z_r]=(r-1)/(r-z),                         (9.2)
```

the product of the PGFs in (9.2), with one deterministic initial step, is
exactly (9.1).  Hence

```text
H_1=0,
H_m =_d 1 + sum_(r=2)^m Z_r,                  m>=2.     (9.3)
```

In particular one may construct the laws so that
`H_(m+1)=H_m+Z_(m+1)` with the increment independent of `H_m`.

### 9.3 Exact distribution

Partial fractions, or equivalently the `(m,1)` transition coefficient in
Section 10, give for all integers `t>=0`

```text
P(H_m>t) = sum_(r=2)^m A_(m,r) r^(-t),        m>=2,     (9.4)
P(H_m<=t)=1-sum_(r=2)^m A_(m,r) r^(-t).                  (9.5)
```

For `m=1`, the survival probability is zero and the CDF is one.  Differencing
(9.4) gives, for `m>=2` and `t>=1`,

```text
P(H_m=t)
 = (m-1) sum_(r=2)^m
   (-1)^(r-2) binom(m-2,r-2) r^(-t).          (9.6)
```

The mass is zero for `t<=0`; in particular `P(H_m=1)=1/m`.

### 9.4 Moments and sharp tail

From (9.3),

```text
E H_m   = 1+h_(m-1),
Var H_m = h_(m-1)+h_(m-1)^(2),                m>=2.     (9.7)
```

The `r=2` coefficient in (9.4) is `m-1`, while every other base is strictly
smaller than `1/2`.  Thus

```text
lim_(t->infinity) 2^t P(H_m>t) = m-1,         m>=2.     (9.8)
```

Consequently the PGF has exact radius two for every `m>=2`.

## 10. One-dimensional transition and target resolvents

For every `m>=k>=1` and `t>=0`,

```text
p_t(m,k) := P_m(X_t=k)
          = sum_(r=k)^m C_(m,k;r) r^(-t).      (10.1)
```

The corresponding discounted occupation is

```text
U_(m,k)(z) := sum_(t>=0) p_t(m,k) z^t
 = 0,                                                   m<k,
 = k/(k-z),                                             m=k,
 = z(m-1)! / [(k-1)! prod_(r=k)^m(r-z)],                m>k.    (10.2)
```

Equivalently, throughout its disk of convergence,

```text
U_(m,k)(z)=sum_(r=k)^m C_(m,k;r)/(1-z/r).       (10.3)
```

For the first hitting time `tau_k`, strong Markov factorization at `tau_k`
gives, when `m>k`,

```text
E_m[z^tau_k ; tau_k<infinity]
 = z(m-1)!/[k! prod_(r=k+1)^m(r-z)].            (10.4)
```

Thus

```text
P_m(tau_k<infinity)=1/k,
(tau_k | tau_k<infinity) =_d
   1+sum_(r=k+1)^m Z_r.                          (10.5)
```

For `m=k`, the hit probability is one and `tau_k=0`; for `m<k`, it is zero.
For transient `k>=2`, the Green count through all times is

```text
G_1(m,k)=0             if m<k,
         k/(k-1)       if m=k,
         1/(k-1)       if m>k.                  (10.6)
```

Indeed, once level `k` is reached, its consecutive dwell has mean
`k/(k-1)` and the chain can never return after leaving it.  The absorbing
target `k=1` has hit probability one, killed-before-hit Green zero, and
infinite ordinary occupation.

## 11. Rectangle absorption time

Let the coordinate chains be `A_t,B_t` and define

```text
T_(a,b)=inf{t>=0:(A_t,B_t)=(1,1)}.
```

Using the same coordinate randomness that defines the rectangle update,

```text
T_(a,b)=max(H_a,H_b)                                  (11.1)
```

pathwise, where the two coordinate hitting times are independent.  Set
`F_m(t)=P(H_m<=t)` and `F_m(-1)=0`.  Then, for `t>=0`,

```text
P(T_(a,b)<=t)=F_a(t)F_b(t),                            (11.2)
P(T_(a,b)=t)=F_a(t)F_b(t)-F_a(t-1)F_b(t-1).            (11.3)
```

Since `P(T>t)=P(H_a>t)+P(H_b>t)-P(H_a>t)P(H_b>t)`, the
finite rational PGF is

```text
E[z^T] = 1+(z-1) [
  sum_(r=2)^a A_(a,r)/(1-z/r)
 +sum_(s=2)^b A_(b,s)/(1-z/s)
 -sum_(r=2)^a sum_(s=2)^b A_(a,r)A_(b,s)/(1-z/(rs))
].                                                     (11.4)
```

For a nonabsorbing start, (11.4) is a PGF for `|z|<2` and has exact radius
two; for `(a,b)=(1,1)` it is the constant one.  Its rational continuation is
understood away from displayed poles.

The first two raw moments follow by summing the tail:

```text
E T =
  sum_r A_(a,r) r/(r-1)
 +sum_s A_(b,s) s/(s-1)
 -sum_(r,s) A_(a,r)A_(b,s) rs/(rs-1),                 (11.5)

E T^2 =
  sum_r A_(a,r) r(r+1)/(r-1)^2
 +sum_s A_(b,s) s(s+1)/(s-1)^2
 -sum_(r,s) A_(a,r)A_(b,s) rs(rs+1)/(rs-1)^2.         (11.6)
```

The same empty-sum convention covers a unit side.  Sharp consequences are:

```text
T_(a,b)=0 almost surely  iff  (a,b)=(1,1);
P(T_(a,b)=1)=1/(ab)      for every nonabsorbing start;
support(T_(a,b))={1,2,...} for every nonabsorbing start;
lim 2^t P(T_(a,b)>t)=a+b-2;
max(E H_a,E H_b) < E T_(a,b) < E H_a+E H_b,            (11.7)
```

where the strict mean inequalities in (11.7) require `a,b>=2`.  If one side
is one, `T` is exactly the other coordinate clock and both relevant boundary
equalities hold.

## 12. Every-target spatial potential

Coordinate independence and (10.1) give, for every accessible target
`1<=i<=a`, `1<=j<=b` and every `t>=0`,

```text
P^t_((a,b),(i,j))
 = p_t(a,i)p_t(b,j)
 = sum_(r=i)^a sum_(s=j)^b
   C_(a,i;r) C_(b,j;s) (rs)^(-t).              (12.1)
```

If `i>a` or `j>b`, the target is inaccessible and every expression below is
zero.  The discounted every-target potential is

```text
U_((a,b),(i,j))(z)
 = sum_(t>=0) z^t P^t_((a,b),(i,j))
 = sum_(r=i)^a sum_(s=j)^b
   C_(a,i;r) C_(b,j;s) / (1-z/(rs)).            (12.2)
```

Equation (12.2) first holds in its disk of convergence and then as a rational
identity.  If `(i,j)!=(1,1)`, it may be evaluated at `z=1`; every occurrence
then precedes absorption, and the Green kernel is

```text
K_((a,b),(i,j))
 = sum_(r=i)^a sum_(s=j)^b
   C_(a,i;r) C_(b,j;s) / (1-1/(rs)).            (12.3)
```

At a transient target `(i,j)`, the self-loop probability is `1/(ij)`.  Once
the process leaves that target it can never return, so its mean dwell,
including the arrival time, is `ij/(ij-1)`.  Therefore its visit probability
and defective first-hit PGF are

```text
P_((a,b))(tau_(i,j)<infinity)
  = (ij-1)/(ij) K_((a,b),(i,j)),                 (12.4)

E_((a,b))[z^tau_(i,j);tau_(i,j)<infinity]
  = (1-z/(ij)) U_((a,b),(i,j))(z).               (12.5)
```

Starting at a transient target gives `K=ij/(ij-1)`, hit probability one, and
first-hit time zero.  For target `(1,1)`, hit probability is one and the
killed-before-absorption Green is zero; the ordinary occupation is infinite.
For `|z|<1`, its discounted potential is instead

```text
U_((a,b),(1,1))(z)=E[z^T_(a,b)]/(1-z).           (12.6)
```

Equations (12.1)--(12.6) are the independent spatial theorem axis.

## 13. Remarks and consistency checks

- `E T_(4,3)=32927/9240` and
  `E T_(4,3)^2=689023681/42688800`.
- From start `(4,3)`, selected Green values are
  `K(1,2)=841/1540`, `K(2,2)=163/770`,
  `K(3,2)=213/1540`, and `K(4,3)=12/11`.
- The alternating sums in (9.4), (10.1), and (12.3) are exact rational
  expressions.  Their probabilistic derivations prove nonnegativity; no
  termwise sign claim is made.
- Symmetry under exchanging the two axes is literal and is visible in every
  rectangle formula.

## 14. Boundaries and nonclaims

The package proves nothing about continuous rectangles, nonuniform cell
weights, more than two coordinates, moving anchors, noisy observations,
quasi-stationarity, scaling limits, cover times, or optimal control.  It does
not claim that the finite rational forms are reduced at every parameter or
that a bounded owner-search miss establishes novelty.

## 15. Risks and required next gate

1. Ross's strict uniform descent and Durrett's independent-visit treatment
   own the embedded skeleton and much of the harmonic/visit mechanism.
2. Independent-geometric factorizations, maxima of independent clocks,
   tensor kernels, first-step equations, and finite resolvents are generic
   zero-credit tools.
3. What remains potentially distinctive is only the literal anchored-
   rectangle packaging with the complete two-dimensional clock plus
   every-target potential.  A specialist must decide whether that conjunction
   clears the paper-level contribution threshold.
4. Until then this package remains `OWNER_AMBER / HOLD_EXTERNAL`.
