# Extensions of the complete indecomposable radial flow

**Portfolio ID:** ASFS-FRONTIER-20260916-19  
**Research date:** 2026-09-16  
**Status:** PORTFOLIO ADVANCE — RAPID-DECAY COMPLETION, CONSERVATIVE COPRODUCT AND FULL-SECTION DETERMINANT; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## 1. Four questions, without combining different owners

The [frozen scope](candidate-card.md) extends the specific
[193 construction](../193-indecomposable-radial-quotient/paper.md), not
a collection of unrelated prime clocks. That owner is the entire
nonzero finite-support positive cone of the integer indecomposable
quotient I/I^2, divided by D(e_n)=n e_n. Its common radial flow has
an embedded full section S, with actual first return and roof

\[
 c(u)=\sum_a\frac{u_a}{a},\qquad
 F(u)=\frac{D^{-1}u}{c(u)},\qquad
 \tau(u)=-\log c(u)\ge\log2.
\tag{1}
\]

Here a ranges over the atoms derived from the all-integer quotient;
they are primes by the quotient's multiplication argument, not an
input list. S contains every nonnegative finite-support unit-mass
state, with the original family of weighted coefficient norms. All
mixed states remain present and aperiodic; each axis belongs to one
actual log-prime circle of the full flow.

The new questions are distinct: 194 completes the entire cone; 196
constructs a conservative coproduct lift of every finite-support face;
197 changes the observable Hilbert space of the original full S;
SC19-CB tests that same return on all C_b(S). A positive answer for
one is not an operator, topology or geometry theorem for another.
In particular 197 is not automatically an operator on the 194
completion or the 196 lifted carrier. No old package is changed.

## 2. SC19-CB: full bounded-continuous composition is not compact

This exact short screen is frozen in the portfolio card. For fixed
real s>0 its owner is the complex Banach space C_b(S), with the
supremum norm on the entire original S, and the actual forward
weighted-composition operator

\[
 L_sf(u)=c(u)^s f(Fu).
\tag{2}
\]

This is not a sum over multiple inverse branches. The old 181
many-predecessor constant-function obstruction does not apply by
analogy; (2) must be tested on its own complete space.

**Boundedness and its exact norm.** The function c is positive and
continuous, with c<=1/2 and
abs(c(u)-c(v))<=||u-v||_0/2. The return F is a homeomorphism in
the original topology. Consequently L_s preserves bounded continuity
and ||L_s||<=2^(-s). The constant function 1 has norm one, and
(L_s1)(q_2)=2^(-s), proving equality. Thus the failure is not
unboundedness or missing constant-function membership. Also L_s1=c^s
is not constant, so constants alone are not an invariant replacement.

**Full mixed-edge test.** Put u(t)=t q_2+(1-t)q_3 for 0<=t<=1.
These are all actual states in S, and direct substitution gives

\[
 c(u(t))=\frac{t+2}{6},\qquad
 F(u(t))=u(h(t)),\qquad h(t)=\frac{3t}{t+2},\quad
 h^{-1}(x)=\frac{2x}{3-x}.
\tag{3}
\]

For j>=1 set x_j=2^(-j), r_j=x_j/4 and take the continuous tent
g_j(x)=max(0,1-abs(x-x_j)/r_j). Define f_j(u)=g_j(u_2) on the
whole S, not merely on its edge. Coordinate evaluation is continuous,
so these are elements of C_b(S) of norm one. Their supporting
intervals [3x_j/4,5x_j/4] are pairwise disjoint: the next interval's
right endpoint is 5x_j/8<3x_j/4. Each f_j vanishes at every axis
point q_a, whose u_2 coordinate is either zero or one.

Let t_j=2x_j/(3-x_j) and v_j=u(t_j). Every v_j is a genuinely
mixed state, F(v_j)=u(x_j), and c(v_j)=1/(3-x_j). For j different
from k we therefore have

\[
 \|L_sf_j-L_sf_k\|_\infty
 \ge (3-x_j)^{-s}\ge3^{-s}>0.
\tag{4}
\]

The image of the unit ball contains this uniformly separated sequence,
so it is not relatively compact. This proves noncompactness of (2)
on the full C_b(S). The edge supplies test points and the functions
are globally defined; the carrier was never restricted to the edge.
The obstruction is invisible to tests looking only at the axes.

**Precise nuclear/determinant stop.** An ordinary Banach nuclear
representation sum_l lambda_l(f)y_l with
sum_l ||lambda_l|| ||y_l||_infinity finite would converge in operator
norm from its finite-rank truncations. Such a limit is compact:
finite-rank images of the unit ball are totally bounded, their uniform
approximations remain totally bounded, and C_b(S) is complete.
Equation (4) therefore rules out that ordinary nuclear representation
and the corresponding nuclear-trace/Fredholm-determinant route for
this exact sup-norm owner.

Decision: **STOP this representation contract**, not the original flow
or every possible analytic space. C_b is not being called a Hilbert
space or assigned a Hilbert trace-class label. No assertion that
I-L_s fails to be a Fredholm operator is made; that is a different
question from constructing a Fredholm determinant by a nuclear trace.
The separately frozen 197 space is a new representation, not an
in-place alteration of (2). No 195 package is needed for this decisive
short proof, and no essential-spectrum or regularized-trace claim is
added after the stop.

## 3. 194: a proper completion, not a relabelled finite cone

The separately frozen
[194 / AQC-20260916-RDC01](../194-rapid-decay-cone-completion/paper.md)
and its [actual review](../194-rapid-decay-cone-completion/evidence/review.md)
establish a new full topological owner. The completion of the original
indecomposable space is exactly

\[
 E=\{b=(b_a):\sum_a a^k|b_a|<\infty
              \text{ for every integer }k\ge0\}.
\tag{5}
\]

This identification is proved using coordinate limits of sequences
Cauchy in every norm and the same finite truncations converging in
every weighted norm. The positive closure consists of all nonnegative
vectors in E. In particular the all-integer series sum_(n>=2)e^(-n)q_n
gives a genuinely infinite-support positive state. Completion changes
the set of states, not only terminology.

On every state of E, D and its inverse satisfy
||Db||_k=||b||_(k+1) and ||D^(-1)b||_k<=||b||_k/2. They therefore
extend as mutually inverse continuous maps for the whole norm family.
Removing zero from the positive cone leaves finite positive mass at
every state. The same mass-annulus estimates prove freeness, quotient
Hausdorff separation and continuity of the complete radial action,
without local compactness. The full completed section has its actual
first return (1), and all crossing-time gaps remain at least log 2.

The decisive infinite-support test is not an approximation by finite
periodic ledgers. Directly, a return requires one integer j such that
exp(t)b=D^j b. Every positive coordinate then imposes exp(t)=a^j.
Two distinct support values forbid every nonzero j, including when
the support is infinite. Singleton states give exactly one circle
per atom with least time log a and all repeats. Thus new states
are retained but create no hidden periodic packets.

The old finite cone is dense and D-saturated in the new one. For
an ambient open set O, its quotient image intersected with the finite
image equals the quotient image of O intersected with the finite
cone. Openness of the quotient map therefore proves that 193's old
flow embeds with its actual topology, densely and time-preservingly.
This is a proper embedding, not equality of the two owners.

Two adverse controls are load-bearing. In the lone unweighted l1
completion the vector b_(p_j)=1/(j p_j), for atoms in increasing
order, is summable, but Db has the divergent harmonic coefficients
1/j. The integer multiplier would not act on that whole carrier.
If zero is instead kept, D^(-j)b tends to zero, making a nonzero
orbit class nonclosed in the quotient; the quotient is not T1.
Neither altered completion nor added zero is used to replace (5).

Decision: **ADVANCE the full completed topological owner.** Completeness
of E, completeness of the radial flow and completeness of the punctured
cone as a metric subspace are distinct; only the first two hold as
asserted. Naturalness remains OPEN. No symplectic, Hilbert, operator,
trace or determinant is supplied by 194 or borrowed from 197.

## 4. 196: a full conservative lift, with an explicit topology cost

The new [196 / ASC-20260916-FCL01](../196-face-cotangent-conservative-lift/paper.md)
retains every strict finite-support face Delta_J^o, every covector in
its cotangent bundle and every point of a common transverse real plane.
Its base is the disjoint topological coproduct
M=coproduct_J(T*Delta_J^o times R2), with the canonical component
form plus dQ wedge dP. The map is the full cotangent lift of the
old F on each face, times B(Q,P)=(2Q,P/2). The roof is exactly
rho=tau composed with the forgetful map h:M->S.

The whole-state proof is particularly explicit. For
J={a0,...,a_(m-1)}, global log-ratio coordinates
y_i=log(u_(a_i)/u_(a0)) identify the strict face with R^(m-1).
The base return is the translation y->y+v_J, where
(v_J)_i=log(a0/a_i). In its full cotangent coordinates eta,

\[
 G^r(y,\eta,Q,P)=(y+r v_J,\eta,2^rQ,2^{-r}P),
 \qquad
 \omega_J=\sum_i dy_i\wedge d\eta_i+dQ\wedge dP.
\tag{6}
\]

This proves global invertibility and exact symplecticity for every
component and every momentum. The suspension uses all these states.
Its deck action is (z,t)->(Gz,t-rho(z)); for every integer r its
elapsed time is

\[
 T_r(u)=-\log\sum_a u_a a^{-r},\qquad
 T_{r+1}(u)-T_r(u)=\rho(G^rz)\ge\log2.
\tag{7}
\]

The complete two-sided flow and Hausdorff endpoint quotient follow
from the full time cover: thin horizontal strips have disjoint
nontrivial deck translates, only finitely many translates can meet
two bounded strips, and (7) diverges in both directions. Unbounded
momenta create no finite-time accumulation of crossings.

If J has two or more atoms, v_J is nonzero and (6) excludes every
positive return, for all covectors and plane states. If J is a
singleton, the cotangent factor has dimension zero, but the entire
uniform R2 factor remains; its only periodic point is Q=P=0.
Thus the complete flow has one intrinsic primitive circle per prime,
with actual time log p, repeats r log p and transverse monodromy
diag(2^r,2^(-r)). The centers are a conclusion of the full iterate
equation, not a selected periodic subcarrier.

The geometric cost is essential. Components have dimension 2|J|,
not one fixed dimension. The forgetful h is continuous and onto but
not a quotient map: h^(-1){q_2} is the whole open singleton component,
whereas {q_2} is not open in the original S. The old mixed states
(1-1/k)q_2+q_3/k approach q_2 in every original norm, but their lifts
cannot converge to that disjoint component. The full projection
Pi([z,t])=[exp(t)h(z)] is continuous, onto and time-preserving by
exact deck compatibility. It too is nonquotient: the old prime circle
has an open singleton-component preimage but is not open in X.
Noncentral singleton lifted trajectories can be aperiodic while
projecting onto that old periodic circle.

Decision: **ADVANCE this new symplectic coproduct, not a symplectic
realization of 193's original topology.** It is neither a fixed-
dimensional ASFS manifold nor a supplied lamination. Replacing B by
the identity would create continuous prime packet families; omitting
the plane would leave zero-dimensional singleton bases. The actual
hyperbolic factor and new topology are openly declared designs.
No Hamiltonian, contact form, completed carrier or analytic operator
is attached to this result. Its
[separate review](../196-face-cotangent-conservative-lift/evidence/review.md)
owns the complete mathematical audit.

## 5. 197: an actual full-section determinant on chosen power observables

The [197 / AQC-20260916-SPT01](../197-section-power-transfer/paper.md)
keeps the original finite-support S, topology, F and tau unchanged.
For complex s with sigma=Re(s)>1, take H=ell^2(A;C) and define

\[
 J_s b(u)=\sum_a b_a u_a^s,\qquad
 u_a^s=\exp(s\log u_a)\ (u_a>0),\quad 0^s=0.
\tag{8}
\]

The logarithm is the real logarithm on positive numbers. On every
state the sum is finite, but b need not be finitely supported. The
bound sum_a u_a^(2 sigma)<=1 gives ||J_s b||_infinity<=||b||_2
uniformly on all S and also bounds every coefficient tail uniformly.
The derivative of x^s has modulus at most |s| on [0,1], so
|J_s b(u)-J_s b(v)|<=|s| ||b||_2 ||u-v||_0. This proves continuity
in the original stronger topology, not merely finite pointwise
evaluation. Evaluating at q_a recovers b_a, proving injection.
Some coordinate differs for every pair of distinct states, and its
power has different modulus, so the image distinguishes all mixed
states as well as axes.

Only after that injection, H_s=J_s H receives its transported
Hilbert norm. Its reproducing kernel is
K_s(u,v)=sum_a u_a^s conjugate(v_a^s), with inner product linear
in the first argument. Completeness concerns this Hilbert norm,
not closedness of H_s in the C_b sup norm.

For the actual forward weighted composition (2), the real-positive
branch makes cancellation valid on every full state:

\[
 c(u)^s\sum_a b_a\left(\frac{u_a}{a c(u)}\right)^s
 =\sum_a a^{-s}b_a u_a^s.
\tag{9}
\]

Thus H_s is genuinely invariant, and L_s J_s=J_s T_s where
T_s b=(a^(-s)b_a)_a. This proves the operator's ownership before
assigning a diagonal spectrum. It does not replace S by its axes;
for example on u=(q_2+q_3)/2 the actual c=5/12 and F coefficients
3/5,2/5 give the same cancellation, and (9) covers every support.
Repeated composition retains the mixed accumulated time (7), not
an artificially constant roof.

The operator is ordinary Hilbert trace class for sigma>1:
its singular values are a^(-sigma), whose sum is bounded by the
convergent integer sum sum_(n>=2)n^(-sigma). Exact finite-rank
trace-norm tails are at most N^(1-sigma)/(sigma-1). Absolute
double sums and Parseval give basis-independent power traces.
The ordinary exterior-power determinant series is absolutely
bounded by exp(sum_a a^(-sigma)). Consequently

\[
 \operatorname{tr}_{H_s}(L_s^r)=\sum_a a^{-rs},\qquad
 D_{197}(s)=\det_{H_s}(I-L_s)
 =\prod_a(1-a^{-s})
 =\exp\left(-\sum_{r\ge1}\frac1r\sum_a a^{-rs}\right).
\tag{10}
\]

These expressions converge locally uniformly and define a nonzero
holomorphic determinant on the stated sufficient half-plane, with
normalization tending to one as real s tends to infinity. The full
radial flow has exactly its one log-a circle per atom and no mixed
periodic state. Its ordinary unit-weight primitive/repetition product
therefore gives Z_X(s)=D_197(s)^(-1) in this same domain. No orbit,
clock, multiplicity or analytic object is borrowed from a comparator.
This identity comes from (9) and the full ledger, not an assumed
geometric fixed-point trace formula.

The representation limitations are part of the result. Nonzero
constants cannot belong because axis evaluations would force a
nonsquare-summable constant coefficient sequence. Products such as
u_a^s u_b^s, a different from b, vanish on all axes but not on a
mixed state, so they cannot belong either. H_s is not an algebra
and does not contain all C_b(S). Different s give different physical
function spaces: the axis coefficients of u_a^s in H_t would force
the same coordinate vector, while its edge values x^s cannot equal
x^t for all 0<x<1 unless s=t. A fixed abstract coefficient space
does not therefore yield a fixed physical Hilbert flow or generator.
The complex coefficients are observables on the unchanged positive
real carrier, not a complexification of its states.

Decision: **ADVANCE this declared full-section analytic contract.**
The larger C_b noncompactness in Section 2 is not contradicted:
its obstructing tents vanish on all axes and cannot be nonzero
members of H_s, whose axis values determine the entire function.
Point separation and inclusion of all observables are different.
A generic free alphabet with distinct multipliers lambda_a>=2 and
summable lambda_a^(-sigma) admits the same construction, so the
identity does not settle arithmetic or representation naturalness.
No continuation, target-zero statement, regularized trace, fixed
physical generator or operator on 194/196 is supplied. The
[actual separate review](../197-section-power-transfer/evidence/review.md)
records its full proof audit and exact byte scope.

## 6. Final portfolio boundary and next decision

The four questions yield three bounded ADVANCE results and one
short STOP. There are three substantive packages (194, 196, 197)
and this portfolio; 195 remains unused. These are not four new
geometries or one synthesized object satisfying all obligations.

| Contract | Carrier retained or changed | Exact additional result | Not transferred |
| --- | --- | --- | --- |
| 194 | New all-weight completion, with every infinite support | Hausdorff complete flow; dense old topological subflow; unchanged all-packet clock | No 197 operator or 196 symplectic structure |
| SC19-CB | Original full S and all C_b with sup norm | Bounded actual composition, noncompact on mixed states | No universal no-go for other function spaces |
| 196 | New disjoint-face cotangent coproduct with all momenta | Componentwise symplectic bases, full packets/clock and nonquotient projection | No realization of old cross-face topology, completion or analytic owner |
| 197 | Original full S, new s-dependent observable Hilbert spaces | Ordinary trace-class forward composition and determinant of the same orbit ledger on Re s>1 | No all-C_b trace, fixed physical Hilbert flow or transfer to 194/196 |

The source remains the precise prime-symbolic indecomposable replacement
of integer multiplication, not arbitrary unrelated geometry. The
quotient, positivity, scale law, universal speed and additional topology
or observable choices remain declared construction inputs. Their
validity and naturalness are separate questions. Naturalness stays
OPEN; no classical A0--A2 pass, formal Route coordinate or Route-B
entry is claimed by the portfolio or by file completion.

A next-fork hypothesis, not a fifth lane, asks whether the integer
size multiplier can be characterized by the finite cokernel index
of positive-integer endomorphisms of (Z,+). That would need a fresh
card and proof in its specified category. Even a positive answer
would not automatically justify I/I^2, positivity, the time law or
natural A0. No such new norm-characterization result is established
or reviewed in this batch.

The [ledger](claim-ledger.md) and [evidence index](evidence/README.md)
separate mathematical outcomes, actual review receipts and final
integration. Each substantive contract has one actual separate
mathematical review. The portfolio's separate combined invocation
rederives Section 2 and checks owner-level summaries, rather than
adding another substantive review tree. Actual completion is recorded
in the receipts, not presumed from this prose. Every new mathematical
claim is supported by the cited owner proof or the self-contained
short screen; no finite numerical sample substitutes for an infinite
result. ARS supplies bounded claim/evidence/reasoning and adverse
controls only. Calls inherit the model and context and are nonblind,
not human peer review or independent-error certificates. Root owns
the sole final integrated mechanical verification.
