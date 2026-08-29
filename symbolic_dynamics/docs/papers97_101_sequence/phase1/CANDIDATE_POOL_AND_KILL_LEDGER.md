# Papers 97–101 candidate pool and kill ledger

Evidence cutoff: 2026-08-29 UTC. Route: **A / Symbolic Dynamics**.
External release: **HOLD**.

This round began from the P1–P96 collision firewall and used a two-probe
patience budget.  A candidate advanced only when an exact first calculation
exposed a theorem-sized mechanism, a second independent calculation
preserved it, and a bounded owner search left a residual statement after
explicit subtraction.  Search absence is recorded only as
`BOUNDED_NO_EXACT_COLLISION_FOUND`; it is never a claim of worldwide novelty.

## Frozen five-paper sequence

| ID | Dynamical system | Concrete residual advance | Gate |
|---:|---|---|---|
| P97 | nonempty subsets of `F_p` under `A -> A+A` | complete recurrent set and zeta; exact cardinality-layer absorption depth; first-period anomaly recovers `p` and `ord_p(2)` | `GO_OWNER_SUBTRACTED_ADDITIVE_COMBINATORICS` |
| P98 | equal adjacent `r`-block-sum shift over `F_q` | global recurrence normal form; characteristic-`p` torsion staircase for every fixed count; zeta and orbit census | `GO_OWNER_SUBTRACTED_ALGEBRAIC_SHIFT` |
| P99 | index-`N` sublattices of `Z^2` under a unipotent shear | complete HNF cycle decomposition, fixed counts and finite zeta; prime-power valuation staircase and parameter recovery | `GO_OWNER_SUBTRACTED_SUBGROUP_COUNTING` |
| P100 | least-significant-nonzero-digit erasure on `Z/p^r Z` | exact digit-sum hitting time, full transient profile, sharp depth, moments, local limit and `(p,r)` recovery | `GO_OWNER_SUBTRACTED_DIGIT_SUM` |
| P101 | iid floor/cap maps of the interval with atomless thresholds | interval-or-constant normal form; exact distribution-free synchronization law; critical tail prefactor and quenched/annealed separation | `GO_OWNER_SUBTRACTED_MONOTONE_RDS` |

## Diversity ledger

| Field | P97 | P98 | P99 | P100 | P101 |
|---|---|---|---|---|---|
| phase space | finite power set | finite algebraic subshift | finite Hecke/HNF lattice set | finite local ring | compact interval under random maps |
| action | nonlinear Minkowski self-sum | deterministic shift | unimodular group action | deterministic absorbing map | iid semigroup cocycle |
| headline invariant | recurrent core and absorption layers | torsion-resonant fixed sequence | cycle lengths and zeta | transient-depth polynomial | synchronization-time law |
| proof engine | Cauchy–Davenport plus doubling order | polynomial gcd with repeated roots | Hermite normal form | base-`p` digit conjugacy | order statistics and semigroup normal form |

No selected pair shares both its state object and proof engine.  P97 and the
immediately preceding P96 both use finite subsets, but P96 is a pointwise
hyperspace lift of circle expansion whereas P97 is a nonlinear binary set
operation whose iterates are growing sumsets.  P98 is the only selected
shift of finite type.  P99 and P100 are both arithmetic finite systems, but
one is a bijective lattice action and the other a noninvertible digitwise
absorber.

## Frozen early signals

### P97 — sumset squaring

For an odd prime `p`, let `Phi(A)=A+A` on nonempty subsets of `F_p` and put
`h=ord_p(2)`.  Iteration gives `Phi^t(A)=2^t A`, where the right side is an
iterated sumset.  Every set of size at least two reaches `F_p`; the recurrent
points are `F_p`, `{0}`, and the nonzero singletons.  Therefore

```text
Fix(Phi^n) = 2 + (p-1) 1_{h|n},
zeta_Phi(z) = (1-z)^(-2) (1-z^h)^(-(p-1)/h).
```

On the layer `|A|=m>=2`, Cauchy–Davenport and an arithmetic-progression
extremizer give the exact worst absorption depth

```text
ceil(log_2((p-1)/(m-1))).
```

Literal power-set enumeration and the independent additive-growth proof
agree for `p=3,5,7,11,13`.

### P98 — equal adjacent block sums

Let `X_(q,r)` contain the two-sided `F_q` sequences satisfying

```text
sum_{j=0}^{r-1} x_{i+j} = sum_{j=r}^{2r-1} x_{i+j}
```

at every `i`.  This is the finite companion system annihilated by

```text
f_r(z)=(z^r-1)^2/(z-1)
```

and has `q^(2r-1)` points.  Write `char(F_q)=p`,
`r=p^a r_0`, `n=p^b n_0`, with `p` prime to `r_0 n_0`, and
`g=gcd(r_0,n_0)`.  The first signal is the repeated-root formula

```text
D_r(n)=min(2p^a-1,p^b)+(g-1)min(2p^a,p^b),
Fix(sigma^n)=q^D_r(n).
```

Polynomial-gcd degrees and literal recurrence matrices agree for four
characteristics, all `r<=8`, and all `n<=12` in the discovery spike.

### P99 — unipotent shear on fixed-index lattices

For `U=[[1,1],[0,1]]`, act on index-`N` sublattices of `Z^2`.  In unique HNF
coordinates `L_(a,b,c)=<(a,0),(b,c)>`, `ac=N`, `0<=b<a`, the action is

```text
(a,b,c) -> (a,b+c mod a).
```

The `a`-layer has `gcd(a,c)` cycles of length `a/gcd(a,c)`.  Consequently

```text
Fix(T_N^t)=sum_{a|N, a|tN/a} a,
zeta_T(z)=prod_{a|N}(1-z^(a/gcd(a,N/a)))^(-gcd(a,N/a)).
```

HNF enumeration and an independent stabilizer calculation passed 10,200
exact checks for `N<=100` and `t<=2N`.

### P100 — least-valuation digit erasure

On `Z/p^r Z`, put `E(0)=0` and

```text
E(x)=x-p^v_p(x)  (x != 0).
```

Each step decreases the least significant nonzero base-`p` digit without a
borrow.  Thus the absorption time is exactly the digit sum and

```text
sum_x u^tau(x)=(1+u+...+u^(p-1))^r.
```

This yields the exact maximum, symmetry, unimodality, mean, variance, CLT,
local limit, and recovery of `(p,r)` from the profile.  Digit conjugacy and a
separate layer recurrence passed 1,061,987 orbit checks and 28 profile
identities in the discovery spike.

### P101 — random floor/cap interval maps

At each time choose a floor `x -> max(x,U)` with probability `p` or a cap
`x -> min(x,U)` with probability `1-p`, with iid atomless thresholds.  Until
collapse, every product is a clamp to `[A_t,B_t]`; collapse occurs when a
floor threshold crosses a cap threshold.  If `T` is the first constant
product, exact threshold-order cancellation gives

```text
P(T>t)=sum_{ell=0}^t p^ell(1-p)^(t-ell),
E[z^T]=p(1-p)z^2/((1-pz)(1-(1-p)z)).
```

Hence `T` is a sum of independent geometric variables with parameters `p`
and `1-p`; at `p=1/2` its tail is `(t+1)2^(-t)`.  For uniform thresholds the
mean image diameter is `P(T>t)/(t+1)`.  Enumeration of update words and of
all threshold orders gives two independent exact controls through `t=8`.

## Killed or reserved candidates

| Candidate | Decision | Reason |
|---|---|---|
| full transformation monoid squaring | `KILL_FIREWALL_OWNER_RISK` | attractive fixed formulas reduce to generic functional-digraph census, explicitly excluded this round; transformation-semigroup index/period owners are close |
| graph squaring | `RESERVE_DIRECT_BACKGROUND` | Bell attractor and diameter depth are exact, but graph powers and graph-operator dynamics own most of the mechanism |
| Jordan subspace closure `U -> U+NU` | `RESERVE_CONTROL_OWNER` | basin counts are exact, but the map is the standard reachable-subspace algorithm and the one-block result is too thin |
| projective-line unipotent action over `Z/p^r` | `RESERVE_INTERNAL_P99` | complete zeta exists, but it shares the unipotent valuation-stabilizer engine with P99 |
| cyclic-subgroup compression `H -> pH` | `RESERVE_INTERNAL_P100` | exact rooted tree, but it would add a second local-ring absorber |
| uniform codimension-one projection product | `RESERVE_BATCH_DIVERSITY` | exact pure-death law is strong; held to avoid a second random information-loss paper next to P101 and soon after P93 |
| Bernoulli leaky cyclic register | `RESERVE_INTERNAL_P93` | exact but closer to the P93 symbolic fiber-loss narrative than P101 |
| necklace decimation | `KILL_DIRECT_OWNER` | multiplier/decimation classes are directly studied |
| Frobenius–Jordan and linear CA candidates | `KILL_OWNER_AND_INTERNAL` | general finite-linear functional graphs are owned and the engine collides with P70/P92 |
| Kreweras complement and 0-Hecke walk | `KILL_DIRECT_OWNER` | orbit/Markov dynamics are directly covered |
| single-hole doubling and one-forbidden-word shifts | `KILL_INTERNAL_P52` | word-autocorrelation owner plus direct internal collision |
| rank-one matrix products, overwrite maps, iid full maps | `KILL_THIN_OR_DIRECT_OWNER` | exact formulas are known geometric/coupon/occupancy repackagings |

## Authority boundary

The five selections are frozen internal theorem contracts, not publication
claims.  Public posting, submission, venue choice, author contact, specialist
priority clearance, and absolute novelty language remain unauthorized and
`HOLD`.
