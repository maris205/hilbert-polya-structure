# Proof package

## Claim

Let \(C_n=\mathbb Z/n\mathbb Z\).  For \(n\ge3\), let \(Q_n\) stay put with
probability \(1/2\) and move to each neighbour with probability \(1/4\).  For
\(n=2\), the two directed neighbour choices coalesce, so the other vertex has
probability \(1/2\); for \(n=1\), \(Q_1=(1)\).  On
\(\Omega_n=\mathbb Z_2^{C_n}\times C_n\), define one step by independently
rerandomizing the lamp at the current position to a fair bit, applying \(Q_n\),
and independently rerandomizing the lamp at the arrival position.

The uniform law is the unique reversible stationary law.  Under the Walsh
transform in the lamps,
\[
 P_n\cong\bigoplus_{A\subseteq C_n}D_AQ_nD_A,
 \qquad D_A(x,x)=\mathbf1_{\{x\notin A\}}.                 \tag{1}
\]
For \(A=\varnothing\), the eigenvalues are
\[
 c_{n,k}=\frac{1+\cos(2\pi k/n)}2,
 \qquad 0\le k<n.                                        \tag{2}
\]
For \(A\ne\varnothing\), write the nonempty cyclic runs of \(C_n\setminus A\)
as lengths \(\ell\).  The block has \(|A|\) zero eigenvalues and, for every
run, the simple eigenvalues
\[
 p_{\ell,j}=\frac12+\frac12\cos\frac{\pi j}{\ell+1},
 \qquad 1\le j\le\ell.                                  \tag{3}
\]
The associated eigenvectors are Walsh characters times coordinate delta
vectors on deleted sites or discrete sine vectors on a surviving run.  These
vectors form a complete orthogonal eigenbasis.

Equivalently, with \(R_A\) the multiset of positive run lengths,
\[
 \det(zI-P_n)=
 \det(zI-Q_n)\prod_{\varnothing\ne A\subseteq C_n}
 z^{|A|}\prod_{\ell\in R_A}\prod_{j=1}^{\ell}(z-p_{\ell,j}). \tag{4}
\]
For \(n\ge3\), the largest nonconstant eigenvalue, its multiplicity and the
sharp \(L^2\) contraction are
\[
 \lambda_{\mathrm{top}}=\frac{1+\cos(\pi/n)}2,
 \qquad m(\lambda_{\mathrm{top}})=n,
 \qquad \|P_n^tf\|_2\le\lambda_{\mathrm{top}}^t\|f\|_2   \tag{5}
\]
for every mean-zero \(f\), with equality on the slow eigenspace.  Thus
\(\operatorname{gap}(P_n)=(1-\cos(\pi/n))/2\).

## Status

PROVABLE AS STATED.

## Assumptions and notation

- Lamp rerandomizations are independent fair replacements, not deterministic
  toggles.
- Inner products use the uniform probability law on \(\Omega_n\).
- A run is a connected component of the induced subgraph on
  \(C_n\setminus A\); zero-length runs are omitted.
- Formula (2) uses only \(k=0\) when \(n=1\).

## Proof strategy and dependency map

1. A single fair switch becomes a support-deletion projection in each Walsh
   sector.
2. This identifies all blocks and proves self-adjointness.
3. Deleted cycles split into tridiagonal killed paths, diagonalized by sines.
4. Orthogonality and dimension counting give completeness and (4).
5. Monotonicity of the path top eigenvalue identifies the exact slow mode.

## Proof

### 1. Reversibility and uniqueness

Let \(S\) be the Markov operator that replaces the lamp at the present
position by a fair bit.  It is conditional expectation with respect to all
other coordinates and hence is an orthogonal projection in uniform
\(L^2(\Omega_n)\).  The lifted position kernel \(Q_n\) is self-adjoint because
its transition matrix is symmetric.  Therefore \(P_n=SQ_nS\) is
self-adjoint and preserves constants, proving uniform reversibility.

From any state one may follow a positive-probability position path visiting
all vertices, choose prescribed outcomes at the switches, and finish at any
chosen position.  Thus the finite chain is irreducible.  Its stationary law is
therefore unique.  This argument also covers \(n=1,2\) under the frozen
coalescing conventions.

### 2. Walsh reduction

For \(A\subseteq C_n\), put
\(\chi_A(\eta)=(-1)^{\sum_{x\in A}\eta(x)}\).  The functions
\(\chi_A(\eta)g(x)\), as \(A\) varies and \(g\in\mathbb C^{C_n}\), are an
orthogonal decomposition of the full space.  If the current position is
\(x\notin A\), switching does not change \(\chi_A\).  If \(x\in A\), averaging
the new fair lamp gives zero.  Consequently
\[
 S(\chi_Ag)=\chi_A D_Ag.
\]
The position move leaves \(\chi_A\) unchanged, so applying switch, move and
switch yields \(\chi_A D_AQ_nD_Ag\).  This proves (1).

### 3. Every block

For \(A=\varnothing\), \(D_A=I\), and the cyclic Fourier vectors
\(x\mapsto e^{2\pi ikx/n}\) give (2).

Let \(A\ne\varnothing\).  Coordinates in \(A\) are killed on both sides of
\(D_AQ_nD_A\), so their delta vectors give \(|A|\) zero eigenvectors.  For
\(n\ge3\), each surviving run of length \(\ell\) carries the tridiagonal matrix
with diagonal \(1/2\) and adjacent entries \(1/4\).  At run coordinate
\(1\le r\le\ell\), set
\[
 u_j(r)=\sin\frac{\pi jr}{\ell+1},\qquad u_j(0)=u_j(\ell+1)=0.
\]
The sine addition identity gives
\[
 \frac14u_j(r-1)+\frac12u_j(r)+\frac14u_j(r+1)
 =p_{\ell,j}u_j(r).
\]
Discrete sine orthogonality supplies \(\ell\) orthogonal vectors.  Different
runs and different Walsh sectors are orthogonal.  Deleted deltas plus all run
sines contribute \(|A|+\sum_{\ell\in R_A}\ell=n\) vectors in sector \(A\);
hence no eigenvector is missing.  The same calculation for a singleton
survivor proves the \(n=2\) block formula, and \(n=1\) is immediate.  Multiplying
all block factors proves (4).

### 4. Gap, multiplicity and sharp decay

All listed eigenvalues lie in \([0,1]\).  In the empty-support sector, the
largest eigenvalue below one is
\((1+\cos(2\pi/n))/2\).  In a nonempty-support sector, every run has
\(\ell\le n-1\), and its top eigenvalue is
\((1+\cos(\pi/(\ell+1)))/2\), which increases strictly with \(\ell\).
Therefore the global nonconstant maximum is attained exactly when \(A\) is a
singleton and its complement is the unique run of length \(n-1\).  There are
exactly \(n\) such supports and each contributing path eigenvalue is simple.
This proves (5), including the multiplicity.  Spectral expansion of a mean-zero
function gives the inequality, and a \(\lambda_{\mathrm{top}}\)-eigenvector gives
equality.

For \(n=2\), the empty block has spectrum \(\{1,0\}\), each singleton block
contributes \(1/2\) and one zero, and the full-support block is zero; the gap is
\(1/2\).  For \(n=1\), the two-state lamp chain has spectrum \(\{1,0\}\) and
gap one.

## Collision and claim boundary

The closest retained owners are C171 (independent hypercube flipping), C183
(random transpositions), C192 (chamber walks), and C338 (Wilson cycle popping).
None has a moving lamp field or the Walsh-to-vertex-deletion block theorem.
No infinite-group spectral type, percolation transition, arithmetic clock,
target determinant, Euler factor, root number, target zero match, automorphy or
Hilbert--Pólya operator is claimed.

## Open risks

The result depends essentially on fair rerandomization.  Biased replacement or
deterministic toggling changes the Fourier blocks and lies outside this theorem.
