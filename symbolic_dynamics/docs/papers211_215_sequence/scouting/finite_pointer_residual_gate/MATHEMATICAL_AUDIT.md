# Deductive audit of the exact candidate

This document audits the sealed PROOF_PACKAGE.md, not a modified theorem.
All arithmetic below is hand algebra, not an executed enumerator or a
literal-state pilot. No implementation was imported.

## 1. Carrier, reversibility and invariant

The target (a,b,g) determines the old state uniquely as
(g(a),a,g[a:=b]). Substitution in both orders restores every coordinate,
including a=b and self-loops. Hence the full state map is a permutation.
This part was already in the old negative desk and contributes no new axis.

Represent each stored arrow and the ordered register edge as an undirected
multiset edge, without edge identities. At a tick, one stored edge trades its
role with the register edge, preserving multiplicities even when endpoints
coincide. A functional component has equally many vertices and edges.
The register edge either adds an edge within one such component or joins
two such components. The active component therefore has E=V+1 in either
case; every other component is untouched.

The degree-one pruning argument is valid. In the current active orientation,
u has two outgoing edges counting the extra edge, while every other vertex
has one. A leaf cannot be u; its only edge is its stored outgoing edge
toward the remaining graph. Removing that leaf removes no remaining vertex's
outgoing edge, so the argument iterates. If the register edge were removed,
its tail u would have to be removed, which is impossible. Thus both
registers remain in the two-core throughout the orbit. The orientation on
every pruned tree and every inactive component is frozen.

This also handles an active u initially lying on what is a feeding path
for the original f: the extra edge can put that path into the augmented
core. One must not prune the original f-component before adding the extra
edge.

In the nonempty connected core, minimum degree is two and
sum(deg-2)=2. Thus there is one degree-four vertex or two degree-three
vertices. Following maximal degree-two chains gives precisely a figure-eight,
barbell or theta, with loops and repeated direct edges allowed. The graph
classification is complete; no simple-graph assumption is being used.

## 2. Forced chains, anchors and exact periods

At an internal chain vertex, the arriving extra edge and its unique stored
outgoing edge force the next move. The old incoming edge is stored reversed.
A selected chain is therefore followed to a branch while reversing. There
is no internal vertex at which an extra choice or hidden cyclic order can
be made. Every state reaches a branch anchor.

A rooted cycle of length one or two has one observable orientation. A loop
stores its own vertex; on a two-cycle each nonbranch destination is the
opposite endpoint, irrespective of a temporary name for its parallel edge.
For length at least three, orientation reversal changes a nonbranch
vertex's destination and produces two distinct orientations.

For a figure-eight, choose the shared branch and one specified cycle.
An anchor departs into that cycle; the other cycle carries the branch's
stored arrow. Two successive complete cycle traversals restore this
departure anchor and reverse both cycle orientations. The block takes
a+b ticks. It is a return if both orientations are invisible; otherwise
two blocks are needed. The prescribed cycle departure at the branch
cannot recur halfway between these blocks unless both cycles are loops.
That exceptional core has just one state. When a cycle is long, either
ordered departure from a nonbranch vertex occurs exactly once in the
four-traversal block, ruling out every shorter period.

For a barbell, choose the smaller-labelled branch as A and an anchor
departing along the bridge toward B. Its four macro traversals are bridge,
B-cycle, reverse bridge, A-cycle. They take h=a+b+2c ticks and jointly
reverse the cycles while restoring the bridge anchor. The same departure
from A along the bridge occurs only at macro-block boundaries. Thus the
minimum is h when both reversals are invisible and 2h otherwise. The
bridge neighbour and the cycle neighbour at A are distinct even for loops
or two-edge cycles; no hidden shorter anchor occurs.

For a theta, temporarily name the three chains. At an active branch the
outgoing extra, outgoing stored and incoming chains have roles (i,j,k).
After traversing i the roles at the opposite branch are (k,i,j).
Branch parity and this three-cycle give six traversals i,k,j,i,k,j and
2(a+b+c) ticks. If any chain is nondirect, an ordered departure from one
of its internal vertices appears once in this whole block, proving
minimality after edge identities are forgotten. If all chains are direct,
the temporary names are not states: only the two opposite ordered
register pairs remain, so the actual period is two.

These arguments establish exactly the seven table rows in the dossier.
They do not merely show that the stated periods are upper bounds.

## 3. Orbit multiplicities on each fixed labelled core

At the prescribed-cycle figure-eight anchor or directed-bridge barbell
anchor, the full configuration is specified by one observable orientation
per cycle. Successive returns to the anchor generate simultaneous reversal.
The quotient of their one- or two-element orientation sets has two
classes exactly when both cycles are long; otherwise it has one.
Every state reaches such an anchor, and the anchor contains no unspecified
stored pointer, so this counts all orbits without overcounting phases.

At a fixed theta branch, the three chain roles are identified by cyclic
rotation after an even number of chain traversals. Three distinguishable
chains have two cyclic orders. Only empty direct paths can coincide:
nondirect paths have disjoint, nonempty sets of fixed vertex labels.
With at least two direct paths, forgetting their temporary identities
merges the two cyclic orders. Thus there is one orbit in that case and
two otherwise. In the triple-direct case the actual phase length is
already two, as above.

This is genuine orbit-class information. It is not supplied by bijectivity,
nor by the statement of a period alone. The scalar period of the
figure-eights (a,b)=(1,5) and (3,3) is 12 on five core vertices in each case,
but their fixed-core orbit counts differ, one versus two.

## 4. Period set and maximum

Let s be core size. Short-cycle figure-eights and the triple-direct theta
supply only 1,2,3,4. A short-cycle barbell has
p=2s+2-(a+b)<=2s; when odd, a+b=3 and p=2s-1.
Every remaining period is even.

A nonshort figure-eight or theta has s>=3 and p=2s+2<=4n-4.
A nonshort barbell has a+b>=4 and
p=4s+4-2(a+b)<=4s-4<=4n-4.
The n=2 rows must be treated separately: they give 1,2,3,4, hence the
maximum 4=4n-4. The n=1 sole state is fixed.

Attainment is complete, including the small empty ranges. Periods one,
two and three have the cores specified in the dossier. Two loops joined
by a bridge of length k-1 give every even 2k for 2<=k<=n.
A loop and a two-edge cycle joined by such a bridge give every odd
2k+1 for 2<=k<=n-1. The length-(s-1) theta path together with two direct
paths gives half-periods 4 through n+1 on s=3,...,n.

For the remaining half-period k with 6<=k<=2n-2, the author's
c=max(1,k-n-1), r=k-2c obeys c>=1, r>=4 and s=r+c-1<=n:
if k<=n+2 then c=1 and s=k-2<=n; otherwise s=n and
r=2n+2-k>=4. Cycles (1,r-1) and bridge c supply period 2k.
For n>=4 this overlaps the theta interval without a missing half-period;
n=2,3 were already explicit. Padding by inactive loops does not change
a state period. Thus the exact set is
{1,...,2n} union {2n+2,2n+4,...,4n-4} for n>=2.

This also checks the sharp witnesses: a three-vertex theta at n=3;
cycles (1,3) with bridge n-3 at n>=4; and the two-loop barbell at n=2.

## 5. Direct audit of the bivariate series

The exponent of t is core size and q marks the actual, unquotiented
state period. All coefficients are labelled counts divided by s!.

A rooted undirected a-cycle has list weight 1 for a=1,2 and 1/2 for
a>=3. Multiplying the two cycle weights by the independently established
number of orbit decorations gives weight 1 for two short cycles and
1/2 for every other pair. In particular the factor two when both cycles
are long is essential: omitting it is an orbit-count error, despite
leaving the period formula unchanged.

For a figure-eight, interchange of the two rooted cycles is free on
labelled structures except the pair of empty loops. Therefore the loop
exception is tq and the other short pairs are t^2 q^3+t^3 q^4/2.
Put x=tq^2 and D=(1-x)^(-2)-(1+x)^2. Ordered nonshort pairs then give
tq^4 D/4. This is exactly the author's C_8.

For a barbell, interchange of the two distinct branch labels is free.
The c-1 internal bridge labels form an ordered list. Short cycles give
t^2 q^4(1+tq)^2/[2(1-tq^2)], since every additional bridge vertex adds
two ticks to the short period. Nonshort cycles have period
2a+2b+4c and coefficient 1/4 for each ordered pair; their sum is
t^2 q^8 D/[4(1-tq^4)]. This matches C_B, including each loop or
double-edge endpoint case.

For a theta, choose an unordered pair of distinct labelled branches,
weight t^2/2, and orient each internal list from the smaller branch.
Write Q=x/(1-x). Three direct paths contribute t^2 q^2/2 directly.
For k=1,2,3 nondirect paths the unordered path factor is Q^k/k!,
while the orbit multipliers are 1,2,2. The common q^6 factor completes
the period marking. Hence the other term is
t^2 q^6(Q+Q^2+Q^3/3)/2, exactly C_Theta.
There is no erroneous division by 3! for indistinguishable empty paths.

## 6. Frozen complement and all-n evaluation

Given a core label set S and one core orbit, choose any map
g:[n]\S -> [n]. Every component of these complementary arrows either
eventually reaches S and is an inward forest, or has its own directed
cycle and is disjoint from S. It cannot add a cycle to the active core:
each outside vertex has a single forward destination, so an outside
cycle has no forward path into S. Thus attaching g preserves the chosen
core and never changes its pointers.

Conversely pruning the invariant active component recovers S, and the
unchanged outside arrows recover g uniquely from every full orbit.
Different g values cannot be merged by time evolution. The extension
multiplicity is exactly n^(n-s), independent of p. Combining the label
choice with the core EGF gives
o_(n,p)=sum_(s=1)^n (n)_s n^(n-s)[t^s q^p]C(t,q).
No restriction to connected f or initially connected pointer components
has entered this argument.

At q=1 the three core series simplify to the rational expression
(t-t^2+t^4/2-t^5/12)/(1-t)^3. Coefficient extraction gives c_1=1,
c_2=2 and c_s=(5s^2+s+24)/24 for s>=3. For s>=5 this follows by
combining
binom(s+1,2)-binom(s,2)+binom(s-2,2)/2-binom(s-3,2)/12;
s=3,4 separately give 3 and 9/2. These are EGF coefficients,
so their being nonintegral is not a defect.

Fixed-iterate counts sum p o_(n,p) over p dividing the iterate. This
finite-permutation conversion is standard and gets no additional credit.

## 7. Hand coefficient controls and finite-coverage ceiling

Direct expansion of the audited rational series, not orbit execution,
gives the following core coefficients:

- [t]C=q.
- [t^2]C=q^2/2+q^3+q^4/2.
- [t^3]C=q^4/2+q^5+q^6/2+q^8.
- [t^4]C=q^6/2+q^7+q^8/2+2q^10+q^12/2.

Thus the all-carrier orbit polynomials predicted by the theorem are:

- n=1: q.
- n=2: 4q+q^2+2q^3+q^4.
- n=3: 27q+9q^2+18q^3+12q^4+6q^5+3q^6+6q^8.
- n=4: 256q+96q^2+192q^3+144q^4+96q^5+60q^6+24q^7
  +108q^8+48q^10+12q^12.

Their orbit totals are 1,8,81,1036. Multiplying each coefficient by
its exponent and summing gives 1,16,243,4096 respectively. These are
deductive expectations, not an independent finite test of R.
The q coefficient gives n^n fixed states, already known directly.

The proposed n<=4 literal pilot cannot exercise both-long-cycle
figure-eights or barbells, nor the all-nondirect theta class.
The all-parameter orientation arguments above cover those cases.
No larger computation is needed or authorized by this review; any
later finite report must state the limitation rather than claim every
row was observed.

