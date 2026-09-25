# A full-section power space with its actual weighted-return determinant

**Paper ID:** 197-section-power-transfer  
**Candidate ID:** AQC-20260916-SPT01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — FULL-SECTION POWER REPRESENTATION AND ORDINARY FREDHOLM IDENTITY ON RE S > 1; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The original finite-support indecomposable cone flow of 193 is left
unchanged. On its whole normalized section, including every mixed state,
we construct a Hilbert space of coordinate-power observables for each
complex s with Re(s)>1. It embeds continuously and injectively into
bounded continuous functions, is a reproducing-kernel Hilbert space and
separates all section states. The actual forward weighted-return operator
preserves it and is explicitly unitarily represented by multiplication
by a^(-s) on the coefficient space. Its ordinary trace and all power
traces converge in this half-plane and generate the full flow's
unweighted repetition series; its Fredholm determinant converges there
and equals the inverse of the corresponding primitive-orbit product. No state-space
restriction to closed axes is made. The physical observable spaces vary
with s, exclude nonzero constants, are not algebras and are not all
bounded continuous functions. Their engineered choice and a generic
alphabet control leave source-clock and representation naturalness OPEN.
No continuation, target divisor, fixed physical Hilbert generator,
classical symplectic realization or formal Route result is supplied.

## 1. Frozen question and the exact geometric owner

The [candidate card](candidate-card.md) was frozen before these proofs
under the [Round 19 scope](../198-cone-extension-frontier/candidate-card.md).
This paper asks only whether its declared analytic representation works
on the unchanged full owner of
[193](../193-indecomposable-radial-quotient/paper.md). It does not complete
that cone, replace its topology by disjoint faces or attach this operator
to another geometric lift.

Start with the real monoid algebra of all positive integers, finite
support basis e_n and product e_m e_n=e_(mn). Let I be the span of
nonunits and Q=I/I^2. The product space I^2 is exactly the coordinate
span of composite e_n: every product of two nonunits is composite and
every composite has such a factorization. Thus the basis atoms A of Q
are precisely prime classes q_a. This conclusion is derived from the
all-integer source; no prime table selects the input coordinates.

The old quotient norms are ||v||_k=sum_a a^k |v_a|, k>=0, on finite
support. Retain their whole topology, the entire nonzero positive cone
P, D(q_a)=a q_a and X=P/<D>. Its complete real flow is
phi_t[v]=[exp(t)v]. The normalized section, actual first return and
elapsed time proved in 193 are

\[
 S=\{u=\sum_a u_aq_a:u_a\ge0,\ \text{finite support},\ \sum_a u_a=1\},
 \quad c(u)=\sum_a\frac{u_a}{a},\quad
 F(u)_a=\frac{u_a}{a c(u)},\quad \tau(u)=-\log c(u).
 \tag{1}
\]

S has its original subspace topology, not the discrete or coproduct
topology on its faces. In particular ||.||_0 is continuous, but the
topology is not replaced by the single zero-th norm. The map F is a
homeomorphism with inverse Du/||Du||_0. The roof satisfies tau>=log 2.
The full endpoint suspension is time-preservingly homeomorphic to X.
These are specific proved dependencies in 193, not newly asserted
topology or imported facts about a different scale owner.

| Same-object field | Definition used here | Ownership boundary |
| --- | --- | --- |
| Source and lineage | Integer-factor admissibility -> indecomposables -> positive radial carrier -> actual first return | A declared replacement of the prime-symbolic observable; not chronological factorization or a Logistic/Henon conjugacy |
| Full geometric owner | Original P/<D> and radial flow of 193 | Every finite mixed state retained; no completion |
| Section and roof | Equation (1), original section topology | No independently imposed prime roof |
| Analytic representation | H_s=J_s ell^2(A), defined below | Chosen observable subspace; not all functions on X or S |
| Operator | Forward weighted composition using (1) | No inverse-branch sum, extra branches or operator borrowed from 174/179 |
| Central function | det_(H_s)(I-L_s) | Ordinary Hilbert determinant only for Re(s)>1 |
| Later geometry and spectrum | NOT SUPPLIED | No Hamiltonian, contact, quantum or fixed physical generator owner |

The [prior-work guide](../../docs/prior_work/README.md) supplies the
prime-symbolic lineage and the demand for same-object operator geometry.
Its external-paper statements are not mathematical premises of this proof.
No global mathematical novelty or bibliographic completeness is claimed.

## 2. A Hilbert space on every section state

Fix s in C with sigma=Re(s)>1 and let H=ell^2(A;C), with inner product
linear in the first argument. For x>0 set x^s=exp(s log x), with the
real logarithm, and set 0^s=0. Define

\[
 J_s b(u)=\sum_a b_a u_a^s,\qquad b\in H,\ u\in S.
 \tag{2}
\]

Every value is a finite sum, but no finite-support restriction is imposed
on b and no maximum support size is imposed on u.

**Proposition 1 (full-state embedding and separation).** J_s is an
injective continuous linear map H->C_b(S), of operator norm one.
The image separates every pair of distinct points of S, not only its
singleton states.

**Proof.** Since 0<=u_a<=1 and sum_a u_a=1,

\[
 \sum_a |u_a^s|^2=\sum_a u_a^{2\sigma}\le1,
 \qquad |J_s b(u)|\le\|b\|_2.
 \tag{3}
\]

The continuous real-variable function x^s on [0,1] has derivative
s x^(s-1) on (0,1], extending continuously by zero at zero because
sigma>1. Consequently |x^s-y^s|<=|s| |x-y| on this interval. For
u,v in S their combined support is finite, and Cauchy--Schwarz gives

\[
 |J_s b(u)-J_s b(v)|
 \le |s|\,\|b\|_2\|u-v\|_2
 \le |s|\,\|b\|_2\|u-v\|_0.
 \tag{4}
\]

Thus J_s b is continuous for the original stronger weighted-norm
topology and bounded on all S. At the singleton state q_a it has value
b_a. Therefore J_s is injective, and equality in the operator-norm
bound occurs for b equal to a coordinate unit vector. If u differs
from v, some u_a differs from v_a. Their s-th powers differ because
their absolute values u_a^sigma and v_a^sigma differ. The image of that
coordinate unit vector separates u and v. This includes every mixed
state. QED.

Only now equip H_s=J_s H with the transported inner product and norm.
It is complete because H is complete and J_s is a bijective isometry
onto this image by definition. This completes a space of observables,
not the state cone or its section. Completeness refers only to the
transported Hilbert norm; no closedness of the image in the C_b
sup norm is claimed. Finite coefficient sums are dense
in H_s; by (3) their convergence is also uniform on S.

**Proposition 2 (kernel and explicit limitations).** H_s is a
reproducing-kernel Hilbert space on all S, with

\[
 K_s(u,v)=\sum_a u_a^s\overline{v_a^s},\qquad
 \|\operatorname{ev}_u\|=\Bigl(\sum_a u_a^{2\sigma}\Bigr)^{1/2}\le1.
 \tag{5}
\]

It contains no nonzero constant, is not closed under pointwise products
and is a proper subspace of C_b(S). If s and t are distinct parameters
in the frozen half-plane, H_s and H_t are different sets of functions.

**Proof.** The kernel function K_s(.,v) is J_s applied to the finite
coefficient vector (overline(v_a^s))_a. Our inner-product convention
gives <J_s b,K_s(.,v)>=sum_a b_a v_a^s=J_s b(v). The evaluation
norm is exactly the coefficient-vector norm, proving (5).

If J_s b is the constant c, evaluating at every q_a gives b_a=c.
There are infinitely many atoms: if the prime list were finite, one
more than their product would have a prime divisor outside the list.
Thus b is square summable only if c=0. In particular the bounded
continuous function 1 is not in H_s. For distinct a,d, the two image
functions u_a^s and u_d^s have product zero at every q_b but a nonzero
value at (q_a+q_d)/2. No H_s function can have these values, since
its singleton values determine all its coefficients. Hence H_s is not
an algebra.

Finally if u_a^s belonged to H_t, singleton evaluations would force
its coefficient vector in that space to be the same coordinate unit
vector. It would equal u_a^t everywhere. Along a two-atom edge this
would imply x^s=x^t for every 0<x<1, which forces s=t by varying log x
over a real interval. This proves the final assertion. QED.

The same fixed abstract H therefore parametrizes genuinely different
physical observable spaces. It does not automatically define a fixed
physical Hilbert realization of the time flow. Point separation means
states are distinguishable by the chosen observables; it does not say
arbitrary observables or their products are represented. In fact every
image function's mixed-state values are constrained by its singleton
values through (2). This is an explicit representation design, not a
claim of canonical analytic structure.

## 3. The actual full-section return operator

Define the forward weighted-composition rule on the whole section by

\[
 \mathcal L_s f(u)=e^{-s\tau(u)}f(Fu)=c(u)^s f(Fu).
 \tag{6}
\]

It is already bounded on C_b(S): continuity follows from (1), and
its sup-norm bound is at most 2^(-sigma). The contract here concerns
its restriction to H_s, not compactness of that much larger Banach
space and not an inverse-branch transfer convention.

**Proposition 3 (actual intertwining).** H_s is invariant under (6).
For all b in H and every u in the full S,

\[
 \mathcal L_s J_s b=J_s T_s b,
 \qquad (T_s b)_a=a^{-s}b_a.
 \tag{7}
\]

Thus L_s is a bounded everywhere-defined Hilbert operator on H_s,
unitarily equivalent under J_s to T_s, with norm 2^(-sigma).

**Proof.** All nonzero quantities u_a,a,c(u) are positive real. Hence
the chosen logarithm is additive under their products, without a
complex branch ambiguity. Using the finite support at each state,

\[
 c(u)^s\sum_a b_a\left(\frac{u_a}{a c(u)}\right)^s
   =\sum_a a^{-s}b_a u_a^s=J_s T_s b(u).
 \tag{8}
\]

The zero-coordinate terms also agree by the specified 0^s convention.
The coefficient multiplier has norm sup_a a^(-sigma)=2^(-sigma).
This proves invariance before any spectrum or trace is assigned. QED.

For the explicit mixed state u=(q_2+q_3)/2, c(u)=5/12 and
F(u)=(3q_2+2q_3)/5. On the coordinate observable f(u)=u_2^s,
formula (6) gives (5/12)^s(3/5)^s=4^(-s), exactly the right-hand
side of (7) at this mixed state. The proof (8), not just this check,
covers all finite supports and all coefficients.

For an integer r>=1 put c_r(u)=sum_a u_a a^(-r). Iterating (1)
and cancelling the successive normalizations gives

\[
 F^r(u)_a=\frac{a^{-r}u_a}{c_r(u)},\quad
 \sum_{j=0}^{r-1}\tau(F^j u)=-\log c_r(u),\quad
 \mathcal L_s^r f(u)=c_r(u)^s f(F^r u).
 \tag{9}
\]

These are the actual multiple-return times, including mixed states;
they are not r times a constant roof except on singleton states.

## 4. Ordinary traces and Fredholm determinant on the sufficient domain

Let e_a be the standard coefficient basis, P_a its rank-one orthogonal
projection and lambda_a=a^(-s). Equation (7) gives

\[
 T_s=\sum_a\lambda_a P_a,\qquad
 \sum_a|\lambda_a|=\sum_a a^{-\sigma}
 \le\sum_{n=2}^\infty n^{-\sigma}<\infty.
 \tag{10}
\]

The final convergence follows directly from the integral bound for a
decreasing positive power function. Each P_a has trace norm one, and
the partial sums converge in trace norm. Equivalently T_s^*T_s is
diagonal with entries a^(-2 sigma), so the singular values are precisely
a^(-sigma). This proves ordinary Hilbert trace class, not a Banach
space nuclearity analogy or a regularized trace.

For completeness, the trace formula does not depend on reading a
selected diagonal. For any orthonormal basis (v_j) of H,

\[
 \sum_{j,a}|\lambda_a|\,|\langle v_j,e_a\rangle|^2
   =\sum_a|\lambda_a|<\infty
 \tag{11}
\]

by Parseval. Absolute convergence permits exchanging the sums in the
diagonal trace, giving tr(T_s)=sum_a lambda_a. The same argument
applies to every power and is transported unitarily to H_s. Thus

\[
 \operatorname{tr}_{H_s}(\mathcal L_s^r)=\sum_a a^{-rs},
 \qquad
 \|\mathcal L_s^r\|_1=\sum_a a^{-r\sigma},\quad r\ge1.
 \tag{12}
\]

No unknown prime-counting asymptotic is needed for these convergence
claims. With the arithmetic cutoff a<=N and integer N>=2, the omitted
trace norm has the explicit all-integer bound

\[
 \sum_{a>N} a^{-\sigma}
 \le\sum_{n>N}n^{-\sigma}
 \le \frac{N^{1-\sigma}}{\sigma-1}.
 \tag{13}
\]

The determinant is the ordinary Fredholm determinant, which here can
be constructed without a general spectral theorem: in the orthonormal
basis of k-th exterior powers, wedge^k T_s is diagonal with entries
lambda_(a_1)...lambda_(a_k) for a_1<...<a_k. Their absolute sum is
at most (sum_a |lambda_a|)^k/k!. Consequently the ordinary exterior-
power Fredholm series converges absolutely and its finite-rank
approximations give

\[
 \begin{split}
 D_{197}(s)&=\det_{H_s}(I-\mathcal L_s)
          =\sum_{k\ge0}(-1)^k\operatorname{tr}(\wedge^k T_s)\\
          &=\prod_a(1-a^{-s})
           =\exp\left(-\sum_{r\ge1}\frac1r\sum_a a^{-rs}\right).
 \end{split}
 \tag{14}
\]

The k=0 term is 1, fixing normalization. To justify the last equality
directly, |a^(-s)|<=2^(-sigma)<1 and

\[
 \sum_{a,r\ge1}\frac{a^{-r\sigma}}r
 \le\frac{1}{1-2^{-\sigma}}\sum_a a^{-\sigma}<\infty.
 \tag{15}
\]

Thus the power-series logarithms may be summed absolutely, and their
exponential is nonzero. This is a specified logarithm through its
convergent series; no global logarithm choice across a continuation is
being made. On any compact subset of Re(s)>1, choose a common lower
bound sigma_0>1 and apply (10) and (15). Local uniform convergence
of the exponential series proves that (14) is holomorphic and nonzero
throughout this half-plane. It tends to 1 as real s tends to positive
infinity, also by the all-integer majorant.

These are infinite exact estimates, not a finite numerical inference.
No assertion about a sharp convergence boundary, continuation, zeros
outside this domain or a completed determinant is needed or made.

## 5. Match with this flow's complete orbit ledger

An actual return of [v] under the unchanged radial flow means
exp(t)v=D^j v for one common integer j. In every nonzero coordinate
this requires exp(t)=a^j. For j nonzero this is impossible for two
distinct positive atoms. Thus every mixed state is aperiodic. A
singleton support has time stabilizer (log a)Z, and all its positive
amplitudes lie on one actual radial orbit. There is exactly one
primitive circle gamma_a for each derived atom a, of time log a,
with every positive repeat r log a. This restates the complete
all-support argument of 193, not an assumption that the axes exhaust
the state space.

The section description agrees: equation (9) gives F^r u=u only when
a^(-r) is the same for every atom in its support, hence only at q_a.
Those section points have primitive return number one. Therefore,
with unit orbit weight and ordinary positive repetition convention,

\[
 \begin{split}
 \log Z_X(s)
  &=\sum_{\gamma\ \mathrm{primitive}}\sum_{r\ge1}
       \frac{e^{-srT_\gamma}}r
    =\sum_a\sum_{r\ge1}\frac{a^{-rs}}r\\
  &=\sum_{r\ge1}\frac{\operatorname{tr}_{H_s}(\mathcal L_s^r)}r,
 \qquad Z_X(s)=D_{197}(s)^{-1},\quad \Re(s)>1.
 \end{split}
 \tag{16}
\]

Every closed orbit of the full X is included with its intrinsic
multiplicity. Mixed states contribute no missing primitive packet
because they do not close, not because they were removed. There are
no additional assigned stability factors, von Mangoldt weights or
selected representatives in (16). The trace identity is proved by
the explicit representation and full ledger, not by an unproved
geometric fixed-point trace theorem. It belongs to this analytic
extension of 193 and is not thereby an operator of a completed cone
or symplectic coproduct in a different package.

## 6. Adverse controls and scope

| Control or objection | Exact outcome | Consequence |
| --- | --- | --- |
| Entire mixed states rather than axes | Equations (4), (8), (9) hold on all S; mixed points remain distinguishable and aperiodic | Full state ownership retained, without claiming all observables |
| Replace tau by unit roof but keep J_s and F | For f=u_2^s, the changed rule gives e^(-s)c(u)^(-s)2^(-s)u_2^s, not (8) | Cancellation and the proved determinant use the actual nonconstant roof; unit roof is a different-owner control |
| Nonzero constants and products | Proposition 2 excludes constants and u_a^s u_d^s for a different from d | H_s is proper, nonunital and not an algebra; point separation alone gives no full-observable claim |
| Vary s | Proposition 2 proves different sets H_s | Fixed abstract coefficients do not supply a fixed physical Hilbert flow or its generator |
| Change representation to full C_b | No compactness or ordinary determinant on that whole space is inferred here | This is the frozen power-space contract only |
| Finite-rank truncation | Equation (13) bounds the exact infinite trace-norm tail | A cutoff is not a sampled global proof; no numerical experiment was run |
| Generic free commutative alphabet | For distinct generator multipliers lambda_a>=2 with sum_a lambda_a^(-sigma)<infinity, the same whole-section computation gives eigenvalues lambda_a^(-s) and periods log lambda_a | PROVES_TOO_MUCH for unique arithmetic naturalness; summability must be separately assumed in the changed alphabet |
| Repeated multipliers in that changed alphabet | Mixed supports with equal multipliers would also be recurrent | Distinctness is essential to the packet comparison, not just the trace calculation |

The generic-alphabet control uses the corresponding multiplicative
norm and its weighted coefficient topology. It does not claim the
same sufficient half-plane for an arbitrary unbounded-density alphabet:
the summability condition is explicit. Positivity, indecomposables,
the size law, speed normalization and now the coordinate-power norm
are declared engineering. An operator identity does not make those
choices uniquely natural or resolve the programme's stronger A0.

## 7. Gate assessment and decision

| Obligation | Evidence for this exact extension | Status and remaining boundary |
| --- | --- | --- |
| T0 same-object carrier and analytic representation | Unchanged 193 owner, Propositions 1--3 and actual (8) | ESTABLISHED in the topological cone-quotient category |
| T1-style arithmetic and clock | All-integer indecomposable source and old actual first return | Scoped mechanism retained; source-clock naturalness OPEN |
| T2 packets and repetitions | Complete all-support equation and (9), Section 5 | ESTABLISHED for the unchanged full X |
| T3 operator, traces and determinant | Equations (10)--(16) on Re(s)>1 | ESTABLISHED for this declared H_s only |
| Classical A0--A2 | No classical symplectic carrier is provided | NOT APPLICABLE; no natural-A0 or formal A2 pass |
| Formal Route coordinates / Route B | No formal evaluator or readiness contract invoked | UNASSIGNED / NOT INVOKED |

Decision: ADVANCE the bounded analytic contract. It supplies an actual
full-section weighted-return representation and an ordinary determinant
equal to the inverse unit-weight primitive-orbit product,
det(I-L_s)=Z_X(s)^(-1), in its proved convergence domain. Stop this
contract at that result. A fixed physical Hilbert
flow, another geometric carrier, a different norm, continuation or
target-divisor statement would require a separately frozen obligation.
Naturalness remains OPEN rather than being converted into a formal
Route credit by the existence of a useful engineered representation.

## Evidence and reproducibility

The [card](candidate-card.md) precedes the proof; the
[claim ledger](claim-ledger.md) records positive claims and explicit
nonclaims. The [evidence index](evidence/README.md) records actual
review and integration receipts separately. Inputs are exact integer
multiplication, the specified full topology, real-positive powers and
ordinary square-summable coefficient Hilbert space. Methods are the
pointwise cancellation, elementary norm estimates, absolute sums and
explicit finite-rank/exterior-power limits above. No prime dataset,
Riemann-zero data, finite precision, simulation, script or external
theorem with unchecked hypotheses is used. No external literature
fact is required for the result.

ARS is used only for bounded claim/evidence/reasoning and adverse
counterargument discipline. Model drafting and the actual separately
invoked review share context and selected model settings; they are
nonblind, not human peer review, venue validation or an independent-
error certificate. No full ARS pipeline or publication deliverable
is claimed.
