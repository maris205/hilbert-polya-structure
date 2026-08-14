# Proof Audit — Frobenius Suspension on \(\mathbb P^1/\mathbb F_2\)

Audit date: 2026-08-13  
Candidate: `FF-FROB-SUSP-P1-F2`  
Scope: theorem verification and adversarial controls; no manuscript drafting  
Route: dual evaluation against the native Hasse--Weil target and the Riemann
rational-prime target

## 1. Audit conclusion

All frozen obligations O1--O10 survive direct proof, with one essential scope
split.

- Against the **native** target
  \(Z(\mathbb P^1_{\mathbb F_2},2^{-s})\), the construction gives an exact
  positive control: closed points, primitive Frobenius cycles, and primitive
  suspension orbits are canonically indexed by the same objects; the period is
  \(\deg(x)\log 2\); and the unweighted orbit zeta is exactly
  \(1/((1-2^{-s})(1-2^{1-s}))\).
- Against the **Riemann** target, the same object is rejected analytically.  A
  fixed \(Q=\ell^f\) clock can meet a rational-prime-power clock only in the
  characteristic \(\ell\), and the continued native determinant is periodic in
  imaginary time with period \(2\pi/\log Q\).
- The apparent repair
  \(\coprod_p\mathbb R/(\log p)\mathbb Z\) reproduces \(\zeta(s)\) exactly,
  but is a universal target compiler.  Its exact A1--A2 algebra cannot repair
  its `A0_FAIL`.

The evidence level is `PROVED` for the orbit dictionary, zeta identity,
convergence boundary, clock obstruction, and compiler theorem.  No zero table,
prime fit, network access, or empirical parameter selection is used.  Route B
remains false.

## 2. Frozen definitions and conventions

Let

\[
  X=\mathbb P^1_{\mathbb F_2},\qquad
  S=X(\overline{\mathbb F}_2)_{\mathrm{disc}},\qquad
  F(a)=a^2,
\]

where `disc` is an explicit `MODELING_CHOICE`.  Put \(\tau=\log 2\) and let
\(\mathbb Z\) act on \(S\times\mathbb R\) by

\[
  n\cdot(a,u)=(F^n a,u-n\tau).
\]

The mapping torus and vertical flow are

\[
  M_F=(S\times\mathbb R)/\mathbb Z,
  \qquad \phi^t[a,u]=[a,u+t].
\]

The determinant convention is the unweighted primitive-orbit zeta

\[
  \zeta_{\rm orb}(s)
  =\prod_{\gamma\in\mathcal P(M_F)}
     (1-e^{-s\ell_\gamma})^{-1}.
\]

There is no potential, phase, half-shift, stability factor, or fitted
normalization.  Arithmetic Frobenius and inverse/geometric Frobenius reverse
cycle orientation but have the same primitive lengths and the same frozen
zeta.

## 3. Closed points, Frobenius cycles, and primitive flow orbits

### Lemma 3.1 — closed points of the affine chart

The closed points of \(\mathbb A^1_{\mathbb F_2}\) are in bijection with monic
irreducible polynomials \(f\in\mathbb F_2[T]\).  If \(\deg f=d\) and \(a\) is
one root, then

\[
  a,\ a^2,\ a^{2^2},\ldots,a^{2^{d-1}}
\]

are the distinct roots of \(f\), and the square Frobenius has least period
\(d\) on this set.

**Proof.**  The residue field at the point \((f)\) is
\(\mathbb F_2[T]/(f)\cong\mathbb F_{2^d}\).  Thus \(F^d(a)=a\).  If
\(F^n(a)=a\), then \(a\in\mathbb F_{2^n}\), hence
\(\mathbb F_2(a)=\mathbb F_{2^d}\) embeds in \(\mathbb F_{2^n}\), which
forces \(d\mid n\).  Therefore \(d\) is the least period.  The Frobenius
conjugates are all roots and there are \(d\) of them. \(\square\)

The missing point at infinity is \(\mathbb F_2\)-rational and is a fixed
Frobenius cycle.  Consequently the number \(a_d\) of degree-\(d\) closed points
on \(\mathbb P^1/\mathbb F_2\) is

\[
  a_1=3,
  \qquad
  a_d=\frac1d\sum_{e\mid d}\mu(e)2^{d/e}\quad(d>1).
\]

The formula for \(d>1\) is the usual count of monic irreducibles; the three
degree-one points are \(0,1,\infty\).

### Lemma 3.2 — complete Frobenius-cycle ledger

Every element of \(S\) belongs to one finite Frobenius cycle, and those cycles
are in bijection with closed points of \(X\).  If

\[
  N_n=\#X(\mathbb F_{2^n})=2^n+1,
\]

then

\[
  N_n=\sum_{d\mid n}d\,a_d.
\]

**Proof.**  Every algebraic coordinate belongs to some finite extension, so
every geometric point is fixed by some \(F^n\).  A cycle of least length \(d\)
contributes all of its \(d\) points to \(\operatorname{Fix}(F^n)\) exactly when
\(d\mid n\).  Summing over cycles proves the identity.  Lemma 3.1 and the point
at infinity give the closed-point indexing. \(\square\)

This proves the precise three-way dictionary

\[
  \boxed{
  \text{closed point }x
  \longleftrightarrow
  \text{primitive Frobenius cycle }C_x
  \longleftrightarrow
  \text{primitive suspension orbit }\gamma_x.}
\]

### Proposition 3.3 — suspension decomposition and least periods

There is a flow-preserving homeomorphism

\[
  M_F\cong
  \coprod_{x\in|X|}\mathbb R/(\deg(x)\log2)\mathbb Z.
\]

In particular, \(\gamma_x\) has least period

\[
  \ell_x=\deg(x)\log2=\log(2^{\deg x})=\log N(x),
\]

and its \(r\)-fold repetition has period \(r\ell_x\).

**Proof.**  Choose \(a\in C_x\) and write \(d=\deg(x)\).  On the suspension
of that cycle define

\[
  \Psi_x([F^j a,u])=u+j\log2\pmod{d\log2}.
\]

The defining action sends \((F^j a,u)\) to
\((F^{j+n}a,u-n\log2)\), and both representatives have the same image under
\(\Psi_x\); hence it is well defined.  It is a continuous bijection with the
obvious continuous inverse and intertwines vertical translation.  The least
positive return requires exactly \(d\) base iterates, so the period is
\(d\log2\).  Distinct cycles are disjoint open-and-closed components because
\(S\) is discrete. \(\square\)

### Topological checks

- The \(\mathbb Z\)-action is free because equality of real coordinates forces
  \(n\log2=0\).
- It is properly discontinuous because a compact real projection meets only
  finitely many of its integer translates.
- The quotient is Hausdorff and locally compact; the explicit circle
  decomposition also proves these properties directly.
- It is second countable because there are countably many closed points and
  each circle is second countable.
- It is noncompact because it has infinitely many open-and-closed circle
  components.
- Primitive orbits are locally finite by length: below \(T\), only degrees
  \(d\leq T/\log2\) occur, and there are finitely many closed points of each
  such degree.

The flow is therefore a legitimate locally compact continuous-time flow after
the discrete topology is disclosed.  It is also dynamically degenerate: there
is no nonzero transverse tangent direction, hyperbolicity, mixing, or orbit
interaction.

## 4. Exact zeta identity

### Theorem 4.1 — Artin--Mazur = orbit = Hasse--Weil

As formal series in \(z\),

\[
\begin{aligned}
  \zeta_{AM}(z)
  &=\exp\!\left(\sum_{n\ge1}\frac{N_n}{n}z^n\right)\\
  &=\prod_{d\ge1}(1-z^d)^{-a_d}\\
  &=\prod_{x\in|X|}(1-z^{\deg x})^{-1}\\
  &=Z(X,z).
\end{aligned}
\]

With \(z=2^{-s}\), this is the primitive-orbit identity

\[
  \boxed{
  \zeta_{\rm orb}(s)
  =Z(\mathbb P^1_{\mathbb F_2},2^{-s})
  =\frac1{(1-2^{-s})(1-2^{1-s})}.}
\]

**Proof.**  The fixed-point ledger in Lemma 3.2 gives

\[
\begin{aligned}
  \sum_{n\ge1}\frac{N_n}{n}z^n
  &=\sum_{n\ge1}\frac{z^n}{n}\sum_{d\mid n}d a_d\\
  &=\sum_{d\ge1}a_d\sum_{r\ge1}\frac{z^{rd}}r\\
  &=-\sum_{d\ge1}a_d\log(1-z^d).
\end{aligned}
\]

Exponentiating proves the first three equalities.  Proposition 3.3 replaces
\(z^{\deg x}\) by \(e^{-s\ell_x}\).  Finally,

\[
\begin{aligned}
  Z(X,z)
    &=\exp\!\left(\sum_{n\ge1}\frac{(2^n+1)z^n}{n}\right)\\
    &=\exp(-\log(1-2z)-\log(1-z))\\
    &=\frac1{(1-2z)(1-z)}.
\end{aligned}
\]

No analytic rearrangement is needed for the formal-series identity; every
coefficient involves finitely many divisors.  Analytic convergence is audited
separately below. \(\square\)

### Corollary 4.2 — endogenous repetition and logarithmic weights

On the absolute-convergence half-plane,

\[
  \log\zeta_{\rm orb}(s)
   =\sum_{x}\sum_{r\ge1}\frac{N(x)^{-rs}}r
\]

and

\[
  -\frac d{ds}\log\zeta_{\rm orb}(s)
   =\sum_x\sum_{r\ge1}\log N(x)\,N(x)^{-rs}.
\]

Thus \(1/r\) is forced by the logarithm of a primitive factor, and
\(\log N(x)=\ell_x\) is forced by differentiation with respect to suspension
time.  Neither is inserted as a potential.  Aggregated at exponent
\(n=rd\), the logarithmic-derivative coefficient is

\[
  (\log2)\sum_{d\mid n}d a_d=(2^n+1)\log2.
\]

This positive result does **not** generate a Riemann explicit-formula sign,
phase, or \(N(x)^{-r/2}\) amplitude.  Adding a half-shift would change the
frozen candidate.

## 5. Exact analytic domain and native continuation

### Theorem 5.1 — absolute convergence exactly for \(\Re s>1\)

Let \(\sigma=\Re s\).  Absolute convergence of the logarithmic orbit expansion
is equivalent to

\[
  \sum_{n\ge1}\frac{N_n}{n}2^{-\sigma n}
  =\sum_{n\ge1}\frac{2^n+1}{n}2^{-\sigma n}<\infty.
\]

The first summand is \(2^{(1-\sigma)n}/n\).  It is summable when
\(\sigma>1\), is the harmonic series when \(\sigma=1\), and fails even the
term test when \(\sigma<1\).  The second summand is harmless for
\(\sigma>0\) and cannot repair divergence.  Hence the abscissa is exactly one.
\(\square\)

The rational expression supplies meromorphic continuation to all
\(s\in\mathbb C\).  This continuation must not be confused with Euler-product
convergence.

### Proposition 5.2 — native functional relation and imaginary clock

Writing \(Z(t)=1/((1-t)(1-2t))\), direct algebra gives

\[
  Z\!\left(\frac1{2t}\right)=2t^2Z(t).
\]

Equivalently,

\[
  \zeta_X(1-s)=2^{1-2s}\zeta_X(s).
\]

This is the native \(\mathbb P^1\) functional relation.  It is not the
completed Riemann functional equation.  Also,

\[
  \zeta_X\!\left(s+\frac{2\pi i k}{\log2}\right)=\zeta_X(s),
  \qquad k\in\mathbb Z,
\]

because the function depends only on \(2^{-s}\).  Its two pole lattices are

\[
  s=\frac{2\pi i k}{\log2},
  \qquad
  s=1+\frac{2\pi i k}{\log2}.
\]

The cohomological Frobenius determinant explains the native rational
continuation, but no operator conjugacy identifies it with a return derivative
or trace-class transfer operator of the disjoint-circle flow.  That bridge is
`OPEN / NOT_TESTABLE`, not silently supplied by equality of scalar functions.

## 6. One-clock obstruction across residue characteristics

### Theorem 6.1 — support intersection

Let \(Q=\ell^f\), with \(\ell\) rational prime and \(f\ge1\).  If positive
integers \(n,r\) and a rational prime \(p\) satisfy

\[
  n\log Q=r\log p,
\]

then \(p=\ell\) and \(fn=r\).  If the target equality is primitive,
\(n\log Q=\log p\), then \(Q=p=\ell\) and \(f=n=1\).

**Proof.**  Exponentiation yields \(\ell^{fn}=p^r\).  Unique factorization in
\(\mathbb Z\) forces \(p=\ell\), then equality of exponents gives
\(fn=r\).  For \(r=1\), positivity of \(f,n\) forces both to be one.
\(\square\)

Therefore a fixed finite-field suspension clock can intersect only the
prime-power lattice of its own characteristic.  Enlarging the variety over the
same field changes the closed-point multiplicities but never leaves
\((\log Q)\mathbb N\).  This is an A0/A2 incompatibility with the rational-prime
target, not a numerical near-miss.

### Corollary 6.2 — no fixed imaginary period for the rational Euler product

The finite-field function has nonzero imaginary period
\(2\pi/\log Q\).  By contrast, if the rational Euler product were periodic by
some nonzero \(iT\) on \(\Re s>1\), uniqueness of absolutely convergent
Dirichlet series would force \(n^{-iT}=1\) for every integer \(n\) with a
nonzero Dirichlet coefficient, in particular for \(n=2,3\).  Then
\(T\log2,T\log3\in2\pi\mathbb Z\), which is impossible for nonzero \(T\)
because \(2^a=3^b\) has no positive integer solutions.  The analytic clock
fingerprints are therefore structurally different without consulting any zero.

## 7. Universal circle compiler and the proves-too-much control

### Theorem 7.1 — arbitrary Euler-product compiler

Let \(J\) be countable and let \(L_j>0\) be locally finite in length:
\(\#\{j:L_j\le T\}<\infty\) for every \(T\).  The flow

\[
  M_L=\coprod_{j\in J}\mathbb R/L_j\mathbb Z
\]

with translation on each component is locally compact, Hausdorff, second
countable, and has exactly one primitive orbit of length \(L_j\) per component.
Where the product converges,

\[
  \zeta_{M_L}(s)=\prod_{j\in J}(1-e^{-sL_j})^{-1}.
\]

**Proof.**  All topological statements follow componentwise, and local
finiteness gives a finite primitive ledger below any length cutoff.  A circle
translation has its whole component as one primitive orbit; its repetitions
give the geometric Euler factor.  Multiplying the factors proves the identity.
\(\square\)

Taking \(L_p=\log p\) yields

\[
  \coprod_p\mathbb R/(\log p)\mathbb Z,
  \qquad
  \zeta_{M_L}(s)=\prod_p(1-p^{-s})^{-1}=\zeta(s)
\]

for \(\Re s>1\).  But the construction has queried both the target primitive
index set and every target clock before the dynamics exists.  The same theorem
compiles composite-only factors, randomized lengths, or any prescribed locally
finite divisor.  It therefore receives

```text
A0_FAIL
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_A_REJECTED
```

even though its formal A1 and tautological orbit-product A2 are exact.

### Proposition 7.2 — same-cycle-type control

Let \(G\) be a permutation of a countable discrete set such that every point
is periodic and the number of cycles of each finite length equals the
corresponding Frobenius count.  Then \(G\) is conjugate to Frobenius as a
discrete dynamical system: choose a bijection cycle by cycle, preserving
cyclic order.  Its constant-roof suspension is consequently flow-conjugate to
\(M_F\) and has the same orbit zeta.  The all-points-periodic hypothesis is
necessary: extra infinite orbits would not be recorded by the finite-cycle
counts.  The bare flow therefore remembers the cycle-count sequence \((a_d)\),
but not the algebraic geometry or etale cohomology that generated it.  A
dynamical--cohomological operator bridge cannot be inferred from the circle
topology alone.

## 8. Deterministic-control design and audit

The companion program uses only exact integer arithmetic, finite polynomial
enumeration over \(\mathbb F_2\), and deterministic floating-point evaluations
of already-proved formulas.

It performs the following independent checks.

1. Enumerate every monic polynomial over \(\mathbb F_2\) through the frozen
   degree cutoff and certify irreducibility with the Frobenius/Rabin criterion.
2. Add the point at infinity at degree one and check
   \(2^n+1=\sum_{d\mid n}d a_d\) at every enumerated degree.
3. Expand the finite orbit Euler product as a formal power series and compare
   every coefficient with
   \(1/((1-z)(1-2z))\), whose coefficient at \(z^n\) is \(2^{n+1}-1\).
4. Emit the repetition ledger that separates the \(1/r\) coefficient from the
   \(\deg(x)\log2\) derivative weight.
5. Show partial Euler-log behavior on both sides of \(\Re s=1\), without using
   this finite display as proof of the abscissa.
6. Check imaginary periodicity numerically as a software regression test.
7. Exhaust a finite clock-intersection grid generated at runtime and verify
   that all solutions use the characteristic prime.
8. Apply the circle compiler to unrelated synthetic length sets, demonstrating
   that exact compilation is content-free without A0.

The code does not use Riemann zeros, spectral targets, optimization, random
seeds, network access, or a hard-coded rational-prime table.  Numerical output
is evidence for implementation integrity only; theorem statuses come from the
proofs above.

## 9. Obligation-by-obligation result

| Obligation | Result | Evidence | Location |
|---|---|---|---|
| O1 Frobenius/closed-point dictionary | pass | `PROVED` | Lemmas 3.1--3.2 |
| O2 topology | pass after disclosed discrete topology | `PROVED` + `MODELING_CHOICE` | Proposition 3.3 and topological checks |
| O3 primitive/repetition ledger | pass | `PROVED` | Proposition 3.3, Corollary 4.2 |
| O4 three zeta conventions agree | pass for native target | `PROVED` | Theorem 4.1 |
| O5 weight provenance | pass | `PROVED` | Corollary 4.2 |
| O6 analytic boundary | pass | `PROVED` | Theorem 5.1 |
| O7 one-clock test | pass as an obstruction | `PROVED` | Theorem 6.1 |
| O8 non-tautology gate | native passes; disjoint repair fails | `PROVED` | Theorem 7.1 |
| O9 native/target split | pass | `PROVED` | Section 10 |
| O10 no-zero integrity | pass | `PROVED` by artifact/input audit | Section 8 |

## 10. Dual Route-A evaluation

### 10.1 Native Hasse--Weil calibration

| Layer | Verdict | Evidence | Boundary |
|---|---|---|---|
| A0 | `A0_ANALYTIC_ARITHMETIC_ORIGIN` | `PROVED` | fixed scheme and Frobenius generate the ledger |
| A1 | `A1_PASS_ANALYTIC` | `PROVED` | exact primitive cycles, periods, repetitions, multiplicity, completeness |
| A2 | `A2_ANALYTIC_DETERMINANT` | `PROVED` | exact orbit-zeta identity; no transfer-operator claim |
| A3 | `A3_CONTROLLED_CONTINUATION` | `PROVED` | native rational continuation and functional relation; cohomological source kept explicit |
| A4 | `A4_FAIL` | `NOT_TESTABLE` | no natural quantum or scattering lift is defined |

Scoped overall status:
`ROUTE_A_SUCCESS_ROUTE_B_NOT_READY` **for the native finite-field calibration
only**.  This wording is not a promotion toward the Riemann target.

For the theorem-level A2 identity, training/test zero errors, missing/extra
zero counts, cutoff drift, and precision drift are `not_applicable_exact_identity`.
The finite coefficient checks are regression tests, not fitted validation.

### 10.2 Riemann rational-prime target

| Layer | Verdict | Evidence | Boundary |
|---|---|---|---|
| A0 | `A0_FAIL` | `PROVED` | one characteristic only; wrong primitive support |
| A1 | `A1_PASS_ANALYTIC` as a flow | `PROVED` | exact ledger, but for the wrong arithmetic objects |
| A2 | `A2_FAIL` | `PROVED` | determinant is the wrong Euler product and is single-clock periodic |
| A3 | `A3_FAIL` | `PROVED` for incompatibility; `NOT_TESTABLE` for absent bridges | no Riemann gamma factor, FE, or natural Weil compression |
| A4 | `A4_FAIL` | `NOT_TESTABLE` | no lift and no clock-preserving quantization |

Overall: `ROUTE_A_REJECTED`.

### 10.3 Tautological \(\operatorname{Spec}\mathbb Z\) circle control

| Layer | Verdict | Evidence | Boundary |
|---|---|---|---|
| A0 | `A0_FAIL` | `PROVED` information-flow audit | primes and \(\log p\) roofs define the phase space |
| A1 | `A1_PASS_ANALYTIC` | `PROVED` | one circle per encoded prime |
| A2 | `A2_ANALYTIC_DETERMINANT` | `PROVED`, tautological | exact only because the target was compiled in |
| A3 | `A3_FAIL` | `NOT_TESTABLE` dynamically | continuation and FE come from external number theory |
| A4 | `A4_FAIL` | `NOT_TESTABLE` | no natural lift |

Overall: `ROUTE_A_REJECTED / PROVES_TOO_MUCH`.

For all three readings:

```yaml
route_b_invocation_allowed: false
```

## 11. Claim boundary and next theorem obligation

The certified claim is an exact finite-field calibration plus an exact
characteristic-zero transfer obstruction.  It is not a Hilbert--Polya model,
not a trace-formula construction for the circle flow, and not evidence that a
Riemann operator exists.

The next smallest admissible construction must be a **single coupled,
non-disjoint phase space across residue characteristics**.  Before determinant
or spectral analysis it must prove:

1. one return mechanism generates the primitive closed objects;
2. \(\log N(x)\) is derived as return time rather than read from the target;
3. the topology or operator framework couples distinct characteristics; and
4. an exact control separates it from Theorem 7.1's universal compiler.

Until then the finite-field suspension remains a positive structural prior,
and the disjoint-prime suspension remains a proved obstruction rather than a
candidate.
