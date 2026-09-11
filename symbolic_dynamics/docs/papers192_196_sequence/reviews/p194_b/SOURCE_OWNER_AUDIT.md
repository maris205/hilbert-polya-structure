# P194 Review-B source and owner-collision audit

## Decision

The repaired bibliography and subtraction boundary pass Review B.  One
historical Major omission is resolved; there are no open source or collision
findings.  The result is only an internal nonidentity audit:

`OWNER_AMBER / HOLD_EXTERNAL / NOVELTY_CLAIM_NOT_AUTHORIZED`.

## Closest external dynamical source

The primary record is Colin Defant and Nathan Williams, *Crystal Pop-Stack
Sorting and Type A Crystal Lattices*, *European Journal of Combinatorics* 103
(2022), 103514, DOI
[10.1016/j.ejc.2022.103514](https://doi.org/10.1016/j.ejc.2022.103514),
[arXiv:2109.08251](https://arxiv.org/abs/2109.08251).

Their Definition 2.1 starts from a vertex `b`, freezes the set of colours of
edges entering `b`, restricts the crystal to those colours, and sends `b` to
the unique source of its connected component in that restricted crystal.
Their operator is noninvertible; every forward orbit contains the
highest/minimal vertex, and the maximum orbit size is the Coxeter number.
These orbit-to-highest and sharp-orbit results directly occupy the generic
deterministic crystal-sorting surface.

The repaired P194 manuscript cites and zero-credits that entire surface.
Its residual map is literally different:

| feature | Defant--Williams pop-stack | P194 |
|---|---|---|
| colours used in one epoch | all colours in the starting descent set | the least currently usable colour only |
| size of update | unique source of a restricted connected component; potentially many edges | exactly one `e_i` edge |
| feedback | descent set is frozen for the macrostep | availability is recomputed after the edge |
| retained enumeration | no credit claimed by P194 for orbit convergence or sharpness | labelled one-step `f_i` predecessor atlas and stable full-fibre threshold |

In P194's three-letter convention, `321` has both colours available.  The
restricted component on those two colours has source `111`, whereas P194's
one epoch is `e_1(321)=311`.  This gives a direct literal nonidentity witness;
it does not prove novelty.

## Bibliography integrity

The current manuscript cites exactly these six keys, and the bibliography
contains exactly the same set:

```text
BumpSchilling2017
DefantWilliams2022
Fulton1997
Kashiwara1991
Sagan2001
Stanley2023
```

The first five classical subject areas—crystal bases/operators, word-crystal
components, RSK/tableaux, Schur specialization, hook formulas, and the RSK
involution correspondence—are explicitly zero-credit.  Defant--Williams is
also zero-credit.  No source is used to claim the P194 scheduler theorem, and
no bounded non-hit is promoted to novelty evidence.

## Internal-history collision matrix

| occupied surface | transfer pressure | binding subtraction/nonidentity |
|---|---|---|
| P144 leftmost Dyck reassociation | least/leftmost available move, ballot language, exact fibres | generic scheduler and ballot credit are removed; P144 changes a Dyck factor by reassociation, while P194 changes one letter on a coloured crystal edge |
| P181 first-descent prefix reversal | first defect, target-local inverse test | selector form and generic inverse bookkeeping are removed; P181 has a prefix reversal and a shallow fixed/2-cycle core, unlike P194's component sinks and weight tail |
| P142--P146 scout P02 | RSK insertion-tableau retraction and recording-tableau fibres | the RSK-retraction firewall is respected because P194 never applies RSK as its update; every RSK decomposition fact is zero-credit |
| P152--P156 RSK shape process | Schur/RSK layer and endpoint laws | those classical enumerative axes are zero-credit; P194 retains only a labelled word-level edge scheduler and target atlas |
| P166 RSK diagonal/recording feedback | RSK feedback, hook and involution counts | P194's update is a Kashiwara edge on the original word; its involution census carries no residual credit |
| P113 principal-hook partition dynamics | Ferrers/hook vocabulary, monotone clock, fibres | P113 regroups partition cells; neither its update nor inverse engine gives P194's signature-conditioned `f_i` sources |
| standing 0-Hecke/sorting firewall | ordered simple colours, descents, monotone rank | generic least-descent and sorting credit are removed; the surviving target condition tests lower-colour availability after a specific lowering |
| P192 within-batch Hurwitz scheduler | adaptive least-index move and exact inverse atlas | P192 changes adjacent factors with fixed product and an advancing index; no crystal-signature or Schur-component theorem transfers |
| P193 within-batch block sorting | word/permutation carrier and deterministic scheduler | P193 simultaneously swaps positions and refines direct-sum blocks; P194 changes a letter value and stays in a crystal component |

No inspected item gives a literal conjugacy that preserves the full tuple

```text
(tensor order, sign encoding, cancellation, edited occurrence,
 least-colour order, one-edge recomputation, targetwise inverse test).
```

That bounded non-hit is convention-sensitive and cannot clear ownership.

## Repair acceptance

P194-B1 is closed because the current manuscript and all named companion
ledgers:

- give the exact Defant--Williams bibliographic coordinates;
- describe the restricted-descent component-source definition;
- grant zero contribution credit to its convergence and maximum-orbit
  surface;
- state the one-edge/recompute distinction without turning it into a novelty
  claim;
- retain `OWNER_AMBER / HOLD_EXTERNAL`.

Any later source implementing the same least-current one-edge schedule up to
word reversal, colour reversal, or another full convention conjugacy—or a
result mechanically transferring the labelled predecessor atlas—must reopen
the owner gate.
