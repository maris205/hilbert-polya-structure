# Residue-block rectangle flow and continuous families of primitive packets

Candidate ID: ABF-20260925-RBR01.
Paper: 486-residue-block-rectangle-flow; batch PRE-P0-STRUCTURE-20260925-AB, round 2/5.
Date: 2026-09-25. Type: partial geometric ABF MAIN.
Outcome: OWNED RECTANGLE FLIGHT; CONTINUUM HORIZONTAL PACKETS — STOP / FORK

## Abstract

The current rectangle determines which arithmetic seam is crossed; its residue-block
update changes the dimensions of the next rectangle. The frozen quotient is a
Hausdorff translation surface, and unit-speed motion defines a unique maximal
partial real action with its original flat measure. Its inverse IMAGE is one,
but its clock is actual flight time, not the logarithm of IMAGE. Missing corners
cause genuine incompleteness; finite-time infinite seam crossing cannot occur.
The complete prescribed horizontal window has continuum many distinct primitive
packets. MAIN has circumferences 1 and 3, with entire time isotropy respectively
\(\mathbb Z\) and \(3\mathbb Z\). All three controls retain their own continuous
packet families. No other-direction census, corner completion or clock repair
is used. The one-packet-per-prime target fails on the intact full flow.

## 1. Contract, source and four separate owners

The [91-line card](candidate-card.md) fixes the source and the proof window.
The [claim-intent baseline](claim-ledger.md) was written before this manuscript.
For positive integers \(a,b\ge1\), put \(k=\lfloor(a-1)/b\rfloor\) and
\[
r_b(a)=(a-1)\bmod b,\qquad
h_b(a)=kb+1+((r_b(a)+1)\bmod b).                         \tag{1}
\]
On the block \(\{kb+1,\ldots,(k+1)b\}\), this is the cyclic successor.
It is a bijection; replacing \(+1\) by \(-1\) modulo \(b\) gives its exact
inverse. In particular \(h_1\) is the identity, without a special deleted unit.
Let \(\pi(2j-1)=2j\) and \(\pi(2j)=2j-1\).
The following table specifies each owner's physical dimensions and seam maps:

| Owner | Width \(w_{ab}\) | Height \(B_{ab}\) | Right update \(P_b(a)\) | Up update \(Q_a(b)\) |
| --- | --- | --- | --- | --- |
| M MAIN | \(a\) | \(b\) | \(h_b(a)\) | \(h_a(b)\) |
| R ROOT-OFF | \(a\) | \(b\) | \(a\) | \(b\) |
| D DIVISIBILITY-OFF | \(a\) | \(b\) | \(\pi(a)\) | \(\pi(b)\) |
| L LENGTH-FEEDBACK-OFF | 1 | 1 | \(h_b(a)\) | \(h_a(b)\) |

For each row separately, take the disjoint union of closed rectangles
\([0,w_{ab}]\times[0,B_{ab}]\) minus their four corners. Identify
\[
(a,b;w_{ab},y)\sim(P_b(a),b;0,y),\quad 0<y<B_{ab},
\]
\[
(a,b;x,B_{ab})\sim(a,Q_a(b);x,0),\quad 0<x<w_{ab}.       \tag{2}
\]
The matching heights/widths in (2) are equal for every row of the table.
Write \(\Sigma_V\) for the exact quotient and \(X_V=\Sigma_V\times S^1\).
No angle, transverse point, unit label or seam point is selected or discarded.
Corners were excluded by the original definition, not by this audit.
There is no additional quotient by label symmetries or equal geometric sizes.

For positive integers \(1<d<n\), use the whole rectangle labelled \((n,d)\).
At its right seam, (1) wraps to \(n-d+1\) precisely when \(d\mid n\);
otherwise it advances to \(n+1\). This is the proper-divisor symbolic interface.
Actual position and direction select right/left/up/down transport; updated labels
change subsequent dimensions. The interface is not a static primality acceptor.
The chosen block cycle and flat geometry are nevertheless design inputs:
no old Logistic/Hénon conjugacy or strong naturalness theorem is asserted.

## 2. Quotient topology, flat atlas and exact seam inverses

An interior point has one representative. Every open-edge point has exactly two:
its paired opposite-edge point in (2), possibly in the same rectangle.
There are no longer seam classes, since a noncorner point lies on only one edge
and each side pairing has its unique inverse. This also handles self-glued units.

Interior Euclidean disks give charts. Around a right seam at height \(y_0\),
choose a radius smaller than both adjacent widths and the distances to edge ends;
if the two sides belong to one rectangle, also make their collars disjoint.
The right collar has coordinates \((x-w_{ab},y)\), and the paired left
collar has coordinates \((x,y)\). They glue to an open disk centered at \((0,y_0)\).
Top/bottom collars give the analogous chart. Their preimages are relatively open
in the two rectangles, so these chart neighborhoods are quotient-open.
Conversely a quotient-open neighborhood of a seam contains such a smaller pair
of collars, by openness at both representatives. Thus these are charts for the
specified quotient topology, not for a replacement topology.

Two distinct quotient points have finite, disjoint sets of representatives.
Choose their interior disks or paired collars small enough to be disjoint in
each of the finitely many rectangles involved and to avoid all other edges.
These are disjoint saturated neighborhoods. Hence \(\Sigma_V\) is Hausdorff.
Rational interior disks and rational edge-center/radius collars give a countable
basis, including coverage of all irrational edge coordinates.
All chart transitions are translations, with integer translation vectors because
all four owners have positive-integer side lengths. The quotient is therefore
a second-countable oriented smooth flat surface without boundary, possibly
disconnected and metrically incomplete. Its area form is locally \(dx\wedge dy\).

The declared quotient Borel structure equals the atlas Borel structure.
One inclusion follows from continuity of the quotient map. For the other, a set
with Borel preimage restricts in a chart to one interior piece or two Borel
half-disk pieces, whose union is Borel. The countable chart cover finishes the
argument. A countable Borel partition subordinate to these charts identifies
the space with a countable disjoint union of Borel Euclidean subsets, so it is
standard Borel. The same conclusions hold after taking the full \(S^1\).

The actual inverse of a right gluing from label \((a,b)\) is a left crossing
from its target, using \(P_b^{-1}\) and the predecessor's own width.
An up gluing is inverted using \(Q_a^{-1}\) and the predecessor's own height.
Right/left inverses require \(0<y<B\); up/down inverses require \(0<x<w\).
For M/L these inverses are the negative modular steps in (1); R uses identity;
D uses \(\pi\) itself. These enumerate every inverse seam because the side
pairings are bijections and the seam classes have exactly two representatives.
Corners supply no extra inverse, and no inverse is selected from competing
itineraries. Seam representatives describe one state, not two zero-time arrows.

## 3. Full partial real action and its actual domains

In a flat chart let \(v=(\cos\theta,\sin\theta)\) and
\[
\dot q=v,\qquad \dot\theta=0.                           \tag{3}
\]
Translations have identity linear part, so (3) agrees on every chart overlap,
including a seam tangent. Local straight flights are unique. Concatenating
them gives a unique maximal connected open time interval \(I_z\ni0\).
Write \(\Phi^t z\) for this continuation when \(t\in I_z\).
Every compact legal time segment has a finite chart subdivision by its compact
image and the local flow construction. In particular there is no arbitrary
waiting, reflection, or discontinuous choice at a tangent seam.

There is also an explicit exact-domain algorithm. In a rectangle interior move
along the current straight ray to the first side. If it meets an open side,
apply (2) or its actual inverse according to direction and continue.
If two sides are met at their common corner, the limiting time is excluded.
A trajectory lying on an open seam uses its collar chart until the seam end;
that missing-corner endpoint is excluded as well.
Run the same algorithm backwards for negative time.
This includes every physical direction and every legal finite incoming history.

For these four owners, finite-time infinite seam execution is impossible.
During any finite itinerary develop the charts in \(\mathbb R^2\).
The developed position is \(q_0+tv\), and all coordinate offsets are integer.
Every transverse vertical crossing therefore has developed first coordinate
in \(\mathbb Z\), and every transverse horizontal crossing has second coordinate
in \(\mathbb Z\). If a velocity component is nonzero its developed coordinate
is strictly monotone, so each integer level is crossed at most once.
A time segment of length \(T\) meets at most
\((|v_x|+|v_y|)T+4\) such levels. If a component is zero, there is no transverse
crossing in that direction; a segment lying along that seam ends at its corner
or has a finite collar cover on every proper compact subsegment.
Thus no infinite sequence of transverse events fits in finite time.
With only finitely many events, finitely many labels are visited.
An endpoint away from a corner has a flat chart and extends, so no other
finite-time escape occurs.

Consequently \(I_z=(-\tau_-(z),\tau_+(z))\), where each finite \(\tau_\pm\)
is exactly the first missing-corner hitting time in the corresponding algorithm,
and is infinity if there is no such hit. Hitting instants themselves are not
objects or arrows. All prior real states and all their finite histories remain.
For example the bottom seam of label \((1,1)\), at \(0<x<1\) with
\(v=(1,0)\), approaches a deleted corner at time \(1-x\) in every owner.
Both seam representatives approach their deleted corners; no regular chart can
contain this limit, since its finitely many representative pieces stay locally
away from those corners. These are genuine incomplete states, not stationary
terminal states with invented real isotropy.

Local continuation depends smoothly on initial data; a finite chart subdivision
of a legal compact segment gives an open neighborhood of legal executions.
Thus \(\mathcal D=\{(t,z):t\in I_z\}\) is open and \(\Phi\) is smooth there.
Uniqueness, reversing the same chart path, and concatenation give
\[
I_{\Phi^s z}=I_z-s,\quad
\Phi^{t+s}z=\Phi^t(\Phi^s z),\quad
(\Phi^t)^{-1}=\Phi^{-t}.                               \tag{4}
\]
In (4) both constituent times must be legal.
For any target \(z\), its entire inverse at time \(t\) exists exactly when
\(-t\in I_z\), and is the unique \(\Phi^{-t}z\). No outgoing test at a later
excluded corner, integer cutoff or history-depth truncation is introduced.

## 4. Original measure, IMAGE and physical-time groupoid

Each owner has its own pushforward
\[
\mu_V(E)=\sum_{a,b\ge1}\int_{R^V_{ab}\setminus\{\text{corners}\}}
\int_{S^1}\mathbf1_E([a,b,q],\theta)\,dq\,\frac{d\theta}{2\pi}. \tag{5}
\]
Seams are null, so their paired representatives do not double area.
Every flat chart has density \(dq\,d\theta/(2\pi)\), also across a seam:
its two half-disks contribute their separate halves. The measure is sigma-finite.

For a fixed legal time, in initial/final flat charts the local flow has form
\[
(q,\theta)\longmapsto(q+t(\cos\theta,\sin\theta)+\lambda,\theta),
\]
with a constant chart translation \(\lambda\). Its derivative is block triangular,
with diagonal blocks \(I_2\) and 1, hence determinant one.
The same holds for its actual inverse. Countably many such neighborhoods cover
the open domain of \(\Phi^t\). Disjointifying the cover and using injectivity
from (4) proves for EVERY Borel \(E\subset\operatorname{dom}\Phi^{-t}\)
\[
\mu_V(\Phi^{-t}E)=\int_E1\,d\mu_V.                     \tag{6}
\]
The derivative supplies the pointwise version \(J_{\Phi^{-t}}\equiv1\), including
all retained seams, tangent directions and measure-zero horizontal families.
The atlas transitions also have determinant one, so this version is consistent.
Each of the four table rows satisfies this proof with its own dimensions and
own seams. No measure or clock has been transferred between owners.

The physical clock is \(t\), and the actual groupoid is
\[
G_V=\{(\Phi^t z,t,z):t\in I_z\},\qquad c(g)=t.           \tag{7}
\]
Source is \(z\), range is \(\Phi^t z\); inversion negates \(t\), composition adds it.
The arrow space is represented by the open \(\mathcal D\) and is Borel.
Equal endpoints at different times are different arrows; redundant seam charts
do not create new arrows. The time-clock kernel is precisely the unit arrows.
The IMAGE logarithmic cocycle is zero on all arrows by (6), so its kernel is
all \(G_V\), and its intersection with the time kernel is the units.
There is no integer lag counter or added real-height extension in this owner.
In particular measure preservation does NOT give a zero physical clock.

For any \(z\), all incoming histories are its legal negative-time continuations
and their concatenations under (4). Their full orbit is
\(\mathcal O(z)=\{\Phi^t z:t\in I_z\}\); no other predecessor can enter it.
If a nonzero return exists, uniqueness repeats its segment in both directions,
so the orbit is complete and its time stabilizer \(H_z\) is a subgroup of
\(\mathbb R\). It is closed by continuity and has no arbitrarily small nonzero
element: a sufficiently short straight flight in one chart cannot return.
Thus its entire group is \(H_z=L\mathbb Z\) for a unique \(L>0\).
If there is no return, \(H_z=\{0\}\), including every incomplete orbit.
This is a structural dichotomy, not a census of the other directions.
The kernel of forgetting time and retaining only endpoint pairs is exactly
the bundle of these isotropy groups; it is not silently factored out.

On a periodic orbit the full phase is \(s\bmod L\), with
\(\Phi^t(s)=s+t\bmod L\). Arrows between phases \(s,s'\) are precisely
\(t=s'-s+kL\), \(k\in\mathbb Z\); their self-arrows are exactly \(kL\).
The least positive physical primitive is \(L\), repeated by \(kL\).
For a nonperiodic orbit, \(s\mapsto\Phi^s z\) is one-to-one on the full open
interval \(I_z\); changing base translates this time coordinate.
No extra stationary endpoint, phase quotient, or attracting incoming basin occurs.

## 5. Entire horizontal-window packets

The frozen starting labels are \(W=\{(1,1),(1,2),(2,2)\}\).
Take BOTH \(v=\varepsilon e_1\), \(\varepsilon=\pm1\), every
\(0<\eta<B_{ab}\), and every longitudinal phase, including actual vertical seams.
Horizontal flight never hits the top/bottom boundaries and keeps \(b,\eta,v\).
For \(\varepsilon=+1\), positive time follows \(P_b\); for \(\varepsilon=-1\),
it follows \(P_b^{-1}\). The entire cycle, not just its initial W representative,
belongs to the audited orbit.

For a finite positive-direction cycle \(a_0,\ldots,a_{r-1}\), put
\[
C=\sum_{i=0}^{r-1}w_{a_i b},\qquad
p=\sum_{j<i}w_{a_j b}+x\pmod C.                        \tag{8}
\]
The vertical seam pairings identify exactly the endpoints in (8).
Hence the strip is \((\mathbb R/C\mathbb Z)\times(0,B)\), and its flight is
\(p(t)=p+\varepsilon t\bmod C\). All its times are legal: positive widths
and interior \(\eta\) exclude both corners and finite accumulation.
Therefore \(\Phi^t z=z\) if and only if \(t\in C\mathbb Z\).
This proves ENTIRE H, least physical primitive, and every phase/repetition;
it is not merely an exhibited seam-count period.

For MAIN the W row \(b=1,a=1\) is a single width-1 cycle.
For \(b=2\), (1) gives \(1\mapsto2\mapsto1\), with widths 1 and 2.
For R each label is fixed. For D, \(\pi\) interchanges 1 and 2 at either b.
For L the MAIN label cycles remain, but both widths and heights are one.
Thus the complete four-owner window is:

| Owner | Distinct family / W entrances | Full label cycle | Own \(\eta\) range | \(C\), hence ENTIRE \(H=C\mathbb Z\) |
| --- | --- | --- | --- | --- |
| M | \((1,1)\) | \((1,1)\) | \((0,1)\) | 1 |
| M | \((1,2),(2,2)\) | \((1,2)\leftrightarrow(2,2)\) | \((0,2)\) | 3 |
| R | \((1,1)\) | \((1,1)\) | \((0,1)\) | 1 |
| R | \((1,2)\) | \((1,2)\) | \((0,2)\) | 1 |
| R | \((2,2)\) | \((2,2)\) | \((0,2)\) | 2 |
| D | \((1,1)\) | \((1,1)\leftrightarrow(2,1)\) | \((0,1)\) | 3 |
| D | \((1,2),(2,2)\) | \((1,2)\leftrightarrow(2,2)\) | \((0,2)\) | 3 |
| L | \((1,1)\) | \((1,1)\) | \((0,1)\) | 1 |
| L | \((1,2),(2,2)\) | \((1,2)\leftrightarrow(2,2)\) | \((0,1)\) | 2 |

Every row includes both signs separately. L uses its own unit-square boundary:
there is no transverse coordinate between 1 and 2 even at integer label b=2.
The D orbit through \((1,1)\) necessarily includes \((2,1)\); this is following
the prescribed orbit, not broadening the starting window.

Within a row, all longitudinal phases give ONE packet for each \((\eta,\varepsilon)\).
Different \(\eta\)'s are not flow-related, since the entire horizontal execution
preserves \(\eta\). Different signs are not related, since the full flow preserves
the direction as a state. Different rows are not related either: their actual
horizontal label cycles are disjoint. Vertical seam equivalence at an initial
phase is already included in (8); no horizontal-boundary identification applies
to an interior \(\eta\). Uniqueness of the FULL flow rules out a hidden alternative
excursion that would join two rows or transverse coordinates.
Thus M/D/L's W entrances \((1,2)\) and \((2,2)\) represent the same packet
exactly when their own \(\eta\) and sign agree. R's three entrances stay separate,
even when the circumferences agree. This is exact deduplication, not time-based merging.
Every row contains a continuum of distinct primitive packets for each sign.
All incoming to each such orbit is precisely that same complete circle by (4).

## 6. Decision, limits and provenance

MAIN already has a continuum of distinct positive primitive packets of time 1.
This contradicts the target's countable one-packet-per-prime ledger.
It also supplies a direct purity failure: the elementary exponential series gives
\(2<e=\sum_{n\ge0}1/n!<3\), since
\(\sum_{n\ge2}1/n!<\sum_{n\ge2}2^{-(n-1)}=1\).
Hence \(1\ne\log p\) for every ordinary integer prime p.
Time 1 is primitive because its ENTIRE H is \(\mathbb Z\), not a chosen repetition.
The controls retain continuous packet families under their OWN actions.
The adverse mechanism therefore does not require the arithmetic wrap predicate.

| Obligation | Scoped result |
| --- | --- |
| Quotient/flat atlas/Borel/partial action/all inverse domains | ESTABLISHED for all four owners |
| Original measure and every-Borel/full-point IMAGE | ESTABLISHED; \(J=1\), separate from physical time |
| Finite-time infinite seam escape | EXCLUDED; missing-corner incompleteness retained |
| Source lineage and actual two-way geometry feedback | Exact interface established; strong naturalness OPEN |
| W horizontal H/phase/repetition/full incoming/multiplicity | COMPLETE for all four owners |
| MAIN positive-ledger nonemptiness | ESTABLISHED |
| MAIN universal prime-only purity / target packet multiplicity | REFUTED |
| All-prime coverage and other-direction periodic census | OPEN / NOT AUDITED |
| T0 / target T1–T2 | Owner established / target NOT PASSED |
| T3 / classical ASFS / formal coordinates / B | NOT AUDITED / NOT APPLICABLE / UNASSIGNED / NOT INVOKED |

No angle census, log-coordinate change, corner filling, prime-dependent length,
measure repair or new owner is introduced. The full source remains intact as
originally defined; the horizontal gate is only an audit subfamily. Decision:
STOP / FORK, not a theorem against every arithmetic geometric flow.

Author fully read the original card 1–91 through EOF, SHA-256
e023221e92c2939d80aba491c149437d96d1b1131fbe61045338361ca9dd73ba,
and the stream template. The methods are exact seam topology, straight-flight
continuation, local change of variables and finite-cycle algebra.
No scientific code, approximate experiment, external theorem or network was used.
No CP1 scope, raw, reviewer or peer manuscript was read by this author.

Design-only comparison: author read [334 card](../334-factor-exchange-seam-billiard/candidate-card.md)
1–162/250, prefix SHA
d4d2616a4e0ce8b39948a1408ccc55fe71136e9456b2d0af2d76531c00b26cde;
same-author helper read [392 card](../392-divisor-torus-cover/candidate-card.md)
1–49/114, prefix SHA
ab5e90f5e492f5b002408e742f6c7991a8d59ca7777d1fb2950380c826c9e521.
Appended outcome headings, not their bodies or proofs, were additionally exposed.
The definitions compare disk factor-exchange seams and one-way path/torus coupling;
no old mathematical result is transferred. Prior 334 authorship, shared history,
the readme1–110 batch overviews, and pre-freeze transverse/lattice risk discussion
are disclosed: this was not blind or outcome-sealed design.
An additional root-requested, separate log-coordinate design comparison read
171 card1–37/103, prefix SHA
807f19dee50ea2b0b2e8f4d3da71cb0c7f5563173f5cadc4d4787e86cd6f82e2,
and 176 card1–33/114, prefix SHA
2fb860fc2dc846c91577d35ed70d0a1b1b13f40cdc3ebde08cd10993e8941169,
with result/erratum headings only.
Those Hamiltonian definitions and the changed-geometry reserve are not proof inputs.

Same-author helper /root/arithmetic_feedback_scout/dss_g_fixed_author read only
the full 91-line card, measured its same hash, and derived R/D/L's horizontal
cycles, transverse domains, entire H and entrance deduplication.
The author independently checked and integrated this subproof.
The helper read no reviewer/other proof and is not an independent review seat.
AI agents supplied mathematical derivation, drafting and internal checking;
no human or external verification is certified. Shared-model work is NOT_CALIBRATED.
Data availability: the definitions and exact derivation are in this package;
there is no experimental dataset. Ethics: no human subjects or private data.
Contributions: AI-assisted design, analysis and drafting as disclosed; human
authorship responsibility is not certified here. Funding and conflicts were
not supplied, so no declaration of their absence is made.

Navigation: [card](candidate-card.md), [ledger](claim-ledger.md),
[README](README.md), [separate final review](evidence/review.md).
