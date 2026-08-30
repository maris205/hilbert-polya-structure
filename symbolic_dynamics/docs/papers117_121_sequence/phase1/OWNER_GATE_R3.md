# R3 hostile owner gate: maximal permutation-bond-run contraction

**Audit date:** 2026-08-30  
**External status:** `HOLD_EXTERNAL`  
**Gate verdict:** **KILL / ABANDON (2.5/10)**

## Bottom line

The spike is mathematically sound, including its fibre series and its
`2^(n-1)` deepest census.  It nevertheless fails the owner gate.  The literal
one-step operation is already present in Cerbai--Ferrari's canonical peg
reduction: their `peg(pi)` replaces every maximal increasing or decreasing
strip by one entry, rescales, and records the strip type by a `+`, `-`, or
dot decoration.  If `und` erases those decorations, then the proposed map is
exactly

\[
   K(\pi)=\operatorname{und}(\operatorname{peg}(\pi)).
\]

This is a literal equality of finite maps, not an analogy.  Moreover, the
target-local fibre OGF is the disjoint sum of the clean, compact peg-filling
series developed by Homberger--Vatter.  After those two subtractions, the
credible unowned residue is iteration of `und o peg`, especially the sharp
depth and binary extremal lift tree.  That is a valid but thin theorem spike,
not a paper-scale package.  The stipulated gate therefore forces **KILL**.

## Literal reconstruction and claims audited

For `pi=pi_1...pi_n`, call `(i,i+1)` a bond when
`|pi_i-pi_(i+1)|=1`.  Cut the one-line word into its maximal bond runs,
replace each run by its minimum, and standardize the resulting word.  The
phase space is the disjoint union of all finite symmetric groups (including
the conventional empty state if desired).

The spike proposes the following claim package.

1. Every bond run is monotone and interval-valued, and
   `|K(pi)|=|pi|-b(pi)`, where `b(pi)` is the number of bonds.
2. The fixed points are precisely the bond-free, or non-attacking-king,
   permutations; every nonfixed orbit strictly loses rank, so there are no
   nontrivial recurrent orbits and depth is at most `n-1`.
3. For `sigma in S_k`, the complete one-step fibre has the three-state OGF

   \[
   P_\sigma(x)=\sum_{\eta\in A(\sigma)}
      \frac{x^{k+h(\eta)}}{(1-x)^{h(\eta)}}.
   \]

   Here each target entry is a singleton (`0`) or is inflated to an
   increasing/decreasing block (`+`/`-`), and `A(sigma)` forbids precisely the
   boundary states that would fuse across a target bond.
4. The maximum depth on `S_n` is `n-1`.
5. Exactly `2^(n-1)` permutations of length `n` attain that depth.

Claims 1--3 are correct but substantially or completely owned.  Claims 4--5
appear to be the residual temporal delta found by this bounded audit.

## Decisive direct owner

Cerbai and Ferrari, [*Permutation patterns in genome rearrangement problems:
The reversal model*](https://doi.org/10.1016/j.dam.2019.10.012), *Discrete
Applied Mathematics* **279** (2020), 34--48, define increasing and decreasing
strips as maximal consecutive substrings whose successive values differ by
`+1` or `-1`.  In their canonical peg encoding, every strip is replaced by
one representative, the result is rescaled, and the representative is
decorated `+`, `-`, or dotted according to whether the strip is increasing,
decreasing, or a singleton; see their Section 2.1.  The corresponding
[preprint](https://arxiv.org/abs/1903.08774) exposes the same definition.

Distinctness makes every R3 bond run monotone: a walk with increments in
`{+1,-1}` cannot change sign without immediately repeating a value.  Thus
R3's maximal bond runs and Cerbai--Ferrari's strips are the same blocks.
Both reductions retain one entry per block and standardize/rescale.  Choosing
the minimum rather than another representative has no effect after
standardization because the blocks are disjoint value intervals.  Therefore
erasing the peg decorations gives exactly `K`, for every input permutation.

This conclusion is stronger than saying that peg permutations provide useful
language for R3.  They directly own the canonical one-step reduction from
which R3 is obtained by forgetting information.  Their earlier conference
paper, [*Permutation patterns in genome rearrangement
problems*](https://ceur-ws.org/Vol-2113/paper12.pdf), GASCom 2018, already
gave the analogous increasing-strip reduction; the 2020 paper supplies the
two-orientation literal collision.

## Fibre OGF: valid, but not an independent residual engine

The OGF passed a hostile mathematical reconstruction.

- An inflated target entry has weight `x` in state `0` and
  `x^2/(1-x)` in either signed state.
- Only adjacent target values that occupy adjacent positions can cause two
  inflated blocks to fuse.  Across an increasing target bond the forbidden
  pairs are exactly those with both endpoints in `{0,+}`; across a decreasing
  bond they are exactly those with both endpoints in `{0,-}`.
- A state assignment plus its positive block lengths determines a unique
  interval partition of the source values, so the formula neither omits a
  multiplicity nor double-counts a preimage.

For example, when `sigma=12`, the admissible decorations are
`(0,-),(+,-),(-,0),(-,+),(-,-)`, and hence

\[
  P_{12}(x)=\frac{2x^3}{1-x}+\frac{3x^4}{(1-x)^2}.
\]

But this verification does not establish novelty.  Homberger and Vatter,
[*On the effective and automatic enumeration of polynomial permutation
classes*](https://doi.org/10.1016/j.jsc.2015.11.019), *Journal of Symbolic
Computation* **76** (2016), 84--96, develop exactly the relevant machinery:
monotone interval inflations of peg permutations, unique coarsest monotone
interval partitions, compactness, cleanliness, and rational filling-vector
series.  In their coordinates, signed entries have minimum filling length two
and dotted entries length one.  Their compactness exclusions are precisely
the boundary exclusions above, while cleanliness removes ambiguous dotted
`12`/`21` intervals.

Consequently the R3 fibre is the following standard peg decomposition:

\[
 \{\pi:K(\pi)=\sigma\}
 =\bigsqcup_{\epsilon:\,\sigma^\epsilon\ \text{clean and compact}}
   \{\pi:\operatorname{peg}(\pi)=\sigma^\epsilon\},
\]

and `P_sigma` is the corresponding finite sum of the usual filling-vector
series.  The three-state transfer matrix is a convenient specialization, but
after owner subtraction it cannot serve as a second independent paper
engine.  It receives **zero novelty credit** in this gate.

## Deepest `2^(n-1)` residual: correct but too narrow

The extremal argument also survives hostile checking.

Depth `n-1` requires a loss of exactly one at every nonterminal step, hence
exactly one bond at every such state.  If a target has one bond, a
length-one-higher source with one bond can be formed in exactly two ways:
inflate one or the other endpoint of the target bond, with the orientation
forced so that the old boundary bond is broken and the new internal bond is
retained.  All other single inflations either leave the old bond in place or
create another boundary bond.  The singleton has the two base lifts `12`
and `21`.  Thus the extremal lift tree is binary and

\[
   D_1=1,\qquad D_n=2D_{n-1}=2^{n-1}.
\]

The supplied deterministic verifier independently recomputed literal
fibres, depths, the two-lift lemma, and the census through length seven:

```text
r3_fibre_verify: PASS
assertions=14778
max_depth(n)=n-1
deepest_count(n)=2^(n-1)
fibre=three_state_signed_bond_path_partition_function
```

No source located in the bounded search stated this iterated sharp-depth
theorem or the binary deepest census.  That non-hit is not a novelty claim.
Even treating Claims 4--5 as new, they leave only one short extremal theorem:
the absence of cycles and the upper bound follow immediately from rank loss,
while fixed points and one-step fibres are owned.  The residue therefore does
not clear the requested paper-scale threshold.

## Owner landscape and subtraction ledger

| lane | primary owner or direct neighbour | hostile subtraction |
|---|---|---|
| Bonds and runs | Homberger, [*Counting Fixed-Length Permutation Patterns*](https://doi.org/10.61091/ojac-703), *OJAC* **7** (2012) | Bond/run terminology and static deletion facts: zero credit. |
| Bond-free permutations | Riordan, [*A recurrence for permutations without rising or falling successions*](https://doi.org/10.1214/aoms/1177700181) (1965); Bagno et al., [*On the poset of non-attacking king permutations*](https://doi.org/10.1016/j.ejc.2020.103119) (2020) | Fixed-point class, its terminology, and its enumeration: zero credit. |
| Literal strip reduction | Cerbai--Ferrari (2020), above | `K=und o peg`: direct collision; map and one-step canonical decomposition: zero credit. |
| Inflation / substitution | Homberger--Vatter (2016), above; Albert--Atkinson, [*Simple permutations and pattern restricted permutations*](https://doi.org/10.1016/j.disc.2005.06.016) (2005) | Monotone inflation, interval quotient/deflation, and unique block decomposition: zero credit. |
| Wreath-product strip framework | Atkinson--Stitt, [*Restricted permutations and the wreath product*](https://doi.org/10.1016/S0012-365X(02)00443-0) (2002) | General irreducible inflation framework: background only, but further narrows structural claims. |
| Deletion / insertion reconstruction | Smith, [*Permutation Reconstruction*](https://doi.org/10.37236/1149) (2006); Gouveia--Lehtonen, [*Permutation reconstruction from a few large patterns*](https://doi.org/10.37236/10403) (2021) | Delete-and-standardize decks and inverse insertions: zero-credit neighbouring machinery, not the decisive collision. |
| Recent interval structure | Bouvel--Cioni--Izart, [*The Interval Posets of Permutations Seen from the Decomposition Tree Perspective*](https://doi.org/10.1007/s11083-024-09690-w), *Order* **42** (2025), 459--479 | Modern decomposition-tree/interval-poset context; no exact temporal theorem found. |
| 2025--2026 king work | Li--Zhang, [*Mesh patterns in king permutations*](https://arxiv.org/abs/2411.18131); Li--Kitaev, [*King Permutations and Partially Ordered Patterns*](https://doi.org/10.5281/zenodo.19949822) (2026) | Recent static avoidance/enumeration only; it does not restore novelty to the fixed-point claim. |

The first two rows make the endpoints familiar; the third and fourth rows are
fatal.  In particular, “iteration was not studied” cannot be used to reclaim
the already-defined map or its peg-filling fibres.

## Literal comparison with P105

P105 is not the direct collision, but it raises an additional internal-scope
cost.

| feature | P105 | R3 |
|---|---|---|
| representation | cycle notation | one-line notation |
| update | synchronously remove the least label from each nontrivial cycle and make it fixed | synchronously contract every maximal bond strip, then standardize |
| ground set | fixed `S_n` | rank-changing union of `S_n` |
| recurrent set | unique identity | all bond-free king permutations |
| sharp clock | longest cycle length minus one; global `n-1` | repeated strip contraction; global `n-1` |
| deepest census | `(n-1)!` cycles of length `n` | `2^(n-1)` binary one-bond lifts |
| fibre mechanism | matching output cycles to peeled fixed points | monotone interval/peg fillings |

Thus R3 and P105 are neither conjugate nor the same update; P105 alone would
not force a kill.  Nevertheless both occupy an internal “permutation
contraction with a sharp `n-1` clock and explicit fibres” lane.  Once the
external peg collision removes R3's update and fibre engine, this editorial
overlap makes the remaining extremal theorem still less suitable as a new
paper.

## Search boundary through 2026

The bounded search used exact and synonymous formulations across:

- permutation bonds, adjacencies, successions, and maximal consecutive runs;
- increasing/decreasing strips, conserved strips, strip reduction, strip
  contraction, and repeated/iterated strip contraction;
- monotone interval inflation, substitution decomposition, quotient,
  deflation, clean/compact peg permutations, and filling vectors;
- deletion-standardization, inverse insertion, reconstruction decks, king
  permutations, functional graphs, transients, and depth;
- the same combinations with 2025 and 2026 filters.

Direct publisher or proceedings pages and accessible full texts were checked
for the sources above.  Searches such as `permutation repeatedly contract
maximal strips`, `iterated peg permutation`, `successive contraction monotone
intervals`, and `bond-run functional graph` did not expose a publication
stating the exact iteration or the `2^(n-1)` deepest theorem.  This is a
bounded result as of the audit date, not proof of absence.

## Score, strongest objection, and hard action

| component after subtraction | credit |
|---|---:|
| literal update and one-step reduction | 0 -- direct `und(peg(pi))` owner |
| bond/run and king fixed-point facts | 0 -- classical owners |
| fibre OGF / transfer matrix | 0 -- clean compact peg-filling specialization |
| no cycles and depth upper bound | negligible -- automatic rank descent |
| sharp depth and `2^(n-1)` deepest family | positive, apparently residual in this bounded audit |
| aggregate hostile score | **2.5/10** |

**Strongest objection.**  “The manuscript would iterate a known canonical
strip reduction only after erasing the decorations that make it canonical;
its advertised fibre theorem is the standard clean-compact peg filling
decomposition.  Only the binary extremal lift count remains.”

**Hard action: KILL / ABANDON.**  The gate condition required both absence of
a direct owner and a paper-scale residual.  R3 satisfies neither after literal
comparison.  Re-entry would require a materially larger temporal theorem --
for example a closed pointwise depth statistic, full depth-layer recurrence,
or genuinely multi-step fibre law not reducible to peg filling vectors -- and
would require a fresh owner audit.  The current spike must not be promoted.
