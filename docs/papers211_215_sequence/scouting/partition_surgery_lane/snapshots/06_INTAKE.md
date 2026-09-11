# Eighth finite-structure intake — fixed before numerical execution

2026-09-06 UTC. Current owner/author: `batch197_fifth_scout`.
The earlier [DESK_CHECKPOINT.md](DESK_CHECKPOINT.md), written by
`batch197_fosp_gate`, is preserved unchanged. It contains no executed
pilot or frozen cutoff. The six definitions and bounds below supersede
that tentative slate for this new bounded task; they do not retroactively
turn the desk proposals into completed attempts.

Only this directory is writable. No central index, old package, Git
operation, new paper ID or reserve is authorized here. P207 independent
Review B has priority when root supplies its physical frozen input; this
scout must checkpoint promptly when that happens.

The six literals span integer partitions, Boolean square matrices,
fixed-order DAGs, finite self-maps, and ordered capacity-item tuples.
The last carrier is explicitly tuple-based; it is not counted as an
additional non-word carrier. The two partition maps are distinct literals,
not two automatically independent research mechanisms.

## WGP — weighted-gap partition regrouping

For every integer partition $\lambda=(\lambda_1\ge\cdots\ge\lambda_k>0)$
of $N$, put $\lambda_{k+1}=0$ and replace it by the decreasing sort of
the positive integers $i(\lambda_i-\lambda_{i+1})$, one integer per
positive gap. The empty partition is fixed. Mass is preserved by
$\sum_i i(\lambda_i-\lambda_{i+1})=N$.

Fixed complete boxes: all partitions of $N=0,\ldots,24$.
This is **not** tentative DGR, which takes $i$ separate copies of
the gap. For example $(4,2,1)$ goes to $(3,2,2)$ here, while DGR
gives $(2,1,1,1,1,1)$. Gap coordinates and partition regrouping
are static primitives and receive no new value by themselves.

## DSR — Durfee-square repacking

On the same partition carriers and the same fixed $N=0,\ldots,24$,
let $d=\max\{i:\lambda_i\ge i\}$, with $d=0$ on empty input.
Subtract $d$ from each of the first $d$ parts, retain all later
parts, append one part $d^2$ when positive, discard zeros, and sort.
The removed square has exactly the appended mass, so this is a
self-map on partitions of $N$.

This is not the old Durfee-row solitaire C11, which subtracts only
1 from each of the first $d$ parts and appends $d$. Nor is it P113
principal-hook regrouping or P160 corner stripping. The old formulas
must not transfer merely because all use a Durfee size; all static
Durfee decomposition/partition enumeration credit is deducted.

## UPA — unique-permanental adjugate support

The carrier is all Boolean $n\times n$ matrices, including every
diagonal pattern. Define

$$F(A)_{ij}=\mathbf1\{\operatorname{per} A(j\mid i)=1\},$$

where $A(j\mid i)$ deletes row $j$ and column $i$, and the permanent
is the ordinary nonnegative integer matching count. The empty minor
has permanent 1. The $0\times0$ matrix is fixed.

Fixed complete boxes: $n=0,\ldots,4$, at most 65,536 matrices.
Do not replace equality to 1 by positivity or parity. For $n\le3$
the minor sizes are at most two, so this agrees with characteristic-two
adjugation. P103/Jacobi deductions consume that slice; it cannot
justify a new matrix theorem. The first genuinely different tested
minor size is three. General matching/permanent theory is also deducted.

## DP3 — path-count residue-one DAG feedback

The carrier is every directed graph on $\{0,\ldots,n-1\}$ whose
edges satisfy $i<j$. Include $i\to j$ in the output exactly when the
number of positive-length directed paths from $i$ to $j$ is congruent
to 1 modulo 3. Empty graphs and the $n=0$ carrier are included.

Fixed complete boxes: $n=0,\ldots,6$, at most 32,768 DAGs.
This is not the old UPC exactly-one-path literal; the complete ordered
DAG on four vertices has four paths from 0 to 3, so DP3 retains that
pair and UPC does not. Directed path counting, incidence-algebra
inversion and a generic triangular Boolean reset/flip mechanism must
be deducted before attributing a temporal advance.

## BRF — backward-reachability cardinality feedback

For every self-map $f:\{1,\ldots,n\}\to\{1,\ldots,n\}$ set

$$F(f)(i)=|\{j:\text{for some }k\ge0,\ f^k(j)=i\}|.$$

The count includes $i$, so lies in $\{1,\ldots,n\}$. For $n=0$
the unique empty function is fixed.

Fixed complete boxes: $n=0,\ldots,6$, at most 46,656 functions.
This literal was suggested in the prior desk checkpoint; that provenance
is retained. It is not old OS (forward-orbit cardinality minus one),
old HC (immediate indegree modulo $n$), or old eventual-period feedback.
Classical functional-graph decomposition and occupancy counts are owned;
their availability does not itself close a full inverse or temporal theorem.

## FFR — first-fit residual feedback

Fix capacity $M\ge0$ and number of ordered items $k\ge0$.
The carrier is every tuple in $\{0,\ldots,M\}^k$. Process items
in the stated order by ordinary first fit: place an item into the
earliest opened bin with enough unused capacity, opening a new bin
of capacity $M$ when none qualifies. After **all** placements, replace
each original item by the final unused capacity of its assigned bin.
Zero items fit the first existing bin; a first zero opens a bin.
An empty tuple remains empty. These conventions include $M=0$.

Fixed complete boxes: every $M=0,\ldots,5$ and $k=0,\ldots,5$.
This literal also comes from the prior desk checkpoint. Ordinary
first-fit packing and any bin-assignment/polytope inverse are static
inputs, not separate claims. This is not a rank, contrast, or HVD rule.

## Pre-pilot rejected directions and gate

No numerical execution has preceded this intake. The internal literal
search already excludes the following as non-executed alternatives:

- unique-path UPC, the sixth lane's full closure-generator adapter;
- odd cyclic-triangle reversal, exactly historical TCR;
- ordinary Boolean permanental adjugate positivity: its perfect-matching
  branch is a permutation-twisted transitive-closure operation;
- DTD edge-span doubling, old filtration/erosion; greedy forest
  complementation, ordinary activity intervals; principal hooks,
  graph closures, Gram/Fitting maps, rank/contrast/HVD variants.

The first pilot is exactly these 105 fixed complete boxes. Neither a
maximum cutoff nor an additional full box may be added to rescue a weak
signal. Subsequent checks must address a stated proof or collision in
the same boxes. A retained proposal requires proved all-parameter
temporal/core structure and a materially separate evaluated inverse or
extremal residual after full deductions. Otherwise record NO_PROMOTION,
not a reserve. Numerical agreement alone proves no all-size assertion.
