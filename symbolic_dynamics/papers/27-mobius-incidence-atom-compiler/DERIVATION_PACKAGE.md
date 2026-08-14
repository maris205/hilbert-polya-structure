# Derivation Package — Paper27 / SD-C29

## D1. From the source relation to atoms

Set \(\bar\zeta=\zeta-\delta\). Then

\[
(\bar\zeta*\bar\zeta)(1,n)
=\sum_{1<c<n}\mathbf1_{c\mid n}.
\]

It is zero precisely when \(n\) covers \(1\). In integer divisibility this is
equivalent to primality, but the formula is poset internal and changes
equivariantly when the source relation changes.

## D2. Compiler multiplication

\[
\begin{aligned}
q_nq_m
&=(\zeta\varepsilon_n\mu)(\zeta\varepsilon_m\mu)\\
&=\zeta\varepsilon_n(\mu\zeta)\varepsilon_m\mu\\
&=\zeta\varepsilon_n\varepsilon_m\mu\\
&=\delta_{nm}q_n.
\end{aligned}
\]

This identity is stronger than cancellation after trace: mixed labels vanish
as operators.

## D3. Word coefficient

For \(w=n_1\cdots n_r\),

\[
A_w
=\prod_{j=1}^r\mathbf1_{\operatorname{At}(P)}(n_j)q_{n_j}
=\mathbf1_{\{n_1=\cdots=n_r=p\in\operatorname{At}(P)\}}q_p.
\]

Therefore \(\operatorname{Tr}A_w\in\{0,1\}\) and the surviving cyclic class is
the atom loop \([p]\), not the composite letter \([p^r]\).

## D4. Finite determinant

With \(Q(b)=\sum_n b_nq_n\), orthogonality gives

\[
Q(b)^r=\sum_n b_n^rq_n.
\]

At a finite cutoff,

\[
\log\det(I-zQ(b))
=-\sum_{r\ge1}\frac{z^r}{r}\sum_n b_n^r
=\sum_n \log(1-zb_n),
\]

so \(\det(I-zQ(b))=\prod_n(1-zb_n)\). The same equality follows immediately
from \(Q(b)=\zeta\operatorname{diag}(b_n)\zeta^{-1}\).

## D5. Rank-one norm

Write \(q_p=|r_p\rangle\langle v_p|\) with

\[
r_p=e_1+e_p,\qquad
\langle v_p,x\rangle=\sum_{k\ge1}\mu(k)x_{pk}.
\]

Then

\[
\|r_p\|_\eta^2=1+p^{2\eta},
\qquad
\|v_p\|_\eta^2
=\sum_{k\ge1}\frac{\mu(k)^2}{(pk)^{2\eta}}
=p^{-2\eta}C_\eta.
\]

Rank one gives

\[
\|q_p\|_1=\|r_p\|_\eta\|v_p\|_\eta
=\sqrt{(1+p^{-2\eta})C_\eta}.
\]

The Euler identity

\[
\sum_{k\ge1}\frac{\mu(k)^2}{k^w}
=\prod_\ell(1+\ell^{-w})
=\frac{\zeta(w)}{\zeta(2w)}
\]

at \(w=2\eta>1\) gives the closed form for \(C_\eta\).

## D6. Global similarity bounds

Under \(U_\eta x=(n^\eta x_n)_n\), define downsampling
\((S_kX)_a=X_{ak}\). Then

\[
U_\eta ZU_\eta^{-1}=\sum_{k\ge1}k^{-\eta}S_k,
\qquad
U_\eta MU_\eta^{-1}=\sum_{k\ge1}\mu(k)k^{-\eta}S_k.
\]

Since \(\|S_k\|\le1\), absolute convergence for \(\eta>1\) gives

\[
\|Z_\eta\|\le\sum_k k^{-\eta}=\zeta(\eta)
\]

and

\[
\|M_\eta\|\le\sum_k|\mu(k)|k^{-\eta}
=\prod_\ell(1+\ell^{-\eta})
=\frac{\zeta(\eta)}{\zeta(2\eta)}.
\]

## D7. Marker threshold

For \(2^j\le n<2^{j+1}\), \(\ell(n)=2j+1\). Hence, for fixed \(\rho>0\),

\[
\rho\,n^{2\log_2\rho}/\rho^2
\le \rho^{\ell(n)}
\le \rho\,n^{2\log_2\rho}\rho^2
\]

after choosing the inequality direction according to \(\rho\); equivalently
\(\rho^{\ell(n)}\asymp_\rho n^{2\log_2\rho}\). Thus

\[
\sum_p \rho^{\ell(p)}p^{-\sigma}
\quad\text{converges iff}\quad
\sigma-2\log_2\rho>1.
\]

At \(\rho=1\), this reduces to \(\sigma>1\).

## D8. Full trace expansion

\[
\begin{aligned}
\log\det(I-zT_\eta)
&=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}T_\eta^r\\
&=-\sum_{r\ge1}\frac{z^r}{r}
  \sum_p u^{r\ell(p)}p^{-rs}\\
&=\sum_p \log(1-zu^{\ell(p)}p^{-s}).
\end{aligned}
\]

Exponentiation gives the atom product. The trace-class theorem justifies
interchanging the locally uniform sums near \(z=0\).

## D9. Local de Rham cancellation

For an affine contraction with derivative \(\vartheta_w\), the zero-form
weighted-composition trace has the factor
\((1-\vartheta_w)^{-1}\), while the one-form trace has
\(\vartheta_w(1-\vartheta_w)^{-1}\). Their difference is

\[
\frac1{1-\vartheta_w}
-\frac{\vartheta_w}{1-\vartheta_w}=1.
\]

Incidence orthogonality first removes mixed source words; de Rham grading then
removes the local stability denominator. The mechanisms are independent.

## D10. Route derivation

\[
\text{source cover}
\Longrightarrow \text{exact atom words}
\Longrightarrow A1\text{ pass},
\]

\[
\text{trace class plus de Rham ratio}
\Longrightarrow A2\text{ analytic determinant},
\]

but

\[
\text{incidence similarity}
\Longrightarrow \text{atom-table determinant},
\qquad
\text{\(u=1\) eigenvalue barrier}
\Longrightarrow A3\text{ fail}.
\]

With no critical-line carrier, A4 fails. The result is therefore a genuine
A1 advance inside an overall rejected route.
