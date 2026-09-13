# Independent check of the cyclic Hénon resonance boundary

Date: 2026-09-06.

## 1. Input and bounded scope

The actual supplementary input was read completely:

- PAPER29_CYCLIC_HENON_RESONANCE_BOUNDARY_20260905.md;
- 544 lines;
- SHA256 c43b33be00c0051e7f3cdb429221ff36a212b8e19aa6e3acd724a3cd229c2ef9.

This review concerns only the new boundary supplement. The already
checked main theorem, its V2 proof and its earlier independent report
are not reopened. The main V2 dependency is the version with SHA256
f488e8a7cd5a2c71a4975b2f004b21c87d20f4afb29c967318781963fb2955f0.

The supplementary author is not this reviewer. No other independent
reviewer's messages or report are used. Only the present newly assigned
file is written; the supplement and main proof remain unchanged.

## 2. Claim and mathematical status

**Status: PROVABLE AS STATED.**

The full new determinant formula, the local actual degeneracy
hypersurfaces, the two concrete curves, and the fixed-selection
obstruction follow with the stated quantifiers. No additional
hypothesis or restriction of the theorem is needed. No unresolved
mathematical error was found.

This is a correctness decision, not a novelty score, scientific-value
decision, candidate PASS, or long-paper acceptance.

The checked assumptions are:

- $k\ge6$ is fixed and divisible by six.
- Every selected macro period is one.
- The $i$th selected word has its only minus sign in phase $i$.
- The $k$ ordered factor coefficients vary independently.
- Derivatives are in $u$, holding nonzero $\epsilon$ fixed.
- The restriction $u=\epsilon v$ is made after differentiation.
- The analytic construction is used on bounded $v$-sets, with the
  $\epsilon$-radius allowed to depend on such a set.

In particular no assertion for arbitrary macro periods or alternative
cycle selections is being checked or inferred here.

## 3. Notation, inherited input and dependency map

Let
$$
F_{\epsilon,u}=H_{c_{k-1}}\circ\cdots\circ H_{c_0},
\qquad H_c(x,y)=(x^2+c-y,x),
\qquad c_j=\epsilon^{-2}(u_j-1),
$$
and let $\rho_i$ be the return trace of selected fixed point $i$.
Write
$$
K_{ij}=\rho_i^{-1}\partial_{u_j}\rho_i,\qquad
D_k(\epsilon,v)=\epsilon^{-(k+1)}
                    \det K(\epsilon,\epsilon v).
$$

Let $q_\nu(j)=k^{-1/2}e^{2\pi i\nu j/k}$. The resonant subspace
$$
R=\operatorname{span}\{q_+,q_-\},\qquad
q_+=q_{k/6},\quad q_-=q_{5k/6},
$$
uses frequencies $\pm\pi/3$. The perturbation coordinates
$$
\widehat v_\pm=\frac1k\sum_j v_j e^{\mp2\pi i j/3}
$$
instead have frequencies $\pm2\pi/3$. This distinction matters for
the off-diagonal entries below. Over $\mathbb C$, these two
coefficients are independent, not conjugates.
Let $S$ denote cyclic phase shift and $\Pi_R$ the Fourier projection
onto $R$.

The accepted parent construction supplies the actual holomorphic
normalized row expansion
$$
K(\epsilon,u)=\mathbf1g_0(u)
 +\epsilon(J-2I)G(u)+\epsilon^2T(u)+O(\epsilon^3),
\qquad J=\mathbf1\mathbf1^T,
$$
where
$$
g_0(u)_j=-\frac1{2(1-u_j)},\qquad
G(u)_{i,\cdot}=d_uh_i,\qquad
h_i=\frac{\sqrt{1-u_i}}2
\bigl((1-u_{i-1})^{-1}+(1-u_{i+1})^{-1}\bigr).
$$
The factor $J-2I$ is specific to the present all-period-one selection.
At zero,
$$
G(0)=C=\frac12(S+S^{-1}-I),\qquad
T(0)=-\frac14J+B,
$$
$$
B=-\frac32I+\frac54(S+S^{-1})-(S^2+S^{-2}).
$$
The inherited spectral calculation gives $B|_R=3I_R/4$.
The supplement's formulas (B13)--(B16) agree with this input, including
the Riccati contribution; no replacement by an orbit-equation
Jacobian has occurred.

The genuinely new proof chain is:

1. Differentiate the first jet in the coefficient direction $v$.
2. Retain the moving constant-row elimination.
3. Compute the full resonant block, including its dependence on
   the two double-frequency coefficients of $v$.
4. Embed that block in the complete rescaled matrix and check its
   Schur complement even at singular resonant parameters.
5. Apply the holomorphic implicit function theorem to actual zeros.

## 4. Moving constant-row correction

For a nonconstant Fourier column, set
$$
\widetilde q_\nu(u)=q_\nu-
q_0\frac{g_0(u)q_\nu}{g_0(u)q_0}.
$$
The denominator is nonzero near $u=0$, and this is an exact
annihilator of $g_0(u)$. The resulting column matrix $Q(u)$ has the
same determinant as the ordered Fourier matrix $P$, and both
$Q$ and $Q^{-1}$ are locally bounded and holomorphic.

For $q\in R$, expansion at $u=\epsilon v$ gives
$$
\widetilde q(\epsilon v)
=q-\epsilon r_q(v)q_0+O(\epsilon^2),\qquad
r_q(v)=\frac{v^Tq}{\sqrt k}.
$$
Indeed, the numerator of the ratio begins with
$-\epsilon v^Tq/2$, and its denominator begins with $-\sqrt k/2$.
The transpose is bilinear; no conjugate of $v$ is introduced.

Substitution in the actual row expansion yields
$$
\begin{aligned}
\lim_{\epsilon\to0}\epsilon^{-2}
K(\epsilon,\epsilon v)\widetilde q(\epsilon v)
={}&T(0)q+(J-2I)G'(0)[v]q\\
&-r_q(v)(J-2I)Cq_0.
\end{aligned}
$$
The last term is required in the full column. It lies in the
constant direction since $Cq_0=q_0/2$. Only after retaining it
may one project onto $R$, where it vanishes. This verifies the
supplement's handling of the moving common row.

The effective projected block is consequently
$$
R(v)=\frac34I_R-2\Pi_R G'(0)[v]\big|_R.
$$
This formula alone is not yet the full determinant calculation;
the complementary directions are checked in Section 6.

## 5. Independent Hessian and Fourier calculation

Expansion of the explicit scalar $h_i$ gives
$$
\begin{aligned}
h_i={}&1+\frac12(u_{i-1}+u_{i+1}-u_i)
 +\frac12(u_{i-1}^2+u_{i+1}^2)\\
&-\frac14u_i(u_{i-1}+u_{i+1})-\frac18u_i^2+O(\|u\|^3).
\end{aligned}
$$
Before using resonance, its Hessian satisfies
$$
\begin{aligned}
(G'(0)[v]w)_i={}&v_{i-1}w_{i-1}+v_{i+1}w_{i+1}\\
&-\frac14v_i(w_{i-1}+w_{i+1})
-\frac14(v_{i-1}+v_{i+1})w_i-\frac14v_iw_i.
\end{aligned}
$$
For $w\in R$, the relation $w_{i-1}+w_{i+1}=w_i$ reduces this
to (B23). Thus no Hessian term was lost in obtaining that formula.

For input $w_i=e^{i\theta i}$ and perturbation mode
$v_i=e^{i\phi i}$, with $\theta=\pm\pi/3$, the coefficient in
$-2G'(0)[v]w$ is
$$
-4\cos(\theta+\phi)+\cos\phi+1.
$$
Its output has frequency $\theta+\phi$. Projection back to $R$
permits only $\phi=0$ or the frequency that exchanges the two
resonant modes. The constant perturbation gives coefficient zero.
The exchange perturbation gives coefficient $-3/2$.

With the precise Fourier convention in Section 3, this proves
$$
\boxed{
R(v)=
\begin{pmatrix}
3/4&-(3/2)\widehat v_+\\
-(3/2)\widehat v_-&3/4
\end{pmatrix}.
}
$$
There is no missing factor of $k$ from the unitary input columns:
the perturbation Fourier coefficients use the usual $1/k$
normalization, and input and output columns have the same
$k^{-1/2}$ normalization.

The frequency computation is valid for every multiple of six, not
only $k=6$. It also explains why all other Fourier coefficients
of $v$ disappear from the leading determinant, although they may
appear in other blocks of the limiting matrix.

## 6. Full block matrix, Schur coupling and prefactor

Order $P$ with the constant mode first, the $k-3$ nonconstant
nonresonant modes next, and $R$ last. Use analytic column scales
$$
\Delta_\epsilon=\operatorname{diag}
(1,\underbrace{\epsilon,\ldots,\epsilon}_{k-3},
\epsilon^2,\epsilon^2),
$$
not their absolute values, and define
$$
\mathcal A=P^{-1}K(\epsilon,\epsilon v)
Q(\epsilon v)\Delta_\epsilon^{-1}.
$$

Exact elimination of $g_0(u)$ makes every nonconstant column
divisible by $\epsilon$. For a resonant column, its first-order
coefficient vanishes at $u=0$, so composition with $\epsilon v$
provides the second factor. The normalized matrix thus extends
jointly holomorphically through $\epsilon=0$ on every bounded
$v$-domain after choosing an appropriate $\epsilon$-radius.
The cubic row remainder gives locally uniform $O(\epsilon)$
error after the largest column division.

Let $U$ be the complementary Fourier subspace. The constant
column has limit $-k/2$ in its own direction; each other $U$
column has limit
$\ell_\nu=1-2\cos(2\pi\nu/k)$ in its own direction.
In particular their limiting $R$ components vanish, independently
of $v$. Hence the complete limit is
$$
\mathcal A(0,v)=
\begin{pmatrix}
D_U&Z(v)\\0&R(v)
\end{pmatrix},\qquad
D_U=\operatorname{diag}(-k/2,(\ell_\nu)).
$$

The upper-right block must not be silently set to zero. For example,
on $v_j=t\cos(2\pi j/3)$ a resonant input has a contribution
$9tq_{k/2}/4$ in the nonresonant $\pi$ mode, as stated in the
supplement. This is obtained by inserting the frequency
$\phi=\pm2\pi/3$ that sends the input to $\pi$ in the preceding
Fourier coefficient.

On a compact $v$-set, the $UU$ block remains invertible and boundedly
so for small $\epsilon$. Its Schur complement is
$$
\mathcal A_{RR}
-\mathcal A_{RU}\mathcal A_{UU}^{-1}\mathcal A_{UR}
=R(v)+O(\epsilon),
$$
because $\mathcal A_{RU}=O(\epsilon)$, whereas the other factors
are bounded. No inverse of $R(v)$ is taken. This justifies the
calculation also on its zero-determinant set, where an argument
that inverted the resonant block would have failed.

Finally, $\det Q=\det P$ cancels the Fourier phase factor exactly.
Since $\det\Delta_\epsilon=\epsilon^{k+1}$,
$\det\mathcal A=D_k$. The already established nonzero-mode product
$\prod_{\nu\in U\setminus\{0\}}\ell_\nu=k^2/3$ gives
$$
\det D_U=-\frac{k^3}{6},\qquad
\det R(v)=\frac9{16}(1-4\widehat v_+\widehat v_-).
$$
Thus the full, correctly normalized determinant is
$$
\boxed{
D_k(0,v)=-\frac{3k^3}{32}
                  (1-4\widehat v_+\widehat v_-).
}
$$
At $v=0$ this agrees with the accepted main prefactor for $a_i=1$.
The present calculation additionally establishes the entire
bounded-$v$ leading polynomial, not just that consistency check.

## 7. Leading cylinder and actual holomorphic zero sets

The two displayed Fourier coordinates are independent complex-linear
coordinates. Therefore
$$
\mathcal C_k=\{v:\widehat v_+\widehat v_-=1/4\}
$$
is the full leading zero set. Both coordinates are nonzero on it,
and all other Fourier coordinates are free. It is a smooth complex
hypersurface, isomorphic to $\mathbb C^*\times\mathbb C^{k-2}$.

At any finite point of this cylinder,
$$
\partial_{\widehat v_+}D_k(0,v)
=\frac{3k^3}{8}\widehat v_-\ne0.
$$
Joint holomorphy established in Section 6 allows the holomorphic
implicit function theorem to be applied to the actual function
$D_k$, not merely to its leading polynomial. In a neighborhood of
that point the zero set is a smooth hypersurface and has the form
$$
\widehat v_+
=\frac1{4\widehat v_-}+O(\epsilon),
$$
with a holomorphic local error.

The extension and hypersurface here are in $(\epsilon,v)$.
For nonzero $\epsilon$ their points are actual zeros of $\det K$.
No smooth extension in the original $(\epsilon,u)$ coordinates at
the collapsed point $\epsilon=u=0$ is needed or claimed.
Likewise there is no assertion uniform over unbounded parts of
the cylinder or classification of all global critical components.

## 8. Concrete curves, exact rank and real parameters

On $v_j=t\cos(2\pi j/3)$, Fourier orthogonality gives
$\widehat v_+=\widehat v_-=t/2$. Define
$$
d_k(\epsilon,t)=D_k(\epsilon,(t\cos(2\pi j/3))_j).
$$
Then
$$
d_k(0,t)=-\frac{3k^3}{32}(1-t^2).
$$
The two zeros are simple:
$$
\partial_t d_k(0,\pm1)=\pm\frac{3k^3}{16}\ne0.
$$
The implicit function theorem gives two actual holomorphic branches
$t_\pm(\epsilon)=\pm1+O(\epsilon)$.

At their nonzero-$\epsilon$ points,
$$
\partial_t\det K=\epsilon^{k+1}\partial_t d_k\ne0.
$$
If the matrix had rank at most $k-2$, all cofactors would vanish,
so every first derivative of its determinant would vanish. Thus
its rank is exactly $k-1$ along either curve.

The selected fixed points remain distinct and simple, and their
traces remain nonzero, because the vector with entries
$u_j=\epsilon t_\pm(\epsilon)\cos(2\pi j/3)$
lies in the parent orbit domain. The rank loss is in the
coefficient-to-trace differential; it is not an eigenvalue-one
degeneracy of a return map.

For real $\epsilon$, complex conjugation preserves the real
coefficient equations and each selected real sign branch. Uniqueness
of the two implicit-function branches based at real $t=\pm1$
therefore makes $t_\pm(\epsilon)$ real. The supplementary real
observation is justified, although the complex theorem does not
depend on it.

## 9. What the obstruction does and does not prove

The displayed zero points have $u(\epsilon)\to0$. Hence every fixed
open $u$-neighborhood of zero contains such a zero for all
sufficiently small nonzero $\epsilon$. This disproves a common,
$\epsilon$-independent nonvanishing neighborhood for this same
selected tuple. It also disproves a positive determinant lower
bound throughout such a neighborhood.

It does not disprove full rank for another selection of cycles at
those parameters. In particular:

- the supplement fixes the $k$ single-minus macro-fixed words;
- it does not optimize the cycle selection as parameters vary;
- it does not establish failure of every possible trace-coordinate
  system or a universal spectral relation;
- it does not extend the degeneracy assertion to arbitrary periods.

There is no conflict with the main theorem's sufficiently small
wedge $u=\epsilon v$. The concrete leading zeros occur at $t=\pm1$,
outside a sufficiently small neighborhood of $v=0$. The supplement
does not prove a maximal wedge, an optimal anisotropic shape, or
an unavoidable neighborhood restriction for every selection.

The derivative normalization is also correct:
$K_v=\epsilon K_u$ and $K_c=\epsilon^2K_u$ at fixed nonzero
$\epsilon$. These preserve rank and actual zeros, but change the
displayed order of the determinant at $\epsilon=0$.

## 10. Defects, unresolved risks and disposition

No incorrect coefficient, Fourier normalization, omitted Schur term,
invalid implicit-function step, or quantifier failure was found.
No amendment to the supplementary theorem is required.

The genuinely delicate distinctions are already respected in the
input: both constant-row correction and complementary modes are
retained; only the invertible complementary block is eliminated;
actual zeros are obtained from holomorphy, not inferred directly
from a truncated expansion; and the failure statement is confined
to the fixed selected tuple.

Mathematical status of this supplement: **PROVABLE AS STATED**.
No new review of the accepted main theorem is implied by this result.

## 11. Incremental content and natural proof volume

The supplement adds a genuine boundary result to the accepted
existence-and-order theorem. The new information is the complete
two-Fourier-coordinate dependence of the rescaled determinant and
the resulting actual critical set. In particular it turns the
main theorem's deliberately small resonant region into a statement
with a proved obstruction to enlarging that region to a fixed
$u$-neighborhood for the same tuple.

The true additional proof consists of:

1. The Hessian calculation and its two-mode projection.
2. The full block calculation proving that complementary coupling
   does not alter the leading polynomial.
3. The actual degeneracy hypersurface, explicit transverse curves,
   rank statement and correctly limited neighborhood consequence.

The orbit/Riccati construction, parent second-order coefficients,
Fourier product, and general column-rescaling method are inherited
and should not be counted a second time. The analytic implicit
function theorem is a tool, not a separate new method. The real
observation and the two curves are consequences of the same
critical-boundary theorem, not independent paper-sized results.

After integration and removal of repeated parent material, this
supplement naturally contributes approximately 3--5 substantive
English pages, including its theorem and necessary scope discussion.
The source's 544 Markdown lines, 2,553 whitespace-delimited words
including mathematical tokens, and 31 numbered displays are not
a compiled page count.

Relative to the earlier approximate 16--20-page assessment of the
main mathematical package, a deduplicated combined main text around
19--24 substantive pages is now a plausible editorial range.
This is not a commitment to reach 22 pages, a certification of the
22--30-page gate, or evidence of scientific value by itself. The
eventual content and layout must justify any such page count without
repeating the shared analytic setup or expanding corollaries into
nominally separate contributions.

Correctness, novelty, scientific value and candidate acceptance
remain separate decisions. This report assigns only the mathematical
status above.
