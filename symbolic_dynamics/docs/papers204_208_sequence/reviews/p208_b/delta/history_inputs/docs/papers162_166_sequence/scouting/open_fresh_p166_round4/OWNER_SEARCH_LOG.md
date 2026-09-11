# P166 Round-4 owner and collision audit

Status: **bounded search complete / KILL_ALL / HOLD_EXTERNAL**  
Search date: 2026-09-03.

This log records source subtraction, not novelty certification.  Scholarly
searches used literal-map phrases, equivalent algebraic descriptions, and
carrier-specific keywords.  A non-hit never counted as a novelty result.

## GDI — direct public literal owner

Queries included `"x + gcd(x,n)" functional graph`, `gcd cascade map Z/nZ`,
and the height sequence `sum e(p-1)`.

- Dhruv Palla, “Functional graph of `x -> x+gcd(x,n)` on `Z/nZ`,” Mathematics
  Stack Exchange, asked 12 June 2026:
  <https://math.stackexchange.com/questions/5140351/functional-graph-of-x-mapsto-x-gcdx-n-on-mathbbz-n-mathbbz>.
  This is the exact literal map.  The answer derives the least-prime
  recursion and the orbit length of `1`.
- OEIS A059975, internal record:
  <https://oeis.org/A059975/internal>.  As of the frozen record, its comments
  explicitly identify the number of iterations from `1`, call it the height
  of this rooted functional graph, link the Palla discussion, and give
  `a(n)=sum e_i(p_i-1)`.

The target-fibre divisor condition may not be present there, but a new inverse
corollary is insufficient after the literal system and sharp temporal axis
are publicly owned.  Internally, P128 (`translation-gcd-depth-fibres`) and
P142 (`valuation-gcd-prime-power-divisors`) also make gcd stratification and
depth/fibre arguments unavailable as a fresh proof engine.

Decision: **direct owner kill**.

## CSP — standard power-map neighborhood and trivialization

Queries included `functional graph power map finite groups`, `permutation
centralizer order power`, and `state-dependent exponent centralizer size`.

- C. Qureshi and L. Reis, “On the functional graph of the power map over
  finite groups,” Discrete Mathematics 346 (2023), arXiv:
  <https://arxiv.org/abs/2107.00584>.
- E. Larson, “Power maps in finite groups,” arXiv:
  <https://arxiv.org/abs/1707.06696>.

No source is needed to kill the exact proposed map: the centralizer order of
a permutation contains every occurring cycle length as a factor, so the map
is identically the group identity.  P102 and P154 are the closest internal
group-algebra/normalizer occupants.

Decision: **no residual theorem**.

## POC — internal proof-engine collision

External queries for the exact adaptive outer-product map did not locate a
direct owner.  That non-hit receives no positive credit.  The internal test is
decisive:

- P127 (`parity-transpose-looped-digraphs`) already has a binary matrix
  carrier, row/column margins, a rank-one parity correction, an even-hyperplane
  image, exact tail one, small recurrent periods, and a codomain-wide
  `0/1/large` fibre trichotomy.
- POC changes square matrices to rectangles and deletes the transpose.  All
  main proofs still proceed through exactly the same parity quotient and
  margin reconstruction.

Decision: **P127 proof-silhouette kill**, despite complete formulas.

## CTC — classical self-commutator, thin residual

Queries included `self-commutator AA* - A*A`, `AA^T-A^TA 2 by 2 finite
field`, `normal matrices self commutator`, and `image of matrix
self-commutator`.

- The operation `[A,A^*]=AA^*-A^*A` is standard in the theory of normal
  matrices; vanishing is precisely normality.  One representative primary
  treatment is Elsner and Ikramov, “Normal matrices: an update,” Linear
  Algebra and its Applications 285 (1998), 291--303 (the accessible scan used
  in the search discusses the self-commutator):
  <https://www.ee.iitb.ac.in/~belur/ee636/files/books/normal-matrices-20-elsner.pdf>.
- Bounded searches found no direct source treating iteration of this exact
  `2 x 2` finite-field map.  This is a non-hit, not a novelty finding.

The reason to kill is structural.  Every first output is symmetric, so the
second output is zero by the defining normality identity.  The remaining
odd/char-2 calculations are a two-variable quadratic image and fibre count.
The rank split is the standard isotropy count for `x^2+y^2`.  Internally:

- P103 owns polynomial matrix collapse/image staircases;
- P125 owns depth-at-most-two quadratic-state fibres and exact depth layers;
- P127 owns shallow matrix feedback plus every-target fibres;
- P161 owns a height-two finite-field quadratic/singular fibre atlas.

No one comparison is asserted as literal duplication.  Together they leave
no independent second axis after the classical self-commutator is subtracted.

Decision: **theorem-thin/collision kill**.

## DPS — classical Seidel switching and P127

Queries included `Seidel switching Eulerian graphs`, `switching classes
Euler graphs equal in number`, and `odd degree set switching`.

- C. L. Mallows and N. J. A. Sloane, “Two-graphs, switching classes and Euler
  graphs are equal in number,” SIAM Journal on Applied Mathematics 28 (1975),
  876--880.  Its title and bibliographic record are visible in the references
  of Harries--Liebeck:
  <https://doi.org/10.1017/S144678870001199X>.
- A. Abiad, S. Butler, and W. H. Haemers, “Graph switching, 2-ranks, and
  graphical Hadamard matrices,” arXiv:
  <https://arxiv.org/abs/1801.01149>, is a modern primary reference for the
  established Seidel-switching setting.

The adaptive choice of the odd set gives a neat parity calculation, but the
odd-`n` projection onto Eulerian graphs sits directly on the classical
switching/Eulerian correspondence.  Internally its parity collapse,
uniform-fibre linear quotient, and involutive even branch collide with P127.

Decision: **classical-owner plus internal-engine kill**.

## HOP — no direct owner hit, no closed theorem

Queries included `hypergraph boundary graph triangles parity dynamics`,
`edge lies in odd number of triangles operator`, `A Hadamard A^2 mod 2 graph
map`, and `triangle hypergraph boundary iteration`.

The search returned the mature surrounding subjects—simplicial boundary
operators, triangle enumeration, and nonlinear Boolean adjacency
operations—but no direct theorem for this exact iteration.  That non-hit was
not promoted.  The attempted every-target law retains the unevaluated factor

```text
#{Eulerian g : Tri(g)=K},
```

and the quotient census changes substantially at `n=6,7`.  Internally P97
(relation/sumset squaring) and P143 (nonlinear Boolean row residual) are the
nearest algebraic silhouettes, but the primary failure is earlier: there is
no all-parameter temporal or inverse theorem to compare.

Decision: **mathematical-spine kill**.

## CTR — classical tree center and thin marker motion

Queries included `tree center one vertex two adjacent Jordan`, `move vertex
toward tree center dynamics`, and `self-stabilizing tree center`.

- Jordan's theorem that a tree center is one vertex or two adjacent vertices
  is classical; a modern primary discussion is P. J. Slater, “Centers to
  centroids in graphs,” Journal of Graph Theory 2 (1978), 209--222:
  <https://doi.org/10.1002/jgt.3190020304>.
- S. Ghosh, A. Gupta, T. Herman, and S. V. Pemmaraju, “Self-stabilizing
  algorithms for finding centers and medians of trees,” SIAM Journal on
  Computing 30 (2000), provides a direct algorithmic tree-center owner
  neighborhood: <https://doi.org/10.1137/S0097539798427156>.

The precise marked-root map did not appear in the bounded search.  Its entire
proof, however, is unique-path distance bookkeeping on a fixed tree.  P151
already occupies a finite-tree moving-marker/first-passage interface; P148 is
not a literal collision because it contracts a plane tree, but it reinforces
that no credit is available for classical center geometry alone.

Decision: **thin static-marker kill**.

## Aggregate conclusion

| candidate | direct literal owner | classical ingredient consumes main axis | internal silhouette fatal | gate |
|---|---:|---:|---:|---|
| GDI | yes | yes | P128/P142 reinforce | KILL |
| CSP | no exact adaptive owner needed | yes | P102/P154 reinforce | KILL |
| POC | no hit | no | P127 | KILL |
| CTC | no exact dynamic hit | yes | P103/P125/P127/P161 | KILL |
| DPS | classical correspondence | yes | P127 | KILL |
| HOP | no hit | background only | not reached | KILL |
| CTR | no exact marker-map hit | yes | P151; nearby P148 | KILL |

No owner-thin survivor remains.  `KILL_ALL` is intentional and should not be
weakened to fill the P166 slot.

