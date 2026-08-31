# Second nondivisor algebraic replacement scout

**Status:** internal discovery and hostile novelty gate only; **HOLD
EXTERNAL**.  The handles below are audit labels, not manuscript numbers.  No
novelty, priority, release, or submission claim is made.

**Search snapshot:** 2026-08-31 UTC.

## 1. Outcome first

This lane audited **21 genuinely new literal finite systems** after the
divisor/valuation/tent/annihilator lane was closed.  It did not re-enter any
divisor lattice, ideal power/colon/annihilator carrier, ordinary linear or
unipotent action, bare power map, generic finite-field polynomial iteration,
bounded-rank module-functor accident, or standard involution.  Its carriers
are:

- conjugacy types in symmetric groups, transformed by orbit partitions of
  characteristic subgroups of centralizers;
- block types transformed by characteristic subgroups of Young subgroups;
- the Boolean semigroup of binary relations;
- full finite transformation monoids; and
- the genuinely nonassociative seven-point Fano Steiner quasigroup.

The severe gate leaves:

- **one theorem-ready internal promotion on external owner hold:** `CT1`;
- **20 kills**; and
- no second algebraic slot.

The promoted object is not the already killed equal-part coagulation map.
For a permutation `sigma` of cycle type

```text
lambda = 1^(m_1) 2^(m_2) ...,
```

let `CT1(lambda)` be the partition of `n` formed by the orbit sizes of the
derived subgroup

```text
[C_(S_n)(sigma), C_(S_n)(sigma)]
```

on the original `n` points.  Since

```text
C_(S_n)(sigma) = product_j (C_j wr S_(m_j)),
```

the exact local factor rule is

```text
j^(m_j)  ->  1^j       if m_j = 1,
               j^2       if m_j = 2,
               (j m_j)   if m_j >= 3.                 (CT1.1)
```

Outputs from different `j` are then collected and sorted.  Thus `CT1`
simultaneously splits, preserves, and merges conjugacy-type blocks.  It is
not induced by powering a permutation, not a coordinatewise arithmetic map,
and not the old parallel equal-part merge.

The signal now has an all-weight proof spine.  Every orbit has eventual
period at most two, and a coloured-tag potential gives the honest universal
bound

```text
tail(lambda) <= 2 length(lambda) <= 2n.              (CT1.2)
```

This bound is deliberately **not claimed sharp**.  All **540,634** partitions
through weight 45 have maximum tail only six; the first weights attaining
maximum tails `0,1,2,3,4,5,6` are

```text
1, 2, 5, 9, 15, 30, 45.
```

The proof also classifies every fixed point and strict two-cycle and gives
ordinary generating functions for both classes.  The independent inverse
side remains the every-target one-step fibre coefficient in Section 4.2.
Thus the former proof hold is closed.  `CT1` receives
`PROMOTE_INTERNAL_THEOREM_READY_OWNER_HOLD`: the mathematics is coherent
enough for internal development, while priority, specialist ownership, and
external release remain unresolved.

## 2. Reproducible exact contract

[`verify_nondivisor_algebra.py`](verify_nondivisor_algebra.py) is
dependency-free.  Every displayed carrier is exhaustively enumerated.  There
is no floating point, random seed, sampling, network access, third-party
package, or timestamp in the executable.

Reproduce the frozen [`CANONICAL.txt`](CANONICAL.txt) with

```bash
cd docs/papers132_136_sequence/replacement_scout/nondivisor_algebra
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_nondivisor_algebra.py)
```

The 21-system ledger contains **686,367 parameter-labelled states**.  Focused
checks additionally enumerate all 540,634 partitions through weight 45 and
all 66,064 square relations of orders two through four.  The executable
makes **14,220,017 exact assertions** and returns `STATUS=PASS`.

The verifier has independent routes where a formula is retained:

1. `CT1` is computed once by (CT1.1) and again by a multivariate coefficient
   expansion for every target through weight 30;
2. the first and second derived-orbit rules are recomputed inside 18 literal
   permutation wreath products, not assumed from the partition code; and
3. the all-weight recurrent decoder and its fixed/two-cycle generating
   functions agree on every partition through weight 30, and the decoder
   itself agrees through weight 45; the tagged lift separately checks 118,634
   reachable coloured states and 56,961 instances of the two-clean-step
   lemma; and
4. the endpoint and depth of `R -> R R^T R` are computed once by Boolean
   multiplication and again by bipartite components and graph distances.

Enumeration is falsification evidence, not a proof for unbounded parameters
and not novelty evidence.

## 3. Permanent 21-system ledger

### 3.1 Centralizer and Young-subgroup orbit types

Every row was completely enumerated on all integer partitions of every
weight `1 <= n <= 30`, for 28,628 states per system.

| Handle | Literal self-map on partitions of `n` | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `CT1` | Orbit-size partition of the derived subgroup of `C_(S_n)(sigma)`. | All-weight period at most two; nonsharp tail bound `2n`; complete recurrent decoder and generating functions; one-step fibres as large as 415 in the common box. | **INTERNAL PROMOTION / EXTERNAL OWNER HOLD.**  Structural centralizer and wreath-commutator inputs are zero credit.  Residual value is only the tagged temporal theorem, recurrent census, and target-fibre transfer. |
| `CT2` | Orbit-size partition of the second derived subgroup of the same centralizer. | Periods `1,2`, maximum tail 4, at most 122 recurrent points, maximum fibre 1,511. | **KILL SIBLING.**  Same carrier and proof engine as `CT1`, with a weaker exact package. |
| `CT3` | Orbit-size partition of the solvable radical of the centralizer. | Fixed-only recurrence, maximum tail 4, up to 1,120 fixed points. | **KILL INTERNAL/OWNER.**  It is bounded-multiplicity Glaisher coagulation in group language. |
| `CT4` | Orbit-size partition of the center of the centralizer. | Tail at most one and maximum fibre two. | **KILL THIN.**  The sole change is `1^2 -> 2`; every other local class is unchanged. |
| `YT1` | Orbits of the derived subgroup of the Young subgroup `product_i S_(lambda_i)`. | Idempotent after one step; maximum fibre 16. | **KILL.**  Merely replaces every part 2 by two ones. |
| `YT2` | Orbits of the second derived Young subgroup. | Idempotent after one step; maximum fibre 91. | **KILL.**  Merely replaces every part 2 or 3 by ones. |
| `YT3` | Orbits of the solvable radical of the Young subgroup. | Idempotent after one step; maximum fibre 436. | **KILL.**  Merely splits parts at least 5 into ones. |
| `YT4` | Orbits of the center of the Young subgroup. | Idempotent after one step; only 16 fixed states at weight 30. | **KILL.**  Merely splits every part at least 3 into ones. |

### 3.2 Boolean relation semigroup

Each map was completely enumerated on all `2^(n^2)` relations for
`n=2,3,4`, or 66,064 states per map.  Composition is Boolean relation
composition and `T` denotes converse.

| Handle | Literal self-map | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `SR1` | `R -> R R^T R`. | Fixed-only recurrence, tail at most two; 2,100 fixed relations at order four.  Exact endpoint and clock are in Section 5.2. | **KILL DIRECT/INTERNAL.**  This is synchronous difunctional closure and has the same terminal geometry as the current asynchronous `BR1`. |
| `SR2` | `R -> (R R^T) intersect (R^T R)`. | Fixed-only, tail at most three, image size 113 at order four. | **KILL.**  Shallow meet of Green supports. |
| `SR3` | `R -> (R R^T) union (R^T R)`. | Same small image and depth range; maximum fibre 37,881. | **KILL.**  Join instead of meet does not create a temporal theorem. |
| `SR4` | `R -> R intersect (R R^T)`. | Fixed-only, tail at most three; 27,528 fixed order-four relations. | **KILL.**  One-sided support erosion with no stable fibre law. |
| `SR5` | `R -> R intersect ((R R^T) union (R^T R))`. | Fixed-only, tail at most three; 48,402 fixed order-four relations. | **KILL.**  Even shallower two-sided support test. |
| `SR6` | `R -> (R R^T)(R^T R)`. | Fixed-only, tail at most two; maximum fibre 34,889. | **KILL.**  Green-support product collapse. |

### 3.3 Full transformation monoids

The pair map was checked on all pairs in `T_2,T_3`; the triple maps on all
triples.  `TM5` was additionally checked on every element of `T_4`.

| Handle | Literal self-map | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `TM1` | `(f,g) -> (f g f, g f g)`. | 745 states; periods `1,2`, tail at most two. | **KILL.**  Standard sandwich words plus no all-`n` census or fibre theorem. |
| `TM2` | `(f,g,h) -> (f g, g h, h f)`. | 19,747 states; periods `1,2,3,6,24`, tail at most six. | **KILL DESPITE RECURRENCE.**  The long period at `T_3` is a finite word-map signal without a structural parameter law. |
| `TM3` | `(f,g,h) -> (f g h, g h f, h f g)`. | Periods `1,3`, tail at most four, maximum fibre 297. | **KILL.**  Generic cyclic word substitution. |
| `TM4` | `(f,g,h) -> (f g f, g h g, h f h)`. | Periods through six, tail at most five. | **KILL.**  No invariant, all-iterate normal form, or target-fibre law. |
| `TM5` | Send `f` to the idempotent selecting the least member of each kernel class. | Tail at most one; fixed counts `2,5,15` in degrees `2,3,4`. | **KILL THIN/ORDER-DEPENDENT.**  A chosen Green-class normal form, not dynamics. |

### 3.4 Nonassociative controls

Write the seven Fano points as the nonzero vectors of `F_2^3`, and define the
Steiner product by `x*x=x` and `x*y=x xor y` for `x != y`.  The executable
checks the Latin, commutative, idempotent, and Steiner identities directly.

| Handle | Literal self-map on `Q^3` | Exact pilot fingerprint | Hostile disposition |
|---|---|---|---|
| `FQ1` | `(x,y,z) -> (x*y,y*z,z*x)`. | All 343 triples; tail at most one, periods `1,3`, 175 recurrent states. | **KILL FIXED-CARRIER ACCIDENT.**  Nonlinear and not a group action, but only one seven-point carrier and no extensible theorem. |
| `FQ2` | `(x,y,z) -> ((x*y)*z,(y*z)*x,(z*x)*y)`. | Same period/tail census but different fibres, with maximum 25. | **KILL.**  A second Fano-table accident is not an independent family. |

## 4. `CT1`: all-weight theorem package and owner gate

### 4.1 Literal group reduction

Let `sigma` have `m_j` cycles of length `j`.  The classical centralizer
decomposition gives

```text
C_(S_n)(sigma) = product_j W_(j,m_j),
W_(j,m) = C_j^m semidirect S_m.
```

Put

```text
B_0 = {(a_1,...,a_m) in C_j^m : sum_i a_i = 0}.
```

Then

```text
W_(j,1)' = 1,
W_(j,2)' = B_0,
W_(j,m)' = B_0 semidirect A_m       for m >= 3.
```

Here is the complete factor proof, rather than an appeal to the pilot.  The
coordinate-sum map on the base and the sign map on `S_m` give an abelian
quotient, so

```text
W_(j,m)' <= B_0 semidirect A_m.
```

Conversely, commutators of a base translation with a transposition generate
all coordinate differences, hence all of `B_0`; commutators inside the top
copy of `S_m` generate its derived subgroup `A_m`.  Equality follows, with
the evident specializations `m=1,2`.

On the natural points `(block,coordinate)`, `B_0` is transitive inside each
block when `m>=2`: translate the chosen block and compensate in another.
For `m=2` there is no block permutation in the derived subgroup, giving two
orbits of size `j`.  For `m>=3`, `A_m` is transitive on the blocks, so the
whole factor is transitive.  For `m=1` the derived group is trivial.  Derived
subgroups commute with direct products, proving (CT1.1) for every `j,m`.
The verifier independently reconstructs these orbit sizes from literal
permutation multiplication and commutators in 18 wreath products, including
every threshold case `m=1,2,3,4,5`.

This reduction is mathematically correct but not itself contribution credit.
Centralizers of permutation types and their wreath decomposition are
classical, and commutator subgroups of wreath products are an established
subject.

### 4.2 Every one-step target fibre

For a target partition `mu=1^(r_1)...n^(r_n)`, introduce variables
`x_1,...,x_n`.  A source multiplicity at size `j` independently chooses:

```text
m_j=0: 1,
m_j=1: x_1^j,
m_j=2: x_j^2,
m_j>=3: x_(j m_j).
```

Mark source weight by `z`.  Therefore

```text
Phi_n(x_1,...,x_n)
 = [z^n] product_(j=1)^n
   (1 + z^j x_1^j + z^(2j) x_j^2
      + sum_(m=3)^floor(n/j) z^(jm) x_(jm)),          (CT1.3)
```

and the exact fibre is

```text
# CT1^(-1)(mu)
 = [x_1^(r_1) ... x_n^(r_n)] Phi_n.                  (CT1.4)
```

In particular, a target is in the image exactly when this coefficient is
positive.  This is an all-target identity, not an average.  The verifier
checks all **5,379** target cells through weight 30 by comparing the
coefficient expansion with literal partition enumeration.

The coefficient formula is exact inverse geometry, not an average or a
support-only statement.  It is nevertheless credited only as one member of
the package: no novelty value is assigned to formal product extraction by
itself.

### 4.3 All-weight temporal theorem

Lift an initial partition to coloured parts by giving every initial part a
different tag.  A split sends all resulting singleton parts the same tag; a
preserved pair keeps its tags; a merge replaces all participating tags by
their union.  Tags therefore form a coarsening partition of the initial tag
set.  Call a transition **crossing** when it merges two distinct current
tags, and let `c_t` be the number of current tags.  Then `c_t` never increases
and every crossing transition strictly decreases it.

The key invariant is stronger than tag monotonicity:

> For every current tag `T`, if `w(T)` is the total weight of its initial
> parts, then the pieces carrying `T` are either one part of size `w(T)`
> (the whole phase) or exactly `w(T)` singleton parts (the split phase).

This follows by induction directly from the three cases in (CT1.1).  In
particular, at a noncrossing transition:

- for each size at least two, one whole-phase tag of that size splits, while
  two such tags are preserved as a dimer; three would cross-merge;
- if the total singleton multiplicity is at most two, those singleton phases
  persist; and
- if it is at least three, noncrossing is possible only when all singleton
  pieces have one tag, in which case they merge back to its whole phase.

**Two-clean-step lemma.**  If two consecutive transitions are noncrossing,
the state after the first of them is periodic with period dividing two.

To prove the lemma, inspect the preceding phase rules.  Paired whole tags
stay paired.  A unique whole tag becomes the only possible large split tag
at the middle state and either returns on the next update (weight at least
three) or damps to a fixed split state (weights one or two).  A large split
tag at the first state becomes a unique whole tag at the middle state.  A
second clean transition forbids two distinct large split tags, forbids a
large split tag together with persistent singleton tags, and forbids a third
whole tag at any occupied size.  Hence the middle state is a disjoint union
of fixed dimers and singleton residue, together with at most two whole/split
oscillators in opposite phases.  Writing `H_a` for one whole tagged part of
mass `a` and `S_a` for its `a` tagged singletons, the only nonconstant middle
factors are explicitly

```text
H_a       <-> S_a,                 a>=3,
H_a + S_b <-> S_a + H_b,           a,b>=3,
```

while `H_j+H_j`, singleton residue of total at most two, and the damped
`S_2` factor are fixed.  Thus applying the update twice returns every tagged
piece to the middle state.  This proves the lemma without erasing the tags.

If the initial partition has `ell` parts, there are initially `ell` tags and
at most `ell-1` crossing transitions.  Before the recurrent part of an orbit,
every pair of consecutive transitions contains a crossing transition by the
lemma.  If the tail exceeded `2 ell`, its first `2 ell` transitions could be
grouped into `ell` consecutive pairs, each containing a crossing, which is
impossible.  Hence

```text
tail(lambda) <= 2 ell(lambda) <= 2n,
eventual period(lambda) in {1,2}.                    (CT1.2 revisited)
```

The argument gives a strict potential and a uniform clock, but **not the
sharp clock**.  The observed maximum tails through weight 45 are far smaller
than `2n`; no equality claim or formula for the maximum tail is made.

### 4.4 Complete recurrent decoder and census

Let

```text
Delta_D = product_(j in D) j^2
```

denote an arbitrary finite set of dimer sizes `D subset {2,3,...}`.  The
two-clean-step proof gives the following exhaustive, disjoint uncoloured
classification:

| Class | Exact recurrent object | Restrictions |
|---|---|---|
| `B` | fixed `1^e Delta_D` | `e in {0,1,2}` |
| `O1` | strict cycle `a Delta_D <-> 1^a Delta_D` | `a>=3`, `a notin D` |
| `O2=` | fixed `a 1^a Delta_D` | `a>=3`, `a notin D`; the two coloured oscillators swap but their uncoloured partition is unchanged |
| `O2!=` | strict cycle `a 1^b Delta_D <-> b 1^a Delta_D` | `3<=a<b`, `D` avoids `a,b` |

Indeed, on a coloured cycle there can be no crossing transition.  Whole tags
of an equal size either occur in persistent pairs or are oscillators.  At
most one oscillator can be in split phase, and at most one other can be in
whole phase; otherwise a future singleton class cross-merges.  A persistent
singleton cannot coexist with an oscillator for the same reason.  Amplitude
two is damping, not oscillatory.  These observations give exactly `B`, one
oscillator, or two antiphase oscillators, and prove both exhaustiveness and
the stated exclusions.  Thus this table is an immediate global decoder from
the multiplicities, not a bounded census.

For exact counts, put

```text
D(q)   = product_(j>=2) (1+q^(2j)),
D_A(q) = product_(j>=2, j notin A) (1+q^(2j)).
```

If `f_n` counts fixed points and `c_n` counts strict two-cycles once each,
then the classification gives the formal ordinary generating functions

```text
sum_(n>=0) f_n q^n
 = (1+q+q^2) D(q) + sum_(a>=3) q^(2a) D_{a}(q),      (CT1.5)

sum_(n>=0) c_n q^n
 = sum_(a>=3) q^a D_{a}(q)
   + sum_(3<=a<b) q^(a+b) D_{a,b}(q).                (CT1.6)
```

The recurrent-point count is `f_n+2c_n`.  At weight 30 these formulas give
`f_30=59`, `c_30=139`, and 337 recurrent points, exactly matching the literal
functional graph.  The verifier checks all coefficients through weight 30,
the decoder on every partition through weight 45, and the tagged lemma on
all 118,634 reachable coloured states arising through weight 30.

### 4.5 Exact owner subtraction

The following receive **zero credit**:

- Britnell and Wildon, [*Orbit coherence in permutation
  groups*](https://doi.org/10.1515/jgt-2013-0029), study orbit partitions in
  permutation centralizers and explicitly use the wreath-product
  decomposition.  Centralizer orbit-partition language is owned.
- Skuratovskii, [*Commutators of Sylow subgroups ... and commutator width in
  the wreath product of groups*](https://arxiv.org/abs/1812.10481), studies
  commutator subgroups in permutational wreath products.  The group-theoretic
  factor calculation is owned background.
- Eliahou and Erickson, [*Mutually describing multisets and integer
  partitions*](https://doi.org/10.1016/j.disc.2012.11.014), already study an
  iterated multiplicity-description system on partitions.  Generic
  multiplicity dynamics and short-cycle rhetoric are not new.
- Baalbaki, Bonanno, Del Vigna, Garrity and Isola,
  [*On integer partitions and continued fraction type
  algorithms*](https://doi.org/10.1007/s11139-023-00791-5), give a recent
  primary example of a weight-preserving partition self-map.  Merely putting
  a new map on `P(n)` is no novelty argument.
- The old internal `C5` map merges every equal-part class `j^m` to `jm`.
  Its logarithmic collision clock and distinct-part endpoint remain killed.
  `CT3`, not `CT1`, falls almost literally into that mechanism.

Searches for the exact phrases `orbit partition of the derived subgroup of a
permutation centralizer`, `derived centralizer orbit type symmetric group`,
and the three cases in (CT1.1) located no source printing this self-map or its
functional graphs.  This bounded non-hit is not a novelty certificate.  The
closest sources already own all structural ingredients, leaving only the
proved tagged temporal theorem, recurrent census, and inverse package as
possible residual value.

## 5. Why the other 20 systems die

### 5.1 The remaining type maps

The second-derived centralizer factor has the exact local rule

```text
j^m -> 1^(jm)  for m<=2,
       j^3     for m=3,
       (jm)    for m>=4.
```

It is correct and has real two-cycles, but it shares the entire carrier,
wreath reduction, coefficient-transfer method, and owner boundary with
`CT1`.  Carrying both would be cosmetic portfolio duplication, so `CT2` is
killed even before a fibre expansion.

For `CT3`, the solvable radical of `C_j wr S_m` is the full wreath product
for `m<=4` and its base `C_j^m` for `m>=5`.  Hence it merges an equal class
only when its multiplicity lies in `2,3,4`.  The observed depth comes from
repeated bounded equal-part merging; Glaisher/2048 ownership and the old `C5`
firewall are decisive.  `CT4` and all four Young maps are explicit one-step
block splits listed in the ledger.  They are useful negative controls, not
paper candidates.

### 5.2 `SR1` has an exact law and still gets zero credit

Put `B=R^T R`.  Direct associativity gives

```text
SR1^t(R) = R B^((3^t-1)/2).                           (SR1.1)
```

In the bipartite graph of `R`, this includes exactly the left-to-right pairs
joined by an alternating path of length at most `3^t`.  Its endpoint is the
complete biclique on each nontrivial connected component, and its exact depth
is

```text
ceil(log_3 D_cross(R)),                               (SR1.2)
```

where `D_cross` is the maximum finite distance from a left vertex to a right
vertex.  The verifier checks (SR1.2) on all 66,064 displayed relations.

These formulas do not rescue the map:

- Backhouse and Oliveira, [*On
  difunctions*](https://doi.org/10.1016/j.jlamp.2023.100878), identify
  difunctional relations by `R R^T R subset R` and as disjoint rectangles.
- Kahl, [*A Relation-Algebraic Approach to Graph Structure
  Transformation*](https://www.cas.mcmaster.ca/~kahl/Publications/RelRew/RelRew_TR2002-03.pdf),
  Definition 5.2.1, gives the least difunctional closure explicitly as
  `(R R^T)^* R = R (R^T R)^*`.
- The current replacement stochastic scout's asynchronous `BR1` already has
  the same endpoint plus every-target connected-bipartite reliability
  polynomial.  Synchronizing the clock cannot take a second slot.

Thus endpoint, recurrence, path law, and terminal geometry all receive zero
credit.  `SR2`--`SR6` are shallower Boolean combinations of row/column
supports.  Plemmons and West's [*On the Semigroup of Binary
Relations*](https://msp.org/pjm/1970/35-3/pjm-v35-n3-p23-p.pdf) and the later
finite-semigroup literature already own the Boolean-matrix/Green framework;
the pilots expose no residual temporal invariant.

### 5.3 Transformation words and the Fano controls

The full transformation monoid is an important natural carrier, but generic
short word substitution is not a theorem.  East, Egri-Nagy, Mitchell and
Peresse, [*Computing finite
semigroups*](https://doi.org/10.1016/j.jsc.2018.01.002), treat Green classes,
regularity and idempotents across transformation and other regular monoids.
Those structural notions receive zero credit here.

`TM2` is the best-looking false positive: `T_3^3` already contains a
24-cycle.  The same pilot also has several smaller periods and no stable
rank-only, kernel-only, or image-only classification.  A lone small-degree
period is not an all-family result.  `TM1`, `TM3`, and `TM4` have the same word
map problem; `TM5` is explicitly an order-dependent one-step normal form.

The Fano maps satisfy the user's non-group-action condition: their diagonal
is idempotent and their multiplication is not an affine group action.  They
still fail the family gate.  Moore's [*Quasilinear Cellular
Automata*](https://arxiv.org/abs/adap-org/9701001) already places quasigroup
and Steiner-system updates in an algebraic dynamics setting.  Our two maps
are fully solved only on the unique seven-point table, stabilize after one
tail step, and have no size parameter.  Both are killed.

## 6. P1--P131 and current-batch collision firewall

| This lane | Closest occupied material | Exact distinction and consequence |
|---|---|---|
| `CT1` versus P113 | P113 principal-hook iteration on the same integer-partition carrier | P113 regroups Ferrers cells into principal hooks and is driven by a Ferrers-gap increment with sharp depth `floor(n/2)`; `CT1` applies the multiplicity thresholds `1/2/>=3` induced by a centralizer-derived subgroup, has genuine two-cycles, and uses tag coarsening with only the nonsharp bound `2n`.  The literal maps and potentials differ, but the shared carrier plus fibre-product/clock package is a serious portfolio subtraction. |
| `CT1` versus P123 | P123 odd-component complementation on labelled graphs | P123 complements selected actual graph components and its component partition refines through a co-component/cotree mechanism.  `CT1` never complements a graph: the set-partition/tag lift is only a proof cover, its tag partition coarsens only on mergers, and its recurrent objects are whole/singleton oscillators.  No literal or theorem identity is imported from P123. |
| `CT1/CT2` versus other occupied type lanes | P105 permutation cycle-type pruning; P110 partition shift--join; old multiplicity-profile controls | The update uses a characteristic subgroup of the full permutation centralizer and is neither powering, deletion, nor a lattice shift--join.  `CT2` is killed as a same-engine sibling; only the complete `CT1` temporal/fibre package survives internally. |
| `CT3` | old `C5` parallel equal-part coagulation | The multiplicity window `2..4` changes the literal map but not the collision/coagulation mechanism.  **Kill internal.** |
| `CT4/YT1--YT4` | P105 pruning and generic block refinement | New group definitions collapse to one-step local block splits.  Literal difference has no theorem value. |
| `SR1` | P106 graph polarity, P123 component complementation, P127 looped-relation parity, current asynchronous `BR1` | The synchronous word is new, but its endpoint and inverse geometry are already occupied by `BR1` and externally by difunctional closure. |
| `SR2--SR6` | P106/P127 relation and Boolean-matrix lanes | No literal duplicate was found; all pilots nevertheless reduce to shallow Green-support combinations. |
| `TM1--TM5` | P111 positive matrix semigroup, P112 reset semigroups, prior single-sandwich and `(xy,yx)` controls | These are new multi-state word maps on `T_n`, not the occupied systems.  Generic semigroup words without a parameter-uniform classification remain below threshold. |
| `FQ1/FQ2` | prior Alexander-quandle braid control | The Fano operation is genuinely nonaffine and is not a group action.  Its fixed seven-point carrier, rather than an internal collision, kills it. |

The four other current replacement scouts were also searched.  The only
direct current-batch collision is `SR1` with asynchronous `BR1`; it is
recorded as a kill, not hidden as a thematic similarity.  No divisor,
valuation, tent, annihilator, ideal-power, finite-field generic-polynomial,
or bounded-rank functor mechanism was reintroduced.

## 7. Bounded current primary-owner search log

| Candidate family | Representative literal queries | Closest primary material located | Consequence |
|---|---|---|---|
| `CT1/CT2` | `orbit partition derived subgroup centralizer permutation`; `commutator subgroup C_j wreath S_m orbits`; `derived centralizer orbit type symmetric group`; exact three local cases | Britnell--Wildon centralizer orbit partitions; wreath-commutator papers; partition multiplicity dynamics | structural formula is owned background; exact self-map, tagged theorem, decoder, and functional graph were not located; **theorem-ready internal / owner hold**, never “novel” |
| `CT3/CT4` | `solvable radical centralizer symmetric group cycles`; `center of permutation centralizer orbits` | standard characteristic-subgroup and wreath decompositions; Glaisher/equal-part merging neighbors | exact local rules are elementary corollaries; **kill** |
| `YT1--YT4` | `orbit partition derived Young subgroup`; `center Young subgroup orbits` | standard derived series `S_n'`, `A_n'`, centers and radicals | one-step identities; **kill** |
| `SR1` | `R R inverse R iteration`; `A A transpose A Boolean matrix`; `least difunctional closure` | Backhouse--Oliveira; Kahl; classical Boolean-relation semigroup papers | direct owner plus current internal collision; **kill** |
| `SR2--SR6` | exact Boolean products with `RR^T` and `R^TR`; `Green relations Boolean matrices` | Plemmons--West; modern finite-semigroup computation | mature structure, shallow pilots; **kill** |
| `TM1--TM5` | `full transformation monoid mutual sandwich dynamics`; exact cyclic word tuples; `kernel idempotent selector` | transformation variants, Green classes, idempotent-generated semigroups | no exact temporal hit, but also no theorem spine; **kill rather than infer novelty from absence** |
| `FQ1/FQ2` | `Steiner quasigroup dynamics cyclic product`; exact Fano triple maps | quasigroup/Steiner cellular automata and quasigroup dynamics | fixed-carrier controls only; **kill** |

Only primary papers, author manuscripts, and exact mathematical
documentation were used for ownership decisions.  Search-result absence is
never recorded as novelty, and bibliographic coverage is not claimed to be
exhaustive.

## 8. Final ranked gate

| Rank | Handle | Mathematical status | Gate |
|---:|---|---|---|
| 1 | `CT1` | Exact centralizer-derived type rule; all-weight period at most two and tail at most `2n`; complete recurrent decoder/OGFs; every-target one-step fibre | **INTERNAL PROMOTION / EXTERNAL OWNER HOLD.**  The former proof hold is closed; require specialist ownership review and a value decision before any allocation or release. |
| 2 | `CT2` | Correct second-derived sibling with real two-cycles | **KILL PORTFOLIO DUPLICATE.**  Do not carry two centralizer-derived partition maps. |
| 3 | `SR1` | Exact all-iterate path law and sharp clock | **KILL OWNER/INTERNAL.**  Difunctional closure and current `BR1` consume it. |
| 4--21 | all others | Exact negative evidence, one-step identities, or small-carrier anomalies | **KILL.** |

The honest result is therefore **one theorem-ready internal lead on owner
hold, not an externally cleared paper**.  Its residual contract is precise:
the tagged all-weight dynamics, complete recurrent census, and target-wise
inverse product after all centralizer/wreath and generic partition-dynamics
background is subtracted.  A specialist locating a direct owner of that
residual package should kill the lead; the lane must not retreat to a
divisor, relation-closure, or equal-part-coagulation variant.

## 9. AI-assistance disclosure and limitations

Candidate generation, code, bounded web search, and this report were produced
with AI assistance.  The executable is the exact audit trail.  It does not
prove unbounded claims, establish bibliographic priority, replace specialist
group/partition review, or justify external release.
