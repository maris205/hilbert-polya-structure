# LRC01 — frozen-card independent raw derivation

Candidate: ABF-CONTROL-20260925-LRC01. Paper489, Batch AB round5/5.
Reviewer: `/root/rcr01_independent_review`, 2026-09-25 UTC.
Stage: DISTINCT RAW RELEASE; manuscript LOCKED.
Changed-geometry CONTROL, not MAIN. Same-model/shared-history NOT_CALIBRATED.

## 0. Input, method and non-exposure

Sole new scientific input: `candidate-card.md`, FULL1–84/EOF, SHA-256
`d875b4d93fa3cd5b37e4fd5a6e6a94a5841bd3ddfcf2a7ad8460f2ca68967068`.
Own CP1 has149 lines, SHA-256
`63c98d4b0cb760189cec4eb6a18e1efbdac1492eb8b594683eeaf9c18f15e4ba`.
No author paper/README/ledger, peer/helper result,486 scientific file,
old proof or other scientific source was read. Earlier disclosed shared
history is retained, not represented as blind or isolated execution.

Personally completed ARS/local instruction reads are retained as disclosed
in CP1. The bounded original-proof adaptation uses exact definitions and
proofs, not numeric scores, an issue quota or a literature campaign.
No scientific code/numerics, external network, Git, PDF, old edit or490.
All constructions below are made afresh from the card, not transferred
from486. The only orbit-classification window is the full legal saturation
of the open label(1,1) cell in each of the four separately owned objects.

## 1. Labels, complete seam inverses and the declared geometries

For fixed positive integer b write a-1=qb+r,0<=r<b. Then

    h_b(a)=qb+1+((r+1) mod b),
    h_b^{-1}(a)=qb+1+((r-1) mod b).                     (1.1)

Thus h_b is a bijection of each b-element positive-integer block.
Its wrap occurs exactly when r=b-1, equivalently b divides a; otherwise
it advances within that block. This gives the stated residue/divisor
mechanism without a prime table or an external action selector.
Let pi interchange(2k-1,2k) for each k>=1, so pi^{-1}=pi.

Use the following translation coordinates and length data on each OWN
cell, always removing all four corners but retaining every open edge:

| Owner | Coordinates | Horizontal/vertical lengths | Right/top label updates |
| --- | --- | --- | --- |
| LRC primary CONTROL | u=log x,v=log y | alpha_a=log(a+1),alpha_b=log(b+1) | (h_b(a),b),(a,h_a(b)) |
| R | u=log x,v=log y | alpha_a,alpha_b | (a,b),(a,b) |
| D | u=log x,v=log y | alpha_a,alpha_b | (pi(a),b),(a,pi(b)) |
| E | u=x-1,v=y-1 | a,b | (h_b(a),b),(a,h_a(b)) |

Call the relevant lengths w_a,w_b. A right edge has exact domain
u=w_a,0<v<w_b and maps to u'=0,v'=v in the updated cell. A top edge
has v=w_b,0<u<w_a and maps to v'=0,u'=u. No corner belongs to a domain.
The horizontal update preserves b, so the vertical edge lengths agree;
the vertical update preserves a, so the horizontal edge lengths agree.

At a left edge in label(a,b), the complete inverse neighbor is
(h_b^{-1}(a),b) for LRC/E, the same label for R, or(pi(a),b) for D;
restore its right-edge coordinate to that predecessor's w-length and
keep v. At a bottom edge similarly use h_a^{-1}(b), b, or pi(b),
restore its top coordinate and keep u. These are bijective seam inverses
on the FULL open edges. There is no choice of another incoming label.
This explicit matching verifies the atlas hypotheses separately for
all four owners; E has not inherited the logarithmic lengths or measure.

## 2. Exact quotient, separation, atlas and Borel measure

Start from the topological disjoint union Y of the countably many closed
rectangles with their corners deleted, using the stated coordinates.
Each remaining boundary point lies on exactly ONE open edge. Consequently
the seam equivalence classes have two points, including self-glued sides
of one cell, while interior classes are singletons. There is no hidden
corner equivalence class or chain of identifications through a corner.

The quotient map q:Y->X_O is closed. Indeed each open edge is closed
relative to its corner-deleted rectangle. For a closed subset C of Y,
its saturation is C together with the edge-pair images of its boundary
parts. In any fixed rectangle only four neighboring edge images enter.
Each is closed in the corresponding edge and hence in that rectangle;
their finite union with C is closed. Thus the saturation is closed in Y,
which is exactly the quotient criterion for q(C) to be closed.

Y is Hausdorff and metrizable. Distinct finite equivalence classes admit
disjoint open neighborhoods U,V in Y. Since q is closed, the sets
X_O minus q(Y minus U) and X_O minus q(Y minus V) are disjoint open
neighborhoods of their quotient points. This proves Hausdorff separation.

Interior charts are the ordinary open coordinate rectangles. At a right/
left seam choose a small v-interval avoiding both removed corners and
epsilon smaller than both adjacent horizontal lengths. Combine the
right collar of the old cell and the left collar of its neighbor in
coordinates

    (U,V)=(u-w_a,v) on the old collar,
    (U,V)=(u',v') on the new collar.                    (2.1)

Its quotient is an open rectangle spanning U=0. Top/bottom collars have
the corresponding formula(V=v-w_b on the old side, V=v' on the new).
Small collars meet no other edge. These are saturated neighborhoods,
so the charts are homeomorphisms for the EXACT quotient topology.
On overlaps all transitions are translations, on each overlap component.
Countably many rational subcharts cover interiors and collars, proving
second countability and giving a two-dimensional translation atlas.
There is no residual boundary at a retained seam and no chart at a corner.

This proves the declared smooth/Borel carrier directly. In LRC/R/D the
smooth matching is in LOG coordinates, not in the unmodified Euclidean
normal coordinate x or y. Their within-cell exponential vector need not
match raw Euclidean normal derivatives; that is not the frozen atlas.
E instead really uses the Euclidean translation structure specified for it.
No assertion about a regular quotient of the FLOW ORBITS is needed.

Define the original measure by summing the given cell measures through q.
Edges have zero area, so double seam representations add no mass. In every
interior or collar chart this measure is exactly du dv: for LRC/R/D,
dx dy/(xy)=du dv; for E,dx dy=du dv. The collar's two half-strip areas
join correctly across a zero-area seam. Thus this is a well-defined
sigma-finite Borel measure on the exact quotient, with the prescribed
original normalization, not a subsequently chosen invariant probability.

## 3. Actual partial flow, inverse, time groupoid and every-Borel IMAGE

For ALL four owners the vector field in its OWN declared charts is
(du/dt,dv/dt)=(1,1). Translation transitions preserve this vector.
Local solutions are uniquely(u+t,v+t), with actual time t. Gluing these
unique local solutions gives a unique maximal connected interval I_z
containing0 and a continuous trajectory Phi^t z,t in I_z. Every legal
compact interval has a finite chart execution: the compact trajectory
is covered by chart neighborhoods, and their time preimages permit a
finite subdivision. Conversely such compatible chart executions are the
same unique local solution, so no additional path is silently admitted.

Maximality and uniqueness imply

    I_{Phi^t z}=I_z-t,
    Phi^s(Phi^t z)=Phi^{s+t}z                           (3.1)

whenever the intervening times lie in that legal interval. Thus this is
the frozen partial action, not an artificial complete extension. Its
domain{(t,z):t in I_z} is open: a finite execution through open charts
persists for nearby initial points and times. In particular D_t is open,
and Phi^t:D_t->D_{-t} is a Borel/smooth bijection with inverse Phi^{-t}.

Within one original log cell, the inverse is EXACTLY

    (x,y) -> (x exp(-t), y exp(-t)),                    (3.2)

on the actual within-cell time domain. In E it is(x-t,y-t) instead.
For crossings, reverse the executed chart pieces in reverse order,
using the complete left/bottom seam inverses of §1. This specifies every
inverse domain and all incoming finite histories: an expression continued
past a missing corner is NOT an inverse. The path is unique for fixed
endpoint and elapsed time; there are no discretionary seam branches.

In fact no finite-time infinite-seam execution occurs in these four
owners. For LRC/R/D each width/height is at least log2; for E at least1.
Between two successive right crossings, u runs from0 through the whole
width of its current a. Top crossings change b only, so cannot shorten
that width. Hence consecutive right crossings are separated by at least
the same positive lower bound. The analogous fact holds for top crossings,
and in reverse time for left/bottom crossings. Each bounded time interval
therefore has only finitely many seam crossings. If a maximal trajectory
ends at finite time, its last cell coordinates have a limit; any retained
interior/seam limit would allow local continuation. Such an endpoint must
be a missing corner. This proves absence of that possible escape mode,
not completeness of the flow or permission to adjoin a corner.

Own IMAGE is distinct from time. In log coordinates a finite execution
is locally a translation, with measure-Jacobian1. Equivalently, within
one cell the Lebesgue inverse determinant in(3.2) is exp(-2t), while the
density at the inverse point is exp(2t)/(xy); these factors cancel for
the ORIGINAL dx dy/(xy). E separately has ordinary translation inverse
Jacobian1 for its own dx dy. Seam charts use the same own area forms.

For a fixed t, cover D_t by countably many neighborhoods on which the
whole finite execution gives a translation between its initial/final
charts; second countability permits such a cover. Partition it into
disjoint Borel pieces. Each piece's every-Borel IMAGE preserves measure,
and global injectivity of Phi^t makes their images disjoint. Therefore

    mu_O(Phi^t B)=mu_O(B) for EVERY Borel B subset D_t,  (3.3)

including seams and infinite-measure B. No a.e. trajectory deletion is
used. Relative measure-Jacobian1 does NOT set physical time to0: the
clock is the elapsed ODE time t, not minus its logarithmic Jacobian.
There is no added height fibre or normalization by sqrt2.

The actual groupoid has arrows(Phi^t z,t,z),t in I_z. Inverse reverses
t, and composition adds times under(3.1). Its parametrization by the
open(t,z) domain makes it Borel. Only equal triples are identified;
different repeated return times remain different arrows. Every legal
finite incoming arrow to z is(z,t,Phi^{-t}z) with -t in I_z. The full
reverse/maximal histories are exactly the reversed unique trajectories;
no branch word or missing endpoint creates a further history.

The entire return-time set is H_z={t in I_z:Phi^t z=z}. A nonzero return
lets one repeat its legal closed segment in both directions, hence the
maximal interval is R. Returns then form a subgroup of R. Since the
nonzero vector(1,1) moves every point in a local chart, there is a
neighborhood of0 with no nonzero return. The subgroup is therefore either
{0} or LZ with a least positive L: the infimum of positive returns is
positive, and a sequence approaching it must eventually be constant,
else differences would give arbitrarily small nonzero returns.
Thus every incomplete or nonreturning orbit has H={0}. A displayed
period alone is not used to identify L; the entire groups are computed
on the tested saturations below. Other label classes remain unclassified.

## 4. A complete phase lemma for the explicit tested surfaces

On an actual square torus T_s^2=(R/sZ)^2 with coordinates(U,V), the
flow is(U+t,V+t). The transverse coordinate

    delta=(V-U) mod s                                  (4.1)

is invariant. On a delta-circle avoiding all removed points, every U
phase occurs, the orbit is complete, and a return requires t in sZ
from the U coordinate alone. Conversely all such times return legally.
Hence ENTIRE H=sZ, primitive s, and positive repetitions js,j>=1.
Two different delta values are different FULL packets, not different
representatives of a single orbit; within one such circle every phase
theta=U mod s occurs. The times from phase theta_w to theta_z are
theta_z-theta_w+ms, all integers m, after choosing representatives.

If a delta-circle meets removed points, a maximal orbit is instead one
connected open arc between consecutive punctures, in its increasing-U
lift. On an arc0<theta<d, its maximal interval is

    I_theta=(-theta,d-theta),  H={0}.                   (4.2)

All points of that arc form one incomplete packet, with every legal real
phase theta retained and unique elapsed time theta_z-theta_w between
two of them. The incoming times to theta are exactly(theta-d,theta).
No extra time plus s is legal across its missing endpoint. A punctured
geometric circle is not made periodic by adjoining its limit point.
This lemma is applied only after proving each actual quotient and full
saturation below, so it is not a borrowed flow owner.

## 5. Primary LRC CONTROL — full saturation of the open(1,1) cell

From(1.1), h_1(1)=h_1^{-1}(1)=1. Both seams of the(1,1) cell return
to the same label, and their only inverse neighbors are that label too.
No outside label can enter or leave this component, including in reverse
time. Put ell=log2. The map from its log square to(U,V) mod ell is an
exact quotient identification with

    T_ell^2 minus{(0,0)}.                              (5.1)

Every seam point has a sufficiently small legal translate into the open
square, so its FULL saturation is the entire punctured torus(5.1).
No independent direction or height variable has been added.

For each delta in(0,ell), the delta-circle avoids the missing point.
It is one complete packet with EVERY real phase theta mod ell, and

    ENTIRE H=ell Z,  primitive log2,
    all positive repetitions j log2.                  (5.2)

These are continuum many DISTINCT full packets, because delta is both
invariant and a complete orbit test for the nonzero delta circles.
Each one meets the original open square; none is a representative-only
selection. All seam phases are included through the quotient coordinates.

The delta=0 circle loses its sole corner point. Its remaining open arc
(U,V)=(theta,theta),0<theta<ell, is ONE incomplete packet. It has exactly
the intervals and H={0} in(4.2) with d=ell. It has no positive primitive
or positive repetitions. There are no additional packets in this
saturation: all transverse values and all surviving phases were exhausted.
Forward/reverse histories and all incoming are those in §4; uniqueness
and the closed label component exclude hidden incoming from other cells.

The positive prime-time value log2 is present, but continuum many packets
with that SAME primitive already contradict the at-most-one packet for
prime2 clause. This is not a claim that another prime is absent globally.
STOP this changed-geometry CONTROL at the stated window; no later orbit
elsewhere can remove these already distinct owned packets.

## 6. Control R — independently owned identity updates

R's identity updates make the(1,1) cell its own complete label component
directly, with the same fixed log lengths ell, its OWN quotient measure
du dv and its OWN exponential ODE time. Its four deleted corners again
give exactly the punctured torus T_ell^2 minus{0}; its open-cell saturation
is all of it by the same explicit small-time seam-entry argument.
These facts use R's own gluing, not an inherited claim from LRC or486.

Thus delta in(0,ell) parametrizes its entire continuum of complete packets,
with all theta mod ell phases, H=(log2)Z, primitive log2 and repetitions
j log2. Delta0 gives exactly one incomplete open-diagonal packet, with
I_theta=(-theta,ell-theta), H={0}, and all incoming times(theta-ell,theta).
No other packet occurs in this saturation. The identical local result
when both arithmetic updates are disabled is a direct PROVES_TOO_MUCH
warning: this tested positive time/multiplicity is not evidence that
the residue rule has selected a unique prime packet.

## 7. Control D — the saturation is NOT the whole four-cell component

Under pi and its inverse, the labels reachable from(1,1) lie in{1,2}^2.
All four are in its cell-gluing component, with no inverse seam from any
outside label. Put ell=log2, m=log3 and P=ell+m=log6; ell<m.
For a=1 take offset0, for a=2 take offset ell, and likewise for b.
Then

    U=offset(a)+u mod P,
    V=offset(b)+v mod P                                (7.1)

identifies the ACTUAL four-cell quotient with the square torus T_P^2
minus exactly the four grid points

    S={(0,0),(ell,0),(0,ell),(ell,ell)}.                 (7.2)

Indeed right crossing1->2 occurs at U=ell,2->1 at U=P=0;
the vertical crossings have the corresponding V values. Every open grid
edge is paired as required; precisely the cell corners in(7.2) are absent.
The own log-area sum is dU dV on this quotient, and the OWN time evolution
is(U+t,V+t), not a rescaling by a seam count or by the number of cells.

The initial open(1,1) cell has0<U,V<ell. Its transverse values modulo P
are exactly

    delta in A=(0,ell) union(m,P),  or delta=0.          (7.3)

For example small positive V-U gives the first interval and negative
V-U gives the second; strict bounds exclude their endpoints. Conversely
every difference in(-ell,ell) is realized by interior points.
The four punctures have transverse values0,m,ell,0 respectively.
Therefore every delta in A avoids every puncture. Its whole delta-circle
is the full flow packet, is entirely in the saturation, and has

    ENTIRE H=P Z, primitive log6,
    all phases theta mod P, all positive repeats j log6.(7.4)

There are continuum many such distinct packets, parametrized exactly by
the two open intervals A. Both label coordinates traverse their own two
widths in time P; a shorter apparent label/seam subword is not a return
of the quotient point, because U+t must agree with U modulo P.

For delta=0 the punctures at U=0 and U=ell split the ambient diagonal.
The original open cell meets ONLY the arc0<U=V<ell. That arc is one
incomplete packet with I_theta=(-theta,ell-theta), H={0}, all legal real
phases theta in(0,ell), and incoming times(theta-ell,theta). It cannot
reach the other diagonal arc through the missing corner at(ell,ell).

Consequently the EXACT tested saturation is

    {delta in A, every U phase mod P}
    union {(theta,theta):0<theta<ell}.                  (7.5)

It is a proper subset of the four-cell component. Invariance of delta
excludes the other transverse values; missing diagonal endpoints exclude
the other delta0 arc. There is no alternate outside-label route into
them, by the inverse label closure already proved. They are not silently
included or discarded from a claimed whole-component classification;
their exclusion from THIS saturation is part of its exact ownership.
No further orbit classification outside(7.5) is needed for the gate.

All finite incoming and reverse histories of selected packets are the
complete/arc histories of §4. Since6 is not prime and logarithm is
injective, the positive primitive log6 is not log p for any prime.
D thus already has extra positive nonprime packets in the tested family;
their complete multiplicity and all phases are retained.

## 8. Control E — actual Euclidean time and own measure

For E, h_1 and its inverse again fix label(1,1), so the tested component
cannot acquire outside incoming. Its declared coordinates are U=x-1,
V=y-1 with side length1. Actual unit velocity and dx dy=dU dV give

    T_1^2 minus{0},  Phi^t(U,V)=(U+t,V+t) mod1.          (8.1)

Every retained seam point has a small legal translate into the open cell,
so the entire punctured unit torus is its open-cell saturation. This
quotient, its inverse translations and IMAGE were proved from E's OWN
Euclidean charts in §§1–3; log-area preservation was not imported.

Every delta in(0,1) is one complete packet, with ENTIRE H=Z, primitive1,
every phase theta mod1 and all positive repeats j. There are continuum
many distinct packets. Delta0 is exactly one incomplete diagonal arc
0<theta<1, with I_theta=(-theta,1-theta), H={0}, and incoming times
(theta-1,theta); no missing corner is filled. These exhaust the saturation.

The actual time1 is not log p for any integer prime. For an exact check,
exp(1)=sum_{k>=0}1/k! lies strictly between2 and3: the terms after k=1
are positive, and 1/k!<=1/2^{k-1} for k>=2, with strict inequality for
some k, bounds their total strictly below1. Hence no integer equals e.
This is an elementary analytic inequality, not a numerical census.
The extra positive nonprime packets persist without any clock relabeling.

## 9. Complete bounded ledger and gate limits

| Own tested saturation | Complete packet parameter | ENTIRE H / positive primitive | Incomplete packets |
| --- | --- | --- | --- |
| LRC | delta in(0,log2), all phases mod log2 | (log2)Z / log2, all integer repeats | One open diagonal, length log2, H=0 |
| R | delta in(0,log2), all phases mod log2 | (log2)Z / log2, all integer repeats | One open diagonal, length log2, H=0 |
| D | delta in(0,log2) union(log3,log6), all phases mod log6 | (log6)Z / log6, all integer repeats | One selected diagonal arc, length log2, H=0 |
| E | delta in(0,1), all phases mod1 | Z / 1, all integer repeats | One open diagonal, length1, H=0 |

Each row describes every point and actual continuation in its own tested
saturation, with continuum many distinct complete packets and exactly
one incomplete packet. No nonreturning complete packet is omitted from
these saturations: all nonzero allowed transverse values give the proved
complete periodic circles; the only remaining selected packet is the
incomplete arc. Other label classes, and D's unselected part of its
four-cell component, have NOT received a global return classification.

The CONTROL's failure is exact packet multiplicity at the genuine prime
time log2. D/E additionally give genuine nonprime times on their own
tested packets. Every H is the ENTIRE return-time group in the actual
full owner, and every repeat/phase/incoming trajectory remains present.
The excluded punctures are not zero-measure exceptions repaired a.e.;
they are absent points at which actual maximal histories terminate.

Decision: STOP LRC01 as the frozen changed-geometry CONTROL. The log
geometry owns exponential transport, original log-area IMAGE and its
actual time, but it does not repair the exact prime-packet target.
R's identical tested family shows that the positive log2 by itself is
not evidence of arithmetic selection; continuum transverse multiplicity
is a full geometric obstruction, not a sampled or centre-only witness.
No broader parameter robustness, strong naturalness, all-prime coverage,
or architecture advance is claimed. No tuning another geometry follows.

T0 ownership/partial-flow construction is established for the four stated
owners, and the bounded T2 ledger is complete. Arithmetic T1 target is
NOT PASSED; classical ASFS fields NOT APPLICABLE; T3 NOT AUDITED;
formal coordinates UNASSIGNED; Route B NOT INVOKED. There is no MAIN
promotion,486 result transfer, added height variable, determinant or operator.

After FULL self-read and receipt this raw freezes. Card/scope stay
unchanged. HOLD for root FULL raw read and DISTINCT PAPER UNLOCK before
any author-surface access or CP2/CP3 comparison. No490 or next group is
authorized; the completed group still requires user confirmation.
