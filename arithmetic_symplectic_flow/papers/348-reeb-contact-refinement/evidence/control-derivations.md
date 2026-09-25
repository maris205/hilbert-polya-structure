# RCF01 — complete derivations for the three frozen controls

Candidate ID: `ANG-20260921-RCF01`.
Control status: `OWN CONTROL LEDGERS PROVED; NO CONTROL PRIME-PACKET PASS`.
Date: 2026-09-21. This is a control-only evidence document, not a MAIN verdict.

## 1. Input, authority and review boundary

The sole scientific input is the complete 187-line
[frozen card](../candidate-card.md), SHA-256
`9fd564c3a42a09fb38463c860daa4cc451887015e3334485108b1537cba8622a`.
All assertions below are derived here from its definitions. No result from
344, MAIN's new manuscript, another review, or a source scout is invoked.
The controls are changed owners, not repairs or transferable credits.

The author read local AGENTS.md completely (221 lines), plan.md completely
(411 lines), and readme.md lines 1--30 for authority/recovery only. That last
read exposed the preceding 347 summary; it is not a scientific dependency.
The author also read the ARS 3.22.0 router, deep-research workflow, DA role,
logical-fallacies reference and model-runtime policy completely. A truncated
DA passage was reread at lines 140--195 before mathematical work.

This is an authorized, bounded exact-mathematics task. The three audit stages
are raw-definition scrutiny, complete derivation, and adverse/scope checking;
no forced issue quota, full publication pipeline, or model change is used.
Execution is inherited-runtime, shared-history, single-model AI work,
`NOT_CALIBRATED`, not blind or external peer review, cross-model verification,
independent-error assurance, or formal verification.

Only this file is writable by this author. The source card, other package
files and all historical packages remain untouched. No scientific numerical
experiment, external lookup, upload, Git operation, PDF, operator, trace,
or formal Route evaluation is part of this derivation.

## 2. Common coordinates, form, measures and physical actions

Write E=R_u x R_v x R_z. The global chart change

    u=log q, v=q*xi; q=exp(u), xi=exp(-u)*v

is a smooth bijection from q>0, xi,z real onto E. Its orientation identity is

    du wedge dv wedge dz = dq wedge dxi wedge dz.                 (C1)

Thus the original atlas measure is counting_W times Lebesgue on E; no
measure, atom, zero state or sign has been changed. In these coordinates,

    beta=(1+v*z)du+(v dz-z dv)/2,
    d beta=(z dv+v dz) wedge du+dv wedge dz,
    beta wedge d beta=du wedge dv wedge dz.                       (C2)

Indeed the last coefficient is (1+vz)-vz/2-vz/2=1. This proves contact
nondegeneracy and positive orientation on the ENTIRE chart, including
v*z=-1 and both coordinate axes. No energy surface is selected.

The retained physical action for FACTOR-OFF and UNIT-HOLONOMY is

    Phi^t(u,v,z)=(u+t,exp(t)*v,exp(-t)*z),
    R=partial_u+v partial_v-z partial_z.                          (C3)

Direct substitution gives beta(R)=1 and

    contraction_R(d beta)=-(z dv+v dz)+(v dz+z dv)=0.

It is the Reeb field everywhere. The action is complete, satisfies the
group law, preserves beta exactly, and has determinant 1 in E. In original
coordinates its determinant is exp(t)*1*exp(-t)=1. Consequently for EVERY
Borel atlas set A, including null sets and infinite-measure sets,

    mu(Phi^t(A))=mu(A).                                          (C4)

This follows from smooth change of variables chart by chart and countable
additivity, not merely from a formal infinitesimal divergence calculation.

DRIFT-ONLY instead has

    Psi^t(u,v,z)=(u+t,v,z), U=partial_u,
    beta(U)=1+v*z, contraction_U(d beta)=-z dv-v dz.               (C5)

It is complete and strictly preserves beta, since beta is u-independent.
Its determinant is 1, both in E and as exp(t)*exp(-t)*1 in (q,xi,z).
It preserves mu on EVERY Borel set and preserves the contact volume.
It is NOT beta's Reeb action: both Reeb equations hold at the same point
only when v=z=0. On an axis away from the origin the second equation fails;
on v*z=-1 even beta(U)=1 fails. This is a property of this changed control,
not a failure of (C3), and no replacement time or form is made.

## 3. Complete word dynamics, without a factor table

A cover atom is exactly an integer r>1 with no proper nonunit divisor.
Factorization exists by induction on n: a nonatom n splits into smaller
positive factors d,n/d, which can be factored inductively. For uniqueness,
the Euclidean algorithm gives Bezout's identity; hence an atom r dividing
AB divides A or B, because if r does not divide A then gcd(r,A)=1.
Applying this repeatedly and cancelling equal atom factors proves unique
factorization with multiplicity. Sorting gives the uniquely defined fct(n).
This argument uses integer arithmetic, not a list or per-atom parameter.

For any nonempty word w=(a_1,...,a_l), let g(w)=gcd(a_1,...,a_l).
Repeated first-pair coalescence decreases length by one and reaches
the singleton (g(w)) in exactly l-1 steps. This follows inductively from
associativity of gcd; all ordered words, units and repetitions are included.

For the main word rule C, used by DRIFT-ONLY and UNIT-HOLONOMY:

- If g(w)=r^e for an atom r and e>=1, the word eventually reaches (r).
  For e=1 it is already that singleton after coalescence. For e>=2,
  fct(r^e) is e copies of r, which coalesce to (r).
- If g(w)=1, the singleton (1) takes one actual step to empty.
- If g(w)>1 has at least two distinct atom factors, the gcd of its entire
  factor word is 1; it therefore coalesces to (1), then reaches empty.
- Empty itself is terminal, with no successor or artificial absorbing loop.

Define B_r={nonempty w:g(w)=r^e for some e>=1}; define B_0 as all
remaining words, including empty. These are exhaustive and disjoint.
Every B_r reaches the word-fixed core (r); every B_0 reaches empty in
finite time. There are no other word cycles or word basins.

For FACTOR-OFF, EVERY singleton (n), including n=1 and composites, is
word-fixed. Its exhaustive basins are

    B^F_n={nonempty w:g(w)=n}, n>=1; B^F_empty={empty}.           (C6)

Empty is isolated at the word level for this control: no word maps to it.
The first hitting time of (n) in B^F_n is l-1. These changed basins must not
be replaced by the atom-power basins of C.

For either scaled source, let h(w) be the first hitting time of its stated
core (empty or a fixed singleton), and put

    A(w)=sum_(0<=j<h(w)) log(first entry of C_*^j(w)).             (C7)

The sum is empty for a core word. Here C_* is the OWN word rule, C_F or C.
All terms correspond to valid steps; no terminal evaluation occurs. Define
the normalized geometric coordinate U_w=u-A(w). The actual source iterate
to the core sends (u,v,z) to (U_w,v,z). This is an identity on the whole
chart, not a chosen section. For UNIT-HOLONOMY use the same main-C h(w),
but no scaling sum: its core geometric coordinates are exactly (u,v,z).

## 4. Exhaustive OWN inverse domains and source IMAGE

For FACTOR-OFF, a target (w',Q,X,Z) has exactly these predecessors:

    ((n),nQ,X/n,Z),               if w'=(n), n>=1;
    ((a,b,tail),aQ,X/a,Z),        if w'=(g,tail), gcd(a,b)=g.       (C8)

There are none when w'=empty. The singleton condition is w'=(n), NOT
fct(n)=w'. Conversely every displayed source maps back to the target;
any predecessor is a singleton or a longer word and hence is on this list.
Each real inverse domain is the ENTIRE target chart Q>0, X,Z real.

For DRIFT-ONLY the exhaustive list is

    ((n),nQ,X/n,Z),               if fct(n)=w', n>=1;
    ((a,b,tail),aQ,X/a,Z),        if w'=(g,tail), gcd(a,b)=g.       (C9)

In particular empty has the unique predecessor from the singleton (1),
with identity geometry. The proof is the same two-case inversion of its
OWN frozen C and S, and uses no theorem about another owner.

For UNIT-HOLONOMY the word conditions are those in (C9), but the real maps
are identities:

    ((n),Q,X,Z),                 if fct(n)=w', n>=1;
    ((a,b,tail),Q,X,Z),           if w'=(g,tail), gcd(a,b)=g.      (C10)

Every such domain is again the entire target chart. This is not the
cotangent-scaled inverse or a restriction of its target domain.

Within each list the singleton and longer-word families have different
source words. Distinct (a,b,tail) also have distinct source words. The
factorization condition determines n uniquely when it holds. Thus no
actual predecessor is counted twice. Nonempty targets have countably
infinitely many gcd-pair predecessors, for example a=g,b=k*g, k>=1.
The full image of FACTOR-OFF is exactly the nonempty charts; the full
images of DRIFT-ONLY and UNIT-HOLONOMY are all Y. Incoming terminal data
in the latter two controls have not been removed.

The inverse derivative for (C8)/(C9) is diag(a,1/a,1), where a is the
source's first entry; for (C10) it is identity. Each has determinant 1.
Therefore, for every individual inverse theta and EVERY Borel set A
in its exact full domain,

    mu(theta(A))=integral_A 1 dmu.                              (C11)

This is ordinary affine change of variables, including the entire zero
sets, with its all-point analytic version fixed at every point. Summing
over the disjoint actual source charts gives the corresponding full
preimage statement, possibly with infinite multiplicity. Finite actual
branch-pair transports also have determinant 1 and satisfy (C11) on every
Borel set. The source IMAGE logarithmic cocycle is identically zero in
ALL three controls. Its kernel is the WHOLE groupoid; it is not physical
time and is not used to assign a roof or a period.

## 5. Actual retained-lag groupoids, kernels and full quotient topology

Each control uses exactly its actual triples (y,m-n,x), with S_*^m y=S_*^n x
and all required steps valid. Source is x and target is y. Identity and
inverse have the usual triple formulas; composition adds integer lags.
For closure, compare the two iterate exponents on the shared middle point.
Advance the shorter one to the longer one using the actual known longer
history. This produces a common future and the summed lag. It never
advances a terminal beyond its lifetime. Associativity follows from triple
composition. Equal triples are single arrows, regardless of presentations.

Here are exhaustive normal forms. They also prove all orbit and isotropy
claims without replacing actual histories by free rewrite words. Write
y=(w_y,u_y,v_y,z_y), x=(w_x,u_x,v_x,z_x), and lag l. In each line require
v_y=v_x and z_y=z_x. Words in different stated basins have NO arrows.

### 5.1 Scaled sources: FACTOR-OFF and DRIFT-ONLY

In a fixed-singleton basin whose core integer n>1, set L=log n. Then

    (y,l,x) is an arrow iff
    U_(w_y)-U_(w_x)=(l-h(w_y)+h(w_x))*L.                        (C12)

Proof: after first hitting the core, each further iterate subtracts L
from u and keeps v,z. Equality of core futures gives (C12). Conversely,
choose two sufficiently large valid exponents with difference l; (C12)
then gives equality. Earlier common futures can always be advanced to
the core, so no finite incoming arrow is lost. Thus the lag between two
given equivalent points is unique, and ALL point isotropy is trivial.

In FACTOR-OFF's n=1 basin, the normal form instead is

    U_(w_y)=U_(w_x), with EVERY integer l allowed.               (C13)

Here the core step is genuinely identity, so both histories can be
advanced independently after their core entrances. ALL points have
I_x=Z, acting as the identity germ; this includes every nonzero transverse
point and every finite incoming word, not merely the singleton chart.

In a scaled terminal basin, the normal form is

    U_(w_y)=U_(w_x), l=h(w_y)-h(w_x).                           (C14)

Any common future can be advanced to the common terminal, and no later
step is legal. Conversely equality at those terminal iterates proves the
displayed arrow. All isotropy is trivial. This covers DRIFT-ONLY's entire
B_0. For FACTOR-OFF's isolated empty chart, h=A=0 and only identity arrows
remain. In particular it is not merged with the n=1 basin.

The full quotient maps are therefore

    terminal or F n=1 basin:  (w,u,v,z) -> (u-A(w),v,z) in R^3;
    singleton n>1 basin:     (w,u,v,z) -> ([u-A(w)]_L,v,z)
                             in (R/LZ) x R^2.                 (C15)

FACTOR-OFF has one terminal component, one n=1 component and one cylinder
for EVERY integer n>=2. DRIFT-ONLY has one terminal component and one
cylinder for EACH atom r. The fibre statements are iff statements from
(C12)--(C14), not a representative selection.

### 5.2 UNIT-HOLONOMY

Actual real coordinates never change under its source. In B_r,

    (y,l,x) is an arrow iff (u_y,v_y,z_y)=(u_x,v_x,z_x),
    with EVERY l in Z allowed.                                (C16)

All word histories eventually reach the word-fixed (r), with identity
geometry, so sufficiently large exponents realize any lag. Hence I_x=Z
at EVERY point in EVERY B_r. In B_0 the coordinate equality is the same,
but l=h(w_y)-h(w_x), and I_x={0}. Empty and (1) belong to this full
terminal basin; an absorbing terminal step is never used.

The full quotient has one copy of R^3 for B_0 and one copy for every B_r:

    (w,u,v,z) -> (basin(w),u,v,z).                              (C17)

There is no u-circle, even though the atom basins have lag isotropy Z.

### 5.3 Topology, effective kernel and descended geometry

For each fixed source word, target word and lag, the normal forms give
either no arrow or the graph of a global affine coordinate diffeomorphism.
These sectors are open and closed in the inherited topology, because word
labels and lag are discrete. Consequently the ACTUAL groupoid is a
countable disjoint union of smooth graphs, Hausdorff, locally compact,
second countable and etale, with smooth local source/range maps.

Forgetting lag to obtain the effective orbit relation has precisely the
isotropy kernel already listed: Z on FACTOR-OFF's n=1 basin and on
UNIT-HOLONOMY's atom basins, identity elsewhere. The nontrivial elements
are identity germs, not removed states. The original groupoids retain
them; the coarse quotient does not pretend that they vanished from G.
The kernel of the INTEGER-LAG homomorphism, a different notion, is obtained
by setting l=0 in (C12)--(C16); it can contain arrows between different
charts. Neither kernel is the source IMAGE kernel, which is all G.

Every map (C15)/(C17) is open: on each word chart it is a diffeomorphism
to R^3 or the standard open covering R x R^2 -> (R/LZ) x R^2.
It is surjective and has precisely the actual G-orbits as fibres.
Therefore the specified FULL quotient topology is exactly the displayed
disjoint-union manifold topology, not an assumed transversal topology.
All quotient components are Hausdorff smooth three-manifolds, and their
countable union is Hausdorff and second countable.

Every source arrow translates u by a constant and preserves v,z, or is
identity in these coordinates. Thus every actual branch strictly preserves
beta. It descends to (C15)/(C17). On a cylinder replace du by the globally
defined closed form dtheta; on a line use dU. The descended contact volume
is dtheta wedge dv wedge dz or dU wedge dv wedge dz, with positive sign.

This volume is NOT the pushforward of atlas counting measure. In a cylinder
even one singleton chart is an infinite covering in u; in each line
component with incoming charts there are infinitely many equivalent word
charts (unit words for the terminal/main basin, repeated n words for a
fixed gcd basin). Their counting pushforward gives infinite mass to
positive-volume sets. FACTOR-OFF's isolated empty chart is the explicit
exception: there its one-chart pushforward does equal the volume. No
infinite-sheeted pushforward is used as a locally finite quotient volume.

Both physical actions commute with each own source map and hence with all
actual arrows. This can be checked before quotienting: the scaled source
is (u,v,z)->(u-log a,v,z), and UNIT-HOLONOMY is identity in real coordinates.
The quotient actions are exactly (C3) or (C5), with u understood modulo L
only on the cylinder components. They are complete and smooth there.
Strict contact transport and the Reeb equations descend locally. Their
quotient volume preservation on EVERY Borel set follows from the local
determinant-one formulas and a countable Borel chart partition. No finite
total-volume or recurrence theorem is asserted.

## 6. FULL physical return groups, phases and primitive multiplicity

For any control, H_[x]={t:[physical_flow^t x]=[x]}. Commutation with all
actual arrows proves representative independence in both directions.
It is computed below from complete quotient coordinates, not source I_x
or the zero IMAGE cocycle. The explicit formulas exhaust ALL points.

### 6.1 FACTOR-OFF: every integer core, one circle each

In its isolated empty component and its complete gcd=1 component, the
coordinate U is a real line and changes by t. Hence H={0} for EVERY point.
This holds despite I_x=Z throughout the latter component. The complete
free-flow orbit labels there are (exp(-U)*v,exp(U)*z); U is the real phase.

For n>=2, the return equations on its full cylinder are

    t in (log n)Z, exp(t)*v=v, exp(-t)*z=z.                     (C18)

For nonzero t both exponential factors differ from 1. Thus

    H=(log n)Z  exactly when v=z=0;
    H={0}      at EVERY other transverse point.                (C19)

The zero plane coordinates leave the ENTIRE theta-circle, and the physical
flow is transitive on that circle. Therefore there is EXACTLY ONE primitive
physical orbit for each integer n>=2, with least length log n and all
positive returns k log n, k>=1, repetitions of that SAME orbit. All incoming
words in B^F_n map to its actual phases theta=[u-A(w)]_(log n); they do not
create extra copies. Different n are separated by the full word-basin
invariant, so a composite core is not the repetition of a different
integer's orbit merely because its numerical length is a multiple.

For completeness, all nonperiodic cylinder orbits retain their phases too.
On v!=0 they are classified by

    sign(v), v*z, [theta-log|v|]_(log n).

On v=0,z!=0 they are classified by sign(z) and
[theta+log|z|]_(log n). Equality of these invariants is sufficient as well
as necessary: choose t to match the nonzero transverse coordinate, then
the indicated phase equation matches theta. Thus no nonzero point is
silently discarded or identified with the central circle.

There are no stationary physical points, dense return groups or other
periodic loci. The control fails the prime-packet target because EVERY
composite n>=2 owns an additional primitive circle, not because its
source IMAGE or contact geometry failed.

### 6.2 DRIFT-ONLY: an entire transverse plane of circles per atom

On its full terminal component, Psi shifts the real U coordinate and
H={0} for every point. The free-orbit labels are simply (v,z), with U
the real phase. The units and mixed-factor terminal basins are included.

On each atom-r cylinder, Psi changes only theta:

    (theta,v,z) -> (theta+t,v,z),
    H=(log r)Z for EVERY (v,z) in R^2.                          (C20)

At fixed (v,z) the full theta-circle is one physical orbit. Different
transverse pairs cannot merge under source arrows or physical flow.
There are therefore exactly |R^2| distinct primitive circles in EACH
atom basin, each of least length log r, with all its positive returns
k log r belonging to that same circle. Its phase on any incoming word
is [u-A(w)]_(log r). This includes both axes and all nonzero points.

ALL source point isotropy here is nevertheless trivial by (C12)/(C14).
Physical periods do not require source isotropy. There are no stationary
points, dense return groups, composite word-core basins or other returns.
The control has excessive intrinsic multiplicity and its frozen physical
action is not Reeb for beta, despite strict contact and volume conservation.

### 6.3 UNIT-HOLONOMY: lag recurrence without any physical return

Every quotient component retains u in R. Under Phi, equality of quotient
points requires u+t=u, hence t=0 independently of v,z. Consequently

    H={0} at EVERY point of EVERY basin.                        (C21)

All physical orbits are free real lines, classified within each basin by
(exp(-u)*v,exp(u)*z), with u as phase. Distinct basins never merge. There
are no primitive closed physical orbits, repetitions, stationary points
or dense/nondiscrete time-return groups. In particular I_x=Z on ALL atom
basins is retained as ineffective source lag, even at nonzero transverse
points; it does not manufacture a u-period or a physical closed orbit.
The Reeb and contact-volume properties remain valid by (C2)--(C4).

## 7. Adverse audit, limits and integration boundary

The three controls isolate different requirements, with no cross-owner
assembly: FACTOR-OFF has correct finite circle multiplicity but composite
primitives; DRIFT-ONLY has atom basins but continuum primitive multiplicity
and a non-Reeb chosen time; UNIT-HOLONOMY has contact/Reeb geometry and
source lag recurrence but no physical closed orbits at all.

The strongest false inference would be that zero source IMAGE clock or
nontrivial source isotropy decides physical periods. Equations (C18)--(C21)
refute both implications on the full frozen controls. Another false
inference would identify an infinite atlas-measure pushforward with the
descended contact volume; Section 5 gives its precise exception and failure.

All statements above are exact algebraic, differential and quotient-topology
proofs on infinite, untruncated carriers. No orbit table or numerical sample
is an input. Units, empty terminals, every incoming word, both signs and
all nonzero transverse points have been accounted for explicitly.

No unverified MAIN Gate1 lemma is needed: the common coordinate identities
and each control's full quotient are proved here directly. This document
does not adjudicate MAIN's final multiplicity or naturalness, and a correct
control ledger is not a positive verdict for MAIN. fct, ordering, gcd
scheduling, scaling, beta and the choice of physical action remain declared
designs, not proved canonical constructions. T3 is not supplied, classical
A0/A1/A2 are not evaluated here, formal coordinates remain UNASSIGNED and
Route B is NOT INVOKED. Integration and MAIN's portfolio decision belong
to the root author after the authorized independent checks.

## 8. Auxiliary check and artifact validation receipt

A bounded auxiliary worker was dispatched in parallel, after the source
read and before the local derivations were finished. Before receiving ANY
mathematical auxiliary response, this author completed all three
classifications locally and sent the root their basin/quotient/isotropy,
Reeb, measure and complete physical-return formulas. The auxiliary worker
was tasked only to check word basins, retained-lag kernels and full quotient
topology from the same 187-line card. Its later complete response also
checked the physical-return and DRIFT Reeb consequences. All agree with
the author's already-committed formulas; no scientific correction resulted.

Auxiliary identity:
`/root/gnr_control_basin_check/control_source_kernel`.
Its reported scientific text access was only the original card lines
1--187 with the same SHA-256; it additionally read plan and the applicable
ARS instructions. It reported no paper/344 proof/review/scout/peer reads,
file writes, networking, scientific numerical work or further delegation.
It inherited context; no blind, external, cross-model or independent-error
claim follows from this parallel check.

The author wrote and read back all 450 lines of the initial derivation.
That pre-receipt draft had SHA-256
`77f4c6f4c690f5413c83a91e4f6f2d7b9218ebaeaa5b97e864e030d97ba08b29`.
The present receipt clarifies execution chronology and records validation;
the mathematical Sections 2--7 have not changed after that readback.

Read-only mechanical QA checked the one relative Markdown link, eight
identity/scope markers, trailing whitespace, single final newline, and the
original 187-line input hash; all passed with zero reported issues.
The commands were sed/wc/sha256sum, head -n 187 for the locked prefix, and
a short Python standard-library link/format/hash check with no file writes.
For exact exposure accounting: that Python check read the card's complete
bytes into memory before slicing the first 187 lines for hashing. It did
not print, render or scientifically use the appended outcome, which this
author did not read as text. The preceding shell prefix check used only
head -n 187. No outcome has been imported into the scientific input.

Only this evidence file was created/edited, using apply_patch. Final
receipt-only format/link/hash validation and the final file digest are
reported in the handoff, without a self-referential hash inside this file.

EOF — complete control derivations and provenance; MAIN decision not issued.
