# CRC: cyclic strict-record count feedback — author proof spike

2026-09-05 UTC; root. Status: temporal proof complete / inverse structure
under inspection / NOT ADMITTED. No independent value review or paper ID.

## Literal map and proved temporal part

For n≥1 and q≥n use [q]^n, with indices modulo n and [q]={1,…,q}.
R(w)_i is the number of strict left-to-right records in
w_i,w_(i+1),…,w_(i+n-1). The initial letter is always a record. This is
synchronous recomputation, not rotation of w. R(w)_i≤n≤q gives closure.

Let D_n be the integer words b with min b=1 and b_i−b_(i+1)≤1 at every
cyclic edge. These inequalities already imply max b≤n. Let C_n⊆D_n
add the opposite inequalities, so all cyclic differences are −1,0,1.

**Temporal theorem.** R([q]^n)=D_n, R²([q]^n)=C_n, and on C_n,
R(c)=(max c+1)·1−c. Consequently R⁴=R², C_n is the exact recurrent
set, and its only fixed point is 1^n. All other recurrent orbits have
period two. The sharp maximum tail is zero for n=q=1, one for n≤2
and q>1, and two for n≥3. The first-image size is binom(2n−1,n−1),
and the recurrent size is the central trinomial coefficient

    [z^0](z^(-1)+1+z)^n = sum_(j=0)^floor(n/2) n!/(j!²(n−2j)!).

Proof. If b=R(w), precisely the positions of the global maximum of w
have b_i=1. The records in the scan starting at i, except its first
letter, form a subset of those in the scan starting at i+1. Thus
b_i≤b_(i+1)+1. More explicitly, discard the final w_i in the latter
scan: if it were a new maximum then w_i is the global maximum and
b_i=1; otherwise this deletion changes nothing. This establishes D_n.

Conversely take b∈D_n and set w_i=n+1−b_i. Its cyclic upward steps
are at most one and its maximum is n. A scan starting at w_i must
visit every integer level w_i,…,n, and there can be no other strict
record values. It therefore has n−w_i+1=b_i records, proving exact
first-image surjectivity, with a source in [n]^n⊆[q]^n.

For b∈D_n put c=R(b). We already know c_i≤c_(i+1)+1. To obtain the
reverse bound, compare a=b_i and b_(i+1). If a is smaller than the next
letter, the next position is the first new record, so c_i=c_(i+1)+1.
If equal, c_i=c_(i+1). If a is larger, the unit-downstep condition
forces b_(i+1)=a−1. The scan from i+1 can then acquire at most one
extra record value, namely a, before the records strictly greater than
a shared by both scans. Hence c_(i+1)−c_i is zero or one. This also
covers a being a global maximum: the extra a appears by the final
position at latest. Thus c∈C_n.

On C_n every upward step is at most one. Starting at c_i and scanning
to M=max c visits every integer level through M, so R(c)_i=M+1−c_i.
This reflection again has minimum one and maximum M, and is an
involution. Every c is consequently its own two-step predecessor.
The claimed second image, recurrence and power identity follow.
Reflection fixes a word only if all its coordinates are equal; its
minimum then makes it 1^n.

For n=1, every input maps to 1, giving the stated q boundary. For n=2,
D_2=C_2, and 2^2 is outside the core when q≥2, proving height one.
For n≥3 take w=1^(n−2)23. Its first image is 3^(n−2)21, whose cyclic
edge from the final 1 to the initial 3 is not a unit step. It is not
recurrent, so its source has tail two.

For counting, the differences d_i=b_(i+1)−b_i of a D_n word satisfy
d_i≥−1 and sum d_i=0. Conversely such a difference word has a unique
height representative with minimum one. Thus k_i=d_i+1 are precisely
weak compositions of n into n labelled slots, counted by
binom(2n−1,n−1). On C_n the differences lie in {−1,0,1}; choosing equal
numbers j of positive and negative steps gives the displayed trinomial
count. These are classical stars-and-bars and bridge counts, not separate
new counting primitives. QED.

## A proposed exact one-step inverse structure (not yet independently checked)

For b∈D_n its roots are the positions b_i=1. For a nonroot i let p(i)
be the first cyclic position to its right with b_p<b_i; by the unit-drop
property it has b_p=b_i−1. These parent pointers define an ordered forest
of next-greater predecessors, each component ending at its root in cyclic
left-to-right order. Children are ordered by their occurrence before their
parent. For a proposed source w, the proposed equivalent conditions are:

1. all roots have a common value M;
2. each nonroot has strictly smaller value than its parent;
3. the values of the ordered children of any vertex are weakly decreasing.

Necessity route: when R(w)=b, the actual first strictly larger letter
after i has exactly one fewer record, and every intervening position has
at least b_i records. Therefore it is p(i). Siblings farther to the right
cannot exceed an earlier sibling, as that would intervene before the
earlier sibling's claimed first-larger parent. Roots must be global maxima.

Sufficiency route to check carefully: the depth parent forest decomposes
into contiguous postorder subtrees. Between i and p(i) are exactly later
sibling subtrees. Their roots are at most w_i and all their descendants
are smaller than those roots. Thus no intervening vertex is larger than
w_i, while p(i) is; p(i) is its first-larger successor. Repeated parents
give b_i records ending at a maximum-valued root.

If this equivalence survives a separate check, define for each vertex i
and each positive integer s the number Q_i(s) of subtree labellings with
w_i=s. A leaf has Q_i(s)=1, and for children c_1,…,c_k,

    Q_i(s)=sum_(s>a_1≥…≥a_k≥1) product_j Q_(c_j)(a_j).

The proposed every-target fibre is sum_(M=1)^q product_roots Q_i(M),
zero outside D_n. This is an evaluated finite recursive decoder, not a
claimed new order-polynomial theory or efficient general counting result.
Classical Cartesian/plane-tree and P-partition adapters must be located
before treating it as an independent value axis. No maximum-fibre or
every-time-fibre theorem is proved here.

## Evidence and value boundary

The six-rule `circular_statistics_pilot.py` and full
`CIRCULAR_STATS_CANONICAL.jsonl` exhaust [n]^n through n=6. For CRC they
give image sizes 1,3,10,35,126,462 and recurrent sizes 1,3,7,19,51,141.
These finite numbers motivated, but do not prove, the deductions above.
No standalone CRC theorem verifier or source gate has yet been completed.

Internal full-text searches found no literal cyclic-record feedback match;
they did find occupied record/prefix families and ordinary Motzkin-height
erosion. Those are not an ownership certificate in either direction.
The CCS pilot is exactly the permanently killed equal-cardinality merger
after quotienting equality blocks and will not be pursued. CRC is not
admitted merely because its temporal proof closes or its first image has
a classical closed count. The inverse route and exact owner subtraction
remain necessary; bounded search nonhits receive zero novelty credit.
