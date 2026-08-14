# Derivation package — Paper 28 / SD-C30

## 1. Similarity reduction

The source compiler gives \(q_n=ZE_nM\), \(M=Z^{-1}\). Thus

\[
T_s=\sum_{p\in A}p^{-s}ZE_pM
=Z\left(\sum_{p\in A}p^{-s}E_p\right)M
=ZD_s^AM.
\]

Both implications

\[
D_s^A\in\mathcal S_q\Longrightarrow T_s\in\mathcal S_q,
\qquad
T_s\in\mathcal S_q\Longrightarrow D_s^A\in\mathcal S_q
\]

follow from multiplication by \(Z,M\). Hence the oblique basis changes
norm constants but not Schatten membership.

The singular values of \(D_s^A\) are \(p^{-\sigma}\), where
\(\sigma=\Re s\). Therefore

\[
\|D_s^A\|_q^q=\sum_{p\in A}p^{-q\sigma}.
\]

For primes this is finite exactly when \(q\sigma>1\).

## 2. Reflected common strip

The top-right block requires \(q\sigma>1\). The bottom-left block has
coefficients \(p^{-(1-s)}\) and requires

\[
q(1-\sigma)>1.
\]

Combining:

\[
\frac1q<\sigma<1-\frac1q.
\]

The interval width is \(1-2/q\); it is positive iff \(q>2\). Thus
\(\det_2\) cannot reach the critical line, while \(\det_3\) can.

### Marker ownership

The threshold above is for \(u=1\). For
\[
T_s(u)=\sum_pu^{\ell(p)}p^{-s}q_p
\]
the diagonal Schatten sum becomes
\[
\sum_p|u|^{q\ell(p)}p^{-q\sigma}.
\]
This is a different summability problem when \(|u|<1\). In every
\(r\)-th power or word ledger the marker is
\(u^{r\ell(p)}\); replacing it by \(u^{\ell(p)}\) would violate marker
ownership and change the object.

## 3. Why the reflection is holomorphic

The ordinary adjoint \(T_s^*\) is anti-holomorphic in \(s\). The
source-real reflection

\[
X^\sharp=JX^*J
\]

is complex-linear. Thus \(s\mapsto T_{1-s}^\sharp\) is holomorphic.
On \(s=1/2+it\),

\[
p^{-(1-s)}=p^{-\overline s},
\]

so the reflected block becomes the true adjoint. This is the precise
division of labor: holomorphy off the line and self-adjointness on it.

## 4. Rank-one Gram contraction

With

\[
q_n(a,b)=\mathbf1_{a\mid n}\,
\mu(b/n)\mathbf1_{n\mid b},
\]

write \(q_n=u_nv_n^{\mathsf T}\). For \(W_\eta=\operatorname{diag}
(n^{2\eta})\),

\[
q_q^\sharp=W_\eta^{-1}v_qu_q^{\mathsf T}W_\eta.
\]

Consequently

\[
\operatorname{Tr}(q_pq_q^\sharp)
=(u_q^{\mathsf T}W_\eta u_p)
(v_p^{\mathsf T}W_\eta^{-1}v_q).
\]

For \(p=q\),

\[
u_p^{\mathsf T}W_\eta u_p=1+p^{2\eta},
\]

\[
v_p^{\mathsf T}W_\eta^{-1}v_p
=p^{-2\eta}\sum_k\mu(k)^2k^{-2\eta}
=p^{-2\eta}C_\eta.
\]

For \(p\ne q\), the primal overlap is \(1\). The dual overlap is

\[
\sum_{\substack{b:pq\mid b}}
\mu(b/p)\mu(b/q)b^{-2\eta}.
\]

Put \(b=pqk\). Nonzero terms require \(k\) squarefree and coprime to
\(pq\), and the sign product is \(+1\). Hence

\[
G_{pq}
=(pq)^{-2\eta}
\prod_{\ell\ne p,q}(1+\ell^{-2\eta})
=C_\eta
\frac{(pq)^{-2\eta}}
{(1+p^{-2\eta})(1+q^{-2\eta})}.
\]

## 5. Exact two/three-atom phase

At \(s=1/2+it\), let

\[
a_p=p^{-1/2-it}.
\]

For a finite set \(F\),

\[
\operatorname{Tr}\mathcal B_s^2
=2\sum_{p,q\in F}a_p\overline{a_q}G_{pq}.
\]

The diagonal term is \(2G_{pp}/p\). For \(p<q\), the ordered pair and
its reverse sum to

\[
\frac{4G_{pq}}{\sqrt{pq}}
\cos\left(t\log\frac qp\right).
\]

Thus two atoms give one frequency and three atoms give three.

At \(\eta=2\),

\[
C_2=\frac{105}{\pi^4},
\quad
G_{22}=\frac{1785}{16\pi^4},
\quad
G_{33}=\frac{2870}{27\pi^4},
\quad
G_{23}=\frac{105}{1394\pi^4}.
\]

The exact \(2,3\)-atom cutoff is

\[
G_{22}+\frac{2G_{33}}3
+\frac{4G_{23}}{\sqrt6}
\cos\left(t\log\frac32\right).
\]

Adding atom \(5\) uses

\[
G_{55}=\frac{105\cdot626}{625\pi^4},
\quad
G_{25}=\frac{105}{10642\pi^4},
\quad
G_{35}=\frac{105}{51332\pi^4}.
\]

## 6. Divergence and regularization ledger

Since \(G_{pp}\ge C_\eta\),

\[
\sum_p\frac{2G_{pp}}p=\infty.
\]

The countable operator is not Hilbert–Schmidt, so the full second trace
is not defined. Third regularization is the first honest option:

\[
\log\det{}_3(I-zB)
=-\sum_{m\ge3}\frac{z^m}{m}\operatorname{Tr}(B^m).
\]

For an off-diagonal block \(B\), all odd trace powers vanish. The
ledger is therefore:

| Power | Status |
|---:|---|
| \(1\) | removed by \(\det_3\), and block trace formally zero |
| \(2\) | removed by \(\det_3\); not trace class on the line |
| \(3\) | retained but exactly zero by block parity |
| \(4\) | retained and first nonzero spectral moment |

## 7. Isolated fourth frequency

The fourth moment is

\[
\operatorname{Tr}B_s^4
=2\sum_{p,q,r,u}
a_p\overline{a_q}a_r\overline{a_u}
\operatorname{Tr}(q_pq_q^*q_rq_u^*).
\]

The tuple \((p,q,p,q)\) gives

\[
\frac{2G_{pq}^2}{pq}
\exp\left(2it\log\frac qp\right)
\]

after the outer block factor. Adding its conjugate produces

\[
\frac{4G_{pq}^2}{pq}
\cos\left(2t\log\frac qp\right).
\]

The ratio of two products of two primes can equal \(q^2/p^2\) only
for the same multisets, so this frequency cannot cancel.

At \((p,q,\eta)=(2,3,2)\), the coefficient simplifies to

\[
\frac{3675}{971618\pi^8}.
\]

## 8. Metric transfer

The metric equation \(Gq_p=q_p^*G\) becomes, after multiplying by
\(Z^*\) and \(Z\),

\[
K E_p=E_pK,\qquad K=Z^*GZ.
\]

Every active coordinate therefore has a zero off-diagonal row and
column in \(K\). Put

\[
U=G^{1/2}ZK^{-1/2}.
\]

Then \(U^*U=I\), and because \(K\) commutes with the active diagonal,

\[
G^{1/2}T_sG^{-1/2}=UD_s^AU^*.
\]

The reflected atom block squares to \(p^{-1}I_2\), so the paired
eigenvalues are \(\pm p^{-1/2}\), independent of \(s\). Pairing the
third-regularized eigenvalue factors gives

\[
(1-z^2/p)e^{z^2/p}.
\]

Its logarithm starts with \(-z^4/(2p^2)\), establishing product
convergence while making the loss of \(t\)-motion explicit.
