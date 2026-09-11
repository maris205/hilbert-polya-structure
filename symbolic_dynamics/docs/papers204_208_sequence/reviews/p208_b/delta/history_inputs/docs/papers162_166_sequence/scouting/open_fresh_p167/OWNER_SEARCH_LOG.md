# Bounded owner and internal-collision audit — open-fresh P167

**Search date:** 2026-09-03 UTC  
**Scope:** three tested literal systems only  
**External state:** `HOLD_EXTERNAL`

This is an early owner gate, not a systematic review, novelty opinion,
priority claim, or freedom-to-operate search.  Direct definitions and proof
engines are enough to kill; a query non-hit is never positive evidence.

## Search strings

Spelling and notation variants of the following were searched in primary
paper repositories, publisher records, and the local P1--P164 corpus:

```text
greedy complement matching path iteration
monomer dimer tiling greedy retile dynamics
maximal matching complement map path Padovan preimage
Rule 184 finite exact transient preimage recurrent core
perfect matching rooted switch walk star transposition conjugation
perfect matching rewiring random transposition association scheme
star transposition factorization fixed point free involution
projective plane polarity flag involution absolute points conic
orthogonal polarity q+1 absolute points PG(2,q)
```

## `GCM`: exact-map non-hit, decisive internal proof collision

The bounded title/abstract search found no primary record for the exact
simultaneous rule “erase old dimers, then greedily match every old monomer
run.”  This non-hit contributes no positive evidence.

The relevant primary controls are instead proof-engine owners:

- Fukś, “Solution of the density classification problem with two cellular
  automata rules,” *Physical Review E* 55 (1997), R2081,
  [DOI 10.1103/PhysRevE.55.R2081](https://doi.org/10.1103/PhysRevE.55.R2081),
  uses Rule 184's free/jammed phase transition and exact preimage counting.
- Fukś, “Exact results for deterministic cellular automata traffic models,”
  *Physical Review E* 60 (1999), 197--202,
  [DOI 10.1103/PhysRevE.60.197](https://doi.org/10.1103/PhysRevE.60.197),
  derives arbitrary-time traffic results by reducing preimages to lattice-path
  counts.

The local decisive comparison is P90, `rule184-particle-periodic-zeta`.  P90
already contains all three interfaces used by `GCM`: a sharp finite core-entry
clock, alternating hard-core recurrent configurations, and exact preimage
enumeration.  `GCM` is not claimed to be the same map, but its leftmost even
edge is a one-sided traffic defect that moves monotonically until the same
kind of alternating core is reached.  Its inverse grammar counts the same
finite-transducer prehistory object.  The all-vertical Padovan fibre is static
maximal-matching enumeration.  There is no residual theorem independent of
that transfer.

Decision: **`KILL_INTERNAL_TRAFFIC_TRANSDUCER`**.

## `SRW`: direct star-transposition and matching-rewiring engines

The exact identity

```text
M -> (0 v) M (0 v)
```

places the process on the fixed-point-free-involution conjugacy class and
makes every history a word in star transpositions.  The closest primary
controls are:

- Olesker-Taylor, “Cutoff for Rewiring Dynamics on Perfect Matchings,”
  [arXiv:2108.11890](https://arxiv.org/abs/2108.11890), defines the natural
  perfect-matching random walk by choosing matched pairs, disassociating their
  endpoints, and re-pairing them.  Its `k=2` discussion explicitly connects
  the matching walk to random transpositions and representation theory.
- Pak, “Reduced decompositions of permutations in terms of star
  transpositions, generalized Catalan numbers and k-ary trees,” *Discrete
  Mathematics* 204 (1999), 329--335,
  [DOI 10.1016/S0012-365X(98)00377-X](https://doi.org/10.1016/S0012-365X(98)00377-X),
  studies factorizations by `(1 i)` directly.
- Féray, “Partial Jucys--Murphy elements and star factorizations,”
  [arXiv:0904.4854](https://arxiv.org/abs/0904.4854), treats arbitrary star-
  transposition factorization counts through Jucys--Murphy machinery.
- Srinivasan, “The perfect matching association scheme,” *Algebraic
  Combinatorics* 3 (2020), 559--591,
  [DOI 10.5802/alco.104](https://doi.org/10.5802/alco.104), owns the standard
  orbital coordinates for pairs of perfect matchings.

`SRW` anchors one of the two switched pairs at the root and chooses one of the
two nontrivial re-pairings through the sampled endpoint.  That change does not
escape either owner: the full endpoint law remains a star-factorization
coefficient on the perfect-matching conjugacy class.  The root-partner
projection is only a lazy complete graph and has no target-resolved residual.

Decision: **`KILL_DIRECT_MATCHING_REWIRING_OWNER`**.

## `OFP`: definition-level polarity involution

Primary controls inspected include:

- Tait and Timmons, “Independent sets in polarity graphs,”
  [arXiv:1601.05058](https://arxiv.org/abs/1601.05058), explicitly defines
  polarity through point--polar-line incidence and records the standard
  Erdős--Rényi orthogonal polarity of `PG(2,q)`.
- Loucks and Timmons, “Triangle-free induced subgraphs of polarity graphs,”
  [arXiv:1703.06347](https://arxiv.org/abs/1703.06347), uses the same finite-
  plane orthogonal-polarity object.
- D'haeseleer and Durante, “On absolute points of correlations in
  `PG(2,q^n)`,” [arXiv:2005.05698](https://arxiv.org/abs/2005.05698), treats
  absolute-point sets of correlations and notes that the reflexive polarity
  cases over finite fields are classical.

Once a polarity is fixed, swapping a point and line through it is simply the
defining incidence-reversing involution.  The `q+1` fixed flags are the
absolute conic.  No exact-title search is needed to kill an involution with
singleton fibres and a classical fixed locus.

The local geometry and matching/incidence scouts already reject polarity
threshold maps for lacking an all-parameter second axis.  `OFP` is even
thinner: it never leaves the recurrent set.

Decision: **`KILL_DIRECT_POLARITY_INVOLUTION`**.

## P1--P164 collision summary

| system | nearest internal occupancy | collision conclusion |
|---|---|---|
| `GCM` | P90 Rule-184 sharp core entry/preimages; P147 run consolidation as a weaker secondary warning | dominant temporal and inverse proof silhouette occupied; kill |
| `SRW` | P130 matching-component interface; current `M01 OMD` matching-overlay kill; P145 generic symmetric finite walk warning | direct external owners already decisive; no re-entry |
| `OFP` | P154 involutive finite-group structure; P161 finite-field geometry; current polarity-threshold kills | classical involution and absolute shell; kill |

P162 random translation intersection, P163 complemented-shadow dynamics, and
P164 cyclic equality feedback use different literal carriers, but none opens
a slot: this lane is killed by older internal occupancy or direct owners.

## Final gate

```text
GCM  KILL_INTERNAL_TRAFFIC_TRANSDUCER
SRW  KILL_DIRECT_MATCHING_REWIRING_OWNER
OFP  KILL_DIRECT_POLARITY_INVOLUTION
GREEN 0
FINAL KILL_ALL
HOLD_EXTERNAL
```
