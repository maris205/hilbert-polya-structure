# Independent hostile gate — combinatorial finalists PM1 and GR1

**Status:** Stage-1 owner/value audit; **HOLD EXTERNAL**.  `PM1` and `GR1`
are scout labels, not paper numbers.  This file neither assigns a paper number
nor makes a novelty, priority, or publication claim.

**Evidence cutoff:** 2026-08-31 UTC.  The audit used primary papers and
publisher/author/arXiv full texts.  Search non-hits are reported only as
bounded non-hits; they are never treated as novelty evidence.

## 1. Gate decision

| Scout finalist | Hostile decision | Controlling reason | Residual status |
|---|---|---|---|
| **PM1**, simultaneous concatenation of consecutive canonical permutation cycles | **KILL (current contract)** | The endpoint is exactly the established parenthesis-erasure/`Flatten` map, the local merge is an explicitly published deletion of `)(` and a classical cut--join, and the cycle-length evolution is ordinary composition coarsening.  The only non-hit is the deterministic adjacent-pair scheduler; its current consequences are generic list-compaction consequences. | **No present paper contract.**  A narrowly specified all-time fibre program may re-enter, but none of the current clock/Stirling/terminal-cut claims is enough. |
| **PM1 with every arity `b>=2`** | **KILL (no lift)** | Replacing pairs by blocks of `b` changes only the logarithm base and the width of the Stirling bands.  The endpoint and all terminal fibres are literally independent of `b`. | Re-entry would require genuinely `b`-sensitive intermediate-fibre theorems, not the family statement itself. |
| **GR1**, `G -> G^2` on labelled simple graphs | **KILL** | The literal operator is the classical graph square.  Every proposed theorem follows from the graph-power distance identity plus the classical labelled-component formula.  The same candidate was already logged twice internally as direct-background reserve/kill. | **None.**  `G -> G^r` is the same zero-credit base change, not a re-entry route. |

There is therefore **no PASS and no RESERVE among the two current
contracts**.  PM1 has a possible future re-entry specification; that is not a
reservation of the present candidate.  GR1 has no residual theorem contract.

## 2. Audit standard and bounded search

The gate asks two separate questions.

1. **Literal ownership:** has the same map, or a map differing only by a
   transparent encoding, already appeared?
2. **Residual value:** after all owned or one-line consequences are assigned
   zero contribution credit, is there still a paper-sized theorem package?

Failure of the first question is sufficient but not necessary for a kill.  A
candidate can also fail because its only unowned feature is a scheduler whose
entire theorem list follows from a generic list/composition normal form.

Representative searches were run in literal and equivalent language, with
full texts inspected for the controlling hits:

- PM1 literal: `erase parentheses standard cycle notation permutation`,
  `merge adjacent cycles canonical cycle notation`, `flattened permutation
  preimage cuts`, and `repeated pairwise cycle merge Stirling depth`;
- PM1 equivalent: `cycle composition coarsening consecutive parts`,
  `transposition joins two cycles cut join`, `Foata cycle word map fibre`, and
  `b-ary consecutive cycle merge permutation`;
- GR1 literal: `iterate graph square finite dynamics`, `repeated graph
  squaring diameter`, and `graph-square preimages cluster graph`;
- GR1 equivalent: `powers of graphs distance at most k`, `diameter bounded
  labelled connected graphs`, and `component property exponential generating
  function`.

The search included 2024--2026 literature.  For example, Baril--Ramirez
continue the flattened-permutation line in 2026
([DOI 10.1007/s00010-026-01275-9](https://doi.org/10.1007/s00010-026-01275-9)),
Khanna--Loehr treat canonical cycle compositions and composition refinement
in 2026
([DOI 10.37236/14164](https://doi.org/10.37236/14164)), and Pierron treats
graph powers in 2024
([DOI 10.1016/j.ejc.2023.103822](https://doi.org/10.1016/j.ejc.2023.103822)).
These currency checks are not themselves literal-dynamics collisions.  The
bounded search found no primary source packaging PM1's repeated adjacent-block
scheduler with its exact finite functional graph, and no primary source using
GR1's elementary consequences as this exact finite-dynamics package.  Those
non-hits do not rescue either candidate after owner/value subtraction.

## 3. PM1 reconstructed exactly

Write a permutation in standard cycle form

```text
pi = (C_1)(C_2)...(C_c),
```

where every cycle word starts at its least entry and the cycle minima increase
from left to right.  PM1 deletes the parentheses between `C_1,C_2`, between
`C_3,C_4`, and so on.  Thus

```text
Phi_2(pi) = (C_1 C_2)(C_3 C_4)...,
```

with an unpaired last cycle retained.  Concatenation is associative, and the
first entry of each new word remains the minimum of its support, so subsequent
rounds retain the same canonical block order.

The scout contract consists of:

1. consecutive initial cycles are grouped in blocks of at most `2^t` after
   `t` rounds;
2. `c(Phi_2^t(pi))=ceil(c(pi)/2^t)` and
   `depth(pi)=ceil(log_2 c(pi))`;
3. depth layers are unsigned-Stirling bands in the initial cycle count;
4. all `n`-cycles are fixed and the zeta function records only these fixed
   points;
5. the endpoint erases every parenthesis in the initial standard cycle form
   and wraps the resulting word as one cycle;
6. a terminal fibre is described by admissible cuts of the target word; and
7. the increasing target word uniquely has all `2^(n-1)` cut sets.

All seven statements can be correct and still have zero or insufficient
residual contribution.  The issue at this gate is ownership and theorem value,
not the finite pilot.

## 4. PM1 direct and equivalent ownership

### 4.1 The endpoint is an existing named map

Can--Cherniavsky define exactly the convention used by PM1: each cycle starts
at its minimum, cycles are ordered by increasing minima, singleton cycles are
retained, and `Omega:S_n -> S_n` is obtained by omitting all parentheses.
They explicitly note that `Omega` is non-injective and organize its images by
the composition of cycle lengths.  See
[Can and Cherniavsky, *Omitting Parentheses from the Cyclic Notation*](https://arxiv.org/pdf/1308.0936),
published as
[DOI 10.1007/s00009-014-0467-1](https://doi.org/10.1007/s00009-014-0467-1).

Mansour--Shattuck--Wang use the same standard cycle convention and call the
same parenthesis-erased word `Flatten(pi)`.  See their primary full text,
[arXiv:1307.3637](https://arxiv.org/pdf/1307.3637), and the journal article
[DOI 10.4310/JOC.2013.v4.n3.a4](https://doi.org/10.4310/JOC.2013.v4.n3.a4).
The continuing 2026 literature cited above confirms that “flattened
permutation” is an active established object rather than an isolated notation.

If `J` sends a word beginning with `1` to the `n`-cycle obtained by enclosing
that word in parentheses, then PM1's endpoint is exactly

```text
E_n = J o Omega = J o Flatten.
```

`J` is a transparent bijective repackaging.  Therefore PM1 receives **zero
credit for defining, discovering, or identifying the endpoint map**.

### 4.2 The local merge is already explicit parenthesis deletion

Pozdnyakov--Steele use the same minimum-first/increasing-minima “first cycle
representation” and define a bijection by deleting a back-to-back parenthesis
pair.  Their displayed example is

```text
(153)(24)(67) -> (15324)(67).
```

That is PM1's local concatenation operation.  Their paper applies the deletion
at a distinguished boundary rather than running PM1's full parallel
scheduler, so it is not a literal owner of the entire iteration.  It is,
however, a direct owner of the atomic combinatorial move.  See
[Pozdnyakov and Steele, *Buses, Bullies, and Bijections*](https://vladimir-pozdnyakov.github.io/papers/BBB.pdf),
[DOI 10.4169/math.mag.89.3.167](https://doi.org/10.4169/math.mag.89.3.167).

The group-theoretic formulation is equally classical.  If

```text
A=(a_1 ... a_r),  B=(b_1 ... b_s),
```

then, with the usual right-composition convention,

```text
A B (a_r b_s) = (a_1 ... a_r b_1 ... b_s).
```

Thus every PM1 atomic merge is a join transposition.  Goulden--Jackson's
primary cut--join treatment explicitly assigns a join operator to a
transposition that joins two different cycles.  See
[the primary paper](https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjpams1997.pdf),
[DOI 10.1090/S0002-9939-97-03880-X](https://doi.org/10.1090/S0002-9939-97-03880-X).
PM1 receives **zero credit for the fact that concatenation joins two cycles or
for its cut--join interpretation**.

### 4.3 Foata is background; `Omega/Flatten` is the exact owner

Foata's cycle-to-word transformations are the classical background for
encoding cycle structure by word statistics; the primary source is
[Foata, *On the Netto inversion number of a sequence*](https://www.ams.org/proc/1968-019-01/S0002-9939-1968-0223256-9/S0002-9939-1968-0223256-9.pdf),
[DOI 10.1090/S0002-9939-1968-0223256-9](https://doi.org/10.1090/S0002-9939-1968-0223256-9).
The audit does **not** identify PM1's endpoint with every conventional version
of Foata's first fundamental transformation: cycle-start and cycle-order
conventions differ across formulations, and the classical transformation is
usually used as a bijection whereas `Omega` is non-injective.  The precise
subtraction is:

- Foata receives the broad cycle-word encoding background;
- Can--Cherniavsky and the flattened-permutation literature receive the exact
  minimum-first/increasing-minima parenthesis-erasure map; and
- PM1 retains no endpoint-definition credit merely by wrapping the flattened
  word as one cycle.

This distinction avoids both under-citing the exact owner and over-claiming
that Foata published the full PM1 finite map.

### 4.4 Cycle compositions own the length-level normal form

Khanna--Loehr define canonical cycle notation and the ordered composition of
cycle lengths, then treat refinement/coarsening of compositions, where a
coarsening replaces consecutive parts by their sum.  Their cycle minima are
ordered in the opposite direction, so they do not own PM1's literal endpoint;
they do own the composition-level calculus after the harmless reversal of
order.  See
[the primary journal PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p12/pdf/),
[DOI 10.37236/14164](https://doi.org/10.37236/14164).

On the initial length composition

```text
(|C_1|,|C_2|,...,|C_c|),
```

PM1 simply replaces consecutive pairs by their sums.  Therefore the
composition coarsening, its binary block tree, and the statement that the
cycle count is halved with ceiling receive **zero credit**.

## 5. Exact zero-credit subtraction for PM1

| Proposed item | Gate subtraction | Credit after subtraction |
|---|---|---:|
| Minimum-first cycles ordered by increasing minima | Standard cycle notation used verbatim by `Omega`, `Flatten`, and the first-cycle representation | 0 |
| Delete `)(` to concatenate two adjacent cycle words | Explicit published parenthesis-deletion bijection; also a join transposition | 0 |
| Endpoint obtained by erasing all parentheses | Exact `Omega/Flatten`, followed by the transparent wrapper `J` | 0 |
| Ordered cycle-length composition and adjacent block sums | Classical composition coarsening; recent primary treatment explicitly includes cycle compositions and consecutive-part sums | 0 |
| `c_t=ceil(c/2^t)` and `ceil(log_2 c)` depth | Generic balanced binary compaction of a list | 0 |
| Unsigned-Stirling depth bands | The number of permutations with `c` cycles is the classical unsigned Stirling number; substitute the generic clock interval | 0 |
| Fixed set `(n-1)!`, no nontrivial cycles, and zeta | Immediate from strict cycle-count decrease until one cycle | 0 |
| Terminal fibre as admissible parentheses/cuts | Formally a correct inverse description of the already-owned `Omega`; the present statement is a definitional cut bijection, not an evaluated pointwise formula | 0 for the present contract |
| Unique `2^(n-1)` terminal maximum at `12...n` | At most every gap can be cut; equality permits the all-singleton cut, which forces the word to increase | 0 |
| Exhaustive checks through `S_9` | Valuable correctness control, but not mathematical contribution after the theorem list is subtracted | evidence only |

The residual before value review is only this sentence:

> Apply all individually known adjacent parenthesis deletions in parallel at
> the deterministic boundaries `1|2, 3|4, ...`, then repeat.

That scheduler is a bounded-search non-hit.  It is not a paper-sized residual
because every theorem currently attached to it is the generic block-compaction
normal form or the already-owned endpoint.

## 6. The proposed all-arity strengthening does not lift PM1

For fixed `b>=2`, define `Phi_b` by partitioning the current canonical cycle
list into consecutive groups of at most `b`, concatenating every group, and
retaining the final shorter group.  Let the initial cycle words be
`C_1,...,C_c`.

### Lemma (exact `b`-ary iterate)

After `t` rounds, the cycles are the concatenated consecutive blocks

```text
C_1...C_(b^t),
C_(b^t+1)...C_(2b^t),
...,
```

with the last block truncated at `c`.  Consequently

```text
c(Phi_b^t(pi)) = ceil(c(pi)/b^t),
depth_b(pi) = 0                         if c(pi)=1,
              ceil(log_b c(pi))        if c(pi)>=2.
```

**Proof.**  The statement is immediate at `t=0`.  Concatenating consecutive
groups of at most `b` blocks of width at most `b^t` gives consecutive blocks
of width at most `b^(t+1)`.  The minimum of the first constituent cycle remains
the minimum of the merged support, so the block order remains canonical.
Induction proves the block description and the cycle-count formula.  The first
time that ceiling equals one is the displayed depth.  QED.

Thus the exact depth census is only the base-`b` Stirling band

```text
d=0:  [{n \atop 1}],
d>=1: sum_(b^(d-1) < k <= min(b^d,n)) [{n \atop k}].
```

More decisively, associativity gives, for every `b>=2`,

```text
E_(n,b)(pi) = (C_1 C_2 ... C_c) = J(Omega(pi)).
```

Hence

```text
E_(n,b)^(-1)(tau) = E_(n,2)^(-1)(tau)
```

for every target `n`-cycle `tau`.  The admissible-cut fibres, their sizes,
their extrema, and the unique `2^(n-1)` maximum are **exactly independent of
`b`**.

**Hostile conclusion on the family extension:** **KILL / NO RESIDUAL LIFT.**
The arity is only the radix of a deterministic list compactor.  It changes the
clock base just as `G -> G^3` changes the logarithm base behind graph
squaring.  Presenting all `b` at once makes the generic mechanism clearer; it
does not turn the endpoint or cut fibres into a new family theorem.

## 7. PM1 internal portfolio firewall

### 7.1 P105: same carrier and same canonical cycle decomposition

The [P105 theorem contract](../../papers102_106_sequence/phase1/THEOREM_CONTRACTS.md)
and PM1 both act on `S_n` through minimum-first cycle words.  They are
not conjugate and their forward invariants differ:

| Axis | P105 | PM1 |
|---|---|---|
| Literal update | Splice the least label out of each nontrivial cycle and make it a singleton | Concatenate adjacent whole cycle words |
| Clock | Longest cycle length minus one; linear sharp depth | Number of cycles under balanced compaction; logarithmic sharp depth |
| Endpoint | The identity / fully pruned canonical endpoint | Many orientation-sensitive `n`-cycles |
| Reverse geometry | Label-threshold matching factors for one-step predecessors | Parenthesis/cut choices for a known flattening map |

This proves nonidentity, not paper separation.  The portfolio already spent a
paper on exact labelled surgery and reverse fibres on this exact carrier and
representation.  PM1 must therefore contribute substantially more than
“another exact transient and fibre statement.”  After external owner
subtraction, it does not.

### 7.2 P110: deterministic coarsening is already a portfolio motif

The [P110 theorem contract](../../papers107_111_sequence/phase1/THEOREM_CONTRACTS.md)
repeatedly replaces a set partition by its join with a cyclic translate.
Its coarsening is global and symmetry-generated; its endpoints are cyclic
coset partitions, its basins use Möbius--Bell inversion, and its deepest shell
uses primitive chords.  PM1 instead selects adjacent blocks by label-dependent
canonical order.  There is no literal collision.

Nevertheless, the shared silhouette is monotone coarsening of a canonical
partition until a normal form.  P110 retains nontrivial subgroup/coset and
Möbius geometry after generic closure is subtracted.  PM1 retains only the
scheduler.  The comparison therefore lowers PM1's value rather than rescuing
it.

### 7.3 P126: the binary tree, and hence the base-change clock, is occupied

The [P126 theorem contract](../../papers122_126_sequence/phase1/THEOREM_CONTRACTS.md)
synchronously replaces each part of an integer composition by balanced
children and derives a free-monoid iterate kernel, suffix decoder, every-target
one-run fibre product, and all-iterate image series.  Its update is refinement,
whereas PM1's cycle-length update is coarsening, so the maps are not inverses
or conjugates on their full carriers.

The temporal skeleton is still the same generic synchronous free-monoid
block tree: width changes by powers of the scheduler arity.  P126 earned its
residual from a complete kernel and decoding theory, not from the logarithmic
clock.  PM1 presently supplies no comparable all-iterate inverse theory.  The
`b>=2` extension increases, rather than decreases, this collision pressure.

### 7.4 Internal conclusion

PM1 survives a literal-map firewall against P105/P110/P126, but fails the
stronger **portfolio-value firewall**:

- P105 occupies permutation/canonical-cycle dynamics with exact reverse
  geometry;
- P110 occupies deterministic partition coarsening with nontrivial endpoint
  geometry; and
- P126 occupies the synchronous fixed-radix block-tree mechanism in its
  binary form and adds a real all-iterate decoder.

The unowned PM1 scheduler is weaker than each relevant occupied residual.

## 8. PM1 decision and possible re-entry contract

### Decision

**KILL_CURRENT_CONTRACT.**  Do not freeze a manuscript around the binary map,
the all-`b` family, the Stirling bands, fixed points/zeta, terminal cut
bijection, or `2^(n-1)` extremum.  Those are exactly the claims removed above.

### Re-entry is allowed only after a new theorem, not by expansion of prose

The following is a **future re-entry gate**, not a current reserve and not a
claim that the results are true.  A renewed candidate must prove at least one
item from A and one independently valuable item from B.

**A. Pointwise all-time inverse theory.**  For arbitrary `b,t` and arbitrary
target permutation with several canonical cycles, give an evaluated formula,
finite automaton, or transfer-matrix polynomial for

```text
|Phi_b^(-t)(tau)|,
```

not merely “count the valid cuts.”  It must account for the forced
`b^t`-sized source-cycle groups and for the global increase of all source-cycle
minima across target-cycle boundaries.  It should specialize correctly to
one-step and terminal fibres and expose a genuinely `b`-dependent intermediate
law.

**B. A second non-definitional theorem.**  Acceptable forms include one of:

- a closed multivariate admissible-cut polynomial by number of source cycles,
  with a structural factorization in terms of records, Cartesian trees, or
  another intrinsic statistic of the target word;
- exact aggregate moments or a limit law for fibre sizes over target
  `n`-cycles, derived from that structure rather than from brute-force
  summation;
- a sharp classification of all intermediate-fibre maximizers/minimizers for
  every `b,t`, including equality cases; or
- a complete all-iterate image/kernel description comparable in strength to
  P126's decoder, with at least one consequence not determined solely by the
  initial cycle count.

Merely restating the induction in Section 6, replacing `2` by `b`, tabulating
more small `n`, or giving a dynamic program that is just exhaustive cut
enumeration does not satisfy re-entry.

## 9. GR1 reconstructed exactly

For a labelled simple graph `G`, let `G^r` join two distinct vertices when
their graph distance in `G` is at most `r`, and define

```text
Psi(G) = G^2.
```

The scout contract states:

1. `Psi^t(G)=G^(2^t)`;
2. every connected component becomes a clique, at depth
   `ceil(log_2 D(G))` with the conventional depth-zero cases;
3. fixed points are cluster graphs, counted by the Bell number `B_n`;
4. the basin of a target with clique-block sizes `m_i` is
   `product_i c_(m_i)`, where `c_m` counts connected labelled graphs;
5. its one-step fibre is `product_i q_(m_i)`, where `q_m` counts connected
   labelled graphs of diameter at most two; and
6. the depth-at-most-`t` exponential generating function is

   ```text
   exp(sum_(m>=1) c_m^(<=2^t) z^m/m!).
   ```

Again, the hostile gate accepts these identities as correct.  Their derivation
is exactly why the candidate is killed.

## 10. GR1 direct ownership and deduction chain

### 10.1 The literal update is the classical graph square

Ross--Harary studied `G^2` in 1960, defining adjacency through walks/distances
of length at most two and opening a mature square/root literature.  See
[Ross and Harary, *The Square of a Tree*](https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1960.tb03936.x),
[DOI 10.1002/j.1538-7305.1960.tb03936.x](https://doi.org/10.1002/j.1538-7305.1960.tb03936.x).

Lin--Skiena define the general `n`th graph power by distance at most `n` and
study graph roots algorithmically.  See
[Lin and Skiena, *Algorithms for Square Roots of Graphs*](https://epubs.siam.org/doi/10.1137/S089548019120016X),
[DOI 10.1137/S089548019120016X](https://doi.org/10.1137/S089548019120016X).
Motwani--Sudan establish the mature computational difficulty of graph roots:
[primary article](https://www.sciencedirect.com/science/article/pii/0166218X94000239),
[DOI 10.1016/0166-218X(94)00023-9](https://doi.org/10.1016/0166-218X(94)00023-9).

This is direct ownership of the literal operator, not merely a neighboring
graph process.

### 10.2 Every temporal statement is the distance identity

For positive integers `a,b`, shortest-path distances give

```text
(G^a)^b = G^(ab).
```

Therefore `Psi^t(G)=G^(2^t)`.  Graph powers preserve connected components,
and a connected component of diameter `d` becomes complete exactly when the
power exponent reaches `d`.  It follows immediately that:

- the endpoint completes each original component to a clique;
- the depth is the ceiling of the base-two logarithm of the largest component
  diameter (with isolated/complete components already fixed);
- fixed graphs are exactly disjoint unions of cliques;
- there are no nontrivial cycles because edges only accumulate; and
- replacing square by the `r`th power changes only `2^t` to `r^t`.

No additional dynamical mechanism is present.

### 10.3 Every census statement is the labelled component theorem

Gilbert begins with an arbitrary property `P` of connected graphs and derives
the recurrence/logarithmic exponential generating function relating connected
`P`-graphs to arbitrary labelled graphs all of whose components have `P`.
See
[Gilbert, *Enumeration of Labelled Graphs*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AE983E082134E56900EE87A88F95A72C/S0008414X00036907a.pdf/enumeration-of-labelled-graphs.pdf),
[DOI 10.4153/CJM-1956-046-2](https://doi.org/10.4153/CJM-1956-046-2).

Apply that theorem with:

- `P = connected` to obtain the product of connected-graph counts for an
  endpoint with prescribed clique blocks;
- `P = connected and diameter<=2` to obtain the one-step fixed-target fibre;
  and
- `P = connected and diameter<=2^t` to obtain the depth-prefix exponential
  formula.

The Bell fixed count is the elementary bijection between cluster graphs and
set partitions.  Thus the conjunction of GR1's formulae is not an independent
enumerative engine; it is a direct substitution of a diameter bound into the
classical component schema.

## 11. Exact zero-credit subtraction for GR1

| Proposed item | Gate subtraction | Credit after subtraction |
|---|---|---:|
| `G -> G^2` | Literal classical graph-square operator | 0 |
| `(G^a)^b=G^(ab)` and `G^(2^t)` iterates | Definitional distance identity for graph powers | 0 |
| Logarithmic diameter clock and path sharpness | First exponent reaching component diameter; the path has maximum diameter `n-1` | 0 |
| Component-clique endpoint | Immediate from graph power and preservation of components | 0 |
| Cluster-graph fixed points and Bell number | Standard set-partition/cluster-graph bijection | 0 |
| No other cycles and fixed-point zeta | Edge-monotonicity plus the fixed classification | 0 |
| Endpoint basin `product c_(m_i)` | Independent choice of a connected labelled graph on each prescribed block | 0 |
| One-step fibre `product q_(m_i)` | Same component product with diameter `<=2` | 0 |
| Depth-prefix EGF | Gilbert's arbitrary connected-property component formula with `P: diameter<=2^t` | 0 |
| Exact exhaustive pilot through `n=6` | Correctness evidence only | evidence only |

Nothing remains after this table.  “All statements are presented together as
a finite dynamical system” is packaging, not a residual theorem.

## 12. GR1 internal repeat and value decision

GR1 is not merely close to an internal paper; it is a repeated rejected intake
candidate.

1. The
   [P97--P101 candidate ledger](../../papers97_101_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md)
   records **graph squaring** as
   `RESERVE_DIRECT_BACKGROUND`: Bell attractor and diameter depth are exact,
   but graph powers and graph-operator dynamics own the mechanism.
2. The
   [P112--P116 root scout](../../papers112_116_sequence/scouting/ROOT_SCOUT.md)
   records **R5 graph squaring** with the same Bell
   fixed core and logarithmic diameter signal, and marks it
   `kill/direct-background reserve` because graph powers own the mechanism.
3. The
   [current combinatorial scout](../scouting/combinatorial/SCOUT.md)'s GR2
   (`G -> G^3`) was already killed behind GR1 as a
   mere logarithm-base change.

The current theorem list adds endpoint-basin and diameter-bounded component
products, but Section 10.3 shows that these are the immediate classical
labelled-component substitution anticipated by the earlier value concern.
The new packaging therefore does not overturn either prior decision.

**Decision:** **KILL_DIRECT_OWNER_AND_INTERNAL_REPEAT.**  There is no honest
residual contract for GR1.  Do not re-enter it as `G -> G^r`, by adding more
diameter tables, or by expanding the zeta bookkeeping.  Re-entry would require
a materially different graph operator with a non-classical inverse geometry;
that would be a new candidate, not GR1.

## 13. Final freeze instruction

- Remove PM1 and GR1 from the current finalist slate.
- Do not assign either a paper number.
- Preserve the PM1 computational pilot as a verified scout artifact; it may
  support the precise all-time-fibre re-entry test in Section 8.
- Preserve the GR1 pilot only as a regression/control example for generic
  closure dynamics.
- Do not advertise either bounded search non-hit as novelty.
- Maintain **HOLD EXTERNAL** until a later gate supplies a genuinely residual
  theorem contract.

## 14. Primary-source ledger

| Source | Direct relevance to this gate | Stable link |
|---|---|---|
| D. Foata (1968), *On the Netto inversion number of a sequence* | Classical cycle-to-word transformation background; not claimed as the exact PM1 endpoint owner | [DOI 10.1090/S0002-9939-1968-0223256-9](https://doi.org/10.1090/S0002-9939-1968-0223256-9) |
| M. B. Can and Y. Cherniavsky (2015; online 2014), *Omitting Parentheses from the Cyclic Notation* | Exact minimum-first/increasing-minima `Omega` parenthesis-erasure map | [arXiv full text](https://arxiv.org/pdf/1308.0936); [DOI 10.1007/s00009-014-0467-1](https://doi.org/10.1007/s00009-014-0467-1) |
| T. Mansour, M. Shattuck, and D. G. L. Wang (2013), *Counting subwords in flattened permutations* | Same standard-cycle convention and exact `Flatten` map | [arXiv full text](https://arxiv.org/pdf/1307.3637); [DOI 10.4310/JOC.2013.v4.n3.a4](https://doi.org/10.4310/JOC.2013.v4.n3.a4) |
| V. Pozdnyakov and J. M. Steele (2016), *Buses, Bullies, and Bijections* | Explicit adjacent `)(` deletion/concatenation in the same cycle convention | [author-hosted full text](https://vladimir-pozdnyakov.github.io/papers/BBB.pdf); [DOI 10.4169/math.mag.89.3.167](https://doi.org/10.4169/math.mag.89.3.167) |
| I. P. Goulden and D. M. Jackson (1997), *Transitive Factorisations into Transpositions and Holomorphic Mappings on the Sphere* | Classical transposition join operator on permutation cycles | [author/institution full text](https://uwaterloo.ca/math/sites/default/files/uploads/documents/gjpams1997.pdf); [DOI 10.1090/S0002-9939-97-03880-X](https://doi.org/10.1090/S0002-9939-97-03880-X) |
| A. Khanna and N. A. Loehr (2026), *A Local Framework for Proving Combinatorial Matrix Inversion Theorems* | Canonical cycle compositions and consecutive-part refinement/coarsening | [journal full text](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p12/pdf/); [DOI 10.37236/14164](https://doi.org/10.37236/14164) |
| J.-L. Baril and J. L. Ramirez (2026), *Some distributions on increasing and flattened permutations* | Current-field check for mature flattened-permutation enumeration | [DOI 10.1007/s00010-026-01275-9](https://doi.org/10.1007/s00010-026-01275-9) |
| I. C. Ross and F. Harary (1960), *The Square of a Tree* | Early direct graph-square source | [DOI 10.1002/j.1538-7305.1960.tb03936.x](https://doi.org/10.1002/j.1538-7305.1960.tb03936.x) |
| Y.-L. Lin and S. S. Skiena (1995), *Algorithms for Square Roots of Graphs* | Explicit general distance definition of graph powers and root theory | [DOI 10.1137/S089548019120016X](https://doi.org/10.1137/S089548019120016X) |
| R. Motwani and M. Sudan (1994), *Computing roots of graphs is hard* | Mature graph-root complexity; corroborates direct-owner depth | [DOI 10.1016/0166-218X(94)00023-9](https://doi.org/10.1016/0166-218X(94)00023-9) |
| E. N. Gilbert (1956), *Enumeration of Labelled Graphs* | General labelled-component property recurrence and logarithmic EGF | [publisher full text](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AE983E082134E56900EE87A88F95A72C/S0008414X00036907a.pdf/enumeration-of-labelled-graphs.pdf); [DOI 10.4153/CJM-1956-046-2](https://doi.org/10.4153/CJM-1956-046-2) |
| T. Pierron (2024), *A Brooks-like result for graph powers* | Current-field check; not a literal finite-dynamics collision | [DOI 10.1016/j.ejc.2023.103822](https://doi.org/10.1016/j.ejc.2023.103822) |
