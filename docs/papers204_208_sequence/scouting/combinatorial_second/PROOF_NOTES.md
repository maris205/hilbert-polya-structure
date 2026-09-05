# Second combinatorial lane: proved fragments and exact boundaries

2026-09-05 UTC. Author: `batch197_fosp_gate`. These deductions are scouting
work, not independent review or admission. All carriers are finite and every
update is synchronous from the old state. Bounds and literal code are in
[the report](SCOUT_REPORT.md). No all-parameter conclusion is inferred from
the functional-graph census.

## PR — reverse a least predecessor

For every function f:[n]→[n], set T(f)(v)=min f⁻¹(v) if the predecessor set
is nonempty, and T(f)(v)=f(v) otherwise. Labels are 0,…,n−1 in the program.

Let E(f) be the set of unordered pairs {v,f(v)}, including singleton loops.
Every new arrow is either a reversed old arrow or an unchanged old arrow;
therefore E(Tf)⊆E(f). This proves finite eventual stabilization of the
underlying edge set, **not** stabilization of the arrow assignment.
The observed eventual periods 1 and 2 up to n=6 have not been proved for all
n. A putative reduction to a fixed least-neighbour walk was not established:
the entire function, its predecessor sets and potentially its edges evolve.
No general inverse or sharp height formula is claimed. Disposition:
`KILL_UNCLOSED_TEMPORAL_AND_INVERSE` for this intake; preserve the fragment.

## ZR — parallel cyclic 001→110

For n≥3, simultaneously replace every cyclic occurrence of 001 by 110.
Distinct occurrences are disjoint because 001 is unbordered. For n=1,2 the
literal map is the identity, not a repeated-index rewrite.

### Termination and fixed points

Each replacement raises the number of ones by one. Thus every nonfixed step
strictly increases it; a nonfixed word initially contains a one, so every
orbit reaches a fixed word in at most n−1 steps. A cyclic binary word with
a one and a pair 00 has a last pair of zeros immediately before the next
one, hence an occurrence 001. Consequently the fixed words are precisely
the all-zero word together with cyclic words avoiding 00. Their count is
L_n+1, where L_0=2,L_1=1,L_n=L_{n−1}+L_{n−2}: the 00-avoiding count is
the trace of the n-th power of [[0,1],[1,1]]. The same count agrees with the
two degenerate identity cases. There are no nontrivial recurrent cycles.

The census suggests sharp height floor(n/2) for n=3,…,14, but this stronger
bound remains **unproved**. We do not replace it by a guessed proof.

### Exact target fibres

For a target y and n≥3, let Q(y) be the cyclic start positions of 110 and
P(y) those of 001. Occurrences in either individual set are pairwise
disjoint. Every possible predecessor is obtained uniquely by choosing
J⊆Q(y) and reversing its selected 110 blocks to 001. Indeed each actual
forward rewrite leaves such a target block, and outside those blocks the
source equals the target. Distinct choices change different coordinates.

After a reversal at q the only newly created 001 occurrence is the intended
one at q. To verify this, the changed sites q,q+1,q+2 become 0,0,1; an
occurrence overlapping them and starting at q−2,q−1,q+1 or q+2 is blocked
by the indicated new 0 or 1. A pre-existing target occurrence at j is
destroyed precisely when a selected Q block starts at j−2 or j+2 modulo n.
These exhaust compatible overlaps of 001 and 110. This remains true in
n=3,4 by using sets of modular positions (coincident offsets are not counted
twice). Thus the exact fibre is

    |T⁻¹(y)| = #{J⊆Q(y): J∩({j−2,j+2}∩Q(y))≠∅ for every j∈P(y)}.

An empty constraint gives zero predecessors. This is a vertex-cover count
on the distance-four constraint graph, with possible singleton constraints;
no unproved path-product simplification is needed. If P(y) is empty every
subset is allowed. Since |Q(y)|≤floor(n/3), the maximum fibre is
2^floor(n/3), attained by y=(110)^k 1^r for n=3k+r. Equality holds exactly
when |Q(y)|=floor(n/3) and P(y)=∅: any nonempty constraint excludes the
empty selection, and fewer Q blocks give a strict smaller upper bound.
For n=1,2 every fibre has size one.

Complementation followed by coordinate reversal conjugates the literal rule
to cyclic parallel 011→100. This is the classical Fibonacci carry local
replacement, but is not the same whole algorithm as left-to-right linear
normalization. Only the common primitive and monotone digit-count proof
are deducted. The stronger time formula is not available. Disposition:
`NO_ADMISSION_OWNER_VALUE_AND_SHARP_CLOCK_HOLD`; the exact inverse fragment
is retained without promoting a paper or reserve.

## BS — balanced split followed by partition conjugation

For a partition λ of n, split each a into floor(a/2),ceil(a/2), discard
zeros, sort, and take ordinary Ferrers conjugation. Equivalently Tλ is the
sequence of column sums of its 2-modular diagram: a row for a=2j consists
of j entries 2, and for a=2j+1 consists of j entries 2 followed by 1.

Define C by replacing each pair of equal odd parts 2j+1 by 2j and 2j+2,
discarding zero parts. Do all pairs simultaneously; retain a single odd
part if its old multiplicity is odd. The replacement preserves every
2-modular column sum, so T=T C. The image of C consists of partitions
with no repeated odd parts. On this class a 1 is at the bottom of its
column, and modular diagram transposition is a genuine involution σ.
Also Tλ belongs to this class: writing c_a for old multiplicities, its
j-th part is 2·#{a≥2j}+c_(2j−1); whenever that part is odd, the positive
c_(2j−1) forces a strict decrease before the next part. Therefore

    T=σ C,     T²=C,     T³=T.

The first image and recurrent set are exactly the no-repeated-odd class;
height is at most one. This is an explicit adapter to an owned involution,
not a new temporal mechanism.

For completeness, the inverse is also elementary. If target μ repeats an
odd part its fibre is empty. Otherwise put λ=σμ=Tμ and let e_j be the
multiplicity of 2j in λ. A source in C⁻¹(λ) is specified uniquely by the
numbers k_j≥0 of added pairs of odd part 2j+1, subject to

    k_(j−1)+k_j ≤ e_j   (j≥1).

All k_j eventually vanish. The source odd multiplicities equal the core
odd multiplicities plus 2k_j, while its even multiplicity at 2j is
e_j−k_(j−1)−k_j. This proves the finite capacitated-path counting formula
implemented by the control DP. Disposition: `KILL_MODULAR_INVOLUTION_LIFT`.

## BA — two-velocity annihilation on a ring

A state lies in {−1,0,+1}^{Z/n}. Opposite particles annihilate if their
continuous paths collide: an adjacent +,− pair disappears before integer
landing, every remaining particle moves one site at its assigned velocity,
and opposite same-site landings cancel. The program implements those two
collision cases, including the cyclic edge, exactly.

Every survivor retains its initial velocity. If opposite signs were still
present after floor(n/2) steps, trace these two survivors back to their
initial sites. Their clockwise separation from the + particle to the −
particle is in {1,…,n−1}; their paths meet within (n−1)/2 units of time,
a contradiction. Hence by that integer time only one sign remains.
Such states translate rigidly and are recurrent with period dividing n.
They are exactly the recurrent states, because a mixed-sign state loses
particles within the stated bound and can never recover them. Their count
is 2^(n+1)−1. The time bound is sharp for n≥2: put + at 0 and − at n−1
and zeros elsewhere. Their annihilation first becomes visible at integer
time ceil((n−1)/2)=floor(n/2). For n=1 every state is fixed.

This is directly the finite periodic two-speed ballistic-annihilation
mechanism, not merely a shared analogy. No separate non-generic inverse
atlas has been established. Disposition: `KILL_CLASSIC_BALLISTIC_MECHANISM`.

## AZ — autocorrelation-zero feedback

For A⊆Z/n set T(A)=Z/n \ (A−A). Every image is symmetric under negation.
A fixed set is therefore symmetric, so A−A=A+A and the fixed equation is
exactly A=(Z/n)\(A+A): a symmetric complete sum-free set. Conversely that
condition implies fixedness. This identifies an owned static object; it
does not supply its enumeration or an orbit theorem. Empty and full sets
form a two-cycle. Although the map is antitone, it is not presented as a
Galois polarity; antitonicity alone does not imply eventual period at most
two. No universal recurrent classification, sharp clock or pointwise
inverse formula has been proved. Disposition: `KILL_UNCLOSED_DYNAMICS`.

## MA — reversed minimal-absent fixed-length language

The states are all languages L⊆{0,1}^n. Regard words as directed edges of
the binary de Bruijn graph on (n−1)-words; V(L) is the union of their
prefix/suffix endpoints, and C(L)=E[V(L)] is the induced-edge closure.
The update is T(L)=ρ(C(L)\L), with ρ reversing every word. For empty L,
V(L)=∅, including the n=1 case. The closure is extensive, monotone and
idempotent: V(C(L))=V(L), because every old edge is retained and no new
endpoint is added. Reversal commutes with this closure.

Let U(L)=C(L)\L. Idempotence and monotonicity give C(U(L))⊆C(L), hence

    U²(L)=C(U(L))∩L⊆L,       T²(L)=U²(L).

The even iterates descend, so an orbit eventually has period 1 or 2, with
height at most 2|L| (and hence at most 2^(n+1)). This is a generic theorem
for an involution commuting with any closure, not a language-specific
temporal result. The observed height eight at n=4 also refutes T³=T.

For target Y=ρ(target), a source with endpoint set V must be exactly
E[V]\Y. It is valid precisely when Y⊆E[V] and V(E[V]\Y)=V. Therefore

    |T⁻¹(target)| = Σ_(V⊆vertices)
                    1[Y⊆E[V] and V(E[V]\Y)=V].

The source determines its V uniquely, so there is no double count. The same
formula works on any fixed directed graph with the relevant involution.
Both axes therefore transfer to generic induced-edge closure dynamics.
Disposition: `KILL_GENERIC_CLOSURE_BOUNDARY`; a minimal-absent-word name
does not restore contribution credit.

## Verification boundary

[verify_controls.py](verify_controls.py) checks the proved fragments within
the original pilot boxes, including every ZR inverse subset, the BS inverse
DP, the MA inverse support sum and explicit BA sharp witnesses. Its actual
full canonical has 655,223 passing assertions. It imports the lane's literal
maps and is explicitly an **author-level control**, not process-independent
review. These finite checks pressure the deductions above but prove no
unclaimed extrapolation. No candidate receives a formal paper number.
