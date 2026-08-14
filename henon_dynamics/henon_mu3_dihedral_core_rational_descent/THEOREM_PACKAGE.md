# HCS-C53 theorem package

## 1. Explicit descent in every row

Let \(K=\mathbf Q(\rho)\), where \(\rho^2+\rho+1=0\), and let
\(\tau(\rho)=\rho^2\). For \(n\ge2\), put \(N=2n\) and

\[
C_n=\sum_{i=0}^{N-1}x_i^3,\qquad
Q_{n,\rho}=\sum_{i=0}^{N-2}x_ix_{i+1}+\rho x_{N-1}x_0.
\]

Set \(\sigma(i)=-i\pmod N\), and set \(e_i=1\) when \(i\ne0\) is even
and \(e_i=0\) otherwise. Define

\[
(M_nx)_i=\rho^{e_i}x_{\sigma(i)}.
\]

**Theorem A (symbolic Weil descent).** For every \(n\ge2\),

\[
C_n(M_nx)=C_n(x),\qquad
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x),\qquad
M_n\tau(M_n)=I.
\]

Thus \(M_n:X_n^\tau\to X_n\) is a descent datum for
\(X_n=V(C_n,Q_{n,\rho})\).

Put \(\theta=1+2\rho\), so \(\theta^2=-3\). In the ordered rational
coordinates

\[
(u_0,a_1,b_1,\ldots,a_{n-1},b_{n-1},c),
\]

define \(B_n\) by

\[
x_0=u_0,
\quad x_i=a_i+\theta b_i,
\quad x_{N-i}=\rho^{e_i}(a_i-\theta b_i)\ (1\le i<n),
\]

and

\[
x_n=\kappa_nc,\qquad
\kappa_n=\begin{cases}1,&n\text{ odd},\\1+\rho,&n\text{ even}.
\end{cases}
\]

Then

\[
M_n\tau(B_n)=B_n,
\qquad
\det B_n=(2\theta)^{n-1}\rho^{\lfloor(n-1)/2\rfloor}\kappa_n\ne0.
\]

The descended equations are

\[
C_{n,0}=u_0^3+\sum_{i=1}^{n-1}(2a_i^3-18a_ib_i^2)
          +(-1)^{n+1}c^3,
\]

\[
\begin{aligned}
Q_{n,0}={}&u_0(a_1+3b_1)\\
&+\sum_{i=1}^{n-2}
(a_ia_{i+1}+3a_ib_{i+1}+3b_ia_{i+1}-3b_ib_{i+1})+R_n,
\end{aligned}
\]

where

\[
R_n=\begin{cases}
(a_{n-1}+3b_{n-1})c,&n\text{ odd},\\
2a_{n-1}c,&n\text{ even}.
\end{cases}
\]

Direct substitution gives

\[
C_n(B_nu)=C_{n,0}(u),\qquad
Q_{n,\rho}(B_nu)=(1+\rho)Q_{n,0}(u).
\]

Therefore \(X_{n,0}=V(C_{n,0},Q_{n,0})/\mathbf Q\) base-changes to
the frozen source-ordered \(X_n/K\). Theorem A is equation-level and does
not assert smoothness.

For \(n=4\), after renaming
\((u_0,a_1,b_1,a_2,b_2,a_3,b_3,c)=(u_0,\ldots,u_7)\),

\[
\begin{aligned}
C_{4,0}={}&u_0^3+2u_1^3-18u_1u_2^2+2u_3^3-18u_3u_4^2\\
&+2u_5^3-18u_5u_6^2-u_7^3,
\end{aligned}
\]

\[
\begin{aligned}
Q_{4,0}={}&u_0u_1+3u_0u_2+u_1u_3+3u_1u_4+3u_2u_3-3u_2u_4\\
&+u_3u_5+3u_3u_6+3u_4u_5-3u_4u_6+2u_5u_7.
\end{aligned}
\]

Here \(\det B_4=24\theta\).

## 2. Certified rational packets

For the certified smooth rows \(n=2,3,4\), let

\[
\mathsf E_n=\mathbf1\oplus
(S_n,\pi_{\mathrm{prim}},n-1),\qquad
\mathsf O_n=(X_{n,0},\pi_{2n-3},n-2),
\]

and \(\mathsf W_n=\mathsf E_n\oplus\mathsf O_n\).

**Theorem B (rational packet).** These are Chow-motivic packets over
\(\mathbf Q\), their base changes are the C51 packets, and

\[
\operatorname{rank}\mathsf E_n=\frac{4^n+5}{3},\qquad
\operatorname{rank}\mathsf O_n=\frac{2(4^n-4)}3,
\qquad \operatorname{rank}\mathsf W_n=4^n-1.
\]

Thus \(\operatorname{rank}\mathsf W_n=15,63,255\) for \(n=2,3,4\).
For \(n\ge5\), this packet statement is conditional on smoothness and a
C51-type motivic extraction; only Theorem A is unconditional there.

## 3. Split denominator conversion and inert obstruction

Let \(\chi_K\) be the quadratic character of \(K/\mathbf Q\). Away from
a common finite bad set, Artin formalism gives the incomplete identity

\[
L_K(\mathsf W_{n,K},s)=L_{\mathbf Q}(\mathsf W_n,s)
L_{\mathbf Q}(\mathsf W_n\otimes\chi_K,s).
\]

At a good split rational prime \(p\), the two \(K\)-prime factors are
identical, hence

\[
L_{K,p}(\mathsf W_{n,K},u)=L_{\mathbf Q,p}(\mathsf W_n,u)^2.
\]

**Theorem C (split-local repair).** In the origin-normalized Euler
logarithm, the C51 exponent \(2/n\) becomes \(4/n\) on the single rational
factor. Its reduced denominator is \(n/\gcd(n,4)\). Consequently, among the
fractional certified rows,

\[
n=3:\ \frac43,\qquad n=4:\ 1,
\]

and at every good split \(p\),

\[
\boxed{
\left(L_{K,p}(\mathsf W_{4,K},u)\right)^{1/2}_{\operatorname{Log}_0}
=L_{\mathbf Q,p}(\mathsf W_4,u).}
\]

The right side is one ordinary rank-255, exponent-one rational local
factor. This clears the C51 direct-\(K\) obstruction through its explicitly
allowed quadratic Galois counterpacket; it does not create a rank-
\(255/2\) \(K\)-system. For a Tate-normalized packet, “ordinary” refers to
integral rank and local multiplicity, not necessarily coefficients in
\(\mathbf Z\).

At a good inert \(p\), if
\(P_p(U)=\prod_i(1-\alpha_iU)\), then

\[
P_{K,v}(T)=\prod_i(1-\alpha_i^2T),\qquad
P_{K,v}(U^2)=P_p(U)P_p(-U).
\]

This is generally not a square. No inert or global half-root, meromorphic
continuation, or functional equation is claimed.

Every local statement uses geometric Frobenius, normalized by
\(\operatorname{Frob}_p\mid\mathbf Q_\ell(-1)=p\), as in C49--C52.

## 4. The rational rank-10 core

For \(n=4\), the C52 symmetry group is the order-24 group
\(G=\operatorname{Dih}(C_{12})=\langle r,s\mid r^{12}=s^2=1,
srs=r^{-1}\rangle\). Transport by the descent datum is

\[
\delta(r)=r^{-1},\qquad \delta(s)=sr^{-1}=rs,
\]

so

\[
\delta(r^k)=r^{-k},\qquad \delta(r^ks)=r^{1-k}s.
\]

It defines a nonconstant finite étale \(\mathbf Q\)-group scheme
\(\mathscr G\) of rank 24, split by \(K\). The 24 geometric
automorphisms are not asserted to be individual \(\mathbf Q\)-maps.

Let

\[
e_G=\frac1{24}\sum_{g\in G}[\Gamma_g].
\]

The transport above permutes all 24 graphs. If
\(q:(X_{4,0}^2)_K\to X_{4,0}^2\), define

\[
e_{\mathscr G}=\frac12q_*e_G.
\]

Then \(q^*e_{\mathscr G}=e_G\); the identity \(q_*q^*=2\) makes
\(q^*\) injective on Chow groups with rational coefficients. Thus all
projector identities descend. With

\[
\pi_5=\Delta-\sum_{i=0}^5\frac16h^{5-i}\times h^i,
\]

put

\[
\pi_{\mathrm{core},0}=\pi_5e_{\mathscr G},\qquad
\pi_{\mathrm{lev},0}=\pi_5-\pi_5e_{\mathscr G}.
\]

**Theorem D (rational core).** These are mutually orthogonal,
self-transpose rational Chow projectors, and

\[
\mathsf O_4=\mathsf O_{4,\mathrm{core}}
\oplus\mathsf O_{4,\mathrm{lev}},\qquad
\operatorname{rank}=10+158.
\]

Together with the rank-87 even packet, this gives \(87+10+158=255\).
The untwisted core has Hodge numbers

\[
h^{4,1}=h^{1,4}=1,\qquad h^{3,2}=h^{2,3}=4.
\]

After one Tate twist it is of Calabi--Yau-threefold Hodge type. No actual
Calabi--Yau variety, irreducibility, or absence of further Chow projectors
is asserted.

## 5. Arithmetic of the raw core

Write

\[
\mathsf M_0=(X_{4,0},\pi_{\mathrm{core},0},0)
\]

for the untwisted rank-10 rational summand.

**Theorem E (strictly compatible rank-10 polynomial).** There is a finite
set \(S\) such that, for \(p\notin S\) and every \(\ell\ne p\),

\[
P_p(T)=\det\!\left(1-\operatorname{Frob}_pT
\mid H_\ell(\mathsf M_0)\right)
=\sum_{k=0}^{10}a_kT^k
\]

is a degree-10 polynomial in \(\mathbf Z[T]\), independent of \(\ell\).
It is pure of weight 5. The self-transpose projector and Poincaré duality
give

\[
a_{10-k}=p^{25-5k}a_k\qquad(0\le k\le10).
\]

Equivalently,

\[
P_p(T)=p^{25}T^{10}P_p\!\left(\frac1{p^5T}\right).
\]

The twice-twisted realization \(\mathsf M_0(2)\), which is the core inside
the normalized C51 odd packet, has weight 1 and strictly compatible local
polynomials

\[
P_p^{(2)}(T)=P_p(T/p^2)\in\mathbf Q[T].
\]

The polynomial \(P_p^{(2)}\) need not lie in \(\mathbf Z[T]\).

To prove Theorem E, spread the variety and projector outside a finite set.
Correspondence traces make
\(\chi_{p,\mathrm{core}}(U)=\det(U-F_p)\) an element of
\(\mathbf Q[U]\), independent of \(\ell\). The full monic
smooth-projective polynomial \(\chi_{p,H^5}(U)\in\mathbf Z[U]\) factors
as the two monic rational polynomials attached to the projector and its
complement. Their roots are algebraic integers, so Gauss's lemma (or
\(\mathbf Q\cap\overline{\mathbf Z}=\mathbf Z\)) puts both factors in
\(\mathbf Z[U]\). Finally,

\[
P_p(T)=T^{10}\chi_{p,\mathrm{core}}(T^{-1})\in\mathbf Z[T].
\]

Clearing a projector denominator alone is not an integrality proof, and
\(P_p(T)=\det(1-F_pT)\) is not called monic. Purity is inherited from
\(H^5\); reciprocity follows from the nondegenerate restriction of the
degree-five Poincaré pairing.
