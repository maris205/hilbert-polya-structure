# MBO: exact threshold-chain reduction and no-promotion boundary

This is an author desk proof, not an independent gate. The literal and full
parameter carrier are frozen in INTAKE.md. No numerical statement is used.

## 1. Full-carrier conjugacy

For each a in {q,...,2q}, define the labelled simple graph

    G_a(D) = ([n], {ij : i < j and d_ij <= a}).

Let C be the set of all nested chains G_q <= ... <= G_(2q) = K_n, with
inclusion meaning inclusion of edge sets on the same labelled vertex set.
The coding J(D) = (G_q(D),...,G_(2q)(D)) is a bijection from the declared
metric carrier onto C. Indeed, D is recovered by assigning each edge its
first level of appearance. Every edge appears because the last graph is
K_n, and the resulting entries lie in [q,2q], so the triangle inequalities
hold automatically. This proves both directions, not just a projection.

For a simple graph G, define N(G) to join distinct i,j exactly when they
have an old common neighbor k. Since G has no loops, any witness k is
automatically distinct from both i and j. For all a and i != j,

    T(D)_ij <= a
    iff some k not in {i,j} satisfies d_ik <= a and d_kj <= a
    iff ij belongs to N(G_a(D)).

Consequently J T = N^chain J, where N^chain acts coordinatewise. This map
preserves C: N is inclusion-monotone, and N(K_n)=K_n for n >= 3. In
particular, for every integer t >= 0, the complete all-time formula is

    G_a(T^t(D)) = N^t(G_a(D)).

This is a full conjugacy to an invariant nested-chain restriction of a
product. It is NOT a claim that C is the unrestricted Cartesian product of
all graph carriers. Nesting couples which tuples are admissible, but it
does not couple their forward updates.

## 2. Exact generic temporal consequences

For a finite self-map F, let tau_F(x) be the least time at which the orbit
is recurrent, and let p_F(x) be its eventual least period. Then

    tau_T(D) = max_a tau_N(G_a(D)),
    p_T(D) = lcm_a p_N(G_a(D)).

Proof. Once every coordinate is recurrent, a common multiple of its periods
returns the whole labelled chain to itself. The tuple is therefore
recurrent at the largest coordinate entrance time. Conversely, if a tuple
is recurrent, its projection onto every coordinate is recurrent, so no
earlier tuple entrance time is possible. A return time of a recurrent
tuple is exactly a simultaneous return time of all coordinates, hence the
least positive return time is their least common multiple. The inverse J
preserves both notions. This argument includes fixed coordinates and the
top coordinate K_n, whose period is one.

It follows that D is recurrent exactly when every G_a(D) is recurrent for
N, and D is fixed exactly when every G_a(D) is fixed for N. These are exact
reductions, not an independent structural classification of N's core.
No sharp all-n entrance bound or closed cycle census is asserted here.

There is an invariant binary-level embedding of every simple graph G:
let d_ij=q on its edges and d_ij=2q on its nonedges. All thresholds below
2q then equal G, so T carries this metric to the metric encoding N(G).
Thus any nontrivial recurrence visible in this subcarrier is already
recurrence of the unweighted owner map. For example, on labels Z/5Z,
the cycle with differences +/-1 maps to the cycle with differences +/-2
and then back, because doubling +/-2 gives +/-1 modulo five. The two
graphs are different on the fixed labels. Their two-level metrics have
exact period two. This is a symbolic calculation, not a pilot.

## 3. Complete but generic inverse reduction

For a target Y, write H_a=G_a(Y). Its entire predecessor set is in
bijection under J with

    {(G_q,...,G_(2q)) in C : N(G_a)=H_a for every a}.

Necessity follows from the intertwining identity. Conversely, any such
nested chain gives one metric D by first appearance, and every threshold
of T(D) equals the corresponding threshold of Y. Injectivity of J implies
T(D)=Y. Distinct chains give distinct predecessors. This proves completeness
and nonredundancy of the reduction, without pretending to enumerate the
single-level N-roots or the nested compatibility constraints.

In particular, the fibre is NOT generally the Cartesian product of its
single-level root sets. No product cardinality formula is claimed. No
closed all-target root parametrization, fibre maximum, extremizer census,
or independent inverse-axis theorem has been established. Merely rewriting
the root equations as an indicator sum would not fill that gap.

## 4. Literal boundaries to earlier systems

Old exact-distance-two dynamics only joins nonadjacent vertices at distance
two. In contrast, N joins adjacent vertices too when a triangle supplies a
third-vertex witness. Thus N(K_3)=K_3, whereas exact-distance-two sends K_3
to the empty graph. The identity adapter fails. We do not infer a global
nonconjugacy theorem from this example.

Old Boolean Gram dynamics Gamma(A)=AA^T retains its produced loops. On a
symmetric zero-diagonal adjacency matrix, one application agrees with N
only off the diagonal; Gamma places a loop at every old nonisolated vertex.
For a single edge plus an isolated vertex, N erases the edge and produces
the empty graph, whereas Gamma produces two loops and thereafter holds.
There is also an explicit obstruction to simply forgetting produced loops
along a Gamma orbit: let G be the path 1--2--3. Then N(G) is the single
edge 13 plus isolated vertex 2, and N^2(G) is empty. But Gamma(A_G) is the
fully looped clique on {1,3} together with the single loop at 2. It is fixed
by Gamma, so forgetting the diagonal of Gamma^2(A_G) still leaves edge 13.
Thus offdiag(Gamma^2(A_G)) differs from N^2(G). This is a symbolic check.
Repeatedly deleting the diagonal changes the orbit mechanism. The known
loop-retaining Boolean-power clock therefore cannot simply be imported.
Again, this is exact failure of the proposed identity/forgetful adapter,
not a universal nonconjugacy claim.

## 5. Disposition

KILL_GENERIC_THRESHOLD_LIFT / NO_PROMOTION. The metric carrier has no
intrinsic triangle-constraint coupling; forward dynamics is precisely a
synchronized invariant-chain product of a direct-owner graph map. The
all-time formula and max/lcm laws are fully proved, but are the excluded
generic mechanism rather than a new recurrent axis. The inverse statement
only transfers the old root problem plus nesting, and supplies no new
extremum. This fails the required two-axis entry threshold before any
scientific execution. Zero pilot boxes remain the declared scope.
