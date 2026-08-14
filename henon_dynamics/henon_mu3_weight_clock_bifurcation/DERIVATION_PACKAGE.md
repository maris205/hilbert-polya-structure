# HCS-C51 derivation package

## 1. Radial root partition

Fix \(n\in\{2,3,4\}\) and a good split prime \(p\).  Write

\[
 \Phi=2\mathcal C_n+\mathcal Q_{n,\rho}.
\]

For each nonzero projective direction \([x]\in\mathbf P^{2n-1}(\mathbf
F_p)\), points on the line have the form \(tx\), and

\[
 \Phi(tx)=t^2(2t\mathcal C_n(x)+\mathcal Q_{n,\rho}(x)).
\]

Besides \(t=0\), the number of nonzero roots is:

| projective stratum | nonzero roots |
|---|---:|
| \(\mathcal C_n\ne0,\ \mathcal Q_{n,\rho}\ne0\) | \(1\) |
| \(\mathcal C_n\ne0,\ \mathcal Q_{n,\rho}=0\) | \(0\) |
| \(\mathcal C_n=0,\ \mathcal Q_{n,\rho}\ne0\) | \(0\) |
| \(\mathcal C_n=\mathcal Q_{n,\rho}=0\) | \(p-1\) |

Therefore

\[
 Z_{p,n}
 =1+\#\!\left(\mathbf P^{2n-1}\setminus(S_n\cup Q_n)\right)
 +(p-1)\#X_n
 =1+P_{2n-1}-\#S_n-\#Q_n+p\#X_n.             \tag{D1}
\]

The last form separates the cubic, quadric, and intersection deviations.

## 2. Split quadric and Tate cancellation

In even--odd coordinates, the matrix of \(\mathcal Q_{n,\rho}\) is
bipartite and nonsingular for \(\rho^3=1\), \(\rho\ne1\), in the
three source rows.  It is a split quadric in \(\mathbf P^{2n-1}\), hence

\[
 \#Q_n=P_{2n-2}+p^{n-1}.                              \tag{D2}
\]

With

\[
 \#S_n=P_{2n-2}+A_{p,n},\qquad
 \#X_n=P_{2n-3}-B_{p,n},
\]

substitution into (D1) gives

\[
\begin{aligned}
Z_{p,n}
&=1+P_{2n-1}-2P_{2n-2}-p^{n-1}
  +pP_{2n-3}-A_{p,n}-pB_{p,n}\\
&=p^{2n-1}-p^{n-1}-A_{p,n}-pB_{p,n}.
\end{aligned}                                         \tag{D3}
\]

Multiplying by \(2p^{-(n-1)}\) and subtracting \(2p^n\)
produces

\[
 C_{p,n}=-2-\frac{2A_{p,n}}{p^{n-1}}
              -\frac{2B_{p,n}}{p^{n-2}}.             \tag{D4}
\]

This cancellation is source-native: it uses the ordered closing edge and
does not pass through any transition matrix.

## 3. Trace normalization and weights

The cubic \(S_n\) has even dimension \(2n-2\), so its primitive middle
trace enters the point count with positive sign:

\[
 A_{p,n}=\operatorname{Tr}\!
 \left(F_p\mid H^{2n-2}_{\mathrm{prim}}(S_n)\right).
\]

The intersection \(X_n\) has odd dimension \(2n-3\), so its middle trace
enters with negative sign:

\[
 B_{p,n}=\operatorname{Tr}\!
 \left(F_p\mid H^{2n-3}(X_n)\right).
\]

Twisting by \(n-1\) and \(n-2\), respectively, gives

\[
 e_{p,n}=1+\frac{A_{p,n}}{p^{n-1}},\qquad
 o_{p,n}=\frac{B_{p,n}}{p^{n-2}},
\]

of weights zero and one.  Equation (D4) becomes

\[
 C_{p,n}=-2(e_{p,n}+o_{p,n}).                         \tag{D5}
\]

Deligne purity gives \(e_{p,n}=O(1)\) and
\(o_{p,n}=O(p^{1/2})\), uniformly away from the finite bad sets.

## 4. Rank \(4^n-1\)

For a smooth cubic hypersurface \(S_n\subset\mathbf P^{2n-1}\), the
Jacobian-ring computation gives

\[
 b^{\mathrm{prim}}_{2n-2}(S_n)=\frac{4^n+2}{3}.       \tag{D6}
\]

For a smooth \(X_n=(2,3)\subset\mathbf P^{2n-1}\),

\[
 c(TX_n)=\frac{(1+H)^{2n}}{(1+2H)(1+3H)},\qquad
 \deg X_n=6.                                          \tag{D7}
\]

Direct coefficient extraction yields

\[
 [H^{2n-3}]
 \frac{(1+H)^{2n}}{(1+2H)(1+3H)}
 =\frac{3n+1-4^n}{9}.                                 \tag{D8}
\]

Thus

\[
 \chi(X_n)=6\frac{3n+1-4^n}{9}
 =\frac{2(3n+1-4^n)}{3}.                              \tag{D9}
\]

Weak Lefschetz identifies every nonmiddle Betti number with that of
\(\mathbf P^{2n-3}\).  Since the dimension is odd, there are \(2n-2\)
even Tate contributions and

\[
 b_{2n-3}(X_n)
 =(2n-2)-\chi(X_n)
 =\frac{2(4^n-4)}{3}.                                 \tag{D10}
\]

Adding the extra trivial line in \(E_n\),

\[
 \operatorname{rank}(E_n\oplus O_n)
 =1+\frac{4^n+2}{3}+\frac{2(4^n-4)}{3}
 =4^n-1.                                              \tag{D11}
\]

Equations (D6)--(D11) hold for every smooth family member.  Their
application to the Hénon source is limited to \(n=2,3,4\).

## 5. Leading logarithm

Since \(d_p=(p-1)/2\), equation (D5) gives

\[
 c_{p,n}=-\frac{4(e_{p,n}+o_{p,n})}{p-1}.             \tag{D12}
\]

Let \(\ell_n^{(S)}\) omit the finitely many split primes in the frozen
bad set \(S\).  For the good-prime sum,

\[
 -\frac{\ell_n^{(S)}(s)}{n}
 =\frac{4}{n}\sum_{\substack{p\equiv1(3)\\p\notin S}}
 (e_{p,n}+o_{p,n})p^{-ns}
 \sum_{j\ge1}p^{-j}.                                  \tag{D13}
\]

At a good split \(p\notin S\), the two degree-one primes of \(K\) have
equal trace.
The degree-one term of
\((2/n)\operatorname{Log}L_K^{(S)}(E_n\oplus O_n,ns+1)\), with the finite
bad set \(S\) omitted, is therefore

\[
 \frac{4}{n}(e_{p,n}+o_{p,n})p^{-ns-1},               \tag{D14}
\]

which is exactly the \(j=1\) term of (D13).

The \(j\ge2\) part of (D13) is absolutely summable on a half-plane larger
than \(\Re s>0\).  The degree-\(m\ge2\) terms in the Euler logarithm are
bounded by

\[
 O\!\left(p^{-mn\Re s-m/2}\right)
\]

for the weight-one packet, and better for weight zero.  Their prime sum
converges normally for \(\Re s>0\).  Inert-prime degree-one terms outside
\(S\) have norm \(p^2\) and satisfy the same boundary.  Hence the
difference of (D13) and the incomplete standard Euler logarithm
defines a holomorphic function on \(\Re s>0\).  Exponentiating it gives
the canonical nonzero residual \(H_{n,S}\), relative to the frozen set
\(S\).  Finally,
\[
 -\frac{\ell_n(s)-\ell_n^{(S)}(s)}{n}
 =-\frac1n\sum_{\substack{p\in S\\p\equiv1(3)}}c_{p,n}p^{-ns}
\]
is a finite entire Dirichlet polynomial; its exponential is nonzero and is
included in \(H_{n,S}\).

The original series itself has terms
\(O(p^{-n\Re s-1/2})\), so its natural absolute-convergence domain from
the weight bound is \(\Re s>1/(2n)\).

## 6. Center map and tower

The denominator identity in (D13) fixes

\[
 u_{n,j}=ns+j,\qquad j\ge1.                           \tag{D15}
\]

The standard pure weight-\(w\) reflection is

\[
 u\longmapsto w+1-u.
\]

Writing the reflected variable as \(ns'+j\) gives

\[
 s'=\frac{w+1-2j}{n}-s,
\]

and therefore the reflection center is

\[
 s_{n,j}(w)=\frac{(w+1)/2-j}{n}.                      \tag{D16}
\]

For \(w=1,j=1\), this is zero for every \(n\).  For \(w=0,j=1\),
it is \(-1/(2n)\), producing \(-1/4,-1/6,-1/8\).
For the odd tower \(j\ge2\), it is \(-(j-1)/n\).

## 7. Why twisting cannot repair the mismatch

A Tate twist \(V(k)\) has weight \(w-2k\) and local eigenvalues
\(\alpha p^{-k}\).  Preserving the same coefficient
\(\alpha p^{-ns-j}\) requires replacing \(j\) by \(j-k\).  Thus

\[
 \frac{(w-2k+1)/2-(j-k)}{n}
 =\frac{(w+1)/2-j}{n}.                                \tag{D17}
\]

The mapped center is invariant.  A formal half twist obeys the same
identity.  If the variable is not shifted, the coefficient changes by a
factor \(p^{\pm1/2}\), so the operation changes the source object.

## 8. Direct-system divisibility

The leading standard logarithm occurs with exponent \(2/n\).  A direct
finite-rank source packet realizing this power without changing the
split-prime trace would need dimensions

\[
 \frac{2}{n}\operatorname{rank}E_n,\qquad
 \frac{2}{n}\operatorname{rank}O_n.                   \tag{D18}
\]

For \(n=3\), these are \(46/3\) and \(80/3\).  For \(n=4\), their sum
is \(255/2\).  This proves the direct \(K\)-packet obstruction and
nothing stronger.  Restriction of scalars doubles the source dimensions,
removing the bare \(n=4\) parity failure while changing the object; it
does not repair the \(n=3\) denominators.

## 9. The \(\chi_y\) calculation

For \(X_4=(2,3)\subset\mathbf P^7\), Hirzebruch--Riemann--Roch gives

\[
 \chi_y(X_4)=6[H^5]\,
 \frac{Q_y(H)^8}{(1+y)Q_y(2H)Q_y(3H)},\qquad
 Q_y(x)=\frac{x(1+ye^{-x})}{1-e^{-x}}.                \tag{D19}
\]

Only terms through degree five can contribute.  The finite Taylor
expansion

\[
 Q_y(x)=(1+y)+\frac{1-y}{2}x+\frac{1+y}{12}x^2
 -\frac{1+y}{720}x^4+O(x^6)
\]

produces

\[
 \chi_y(X_4)=1-82y^2+82y^3-y^5.                      \tag{D20}
\]

Weak Lefschetz and Hodge symmetry write the same polynomial as

\[
 1+(a-1)y+(1-b)y^2+(b-1)y^3+(1-a)y^4-y^5.
\]

Comparison gives \(a=h^{4,1}=1\) and \(b=h^{3,2}=83\).  Twisting the
middle cohomology by \(2\) yields

\[
 O_4:(2,-1)^1+(1,0)^{83}+(0,1)^{83}+(-1,2)^1.
\]

This calculation identifies a Hodge-theoretic target, not an algebraic
projector.
