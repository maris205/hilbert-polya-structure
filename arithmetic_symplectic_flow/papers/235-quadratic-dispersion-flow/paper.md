# Quadratic log dispersion preserves a global factor flow but not prime-exclusive returns

**Paper ID:** `235-quadratic-dispersion-flow`  
**Candidate ID:** `ANG-20260918-QDF01`  
**Date / status:** 2026-09-18; `GLOBAL OWNER ESTABLISHED; MIXED-PRIME RETURN — STOP / FORK`.  
**Formal Route coordinates:** `UNASSIGNED`. **Route B:** `NOT INVOKED`.

## Abstract

We test one new layer on the all-integer factor-interaction architecture:
replace logarithmic linear dispersion by its square while keeping the full
charge shell and ordered fusion/fission coefficients. This is a new action,
not a retiming of the earlier resonant candidate. Its interaction picture
is time-dependent, but uniform quadratic estimates and exact charge
cancellation still give a unique two-sided global mild flow on the complete
shell. Squared-log dispersion destroys linear multiplication resonance.
Nevertheless, the powers-of-6 sector remains invariant. An energy minimum
on its charge sphere exists by a compact form-domain embedding. We prove
that the multiplier is positive, recover the strong generator domain, and
obtain an actual mixed-prime periodic orbit of the full equation, with its
least physical period. Thus detuning this linear layer does not remove the
frozen source obstruction. The candidate stops without deleting modes or
altering its clock; naturalness and the remaining periodic ledger stay open.

## 1. Object, layer and lineage

The [version-1 card](candidate-card.md) precedes this audit. The precise
question is whether one fixed nonlinear-dispersion layer can preserve the
global-owner result while changing the mixed-prime return conclusion of
[233](../233-multiplicative-resonant-flow/paper.md). This is a dispersion
fork of that architecture, not a claimed independent source mechanism.

| Item | Owner in QDF01 | Boundary |
| --- | --- | --- |
| Carrier | Entire Q=1 shell in E below, with E norm topology | No energy or finite-support restriction of the main flow |
| Action | Mild equation (1) with D=L squared | Not the 233 action or a renamed character flow |
| Arithmetic source | All ordered factor triples (a,b,ab), coefficient 1/(ab) | Genuine interaction; design naturalness OPEN |
| Physical time | The parameter t of equation (1) | No inserted roof or target log-prime period |
| Packets | All nonconstant primitive point orbits, modulo actual time translation | Repeats traverse the same orbit; no phase quotient |
| Geometry | Infinite-dimensional mode action and its transformation groupoid | Classical A0/A1/A2 NOT APPLICABLE |
| Analytic/quantum owner | NOT SUPPLIED | No trace, zeta, determinant or target spectrum |

The preserved [prior-work arrow](../../docs/prior_work/README.md) is the
proper-divisor prime/composite observable, replaced by its complete
factor-triple network and then by coherent factor/product exchange.
Squared-log dispersion is an additional fixed deformation of that mode
equation. We assert no chronological-sieve, Logistic or Henon conjugacy.
The source and dispersion are all-integer designs, not prime tables,
prime-specific weights, von Mangoldt inputs or zero-data fitting.

The layered proof reuses verified estimates by checking their unchanged
inputs. It does not reuse a gate verdict or infer that added complexity
improves prime selection. The new action and its actual returns are proved
separately below.

## 2. Exact definitions and domains

Put w_n=log n and define

\[
E=\ell^2(w_n),\qquad Q(z)=\sum_{n\ge2}w_n|z_n|^2,
\qquad\mathcal M=Q^{-1}(1).
\]

Let

\[
(Lz)_n=w_nz_n,\quad (Dz)_n=w_n^2z_n,\quad
(R_tz)_n=e^{-itw_n^2}z_n,
\]
\[
D(D)=\left\{z:\sum_{n\ge2}w_n^5|z_n|^2<\infty\right\}.
\]

The prescribed full-state equation is

\[
z(t)=R_tz_0-i\int_0^t R_{t-s}N(z(s))\,ds,\qquad z_0\in E,\tag{1}
\]
\[
N_n(z)=\frac1{2n}\sum_{\substack{a,b\ge2\\ab=n}}z_az_b
       +\sum_{b\ge2}\frac{z_{nb}\bar z_b}{nb}.
\]

All factor pairs are ordered, including the diagonal. Define

\[
B(z)=\sum_{a,b\ge2}\frac{\bar z_{ab}z_az_b}{ab},\quad
C(z)=\operatorname{Re}B(z),\quad
K(z)=\sum_{n\ge2}w_n^2|z_n|^2.\tag{2}
\]

K is finite on the form space
Y={z:sum w_n squared |z_n| squared is finite}; it need not be finite on E.
Here "form space" means the domain of the Hamiltonian quadratic K in the
unweighted coordinate pairing. It is not the spectral form domain of D
as an operator on the weighted Hilbert space E, which instead requires
sum w_n cubed |z_n| squared to be finite.
The formal Hamiltonian is H=K+C, with ambient weak form
i sum dz_n wedge d(bar z_n). The charge shell is not declared symplectic.
The global flow is defined by (1), not by assuming a strong vector field
or a finite Hamiltonian at every point of E.

We also use the distinct character symmetry

\[
(S_sz)_n=e^{-isw_n}z_n.\tag{3}
\]

Its parameter s is not identified with the physical time of (1).

## 3. What survives detuning, and what does not

### Lemma 1 — Uniform quadratic bounds and charge cancellation

Set U=sum_(n>=2) n^(-2) and V=sum_(n>=2) [n squared log n]^(-1).
Both are finite. Write N=A(z,z)+F(z,z), where

\[
A_n(z,y)=\frac1{2n}\sum_{ab=n}z_ay_b,\qquad
F_n(z,y)=\sum_{b\ge2}\frac{z_{nb}\bar y_b}{nb}.
\]

Then

\[
\|A(z,y)\|_E\le\sqrt{UV/2}\|z\|_E\|y\|_E,
\quad
\|F(z,y)\|_E\le\sqrt{UV}\|z\|_E\|y\|_E.\tag{4}
\]

In particular N is real-smooth and locally Lipschitz on E, uniformly on
fixed norm balls. The cubic C is real-smooth and absolutely convergent, and

\[
DC(z)[h]=2\operatorname{Re}\sum_n\bar h_nN_n(z),\quad
\operatorname{Im}\sum_n w_n\bar z_nN_n(z)=0,\quad
N(S_sz)=S_sN(z).\tag{5}
\]

**Proof.** Normalize coordinates by x_n=sqrt(w_n)z_n. The squared
coefficient sums for A and F are respectively

\[
\sum_{a,b}\frac{w_{ab}}{4a^2b^2w_aw_b}=UV/2,
\qquad
\sum_{n,b}\frac{w_n}{n^2b^2w_{nb}w_b}\le UV.
\]

Cauchy--Schwarz on the coefficient tensors proves (4). Applying the same
bounds to absolute coordinate values justifies absolute convergence of
B=2 sum bar z_n A_n(z,z), since E embeds in ordinary ell squared.
Continuous multilinear differentiation proves the first formula in (5).

For the charge identity let T_(a,b)=bar z_(ab) z_a z_b. The weighted
pairing with N equals

\[
\frac12\sum_{a,b}\frac{w_a+w_b}{ab}T_{a,b}
+\sum_{a,b}\frac{w_a}{ab}\overline{T_{a,b}}
=\frac12\sum_{a,b}\frac{w_a+w_b}{ab}
(T_{a,b}+\overline{T_{a,b}}),
\]

which is real. Absolute convergence follows from (4) and the E inner
product. Finally w_(ab)=w_a+w_b proves S-equivariance term by term. These
arguments use the charge and interaction, not the choice of D. They
re-establish the unchanged estimates from 233 for this new owner. ∎

In contrast, N is **not** equivariant under R. For example a pure n input
generates its n-squared fusion component, whose input phase is
exp(-2it w_n squared), whereas R_t at n squared has phase
exp(-4it w_n squared). They differ at generic t. Thus the autonomous
interaction-picture equation of 233 is unavailable here. Loss of this
linear resonance does not imply loss of the character symmetry (5).

### Theorem 2 — Global full-shell mild action

For every z_0 in E, equation (1) has a unique mild solution for all real
times. It preserves Q and defines a jointly continuous action on E and
on the entire shell M.

**Proof.** R_t is a strongly continuous isometric group on E, by finite
sequence approximation. Set u(t)=R_(-t)z(t) and

\[
J_t(u)=R_{-t}N(R_tu).
\]

Equation (1) is equivalent to the non-autonomous E-valued ODE

\[
\dot u(t)=-iJ_t(u(t)),\qquad u(0)=z_0.\tag{6}
\]

The function (t,u) maps continuously to J_t(u). Isometry of R and (4)
give uniform local Lipschitz and boundedness estimates on every E ball,
independent of time. Picard iteration gives a unique local continuously
differentiable E solution. Crucially, charge can be differentiated along
(6), even when z_0 is outside D(D):

\[
\frac{d}{dt}Q(u(t))
=2\operatorname{Re}\langle u,-iJ_t(u)\rangle_E
=2\operatorname{Im}\langle R_tu,N(R_tu)\rangle_E=0.\tag{7}
\]

Here the inner product is conjugate-linear in the first slot. The norm
is therefore fixed. Uniform bounds on the right side of (6) make a
solution Cauchy at any finite endpoint; its limit in E restarts the local
construction. This proves continuation in both directions and Q(z)=Q(u).

Time translation of a mild solution satisfies the same autonomous
equation (1) with its new initial state, as follows by splitting the
Duhamel integral and using the group law of R. Uniqueness therefore gives
Phi_(t+s)=Phi_t composed with Phi_s. No autonomous flow law is assumed
for (6) itself. Local Lipschitz dependence, the conserved norm and strong
continuity of R give joint continuity on bounded time intervals. ∎

The transformation groupoid has all z in M as objects and (z,t) as arrows
from z to Phi_t(z). Generic E trajectories have only the mild regularity
just proved. We do not claim D(D)-regularity or finite K for every state.

The interaction is genuine: at a pure n state, the (n squared) component
of N equals \(z_n^2/(2n^2)\), so the pure-mode set is not invariant under
the full nonlinear action. Neither detuning nor existence of a diagonal
comparison group turns the integer label into a static classifier.

## 4. The invariant mixed-prime probe

Let ell=log 6 and identify the complete subspace E_6 with x_k=z_(6^k),
k>=1. In these coordinates

\[
Q_6(x)=\ell\sum_{k\ge1}k|x_k|^2,\quad
K_6(x)=\ell^2\sum_{k\ge1}k^2|x_k|^2,\quad
B_6(x)=\sum_{i,j\ge1}6^{-(i+j)}\bar x_{i+j}x_ix_j.\tag{8}
\]

### Lemma 3 — Full-flow invariance and a uniform cubic bound

E_6 is invariant under the full mild action. On Q_6=1,

\[
|C_6(x)|\le A_6:=\frac1{25\ell^{3/2}},\qquad K_6(x)\ge\ell.\tag{9}
\]

**Proof.** Both R and S preserve E_6. Fusion of supported inputs stays
on powers of 6. In a nonzero fission summand, nb=6^r and b=6^s force
n=6^(r-s), with r>s because n>=2. Hence N(E_6) is contained in E_6;
uniqueness in Theorem 2 gives actual-flow invariance. On the Q-unit
sphere, |x_k|<=ell^(-1/2), so the absolute cubic is bounded by
ell^(-3/2) sum_(i,j>=1) 6^(-i-j)=A_6. The quadratic inequality follows
from k squared>=k. ∎

E_6 is only a probe in the full carrier, never a replacement for it. Every
active integer 6^k has both prime factors 2 and 3, so any nonconstant
periodic orbit in this sector violates the frozen single-prime support
interpretation.

## 5. A compact variational layer produces an actual periodic packet

### Theorem 4 — Attained energy minimum and physical least period

The constrained energy

\[
h_6=\inf\{K_6(x)+C_6(x):Q_6(x)=1,\ K_6(x)<\infty\}\tag{10}
\]

is attained at a state u in E_6. It obeys h_6<ell, belongs to D(D), and
satisfies the full coordinate equation

\[
Du+N(u)=\omega Lu,\qquad
\omega=K_6(u)+\tfrac32C_6(u),\qquad
\ell-\tfrac32A_6\le\omega<\ell.\tag{11}
\]

In particular omega>0 and u_6 is nonzero. The curve

\[
z(t)=S_{\omega t}u\tag{12}
\]

is an actual nonconstant strong solution of the full equation (1). Its
least positive physical return time is

\[
T=\frac{2\pi}{\omega\log6},\qquad
\{t:\Phi_tu=u\}=T\mathbb Z.\tag{13}
\]

**Proof.** The bound (9) shows h_6>=ell-A_6. The pure 6 state has Q=1,
K=ell and C=0, so h_6<=ell. A minimizing sequence therefore has bounded
K_6, since K_6<=H_6+A_6 on the constraint.

Let Y_6 be the Hilbert form space with squared norm K_6. A K-bounded
sequence has a weakly convergent subsequence in Y_6. Its embedding into
E_6 is compact: for every integer J>=1,

\[
\ell\sum_{k>J}k|x_k|^2
\le\frac{K_6(x)}{(J+1)\ell}.\tag{14}
\]

Finite-coordinate convergence and this uniform tail bound give strong
E_6 convergence. Thus Q=1 is retained at the limit u, C_6 converges by
Lemma 1, and lower semicontinuity of K_6 proves attainment of (10).
This is compactness of the form-space inclusion, not compactness of the
Q-unit sphere in its own norm.

Strict improvement over the pure state follows from the exact trial

\[
x_1=\sqrt{(1-2\ell\varepsilon^2)/\ell},\quad
x_2=-\varepsilon,\quad x_k=0\ (k\ge3),
\quad 0<\varepsilon<(2\ell)^{-1/2}.
\]

It has Q=1 and

\[
H_6(x)=\ell+2\ell^2\varepsilon^2
-\frac{\varepsilon(1-2\ell\varepsilon^2)}{36\ell}<\ell\tag{15}
\]

for sufficiently small positive epsilon, because the right derivative
at zero is -1/(36ell). Consequently C_6(u)<0, since K_6(u)>=ell.

H_6 and Q_6 are continuously differentiable real functionals on Y_6,
and DQ_6(u) is nonzero. The constraint multiplier therefore yields
DH_6(u)=omega DQ_6(u) for some real omega. This can also be obtained
by decomposing directions into the kernel of DQ and one radial direction.
Testing single-coordinate directions gives, initially as a form identity,

\[
(k\ell)^2u_{6^k}+N_{6^k}(u)=\omega k\ell u_{6^k}.
\]

Outside E_6 all three terms vanish by invariance. Evaluating the real
derivative on u, using degree 2 of K and degree 3 of C, gives
2K_6+3C_6=2omega, which proves the formula in (11). It is a finite
multiplier, because K_6 and C_6 are finite at the minimizer. The lower
bound follows from (9); the upper bound follows from
omega=h_6+C_6(u)/2<h_6<ell. Since ell>1 and A_6<1/25, omega>0.

There is no unbounded-domain inference from the form identity alone.
For y=log n>2|omega|, that identity gives

\[
\tfrac12 y^2|u_n|\le|(y^2-\omega y)u_n|=|N_n(u)|.
\]

Since N(u) is in E, it follows that sum y^5|u_n| squared is finite
on this tail. Only finitely many n lie below the threshold, so u belongs
to D(D). In particular Lu is in E, and (11) is a strong E identity.

Furthermore K_6(u)=h_6-C_6(u)<ell+A_6<2ell. If u_6 were zero,
every supported exponent would be at least 2 and K_6>=2ell Q_6=2ell,
a contradiction. Hence u_6 is nonzero. The strict C_6(u)<0 also shows
that the minimizer is not just a pure-mode state with the coupling ignored.

Finally D commutes with S, and Lemma 1 gives N(S_su)=S_sN(u).
Differentiating (12) in E is legitimate at this domain-valued u and gives

\[
i\dot z(t)=\omega Lz(t)=Dz(t)+N(z(t)).
\]

Variation of constants with R gives (1), and Theorem 2 identifies it
with the actual full mild action. All active modes are 6^k. A return at
t occurs exactly when omega ell k t is in 2pi times the integers for
every active k. The nonzero k=1 coordinate forces omega ell t to be
in 2pi times the integers, which is also sufficient for all k. This
proves (13), nonconstancy and the physical least-period claim. ∎

Every r-fold traversal has time rT and is a repetition of this same
orbit. It is not a new packet with label 6^r. Neither uniqueness of the
minimizer nor classification of the other periodic orbits follows.

## 6. Controls and the actual structural boundary

| Test | Exact outcome | What it does not establish |
| --- | --- | --- |
| Replace L by D=L squared | R-equivariance of N fails; the interaction ODE becomes time-dependent | Loss of multiplicative character symmetry or prime-selective returns |
| Retain weighted charge Q | Charge cancellation survives and bounds every E solution | A target prime-log clock or strong regularity for all states |
| Zero-coupling control | Pure n mode has period 2pi/(log n) squared, including composites | A result for the actual nonlinear minimizer |
| Actual nonlinear minimizer | H_6<log6 and C_6<0; full nonlinear equation owns the periodic packet | A perturbative approximation or a finite-cutoff orbit |
| Keep only prime-power sectors | Deletes genuine mixed-prime states from M | An allowed repair of QDF01 |
| Use S as the main action | Changes the owner and physical clock | A shortcut to the actual mild equation |

The result is not a no-go theorem for every detuning or every dispersive
arithmetic equation. For this fixed fork, however, the new dispersion does
not alter the factor-support closure, character symmetry, or compact
constrained-energy mechanism that produces the mixed-prime return.
The [234 class audit](../234-multiplicative-sector-obstruction/candidate-card.md)
addresses a different variation: bounded symmetric interaction coefficients
with linear logarithmic dispersion. Its theorem is not assumed in this proof.

These two bounded tests distinguish numerical coefficient adjustment from
the structural conditions a future design must actually examine. Breaking
one of those conditions is not by itself a proof of success. A future
candidate must retain the prime-symbolic lineage and establish its full
owner, source and physical returns anew.

## 7. Gate assessment and decision

| Obligation | QDF01 evidence | Status / limit |
| --- | --- | --- |
| T0 | Theorem 2 constructs the complete norm-topological action and groupoid | ESTABLISHED for the mild owner |
| T1 | Explicit factor feedback and unchanged physical time | Design naturalness OPEN; no prime-length theorem |
| T2 | Theorem 4 constructs an actual mixed-prime primitive with exact least time | Frozen prime-support criterion FAIL; remainder NOT CLASSIFIED |
| T3 | No trace, determinant, zeta or later spectral object | NOT ADVANCED |
| Classical A0/A1/A2 | No finite-dimensional symplectic suspension | NOT APPLICABLE |
| Formal Route / B | No formal evaluation | UNASSIGNED / NOT INVOKED |

**Decision: STOP / FORK.** Keep the global-owner and domain-sensitive
variational arguments as reusable proof methods. Do not promote this
candidate past its intrinsic mixed-prime return obstruction. The full
shell, coefficients, dispersion and physical time remain unchanged, so
the same-object ledger is intact. Repeated dispersion tuning is not the
next step authorized by this bounded layer test.

## Reproducibility, limitations and disclosure

All exact inputs appear in the [card](candidate-card.md), all claims in
the [ledger](claim-ledger.md), and technical/mechanical verification in the
[evidence record](evidence/README.md). The proof uses no floating-point
calculation, orbit cutoff, numerical minimizer or external dataset. The
trial in (15) and tail in (14) are exact arguments, not simulation output.
The value of h_6 or omega is not numerically computed, and no uniqueness,
stability, full periodic classification or naturalness theorem is claimed.

Data availability: definitions and proofs are contained in this package.
Ethics: no human subjects or private data. Contributions: AI-assisted
formalization, proof drafting and bounded technical checking; no human
CRediT role is inferred. Funding and conflicts were not supplied. This is
an internal research record, not external peer review, publication readiness
or a correctness certificate. ARS informed explicit dependency, counterexample
and evidence boundaries, not research authority or formal Route status.
