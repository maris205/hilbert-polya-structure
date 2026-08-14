# Paper 7 Phase-3 mathematical proof audit

Status: **PHASE-3 AMENDMENT v1 — M1--M4 CLOSED MATHEMATICALLY; M5
INDEPENDENT EXACT-BYTE RE-LOCK PENDING**  
Date: 2026-08-14  
Scope: mathematical analysis of the frozen proxy only; source ownership and
P7-9 are not adjudicated here

Amendment ID: `P7-PH3-AMEND-2026-08-14-v1`; crosswalk:
`phase3_protocol_amendment.md`.

Superseding inputs:

- `research_protocol.md`, SHA-256
  `2f8dc9a802cfcf8b578db24419909de710563ece62cf026e9848fac437ba1581`;
- `candidate_lock.md`, SHA-256
  `73314bb031f663e8532a922821e66b20f31bd6f20b06a801a25147d6e55a17a0`;
- `operator_source_audit.md`, SHA-256
  `69a76991c94cab24652c8d7d9f71c47a8eba70fcd7d1d4148689d47ff56e8b04`.

Historical pre-amendment inputs were protocol SHA-256
`0029ea437f9318ff4962830ed4d197cdad0d355968364a52bbeefc63a9db96c4`
and candidate SHA-256
`0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa`.
They remain provenance records, not current locks.

No statement below transfers a proxy-owned measure, algebra, trace, return
distribution, zero mode, or determinant to `DEN-WITT-Z-FIN`.

## 1. Verdict and required theorem correction

| Target | Mathematical verdict | Essential boundary |
|---|---|---|
| P7-1 | **PROVED** | Component operator is in the bounded `tau_p` trace ideal; the concrete local/global FNS foundation is proved below. |
| P7-2 | **PROVED** | The global block is bounded, but for nonzero `f` it is globally `L1` exactly when `sum_p m_p log p` converges. Unit masses fail. |
| P7-3 | **PROVED** | The positive-time formula is a locally finite Radon measure/distribution, not a global trace evaluation outside `L1`. |
| P7-4 | **PROVED; VERSIONED CORRECTION APPLIED** | In the **bounded** trace ideal one needs both `Re(s)>=0` and the weighted Dirichlet sum. The sum alone is the criterion only in the affiliated-operator `L1` space. Unit masses give exactly `Re(s)>1`. |
| P7-5 | **PROVED AFTER M3--M4 REPAIR** | The complex object is the branch-fixed principal trace-log scalar on its open relative-norm domain. FK gives its modulus only; the actual `B_p` ordinary multiplicity is proved below. |
| P7-6 | **PROVED WITH SCOPE AFTER M2 REPAIR** | The concrete trace is FNS, and positive sequences classify the frozen **central-scalar trace family**, not all traces on the algebra. |
| P7-7 | **PROVED** | Coefficient equality forces `m_p=1`; this is target-conditioned uniqueness and cannot prove provenance. |
| P7-8 | **PROVED, MATHEMATICAL PART ONLY** | Both branches are probability-base blind; the zero-mode branch is an arbitrary-clock compiler. |

The correction to P7-4 is load-bearing.  Write

```text
K_s in M intersect L^1(M,tau_m)
  iff Re(s) >= 0 and sum_p m_p p^(-Re(s)) < infinity.
```

If `L^1(M,tau_m)` instead denotes the full space of affiliated measurable
operators, the summability condition alone is correct, but that is not the
bounded relative Banach-algebra domain used by the determinant theorem.

## 2. Frozen conventions and trace-domain lemma

Put

```text
L_p = log p,
S_L = R/LZ,
Kappa_L = L2(S_L,du),
H_p = L2(B_p,mu_p) tensor Kappa_(L_p),
M_p = L-infinity(B_p,mu_p) bar-tensor B(Kappa_(L_p)).
```

Here `du` is ordinary Lebesgue measure on `[0,L)`, and `mu_p` is Haar
probability, so `mu_p(B_p)=1`.  The normalized Fourier basis is

```text
e_(n,L)(u) = L^(-1/2) exp(2 pi i n u/L),  n in Z.
```

Freeze the Fourier transform and inverse as

```text
fhat(xi) = integral_R f(t) exp(-i t xi) dt,
f(t) = (1/(2 pi)) integral_R fhat(xi) exp(i t xi) dxi.
```

Freeze the right-regular circle translation by

```text
(U_L(t)g)(u) = g(u-t).
```

Thus

```text
U_L(t)e_(n,L) = exp(-2 pi i n t/L)e_(n,L).
```

Using the opposite translation sign only replaces `n` by `-n`; it does not
change a full lattice sum, but it must not be mixed into an unreindexed
display.

The global algebra is the bounded product

```text
M = product_p^infinity M_p
  = {(A_p)_p : sup_p ||A_p|| < infinity}
```

on the Hilbert direct sum.  For `0<m_p<infinity`, the positive-cone trace is

```text
tau_m(A) = sum_p m_p tau_p(A_p),
tau_p(A_p) = integral_(B_p) Tr_Kappa(A_p(b)) dmu_p(b),  A>=0.
```

Throughout this audit the **bounded trace ideal** means

```text
L^1_tau(M) = {A in M : tau_m(|A|)<infinity}.
```

For a bounded block `A=(A_p)`, functional calculus is componentwise, hence
`|A|=(|A_p|)`.  It follows directly from the positive-cone definition that

```text
A in L^1_tau(M)
  iff sum_p m_p tau_p(|A_p|) < infinity,

||A||_(1,tau_m) = sum_p m_p ||A_p||_(1,tau_p).
```

This membership formula is now backed by the following concrete
faithful-normal-semifinite trace lemma; it is not being inferred from
Dirichlet convergence.

### 2.1 Concrete local and global FNS trace lemma

Identify the component algebra as the direct integral

```text
M_p = integral_(B_p)^direct-sum B(Kappa_(L_p)) dmu_p(b).
```

For `A_p>=0`, set

```text
tau_p(A_p) = integral_(B_p) Tr_Kappa(A_p(b))dmu_p(b).
```

The ordinary fiber trace satisfies
`Tr(X(b)^*X(b))=Tr(X(b)X(b)^*)`; integration gives traciality.  If
`tau_p(A_p)=0`, then the nonnegative function `Tr(A_p(b))` vanishes almost
everywhere, hence `A_p(b)=0` almost everywhere; this gives faithfulness.  The
direct-integral trace theorem gives normality.  In its net form, for every
increasing bounded net `A_(p,i) ↑ A_p` in the positive cone,

```text
tau_p(A_p) = sup_i tau_p(A_(p,i)).                              (2.1)
```

This is a statement for arbitrary directed nets, not just sequences.

For a concrete semifinite approximation, let `Q_(p,N)` be the projection of
`Kappa_(L_p)` onto the circle modes `|n|<=N`, and put

```text
E_(p,N) = 1_(B_p) tensor Q_(p,N),
A_p^(N) = A_p^(1/2) E_(p,N) A_p^(1/2).                          (2.2)
```

The order claim in (2.2) requires the cutdown in exactly this congruence form.
Because `E_(p,N+1)-E_(p,N)>=0`,

```text
A_p^(N+1)-A_p^(N)
 = A_p^(1/2)(E_(p,N+1)-E_(p,N))A_p^(1/2) >= 0.
```

Also `0<=A_p^(N)<=A_p` and `A_p^(N)↑A_p` strongly.  Traciality applied to
`X=A_p^(1/2)E_(p,N)` gives

```text
tau_p(A_p^(N))
 = tau_p(E_(p,N)A_pE_(p,N))
 <= ||A_p|| tau_p(E_(p,N))
 = ||A_p||(2N+1) < infinity.                                   (2.3)
```

Thus (2.1)--(2.3) exhibit finite-weight positive subelements increasing to
every bounded positive `A_p`; `tau_p` is faithful, normal, and semifinite.

Now let `A=(A_p)_p>=0` in the bounded product.  Index a net by pairs
`(F,mathbf N)`, where `F` is a finite set of primes and
`mathbf N=(N_p)_(p in F)`.  Order these pairs by inclusion of `F` and
coordinatewise increase of the already present `N_p`, and define

```text
A^(F,mathbf N)_p = A_p^(N_p),  p in F,
A^(F,mathbf N)_p = 0,          p not in F.                      (2.4)
```

The net (2.4) is increasing, lies below `A`, and converges strongly to `A` on
the Hilbert direct sum.  Each term has finite global weight:

```text
tau_m(A^(F,mathbf N))
 <= ||A|| sum_(p in F)m_p(2N_p+1) < infinity.                  (2.5)
```

Global normality also holds for arbitrary increasing nets.  Indeed, if
`A_i↑A`, local normality and directedness give

```text
sup_i sum_p m_p tau_p(A_(i,p))
 = sum_p m_p sup_i tau_p(A_(i,p))
 = sum_p m_p tau_p(A_p).                                      (2.6)
```

For clarity, the nontrivial inequality in (2.6) is obtained first on a finite
prime set: choose one approximating index for each of its finitely many
components and then a common upper bound in the directed set.  Taking the
supremum over finite prime sets gives the countable sum.  Equations
(2.4)--(2.6) then give

```text
tau_m(A) = sup_(F,mathbf N)tau_m(A^(F,mathbf N)).               (2.7)
```

Since every `m_p` is positive and finite, component faithfulness passes to the
sum.  Therefore the stated positive-cone formula defines a faithful normal
semifinite trace `tau_m`, and the bounded `L1` criterion preceding (2.1) is
legitimate.

## 3. P7-1 — component Fourier diagonalization and Poisson trace

For `f in C_c^infinity(R)`, define the integrated translation operator

```text
T_L(f) = integral_R f(t)U_L(t)dt
```

in the integrated unitary representation.  It is bounded and
`||T_L(f)||<=||f||_1`.  The frozen sign convention gives

```text
T_L(f)e_(n,L) = fhat(2 pi n/L)e_(n,L).
```

Since `fhat` is Schwartz,

```text
sum_(n in Z) |fhat(2 pi n/L)| < infinity.
```

Consequently `T_L(f)` is ordinary trace class on `Kappa_L`.  The component
operator is the constant decomposable field

```text
C_(p,f) = 1_(B_p) tensor T_(L_p)(f).
```

Because `mu_p` is a probability,

```text
C_(p,f) in L^1_(tau_p)(M_p),

||C_(p,f)||_(1,tau_p)
  = sum_(n in Z) |fhat(2 pi n/L_p)|,

tau_p(C_(p,f))
  = sum_(n in Z) fhat(2 pi n/L_p).
```

Here `T_L(f)` is ordinary Hilbert trace class on the circle factor, whereas
`1_(B_p) tensor T_L(f)` is generally **not** ordinary Hilbert trace class on
`H_p` when `L2(B_p)` is infinite-dimensional.  The displayed component
membership is membership in the semifinite `tau_p` trace ideal.

For completeness, periodize `f` by

```text
F_L(u) = sum_(r in Z) f(u+rL).
```

It is a smooth `L`-periodic function, and its `n`th Fourier coefficient is
`L^(-1)fhat(2 pi n/L)`.  Absolute convergence permits evaluation at zero:

```text
sum_(r in Z) f(rL)
  = (1/L) sum_(n in Z) fhat(2 pi n/L).
```

Therefore

```text
tau_p(C_(p,f)) = L_p sum_(r in Z) f(rL_p).
```

This proves P7-1 with the operator, trace, measure, and Fourier conventions all
fixed.  The same computation does not yet take a trace over the prime index.

## 4. P7-2 — bounded global block, exact `L1` criterion, and asymptotic

First distinguish boundedness from trace-ideal membership.  For every prime,

```text
||C_(p,f)|| = sup_n |fhat(2 pi n/L_p)| <= ||f||_1.
```

Hence

```text
C_f = (C_(p,f))_p
```

is always a bounded element of `M`.  By the global trace-domain lemma,

```text
C_f in L^1_(tau_m)(M)
  iff sum_p m_p sum_(n in Z)|fhat(2 pi n/L_p)| < infinity.       (4.1)
```

To sharpen (4.1), let `g(xi)=|fhat(xi)|`.  It is continuous, integrable, and
rapidly decreasing.  The whole-line Riemann-sum theorem gives, as `L->infinity`,

```text
(2 pi/L) sum_(n in Z) g(2 pi n/L)
  -> integral_R g(xi)dxi.
```

Thus

```text
||C_(p,f)||_(1,tau_p)
  ~ c_f L_p,

c_f = (1/(2 pi)) integral_R |fhat(xi)|dxi.                     (4.2)
```

If `f` is nonzero, Fourier injectivity gives `c_f>0`.  Since `L_p=log p`
tends to infinity, (4.2) supplies eventual two-sided positive bounds.  Hence,
for every fixed nonzero `f`, the exact mass criterion simplifies to

```text
C_f in L^1_(tau_m)(M)
  iff sum_p m_p log p < infinity.                               (4.3)
```

For unit masses, the summands in (4.1) are asymptotic to
`c_f log p`; in particular they do not tend to zero.  Therefore the global
trace norm diverges.  This proves P7-2.  Notice that this failure holds even
when the signed component traces below vanish for all sufficiently large
primes.

## 5. P7-3 — positive-time return measure and the non-trace boundary

Let `f in C_c^infinity((0,infinity))`.  The component formula has no
nonpositive repetitions, so define

```text
Theta_m(f)
  = sum_p m_p L_p sum_(r>=1) f(rL_p).
```

Equivalently,

```text
Theta_m = sum_p sum_(r>=1) m_p L_p delta_(rL_p).                 (5.1)
```

This is a locally finite positive Radon measure on `(0,infinity)`.  Indeed, if
the compact support lies in `[a,b]` with `0<a<=b`, then a contributing pair
satisfies

```text
p <= exp(b),
r <= b/log 2.
```

There are only finitely many such pairs.  No growth hypothesis on the
sequence is needed beyond each individual `m_p` being finite, because only
finitely many masses occur on any compact positive-time set.  Hence (5.1) is
also a distribution of order zero.

If the global condition (4.1) happens to hold, absolute trace summability
does license

```text
tau_m(C_f) = Theta_m(f).
```

Outside that domain, the right side remains defined by (5.1), but the left
side is not a finite evaluation of the normal semifinite trace.  For example,
with unit masses and nonzero positive-time `f`, all sufficiently large
component traces are zero by Poisson summation, while P7-2 proves that the
sum of component trace norms diverges.  The zeros are Fourier-mode
cancellations, not an extension of `tau_m`.

The exclusion of time zero is essential.  If zero is admitted, the `r=0`
terms carry total coefficient

```text
f(0) sum_p m_p L_p.
```

This is finite only under an additional mass condition (or when `f(0)=0`).
No zero-time regularization is part of P7-3.

## 6. P7-4 — zero mode and its exact bounded trace-ideal domain

Let

```text
P_(0,p) = 1_(B_p) tensor |e_(0,L_p)><e_(0,L_p)|.
```

Then `P_(0,p)` is a projection in `M_p` and

```text
tau_p(P_(0,p)) = 1.
```

For `s in C`, write `sigma=Re(s)` and set

```text
K_s = (p^(-s)P_(0,p))_p.
```

Its operator and trace norms are

```text
||K_s|| = sup_p p^(-sigma),
tau_m(|K_s|) = sum_p m_p p^(-sigma).                            (6.1)
```

For the infinite prime index set,

```text
K_s in M iff sigma>=0.
```

Indeed, for `sigma>=0` the supremum is `2^(-sigma)`; for `sigma<0`, the
coefficients grow without bound.  Combining this with (6.1) proves

```text
K_s in M intersect L^1(M,tau_m)
  iff sigma>=0 and sum_p m_p p^(-sigma)<infinity.               (6.2)
```

For every `s`, the closed block-diagonal operator with blocks
`p^(-s)P_(0,p)` is affiliated with `M`; its absolute value has blocks
`p^(-sigma)P_(0,p)`.  Applying the extended trace to its increasing bounded
spectral truncations gives

```text
K_s in affiliated L^1(M,tau_m)
  iff sum_p m_p p^(-sigma)<infinity,
||K_s||_(1,tau_m) = sum_p m_p p^(-sigma).                       (6.2a)
```

Thus in the full affiliated-operator noncommutative `L1` space, the second
condition alone is the norm criterion.  If rapidly decaying masses make that
sum finite for a negative `sigma`, `K_s` is an integrable **unbounded
affiliated operator**, not an element of the bounded algebra and not in the
relative determinant domain frozen here.

### Unit masses: exact if and only if

For `m_p=1`,

```text
sum_p p^(-sigma) < infinity iff sigma>1.                        (6.3)
```

For `sigma>1`, this is a subseries of the convergent positive series
`sum_(n>=2)n^(-sigma)`.  For `0<sigma<=1`, it dominates
`sum_p 1/p`, which diverges by the self-contained lemma below.  For
`sigma<=0`, its terms fail to tend to zero.

**Reciprocal-prime lemma.**  For `x>=2`, unique factorization gives the
finite-Euler-product identity

```text
product_(p<=x)(1-1/p)^(-1)
  = sum_(n: every prime divisor of n is <=x) 1/n
  >= sum_(n<=floor(x))1/n.
```

The last harmonic partial sum is unbounded.  If `sum_p 1/p` converged, then

```text
-log(1-1/p) <= 2/p,  p>=2,
```

would make the logarithms of all finite products uniformly bounded, a
contradiction.  Thus `sum_p1/p` diverges, proving (6.3) without using the
zeta function as input.

Consequently the unit-mass candidate satisfies

```text
K_s in M intersect L^1(M,tau) iff Re(s)>1.
```

On this half-plane `||K_s||=2^(-Re(s))<1`, so `I-K_s` is invertible in `M`.

## 7. P7-5 — relative-norm holomorphy and principal trace-log scalar

### 7.1 General mass half-plane

Let

```text
S_m(sigma) = sum_p m_p p^(-sigma)
```

and let `sigma_c(m)` be its abscissa of convergence, with the usual values
`+infinity` or `-infinity` allowed.  The bounded local determinant domain is

```text
H_m = {s in C : Re(s)>max(0,sigma_c(m))}.                        (7.1)
```

It can be empty if `sigma_c(m)=+infinity`.  It is open, and every `s in H_m`
satisfies both

```text
sum_p m_p p^(-Re(s)) < infinity,
||K_s|| = 2^(-Re(s)) < 1.
```

No boundary point is included, even if the weighted series happens to
converge there.  The Banach ideal required by the relative determinant
framework is

```text
L^1_tau(M) = M intersect L^1(M,tau_m),
||X||_rel = ||X|| + ||X||_(1,tau_m).                            (7.2)
```

We now prove holomorphy in this relative norm, rather than in trace norm alone.
Fix a compact set `C subset H_m`, put

```text
a = min_(s in C)Re(s) > max(0,sigma_c(m)),
```

and choose `sigma_0` with `sigma_c(m)<sigma_0<a`.  Write
`delta=a-sigma_0>0`.  For every integer `k>=0`,

```text
||K_s^(k)||_(1,tau_m)
 = sum_p m_p(log p)^k p^(-Re(s))
 <= C_(k,delta)S_m(sigma_0),                 s in C.            (7.3)
```

For the prime truncation `K_(s,P)` the missing operator tail obeys

```text
sup_(s in C)||K_s^(k)-K_(s,P)^(k)||
 <= sup_(p>P)(log p)^k p^(-a) -> 0,           P->infinity,       (7.4)
```

while (7.3), with the corresponding series tail, makes the trace-norm tail
tend to zero locally uniformly.  The same estimates apply for every
derivative.  Since the finite-prime truncations are entire, (7.3)--(7.4)
prove that `s -> K_s` is holomorphic on `H_m` in `||.||_rel`.

The logarithm also converges in both parts of that norm.  On `C` put

```text
q=2^(-a)<1,    M_0=S_m(a)<infinity.
```

Then, uniformly for `s in C` and `r>=1`,

```text
||K_s^r|| <= q^r,
||K_s^r||_(1,tau_m) <= M_0 q^(r-1).                            (7.5)
```

Consequently

```text
sum_(r>=1)(||K_s^r||+||K_s^r||_(1,tau_m))/r
 <= sum_(r>=1)(q^r+M_0q^(r-1))/r < infinity                   (7.6)
```

locally uniformly.  The derivative series is locally uniform in the same
norm as well.  Indeed, the diagonal blocks commute and

```text
d/ds (K_s^r/r) = K_s^(r-1)K_s',
||K_s^(r-1)K_s'||_rel <= q^(r-1)||K_s'||_rel,                  (7.7)
```

where `||K_s'||_rel` is uniformly bounded on `C` by (7.3)--(7.4).  Thus the
logarithm branch fixed at the identity is a relative-norm holomorphic map,

```text
Log_0(I-K_s) = -sum_(r>=1)K_s^r/r,                              (7.8)
```

with convergence in `||.||_rel`, locally uniformly on `H_m`.  Define only on
this branch and open domain

```text
D_tau^pr(s) = exp(tau_m(Log_0(I-K_s))).                          (7.9)
```

It is a holomorphic, nonvanishing scalar function.

### 7.2 Exact trace-log and product

Since `P_(0,p)^r=P_(0,p)`, absolute convergence gives

```text
tau_m(K_s^r) = sum_p m_p p^(-rs).
```

The double series is absolutely and locally uniformly convergent because

```text
sum_p sum_(r>=1) m_p p^(-r sigma)/r
 <= S_m(sigma)/(1-2^(-sigma)).                                  (7.10)
```

Therefore sums and trace may be interchanged:

```text
D_tau^pr(s)
 = exp(-sum_(r>=1)tau_m(K_s^r)/r)
 = exp(-sum_p m_p sum_(r>=1)p^(-rs)/r)
 = exp(sum_p m_p Log_0(1-p^(-s))).                              (7.11)
```

For nonintegral masses, the notation

```text
product_p (1-p^(-s))^(m_p)
```

means exactly the final branch-fixed exponential in (7.11); it is not an
unqualified algebraic power.  With unit masses, `sigma_c=1` and

```text
D_tau^pr(s) = product_p(1-p^(-s)),
Z_m(s) = D_tau^pr(s)^(-1)
       = product_p(1-p^(-s))^(-1),        Re(s)>1.               (7.12)
```

The product is derived from the absolutely convergent trace-log sum.  No
general complex multiplicativity theorem for a semifinite determinant is
being used.

### 7.3 The actual `B_p` and ordinary Hilbert multiplicity

The ordinary-Hilbert exclusion requires a lemma about the frozen packet base,
not a generic control space.  Put

```text
G_p = Zhat_(p)^x = product_(ell!=p) Z_ell^x,
H_p = p^Zhat subset G_p,
B_p = G_p/H_p.
```

Here `H_p` is the closed procyclic **image** of the exponent map; injectivity
of that map is neither asserted nor needed.  Let `I_p` be the infinite set of
odd primes `ell!=p` and define the coordinatewise sign subgroup

```text
S_p = {epsilon in G_p :
       epsilon_ell in {+1,-1} for ell in I_p,
       epsilon_ell=1 otherwise}.
```

Then `S_p` is isomorphic to `product_(ell in I_p)C_2` and every one of its
elements has order dividing two.  A procyclic profinite group has at most one
nonidentity involution: if it had two, an open normal subgroup avoiding those
two elements and their product would yield a finite cyclic quotient with two
distinct nonidentity involutions.  Hence

```text
|S_p intersect H_p| <= 2.
```

The quotient map `G_p -> B_p` therefore has an infinite (indeed uncountable)
image on `S_p`.  In particular, the actual abstract compact group `B_p` is
infinite.

Let `mu_p` be its normalized Haar probability.  Translation invariance makes
all singleton masses equal.  If their common value were positive, finite sets
of arbitrarily large cardinality would have measure greater than one; hence

```text
mu_p({b})=0 for every b in B_p.                                 (7.13)
```

No broader nonatomicity assertion is needed.  To prove the required Hilbert
dimension directly, fix any positive integer `N`.  Choose `N` distinct points
of `B_p` and pairwise disjoint nonempty open neighborhoods of them.  Every
nonempty open subset of a compact group has positive Haar measure, since
finitely many translates of a smaller open neighborhood cover the group.
The indicator functions of those `N` disjoint open sets are nonzero and
pairwise orthogonal in `L2(B_p,mu_p)`.  Since `N` is arbitrary,

```text
dim L2(B_p,mu_p) = infinity.                                   (7.14)
```

Consequently the range of
`I_(L2(B_p)) tensor |e_0><e_0|` is isomorphic to `L2(B_p,mu_p)` and has
infinite ordinary Hilbert rank.

### 7.4 Determinant taxonomy and forbidden upgrades

1. **Fuglede--Kadison.**  The positive semifinite determinant is defined on
   the same invertible `I+L1` element and, since this family is normal and
   diagonal,

   ```text
   Delta_tau(I-K_s)
     = exp(sum_p m_p log|1-p^(-s)|)
     = |D_tau^pr(s)|.
   ```

   It equals the complex value itself only on a real interval where that value
   is positive, in particular for real `s>1` with unit masses.  For nonreal
   `s` it discards phase and is not a holomorphic Euler product.

2. **de la Harpe--Skandalis.**  The relative construction is naturally
   quotient-valued.  Equations (7.8)--(7.9) select the local scalar lift along
   the logarithm path fixed at the identity.  They do not create a canonical
   global complex scalar determinant on all of `I+L1`.

3. **Breuer--Fredholm.**  On `H_m`, `I-K_s` is already invertible, so it is
   Breuer--Fredholm with index zero.  This supplies no complex determinant and
   does not license the phrase “Breuer determinant.”

4. **Ordinary Hilbert Fredholm determinant.**  In the intended representation,

   ```text
   P_(0,p) = I_(L2(B_p)) tensor |e_0><e_0|.
   ```

   By (7.13)--(7.14), the frozen packet base has infinite-dimensional
   `L2(B_p)`, so this
   projection has infinite ordinary Hilbert rank and trace.  Thus every
   nonzero block `p^(-s)P_(0,p)` fails ordinary Hilbert trace class, and the
   ordinary Fredholm determinant of `I-K_s` is undefined there.  The
   semifinite trace integrates normalized transverse mass; it is not the
   ordinary trace of the represented operator.

5. **Dynamical terminology.**  The zero-mode determinant is not the
   determinant of `C_f`, a flat/groupoid trace determinant, or a
   primitive-orbit Ruelle determinant.  Right-half-plane equality alone says
   nothing about continuation, functional equation, Gamma factors, divisor,
   or a Hilbert--Polya spectrum.

This proves P7-5 in the maximal terminology authorized by the source audit.

## 8. P7-6 — exact central-scalar mass-family classification

Fix the local traces `tau_p` once and for all.  For every sequence
`m=(m_p)` with `0<m_p<infinity`, the positive-cone sum `tau_m` is a faithful
normal semifinite trace by the concrete direct-integral and directed-cutdown
proof in Section 2.1.  In particular, (2.6) proves normality for increasing
nets, and the finite-prime/circle-mode net (2.4) supplies finite-weight
subelements increasing to every bounded positive element.  This replaces the
insufficient shortcut of selecting just one nonzero central component.

Within the frozen ansatz

```text
tau|_(z_p M) = m_p tau_p,
```

where `z_p` is the `p`th central support, the sequence `m` is recovered by

```text
m_p = tau(P_(0,p)).
```

Thus positive finite sequences classify exactly this **central-scalar
family**.  Allowing `m_p=0` destroys faithfulness on that summand; assigning
an infinite scalar destroys semifiniteness there.

This is deliberately not a classification of all faithful normal semifinite
traces on `M`.  Even on a single decomposable component, a positive finite
nonconstant central density `w_p(b)` gives, when permitted by the fixed
measurable structure,

```text
A -> integral_(B_p) w_p(b)Tr(A(b))dmu_p(b),
```

which is generally not a scalar multiple of `tau_p`.  The protocol froze
constant density and varies only its central scalar.

Every local symmetry that already preserves `tau_p` remains a symmetry after
multiplication by `m_p`.  This includes circle-translation conjugacy, fiber
unitary conjugacy, and base changes that actually preserve `mu_p`.  The mass
does not prove that an unverified coordinate change preserves the measure.

If one component is copied as a new orthogonal central summand with the same
local trace and mass, then for a copied positive operator

```text
tau_copy(A_p direct-sum A_p) = 2m_p tau_p(A_p).
```

The corresponding return coefficient and trace-log exponent double.  Splitting
the old mass between the two copies would restore the old number only by a new
renormalization choice.  Hence additivity detects copying and no
within-component invariance selects `m_p=1`.  This proves the scoped P7-6.

## 9. P7-7 — coefficient uniqueness and why it is not provenance

On any common half-plane of absolute convergence, (7.11) gives

```text
-Z_m'(s)/Z_m(s)
  = sum_p sum_(r>=1) m_p(log p)p^(-rs).                          (9.1)
```

The rational-prime target series is

```text
sum_p sum_(r>=1) (log p)p^(-rs).                                (9.2)
```

We use the standard uniqueness lemma, included here to keep the inference
explicit.

**Dirichlet-series uniqueness lemma.**  Suppose
`sum_(n>=1)c_n n^(-s)` converges absolutely on `Re(s)>sigma_0` and vanishes
there.  If `n_0` is the least index with `c_(n_0) != 0`, multiply by `n_0^s`
and let real `s->infinity`.  For one fixed `sigma_1>sigma_0`, dominated
convergence applies to

```text
n_0^s sum_(n>n_0)c_n n^(-s),
```

using `sum_n |c_n|n^(-sigma_1)<infinity`; the tail tends to zero.  The limit
is then `c_(n_0)`, a contradiction.  Hence every coefficient is zero.

Apply the lemma to the difference of (9.1) and (9.2).  A positive integer
`p^r` determines its underlying prime uniquely, and the coefficient at the
primitive index `n=p` is

```text
(m_p-1)log p.
```

Equality of the logarithmic derivatives therefore forces

```text
m_p=1 for every rational prime p.                               (9.3)
```

Conversely, unit masses plainly give coefficient equality in `Re(s)>1`.

Equation (9.3) is a uniqueness statement **conditional on demanding the
target series**.  It does not show that closed-point counting measure, the
published packet, or a source-defined transverse measure transports to these
central trace weights.  Choosing the masses by imposing (9.2) uses the desired
Euler coefficients as input and is provenance-circular.  An independently
proved transport could use (9.3) as a consistency check, but P7-7 cannot close
the unit-mass provenance gate or same-object certificate T7.

## 10. P7-8 — strict base- and clock-blindness controls

### 10.1 Probability-base blindness

Replace `B_p` by a singleton or by any probability space `(Omega_p,nu_p)`,
and keep the constant fiber operators.  Then for every trace-class `T` on the
circle factor,

```text
integral_(Omega_p)Tr(T)dnu_p = Tr(T).
```

Therefore the following quantities are unchanged:

```text
tau_p(C_(p,f)),
||C_(p,f)||_(1,tau_p),
tau_p(P_(0,p)),
tau_m(K_s^r),
Theta_m,
D_tau^pr.
```

Only the normalization `nu_p(Omega_p)=1` is used.  A finite base measure of
mass `c_p` would simply rescale the formulas and can be absorbed into `m_p`.
Thus neither analytic branch detects the topology, cardinality, or packet
geometry of the base.

The ordinary Hilbert determinant behaves differently and exposes the
distinction: for a singleton base the zero-mode projection has ordinary rank
one, so the global `K_s` is ordinary trace class for unit masses on
`Re(s)>1`; for the intended infinite base it has infinite ordinary
multiplicity.  The semifinite formula being identical in both cases is the
base-blind, proves-too-much control.

### 10.2 Arbitrary-clock compiler

Let `(L_j)_(j in J)` be a countable, locally finite list of positive lengths,
meaning that `{j:L_j<=R}` is finite for every `R>0`.  Let `m_j` be positive
finite masses and repeat the same construction with circles `R/L_jZ`.  Then

```text
tau_j(C_(j,f)) = L_j sum_(r in Z)f(rL_j),

Theta_(m,L) = sum_j sum_(r>=1)m_jL_j delta_(rL_j),

tau(K_s^r) = sum_j m_j exp(-rsL_j).
```

Local finiteness of the length list makes `Theta_(m,L)` locally finite on
positive time.  On any half-plane where the zero-mode block is bounded,
trace class, and has norm below one, the same proof gives

```text
D_tau^pr(s)
  = exp(sum_j m_j Log_0(1-exp(-sL_j))).                          (10.1)
```

For an infinite locally finite list, the lengths are unbounded, and therefore
the zero-mode block is bounded exactly for `Re(s)>=0`; its norm is strictly
below one for `Re(s)>0`.  In the bounded trace ideal the exact condition is

```text
Re(s)>=0 and sum_j m_j exp(-Re(s)L_j)<infinity.
```

The power-series determinant additionally uses `Re(s)>0`.  Thus prescribed
prime clocks, composite clocks, or a different locally finite clock ledger
all compile their corresponding branch-fixed product by the same mechanism.
Formula (10.1) is strict mathematics but supplies no arithmetic ownership.

## 11. Final domain and ownership boundary

The proved implications are exactly:

```text
component smooth smear
  -> component bounded trace-ideal operator
  -> Poisson component trace;

global bounded smear + sum_p m_p||C_(p,f)||_1<infinity
  -> legitimate global tau_m evaluation;

positive-time local finiteness alone
  -> Radon return distribution, not a tau_m extension;

bounded K_s + trace-ideal summability + ||K_s||<1
  -> principal trace-log determinant;

target logarithmic-derivative equality
  -> unique masses, not mass provenance.
```

P7-9 remains outside this deliverable.  In particular, none of these proofs
constructs or transports a packet Haar system, disintegration, groupoid,
representation, normal trace, zero mode, or determinant on the published
`DEN-WITT-Z-FIN` flow.  The exact determinant is simultaneously a valid proxy
theorem and a base-blind arbitrary-clock compiler; those two facts must remain
visible together.
