# Proof package: beta-two Dyson--Ornstein--Uhlenbeck diffusion

## Claim

For every integer $N\geq 1$, Hermitian Ornstein--Uhlenbeck diffusion in the
trace-metric normalization induces on the ordered eigenvalues a conservative,
noncolliding diffusion. Its transition kernel is the energy-shifted Doob
$h$-transform of the Karlin--McGregor determinant for $N$ independent scalar
Ornstein--Uhlenbeck particles. Its reversible law is the ordered GUE density,
and its complete $L^2$ spectrum is indexed by partitions with at most $N$
parts. The sharp generator gap is $1/2$.

## Status

`PROVABLE AS STATED`

The normalization is part of the statement. Changing either the matrix
Brownian covariance or the confining drift changes the Coulomb coefficient,
Gaussian variance, time scale, and gap.

## Assumptions

- $N$ is a fixed positive integer.
- $\mathrm{Herm}_N$ has real inner product
  $\langle A,B\rangle=\operatorname{Tr}(AB)$.
- $\mathcal B_t$ is standard Brownian motion for this Euclidean metric.
- The matrix process solves
  $$
  dH_t=d\mathcal B_t-\frac12H_t\,dt. \tag{1}
  $$
- The initial matrix has simple spectrum. Its eigenvalues are labeled in the
  open chamber
  $$
  W_N=\{x\in\mathbb R^N:x_1<\cdots<x_N\}. \tag{2}
  $$
- $\operatorname{He}_m$ denotes the monic probabilists' Hermite polynomial.

## Notation

Set
$$
h(x)=\Delta(x)=\prod_{1\leq i<j\leq N}(x_j-x_i),
\qquad d=\deg h=\frac{N(N-1)}2. \tag{3}
$$
Thus $h>0$ on $W_N$. The independent scalar Ornstein--Uhlenbeck generator is
$$
\mathcal L_0=\frac12\sum_{i=1}^N(\partial_i^2-x_i\partial_i). \tag{4}
$$
For $t>0$, put $r=e^{-t/2}$ and $\sigma_t^2=1-r^2=1-e^{-t}$.

## Proof strategy and dependency map

1. The trace metric fixes every entry covariance. Second-order Hermitian
   perturbation theory then gives the ordered eigenvalue SDE up to collision.
2. Alternation proves $\Delta h=0$, while homogeneity proves
   $\mathcal L_0h=-dh/2$.
3. The reflection principle gives the killed determinant kernel. Andréief's
   identity and the leading terms of Gaussian moments prove its exact
   $h$-mass, hence conservativity of the Doob transform.
4. The transformed generator equals the eigenvalue generator. Conservativity
   of the minimal chamber diffusion excludes a finite collision time.
5. Scalar Hermite eigenfunctions are wedged into Slater determinants.
   Dividing by $h$ gives symmetric polynomial eigenfunctions. Exterior-power
   completeness proves that no $L^2$ spectrum is missing.
6. Partition enumeration gives multiplicities, the heat trace, and the sharp
   gap. Conjugation by the equilibrium square root gives the source-local
   free-fermion oscillator interpretation.

## Theorem 1: matrix radial SDE

Let $x_1(t)<\cdots<x_N(t)$ be the ordered eigenvalues of (1). Then, for
independent standard real Brownian motions $B_1,\ldots,B_N$,
$$
dx_i=dB_i+\sum_{j\ne i}\frac{dt}{x_i-x_j}-\frac{x_i}{2}\,dt,
\qquad 1\leq i\leq N. \tag{5}
$$
Equivalently, its generator on $C_c^2(W_N)$ is
$$
\mathcal L=\frac12\sum_i\partial_i^2+
\sum_i\left(\sum_{j\ne i}\frac1{x_i-x_j}-\frac{x_i}{2}\right)\partial_i.
\tag{6}
$$

### Proof

Step 1. Choose the trace-orthonormal basis
$$
E_{ii},\quad \frac{E_{ij}+E_{ji}}{\sqrt2},\quad
\frac{\mathrm i(E_{ij}-E_{ji})}{\sqrt2}\qquad(i<j). \tag{7}
$$
The Brownian coefficient of every basis vector has quadratic variation $dt$.
Consequently, in any instantaneous eigenbasis $u_1,\ldots,u_N$,
$$
d\langle u_i,\mathcal B u_i\rangle\,
d\langle u_j,\mathcal B u_j\rangle=\delta_{ij}\,dt,
\qquad
\mathbb E|\langle u_j,d\mathcal B u_i\rangle|^2=dt\quad(i\ne j). \tag{8}
$$

Step 2. For a simple Hermitian eigenvalue, second-order perturbation gives
$$
d x_i=\langle u_i,dH\,u_i\rangle+
\sum_{j\ne i}\frac{|\langle u_j,d\mathcal B\,u_i\rangle|^2}{x_i-x_j}.
\tag{9}
$$
The martingale terms in (8) are independent standard real Brownian motions.
The finite-variation part of $-Hdt/2$ is $-x_i dt/2$, and the second relation
in (8) supplies exactly one copy of $(x_i-x_j)^{-1}dt$. This proves (5) up
to the first collision. The construction below proves that the collision
time is infinite and therefore closes the derivation globally. $\square$

## Theorem 2: killed kernel, Doob transform, and no collision

The scalar kernel for $dY=dB-Ydt/2$ is
$$
p_t(a,b)=\frac1{\sqrt{2\pi(1-r^2)}}
\exp\left[-\frac{(b-ra)^2}{2(1-r^2)}\right]. \tag{10}
$$
The transition density in $W_N$ for $N$ independent copies killed at the
first collision is
$$
q_t(x,y)=\det[p_t(x_i,y_j)]_{i,j=1}^N. \tag{11}
$$
Moreover,
$$
\int_{W_N}q_t(x,y)h(y)\,dy=r^d h(x). \tag{12}
$$
Hence
$$
k_t(x,y)=r^{-d}\frac{h(y)}{h(x)}q_t(x,y)
=e^{dt/2}\frac{h(y)}{h(x)}q_t(x,y) \tag{13}
$$
is a conservative Markov density. Its continuous diffusion started at any
$x\in W_N$ never reaches $\partial W_N$, and its generator is (6).

### Proof

Step 1: the Vandermonde eigenfunction. The Laplacian is invariant under
coordinate permutations, so $\Delta h$ is alternating. Every alternating
polynomial is divisible by $h$, but $\deg(\Delta h)=d-2<d$. Therefore
$\Delta h=0$. Euler's identity for the homogeneous polynomial $h$ gives
$x\cdot\nabla h=dh$. Substitution in (4) yields
$$
\mathcal L_0h=-\frac d2h. \tag{14}
$$

Step 2: absorption. The scalar Ornstein--Uhlenbeck law is invariant under
permuting coordinates, and each wall $x_i=x_j$ is a reflection hyperplane.
Pairing a path with the path reflected after its first wall hit cancels all
wall-hitting contributions. The surviving signed permutation sum is exactly
the determinant (11). This is the continuous Karlin--McGregor reflection
formula.

Step 3: exact $h$-mass. Both $q_t(x,\cdot)$ and $h$ are alternating, so their
product is symmetric. Thus the left side of (12) is $1/N!$ times its integral
over $\mathbb R^N$. Write $h(y)=\det[y_j^{i-1}]$. Andréief's identity gives
$$
\int_{\mathbb R^N}q_t(x,y)h(y)\,dy
=N!\det\left[\int_{\mathbb R}p_t(x_i,y)y^{j-1}\,dy\right]_{i,j=1}^N.
\tag{15}
$$
The $(j-1)$st moment of $N(rx_i,1-r^2)$ is a polynomial in $x_i$ of degree
$j-1$ with leading coefficient $r^{j-1}$. Lower-degree column operations
remove all remaining terms, leaving $r^{0+1+\cdots+(N-1)}h(x)=r^dh(x)$.
Equations (15) and the chamber factor $1/N!$ prove (12).

Step 4: transformed generator. For smooth compactly supported $f$,
$$
h^{-1}\mathcal L_0(hf)+\frac d2f
=\mathcal L_0f+\nabla\log h\cdot\nabla f. \tag{16}
$$
Since
$$
\partial_i\log h=\sum_{j\ne i}\frac1{x_i-x_j}, \tag{17}
$$
(16) is (6). Equation (12) says $\int k_t(x,y)dy=1$, so the minimal
$h$-transformed chamber diffusion has infinite lifetime. A boundary hit by a
continuous path would be its killing time; therefore its probability before
any fixed $t$ is zero. A countable union over integer $t$ proves no collision
for all finite times. Local pathwise uniqueness away from the walls, together
with the standard electrostatic-repulsion theorem, identifies this process
with the unique global strong solution of (5). $\square$

## Theorem 3: reversible GUE law

The probability measure
$$
\pi_N(dx)=Z_N^{-1}e^{-|x|^2/2}h(x)^2\,1_{W_N}(x)\,dx,
\qquad
Z_N=(2\pi)^{N/2}\prod_{j=0}^{N-1}j!, \tag{18}
$$
is reversible for $k_t$ and is the ordered eigenvalue law of the invariant
matrix Gaussian density proportional to $e^{-\operatorname{Tr}H^2/2}$.

### Proof

Step 1. The drift in (6) is one half the logarithmic gradient of the density
in (18):
$$
\frac12\partial_i\log(e^{-|x|^2/2}h^2)
=-\frac{x_i}{2}+\sum_{j\ne i}\frac1{x_i-x_j}. \tag{19}
$$
Thus $\mathcal L=(2\pi_N)^{-1}\nabla\cdot(\pi_N\nabla)$ in density notation,
which gives formal symmetry. It also follows directly from scalar detailed
balance in (10), the determinant (11), and the two $h$ factors in (13).

Step 2. To normalize, use $h=\det[\operatorname{He}_{i-1}(x_j)]$ and
Andréief's identity. Scalar Hermite orthogonality gives
$$
\int_{\mathbb R^N}e^{-|x|^2/2}h(x)^2\,dx
=N!(2\pi)^{N/2}\prod_{j=0}^{N-1}j!. \tag{20}
$$
The integrand is symmetric, so the chamber integral is $1/N!$ of (20),
which is $Z_N$. The Weyl integration Jacobian is $h^2$; applying it to the
invariant matrix Gaussian proves the last assertion. $\square$

## Theorem 4: complete partition spectrum

Let $\kappa=(\kappa_1\geq\cdots\geq\kappa_N\geq0)$ be a partition, and set
$$
m_i=\kappa_{N+1-i}+i-1,\qquad 1\leq i\leq N. \tag{21}
$$
Then $0\leq m_1<\cdots<m_N$ and
$\sum_i m_i=d+|\kappa|$. Define
$$
D_m(x)=\det[\operatorname{He}_{m_i}(x_j)]_{i,j=1}^N,
\qquad
\Phi_\kappa(x)=\frac{D_m(x)}{h(x)}. \tag{22}
$$
The quotient $\Phi_\kappa$ is a symmetric polynomial and
$$
\mathcal L\Phi_\kappa=-\frac{|\kappa|}{2}\Phi_\kappa. \tag{23}
$$
The family $\{\Phi_\kappa\}$ is a complete orthogonal basis of
$L^2(W_N,\pi_N)$. Its exact squared norm is
$$
\|\Phi_\kappa\|_{L^2(\pi_N)}^2
=\frac{\prod_{i=1}^N m_i!}{\prod_{j=0}^{N-1}j!}. \tag{24}
$$
Consequently, the eigenvalue $-k/2$ has multiplicity
$p_N(k)$, the number of partitions of $k$ with at most $N$ parts.

### Proof

Step 1. Strict increase in (21) follows from
$$
m_{i+1}-m_i=1+\kappa_{N-i}-\kappa_{N+1-i}\geq1. \tag{25}
$$
$D_m$ is alternating, hence divisible by the minimal-degree alternating
polynomial $h$. The quotient is symmetric and has degree
$\sum_i m_i-d=|\kappa|$.

Step 2. The scalar Hermite equation is
$$
\frac12(\operatorname{He}_n''-x\operatorname{He}_n')
=-\frac n2\operatorname{He}_n. \tag{26}
$$
Expanding the determinant into tensor products and applying $\mathcal L_0$
to each coordinate gives
$$
\mathcal L_0D_m=-\frac12\left(\sum_i m_i\right)D_m. \tag{27}
$$
Apply the conjugacy (16) to $D_m=h\Phi_\kappa$ and use
$\sum_i m_i=d+|\kappa|$. This proves (23).

Step 3. Scalar Hermite polynomials form a complete orthogonal Gaussian
$L^2(\mathbb R)$ basis. Their antisymmetrized tensor products $D_m$, with
strictly increasing $m$, therefore form a complete basis of the
antisymmetric sector of Gaussian $L^2(\mathbb R^N)$. Multiplication by $h$
and antisymmetric extension from $W_N$ identify that sector, up to a fixed
normalizing constant, with $L^2(W_N,\pi_N)$. Division by $h$ therefore sends
the complete Slater basis to the complete family in (22); no extra spectrum
remains.

Step 4. Andréief and scalar Hermite orthogonality give
$$
\int_{\mathbb R^N}D_mD_n e^{-|x|^2/2}\,dx
=\delta_{mn}N!(2\pi)^{N/2}\prod_i m_i!. \tag{28}
$$
Divide by $N!$ for the chamber and by $Z_N$ from (18). The result is (24).
Finally, (21) is a bijection between strict Slater labels above the filled
ground state $(0,1,\ldots,N-1)$ and partitions of arbitrary size with at most
$N$ parts. This proves the multiplicity statement. $\square$

## Corollary 5: sharp gap, heat trace, and source determinant

For mean-zero $f\in L^2(\pi_N)$,
$$
\|P_tf\|_2\leq e^{-t/2}\|f\|_2. \tag{29}
$$
Equivalently,
$$
\operatorname{Var}_{\pi_N}(f)
\leq2\langle f,-\mathcal Lf\rangle_{\pi_N}
=\int_{W_N}|\nabla f|^2\,d\pi_N. \tag{30}
$$
The constant is sharp because $x_1+\cdots+x_N$ has eigenvalue $-1/2$.
For $t>0$, $P_t$ is trace class and
$$
\operatorname{Tr}P_t
=\sum_\kappa e^{-t|\kappa|/2}
=\prod_{j=1}^N(1-e^{-jt/2})^{-1}. \tag{31}
$$
Its source-local Fredholm determinant is
$$
\det(I-zP_t)=\prod_{k=0}^{\infty}
(1-ze^{-kt/2})^{p_N(k)}. \tag{32}
$$

### Proof

The complete spectrum in Theorem 4 has a simple zero level and first positive
decay exponent $1/2$, proving (29)--(30) and sharpness. The generating
function for partitions with at most $N$ parts is the finite Euler product in
(31). It is finite for every $t>0$, so $P_t$ is trace class. The standard
trace-class eigenvalue product gives (32). $\square$

## Corollary 6: source-local oscillator conjugacy

Let
$$
\psi_0(x)=e^{-|x|^2/4}h(x). \tag{33}
$$
Multiplication by the normalized $\psi_0$ sends $L^2(W_N,\pi_N)$ to the
antisymmetric Dirichlet sector of Lebesgue $L^2(W_N)$ and gives
$$
-\psi_0\mathcal L\psi_0^{-1}
=-\frac12\Delta+\frac{|x|^2}{8}-\frac N4-\frac d2. \tag{34}
$$
The inverse-square Calogero term cancels at $\beta=2$. Equation (34) is a
free-fermion harmonic-oscillator representation of this source diffusion.
It supports only the strict `A4_FORMAL_HINT` label: it is not a
Hilbert--Pólya operator and is not tied to any target zero set.

### Proof

Since $\mathcal L=\frac12\Delta+\nabla\log\psi_0\cdot\nabla$,
direct differentiation gives
$$
-\psi_0\mathcal L\psi_0^{-1}
=-\frac12\Delta+\frac12\frac{\Delta\psi_0}{\psi_0}. \tag{35}
$$
Use $\Delta h=0$ and $x\cdot\nabla h=dh$ to compute
$$
\frac{\Delta\psi_0}{\psi_0}
=\frac{|x|^2}{4}-\frac N2-d. \tag{36}
$$
Substitution proves (34). $\square$

## Boundary and degenerate cases

- $N=1$: $h=1$, $d=0$, and all statements reduce to scalar
  Ornstein--Uhlenbeck theory with gap $1/2$.
- $t=0$: (13) is understood as the weak identity-kernel limit. Density
  formulas are asserted for $t>0$.
- Initial collision: the theorem assumes $x\in W_N$. No entrance law from a
  multiple eigenvalue is claimed.
- Infinite $N$: every theorem is for fixed finite $N$. No large-$N$ limit is
  asserted.

## Corrections or missing assumptions

None. The ordered chamber, trace metric, unit Brownian variance, and drift
$-H/2$ are frozen explicitly.

## Open risks

None within the stated finite-$N$ theorem. The Route-A arithmetic gate fails
independently of the exact solvability proved here.
