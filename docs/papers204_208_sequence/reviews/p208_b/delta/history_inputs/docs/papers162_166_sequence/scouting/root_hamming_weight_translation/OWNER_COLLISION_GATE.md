# Owner and internal-collision gate

**Outcome: `GREEN_OWNER_THIN / HOLD_EXTERNAL`.**  This is a bounded search
record, not proof of novelty, priority, or freedom to publish.

## 1. Literal and structural repository audit

The repository-wide audit searched Markdown, TeX, and Python sources for the
literal rule and for structural aliases including

```text
Hamming-weight translation
weight-dependent translation
x + wt(x) 1
translate by support size / cardinality
histogram dynamics
i+c_i mod n
parking functions / circular compositions / siteswap / juggling
```

No previous paper or scout states the literal family

```text
(Z/nZ)^n -> (Z/nZ)^n, x -> x+w(x)1
```

or the depth formula in the theorem contract.  The closest hits were the
killed adaptive-action controls `HWR`, `SVT`, `CLT`, `AQN`, and `XCT`, plus
occupied P63/P78/P96/P126/P162.  They are compared below.

## 2. Public owner audit

### Exact binary boundary

Meyer and Pommersheim,
[*Single query learning from abelian and non-abelian Hamming distance
oracles*](https://arxiv.org/abs/0912.0583), Chicago Journal of Theoretical
Computer Science (2010), define

```text
hat(x)=x       if wt(x) is even,
hat(x)=bar(x)  if wt(x) is odd.
```

On a binary word this is `x+(wt(x) mod 2)1`.  It is exactly the present
coupled family only at the isolated boundary `n=2`, where alphabet size and
word length are both two.  Therefore the `n=2` permutation is directly owned
and receives zero contribution credit.  The source does not study alphabet
`Z/nZ`, length `n`, the histogram maps, or the all-`n` depth/fibre formulas.

### One-ball siteswaps: direct owner of the recurrent histogram slice

Buhler, Eisenbud, Graham, and Wright,
[*Juggling Drops and Descents*](https://doi.org/10.1080/00029890.1994.11996984),
American Mathematical Monthly 101 (1994), 507--519, give the siteswap landing
criterion: a nonnegative period-`n` sequence `a` is valid precisely when
`i -> i+a_i mod n` is a permutation, and its mean is the number of balls.
For a histogram `c` with `sum c_i=n`, the recurrent condition for every phase
is therefore exactly the one-ball siteswap slice.  Its gap-vector description
and the count `2^n-1` of such histograms receive zero contribution credit.

This is substantial but not a direct owner of the endofunction outside its
permutation slice.  It does not give the transient depth formula, the
multinomially lifted least-period census on labelled words, or target fibres
of the original Hamming-weight map.

### Parking/occupancy and circular shift background

Konheim and Weiss,
[*An Occupancy Discipline and Applications*](https://doi.org/10.1137/0114101),
SIAM Journal on Applied Mathematics 14 (1966), 1266--1274, is foundational
for parking functions and linear-probing occupancy.  Kenyon and Yin,
[*Parking functions: From combinatorics to probability*](https://arxiv.org/abs/2103.17180),
record the circular simultaneous-translation argument and histogram
specifications.  These sources own the generic occupancy histogram and
circular-orbit language.  They do not state the update `x -> x+w(x)1` or its
functional graph.

Meyles, Harris, Jordaan, Kirby, Sehayek, and Spingarn,
[*Unit-Interval Parking Functions and the
Permutohedron*](https://arxiv.org/abs/2305.15554), directly records the
Fubini/ordered-Bell enumeration in a parking-function setting.  Stirling
numbers, surjection sums, Fubini numbers, and their exponential generating
functions are treated here as classical enumeration and receive zero credit.

### Statistic-controlled actions

Hoyer and Spalek,
[*Quantum Fan-out is Powerful*](https://theoryofcomputing.org/articles/v001a005/v001a005.pdf),
Theory of Computing 1 (2005), 81--103, compute a one-qubit phase rotation
whose angle is controlled by Hamming weight.  This is broad precedent for a
weight-controlled operation, not a coordinate rotation and not the present
alphabet translation.  The distinction corrects overbroad wording in an
older internal scout.

Exact-expression searches through 2026-09-03 for the literal map, the phase
map with total mass `n`, and the conjunction of its Stirling depth census and
target-multiplicity fibres found no primary direct owner.  A bounded non-hit
is not novelty evidence.

## 3. Internal P1--P165 firewall

| comparator | occupied mechanism | decisive separation / subtraction |
|---|---|---|
| P63, rank-one XOR inverse radius | the finite-group derivative forgets exactly global alphabet translation | the free diagonal action is zero-credit background; HWT uses its changing histogram to build a noninvertible phase endofunction, not a derivative quotient or inverse-radius theorem |
| P78, complete-bipartite sandpile translations | fixed group translation, uniform cycles, zeta | HWT is state-dependent, has nonuniform periods and tails through `n-2`, and has nonuniform target fibres |
| P96, finite-subset circle expansion | cyclic orbit unions, fixed counts, zeta, temporal Möbius census | different carrier and literal map; HWT's depth and inverse formulas are multinomial occupancy statements, not an induced expanding-circle hyperspace action |
| P126, balanced composition refinement | ordered compositions, a sharp clock, every-iterate image and fibre products | HWT's weak histogram composition is an orbit coordinate only; its map is `i->i+c_i`, recurrent periods are nontrivial, and its inverse theorem is on labelled modular words |
| P162, random translation intersection | translations plus a target-stabilizer source/history polynomial | HWT is deterministic and its fibres test target symbol multiplicities; no stabilizer, erosion, random-rank, or history-span proof transfers |
| killed `HWR/SVT/CLT` | an invariant statistic freezes a cyclic rotation or alphabet translation, leaving action-only cycles and singleton fibres | Hamming weight is not invariant under HWT; the changing statistic produces the sharp `n-2` transient tower and nonuniform fibres |
| killed `AQN` | cyclic difference quotient, transition-stratified rotation, depth at most one | HWT has no difference code or section; P63's quotient engine does not prove its mass-exhaustion or target-multiplicity formulas |
| killed `XCT` | translate a subset by XOR centroid; translation stabilizers control fibres | HWT acts on modular words, has all periods and linear-height tails, and its inverse is a marked occupancy condition rather than a subgroup-stabilizer filter |

The generic diagonal quotient, finite-map zeta conversion, multinomial
histogram lift, and classical Stirling identities are explicitly subtracted.
No internal proof engine supplies both the exact depth census

```text
d! sum_s binom(n,s)S(s,d)(n-d-1)^(n-s)
```

and the arbitrary-target marked exponential fibre polynomial.

## 4. Decision and kill switch

The candidate passes only at `GREEN_OWNER_THIN` because one full recurrent
slice is classical one-ball siteswap theory and the `n=2` literal map is
owned.  What remains after subtraction has three coherent pieces:

1. all-parameter histogram functional graphs and exact labelled least-period
   counts;
2. a sharp full transient census, including equality structure and the last
   layer; and
3. an independent every-target inverse criterion and complete fibre-size
   polynomial.

This exceeds a simple reduction or action-only construction.  Nevertheless,
a direct source for the literal all-`n` conjunction or an internal proof
transfer not located here changes the verdict immediately to `KILL`.
Maintain `HOLD_EXTERNAL`.
