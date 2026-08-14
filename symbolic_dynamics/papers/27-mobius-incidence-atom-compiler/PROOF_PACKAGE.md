# Proof Package — Paper27 / SD-C29

## P0. Ambient algebra

For a locally finite poset \(P\), the incidence product is

\[
(f*g)(a,b)=\sum_{a\le c\le b}f(a,c)g(c,b).
\]

On \(P=(\mathbb N_{\ge1},\mid)\), all intervals are finite. Let \(\delta\) be
the identity, \(\zeta(a,b)=\mathbf1_{a\mid b}\), and
\(\mu=\zeta^{-1}\). Let \(\varepsilon_n\) be the diagonal coordinate
idempotent.

## P1. Covers are source atoms

**Claim.**

\[
\operatorname{At}(P)=\{n>1:(1,n)=\varnothing\}=\mathbb P.
\]

**Proof.** If \(n\) is composite, \(n=ab\) with \(1<a<n\), so \(a\) lies in
\((1,n)\). Conversely, any strict divisor \(1<a<n\) gives a nontrivial
factorization \(n=a(n/a)\), so \(n\) is composite. The convolution expression
\(((\zeta-\delta)*(\zeta-\delta))(1,n)\) counts strict intermediate divisors
and vanishes exactly on covers. No prime table is used.

## P2. Kernel formula

Define \(q_n=\zeta*\varepsilon_n*\mu\). Then

\[
q_n(a,b)=\mathbf1_{a\mid n\mid b}\mu_{\rm arith}(b/n).
\]

Only the intermediate coordinate \(n\) survives the two convolutions:

\[
(\zeta*\varepsilon_n*\mu)(a,b)
=\zeta(a,n)\mu(n,b).
\]

For the divisibility poset \(\mu(n,b)=\mu_{\rm arith}(b/n)\).

## P3. Complete primitive-idempotent system

For all \(m,n\),

\[
q_nq_m
=\zeta\varepsilon_n\mu\zeta\varepsilon_m\mu
=\delta_{nm}q_n.
\]

At a finite cutoff,

\[
\sum_n q_n=\zeta\left(\sum_n \varepsilon_n\right)\mu=\delta.
\]

On the countable algebra this sum is intervalwise finite. Conjugation by the
unit \(\zeta\) preserves primitivity of each coordinate idempotent.

## P4. Exact word selector

Set \(A_n=\mathbf1_{\operatorname{At}(P)}(n)q_n\). For a nonempty word
\(w=n_1\cdots n_r\):

- a nonatom letter makes the product zero;
- two different atom letters make it zero by orthogonality;
- a monochromatic atom word gives \(q_p^r=q_p\), of trace one.

Therefore

\[
\operatorname{Tr}(A_{n_1}\cdots A_{n_r})
=\mathbf1_{\{n_1=\cdots=n_r\in\operatorname{At}(P)\}}.
\]

The expression is cyclically invariant. A source letter \(p^r\) is nonatom
and dies; a temporal repetition \(p,p,\ldots,p\) survives with marker
\(u^{r\ell(p)}\).

## P5. Finite radical-conjugacy theorem

Let \(J_N\) be the zero-diagonal radical of \(I(P_N)\). Suppose
\(\{e_x\}\) and \(\{f_x\}\) are complete orthogonal primitive families with
\(f_x\equiv e_x\pmod{J_N}\). Put

\[
v=\sum_x f_xe_x.
\]

Then \(v\equiv1\pmod{J_N}\), hence \(v\) is a unit because \(J_N\) is
nilpotent. Orthogonality gives

\[
f_xv=f_xe_x=ve_x,
\]

so \(f_x=ve_xv^{-1}\). For the canonical compiler, \(v=\zeta\) and
\(q_n=\zeta\varepsilon_n\zeta^{-1}\).

Consequently, for any scalars \(b_n\),

\[
\operatorname{Tr}\left(\sum_n b_nq_n\right)^r=\sum_n b_n^r,
\qquad
\det\left(I-z\sum_n b_nq_n\right)=\prod_n(1-zb_n).
\]

The theorem fixes the semisimple observable, not the adjoint Gram geometry.

## P6. Scalar ablation no-gos

The arithmetic Möbius scalar is not an atom idempotent:
\(\mu(2)=-1\), \(\mu(6)=1\), and \(\mu(4)=0\). The von Mangoldt function
has prime-power support but is an endpoint scalar. The unfiltered \(q_n\)
family contains every composite coordinate. Hence the cover predicate owns
atom selection; Möbius conjugation owns orthogonalization.

## P7. Weighted rank-one theorem

For

\[
H_\eta=\left\{x:\sum_{n\ge1}n^{2\eta}|x_n|^2<\infty\right\},
\qquad \eta>\tfrac12,
\]

the atom action is

\[
q_px=\left(\sum_{k\ge1}\mu(k)x_{pk}\right)(e_1+e_p).
\]

The range vector has norm squared \(1+p^{2\eta}\). The functional has squared
dual norm

\[
p^{-2\eta}C_\eta,\qquad
C_\eta=\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
=\frac{\zeta(2\eta)}{\zeta(4\eta)}.
\]

Thus

\[
\|q_p\|_1=\sqrt{(1+p^{-2\eta})C_\eta}\le\sqrt{2C_\eta}.
\]

The functional evaluates to one on \(e_1+e_p\), proving idempotence and trace
one. For distinct atoms its evaluation on \(e_1+e_q\) is zero, proving
\(q_pq_q=0\).

## P8. Bounded global similarity

Under the unitary reweighting \(X_n=n^\eta x_n\),

\[
(Z_\eta X)_a=\sum_{k\ge1}k^{-\eta}X_{ak},\qquad
(M_\eta X)_a=\sum_{k\ge1}\mu(k)k^{-\eta}X_{ak}.
\]

Every downsampling \(X\mapsto(X_{ak})_a\) has norm at most one. For
\(\eta>1\), the two operator series converge absolutely and

\[
\|Z_\eta\|\le\zeta(\eta),\qquad
\|M_\eta\|\le\frac{\zeta(\eta)}{\zeta(2\eta)}.
\]

Finite-support inversion extends by continuity, giving
\(Z_\eta M_\eta=M_\eta Z_\eta=I\) and
\(q_p=Z_\eta\varepsilon_pM_\eta\). No global bounded similarity is claimed
for \(1/2<\eta\le1\).

## P9. Holomorphic trace-class transfer

If

\[
\sum_p|u|^{\ell(p)}p^{-\operatorname{Re}s}<\infty,
\]

the uniform trace-norm bound proves locally uniform trace-norm convergence of

\[
T_\eta(s,u)=\sum_p u^{\ell(p)}p^{-s}q_p.
\]

Pair annihilation gives

\[
T_\eta(s,u)^r=\sum_p u^{r\ell(p)}p^{-rs}q_p,
\qquad
\operatorname{Tr}T_\eta(s,u)^r=\sum_p u^{r\ell(p)}p^{-rs}.
\]

The trace-log identity near \(z=0\), followed by entire continuation in \(z\),
gives

\[
\det(I-zT_\eta(s,u))
=\prod_p(1-zu^{\ell(p)}p^{-s}).
\]

For \(\rho=|u|>0\), gamma length gives
\(\rho^{\ell(n)}\asymp_\rho n^{2\log_2\rho}\), so the exact half-plane is
\(\operatorname{Re}s>1+2\log_2\rho\).

## P10. Sharp \(u=1\) barrier

Every \(e_1+e_p\) is an eigenvector of \(T_\eta(s,1)\) with eigenvalue
\(p^{-s}\). Eigenvalues of a trace-class operator are absolutely summable.
Since \(\sum_p p^{-\sigma}\) diverges for \(\sigma\le1\), this realization is
not trace class there. This is an operator obstruction, not a statement about
scalar meromorphic continuation.

## P11. Honest graded holomorphic coupling

Let \(U_{p,0}\) and \(U_{p,1}\) be the inherited zero- and one-form pullbacks
with a common trace-norm bound and local identity

\[
\operatorname{Tr}U_{w,0}-\operatorname{Tr}U_{w,1}=1.
\]

Both

\[
\mathcal T_k(s,u)=\sum_p u^{\ell(p)}p^{-s}q_p\otimes U_{p,k}
\]

are trace class on the common absolute domain. Mixed source words vanish
before the holomorphic trace, while the local de Rham difference equals one.
Hence

\[
\operatorname{Tr}\mathcal T_0^r-\operatorname{Tr}\mathcal T_1^r
=\sum_p u^{r\ell(p)}p^{-rs}
\]

and

\[
\frac{\det(I-z\mathcal T_0)}{\det(I-z\mathcal T_1)}
=\prod_p(1-zu^{\ell(p)}p^{-s}).
\]

This is a graded relative ratio of two honest determinants.

## P12. Final logical implication

P1–P4 prove A1 analytically from the source. P7–P11 prove A2 on a precise
domain. P5 and P8 show that ordinary cyclic observables collapse to atom
coordinates. P10 blocks same-object trace-class continuation at \(u=1\).
There is no spectral law. Therefore A3 and A4 fail and Route A is rejected.
