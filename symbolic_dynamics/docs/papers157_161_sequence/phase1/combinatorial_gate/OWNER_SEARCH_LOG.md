# Bounded owner search for replacement systems

**Date:** 2026-09-02 UTC  
**Scope:** the five strongest or most owner-sensitive replacements  
**Search mode:** generic keyword search, primary papers and journal pages
preferred  
**External state:** `HOLD_EXTERNAL`

No repository text or candidate proof was sent outside.  The searches below
establish positive adjacency or ownership; a non-hit establishes nothing.

## 1. `TLS`: cyclic Temperley--Lieb sweep on link patterns

### Queries

```text
Temperley Lieb product e_1 e_2 link patterns rotation boundary arc
noncrossing matching Temperley Lieb generator sweep rotation
link pattern preimages Temperley Lieb generator Catalan tree
```

### Hits and scope

1. S. Ng,
   [*Link Patterns and the Catalan Tree*](https://arxiv.org/abs/1305.4877),
   directly develops link-pattern generation by taking preimages of a fixed
   Temperley--Lieb generator.  This owns the carrier, local generator, and
   inverse-generator viewpoint.  It does not state the exact ordered cyclic
   sweep or its `1+returns` target fibre in the material inspected.
2. The primary FPL/link-pattern literature represented by
   [*Link patterns of quarter-turn symmetric FPL configurations*](https://dmtcs.episciences.org/3644/pdf)
   explicitly defines the cyclic generators by the same reconnection rule and
   records rotation of circular link patterns.  It owns both ingredients of
   the residual periodic core, although the bounded search did not locate the
   precise product `e_0...e_(2n-1)` as a named deterministic map.

### Internal chain and decision

P130 already uses chord matchings, a retraction to a noncrossing core, and
target-resolved fibres.  More decisively, after deleting the forced boundary
arc and rotating once, the TLS target indegree is exactly one plus the number
of primitive Dyck factors.  P144 proves the same primitive-factor cut inverse,
the same ballot distribution, and the same unique maximum fibre.  Therefore
the precise product non-hit cannot create paper value.

**Decision:** `KILL_P130_P144_TRANSFER`.

## 2. `DFG`: checkerboard toggles of ladder domino tilings

### Queries

```text
toggle group independent sets path bipartite Coxeter element orbit
domino tilings 2 by n face toggle gyration independent set path
```

### Direct hit

Michael Joseph and Tom Roby,
[*Toggling Independent Sets of a Path Graph*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i1p18),
Electronic Journal of Combinatorics 25(1), P1.18 (2018), DOI
[10.37236/6755](https://doi.org/10.37236/6755), directly studies Coxeter
elements of vertex toggles on path independent sets, including orbit sizes and
homomesy.

A `2 x n` domino tiling is exactly an independent set of the path of possible
horizontal blocks.  Even-face then odd-face toggling is a bipartite Coxeter
element in that direct owner's system.  The observed `3n-10` maximum cannot be
repackaged through the tiling encoding.

**Decision:** `KILL_DIRECT_OWNER`.

## 3. `MVT`: Markoff--Vieta rotor

### Queries

```text
Markoff triples modulo p Vieta involutions dynamics
Markoff surface finite field Nielsen moves orbit
```

### Direct hits

1. Campos-Vargas,
   [*Markoff triples and generating pairs of SL2(F_p)*](https://arxiv.org/abs/2508.21671),
   studies finite-field Markoff level sets, the action of Vieta involutions,
   exceptional orbits, and the Nielsen correspondence.
2. Palesi,
   [*Dynamique de l'action du groupe modulaire et triplets de Markov*](https://proceedings.centre-mersenne.org/articles/10.5802/tsg.298/),
   DOI [10.5802/tsg.298](https://doi.org/10.5802/tsg.298), supplies broader
   modular-group/Markoff-triple dynamics.

The scout update is a fixed word consisting of a coordinate cycle and one of
these Vieta generators.  A new theorem about that word would have to beat the
active orbit literature, not merely enumerate small primes.

**Decision:** `KILL_DIRECT_VIETA_ACTION`.

## 4. `HWT`: full Hurwitz sweep

### Queries

```text
Hurwitz action transposition factorizations long cycle full twist
Hurwitz action reduced reflection factorizations Coxeter element
```

### Direct hits

1. Baumeister, Gobet, Roberts, and Wegener,
   [*On the Hurwitz action in finite Coxeter groups*](https://arxiv.org/abs/1512.04764),
   proves the direct Hurwitz-action transitivity criterion for reduced
   reflection factorizations, including Coxeter elements.
2. Lewis and Reiner,
   [*Circuits and Hurwitz action in finite root systems*](https://nyjm.albany.edu/j/2016/22-63.html),
   studies Hurwitz orbits of reflection factorizations in finite real
   reflection groups.

The full-sweep power/conjugation identity is the standard braid full-twist
mechanism, and the `n^(n-2)` carrier count is the classical reduced
transposition-factorization count.  There is no owner-thin residual in merely
selecting one braid word.

**Decision:** `KILL_DIRECT_HURWITZ`.

## 5. `CRW`: greedy oriented reduced-word graph

### Queries

```text
oriented braid relations reduced words longest permutation rewriting
reduced word graph commutation braid moves diameter longest element
```

### Hits and scope

1. Jennifer Elder,
   [*On Graphs of Sets of Reduced Words*](https://arxiv.org/abs/2201.12887),
   directly defines the graph on reduced words with commutation and long-braid
   edges and studies its subgraphs/classes.
2. Reiner and Roichman,
   [*Diameter of reduced words*](https://arxiv.org/abs/0906.4768), determines
   braid-relation graph diameters for longest elements in finite reflection
   groups.

The exact leftmost lex orientation was not found as a named map.  That leaves
only an arbitrary deterministic scheduler on a directly owned relation graph;
its multiple local sinks and short census do not supply an invariant second
theorem.

**Decision:** `KILL_SCHEDULER_AND_WORD_GRAPH`.

## 6. Confirmatory direct-map hits

- Burrows and Wheeler's original report,
  [*A Block-sorting Lossless Data Compression Algorithm*](https://www.cl.cam.ac.uk/teaching/2425/Bioinfo/papers/burrows_wheeler.pdf),
  explicitly defines sorting all cyclic rotations and extracting the last
  column.  This is exactly `BWT`; its cyclic fibre is definitional.
- Rowmotion/promotion on order ideals and plane partitions has an extensive
  direct literature; for example Striker and Williams,
  [*Promotion and rowmotion*](https://doi.org/10.1016/j.ejc.2012.10.003),
  treats the operator and its classical product-of-chains context.  `PPR` is
  therefore a direct-map kill.

Latin parastrophe, projective polarity, and polygon rotation are classical
coordinate/group symmetries.  They were killed from their literal definitions
and unit-fibre/short-period silhouettes; a broader priority search would not
repair their missing independent axes.

## Summary

| candidate | positive owner result | unsupported scope | verdict |
|---|---|---|---|
| TLS | TL generators, their preimages, circular rotation | exact ordered product non-hit | killed internally by P130/P144 |
| DFG | exact path toggle/Coxeter system | none material | direct kill |
| MVT | finite-field Vieta/Nielsen orbit action | exact chosen-word census | direct-action kill |
| HWT | exact Hurwitz carrier/action | selected sweep cycle census | direct kill |
| CRW | reduced-word relation graph and diameter | exact greedy orientation | scheduler-thin kill |

The complete 12-system ledger is `REPLACEMENT_SCOUT.md`.  No search result
authorizes priority language, numbering, drafting, Git synchronization, or
external release.
