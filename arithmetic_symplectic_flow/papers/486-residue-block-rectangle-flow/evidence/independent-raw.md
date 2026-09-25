# RBR01 — independent card-only geometric and horizontal-gate proof

## Authority and scientific access

ABF-20260925-RBR01; Paper486; batch AB round2/5.
Sole scientific input: candidate-card.md, FULL read1–91 through EOF;
SHA256 e023221e92c2939d80aba491c149437d96d1b1131fbe61045338361ca9dd73ba.
Frozen CP1: scope-review.md,73lines, SHA256 cae2b5ad04d94f5e560347a28e763bd4330d4a31cbe6781ed25a83fa5ea2268c.
Distinct RAW RELEASE followed root's complete CP1 read; manuscript access remains locked.
No author surface, peer/helper proof, old proof or other current scientific file was opened.
Prior same-model history and personally read ARS/local instructions are retained and disclosed;
NOT_CALIBRATED, not blind/human/external or independently calibrated review.
Only this raw file is written. No helper, scientific code/numerics, network, Git, PDF or old edit.

## 1. Four complete sets of geometric data

Write a=kb+r+1, k>=0,0<=r<b. Then h_b(a)=kb+1+(r+1 mod b).
It permutes each block{kb+1,...,kb+b}; its inverse uses r-1 modulo b.
Thus h_b(a)=a-b+1 when b divides a, otherwise a+1, with h_1(a)=a.
The vertical permutation is the same construction with a,b interchanged.
Let H,V denote the right/up permutations of labels, and w,l the physical width/height.

| Owner | H(a,b) | V(a,b) | w,l |
| --- | --- | --- | --- |
| M MAIN | (h_b(a),b) | (a,h_a(b)) | a,b |
| R ROOT-OFF | (a,b) | (a,b) | a,b |
| D DIVISIBILITY-OFF | (pi(a),b) | (a,pi(b)) | a,b |
| L LENGTH-FEEDBACK-OFF | (h_b(a),b) | (a,h_a(b)) | 1,1 |

Here pi exchanges2k-1 and2k and is an involution on every positive integer.
For each row H,V are bijections of ALL labels. H preserves the actual height l;
V preserves the actual width w. Both dimensions are positive integers.
These verified conditions, not borrowed periods, support the common construction below.
No commutation of H and V is required or assumed; they do not define an asserted Z^2 action.
All L seam coordinates use0<x<1 and0<y<1, even when its labels a,b are larger.

## 2. The exact quotient is a Hausdorff translation surface

For each owner take the disjoint topological union of its closed rectangles minus their corners.
An interior point belongs to no seam relation. A noncorner edge point belongs to exactly one
side type and has exactly one partner, because H/V are bijections and preserve the edge length.
Its partner lies on the opposite side and has no other relation except the inverse pairing.
Consequently every equivalence class has size1 in an interior or size2 on an edge.
This also applies to identity updates: opposite edges in one rectangle remain two representatives.
There are no corner classes, interior identifications or hidden transitive four-edge identifications.

Interior Euclidean disks give charts. At an edge point choose an interval away from both endpoints
and thin collars on its two paired rectangles, avoiding every other edge. Glue the two half-collars
by the declared translation. The result is an open Euclidean rectangle chart across that seam.
Its preimage in the disjoint union is open and saturated, including both paired half-collars.
When both sides have one label, take disjoint sufficiently thin collars within that rectangle.
These charts give exactly the quotient topology, not a finer imposed topology.
Their transition maps are locally translations, with derivative the identity.

Two distinct classes have finite, disjoint sets of representatives. Shrink their interior disks
or paired collars to avoid each other's representatives and all unrelated edges; if they use the
same seam, choose disjoint intervals or collars as appropriate. This gives disjoint saturated
neighborhoods, proving Hausdorff separation. Rational-coordinate choices in the countably many
rectangles and seams provide a countable basis of charts. Thus the quotient is a second-countable
Hausdorff smooth translation surface without boundary, not a claim of metric or flow completeness.
Its area form dx wedge dy is well-defined. No classical ASFS base/roof/suspension is thereby supplied.

The quotient Borel structure agrees with the Borel structure of this topology. One direction
follows from continuity of the quotient map. For the converse, if the full preimage of E is Borel,
intersect with each chart's one or two Borel half-collar pieces. Their coordinate images are Borel
subsets of the Euclidean chart; a countable chart cover makes E Borel on the surface.
The same arguments apply separately to M/R/D/L by the data verified in section1.

## 3. Unique flight, exact domains and absence of finite-time infinite crossings

On X=Sigma times S^1 use chart coordinates(x,y,theta) and the smooth nonvanishing vector field
(cos theta,sin theta,0). Translation changes of charts preserve it and do not rotate theta.
Local straight-line solutions agree on every overlap, giving unique maximal continuations.
Seam-tangent points use these same two-sided charts. They are not assigned stationary waiting times.

An exact event description starts in the actual rectangle. For an interior point and forward time,
compute the positive times to its vertical and horizontal sides in the direction v, ignoring
a side pair parallel to v. At a strict first hit, use H/H^(-1) or V/V^(-1), with the actual
opposite-edge coordinate of that owner, and continue. A simultaneous hit of two sides is a
missing corner and ends the legal interval; do not choose an order of two updates at that corner.
An initial seam point is continued in its flat seam chart, entering the determined side when
transverse, or travelling along the seam until its endpoint when tangent. Backward time uses
the inverse updates and the same state direction v; it does not identify v with -v.

Here no finite-time infinite-crossing obstruction actually occurs. Develop any flight segment
into the plane, starting with its rectangle at integer offset0. At each crossing the next
rectangle has an integer-translated offset, since every side length is a positive integer.
The developed flight is Q(t)=Q(0)+t v and every transverse vertical/horizontal crossing occurs
respectively at an integer value of Q_x/Q_y. A nonzero component is strictly monotone, so in
time span T it encounters only finitely many such integer values, at most |v_i|T+2 per axis.
There is at most one corresponding transverse crossing per value: the paired local chart
immediately enters the next positive-width/height rectangle, and a corner encounter stops.
If a component vanishes, there is no transverse crossing in that direction. An orbit lying
on that seam uses its paired collar and stops at a missing endpoint instead of changing labels
infinitely often. Therefore legal compact segments admit finite chart executions.
Integer lattice points inside a larger rectangle are NOT deleted: the lattice is used only
to bound possible actual edge crossings, not to replace the owner by a punctured plane.

Let tau_+(z),tau_-(z) be the first missing-corner times in the forward/backward event procedure,
or infinity if none is encountered. Both are strictly positive. A finite maximal endpoint
with no corner could be extended in an interior or seam chart, since only finitely many
crossings precede it. Hence the exact maximal domain is I_z=(-tau_-(z),tau_+(z)).
For real t, D_t={z:t in I_z}; Phi^t:D_t->D_(-t) is bijective with inverse Phi^(-t).
Local continuation along a legal compact segment makes D={(t,z):t in I_z} open and Phi smooth
there; in particular all domains and maps are Borel. Uniqueness and maximality give
I_(Phi^t z)=I_z-t and Phi^s(Phi^t z)=Phi^(t+s)z whenever t and t+s belong to I_z.
These are the precise partial real-action laws, with no arbitrary continuation past a corner.

None of the four full flows is complete. At a horizontal seam choose0<x<w and v=(1,0).
Both paired rectangles have the same width w; the orbit runs along that seam to its missing
endpoints, with I=(-x,w-x). Those limits are not any existing quotient point: every existing
point has an interior or seam neighborhood supported away from these deleted corner coordinates.
This is allowed incompleteness of the frozen partial owner, not a new exclusion or owner failure.

## 4. Original measure and all-point IMAGE are not physical time

Push forward the sum of rectangle area times dtheta/(2pi), on the declared corner-deleted
rectangles. Every interior chart receives one copy of area; every seam chart receives two
complementary half-chart areas. The seam itself has zero measure, so there is no double mass.
This is a locally finite, sigma-finite measure on X, equal in each chart to dx dy dtheta/(2pi).
No finite global normalization, survival law or probability assumption is inserted.

In flat coordinates the derivative of a fixed legal-time map is
[[1,0,-t sin(theta)],[0,1,t cos(theta)],[0,0,1]], up to translation charts, with determinant1.
Continuation preserves this local formula because all spatial transitions are translations.
It applies at seam and seam-tangent points as well as rectangle interiors.
For any fixed real t and EVERY Borel E subset D_t, change of variables on a countable chart
cover, refined to a disjoint measurable partition, gives mu(Phi^t E)=mu(E).
Bijectivity on D_t avoids image multiplicities; countable additivity also covers infinite mass.
Thus forward and inverse local IMAGE are exactly1 at all actual points, not merely a chosen
a.e. density on null trajectories. This is geometric volume preservation on legal domains,
not a claim of a globally defined invariant probability flow.

The actual groupoid is {(Phi^t z,t,z):t in I_z}; composition adds actual times and inverse
negates time, as section3 proves. Equal endpoints at different t remain different arrows.
Its physical clock is c=t. Its clock kernel consists only of units; the logarithm of IMAGE
would instead be identically0 on all arrows and is NOT this clock. No height extension is added.
All finite incoming arrows to z are exactly (z,t,Phi^(-t)z) with -t in I_z.
They include every legal real time and every reverse flight, not only seam-to-seam pieces.

## 5. Entire isotropy and phase, including incomplete trajectories

For any z, a nonzero return t gives I_z=I_z-t, so the open interval I_z must be all R.
Thus every periodic trajectory is complete even though the full flow is not.
On such a trajectory H_z is a subgroup by the actual action laws and closed by continuity
and Hausdorff separation. A sufficiently short nonzero flight cannot return in a flat chart,
because |v|=1. Hence0 is isolated in H_z. A nontrivial H_z therefore has a least positive
element L and is exactly L Z: take its positive infimum, use closedness, then Euclidean division.
All repeated returns are kL, with integer k, and the full orbit phase is R/L Z.
If H_z={0}, the orbit map t->Phi^t z is injective on I_z; its phase parameter is that actual
open interval, which is R only when the orbit is complete. Incomplete points are not replaced
by complete lines or deleted for lack of a positive return. No stationary trajectory is present.

The horizontal gate below computes H directly, not just one member of it. These isotropy
facts for other directions are structural and do not classify which angled orbits return.

## 6. Complete horizontal slices and their full-flow packet identity

Fix a row b and a finite H-cycle C=(a_0,...,a_(j-1)). Its physical height is constant along
that cycle. For every open transverse coordinate y and sign sigma=+1 or-1, take all horizontal
segments in those labels, with direction(sigma,0), and identify the actual vertical seams.
The resulting slice has coordinate
u=sum_(i<k)w(a_i,b)+x modulo L_C, L_C=sum_(i<j)w(a_i,b).
This is a full circle, including seam phases, not a selected section or centre.
Its dynamics is u(t)=u+sigma t modulo L_C, so ENTIRE H=L_C Z and primitive L_C.
An oriented phase phi=sigma u modulo L_C makes time act by phi->phi+t.
All repeated periods are kL_C; all arrows between two phase points have times
phi_target-phi_source+kL_C. Every finite incoming/reverse history stays on this same circle.

All these orbits are complete: their y lies strictly inside the row, so they never hit a
horizontal edge or a corner. Directions are constant, and each encountered vertical seam
keeps b,y. Therefore different open y values or different signs cannot meet under the FULL flow.
Distinct H-cycles/rows likewise cannot meet along these horizontal flights, even if another
direction could pass between those rectangles. Quotient interiors have no extra identifications.
Different W labels in one actual H-cycle are phases of the same family, not extra packets.
Horizontal directions have zero angular measure, but their entire geometric orbits are retained.

## 7. All W families for each separately owned flow

The following table identifies each distinct family ONCE. Every row includes ALL its displayed
open transverse interval, BOTH signs, ALL phase points modulo L, and every repeated return.

| Owner | W entry labels / actual horizontal label cycle | Transverse y | Entire H; primitive |
| --- | --- | --- | --- |
| M | (1,1); cycle{(1,1)} | (0,1) | Z;1 |
| M | (1,2) and(2,2); cycle{(1,2),(2,2)} | (0,2) | 3Z;3 |
| R | (1,1); singleton cycle | (0,1) | Z;1 |
| R | (1,2); singleton cycle | (0,2) | Z;1 |
| R | (2,2); singleton cycle | (0,2) | 2Z;2 |
| D | (1,1); cycle{(1,1),(2,1)} | (0,1) | 3Z;3 |
| D | (1,2) and(2,2); cycle{(1,2),(2,2)} | (0,2) | 3Z;3 |
| L | (1,1); singleton cycle | (0,1) | Z;1 |
| L | (1,2) and(2,2); cycle{(1,2),(2,2)} | (0,1) | 2Z;2 |

For M/L, the cycles follow directly from the residue blocks: b=1 fixes a=1, while b=2
exchanges a=1 and2. For M their widths sum to1+2; for L to1+1 under its OWN unit geometry.
R keeps each label, so each circumference is its actual width a; its two period1 rows remain
different flow families. D uses the2-cycle of pi, including(2,1) outside W when starting at(1,1).
Following it is required by the complete owner, not an enlargement of the precommitted gate.
Its two height rows have equal circumference3 but are different horizontal families.
The L row b=2 has physical transverse interval(0,1), not the old interval(0,2).
Leftward travel reverses the same cycle and has the same positive primitive, but its direction
is a different state and packet. These statements exhaust the specified W/horizontal family.

## 8. Gate outcome and bounded handoff

Already the MAIN family through(1,1), at fixed sign and y ranging over(0,1), is a continuum
of distinct FULL flow packets with one positive primitive length1. The target permits at most
one packet at any prime logarithm and no other lengths. If1 were such a logarithm it would
violate uniqueness; if not, these are extras. No transcendence assertion is needed to conclude
failure, and no one-per-transverse-position selection can repair it under this frozen owner.
The other MAIN family supplies the same decisive multiplicity at length3. Each control likewise
fails its own same horizontal gate by a continuum at the positive lengths proved in its row.
Their failures are separately derived; no physical period or relation is transferred to MAIN.

Portfolio: STOP/FORK. The full partial geometric owner, inverse/action laws and all-point
IMAGE are established, with no finite-time infinite crossings but genuine corner incompleteness.
The target fails on the entire predeclared horizontal family; no angled-orbit census or global
prime-coverage classification is performed. Local area preservation is not a classical ASFS,
and a section cannot replace the full source. Strong naturalness is not established.
T0 is established for this partial owner; the requested arithmetic/packet target is NOT PASSED;
T3 NOT AUDITED; classical ASFS NOT APPLICABLE; formal coordinates UNASSIGNED; B NOT INVOKED.
EOF — card-only raw complete; full self-read/freeze, then HOLD for distinct PAPER UNLOCK.
