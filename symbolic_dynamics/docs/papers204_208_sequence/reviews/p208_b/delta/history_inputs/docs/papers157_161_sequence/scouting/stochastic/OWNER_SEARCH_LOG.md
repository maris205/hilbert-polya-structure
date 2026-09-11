# Bounded owner-search log — stochastic/graph/spatial scout

**Search date:** 2026-09-02 UTC  
**Batch:** P157–P161 Route-A Stage 1  
**External status:** `HOLD_EXTERNAL`

## Search boundary

This was a bounded owner-risk screen for the five candidates with the clearest
exact silhouettes after local falsification: `CIC`, `PMI`, `RII`, `PLI`, and
`RCR`.  Searches used public web, arXiv, publisher, DOI, and institutional
records; no manuscript, problem anchor, private note, or claimed result was
sent to an external model or person.  The screen did not include a complete
MathSciNet/Zentralblatt review, citation-chain closure, non-English search, or
specialist consultation.

The classifications below are deliberately asymmetric.  A direct hit can kill
or narrow a candidate.  A non-hit means only that these finite queries did not
return a direct owner; it does **not** mean novelty, priority, ownership,
freedom to operate, or permission to post or submit.

## Search matrix

### `CIC` — repeated random-cut intersection

Literal target searched: start from `K_n`; at every epoch draw a fair vertex
bicolouring and retain only edges crossing every cut drawn so far.  The target
conjunction was the all-time empty-state law plus the exact labelled fibre law
for a disjoint union of complete bipartite components.

Bounded queries:

- `graph edges surviving every random cut antipodal binary labels`
- `intersection of cuts graph theory complete bipartite`
- `antipodal binary labels graph adjacency complementary codewords`
- `intersection of complete bipartite spanning graphs characterization`

Nearest returned records:

- Erdős and Pyber, [*Covering a graph by complete bipartite
  graphs*](https://doi.org/10.1016/S0012-365X(96)00124-0), studies biclique
  edge partitions, not an iid intersection-of-cuts process or its temporal and
  fibre law.
- Zhao, Yağan, and Gligor,
  [*On k-connectivity and minimum vertex degree in random
  s-intersection graphs*](https://arxiv.org/abs/1409.6021), uses shared random
  items to create edges.  `CIC` instead retains an edge exactly when two full
  bit histories are complements.  The random-intersection-graph results do not
  own the literal update or stated conjunction.

Result: **bounded direct-owner non-hit; `OWNER_THIN`, unresolved**.  Binary
coding, inclusion–exclusion, graph cuts, and complete-bipartite terminology are
standard and receive zero contribution credit.  Stage 2 must search cut-space,
biclique-dimension, separating-system, and random graph-process citation
chains.  This non-hit is not a novelty finding.

### `PMI` — repeated perfect-matching intersection

Literal target searched: draw iid uniform perfect matchings of `K_{2n}` and
intersect all edge sets seen so far.  The target conjunction was the exact
all-`n,t` law of the common-edge count, its absorption transform, and the
every-target matching fibre.

Bounded queries:

- `intersection of random perfect matchings common edges`
- `common edges random perfect matchings distribution`
- `deranged matchings number common edges fixed perfect matching exact`
- `perfect matching derangement graph association scheme`

Material hits:

- Spiro and Surya,
  [*Counting Deranged Matchings*](https://arxiv.org/abs/2211.01872), owns the
  deranged-matching boundary and an asymptotic Poisson law for the number of
  edges shared by one uniform perfect matching and one fixed matching.
- Bučić, Devlin, Hendon, Horne, and Lund,
  [*Perfect matchings and derangements on
  graphs*](https://arxiv.org/abs/1906.05908), owns graph-perfect-matching
  intersection/derangement questions in a broader carrier.
- Granet and Joos,
  [*Random perfect matchings in regular
  graphs*](https://arxiv.org/abs/2301.10131), owns approximate-Poisson common
  edge counts against a fixed matching or spanning regular graph in robust
  expanders.
- Bamberg and Klawuhn,
  [*On the association scheme of perfect matchings and their
  designs*](https://arxiv.org/abs/2507.00813), confirms that pair relations of
  perfect matchings sit in an established association-scheme framework.

No returned record printed the repeated `t`-fold intersection law and exact
every-residual-matching fibre in the form tested here.  Nevertheless the
`t=2` boundary, derangement counts, matching symmetry, association scheme, and
inclusion–exclusion ingredients are owned inputs.

Result: **`OWNER_AMBER`**.  Retain only as a conditional Stage-2 candidate;
require full-text/citation-chain subtraction and a contribution that is not
merely “replace 2 by `t`” in a known matching-derangement formula.  This is not
currently an owner-thin recommendation.

### `RII` — iid fixed-window intersection on a path

Literal target searched: intersect iid uniformly placed length-`ell` lattice
intervals in a path, with absorption at the empty intersection.  The target
conjunction was its finite-power absorption law and an exact position-uniform
fibre atlas for every nonempty target interval.

Bounded queries:

- `intersection of random intervals discrete uniform fixed length`
- `discrete uniform sample range exact distribution max min`
- `sample range discrete uniform distribution exact`
- `random intervals intersection range order statistics discrete`

No direct primary owner was returned.  The relevant reduction is transparent:
the current intersection is determined by the minimum and maximum sampled
window starts, so classical discrete order-statistic/range counting owns the
main input and receives zero credit.  Search results concerning random closed
sets, interval coverage, continuous intervals, and unrelated uses of
“range” were not treated as evidence.

Result: **bounded direct-owner non-hit; `OWNER_THIN_RESERVE`, unresolved**.
The literal dynamic plus every-target fibre may be paper-sized, but the proof
engine is elementary sample-range inclusion–exclusion and is too close to
`CIC`/`PMI` at the batch level.  It is a replacement reserve, not a concurrent
recommendation.  Non-hit is not novelty.

### `PLI` — projective-line intersection in `PG(2,q)`

Literal target searched: start with all points of `PG(2,q)` and repeatedly
intersect with an iid uniform projective line.  The target conjunction was the
three-state size law (line/point/empty) and exact point fibres.

Bounded queries:

- `finite projective plane random lines intersection distribution`
- `projective plane random hyperplanes intersection rank distribution finite field`
- `random matrix over finite field rank distribution independent rows`
- `rank distribution random matrices finite fields`

Material hits:

- Fulman and Goldstein,
  [*Stein's method and the rank distribution of random matrices over finite
  fields*](https://arxiv.org/abs/1211.0504), treats established exact finite
  rank distributions and their limits.
- Salmond, Grant, Grivell, and Chan,
  [*On the rank of random matrices over finite
  fields*](https://arxiv.org/abs/1404.3250), is another primary random
  finite-field rank record.

The pilot law also follows immediately from the projective-plane axioms: all
identical sampled lines leave a line, at least two distinct concurrent lines
leave their unique point, and otherwise the intersection is empty.  Thus even
without a literal-title hit, the proposed theorem package is a thin
projectivized rank/incidence special case.  Internally it is also too close to
P153's finite-plane carrier.

Result: **`KILL_OWNER_RANK`**.  No Stage-2 owner search is justified.

### `RCR` — random anchored-rectangle contraction

Literal target searched: from `[1,a] x [1,b]`, choose one current lattice cell
uniformly and keep the origin-anchored subrectangle ending at that cell.  The
target conjunction was an exact absorption transform through independent
coordinate chains plus a closed Green kernel for every level.

Bounded queries:

- `random decreasing Markov chain choose uniformly integer between 1 and current absorption time`
- `uniformly from 1 current state Markov chain decreasing`
- `renewal approximation absorption time decreasing Markov chain`
- `random rectangle contraction lattice point anchored subrectangle`

Nearest returned record:

- Alsmeyer and Marynych,
  [*Renewal approximation for the absorption time of a decreasing Markov
  chain*](https://arxiv.org/abs/1509.01704), owns a broad asymptotic framework
  for eventually strictly decreasing chains.  The `RCR` coordinate chain has
  self-loops; its embedded jump chain is decreasing, so that framework is an
  important owner-risk neighbour, but the returned record does not state the
  exact rational PGF, two-coordinate maximum factorisation, or Green atlas
  used here.

Searches for the literal anchored rectangle returned geometric packing and
generic absorbing-chain material rather than this update.

Result: **bounded direct-owner non-hit; `OWNER_THIN`, unresolved**.  Generic
absorbing-chain algebra, first-step recurrences, and product-chain facts receive
zero contribution credit.  Stage 2 must close the decreasing-chain citation
graph and search leader-election, random descent, nested rectangles, and
record-minimum terminology.  This non-hit is not novelty.

## Decisive early-owner hits on killed controls

These were not among the five strongest theorem candidates, but a quick
literal search found decisive owners and prevented wasted work.

- `OKC` is exactly the classical OK Corral transition.  Kingman and Volkov,
  [*Solution to the OK Corral Model via Decoupling of Friedman's
  Urn*](https://doi.org/10.1023/A:1022294908268), gives exact survivor results;
  Kuba's [general weighted treatment](https://arxiv.org/abs/1003.1603) further
  removes any residual owner-thin claim.  Decision: `KILL_DIRECT_OWNER`.
- `STI` is literally an intersection of random spanning trees.  London and
  Pluhár,
  [*Intersection of random spanning trees in complex
  networks*](https://doi.org/10.1007/s41109-023-00600-4), directly owns the
  named process and expected-intersection setting.  The Cayley/forest-extension
  calculation in the pilot is generic zero-credit machinery.  Decision:
  `KILL_DIRECT_OWNER_ENGINE`.

## Owner-gate conclusion

The two current owner-thin recommendations are `CIC` and `RCR`; both remain
strictly internal and unresolved.  `PMI` is mathematically strong but
owner-amber.  `RII` is an owner-thin reserve, and `PLI` is killed.  Because
`CIC`, `PMI`, and `RII` all use repeated set intersection and finite
inclusion–exclusion, at most one may advance unless a later proof-engine audit
demonstrates genuine separation.

`HOLD_EXTERNAL` remains in force.  Nothing in this log is a novelty,
authorship, priority, ownership, release, posting, or submission certificate.
