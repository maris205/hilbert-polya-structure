# BQC tree-fibre upgrade — focused specialist gate

**Object:** consecutive-block loopless OR quotient on labelled simple graphs  
**Prior status:** `AMBER_LOW_OWNER_AND_MASS_GATE`  
**Current author-side status:** `FOCUSED_GREEN_PENDING_INDEPENDENT_HOSTILE_GATE`  
**Lifecycle:** `HOLD_EXTERNAL`

## 1. Why this is not another marginal of the old edge-bin product

For time `t`, write `s=(s_1,...,s_m)` for the actual consecutive block
sizes, including the short last block.  The previous inverse polynomial lets
each source-edge bin act independently.  It cannot count source graphs which
are trees, because acyclicity and connectivity couple all bins globally.

Let `H` be a supported target.  Form the clique blow-up

```text
K(H;s)=H[K_(s_1),...,K_(s_m)]:
```

each target vertex becomes a clique of its actual block size, and each target
edge becomes a complete bipartite join.  A labelled source tree maps to
exactly `H` iff it is a spanning tree of `K(H;s)` and uses at least one edge
from every cross-block bin indexed by `E(H)`.  Consequently

```text
TreeFib_s(H)
  = sum_(F subseteq E(H)) (-1)^(|E(H)|-|F|) tau(K(F;s)).       (1)
```

This is Boolean-lattice inversion over required quotient edges, followed by
a Matrix--Tree calculation.  It is not obtained by specializing the old
source-edge polynomial: that polynomial forgets connectedness and cycles.

## 2. Reduced determinant for every summand

For a graph `F` on `[m]`, put

```text
D_i(F;s)=sum_(ij in E(F)) s_j,
alpha_i=s_i+D_i,
Q_ii=D_i,
Q_ij=-s_j  if ij in E(F), and 0 otherwise.
```

For any index `r`, let `Q^(r)` delete row and column `r`.  Block-constant and
within-block zero-sum subspaces of the full Laplacian give

```text
tau(K(F;s))
  = [det Q^(r) / s_r] product_i alpha_i^(s_i-1).              (2)
```

The expression is independent of `r`.  It also handles all boundaries:

- if `F` is disconnected, the cofactor is zero;
- for one block, it becomes Cayley's `s_1^(s_1-2)` (with the singleton
  convention equal to one);
- when all `s_i=1`, (1) is one for a tree target and zero otherwise;
- summing (1) over every target gives `n^(n-2)`.

Equations (1)--(2) are an exact every-time, every-target **tree-fibre atlas**
for the dynamical map.  The proof engine is global Laplacian decomposition,
not independent subset bins.

## 3. A small inverse result

The full phase size recovers `n`.  At time one the empty-target fibre is
`2^I`, where

```text
I(n,c)=sum_i binom(s_i,2).
```

For fixed `n`, `I(n,c)` is strictly increasing for `1<=c<=n`: increasing the
capacity from `c` to `c+1` moves vertices from later blocks into earlier
blocks, and each such move strictly increases the number of within-block
pairs before the partitions finally coalesce.  Thus the phase size together
with the time-one empty fibre identifies `(n,c)`.  This is useful but remains
a marginal of the edge-bin theorem and is not counted as the independent
upgrade; the tree atlas is the value-bearing third axis.

## 4. Exact falsification record

`verify_bqc_upgrade.py` uses only the Python standard library.  It:

1. generates every labelled tree through `n=8` independently by Pruefer
   words;
2. applies the literal consecutive-block quotient;
3. compares every target count, including zero fibres, with (1)--(2);
4. checks total Cayley mass and every boundary width `1<=c<=n`; and
5. checks strict parameter-probe monotonicity for every `2<=n<=512`.

The canonical transcript is stored beside this gate.  Computation is a
falsifier, not a proof.

## 5. Ownership subtraction

All of the following receive zero contribution credit:

- quotient graphs and existential adjacency under a vertex partition;
- independent edge-bin enumeration and powerset direct images;
- Kirchhoff's Matrix--Tree theorem and Cayley's tree count;
- clique/generalized-join blow-ups and their spanning-tree formula; and
- ordinary inclusion--exclusion.

The 2026 paper by Liu, Li, You, Hua, and Chen, *Enumeration of spanning trees
and resistance distances of generalized blow-up graphs*, DOI
`10.1016/j.dam.2025.11.014`, directly occupies generalized blow-up tree
enumeration.  Parthasarathy's 1968 paper, DOI `10.4153/CJM-1968-005-0`,
occupies graph enumeration relative to a prescribed partition.  Neither
record, on the inspected evidence, states the literal iterated quotient
dynamics or the required-edge inversion (1) resolving every target tree
fibre.  This is a bounded non-hit, never a priority claim.

After subtraction, the residual conjunction is:

1. the exact `c`-adic semigroup law and sharp edge-coalescence clock;
2. the every-time weighted all-source inverse atlas; and
3. the globally coupled every-time, every-target tree-fibre atlas (1)--(2).

This is now paper-sized on the author side, but an independent hostile gate
must decide whether the third axis is sufficiently separate or merely a
standard source-class refinement.  No paper number is assigned here.
