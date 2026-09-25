# Completing the positive cone without creating hidden prime packets

**Paper ID:** 194-rapid-decay-cone-completion  
**Candidate ID:** AQC-20260916-RDC01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — COMPLETE RAPID-DECAY SPACE AND HAUSDORFF ALL-SUPPORT PRIME-LOG FLOW; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

The integer indecomposable positive-cone construction extends from finite
support to the completion for every polynomially weighted coefficient
norm. The resulting vector space is complete and has genuine infinite-
support positive states. The entire punctured positive cone has a
Hausdorff integer-dilation quotient with a complete radial flow. All new
mixed states are aperiodic; the full primitive ledger remains one circle
per prime, with actual time log p and all repeats. The old flow embeds
densely and time-preservingly, not just set-theoretically. An actual
global section and return roof are derived on the entire completion.
In contrast, completion in the lone unweighted norm does not permit
the integer-size map on every state. This is a topological completion
result, not a Hilbert, symplectic or analytic realization; arithmetic
naturalness remains open.

## 1. Frozen extension, arithmetic source and ownership

The [version-1 card](candidate-card.md) predates the proof. The parent
[193](../193-indecomposable-radial-quotient/paper.md) keeps all finite
positive supports. Here the carrier is enlarged to its full all-norm
completion, requiring a new owner and new infinite-support arguments.
The parent is not edited, retrospectively completed or credited with
these new states.

The [source lineage](../../docs/prior_work/README.md) is proper-factor
admissibility -> integer multiplicative words -> the indecomposable
quotient -> positive geometry -> a completion containing all rapidly
decaying arithmetic mixtures. This is a specified replacement and
extension of the prime/composite symbolic source. It is not an executed
trial-division flow or an asserted Logistic/Henon conjugacy.

| Field | Frozen owner | Boundary |
| --- | --- | --- |
| Arithmetic source | A=real monoid algebra of all positive integers, I=span of its nonunits, Q=I/I^2 | No prime predicate, prime table or target-zero data |
| Completion | Completion of Q for every quotient coefficient norm \|\|.\|\|_k, k>=0 | Not the lone unweighted completion or coordinate-product topology |
| Positive carrier | Closure of the finite nonnegative cone, with zero removed | Every permitted infinite support remains present |
| Integer action | Continuous extension of D(e_n)=n e_n and its inverse | Existence on the full completion must be proved |
| Full flow | X_hat=P_hat/<D>, phi_t[v]=[exp(t)v] | Same global speed, no prescribed per-prime roof |
| Periodic convention | All actual primitive time orbits and all positive repetitions | No finite-support inference for new states |
| Analytic / classical owner | NOT SUPPLIED | No trace, determinant, Hilbert, symplectic, contact or Hamiltonian assertion |

Naturalness remains OPEN for the algebraic quotient, positivity and scale
law. A successful completion does not distinguish these engineering
choices from every alternative arithmetic norm.

## 2. Exact identification and completeness of the new space

Write e_m e_n=e_(mn) in A, with all vectors initially finitely supported.
The subspace I^2 is exactly the span of composite e_n: products of two
nonunits are composite, and every composite has such a factorization.
Thus Q has basis q_p=[e_p] for primes p. This description is derived
from all integer multiplication, not used as an external input alphabet.

For a finite vector q=sum_p b_p q_p, the frozen quotient seminorm is

\[
\|q\|_k=
\inf_{q=[\sum a_ne_n]}\sum_{n\ge2}n^k|a_n|
=\sum_p p^k|b_p|,\qquad k\ge0.
\tag{1}
\]

Every representative has the same prime coefficients, and setting its
composite coefficients to zero attains the infimum. These are norms.

**Proposition 1 (the entire completion).** The frozen completion E is
canonically the real space

\[
E=\left\{b=(b_p):\|b\|_k=\sum_p p^k|b_p|<\infty
\text{ for every integer }k\ge0\right\}
\tag{2}
\]

with its countable-family norm topology. It is a complete metrizable
locally convex vector space. Finite vectors are dense. The closed
positive cone C is exactly the vectors b_p>=0, and P_hat=C minus {0}.

**Proof.** The metric sum_(k>=0) 2^(-k-1) min(1,||b-c||_k)
gives the displayed topology. A sequence Cauchy in every norm has a
limit in each coordinate, since |b_p-c_p|<=p^(-k)||b-c||_k.
Fix k and epsilon>0, and take j,l sufficiently large that
||b^(j)-b^(l)||_k<epsilon. On any finite set of coordinates, let
l tend to infinity in this inequality. Taking the supremum over finite
coordinate sets then gives ||b^(j)-b||_k<=epsilon. For one such j,
||b||_k<=||b^(j)||_k+epsilon<infinity. This holds for every k,
proving both membership in (2) and convergence in the actual topology.

For any b in (2), retain coordinates p<=N. The tail of each convergent
nonnegative sum in (2) tends to zero as N grows, so these same finite
truncations converge in every norm. Hence (2) is precisely the
completion of (1), not a larger product space. Coordinate evaluation
is continuous, so closure of finite nonnegative vectors has no negative
coordinate. Conversely truncating any nonnegative b in (2) gives
nonnegative finite approximants. This proves the cone assertion. QED.

For a genuine new state take the all-integer-defined limit

\[
v_* = \lim_{N\to\infty}\sum_{n=2}^{N}e^{-n}q_n.
\tag{3}
\]

For every k its coefficients are dominated by the convergent sum
sum_(n>=2)n^k e^(-n). Its nonzero coordinates are e^(-p) for every
prime p. There are infinitely many such coordinates by the elementary
Euclidean infinitude argument. Thus completion has added actual states,
not merely changed a name or a topology on the same finite set of supports.

Completeness in Proposition 1 concerns E. It does not assert that the
punctured cone P_hat is complete in the restricted metric: for example
j^(-1)q_2 tends to the removed zero. Flow completeness below is a
separate property of an explicit global time law.

## 3. Full multiplier, quotient topology and real-time completeness

Define (Db)_p=p b_p and (D^(-1)b)_p=p^(-1)b_p. On the entire E,

\[
\|Db\|_k=\|b\|_{k+1},\qquad
\|D^{-1}b\|_k\le\tfrac12\|b\|_k.
\tag{4}
\]

These are mutually inverse continuous linear maps, preserving C and
P_hat. They agree with the frozen maps on dense Q, so they are their
unique continuous extensions. This is not a bounded-operator assertion
in the single norm ||.||_0. All integer powers preserve every state.

On P_hat let m(v)=||v||_0=sum_p v_p. It is finite, continuous and
strictly positive. For every integer j>=0,

\[
m(D^jv)\ge2^j m(v),\qquad
m(D^{-j}v)\le2^{-j}m(v).
\tag{5}
\]

**Proposition 2 (complete full quotient owner).** The D action on
P_hat is free and locally properly discontinuous. Its quotient X_hat
is Hausdorff, and phi_t[v]=[exp(t)v] is a jointly continuous complete
real flow on every retained state, including infinite support.

**Proof.** Equation (5) excludes a fixed point of any nontrivial D
power. A mass annulus a<m(v)<b with 0<a<b<2a is disjoint from
each of its nontrivial translates, giving the local assertion.

For two inequivalent states choose neighborhoods whose masses lie in
a common interval [a,b] in (0,infinity). If an integer translate of
one neighborhood meets the other, then 2^(|j|)a<=b. Only finitely
many j qualify. For each, the two reference states are not related
by D^j, so the Hausdorff topology of E permits neighborhoods whose
corresponding translates are disjoint. Intersect these finitely many
choices. Their full saturated open sets remain disjoint, producing
disjoint open quotient neighborhoods. This proves Hausdorff separation
without an assumption of local compactness. Likewise each compact set
has positive minimum and finite maximum mass and meets only finitely
many of its integer translates.

Multiplication by exp(t) preserves (2) and the positive punctured cone
for every real t, is jointly continuous, and commutes with D. It
descends to the asserted action. The quotient map pi_hat is open,
because saturation is a union of homeomorphic translates. Therefore
id_R times pi_hat is an open quotient map, so the descended action
is jointly continuous. Exponential addition gives the group law and
the inverse at time -t. The formula exists for every real time,
independently of a section or a finite-support approximation. QED.

## 4. The true section on all infinite as well as finite supports

Let S_hat={u in P_hat:m(u)=1}. Put

\[
F(u)=\frac{D^{-1}u}{m(D^{-1}u)},\qquad
\tau(u)=-\log m(D^{-1}u).
\tag{6}
\]

The mass in (6) is strictly positive even for infinite support and
at most 1/2. Thus F is continuous, tau is continuous and tau>=log 2.
The inverse map is F^(-1)(u)=Du/m(Du), defined on every u by (4).

**Proposition 3.** pi_hat(S_hat) is an embedded global section, (6)
is its actual first return and elapsed roof, and its complete endpoint
suspension is time-preservingly homeomorphic to X_hat.

**Proof.** The mass annulus 3/4<m<5/4 has disjoint nontrivial D
translates and contains all of S_hat. Its open quotient chart embeds
the entire section with the original subspace topology. The map

\[
S_{\!\mathrm{hat}}\times\mathbb R\longrightarrow P_{\!\mathrm{hat}},
\qquad (u,r)\longmapsto e^r u
\tag{7}
\]

is a homeomorphism, with inverse v->(v/m(v),log m(v)). In these
coordinates D^(-1) is exactly (u,r)->(Fu,r-tau(u)). This conjugates
the full integer actions, not merely half-open fundamental sets.

All section-intersection times from [u] are

\[
t_j(u)=-\log m(D^{-j}u),\qquad j\in\mathbb Z.
\tag{8}
\]

Here t_0=0, and (5) gives t_(j+1)-t_j>=log 2 for every integer
j. Consequently t_1 is the true first positive return, with no
additional crossings; these times tend to plus and minus infinity
in their respective directions. The intervals between consecutive
times give the full endpoint suspension and its topology through
(7). No new infinite-support state has finite-time return accumulation.
QED.

## 5. Every completed-state packet and the actual old-owner embedding

**Theorem 4 (no hidden packets after completion).** The entire X_hat
has one primitive oriented circle per prime p, of least time log p,
with repetitions r log p. Every state with at least two nonzero
coordinates, including every infinite-support state, has trivial time
stabilizer. There is no additional stationary point.

**Proof.** A return of [v] at time t means one common integer j obeys
exp(t)v=D^jv. Continuous coordinate evaluation gives
exp(t)=p^j at every coordinate with v_p>0. If j=0, then t=0.
For j nonzero, two distinct positive integers cannot have equal j-th
powers. Thus every nonsingleton support has only the zero return time.
This is a direct equation on each full state, not a limit of finite
packet classifications.

On support {p}, the stabilizer is exactly (log p)Z. All positive
amplitudes are connected by actual radial time, so this is one circle
rather than multiple amplitude packets. Distinct prime supports are
not related by D or by the flow. Every state has nonempty support;
the listed discrete or trivial stabilizers rule out a stationary
point. The least and repeated times follow at once. QED.

**Proposition 5 (dense time-preserving topological embedding).** The
193 flow is a dense invariant topological subflow of this new flow.
The same statement holds for the normalized return sections.

**Proof.** Let P_fin be the old positive punctured cone. Its original
norm-family topology is the subspace topology from E, and it is dense
in P_hat by positive truncations. It is D-saturated: multiplication
by a nonzero coordinate multiplier never changes support. Thus its
old quotient maps injectively to X_hat with exactly the old fibers.

For any open O in P_hat, saturation gives

\[
\pi_{\!\mathrm{hat}}(O\cap P_{\mathrm{fin}})
=\pi_{\!\mathrm{hat}}(O)\cap
  \pi_{\!\mathrm{hat}}(P_{\mathrm{fin}}).
\tag{9}
\]

Since pi_hat is open, its restriction to P_fin is an open continuous
surjection onto that image with its subspace topology. Its induced
map from the old quotient is therefore a homeomorphism onto the
image, not just a set injection. Every nonempty open set of X_hat
has an open nonempty preimage and thus meets the image of dense
P_fin. The flow formulas agree on P_fin and preserve it, proving
density and time-preserving invariance. Normalizing positive truncations
by their converging masses proves density on S_hat; the formulas in
(6) restrict to the old return map and roof. QED.

The embedding is not onto: the state (3) and its entire quotient
orbit retain infinite support under D and radial time. No finite
state represents that orbit.

## 6. Adverse controls: why this particular completion matters

**Only the unweighted norm.** Its completion is ordinary real l1 over
the derived atoms. Enumerate them increasingly as p_j; then p_j>=j+1.
The positive vector b_(p_j)=1/(j p_j) belongs to l1, because its mass
is at most sum_j 1/(j(j+1)). But D b has coefficients 1/j and
infinite mass. Thus D is not a full-space self-map on that larger
punctured l1 cone. This changed-owner control stops before a full
quotient flow; it cannot replace the all-norm space (2).

**Only coordinate-product topology.** On the old finite positive cone,
q_2+q_(p_j) tends coordinatewise to q_2 as p_j tends to infinity,
but its mass is always 2 rather than 1. The mass used in our section
is not continuous for that topology. This is not a theorem that every
other product-topological quotient is non-Hausdorff; it rules out
silently substituting that topology in the present proof.

**Retain zero.** D^(-j)v tends to zero in every norm by (4). Thus,
in the quotient of the full cone C including zero, each nonzero D
orbit has zero in its closure. Its singleton quotient class is not
closed, so this enlarged quotient is not T1, hence not Hausdorff.
Zero also supplies a stationary orbit. Removing it was a frozen
definition, not a post-proof repair.

**Signs and complex phases.** If those changed carriers are admitted,
the same radial law gives two sign circles per prime or a continuum
of complex-phase circles. The main positive cone has neither extension.
Keeping positive infinite mixtures, in contrast, really is within
the frozen owner and creates no hidden periodic packet by Theorem 4.

**Clock design.** With the changed uniform speed exp(c t), c>0,
the same return equation gives (log p)/c. Replacing the underlying
multiplicative generator norm can likewise change the clock. Those
are different declared designs, and the ability to complete this
one does not prove it uniquely natural or physically selected.

## 7. Decision and limits

| Obligation | Exact result | Status / limit |
| --- | --- | --- |
| Full completion and positivity | Proposition 1 and the explicit infinite state (3) | ESTABLISHED; E is complete, not the punctured cone in every inherited metric |
| Full quotient and real-time owner | Propositions 2--3 on every new state | ESTABLISHED topological AQC construction, no local compactness assumed |
| Primitive clock and repetitions | Theorem 4 for every finite or infinite support | ESTABLISHED, one log-prime circle per prime |
| Relation to old 193 | Proposition 5, dense invariant topological embedding | ESTABLISHED, not equality of the two carriers |
| Arithmetic/source-clock naturalness | Same explicit quotient, positivity and scale controls remain | OPEN; no natural A0 claim |
| Analytic operator or determinant | No analytic contract frozen here | NOT SUPPLIED; no credit from neighboring branches |
| Classical geometry / formal Route / Route B | No classical owner or formal protocol | NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

Decision: ADVANCE the completed-carrier construction. The extension adds
genuine infinite-support states without changing the prime-only packet
law, and its exact relation to 193 is proved. This audit ends at that
result. A Hilbert representation, conservative geometric lift or
analytic trace requires its own frozen owner and compatibility proof;
a theorem for finite-support functions alone cannot be transferred here.

## Evidence and reproducibility

The [card](candidate-card.md) fixes all inputs; the [claim ledger](claim-ledger.md)
and [evidence index](evidence/README.md) distinguish exact proof, controls,
review and mechanical verification. Every infinite assertion above is
proved by summability bounds, coordinate equations or quotient topology.
Truncations are used to prove density, never as numerical evidence for
the full periodic ledger. No numerical computation, precision choice,
data table, experiment script or external theorem is needed. ARS is
limited to claim/evidence/reasoning and adverse scope checks; the
separate model review is nonblind and not human peer review.
