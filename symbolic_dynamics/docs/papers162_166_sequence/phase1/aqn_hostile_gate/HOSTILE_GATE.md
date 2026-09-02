# AQN hostile specialist gate

**Date:** 2026-09-03 UTC  
**Object:** adaptive quotient-normalized rotation (`AQN`)  
**Frozen input:** `scouting/replacement_adaptive_maps/`  
**External state:** `HOLD_EXTERNAL`

## Verdict

```text
AQN  KILL_OWNER_REDUCTION_AND_INTERNAL_PROOF_ENGINE_COLLISION
HOLD_EXTERNAL
```

I found **no counterexample** to Contracts A--D as actually bounded.  The
iterate, image, depth-one graph, all-positive-time fibres, fixed-count
formula, point periods, and odd-field labelled recovery are correct.  This is
therefore not a mathematical-error kill.

It is a paper-allocation kill.  After the mandatory owner subtraction, the
package is an elementary composition of:

1. the cyclic derivative quotient by global alphabet translation;
2. rotation on zero-sum difference words, stratified by a rotation-invariant
   transition count;
3. a coordinate-zero section of each translation orbit; and
4. Burnside/Möbius and single-parity-check enumeration.

The first item is now a particularly close external theorem of
Grinberg--Mao and is already the exact internal proof engine of P63.  The
second and fourth items have direct classical owners.  The remaining
state-selected section gives attractive formulas, but its image/fibre and
weighted-fibre conclusions are one-line consequences of those owned group
actions.  Parameter recovery is correct and neat, yet is not enough to make
the residual paper-sized.

## Independent derivation

Index coordinates by `Z/nZ` and use the scout's convention

```text
(R^u w)_i = w_(i+u),
Delta(w)_i = w_(i+1)-w_i,
k(w) = |supp Delta(w)|,
s = c k(w).
```

### 1. Invariant and iterate

Subtracting a constant disappears under `Delta`, and rotation commutes with
`Delta`.  Hence

```text
Delta(T_c(w)) = R^s Delta(w),
k(T_c(w)) = k(w).
```

The shift `s` is therefore frozen along the orbit.  Direct induction gives,
for every `t>=1`,

```text
T_c^t(w) = R^(ts) w - w_((t-1)s) 1.
```

The induction step is not circular: the zero-coordinate subtracted at the
next application is

```text
(T_c^t(w))_0 = w_(ts)-w_((t-1)s),
```

which telescopes with the previous additive offset.

### 2. Image, quotient, and depth

For `y=T_c(w)`, coordinate `-s` is

```text
y_(-s) = w_0-w_0 = 0.
```

Since `k(y)=k(w)`, every image point satisfies

```text
y_(-c k(y))=0.                                      (I)
```

Conversely, if `y` satisfies (I), then for every `a in F_q`

```text
w_i = y_(i-s)+a
```

has `k(w)=k(y)`, has `w_0=a`, and maps to `y`.  These are all sources.
Thus the image is exactly (I), every positive indegree is `q`, and the image
has one representative from each free global-translation orbit.  Therefore

```text
|Y|=q^(n-1).
```

The restriction to `Y` is a permutation because `Delta` identifies `Y`
bijectively with the zero-sum difference code and sends its update to

```text
d -> R^(c |supp d|) d.
```

Among the `q` one-step sources of a recurrent point, exactly one is the
section representative in `Y`; the other `q-1` sources lie outside `Y`.
Consequently all and only outside points have depth one.

### 3. Point periods

Let `p(d)` be the least rotational period of `d=Delta(y)`.  On the fixed
support stratum the update is rotation by `c k`, so its orbit length is

```text
p(d) / gcd(p(d), c k).
```

Equality of difference words suffices because both resulting words are the
unique section representatives of the same translation class.  Contract A3
is correct, including `c=0` and `k=0`.

## Image-union attack

There are two different statements here, only one of which is true.

The correct disjoint decomposition is

```text
Y = disjoint_union over k of
    {y : k(y)=k and y_(-ck)=0}.                     (II)
```

Disjointness comes solely from the `k(y)=k` clauses.  The naked coordinate
hyperplanes

```text
H_k={y:y_(-ck)=0}
```

are not disjoint, and their union is not `Y`.  The independent exact attack
at `(q,n,c)=(3,5,1)` found:

```text
|union_k H_k| = 211,
|Y|           = 81.
```

The zero word belongs to all six indexed `H_k`.  Moreover
`(0,0,0,1,0)` belongs to the raw union but has two changes and fails its
required coordinate test because its coordinate `-2` is `1`.

No frozen formula fails: the scout states `Y={y:y_(-ck(y))=0}` rather than
the false raw union.  Any future text must use (II) and must not call the
unqualified hyperplanes a disjoint union.

## All-positive-time fibre attack

Solving the exact iterate for a supported target gives, for `t>=1`,

```text
w_i^(a) = y_(i-t c k(y))+a,  a in F_q.
```

The consistency equation at source coordinate `(t-1)c k(y)` is exactly the
image condition `y_(-c k(y))=0`; it introduces no additional `t`, gcd, or
small-parameter restriction.  Thus every positive-time fibre has `q` points.

The **source set is generally not independent of `t`**.  At
`(q,n,c)=(3,5,1)` and target `(0,0,0,0,1)`, the exact source sets at times one
and two are different.  What is independent of `t` is only the zero-count
polynomial.  Indeed,

```text
N_0(w^(a)) = N_(-a)(y),
sum_a z^N_0(w^(a)) = sum_b z^N_b(y),
```

because rotation preserves symbol multiplicities and `a -> -a` permutes
the field.  For the displayed witness the polynomial has coefficient
profile

```text
z^0 + z^1 + z^4.
```

The frozen Contract B is correctly worded, but the allowable ceiling is:
“the weighted fibre polynomial is `t`-independent,” never “the positive-time
fibres are `t`-independent.”  This axis is a static inventory of one global
translation orbit, not a second dynamical mechanism.

## Fixed-count formula

Under the bijection `Y -> D_(q,n)` supplied by `Delta`, a point is fixed by
`T_c^ell` exactly when its difference word is fixed by
`R^(ell c k)` on its support-`k` stratum.

Put

```text
g=gcd(n,ell c k),  r=n/g.
```

The position permutation has `g` cycles, each of length `r`.  An invariant
difference word is constant on each cycle.  Therefore its support size is a
multiple of `r`; write `k=rs`.  Choose the `s` nonzero cycles in `binom(g,s)`
ways.  Its zero-sum constraint is

```text
r(a_1+...+a_s)=0 in F_q.
```

If `q|r`, the constraint vanishes and there are `(q-1)^s` assignments.  If
`q` does not divide `r`, scalar cancellation reduces it to a nonzero
zero-sum tuple, counted by

```text
((q-1)^s + (q-1)(-1)^s)/q.
```

This proves C2, including the `s=0` term.  Möbius inversion then proves C3.
The verifier exercised 132 `q|r` branches, 5,280 `q not|r` branches, and
3,700 `r not|k` zero branches.  No characteristic boundary failed.

## Recovery and boundary audit

### Frozen odd-field claim

For odd `q` and `n>=3`, a unique-zero word with two changes exists: put one
zero at the required position and use one fixed nonzero symbol elsewhere.
A unique-zero word with three changes also exists: use the singleton zero
and two nonempty constant runs with distinct nonzero values.  This second
construction is precisely where oddness is used.

Every such admitted target forces its unique zero to positions

```text
z_2=-2c,  z_3=-3c.
```

Their difference is `c` modulo `n`.  No inversion of `2` or `3` is being
performed, so `2|n`, `3|n`, or `gcd(6,n)>1` creates no exception.  The test
included every `c` for odd-prime carriers through `(3,7)`, `(5,5)`, and
`(7,4)`; all `n` labelled atlases were distinct in every row.

The orientation qualification is essential.  Reflection
`J(w)_i=w_(-i)` satisfies

```text
J T_c = T_(-c) J.
```

Thus an atlas known only up to reflection cannot distinguish `c` from `-c`.
The frozen contract asks for a labelled atlas and is sound.

### Small and binary boundaries

- `n=1`: `c=0` is the only parameter; all `q` states map to zero.
- `n=2`: every nonconstant word has `k=2`, hence `ck=0 mod 2`; the maps and
  image atlases are independent of `c`, for odd `q` as well as binary `q`.
- `c=0`: `T(w)=w-w_0 1` is idempotent and fixes exactly the `q^(n-1)` words
  with coordinate zero equal to zero.
- `q=2`: every cyclic change count is even.  For odd `n`, the unique-zero
  `k=2` probe alone recovers `c` because multiplication by two is invertible.
  For even `n`, `c` and `c+n/2` define the same map; the exact atlas classes
  through `n=9` are recorded in `CANONICAL.txt`.  The scout deliberately
  makes no binary recovery claim, so this is a sharper ceiling, not a repair.

The functional graph alone still recovers `q` from its positive indegree and
then `n` from `|Y|=q^(n-1)`, including `n=1`.

## Primary-owner audit

### Direct owner of the quotient bridge

Darij Grinberg and Peter Mao, [*Necklaces over a group with identity
product*](https://arxiv.org/abs/2405.08937), v1 submitted in 2024 and current
v4 dated 2026, is much closer than the scout's owner log records.  Their
Theorem 7.1 studies “homogeneous necklaces,” namely tuples modulo cyclic
rotation and simultaneous left multiplication.  Their explicit bijection is

```text
Delta(a)_j = a_(j-1)^(-1) a_j,
```

from those orbits to identity-product necklaces, with cumulative products as
inverse.  For the additive group of `F_q`, this is exactly AQN's difference
map, global-translation quotient, zero-sum target, and rotation
intertwining.  The paper also records the earlier homogeneous-sequence
owners:

- N. J. Fine, [*Classes of periodic sequences*](https://doi.org/10.1215/ijm/1255381350),
  Illinois J. Math. 2 (1958), 285--302;
- E. N. Gilbert and J. Riordan,
  [*Symmetry types of periodic sequences*](https://doi.org/10.1215/ijm/1255631587),
  Illinois J. Math. 5 (1961), 657--665.

Grinberg--Mao does not state the literal endofunction `T_c`, so this is not an
exact-map priority hit.  It does, however, own the whole quotient/conjugacy
engine on which AQN's recurrent and inverse structure rests.

### Direct owners of the remaining ingredients

- F. Bianconi and E. Brugnoli,
  [*Enumerating necklaces with transitions*](https://doi.org/10.1017/S0004972721000307),
  Bull. Aust. Math. Soc. 105 (2022), 1--11, gives a closed-form treatment of
  necklaces refined by exactly the number of unequal cyclic adjacencies.
  AQN's `k` is that transition statistic.
- R. L. Rivest,
  [*The RC5 Encryption Algorithm*](https://doi.org/10.1007/3-540-60590-8_7)
  (1994/1995), explicitly foregrounds cyclic word rotations by
  plaintext-dependent amounts.  It owns the broad data-dependent-rotation
  mechanism, though not AQN's transition statistic or quotient.
- MacWilliams/single-parity-check enumerators own the nonzero zero-sum count;
  ordinary necklace theory owns rotation fixed counts and Möbius cycle
  extraction.

One source in the scout should **not** be described as a literal cyclic-word
rotation owner.  Høyer--Špalek,
[*Quantum Fan-out is Powerful*](https://doi.org/10.4086/toc.2005.v001a005),
uses `R_z(phi |x|)`, a one-qubit phase rotation whose angle is controlled by
Hamming weight.  It is useful broad context for statistic-controlled
operations, but it does not rotate the coordinates of the input word.
This correction does not weaken the kill because Rivest and, more
importantly, Grinberg--Mao supply the relevant ownership pressure.

Exact-expression searches for the full conjunction of support-of-cyclic-
difference, rotation by `c k`, and subtraction of the old first symbol found
no literal owner.  This negative result is not novelty evidence.

## Internal P1--P161 collision

P63, `rank-one-xor-inverse-radius`, is decisive.  Its Lemma 2.1 proves for an
arbitrary finite group that

```text
Delta_G(x)_i=x_i^(-1)x_(i+1)
```

has fibres exactly equal to global left-translation orbits.  Its proof
integrates equal derivatives in both directions, and its controls explicitly
include finite cyclic groups.  In additive `F_q` notation this is precisely
AQN's quotient and `q`-source engine.  AQN changes the finite carrier and adds
a state-dependent rotation plus a section, but it does not introduce a new
inverse mechanism.

Further proximity is nonfatal by itself but cumulative:

- P110 already records the even-transition obstruction for binary cyclic
  functions;
- P117 is a cyclic-word dynamics organized by transition/run strata;
- P98 already occupies noninvertible finite-field word maps with exact
  images/fibres, although its linear-algebra engine is different; and
- the P117--P121 crossing-rotation kill ledger already treats
  “rotation by an invariant statistic, then period by orbit-size/gcd” as an
  owned action reduction.

The scout's internal table omitted the strongest collision, P63, and stated
that no proof-engine transfer was detected.  That conclusion is not
sustainable.

## Theorem-mass assessment and claim ceiling

The literal theorem package is coherent and could be kept as an internal
exact-system note.  It should not consume a P162--P166 paper slot without a
new axis that survives the quotient reduction.

The maximum defensible frozen claim is:

> For the explicitly defined labelled map `T_c`, the difference quotient
> conjugates the recurrent restriction to transition-stratified rotations of
> the zero-sum code.  Choosing the state-dependent coordinate-zero section
> gives a depth-one functional graph with `q` sources per supported target,
> the displayed fixed-count specialization, a `t`-independent symbol-count
> polynomial, and odd-field labelled recovery of `c`.

Required zero-credit declarations for any reuse:

1. Grinberg--Mao/Fine/Gilbert--Riordan own the derivative/homogeneous-necklace
   quotient bridge.
2. P63 owns the exact derivative-fibre proof engine internally.
3. Transition-refined necklaces, data-dependent rotations, SPC weights,
   Burnside, and Möbius inversion are ingredients, not contributions.
4. Only the stratum-intersected image union is disjoint.
5. Only the weighted polynomial, not the source set, is independent of
   positive time.
6. Recovery is labelled/oriented; reflection sends `c` to `-c`.

## Executable evidence

The independent verifier imports no author/scout code.  It exhausts all
states for 98 configurations:

```text
q=2, 1<=n<=9;
q=3, 1<=n<=7;
q=5, 1<=n<=5;
q=7, 1<=n<=4;
all c in Z/nZ.
```

It checks the literal iterate, invariant, exact image, disjoint stratum
decomposition, raw-hyperplane countercontrol, every target at five positive
times, actual and predicted source sets, weighted polynomials, recurrent
predecessors and leaves, point periods, all change counts, fixed counts
through `2n+3`, both characteristic branches, recovery sets, reflection,
and small/binary boundaries.

```text
assertions:              1,606,561
status:                  PASS
two replay hashes:       55739b0c...1156fb6a
replays byte-identical:  yes
verifier SHA-256:         ce893736...9345c450
```

Full deterministic output is frozen in `CANONICAL.txt`.

## Final gate

```text
formula correctness  PASS
literal direct owner NO HIT IN BOUNDED PRIMARY SEARCH
residual theorem mass INSUFFICIENT AFTER OWNER SUBTRACTION
portfolio collision  P63 PROOF ENGINE; ADDITIONAL CYCLIC-WORD PROXIMITY
decision             KILL_OWNER_REDUCTION_AND_INTERNAL_PROOF_ENGINE_COLLISION
external             HOLD_EXTERNAL
```
