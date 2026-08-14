# HCS-C53 derivation package

## D1. Why the semilinear reversal works

Write \(N=2n\), \(\sigma(i)=-i\pmod N\), and
\((M_nx)_i=\rho^{e_i}x_{\sigma(i)}\), with \(e_i=1\) exactly for nonzero
even \(i\). Since \(3e_i\) is divisible by three,

\[
C_n(M_nx)=\sum_i\rho^{3e_i}x_{\sigma(i)}^3=C_n(x).
\]

The quadratic has three transformed edge classes:

\[
\begin{array}{ccl}
i=0&:&x_0x_1\mapsto x_0x_{N-1}\quad\hbox{with phase }1,\\
1\le i\le N-2&:&x_ix_{i+1}\mapsto x_{N-i}x_{N-i-1}
\quad\hbox{with phase }\rho,\\
\text{closing}&:&\rho x_{N-1}x_0\mapsto\rho x_1x_0.
\end{array}
\]

Thus the closing coefficient becomes \(1\) and all nonclosing
coefficients become \(\rho\). Since \(\rho\rho^2=1\), termwise collection
gives

\[
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x).
\]

Also \(\sigma^2=1\), and the phase on the return is
\(\rho^{e_i}\tau(\rho^{e_{\sigma(i)}})=1\), because
\(e_{\sigma(i)}=e_i\). Hence \(M_n\tau(M_n)=I\).

## D2. Fixed basis and determinant

Let \(\theta=1+2\rho\), so \(\tau(\theta)=-\theta\). Each pair
\((i,N-i)\), \(1\le i<n\), contributes the fixed columns

\[
x_i=a_i+\theta b_i,\qquad
x_{N-i}=\rho^{e_i}(a_i-\theta b_i).
\]

The fixed central coordinate is \(x_n=c\) for odd \(n\) and
\(x_n=(1+\rho)c\) for even \(n\). After pairing rows \(i,N-i\), the
\((a_i,b_i)\) block has determinant \(-2\rho^{e_i}\theta\). The row
permutation from source order to paired order has sign
\((-1)^{n-1}\), cancelling the product of the \(n-1\) block signs.
There are \(\lfloor(n-1)/2\rfloor\) even indices in
\(1,\ldots,n-1\). Hence, in the frozen variable and row order,

\[
\det B_n=(2\theta)^{n-1}\rho^{\lfloor(n-1)/2\rfloor}\kappa_n.
\]

For \(n=4\), this is

\[
(2\theta)^3\rho(1+\rho)=24\theta.
\]

The nonzero determinant supplies an actual \(K\)-linear coordinate change,
not merely an abstract descent datum.

## D3. Rational equations

For every paired coordinate,

\[
(a+\theta b)^3+(a-\theta b)^3=2a^3-18ab^2.
\]

The central cube equals \(c^3\) for odd \(n\), while
\((1+\rho)^3=-1\) gives \(-c^3\) for even \(n\). This yields \(C_{n,0}\).
Expanding adjacent coordinate pairs and using \(\theta^2=-3\) gives the
four-term block in \(Q_{n,0}\). The central edge is
\((a_{n-1}+3b_{n-1})c\) in odd rows and \(2a_{n-1}c\) in even rows.
Finally,

\[
C_n(B_nu)=C_{n,0}(u),\qquad
Q_{n,\rho}(B_nu)=(1+\rho)Q_{n,0}(u).
\]

The scalar \(1+\rho\ne0\) does not change the common zero locus.

## D4. Dihedral graph descent

The transported Galois action on the order-24 C52 group is

\[
r^k\mapsto r^{-k},\qquad r^ks\mapsto r^{1-k}s.
\]

It is a permutation of all 24 elements, so the Reynolds cycle
\(e_G=24^{-1}\sum_g\Gamma_g\) is Galois-stable. For the quadratic base-change
map \(q\),

\[
e_{\mathscr G}=\frac12q_*e_G,\qquad
q^*e_{\mathscr G}=\frac12(e_G+\tau e_G)=e_G.
\]

Moreover \(q_*q^*=2\), so rational pullback is injective. Idempotence,
self-transpose, orthogonality, and commutation with the rational middle
projector can therefore be checked after pullback to \(K\), where they are
the frozen C52 identities.

## D5. Local-factor algebra

At split \(p\), base change supplies two copies of the rational factor:

\[
L_{K,p}=L_{\mathbf Q,p}^2.
\]

Multiplication of the C51 exponent \(2/n\) gives exponent \(4/n\), whose
reduced denominator is \(n/\gcd(n,4)\). This calculation is unconditional
for the certified motivic rows \(n=2,3,4\), and conditional for any later
row on the existence of the analogous smooth packet. It uniquely clears
the fractional exponent at \(n=4\), but leaves \(4/3\) at \(n=3\).

At inert \(p\), \(\operatorname{Frob}_v=\operatorname{Frob}_p^2\). Thus
the eigenvalues become \(\alpha_i^2\), and

\[
P_{K,v}(U^2)=\prod_i(1-\alpha_i^2U^2)
=\prod_i(1-\alpha_iU)(1+\alpha_iU)=P_p(U)P_p(-U).
\]

This derivation is the firewall preventing a split identity from being
promoted to a global square root.
