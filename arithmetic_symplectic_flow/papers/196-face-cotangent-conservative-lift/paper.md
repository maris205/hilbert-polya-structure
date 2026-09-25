# A full conservative face-cotangent lift with unchanged prime-circle time

**Paper ID:** 196-face-cotangent-conservative-lift  
**Candidate ID:** ASC-20260916-FCL01  
**Research date:** 2026-09-16  
**Status:** ADVANCE — COMPLETE SYMPLECTIC COPRODUCT WITH FULL LOG-PRIME PACKETS; NEW TOPOLOGY; NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Abstract

We lift every open finite-support face of the full indecomposable radial
section to its entire cotangent bundle, multiply by one uniform real
hyperbolic plane, and retain the disjoint coproduct of all such components.
The full cotangent map is symplectic on each component. Its endpoint
suspension uses the original radial first-return roof and is complete.
The entire periodic ledger consists of one primitive oriented orbit per
prime, with actual time log p and all repeats; every mixed support and
every noncentral singleton transverse state is retained and aperiodic.
The transverse return multipliers are 2 and 1/2. A continuous surjective
time-preserving projection reaches the entire original cone flow. It is
not a quotient map or conjugacy: the new disjoint-face topology removes
the original cross-face convergence, and component dimensions vary.
This is an arithmetic symplectic coproduct, not a fixed-dimensional ASFS
manifold, a supplied lamination, a Hamiltonian flow or an analytic owner.
The geometry does not settle the disclosed source-clock naturalness gap.

## 1. Identity, lineage and bounded question

The [version-1 card](candidate-card.md) froze this owner before proof.
It is the geometry lane of [198](../198-cone-extension-frontier/candidate-card.md),
not a revision of [193](../193-indecomposable-radial-quotient/paper.md).
The exact question is whether a whole positive-dimensional conservative
extension can retain that full source, genuine return time, primitive
multiplicity and repetition law without choosing a periodic subcarrier.

The lineage is proper-factor symbolic admissibility -> the indecomposable
observable of integer multiplication -> the full positive radial quotient
and derived return -> an explicit face-cotangent geometric lift. This
implements a particular conservative extension of the
[prior-work source](../../docs/prior_work/README.md); it does not assert
a Logistic or Henon conjugacy, physical trial division or a unique
natural realization. No external prime or zero data are used.

| Item | This frozen owner | Boundary |
| --- | --- | --- |
| Arithmetic source | All-integer multiplication and its declared indecomposable quotient | Atoms are derived, not loaded from a prime list |
| Base | Every full T*Delta_J^o times R^2 in the disjoint coproduct M | Different dimensions and a new topology |
| Two-form | Canonical cotangent form plus dQ wedge dP on every component | No single fixed-dimensional global manifold claim |
| Base map G | Full cotangent lift of the original return F, times (2Q,P/2) | No deleted momentum or transverse state |
| Roof and flow | rho=tau composed with h; entire endpoint suspension Y | No time rescaling or unit-roof substitution |
| Arithmetic/geometric relation | Continuous onto h and time-preserving onto Pi to the whole 193 flow | Neither map is a quotient identification |
| Packets | Every primitive oriented closed orbit of Y, with all repetitions | Projection alone does not make a lifted trajectory periodic |
| Analytic/later owner | NOT SUPPLIED | No operator, determinant, trace, contact, Hamiltonian or quantum result |

## 2. Source and entire face geometry

Let the monoid algebra have basis e_n, n>=1, with e_m e_n=e_(mn).
The ideal I of nonunits has I^2 equal to the coordinate span of all
composite e_n: every product of two nonunits is composite and every
composite has such a product. Thus the declared quotient Q=I/I^2 has
exactly the surviving classes q_p for prime p. Denote this derived atom
set by A. The multiplier of atom a is its original integer a; no second
per-atom assignment is made.

As in 193, S consists of all finite positive coefficient vectors of
total mass one, allowing zero coefficients outside their nonempty support.
Its topology is inherited from the full family of weighted norms
||v||_k=sum_a a^k |v_a|, k>=0. Its genuine radial first return is

\[
c(u)=\sum_a\frac{u_a}{a},\qquad
F(u)=\frac{D^{-1}u}{c(u)},\qquad
\tau(u)=-\log c(u)\ge\log2.
\tag{1}
\]

Here D q_a=a q_a. Section 4 of the 193 proof derives (1) from its
whole radial quotient; this paper retains those data and constructs a
new owner above them. It does not take a period formula as a new input.

For each nonempty finite J subset A, let Delta_J^o be the whole strict
positive unit simplex on J. Freeze

\[
M=\coprod_J M_J,\qquad
M_J=T^*\Delta_J^o\times\mathbb R^2,
\qquad \omega_J=-d\theta_J+dQ\wedge dP.
\tag{2}
\]

Each M_J has dimension 2|J|. The topology is the disjoint coproduct,
so every component is open and closed. It is Hausdorff, and the
countably many finite supports give a countable collection of ordinary
smooth symplectic components. No boundaries of different faces are
glued. The full range of covectors and real Q,P belongs to (2).

**Proposition 1 (global component maps and symplecticity).** The frozen
map G=C_(F restricted to Delta_J^o) times B, B(Q,P)=(2Q,P/2),
is a smooth symplectomorphism on every entire component. It and its
inverse are continuous on the full coproduct. In particular no finite
iterate needs a completion, a momentum cutoff or a deleted state.

**Proof.** Write J={a_0,...,a_(m-1)}. For m>1 use global coordinates

\[
y_i=\log(u_{a_i}/u_{a_0}),\quad 1\le i<m.
\tag{3}
\]

Their inverse is u_(a_0)=1/(1+sum_i exp y_i) and
u_(a_i)=exp(y_i)/(1+sum_j exp y_j). This identifies the entire strict
simplex with R^(m-1), not only a local neighborhood. In these coordinates
f_J=F restricted to the face is the translation

\[
y\longmapsto y+v_J,\qquad
(v_J)_i=\log(a_0/a_i).
\tag{4}
\]

The common normalization c(u) cancels in each ratio. Formula (4)
provides a smooth global inverse, equivalently u->Du/sum_a a u_a.
For cotangent coordinates eta with theta_J=sum_i eta_i dy_i,
the full lift becomes (y,eta)->(y+v_J,eta). Indeed its covector rule
is xi->xi composed with (D f_J)^(-1), and D f_J is the identity in
these global coordinates. For m=1 both y and eta are absent.

Thus, for every component and all its states,

\[
G(y,\eta,Q,P)=(y+v_J,\eta,2Q,P/2),\qquad
\omega_J=\sum_i dy_i\wedge d\eta_i+dQ\wedge dP.
\tag{5}
\]

The inverse is (y-v_J,eta,Q/2,2P). Formula (5) directly preserves
the displayed closed nondegenerate form, including the singleton case
omega=dQ wedge dP. Equivalently the cotangent factor preserves theta_J
itself. Since every component is invariant and open, these maps and
their inverses are continuous on the coproduct. The componentwise
Liouville volume is preserved; its coproduct sum is not a finite-volume
or probability normalization. QED.

## 3. Projection and the topology that has actually changed

Define h:M->S by h(u,xi,Q,P)=u. On each fixed finite J the weighted
norm topology restricted to that face agrees with its ordinary finite-
dimensional topology: each norm is a finite weighted sum, and the
zero-th norm already gives its usual topology. The component projection
is continuous. The universal property of the disjoint coproduct therefore
makes h continuous on all M. It is onto, since any u has a finite
support and the lift (u,0,0,0) belongs to that support component.
The definition gives

\[
hG=Fh,\qquad \rho=\tau h.
\tag{6}
\]

This does not preserve the old topology as an identification. For
k>=2, u_k=(1-1/k)q_2+(1/k)q_3 converges to q_2 in every old norm,
because ||u_k-q_2||_ell=(2^ell+3^ell)/k. Its zero-covector lifts
in M_{2,3} cannot converge to a point of the disjoint open M_{2}.
More decisively h^(-1)({q_2})=M_{2} is open, while {q_2} is not
open in S. Hence h is not even a quotient map. This is a deliberately
new conservative coproduct above 193, not a symplectic structure on
193's original section or a claimed lamination through face boundaries.

## 4. The full endpoint suspension is complete and owns the clock

Let the full time cover be M times R and define the deck map

\[
H(z,t)=(Gz,t-\rho(z)).
\tag{7}
\]

It is a homeomorphism, smooth on each component. For u=h(z), define
for every integer r

\[
c_r(u)=\sum_{a\in\operatorname{supp}u}u_a a^{-r},\qquad
T_r(u)=-\log c_r(u).
\tag{8}
\]

All sums are finite and positive, and c_0=1. Iteration of (1) gives
F^r u=D^(-r)u/c_r(u), including negative r. Moreover
c(F^r u)=c_(r+1)(u)/c_r(u). Therefore

\[
H^r(z,t)=(G^rz,t-T_r(u)),\qquad
T_{r+1}(u)-T_r(u)=\rho(G^rz)\ge\log2.
\tag{9}
\]

In particular T_r>=r log2 for positive r and T_r<=r log2 for
negative r. Both directions diverge; the potentially unbounded covectors
do not enter the roof.

**Proposition 2 (complete whole-owner suspension).** The time-cover
quotient by H is Hausdorff and agrees with the full endpoint suspension

\[
Y=\{(z,t):0\le t\le\rho(z)\}/
((z,\rho(z))\sim(Gz,0)).
\tag{10}
\]

Translation induces a jointly continuous complete flow psi on all Y,
smooth on each suspended component. Its embedded global section is M,
with actual first return G and elapsed time rho.

**Proof.** By (9) every nonzero deck iterate changes the real coordinate
by at least |r| log2 in absolute value. Thus every horizontal open strip
of width less than log2 is disjoint from each of its nontrivial deck
translates. The quotient map is open, since saturation is a union of
homeomorphic translates; its restriction to such a strip is a chart
homeomorphism onto an open image. For two inequivalent cover points,
choose bounded real-coordinate neighborhoods. Only finitely many deck
translates of one can meet the other. The Hausdorff cover and continuity
of those finitely many maps allow the neighborhoods to be shrunk so
none meet. Their saturations separate the two quotient points. This
proves Hausdorffness without a compactness assumption on M.

The times T_r(z) are strictly increasing and tend to both infinities.
Every cover point has a unique half-open representative obtained by
the integer r for which T_r(u)<=t<T_(r+1)(u); applying H^r gives
0<=t-T_r(u)<rho(G^rz). Endpoints have exactly the identifications
in (10). This representative description also has the required quotient
topology: away from an endpoint it is a cover chart, and around a seam
the negative and positive pieces of a short horizontal chart glue by
the homeomorphism (7). Both the endpoint model and time-cover quotient
use these same charts, so their natural bijection is a homeomorphism.

Translation (z,t)->(z,t+s) commutes with H, exists for every real s
and descends. Since the cover quotient is open, its product with R is
an open quotient map; this proves joint continuity of the descended
action. The strip charts and smooth (7) give its smooth componentwise
form. Completeness is an everywhere-defined action, not an assertion
that the finite-support source space is metrically complete.

The same strip chart embeds M at t=0. A positive return from [z,0]
to this section occurs exactly at t=T_r(hz) with r>=1. Equation (9)
shows that the first is r=1, with point Gz and time rho(z). There
is no forward or backward finite-time accumulation of crossings. QED.

Every suspended component has odd dimension 2|J|+1. The proof has not
given it a symplectic form, contact form or Hamiltonian realization.

Let X be the complete original flow space of 193. There is a continuous
surjective map of entire flows

\[
\Pi:Y\longrightarrow X,\qquad
\Pi([z,t])=[e^t h(z)],\qquad
\Pi\psi^s=\varphi^s\Pi.
\tag{11}
\]

Indeed (6) and exp(-rho)=c imply
exp(t-rho(z))h(Gz)=D^(-1)exp(t)h(z); the two vectors represent the
same point of X. The continuous cover map therefore descends. Any
v in the full old positive cone can be written v=exp(t)u with u
in S; choosing a zero-covector lift proves surjectivity. Equation (11)
then follows from the same actual translation, with no time change.

The map is not a conjugacy or quotient map. The inverse image of the
old prime circle gamma_2 is precisely the whole open suspended singleton
component Y_{2}. Yet gamma_2 is not open in X: the old points [u_k]
above lie outside it and converge to [q_2]. In particular this complete
factor relation must not be described as retaining the old topology.

## 5. Every periodic state, primitive orbit and transverse multiplier

**Theorem 3 (complete intrinsic packet ledger).** The entire Y has
exactly one primitive oriented closed orbit gamma_a^lift per atom a,
hence per prime p. Its least positive period is log p, with all and
only positive repeats r log p. All mixed-support states and all
noncentral singleton transverse states are aperiodic. The Poincare
monodromy is diag(2,1/2), and for the r-th repetition diag(2^r,2^(-r)).

**Proof.** Formula (5) gives the full iterate, for any positive integer r,

\[
G^r(y,\eta,Q,P)=(y+rv_J,\eta,2^rQ,2^{-r}P).
\tag{12}
\]

If |J|>=2, every atom differs from a_0, so v_J is nonzero and
y+rv_J cannot equal y. No covector or transverse state can cancel
that base displacement. If |J|=1, there is no y or eta, and (12)
fixes a point if and only if Q=P=0. That point is already fixed
at r=1. Consequently the complete base periodic-point set is exactly
one point z_a over each singleton, with no higher primitive cycles.
This classification used all of M; the centers were not selected as
a new phase space or as an imposed section.

Every flow trajectory crosses M. A positive time t returning [z,0]
to itself must satisfy G^r z=z and t=T_r(hz) for one r>=1 by
the deck equation (9). Conversely those equalities give a return.
Thus the above exhaustive base classification is also exhaustive for
Y. At z_a the unmodified expression (1) has c(q_a)=1/a, so
rho(z_a)=log a. Each fixed base point suspends to one circle, whose
time stabilizer is exactly (log a)Z. Its entire t coordinate is one
oriented trajectory, not separately counted phases or amplitudes.
Different components never identify, giving multiplicity one per atom.
The source calculation in Section 2 identifies these atoms with primes.
No trajectory is fixed for all time, because every positive return is
at least log2.

On the singleton component the first-return map on the whole transverse
plane is exactly B. Its derivative at the fixed point is diag(2,1/2);
the r-fold return is B^r. Neither multiplier is 1 for any positive r,
so these are isolated nondegenerate hyperbolic return points within
their actual components. The full flow derivative has additionally its
usual neutral time direction; no omitted face-boundary directions exist
in this coproduct topology. QED.

Equation (11) gives a bijection of the two primitive closed-orbit ledgers
and preserves each repeat time. It does not assert a bijection of all
trajectories: for example every noncentral singleton lifted trajectory
is aperiodic but projects to the old closed prime circle. For the mixed
state u=(q_2+q_3)/2, the same first crossing gives F(u)=(3q_2+2q_3)/5
and time log(12/5), for every covector and Q,P over it. These retained
states provide a concrete non-axis ownership control, not a finite test
standing in for the all-support proof.

## 6. Controls, adverse findings and limits

| Control | Exact finding | Consequence |
| --- | --- | --- |
| All mixed supports and all covectors | Nonzero translation in (12) forbids every positive return | No periodic subcarrier was chosen to remove mixed packets |
| Full singleton transverse plane | Only Q=P=0 solves B^r(Q,P)=(Q,P) | The unique closed packet is intrinsic to the full positive-dimensional base |
| Replace B by identity | Every Q,P is periodic over a singleton, producing a continuous orbit family | This changed owner fails multiplicity; the frozen hyperbolic factor is a substantive design |
| Omit the plane | Singleton components have dimension zero | That changed construction does not provide the required positive-dimensional prime base |
| Old face-boundary convergence | The sequence in Section 3 converges in S but not to a singleton component in M | h and Pi are continuous onto, not quotient maps or conjugacies |
| Replace rho by a unit roof | Every prime fixed base point would have actual period one | Clock credit belongs only to the frozen pulled-back radial roof |
| Omit I/I^2 | Composite axes such as 4 and 6 also give distinct primitive packets | Indecomposable source design is responsible for prime selectivity |
| Use a free commutative source with distinct generator multipliers lambda_a>=2 | The same coordinate argument gives one packet of period log lambda_a per generator | PROVES_TOO_MUCH; conservative realization does not force arithmetic naturalness |

In the last control the whole source/radial construction and topology
are changed accordingly; it is not a modification of this card. Equal
generator multipliers would make some v_J vanish and allow mixed
periodicity, so distinctness is an explicit hypothesis. The constant
transverse multiplier 2 is universal and not tuned prime by prime,
but it is still an engineering choice. No arithmetic stability-weight
law follows from the computed monodromy.

The proof covers every finite support with no size cutoff, every
covector, every transverse state and every integer return. It is an
exact argument, not an extrapolation from finitely many trajectories.
It says nothing about an infinite-support completion, restoration of
cross-face topology, a fixed-dimensional carrier or perturbation
stability of the entire arithmetic construction.

## 7. Scoped gate assessment and decision

| Obligation | Result for ASC-20260916-FCL01 | Remaining boundary |
| --- | --- | --- |
| T0 carrier/type/ownership | ESTABLISHED: complete componentwise symplectic coproduct and actual endpoint flow | New topology and varying dimension, not classical fixed-dimensional ASFS |
| T1-style source/clock | ESTABLISHED as a declared extension of the derived all-integer source and actual roof | Source-clock naturalness OPEN |
| T2 all packets and repeats | ESTABLISHED: one log-prime primitive circle, all repeats and full monodromy | Includes all states; not a prime-axis or center restriction |
| Old full-flow relation | ESTABLISHED: continuous onto time-preserving Pi | Not quotient, injective, topological or symplectic conjugacy |
| T3 analytic owner | NOT INVOKED / NOT SUPPLIED | No transfer, determinant, trace or function-space result |
| Classical A0--A2 and formal Route | No classical fixed-dimensional contract evaluated; formal coordinates UNASSIGNED | No natural-A0 pass or Route-A readiness |
| Route B / later geometry | NOT INVOKED / NOT SUPPLIED | No Hamiltonian, contact, Hilbert or quantum inference |

Decision: ADVANCE the bounded conservative-coproduct construction. It
genuinely supplies positive-dimensional symplectic bases and the full
intrinsic prime-clock ledger under a precisely disclosed new topology.
Stop this contract here: replacing that topology, unifying dimensions,
adding an infinite-support completion, or attaching an analytic/later
owner needs a fresh card and full-state audit. No result of another
Round-19 lane is silently attached to this owner, and 193 is unchanged.

## Evidence and reproducibility

The [card](candidate-card.md) precedes the proof. The
[claim ledger](claim-ledger.md) separates exact results from OPEN and
NOT SUPPLIED obligations. The [evidence index](evidence/README.md)
records read-only source inputs, author method and actual review state.
No script, numeric tolerance, prime table, zero sample or computational
experiment supplies these global conclusions. All new results are
derived above; 193 is a local mathematical dependency explicitly
identified at (1) and (11), not a transferred Route or review verdict.
ARS is used only for bounded claim/evidence/reasoning and adverse
scope checks. Review is a separate actual model invocation with shared
context and nonblind feedback, not human peer review or an independent-
error certificate. No external publication or venue-fit claim is made.
