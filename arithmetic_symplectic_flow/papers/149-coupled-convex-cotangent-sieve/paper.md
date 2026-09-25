# Coupled convex sieve dynamics: prime-only hyperbolic packets in a full four-dimensional cotangent map

**Paper ID:** 149-coupled-convex-cotangent-sieve  
**Candidate ID:** ASFS-20260915-CCS01  
**Date:** 2026-09-15  
**Status:** PRIME-ONLY FOUR-DIMENSIONAL HYPERBOLIC PACKETS AND ORDINARY ZETA ESTABLISHED; CLOCK / TRACE OPEN.  
**Route:** Owner-level arithmetic, full periodic ledger and ordinary scalar zeta;
formal Route coordinates UNASSIGNED; Route B NOT INVOKED.

## Abstract

We construct one smooth canonical symplectomorphism on the full countable
disjoint union of four-dimensional cotangent spaces indexed by every integer
and its dyadic witness phase. Local divisibility witnesses drive a genuinely
coupled two-variable convex-gradient map; its cotangent lift is the frozen
symplectic owner. A bounded-drift argument excludes every composite periodic
configuration. A strictly increasing norm excludes every nonzero prime
periodic configuration, and the complete momentum equation eliminates every
nonzero periodic cotangent vector. Consequently there is exactly one
intrinsic primitive packet per prime and no other closed packets. Every
packet is hyperbolic in all four transverse directions, with explicit
nonvanishing repetition denominators. The unit-roof flow owns periods
K_p=max(1,floor(log_2(p-1))), repetitions r K_p and the ordinary zeta with
one Euler factor per prime, whose logarithmic series has absolute-convergence
abscissa log 2. This resolves the parabolic limitation for this new object;
it does not supply exact log p timing, an operator trace, a Fredholm
determinant, canonical Riemann relevance or a formal Route pass.

## 1. Candidate identity and same-object ledger

The [version-1 card](candidate-card.md) preceded this proof. For every n>=2
define

\[
K_n=\max(1,\lfloor\log_2(n-1)\rfloor),\qquad
B(n,k)=\{d:2^k\le d<2^{k+1},\ d<n\},
\]
\[
b(n,k)=\sum_{d\in B(n,k)}1_{\{d\mid n\}},\qquad
a(n)=\sum_{k=1}^{K_n}b(n,k).
\tag{1}
\]

Binary integer length defines K_n without a prime table. For n>=3 these
blocks partition exactly 2,...,n-1; for n=2 the single block is empty.
Thus a(n) is the number of proper divisors in that range. The update uses
the local b(n,k), not an externally supplied primality flag or a(n).

Put X=(x,y), e_1=(1,0), alpha_n=1/(4K_n), and

\[
U(X)=\log\cosh x+\log\cosh y+\log\cosh(x+y),
\]
\[
f_{n,k}(X)=X+\alpha_n\nabla U(X)+2b(n,k)e_1.
\tag{2}
\]

The entire frozen symplectic base is

\[
M=\coprod_{n\ge2,\ 1\le k\le K_n}\mathbb R^4_{n,k},\qquad
\omega=dx\wedge d\xi_1+dy\wedge d\xi_2,
\]
\[
F(n,k,X,\xi)=
\left(n,k^+,f_{n,k}(X),Df_{n,k}(X)^{-T}\xi\right),
\tag{3}
\]

where k^+ is cyclic successor. All real configurations and momenta are
included before any periodic equations are imposed.

| Item | Owner in ASFS-20260915-CCS01 | Evidence / boundary |
| --- | --- | --- |
| Arithmetic source | The local tests (1) executed in (2) | Operational prime selection proved on the full carrier |
| Base geometry | Full four-dimensional M, canonical omega and exact map (3) | Global smooth symplectomorphism proved below |
| Symbolic relation | Integer, phase and witness observations of (3) | Constraint deformation; no full Markov coding claimed |
| Clock | Unit macrostep roof over (3) | No prime-dependent logarithmic roof |
| Flow | Mapping torus of this exact F and roof | Complete five-dimensional flow, not automatically Hamiltonian |
| Full periodic ledger | All configurations and all momenta, modulo cyclic phase | One primitive packet per prime; no composites |
| Monodromy | Derivative of this same F along these same packets | Four-dimensional hyperbolicity and repetitions explicit |
| Analytic convention | Ordinary unweighted Z of the full flow ledger | Absolute logarithmic series for Re(s)>log 2 |
| Operator / space / trace | NOT SUPPLIED | Nonzero geometric denominators alone do not create a trace formula |
| Measure | Canonical symplectic volume on each component | No finite invariant probability or trace measure |
| Later owner | Contact, Hamiltonian and quantum realizations DEFERRED | No Route-B coordinates |

The manifold is disconnected and noncompact; neither property is hidden.
The fixed term log cosh(x+y) couples both configuration equations and,
through the inverse-transpose derivative, both momentum equations. We do
not claim that this proves irreducibility under every possible coordinate
change. The construction is not 145's parabolic map with a separate
hyperbolic factor: its full configuration source and cotangent dynamics
are newly defined and audited here.

## 2. Question and claim boundary

Can a full higher-dimensional canonical realization of the divisor-symbolic
constraint preserve one prime packet while replacing the neutral directions
of a nonnegative Hénon cycle-sum realization?

For (3), the answer is an exact positive construction. The prime-only
classification covers every real state and every period. Hyperbolicity is
computed from the same complete periodic set, not borrowed from a control.

The nonclaims are exact prime-log periods, a uniquely natural arithmetic
geometry, elementary logarithmic-time primality computation, compactness,
connectedness, a global symbolic conjugacy, analytic continuation, a
transfer operator, a trace identity, target-zero/divisor matching and formal
Route success. A nonzero periodic-point denominator is only the removal
of one local obstruction, not evidence that an operator trace exists.

## 3. Source lineage, data and parameter provenance

The retained prior-work mechanism is the prime/composite admissibility
constraint: n survives precisely when none of d=2,...,n-1 divides it.
The specific deformation is

\[
\text{divisor-exclusion symbols}
\longrightarrow\text{autonomous local dyadic witness phases}
\longrightarrow\text{coupled two-variable drift}
\longrightarrow\text{canonical four-dimensional cotangent map}.
\]

This realizes the move from a low-dimensional nonlinear symbolic constraint
to a conservative geometric owner described in the
[prior-work guide](../../docs/prior_work/README.md). It does not assert a
conjugacy between the original causal sieve trajectory and (3).

All integers, all real states, the coefficients 1/4 and 2, the binary blocks,
and the fixed potential U were frozen before the proof. The normalization
alpha_n=1/(4K_n) is a uniform all-integer rule, not a parameter selected for
each prime. No prime table, Riemann zeros, von Mangoldt weights or orbit fit
is used. A complete scan still evaluates n-2 elementary divisor tests.

The all-integer carrier distinction documented by
[140's scope audit](../140-cyclic-divisor-counter/evidence/carrier-scope-audit.md)
is context, not transferred mathematical credit. Likewise
[145](../145-convex-witness-henon-sieve/paper.md) is the parabolic comparator,
not the source of this candidate's orbit or stability theorem.

## 4. Exact proof

### Proposition 1 — Global configuration diffeomorphisms and canonical lift

Each f_{n,k} is a smooth global diffeomorphism of R^2. The full map F is
a smooth symplectomorphism of M.

**Proof.** Write s(t)=sech^2(t)>0. Direct differentiation gives

\[
\nabla^2U(X)=
\begin{pmatrix}s(x)&0\\0&s(y)\end{pmatrix}
+s(x+y)\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{4}
\]

For every nonzero v this has v^T Hess(U) v>0. Therefore

\[
Df_{n,k}(X)=I+\alpha_n\nabla^2U(X)
\]

is positive definite with eigenvalues greater than 1. In particular it is
invertible everywhere, and integration along a line segment gives

\[
\bigl(f_{n,k}(X)-f_{n,k}(Y)\bigr)\cdot(X-Y)
\ge \|X-Y\|^2.
\tag{5}
\]

Thus f_{n,k} is injective. For any prescribed target Z, minimize

\[
\Phi_Z(X)=\tfrac12\|X\|^2+\alpha_n U(X)
+2b(n,k)x-Z\cdot X.
\tag{6}
\]

Since U>=0, the quadratic term dominates the linear terms at infinity.
Hence (6) is coercive and attains a minimum. Its Hessian is at least I,
so the minimum is unique, and its critical equation is f_{n,k}(X)=Z.
This proves surjectivity. The inverse function theorem, applied at every
point where Df is invertible, makes the unique inverse smooth.

For target (n,k^+,Q,eta), the inverse lift first takes
X=f_{n,k}^{-1}(Q) and then xi=Df_{n,k}(X)^T eta, while reversing the
phase. This is defined globally. For the canonical one-form
theta=xi_1 dx+xi_2 dy, direct substitution gives

\[
F^*\theta
=(Df(X)^{-T}\xi)^T Df(X)\,dX=\xi^T dX=\theta.
\tag{7}
\]

As omega=-d theta, equation (7) proves F^*omega=omega. A countable union of
Euclidean four-spaces is Hausdorff, second countable and smooth, and the
form is closed and nondegenerate on each component. QED.

### Proposition 2 — Complete configuration periodic set

There is a periodic configuration in the n-fibre if and only if n is prime.
For a prime fibre the only periodic configuration is X=0.

**Proof.** A full period m must return the phase, so m=rK_n for an integer
r>=1. Along any orbit, the first component satisfies

\[
x_{t+1}-x_t
=\frac{\tanh x_t+\tanh(x_t+y_t)}{4K_n}
+2b(n,k_t).
\tag{8}
\]

The hyperbolic tangent is strictly between -1 and 1 at every real argument.
Summing (8) over m=rK_n steps therefore gives

\[
x_m-x_0>-\frac r2+2r a(n).
\tag{9}
\]

If n is composite, then a(n)>=1, so the right side is positive. This
contradicts a period. The argument includes all real states, every phase
starting point and arbitrarily many repetitions.

If n is prime, every b(n,k)=0. All configuration steps equal
G(X)=X+alpha_n grad U(X). For X not equal to 0,

\[
X\cdot\nabla U(X)
=x\tanh x+y\tanh y+(x+y)\tanh(x+y)>0.
\tag{10}
\]

Indeed each summand is nonnegative, and at least one of the first two is
positive. Consequently

\[
\|G(X)\|^2-\|X\|^2
=2\alpha_n X\cdot\nabla U(X)
+\alpha_n^2\|\nabla U(X)\|^2>0.
\tag{11}
\]

A nonzero configuration cannot lie on a periodic orbit: its norm strictly
increases at every nonzero iterate, and a putative periodic orbit would
return to the same norm. The origin is fixed because grad U(0)=0.
This includes the empty-witness fibre n=2. QED.

### Proposition 3 — Full cotangent packets and hyperbolic monodromy

The entire periodic set of F is

\[
\{(p,k,0,0):p\text{ prime},\ 1\le k\le K_p\}.
\tag{12}
\]

For each prime p these points form exactly one primitive orbit of period
K_p. Every primitive monodromy and every repetition is nondegenerate and
hyperbolic.

**Proof.** A periodic full state projects to a periodic configuration.
Proposition 2 therefore forces a prime fibre and X=0. Put K=K_p. At the
origin,

\[
J_K=Df_{p,k}(0)
=I+\frac1{4K}\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\tag{13}
\]

Its two eigenvalues are 1+1/(4K) and 1+3/(4K), both greater than 1.
The exact momentum update along this configuration is xi'=J_K^{-T}xi.
For any positive m, neither eigenvalue of (J_K^{-T})^m equals 1.
Thus a full-state period forces xi=0. Conversely these states are periodic.
The cyclic phase rules out any positive period less than K.

At (X,xi)=(0,0), the cross derivative of the momentum equation with respect
to X vanishes because that equation is linear in xi. Thus the one-step
full derivative is diag(J_K,J_K^{-T}), and the primitive monodromy is

\[
P_p=\operatorname{diag}\bigl(J_K^K,(J_K^{-T})^K\bigr).
\tag{14}
\]

Define

\[
\Lambda_{1,K}=\left(1+\frac1{4K}\right)^K,\qquad
\Lambda_{3,K}=\left(1+\frac3{4K}\right)^K.
\tag{15}
\]

The four multipliers of P_p are Lambda_{1,K}, Lambda_{3,K} and their
reciprocals. The first two are strictly greater than 1, and the other two
strictly less than 1. For each repetition r>=1,

\[
\det(I-P_p^r)
=\prod_{j\in\{1,3\}}
\left(\Lambda_{j,K}^{r/2}-\Lambda_{j,K}^{-r/2}\right)^2>0.
\tag{16}
\]

This is the determinant on the full four-dimensional section. No omitted
momentum or neutral direction remains. QED.

Equation (12) follows from the complete periodic equation, not restriction
to a chosen zero section. In particular cotangent thickening introduces no
extra continuum of periodic momenta.

### Proposition 4 — Complete flow, ordinary zeta and its convergence boundary

The unit-roof quotient

\[
M_1=(M\times[0,1])/((z,1)\sim(Fz,0))
\tag{17}
\]

defines a complete five-dimensional suspension flow. Its full primitive
ledger is one oriented orbit gamma_p for each prime, with

\[
T_{\gamma_p}=K_p,\qquad T_{\gamma_p^r}=rK_p.
\tag{18}
\]

Its frozen ordinary unweighted zeta is

\[
Z(s)=\prod_p(1-e^{-sK_p})^{-1},\qquad
\log Z(s)=\sum_p\sum_{r\ge1}\frac{e^{-srK_p}}r.
\tag{19}
\]

The logarithmic series has exact abscissa of absolute convergence log 2.
It converges locally uniformly for Re(s)>log 2, where Z is holomorphic
and nonzero.

**Proof.** The global inverse of F permits any finite positive or negative
number of section crossings. The unit roof prevents finite-time
accumulation, so translation in the quotient is defined for all real time.
A closed flow orbit must cross the section an integral number of times,
and hence comes from a periodic base state. Conversely every primitive
base orbit supplies one primitive closed flow orbit, after identifying its
cyclic section points. Proposition 3 is complete. Reversed orientation is
not a second orbit of the fixed oriented flow. This proves (18) and (19).

For n>=3, the integers with K_n=j are precisely
2^j<n<=2^{j+1}, a set of 2^j integers. If sigma=Re(s)>log 2, then

\[
\sum_p e^{-\sigma K_p}
\le e^{-\sigma}+\sum_{j\ge1}2^j e^{-\sigma j}<\infty.
\tag{20}
\]

The first term separately allows n=2. Since K_p>=1, the absolute value
sum of all repetitions is bounded above by (20) divided by
1-e^{-sigma}. On any compact sub-half-plane this bound is uniform.
Exponentiating the convergent logarithm gives the analytic assertions.

For completeness, the lower bound is derived here without borrowing the
comparator's analytic claim. If sum_p 1/p were finite, then

\[
\prod_{p\le N}(1-1/p)^{-1}
\le\exp\left(2\sum_{p\le N}1/p\right)
\tag{21}
\]

would stay bounded, using -log(1-t)<=2t for 0<=t<=1/2. The finite Euler
product on the left expands into nonnegative reciprocal integers whose
prime factors are at most N. It therefore contains every 1/n for n<=N
by unique factorization. The unbounded harmonic sums contradict (21).
Thus sum_p 1/p diverges. At sigma=log 2 and every prime p>2,

\[
e^{-\sigma K_p}=2^{-K_p}>1/p.
\tag{22}
\]

The first repetition already diverges absolutely, as it does at every
smaller real part. Combined with (20), this proves the exact abscissa.
It does not prove or disprove an analytic continuation. QED.

## 5. Results and limits

This is one four-dimensional canonical owner with intrinsic prime-only
packets, no extra periodic momenta, logarithmic-order macroperiods,
hyperbolic full monodromy and its own ordinary zeta. The local degeneracy
of 145 is absent in this different object; none of its geometry has been
transferred.

For p>2,

\[
0<\log_2 p-K_p<1,\qquad
K_p=\frac{\log p}{\log2}+O(1).
\tag{23}
\]

The actual roof remains one. Both p=5 and p=7 have K_p=2, so no uniform
rescaling can make their two different exact logarithms into these equal
periods. This zeta is not the Riemann Euler product.

The nonvanishing determinants (16) remove a specific local denominator
obstruction. The ordinary weights in (19) are still one, not
1/det(I-P_p^r) or any trace weight. No operator, function space, trace
regularization, analytic continuation, Fredholm identity or target divisor
has been supplied. Replacing the scalar convention by such an analytic
owner would require a separately recorded frozen owner contract.

## 6. Controls and adverse findings

All comparators below were specified in the card. Each is a different
action used only to assess this object; its outputs are not substitute
owners.

| Control | Complete-state result | Interpretation |
| --- | --- | --- |
| Delete b everywhere | One hyperbolic K_n packet for every integer n | Arithmetic, not the cotangent geometry alone, selects primes |
| Replace b by the block cardinality | Only n=2 remains periodic | Every n>=3 has at least one tested integer; n=2's empty block is retained |
| Replace d dividing n by d dividing n+1 on the same blocks | Precisely the fibres with n+1 prime return, with period K_n | Relabelling the arithmetic relation changes the returning fibres |
| Remove log cosh(x+y) from U | Prime-only packets remain, with two equal expanding multipliers and their reciprocals | Coupling is real but is not the source of primality or mathematically necessary to encode the predicate |
| Retain all cotangent momenta | Every nonzero momentum is excluded by its actual period equation | No selected zero section or uncounted continuum |
| Count elementary witness work | n-2 divisor tests per complete K_n scan | The macroclock is not an elementary logarithmic-time primality algorithm |
| Replace local witnesses by general nonnegative integer constraints | Zero-witness fibres return; any full scan with a positive total is excluded | Generic finite constraint realizability limits claims of unique arithmetic naturalness |

Here each arithmetic control keeps the original K_n and geometry. For the
shifted test, every proper divisor of n+1, if one exists with n>=3, is at
most (n+1)/2<=n-1 and is therefore tested. At n=2 the empty block agrees
with primality of n+1=3. Thus the profile in the table includes all small
boundary cases.

For the uncoupled comparator, the Hessian is the positive diagonal matrix
diag(sech^2 x,sech^2 y), the prime norm still strictly increases away from
zero, and the composite x drift is bounded below by -1/(4K_n) per step.
The same full-state arguments apply, with J_K=(1+1/(4K))I. This does not
alter the frozen coupled map.

The general-constraint comparison uses integer-valued nonnegative
witnesses, or more generally a full-scan total at least 1 when nonzero.
Arbitrarily small positive real totals are not covered by (9). The finite
arithmetic witness gap and the chosen bounded drift are part of the
engineering, not consequences of a prime-log physical law.

There is no numerical cutoff or precision extrapolation: every substantive
claim above is a complete proof. The candidate has not been tested for
parameter robustness outside its fixed coefficients, and no such robustness
is claimed. Changed roofs, calibrator operators or cross-candidate
monodromies cannot supply missing analytic evidence.

## 7. Gate assessment

| Gate | Evidence for this exact candidate | Result | Remaining boundary |
| --- | --- | --- | --- |
| P0 | Full global canonical map and complete unit flow | ESTABLISHED | Disconnected noncompact base; no later Hamiltonian owner |
| A0 arithmetic mechanism | Local divisor witnesses, complete selectivity and adversarial controls | Operational endogenous prime selection ESTABLISHED | Generic constraint realization; canonical Riemann relevance OPEN |
| A0 clock component | Same-flow periods K_p and (23) | Logarithmic-order macroclock ESTABLISHED | Exact log p FAILS; natural clock provenance beyond batching OPEN |
| Owner A1 | Complete full-state packets, multiplicity one, repetitions and four-dimensional hyperbolicity | ESTABLISHED | No global hyperbolic or Markov coding theorem asserted |
| Owner A2 scalar layer | Exact full ordinary Z, abscissa log 2 | ESTABLISHED in the stated half-plane | Operator, trace, Fredholm identity, continuation and target divisor OPEN / NOT SUPPLIED |
| Formal Route A | Target/divisor protocol not evaluated | UNASSIGNED | Owner results are not formal coordinates |
| Route B | No readiness and no formal evaluation | NOT INVOKED | No B coordinate |

## 8. Conclusion and portfolio decision

**Advance:** the bounded full A1 and ordinary scalar A2 audit is complete
for ASFS-20260915-CCS01. Retain it as a prime-only genuinely
four-dimensional canonical positive construction with no parabolic
periodic directions.

**Fork** any change of force, roof or analytic-owner convention. The next
discriminating question is a same-object analytic trace/operator framework
or a genuinely different endogenous clock, not further attempts to
remove a unit multiplier that this map no longer has. No such operator
framework or clock change has been carried out here.

## Reproducibility / evidence index

All mathematical results are analytic proofs from the version-1 formulas.
There was no orbit computation, parameter scan, zero comparison or external
theorem search. The independent reviewer separately checked finitely many
integer witness/control profiles as a sanity check, not as proof of any
global classification; its exact scope and command are in the review.
The formulas, inequalities, boundary cases and multiplicity convention
above are the mathematical reproducibility record.

See the [candidate card](candidate-card.md), [claim ledger](claim-ledger.md),
[evidence record](evidence/README.md), [summary](README.md), and
[independent model review](evidence/review.md). Model review is not human
peer review or a substitute for the displayed proofs.
