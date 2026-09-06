# Fourth intake: exact adapters and negative boundaries

Date: 2026-09-05 UTC. These are author scout deductions, not admissions.
All six literal maps were actually piloted before selecting EC for a deep
pass. CP and OR are closed here to prevent their classical image clocks from
being promoted later. UO, OS and MG remain bounded negative scouts.

## CP: circular parking displacement feedback

Carrier {0,...,n-1}^n, n>=1. Cars arrive in label order i=0,...,n-1 on n
cyclically ordered sites. Car i starts at preference a_i and parks at the
first empty site encountered in the positive direction. Let P(a)_i be its
number of advances. At the next epoch these displacements are the new
preferences. This is the standard circular linear-probing statistic, with
the statistic fed back, not an ordinary parking-function subset.

At most i sites are already occupied, so d_i<=i. Let

    E_n = {d: 0<=d_i<=i for every i}.

If d is itself in E_n, induction says car i parks exactly at site i: sites
0,...,i-1 are occupied, and its preference d_i lies in that initial segment
or at i. Therefore

    P(d)_i = i-d_i on E_n.

This is the whole temporal mechanism: P maps into E_n and restricts there
to coordinatewise complement. Every E_n point has its complement as a
preimage. Hence image=core=E_n, P^3=P, height zero for n=1 and one for n>=2.
For n>=2 coordinate i=1 prevents any fixed point, so there are n!/2 strict
two-cycles. No temporal research credit is assigned to this normalizer.

For a target d, let pi be a permutation of the n sites giving the successive
parking locations. It is feasible exactly when, for every i, all d_i cyclic
sites immediately preceding pi_i belong to {pi_0,...,pi_(i-1)}. If feasible,

    a_i = pi_i-d_i mod n

is the unique corresponding preference word. Conversely the parking
algorithm reconstructs pi from this a, so the adapter is bijective.
The inverse is thus precisely a static permutation feasibility count;
each target has at most n! sources. All n! permutations are feasible when
d=(0,...,0,c), 0<=c<n. If d_i>0 for an earlier i<n-1, choose a permutation
placing the predecessor of pi_i at a later car: this fails feasibility.
Thus n! is the maximum, attained exactly by those n targets. This inverse
does not provide a separate mechanism from the old parking statistic.

## OR: prefix occurrence rank = tableau transpose on the image

Carrier {0,...,n-1}^n. Define

    O(a)_i = #{j<i: a_j=a_i}.

Every output b is a lattice word: in every prefix, the number of k entries
is at least the number of k+1 entries. The (k+1)-st occurrence of a colour
cannot precede its k-th occurrence, proving this prefix inequality.

Use zero-based tableau coordinates. For such b, put the label i in row b_i,
in the next available column of that row. Row entries increase by
construction; the prefix inequalities ensure that the cell above each
entry is already present, hence columns increase too. This is the classical
Yamanouchi-rowword bijection with standard Young tableaux T of n cells.
The column of label i is exactly the number of earlier labels in its row,
which is O(b)_i. Thus

    O(rowword(T)) = rowword(T transpose).

This is an exact coordinate conjugacy on the entire first image, not merely
a common census. Every lattice word is attained from its transposed word;
image=core, O^3=O, and the image has the classical total SYT count I_n.
For n>=2 a diagram contains an off-diagonal cell and unique labels forbid
T=T transpose; all core states therefore lie in strict two-cycles. The
pilot I_n values 1,2,4,10,26 are not new dynamical enumeration.

The complete static inverse also has a simple chain-assembly adapter. When
reading target b from left to right, b_i=0 starts a fresh source colour;
there are n-c_0 earlier-unused colours, where c_k is the number of earlier
target entries k. If b_i=k>0, choose an existing colour whose current
occurrence count is k; there are c_(k-1)-c_k such colours. After each step,
update the target prefix counts. Multiplying these options gives exactly
the fibre size, with zero when a required choice count vanishes. Equivalently
the zero positions contribute the falling factorial (n)_(#zeros), and
the positive positions contribute their prefix differences. This counts
labelled chains of repeated letters, independently of any orbit theory.

P194 already uses the classical Yamanouchi/SYT/RSK surface, though its
least-colour crystal scheduler is not O. The external primary rowword
definition and the full conjugacy above, not a false literal P194 identity,
are the decisive subtraction. OR is NO_PROMOTION.

## UO: least label outside the forward orbit

Carrier all f:{0,...,n-1}->{0,...,n-1}. Include the starting point v in its
forward orbit. Set U(f)(v) to the least label outside that orbit if one
exists, and to v when the orbit is the entire carrier. The totalization is
part of the literal map. For n=1,...,5, measured heights are 0,0,3,4,5 and
core sizes 1,4,8,12,12. These observations neither prove a uniform two-cycle
theorem nor give an all-n inverse atlas. No such contract has been obtained.
NO_PROMOTION; no cutoff enlargement or selective graph restriction.

## OS: forward-orbit cardinality feedback

On the same full carrier set define Q(f)(v)=|Orb_f(v)|-1. For n=1,...,5 the
measured heights are 0,0,5,9,11. At n=5 the recurrent periods include 2,8,12.
The statistic is elementary functional-graph data, but feeding all values
back changes the graph. No all-n temporal theorem or independent labelled
inverse contract has been proved. NO_PROMOTION, without claiming a located
paper already contains this literal feedback operator.

## MG: discrete cyclic midpoints and conservative half-sharing

Carrier all subsets S of Z/NZ, represented as binary words. The empty set
is fixed. For a nonempty S, write its points in positive cyclic order and
replace every point p_i by

    p_i + floor(g_i/2) mod N,

where g_i is the positive clockwise gap to the next point. For a singleton
g_0=N. Distinct points remain distinct, because consecutive new points have
positive gap

    g_i' = ceil(g_i/2) + floor(g_(i+1)/2).               (MG.1)

Using a cyclicly tagged ancestral first point makes (MG.1) exact without
confusing wraparound with a fixed least-label anchor. The gap sum remains N,
and the anchor moves by floor(g_0/2). Thus this is conservative integer
half-sharing on positive cyclic gaps plus an anchor cocycle. The empty and
singleton sectors supply only the identity and an ordinary rotation.

This adapter does NOT identify (MG.1) with the usual candy game that adds a
piece after an odd total. For example gaps (1,2) map to (2,1), while rounding
both arithmetic means upward gives (2,2) and does not conserve the sum.
The opened Bal--DeGaetani source owns a neighbouring rounded-sharing model,
not this exact formula. No full-parameter time/core/inverse contract is
proved here. The bounded N=3,...,8 pilots alone do not fill that gap.
NO_PROMOTION. The gap adapter is retained to prevent a renamed sharing
process or elementary singleton rotation being counted as a fresh axis.

## Evidence scope

pilot.py uses a generic path-walk functional-graph decomposition for all
six maps. verify_structure.py separately checks CP's full permutation
source sets and all maxima, and OR's full chain-decoded source sets,
prefix-product formula and tableau transpose, for every target through n=5.
No prior script is imported. These are author controls, not independent
candidate review. Primary source boundaries are recorded separately.
