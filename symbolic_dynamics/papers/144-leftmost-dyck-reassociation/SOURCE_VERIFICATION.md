# Source verification and ownership boundary

**Verification date:** 2026-09-01 UTC
**Status:** bounded author-side source check; **OWNER-THIN / HOLD_EXTERNAL**.
This ledger verifies metadata, records the literal-move comparison demanded by
round 1, and subtracts supported prior ingredients. It does not grant
priority, originality, or release clearance.

## Verification protocol and bounds

- DOI metadata was checked against official publisher or journal records.
- Pallo (2006) was read from the University of Szeged's official *Acta
  Cybernetica* repository; article pp. 802--803 were inspected in full.
- Chapoton (2020) was read from the journal's official Centre Mersenne PDF;
  Section 1.2, especially p. 438, was inspected in full.
- Pallo (2003) metadata and abstract were checked on the official Elsevier
  record, and its comb-order role was cross-checked against Chapoton's explicit
  attribution on p. 438.
- The plane-tree carrier was checked in the official Cambridge excerpt of
  Stanley, Theorem 1.5.1, which gives the standard Catalan bijections among
  plane trees, binary trees, and Dyck paths.
- Searches were bounded to the primary or official records returned by the
  exact queries recorded below. Search non-hits are not novelty evidence.

`references.bib` contains seven cited entries: the four author-stage
background sources and the three direct rotation/comb sources added in round
1.

## Direct rotation and comb sources added in round 1

### `Pallo2006Rotational`

- **Author:** Jean Marcel Pallo
- **Title:** “Rotational Tree Structures on Binary Trees and Triangulations”
- **Venue:** *Acta Cybernetica* 17(4), 799--810
- **Year:** 2006
- **Primary record:** <https://acta.bibl.u-szeged.hu/12796/>
- **Primary PDF:**
  <https://acta.bibl.u-szeged.hu/12796/1/Pallo_2006_ActaCybernetica.pdf>
- **Inspected locus:** pp. 802--803. Pallo selects the leftmost eligible
  left-rotation, proves that the operation is unique away from the greatest
  tree, and obtains a directed tree with a unique greatest root, together with
  a grading and a restricted rotation distance.
- **Credit subtraction:** the idea of a deterministic leftmost-rotation
  scheduler, its rooted functional tree, rank, and distance precede this note
  and receive zero contribution credit.
- **Separating invariant:** after fixing Pallo's unique terminal root, that map
  has one fixed state. `Phi_n` has `Cat_(n-1)` fixed states, so for `n>=3` the
  maps are neither equal nor conjugate, including under mirror or reversal.
  This source is not cited as an owner of the literal `Phi_n` rule.

### `Pallo2003RightArm`

- **Author:** Jean Marcel Pallo
- **Title:** “Right-Arm Rotation Distance between Binary Trees”
- **Venue:** *Information Processing Letters* 87(4), 173--177
- **Year:** 2003
- **DOI:** <https://doi.org/10.1016/S0020-0190(03)00283-7>
- **Metadata gate:** official Elsevier title, author, volume, issue, pages,
  date, DOI, and abstract.
- **Role:** primary binary-tree source to which Chapoton attributes the comb
  (right-arm or left-arm under the relevant conventions) rotation order.
- **Credit subtraction:** the arm-restricted rotation family and its distance
  are zero-credit background. This article is not used to assert the
  depth-refined fibres of `Phi_n`.

### `Chapoton2020DyckOrder`

- **Author:** Frédéric Chapoton
- **Title:** “Some Properties of a New Partial Order on Dyck Paths”
- **Venue:** *Algebraic Combinatorics* 3(2), 433--463
- **Year:** 2020
- **DOI:** <https://doi.org/10.5802/alco.98>
- **Official record/PDF:**
  <https://alco.centre-mersenne.org/articles/10.5802/alco.98/>
- **Inspected locus:** Section 1.2, p. 438. The paper states that comb-order
  covers are precisely Tamari covers for which the slid subpath is at height
  zero, and attributes the binary-tree comb order to Pallo.
- **Credit subtraction:** every nonfixed `Phi_n` edge is one of these
  ground-level comb/Tamari covers; `Phi_n` merely chooses the cover at the
  leftmost ground return. The comb/height-zero correspondence and the atomic
  move receive zero contribution credit.
- **Does not establish here:** Chapoton does not specify the repeated `Phi_n`
  selector or its terminal depth-fibre conjunction.

## Plane-tree carrier and graft/lift subtraction

### `Stanley2015Catalan`

- **Author:** Richard P. Stanley
- **Title:** *Catalan Numbers*
- **Publisher/year:** Cambridge University Press, 2015
- **DOI:** <https://doi.org/10.1017/CBO9781139871495>
- **Inspected locus:** official Cambridge excerpt, Theorem 1.5.1, including
  the standard bijections among plane trees, binary trees, and Dyck paths.
- **Carrier translation:** under the contour bijection, the primitive factors
  `C_1,...,C_k` are exactly the contour words of the ordered subtrees rooted at
  the root's children `T_1,...,T_k`. Therefore

  ```text
  (T_1,T_2,T_3,...,T_k)
      -> (T_1 with T_2 appended as its rightmost child,T_3,...,T_k).
  ```

  The clock is root degree minus one. If a terminal root has unique child
  `S`, the depth-`d` inverse lifts the last `d` children of `S`, in order, to
  become root-level siblings.
- **Credit subtraction:** the contour carrier and this immediate graft/lift
  rewriting are representation-level background, not standalone residual
  claims. Stanley is not cited as asserting the repeated temporal/fibre
  conjunction.

## Other verified background sources

### `HuangTamari1972Associativity`

Samuel Huang and Dov Tamari, “Problems of Associativity: A Simple Proof for
the Lattice Property of Systems Ordered by a Semi-Associative Law,” *Journal
of Combinatorial Theory, Series A* 13(1), 7--13 (1972), DOI
<https://doi.org/10.1016/0097-3165(72)90003-9>. Crossref/publisher metadata
agree. Role: associativity/Tamari lattice background; zero credit.

### `BousquetMelouFusyPrevilleRatelle2012Intervals`

Mireille Bousquet-Mélou, Éric Fusy, and Louis-François Préville-Ratelle, “The
Number of Intervals in the m-Tamari Lattices,” *Electronic Journal of
Combinatorics* 18(2), P31 (2012), DOI
<https://doi.org/10.37236/2027>. Crossref and journal PDF were checked. Role:
path formulations of Tamari-type covers and m-ballot context; zero credit.

### `PanayotopoulosSapounakis2002Prime`

A. Panayotopoulos and A. Sapounakis, “On the Prime Decomposition of Dyck
Words,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 40,
33--39 (2002). The Combinatorial Press record and PDF were checked; no DOI is
asserted. Role: primitive decomposition and enumeration by prime-component
count; the complete component/ballot census is zero credit.

## Literal comparison of the three move descriptions

| description | carrier and selected move | terminal structure | relation to `Phi_n` |
|---|---|---|---|
| `Phi_n` | Dyck path; slide the component after the leftmost ground return across the preceding down-step | forest with `Cat_(n-1)` primitive roots | literal map studied here |
| Pallo (2006) | binary tree; unique leftmost eligible left-rotation | directed tree with one greatest root | genuinely different selector; fixed-root count excludes equality or mirror/reversal conjugacy for `n>=3` |
| comb cover, Pallo (2003)/Chapoton (2020) | arm-restricted binary rotation; equivalently a Tamari cover whose moved Dyck subpath is at height zero | a partial order, not a deterministic map | every nonfixed `Phi_n` edge lies in this cover family; `Phi_n` selects its leftmost available ground cover |
| contour plane tree | graft second root child as rightmost child of the first; inverse lifts a suffix | root degree falls by one per update | exact conjugate representation of `Phi_n`, assigned zero standalone credit |

## Reproducible bounded search log

Sources queried: University of Szeged *Acta Cybernetica* repository, Centre
Mersenne/*Algebraic Combinatorics*, Elsevier/ScienceDirect, Cambridge Core and
its official book excerpt, Crossref metadata, and bounded web discovery used
only to locate primary records.

Exact query families:

```text
"leftmost rotation" binary trees Pallo
"Rotational tree structures on binary trees and triangulations"
"comb partial order" Dyck paths height zero
"Right-arm rotation distance between binary trees"
"ordered plane forest grafting" Dyck paths
"rightmost child graft" plane tree Dyck path
"root rotation" plane tree Dyck
"first-child/next-sibling" comb order Dyck
```

Inspected direct hits were Pallo (2006), Chapoton (2020), Pallo (2003), and
Stanley's official Theorem 1.5.1 excerpt. The grafting queries also returned
generic plane-tree grafting and first-child/next-sibling literature, but no
primary source in this bounded pass was found that stated the same literal
all-time/target-fibre conjunction. This non-hit is only a search limitation;
it is not evidence of novelty, priority, or release readiness.

## Residual after subtraction

No standalone credit remains for deterministic leftmost rotations,
ground-level comb/Tamari covers, primitive factors, the root-degree clock, the
contour graft/lift model, Catalan/ballot layers, or generic coefficient
extraction. The only retained internal residual is the conjunction, for the
specific literal selector `Phi_n`, of its all-time iterate formula and the
target-indexed statement that each feasible depth has exactly one specified
source. Its fibre polynomial and extremal target are consequences of that
conjunction.

No inspected source was used to certify that conjunction as new. The package
therefore remains **OWNER-THIN / HOLD_EXTERNAL**.
