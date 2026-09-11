# Closed pointer reversal: self-contained proof package

Status: P212 SOURCE_PREP_ONLY. This is a paper-local author proof, not an
independent manuscript verdict or a scientific execution report. It restates
and organizes the accepted underlying deductions without changing their
literal carrier, credit boundary, or finite cutoff. Exactly two axes are
retained: exact periods; labelled orbit decorations and census.

## 1. Model, conventions and elementary background

For an integer n≥1, V=[n], let X_n=V×V×V^V and

R(u,v,f)=(v,f(v),f[v:=u]).

All values on the right are old values. In f[v:=u] only the entry at v is
replaced. Registers are ordered, u=v is allowed, and f is arbitrary and total.
There is no nil, stopping predicate, clock, scheduler, distinguished edge
identity or quotient of vertex labels. The carrier has n^(n+2) states.

Given a target (a,b,g), its unique predecessor is
(g(a),a,g[a:=b]). In the update a=v, b=f(v), and g(a)=u, so substitution
recovers both registers and every pointer, including a=b. Conversely that
predecessor maps to (a,b,g). Thus R is a permutation, with preperiod zero and
one immediate predecessor at every state. Fixed states satisfy u=v=f(v):
there are n choices of v and n^(n−1) choices elsewhere, hence n^n in total.
These are background facts, not either retained theorem axis.

## 2. Augmented graph and frozen-complement reduction

Associate one undirected edge {x,f(x)} to each vertex and one extra edge
{u,v}. Preserve edge multiplicities but not edge identities. A loop is one
edge and contributes degree two. Draw the stored edges as x→f(x), and the
extra edge as u→v; consequently u has two outgoing arrows and every other
vertex has one. R changes the extra/stored roles of {u,v} and {v,f(v)} and
reverses the old extra arrow. The undirected multigraph G is invariant.

Every component of a functional digraph has as many undirected edges as
vertices, also for loops and parallel edges. If u,v begin in the same
functional component, their extra edge adds one edge to it. If they begin
in different components, it joins two such components. In either case the
active component has one more edge than vertices. All other components are
functional components and never contain a register.

Repeatedly prune degree-one vertices of the active component. Such a vertex
cannot be active u, which has two outgoing arrows. Its unique incident edge
is its stored outgoing arrow, directed into the remaining graph. Removing
it removes no outgoing arrow of a remaining vertex. Inductively u survives,
the extra edge survives, and v survives. All removed edges are directed
toward the residual two-core K. This applies at every time because G is
invariant, so no register ever reaches a deleted vertex. Its stored arrow
is never overwritten. The arrows in all inactive functional components are
also frozen. Leaf pruning keeps edge excess unchanged, so K has s vertices,
s+1 edges and minimum degree two. It is connected and nonempty.

Let S be its labels. The restriction f|S together with (u,v) is a core state;
f(S)⊆S, and the full frozen complement is the actual map
g:V\S→V, not merely an isomorphism type or number of trees. Both S and g
are uniquely recovered from every state and are invariant along its orbit.
The augmented-edge invariant and pruning are shared background mechanisms,
not an independent third axis.

## 3. Core classification and forced chains

For K, Σ_x(deg(x)−2)=2. Thus there is one vertex of degree four or two
vertices of degree three, all others having degree two. Maximal chains
between branch incidences exhaust K. With a single degree-four branch,
they pair into two closed chains: a figure-eight with cycle lengths a,b≥1
and s=a+b−1. With two degree-three branches, there are either three joining
chains (theta), or one joining chain and a closed chain at each endpoint
(barbell). In each case with lengths a,b,c≥1, s=a+b+c−1. These exhaust
connected cores. A length-one cycle is a loop and a length-two cycle has
two indistinguishable parallel edges. Multiple direct theta paths also
have no separate state identities.

At an internal degree-two vertex, arrival along the extra edge makes the
old stored arrow the next extra arrow and stores the reversed incoming
edge. Its single remaining outgoing choice is forced. Induction traverses
each maximal chain and reverses every stored arrow along it. At a branch,
the next extra edge is likewise its old stored arrow. The outdegree
conditions determine chain directions once the branch roles are specified;
there is no additional cycle or independent direction inside an open chain.
If the active vertex is internal, its chosen extra direction reaches a
branch. These facts establish reachability of the anchors below.

Let O(C) be the observable orientation set of a rooted labelled cycle C.
It has size one at lengths 1 and 2: reversing a loop changes nothing, and
both arrows on a length-two cycle still point to the same opposite vertex.
It has size two at length ≥3, since a branch departure then selects one of
two different neighbours. Reversal is an involution on O(C), trivial
exactly for lengths 1 and 2.

## 4. Figure-eight: minimal period and orbit classes

When both cycles are loops, K has one vertex and a single core state, fixed
by R. Otherwise the cycles are distinguishable by their labelled internal
sets, except that one may be the unique loop. Choose one as C1 and name
the other C2. Anchor at active branch A with extra arrow beginning C1;
the stored arrow at A must begin C2. There is exactly one anchor state
for each pair in O(C1)×O(C2). Forced traversals follow
C1,C2,C1 reversed,C2 reversed.

After h=a+b steps the prescribed-cycle anchor returns with both observable
orientations reversed. If a,b≤2, reversal is invisible. No earlier return
is possible: departures at A alternate between the cycles, whose first
destinations differ unless both are loops. Consequently the non-double-loop
short case has exact period h.

If a cycle has length ≥3, choose an internal vertex z on it. Across the
full 2h traversal block, u=z occurs twice, once with each of its two distinct
neighbours as v. Therefore a specified ordered pair (z,chosen neighbour)
occurs once in that block. If the actual orbit had shorter period, the
same pair would recur more often in the repeated state sequence, a
contradiction. The exact period is 2h at every phase of that orbit.

Every state reaches a branch, and the alternating branch choices reach
the chosen C1 anchor. On the complete set of anchors, equivalence under
R is exactly the equivalence generated by joint reversal (α,β)↦(−α,−β).
It has two classes if both cycles have length ≥3, one class otherwise.
This proves both orbit existence and exhaustion without dividing a state
total by a presumed period.

## 5. Barbell: minimal period and orbit classes

Choose the smaller-labelled branch A, the other B, and anchor at the
extra bridge departure from A toward B. The bridge is directed toward B,
and each branch stores the outgoing edge of its own cycle. Indeed the
B-cycle supplies B's one stored outgoing edge, forcing the bridge toward
B; at A the extra bridge arrow leaves one stored outgoing edge for its
own cycle. There is exactly one anchor for each pair of observable cycle
orientations, with no remaining bridge choice.

The forced macro-block consists of A-to-B bridge, B-cycle, B-to-A bridge,
A-cycle. Its length h=a+b+2c restores the bridge anchor and reverses both
cycles. The ordered bridge departure at A occurs only at these block
boundaries: the bridge neighbour is distinct from every neighbour on
A's own cycle, also for loops and double-edge cycles. Thus when a,b≤2
the exact period is h; otherwise it is 2h. Joint reversal gives two
classes if both a,b≥3 and one otherwise. An active state on a cycle
reaches its branch then the bridge; an active state on the bridge reaches
a branch then its cycle, and the forced blocks reach the chosen anchor.
All states have therefore been accounted for.

## 6. Theta: minimal period and the unlabelled-direct-path quotient

Distinguish the three maximal chains temporarily for this proof, not in
the state space. At an active branch their roles are extra outgoing i,
stored outgoing j, and incoming k. Traverse i. At the other branch the
old stored outgoing chain was k, and the reversed incoming chain i is now
stored, so the role triple becomes (k,i,j). Six traversals use
i,k,j,i,k,j, traversing every chain in both directions. They restore the
state in 2(a+b+c) steps.

If a chain has an internal vertex z, the full block contains exactly one
occurrence of (u=z,v=one specified neighbour). Hence the period is the
full block length, even if the remaining two paths are identical direct
edges. If all paths are direct, forgetting the artificial edge identities
leaves f(A)=B,f(B)=A and the two register states (A,B),(B,A). R swaps them,
so the exact period is two, not six.

At a prescribed branch, two traversals rotate the role triple cyclically.
Three distinguishable chains therefore have exactly two cyclic orders.
Only direct chains may coincide, because each nondirect chain has a
disjoint nonempty labelled internal set. If at least two paths are direct,
the two orders become one cyclic order of a multiset. Otherwise they
remain distinct. The role assignment determines all arrows and the
registers of an anchor state, and each internal starting state reaches
a branch. Thus these classes give all and only the R-orbits.

The resulting complete table, for a fixed labelled K and fixed g, is:

| Shape / parameter condition | Exact period | Number of orbits |
|---|---:|---:|
| Figure-eight a=b=1 | 1 | 1 |
| Figure-eight a,b≤2, not both 1 | a+b | 1 |
| Figure-eight max(a,b)≥3 | 2(a+b) | 2 if both ≥3, otherwise 1 |
| Barbell a,b≤2 | a+b+2c | 1 |
| Barbell max(a,b)≥3 | 2(a+b+2c) | 2 if both ≥3, otherwise 1 |
| Theta a=b=c=1 | 2 | 1 |
| Any other theta | 2(a+b+c) | 1 if at least two paths direct; otherwise 2 |

## 7. Complete attained period set and sharpness

For n=1 the sole state is fixed. For n≥2 the period set is
{1,…,2n} ∪ {2n+2,2n+4,…,4n−4}, empty ranges understood.

Upper bounds: let s≤n be core size. Odd periods beyond one arise only
in short-cycle rows. The short figure-eight has period 3 or 4, while a
short barbell has p=a+b+2c=2s+2−(a+b)≤2s; an odd value requires a+b=3
and is 2s−1. The triple-direct theta has period 2. The nonshort
figure-eight and nontrivial theta have even p=2s+2≤4n−4 for s≥3.
For a nonshort barbell a+b≥4, so
p=4s+4−2(a+b)≤4s−4≤4n−4. The n=2 rows give only 1,2,3,4.

Attainment: 1 is a double loop, 2 a triple-direct theta, 3 a figure-eight
with lengths (1,2). A barbell (1,1,k−1), 2≤k≤n, uses k vertices and
gives 2k. A barbell (1,2,k−1), 2≤k≤n−1, uses k+1 vertices and gives
2k+1. These realize all integers through 2n. Theta (1,1,s−1), 3≤s≤n,
has half-period s+1, covering 4,…,n+1.

For every 6≤k≤2n−2, set c=max(1,k−n−1), r=k−2c. If k≤n+2 then
c=1, r=k−2≥4 and s=r+c−1=k−2≤n. Otherwise c=k−n−1, s=n and
r=2n+2−k≥4. The nonshort barbell (1,r−1,c) has period 2k.
These constructions cover any even value missing from the earlier
intervals (for n=2,3,4 the directly stated cases already exhaust the
set). Pad unused labels with inactive fixed loops. A sharp witness is
the two-loop barbell at n=2, theta (1,1,2) at n=3, and barbell
(1,3,n−3) for n≥4.

This is retained axis 1. The cycle and path counting required below is
additional information, although it uses the same anchors.

## 8. Labelled orbit-decoration weights

On a fixed s-element label set count all admissible core multigraphs and
their orbit classes. Divide the period-p count by s! and call it c_(s,p).
Let C(t,q)=Σ c_(s,p)t^s q^p. These are EGF coefficients and need not be
integers. Labels remain distinct throughout. A sequence of ℓ distinct
internal labels has EGF weight t^ℓ.

A rooted undirected cycle of length a has weight u_a t^(a−1), where
u_1=u_2=1 and u_a=1/2 for a≥3. The factor one half comes from reversing
an ordered list of at least two distinct internal labels; it is not
valid for the empty or singleton list. Multiplying by the proven number
of diagonal-reversal classes for a pair of cycles gives

u_a u_b(1+1_{a,b≥3}) = 1 if a,b≤2, and 1/2 otherwise.

This combines a symmetry of core presentations with the actual orbit
decoration count. It does not claim that the core orientations are
newly discovered counting operations.

## 9. Three rational bivariate pieces

Set x=tq², Q=x/(1−x), D=(1−x)^(−2)−(1+x)². We prove

C8(t,q)=tq+t²q³+(1/2)t³q⁴+(1/4)tq⁴D,

CB(t,q)=t²q⁴(1+tq)²/[2(1−tq²)] + t²q⁸D/[4(1−tq⁴)],

CTheta(t,q)=(1/2)t²q²+(1/2)t²q⁶(Q+Q²+Q³/3),

and C=C8+CB+CTheta.

For C8, the shared root contributes t. Interchanging two cycles acts
freely on labelled presentations unless both are loops; hence divide
by two outside that exception. The double loop contributes tq directly.
The short ordered pairs (1,2),(2,1),(2,2) give t²q³+t³q⁴/2. For the
other ordered length pairs, the combined cycle/decoration/interchange
weight is 1/4. Writing i=a−1,j=b−1 gives

(1/4) Σ_{max(a,b)≥3} t^(a+b−1)q^(2a+2b)
 = (1/4)tq⁴[Σ_{i,j≥0}x^(i+j)−(1+x)²] = (1/4)tq⁴D.

For CB, the two branch labels are distinct, so interchange of endpoints
acts freely, with factor 1/2 even if the cycle lengths coincide. The
bridge contributes c−1 ordered internal labels. For short cycles the
sum (1/2)Σ_{a,b≤2,c≥1}t^(a+b+c−1)q^(a+b+2c) factors as the first
displayed CB term. For nonshort pairs the combined factor is 1/4,
and their period is 2a+2b+4c. Summing positive c gives the second term.
This includes all loop and double-edge cases without labelled edge IDs.

For CTheta, an unordered pair of distinct branch labels contributes
t²/2. Fix either label-induced ordering of the endpoints to describe
internal path lists. A nondirect path with ℓ≥1 internal vertices has
weight (tq²)^ℓ; summing gives Q. If all three paths are direct, add
period weight q², not q⁶. Otherwise choose k=1,2,3 nondirect paths.
Their disjoint nonempty labelled sets make their unordered collection
contribute Q^k/k!, with decoration multipliers respectively 1,2,2.
Every traversal has the additional period contribution q⁶ from the
three path lengths before their internal vertices are counted. Thus
the terms are Q,Q²,Q³/3, each multiplied by t²q⁶/2. Direct paths are
identical and require no fictitious path-label factorial. This proves
all three rational expressions constructively.

## 10. Arbitrary frozen-complement bijection

Choose S⊆[n] with |S|=s, a labelled core and one of its orbit decorations,
then any total map g:[n]\S→[n]. There are n^(n−s) such maps. Each point
outside S either eventually enters S under g or eventually joins a
functional cycle wholly outside S. In the first case its component
adds an inward directed tree to the core; in the second it is inactive.
An outside directed cycle cannot also have a forward path into S.
Hence the core remains exactly S, and the registers never leave it.
The added pointers do not affect the core orbit and stay fixed.

Conversely the invariant graph of any full state uniquely recovers S
by active-component pruning, and recovers the actual g as its unchanged
outside pointers. Restricting the state to S recovers precisely one
core orbit decoration from §§4–6. These operations are inverses on
orbits. Thus, with (n)_s=n!/(n−s)!,

o(n,p)=Σ_{s=1}^n (n)_s n^(n−s)[t^s q^p]C(t,q).

This is retained axis 2 together with the rational evaluation. It is
not a quotient of the full carrier size by a common period. For example,
on five fixed labels a figure-eight (1,5) and a figure-eight (3,3) have
the same period 12 but respectively one and two decorations on each
fixed core and fixed complement. Scalar timing does not contain that
distinction. The two axes share the branch-return structure and are
not asserted to be logically independent theories.

## 11. Explicit total count

Set q=1, U=1+t+t²/[2(1−t)], W=t²/[2(1−t)] and Q=t/(1−t). The rooted
cycle construction gives

C8=t(U²+W²+1)/2,
CB=t²(U²+W²)/[2(1−t)],
CTheta=t²(1+Q+Q²+Q³/3)/2.

Putting these over the common denominator (1−t)³ and collecting the
numerator yields

C(t,1)=(t−t²+t⁴/2−t⁵/12)/(1−t)³.

Since [t^j](1−t)^(−3)=binom(j+2,2) for j≥0 and is zero for j<0,
the coefficient at t^s is
binom(s+1,2)−binom(s,2)+(1/2)binom(s−2,2)−(1/12)binom(s−3,2),
where the last two terms are set to zero until their generating-function
indices are nonnegative. This gives c1=1,c2=2,c3=3,c4=9/2. For s≥5
ordinary polynomial simplification gives (5s²+s+24)/24; that formula
also gives c3,c4. Thus c_s=(5s²+s+24)/24 for all s≥3, and

o(n)=Σ_{s=1}^n (n)_s n^(n−s)c_s.

Fractions among c_s are normal EGF normalization, not fractional orbit
counts. The extension sum itself is integral by the proved bijection.

## 12. Zero-credit consistency consequences and finite limits

The q¹ coefficient of C is t, giving n^n fixed states under the extension
formula, consistent with §1. Formal differentiation of the three pieces
and setting q=1 gives

[q∂_q C(t,q)]_(q=1)=t(1+2t)/(1−t)^4
 = Σ_{s≥1}[s²(s+1)/2]t^s.

The extension of this period-weighted count is n^(n+2), because the
proved orbit partition assigns every full state exactly once. For k≥1,
|Fix(R^k)|=Σ_{p|k}p o(n,p), the standard finite-permutation consequence.
These are consistency checks, not a third theorem axis.

Small formal coefficient controls, derived from §9, are

[t]C=q;
[t²]C=q²/2+q³+q⁴/2;
[t³]C=q⁴/2+q⁵+q⁶/2+q⁸;
[t⁴]C=q⁶/2+q⁷+q⁸/2+2q¹⁰+q¹²/2.

They are prospective verifier controls, not new execution output.
The inherited accepted candidate pilot covered only n=1,2,3,4, all
4,356 states with 50,392 saved candidate checks. It is neither a
paper canonical nor a strict author pair. This source package has not
executed its verifier or compiled a paper. The first two-long-cycle
figure-eight needs s=5, two-long-cycle barbell s=6, and theta with all
three paths nondirect s=5. Their proof is §§4–6 and §9, never the
n≤4 experiment. No cutoff increase is proposed or authorized.
