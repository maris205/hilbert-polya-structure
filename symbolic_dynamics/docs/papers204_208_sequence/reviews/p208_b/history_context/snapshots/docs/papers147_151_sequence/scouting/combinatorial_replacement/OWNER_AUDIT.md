# Direct-owner and claim-subtraction audit: combinatorial replacements

**Date searched:** 2026-09-01.  **External status:** `HOLD_EXTERNAL`.
**Scope:** ELC, PKE, and FPD are audited separately; a search non-hit is never
used as positive evidence.  Only primary papers, author manuscripts, arXiv
records, DOI records, and publisher pages are cited.

## 1. Decision summary

| system | direct-map result | deductions made before scoring | residual theorem package | gate |
|---|---|---|---|---|
| **ELC** | no source found for the deterministic map that deletes every odd generation, promotes its ordered grandchildren, resets parity, and iterates it | Catalan carrier counts, generic vertex contraction, even/odd-level statistics, and the elementary height-halving observation receive zero credit | literal iterate law; sharp pointwise and extremal clock; every-target size-refined fibre `y^I/(1-y)^(2m-1)`; algebraic image series | **PASS_FOCUSED** |
| **PKE** | no source found for iterating the standardized ordered list of endpoint-inclusive peak values | all ordinary peak/pinnacle statistics, admissible pinnacle sets/orderings, and generic zigzag-poset linear-extension technology receive zero credit | exact images of every iterate, explicit right sections at every rank, sharp logarithmic clock, and target multiplicities after summing over comparison words | **PASS_REPAIRED** |
| **FPD** | the terminal derangement reduction is explicitly present in fix-Mahonian work; smallest-fixed-point enumeration also meets the scheduled insertion rule | derangement census, fixed-point distribution, standardization, and cycle-species factorization receive zero credit | only “delete least rather than all at once”, with clock equal to the initial number of fixed points | **KILL_DIRECT_TRANSFER** |

`PASS` here means paper-sized enough for internal Stage-1 continuation, not an
external novelty certificate.  ELC and PKE still require a specialist search
before paper allocation or release.

## 2. ELC: even-level contraction of plane trees

### 2.1 Exact literal searched

For a rooted plane tree, retain the vertices at even depth.  Each original
grandchild becomes a child of its grandparent, and the left-to-right order is
the concatenation of the intervening child blocks.  Reset the retained root to
depth zero and repeat.  The searches included the following combinations:

- `plane tree even-level contraction`, `even generation skeleton`;
- `rooted ordered tree grandchildren promotion`;
- `alternating levels edge contraction`, `grandchildren become children`;
- `operadic rooted-tree edge contraction`; and
- `Horton-Strahler reduction`, `tree pruning`, and `simultaneous rotation`.

The first four exact formulations produced no direct primary hit.  The last
two deliberately probe nearby mechanisms and did produce owners, but their
maps differ.

### 2.2 Primary-source subtraction

1. Chen, Li, and Shapiro,
   [*The Butterfly Decomposition of Plane Trees*](https://arxiv.org/abs/math/0511045),
   [DOI 10.1016/j.dam.2007.04.020](https://doi.org/10.1016/j.dam.2007.04.020),
   own doubly rooted plane-tree decompositions and parity identities for
   vertices/leaves at even and odd height.  ELC therefore claims no novelty
   for parity statistics or for Catalan encodings.
2. Berkemer, Höner zu Siederdissen, and Stadler,
   [*Compositional Properties of Alignments*](https://doi.org/10.1007/s11786-020-00496-8),
   explicitly use deletion/contraction in ordered forests so that children of
   a removed vertex are promoted in sibling order.  The primitive promotion
   operation receives zero credit.  Their map is driven by alignment labels;
   it does not select all odd generations, reset parity, iterate the resulting
   self-map, or enumerate its fibres.
3. Nichols, Pilz, Tóth, and Zehmakan,
   [*Transition Operations over Plane Trees*](https://arxiv.org/abs/1810.02839),
   [DOI 10.1016/j.disc.2020.111929](https://doi.org/10.1016/j.disc.2020.111929),
   obtain logarithmic bounds using simultaneous rotations/starification.
   ELC changes the vertex set and has a target-resolved insertion inverse; it
   is not a rotation system.  The bare phrase “logarithmic plane-tree
   transformation” consequently receives no credit.
4. Kovchegov and Zaliapin,
   [*Horton Law in Self-Similar Trees*](https://arxiv.org/abs/1511.01558),
   study repeated leaf pruning plus suppression of degree-two chains.
   Horton--Strahler order is a branching-complexity clock, whereas ELC's clock
   is the binary length of ordinary height.  Neither map nor inverse transfers.
5. Saïdi,
   [*Weighted rooted trees and deformations of operads*](https://arxiv.org/abs/1405.6854),
   and Mohamed--Manchon,
   [*Doubling bialgebras of rooted trees*](https://arxiv.org/abs/1605.03421),
   confirm that operadic substitution and tree contraction are mature
   algebraic operations.  ELC claims no novelty for generic contractions or
   operadic vocabulary.

### 2.3 Internal collision subtraction

- **P114** removes leaves in successive boundary layers.  ELC removes an
  entire parity class and promotes grandchildren; its height changes from
  `h` to `floor(h/2)`, not `h-1`.  P114's leaf-history inverse does not give
  ELC's ordered block-and-gap inverse.
- **P115** decimates coefficient indices and supplies a logarithmic index
  clock.  The generic “divide an index by two” clock is zero-credit.  ELC's
  target fibre comes from independently grouping each ordered child list and
  is not a coefficient-chain fibre.
- **P120** mirrors fringe subtrees without changing size; **P144** performs a
  leftmost Dyck reassociation; **ARC** consolidates equal adjacent composition
  runs.  None supplies the literal map, target inverse, or image series.

### 2.4 Residual after subtraction

Let `m=|U|` and let `I(U)` be the number of internal vertices of a target
plane tree.  The residual conjunction is

```text
E^k(T) retains precisely the original depths divisible by 2^k;
tau(T)=ceil(log2(height(T)+1));
sum_{E(T)=U} y^(|T|-|U|)=y^I(U)/(1-y)^(2m-1);
U is in E(T_n) iff |U|+I(U)<=n.
```

The fibre formula has been rederived locally and checked target by target:
at a target vertex of outdegree `d>0`, productive odd children cut its ordered
child list into nonempty consecutive blocks while empty odd leaves occupy the
gaps, giving `y/(1-y)^(d+1)`; a target leaf gives `1/(1-y)`.  Multiplication
uses `sum_v(deg(v)+1)=2m-1`.  This is not inferred from a state census.

**Gate: `PASS_FOCUSED`.**  Risk remains medium because generic tree
contraction is broad, but the exact deterministic self-map and the full
clock/fibre/image conjunction survived the sources actually located.

## 3. PKE: iterated standardized peak extraction

### 3.1 Exact literal searched

For a permutation `pi`, set fictitious boundary values to zero, read the
values at all local maxima from left to right, and standardize that subsequence.
Repeat on the resulting shorter permutation.  Queries combined `iterated
peaks`, `peak transform`, `local maxima subsequence standardization`,
`pinnacle order`, `ordered pinnacles`, and `peak-value extraction`.

No primary source found in this audit defines and iterates this exact map.

### 3.2 Primary-source subtraction

1. Davis, Nelson, Petersen, and Tenner,
   [*The pinnacle set of a permutation*](https://arxiv.org/abs/1704.05494),
   own the set of values appearing at peaks and its admissibility theory.
2. Rusu and Tenner,
   [*Admissible pinnacle orderings*](https://arxiv.org/abs/2001.08185),
   directly own the question of which relative orders of a fixed pinnacle set
   can occur.  PKE therefore claims no novelty for admissibility of an ordered
   peak-value list.
3. Domagalski, Liang, Minnich, Sagan, Schmidt, and Sietsema,
   [*Pinnacle Set Properties*](https://arxiv.org/abs/2105.10388), and Fang,
   [*Efficient recurrence for the enumeration of permutations with fixed
   pinnacle set*](https://arxiv.org/abs/2106.09147), own efficient static
   recurrences and counts for pinnacle sets/admissible orderings.
4. Alexandersson and Nabawanda,
   [*Peaks are preserved under run-sorting*](https://arxiv.org/abs/2104.04220),
   own a different size-preserving sorting map with a peak-value invariant.
   PKE is a size-decreasing extraction, not run-sorting; nevertheless all
   generic peak-statistic background receives zero credit.

The one-step PKE fibre is indexed only by the *standardized order* of all
endpoint-inclusive peak values, not by a prescribed pinnacle set.  Its exact
multiplicity is a sum of linear-extension counts over all comparison words.
The audit found existence/counting results for pinnacle sets and admissible
orders, but did not find this summed target multiplicity.  Because the proof
uses standard zigzag posets, it is retained as a secondary inverse axis, not
advertised as a stand-alone novelty claim.

### 3.3 Internal collision subtraction

PKE is not comparator sorting, record extraction, a run transform, or a
canonical relabelling of a fixed-size object.  Standardization only returns a
literal peak subsequence to the finite carrier
`S_{<=N}=disjoint_union_{m=1}^N S_m`.  P116 reverses cyclic runs and P132--P141
occupy records/borders/palindromes/Lyndon masks; none takes ordered local
maxima or has the same rank-halving image law.

### 3.4 Residual after subtraction

For every `n>=1` and `k>=1`, the exact rank image is

```text
P^k(S_n) = disjoint_union_{1<=m<=ceil(n/2^k)} S_m.
```

Every inclusion has an explicit right section.  For target `sigma in S_m`
and source length `n>=2m-1`, use the top `m` values in order `sigma`, put one
small valley between successive peaks, and append all unused low values in
decreasing order.  Repeating the minimal odd lift and using the remaining
length in the outer lift gives a section for every iterate.  Consequently

```text
max_{pi in S_n} tau(pi)=ceil(log2 n),
|P^k(S_n)|=sum_{m<=ceil(n/2^k)} m!.
```

Together with the target-indexed comparison-word/zigzag-poset multiplicity,
this is a complete temporal-image axis plus an inverse axis after all static
pinnacle claims are removed.

**Gate: `PASS_REPAIRED`.**  The paper contract must lead with iterated images,
right sections, and the sharp clock.  Pinnacle admissibility and fixed-set
enumeration must appear only as credited background.

## 4. FPD: least-fixed-point deletion

### 4.1 Direct owners

Désarménien and Foata,
[*Fix-Mahonian calculus, I: Two transformations*](https://doi.org/10.1016/j.ejc.2007.09.002),
explicitly form the derangement reduction `Der(sigma)` by deleting the fixed
points and reducing/standardizing the remaining word.  Thus FPD's endpoint is
directly owned.  Deutsch and Elizalde,
[*The largest and the smallest fixed points of permutations*](https://arxiv.org/abs/0904.2792),
study sums of smallest fixed points and the corresponding derangement
identities; this is the same insertion statistic that controls FPD's scheduled
one-step indegree.

### 4.2 Claim subtraction and decision

Deleting one singleton cycle preserves every other singleton cycle.  Hence
the least scheduler merely serializes the owned simultaneous reduction:

```text
tau(sigma)=fix(sigma),
endpoint=Der(sigma),
|basin_n(delta)|=binom(n,|delta|)
```

for each derangement target `delta`.  The basin formula is the classical
choice of labels supporting the non-singleton cycles, exactly the species
factorization already implicit in the derangement reduction.  Internal P105
also occupies cycle-component pruning.  No independent theorem remains.

**Gate: `KILL_DIRECT_TRANSFER`.**

## 5. Audit boundary

Searches were bounded and English-keyword dependent.  `PASS_FOCUSED` and
`PASS_REPAIRED` authorize only continued internal proof/audit work.  They do
not authorize submission, public claims, or assignment of a paper number.
