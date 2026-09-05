# Independent all-parameter reconstruction — P202 Review A

Target: the immutable Round0 main, not the Stage1 gate. Reviewer:
batch197_fosp_gate. The author/gate programs were not opened or imported.
This reconstruction assumes exactly n>=1, synchronous updating, ternary
letters ordered 0<1<2, and indices modulo n. No empty-word system or q>3
extension is inferred. All assertions below are proved for arbitrary n;
finite controls are recorded separately.

## 1. Nine local equations and every source

The local table, with row=current and column=right neighbor, is

| current | next 0 | next 1 | next 2 |
|---|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 0 | 2 | 2 |
| 2 | 0 | 0 | 0 |

Thus an output 1 forces source 0; output 2 forces source 1 whose right
neighbor is nonzero; output 0 permits source 2, or source 1 with right
neighbor 0. A target edge 21 contradicts those two forced requirements.
Conversely, for a target y without 21, set independent coordinate domains

    D_i={0}                 if y_i=1,
        {1}                 if y_i=2,
        {1,2}               if y_i=0 and y_(i+1)=1,
        {2}                 otherwise.

Every tuple in the Cartesian product is a source. For target 2 its next
target is 0 or 2, so every next source is nonzero. For an optional source
1 at target 0, the next source is forced to 0. These observations verify
every edge, including the wrap edge, without assuming that independent
coordinates automatically imply independent output constraints. The local
necessity analysis proves that there are no other sources. Recover the
choice at each target 01 from its first source letter. Hence the bijection
and fibre 2^e01 hold, with zero outside the image.

The cyclic 01 occurrences are vertex-disjoint. At even length, n/2 such
edges leave no vertex and force the two alternating targets. At odd
n=2m+1>=3, m such edges leave exactly one letter; the other cyclic pieces
are identical 01 blocks. According to the leftover letter, the target is
a rotation of 001(01)^(m-1), 011(01)^(m-1), or 012(01)^(m-1).
Each avoids 21. The first two have exactly one 00 or one 11 edge,
respectively; the third has exactly one 2. These unique features prove
primitive rotation orbits and disjointness, so there are exactly 3n, not
at most 3n, maximizing targets. At n=1, the local diagonal is a three-cycle
and every fibre is one. This also checks the cyclic loop boundary directly.

## 2. An eventual coordinate domain, with origin deliberately discarded

A nonconstant image lacking 0 would be a nonconstant cyclic binary word
on {1,2}, hence would contain 21. Between successive maximal zero runs,
avoidance of 21 forces a word 1^a 2^b. Thus the cyclic run list is
(c_i,a_i,b_i), c_i>=1, a_i,b_i>=0, a_i+b_i>=1. It is unique up to rotation
of its list, not an encoding of an absolute first word position.

The inverse result gives each constant target a unique constant source.
Therefore a nonconstant word cannot later become constant. Updating a
zero run makes c_i ones. If b_i>0, the a_i ones all become twos and the
b_i twos become zeros. If b_i=0, a_i>=1: only its final one resets to zero.
Consequently

    c'_i=max(b_(i-1),1),  a'_i=c_i,
    b'_i=a_i-[b_i=0].

Each new one run is positive and has a positive zero run before it; hence
there is no unaccounted merger and k is conserved. The possible a_i=0
in the first image causes no negative length because then b_i>0. After
two updates of any original word, c_i,a_i>=1. This forward-invariant
domain suffices; no assertion that arbitrary proposed run coordinates
are necessarily in F^2(X_n) is needed.

Subtract one from c and a, and zero from b. The nonnegative surplus vector
z has length 3k and mass M=n-2k. Its c,a,b equations are exactly

    z'_c_i=(z_b_(i-1)-1)_+,
    z'_a_i=z_c_i,
    z'_b_i=z_a_i+min(z_b_i,1).

The b positions retain one unit permanently once reached; every remaining
unit advances one bin per tick. Ties do not affect counts. This is an
owned parking factor, not a new mechanism or a labelled-word conjugacy.

## 3. Clearance and its exact clock, including zero mass

Initially a b bin with positive mass is already occupied. Clearance means
all M units retained or all k slots occupied, whichever happens first.
For M=0 it holds at time zero; it is wrong to substitute M=0 into
3 min(k,M)-1.

An arrival-event description eliminates the transit bins. Initial mass in
c_i first arrives at slot i at time 2, mass in a_i at time 1, and initial
excess at b_i reaches slot i+1 at time 3. An occupied slot transmits an
arriving batch to the next slot after three ticks. An empty slot consumes
one unit and transmits the rest after three ticks. Batches with equal
arrival time and destination are combined first. Induction on arrival
epochs proves exact agreement with the synchronous bin equations; thus
the reviewer's heap control is not a different time convention.

Here is the bound independent of any stochastic or Abelian timing result.
If 1<=M<=k, any unit still moving can pass at most M-1 already occupied
slots before being retained. It cannot pass a full ring of k slots and
remain mobile: those occupied slots plus that unit would require k+1
units. From a transit bin its first slot is at distance at most 2, so
its retention time is at most 2+3(M-1). If it starts as excess in an
occupied slot, another unit is already spent there; its first new slot
is at distance 3, followed by at most M-2 further intervals, giving
3+3(M-2). The latter case requires M>=2.

If M>=k and some slot remained empty at T=3k-1, at least one unit would
still be moving. Such a unit has never been retained and has advanced
at each tick. Its T destinations cover every bin except its initial bin.
The persistently empty slot cannot be its initial bin, because positive
initial mass would occupy that slot at time zero. It must therefore have
been visited, a contradiction. This gives 3k-1. At M=k both arguments
are consistent.

Put all M>0 units in a single c bin. The successive slots are filled at
2,5,8,...; clearance first occurs at 3 min(k,M)-1. This covers k=1 and
arbitrarily large M as well as the sparse case. Therefore the bound is
sharp for every pair (k,M), not merely for the parameters tested by code.

## 4. Original-word recurrence, pointwise entry and spatial phase

Let A have edges 00,01,11,12,22,20, and B have edges 01,10,12,20.
On A the local table gives global colour advance C. A is preserved by
C, and no nonempty ternary word can be fixed by C or C^2; its exact
temporal period is 3. On B the table gives the literal next letter,
so F=left rotation R. B is rotation-invariant, hence its period is exactly
the least spatial period of the labelled word.

The intersection has just edges 01,12,20: it has three words when 3|n,
and none otherwise. On those three words the two specified actions agree.

In the forward-invariant run domain, all b_i>=1 is exactly A: a missing
two run produces the forbidden edge 10, while positive two runs leave
only the listed A edges. All units retained is exactly c_i=a_i=1,
b_i in {0,1}, which is exactly B: its circular words concatenate 01
and 012 and have no constant runs. Therefore clearance is equivalent
to entering A union B. Before it, both an empty slot and mobile mass
remain, so neither recurrent condition holds. Clearance sends every
nonconstant orbit to the union; constants were already on its colour
cycle. Since this union is explicitly periodic and forward invariant,
it is the entire recurrent set.

This proves the exact entrance time in the twice-image domain. For an
arbitrary original x the fully explicit convention is h(x)=0 if x is
in the union, h(x)=1 if x is outside it but F(x) is inside, and otherwise
h(x)=2+clearance(F^2(x)). No discarded spatial origin is used to deduce a
period. In particular, periodic run counts alone would not establish the
claimed original-word period; the coordinate checks above do.

## 5. Sharp all-length prehistory

For M=n-2k>0, min(k,M)<=floor(n/3), giving
h(x)<=2+3 floor(n/3)-1. Zero mass or constant twice-images need at most
two preliminary steps. At n=1 the entire carrier is the colour cycle.
At n=2 nonconstant twice-images have k=1,M=0; the upper bound two is
attained by 12 -> 20 -> 01. Thus H(1)=0 and H(2)=2.

For n=3k+r>=3, k>=1, 0<=r<=2, define

    x=1^(k+r+1) 2 (12)^(k-1),
    Fx=2^(k+r+1) 0 (20)^(k-1),
    F^2x=0^(k+r+1) 1 (01)^(k-1).

The nine local rules verify both updates, including k=1 and the cyclic
boundary. The last word has k slots, all empty, and M=k+r mass in one
c bin. Its remaining time is 3k-1>0. Since a recurrent point cannot
precede a nonrecurrent point, both earlier points add exactly two steps.
Hence h(x)=3k+1 and H(n)=3 floor(n/3)+1. This is an existence witness
at each length; it does not classify every maximizing source.

## 6. Census without counting rotation classes accidentally

A closed length-n adjacency walk counts a labelled cyclic word, because
coordinate 0 is distinguished. For image words the matrix is
V(u)=[[1,u,1],[1,1,1],[1,0,1]], with weight u only on 01. Thus its
trace is exactly the image fibre-exponent polynomial. V(1) has two equal
rows, trace 3 and sum of principal 2-minors 1, so its characteristic
polynomial is lambda(lambda^2-3lambda+1). The two nonzero eigenvalues
are the squares of the roots of z^2-z-1. For n>=1 their power sum is
L_(2n); the discarded zero eigenvalue is harmless only at positive n.
The source bijection additionally proves sum_y 2^e01(y)=3^n.

A has matrix I+P3. The eigenvalues 2,exp(i*pi/3),exp(-i*pi/3) give
a_n=2^n+2cos(n*pi/3), hence the printed six-term integer correction.
B has Q=[[0,1,0],[1,0,1],[1,0,0]], characteristic polynomial
lambda^3-lambda-1. Its traces obey b_n=b_(n-2)+b_(n-3), starting
3,0,2 at n=0,1,2. The b_0=3 convention introduces no empty carrier.
Subtracting the actual three-word overlap gives the recurrent count.

For F^t-fixed points, A contributes iff 3|t. A B-word is fixed by R^t
iff it repeats a length-d closed word, d=gcd(n,t); this contributes b_d.
The intersection is counted twice iff 3 divides both n and t, equivalently
3|d, and has three words then. This proves the stated fixed-point formula
for every n,t>=1, including n=1 and periods not divisible by 3.

## 7. Finite falsifiers and limits

The new program constructs all 797,160 states n=1..12 by base-three
integers. It peels indegree-zero vertices and uses union-find on remaining
cycle edges, then propagates depths backwards. Its target inverse uses
independent coordinate domains, not the author's source-edge traversal.
It checks every source set, pointwise depth, exact period, run update,
action and maximizing-target set. The parking heap is independently
compared with bin equations for every weak composition with k=1..4 and
M=0..6 (24,577 configurations), and sharp words are checked through n=180.
The total is 12,775,204 assertions, including bounded owner comparators.
Neither their number nor byte reproducibility proves the all-n theorem
or excludes unexamined owners. Those conclusions have separate scopes.
