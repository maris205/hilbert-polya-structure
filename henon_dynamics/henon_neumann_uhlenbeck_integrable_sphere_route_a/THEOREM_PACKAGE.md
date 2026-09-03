# Proof Package

## Claim

Let $A=\operatorname{diag}(a_1,a_2,a_3)$ with $a_1<a_2<a_3$. On

$$
T^*S^2=\{(x,p)\in\mathbb R^3\times\mathbb R^3:|x|^2=1,\ x\mathbin{\cdot}p=0\}
$$

consider

$$
H(x,p)=\frac12\bigl(|p|^2+x^TAx\bigr),\qquad
\dot x=p,\qquad
\dot p=-Ax+\alpha x,
\quad \alpha=x^TAx-|p|^2. \tag{N}
$$

Put $L_{ij}=x_ip_j-x_jp_i$ and

$$
F_i=x_i^2+\sum_{j\ne i}\frac{L_{ij}^2}{a_i-a_j}. \tag{U}
$$

Then:

1. Equation (N) defines a complete Hamiltonian flow and preserves both constraints.
2. The three $F_i$ are conserved, satisfy
   $$
   \sum_iF_i=1,\qquad \sum_i a_iF_i=2H,
   $$
   and obey $\{F_i,F_j\}_D=0$ for the Dirac bracket on $T^*S^2$.
3. If $R_\lambda=(\lambda I-A)^{-1}$ and
   $$
   U_\lambda=x^TR_\lambda x,\quad
   V_\lambda=x^TR_\lambda p,\quad
   W_\lambda=1+p^TR_\lambda p,
   $$
   then
   $$
   \mathcal L(\lambda)=
   \begin{pmatrix}V_\lambda&U_\lambda\\-W_\lambda&-V_\lambda\end{pmatrix},
   \quad
   \mathcal M(\lambda)=
   \begin{pmatrix}0&1\\\alpha-\lambda&0\end{pmatrix}
   $$
   satisfy $\dot{\mathcal L}=[\mathcal L,\mathcal M]$, while
   $$
   \det\mathcal L(\lambda)
   =U_\lambda W_\lambda-V_\lambda^2
   =\sum_{i=1}^3\frac{F_i}{\lambda-a_i}. \tag{R}
   $$
4. On every connected regular common fiber of two independent members of $\{H,F_1,F_2,F_3\}$, the Liouville--Arnold theorem gives a two-torus. In its angle coordinates the physical flow is $\theta(t)=\theta(0)+t\omega$. It is periodic exactly when a $T>0$ exists with $T\omega\in2\pi\mathbb Z^2$, equivalently when the two nonzero frequencies have rational ratio.
5. The six axial equilibria $x=\pm e_i,p=0$ are respectively elliptic--elliptic for $i=1$, saddle--center for $i=2$, and saddle--saddle for $i=3$. Each set $x_i=p_i=0$ is an invariant $T^*S^1$ Neumann subsystem. If $a_1=a_2=a\ne b=a_3$, the commuting pair $(J_{12},F_3)$, where $J_{12}=L_{12}$, obeys
   $$
   \{J_{12},F_3\}_D=0,\qquad
   2H=a+J_{12}^2+(b-a)F_3,
   $$
   and is independent on a nonempty open set; the other double-spectrum faces follow by permutation. If all three coefficients coincide, every nonstationary orbit is a great circle. Finally, for every fixed $\hbar>0$,
   $$
   \widehat H=-\frac{\hbar^2}{2}\Delta_{S^2}+\frac12x^TAx,
   \qquad D(\widehat H)=H^2(S^2),
   $$
   is a natural self-adjoint compact-resolvent quantization, without any claim of a closed-form quantum spectrum or target-zero interpretation.

## Status

PROVABLE AS STATED.

## Assumptions

- The main Uhlenbeck and rational Lax formulas use the strict ordering $a_1<a_2<a_3$.
- The quantum boundary fixes a real Planck parameter $\hbar>0$.
- The phase space is the real cotangent bundle with the induced round metric and its canonical symplectic form.
- “Regular fiber” means the differentials of two independent commuting integrals have rank two on that connected common level.
- The repeated-spectrum and isotropic cases are separate boundary systems; singular denominators in (U) are never evaluated there.

## Notation

- $L_{ij}=x_ip_j-x_jp_i$ is the ambient angular momentum component.
- $\{\ ,\ \}_D$ is the constrained Dirac bracket
  $$
  \{x_i,x_j\}_D=0,\quad
  \{x_i,p_j\}_D=\delta_{ij}-x_ix_j,\quad
  \{p_i,p_j\}_D=x_jp_i-x_ip_j.
  $$
- The spectral parameter $\lambda$ lies outside $\{a_1,a_2,a_3\}$.

## Proof Strategy

First prove constraint and energy bounds, then differentiate the angular momenta to obtain the integrals. Package the same identities into a rational $2\times2$ Lax matrix. Establish involution directly from the Dirac bracket, apply Liouville--Arnold only to regular compact fibers, and finish by analyzing the boundary equations before defining the bounded-potential quantum Hamiltonian.

## Dependency Map

1. Completeness depends on constraint preservation, energy conservation, and compactness of a fixed energy shell.
2. Conservation and both linear relations depend on the exact identity for $\dot L_{ij}$.
3. The Lax equation depends on three scalar resolvent differential identities.
4. Liouville tori depend on involution, regularity, compactness, and completeness of the commuting flows on the fiber.
5. Boundary types depend on the tangent linearization and the symmetry of repeated eigenspaces.
6. Natural quantization uses self-adjointness of the round Laplacian plus bounded real-potential perturbation.

## Proof

### Step 1: constraints, Hamiltonian form, and completeness

Along (N),

$$
\frac d{dt}|x|^2=2x\mathbin{\cdot}p,
$$

and, on the constraint surface,

$$
\frac d{dt}(x\mathbin{\cdot}p)
=|p|^2-x^TAx+\alpha=0.
$$

Thus both constraints persist. The constrained Hamilton equations for $H$ under the displayed Dirac bracket are exactly (N). Direct differentiation gives

$$
\dot H=p\mathbin{\cdot}(-Ax+\alpha x)+(Ax)\mathbin{\cdot}p=0.
$$

On $H=E$, $|p|^2=2E-x^TAx$ is bounded because $S^2$ is compact. Hence the trajectory remains in a compact subset of $T^*S^2$. The smooth vector field therefore cannot escape in finite time, proving completeness.

### Step 2: Uhlenbeck conservation and the linear relations

The equation gives

$$
\dot L_{ij}
=x_i\dot p_j-x_j\dot p_i
=(a_i-a_j)x_ix_j. \tag{1}
$$

Consequently,

$$
\dot F_i
=2x_ip_i+2\sum_{j\ne i}L_{ij}x_ix_j
=2x_i\left(p_i+\sum_{j\ne i}L_{ij}x_j\right).
$$

Since

$$
\sum_{j\ne i}L_{ij}x_j
=x_i(x\mathbin{\cdot}p)-p_i|x|^2=-p_i,
$$

each $F_i$ is conserved. Pairing the $(i,j)$ and $(j,i)$ terms immediately cancels the fractional pieces in $\sum_iF_i$, so $\sum_iF_i=|x|^2=1$. The weighted pairing gives

$$
\sum_i a_iF_i=x^TAx+\sum_{i<j}L_{ij}^2.
$$

The Gram identity $\sum_{i<j}L_{ij}^2=|x|^2|p|^2-(x\mathbin{\cdot}p)^2=|p|^2$ proves the second relation.

### Step 3: resolvent generator and Lax equation

The residue of $U_\lambda W_\lambda-V_\lambda^2$ at $\lambda=a_i$ is

$$
x_i^2+\sum_{j\ne i}
\frac{(x_ip_j-x_jp_i)^2}{a_i-a_j}=F_i.
$$

Both sides of (R) vanish at infinity and have the same three simple poles and residues, proving (R). Differentiating the scalar resolvents and using $|x|^2=1$ and $x\mathbin{\cdot}p=0$ gives

$$
\dot U_\lambda=2V_\lambda,
\quad
\dot V_\lambda=W_\lambda+(\alpha-\lambda)U_\lambda,
\quad
\dot W_\lambda=2(\alpha-\lambda)V_\lambda. \tag{2}
$$

Matrix multiplication shows that (2) is exactly $\dot{\mathcal L}=[\mathcal L,\mathcal M]$.

### Step 4: Dirac--Poisson involution

For completeness, differentiate (U):

$$
\partial_{x_k}F_i
=2x_i\delta_{ik}
+2\sum_{j\ne i}\frac{L_{ij}}{a_i-a_j}
\bigl(\delta_{ik}p_j-\delta_{jk}p_i\bigr),
$$

$$
\partial_{p_k}F_i
=2\sum_{j\ne i}\frac{L_{ij}}{a_i-a_j}
\bigl(x_i\delta_{jk}-x_j\delta_{ik}\bigr). \tag{3}
$$

Insert (3) into

$$
\{f,g\}_D
=f_x\mathbin{\cdot}g_p-f_p\mathbin{\cdot}g_x
-(f_x\mathbin{\cdot}x)(x\mathbin{\cdot}g_p)
+(f_p\mathbin{\cdot}x)(x\mathbin{\cdot}g_x)
+(f_p\mathbin{\cdot}p)(g_p\mathbin{\cdot}x)
-(f_p\mathbin{\cdot}x)(g_p\mathbin{\cdot}p). \tag{4}
$$

For $i\ne j$, group terms by the unordered index pairs $\{i,j\}$, $\{i,k\}$, and $\{j,k\}$, where $k$ is the remaining index. The coefficients of $L_{ij}$ cancel because $(a_i-a_j)^{-1}=-(a_j-a_i)^{-1}$; the remaining two groups share the denominator product $(a_i-a_k)(a_j-a_k)$ and have opposite numerators after substituting $L_{ik}x_j-L_{jk}x_i=L_{ij}x_k$. Thus $\{F_i,F_j\}_D=0$. The $i=j$ case follows from antisymmetry. This is a finite algebraic cancellation, with no regularity or sampling assumption.

### Step 5: regular Liouville fibers and exact return

The two linear relations leave two functionally independent commuting integrals on an open dense set; an explicit nonzero wedge witness is obtained at $x=(3/5,4/5,0)$, $p=(0,0,t)$ after choosing $t>0$ away from the single exceptional squared value forced by the three $a_i$. A common regular level is closed inside a compact energy shell, hence compact. Liouville--Arnold therefore makes each connected regular component a two-torus and supplies angles in which $\dot\theta=\omega$.

The state returns after $T>0$ exactly when $T\omega$ belongs to $2\pi\mathbb Z^2$. If both components are nonzero, this is equivalent to $\omega_1/\omega_2\in\mathbb Q$; if one component vanishes, the same lattice condition is the unambiguous formulation. Resonant tori form continuously selected families and are not an isolated primitive-orbit ledger.

### Step 6: complete boundary atlas

At $x=\pm e_i,p=0$, tangent perturbations $q_j$, $j\ne i$, satisfy

$$
\ddot q_j=-(a_j-a_i)q_j. \tag{5}
$$

The strict ordering gives elliptic--elliptic, saddle--center, and saddle--saddle types for $i=1,2,3$, respectively. If $x_i=p_i=0$, both of their time derivatives vanish; the face is therefore an invariant $T^*S^1$ subsystem with potential $\tfrac12(a_j\cos^2\theta+a_k\sin^2\theta)$.

If $a_1=a_2=a\ne b=a_3$, equation (1) gives conservation of
$J_{12}=L_{12}$, the Noether momentum of the $SO(2)$ action. The nonsingular
$F_3$ is invariant under that action, hence $\{J_{12},F_3\}_D=0$. Moreover,

$$
(b-a)F_3=(b-a)x_3^2+L_{31}^2+L_{32}^2,
$$

so the Gram identity gives

$$
2H=a+J_{12}^2+(b-a)F_3. \tag{6}
$$

Independence is not merely asserted generically. At

$$
x=(3/5,0,4/5),\qquad p=(0,t,0),
$$

take the tangent variations

$$
v_1=(( -4/5,0,3/5),(0,0,0)),\qquad
v_2=((0,0,0),(0,1,0)).
$$

Then

$$
\det\begin{pmatrix}
dJ_{12}(v_1)&dJ_{12}(v_2)\\
dF_3(v_1)&dF_3(v_2)
\end{pmatrix}
=-\frac{8\bigl(9(b-a)+25t^2\bigr)}{125(b-a)}.
$$

Choose $t>0$ away from the sole possible exceptional value; the determinant
is nonzero, and rank two persists on a nonempty open set. Thus $J_{12}$ and
$F_3$ replace the separate singular $F_1,F_2$ formulas without evaluating a
zero denominator. The other double-eigenvalue faces follow by permutation. If
$A=aI$, equation (N) becomes $\dot p=-|p|^2x$; $|p|$ is constant, so $p=0$
gives the equilibrium sphere and $p\ne0$ gives a great circle of least period
$2\pi/|p|$.

### Step 7: natural quantization and scope

Fix $\hbar>0$. On the compact boundaryless sphere, $-\Delta_{S^2}$ with domain $H^2(S^2)$ is self-adjoint with compact resolvent. Multiplication by the smooth real function $x^TAx/2$ is bounded and self-adjoint. The bounded-perturbation theorem gives the stated self-adjoint compact-resolvent $\widehat H$ on the same domain. The excluded value $\hbar=0$ would leave a bounded multiplication operator whose self-adjoint realization has domain $L^2(S^2)$, not the displayed $H^2(S^2)$ domain.

This operator and the classical Lax curve carry continuously chosen source parameters. Neither supplies rational-prime labels, logarithmic-prime periods, target Euler factors, a target divisor, or a target-zero operator. Therefore the Route-A tuple is `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, the overall verdict is `ROUTE_A_REJECTED`, and Route B remains false. This proves every part of the claim. $\square$

## Corrections or Missing Assumptions

- No genus-two Abel inversion is claimed. The rational Lax spectral curve is exact, while Liouville--Arnold supplies the complete regular-torus statement without an unproved explicit inversion formula.
- The individual fractions (U) are not evaluated at repeated eigenvalues; Noether momenta own those faces.
- The $H^2(S^2)$ quantum domain is asserted only for the fixed regime $\hbar>0$.

## Open Risks

- Singular Liouville fibers beyond the explicitly listed axial, coordinate, and repeated-spectrum faces are not topologically classified.
- No closed-form spectrum of the anisotropic quantum Hamiltonian is asserted.
