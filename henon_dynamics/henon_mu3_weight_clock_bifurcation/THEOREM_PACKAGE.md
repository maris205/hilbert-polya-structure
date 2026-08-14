# HCS-C51 theorem package

## 1. Source normalization

Let

\[
 K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0.
\]

For a rational prime \(p>3\) with \(p\equiv1\pmod 3\), fix one reduction
of \(\rho\) in \(\mathbf F_p\).  For \(n=2,3,4\), retain the ordered
\(2n\)-step phase

\[
 \Phi_{p,n}(x_0,\ldots,x_{2n-1})
 =2\sum_{i=0}^{2n-1}x_i^3+
   \sum_{i=0}^{2n-2}x_ix_{i+1}+\rho x_{2n-1}x_0.       \tag{1}
\]

Let \(Z_{p,n}=\#\Phi_{p,n}^{-1}(0)\), and keep the inherited normalization

\[
 C_{p,n}=2p^{-(n-1)}Z_{p,n}-2p^n,\qquad
 d_p=\frac{p-1}{2},\qquad c_{p,n}=\frac{C_{p,n}}{d_p}. \tag{2}
\]

No chronological edge is averaged and no critical shift is inserted.
Statements about the Hénon source are made outside the finite bad sets
proved in C48--C50.  Family formulas below are conditional on smoothness;
the source application is asserted only for \(n=2,3,4\).

## 2. Projective cancellation theorem

In \(\mathbf P^{2n-1}\), define

\[
 \mathcal C_n=\sum_{i=0}^{2n-1}x_i^3,\qquad
 \mathcal Q_{n,\rho}=\sum_{i=0}^{2n-2}x_ix_{i+1}
                     +\rho x_{2n-1}x_0,
\]

\[
 S_n=V(\mathcal C_n),\qquad
 Q_n=V(\mathcal Q_{n,\rho}),\qquad
 X_n=S_n\cap Q_n.                                     \tag{3}
\]

Put \(P_m(p)=1+p+\cdots+p^m\) and write

\[
 \#S_n(\mathbf F_p)=P_{2n-2}(p)+A_{p,n},
\]

\[
 \#Q_n(\mathbf F_p)=P_{2n-2}(p)+p^{n-1},\qquad
 \#X_n(\mathbf F_p)=P_{2n-3}(p)-B_{p,n}.              \tag{4}
\]

Then radial stratification gives

\[
 Z_{p,n}=1+P_{2n-1}-\#S_n-\#Q_n+p\#X_n,
\]

and exact cancellation yields

\[
 \boxed{Z_{p,n}=p^{2n-1}-p^{n-1}-A_{p,n}-pB_{p,n}},   \tag{5}
\]

\[
 \boxed{C_{p,n}=-2-\frac{2A_{p,n}}{p^{n-1}}
                       -\frac{2B_{p,n}}{p^{n-2}}}.     \tag{6}
\]

The reductions for \(\rho\) and \(\rho^{-1}=\rho^2\) are isomorphic.
Indeed, the cyclic change

\[
 x_0=\rho^2y_{2n-1},\qquad
 x_i=y_{i-1}\quad(1\le i\le2n-1)                     \tag{7}
\]

preserves \(\mathcal C_n\) and carries the \(\rho\)-closing quadric to
the \(\rho^2\)-closing quadric.  Hence both degree-one primes of \(K\)
above a good split rational prime carry the same trace data.

## 3. Two-weight trace and rank theorem

Use geometric Frobenius, with \(F_p\) acting by \(p\) on
\(\mathbf Q_\ell(-1)\).  Define

\[
 E_n=\mathbf Q_\ell(0)\oplus
 H^{2n-2}_{\mathrm{prim}}(S_{n,\overline K},\mathbf Q_\ell)(n-1),
\]

\[
 O_n=H^{2n-3}(X_{n,\overline K},\mathbf Q_\ell)(n-2). \tag{8}
\]

Then \(E_n\) is pure of weight zero and \(O_n\) is pure of weight one.
At a good split prime,

\[
 e_{p,n}=\operatorname{Tr}(F_p\mid E_n)
 =1+\frac{A_{p,n}}{p^{n-1}},\qquad
 o_{p,n}=\operatorname{Tr}(F_p\mid O_n)
 =\frac{B_{p,n}}{p^{n-2}},                            \tag{9}
\]

so

\[
 \boxed{C_{p,n}=-2(e_{p,n}+o_{p,n})}.                 \tag{10}
\]

For every smooth member of the displayed family,

\[
 \operatorname{rank}H^{2n-2}_{\mathrm{prim}}(S_n)
 =\frac{4^n+2}{3},
\]

\[
 \operatorname{rank}H^{2n-3}(X_n)
 =\frac{2(4^n-4)}{3}.                                 \tag{11}
\]

Consequently,

\[
 \boxed{\operatorname{rank}E_n=\frac{4^n+5}{3}},\qquad
 \boxed{\operatorname{rank}O_n=\frac{2(4^n-4)}{3}},
\]

\[
 \boxed{\operatorname{rank}(E_n\oplus O_n)=4^n-1}.    \tag{12}
\]

For the three Hénon rows:

| \(n\) | \(\operatorname{rank}E_n\) | \(\operatorname{rank}O_n\) | total |
|---:|---:|---:|---:|
| 2 | 7 | 8 | 15 |
| 3 | 23 | 40 | 63 |
| 4 | 87 | 168 | 255 |

For \(n=3\), the invariant description is
\(E_3=\mathbf Q_\ell(0)\oplus H^4_{\mathrm{prim}}(S_3)(2)\).
Its finer decomposition over \(K\) contains twenty normalized Tate lines
inside the primitive cohomology and one rank-two non-Tate Jacobi packet;
the extra \(\mathbf Q_\ell(0)\) makes twenty-one Tate lines in \(E_3\).
No decomposition of the full primitive packet into Tate lines is claimed.

## 4. Forced leading logarithmic \(L\)-extraction

Define

\[
 \ell_n(s)=\sum_{p\equiv1\;(\mathrm{mod}\;3)}c_{p,n}p^{-ns},\qquad
 F_n(s)=\exp\!\left(-\frac{\ell_n(s)}{n}\right).       \tag{13}
\]

Fix \(S\) once and for all as the finite set of rational primes that ramify
in \(K\) or occur in the inherited source-defined bad-reduction sets for
\(n=2,3,4\).  Let \(\ell_n^{(S)}\) denote the same sum with
\(p\notin S\).  The
difference \(\ell_n-\ell_n^{(S)}\) is a finite Dirichlet polynomial, so its
exponential is entire and nonzero.  The weight bounds imply normal
convergence and nonvanishing of \(F_n\)
for \(\Re s>1/(2n)\).  Use the standard cohomological local convention

\[
 L_K^{(S)}(V,u)=\prod_{\mathfrak p\nmid S}
 \det\!\left(1-F_{\mathfrak p}N\mathfrak p^{-u}
 \mid V^{I_{\mathfrak p}}\right)^{-1}.                \tag{14}
\]

Here \(\mathfrak p\nmid S\) means that
\(\mathfrak p\) lies above no prime in \(S\).  An omitted standard local factor
may be restored only if it is holomorphic and nonzero on the stated
domain; no arbitrary rational local factor is absorbed.
There exists a canonical origin-normalized holomorphic nonzero function
\(H_{n,S}\) on \(\Re s>0\), including that finite source correction, such
that, initially for
\(\Re s>1/(2n)\),

\[
 \boxed{
 F_n(s)=
 \exp\!\left(\frac{2}{n}\operatorname{Log}_0
 L_K^{(S)}(E_n\oplus O_n,ns+1)\right)H_{n,S}(s).
 }                                                     \tag{15}
\]

Here \(\operatorname{Log}_0\) is the branch obtained by the absolutely
convergent Euler logarithm and normalized to vanish at \(+\infty\).
The equality is an equality of nonzero holomorphic germs.  For \(n=3,4\)
it does not promote the fractional power to a global meromorphic root.

For \(n=2\), C50 proves the integer-power specialization

\[
 F_2(s)=\zeta_K(2s+1)^7
 L\!\left(H^1(C/K),2s+1\right)H_2(s),                 \tag{16}
\]

with standard continuation and functional equations for the two displayed
factors.  No analogous full Hasse--Weil functional equation is asserted
for \(O_3\), \(O_4\), \(H_3\), \(H_4\), or the full Hénon germ.

## 5. Weight--clock bifurcation theorem

The exact normalization forces

\[
 \frac{1}{p-1}=\sum_{j\ge1}p^{-j},\qquad
 u_{n,j}=ns+j.                                        \tag{17}
\]

A completed pure weight-\(w\) factor has standard reflection
\(u\mapsto w+1-u\).  Under \(u=ns+j\), its mapped reflection center is

\[
 \boxed{s_{n,j}(w)=\frac{(w+1)/2-j}{n}}.              \tag{18}
\]

For the leading denominator term \(j=1\),

\[
 s_{n,1}(1)=0\quad(n=2,3,4),                          \tag{19}
\]

whereas

\[
 s_{2,1}(0)=-\frac14,\qquad
 s_{3,1}(0)=-\frac16,\qquad
 s_{4,1}(0)=-\frac18.                                 \tag{20}
\]

Thus the leading odd rail aligns exactly at zero, but the even rail
bifurcates into three centers.  Moreover,

\[
 s_{n,j}(1)=-\frac{j-1}{n}\qquad(j\ge2),              \tag{21}
\]

so the complete denominator tower destroys even the odd alignment.

The \(n=2\) factorization (16) is the minimal theorem-level witness:
\(\zeta_K(2s+1)^7\) has mapped center \(-1/4\), while
\(L(H^1(C/K),2s+1)\) has mapped center \(0\), and both component
functional equations are proved.

## 6. Twist invariance

If a Tate twist \(k\) is made while preserving the same source
coefficient, then

\[
 (w,j)\longmapsto(w-2k,j-k).
\]

Therefore

\[
 \frac{(w-2k+1)/2-(j-k)}{n}
 =\frac{(w+1)/2-j}{n}.                                \tag{22}
\]

Every consistent integral Tate twist preserves the mapped center.
The same algebra applies to a formal half twist.  A half twist at fixed
\(u\), by contrast, multiplies local eigenvalues by \(p^{\mp1/2}\) and
changes the source coefficient; it is not a repair of the locked object.

## 7. Direct compatible-system obstruction

Suppose the leading factor in (15) were the standard \(L\)-function of a
semisimple direct source-native \(K\)-compatible system \(W_n\) whose
split-prime trace is unchanged, with the weight-zero and weight-one packets
retained.  Degree-one primes of \(K\) have density one, and equality of the
leading traces there gives, by Chebotarev density and Brauer--Nesbitt,
\[
 n[W_n]=2[E_n\oplus O_n]
\]
in the semisimple representation ring.  Purity separates the weight-zero
and weight-one summands, so their dimensions must be multiplied by
\(2/n\).  At
\(n=3\) these dimensions are

\[
 \frac23(23,40)=\left(\frac{46}{3},\frac{80}{3}\right),
\]

and at \(n=4\) the total dimension is

\[
 \frac12(87+168)=\frac{255}{2}.
\]

Ordinary finite-rank compatible systems have integral ranks, so no such
direct \(K\)-packet exists.

This conclusion is deliberately scoped.  It does not exclude a
restriction-of-scalars construction, a Galois-orbit counterpacket, a
nonfactorwise identity, or the inherited normalized-semifinite
determinant.  Restriction from \(K\) to \(\mathbf Q\) doubles ranks and
removes the bare \(n=4\) parity obstruction while changing the object and
prime organization.  At \(n=3\), the corresponding candidate dimensions
\(92/3\) and \(160/3\) remain nonintegral.

## 8. Denominator-cleared odd skeleton

Let \(\Lambda(O_n,u)\) denote the expected standard completion of the
pure weight-one factor whenever it exists.  Clearing the denominators in
\(2/n\) gives

\[
 \boxed{
 \mathcal O_6(s)=
 \Lambda(O_2,2s+1)^6
 \Lambda(O_3,3s+1)^4
 \Lambda(O_4,4s+1)^3.
 }                                                     \tag{23}
\]

If each completed factor has its standard reflection
\(\Lambda(O_n,u)=\varepsilon_n\Lambda(O_n,2-u)\), then

\[
 \mathcal O_6(s)=\varepsilon\mathcal O_6(-s).          \tag{24}
\]

Equation (24) is a **conditional skeleton theorem**.  The \(n=2\)
functional equation is inherited and proved.  For \(n=3,4\), (23)
records the uniquely forced expected center and integer exponents; it
does not prove continuation or a functional equation.

## 9. Hodge ledger and C52 gate

The twisted Hodge types are

\[
\begin{array}{c|l}
E_2&(0,0)^7\\
O_2&(1,0)^4+(0,1)^4\\
E_3&(1,-1)^1+(0,0)^{21}+(-1,1)^1\\
O_3&(1,0)^{20}+(0,1)^{20}\\
E_4&(1,-1)^8+(0,0)^{71}+(-1,1)^8\\
O_4&(2,-1)^1+(1,0)^{83}+(0,1)^{83}+(-1,2)^1.
\end{array}                                           \tag{25}
\]

For the fivefold \(X_4=(2,3)\subset\mathbf P^7\), put

\[
 Q_y(x)=\frac{x(1+ye^{-x})}{1-e^{-x}}.
\]

The finite expansion

\[
 Q_y(x)=(1+y)+\frac{1-y}{2}x+\frac{1+y}{12}x^2
 -\frac{1+y}{720}x^4+O(x^6)
\]

gives

\[
 \chi_y(X_4)=6[H^5]\,
 \frac{Q_y(H)^8}{(1+y)Q_y(2H)Q_y(3H)}
 =1-82y^2+82y^3-y^5.                                 \tag{26}
\]

Weak Lefschetz then yields

\[
 h^{4,1}=h^{1,4}=1,\qquad
 h^{3,2}=h^{2,3}=83.                                  \tag{27}
\]

After twisting by \(2\), this is exactly the \(O_4\) row of (25).

At the unique complex place of \(K\), define

\[
 \Gamma_{\mathbf C}(u)=2(2\pi)^{-u}\Gamma(u).
\]

The Hodge rows in (25) give the following expected sector Gamma ledger:

\[
\begin{array}{c|l}
E_2&\Gamma_{\mathbf C}(u)^7\\
O_2&\Gamma_{\mathbf C}(u)^8\\
E_3&\Gamma_{\mathbf C}(u)^{21}\Gamma_{\mathbf C}(u+1)^2\\
O_3&\Gamma_{\mathbf C}(u)^{40}\\
E_4&\Gamma_{\mathbf C}(u)^{71}\Gamma_{\mathbf C}(u+1)^{16}\\
O_4&\Gamma_{\mathbf C}(u)^{166}\Gamma_{\mathbf C}(u+1)^2.
\end{array}                                           \tag{28}
\]

Equation (28) is an expected finite-sector archimedean ledger.  It proves
neither the \(n=3,4\) Hasse--Weil functional equations nor the existence of
an infinite regularized Gamma product for the full denominator tower.
Since the extreme types \((2,-1)\) and \((-1,2)\) occur, the full
\(O_4\) cannot be \(H^1\) of an abelian variety.  HCS-C52 must construct
or obstruct a \(K\)-rational algebraic projector whose realizations are
\(\ell\)-compatible and which separates the rank-two extreme summand from
the rank-166 level-one summand.  A Hodge projector or a single-\(\ell\)
numerical splitting is insufficient.

## 10. Route-A and claim boundary

New C51 delta:

- two-weight source identity and conditional rank \(4^n-1\);
- exact exponent \(2/n\) and residual \(H_{n,S}\) on \(\Re s>0\);
- leading odd alignment and full tower bifurcation;
- twist-invariant center obstruction;
- scoped direct-system rank obstruction;
- denominator-cleared odd skeleton;
- exact \(O_4\) Hodge gate.

Inherited:

- C48--C50 source smoothness for \(n=2,3,4\);
- the \(n=2\) standard factor continuation and functional equation;
- C50 continuation of the complete normalized germ to \(\Re s>1/5\);
- the normalized-semifinite \(\operatorname{Det}_{10}\) realization.

Not proved:

- a full Hénon archimedean completion or functional equation;
- \(n=3,4\) odd Hasse--Weil functional equations;
- a common factorwise center beyond the leading odd rail;
- continuation through \(\Re s=1/5\);
- a self-adjoint Hilbert--Pólya operator.
