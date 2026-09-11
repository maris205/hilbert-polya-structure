# Root-coordinator crossover lane — fixed candidate denominator

This file freezes sixteen literal systems before promotion.  A row is one
system, not one cutoff, parameter choice, complement, or rerun.  The lane
mixes arithmetic words, set maps, transformation semigroups, relations, and
finite-group subset maps so that a failure in one family does not consume the
round.  Exact checks are counterexample pressure only.

| id | carrier | literal update | intended signal |
|---|---|---|---|
| RC01 CDQ | divisor words `D(N)^m` | `x_i <- x_i/gcd(x_i,x_{i+1})`, cyclically | primewise positive differences; finite sharp clock; coprime-neighbour fixed locus; every-target transfer-matrix fibre |
| RC02 CGS | divisor words `D(N)^m` | `x_i <- gcd(x_i,x_{i+1})`, cyclically | sliding gcd windows; exact tail from gaps between valuation minima; terminal-target depth enumerator |
| RC03 SCT | subsets `A subseteq [n]` | `A <- A intersect [|A|]` | self-cardinality rank iteration; sharp height; every-target first-step and terminal fibres |
| RC04 SCE | subsets `A subseteq [n]` | `A <- A union [|A|]` | expansion analogue of RC03 |
| RC05 LSS | subsets of a finite group `G` | `A <- {g:gA=A}` | left-setwise stabilizer; idempotence; image/fixed subgroups; subgroup-poset fibre inversion |
| RC06 PSQ | permutations of `[n]` | `pi <- pi^2` | cycle-type tail/period and square-root fibres |
| RC07 EFS | endofunctions `[n]->[n]` | `f <- f^2` | functional-graph height, cyclicity, and power-semigroup dynamics |
| RC08 RTC | binary relations on `[n]` | `R <- R union (R circle R)` | dyadic transitive closure clock |
| RC09 RSQ | binary relations on `[n]` | `R <- R circle R` | Boolean relation-power dynamics |
| RC10 CBE | subsets of the cycle `C_n` | keep `i` iff `i in A` and `i+1 notin A` | cyclic right-boundary extraction and independent-set image |
| RC11 IMN | words in `(Z/nZ)^n` | coordinate `j` becomes the multiplicity of symbol `j`, modulo `n` | inventory-vector functional graphs |
| RC12 UCD | divisors `d|N` | `d <- gcd(d,N/d)` | primewise unitary-core folding |
| RC13 CPT | subsets `A subseteq [n]` | toggle the prefix `[|A|]` | cardinality-feedback prefix dynamics |
| RC14 HSR | subsets of `Z/nZ` | translate by current cardinality | cardinality-preserving rotation |
| RC15 SGC | subsets of a finite group `G` | `A <- <A>` | subgroup-generation closure and exact generating-set fibres |
| RC16 CNS | subsets of a finite group `G` | `A <- {g:gAg^{-1}=A}` | conjugation stabilizer followed by a normalizer tower |

## Frozen pilot boxes

- RC01: exponent alphabets `0..a`, `2<=m<=6`, `1<=a<=3`.
- RC02: exponent alphabets `0..a`, `2<=m<=7`, `1<=a<=3`.
- RC03/04/10/13/14: all subsets through the script-declared cutoffs.
- RC05/15/16: complete subset spaces of cyclic groups through order eight,
  plus `S_3` and the order-eight dihedral group where declared.
- RC06: every permutation through degree seven.
- RC07: every endofunction through degree five.
- RC08: every relation through order four; RC09 through order three.
- RC11: every word through alphabet/length six where runtime permits; RC12:
  every exponent through the declared range.

The boxes were chosen before observing the final summary.  Passing them does
not prove a theorem, validate a subclass, or establish ownership.
