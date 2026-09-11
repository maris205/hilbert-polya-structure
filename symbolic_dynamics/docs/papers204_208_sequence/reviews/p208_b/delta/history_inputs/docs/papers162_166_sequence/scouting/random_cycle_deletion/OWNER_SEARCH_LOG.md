# RCD bounded owner and internal-collision log

Date: 2026-09-03  
Status: **KILL / HOLD_EXTERNAL / no novelty claim**

## Search clusters

Queries covered:

- random permutation delete cycle containing a uniformly chosen element;
- size-biased deletion of permutation cycles;
- Ewens deletion property and regenerative partition structures;
- unequal coupon collector first-appearance and last-coupon laws;
- permutations whose every cycle meets a fixed marked set;
- partial-permutation cycle deletion Markov chains;
- current 2025--2026 finite permutation/partition deletion records.

A bounded search did not locate a paper using precisely the full state space
of all partial permutations with the exact displayed arbitrary-transition
kernel.  This non-hit has no positive weight.

## Direct mechanism owners

### Size-biased block deletion and Ewens permutations

Gnedin, Haulk and Pitman,
[*Characterizations of exchangeable partitions and random discrete
distributions by deletion properties*](https://arxiv.org/abs/0909.3642),
select an individual uniformly and delete all individuals of the same type;
they explicitly identify this as a size-biased block pick and characterize
the associated partition families.  For a permutation, cycle supports are
the blocks.  Thus the stochastic deletion mechanism at the support-partition
level is direct prior art.

The older regenerative-partition literature likewise treats iterative
size-biased deletion and explicitly uses cycle-size partitions of uniform
permutations.  RCD claims no Ewens/Poisson--Dirichlet deletion property,
Chinese restaurant representation, regenerative structure, or size-biased
ordering.

### Unequal coupon collection and Plackett--Luce order

For a fixed source, cycle `C_i` is a coupon type with mass `|C_i|/n`; inactive
or previously hit labels produce null draws.  Inclusion--exclusion CDFs,
moment formulae, and first-appearance ordering are classical unequal-coupon
machinery.  Doumas and Papanicolaou,
[*The Coupon Collector's Problem Revisited*](https://arxiv.org/abs/1412.3626),
reviews moment and transform formulae for unequal probabilities.  The
size-biased first-appearance order is the standard Plackett--Luce/exponential
race.  These ingredients receive zero credit.

### Marked permutation cycles

The reverse identity `r(m-1)!` follows from the labelled `SET(CYC)` species
after forbidding an all-unmarked cycle, or from an elementary rooted-cycle
bijection.  Surjection counts for a fixed history support are ordinary
inclusion--exclusion/Stirling-number data.  No direct owner is required to
conclude that this single coefficient identity is not an independent
paper-scale axis.

## Internal collisions

- **P105:** already owns a permutation-cycle deletion dynamics, restricted
  cycle EGFs, sharp transient layers, recurrence, and inverse fibres.  RCD
  deletes whole cycles rather than their minima, so this is not literal
  equality, but the cycle-deletion carrier is occupied.
- **S06 in the P147--P151 stochastic scout:** “delete and shortcut a uniform
  active cycle element” was permanently killed as a generic random-order
  wrapper.  RCD uses a coarser whole-cycle deletion but relies on the same
  exchangeable random-scan principle.
- **P136:** its owned random covering process is resolved through
  size-biased/exponential order, inclusion--exclusion, and component products.
  RCD's last-survivor and absorption axes transfer this exact stochastic
  engine to permutation cycles.
- **P158:** already owns repeated random histories, an absorption CDF by
  inclusion--exclusion, complementary-history characterization, and a
  corrected every-labelled-target fibre.  RCD's forward kernel plus history
  support count has the same proof architecture with cycles replacing
  biclique components.
- **P155:** owns a variable-rank permutation-cycle map and target-resolved
  cycle-support fibres weighted by cyclic order `(b-1)!`.  RCD's proposed
  reverse axis is precisely a simpler cycle-support enumeration and loses all
  target shape beyond complement size.
- **P151:** generic first-passage transforms are nearby, but the unequal
  spider's continuant/extremal/inverse geometry is not a literal collision.
  It contributes only a broad warning that “an exact hitting-time law” alone
  is not residual theorem mass.

## Subtraction result

After owner subtraction, the only literal residue is packaging a fixed
partial permutation around a coupon collector.  The forward process forgets
cyclic orientations entirely and depends only on cycle sizes.  The reverse
enumeration reinstates orientations through the classical `(b-1)!` factor,
but produces the target-uniform identity `r(m-1)!`.  It neither separates
targets nor introduces a proof engine independent of the history support.

**Decision: KILL_OWNER_AND_INTERNAL_ENGINE_COLLISION.**  Keep the exact
formulas only as a negative scouting control.  External status remains
`HOLD_EXTERNAL`.
