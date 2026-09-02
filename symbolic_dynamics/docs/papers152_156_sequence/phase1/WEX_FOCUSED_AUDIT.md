# WEX focused proof and owner audit

**Decision:** `RESERVE_NO_FREEZE` (`HOLD_EXTERNAL`).  The original clock
contract is false.  The exact all-rank image and target-fibre axes survive,
and the size-only Fibonacci clock has not been falsified, but its repaired
all-parameter proof gate remains open.  This document makes no novelty,
priority, authorship, or paper-number claim.

## 1. Literal map and notation

For `pi in S_n`, let

```text
W(pi) = std(pi_i : pi_i >= i),
d(pi) = max_i(i-pi_i),
tau(pi) = min{t : W^t(pi) is an identity permutation}.
```

The map is rank-decreasing away from the identity.  The focused question was
the proposed drop-compression lemma

```text
tau(W(pi)) <= M(d(pi)),
M(D)=max_{rho in S_D} tau(rho),  M(0)=0.                 (C5)
```

It is false at source rank 11.

## 2. Exact counterexample to the old clock package

Take

```text
pi = (11,10,9,4,1,2,3,8,5,6,7).
```

Its weak-excedance positions and values are

```text
P = {1,2,3,4,8},       A = {4,8,9,10,11}.
```

The selected word is `(11,10,9,4,8)`, hence

```text
W(pi) = (5,4,3,1,2).
```

Every deficient entry of `pi` has drop four:

```text
5-1 = 6-2 = 7-3 = 9-5 = 10-6 = 11-7 = 4,
```

so `d(pi)=4`.  The target orbit is

```text
(5,4,3,1,2) -> (3,2,1) -> (2,1) -> (1),
```

and therefore `tau(W(pi))=3`.  Literal enumeration gives `M(4)=2`.
Consequently

```text
tau(W(pi)) = 3 > 2 = M(d(pi)).
```

The same source has `tau(pi)=4` and `d(pi)=4`, contradicting the proposed
pointwise implication `tau(pi)>=4 => d(pi)>=F_5=5`.  Thus both C5 and the
pointwise Fibonacci **drop** axis are withdrawn, not repaired by a wording
change.

## 3. Exact U/D/F/X scheduler

The counterexample was not found by random sampling.  It comes from an exact
preimage scheduler that also provides the exhaustive boundary test.

Fix a target `sigma in S_m`.  Let `P={p_1<...<p_m}` be the selected positions
and `A={a_1<...<a_m}` the selected values in a source of rank `n`.  At each
coordinate write

| letter | coordinate membership | queue action |
|---|---|---|
| `U` | `P` only | open a complement value |
| `D` | `A` only | close at a complement position |
| `F` | both `P` and `A` | neither |
| `X` | neither `P` nor `A` | close the oldest value and open the current one |

The `i`th selected position receives `a_{sigma_i}`.  Hence the only cross-chain
precedence constraints are

```text
p_i <= a_{sigma_i}  for every i.                         (S1)
```

Equivalently, the event `A_j` may occur only after `P_{sigma^{-1}(j)}`, with
equality allowed in an `F` step.

### Why FIFO is exact

Let complement values be `B={b_1<...<b_h}` and complement positions be
`Q={q_1<...<q_h}`.  Suppose some matching assigns every complement value below
its position with drop at most `D`.  Then the increasing matching also works:

- the values matched to the first `j` positions show `b_j<q_j`; and
- the positions matched to the first `j` values show `q_j<=b_j+D`.

Thus sorting the matching cannot increase its bottleneck drop.  Conversely, a
precedence-respecting schedule with every FIFO waiting time at most `D`
constructs a literal source by assigning `a_{sigma_i}` at `p_i` and matching
`b_j` to `q_j`.  This proves, for all parameters,

```text
there is p in S_n with W(p)=sigma and d(p)<=D
iff
there is a length-n U/D/F/X schedule for sigma with FIFO delay <=D.   (S2)
```

For the counterexample the schedule is

```text
UUUFXXXFDDD.
```

It has `P={1,2,3,4,8}`, `A={4,8,9,10,11}`, complement values
`B={1,2,3,5,6,7}`, and complement positions `Q={5,6,7,9,10,11}`.  The FIFO
pairs are

```text
1->5, 2->6, 3->7, 5->9, 6->10, 7->11,
```

all of delay four.

### A useful strict-drop consequence

If `sigma_i=i-k` realizes `d(sigma)=k>0`, then at the occurrence of `P_i`,
the event `A_{i-k}` has not occurred earlier.  Immediately before that
coordinate there are at least `k` open FIFO values, all opened at distinct
earlier coordinates, and no complement value can close at a coordinate
containing `P_i`.  The oldest therefore waits at least `k+1` steps.  From (S2),

```text
W(p)=sigma nonidentity  =>  d(p)>=d(sigma)+1.             (S3)
```

Iterating (S3) gives the valid, weaker all-parameter statement
`d(sigma)>=tau(sigma)`.

## 4. Exhaustive falsifier boundary

The independent verifier does not enumerate `S_11`.  It uses (S2) as an exact
branch-and-bound state space.

1. It cross-checks scheduler minimum drop against every literal target,
   including zero fibres, through source rank seven: 5,913 literal sources and
   6,985 target checks.
2. It enumerates every source with drop at most one through rank eleven (2,047
   sources), closing the only target-tail-one failure mode.
3. By (S3), a nonidentity target of a source of rank at most eleven and target
   tail at least two has target rank at most nine.  Every such target is
   enumerated.
4. For each target and each possible source rank, the scheduler tests the
   exact forbidden delay threshold: `2` for target tail two, `4` for tail
   three, and `7` for tail four.  There are 13,402 exact schedule decisions.

There is no compression counterexample through source rank ten.  At rank
eleven there is exactly one failing **target** in this search,
`(5,4,3,1,2)`, with canonical schedule `UUUFXXXFDDD`.  “One target” is not a
claim that the displayed literal source is the only source in its fibre.

The complete cold replay reports 2,442,478 assertions and
`PASS_EXPECTED_FALSIFICATION`.

## 5. What remains of the Fibonacci clock

The counterexample kills the drop axis but does **not** falsify the size-only
conjecture

```text
max_{pi in S_n} tau(pi) = max{t : F_{t+2}<=n}.            (Csize)
```

The exact maxima through rank nine remain

```text
0,1,2,2,3,3,3,4,4,
```

and the sharp witnesses have `(rank,drop,tail)`

```text
(1,0,0), (2,1,1), (3,2,2), (5,3,3), (8,5,4), (13,8,5).
```

The exact minimum of `rank+drop` at tails zero through four is

```text
1,3,5,8,13.
```

This suggests a viable repaired induction, but the required all-size lemma is
not yet proved.  Put `q=W(p)`, `h=|p|-|q|`, and

```text
K(p,q) = d(p)+h-d(q).                                    (R1)
```

The repaired gate would be

```text
tau(q)>=t  =>  K(p,q)>=F_{t+2}.                           (R2)
```

It survives 382,671 nontrivial exact checks through source rank nine.  It also
handles the counterexample: `K=4+6-3=7>=F_5=5`.  If (R2) had a deductive
proof, simultaneous induction on

```text
|q|>=F_{t+2},             |q|+d(q)>=F_{t+3}
```

would close (Csize), because

```text
|p|      >= |q|+d(q),
|p|+d(p) = (|q|+d(q))+K(p,q).
```

The FIFO formalism makes (R2) a precise target, but this audit did not obtain
the required all-parameter skeleton or a counterexample.  Finite survival is
not a proof.  Therefore the proper decision is

```text
KILL old C5 and pointwise drop theorem;
RESERVE size-only clock pending proof of R2 (or another all-size argument).
```

It is not `PASS_FREEZE`.

Two tempting shortcuts are already false.  First, the proposed global fibre
tradeoff

```text
h+d(p) >= |q|+d(q),  q=W(p),                              (Rbad)
```

fails at `p=(1,4,3,2)`, where `q=(1,3,2)`, `h=1`, and the
two sides are `3<4`.  It still fails after requiring target tail at least two:

```text
p=(1,6,5,4,2,3), q=(1,4,3,2), tau(q)=2,
h=2, d(p)=3, |q|=4, d(q)=2, so 5<6.
```

Second, deleting direct-sum identity components does not repair (Rbad).  For

```text
p=(7,2,5,4,1,6,3), q=W(p)=(5,1,3,2,4),
```

the target `q` is sum-indecomposable and has tail two, yet
`h+d(p)=2+4=6<5+2=|q|+d(q)`.  Thus neutral mass can lie inside a
sum-indecomposable component.  Replacing `|q|` by an undefined “essential
rank” merely moves the proof obligation: an all-parameter core selector
compatible with every iterate would still have to be constructed.  No such
selector is asserted here.

## 6. Surviving exact axes

The focused counterexample does not affect the two closed one-step theorems.

### Images and right sections

For `sigma in S_m` and `n>=m`,

```text
sigma in W(S_n) iff n>=m+d(sigma).
```

Necessity follows from `i<=p_i<=a_{sigma_i}<=n-m+sigma_i`.  For
`h=n-m`, the word

```text
(sigma_1+h,...,sigma_m+h,1,...,h)
```

is an explicit right section whenever `h>=d(sigma)`.

### Target-resolved fibres

For selected value and position sets `A={a_1<...<a_m}` and
`P={p_1<...<p_m}` satisfying `p_i<=a_{sigma_i}`, let
`B=[n]\A` and `Q=[n]\P={q_1<...<q_h}`.  The number of deficient complement
matchings is

```text
prod_{j=1}^h (#{b in B:b<q_j}-(j-1)),
```

zero when a factor is nonpositive.  Summing this over admissible `(A,P)` gives
the exact fibre of every target, including zero fibres.

These axes remain `PASS_MATHEMATICALLY`, but without a proved temporal axis
they are held as reserve material rather than promoted to a batch slot.

## 7. Owner-first citation-chain subtraction

### Direct exact-map searches

The following families of queries were run against primary/journal/arXiv
records:

```text
"weak excedance subword" permutation map iteration
"increasing subword of weak excedance letters"
"retain" weak excedance letters permutation standardization
"standardized" "weak excedance" subword
"weak excedance" deletion permutation standardization
iterated weak excedances permutation transform
permutation weak excedance subword map
```

The bounded search did not retrieve the exact iterated standardized map, its
all-rank images, or its target-resolved fibres.  This non-hit is not evidence of
novelty or clearance.

### Exact static collision: identity basin

Fufa Beyene, Jörgen Backelin, Roberto Mantaci, and Samuel A. Fufa,
*Set Partitions and Other Bell Number Enumerated Objects*, Journal of Integer
Sequences 26 (2023), Article 23.1.8, official article and source:

- <https://cs.uwaterloo.ca/journals/JIS/VOL26/Beyene/beyene13.html>
- <https://arxiv.org/abs/2101.07074>

define the rightmost-letter subword of a transposition array, identify its
order behaviour with the weak-excedance-letter subword, and prove in Theorem 27
that permutations whose weak-excedance-letter subword is increasing are counted
by the Bell number.  In WEX language this owns the aggregate one-step identity
basin

```text
sum_m |W_n^{-1}(id_m)| = B_n.
```

That Bell enumeration and the transposition-array proof receive zero credit.
The target-rank refinement and nonidentity target fibres are not stated there,
but any future use must cite and subtract Theorem 27 explicitly.

The citation chain in that paper points to Jean-Luc Baril,
*Statistics-preserving bijections between classical and cyclic permutations*,
Information Processing Letters 113 (2013), 17--22,
<https://doi.org/10.1016/j.ipl.2012.10.003>, for the transposition-array/weak-
excedance interface, and to Baril,
*Gray code for permutations with a fixed number of cycles*, Discrete
Mathematics 307 (2007), 1559--1571,
<https://doi.org/10.1016/j.disc.2006.09.007>, for transposition arrays.  Those
coding facts also receive zero credit.

### Other mandatory static subtraction

- Richard Ehrenborg and Einar Steingrímsson, *The Excedance Set of a
  Permutation*, Advances in Applied Mathematics 24 (2000), 284--299,
  <https://doi.org/10.1006/aama.1999.0671>: excedance-set enumeration.
- Fan Chung, Anders Claesson, Mark Dukes, and Ronald Graham, *Descent
  polynomials for permutations with bounded drop size*, European Journal of
  Combinatorics 31 (2010), 1853--1867,
  <https://doi.org/10.1016/j.ejc.2010.01.011>,
  <https://arxiv.org/abs/0908.2456>: maximum drop and bounded-drop
  enumeration.
- Joanna N. Chen and William Y. C. Chen, *On permutations with bounded drop
  size*, European Journal of Combinatorics 54 (2016), 138--153,
  <https://doi.org/10.1016/j.ejc.2015.12.008>,
  <https://arxiv.org/abs/1306.5428>: bounded-drop bijections and unimodality.
- Einar Steingrímsson and Lauren K. Williams, *Permutation Tableaux and
  Permutation Patterns*, <https://arxiv.org/abs/math/0507149>: weak-excedance
  tableau structure.
- Nantel Bergeron, *The excedance quotient of the Bruhat order,
  quasisymmetric varieties, and Temperley--Lieb algebras*,
  <https://arxiv.org/abs/2302.10814>: weak-excedance position/value classes.

### Portfolio firewall

P149 owns endpoint-local peak extraction, alternating packing, peak right
sections, and zigzag/pinnacle fibres.  WEX shares the broad rank-varying
permutation subsequence-standardization carrier, which receives zero credit.
Its diagonal predicate, maxdrop image obstruction, deficient-board fibres, and
FIFO scheduler are different mechanisms; this difference is a collision
firewall, not a novelty claim.  Given that the portfolio already contains P149,
WEX must retain a proved independent temporal axis before promotion.

## 8. Final ledger

| item | focused result | disposition |
|---|---|---|
| old drop-compression C5 | explicit rank-11 counterexample | `KILL` |
| pointwise Fibonacci drop bound | same counterexample | `KILL` |
| size-only Fibonacci clock | exact support; repaired gate R2 open | `RESERVE_UNPROVED` |
| all-rank image/right section | proof unchanged | `PASS_RESERVE` |
| every-target fibre | proof unchanged; identity aggregate owner subtracted | `PASS_RESERVE` |
| U/D/F/X scheduler | all-size equivalence proved; exact falsifier engine | `PASS_TOOLING` |
| exact-map ownership | bounded non-hit only | `NO_NOVELTY_INFERENCE` |
| WEX paper slot | temporal contract not closed | `RESERVE_NO_FREEZE` |

External state remains `HOLD_EXTERNAL`.
