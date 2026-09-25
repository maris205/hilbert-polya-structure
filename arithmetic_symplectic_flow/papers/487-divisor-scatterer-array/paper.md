# A divisor scatterer array with duplicate primitive flight times

Candidate ID: ABF-20260925-DSA01.
Outcome: OWNED DIVISOR BILLIARD FLOW; DUPLICATE PRIMITIVE TIMES — STOP / FORK.
Paper ID: 487-divisor-scatterer-array.
Date: 2026-09-25. Evidence: exact proofs from the frozen definitions.
Type: full measurable, piecewise-Hamiltonian unit-speed billiard flow.
Classical ASFS fields: NOT APPLICABLE. Formal Route coordinates: UNASSIGNED.
Route B: NOT INVOKED. T3: NOT AUDITED.

## Abstract

We construct the full exterior billiard of the frozen proper-divisor circle
array, including every grazing state and all escaping trajectories. Its
physical flow is complete, reversible and preserves its own Liouville
measure; regular collision branches preserve their own area form. In each
of two specified two-collision itineraries, the complete impact-and-angle
classification contains exactly one closed flow orbit. These distinct
orbits both have entire return-time group `(5/4) Z`. The divisor-off control
instead gives two primitive times `3/2`, while the parity control reproduces
both MAIN packets and the collision-off control has none. Thus the target
of exactly one primitive packet of length `log p` per prime, and no others,
is false, independently of whether `exp(5/4)` is a prime. This is a bounded
negative test of the full geometric owner, not a complete periodic census.

## 1. Identity, question and lineage

For every integer pair `n,d >= 1`, put

\[
D(n,d)\iff 1<d<n\text{ and }d\mid n,
\qquad c_{n,d}=(n,d),\qquad
r_{n,d}=\begin{cases}1/4&D(n,d),\\1/8&\text{otherwise}.\end{cases}
\]

Let `Q` be the plane with these open disks removed, retaining all circles.
On `Q x S^1`, identify only `(q,v)` with `(q,R_q v)` at the same boundary
point, where

\[
R_qv=v-2(v\cdot\nu_q)\nu_q,\qquad
\nu_q=(q-c_{n,d})/r_{n,d}.
\]

Write `M` for this quotient. There is no lattice, translation, address,
collision-word, phase, or time-reversal quotient beyond this identification.
The interior Hamiltonian is `|p|^2/2` on the unit-speed energy shell `H=1/2, |p|=1`;
the reflection rule, not a global smooth Hamiltonian extension, owns impacts.

| Same-object item | Owner and boundary |
| --- | --- |
| Carrier | All of `M`, including boundary classes, grazing and escape |
| Action and inverse | Unit-speed straight flight with specular reflection; negative physical time |
| Measure | Pushforward of `dq1 dq2 dtheta`, with no added boundary atoms |
| Clock | Actual elapsed Euclidean flight time; reflection duration zero |
| Arithmetic | Static proper-divisor bit determines the current circle's geometry |
| Packets | Full closed flow orbits, with their entire return-time groups |
| Controls | Three separate complete owners defined in Section 6 |
| Analytic owner | No transfer operator, zeta, determinant or trace supplied |

The specific lineage arrow is proper-divisor symbolic data -> circle
geometry -> actual collision admissibility and reflection -> next address.
For `n >= 2`, the absence of proper-divisor bits in its row is equivalent
to primality, but the motion is not an algorithm that generates primes or
performs trial division. All addresses coexist in one connected geometry;
`n` is not a fixed component parameter. No Logistic/Henon conjugacy or
classical dimensional-lift theorem is inferred.

The question is whether the full owner can satisfy the stated prime-packet
target. The frozen test uses only
`C1=((4,2),(5,2))` and `C2=((6,2),(7,2))`, allowing every impact point
and unit incidence angle. No further collision-word census is undertaken.

## 2. Full geometric owner, including every boundary state

We first prove a common lemma for any of the three frozen obstacle arrays:
centres `(n,d)`, with each radius in `{1/8,1/4}`. This does not change any
owner; substituting its own radius function constructs each separately.

### 2.1 Geometry and measurable quotient

A bounded set can meet only disks whose lattice centres lie in its bounded
`1/4`-neighbourhood, so the array is locally finite. Distinct centres have
distance at least one; their closed disks are separated by at least `1/2`.
In particular circles never intersect and there are no corner states.
The removed closed-disk family is locally finite, so the interior of `Q`
is precisely the complement of those closed disks.

The domain `Q` is path connected. Given two points in `Q`, their joining
line segment meets only finitely many open disks. Replace each segment
inside a disk by either connecting arc on that circle. The arcs remain in
`Q`, since every other closed disk is disjoint from the circle. The finitely
many replacements give a path between the original points, even if one or
both are boundary points.

Choose the following representative space for the quotient:

\[
S=(Q^\circ\times S^1)\ \cup\
\{(q,v):q\in\partial Q,\ v\cdot\nu_q\geq0\}.
\]

Each equivalence class has exactly one representative in `S`: a transverse
incoming velocity is reflected to the outgoing one, while a tangent
velocity already represents itself. The representative map is Borel,
piecewise identity or the displayed continuous reflection on each circle.
Since `S` is a Borel subset of the ambient standard Borel space, it gives
the quotient a concrete standard Borel structure, equivalent to its
quotient sigma-algebra. Thus no unmeasurable choice or deleted null fibre
is needed. Physical paths also join continuously in the quotient topology
at a reflection; global smooth dependence at grazing is not asserted.

### 2.2 All-point flight rule and non-accumulation

From an interior state, or the chosen outgoing boundary representative,
follow `q+t v` to its first strictly positive circle contact. For a circle
this time is the first admissible positive root of

\[
t^2+2v\cdot(q-c)t+|q-c|^2-r^2=0.
\]

The initial circle's zero root is not a new contact. If there is no finite
contact, follow the ray for all future time. If the infimum of positive
contact times is finite, it is attained: the relevant ray segment is
bounded and only finitely many circles can meet it. Two simultaneous
contacts are impossible because the closed circles are disjoint.

At a transverse hit, the incoming normal component is negative and its
reflection is positive. At a tangent hit, keep the same velocity. In both
cases the future ray leaves the current disk strictly, since for `t>0`

\[
|q+t v-c|^2=r^2+2tr(v\cdot\nu_q)+t^2>r^2
\quad\text{when }v\cdot\nu_q\geq0.
\]

Consequently two consecutive contacts cannot be with the same disk. The
time between consecutive contacts, including grazing contacts, is at least
the `1/2` separation of distinct disks. The first contact from an interior
state can be arbitrarily close, but there are still only finitely many
contacts in every bounded time interval. There is no finite-time Zeno
accumulation. Position travels at unit speed, so it cannot escape to
spatial infinity in finite time either. This proves unique forward motion
for every state, not just almost every state.

Let `I[q,v]=[q,-v]`. It is well defined since `R_q(-v)=-R_q(v)`.
Reversing a constructed path obeys exactly the same rule: reflection is
an involution, and a tangent segment is unchanged. This defines unique
motion for every negative time, proves

\[
\phi^{-t}=(\phi^t)^{-1},\qquad
\phi^{t+s}=\phi^t\phi^s,\qquad I\phi^t I=\phi^{-t},
\]

and gives a complete all-point action of the additive group `R` on `M`.
Neither a missing next contact nor grazing is a terminal state.

Individual contact-time functions are Borel by the quadratic formula and
inequalities. Their countable infimum and the uniquely attaining circle
label are Borel. Iterating this rule, with the finite contact bound on
bounded time intervals, proves that `(t,z) -> phi^t(z)` is jointly Borel.
This is the regularity claimed for the full action.

## 3. Own Liouville measure and regular symplectic section

Define `mu` on the representative space by `dq1 dq2 dtheta` on the
interior and zero measure on the boundary. It is sigma-finite and pushes
to the specified quotient measure. Assigning zero measure to a boundary
does not remove its states or alter their trajectories.

Choose arc length `s`, unit tangent `T(s)` and outward obstacle normal
`nu(s)` on a circle. On transverse outgoing states put `u=v dot T`,
so `-1<u<1` and `v dot nu=sqrt(1-u^2)`. The local flight coordinates
`(s,theta,t) -> (q(s)+t v(theta),theta)` have absolute Jacobian
`|v dot nu|`. At fixed `s`, `|du/dtheta|=|v dot nu|`. Therefore the
physical volume in a transverse flow box is exactly

\[
dq_1\,dq_2\,d\theta=ds\,du\,dt
\quad\text{as positive volume elements}.
\]

Reflection fixes `s` and `u`; hence its two flow-box sides have the same
flux measure. More explicitly, use the incoming angle and signed time
from the contact on both sides of a transverse impact. If the normal's
angle is `beta(s)`, reflection sends the incoming angle `theta` to
`2 beta(s)+pi-theta`, with absolute angle Jacobian one and unchanged
`|v dot nu|`. Thus this stitched box has the same volume density on both
sides, independent of signed time. The flow is translation in that time
coordinate and preserves the box's measure, including its null contact
layer. Free flight itself has Jacobian one.

For completeness, the exceptional histories in this argument are null,
not undefined. For a given circle, the interior states whose future free
line is tangent to it lie in the two hypersurfaces
`det(q-c,v)=+r` or `-r`, restricted by `(q-c) dot v<0`. Their gradients
in `q` have length one, so these sets `N_j` have zero volume.
For a positive rational `a`, let `O_a` consist of interior states having
only transverse contacts through time `a`, with an interior endpoint.
This is open: a compact path has finitely many contacts and nearby circles;
transverse roots are simple and non-contacting circles have positive
clearance. The implicit function theorem gives smooth finite-word
formulas for `phi^a` on `O_a`, and the reversed formulas give a smooth
local inverse. This assertion uses no measure-preservation assumption.

An interior state with a first future graze admits a rational `a` between
the last preceding contact and that graze (or between zero and the graze
if there was no preceding contact). It lies in `O_a`, and its time-`a`
state lies in some `N_j`. All future-grazing states are therefore covered
by the null boundary and the countable union of
`(phi^a|O_a)^(-1)(N_j)`, which is null by local diffeomorphism. Velocity
reversal gives the same result for past grazing. The set `N_g` of all
histories with a grazing event is Borel by the countable actual contact
recursion of Section 2, and is invariant under the full flow. It is null.
No smooth dependence through a grazing event has been used.

Fix any real `t`. On `M` minus `N_g`, the path segment to time `t` is
covered by finitely many free or transverse stitched flow boxes. Their
local time maps preserve volume, including initial or final contact
layers. A countable cover and disjoint Borel refinement, together with
injectivity of the time map, extend this to arbitrary Borel subsets of
`M` minus `N_g`. Finally both `N_g` and its image are null. We obtain,
for every Borel set `A` and every real `t`,

\[
\mu(\phi^t A)=\mu(A).
\]

Images are Borel since the inverse time map is Borel. Thus this is an
all-Borel preservation statement for the full owner, not merely a formal
Jacobian calculation on a selected set of orbits.

There is also an exact area-form statement, limited to regular actual
collision-return branches. If consecutive transverse impacts have arc
coordinates `s,s'`, write `ell=|q'(s')-q(s)|`. The flight's unit velocity
has tangential components `u` and `u'`; reflection at the second circle
does not change its tangential component. Direct differentiation gives

\[
d\ell=-u\,ds+u'\,ds',\qquad
0=d^2\ell=ds\wedge du-ds'\wedge du'.
\]

Hence the branch preserves `ds wedge du`. The actual next-contact guard
is part of that branch: hidden contacts, tangency boundaries and rays
without a next contact are not silently included in its smooth domain.
They remain present in the full physical flow. No global smooth base
symplectomorphism or smooth ASFS suspension is claimed.

## 4. Actual histories, whole isotropy and incoming states

The action groupoid consists of exactly
`(phi^t z,t,z)` for every `z in M` and `t in R`. Composition adds actual
times and inversion changes `t` to `-t`; no distinct time arrows are
identified. Its physical-time cocycle is `c=t`, whose kernel consists
only of unit arrows. This is not a logarithmic IMAGE clock: the measure
is preserved, whereas nonzero physical elapsed times remain nonzero.

For any state, `H_z={t:phi^t z=z}` is the entire isotropy-time subgroup.
It has no nonzero elements arbitrarily near zero. An interior state has
a short collision-free segment on which its position changes; at a
boundary state both its forward and backward outgoing segments similarly
move away from that boundary point. Thus a neighbourhood of zero contains
no nonzero return. A subgroup of `R` with this property is either `{0}`
or `L Z` for a unique `L>0`: in the nontrivial case positive elements
have positive infimum, and two distinct elements close to that infimum
would have a forbidden small difference, so the infimum is attained.
This proves the available full-state isotropy types without enumerating
which untested states are periodic.

If a closed orbit is `gamma={phi^theta z0:theta in R}` with group `L Z`,
all its physical phases are `theta mod L`. For `z=phi^theta z0` and
`w=phi^eta z0`, every arrow from `z` to `w` has precisely a time

\[
t=\eta-\theta+kL,\qquad k\in\mathbb Z.
\]

Its exact full incoming set is just `gamma`: if any state reaches it
at finite positive or negative time, invertibility places that state on
the same full orbit. This statement excludes no asymptotically approaching
trajectory; such a trajectory is not an exact incoming state unless it
actually reaches the orbit. The primitive packet is the orbit itself,
not a chosen collision state, and `kL` for positive integers `k` are
repetitions, not new primitive packets.

## 5. Exhaustive two-collision classification

### 5.1 Necessity at every impact and angle

Consider a two-contact closed traversal between the circles centred at
`a=(n,2)` and `b=(n+1,2)`, with radii `r_a,r_b` from the owner under
study. Let its impacts be arbitrary `A,B`. With no intervening contact,
the outgoing velocity at `A` is `v=(B-A)/|B-A|`. Closing after the contact
at `B` requires the return velocity to be `-v`: it must travel straight
from that same `B` back to the same `A`. Thus reflection at `B` satisfies
`R_B v=-v`, and reflection at `A` satisfies `R_A(-v)=v`.

These equations force normal incidence. Indeed
`2v=2(v dot nu_B)nu_B`, and the incoming sign at `B` gives
`v=-nu_B`; similarly `v=nu_A`. Tangency cannot reverse a nonzero unit
velocity and therefore cannot provide an additional two-contact solution.
Writing `ell=|B-A|>0`, we obtain

\[
A=a+r_a v,\qquad B=b-r_b v,\qquad
b-a=(\ell+r_a+r_b)v.
\]

Since `b-a=(1,0)`, necessarily

\[
v=e_1,\quad A=(n+r_a,2),\quad B=(n+1-r_b,2),
\quad\ell=1-r_a-r_b.
\]

This derives the inner centre-line endpoints from the full incidence
equations; they were not selected as a representative subset. There are
no outer-endpoint, oblique-angle or tangent alternatives for this gate.

### 5.2 Sufficiency in the infinite array

The open segment from `A` to `B` lies strictly outside its two endpoint
disks. Any other centre with second coordinate different from 2 is at
distance at least one from that segment. In row 2, every other integer
centre is outside the pair of adjacent columns, at horizontal distance
at least `1+r_a` or `1+r_b` from the segment. All these distances exceed
every possible radius `1/4`. Hence there is no hidden transverse or
grazing contact anywhere along either traversal of the segment.
The normal reflection at each endpoint reverses the velocity, so the
derived trajectory really is a closed orbit of the full owner.

Start at the boundary class `z0=[A,e1]`. For `0 <= theta <= ell` its
state is `[A+theta e1,e1]`; for `ell <= theta <= 2ell` it is
`[B-(theta-ell)e1,-e1]`, with the stated boundary identifications.
This parameterization is injective on `R/(2ell)Z`: positions are strictly
monotone on each open leg, the velocities on opposite legs differ and
are not identified at interior points, and the two endpoint positions
are distinct. Consequently

\[
H_z=2\ell\mathbb Z\quad\text{for every point of this orbit},
\qquad L=2\ell.
\]

Time reversal does not double this packet. At `z0` it is the same boundary
class, and `I phi^theta z0=phi^{-theta}z0`. Thus the two directions occur
as phases of this one retracing full orbit, not as two orbits identified
by an extra quotient. Section 4 gives its entire incoming set and all
signed phase-to-phase histories.

### 5.3 MAIN results and decisive failure

For `n=4` and `n=6`, the left bit `D(n,2)` is true and the next bit
`D(n+1,2)` is false. Therefore both frozen itineraries have

\[
r_a=1/4,\quad r_b=1/8,\quad
A=(n+1/4,2),\quad B=(n+7/8,2),\quad
\ell=5/8,\quad H=(5/4)\mathbb Z.
\]

Each itinerary contains exactly one packet, including all its phases.
The two packets are distinct in `M`: their spatial projections are the
disjoint segments with first-coordinate ranges `[4+1/4,4+7/8]` and
`[6+1/4,6+7/8]`. A translation is not part of the quotient.

The target requires no positive primitive except `log p`, with exactly
one packet for each ordinary prime. If `5/4` equals some `log p`, these
two packets violate uniqueness. If it does not, either packet violates
the allowed-length condition. These exhaustive alternatives refute the
combined target without any assertion about the arithmetic nature of
`exp(5/4)`. A larger census cannot remove these owned counterexamples.

## 6. Three own controls and adverse findings

DIVISOR-OFF has all radii `1/8`. PARITY has radius `1/4` precisely in
even columns, and `1/8` in odd columns. Each has its own domain, boundary
quotient, complete inverse flow and physical Liouville measure, obtained
by substituting that radius function in Sections 2–4. No MAIN trajectory
or elapsed time is transferred to either control without recomputation.
Sections 5.1–5.2 classify their full prescribed windows, yielding:

| Owner | C1 primitive packets | C2 primitive packets | Entire H on either packet |
| --- | --- | --- | --- |
| MAIN | One, `L=5/4` | One, `L=5/4` | `(5/4) Z` |
| DIVISOR-OFF | One, `L=3/2` | One, `L=3/2` | `(3/2) Z` |
| PARITY | One, `L=5/4` | One, `L=5/4` | `(5/4) Z` |

In DIVISOR-OFF the endpoints are `(n+1/8,2)` and `(n+7/8,2)`, so its
gap is `3/4`. In PARITY the endpoint radii in both windows are exactly
`1/4,1/8`, so its gaps, impacts and full periodic trajectories there are
the same as MAIN's. Each row retains two distinct spatially separated
packets, the whole phase circles, all signed multiples of its own `L`,
and the exact incoming sets proved above. The two-window test therefore
does not distinguish proper divisibility from the parity replacement.

COLLISION-OFF instead has the entire `R^2 x S^1`, including the regions
occupied by former obstacles. Its flow is `(q,v) -> (q+t v,v)`, inverse
time is `-t`, and its triangular derivative has determinant one, preserving
`dq1 dq2 dtheta` on all Borel sets. Since `|v|=1`, equality `q+t v=q`
forces `t=0`. Thus every entire return group is `{0}` and there are no
closed packets anywhere in this control. There is no collision section
and no need to invent C1/C2 events in a flow without obstacles.

These controls show that collisions create the tested returns and the
divisor-dependent radius changes their times relative to DIVISOR-OFF.
They do not certify a prime-specific mechanism: PARITY reproduces both
MAIN windows exactly. The repeated local geometry alone produces equal
periods, a concrete `PROVES_TOO_MUCH` warning. All estimates are exact;
no array cutoff, numerical precision, parameter perturbation, retuning,
or post-failure removal of one packet is used.

## 7. Gate assessment, limitations and decision

| Gate | Evidence and precise state |
| --- | --- |
| T0 | ESTABLISHED for the complete measurable billiard owner, including grazing; regular section symplecticity is explicitly local |
| T1 | Exact static-divisor geometry and endogenous physical time ESTABLISHED; strong arithmetic naturalness OPEN and MAIN/PARITY two-window separation FAILS |
| T2 | Whole two-window packet ownership and repetition laws ESTABLISHED; stated universal purity-plus-uniqueness target REFUTED |
| T3 | NOT AUDITED; no analytic owner introduced |
| Classical ASFS / formal Route | NOT APPLICABLE / UNASSIGNED; Route B NOT INVOKED |

The remainder of the periodic ledger is not classified. Prime coverage,
transverse stability, a global Markov coding and operator theory are not
established. In particular the result is not a no-go theorem for all
arithmetic billiards, conservative carriers or geometric lifts. The
static array and its two radii remain designed inputs; no claim of
canonical arithmetic geometry follows from measure preservation.

The decision is STOP / FORK for DSA01: the full owner itself contains
two distinct positive primitive packets of one time. No tuning or deeper
local search is warranted for this frozen target. A future genuinely
different object needs new authorization and a new frozen identity.

## 8. Reproducibility, access and AI disclosure

The sole current scientific input was the original [candidate card](candidate-card.md),
read fully at lines 1–91 through its explicit EOF marker, SHA256
`a52c8793de88cd52dd03e0157e6aa755ec641c4ea0fa1ac16691f3865637de72`.
The [claim ledger](claim-ledger.md) was first written as OPEN claim intents;
its final dispositions point to the proofs above. The [README](README.md)
is a navigation summary, not additional evidence. At author freeze, the
separate manuscript review had not been accessed or completed by this
author; any subsequent review is a separately owned artifact under `evidence/`.

Prefreeze design access exposed source103's full 11-line original card,
including its negative static-input assertions: SHA256
`9e93488b3a14765595e285646a984344d5410652e9cf2b0c4762cb1c9f9c05fe`.
Source344 lines 1–100 of 218, not EOF, were read for a withdrawn cotangent
alternative; prefix SHA256
`54c2b2c683ca58680fc82612959eedc1abcb6bf04d66e168d4cfac491362e2ad`.
An Outcome heading was visible in a filename/heading search; its appended
body was not read. No old proof was used. These disclosures and shared
476/480 history preclude a blind-origin claim. The two test itineraries
were chosen with design intuition before freeze, not by sealed validation.

This is AI-generated mathematical research and exposition. The main
author integrated the definitions, complete two-window classification,
controls and reporting. One same-author read-only helper,
`cf_foundation_author`, worked on full-flow and measure foundations from
the same original card, not on packet classification or independent
review; its proof was checked and integrated by the main author. No helper
wrote files. Current reviewer evidence, raw reports, peer answers and
other new scientific packages were not read. This shared-history,
same-model process is internal and NOT_CALIBRATED, not external peer
review, human verification, or cross-model validation.

ARS academic writing guidance informed the explicit claim boundaries,
proof/evidence separation and disclosures. The router, writing workflow,
runtime policy, local AGENTS/plan and paper template were refreshed;
retained writing and anti-leakage instructions remained in force. Work
used exact first-principles arguments, `apply_patch`, full text readback,
line counts, hashes and local-link checks. No scientific numerical code,
external literature, network, Git, PDF or old-file edits were used.

Data availability: all mathematical inputs and proofs are in this package;
there is no experimental dataset. Ethics: no human participants, sensitive
data or animal research. Contributions: AI-assisted conceptualization,
formal analysis and writing as disclosed above; no human authorship or
approval is inferred. Funding and conflicts of interest were not supplied
and are not invented. This Markdown record is not a publication submission.
