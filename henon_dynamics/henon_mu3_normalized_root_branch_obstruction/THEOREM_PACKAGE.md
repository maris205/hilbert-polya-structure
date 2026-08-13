# HCS-C46 theorem package

## 1. Exact \(p=7\) sectors

Let \(\zeta=\zeta_7\), \(\rho=2\), and let \(T=U_7^2\).  Write

\[
D_k(z)=\det(I-zT\mid H_k),
\]

for the three eigenspaces of the order-three permutation.  Exact cyclotomic
arithmetic gives \(D_2=D_1\) and explicit \(D_0,D_1\); no numerical
eigenvalues enter.

Put \(\theta=\zeta+\zeta^{-1}\), whose minimal polynomial is

\[
m(\theta)=\theta^3+\theta^2-2\theta-1. \tag{1}
\]

Define the real paired sector polynomials

\[
q_0(\theta,z)=D_0(z)\overline{D_0(z)},
\qquad
q_1(\theta,z)=D_1(z)\overline{D_1(z)}. \tag{2}
\]

In \(\mathbf Q[\theta,z]/(m)\), they are

\[
\begin{aligned}
7q_0={}&-15\theta^2z^5-26\theta^2z^4-26\theta^2z^3
-26\theta^2z^2-15\theta^2z\\
&-3\theta z^5-10\theta z^4-19\theta z^3-10\theta z^2-3\theta z\\
&+7z^6+31z^5+61z^4+72z^3+61z^2+31z+7,\\
7q_1={}&4\theta^2z^2+5\theta z^2+7z^4-12z^2+7.
\end{aligned} \tag{3}
\]

The C43 augmentation is \((D_0/D_1)^2\), so its conjugate-paired factor is
\((q_0/q_1)^2\).

## 2. Exact rational norm

Because \(m\) is monic, the field norm is the resultant in \(\theta\).
Direct elimination yields

\[
\operatorname{Res}_{\theta}(m,q_0)=\frac{P_{18}}{49},
\qquad
\operatorname{Res}_{\theta}(m,q_1)=\frac{P_{12}}7, \tag{4}
\]

where

\[
\begin{aligned}
P_{18}(z)={}&49z^{18}+147z^{17}+147z^{16}-14z^{15}-133z^{14}
-63z^{13}+71z^{12}\\
&+104z^{11}+50z^{10}+13z^9+50z^8+104z^7+71z^6\\
&-63z^5-133z^4-14z^3+147z^2+147z+49,
\end{aligned} \tag{5}
\]

and

\[
P_{12}(z)=7z^{12}-21z^{10}+35z^8-41z^6+35z^4-21z^2+7. \tag{6}
\]

Therefore

\[
\boxed{N_7(z)=\frac{P_{18}(z)^2}{49P_{12}(z)^2}},
\qquad N_7(0)=1. \tag{7}
\]

Its numerator and denominator degrees are \(36\) and \(24\), giving the C45
virtual difference \(12=2(7-1)\).

## 3. Squarefree and coprime certificate

Reduction modulo five preserves the displayed degrees.  The Euclidean
algorithm gives

\[
\gcd(P_{18},P_{12})
=\gcd(P_{18},P_{18}')
=\gcd(P_{12},P_{12}')=1
\quad\text{in }\mathbf F_5[z]. \tag{8}
\]

Hence the same gcds are one over \(\mathbf Q\).  The polynomials are mutually
coprime and squarefree.  Every zero of \(N_7\) has order \(+2\), and every
pole has order \(-2\).

## 4. Non-cube and branch theorem

### Theorem 4.1

The rational function \(N_7\) is not a cube in \(\mathbf C(z)\), hence not in
\(\mathbf Q(z)\).  The origin branch

\[
G_7(z)=\exp\!\left(\frac13\Log_0N_7(z)\right)
\]

has local order \(+2/3\) at every zero and \(-2/3\) at every pole of
\(N_7\).  It cannot extend through any such point as a single-valued
meromorphic scalar function.

Proof.  Every divisor valuation of a cube is divisible by three, whereas (8)
shows that the valuations of \(N_7\) are \(\pm2\).  A single-valued
meromorphic function has integral local order.

All these divisor points lie on \(|z|=1\), because the factors arise from
characteristic polynomials of unitary sector operators and their Galois
conjugates.  Equation (8) excludes cancellation between the two sectors.

## 5. Consequences and scope

The theorem rules out:

- an ordinary rational finite-dimensional determinant ratio for \(G_7\);
- meromorphic crossing of its local divisor by the scalar origin branch;
- promotion of every C45 local root to an ordinary determinant family.

It does not rule out:

- the C45 germ on \(|z|<1\) and \(\Re s>1/2\);
- a determinant associated with a normalized trace in a finite or semifinite
  operator algebra;
- an infinite-dimensional holomorphic realization confined to the half-plane;
- global cancellation after an independently derived construction;
- or a different Hénon dynamics.

No global natural-boundary theorem is claimed.

