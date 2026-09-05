# OR: independent proof reconstruction

This audits the frozen contract with hash
`ba9ed975fef29c761fa2a8faef8f6c23e8a3ce45034387e8ebdbbc5b3405d1ed`.
The derivation uses local source-edge constraints and labelled particles;
the finite checker never assumes the claimed recurrent set to find cycles.

## 1. Literal table and source edges

For adjacent source letters `(a,b)` the output table is

```text
       b=0 1 2
a=0      1 1 1
a=1      0 2 2
a=2      0 0 0.
```

Equivalently the allowed source edges at target symbols are

```text
y=0: 10,20,21,22;
y=1: 00,01,02;
y=2: 11,12.
```

These are all nine source edges with no overlap between output classes.
A source is exactly a closed walk through these successive edge classes,
including closure when `n=1`. This gives an independent inverse algorithm.

Two consecutive outputs `21` would require the shared source letter to be
both nonzero and zero, so it is impossible. Conversely, for a target without
`21`, the choices `x_i=y_i-1 mod3` give a source. At a target `0`, changing
the source `2` to `1` is permitted precisely when the next source is zero,
equivalently when the next target is `1`. Those are all alternatives in the
edge list. Two `01` target edges cannot share a vertex; their binary choices
are independent, including wrap-around. Thus the printed set bijection and
the formula `2^occ01` hold on the entire image.

At length one the closing source edge is diagonal, giving the three-cycle
`0 -> 1 -> 2 -> 0` and one source per target. For every length the constant
target has a unique constant source; hence a nonconstant orbit never becomes
constant. This observation closes the constant/nonconstant split below.

## 2. Maxima and elementary enumeration

If there are `e` cyclic `01` edges, their disjoint endpoints give `2e<=n`.
For even length equality forces the two alternating words. For odd
`n=2m+1>=3`, remove the disjoint `01` pairs. The sole remaining vertex has
letter `0`, `1`, or `2`. Cutting there identifies the three listed words
`001(01)^(m-1)`, `011(01)^(m-1)`, `012(01)^(m-1)` up to rotation.
They all avoid `21`, and a unique doubled-zero, doubled-one, or sole-two
feature forces each orbit to have exactly `n` rotations. Different types
cannot overlap. This proves the full equality classification `2` versus
`3n`, with the separately handled three targets at length one.

Let `M` have all entries one except `M_21=0`. Its trace is 3, its three
principal two-minors sum to 1, and its determinant is zero (two rows agree).
Consequently its characteristic polynomial is `lambda^3-3lambda^2+lambda`.
The nonzero roots are the squares of the two roots of `z^2-z-1`, so
`tr(M^n)=L_(2n)` for every positive `n`. Weighting the `01` edge by `u`
gives the claimed polynomial: every closed walk contributes one monomial
with exponent exactly `occ01`. These are standard transfer facts.

## 3. Run factor and what information it retains

An image word with no zero is constant: otherwise a cyclic word in `1,2`
would contain `21`. In a nonconstant image, start at a zero-run and cut at
every new zero-run. Between them, all ones precede all twos, since `21`
is forbidden. This gives `0^c_i 1^a_i 2^b_i`, with `c_i>=1`,
`a_i+b_i>=1`. Runs may initially have `a_i=0` or `b_i=0`.

Track the old zero-runs by their order. Their zeros produce a one-run of
length `c_i`. If `b_i>0`, the old ones all become twos and the old twos
produce a zero-run of length `b_i`. If `b_i=0`, the final old one resets
to zero and the other `a_i-1` ones become twos. There are no further
mergers, because every new one-run is positive. Thus

```text
c_i'=max(b_(i-1),1), a_i'=c_i, b_i'=a_i-1[b_i=0].
```

The cyclic number `k` of blocks is preserved. After the second original
update both `c_i,a_i>=1`. Subtract their compulsory one unit and arrange
the surplus at positions `3i,3i+1,3i+2` around a `3k` ring. The total is
`M=n-2k`. Only positions `3i+2` can retain a unit; every other unit moves
one position forward at each update. This follows directly by following
each old letter-type contribution, not by assuming a known queue formula.

For checking, assign distinct identities to these surplus units. One unit
already in a parking bin is parked; all others are mobile. After a move,
choose any one arrival to an empty parking bin and park it forever. All
other arrivals remain mobile. The choice of identity cannot change counts.

There is no claim of a full labelled-word conjugacy after discarding the
physical origin. The count coordinates are cyclically indexed. This
factor suffices for a rotation-invariant first-entry question; all eventual
word actions and periods are established on original labelled coordinates.

## 4. Clearance bound and all equality witnesses

For `M=0` there is nothing to move. For `1<=M<=k`, a mobile particle that
has not yet parked cannot complete a full circuit: that would require all
`k` slots to be filled by other particles, although there are at most
`M-1<k` such particles. Its passed slots are distinct and each costs another
parked particle. Starting at a transit bin, the first slot is at distance
at most 2 and there are at most `M-1` occupied slots to pass, hence the
parking time is at most `2+3(M-1)=3M-1`. Starting at an occupied parking
bin consumes one other particle immediately; the bound is even smaller,
`3+3(M-2)`, whenever this case can arise.

For `M>=k`, assume a slot remains empty at time `3k-1`. There are then fewer
than `k` parked particles and therefore a particle still mobile. Since
parked particles never restart, it has moved at every earlier step. Its
first `3k-1` destinations include every bin except its starting bin. It
cannot have missed the empty slot unless it started there; but then it
would have been parked initially. This contradiction proves clearance by
`3k-1`.

In either mass regime, putting all `M` particles in one `c` transit bin
fills the required slots at times `2,5,...,3 min(k,M)-1`. Hence the bound
is sharp for every positive `k,M`, not merely asymptotically. This is a
finite parking calculation; no new parking model is claimed.

## 5. Exact recurrence and point clock

The filled-slot condition is `b_i>=1` for all blocks. Together with positive
`c_i,a_i` it is precisely the original-word constraint that all cyclic
increments are `0` or `1` modulo 3. On that set `A_n`, direct application
of the local table is global addition by one; this preserves the constraint
and every point has period 3.

The no-mobile-particle condition says `c_i=a_i=1`, `b_i in {0,1}`. Its
original words are exactly cyclic concatenations of `01` and `012`, or
equivalently the edge language `B_n` with edges `01,10,12,20`. For each of
these four edges the local output equals the right letter. Thus `F=R`
on `B_n`, and its points have their ordinary spatial rotation periods.

The parking bound reaches one of these two conditions. Before their first
occurrence, both a mobile particle and an empty slot exist, so neither
word criterion holds. Constants were already in `A_n`, and no nonconstant
point becomes constant. These facts prove exhaustion and exact first entry,
not just examples of cycles or a convergence upper bound.

The intersection keeps only edges `01,12,20`, forcing the three labelled
rotations of a repeated `012` if `3|n`, and giving no word otherwise.

## 6. Global sharp tail with small lengths separated

For a nonconstant twice-image, `k>=1` and `M=n-2k>=0`. Positive mass gives
tail at most `2+(3 min(k,n-2k)-1)`; the minimum is at most `floor(n/3)`.
Zero mass or a constant twice-image costs at most two. At `n=1` all states
are recurrent; at `n=2`, `12 -> 20 -> 01 -> 10 -> 01` proves the sharp
value two (the repeated part starts at `01`).

For `n=3k+r`, `r in {0,1,2}`, the printed source
`1^(k+r+1) 2 (12)^(k-1)` has consecutive images
`2^(k+r+1) 0 (20)^(k-1)` and
`0^(k+r+1) 1 (01)^(k-1)`. The latter has all `M=k+r` surplus in one
`c` bin and every slot empty, so it first reaches the core `3k-1` steps
later. No earlier point of the orbit could already be recurrent, since
the recurrent set is forward invariant. Its original tail is exactly
`3k+1`, proving the bound for every `n>=3`.

No complete classification of all maximum-tail source words is claimed by
the contract. The equality classification in Section 2 concerns maximum
fibres, a different question.

## 7. Periodic census on labelled words

The `A` adjacency matrix is `I+P_3`; its eigenvalues are `2,1+omega,
1+omega^2`, and the latter sum of nth powers is the printed six-periodic
epsilon. The `B` matrix has characteristic polynomial `lambda^3-lambda-1`;
direct traces start `b_0=3,b_1=0,b_2=2`, giving the stated recurrence.
These length-zero matrix traces do not introduce an empty-word carrier.

At time `t>=1`, the `A` contribution is all of `A_n` exactly when `3|t`.
A `B_n` word fixed by `R^t` repeats a closed word of length `d=gcd(n,t)`,
so contributes `b_d`. The intersection is counted twice exactly when
`3|d`, contributing the subtraction 3. This proves the all-time formula
without using the parking quotient to infer periods.

## 8. Computational independence and finite scope

The verifier encodes index zero as the least significant ternary digit.
If `Z,O,T` are bitplanes, the output-one plane is `Z`, and the output-two
plane is `O & ~right(Z)`. These update codes generate the entire functional
graph; path dictionaries locate actual cycles and propagate depths.
Inverse edge walks independently enumerate all source sets, not the
author's subset-of-01 construction. Exact source-set agreement is checked
for every target, including unsupported ones, through `n=12`.

Run evolution is checked on every nonconstant image, including absent
one-runs. The token clock is checked on all tested image states in its
positive-`a` domain. Full fibre-polynomial coefficient vectors are compared
with an independent weighted-walk calculation, and all fixed counts
`1<=t<=6n` are compared with the graph's actual cycle census. These finite
checks are counterexample pressure; the preceding arguments prove the
all-parameter statements.
