# HCS-C50 theorem package

## 1. Frozen object and notation

Let

\[
K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0.
\]

For rational primes \(p>3\), \(p\equiv1\pmod 3\), retain the clock
\(\log p\), the field-degree normalization

\[
d_p=\frac{p-1}{2},\qquad c_{p,n}=\frac{C_{p,n}}{d_p},
\]

and the chronological moments inherited from HCS-C45--C49. No transition
matrix is averaged, and no critical shift is inserted.

The C48 curve is the smooth projective completion of

\[
C:\quad y^3=f(x),\qquad
f(x)=-\frac{x(\rho^2x-1)}{\rho(x^3+1)}.                 \tag{1}
\]

It has genus four. At a good split prime set

\[
a_p=p+1-\#C(\mathbf F_p).
\]

The reductions belonging to \(\rho\) and \(\rho^{-1}\) are isomorphic, as
proved in C48, and therefore have the same \(a_p\).

## 2. \(K\)-rational elliptic decomposition

Define automorphisms of \(C\) by

\[
\delta(x,y)=(x,\rho y),\qquad
\iota(x,y)=\left(\frac{\rho^2}{x},-y\right),             \tag{2}
\]

and

\[
T(x)=-\frac{\rho^2(x+1)}{x+\rho^2},\qquad
h=\frac{\rho-1}{3},\qquad
\jmath(x,y)=\left(T(x),\frac{h}{y}\right).              \tag{3}
\]

The exact identities

\[
f(\rho^2/x)=-f(x),\quad T^2=1,\quad
f(T(x))f(x)=h^3,\quad T(\rho^2/x)=\rho^2/T(x)           \tag{4}
\]

give

\[
\delta^3=\iota^2=\jmath^2=1,\qquad
[\iota,\delta]=[\iota,\jmath]=1,\qquad
\jmath\delta\jmath=\delta^{-1}.                         \tag{5}
\]

Thus these automorphisms generate a \(K\)-rational subgroup

\[
G\simeq C_2\times S_3.                                  \tag{6}
\]

The quotient by \(\langle\delta\rangle\) is \(\mathbf P^1_x\).
The involution \(\iota\) has exactly two fixed points, and hence
\(g(C/\langle\iota\rangle)=2\). Consequently,

\[
H^0(C,\Omega_C^1)\simeq
\operatorname{Std}_{+}\oplus\operatorname{Std}_{-}      \tag{7}
\]

as a \(C_2\times S_3\)-representation. Here
\(\operatorname{Std}\) is the rational two-dimensional standard
representation of \(S_3\), and the subscript is the sign of the central
involution \(\iota\).

Put

\[
e_{\mathrm{std}}=1-\frac{1+\delta+\delta^2}{3},\qquad
e_\pm=\frac{1\pm\iota}{2},\qquad
q_\pm=e_\pm e_{\mathrm{std}}\frac{1+\jmath}{2}.         \tag{8}
\]

The \(q_\pm\) are primitive rational idempotents in the two standard matrix
blocks. If \(N\) clears denominators and

\[
E_\pm=\operatorname{im}\!\left(
Nq_\pm:\operatorname{Jac}(C)\longrightarrow\operatorname{Jac}(C)
\right)^0,
\]

then \(E_\pm/K\) are elliptic curves and

\[
\boxed{\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2.}  \tag{9}
\]

This is an isogeny, not a polarized isomorphism. The complete
decomposability of related complex trigonal genus-four Jacobians is not
claimed as new. The new result is the explicit \(K\)-rational decomposition
of this Hénon fibre and its exact use in the chronological Euler factor.

## 3. Exact extraction of the second counterterm

HCS-C48 proves

\[
c_{p,2}=-\frac{28+4a_p}{p-1}.                           \tag{10}
\]

Let

\[
\ell_2(s)=\sum_{p\equiv1(3)}c_{p,2}p^{-2s},\qquad
F_2(s)=\exp\!\left(-\frac{\ell_2(s)}2\right)            \tag{11}
\]

on the original half-plane \(\Re s>1/4\), and use the convention

\[
L(H^1(C/K),u)=
\prod_{\mathfrak p}
\det\!\left(
1-\operatorname{Frob}_{\mathfrak p}N\mathfrak p^{-u}
\mid H^1(C_{\overline K},\mathbf Q_\ell)
\right)^{-1}.                                           \tag{12}
\]

There is a canonical holomorphic nonzero function \(H_2\) on \(\Re s>0\)
such that, initially on \(\Re s>1/4\),

\[
\boxed{
F_2(s)=\zeta_K(2s+1)^7L(H^1(C/K),2s+1)H_2(s).}          \tag{13}
\]

The sign and integer powers in (13) are exact. Each split rational prime
gives two degree-one primes of \(K\), so the first prime coefficient of the
right-hand side is \(14+2a_p\), exactly the coefficient from (11).
The residual logarithm consists of denominator corrections, higher Euler
powers, inert primes of norm \(p^2\), and finitely many bad factors. It
converges locally absolutely for \(\Re s>0\).

Equation (9) gives

\[
L(H^1(C/K),u)=L(E_+/K,u)^2L(E_-/K,u)^2.                 \tag{14}
\]

The Caraiani--Newton modularity theorem over
\(K=\mathbf Q(\sqrt{-3})\) gives entire continuation of both elliptic
\(L\)-functions. Thus (13) continues \(F_2\) holomorphically to
\(\Re s>0\). The continuation need not be zero-free: elliptic
\(L\)-functions may vanish, and the original \(\operatorname{Log}_0\) is
not asserted to remain single-valued through those zeros.

## 4. The frozen fourth moment

For \(p>3\), \(p\equiv1\pmod3\), retain the ordered eight-step phase

\[
\Phi_{p,4}(x_0,\ldots,x_7)
=2\sum_{i=0}^7x_i^3+\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0. \tag{15}
\]

Let \(Z_{p,4}=\#\Phi_{p,4}^{-1}(0)\) and

\[
C_{p,4}=2p^{-3}Z_{p,4}-2p^4,\qquad
c_{p,4}=\frac{2C_{p,4}}{p-1}.                           \tag{16}
\]

In \(\mathbf P^7\), put

\[
S=V\!\left(\sum x_i^3\right),\qquad
Q=V\!\left(\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0\right),
\qquad X=S\cap Q.                                       \tag{17}
\]

Projective direction counting gives

\[
Z_{p,4}=1+\#\mathbf P^7-\#S-\#Q+p\#X.                  \tag{18}
\]

The quadric is split and smooth. In even--odd coordinates its bilinear
block \(M_\rho\) has \(\det M_\rho=1-\rho\ne0\). Hence

\[
\#Q(\mathbf F_p)=P_6(p)+p^3,\qquad
P_m(p)=1+p+\cdots+p^m.                                  \tag{19}
\]

The characteristic-zero fivefold \(X/K\) is smooth. This is proved by the
exact recurrence Gröbner certificate in **PROOF_PACKAGE.md**, not by generic
openness alone. It follows that the integral model is smooth away from a
finite set \(\Sigma_4\) of prime ideals.

At a good prime write

\[
\#S(\mathbf F_p)=P_6(p)+A_p,\qquad
\#X(\mathbf F_p)=P_5(p)-B_p.                            \tag{20}
\]

The primitive middle ranks are

\[
\operatorname{rank}H^6_{\mathrm{prim}}(S)=86,\qquad
\operatorname{rank}H^5(X)=168.                          \tag{21}
\]

Consequently,

\[
|A_p|\le86p^3,\qquad |B_p|\le168p^{5/2}.                \tag{22}
\]

Equations (18)--(20) give

\[
\boxed{Z_{p,4}=p^7-p^3-A_p-pB_p}                       \tag{23}
\]

and

\[
\boxed{C_{p,4}=-2-\frac{2A_p}{p^3}-\frac{2B_p}{p^2}.}   \tag{24}
\]

Therefore

\[
|C_{p,4}|\le174+336\sqrt p,\qquad
\boxed{|c_{p,4}|\le\frac{348+672\sqrt p}{p-1}
=O(p^{-1/2}).}                                          \tag{25}
\]

The finite-exception qualifier is sharp. At \(p=181,\rho=48\), the nonzero
point

\[
(9,158,158,9,104,128,171,153)                           \tag{26}
\]

satisfies the normalized singular recurrence and \(Q=0\). The reduction is
therefore singular, so an all-split smoothness statement is false. This
single bad local factor does not affect an Euler abscissa.

## 5. Fifth-abscissa continuation

Retain

\[
c_{p,1}=-\frac{12}{p-1},\qquad
c_{p,3}=O(p^{-1/2}),\qquad
|c_{p,n}|\le4\cdot4^n.                                  \tag{27}
\]

The first term converges for \(\Re s>0\), the third for \(\Re s>1/6\),
and (25) makes the fourth converge for \(\Re s>1/8\). After replacing the
second term by (13), the untreated tail starts at \(n=5\); its first wall
is \(\Re s=1/5\). Hence the original Euler germ has a canonical
holomorphic continuation

\[
\boxed{\mathcal G^{\mathrm{cont}}(s)\text{ on }\Re s>1/5.} \tag{28}
\]

It may have zeros inherited from (13). No continuation through
\(\Re s=1/5\) is asserted.

## 6. Tenth-order normalized-semifinite determinant

For the inherited normalized faithful semifinite trace,

\[
X_s\in L^q(\mathcal M,\tau)\Longleftrightarrow q\Re s>2. \tag{29}
\]

Thus \(q=10\) is the least fixed integer order valid throughout
\(\Re s>1/5\). For \(n\ne2\), put

\[
\ell_n(s)=\sum_{p\equiv1(3)}c_{p,n}p^{-ns}.
\]

On \(\Re s>1/5\),

\[
\boxed{
\mathcal G^{\mathrm{cont}}(s)=F_2^{\mathrm{cont}}(s)
\exp\!\left(
-\sum_{\substack{1\le n\le9\\n\ne2}}\frac{\ell_n(s)}n
\right)
\operatorname{Det}_{10,\tau,\mathrm{gr}}(I-X_s).}       \tag{30}
\]

This is a trace-associated normalized-semifinite graded determinant. On the
underlying Hilbert direct sum,

\[
X_s\in S^q(\mathcal H)\Longleftrightarrow q\Re s>3,      \tag{31}
\]

so the least fixed classical integer Schatten order on the same half-plane
is \(15\). Its local trace encodes the ordinary Galois norm, not the
degree-normalized root. Equation (30) is not a classical Fredholm
determinant or a classical tenth-order determinant.

## 7. Route-A scope

The evaluator-compatible classification is

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).                   \tag{32}
\]

Overall status: **ROUTE_A_EXPLORATORY**.

The A3 evidence records
**holomorphic_continuation: PROVED_RE_GT_1_5**. Only the extracted elliptic
factor has a known functional equation; the full Hénon object does not.
No Gamma factor, Riemann divisor, zero-counting law, primitive-orbit/prime
correspondence, or self-adjoint Hilbert--Pólya operator is obtained.
**route_b_invocation_allowed** remains false.
