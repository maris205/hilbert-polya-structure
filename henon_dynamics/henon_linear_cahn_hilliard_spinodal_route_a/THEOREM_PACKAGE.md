# Complete theorem package: linear periodic spinodal dynamics

Let \(\mathbb T^d=(\mathbb R/2\pi\mathbb Z)^d\), where \(d\ge1\) is any
finite integer, and let \(H=L^2_0(\mathbb T^d)\). Fix \(\kappa>0\) and
\(\alpha\in\mathbb R\). Put
\[
A=-\kappa\Delta^2-\alpha\Delta,
\qquad D(A)=H^4(\mathbb T^d)\cap H,
\]
and \(r_d(n)=\#\{k\in\mathbb Z^d:|k|^2=n\}\).

## Theorem (all parameters and all represented shells)

1. \(A\) is self-adjoint with compact resolvent, is bounded above, and
   generates a self-adjoint analytic \(C_0\)-semigroup \(S(t)=e^{tA}\).
   For every \(t>0\), \(S(t)\) is trace class.
2. On the Fourier shell \(|k|^2=n>0\),
   \[
   Ae_k=\sigma_ne_k,\qquad \sigma_n=\alpha n-\kappa n^2,
   \]
   with complex multiplicity \(r_d(n)\) (and the same real eigenspace
   dimension after conjugate pairing). On full \(L^2\), the constant mode
   has eigenvalue zero and is the conserved mean.
3. For the chemical potential \(\mu=-\kappa\Delta u-\alpha u\) and
   \[
   \mathcal F(u)=\frac12\int_{\mathbb T^d}
   (\kappa|\nabla u|^2-\alpha|u|^2),
   \]
   every sufficiently regular solution satisfies
   \(u_t=\Delta\mu\) and
   \(\frac d{dt}\mathcal F(u)=-\|\nabla\mu\|_2^2\).
4. The zero solution on \(H\) is exponentially stable iff
   \(\alpha<\kappa\), critical at \(\alpha=\kappa\), and linearly
   spinodally unstable iff \(\alpha>\kappa\). Its unstable Morse index and
   kernel dimension are
   \[
   M=\sum_{\substack{n<\alpha/\kappa\\r_d(n)>0}}r_d(n),\qquad
   K=\sum_{\substack{n=\alpha/\kappa\\r_d(n)>0}}r_d(n).
   \]
   Thus at \(\alpha=\kappa\), \(K=r_d(1)=2d\).
5. The spectral bound is attained. Its fastest shell set is exactly
   \[
   \mathcal N_*=\operatorname*{argmax}_{n\ge1,\ r_d(n)>0}
   (\alpha n-\kappa n^2),
   \]
   with every tie retained. If \(P_n\) is the shell projection and
   \(u_0\ne0\), let \(\lambda_*=\max\{\sigma_n:P_nu_0\ne0\}\). Then
   \[
   e^{-\lambda_*t}S(t)u_0\longrightarrow
   \sum_{\sigma_n=\lambda_*}P_nu_0\quad\text{in }L^2.
   \]
6. Every recurrent state is stationary. In particular, there is no
   nonstationary periodic solution.
7. The singular face \(\kappa=0\) is interpreted with its natural
   generator domain: for \(\alpha\ne0\),
   \(A=-\alpha\Delta\) has domain \(H^2(\mathbb T^d)\cap H\), whereas for
   \(\alpha=0\) the zero generator has domain all of \(H\). If
   \(\alpha<0\) this is the forward heat semigroup; if \(\alpha=0\) it is
   the identity; if \(\alpha>0\), the eigenvalues \(\alpha n\) are
   unbounded above and no bounded \(L^2\) \(C_0\)-semigroup with this
   generator exists.

## Proof

The normalized Fourier functions \(e_k(x)=(2\pi)^{-d/2}e^{ik\cdot x}\)
diagonalize \(A\). Since \(\Delta e_k=-|k|^2e_k\), its eigenvalues are the
displayed \(\sigma_n\). The real polynomial \(-\kappa n^2+\alpha n\) tends
to \(-\infty\), so the diagonal operator is self-adjoint, has compact
resolvent, and is bounded above. The spectral theorem gives a self-adjoint
analytic semigroup. For \(t>0\),
\[
\sum_{k\ne0}e^{t(\alpha|k|^2-\kappa|k|^4)}<\infty,
\]
because the quartic negative term dominates the quadratic one; hence
\(S(t)\) is trace class.

Periodic integration by parts gives
\(\delta\mathcal F/\delta u=-\kappa\Delta u-\alpha u=\mu\), while the PDE
is \(u_t=\Delta\mu\). Therefore
\[
\frac d{dt}\mathcal F(u)=\langle\mu,\Delta\mu\rangle
=-\|\nabla\mu\|_2^2.
\]
The sign factorization
\(\sigma_n=n(\alpha-\kappa n)\) gives the unstable and neutral sets and
their complete lattice multiplicities. Since every positive integer shell
satisfies \(n\ge1\), all rates are negative exactly when
\(\alpha<\kappa\); at equality only \(n=1\) is neutral; above it shell one
is positive.

For completeness, fastest-shell maximization is global and is not inferred
from the finite archive. Completing the square gives
\[
\sigma_n=\frac{\alpha^2}{4\kappa}
-\kappa\left(n-\frac{\alpha}{2\kappa}\right)^2.
\]
If \(\alpha/\kappa\le1\), then for \(n>1\)
\[
\sigma_n-\sigma_1=(n-1)[\alpha-\kappa(n+1)]<0,
\]
so shell one is uniquely fastest. If \(\alpha/\kappa>1\), shell one has
positive rate, whereas every \(n\ge\alpha/\kappa\) has nonpositive rate.
Consequently only represented integers below that explicit finite bound can
maximize. This proves attainment and preserves all equidistant/tied shells.

For any fixed initial datum, the nonempty support has a largest rate because
the rates tend to \(-\infty\). Factoring its exponential from the Fourier
series and using dominated convergence proves the actual-support limit. If
\(S(t_j)u_0\to u_0\) along \(t_j\to\infty\), every Fourier coefficient
obeys \(e^{t_j\sigma_n}\widehat u_0(k)\to\widehat u_0(k)\). A nonzero
coefficient therefore requires \(\sigma_n=0\); the state is stationary.
The periodic statement follows. Finally, on the natural domains stated in
item 7, the \(\kappa=0\) diagonal spectrum gives the stated trichotomy; for
\(\alpha>0\), boundedness at any positive time would contradict
\(\sup_ne^{t\alpha n}=\infty\).

## Evidence and scope boundary

The archive covers dimensions 1–6, 18 parameter cases, 216 shell rows, six
actual-support probes, and three singular-face cases, totaling 1653 audited
leaves. These are regression receipts only. No nonlinear saturation,
coarsening, or pattern-selection theorem follows from this linear result.

The Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` with overall
`ROUTE_A_REJECTED`. Self-adjointness is only a source-side formal hint; no
target zero match or Hilbert--Pólya certification is asserted.
