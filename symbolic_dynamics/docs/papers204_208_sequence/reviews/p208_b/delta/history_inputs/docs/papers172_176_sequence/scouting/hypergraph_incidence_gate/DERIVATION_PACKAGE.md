# Derivation Package

## Target

Derive the finite dynamics of the following literal update on labelled
$3$-uniform hypergraphs on $[n]$: a triple is present at the next time exactly
when the sum of the three current pair-codegrees on that triple is odd.

The requested outputs are the operator identity, odd/even temporal law, rank,
complete functional graph, all-time fibres, and boundary-graph
reconstruction.

## Status

`COHERENT AS STATED`.

No approximation or unproved heuristic is used.  The external/internal owner
decision is negative and is logically separate from coherence.

## Invariant Object

The organizing object is the **boundary graph** $b=Wx$, not the hypergraph
edge count or the Johnson spectrum.  It lies in the Eulerian cycle space of
$K_n$, and the update is its coboundary:

$$
x\xmapsto{W}b\xmapsto{W^{\mathsf T}}Lx.
$$

This factorization carries both the time law and the inverse reconstruction.

## Assumptions

- Coefficients are in $\mathbb F_2$.
- The vertex set is labelled and the carrier contains all $\binom n3$
  possible triples.
- $W$ is the pair-versus-triple inclusion matrix.
- Fibres are labelled fibres; there is no isomorphism quotient.

## Notation

- $C_2,C_1,C_0$ are the triangle, edge, and vertex chain spaces of the full
  simplex.
- $W:C_2\to C_1$ and $D:C_1\to C_0$ are consecutive boundary maps.
- $Z=\ker D=\operatorname{im}W$ is the Eulerian graph space.
- $B=\operatorname{im}D^{\mathsf T}$ is the cut space.
- $\mathcal B=Z\cap B$ is the bicycle space.
- $L=W^{\mathsf T}W$ is the literal update.

## Derivation Strategy

First identify the coordinate rule with the incidence Gram operator.  Then
move one dimension down to the boundary graph and compute
$WW^{\mathsf T}$.  Restriction to $Z$ collapses that operator to a parity
scalar.  Finally, use the bicycle kernel to derive rank and reconstruction,
and use linear-map fibres to derive the functional graph.

## Derivation Map

1. Common pairs of triples give $L=I+A(J(n,3))$.
2. The chain identity $DW=0$ and a triangle-fan basis give
   $\operatorname{im}W=Z$.
3. Common triangles of edges give
   $WW^{\mathsf T}=(n\bmod2)I+D^{\mathsf T}D$.
4. Since $Db=0$ for $b=Wx$, the preceding identity gives
   $L^2=(n\bmod2)L$.
5. The kernel of $W^{\mathsf T}$ on $Z$ is $Z\cap B$.
6. The binary Laplacian of $K_n$ gives bicycle dimension zero for odd $n$
   and $n-2$ for even $n$.
7. Rank-nullity supplies ranks, fibres, depth layers, and zeta functions.
8. The two kernels in the factorization supply boundary and hypergraph lift
   multiplicities.

## Main Derivation

### Step 1: literal algebra

Two different triples contribute an off-diagonal $1$ to $W^{\mathsf T}W$
exactly when they share a pair.  A triple has three pairs, which contributes
a diagonal $1$ modulo two.  Therefore

$$
L=I+A(J(n,3)).                                             \tag{1}
$$

### Step 2: the boundary sufficient statistic

The full simplex has no first homology, and constructively the
$\binom{n-1}{2}$ triangles through a fixed vertex form a basis of the cycle
space.  Hence

$$
\operatorname{im}W=Z,\quad
\dim Z=\binom{n-1}{2},\quad
\dim\ker W=\binom{n-1}{3}.                                \tag{2}
$$

### Step 3: parity acts one dimension lower

For two edges, the number of common triangles is $n-2$ on the diagonal, one
when the distinct edges meet, and zero otherwise.  Thus

$$
WW^{\mathsf T}=\epsilon I+D^{\mathsf T}D,\qquad
\epsilon=n\bmod2.                                         \tag{3}
$$

On $Z$, the second term vanishes.  Therefore

$$
L^2=\epsilon L.                                            \tag{4}
$$

This is an identity, not an approximation.

### Step 4: rank through bicycles

The restriction $W^{\mathsf T}|_Z$ has kernel
$Z\cap Z^\perp=Z\cap B$.  For $K_n$, a cut determined by a vertex subset is
Eulerian only for the zero complementary pair when $n$ is odd, while for
even $n$ the even vertex subsets modulo complementation form an
$(n-2)$-dimensional space.  Hence

$$
\operatorname{rank}L=
\begin{cases}
\binom{n-1}{2},&n\text{ odd},\\
\binom{n-2}{2},&n\text{ even}.
\end{cases}                                                \tag{5}
$$

### Step 5: dynamics and inverse reconstruction

For odd $n$, equations (4)--(5) make $L$ a projection with
$2^{\binom{n-1}{2}}$ fixed states.  Every nonempty time-$t$ fibre for
$t\geq1$ has size $2^{\binom{n-1}{3}}$.

For even $n$, $L^2=0$, zero is the unique recurrent state, and every nonempty
one-step fibre has size

$$
2^{\binom n3-\binom{n-2}{2}}
=2^{n-2}\,2^{\binom{n-1}{3}}.                             \tag{6}
$$

The factorization in (6) has a reconstruction meaning.  For an image $y$,
the solutions of $W^{\mathsf T}b=y$ inside $Z$ form a coset of the bicycle
space: there is one boundary graph for odd $n$ and $2^{n-2}$ for even $n$.
Each boundary graph has $2^{\binom{n-1}{3}}$ hypergraph lifts through $W$.

The full fibre and depth formulas are stated and proved in
`PROOF_PACKAGE.md`.

## Remarks and Interpretation

- The Johnson graph is a useful literal identification, but the boundary
  graph is the sufficient statistic that explains both directions of the
  theorem.
- The parity bifurcation is a bicycle-space phenomenon: $K_n$ is pedestrian
  for odd $n$ and has an $(n-2)$-dimensional even-cut space for even $n$.
- The even one-step fibre is not one undifferentiated kernel count; it splits
  canonically into boundary ambiguity and fillings of a fixed boundary.

## Boundaries and Non-Claims

- At $n=1,2$ the triple carrier is trivial.  At $n=3$ the update is the
  identity.  The first nontrivial odd projection is $n=5$, and the first
  square-zero depth-two graph is $n=4$.
- Computation through $n=6$ is falsification evidence, not the proof of
  equations (1)--(6).
- Peeters (2002) directly states the relevant binary minimal polynomials and
  ranks of $A(J(n,3))+I$; no novelty is claimed for the temporal or rank core.
- The package does not claim new Johnson spectra, inclusion-matrix ranks,
  simplicial homology, bicycle spaces, or generic linear-map fibre facts.

## Open Risks

The derivation has no identified mathematical gap.  The decisive risk is
owner and portfolio compression: after Peeters and the concurrent
odd-degree Seidel-switch incidence--Gram candidate are subtracted, the
remaining boundary-lift refinement is too small for a separate paper.
