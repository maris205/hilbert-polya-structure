# PC-H: a short reduction to the C404 mechanism

This is a bounded collision certificate for the frozen PC-H candidate, not
an admitted paper or a modification of any sealed predecessor. It explains
why noncommuting coefficients do not by themselves provide a new count law.
The underlying degree, complete-intersection and analytic mechanisms remain
owned by [C404](../../continuation_c404_c408_round2/henon_resonance/PROOF_PACKAGE.md).

Let $K=\overline{\mathbb F}_q$, $q$ odd, $a,c\in K^\times$, and set

\[
H(x,y)=(y,y^q+cy^2-ax),\quad
\Phi(x,y)=(x^q,y^q),\quad S=H^{-1}\Phi.
\]

The following argument includes the frozen $a,c\in\mathbb F_{q^2}^\times$
family; the larger coefficient field is mentioned to expose the collision,
not to substitute a broader paper contract.

## Correct clock and operators

Let $\sigma$ raise polynomial coefficients to the $q$-th power while
fixing the variables. Put $T=H^*\sigma$ and $U(P)=P^q$ on $K[x,y]$.
These are additive ring endomorphisms, linear over $\mathbb F_p$, and
both send a constant $b$ to $b^q$. Absolute Frobenius commutes with
every ring endomorphism in characteristic $p$, so $TU=UT$. They need
not be $K$-linear. In particular $\delta=T-U$ is additive and kills
constants, but it is not asserted to be a derivation or ring endomorphism.

The coordinate polynomials $T^n(x),T^n(y)$ are those of

\[
G_n=\sigma^{n-1}(H)\circ\cdots\circ\sigma(H)\circ H.
\]

Indeed $T^n=H^*(\sigma H)^*\cdots(\sigma^{n-1}H)^*\sigma^n$, and
the final $\sigma^n$ fixes $x,y$. Since
$\Phi H^{-1}=(\sigma H)^{-1}\Phi$, the actual native map satisfies

\[
S^n=G_n^{-1}\Phi^n,
\qquad
\operatorname{Fix}(S^n)=\{T^n(x)-U^n(x)=T^n(y)-U^n(y)=0\}.
\]

This uses the twisted product $G_n$, not the generally invalid $H^n$.
For example $G_2=(\sigma H)\circ H$. All $G_n$ are polynomial
automorphisms with nonzero Jacobian determinant.

## The inherited leading-degree cancellation

If $P=b y^D+P_0$, $\deg P_0<D$, and $p\nmid D$, the unique leading
term of $\delta(P)$ is

\[
b^q\overline D c\,y^{q(D-1)+2}.
\]

To see the only relevant change from C404, the leading part is now

\[
b^q\big((y^q+cy^2-ax)^D-y^{qD}\big),
\]

so its first binomial term is nonzero; all later terms and the $P_0$
contribution have strictly smaller degree. This is precisely C404's degree
comparison with a Frobenius on the coefficient. In particular

\[
\delta^j(y)=B_j y^{D_j}+\text{lower-degree terms},\quad
D_j=\frac{q^j+q-2}{q-1},\quad
B_1=c,\quad B_{j+1}=2cB_j^q\ne0.
\]

Write $n=ws$, $w=p^{v_p(n)}$, $p\nmid s$. In the commuting
$\mathbb F_p$-linear operator algebra,

\[
T^w-U^w=\delta^w,\qquad
T^n-U^n=\sum_{i=0}^{s-1}T^{wi}U^{w(s-1-i)}\delta^w.
\]

In the second expression acting on $y$, every summand has the same top
degree $q^{n-w}D_w$ and the same top coefficient $B_w^{q^{n-w}}$:
both $T$ and $U$ raise coefficients to the $q$-th power, and the
top $y^q$ term of $T(y)$ is monic. Their sum is nonzero because
$p\nmid s$. The first fixed polynomial has unique leading monomial
$-x^{q^n}$, since $\deg T^n(x)=q^{n-1}<q^n$.

Thus the same coprime-leading-monomial calculation as C404 yields length

\[
q^n q^{n-w}D_w
=\frac{q^{2n}+(q-2)q^{2n-w}}{q-1}.
\]

The Jacobian of the fixed equations is $DG_n$, because the derivative
of the positive Frobenius power is zero. It is invertible everywhere;
therefore this finite zero scheme is reduced, so the length equals the
ordinary geometric point count. The new finite diagnostics check these
specific operator and leading-term changes at non-base-field coefficients;
they are not the justification for the all-$n$ deduction above.

## Admission significance

The reduction is short because all substantive degree and cycle-distortion
machinery is inherited. The native count law is exactly C404's $m=2$
formula, now with a correct semilinear formulation for the coefficient
extension. No new zeta-analytic theorem was attempted: substituting an
already-identical sequence would repeat the existing conclusion.

Diagonal conjugacy is not needed to force the collision. For reference,
$D_u(x,y)=(ux,u^q y)$ sends the native map to the same displayed form with
$a'=a u^{1-q^2}$, $c'=c u^{2q-q^2}$; it is not asserted that every pair
descends to the base field by this scaling. The stronger point is that the
count mechanism survives whether or not this particular descent exists.

This should be retained as a transparent scope-extension note and counted
as **zero new independent papers**. It adds no target A2 or spectral bridge.
