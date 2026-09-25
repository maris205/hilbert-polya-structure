# Prime circles from a full indecomposable cone and radial quotient

**Paper ID:** 193-indecomposable-radial-quotient  
**Candidate ID:** AQC-20260916-IRC01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — HAUSDORFF FULL-CONE FLOW WITH ONE LOG-PRIME CIRCLE PER PRIME; DECLARED DESIGN; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

We define the indecomposable quotient of the real multiplicative monoid
algebra of all positive integers, retain its entire nonzero finite-support
positive cone, and divide by the integer-size automorphism. Common radial
dilation descends to a complete Hausdorff flow. Its complete primitive
ledger has exactly one circle per prime, of actual length log p, and
no mixed-support periodic orbit. The clock and elimination of duplicate
amplitudes follow from the same quotient action. A global section has a
derived nonconstant roof bounded below by log 2. This is a nonclassical
cone-quotient construction, not a symplectic or analytic realization.
The indecomposable quotient, positivity and scale normalization are
declared designs; their arithmetic naturalness is not proved. No trace
or zeta construction is appended to this bounded packet audit.

## 1. New owner, precise source lineage and question

The [version-1 card](candidate-card.md) was frozen before this proof.
The source is all integer factor multiplication. The lineage is
proper-factor admissibility -> multiplicative factor words -> quotient
by products of two nonunits -> a positive geometric carrier -> an actual
radial quotient flow. This is an algebraic replacement of the
[prime/composite symbolic source](../../docs/prior_work/README.md), not
a time-dependent fit or a claim of Logistic/Henon conjugacy.

This is a new successor to the stopped
[186](../186-multiplicative-bar-clock/README.md). That candidate retained
all bar homology and used a complex unit-modulus character. This one
defines I/I^2 at the outset, works over the real positive cone, and
uses a radial flow on an integer-dilation quotient. Neither its object
nor its proof changes 186's higher composite homology or STOP verdict.
It is also separate from the six frozen lines of
[192](../192-six-architecture-source-frontier/candidate-card.md).

| Field | Same-object definition | Limit |
| --- | --- | --- |
| Arithmetic source | All positive integers, monoid multiplication, and the ideal of nonunits | No prime predicate/list or zero data in the definition |
| Algebraic replacement | Q=I/I^2 | Declared indecomposable observable, not full bar homology |
| Topology | All quotient weighted coefficient norms on finite support | No completion or coordinate-product topology |
| Geometric carrier | Entire nonzero positive cone P, then X=P/<D> | Every mixed finite support is retained |
| Discrete action | D(e_n)=n e_n | One multiplicative integer-size law, not independently assigned prime parameters |
| Time action | phi_t[v]=[exp(t)v] | One universal radial speed; no character or imposed orbit length |
| Packets | Every actual primitive time orbit in X | No representative, amplitude or eigenline is counted without proof |
| Classical and analytic owners | NOT SUPPLIED | No symplectic form, Hamiltonian, contact form, Hilbert generator, trace or determinant |

The [163 card](../163-ordered-cover-scale-suspension/candidate-card.md)
is a nearby scale-flow comparison. Its full two-sided ordered cover
chains are not this cone. This construction has neither symbolic
monotonicity constraints nor sequence shifts. The shared universal
dilation idea does not transfer its topology, trace or orbit results;
all required claims are proved here. No global novelty is asserted.

## 2. The entire indecomposable source and its topology

Let A be the real vector space on e_n for all n>=1, with finite linear
support and multiplication e_m e_n=e_(mn). Its unit is e_1. Let I be
the span of e_n for n>=2 and put Q=I/I^2. Write q_n for the class of e_n.

**Lemma 1.** Q has basis q_p for all primes p. Every composite q_n
vanishes, and no nonzero linear combination of prime classes vanishes.

**Proof.** I^2 is the span of products e_a e_b=e_(ab), a,b>=2.
Every such product is composite, and every composite is such a product.
Thus I^2 is exactly the coordinate span of all composite basis vectors,
not a subspace containing any prime basis direction. QED.

This is an all-integer proof of the quotient, not a preselected alphabet.
It does not assert that the complete homology of a bar complex equals Q.

For k>=0 define the frozen quotient seminorm

\[
\|q\|_k=\inf\left\{\sum_{n\ge2}n^k|a_n|:
q=\left[\sum a_ne_n\right],\quad\text{finite support}\right\}.
\tag{1}
\]

By Lemma 1, if q=sum_p b_p q_p, every representative must have
the same prime coefficients b_p. All composite coefficients can be
set to zero. Consequently

\[
\|q\|_k=\sum_p p^k|b_p|.
\tag{2}
\]

Every (1) is therefore a norm, and their countable family defines a
Hausdorff topological vector space on the algebraic finite-support Q.
For example a compatible translation-invariant metric is
sum_(k>=0) 2^(-k-1) min(1,||q-q'||_k). Completeness is not asserted.

Let P be the image of all finite nonnegative coefficient sums in I,
excluding the zero class. Equivalently, now as a proved description,

\[
P=\left\{\sum_p b_pq_p:b_p\ge0,
\ 0<\sum_p b_p<\infty,\ \text{finite support}\right\}.
\tag{3}
\]

It has the subspace topology from (1). The continuous positive mass
m(v)=||v||_0 equals sum_p b_p. There is no maximum support size, and
v=q_2+q_3 and all its radial translates belong to P. Removing zero
was part of the frozen definition; otherwise its fixed point would
require a different full orbit convention.

## 3. The quotient really is Hausdorff and owns a complete flow

The map D(e_n)=n e_n and its inverse e_n->n^(-1)e_n are algebra
automorphisms preserving I and I^2. They induce mutually inverse maps
on Q preserving P. Equations (1)--(2) imply

\[
\|Dq\|_k=\|q\|_{k+1},\qquad
\|D^{-1}q\|_k\le\tfrac12\|q\|_k.
\tag{4}
\]

Both are continuous for the stated topology. In particular D is not
being treated as a bounded operator for the single norm ||.||_0.
For v in P and j>=0,

\[
m(D^jv)\ge2^j m(v),\qquad
m(D^{-j}v)\le2^{-j}m(v).
\tag{5}
\]

**Proposition 2.** The integer action generated by D on P is free;
the quotient X=P/<D> is Hausdorff. The action is properly discontinuous
locally and has finite intersections on compact sets. The radial
action defines a jointly continuous complete real flow on all X.

**Proof.** Equation (5) rules out D^j v=v for j nonzero. For a small
neighborhood U of v impose a<m(w)<b with 0<a<b<2a. Then no two
distinct D-translates of U meet, by (5). This gives local disjoint
neighborhoods without a local-compactness assumption.

For the Hausdorff assertion take inequivalent v,w in P. Choose
neighborhoods U_0,V_0 of them with mass in a common compact interval
[a,b] in (0,infinity). If D^j U_0 meets V_0, (5) implies
2^(|j|)a<=b. Only finitely many integers j are possible. For each
of them D^j v differs from w, so the Hausdorff topology of P and
continuity of D^j allow U_0,V_0 to be shrunk to U_j,V_j with
D^j U_j disjoint from V_j. Intersect these finitely many neighborhoods.
Their saturated open sets under all D powers are disjoint and descend
to disjoint neighborhoods in X. Thus X is Hausdorff.

Likewise a compact K in P has positive minimum and finite maximum
mass, so D^jK meets K for only finitely many j. No conclusion here
assumes that P is locally compact or a finite-dimensional manifold.

Scalar multiplication (t,v)->exp(t)v is jointly continuous on P,
commutes with D and preserves P for every real t. It therefore
descends to phi_t[v]=[exp(t)v]. The quotient map pi:P->X is open,
since the saturation of an open set is the union of its D-translates.
Thus id_R times pi is an open quotient map, proving joint continuity
of the descended action. Exponential addition gives the group law;
the formula exists for every real time and every state, with inverse
phi_(-t). This is full flow completeness, independent of any section.
QED.

The proof supplies a topological arithmetic cone-quotient flow only.
It does not equip its support faces with symplectic forms or prove
lamination charts across their boundaries.

## 4. A section and actual elapsed return time

Let S={v in P:m(v)=1}. Restricting pi to S is injective by (5).
Set

\[
F(u)=\frac{D^{-1}u}{m(D^{-1}u)},\qquad
\tau(u)=-\log m(D^{-1}u),\qquad u\in S.
\tag{6}
\]

These expressions are derived from the full flow; they are not new
frozen parameters. The denominator is strictly positive and at most
1/2, so tau is continuous and tau>=log 2. F is a homeomorphism with
inverse u->Du/m(Du).

**Proposition 3.** pi(S) is an embedded global section with first
positive return F and actual roof tau in (6). The complete endpoint
suspension of these data is homeomorphic to X, preserving time.

**Proof.** The map

\[
S\times\mathbb R\longrightarrow P,\qquad (u,r)\longmapsto e^r u
\tag{7}
\]

is a homeomorphism: its inverse is v->(v/m(v),log m(v)). In these
coordinates D^(-1) becomes

\[
(u,r)\longmapsto(Fu,r-\tau(u)).
\tag{8}
\]

The quotient of (7) therefore identifies the full time-cover quotient
with X. For an explicit section chart put
U={v in P:3/4<m(v)<5/4}. Equation (5) shows D^j U is disjoint
from U for j nonzero. The open quotient map restricted to U is a
homeomorphism onto its image. Since S is contained in U, pi(S)
has exactly its original subspace topology and is globally embedded.

A positive return from [u] to pi(S) requires
m(D^(-j)e^t u)=1 for an integer j, hence

\[
t=t_j(u)=-\log m(D^{-j}u).
\tag{9}
\]

For j<=0 the time is nonpositive. For j>=1 the times strictly
increase, and t_(j+1)-t_j>=log 2 by (5). The first is j=1,
giving precisely (6). Iterating (6) telescopes to (9), so the
successive sections cover the complete flow. The same lower bound
holds in reverse time. The usual endpoint identifications
(u,tau(u))~(Fu,0) consequently give a homeomorphic fundamental
suspension, with no finite-time accumulation of returns. This also
follows by choosing the unique interval between consecutive times
(9), in either direction, in the time cover (7). QED.

For a mixed normalized state u=(q_2+q_3)/2, the exact values are
F(u)=(3q_2+2q_3)/5 and tau(u)=log(12/5). This state is retained,
and its roof is not a per-prime roof assigned to a chosen axis.

## 5. All primitive packets, not just a selected axis calculation

**Theorem 4.** The entire X has exactly one nonconstant primitive
oriented closed orbit gamma_p for each prime p. Its least positive
period is T_p=log p and its r-fold repetitions have period r log p.
Every mixed-support state has trivial time stabilizer; no additional
fixed point or nonconstant periodic orbit is hidden in X.

**Proof.** For any v=sum_p b_pq_p in P, a time t returns [v] to
itself exactly when there is one integer j with

\[
e^t v=D^jv.
\tag{10}
\]

Comparing every nonzero coefficient gives e^t=p^j for each p in
the support. If j=0 this forces t=0. If two distinct primes occur,
equality of their j-th powers with j nonzero is impossible. This
uses only injectivity of a nonzero integer power on positive numbers,
not rational independence of logarithms. Thus every mixed-support
state has trivial stabilizer.

For a singleton support p, equation (10) says t=j log p. Its time
stabilizer is exactly (log p) Z, so the least positive time is
log p, and the positive repeats are all and only r log p.
All b q_p with b>0 lie on the same actual radial orbit: choosing
t=log(b'/b) maps b q_p to b' q_p already before the D quotient.
Consequently they form one circle, not a continuum of amplitude
packets. Its quotient topology is that of R/(log p)Z via b=e^r,
as also follows from Proposition 3 on the singleton section point.
Different supports cannot be identified by D or the radial flow,
so distinct primes give distinct circles. Every state has a nonempty
finite support and is covered by these cases; none is fixed for
every real time. QED.

The whole carrier was not replaced by the union of these circles.
For example the entire mixed q_2+q_3 orbit remains aperiodic. The
section normalizes a coordinate representation of every radial state;
it is not a deletion of amplitudes, unlike restricting an unrelated
unitary character action to chosen basis vectors.

## 6. Adverse controls and the meaning of this advance

| Control | Exact implication | Limit |
| --- | --- | --- |
| Do not quotient I by I^2 | Every integer basis direction, including 4 and 6, yields its own radial circle | The indecomposable quotient is responsible for prime selectivity and is declared engineering |
| Retain all mixed positive supports | Equation (10) gives trivial stabilizer | No ordering or deletion of mixed states causes prime-only recurrence |
| Compare 186's full bar homology and complex character | Its weight-6 H_2 and reciprocal-logarithmic point time persist there | This theorem does not repair or transfer a verdict to 186 |
| Enlarge to the full real punctured quotient | Each prime has separate positive and negative radial circles | Positivity is an explicit carrier choice; this is a different-owner control |
| Enlarge to the complex punctured quotient with the same radial action | The phase of a singleton coefficient is invariant, giving continuously many prime circles | A Hilbert/complex extension would require its own full packet audit |
| Change radial speed to exp(c t), c>0 | The same equation yields periods (log p)/c | Original speed 1 is declared, not uniquely forced by arithmetic |
| Replace the integer monoid by a free commutative monoid with distinct generator multipliers lambda_a>=2 | The same finite-support argument yields one circle of length log lambda_a per generator | PROVES_TOO_MUCH: an engineered packet mechanism alone does not prove arithmetic naturalness |

For the last control the multipliers define a different multiplicative
norm and its corresponding quotient coefficient topology. Distinctness
is essential: equal generator multipliers would admit mixed recurrent
directions. This comparison proves no classification of other norms.

| Owner-level obligation | Result | Boundary |
| --- | --- | --- |
| T0 carrier and ownership | Hausdorff full cone quotient, complete action and actual global section | ESTABLISHED in the declared topological AQC category |
| T1-style source and clock | Indecomposables derived; actual time derived from the common dilation quotient | Scoped construction ESTABLISHED; source-clock naturalness OPEN |
| T2 full packets and repetition | Theorem 4 covers every state and every repeat | ESTABLISHED; not a selected periodic subcarrier |
| T3 trace/zeta/operator | No such analytic contract frozen here | NOT INVOKED / NOT SUPPLIED |
| Classical A0--A2 | No classical symplectic object is supplied | NOT APPLICABLE; stronger natural A0 is not closed |
| Formal Route coordinates / Route B | No formal protocol run | UNASSIGNED / NOT INVOKED |

Decision: ADVANCE this scoped complete-carrier construction. It genuinely
changes the mechanism of the stopped character proposal and supplies a
full mixed-state owner with the desired packet law. It does not establish
a unique natural source-clock law, physical symplectic realization or
analytic operator. The bounded audit ends here; any analytic, complex,
Hamiltonian or completed-space extension needs a fresh card and its
earliest full-owner discriminator. Neither the previous stopped object
nor a different owner's determinant can supply that next result.

## Evidence and reproducibility

All inputs precede proof in the [card](candidate-card.md). The
[ledger](claim-ledger.md) separates construction, controls and OPEN
claims. The [evidence index](evidence/README.md) records actual separate
review and the final mechanical checks. This is a self-contained exact
argument: the Hausdorff proof is supplied, not inferred from a proper-
action theorem with unverified local-compactness hypotheses. No sampled
orbits, arithmetic table, fitted time, experiment script or numerical
precision is used. ARS is limited to claim/evidence/reasoning and adverse
scope checks; actual different-invocation model review is nonblind,
not human peer review or a certificate of independent errors.
