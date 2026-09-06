# Fourth-lane deductions and stopping boundaries

2026-09-05 UTC. These are author scouting deductions, not an independently
accepted two-axis contract. Finite checks pressure the arguments below but
do not establish their all-parameter quantifiers.

## DPF — depth-to-parent feedback

Assumptions: n>=0, p_i is an integer with 0<=p_i<i, root 0 has depth zero,
and d_i=d_(p_i)+1. The update is F(p)_i=d_i-1=d_(p_i).
There is no graph relabelling between iterations.

Strategy: coordinate contraction gives the temporal statement; exact
conditioning on old depths gives every one-step fibre; maximal used parent
gives the fixed-state census. The inverse is an old independent-attachment
mechanism, not an independent new dynamical contribution.

For every vertex j, d_j<=j, by induction. Hence F(p)_i<=p_i and F preserves
the carrier. A nonfixed step strictly decreases the nonnegative integer
sum_i p_i. Every trajectory therefore terminates at a fixed point, with
tail at most n(n-1)/2. No sharp global clock is asserted.

For n>=1, a fixed tree has k=max_i p_i. If k>0, some p_j=k, so fixedness at
j forces d_k=k. An increasing tree reaches depth k at vertex k only along
the complete initial spine 0,1,...,k, so p_i=i-1 for i<=k. The remaining
parents i>k are arbitrary in {0,...,k}, with at least one equal to k.
Conversely, such a spine and tail are fixed: depths on the spine equal
their labels, and each tail depth is p_i+1. The same description works at
k=0. Therefore the number of fixed states is

    sum_(k=0)^(n-1) [ (k+1)^(n-k) - k^(n-k) ],

and equals one for n=0. This proves the entire recurrent set, not its
basin-depth distribution.

Now fix a target q in the parent-tuple carrier. A source p satisfies
F(p)=q exactly when its old depths are e_0=0 and e_i=q_i+1. Each p_i may
then be chosen independently from earlier vertices of depth e_i-1.
Necessity is the depth recurrence. Sufficiency follows by induction on i:
if the earlier prescribed depths are realized, any allowed parent gives
the prescribed depth at i. Thus

    |F^(-1)(q)| = product_(i=1)^n c_i(q),
    c_i(q) = 1                         if q_i=0,
           = #{j: 1<=j<i, q_j=q_i-1}   if q_i>0.

A zero factor means no source. This is an exact full fibre, with no hidden
coupling or transfer-matrix search. Positive factors are equivalent to q
being a restricted-growth sequence: q_1=0 and
q_i<=1+max(q_1,...,q_(i-1)). Indeed, each newly appearing level needs an
earlier occurrence of the preceding level, and conversely the
restricted-growth rule supplies it. The image is therefore the standard
Bell-number class of set partitions encoded by restricted-growth words.

Adapter subtraction: the classical recursive-tree model is built by
independently attaching each later label to an earlier label. Conditioning
those old choices on the depth sequence e gives exactly the sets above.
The displayed formula is the present author's transparent conditioning
deduction, not falsely attributed to a numbered theorem in the retrieved
source. It removes the entire claimed inverse axis. We have neither a
new sharp clock nor a second residual mechanism; disposition is KILL.

## CRS — derivative-root-set feedback

Assumptions: p is prime, S is any subset of F_p and
P_S(X)=product_(a in S)(X-a), including P_empty=1.

For every a in S,

    P'_S(a) = product_(b in S, b!=a)(a-b) != 0.

Thus S and F(S) are disjoint. If 1<=s=|S|<p, the leading coefficient of
P'_S is the nonzero element s, and its degree is s-1. Consequently
|F(S)|<=s-1. For S=empty, P'_S=0 and F(S)=F_p; for S=F_p,
P_S=X^p-X and F(S)=empty. Every proper nonempty set strictly shrinks
until it reaches empty. The sole recurrent component is the empty/full
two-cycle. Its tail from a proper set is at most |S|, hence the global
height is at most p-1.

This is a complete all-prime recurrent-set proof, but only elementary
degree descent. Derivatives of split finite-field polynomials need not
split in the same field; no real Rolle theorem is imported. A finite
p=11 source mask 15 has orbit 15,672,9,128,0,2047,0,... and tail four.
No exact sharp height, every-target inverse or maximum-fibre theorem is
proved. Disposition: KILL_ELEMENTARY_CLOCK_ONLY.

## IDR — retain intervals with an incomparable pair

Assumptions: P is a strict transitive relation on a finite n-element set.
The tested encoding uses a natural linear extension as the labels.
F(P) contains (x,z) when xPz and there are incomparable u,v with
xPuPz and xPvPz. Incomparability is always evaluated in the input relation
of the current step, not frozen at time zero.

F(P) is irreflexive. If xF(P)y and yF(P)z, any incomparable pair witnessing
the first membership remains inside the old interval (x,z), by
transitivity of P. Hence xF(P)z and the map is closed on strict posets.

Each retained pair has an intermediate vertex, so F(P) is contained in
the relational square P^2. Inductively,

    F^t(P) is contained in P^(2^t),

because F(R) is contained in R^2 for every input poset R and relational
composition preserves containment. A strict poset on n vertices has no
path of n edges, so F^t(P) is empty once 2^t>=n. For n>=1 this gives
height at most ceil(log_2 n); for n=0 the sole state is already empty.
The empty relation is the sole recurrent state.

This proves an upper bound, not a sharp law or equality with squaring.
For example, a chain can have P^2 nonempty but every interval lacks an
incomparable pair, so F(P) is empty. Possible changes of incomparability
under deletion do not invalidate the containment proof; it reapplies to
each new poset. No complete inverse/fibre formula was established.
Disposition: KILL_RELATIONAL_POWER_BOUND_ONLY.

## UEX — exactly-one Johnson neighbour

For k=2, identify the old family with a simple graph G on [n], let A_uv
indicate an edge and d_u be the old degree. The number of old edges
sharing exactly one endpoint with {u,v} is d_u+d_v-2A_uv. Consequently,

    A'_uv = 1 iff d_u+d_v-2A_uv=1.

New nonedges can only join old degrees 0 and 1. Retained old edges must
join degrees 1 and 2. This is an exact useful coordinate identity, but
specifying a target still leaves a coupled degree/adjacency constraint
problem; no product inverse or all-n orbit atlas follows.

For every n>=5, a star with n-2 leaves and one isolated vertex maps to
the star on the same leaves whose centre is the old isolate, leaving the
old centre isolated. Here the centre degree is at least 3, so no old
star edge survives, and exactly the degree-0/degree-1 pairs appear.
The second step restores the original star, giving a strict two-cycle.
This family does not classify all recurrent graphs. Ground-set
complement on k-sets gives an exact conjugacy between parameters k and
n-k; those are not distinct mechanisms. k=0,n are constant empty-family
maps, and k=1,n-1 have the elementary complete-graph neighbourhood rule.
Disposition: KILL_NO_TWO_AXIS_ROUTE.

## CCS — all-triples circumcentre set

Assumptions: p is odd and the quadratic form is x_1^2+x_2^2 on F_p^2.
For a noncollinear triple a,b,c the centre z is uniquely defined by

    2(b-a) dot z = ||b||^2-||a||^2,
    2(c-a) dot z = ||c||^2-||a||^2.

The determinant is nonzero precisely by noncollinearity and odd
characteristic. Therefore F(S) is empty exactly when S contains no
noncollinear triple, equivalently S is collinear (including sets of
size at most two). Every subset of size at least two on a line determines
that line uniquely. There are p(p+1) affine lines, giving the exact
zero-fibre count

    1+p^2+p(p+1)(2^p-p-1).

This is an elementary static affine-line count, not a new all-target
fibre mechanism. In the p=3 finite pilot it is 58, whereas the largest
fibre is 130 at the full target. No extremality of the empty fibre is
asserted. No all-prime orbit theorem was established. Disposition:
KILL_STATIC_ZERO_FIBRE_ONLY.

## SEN — local-sensitivity-one indicator

Let E_i translate a Boolean truth function by the i-th cube coordinate,
and let C complement its output. Local sensitivities of f and C(f) are
identical, so F(C(f))=F(f), in every dimension. This is paired-source
invariance, not complement conjugacy.

At d=0 the map is constant zero. Over F_2 at d=1, F=I+E_1 and F^2=0.
At d=2 the exactly-one condition is parity for a two-bit list, hence
F=E_1+E_2 and F^2=0. For d>=3, exactly one is not odd parity, and this
linear reduction cannot be imported.

In d=4, encoding f(x) at bit x for x=0,...,15, direct substitution gives
the distinct four-cycle

    27 -> 7104 -> 39 -> 10176 -> 27.

For any d>4 extend each function independently of the added coordinates.
The added sensitivity terms are zero, so this embedding commutes with F.
Thus strict four-cycles exist for every d>=4. It disproves any universal
two-cycle-only guess. It is not a complete periodic atlas, a sharp
transient statement or an inverse theorem. Disposition:
KILL_NO_TWO_AXIS_ROUTE.

## Check boundary

The final finite verifier tests map closure, complete forward graphs,
tails, periods and indegrees in its stated boxes; additionally it tests
the DPF full-fibre formula and fixed census, CRS disjointness/strict
shrinkage, UEX's k=2 degree formula, SEN output-complement invariance and
IDR's recurrence/upper bound. The explicit CCS empty-fibre count and
listed short cycle witnesses were separately checked in the same boxes.
Nothing here claims a process-separated review or novelty certification.
