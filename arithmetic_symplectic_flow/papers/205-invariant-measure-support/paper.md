# Finite invariant measures see only the circles, not the whole flow

**Paper ID:** 205-invariant-measure-support  
**Candidate ID:** AQC-20260916-IMS01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — ALL INVARIANT PROBABILITIES CLASSIFIED; FULL-STATE L2 FAITHFULNESS FAILS; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

Every invariant Borel probability measure of the entire completed
positive-cone quotient is an arbitrary countable mixture of normalized
time measures on its singleton-support circles. The proof uses a
deck-invariant logarithmic coordinate on every two-positive-coordinate
open set. Actual time translates that coordinate at a nonzero constant
speed, so disjoint equal-measure strips force every such set to have
zero finite invariant measure. Countably many pairs cover all mixed
states, including infinite supports. This does not remove those states
from the flow. An explicit bounded continuous scalar observable is
nonzero on mixed states but zero in every such L2 space. Infinite
invariant orbit measures provide a control showing why finiteness is
essential. This is a measure/observation result for the fixed 194
geometry, not a general Hilbert obstruction, arithmetic-naturalness
result, spectral identification or borrowed determinant.

## 1. Frozen object, lineage and observation contract

The [version-1 card](candidate-card.md) precedes the proof. The geometry
is exactly [194](../194-rapid-decay-cone-completion/paper.md): let
A be the real monoid algebra of all positive integers, with
e_m e_n=e_(mn), let I be its nonunit span, and Q=I/I^2. The nonzero
atom classes q_a are derived from this algebra. Since I^2 is exactly
the composite span, a ranges over primes, but no prime table was an
input. Write this countable derived index set as mathcal A. Then

\[
E=\left\{v:\|v\|_k=\sum_{a\in\mathcal A}a^k|v_a|<\infty
\text{ for all integers }k\ge0\right\},\quad
\widehat P=\{v\in E:v_a\ge0\}\setminus\{0\},
\tag{1}
\]

\[
(Dv)_a=a v_a,\qquad
\widehat X=\widehat P/\langle D\rangle,\qquad
\phi_t[v]=[e^t v].
\tag{2}
\]

Keep the all-norm topology, its cone subspace topology and the actual
quotient topology. Every finite and infinite support remains present.
The 194 proof establishes that D is a homeomorphism on all of E,
the quotient is Hausdorff, its quotient map pi is open, and phi is
a complete jointly continuous flow. Its unit-mass section has the
actual map F(u)=D^(-1)u/c(u), roof -log c(u), and c(u)=sum_a u_a/a.
These are geometric dependencies, not a measure classification.

The same dependency proves that each singleton support gives exactly
one circle gamma_a, of least time L_a=log a and all positive repeated
times, whereas every mixed support is aperiodic. No new return map,
clock, section, roof or periodic convention is introduced here.

The [source lineage](../../docs/prior_work/README.md) is proper-factor
symbolic admissibility -> all-integer multiplication -> indecomposable
quotient -> positive-cone geometry -> full-state observation. The
current argument retains this precise source and owner; it does not
assert a Logistic/Henon conjugacy or use the external Paper-6 benchmark
as a theorem. Source quotient, positivity, size rule, topology and
speed remain declared designs with naturalness OPEN.

The measures under audit are countably additive Borel probabilities
mu on all of X_hat, invariant under every actual phi_t. No regularity,
local compactness or prior full-support property of mu is assumed.
The associated observation contract is the natural map

\[
\iota_\mu:C_b(\widehat X;\mathbb C)\longrightarrow
L^2(\widehat X,\mu),\qquad f\longmapsto[f]_\mu.
\tag{3}
\]

Boundedness and finite mass make this map defined. Faithfulness here
means injectivity as a map of actual continuous scalar observations,
not some unrelated embedding of an abstract vector space in a Hilbert
space. The L2 time pullback, when mentioned, uses this same phi_t.

## 2. A full-owner translation coordinate on every mixed pair

For two derived atoms a<b define the invariant open set

\[
U_{ab}=\{[v]:v_a>0,\ v_b>0\}\subset\widehat X.
\tag{4}
\]

Its preimage in P_hat is open, since the two coordinate evaluations
are continuous. It is saturated under D, so its image is open in
the actual quotient. Both deck multiplication and radial time preserve
the two positive coordinates.

**Lemma 1 (a genuine time coordinate on each pair set).** The formula

\[
h_{ab}([v])=\frac{\log v_a}{\log a}
             -\frac{\log v_b}{\log b}
\tag{5}
\]

defines a continuous real function on U_ab, and

\[
h_{ab}(\phi_t x)=h_{ab}(x)+t c_{ab},\qquad
c_{ab}=\frac1{\log a}-\frac1{\log b}>0.
\tag{6}
\]

**Proof.** Replacing v by D^j v adds j to each term of (5), so
their difference is unchanged for every integer j. The continuous
function on the saturated preimage therefore descends continuously:
the restriction of the open quotient map to that saturated open set
is again a quotient map. Multiplying v by exp(t) adds t/log a and
t/log b to the respective terms, proving (6). Distinctness a<b and
a>1 make c_ab strictly positive. No other coordinate is changed or
discarded in this argument; v can have arbitrary infinite support.
QED.

The function h_ab is not proposed as a global coordinate on X_hat
or as a new physical clock. Its elementary covariance under the
already fixed physical time is the discriminator.

**Lemma 2 (no finite invariant mass on a mixed pair set).** Every
finite nonnegative invariant Borel measure mu on X_hat satisfies
mu(U_ab)=0.

**Proof.** In U_ab take the Borel strip

\[
W_{ab}=\{x:0\le h_{ab}(x)<c_{ab}\}.
\tag{7}
\]

By (6), the sets phi_n(W_ab), n in Z, are precisely the strips
n c_ab<=h_ab<(n+1)c_ab. They are pairwise disjoint and cover U_ab.
All are Borel because phi_n is a homeomorphism, and invariance makes
their measures equal to mu(W_ab). Arbitrarily many disjoint strips
in a finite measure space imply mu(W_ab)=0. Countable additivity
then gives mu(U_ab)=0. This proof needs only invariance under the
unit-time map; no recurrence theorem or countable topological base
is used. QED.

## 3. Complete classification of invariant probabilities

Let Gamma be the union of all singleton circles gamma_a. A positive
nonzero vector outside that union has at least two positive coordinates,
so exactly

\[
\widehat X\setminus\Gamma=\bigcup_{a<b}U_{ab}.
\tag{8}
\]

There are only countably many pairs, and all sets in this union are
open. Thus Gamma is closed and Borel, not just a set selected from
the periodic ledger. In particular (8) covers every infinite support.

For each a let lambda_a be normalized time measure on gamma_a:
it is the pushforward of ds/L_a on R/(L_a Z) under
s->[exp(s)q_a]. This map is a continuous bijection of the circle
onto gamma_a by the exact return equation from 194; compactness of
its domain and Hausdorffness of X_hat make it a homeomorphism.
Consequently gamma_a is compact and closed, and lambda_a is a Borel
probability invariant under every actual time translation.

**Theorem 3 (all invariant probabilities, with no hidden mixed mass).**
A Borel probability mu on the whole X_hat is flow invariant if and
only if, for a unique family w_a>=0 with sum_a w_a=1,

\[
\mu=\sum_{a\in\mathcal A}w_a\lambda_a.
\tag{9}
\]

In particular every such measure gives Gamma full measure and gives
the entire mixed-state locus zero measure. A finite nonnegative
invariant measure has the same formula with sum_a w_a=mu(X_hat),
including the zero measure.

**Proof.** Lemma 2 and (8) give mu(X_hat minus Gamma)=0. The circles
are pairwise disjoint invariant Borel sets, so w_a=mu(gamma_a) are
nonnegative and sum to one. If w_a>0, the normalized restriction of
mu to gamma_a is a rotation-invariant probability on the time circle
R/(L_a Z).

For completeness such a probability must be normalized length. Its
singletons all have the same mass by rotation invariance; arbitrarily
many distinct points force that mass to be zero. Partition the circle
into n half-open arcs of equal length L_a/n. Each has mass 1/n,
and each union of m consecutive arcs has mass m/n. Translation gives
the same answer for any starting point. Approximation of any arc length
from below and above by rational multiples of L_a, together with
countable additivity and zero endpoint masses, gives its length divided
by L_a. These half-open intervals generate the circle's Borel sets;
finite measures agreeing on intervals agree on their generated Borel
sigma algebra by the elementary uniqueness property for finite
measures. Thus the normalized restriction equals lambda_a. Countable
additivity on Gamma proves (9).

Conversely any countable sum in (9) is a Borel probability. Invariance
of each summand and nonnegative countable summation give invariance
under every phi_t. The masses of the disjoint circles recover every
w_a, proving uniqueness. For nonzero finite total mass normalize
first; zero total mass means the zero measure. QED.

This is concentration on the union of circles, not a claim that one
single circle supports all measures. For example (lambda_2+lambda_3)/2
and mixtures with every w_a positive are legitimate invariant
probabilities. Their choice is additional measure data, not a preferred
measure supplied by the geometry.

## 4. The precise loss in every finite invariant L2 observation

**Proposition 4 (one common nonzero continuous observation is lost).**
There exists a real f in C_b(X_hat), nonzero on mixed states and zero
on Gamma, such that iota_mu(f)=0 for every invariant probability mu.
Thus none of the maps (3) faithfully retains all bounded continuous
observations of the unchanged topological owner.

**Proof.** Set m(v)=sum_a v_a and

\[
\eta(r)=\max\{0,1-4|r-1|\},\qquad
\psi(v)=\eta(m(v))\frac{v_2v_3}{m(v)^2}.
\tag{10}
\]

The coordinates 2 and 3 name derived atom classes; (10) is an
observation test, not an inserted arithmetic mechanism or clock.
Both functions are continuous on their respective domains, and
0<=psi<=1/4. It can be nonzero only when 3/4<m(v)<5/4 and both
specified coordinates are positive. Define on the full cover

\[
\widetilde f(v)=\sum_{j\in\mathbb Z}\psi(D^jv).
\tag{11}
\]

This is a locally finite sum. Indeed near any v there are constants
0<A<B with A<m(w)<B. For j>=0, m(D^j w)>=2^j A, and for j=-n<=0,
m(D^(-n)w)<=2^(-n)B. Only a bounded finite range of integers can
therefore enter the closed mass interval [3/4,5/4], uniformly on
that neighborhood. Moreover at most one summand is nonzero at any
point: two masses in (3/4,5/4) have ratio less than 5/3, whereas
nontrivial deck iterates have mass ratio at least 2 in the increasing
direction. Thus (11) is continuous and bounded by 1/4.

Reindexing its locally finite sum gives f_tilde(Dv)=f_tilde(v), so
it descends to f in C_b(X_hat). Every singleton state makes all
summands zero. At v=(q_2+q_3)/2 only the j=0 term is nonzero and
f([v])=1/4. Hence f is genuinely nonzero on the open mixed locus.
Theorem 3 makes f zero mu-almost everywhere for every permitted mu,
which proves the claim. QED.

For any Borel f with finite L2 norm the classification gives the
exact norm formula

\[
\|f\|_{L^2(\mu)}^2=
\sum_a w_a\frac1{L_a}\int_0^{L_a}
 |f([e^s q_a])|^2\,ds.
\tag{12}
\]

The actual time pullbacks f->f composed with phi_t are unitary on
this L2 space, because mu is invariant and phi_(-t) is their inverse.
This elementary measure representation exists, but (10)--(11) show
exactly why it is not faithful to all continuous full-state scalar
observations. No generator, spectral type or determinant is asserted.

Zero measure is not nonexistence. The mixed locus is nonempty, open
and full of the finite and infinite states retained in (1)--(2).
All their actual flow trajectories remain present, and the continuous
function just constructed distinguishes some of them from every
singleton state. Replacing X_hat by Gamma would change the frozen
owner and is not done here.

## 5. Controls and limitations

**Finiteness is essential.** Choose any actual mixed state x_0, for
example [(q_2+q_3)/2], and let i(t)=phi_t x_0. The 194 return equation
makes i injective. Push Lebesgue measure on R forward by this
continuous orbit map to a Borel measure nu on X_hat. The identity
i(t+s)=phi_s i(t) proves invariance directly. Its total mass is
infinite, and it assigns zero mass to Gamma.

This example is even sigma-finite: each i([-n,n]) is compact, hence
closed in the Hausdorff quotient, and has nu measure 2n by injectivity.
Their union is the orbit, a Borel set; its complement has zero nu
measure. These countably many finite-measure sets cover X_hat after
adjoining that complement. This changed measure class does not
contradict the finite-measure theorem and is not installed as a new
preferred Hilbert owner.

**Mixtures are not suppressed.** Every nonnegative countable weight
family summing to one occurs. The proof identifies no canonical
choice of w_a and does not assert ergodicity of a nontrivial mixture.
The zero-mass conclusion applies to all mixed supports at once, not
only finite supports or a numerically sampled collection.

**Arithmetic specificity / PROVES_TOO_MUCH control.** The strip
argument works for any countable diagonal cone quotient with distinct
multipliers lambda_a>1 and the same radial action, whenever that
whole quotient is a well-defined flow. Replace log a in (5) by
log lambda_a. Only distinctness, countability and finite invariant
measure enter the measure exclusion; primality is not what makes it
work. If two multipliers are equal, a positive ray supported on
those two coordinates instead gives a periodic circle carrying a
finite invariant time measure. Thus distinctness is a real hypothesis,
not a universal law for arbitrary cone flows. The generic control
does not replace the frozen arithmetic owner.

**Observation-class boundary.** Noninjectivity of (3) is not a
no-go theorem for all fixed Hilbert representations. In particular
it does not address weighted nonunitary orbit-feature spaces,
non-invariant reference measures or kernels outside this contract.
It also does not transfer the distinct weighted-return determinant
of 201 to this L2 time action. No zero matching, trace formula,
quantization or formal Route evaluation is undertaken.

## 6. Decision and claim/evidence boundary

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Every mixed pair set has zero finite invariant measure | Lemmas 1--2: actual time coordinate and disjoint Borel strips | Countably additive finite nonnegative measures |
| All invariant probabilities are exactly the mixtures (9) | Equation (8), Theorem 3 and the elementary circle argument | Arbitrary weights; no canonical measure |
| All finite invariant L2 observation maps lose continuous full-state data | Proposition 4 and norm formula (12) | Natural C_b-to-L2 map, not every possible Hilbert model |
| Infinite invariant mass can live on mixed states | Explicit pushforward orbit measure in Section 5 | Outside the finite-measure hypothesis |
| Natural arithmetic source or physical scale selected | Not established by a generic diagonal measure argument | OPEN |
| Symplectic/contact/Hamiltonian or quantum owner | Not constructed | NOT APPLICABLE / NOT SUPPLIED |
| Formal Route / Route B | Not evaluated | UNASSIGNED / NOT INVOKED |

Decision: ADVANCE the exact classification result, and STOP the claim
that an invariant probability's ordinary L2 scalar observation is
faithful to the whole completed topology. The same-object ledger is
intact: neither mixed states nor the clock changed. This bounded lane
ends at that classification and observation obstruction. Other
representation contracts require their own cards and cannot receive
an imported trace or arithmetic-naturalness conclusion from this one.

## Evidence and reproducibility

The [card](candidate-card.md), [claim ledger](claim-ledger.md) and
[evidence index](evidence/README.md) give identity, scope and process
provenance. Exact algebra, countable measure arguments and locally
finite continuous functions prove every new claim. There is no
numerical experiment, support cutoff, precision parameter, external
theorem dependency or unverified literature/novelty claim. The prior
work guide supplies lineage only. ARS contributes bounded CER and
counterargument discipline; it is not used as a full publication
pipeline. A separate model review is nonblind and is not human peer
review or a correctness certificate.
