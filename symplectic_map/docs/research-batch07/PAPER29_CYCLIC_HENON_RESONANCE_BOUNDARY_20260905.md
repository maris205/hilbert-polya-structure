# Resonant critical boundary for a fixed trace-coordinate selection

Date: 2026-09-05. Author-side mathematical supplement, not an independent
review, candidate PASS, project, or publication claim.

The reference normalization is [the main author proof, V2](PAPER29_CYCLIC_HENON_JET_PROOF_V2_20260905.md),
SHA-256 `f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0`.
V1 and V2 are not modified by this supplement. The only new file owned by
this task is the present document.

## Claim and scope

Fix $k\ge6$ with $6\mid k$. Relabel the phases of the main proof by
$j\in\mathbb Z/k\mathbb Z$, represented by $0,\ldots,k-1$, and put
$$
H_c(x,y)=(x^2+c-y,x),\qquad
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},
\qquad c_j=\epsilon^{-2}(u_j-1).
\tag{B1}
$$
This is only an index relabeling, not a change in factor order. For each
$i$, select the length-$k$ sign word $\sigma^{(i)}$ whose only minus sign
is in phase $i$. These are the $k$ selected macro-fixed-point branches:
every macro period in this document is exactly one.

Let $\rho_i$ be the return trace of that fixed point and define
$$
K_{ij}(\epsilon,u)=\frac1{\rho_i}\frac{\partial\rho_i}{\partial u_j},
\tag{B2}
$$
with $\epsilon$ held fixed. The derivative is still in $u$ when the
evaluation point is subsequently restricted to $u=\epsilon v$.

For $v\in\mathbb C^k$, define the two Fourier coefficients
$$
\widehat v_+=\frac1k\sum_{j=0}^{k-1}v_j e^{-2\pi i j/3},\qquad
\widehat v_-=\frac1k\sum_{j=0}^{k-1}v_j e^{2\pi i j/3}.
\tag{B3}
$$
There is no complex conjugation condition on these two coordinates.

**Theorem.** The following statements hold for every such $k$.

1. For every bounded $v$-polydisc, after choosing a sufficiently small
   $\epsilon$-disc, the function
   $$
   D_k(\epsilon,v)
   =\epsilon^{-(k+1)}\det K(\epsilon,\epsilon v),\qquad\epsilon\ne0,
   \tag{B4}
   $$
   extends jointly holomorphically across $\epsilon=0$, and
   $$
   \boxed{D_k(0,v)
   =-\frac{3k^3}{32}
     \left(1-4\widehat v_+\widehat v_-\right).}
   \tag{B5}
   $$
   The convergence to (B5) is $O(|\epsilon|)$ uniformly on smaller
   compact $v$-sets.
2. The leading zero set is the smooth complex cylinder
   $$
   \mathcal C_k=\{v:\widehat v_+\widehat v_-=1/4\}.
   \tag{B6}
   $$
   Near every point of $\{0\}\times\mathcal C_k$, the equation
   $D_k(\epsilon,v)=0$ is a smooth holomorphic hypersurface. In Fourier
   coordinates, it can be solved locally as
   $$
   \widehat v_+=\frac1{4\widehat v_-}+O(\epsilon).
   \tag{B7}
   $$
   This is a local assertion near each point of the cylinder, not a
   uniform assertion at unbounded $v$.
3. On the concrete line
   $$
   v_j=t\cos(2\pi j/3),
   \tag{B8}
   $$
   there are holomorphic functions
   $$
   t_\pm(\epsilon)=\pm1+O(\epsilon)
   \tag{B9}
   $$
   such that the selected trace Jacobian vanishes at
   $u_j=\epsilon t_\pm(\epsilon)\cos(2\pi j/3)$ for every sufficiently
   small nonzero $\epsilon$. At these points its rank is exactly $k-1$.
   The selected fixed points themselves remain distinct and simple,
   and all their traces remain nonzero.
4. Consequently, no fixed $\epsilon$-independent neighborhood of $u=0$
   can make this same selected tuple have a nonvanishing trace Jacobian
   for every sufficiently small nonzero $\epsilon$. In particular it
   cannot support a positive bound $|\det K|\ge c|\epsilon|^{k+1}$
   throughout such a neighborhood.

**Proof status: PROVABLE AS STATED on the author side.** Independent
review remains separate. This theorem does not exclude choosing other
cycles at the degenerate parameters, does not classify the critical
locus of all trace selections, and does not concern arbitrary macro
periods. Its object is the one fixed selection in (B2).

## Assumptions, strategy, and dependency map

Work over $\mathbb C$, in the small-parameter domain in which
$s_j(u)=\sqrt{1-u_j}$ is the branch near $1$. The main proof supplies
uniform orbit and Riccati contractions on a parent $u$-polydisc. Only
the $k$ particular macro-fixed words above are required here; no
exhaustion of all periodic branches is used.

The proof chain is:

1. Retain the second-order orbit and Riccati terms in the actual trace
   differential, including coefficient derivatives.
2. Remove the common zeroth-order row by an exact holomorphic column
   change $Q(u)$, rather than discarding that row at $u\ne0$.
3. Compute the two resonant Fourier projections of the first jet's
   coefficient variation at $u=\epsilon v$.
4. Include the constant and nonresonant directions in a block matrix
   and its Schur complement; their elimination does not change the
   limiting two-dimensional block.
5. Compute its determinant and use the holomorphic implicit function
   theorem at its simple transverse zeros.

## 1. Analytic spectral input and the selected-row jets

The scaled coordinates of a selected fixed point satisfy
$$
z_j^2-s_j^2=\epsilon(z_{j-1}+z_{j+1}).
\tag{B10}
$$
Inverse-square-root contraction on the fixed sign discs gives a
holomorphic branch near $\alpha_j=\sigma_j s_j$. In the sup norm its
Lipschitz constant is $O(|\epsilon|)$. The cyclic Riccati equation is
$$
w_j=2z_j-\frac{\epsilon^2}{w_{j-1}}.
\tag{B11}
$$
It is a second contraction near $2\alpha_j$, with denominators bounded
away from zero and Lipschitz constant $O(|\epsilon|^2)$. On a smaller
parent polydisc both solutions and their coefficient derivatives are
holomorphic and bounded. These facts justify Taylor remainders in the
coefficient $C^1$ norm by Cauchy's formula.

The exact return eigenvalues are $\lambda$ and $\lambda^{-1}$, where
$$
\lambda=\epsilon^{-k}\prod_jw_j,\qquad
\rho=\lambda+\lambda^{-1}.
$$
For sufficiently small nonzero $\epsilon$, $|\lambda|>2^k$ and
$|\lambda^{-1}|<2^{-k}$. Thus the fixed points are simple and their
traces do not vanish. Their sign words are different, so equality of
two phase-space points would force equality of the entire subsequent
phase sequences and hence of the words. They are therefore distinct.

The identity
$$
d_u\log\rho
=\frac{1-\theta}{1+\theta}\sum_jd_u\log w_j,
\qquad
\theta=\epsilon^{2k}\left(\prod_jw_j\right)^{-2},
\tag{B12}
$$
also proves that the normalized differential extends holomorphically
to $\epsilon=0$. Here $d\log$ means division of the differential by
the nonzero function. Since $k\ge6$, the stable-eigenvalue correction
in (B12) is $O_{C^1}(\epsilon^{12})$ and cannot alter the second jet.

For completeness, expansion of (B10) gives
$$
z_j=\alpha_j+\epsilon t_j+\epsilon^2r_j+O_{C^1}(\epsilon^3),
\quad
t_j=\frac{\alpha_{j-1}+\alpha_{j+1}}{2\alpha_j},
\quad
r_j=\frac{t_{j-1}+t_{j+1}-t_j^2}{2\alpha_j}.
$$
Substitution into (B11) shows that, modulo constants with zero
$u$-differential, the second scalar coefficient is
$$
\mathcal L_{2,\sigma}
=\frac14\sum_j\left[
\frac{\alpha_{j-2}}{\alpha_j^2\alpha_{j-1}}
+\frac{\alpha_{j+2}}{\alpha_j^2\alpha_{j+1}}
+\frac1{\alpha_j\alpha_{j+1}}
-\frac{(\alpha_{j-1}+\alpha_{j+1})^2}{\alpha_j^4}
\right].
\tag{B13}
$$
The coefficient of the adjacent-sign term in (B13) includes the
Riccati correction. It would be different if (B11) were omitted.

Put
$$
L_0=\sum_j\log(2s_j),\qquad
g_0=d_uL_0,
\qquad
h_i=\frac{s_i}{2}(s_{i-1}^{-2}+s_{i+1}^{-2}),
$$
and let $G(u)$ be the matrix whose $i$th row is $d_uh_i$. Since the
$i$th selected word has phase means $\mathbf1-2e_i$, its full row
expansion is
$$
K(\epsilon,u)
=\mathbf1g_0(u)
 +\epsilon(J-2I)G(u)
 +\epsilon^2T(u)+O(\epsilon^3),
\qquad J=\mathbf1\mathbf1^T,
\tag{B14}
$$
where $T(u)$ has rows $d_u\mathcal L_{2,\sigma^{(i)}}$. The remainder
is holomorphic and bounded after division by $\epsilon^3$ on smaller
parent polydiscs.

Let $S$ denote a cyclic shift and set
$$
C=\frac12(S+S^{-1}-I),\qquad
B=-\frac32I+\frac54(S+S^{-1})-(S^2+S^{-2}).
\tag{B15}
$$
Then
$$
g_0(0)=-\frac12\mathbf1^T,\qquad
G(0)=C,\qquad T(0)=-\frac14J+B.
\tag{B16}
$$
Here is a direct check of the last identity for every $6\mid k$.
Writing (B13) by adjacent and distance-two correlations gives the
functions $C_{\rm tot},E_j,D_j$ of the main proof. Their gradients at
zero, with $e_j^T$ now a coordinate row, are
$$
dC_{\rm tot}=-\tfrac12\mathbf1^T,\quad
dD_j=\tfrac14e_{j-1}^T-e_j^T+\tfrac14e_{j+1}^T,
$$
$$
dE_j=\tfrac14e_{j-1}^T+\tfrac18e_j^T
      +\tfrac18e_{j+1}^T+\tfrac14e_{j+2}^T.
$$
For the all-plus word these sum to $-\frac14\mathbf1^T$.
A single minus sign at $i$ changes the scalar second coefficient by
$-2(E_{i-1}+E_i+D_{i-1}+D_{i+1})$. Its gradient is
$$
-\tfrac32e_i^T+\tfrac54(e_{i-1}^T+e_{i+1}^T)
 -(e_{i-2}^T+e_{i+2}^T),
$$
which is exactly the $i$th row of $B$. All of these indices are valid
for every $k\ge6$; no six-dimensional computation is being substituted
for the general identity.

## 2. Exact removal of the constant direction

Use unitary Fourier columns
$$
q_\nu(j)=k^{-1/2}e^{2\pi i\nu j/k},\qquad
q_0=\mathbf1/\sqrt k.
$$
Order the Fourier matrix $P$ with the constant column first, then the
$k-3$ nonconstant nonresonant columns, and the two resonant columns
$q_+=q_{k/6}$ and $q_-=q_{5k/6}$ last. Let $\Pi_R$ be the Fourier
projection onto $R=\operatorname{span}\{q_+,q_-\}$.

The entries of $g_0(u)$ are $-1/[2(1-u_j)]$. Since
$g_0(0)q_0=-\sqrt k/2\ne0$, define for $\nu\ne0$
$$
\widetilde q_\nu(u)
=q_\nu-q_0\frac{g_0(u)q_\nu}{g_0(u)q_0}.
\tag{B17}
$$
Let $Q(u)$ have these columns and the unchanged first column $q_0$.
Then
$$
g_0(u)\widetilde q_\nu(u)=0,\qquad
\det Q(u)=\det P.
\tag{B18}
$$
Both $Q$ and its inverse are holomorphic and bounded on a small parent
polydisc. These are column subtractions, not a restriction of the
coefficient parameter space.

Substitute $u=\epsilon v$. For a resonant column $q\in R$, put
$$
r_q(v)=\frac{v^Tq}{\sqrt k}.
$$
The transpose here is bilinear, without conjugating $v$. Taylor
expansion of (B17) gives
$$
\widetilde q(\epsilon v)
=q-\epsilon r_q(v)q_0+O(\epsilon^2).
\tag{B19}
$$
Since $Cq=0$, (B14), (B18), and (B19) imply the full column limit
$$
\lim_{\epsilon\to0}\epsilon^{-2}
K(\epsilon,\epsilon v)\widetilde q(\epsilon v)
=T(0)q+(J-2I)G'(0)[v]q
 -r_q(v)(J-2I)Cq_0.
\tag{B20}
$$
In particular the last, constant-direction correction is present.
It has zero $R$-projection because $Cq_0=q_0/2$ and
$(J-2I)q_0=(k-2)q_0$. Consequently the effective resonant block is
$$
R(v)=\frac34I_R-2\Pi_R G'(0)[v]\big|_R.
\tag{B21}
$$
This conclusion does not omit the moving common row $g_0(u)$: that
row was removed exactly in (B18), and its induced first-order column
change was retained in (B20).

## 3. General Fourier computation of the two-mode block

Expansion of the explicit function $h_i$ gives
$$
h_i=1+\tfrac12(u_{i-1}+u_{i+1}-u_i)
 +\tfrac12(u_{i-1}^2+u_{i+1}^2)
 -\tfrac14u_i(u_{i-1}+u_{i+1})
 -\tfrac18u_i^2+O(\|u\|^3).
\tag{B22}
$$
It follows, for any $w\in R$, using $w_{i-1}+w_{i+1}=w_i$, that
$$
(G'(0)[v]w)_i
=v_{i-1}w_{i-1}+v_{i+1}w_{i+1}
 -\tfrac14(v_{i-1}+v_{i+1})w_i
 -\tfrac12v_iw_i.
\tag{B23}
$$
Take $w_i=e^{i\theta i}$ with $\theta=\pm\pi/3$, and first take a
single Fourier mode $v_i=e^{i\phi i}$. The coefficient of their product
in $-2G'(0)[v]w$ is
$$
-4\cos(\theta+\phi)+\cos\phi+1.
\tag{B24}
$$
To remain in $R$, an input $\theta=\pi/3$ requires either $\phi=0$
or $\phi=-2\pi/3$ modulo $2\pi$. At $\phi=0$, (B24) is zero; at
$\phi=-2\pi/3$, it is $-3/2$. The input $\theta=-\pi/3$ requires
$\phi=0$ or $\phi=2\pi/3$, and the two coefficients are again zero
and $-3/2$. All other Fourier modes project outside $R$.

By linearity in $v$, in the ordered basis $(q_+,q_-)$ this proves
$$
\boxed{R(v)=
\begin{pmatrix}
3/4&-(3/2)\widehat v_+\\
-(3/2)\widehat v_-&3/4
\end{pmatrix}.}
\tag{B25}
$$
The calculation applies to every $6\mid k$: the frequencies
$\pm\pi/3$ and $\pm2\pi/3$ are allowed Fourier frequencies for each
such $k$, and the frequency selection in (B24) uses no other condition
on its size.

On the line (B8), $\widehat v_+=\widehat v_-=t/2$. Hence (B25) becomes
$\frac34\left(\begin{smallmatrix}1&-t\\-t&1\end{smallmatrix}\right)$.
In the real cosine/sine basis of $R$ it is
$$
\boxed{\operatorname{diag}\bigl(\tfrac34(1-t),\tfrac34(1+t)\bigr).}
\tag{B26}
$$
There is a useful further check on the constant-direction issue on
this line. The vector $u$ is three-periodic in its phase index, so
$g_0(u)$ is three-periodic, whereas $q_\pm(j+3)=-q_\pm(j)$.
Thus $g_0(u)q_\pm=0$ exactly along (B8), and the two columns in (B17)
are actually unchanged there. This observation alone does not justify
ignoring the other modes; that elimination is supplied next.

## 4. Holomorphic rescaling, Schur complement, and prefactor

Let
$$
\Delta_\epsilon
=\operatorname{diag}
\left(1,\underbrace{\epsilon,\ldots,\epsilon}_{k-3},
\epsilon^2,\epsilon^2\right)
$$
in the chosen Fourier column order. Define for $\epsilon\ne0$
$$
\mathcal A(\epsilon,v)
=P^{-1}K(\epsilon,\epsilon v)Q(\epsilon v)
 \Delta_\epsilon^{-1}.
\tag{B27}
$$
This matrix extends jointly holomorphically to $\epsilon=0$ on every
bounded $v$-domain after shrinking the $\epsilon$-disc. To verify the
divisions, the zeroth-order term in every nonconstant column vanishes
exactly by (B18). Each nonresonant nonconstant column is consequently
divisible by $\epsilon$. In a resonant column, the first-order
coefficient vanishes at $u=0$ because $Cq_\pm=0$. Its composition with
$u=\epsilon v$ supplies the second factor of $\epsilon$; (B19)--(B20)
give its holomorphic limiting value. The second-order term already
has that factor, and the $O(\epsilon^3)$ remainder remains holomorphic
and bounded after division. This also proves locally uniform
$O(\epsilon)$ convergence of (B27).

Denote the complement of $R$ in this ordered Fourier basis by $U$.
For a nonresonant nonconstant mode $\nu$, set
$$\ell_\nu=1-2\cos(2\pi\nu/k).$$
The constant column limit is $-k/2$ in its own Fourier direction.
Each nonresonant column limit is $\ell_\nu$ in its own direction:
the $u=\epsilon v$ dependence is of higher order in such a column,
and its zeroth-order common row has already been removed. Therefore
$$
\mathcal A(0,v)=
\begin{pmatrix}
D_U&Z(v)\\
0&R(v)
\end{pmatrix},\qquad
D_U=\operatorname{diag}(-k/2,(\ell_\nu)_{\nu\in U\setminus\{0\}}).
\tag{B28}
$$
The off-diagonal block $Z(v)$ is not asserted to vanish. For example,
on (B8), (B23) sends a resonant input partly into the nonresonant
$\pi$ mode. The projected $-2G'(0)[v]q_\pm$ has a contribution
$9tq_{k/2}/4$. This is one of the terms retained in $Z(v)$.

To make elimination explicit, on a compact $v$-set the $UU$ block of
$\mathcal A(\epsilon,v)$ is invertible for small $\epsilon$, with a
bounded inverse. Its Schur complement is
$$
\mathcal A_{RR}
-\mathcal A_{RU}\mathcal A_{UU}^{-1}\mathcal A_{UR}
=R(v)+O(\epsilon).
\tag{B29}
$$
Indeed, the $RU$ block is $O(\epsilon)$ by (B28), whereas the $UR$
block and the inverse $UU$ block remain bounded. Thus neither the
constant direction nor the other nonresonant modes introduce an
additional limiting term into (B25). This argument remains valid at
$\det R(v)=0$; it only inverts $D_U$, never the resonant block.

The determinant factors in (B27) satisfy $\det Q=\det P$ and
$\det\Delta_\epsilon=\epsilon^{k+1}$. Hence
$$\det\mathcal A(\epsilon,v)=D_k(\epsilon,v).\tag{B30}$$
This proves the joint holomorphic extension asserted in the theorem.

For the numerical prefactor, the identity
$$
\prod_{\nu=0}^{k-1}\left(x-2\cos(2\pi\nu/k)\right)
=2\bigl(T_k(x/2)-1\bigr)
$$
has a double root at $x=1$. Its quadratic coefficient there is
$-k^2/3$, because $T_k'(1/2)=0$ and
$T_k''(1/2)=-4k^2/3$. Removing the two zero factors and then the
constant-mode factor $1-2=-1$ gives
$$
\prod_{\substack{1\le\nu<k\\\nu\ne k/6,\,5k/6}}\ell_\nu
=k^2/3.
$$
Consequently
$$
\det D_U=-\frac{k}{2}\frac{k^2}{3}=-\frac{k^3}{6},
\qquad
\det R(v)=\frac9{16}(1-4\widehat v_+\widehat v_-).
$$
Taking the determinant of (B28) proves exactly (B5), including its
sign and prefactor. No $k=6$ numerical or symbolic check is required
for this general calculation.

## 5. Actual degeneracy hypersurfaces and the two explicit curves

The two Fourier coordinates in (B3), together with the remaining
Fourier coordinates $\zeta$, form an invertible complex-linear
coordinate system on $\mathbb C^k$. At a point of $\mathcal C_k$,
both $\widehat v_+$ and $\widehat v_-$ are nonzero. Formula (B5) gives
$$
\left.\frac{\partial D_k}{\partial\widehat v_+}\right|_{\epsilon=0}
=\frac{3k^3}{8}\widehat v_-\ne0.
\tag{B31}
$$
The holomorphic implicit function theorem therefore solves the actual
equation $D_k=0$ locally for $\widehat v_+$ as a holomorphic function
of $(\epsilon,\widehat v_-,\zeta)$. At $\epsilon=0$ that function is
$1/(4\widehat v_-)$, which proves (B7). The nonzero derivative persists
after restricting to a smaller neighborhood. In particular these
are actual smooth degeneracy hypersurfaces, not only zeros of a
truncated expansion.

For the requested concrete curves, define
$$
d_k(\epsilon,t)=D_k\bigl(\epsilon,(t\cos(2\pi j/3))_j\bigr).
$$
On a $t$-disc containing $1$ and $-1$, this is holomorphic and
$$
d_k(0,t)=-\frac{3k^3}{32}(1-t^2),\qquad
\partial_t d_k(0,\pm1)=\pm\frac{3k^3}{16}\ne0.
$$
Two applications of the implicit function theorem yield (B9).
For $\epsilon\ne0$, (B4) shows that these are zeros of the actual
matrix determinant $\det K$.

At either curve, $\partial_t d_k$ remains nonzero. Thus
$\partial_t\det K=\epsilon^{k+1}\partial_t d_k\ne0$ for small nonzero
$\epsilon$. If $K$ had rank at most $k-2$, every cofactor would be
zero and every first derivative of its determinant would vanish.
That contradiction proves rank exactly $k-1$. The simplicity and
disjointness of the underlying fixed points follow from the parent
orbit construction in Section 1, since $u=O(\epsilon)$ stays within
its domain. This rank loss concerns the coefficient-to-trace map,
not an eigenvalue one in the phase-space return map.

The coefficients and the selected sign branches are real under complex
conjugation. Uniqueness in the implicit function theorem consequently
also gives real $t_\pm(\epsilon)$ for sufficiently small real
$\epsilon$. This observation is not needed for the complex theorem,
but confirms that its two displayed curves are not merely an artifact
of allowing nonreal coefficient perturbations.

## 6. Exact consequence and non-consequences

Since $t_\pm$ remain bounded, for every $\eta>0$ the points
$$
u_j(\epsilon)=\epsilon t_\pm(\epsilon)\cos(2\pi j/3)
$$
lie in $\|u\|_\infty<\eta$ for all sufficiently small nonzero
$\epsilon$. At those points the selected determinant is zero.
This proves the impossibility statement for any fixed neighborhood
of $u=0$ and this fixed tuple.

The small wedge $u=\epsilon v$, $\|v\|<\eta_k$ in the main theorem
does not conflict with this result. For example, the leading zeros
on (B8) occur at $|t|=1$, not at $t=0$; choosing a sufficiently small
bounded $v$-neighborhood preserves the main theorem's determinant gap.
No maximality or optimal anisotropic shape of that wedge is claimed.

All derivatives here are in $u$. If they are changed to $v$ at fixed
$\epsilon$, then $K_v=\epsilon K_u$ and the determinant normalization
in (B4) becomes $\epsilon^{2k+1}$. For original coefficient derivatives,
$K_c=\epsilon^2K_u$. These invertible changes for $\epsilon\ne0$ do
not change the actual zero set, but do change its displayed vanishing
order at $\epsilon=0$.

This supplement does **not** assert any of the following:

- failure of every possible selection of cycles at these parameters;
- a global spectral relation or an exact gauge in the factor family;
- classification of the entire critical scheme of the selected trace
  map, or of all marked trace maps;
- a degeneracy result for arbitrary prescribed macro periods;
- a dynamical bifurcation of the selected hyperbolic fixed points;
- novelty, independent review acceptance, long-paper value, or PASS.

The proof is analytic and symbolic for every integer $6\mid k$.
A preliminary read-only $k=6$ CAS check was useful for detecting sign
errors, but it is not a premise or certificate for any universal
statement above. Only this supplementary author file was created.
