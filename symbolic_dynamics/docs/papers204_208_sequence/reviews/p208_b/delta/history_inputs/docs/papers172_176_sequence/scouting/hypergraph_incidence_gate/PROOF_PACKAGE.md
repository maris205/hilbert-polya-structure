# Proof Package: odd pair-codegree feedback on 3-graphs

## Claim

Let $n\geq 1$.  Over $\mathbb F_2$, let

$$
C_2=\mathbb F_2^{\binom{[n]}3},\qquad
C_1=\mathbb F_2^{\binom{[n]}2},\qquad
C_0=\mathbb F_2^{[n]}.
$$

Let $W:C_2\to C_1$ be the edge--triangle incidence map and let
$D:C_1\to C_0$ be the vertex--edge incidence map.  Define

$$
L=W^{\mathsf T}W:C_2\longrightarrow C_2.
$$

Equivalently, if $x$ is a labelled $3$-uniform hypergraph, then $(Lx)_T$ is
the parity of the three pair-codegrees on the pairs contained in $T$.

The following statements hold.

1. If $A$ is the adjacency matrix of the Johnson graph $J(n,3)$, then
   $L=I+A$ over $\mathbb F_2$.
2. If $n$ is odd, then $L^2=L$ and
   $\operatorname{rank}L=\binom{n-1}{2}$.
3. If $n$ is even, then $L^2=0$ and
   $\operatorname{rank}L=\binom{n-2}{2}$.
4. All cycles, depths, zeta functions, and all-time fibres are the ones
   stated in Steps 8--9 below.
5. Given an image hypergraph $y$, the Eulerian boundary graphs $b$ satisfying
   $W^{\mathsf T}b=y$ form a singleton when $n$ is odd and an affine space of
   size $2^{n-2}$ when $n$ is even.  Each such $b$ has exactly
   $2^{\binom{n-1}{3}}$ hypergraph lifts $x$ with $Wx=b$.

## Status

`PROVABLE AS STATED`.

The mathematical claim survives unchanged.  The ownership/collision gate is
separate and is negative.

## Assumptions

- All vector spaces, matrices, ranks, and orthogonal complements are over
  $\mathbb F_2$.
- Subsets index the standard orthonormal bases of the chain spaces.
- Binomial coefficients $\binom ab$ are zero when $0\leq a<b$.
- The full simplex on $[n]$ supplies every pair and every triple.

## Notation

- $N=\binom n3=\dim C_2$.
- $Z=\ker D$ is the cycle space of $K_n$, identified with its Eulerian
  spanning subgraphs.
- $B=\operatorname{im}D^{\mathsf T}$ is the cut space of $K_n$.
- $\mathcal B=Z\cap B$ is the bicycle space.
- $\epsilon=n\bmod 2\in\mathbb F_2$.
- $r_n=\operatorname{rank}L$ and $h_n=N-r_n=\dim\ker L$.

## Proof Strategy

The proof factors the update through the boundary graph $b=Wx$.  The central
identity is

$$
WW^{\mathsf T}=\epsilon I+D^{\mathsf T}D.                 \tag{1}
$$

Because every boundary graph lies in $Z=\ker D$, equation (1) makes
$WW^{\mathsf T}$ act on boundaries as either the identity or zero.  Rank and
reconstruction are then governed by the kernel of $W^{\mathsf T}$ on $Z$,
which is exactly the bicycle space of $K_n$.

## Dependency Map

1. The literal Johnson identity uses common pairs of two triples.
2. Exactness $\operatorname{im}W=Z$ uses the triangle-fan basis and the rank
   of the incidence matrix of the connected graph $K_n$.
3. Equation (1) uses common triangles of two edges.
4. The square law uses equation (1) restricted to $Z$.
5. The rank uses $\ker(W^{\mathsf T}|_Z)=Z\cap B$.
6. The bicycle dimension uses the binary Laplacian $DD^{\mathsf T}$ of $K_n$.
7. Boundary reconstruction uses the two kernels $\ker W$ and
   $\ker(W^{\mathsf T}|_Z)$.
8. The functional graph and fibres use only the square law and rank-nullity.

## Proof

### Step 1: the literal update is $I+A(J(n,3))$

For triples $S,T$, the $(S,T)$ entry of $W^{\mathsf T}W$ is the parity of the
number of pairs contained in both $S$ and $T$.  When $S=T$, this number is
$3$, hence the diagonal entry is $1$.  When $S\neq T$, the number is $1$
exactly if $|S\cap T|=2$, and is $0$ otherwise.  Adjacency in $J(n,3)$ is
defined by intersection size $2$.  Therefore

$$
L=W^{\mathsf T}W=I+A(J(n,3)).                             \tag{2}
$$

The coordinate formula in the claim follows from the same multiplication:
$Wx$ is the pair-codegree vector and $W^{\mathsf T}$ sums its three entries
on each triple.

### Step 2: triangle boundaries are exactly the Eulerian graphs

Every column of $W$ is a triangle, and the two edges of that triangle
incident with any chosen vertex cancel in characteristic two.  Hence
$DW=0$ and $\operatorname{im}W\subseteq Z$.

Fix vertex $n$.  For every $1\leq i<j<n$, let $z_{ij}$ be the boundary of
triangle $\{i,j,n\}$.  These $\binom{n-1}{2}$ vectors are independent:
among them, the edge $\{i,j\}$ occurs only in $z_{ij}$.  Thus

$$
\operatorname{rank}W\geq\binom{n-1}{2}.                  \tag{3}
$$

The vertex--edge incidence matrix $D$ of the connected graph $K_n$ has rank
$n-1$ over $\mathbb F_2$.  Its rows sum to zero, while deleting any one row
leaves independent rows, as is seen from the columns of a spanning tree.
Consequently

$$
\dim Z=\binom n2-(n-1)=\binom{n-1}{2}.                   \tag{4}
$$

Equations (3)--(4) and $\operatorname{im}W\subseteq Z$ prove

$$
\operatorname{im}W=Z,\qquad
\operatorname{rank}W=\binom{n-1}{2},qquad
\dim\ker W=\binom{n-1}{3}.                              \tag{5}
$$

The last identity follows from rank-nullity and Pascal's identity.

### Step 3: the edge upper-Laplacian identity

Consider $Q=WW^{\mathsf T}$ on $C_1$.  Its diagonal entry at an edge $e$ is
the number $n-2$ of triangles containing $e$, reduced modulo two.  This is
$\epsilon$.  For distinct edges $e,f$, its entry is $1$ if they share a
vertex, because then their union is their unique common triangle, and is $0$
if they are disjoint.

The matrix $D^{\mathsf T}D$ has diagonal entry $2=0$ and off-diagonal entry
$1$ exactly for incident edges.  Entrywise comparison proves equation (1):

$$
WW^{\mathsf T}=\epsilon I+D^{\mathsf T}D.
$$

### Step 4: the square law

For $x\in C_2$, put $b=Wx$.  Step 2 gives $b\in Z$, so $Db=0$.  Equation
(1) therefore gives $WW^{\mathsf T}b=\epsilon b$.  It follows that

$$
L^2x=W^{\mathsf T}WW^{\mathsf T}Wx
     =W^{\mathsf T}(WW^{\mathsf T}b)
     =\epsilon W^{\mathsf T}b
     =\epsilon Lx.                                      \tag{6}
$$

Thus $L^2=L$ for odd $n$ and $L^2=0$ for even $n$.

### Step 5: the kernel on boundary graphs is the bicycle space

By Step 2 and the nondegenerate standard dot product,

$$
\ker W^{\mathsf T}=(\operatorname{im}W)^\perp=Z^\perp.
$$

For a graph, the cycle and cut spaces are orthogonal complements, so
$Z^\perp=B$.  Restricting the preceding equality to $Z$ yields

$$
\ker(W^{\mathsf T}|_Z)=Z\cap B=\mathcal B.               \tag{7}
$$

### Step 6: bicycle dimension for $K_n$

Every cut has the form $D^{\mathsf T}s$ for a vertex vector $s\in C_0$.
The vectors $s$ and $s+\mathbf1$ give the same cut, and these are the only
duplications because $K_n$ is connected.  Such a cut is Eulerian precisely
when

$$
DD^{\mathsf T}s=0.                                       \tag{8}
$$

If $n$ is odd, then $DD^{\mathsf T}=J+I$: its diagonal is $n-1=0$ and its
off-diagonal entries are $1$.  The kernel of $J+I$ is
$\langle\mathbf1\rangle$.  Quotienting by the same one-dimensional kernel
of $D^{\mathsf T}$ gives $\dim\mathcal B=0$.

If $n$ is even, then $DD^{\mathsf T}=J$.  Its kernel is the
$(n-1)$-dimensional even-weight vertex space.  Since $\mathbf1$ has even
weight and is the kernel of $D^{\mathsf T}$, equation (8) gives

$$
\dim\mathcal B=n-2.                                      \tag{9}
$$

### Step 7: rank of $L$

The first map $W:C_2\to Z$ is surjective.  Therefore

$$
\operatorname{rank}L
=\operatorname{rank}(W^{\mathsf T}|_Z)
=\dim Z-\dim\mathcal B.                                  \tag{10}
$$

Using Steps 2 and 6 in (10) gives

$$
r_n=
\begin{cases}
\binom{n-1}{2},&n\text{ odd},\\[2mm]
\binom{n-2}{2},&n\text{ even}.
\end{cases}                                               \tag{11}
$$

This proves the two rank claims.

### Step 8: complete functional graph and all-time fibres

For odd $n$, equation (6) makes $L$ a projection.  Its fixed space is
$\operatorname{im}L$, of dimension $r_n$, and every other state has depth
one.  Each nonempty fibre is a coset of $\ker L$ and has size $2^{h_n}$.
Thus

$$
\begin{aligned}
\#\operatorname{Fix}(L)&=2^{r_n},\\
\#\{x:\operatorname{depth}(x)=1\}&=2^N-2^{r_n},\\
\zeta_L(z)&=(1-z)^{-2^{r_n}}.
\end{aligned}                                             \tag{12}
$$

For a target $y$ and time $t$,

$$
\#(L^t)^{-1}(y)=
\begin{cases}
1,&t=0,\\
2^{h_n},&t\geq1\text{ and }y\in\operatorname{im}L,\\
0,&t\geq1\text{ and }y\notin\operatorname{im}L.
\end{cases}                                               \tag{13}
$$

For even $n$, equation (6) gives
$\operatorname{im}L\subseteq\ker L$ and makes zero the unique recurrent
state.  The exact depth layers are

$$
\begin{aligned}
\#D_0&=1,\\
\#D_1&=2^{h_n}-1,\\
\#D_2&=2^N-2^{h_n},\\
\zeta_L(z)&=(1-z)^{-1}.
\end{aligned}                                             \tag{14}
$$

Every nonzero image state is a depth-one child of zero and has
$2^{h_n}$ depth-two predecessors.  A nonzero kernel state outside the image
has no predecessor.  The all-time fibres are

$$
\#(L^t)^{-1}(y)=
\begin{cases}
1,&t=0,\\
2^{h_n},&t=1\text{ and }y\in\operatorname{im}L,\\
0,&t=1\text{ and }y\notin\operatorname{im}L,\\
2^N,&t\geq2\text{ and }y=0,\\
0,&t\geq2\text{ and }y\neq0.
\end{cases}                                               \tag{15}
$$

Equations (12)--(15) prove the complete functional graph and fibre claims.

### Step 9: boundary-graph reconstruction

Fix $y\in\operatorname{im}L$.  An Eulerian graph $b\in Z$ is compatible
with $y$ precisely when $W^{\mathsf T}b=y$.  Because $y$ is in the image of
$W^{\mathsf T}|_Z$, this solution set is a nonempty affine translate of the
kernel in (7).  Steps 6--7 therefore show that the number of compatible
boundary graphs is

$$
\#\{b\in Z:W^{\mathsf T}b=y\}=
\begin{cases}
1,&n\text{ odd},\\
2^{n-2},&n\text{ even}.
\end{cases}                                               \tag{16}
$$

For each compatible $b\in Z=\operatorname{im}W$, its hypergraph lifts form
one affine coset of $\ker W$.  Equation (5) gives

$$
\#\{x\in C_2:Wx=b\}=2^{\binom{n-1}{3}}.                  \tag{17}
$$

Multiplying (16) and (17) recovers the one-step fibre sizes.  In particular,
for odd $n$ each boundary class contains exactly one fixed canonical lift
$W^{\mathsf T}b$; for even $n$ an image state has $2^{n-2}$ possible
Eulerian boundary graphs, each supporting the same number of hypergraphs.
This proves the reconstruction claim.  $\square$

## Corrections or Missing Assumptions

None.  The sharp-height wording needs the following small-carrier convention:
the odd map has positive height only for $n\geq5$, while $n=1,3$ have only
fixed states; the even map has sharp height two for $n\geq4$, while the
triple carrier is trivial at $n=2$.

## Open Risks

- There is no mathematical gap observed in the claim.
- Peeters (2002) directly owns the minimal-polynomial parity split and both
  binary rank formulas after identifying $L=I+A(J(n,3))$.
- Boundary reconstruction is an elementary cycle/cut/bicycle-space
  refinement.  Its correctness does not overcome the external owner or the
  internal incidence--Gram collision recorded in the hostile gate.
