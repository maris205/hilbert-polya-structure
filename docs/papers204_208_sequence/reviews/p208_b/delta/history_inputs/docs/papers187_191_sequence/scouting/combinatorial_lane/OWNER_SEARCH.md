# Bounded owner and history search

Search date: 2026-09-04 UTC.  Status: `OWNER_AMBER / HOLD_EXTERNAL` for the
sole survivor C21.  This is a bounded web-index and internal-corpus check, not
a systematic database review, novelty opinion, priority claim, or permission
to circulate.

## Search protocol

The external pass used literal-update phrases first, then carrier/statistic
neighbors, and preferred primary papers or authoritative technical sources.
The internal pass searched all P1--P186 paper directory titles plus historical
and recent collision ledgers, then read the nearest paper definitions.  Exact
query strings included:

- `site:arxiv.org integer compositions divisibility partial sums parts composition`
- `site:doi.org compositions prefix sum divisible by part ordered composition`
- `"integer compositions" "prefix sums" divisibility`
- `"part divides" "partial sum" composition`
- `"each part" divides "partial sum" composition`
- `integer composition coarsening dynamical system delete cuts divisibility`
- `composition map delete partial sums divisibility`
- `composition rewriting merge adjacent parts divisibility dynamics`
- `"1, 2, 4, 7, 13, 20, 37, 55, 97" composition`
- `"split at the largest gap" clustering`
- `"largest gap" "divisive" cluster split`
- `"maximum gap" "divisive clustering"`
- `site:arxiv.org pop-stack sorting parallel peaks permutation operator`
- `site:doi.org pop-stack sorting permutations adjacent descents simultaneous`
- `site:arxiv.org parallel sorting permutation peaks simultaneous adjacent swaps`

## C21_PDCF: bounded non-hit, still amber

### Authoritative and nearby hits

1. Darij Grinberg, *Some basic properties of compositions*, gives the standard
   bijection between a composition and its internal partial-sum/cut subset,
   including the inverse by successive differences.  This owns the encoding,
   not the divisibility filter or its iteration:
   <https://www.cip.ifi.lmu.de/~grinberg/algebra/comps.pdf>.
2. SageMath's composition documentation likewise treats partial sums and the
   composition--subset bijection as standard software-level background:
   <https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/composition.html>.
3. OEIS A398023 (entered in 2026) counts a nearby but different static class:
   compositions `(c_1,...,c_k)` for which the **index** `i` divides the prefix
   sum.  C21 tests whether the **part** `a_i` divides its ending prefix and then
   iterates simultaneous cut deletion.  The entry is an authoritative
   sequence-neighborhood hit, not a literal owner:
   <https://oeis.org/A398023>.
4. General searches returned weighted, bounded-part, Carlitz, and other
   restricted-composition papers, but no indexed source defining the C21
   self-map, its `N-3` clock, or its every-target fibre DP.  This statement is
   only the result of the queries above.

### Internal subtraction

The closest internal systems were checked at the literal-update level:

| Paper | Occupied mechanism | Why C21 is not that mechanism |
|---|---|---|
| P126 | synchronously split each part into balanced halves | C21 only deletes old cuts and never refines |
| P147 | merge each maximal adjacent run of equal parts | C21 uses part-versus-absolute-prefix divisibility, not equality or runs |
| P169 | transfer last occurrences between cyclic set-partition blocks | different carrier, conserved tokens, and recurrence |
| P181 | reverse the permutation prefix at the first descent | no reversal, descent, or permutation carrier |
| P185 | replace word coordinates by strict-prefix diversity | C21 outputs a coarsening and uses no distinct-letter statistic |
| P186 | rank-compress a subset support and erode its gap word | C21's subset is only the standard cut encoding; its predecessor-dependent divisibility rule is not support compression |
| P131 | rotate Euclidean quotient queues | no quotient rotation, continuants, or nontrivial recurrence |

Local phrase searches for `prefix.*divis`, `partial sum.*divis`, and their
reversals found no C21 update elsewhere in P1--P186.  Nevertheless,
**non-hit is not novelty**.  Final disposition:
`SOLE SURVIVOR / OWNER_AMBER / HOLD_EXTERNAL`.

## C16_MGBF: direct local-operation owner, killed

Abbey, Diepenbrock, Langville, Meyer, Race, and Zhou, *Data Clustering via
Principal Direction Gap Partitioning*, arXiv:1211.4142, explicitly sorts the
projected data and splits at the largest gap between adjacent points:
<https://arxiv.org/abs/1211.4142>.  In one dimension this is C16's local block
split.  PDGP uses a different global cluster scheduler and practical fringe
tolerance; C16 synchronously splits every old block and fixes a leftmost tie.
Those differences leave a real finite-dynamics theorem package, but they do
not clear the literal update engine.  The conservative disposition is
`KILL_DIRECT_UPDATE_OWNER`, with no reserve.

## C03_IPF: non-finalist owner-density check

C03 was not revived: it has an observed sharp-looking clock but neither an
all-`n` normal form nor a target inverse theorem.  The bounded search also
found a dense deterministic sorting-map neighborhood.  In particular,
deterministic pop-stack sorting reverses all maximal decreasing runs in
parallel and has an active iteration/image literature; see Pudwell and Smith,
*A new lower bound for deterministic pop-stack-sorting*, European Journal of
Combinatorics 124 (2025), 104046,
<https://doi.org/10.1016/j.ejc.2024.104046>, and Claesson, Guðmundsson, and
Pantone, *Counting pop-stacked permutations in polynomial time*,
<https://arxiv.org/abs/1908.08910>.  These are not asserted to be the identical
C03 map; they make a clock-only peak-swap note an especially poor ownership
bet.  C03 remains killed before finalist status.
