# Theorem package — HCS-C292

Status: **PROVABLE AS STATED**.

This source-dynamics theorem closes workspace obstruction `HEN-O276`.

Let `m_i>0`, `x_1<...<x_n`, and `v_i` be the canonical data after
mass–momentum premerging of equal initial positions.  The unique global
forward sticky flow is

`X(t)=P_K^m(x+t v)`, `K={z_1<=...<=z_n}`,

where the projection uses `sum m_i z_i^2`.  Its constant-coordinate blocks
are exactly the current clusters.  Equivalently, they are slopes/faces of
the greatest convex minorant through cumulative points
`(M_j,S_j(t))=(sum_{i<=j}m_i,sum_{i<=j}m_i(x_i+t v_i))`.

At each event all maximal collocated consecutive blocks merge.  Several
positions may merge at the same time, and a position may receive arbitrarily
many clusters.  Partitions coarsen, so there are at most `n-1` nontrivial
mergers.  For incoming `(M_a,V_a)`,

`Delta E = (1/(2M)) sum_{a<b} M_a M_b (V_a-V_b)^2`,

with `M=sum M_a`; mass, momentum, and center-of-mass motion are exact.
The atomic measures `rho=sum M delta_X`, `j=sum MV delta_X`, and
`q=sum MV^2 delta_X` satisfy `rho_t+j_x=0`, `j_t+q_x=0`
distributionally.  Kinetic energy satisfies the entropy inequality with one
negative atom of size `Delta E` at each event group.

Proof spine: finite least-contact construction; strict convexity of weighted
projection; pool-adjacent-violators/lower-hull equivalence; induction across
events; completion of squares; ballistic integration by parts and event
cancellation.

Boundaries: initial coincidences are premerged; all masses are positive;
equal-velocity separated clusters need not collide; velocities use a
right-continuous event convention; forward but not backward uniqueness is
claimed.  Finite evidence is not the proof.
