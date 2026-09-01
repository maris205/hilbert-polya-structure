# Narrative report — uniform ear deletion and triangulation endpoints

## Problem

Begin with a labelled convex polygon.  At each step choose uniformly from
every current vertex, delete it, and record the chord joining its current
neighbours.  Stop at a triangle.  The clock is deterministic, but different
deletion orders can coalesce onto triangulations with nonuniform probabilities;
nonuniformity first occurs at \(n=6\).  The aim is to compute every endpoint
mass and its sharp minimum.

## Main result

Every complete deletion order has probability (6/n!).  For a fixed triangulation (T) and possible final face (r), root the weak dual tree at (r).  Histories ending at (r) are exactly child-before-parent orders, so the rooted-tree hook formula gives

\[
H(T,r)=\frac{(n-3)!}{\prod_{v\ne r}s_v^{(r)}}.
\]

Summing over root faces yields (H(T)) and (Pr(T)=6H(T)/n!).  Reinterpreting (H(T)) as the number of ways to delete leaves of the unrooted weak dual until one vertex remains gives a short recurrence.  It proves (H(T)\ge2^{n-3}), with equality exactly for path weak duals.

## Evidence

The exact verifier enumerates all 68,185 deletion histories for
\(3\le n\le9\), all 625 endpoint triangulations, and every final-face
refinement.  It independently reconstructs connected weak duals, checks the
hook formula and total mass, computes the unrooted leaf-order recurrence, and
brute-forces bounded rooted linear extensions.

## Ownership boundary

Ear clipping, convex-polygon triangulations, Catalan enumeration, weak-dual
trees, reduction-order/linear-extension correspondences, and generic tree
hook formulas are classical inputs.  The elementary, owner-thin residual is
the uniform-current-vertex endpoint distribution, its root-face refinement,
and the sharp path-dual minimum.  A bounded owner non-hit is not a novelty
certificate.  Status: anonymous, `HOLD_EXTERNAL`.
