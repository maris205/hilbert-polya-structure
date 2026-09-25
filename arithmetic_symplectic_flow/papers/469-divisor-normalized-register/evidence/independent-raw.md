# DNR01 — frozen card-only independent derivation

Candidate: `ANG-20260925-DNR01`, paper469, version1.
Batch: `ADMISSION-CORE-20260925-X`, round5/5; date label2026-09-25.
Reviewer: `pcr01_independent_review`; root independently authors the paper.

## 0. Input, scope, and independence boundary

This derivation follows the DISTINCT RAW release after root FULL-read of
the189-line CP1 report. The only current scientific input is the unchanged
[candidate card](../candidate-card.md),112 lines, FULL-read through EOF,
SHA256 `9a5be30d0004ea428c781446ce4ed94b4a553e37f496c2e2cadf86066afbbb72`.
The allowed [CP1 report](scope-review.md) has SHA256
`881afe23c9be541fb7c79c25bb72dbdc6e39acd297feb2f630d39bc0781e66c2`.
Both hashes were rechecked immediately before writing this record.

No current author paper, README, ledger, Outcome, helper, peer proof, other
current candidate card, or old proof was read. Instructions and inherited
exposure are recorded in CP1. This is shared-history/same-model procedural
separation, `NOT_CALIBRATED`, not blind, human, cross-model, or external
peer review. No scientific code, numerical experiment, search, network,
Git operation, PDF, or change to an older artifact was used.

All arguments below are exact. The full history description is unrestricted
recursion, with proofs of completeness and exact equivalence tests, as the
card permits. The short gate classifies fixed states globally. It does not
search MAIN's higher periods, adjust the candidate, or infer an arithmetic
conclusion from absence of fixed points. This file must freeze before root
raw access and the distinct later PAPER UNLOCK.

## 1. Four owners and their actual regularity

Write X=R³, v=(x,y,z), mu=ordinary Lebesgue³, and define

    d(v)=1+floor|x+y|,     n(v)=1+floor|x+y+z|,
    A(v)=1+y²+z²,         E={v:d(v) divides n(v)}.

Both d and n are positive integer-valued Borel functions. No coordinate,
face, or null stratum is removed from X. Let F_q(v)=(y,z,(x+q)/A(v))
for every integer q≥1, and F_q^R(v)=(y,z,x+q).

For fixed q, the first two derivative rows of F_q are (0,1,0),(0,0,1).
The last row is

    (1/A, -2y(x+q)/A², -2z(x+q)/A²).

Expansion in the first column gives det DF_q=1/A>0 at EVERY v.
Similarly det DF_q^R=1. Thus every frozen regularity guard is satisfied;
this conclusion was computed in the actual three-dimensional germ, not
borrowed from a scalar coordinate or a prior owner. The actual maps are

    M:E→X,       M(v)=F_(n(v)/d(v))(v),
    O:X→X,       O(v)=F_(max(1,floor(n(v)/d(v))))(v),
    Q:E→X,       Q(v)=F_1(v),
    R:E→X,       R(v)=F^R_(n(v)/d(v))(v).

M/Q/R leave X\E as terminal objects, with units and actual incoming.
O has no terminal forward objects because it is total. No terminal object
is given an absorbing self-loop. These are four separate owners on the
same measured carrier, not four formula choices for MAIN after the gate.

For the entire proper-divisor interface, let integers 1<d<N with d|N and
v=(d−1,0,N−d). Direct substitution gives d(v)=d and n(v)=N, hence M/Q/R
are legal there. The normalized germ determinant is 1/(1+(N−d)²)>0;
R's determinant is1. No interface point is lost to the regularity guard.
The quotient acts in the transport, and all coordinates subsequently shift;
there is no passive integer tag retained as an extra state coordinate.

## 2. Complete inverse atlases, including all boundaries

For target u=(a,b,c) put B=1+a²+b². For M/O define for EVERY q≥1

    theta_q(u)=(cB−q,a,b).

For R define theta_q^R(u)=(c−q,a,b). For Q there is only theta_1(u).
In each definition reconstruct d_q=d(theta_q(u)), n_q=n(theta_q(u));
use the R candidate instead when treating R. The exact inverse domains are

    Y_q^M = {u:n_q=q d_q},
    Y_1^O = {u:n_1<2d_1},
    Y_q^O = {u:q d_q≤n_q<(q+1)d_q}, q≥2,
    Y^Q   = {u:d(theta_1(u)) divides n(theta_1(u))},
    Y_q^R = {u:n_q=q d_q} using theta_q^R.

All candidates on these domains satisfy the appropriate forward equality;
the previously computed guard imposes no further exclusion. All these sets
are Borel, with inequalities and floor-face assignments interpreted exactly.
The special q=1 rule for O includes n<d: max(1,floor(n/d)) is still1.
Q's tested arithmetic quotient can exceed1 but is not its transport label.
No extra inverse copy may be attached to that unused quotient.

Each fixed-label F_q is a global smooth diffeomorphism of R³ with inverse
theta_q; F_q^R likewise has inverse theta_q^R. Restricting to the stated
label/source sets yields countable Borel injective source pieces and actual
Borel inverse images. Source pieces are disjoint because each owner's
actual label is single-valued. Q can use its one injective source piece E.

Completeness is direct: if U(x,y,z)=(a,b,c), the first two coordinates force
y=a,z=b, and the last determines x=cB−q, or x=c−q for R. Its actual label
must pass exactly the stated reconstructed predicate. Conversely any passing
candidate maps to the target. Distinct q give distinct x, so no one-step
source is counted twice. The target itself need not belong to E, and no
next-step predicate at the target is included. This proves the complete
atlas on full X, not merely on a recurrent or legal-forward target subset.

## 3. Every-Borel IMAGE and the fixed all-point clocks

The derivative matrix of theta_q is

    (2ac, 2bc, B)
    (1,   0,   0)
    (0,   1,   0),

so det Dtheta_q=B>0, independent of q. For theta_q^R the determinant is1.
These are the frozen all-point germ versions, including assigned floor
faces, special points, and null periodic points; no a.e. replacement occurs.

The ordinary smooth change-of-variables theorem for the global germ gives,
for every Borel C contained in an actual inverse domain,

    mu(theta_q(C)) = integral_C (1+a²+b²) dmu(a,b,c),
    mu(theta_q^R(C)) = integral_C 1 dmu.

The restricted domains may be nonopen; the theorem applies to every Borel
subset of the global diffeomorphism domain, so that causes no loss. Borel
images follow from the global homeomorphisms as well. Densities are positive
and finite everywhere, and equalities allow infinite integrals. This proves
IMAGE for each actual branch separately, without summing branch densities.

At a normalized legal source v, Uv has first two coordinates y,z. Therefore

    kappa_M(v)=kappa_O(v)=kappa_Q(v)=−log A(v),
    kappa_R(v)=0,

on each owner's OWN domain. Normalized clocks are nonpositive, not an
inserted positive roof. They vanish exactly when y=z=0; R's clock vanishes
everywhere on its domain. No sign is discarded and no illegal outgoing
source is assigned kappa. The forward arrow has clock −kappa as frozen.

## 4. Every finite and infinite history, without a cutoff

For an owner U, let I_U(u) be the set of all passing sources in section2.
Define inverse levels by

    I_U^0(u)={u},
    I_U^(m+1)(u)=union_(w in I_U^m(u)) I_U(w),  m≥0.

These are sets of actual sources, not multisets of labels. Induction proves

    v in I_U^m(u) iff v has m legal U steps and U^m v=u.

The induction step uses the complete one-step atlas in both directions.
Thus every depth is covered, even when levels are empty, finite, or
countably infinite. Coinciding sources at different depths do not remove
their different retained lags. No bound on q or m has been imposed.

All compatible infinite backward histories at u are EXACTLY the sequences

    u_0=u, u_(-1),u_(-2),... with u_(-j) in I_U(u_(-(j−1))) for j≥1.

Equivalently they are the compatible inverse limit of these finite-history
trees with the actual predecessor maps. An infinite history is not inferred
merely from arbitrary nonempty levels. This formula retains all choices and
does not assert existence when compatibility fails. Forward histories are
unique until the first illegal source; O's continue forever. A backward
history ending at an illegal object is valid, but cannot be continued through
an outgoing step there. Two-sided histories require both compatibility and
an infinite legal forward history at the selected time0 object.

Let D_0^U=X and D_(m+1)^U={v in Dom U:Uv in D_m^U}. These Borel sets
give every legal forward depth. For normalized owners put

    P_0(v)=1,
    P_m(v)=product_(j=0 to m−1) A(U^j v),  v in D_m^U.

For R put P_m(v)=1 at every legal depth. Then S_m(v)=−log P_m(v) in all
four owners. A fixed length-m label itinerary is a restriction of a global
smooth diffeomorphism; its inverse determinant at U^m v is P_m(v).
This follows by the chain rule, multiplying the actual one-step inverses.
Countably many finite label words cover all histories, with no extra label
at a Q step. Thus the recursion carries complete clocks as well as sources.

## 5. Retained-lag groupoid, clock descent, and pair IMAGE

Use exactly the card's triples (v,r−s,w) with v in D_r, w in D_s and
U^r v=U^s w, identified only when the endpoints and integer lag agree.
The source is w, the range is v. Every object has its lag0 unit, including
illegal ones. Inverse swaps endpoints and negates lag.

If two witnesses have the same lag, their depths differ by a common
integer shift. Order them so the shift is nonnegative. The longer witness
adds the same legal tail from the first meeting point to both clock sums.
The added terms cancel. Hence

    c(v,r−s,w)=S_r(v)−S_s(w)
              =log(P_s(w)/P_r(v))

is well-defined. To compose witnesses (r,s) and (p,q) through a middle
object, extend their middle depths to L=max(s,p). Legality of that extension
is furnished by the longer existing middle history, and the other endpoint
paths extend along the same tails. The resulting lag is r−s+p−q and the
middle clock sums cancel. This proves additivity, with inverse clock −c.
The forward witness (0,1) gives (Uv,−1,v), clock −kappa(v).

For history-pair IMAGE, fix finite itineraries from w and v to a common
meeting target. The branch transport w→v is the v inverse itinerary
composed with the w forward itinerary, restricted to the actual pair-domain.
Its all-point absolute determinant is

    P_r(v)/P_s(w)=exp(−c(v,r−s,w)).

The global fixed-itinerary germ is a diffeomorphism; restricting its ordinary
change-of-variables identity proves this IMAGE for every Borel subset of
the actual pair-domain. Floor boundaries remain included. Coincident triple
witnesses give the same all-point value by descent, rather than an extra
weight or multiplicity. This is the required compatibility between the
history action and its original-measure clock, not a borrowed density.

The exact three kernels for EACH owner are

    K_lag   = {(v,0,w):some legal equal-depth meeting exists},
    K_clock = {(v,r−s,w):some legal meeting with P_r(v)=P_s(w)},
    K_joint = {(v,0,w):some equal-depth meeting with P_r(v)=P_r(w)}.

Each formula ranges over ALL nonnegative legal depths, with duplicate
triples identified. It is not a finite search. An equivalent test using
any other witness of the same triple gives the same answer. In particular,
equal endpoint heights in the extension do not imply zero lag.

The exact full-object phase/orbit test is

    (v,h_v) ~ (w,h_w)
    iff there exist legal r,s with U^r v=U^s w and
         h_v−h_w=log(P_s(w)/P_r(v)).

The same meeting test without the height equation is the complete source
packet test. Together with section4 this supplies all incoming and all
phase equivalences, without selecting ancestors or a measurable section.

## 6. Entire isotropy, H, phases, and primitive convention

For any partial deterministic U, nonzero source lag isotropy at v occurs
iff its forward history eventually reaches a legal finite cycle. Indeed a
meeting U^r v=U^s v with r>s repeats the state at depth s; conversely an
eventually reached cycle gives such meetings. If that cycle has least length
ell, all source isotropy lags are exactly ell Z. They are not merely a
subgroup generated by an arbitrarily selected return.

Write C for the sum of kappa over that least cycle. The same common-tail
argument gives c(v,t ell,v)=t C, so the ENTIRE image is H_v=CZ. Thus
extension isotropy is ell Z if C=0, and {0} if C≠0. When there is no eventual
cycle, source and extension isotropy and H_v are all zero. This includes
terminal objects and forward-infinite non-eventually-periodic histories.

For normalized M/O/Q, every actual cycle has C<0. Each summand is ≤0. If
their sum were0, every cycle state would have y=z=0. Since each state is
also the successor of another cycle state, every x would be0 as well.
But the actual image of0 is (0,0,1), not0. This contradiction excludes
zero-clock source isotropy, while preserving zero-clock arrows BETWEEN
different objects. Consequently normalized extension isotropy is always
trivial; an eventually periodic packet has H=CZ with least positive
generator −C, and all its positive repetitions n(−C), n≥1.

This conditional all-period structural statement does not classify or
search any higher MAIN period. It identifies the entire H whenever an
eventual cycle is present; the exact iterate/history tests decide membership.
No rational multiplier or integer Jacobian is assumed.

For R, kappa and c are identically0, so K_clock=G_R and
K_joint=K_lag. Moreover the coordinate sum increases by the positive actual
integer q at EVERY legal step. Two different legal depths from one source
cannot coincide. Hence all R source and extension isotropy and H are zero.
This is a direct full-object isotropy calculation, not a finite period scan.
The lag kernel still means all equal-depth mergers, not automatically units.
Every R source packet has real height as its phase, and no positive period.

For Q the transport F_1 is injective even before restriction, so every legal
iterate is injective. Therefore Q's lag and joint kernels are units. Its
clock kernel is still the full product-equality test above, not just units.
In fact for EVERY real x, the source (x,0,0) satisfies d=n and is legal for
M/O/Q, all with transport label1. Its image is (0,0,x+1), a different
object, and its clock is0. Thus all three normalized owners have genuine
nonzero-lag clock-zero arrows; these are not source isotropy.

Here are explicit packetwise coordinates completing the general test.
If a packet ends at a terminal e, let d_v be its arrival depth and
a_v=S_(d_v)(v). All arrows in that packet are

    (v,d_v−d_w,w),  c=a_v−a_w.

The kernel tests are equality of depths, equality of a-values, or both.
Source/extension isotropy and H vanish; the real phase is h−a_v. Every
incoming source of every depth and the endpoint e itself are included.

If a packet is forward-infinite but not eventually periodic, select a
reference object b within that packet solely for notation. There is a
unique lag k_v for an arrow b→v: two different lags would give nonzero
isotropy at b. Let a_v be its unique clock. Then all arrows have lag
k_v−k_w and clock a_v−a_w; the respective kernel tests are equality of
k-labels, a-labels, or both. Real phase is h−a_v. These are packetwise
coordinates, not a claimed global Borel selection.

If a packet eventually reaches a least-ell cycle, choose one core point p,
let d_v be the first arrival at p, and a_v=S_(d_v)(v). Choosing p does not
remove any core phase: every cycle point reaches p legally. The full packet
is union_(m≥0) I_U^m(p), and ALL arrows are

    (v,d_v−d_w+t ell,w), c=a_v−a_w+t C, t in Z.

Every integer t is realized by padding at the cycle. Conversely any
meeting can be continued to p, giving this formula. Its three kernel tests
are respectively d_v−d_w+t ell=0, a_v−a_w+t C=0, and both. Entire phase
is [h−a_v] in R/CZ (R if C=0). Its translation stabilizer is precisely H,
so the primitive/repetition conclusions use the ENTIRE subgroup, including
the degenerate case. Distinct source packets are never identified because
their clocks happen to agree. All real phases remain present.

These three cases exhaust deterministic partial-map packets: two sources
with a common future have the same terminal, eventual cycle, or nonperiodic
infinite tail type. The inverse recursion supplies all their histories,
including every compatible infinite backward history. This is an exact
classification/test schema, not a finite tree presented as an exhaustive
list of all cycles of the nonlinear owners.

## 7. Exhaustive global fixed-state classification

A fixed state of a normalized transport must have x=y=z=t. Its last
coordinate equation is

    t=(t+q)/(1+2t²), hence 2t³=q.

Because q≥1, t>0. Put alpha=2^(−1/3). If q≥2, then t≥1. At every t≥1,

    d(t,t,t)=1+floor(2t)>2t,
    n(t,t,t)=1+floor(3t)≤3t+1≤4t<2d(t,t,t).

For MAIN, an actual q≥2 would equal n/d≥2, contradicting this bound.
For O, an actual q≥2 would require floor(n/d)=q≥2, the same contradiction.
Thus the quotient bound is exhaustive, not numerical: q can only be1.
For Q its transport is already F_1. In all these remaining cases t=alpha.

The exact rational bounds (3/4)^3<1/2<1 prove 3/4<alpha<1. Hence

    1<2alpha<2,   2<3alpha<3,
    d(alpha,alpha,alpha)=2, n(alpha,alpha,alpha)=3.

The point p=(alpha,alpha,alpha) is illegal for M and Q. For O its actual
max/floor label is1, so it is legal and fixed. R has no fixed state because
fixedness forces x=y=z=t and its last equation t=t+q contradicts q≥1.
Thus the complete global ACTUAL fixed sets are

    Fix(M)=empty, Fix(O)={p}, Fix(Q)=empty, Fix(R)=empty.

This includes every sign, floor face, zero coordinate, illegal object, and
label: equality of the first two transport coordinates forced the diagonal,
and the remaining equations and exact label bound exhausted that diagonal.
The unit at an illegal point was not mistaken for a map fixed state.

## 8. The O fixed core and its ENTIRE incoming packet

Let A_*=1+2alpha² and L=log A_*>0. At p the original-measure clock is −L.
The rational bound alpha>3/4 gives A_*>17/8>2, while alpha<1 gives A_*<3.
There is no integer, hence no ordinary prime, strictly between2 and3.
Thus this core's primitive L is not log of an ordinary prime. No decimal
approximation, supplied prime table, or fitted clock was used.

Define the entire fixed-core basin

    B_p=union_(m≥0) I_O^m(p)={v:O^m v=p for some m≥0}.

The unrestricted inverse recursion of section4 is an exact description of
ALL its points, depths, label histories, and compatible infinite histories.
Here one can also identify the first level exactly. Since alpha A_*=alpha+1,
the q candidate at p is (alpha+1−q,alpha,alpha). For q=1 it is p and is
legal for O. For q=2 it is w=(alpha−1,alpha,alpha), with readouts d=1,n=2,
and actual O label2. For q=3 its readouts are d=n=1, so it is rejected.
For q≥4 the exact floors give d=q−2,n=q−3, again not O label q. Therefore

    I_O(p)={p,w},
    B_p={p} union union_(m≥0) I_O^m(w).

The displayed first level is not used as a cutoff. Every predecessor of w,
and every predecessor of those predecessors, is covered by the unrestricted
formula and its induction proof. An infinite history at p either stays at
p forever backward, or has a finite initial string of p's, then w, then an
arbitrary infinite compatible predecessor sequence at w if one exists.
The formulation neither drops such sequences nor assumes their existence.

For each v in B_p let d_v be its least arrival depth at p and
a_v=−log P_(d_v)(v). All its later legal arrival depths are d_v+j, j≥0,
with clock sums a_v−jL. In particular all incoming depths, including those
obtained by arbitrarily many fixed-core repeats, are retained. The ALL-arrow
formula specializes to

    (v,d_v−d_w+t,w), c=a_v−a_w−tL, t in Z.

It supplies every arrow between every pair of incoming objects, not only
returns at p. Source isotropy is Z at every object of B_p, clock image is
the ENTIRE LZ, and extension isotropy is trivial. Full phase is

    [h−a_v]=[h+log P_(d_v)(v)] in R/LZ.

Every phase is present; translations have stabilizer LZ and least positive
period L, with all repeats jL, j≥1. The whole B_p is ONE core packet, not
one new packet per ancestor, depth, label, or phase origin. The fixed-core
ledger therefore has exactly this one O packet, without a claim that O has
no other, higher-period packets.

For completeness the specialized kernels are exactly:

    lag:   t=d_w−d_v, one such arrow for EVERY ordered pair v,w;
    clock: a_v−a_w=tL for some t in Z, with that integer t;
    joint: a_v−d_v(−L)=a_w−d_w(−L), and lag0.

Equivalently the joint condition is
P_(d_v)(v)/A_*^(d_v)=P_(d_w)(w)/A_*^(d_w). These formulas include all
possible cancellations and zero values, without a genericity assumption.
Off B_p, the complete O atlases, packet tests, kernels, and entire-isotropy
classification remain those in sections2–6; no other packet is discarded.

## 9. Admission comparison and the other controls' full objects

The O fixed core has d=2,n=3 and is illegal for MAIN. Hence its adverse
primitive is NOT a MAIN witness. M has no fixed core at all, so its fixed
core ledger is empty. Nonetheless p is an object of M and may have genuine
incoming. In fact the same inverse calculation at p gives

    I_M(p)={w},  with w=(alpha−1,alpha,alpha), d(w)=1,n(w)=2.

The q=1 candidate p is now illegal; q=2 is legal; q=3 and every q≥4 fail
the exact equality n=qd. Thus w→p is a genuine MAIN step into a terminal
object. The entire terminal packet of p in M is

    {p} union union_(m≥0) I_M^m(w).

Its full arrows, all incoming clocks and depths, real phases, kernels, and
zero isotropy/H are the terminal formulas of section6, with M's OWN inverse
recursion. No O predecessor may be imported without retesting M permission.
In particular no O fixed loop or period at p survives this outgoing cut.

For Q the only possible inverse at p is theta_1(p)=p, which fails Q's
permission. Thus p is an isolated terminal unit for Q, not an O-like fixed
core or an artificially relabeled copy of w. Every other Q object and
incoming chain is still governed by its full injective theta_1 recursion,
original-measure clock, product-equality clock kernel, and full real-phase
or cyclic-phase test. Q's empty fixed set makes no higher-period assertion.

R's full inverse atlas uses theta_q^R and its own arithmetic tests. Its
IMAGE and clocks are identically unit/zero as proved, not inherited from
normalized transport. Its complete source packet relation is still the
unrestricted legal meeting relation, with all incoming retained. Sum growth
excludes all source isotropy, H=0, K_clock=G_R, K_joint=K_lag, and every
source packet yields all real-height extension classes with free physical
translation. A zero clock did not create any positive primitive or loop.

For normalized M/O/Q outside the explicitly displayed packets, sections4–6
give exact unrestricted histories, product equations for all kernels, the
entire H classification, and all phase tests. No recurrent-only reduction,
positive-coordinate restriction, or selected inverse label is used. In
particular zero-clock nonzero-lag arrows remain in these full objects.

## 10. Scoped gate outcome and nonclaims

Full original-measure ownership, inverse IMAGE at every point, retained-lag
clock descent, history-pair IMAGE, and complete history/phase tests have
been established for all four frozen maps. The global fixed gate is fully
resolved, not a finite sample: MAIN/Q/R have no fixed states, while O has
the unique core above with a nonprime primitive and its entire incoming
packet. Permission genuinely excludes that O core from MAIN; quotient
feedback and normalization controls retain their own distinct conclusions.

There is no MAIN-owned nonprime or duplicate fixed-core witness. The empty
MAIN fixed ledger also cannot satisfy or refute the full positive-ledger
target, because higher periods have not been classified. The frozen exit
is therefore BOUNDED OPEN/FORK, not arithmetic admission and not a transferred
O obstruction. MAIN higher periods, nonempty positive ledger, prime-only
primitives, packet uniqueness, and all-prime coverage remain OPEN. No new
period search, window, parameter, formula, or candidate is initiated here.

The lineage is the stated proper-divisor admission-to-geometric-feedback
deformation, not a proved classical geometric lift or intrinsic natural
prime source. PROVES_TOO_MUCH and strong naturalness remain OPEN. T0 and
the explicitly proved clock-ownership component have their local scope;
arithmetic T1 is NOT PASSED. T2 statements here are the proved structural
packet/isotropy/repetition laws and the bounded fixed-core audit, not global
arithmetic success. T3 is NOT AUDITED. Classical fields are NOT APPLICABLE,
formal Route coordinates UNASSIGNED, and Route B NOT INVOKED.

This raw record contains no author comparison or CP2/CP3 verdict. After
FULL self-read and immutable hash receipt, only RAW READY metadata will be
sent to the independently working author/root. Current author files remain
unread until the distinct later PAPER UNLOCK. No paper470 is authorized.
