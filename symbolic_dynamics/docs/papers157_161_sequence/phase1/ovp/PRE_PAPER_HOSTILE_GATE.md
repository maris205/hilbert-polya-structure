# OVP independent hostile pre-paper gate

Date: 2026-09-02 (UTC)  
Mode: independent algebraic cold read; author-side formulas and verifier were not trusted  
External state: `HOLD_EXTERNAL`  
Verdict: **`PASS_NARROW`**

This verdict is only an internal theorem gate.  It is not a novelty, priority,
submission-readiness, or paper-number decision.  The system survives only on the
combined exact inverse/iteration/image/census package stated below.  Parallel
peeling, the handshaking lemma, the fixed-point description, the sharp clock,
binary incidence rank, even-graph enumeration, and generic matrix-power
language receive no independent contribution credit.

## 1. Literal system audited

Fix an ambient label set `[n]`.  A state is a simple graph on an arbitrary
subset of `[n]`.  If `D(G)` is the set of vertices having odd degree in the
current graph, then

```text
F(G) = G[V(G) \ D(G)].
```

All vertices in `D(G)` are deleted **simultaneously**.  An `even graph` below
means that every vertex has even degree; it need not be connected.  It should
not be called Eulerian without an added connectivity hypothesis.

## 2. Cold rederivation of the strict inverse

Let the target `H` have fixed vertex set `S`, `|S|=s`.  Let a strict source have
vertex set `S union D`, with `|D|=d>0`; the edges internal to `S` are forced to
be those of `H`.  The variables are the edges with at least one endpoint in
`D`, so their number is

```text
sd + binom(d,2).
```

Write `x_uv` for these binary edge variables.  The necessary and sufficient
conditions for one update to delete exactly `D` and leave `H` are

```text
sum_{v in D} x_uv                         = deg_H(u)  (mod 2),  u in S,
sum_{w in (S union D) \ {v}} x_vw        = 1         (mod 2),  v in D.
```

The coefficient matrix is the binary vertex-edge incidence matrix of the graph
on `S union D` containing exactly the edges incident with `D`.  For `d>0` this
graph is connected (including the one-vertex boundary), so its rank over
`F_2` is `s+d-1`.  The sum of all right-hand sides is

```text
sum_{u in S} deg_H(u) + d = d  (mod 2),
```

because the degree sum of `H` is even.  Therefore the system is consistent
exactly when `d` is even.  In that case its nullity is

```text
sd + binom(d,2) - (s+d-1)
  = s(d-1) + binom(d-1,2).
```

After choosing `D` among the `n-s` unused ambient labels, the independently
derived strict transfer is consequently

```text
B_n(s,m) = binom(n-s,d) 2^[s(d-1)+binom(d-1,2)]
```

when `d=m-s` is positive and even, and is zero otherwise.  No edge statistic
of `H` remains.  This target-independence is real: only the automatically even
sum of the target degree-parity vector is used.

**Formula correction status:** no correction to the proposed positive-even
`d` formula was required.  The following conventions are mandatory and must
remain explicit in any manuscript:

- `B_n` is the **strict** transfer, so its diagonal is zero.  The `d=0`
  one-step fibre is one exactly for an even target (the target itself), and is
  zero for a non-even target.
- Rows are target ranks and columns are source ranks: `B_n[s,m]` counts
  rank-`m` strict predecessors of one fixed rank-`s` target.  No transpose is
  permissible.
- For `d=2` and a fixed deleted label pair, the count is `2^s`.  At `s=0`
  the unique source on that pair is `K_2`; after ambient-label choice the count
  is `binom(n,2)`.

## 3. Matrix orientation and all-time fibres

With rows indexed by target rank and columns by source rank, conventional
matrix multiplication has exactly the required direction:

```text
(B_n^2)(s,m) = sum_k B_n(s,k) B_n(k,m).
```

For each strict rank-`k` predecessor of a fixed target, target-independence
gives the same number `B_n(k,m)` of strict rank-`m` predecessors.  The unique
forward intermediate graph prevents overcounting inverse chains.  A strict
predecessor is necessarily non-even because its nonempty deleted set consists
of odd-degree vertices; hence no strict chain can insert a waiting epoch.

Thus, for a fixed rank-`s` graph `H` and every `t>=0`, the rank-resolved fibre
is

```text
#{G: |V(G)|=m and F^t(G)=H}
  = (B_n^t)(s,m),                    H non-even,
  = (I+B_n+...+B_n^t)(s,m),          H even.
```

For a non-even target all `t` transitions must be strict.  For an even target,
the disjoint alternatives are first arrival after `k` strict transitions,
`0<=k<=t`, followed by waiting at the fixed target.  At `t=0` both formulas
reduce to the identity fibre.

Orientation sentinels at ambient order four are

```text
B_4(0,2)=6,   B_4(2,0)=0,   (B_4^2)(0,4)=24.
```

All three agree with literal enumeration; the transposed convention fails the
second sentinel immediately.

## 4. Image, clock, and temporal census

Every active update deletes a positive even number of vertices.  It follows
that every orbit reaches an even graph in at most `floor(n/2)` steps.  The path
`P_n` loses its two endpoints in every active epoch and attains this bound,
with the empty graph as endpoint for even `n` and a singleton for odd `n`.

For `t>=1`, a non-even rank-`s` target has a `t`-step predecessor exactly when
there are at least `2t` unused ambient labels.  Necessity is the sum of `t`
positive even reverse rank increments; sufficiency uses `t` increments of two,
whose transfer entries are positive.  Therefore

```text
H in im(F^t)  iff  H is even or n-s >= 2t,       t>=1.
```

At `t=0` every state is in the image.  This boundary must not be folded into
the displayed `t>=1` criterion.

On a fixed `s`-set, the number of even simple graphs is

```text
e_0=e_1=1,   e_s=2^binom(s-1,2) for s>=2.
```

Since a deterministic orbit has one even endpoint, summing the even-target
fibres gives the depth CDF

```text
#{G: entrance_time(G) <= t}
  = sum_{s=0}^n binom(n,s) e_s
      sum_{m=0}^n (I+B_n+...+B_n^t)(s,m).
```

Successive differences give the exact depth shells.  This also checks that the
geometric sum belongs only to even targets; placing it on all targets would be
a false formula.

The degenerate carriers are consistent without exceptions hidden in the
proof: for `n=0` there is one state, the empty fixed graph; for `n=1` there are
two states, empty and singleton, and both are fixed.  Their maximum depth is
zero.

## 5. Independent counterexample pressure

The review-side program
[`verify_ovp_hostile.py`](verify_ovp_hostile.py) does not import the author
verifier.  It uses immutable vertex/edge tuples rather than the author's graph
bit-mask representation, reconstructs the update from degrees, constructs an
independently oriented transfer matrix, and separately row-reduces the strict
inverse parity systems over `F_2`.

It performed the following checks.

- All states on all ambient orders `0<=n<=6` were enumerated: respectively
  `1, 2, 5, 18, 113, 1450, 40069` states.
- Literal one-step strict fibres, the `d=0` branch, every iterate through
  stabilization and beyond, every-time rank fibres, every image, fixed counts,
  the clock/path witness, and every temporal CDF were compared with the
  formulas.
- All 511 incidence systems with `s+d<=9`, for every attainable target degree
  parity vector, were checked by coefficient and augmented ranks.
- The run executed `2,919,223` assertions and found no counterexample.

Two clean invocations using `python -B` were byte-identical and each compared
equal to [`OVP_HOSTILE_CANONICAL.txt`](OVP_HOSTILE_CANONICAL.txt).  No
`__pycache__` was left behind.

```text
verifier SHA-256  = 646978030e9f438f9b18562ff9864e83d86f14e8401c3de91467dc8ea3c7aa81
transcript SHA-256 = 9f049f57c7195ce5f28afb660d1ac65bdd2f6d9079c95f11bde787aefe86fed9
cold cmp runs      = 2/2 PASS
```

This finite computation is falsification evidence, not a proof substitute.
The incidence-rank derivation and unique-chain argument above supply the proof.

## 6. Bounded direct-owner audit

The bounded audit was run on 2026-09-02 using generic terminology only, without
repository-specific theorem prose.  Exact and alternate query families
included:

```text
"delete all odd-degree vertices" graph simultaneously
"simultaneous odd-degree vertex deletion" graph
"parallel odd-degree vertex deletion" graph
"parallel odd-degree peeling" graph
"odd-degree peeling" graph
"parity peeling" graph vertices
"all vertices of odd degree" removed graph iteration
"odd/odd vertex removal" graph
"odd degree stripping" graph
"Eulerian vertex deletion" graph
"Eulerian core" graph "odd degree" deletion
site:arxiv.org "odd-degree vertex deletion"
```

No scholarly result returned by this bounded pass stated the literal rule
“delete every currently odd-degree vertex simultaneously” together with the
target-uniform `B_n` inverse and its all-time fibre/image/CDF consequences.
That is a scoped non-hit only.  It must not be paraphrased as “no prior work,”
“first,” “novel,” or an established priority claim.

The closest positive sources and the exact subtraction they force are:

| Source | What it supports/owns | What it does not support in the inspected scope |
|---|---|---|
| Nowakowski and Ottaway, [*Vertex Deletion Games with Parity Rules*](https://www.mathstat.dal.ca/~ottaway/VDel.pdf), *Integers* 5(2), A15 (2005) | Sequential parity-restricted vertex-deletion games; in the main partizan version one player selects an even-degree vertex and the other selects an odd-degree vertex. | A deterministic round deleting the entire current odd set; strict inverse incidence counts; transfer powers. |
| Krüger, [*Analysis of Odd/odd vertex removal games on special graphs*](https://arxiv.org/abs/1304.7997), arXiv:1304.7997 / *Integers* 14, G07 (2014) | Sequential odd/odd removal, terminal all-even positions, and Grundy analysis, especially on bipartite graphs.  It owns the closest odd/odd-removal terminology and removes contribution credit from the terminal-even observation. | Simultaneous update, a deterministic orbit clock, every-target inverse fibres, or image/CDF formulas. |
| Cygan, Marx, Pilipczuk, Pilipczuk, and Schlotter, [*Parameterized Complexity of Eulerian Deletion Problems*](https://doi.org/10.1007/s00453-012-9667-x), *Algorithmica* 68 (2014) | Optimization/decision problems that choose vertex or edge deletions to obtain an all-even graph, with connected and nonconnected variants distinguished. | The forced deletion set of all currently odd vertices or its synchronous iteration. |
| Dabrowski, Golovach, van 't Hof, and Paulusma, [*Editing to Eulerian Graphs*](https://arxiv.org/abs/1410.6863), arXiv:1410.6863 | Minimum graph edits under prescribed degree-parity and connectivity constraints. | The OVP map or its inverse transfer atlas. |
| Jiang, Mitzenmacher, and Thaler, [*Parallel Peeling Algorithms*](https://arxiv.org/abs/1302.7014), arXiv:1302.7014 | The generic parallel-peeling paradigm: in each round all vertices below a degree threshold are removed, mainly on random hypergraphs. | Odd-degree predicates, exact deterministic fibres, or the binary-incidence inverse calculation here. |

Accordingly, “parallel peeling,” “parity deletion,” “odd/odd removal,” “even
terminal graph,” and “Eulerian deletion” are prior-work territory.  The owner
question for the exact literal OVP atlas remains **unresolved, not cleared**;
it must be reopened before any external claim.

## 7. Internal portfolio collision audit

The comparison below was made against the actual manuscripts, at proof-engine
level rather than title or vocabulary level.

| Internal paper | Superficial collision | All-iterate / inverse proof engine | Mechanical migration to OVP? | Gate result |
|---|---|---|---|---|
| P114, rooted-forest leaf peeling | Label-subset carrier, synchronous vertex deletion, clock/fibres | Forest height for iterates; Cayley/species enumeration; local attachment of new leaves with target-leaf inclusion-exclusion | No.  Degree-parity constraints on unrestricted graph edges cannot be obtained from the rooted-forest attachment argument. | Distinct engine; subtract generic pruning/absorption packaging. |
| P123, odd-component complementation | Graph parity vocabulary and synchronous update | Vertex set is retained; odd-order components are complemented; a parity-pruned component/co-component split tree gives transient depth and periods 1/2 | No.  There is neither vertex loss nor an incidence inverse tower. | Distinct literal and engine. |
| P141, weighted threshold greedy MIS | Graph carrier and endpoint laws | Random sequential exponential race on threshold graphs; reverse-stick/hazard analysis | No.  Random weighted selection has no deterministic all-time parity transfer. | Distinct literal and engine. |
| P146, uniform ear deletion in triangulations | Iterated vertex deletion | Random single-ear histories correspond to dual-tree leaf orders; hook products count histories | No.  It is neither simultaneous nor target-uniform, and its proof is a tree-poset history count. | Distinct literal and engine. |
| P148, even-level plane-tree contraction | Closest theorem silhouette: simultaneous reduction, sharp time, fibres, image layers | Depth divisibility under contraction; ordered block/gap reconstruction and plane-tree generating functions | No.  The ordered tree grammar does not yield the connected `F_2` incidence rank or the rank-only transfer powers. | Narrative silhouette collides; algebraic engine does not.  Explicit contrast is mandatory. |

No inspected proof engine mechanically transfers to the OVP strict inverse or
all-iterate formula.  The generic architecture “finite map + clock + fibre +
image” is nevertheless already common in the portfolio and earns zero credit.
The strongest internal risk is P148 at theorem-silhouette level and P114 at
synchronous-deletion vocabulary level; neither is a kill because the state
constraints and inverse reconstruction are not isomorphic.

## 8. Surviving theorem contract and claim ceiling

OVP survives only under the following narrow contract.

1. Prove the positive-even rank-loss strict inverse formula by the connected
   binary incidence system, including target-independence and the `d=0`, `d=2`,
   `n=0`, and `n=1` boundaries.
2. Fix the row-target/column-source orientation and derive the literal
   every-time fibres: `B_n^t` for non-even targets and the geometric sum for
   even targets.
3. Derive the exact time-`t` image criterion and the temporal CDF/shells from
   that transfer, with the `t=0` boundary stated separately.
4. Present the path clock only as structural context, not as the contribution.
5. Use “even graph,” not “Eulerian graph,” unless connectivity is separately
   imposed; make no novelty or priority claim from the bounded owner non-hit.

The defensible residual is the **conjunction** of target-uniform strict inverse
enumeration, correctly oriented all-time transfer powers, and exact image/CDF
consequences for this literal synchronous parity rule.  Removing any of those
three pieces leaves a result too close to classical parity facts, generic
parallel peeling, or the portfolio's existing theorem silhouette.

## 9. Final disposition

**`PASS_NARROW`**: no algebraic formula repair was required, all demanded
boundary cases and matrix orientation survived independent derivation, and no
counterexample appeared in the independent exhaustive/rank audit.  No internal
proof engine among P114/P123/P141/P146/P148 mechanically reproduces the result.
The external direct-owner search is bounded and inconclusive, so the work stays
`HOLD_EXTERNAL`; this gate authorizes neither numbering, TeX drafting, Git
actions, upload, nor a public novelty statement.
