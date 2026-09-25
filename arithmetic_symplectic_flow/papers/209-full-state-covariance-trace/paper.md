# A faithful covariance regularizer and its nonlocalized flow trace

**Paper ID:** 209-full-state-covariance-trace  
**Candidate ID:** AQC-20260916-QCV01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — INJECTIVE FULL-STATE TRACE-CLASS REGULARIZATION; SCOPED STOP AS AN UNREGULARIZED CLOSED-ORBIT TRACE; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

On the fixed Hilbert space of actual continuous observables of the
completed arithmetic cone quotient, we construct a positive injective
trace-class covariance from an explicitly enumerated dense rational
state set. Its range is dense and still separates every state, including
infinite-support states. Composing this operator with actual time
pullback gives a trace-class family with an explicit, bounded continuous
trace. On a prime circle the kernel correlation retains its true
frequency, but the full trace also contains mixed-state correlations and
depends on the chosen sampling measure. It is not the atomic positive-time
closed-orbit distribution. Thus one can actively construct a legitimate
regularized trace without obtaining an intrinsic dynamical trace formula.
No Euler determinant, natural-source result or formal Route pass follows.

## 1. Owner, lineage and claim boundary

The [version-1 card](candidate-card.md) was frozen before this proof.
The geometric dependency is [194](../194-rapid-decay-cone-completion/paper.md);
the exact analytic dependency is
[204](../204-quotient-orbit-feature-hilbert/paper.md), not the different
weighted-return spaces or determinant of 201.

| Field | Frozen owner | Boundary |
| --- | --- | --- |
| Source | All-integer monoid algebra, nonunit ideal I, Q=I/I^2, derived atom classes q_a | No supplied prime table or zero data |
| Completed carrier | E with all norms sum_a a^k abs(v_a); punctured nonnegative cone P_hat; X_hat=P_hat/<D> | Every finite and infinite support, original topology |
| Deck and time | Dv=(a v_a); phi_t[v]=[exp(t)v] | Actual old physical time, not the deck angle |
| Section and repetition | m=1, c=sum_a u_a/a, F=D^(-1)u/c, tau=-log c; one circle of least time log a per atom | All positive repetitions; no mixed periodic states |
| Fixed analytic representation | 204's H=K/ker J of actual continuous functions, kernel kappa, R_t f=f o phi_t | No change of norm, states or spectral parameter |
| New operator | Explicit sampling covariance C and A_t=R_t C on this H | Regularized trace, not Tr(R_t) |
| Symplectic/contact/quantum lift | NOT APPLICABLE / NOT SUPPLIED | No cross-owner geometry or self-adjoint generator |

The [prior-work lineage](../../docs/prior_work/README.md) retained here is
proper-factor symbolic admissibility -> all-integer multiplication ->
indecomposable quotient -> positive geometric flow -> scalar observations.
This is a declared algebraic replacement of the symbolic source, not a
Logistic/Henon conjugacy or proof that the replacement is necessary.
The source quotient, size law, physical speed, topology and representation
norm remain choices whose arithmetic naturalness is OPEN.

From 204 we use an infinite-dimensional separable complex H of bounded
continuous functions, with inner product linear in its first argument,
evaluation vectors k_x=kappa(.,x), and

\[
 f(x)=\langle f,k_x\rangle,\qquad
 \|k_x\|^2=\kappa(x,x)\le B_0\le1,\qquad
 \|R_t\|\le e^{|t|/2}.                                      \tag{1}
\]

The map x->k_x is norm continuous, H separates all states, contains
constants, and R_t is the actual strongly continuous group. Specifically,

\[
 \kappa(x,y)=\sum_j\beta_j\int_{\mathbb R}
 g_j(\phi_r x)\overline{g_j(\phi_r y)}\,\rho(r)\,dr,             \tag{2}
\]

where g_0=1, g_*=exp(2 pi i theta), g_a=w_a,
m(D^(-theta(v))v)=1, w=D^(-theta(v))v,
beta_0=beta_*=1/4, beta_a=2^(-a), rho(r)=exp(-abs(r))/2,
and B_0=sum_j beta_j. All g_j have modulus at most one. These
weights are representation inputs, not an invariant measure on X_hat.

The question is only whether the frozen sampling construction below
gives a faithful trace-class regularizer and what its actual trace means.
We do not assume C commutes with R_t, makes R_t unitary, preserves
constants, or has a bounded inverse. We do not import any determinant.

## 2. A full-support probability without deleting states

Take all nonzero finite-support vectors with positive rational nonzero
coordinates. Write each uniquely as
(a_1,p_1,q_1,...,a_d,p_d,q_d), with increasing derived atoms and
positive coprime numerator-denominator pairs. Order these tuples first
by height a_d+sum_i(p_i+q_i), then lexicographically, proper prefix
first. A height bound bounds every entry and the tuple length, so each
level is finite. There are infinitely many tuples, and this specifies
a sequence v_n, n>=1, listing each vector exactly once. Let x_n=[v_n].
Distinct tuples may give the same quotient state; all such entries stay.
No numerical enumeration or prime lookup is required for the definition.

**Lemma 1 (density).** The set {x_n:n>=1} is dense in the entire
X_hat with its existing topology. Consequently

\[
 \mu=\sum_{n=1}^{\infty}2^{-n}\delta_{x_n}                    \tag{3}
\]

is a Borel probability with full topological support.

**Proof.** A basic neighborhood in E constrains finitely many weighted
norms. Truncate a given nonzero v in P_hat far enough that its tails
in all those norms are as small as prescribed, retaining at least one
positive coordinate. Replace the finitely many retained positive
coordinates by sufficiently close positive rationals. This approximates
v in every constrained norm and stays in P_hat. Thus the listed vectors
are dense in P_hat. The inverse image of a nonempty open subset of the
quotient under the continuous surjective quotient map is nonempty open,
so it meets the list. Therefore the quotient list is dense. Equation
(3) has total mass one, and every nonempty open set contains a point
of positive mass. QED.

This measure is not flow invariant: every x_n has a positive mass,
while its continuous-time orbit contains arbitrarily many distinct
points. Invariance would give them all the same positive mass, contrary
to finiteness. This does not conflict with the invariant-probability
classification in [205](../205-invariant-measure-support/paper.md).
We are not replacing H by arbitrary L2(mu) functions or identifying
physical states almost everywhere. In particular the infinite-support
states, though not themselves in the sampling list, remain in the
domain of every observation and of the actual flow.

## 3. Positive trace-class construction and exact faithfulness

For u,v in H use the linear rank-one convention
(u tensor v)f=<f,v>u. It has trace <u,v> and trace norm
norm(u)norm(v); its single nonzero singular value gives the latter
identity. Finite sums followed by trace-norm limits will be enough;
no orthogonality of different evaluation vectors is assumed.

**Theorem 2 (frozen full-state covariance).** The series

\[
 C=\sum_{n=1}^{\infty}2^{-n}(k_{x_n}\otimes k_{x_n})            \tag{4}
\]

converges in trace norm on the unchanged H. It is positive, self-adjoint,
injective, and has dense range. Its range still separates every two
distinct quotient states. For C_N the first N terms,

\[
 \|C-C_N\|_1\le B_0 2^{-N},\qquad
 \operatorname{Tr}C=\sum_n2^{-n}\kappa(x_n,x_n)\le B_0.        \tag{5}
\]

**Proof.** The n-th rank-one trace norm is at most 2^(-n)B_0,
so completeness of the trace class gives (4) and the tail bound.
Finite partial sums are positive self-adjoint; operator-norm convergence
preserves both properties. The continuous trace functional gives (5).
For every f, the series also gives

\[
 \langle Cf,f\rangle=\sum_n2^{-n}|f(x_n)|^2.                  \tag{6}
\]

If Cf=0, every summand vanishes. The function f is continuous and
vanishes on a dense set, so it vanishes on all X_hat and is the zero
element of the actual-function Hilbert space. Thus ker C={0}.
Self-adjointness implies that the orthogonal complement of ran C is
ker C, so the range is dense. This is not a claim of surjectivity.

For x not equal to y, put h=k_x-k_y. Since H separates points,
h is nonzero. Its continuous function is nonzero somewhere, and hence
on some sampled point. Equation (6) gives <Ch,h>>0. For f=Ch in
ran C, f(x)-f(y)=<Ch,k_x-k_y>>0, proving point separation by the
range itself. This includes any two infinite-support states. QED.

The construction is genuinely infinite rank, since C is injective
on infinite-dimensional H. It cannot have a bounded everywhere-defined
inverse: otherwise the compact operator C times that inverse would
make the identity compact. Each finite partial sum does lose information;
faithfulness is proved for the full series, not inferred from a finite
matrix. The exact tail estimate is an analytic error bound, not a
simulation result. Neither constants in ran C nor an algebra property
of ran C is asserted.

## 4. A trace of the actual flow, with the regularizer visible

**Theorem 3 (regularized time trace).** For every real t the operator
A_t=R_t C on this same H is trace class and

\[
 \|A_t\|_1\le e^{|t|/2}B_0,\qquad
 T(t):=\operatorname{Tr}(R_t C)
      =\sum_n2^{-n}\kappa(\phi_t x_n,x_n).                    \tag{7}
\]

The family t->A_t is trace-norm continuous. The scalar T is continuous
and satisfies abs(T(t))<=B_0 for all real t. The trace truncations obey

\[
 \left|T(t)-\operatorname{Tr}(R_t C_N)\right|
       \le B_0 2^{-N}                                      \tag{8}
\]

uniformly in real t, though the corresponding trace-norm tail estimate
contains exp(abs(t)/2).

**Proof.** Multiplying the trace-norm series by bounded R_t gives
sum_n 2^(-n) (R_t k_(x_n)) tensor k_(x_n), with total trace norm
at most exp(abs(t)/2)B_0. Its trace is
sum_n 2^(-n)<R_t k_(x_n),k_(x_n)>. Evaluation and the convention
k_x=kappa(.,x) give precisely kappa(phi_t x_n,x_n), not its
complex conjugate or a simultaneous shift of both arguments.

For finitely many rank-one terms, strong continuity of R_t gives
trace-norm continuity because the trace norm of each difference is
norm((R_t-R_s)k_(x_n)) norm(k_(x_n)). The tail is uniformly small
on compact time intervals by (1) and (5), proving the assertion for
A_t. Separately, kernel Cauchy--Schwarz in (1) bounds each scalar
term in (7) by B_0, at every time. This proves (8), absolute uniform
convergence on the whole real line, and the stated scalar bound.
Each term is continuous, hence so is T. QED.

This is a trace on the actual, state-separating, fixed physical H.
It is not a trace of R_t alone, which remains noncompact by 204.
Nothing has identified A_(t+s) with A_t A_s; this is a regularized
family, not a new evolution group. Removing C, inverting C on all H,
or forming a limit that yields a distributional trace is outside this
contract. A positive C also does not make T(t) real or positive for
all t, since R_t is nonunitary in the frozen norm.

## 5. What prime circles contribute, and what they do not

For any x on the singleton circle C_a, the true flow has least time
log a. Here w(phi_r x)=q_a and
g_*(phi_r x)=g_*(x) exp(2 pi i r/log a). Substitution in the frozen
kernel (2), with the same time on its two arguments, gives exactly

\[
 \kappa(\phi_t x,x)
       =\frac14+2^{-a}+\frac14 e^{2\pi i t/\log a}.           \tag{9}
\]

Thus this contribution retains the actual fundamental frequency and
its time repetitions. Equation (9) follows from the true flow; no
log-prime roof or fitted Fourier frequency has been added to C.
Nevertheless it is only a smooth constant-plus-one-harmonic correlation,
not a delta singularity at every closed-orbit repeat. No assertion that
H contains every Fourier mode of each circle is being made.

Mixed-state terms are not absent from (7). The sampling list contains
[q_2+q_3], among many mixed states. At t=0 every kernel diagonal obeys
kappa(x,x)>=1/2 because the 0 and * features both have modulus one.
Consequently the sum over mixed sampled states at zero is strictly
positive. Their aperiodicity is preserved: the correlation is not an
orbit-counting sum merely because the same flow has prime circles.

For a precise comparison, define solely as a geometric benchmark

\[
 \mathcal O=\sum_a\sum_{m\ge1}(\log a)\,\delta_{m\log a}
       \quad\hbox{on }(0,\infty).                           \tag{10}
\]

This is the usual primitive-period-weighted listing of the established
circles and their positive repetitions, not an inserted input to C or
a claimed trace theorem. It is locally finite: on a bounded positive
time interval only a<=exp(T) and m<=T/log 2 can occur. It has an
atom of mass log 2 at t=log 2. The distribution associated with the
continuous function T(t) in (7) has no atoms. Hence T(t)dt is not
equal to (10). This scoped nonidentity does not exclude transformed,
smoothed or renormalized trace identities under a future exact contract.
No such identity is proved here.

## 6. Adverse controls: full support does not select arithmetic weights

Keep the candidate (3) unchanged, and compare only as controls

\[
 \mu_{2,\epsilon}=(1-\epsilon)\mu+\epsilon\delta_{[q_2]},
 \quad
 \mu_{3,\epsilon}=(1-\epsilon)\mu+\epsilon\delta_{[q_3]},
 \qquad 0<\epsilon<1.                                     \tag{11}
\]

Both still have full support, and the same argument gives faithful
positive trace-class covariances. By (9), their zero-time traces differ
by epsilon(3/4-5/8)=epsilon/8. Their carrier, flow, primitive circles
and repetition ledger are identical. Thus even these strong observation
properties do not determine a unique trace from the geometric orbit
data. Formula (11) is an explicit robustness control, not an after-the-fact
change to the frozen mu.

**PROVES_TOO_MUCH control.** The rank-one series argument works on any
infinite-dimensional continuous RKHS with uniformly bounded evaluation
norms and a countable dense state set: use positive summable sampling
weights, and continuity gives injectivity and full point separation of
the range whenever the original RKHS separates states. Any bounded
strongly continuous pullback group then gives the same regularized
trace construction. Arithmetic is not required for this functional-
analytic mechanism. In the present object it remains linked to the
source through X_hat and (9), but it does not explain why the sampling
weights or the prior norm should be arithmetically distinguished.

Related work on measure-defined RKHS integral operators provides
context for the general covariance mechanism, not a proof of our flow
claims: Bertrand Gauthier, *Kernel embedding of measures and low-rank
approximation of integral operators*, Positivity 28, 29 (2024),
[DOI](https://doi.org/10.1007/s11117-024-01041-8),
[institutional record and abstract](https://orca.cardiff.ac.uk/id/eprint/166863/).
Only that metadata/abstract was checked here. The present rank-one
proof is given in full and makes no novelty or literature-completeness
claim. It is not a finite-compression proof about Riemann zeros.

## 7. Gate assessment and decision

| Obligation | Result on this exact owner | Decision |
| --- | --- | --- |
| Source, topology, time and primitive ledger | Unchanged 194 geometry, observed on exactly 204 H | Same-object ledger intact; naturalness OPEN |
| Trace-class construction without losing state separation | Positive injective C, dense point-separating range | ADVANCE the precise regularization theorem |
| Actual-flow trace | Formula (7), trace-norm continuity, uniform scalar truncation bound | ESTABLISHED with the explicit C retained |
| Unregularized localized closed-orbit trace | T is continuous, includes mixed states, changes under (11) | SCOPED STOP for identifying this T with (10) |
| Euler determinant / continuation / target divisor | Not constructed or imported | OPEN / NOT EVALUATED |
| Classical A0--A2 / formal Route / B | No classical carrier or formal protocol evaluated | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

Advance this construction as a faithful observation regularizer, and
stop its promotion to an unregularized closed-orbit trace. The exact
next gap is an intrinsic localization mechanism, not merely the existence
of some finite trace. A new localization or limiting proposal needs a
fresh card and must retain this same source, physical clock and owner
or explicitly declare a fork. No parameter tuning or new research lane
is undertaken inside this completed contract.

## Reproducibility and evidence

The [card](candidate-card.md), [claim ledger](claim-ledger.md), and
[evidence index](evidence/README.md) fix definitions, dependencies,
controls, source-reading limits and actual review. There is no numerical
experiment, cutoff-dependent theorem or prime-data file. The explicit
enumeration, convergent series and exact bounds (5), (8) are the
reproducible method. Model review is nonblind and is not human peer
review; mechanical link/hash checks are not mathematical proof.
