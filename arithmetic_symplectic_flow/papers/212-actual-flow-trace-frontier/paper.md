# Actual-time regularization: covariance and limits of temporal smoothing

**Portfolio ID:** ASFS-FRONTIER-20260916-22  
**Research date:** 2026-09-16  
**Status:** PORTFOLIO ADVANCE — FULL-STATE REGULARIZED TRACE; TWO TIME-FILTER STOPS; LOCALIZATION AND NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

On the unchanged fixed Hilbert space of full-quotient scalar
observations, an explicit positive injective covariance produces an
ordinary trace-class regularization of actual time pullback. Its dense
range still separates every state. The resulting continuous trace
contains mixed-state correlations and depends on sampling; it is not
the atomic positive-time periodic-orbit distribution. Two short tests
explain why simpler time filtering does not automatically supply the
missing trace: every nonzero-mass admissible convolution on this exact
Hilbert space stays noncompact even after finite-rank correction, and
an external periodic-measure L2 control stays noncompact after removal
of all circle constants whenever its filter transform is nonzero
somewhere. The external control does not decide zero-mass filtering
on the full-state space. Intrinsic localization, arithmetic naturalness
and any determinant or spectral identification remain unproved.

## 1. Three questions, with observation owners kept separate

The [version-1 scope](candidate-card.md) predates these short proofs.
The geometric source is the all-integer multiplicative monoid algebra,
its nonunit ideal I and the declared quotient I/I^2. Products of
two nonunits span exactly the composite coordinates, so its surviving
atom classes q_a are derived from integer factorization. The source
arrow is proper-factor symbolic admissibility -> indecomposable
arithmetic observable -> positive-cone geometry -> actual-flow
observation. The [prior-work guide](../../docs/prior_work/README.md)
provides ancestry, not an imported theorem or a Logistic/Henon
conjugacy.

Retain the entire [194 geometry](../194-rapid-decay-cone-completion/paper.md):

\[
 E=\{v:\sum_a a^k|v_a|<\infty\text{ for every integer }k\ge0\},
 \quad\widehat P=E_+\setminus\{0\},\quad
 (Dv)_a=a v_a,\quad\widehat X=\widehat P/\langle D\rangle,
 \quad\phi_t[v]=[e^t v].
 \tag{1}
\]

All weighted-norm topology, quotient topology, finite and infinite
supports, and actual time are unchanged. Each singleton support gives
one circle C_a of least time L_a=log a and all repeats. Every
mixed support is an actual aperiodic state. The complete section and
its genuine return roof remain those of 194; no time unit is changed.

The fixed Hilbert H of
[204](../204-quotient-orbit-feature-hilbert/paper.md) consists of
actual bounded continuous scalar functions on all X_hat. It contains
constants and separates all states. Its specific closed-kernel
quotient norm satisfies

\[
 \|f\|_\infty\le\sqrt{B_0}\|f\|_H,\quad B_0\le1,
 \qquad R_t f=f\circ\phi_t,\quad \|R_t\|\le e^{|t|/2},
 \tag{2}
\]

with a strongly continuous group. Its norm is nonunitary, and its
unsmoothed time operators are noncompact. Root's 209 contract adds
one specific covariance to this same H. SC22-TC asks whether time
convolution alone works on exactly H. SC22-PF is a deliberately
different, EXTERNAL REPRESENTATION CONTROL on a probability-based
L2 space from 205. That space already loses mixed-state observations;
it cannot rescue or silently replace H.

## 2. SC22-TC: nonzero-mass time smoothing stays noncompact on H

Let eta be measurable and complex with

\[
 M_\eta=\int_{\mathbb R}|\eta(t)|e^{|t|/2}\,dt<\infty,
 \qquad m_\eta=\int_{\mathbb R}\eta(t)\,dt\ne0.
 \tag{3}
\]

**Proposition TC.** The strong integral
S_eta f=integral eta(t)R_t f dt defines a bounded operator on the
exact H, of norm at most M_eta. Neither S_eta nor S_eta+K for
any bounded finite-rank K is compact or ordinary Hilbert trace class.

**Proof.** For each f, strong continuity of R_t f gives a strongly
measurable integrand, with integrable norm bounded by
abs(eta(t)) exp(abs(t)/2) norm(f). Its Hilbert-valued integral exists
and has the asserted bound. This is an integral applied to each
vector; operator-norm continuity of t->R_t is not assumed.

For each actual circle define the bounded linear functional

\[
 \ell_a(f)=\frac1{L_a}\int_0^{L_a}f([e^r q_a])\,dr,
 \qquad |\ell_a(f)|\le\sqrt{B_0}\|f\|_H.
 \tag{4}
\]

Translation around the same time circle gives ell_a R_t=ell_a.
By 204's explicit functions f_b with f_b restricted to C_a equal
to delta_ab, the functionals are linearly independent. This uses
neither global invariance of f_b nor the existence of arbitrary
circle Fourier modes in H.

To make the relevant Hilbert subspace explicit, let k_x be 204's
evaluation vector, so f(x)=<f,k_x> with first-linear inner product.
That proof gives norm continuity of x->k_x. Therefore

\[
 z_a=\frac1{L_a}\int_0^{L_a}k_{[e^r q_a]}\,dr\in H,
 \qquad \ell_a(f)=\langle f,z_a\rangle_H.
 \tag{5}
\]

The real normalized circle integral has the correct conjugation in
the second slot. The vectors z_a are linearly independent by the
same f_b tests. Let E_0 be their closed linear span, an infinite-
dimensional subspace, and let Pi_0 be its orthogonal projection.
Bounded functionals commute with the strong integral, first for
simple integrands and then by their norm limit. Thus

\[
 \ell_a(S_\eta f)=m_\eta\ell_a(f),\qquad
 \langle S_\eta f,z\rangle=m_\eta\langle f,z\rangle
 \quad(z\in E_0),\qquad
 \Pi_0 S_\eta\big|_{E_0}=m_\eta I_{E_0}.
 \tag{6}
\]

The middle equality extends from finite linear combinations to their
closure. It does not assert that E_0 is invariant under S_eta;
the final statement is an orthogonal compression.

For any bounded finite-rank K, the kernel of K restricted to E_0
has finite codimension in E_0 and is infinite dimensional. Choose
an orthonormal sequence u_n in that kernel. Equation (6) gives

\[
 \Pi_0(S_\eta+K)u_n=m_\eta u_n.
 \tag{7}
\]

These images have pairwise distance sqrt(2) abs(m_eta)>0, so they
have no convergent subsequence. A compact S_eta+K followed by a
bounded projection would send the bounded sequence to a sequence
with a convergent subsequence, a contradiction. Taking K=0 covers
S_eta itself. Ordinary Hilbert trace class would imply compactness:
its finite-rank approximants converge in trace norm and hence in
operator norm. Thus it too is excluded. QED.

Decision: STOP the nonzero-mass time-filter class on this frozen H,
including every finite-rank correction. The obstruction is infinitely
many independent invariant circle means, not only one global constant
function. No finite-rank subtraction can erase all those constraints.
The proof does not infer a full Fourier decomposition of H and does
not borrow the invariant measure space of 205.

When m_eta=0, (6) only says that this compression is zero. It gives
no compactness decision for nontrivial zero-mass filters on H; that
case remains OPEN here. The zero filter itself gives the zero compact
operator, so an unqualified claim against every time filter would
already be false. More generally the argument works for any Hilbert
representation with infinitely many bounded independent invariant
functionals: it is not a prime-specific naturalness theorem.
Reservation 210 remains uncreated.

## 3. SC22-PF: removing each circle's constant mode still fails in a control

This is an EXTERNAL REPRESENTATION CONTROL, not a new faithful
full-state candidate. The [205 classification](../205-invariant-measure-support/paper.md)
supplies normalized actual time measures lambda_a on C_a. Freeze

\[
 Z=\sum_a2^{-a},\quad w_a=2^{-a}/Z>0,
 \quad\mu=\sum_aw_a\lambda_a,
 \quad H_\mu=L^2(\widehat X,\mu).
 \tag{8}
\]

The sum Z is finite and positive by the all-integer geometric-series
bound. For actual Borel representatives the norm is

\[
 \|f\|_{H_\mu}^2
 =\sum_a\frac{w_a}{L_a}\int_0^{L_a}|f([e^r q_a])|^2\,dr.
 \tag{9}
\]

Mixed states are still in X_hat but this norm ignores their values.
205 exhibits a nonzero continuous bounded function whose class in
every such space is zero. Equation (8) is not a new interpretation
of the norm in (2).

On each circle let Qf be its normalized circle mean, viewed as a
constant function there. Cauchy--Schwarz gives norm(Qf)<=norm(f).
Circlewise integration shows Q^2=Q and Q is self-adjoint, so P=I-Q
is the orthogonal projection removing all per-circle constants. It
leaves every nonconstant Fourier mode in every circle. This projection
is part of the frozen external control, not a deletion performed on H.

The actual pullbacks V_t f=f composed with phi_t are unitary on
H_mu. They are strongly continuous as well. For an arc indicator on
one circle the squared norm of its translation difference is its
weighted normalized symmetric-difference length, tending to zero as
t tends to zero. Finite linear combinations of such indicators in
finitely many circles are dense: truncate the circle norm sum, and
approximate Borel sets on a circle in measure by finite unions of
arcs. The latter approximable sets form a sigma algebra (use finite
unions, complements and finite-measure truncation of countable unions)
containing the arcs, hence all Borel sets; simple-function approximation
then gives L2 density. Unitarity extends strong continuity from this
dense class to every vector.

For complex eta in L1(R), the strong integral
S_eta^mu f=integral eta(t)V_t f dt therefore exists with norm at
most norm(eta)_1. Freeze the plus-sign Fourier convention

\[
 \widehat\eta(\omega)=\int_{\mathbb R}\eta(t)e^{i\omega t}\,dt
 \tag{10}
\]

and assume it is nonzero at at least one real frequency. This is
the stated hypothesis, not an inference from an unchecked Fourier
uniqueness theorem.

**Proposition PF.** Under this hypothesis S_eta^mu P is noncompact
and is not ordinary Hilbert trace class.

**Proof.** The Fourier transform in (10) is continuous. Indeed
split the difference at abs(t)<=T; its compact-time part is bounded
by T abs(omega-omega_0) norm(eta)_1, and the remaining part by
2 integral_(abs(t)>T) abs(eta(t))dt. First choose T for the tail
and then choose the frequency difference. This proves continuity
without a moment assumption. A nonzero value therefore gives a
nonzero frequency omega_* at which the transform is nonzero, even
if the initially supplied value was at zero.

Every atom circle and every integer k give a normalized vector

\[
 e_{a,k}([e^r q_b])=
 \begin{cases}
 w_a^{-1/2}e^{2\pi i k r/L_a},&b=a,\\
 0,&b\ne a.
 \end{cases}
 \tag{11}
\]

Take value zero on the mixed locus to obtain a Borel representative.
The expression is well defined on the actual time circle. Equation
(9) proves unit norm; distinct atom supports are orthogonal, and
distinct k on one circle are orthogonal by direct exponential
integration. For k not zero, P e_(a,k)=e_(a,k). Actual time gives

\[
 V_t e_{a,k}=e^{i\omega_{a,k}t}e_{a,k},\qquad
 \omega_{a,k}=\frac{2\pi k}{\log a},\qquad
 S_\eta^\mu P e_{a,k}=\widehat\eta(\omega_{a,k})e_{a,k}
 \quad(k\ne0).
 \tag{12}
\]

Choose distinct derived atoms a_n tending to infinity; elementary
integer infinitude suffices, with no prime-distribution estimate.
Let k_n be a nearest integer to omega_* log(a_n)/(2 pi).
Eventually k_n is nonzero and

\[
 \left|\frac{2\pi k_n}{\log a_n}-\omega_*\right|
 \le\frac{\pi}{\log a_n}\longrightarrow0.
 \tag{13}
\]

Continuity of (10) makes the absolute values of the corresponding
eigenvalues bounded below by a positive constant for all sufficiently
large n. The images of the orthonormal e_(a_n,k_n) are orthogonal
with norms bounded away from zero; hence they admit no convergent
subsequence. This disproves compactness, and ordinary trace class
is excluded as in Proposition TC. QED.

The positive weights tending rapidly to zero do not repair this
obstruction: normalization in (11) cancels them. Removing every
circle's constant mode also does not repair it, because (13) uses
nonzero modes at a fixed nonzero limiting frequency, not zero modes.
The proof does not need completeness of the displayed Fourier family;
the explicit orthonormal sequence alone is sufficient.

As a concrete zero-mass control, eta=1_[0,1]-1_[1,2] has integral
zero but hat_eta(pi)=4i/pi, so Proposition PF applies. That example
is a result on H_mu only. No conclusion about its smoothing operator
on 204 H follows: the latter has not been shown to contain the full
family (11). If the transform is zero at every frequency, this
screen makes no claim beyond its frozen hypothesis; in particular
eta=0 produces the zero operator. The zero-mass case on H remains
OPEN, not decided by an attractive comparator calculation.

Decision: STOP the projected periodic-measure filter contract under
its exact transform hypothesis. It is a reusable external control,
not a new candidate, natural arithmetic theorem or rescue of full-state
observation. Reservation 211 remains uncreated.

## 4. 209: an actual-flow trace with an explicit faithful regularizer

[209 / AQC-20260916-QCV01](../209-full-state-covariance-trace/paper.md)
has status ADVANCE — INJECTIVE FULL-STATE TRACE-CLASS REGULARIZATION;
SCOPED STOP AS AN UNREGULARIZED CLOSED-ORBIT TRACE; NATURALNESS OPEN.
Its exact H, evaluation vectors, kernel and R_t are those of 204,
not H_mu of Section 3 and not the s-dependent spaces of 201.

The new sampling rule lists every nonzero positive finite rational
vector once, ordered by its frozen finite-height then lexicographic
tuple rule; let v_n be the list and x_n=[v_n]. Deck-equivalent
repetitions of x_n are retained. Truncating the tails of finitely
many constrained weighted norms and then rationally approximating the
remaining positive coordinates proves density in the full P_hat.
The continuous surjective quotient map gives density of the list
in the existing X_hat topology. Thus

\[
 \nu=\sum_{n\ge1}2^{-n}\delta_{x_n}
 \tag{14}
\]

has full topological support. It is not invariant: any atom of
positive mass has arbitrarily many distinct time translates, which
could not all carry the same positive mass in a finite measure.
The carrier is not restricted to the list or replaced by L2(nu).
Every infinite-support state remains an argument of every actual
function in H.

With first-linear inner product and rank-one convention
(u tensor v)f=<f,v>u, freeze

\[
 C=\sum_{n\ge1}2^{-n}(k_{x_n}\otimes k_{x_n}),\qquad
 A_t=R_t C.
 \tag{15}
\]

Each rank-one trace norm is at most B_0 2^(-n). The full series
therefore converges in ordinary trace norm with tail at most
B_0 2^(-N). It is positive and self-adjoint, and

\[
 \langle Cf,f\rangle=\sum_n2^{-n}|f(x_n)|^2.
 \tag{16}
\]

If Cf=0, continuity and density force f=0 on all states; hence C
is injective. Self-adjointness gives dense range. The range also
separates all states: for x different from y, the vector
h=k_x-k_y is nonzero, and (16) is strictly positive at h.
The actual function Ch then satisfies
(Ch)(x)-(Ch)(y)=<Ch,h>>0. Neither surjectivity nor a bounded inverse
is claimed; an injective compact operator on infinite-dimensional H
cannot have a bounded everywhere-defined inverse.

Actual time pullback gives the trace-class family

\[
 \|R_t C\|_1\le e^{|t|/2} B_0,\qquad
 T(t)=\operatorname{Tr}(R_t C)
     =\sum_n2^{-n}\kappa(\phi_t x_n,x_n).
 \tag{17}
\]

The order of the two kernel arguments follows from the actual
rank-one trace <R_t k_x,k_x>; there is no simultaneous shift or
unjustified complex conjugation. Strong continuity on each rank-one
term plus the trace-norm tail uniform on compact time intervals proves
trace-norm continuity of A_t. Separately, bounded evaluation vectors
give abs(kappa(phi_t x_n,x_n))<=B_0 for every real t. Consequently
T is bounded and continuous, with a scalar truncation tail at most
B_0 2^(-N) uniformly over the whole time line. The trace-norm tail
retains the exp(abs(t)/2) factor; these two bounds are not conflated.

This is a trace of R_t C, not of the noncompact R_t alone. No
semigroup law for A_t, commutation of C with time, preservation of
constants by C or determinant identity is presumed.

On an actual singleton circle the exact 204 kernel gives

\[
 \kappa(\phi_t x,x)=\frac14+2^{-a}
                  +\frac14e^{2\pi i t/\log a},\qquad x\in C_a.
 \tag{18}
\]

The true fundamental frequency and repetitions survive, but this
smooth constant-plus-one-harmonic correlation is not a delta comb.
Mixed sample points also contribute: the rational list contains
[q_2+q_3], and every kernel diagonal is at least 1/2, so their
total zero-time contribution is strictly positive. No mixed periodic
orbits have been invented; the trace simply has not localized on
closed orbits.

The geometric benchmark

\[
 \mathcal O=\sum_a\sum_{r\ge1}(\log a)\delta_{r\log a}
 \quad\text{on }(0,\infty)
 \tag{19}
\]

is locally finite, since a<=exp(T) and r<=T/log2 bound its atoms
up to time T. It has a positive atom at log2. The continuous T(t)
defines an atom-free density T(t)dt, hence is not (19). The benchmark
is an output comparison, not an input weight inserted into C. This
scoped nonidentity leaves future transformed or distributional trace
contracts undecided.

Finally the two comparison measures (1-epsilon)nu+epsilon delta_[q2]
and (1-epsilon)nu+epsilon delta_[q3], for 0<epsilon<1, retain full
support and faithful trace-class covariances but change the zero-time
trace by epsilon/8. All geometric orbit data stay the same. These
are controls, not changes to frozen (14). A generic bounded-evaluation
continuous RKHS with a dense countable state set permits the same
positive rank-one mechanism. Thus this construction establishes a
legitimate full-state regularized trace without selecting its sampling
weights or recovering intrinsic arithmetic localization.

## 5. Portfolio decision and compatibility

| Question | Decision | Exact reason / remaining boundary |
| --- | --- | --- |
| 209 on the exact full-state H | ADVANCE the covariance and regularized trace; STOP its identification with the unregularized orbit comb | C is injective trace class with state-separating range, but T includes mixed correlations and sampling choices |
| SC22-TC on the same H | STOP for nonzero-mass filters and every finite-rank correction | Infinite independent invariant means force a nonzero scalar compression on an infinite-dimensional subspace |
| SC22-PF on external H_mu | STOP under the nonzero-transform hypothesis, even after per-circle constants are projected out | Nonconstant frequencies on different circles accumulate at a transform value bounded away from zero |

There is one substantive candidate package, 209, and two short
controls. Reservations 210 and 211 remain uncreated. The portfolio
is not an additional candidate paper and does not combine the different
observation spaces into a stronger theorem.

The positive and negative results are compatible. The infinite-rank
sampling covariance is not the scalar time convolution audited by
TC and is not a finite-rank correction of it. The regularizer cannot
be removed from the trace formula as a harmless notation. PF uses all the
Fourier modes genuinely present in a measure representation that is
already blind to mixed-state observations; those modes are not
established in H. Zero-mass filtering on exact H remains OPEN in
this batch. Neither short stop rules out every regularizer, while
the existence of one trace-class regularizer does not supply an
intrinsic closed-orbit trace.

Naturalness remains OPEN. New localization, limiting or distributional
constructions would require new cards. No such extra line is opened
here, and 201's weighted-return determinant is not imported.

## 6. Evidence and owner limits

Exactly one substantive question, 209, and two short controls are
authorized. This portfolio is an integration record, not a fourth
analytic candidate. The two read-only authors derive bounded reports;
one different combined reviewer audits the final short proofs and
owner boundaries. Calls inherit the model and shared context, are
nonblind, and are not human peer review or independent-error evidence.
ARS contributes only bounded CER and counterargument checks.

No numerical filter sample, fitted spectral data, external theorem,
prime table, clock mutation or model/API upload supports the proofs.
Root alone owns navigation and the final integrated mechanical check.
Regularization, ordinary trace, intrinsic periodic-orbit distribution
and determinant identity are distinct obligations. No 201 determinant,
self-adjoint generator, quantum interpretation, natural A0 or formal
Route result is supplied by these short tests. Formal Route remains
UNASSIGNED and Route B remains NOT INVOKED.

The [claim ledger](claim-ledger.md), [evidence index](evidence/README.md),
[combined scope review](evidence/review.md) and
[209 actual review](../209-full-state-covariance-trace/evidence/review.md)
record exact proof boundaries and actual audit bindings. Assignments
and links alone do not certify completion of a review or mechanical
check; actual reports and unbound receipts record their outcome.
