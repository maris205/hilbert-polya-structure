# Independent proof audit: eventual-period feedback

Date: 2026-09-05 UTC. **PROVABLE AS STATED**, for the submitted conservative
contract. This audit is Stage1, not Review A/B of a numbered manuscript.
No author implementation is imported. The author proof and code were
visible; this is process/code separation, not a claim of uncorrelated errors
or a cross-model review.

## Claim and assumptions

For each n>=1 the carrier is every labelled function f:[0,n-1]->[0,n-1].
P(f)(i) is one less than the length of the cycle eventually reached from i.
The subtraction is numerical, not an arbitrary relabelling. The absorber is
the constant-zero function, not the identity. Each epoch recomputes the
entire functional graph of the current function.

The audited claims are: sole recurrent state zero; all-rank sharp height
thresholds N_2=2, N_(h+1)=N_h(N_h+1)/2; complete extremizers only at critical
sizes; every-target one-step fibre/image criterion; unique largest fibre
(n+1)^(n-1). A pointwise scalar height formula, all-time fibre formula, and
classification of all noncritical deepest states are NOT submitted claims.

## Proof strategy and dependency map

1. An output value j imposes a disjoint cycle-vertex cost j+1 on its source.
2. Minimum distinct cycle costs yield triangular rank contraction.
3. A labelled core extension realizes every threshold without changing
   the cycle structure that the next epoch sees.
4. Equality in the cycle costs gives a recursive permutation class.
5. Independently, the component containing a prescribed label gives a
   recurrence for target block counts; strict rooted-forest comparison
   locates the maximum.

The last two steps do not assume the rank equality or the sharp construction.

## 1. Cycle-cost certificate and termination

Let J=im P(f). For each j in J choose one source cycle of length j+1.
These chosen cycles are pairwise disjoint; their vertices lie in im f.
Consequently

```
rank(f) >= sum_(j in J)(j+1) >= |J|(|J|+1)/2.
```

If |J|>=2 then rank(f)>|J|. If |J|=1 then P(f) is constant;
every constant function has a one-cycle and P^2(f)=0. Along any orbit,
rank therefore decreases until a constant appears, followed by zero.
Only zero can be recurrent. This also proves that height, defined as
first hitting time of zero, is finite and equals the usual transient.

Rank one is an important boundary: zero has height0, each other constant
has height1. Such other constants exist exactly when n>=2.

## 2. Minimal cost for a given height

A state of height at least2 cannot have rank1, so has rank>=N_2=2.
If height(f)>=h+1, then height(P(f))>=h and its rank is at least N_h.
The preceding certificate forces rank(f)>=T(N_h)=N_(h+1).
This proves the claimed necessary condition for every h>=2.

The inequality is NOT an equality law for rank evolution. For example,
two rank3 permutations can have different next ranks. No scalar triangular
iteration is asserted to be conjugate to P.

## 3. Core extensions and attainment

Suppose g takes every value in C=[0,k-1]. Its directed cycles are exactly
those of g restricted to C. In addition, P(g) again takes its values in C.
Restriction to C therefore commutes with every P epoch, and for t>=1,
P^t(g)=0 iff P^t(g|C)=0: at the previous epoch, all cycles are loops in
one graph exactly when they are loops in the other.

This does not assert height preservation when the restricted state is
already zero. An extension of zero can have height0 or1. The construction
below uses a positive-height restriction, where height is preserved.

Starting with the swap on two labels, let u be a height-h permutation on
k=N_h labels. For every old label i, create a cycle anchored at i, using
u(i) new vertices. These cycles are disjoint, use exactly

```
k+sum_i u(i)=k+k(k-1)/2=T(k)
```

vertices, and yield a permutation v. Its period-feedback restriction on
the old labels is u, while all its values lie in [0,k-1].
Thus height(P(v))=h and height(v)=h+1.

Adding fixed points to v gives a permutation of any desired larger rank r
until the next threshold. Its first feedback has the unchanged core and
zero outside. Adding vertices with arrows to zero raises the carrier size
to any n>=r without raising the rank. This proves exact maxima for every
(n,r), including the rank-one exception described above.

## 4. Critical-size equality is complete

At n=N_h a height-h state must have full rank and is a permutation.
For h>=3, k=N_(h-1), equality in every cycle-cost inequality forces:
one cycle of each length1,...,k, no other cycle, and no noncyclic vertices.
Its feedback takes values precisely0,...,k-1. Its core restriction is a
height-(h-1) function on k labels, hence a permutation.

The converse follows from the core lemma. Thus the recursive criterion
is necessary and sufficient, not just a witness family.
For each lower-level permutation, every cycle receives exactly one
prescribed old label. If m=N_h-k labels are fresh, allocating them to
cycles of sizes1,...,k contributes m!/prod_j j!, and arranging cyclic
orders contributes prod_j j!. Each top state is recovered uniquely from
these data. The number therefore multiplies by m!:

```
D_2=1, D_h=D_(h-1)(N_h-N_(h-1))!.
```

This is only the equality classification at n=N_h. No square-root formula
from P137, ordinary triangular number sequence, or generic rank descent
supplies the recursive label-placement condition.

## 5. Independent target recurrence and inverse equivalence

For a target g, an arrow f(i)=v preserves eventual period. Hence each
nonempty set B_j={i:g(i)=j} is f-invariant, and every component within B_j
has cycle length d=j+1. Conversely this condition on every block forces
P(f)=g. These statements include unsupported targets.

Let c_d(m) count a connected mapping on a prescribed m-set with cycle d:

```
c_d(m)=0 (m<d);
c_d(d)=(d-1)!;
c_d(m)=C(m,d)(d-1)! d m^(m-d-1) (m>d).
```

Choose the cyclic vertices, their directed cyclic order, and a forest
rooted at those cyclic vertices. This is classical labelled enumeration.
If a_d(k) counts arbitrary such components on a k-set, distinguish its
least label and choose the size m of the component containing it:

```
a_d(0)=1;
a_d(k)=sum_(m=d)^k C(k-1,m-1)c_d(m)a_d(k-m).
```

This component recurrence is the reviewer's formula implementation.
It differs from the submitted simultaneous cyclic-vertex sum, but both
count the same class. Therefore the target fibre is prod_j a_(j+1)(|B_j|).

Existence is equivalent to |B_j|>=j+1 for every nonempty block: necessity
requires one such cycle, sufficiency attaches any extra vertices to a
single such cycle. The multinomial image count follows by assigning the
label sets. No temporal theorem is used for this atlas.

## 6. Unique maximal fibre

For each m>=d, the connected mapping count satisfies

```
c_d(m)/c_1(m)=(m)_d/m^d.
```

For d=1 equality holds. For d>=2 this ratio is strictly below1.
The labelled set-of-components construction has nonnegative coefficients,
so a_d(k)<=a_1(k), strictly whenever k>=d>=2. Here a_1(k) is the number
of rooted forests, equal to (k+1)^(k-1) for k>=1, and a_1(0)=1.

For two or more prescribed nonempty blocks, disjoint union injects their
rooted forests into rooted forests on the union. It is not surjective:
a rooted tree containing vertices from distinct blocks lies outside the
image. Thus splitting into multiple blocks is strictly suboptimal.
A target with one nonempty block and label j>=1 is strictly suboptimal
by the previous inequality. The sole equality target is g=0.
At n=1 this is the single state and the value is1.

## Corrections and open risks

No correction of the submitted mathematical theorem is required.
Unbounded parameter proofs were checked deductively; finite boxes are
falsification pressure only. External ownership and the explicit scope of
the word-lane statistic-writeback filter are handled in SOURCE_AND_SCOPE.md.
All standard forest, EGF, cycle-finding, and numerical-sequence facts
remain zero-credit background.

