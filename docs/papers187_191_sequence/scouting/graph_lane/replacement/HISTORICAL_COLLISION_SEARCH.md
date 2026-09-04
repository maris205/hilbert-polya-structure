# Pre-pilot historical collision search

Status: replacement scouting only.  This search was completed **before** any
replacement pilot was written or run.  The identifiers `RX01`--`RX12` below
are lane-local denominator labels, not paper numbers.

## Corpus and reproducible search

The internal corpus was the complete visible P1--P186 paper tree together
with the batch ledgers and collision firewalls.  The following read-only
commands were used from the repository root (case-insensitively where shown):

```text
find papers -mindepth 1 -maxdepth 2 -type f -name '*.tex' -print | sort
find docs -type f \( -iname '*kill*ledger*.md' -o -iname '*collision*.md' -o -iname '*candidate*pool*.md' \) -print | sort
rg -n -i 'graph|digraph|relation|poset|tree|forest|hypergraph|clutter|orientation|Markov|kernel' papers docs
rg -n -i 'closure|switch|exclusion|row[- ]?(sum|stat|degree)|Gram|polarity|blocker|line graph|source.to.sink|click|prun|peel|copy|singleton|Glaisher|equal[- ]?(part|cardinality|size)|component' papers docs
rg -n -i 'farthest|antipod|eccentric|diameter|centroid|reroot|rooted tree|nearest leaf' papers docs
```

The broad output was then narrowed to every
`docs/papers*_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md`, every
`SYSTEM_COLLISION_FIREWALL.md`, the P167--P186 and current-batch
`HISTORICAL_COLLISION_SEED.md` files, and the current P187--P191 root,
combinatorial, algebra, and frozen graph-lane ledgers.  This was a formula and
update-rule comparison, not a title-only comparison.

## Binding exclusions found before computation

| Internal owner / ledger | Mechanism treated as occupied | Consequence for this replacement pass |
|---|---|---|
| P106 and P106-era collision maps | antitone graph/neighbourhood polarity, `F^3=F`, blocker/formal-concept shadows | `RX08` exact-transversal polarity is desk-killed even if its census is clean. |
| P107--P111 candidate ledger | source-to-sink click dynamics and iterated line graphs have direct owners | `RX04` is desk-killed as a click process; no line-graph variant enters the denominator. |
| P114, P117, P120 and later tree gates | pruning/peeling, pointer squaring, rootward-path and centre/centroid shadows | nearest-leaf projection `RX02` and geodesic pursuit `RX03` receive no credit; path compression and centre finding were excluded before candidate formation. |
| P122--P141 Glaisher hostile gate and later collision ledgers | repeated equal-cardinality/equal-part coagulation is permanently occupied | Frozen `G02` is not repaired or renamed here; no component-size merger is admitted. |
| P137--P143 relation ledgers | relation powering/cubing, row-inclusion residuals, statistic kernels | `RX06`, `RX07`, and `RX09` are killed as Gram/power/statistic transfers. |
| P145, P158, P159, P177, P179, P183 | push/switch orientations, cuts, pruning, commuting parity support, singleton isolation, incoming copy | ordinary closure, toggling, cut, copy, and isolation variants were removed before the denominator was frozen. |
| P171 and P172--P186 collision seeds | Boolean Gram transforms, self-image erosion, random quotienting, translation/intersection, support compression | exact-one Gram `RX06` is not credited as new merely because `1` replaces Boolean `>0`. |
| Current P187--P191 lanes | equality-block merger, block-minimum peeling, algebraic replacements, and root-coordinator candidates | all are treated as live internal reservations; none is mechanically transported into this lane. |

The four mechanisms named in the replacement order are therefore hard
pre-pilot gates:

- standard closures are killed without allowing endpoint data to rescue them;
- local switches/clicks are killed without allowing reversibility to rescue
  them;
- coordinate swaps on fixed-weight subsets are killed as exclusion walks;
- row, degree, overlap, or containment-statistic quotients are killed without
  allowing a new carrier name to rescue them.

## Residual question

Only `RX01`, least-antipode rerooting of a labelled tree, survived the internal
formula comparison long enough to justify a theorem spike.  It preserves the
entire unrooted tree and changes only the distinguished root, but it is not a
centre projection, pruning, pointer jump, switch, exclusion walk, or
row-statistic quotient.  The proposed axes are (1) a uniform all-time
two-cycle theorem determined by a canonical diameter pair and (2) exact
metric-halfspace fibres, equivalently an exact transition spectrum on every
tree.  Those axes still require bounded external owner checking.

This corpus search is a collision filter only.  A missing `rg` hit is not
evidence of novelty, priority, or publication clearance.
