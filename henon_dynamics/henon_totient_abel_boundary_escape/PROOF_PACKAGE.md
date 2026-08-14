# Proof package

## 1. Exact source packet

Fix the HCS-P51 primitive period-four orbit.  Its signed unstable multiplier
is positive and equals

\[
L=289+24\sqrt{145}>1,
\qquad L+L^{-1}=578,
\qquad N_{\mathbb Q(\sqrt{145})/\mathbb Q}(L)=1.
\tag{1.1}
\]

For every \(n\ge3\), define

\[
\beta_n=L^{-\varphi(n)/2}\Phi_n(L).
\tag{1.2}
\]

Cyclotomic reciprocity makes (1.2) a polynomial in
\(T=L+L^{-1}=578\), hence \(\beta_n\in\mathbb Z\).  Pairing conjugate roots
of \(\Phi_n\) shows \(\beta_n>0\).  Let

\[
D_n=\operatorname{Div}_{\mathbb Q}(\beta_n)
=\sum_p v_p(\beta_n)[\gamma_4,n,p]
\tag{1.3}
\]

in the HCS-P51 source-tagged space.  Its weighted norm is exactly

\[
b_n:=\|D_n\|_{\rm tag}=\log\beta_n.
\tag{1.4}
\]

The tags include \(n\), so the supports of \(D_n\) and \(D_m\) are disjoint
when \(n\ne m\).

## 2. Uniform totient packet formula

### Theorem 2.1

For every \(n\ge3\),

\[
b_n=\frac{\varphi(n)}2\log L+\varepsilon_n,
\qquad
\varepsilon_n=
\sum_{d\mid n}\mu(n/d)\log(1-L^{-d}).
\tag{2.1}
\]

Moreover

\[
|\varepsilon_n|\le
C_L:=\sum_{d\ge1}-\log(1-L^{-d})<\infty.
\tag{2.2}
\]

For the frozen multiplier, the executable bound is

\[
C_L<0.001735.
\tag{2.3}
\]

#### Proof

For \(n>1\), cyclotomic Möbius inversion gives

\[
\Phi_n(L)=\prod_{d\mid n}(L^d-1)^{\mu(n/d)}.
\]

Since \(L^d-1=L^d(1-L^{-d})\) and
\(\sum_{d\mid n}\mu(n/d)d=\varphi(n)\), taking real logarithms in
(1.2) proves (2.1).  The signs of the Möbius coefficients and the inclusion
of divisors in the positive integers give

\[
|\varepsilon_n|
\le\sum_{d\mid n}|\log(1-L^{-d})|
\le C_L.
\]

Finally \(-\log(1-x)\le x/(1-x)\) for \(0<x<1\), so the series defining
\(C_L\) is bounded by a convergent geometric tail.  Direct interval-safe
evaluation of the first 32 terms plus this tail gives (2.3). \(\square\)

## 3. The elementary totient average

### Lemma 3.1

As \(x\to\infty\),

\[
S_\varphi(x):=\sum_{n\le x}\varphi(n)
=\frac{3}{\pi^2}x^2+O(x\log(2x)).
\tag{3.1}
\]

#### Proof

The identity

\[
\varphi(n)=n\sum_{d\mid n}\frac{\mu(d)}d
\]

gives

\[
S_\varphi(x)
=\sum_{d\le x}\mu(d)\sum_{m\le x/d}m
=\frac12\sum_{d\le x}\mu(d)
\left(\lfloor x/d\rfloor^2+\lfloor x/d\rfloor\right).
\]

Replacing the floors costs \(O(x\sum_{d\le x}d^{-1})\), hence

\[
S_\varphi(x)=\frac{x^2}{2}
\sum_{d\le x}\frac{\mu(d)}{d^2}+O(x\log(2x)).
\]

The omitted tail of the absolutely convergent series is \(O(x^{-1})\),
and \(\sum_{d\ge1}\mu(d)d^{-2}=1/\zeta(2)=6/\pi^2\).  This proves
(3.1). \(\square\)

### Corollary 3.2

For \(\tau\downarrow0\),

\[
\sum_{n\ge1}\varphi(n)e^{-\tau n}
=\frac{6}{\pi^2\tau^2}
+O\!\left(\frac{\log(2/\tau)}{\tau}\right).
\tag{3.2}
\]

#### Proof

Stieltjes summation and (3.1) give

\[
\sum_{n\ge1}\varphi(n)e^{-\tau n}
=\tau\int_0^\infty S_\varphi(x)e^{-\tau x}\,dx.
\]

The main integral is
\(\tau(3/\pi^2)\int_0^\infty x^2e^{-\tau x}dx
=6/(\pi^2\tau^2)\).  Scaling \(y=\tau x\) bounds the error by the
quantity in (3.2). \(\square\)

## 4. Scalar Abel law

Put

\[
Z(\tau)=\sum_{n\ge3}b_ne^{-\tau n},
\qquad \tau>0.
\tag{4.1}
\]

### Theorem 4.1 (totient Abel boundary)

As \(\tau\downarrow0\),

\[
Z(\tau)=
\frac{3\log L}{\pi^2\tau^2}
+O_L\!\left(\frac{\log(2/\tau)}{\tau}\right).
\tag{4.2}
\]

Consequently, with \(u=e^{-\tau}\),

\[
\boxed{
\lim_{u\uparrow1}(1-u)^2
\sum_{n\ge3}\|D_n\|_{\rm tag}u^n
=\frac{3\log L}{\pi^2}}
\tag{4.3}
\]

and numerically

\[
\frac{3\log L}{\pi^2}
=1.9330777456585248\ldots .
\tag{4.4}
\]

#### Proof

Insert (2.1) into (4.1).  Corollary 3.2 gives the leading term and error.
The uniformly bounded correction contributes at most
\(C_L\sum_{n\ge3}e^{-\tau n}=O_L(\tau^{-1})\).  This proves (4.2).
Since \((1-e^{-\tau})/\tau\to1\), (4.3) follows. \(\square\)

The power two and the factor one half in (2.1) are forced.  Replacing
\((1-u)^2\) by \((1-u)\), or replacing \(3\log L/\pi^2\) by
\(6\log L/\pi^2\), gives a false statement.

## 5. A canonical blown-up boundary profile

Define the probability measure on \([0,\infty)\)

\[
\mu_\tau=
\frac1{Z(\tau)}
\sum_{n\ge3}b_ne^{-\tau n}\delta_{\tau n}.
\tag{5.1}
\]

### Theorem 5.1 (Gamma escape profile)

As \(\tau\downarrow0\),

\[
\mu_\tau\Longrightarrow \Gamma(2,1),
\tag{5.2}
\]

where the limit has density \(xe^{-x}\mathbf1_{x\ge0}\,dx\).

#### Proof

For every \(s\ge0\), the Laplace transform of (5.1) is

\[
\int e^{-sx}\,d\mu_\tau(x)
=\frac{Z((1+s)\tau)}{Z(\tau)}.
\tag{5.3}
\]

Theorem 4.1 makes the ratio tend to \((1+s)^{-2}\), the Laplace
transform of the claimed Gamma law.  Tightness can be checked without any
black-box Tauberian input: Theorem 2.1 gives \(b_n\le c_Ln+C_L\), so the
mass with \(\tau n\ge R\) is bounded, after division by
\(Z(\tau)\asymp\tau^{-2}\), by a constant multiple of
\((R+1)e^{-R}\), uniformly for small \(\tau\).  Every subsequential weak
limit therefore has Laplace transform \((1+s)^{-2}\); uniqueness of
Laplace transforms proves (5.2). \(\square\)

This profile keeps the cyclotomic grading after blowing up the boundary.
It is not a prime-label law and does not reconstruct the individual divisor
atoms.

## 6. Escape from the original tagged Banach space

In the fixed-orbit tagged subspace define

\[
E_\tau=\tau^2\sum_{n\ge3}e^{-\tau n}D_n.
\tag{6.1}
\]

Every term is positive and different \(n\)'s have disjoint source tags.
Therefore Theorem 4.1 gives

\[
\|E_\tau\|_{\rm tag}
=\tau^2Z(\tau)
\longrightarrow A_L:=\frac{3\log L}{\pi^2}>0.
\tag{6.2}
\]

### Theorem 6.1 (no tagged-vector boundary)

The family \(\{E_\tau:0<\tau<1\}\) has no norm-convergent subnet and no
weakly convergent subnet in the original weighted tagged \(\ell^1\) space.

#### Proof

For each fixed tagged coordinate \((\gamma_4,n,p)\), its coefficient in
\(E_\tau\) is
\(\tau^2e^{-\tau n}v_p(\beta_n)\), which tends to zero.  Any norm limit
would therefore have every coordinate zero and hence would be the zero
vector, contradicting (6.2).

For weak convergence the same coordinate functionals again force any weak
limit to be zero.  On the other hand, the norm-one positive mass functional

\[
\mathfrak m\!\left(\sum c_{n,p}[\gamma_4,n,p]\right)
=\sum c_{n,p}\log p
\]

satisfies \(\mathfrak m(E_\tau)=\|E_\tau\|_{\rm tag}\to A_L\), another
contradiction.  The argument applies to every subnet. \(\square\)

Thus scalarization has not magically produced a lossless divisor boundary.
Mass escapes to indices \(n\asymp\tau^{-1}\), and the Gamma profile is the
correct compactification of that escape at the level of total packet mass.

## 7. What is and is not closed

### Proved

1. exact uniform totient asymptotics for the period-four packet mass;
2. the scalar Abel constant \(3\log L/\pi^2\);
3. the \(\Gamma(2,1)\) scaled-index escape profile;
4. nonexistence of a norm or weak limit in the original tagged space.

### Still open

1. interchange of the Abel boundary with the P51 pressure-weighted all-orbit
   sum;
2. a boundary topology retaining the individual prime-ideal atoms;
3. a von-Mangoldt trace law;
4. analytic continuation or a Fredholm determinant;
5. a Hilbert--Pólya operator.

The next large theorem should globalize (4.3)--(5.2) across primitive orbits
with a pressure-uniform remainder.  It should not assume that the scalar
Gamma profile is an operator determinant.
