# Proof package

## 1. Source object and claim

Let

\[
H_6(q,p)=(1-6q^2-p,q)
\]

be restricted to the four-state survivor certified in HCS-P31 and used in
HCS-P43--P52.  For a primitive orbit \(\gamma\), write

\[
m(\gamma)=m,\qquad
\Lambda_\gamma=|\lambda_\gamma|>1,\qquad
t_\gamma=\lambda_\gamma+\lambda_\gamma^{-1},
\]

and put \(F_\gamma=\mathbb Q(t_\gamma)\).  HCS-P49 gives, for every
\(n>2\),

\[
\beta_{\gamma,n}
=\lambda_\gamma^{-\varphi(n)/2}\Phi_n(\lambda_\gamma)
\in\mathcal O_{F_\gamma}.
\tag{1.1}
\]

Its source-tagged effective divisor is \(D_{\gamma,n}\), and HCS-P51 proves

\[
b_{\gamma,n}:=\|D_{\gamma,n}\|_{\rm tag}
=\log\left|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}\right|.
\tag{1.2}
\]

Let \(f_\gamma\) be the monic minimal polynomial of
\(\lambda_\gamma\), and define the **Mahler spectral height**

\[
\mathcal H_\gamma=\log M(f_\gamma).
\tag{1.3}
\]

If \(h_*\) is the certified pressure root, set

\[
\widehat\ell_\gamma=h_*\log\Lambda_\gamma,
\qquad
\sigma_0=\frac{\log(2\phi)}{h_*\log J_*},
\qquad
J_*=\frac{\sqrt{17}+\sqrt{13}}2.
\tag{1.4}
\]

The main theorem is the locally uniform boundary exchange

\[
\boxed{
\lim_{\tau\downarrow0}\tau^2
\sum_{\gamma\ {m primitive}}e^{-s\widehat\ell_\gamma}
\sum_{n\ge3}b_{\gamma,n}e^{-\tau n}
=\frac3{\pi^2}
\sum_{\gamma\ {m primitive}}e^{-s\widehat\ell_\gamma}
\mathcal H_\gamma}
\tag{1.5}
\]

for \(\Re s>\sigma_0\).  This is the all-orbit theorem left open by
HCS-P52.  It is a scalar mass theorem in the already certified P51
half-plane, not a pressure-critical continuation theorem.

## 2. Reciprocal embeddings and the correct height

Put \(K_\gamma=\mathbb Q(\lambda_\gamma)\).  Inversion is a nontrivial
automorphism of \(K_\gamma\) and its fixed field is \(F_\gamma\).  Hence
every embedding \(\sigma:F_\gamma\hookrightarrow\mathbb C\) has two
extensions to \(K_\gamma\), sending \(\lambda_\gamma\) to the reciprocal
roots of

\[
X^2-\sigma(t_\gamma)X+1.
\]

Choose one root \(\rho_\sigma\) with \(|\rho_\sigma|\ge1\).  Then

\[
\mathcal H_\gamma
=\sum_{\sigma:F_\gamma\hookrightarrow\mathbb C}
\log|\rho_\sigma|.
\tag{2.1}
\]

Indeed, the conjugates of the algebraic unit \(\lambda_\gamma\) occur in
the pairs \(\rho_\sigma,\rho_\sigma^{-1}\).  The product of
\(\max(1,|z|)\) over such a pair is \(|\rho_\sigma|\), proving (2.1) from
the definition of Mahler measure.  The physical real embedding contributes
\(\log\Lambda_\gamma\), so

\[
\mathcal H_\gamma\ge\log\Lambda_\gamma>0.
\tag{2.2}
\]

This distinction matters.  In general \(\mathcal H_\gamma\) is not merely
\(\log\Lambda_\gamma\); nonphysical conjugate pairs outside the unit circle
also contribute.

No \(\rho_\sigma\) is a root of unity.  Otherwise a conjugate of
\(\lambda_\gamma\) would be a root of unity, so the irreducible minimal
polynomial of \(\lambda_\gamma\) would be cyclotomic, contradicting
\(|\lambda_\gamma|>1\).

## 3. One-orbit spectral-height asymptotic

Cyclotomic reciprocity supplies a polynomial \(q_n\in\mathbb Z[T]\) such
that

\[
q_n(X+X^{-1})=X^{-\varphi(n)/2}\Phi_n(X),
\qquad n>2.
\tag{3.1}
\]

Thus \(\beta_{\gamma,n}=q_n(t_\gamma)\).  Taking logarithms of the
cyclotomic Möbius product gives, for every embedding \(\sigma\),

\[
\log|\sigma(\beta_{\gamma,n})|
=-\frac{\varphi(n)}2\log|\rho_\sigma|
+\sum_{d\mid n}\mu(n/d)\log|\rho_\sigma^d-1|.
\tag{3.2}
\]

### 3.1. Conjugates off the unit circle

If \(|\rho_\sigma|>1\), then

\[
\log|\rho_\sigma^d-1|
=d\log|\rho_\sigma|+\log|1-\rho_\sigma^{-d}|.
\]

Since \(\sum_{d\mid n}\mu(n/d)d=\varphi(n)\), equation (3.2) becomes

\[
\log|\sigma(\beta_{\gamma,n})|
=\frac{\varphi(n)}2\log|\rho_\sigma|
+\epsilon_{\sigma,n},
\tag{3.3}
\]

where

\[
\epsilon_{\sigma,n}
=\sum_{d\mid n}\mu(n/d)\log|1-\rho_\sigma^{-d}|.
\]

The geometric series

\[
\sum_{d\ge1}-\log(1-|\rho_\sigma|^{-d})
\]

converges.  Therefore \(|\epsilon_{\sigma,n}|\le C_\sigma\) uniformly in
\(n\).

### 3.2. Conjugates on the unit circle

Suppose \(|\rho_\sigma|=1\).  Theorem 1.2 and its consequence (15) in
Yamada's two-logarithm estimate imply that, because
\(\rho_\sigma\) is algebraic and not a root of unity, there is a constant
\(C_\sigma>0\) such that

\[
|\log|1-\rho_\sigma^d||
\le C_\sigma(1+\log d)^2
\qquad(d\ge1).
\tag{3.4}
\]

To pass from Yamada's argument bound to (3.4), take the principal argument
\(\theta_d=\arg(\rho_\sigma^d)\in[-\pi,\pi]\) and use

\[
\frac{2}{\pi}|\theta_d|
\le |1-e^{i\theta_d}|\le2.
\]

The elementary divisor bound \(\tau(n)\le2\sqrt n\) now gives

\[
\left|
\sum_{d\mid n}\mu(n/d)\log|1-\rho_\sigma^d|
\right|
\le 2C_\sigma\sqrt n(1+\log n)^2.
\tag{3.5}
\]

There is no height main term in this case because
\(\log|\rho_\sigma|=0\).

### Theorem 3.1 (one-orbit Mahler-height law)

For every primitive orbit \(\gamma\),

\[
b_{\gamma,n}
=\frac{\varphi(n)}2\mathcal H_\gamma
+R_{\gamma,n},
\qquad
|R_{\gamma,n}|
\le C_\gamma\sqrt n(1+\log n)^2.
\tag{3.6}
\]

#### Proof

Sum (3.3) and (3.5) over the finitely many embeddings of
\(F_\gamma\).  The leading terms sum to (2.1), while all remainders can be
absorbed in one orbit-dependent constant.  Equation (1.2) is the sum of the
embedding logarithms, proving (3.6). \(\square\)

The source theorem is used only for the possible unit-circle conjugates.
The three finite H6 sentinels have none; the separate reciprocal Salem
fixture in the certificate has two and prevents the proof from silently
assuming hyperbolicity at every algebraic embedding.

## 4. One-orbit Abel limit

HCS-P52 proves the totient Laplace law

\[
\lim_{\tau\downarrow0}\tau^2
\sum_{n\ge1}\varphi(n)e^{-\tau n}=\frac6{\pi^2}.
\tag{4.1}
\]

The error in (3.6) is negligible at this scale, because integral comparison
gives

\[
\tau^2\sum_{n\ge3}\sqrt n(1+\log n)^2e^{-\tau n}
=O\!\left(\tau^{1/2}(1+|\log\tau|)^2\right)=o(1).
\tag{4.2}
\]

Consequently:

### Corollary 4.1 (one-orbit Abel coefficient)

For every primitive orbit \(\gamma\),

\[
\lim_{\tau\downarrow0}\tau^2
\sum_{n\ge3}b_{\gamma,n}e^{-\tau n}
=\frac3{\pi^2}\mathcal H_\gamma.
\tag{4.3}
\]

The factor \(3\), rather than \(6\), is forced by the half-cyclotomic
normalization in (1.1).

## 5. Pressure-uniform domination

For a period-\(m\) orbit, HCS-P51 proves the uniform source bound

\[
0\le b_{\gamma,n}
\le K_m n,
\qquad
K_m=2^m\left(a+bm\right),
\tag{5.1}
\]

with

\[
a=\log(2\sqrt3),
\qquad
b=\frac12\log(3+2\sqrt7).
\]

For \(0<\tau\le1\),

\[
\tau^2\sum_{n\ge3}ne^{-\tau n}
\le\tau^2\frac{e^{-\tau}}{(1-e^{-\tau})^2}\le4.
\tag{5.2}
\]

Hence the normalized contribution of one period-\(m\) orbit is at most
\(4K_m\), uniformly as \(\tau\downarrow0\).

The P51 symbolic census and expansion bound give

\[
\#\{\gamma:m(\gamma)=m\}\le3\phi^m,
\qquad
\widehat\ell_\gamma\ge h_*m\log J_*.
\tag{5.3}
\]

For every \(\sigma>\sigma_0\), equations (5.1)--(5.3) yield the summable
majorant

\[
12\sum_{m\ge1}(a+bm)
\left(2\phi e^{-\sigma h_*\log J_*}\right)^m<\infty.
\tag{5.4}
\]

This is the missing pressure-uniform domination.  It uses the same safe
half-plane as P51 and no orbit-dependent remainder constant from (3.6).

## 6. The all-orbit scalar boundary

Let \(\mathfrak m:\mathcal B_{\rm tag}\to\mathbb C\) be the norm-one
mass functional which assigns to every weighted basis atom its
residue-degree logarithmic mass.  For \(\tau>0\), define

\[
Z(s,\tau)
=\mathfrak m\bigl(\mathcal G(s,e^{-\tau})\bigr)
=\sum_\gamma e^{-s\widehat\ell_\gamma}
\sum_{n\ge3}b_{\gamma,n}e^{-\tau n}.
\tag{6.1}
\]

### Theorem 6.1 (pressure-weighted all-orbit Abel law)

For \(\Re s>\sigma_0\),

\[
\tau^2Z(s,\tau)\longrightarrow
\mathcal A(s):=rac3{\pi^2}
\sum_\gamma e^{-s\widehat\ell_\gamma}\mathcal H_\gamma
\tag{6.2}
\]

locally uniformly in \(s\).  The series defining \(\mathcal A\) converges
normally and \(\mathcal A\) is holomorphic in that half-plane.  Equivalently,
for real \(0<u<1\),

\[
(1-u)^2\mathfrak m(\mathcal G(s,u))\longrightarrow\mathcal A(s).
\tag{6.3}
\]

#### Proof

Corollary 4.1 gives the limit orbit by orbit, while (5.4) is a summable
majorant.  Dominated convergence proves (6.2) pointwise.  On a compact
subset of the half-plane, use the leftmost real part in (5.4).  First choose
a period cutoff making the majorant tail uniformly small, then apply the
finite-orbit convergence; this proves local uniformity.

The limit in Corollary 4.1 and (5.2) also bound
\(\mathcal H_\gamma\) by a constant multiple of \(K_m\), so the series for
\(\mathcal A\) has the same normal majorant.  Holomorphy follows from the
Weierstrass theorem.  Finally,
\((1-e^{-\tau})/\tau\to1\), proving (6.3). \(\square\)

Using the source-locked lower bound \(h_*\ge0.277980\), the fully numerical
safe domain remains

\[
\Re s>3.125206884004728\ldots .
\tag{6.4}
\]

No statement at equality or at a thermodynamic pressure singularity is
included.

## 7. Joint orbit--index boundary law

Fix real \(\sigma>\sigma_0\), and put

\[
S_{\mathcal H}(\sigma)
=\sum_\gamma e^{-\sigma\widehat\ell_\gamma}\mathcal H_\gamma.
\tag{7.1}
\]

It is finite and positive.  Define a probability on primitive orbits by

\[
\pi_\sigma(\gamma)
=\frac{e^{-\sigma\widehat\ell_\gamma}\mathcal H_\gamma}
{S_{\mathcal H}(\sigma)}
\tag{7.2}
\]

and a probability on the orbit--scaled-index space by

\[
\nu_{\sigma,\tau}
=\frac1{Z(\sigma,\tau)}
\sum_{\gamma}\sum_{n\ge3}
e^{-\sigma\widehat\ell_\gamma}b_{\gamma,n}e^{-\tau n}
\delta_{(\gamma,\tau n)}.
\tag{7.3}
\]

### Theorem 7.1 (product boundary profile)

As \(\tau\downarrow0\),

\[
\nu_{\sigma,\tau}
\Longrightarrow
\pi_\sigma\otimes\Gamma(2,1),
\tag{7.4}
\]

where \(\Gamma(2,1)\) has density \(xe^{-x}\mathbf1_{x\ge0}\,dx\).
Equivalently, for every bounded function \(F\) on the countable primitive
orbit set and every \(r\ge0\),

\[
\lim_{\tau\downarrow0}
\int F(\gamma)e^{-rx}\,d\nu_{\sigma,\tau}(\gamma,x)
=\frac1{(1+r)^2}\sum_\gamma\pi_\sigma(\gamma)F(\gamma).
\tag{7.5}
\]

#### Proof

Apply Theorem 6.1 at \((1+r)\tau\) to the numerator of (7.5), with the
bounded factor \(F(\gamma)\) inserted.  The same majorant (5.4) applies.
After multiplying numerator and denominator by \(\tau^2\), their ratio
tends to the right side of (7.5).

Tightness in the orbit coordinate follows by choosing a finite period tail
in (5.4).  Tightness in the scaled-index coordinate follows from (5.1) and
the elementary tail bound

\[
\tau^2\sum_{\tau n\ge R}ne^{-\tau n}
\ll(R+1)e^{-R}.
\]

The mixed transforms in (7.5) determine the product probability, proving
(7.4). \(\square\)

Thus the Gamma profile found on the period-four orbit in P52 survives the
all-orbit pressure sum.  The new orbit marginal is the pressure-weighted
Mahler-height law (7.2).

## 8. The tagged vector still has no boundary

For real \(\sigma>\sigma_0\), define

\[
E_{\sigma,\tau}
=\tau^2\sum_{\gamma}\sum_{n\ge3}
e^{-\sigma\widehat\ell_\gamma}e^{-\tau n}D_{\gamma,n}
\in\mathcal B_{\rm tag}.
\tag{8.1}
\]

All coefficients are positive, so Theorem 6.1 gives

\[
\|E_{\sigma,\tau}\|_{\rm tag}
=\mathfrak m(E_{\sigma,\tau})
=\tau^2Z(\sigma,\tau)
\longrightarrow\frac3{\pi^2}S_{\mathcal H}(\sigma)>0.
\tag{8.2}
\]

### Theorem 8.1 (all-orbit tagged-mass escape)

The family \(E_{\sigma,\tau}\), \(0<\tau<1\), has no norm-convergent
subnet and no weakly convergent subnet as \(\tau\downarrow0\).

#### Proof

Every fixed coordinate \((\gamma,n,\mathfrak q)\) has coefficient
\(O(\tau^2e^{-\tau n})\), hence tends to zero.  Any norm limit would
therefore be zero, contradicting (8.2).  Any weak limit is also forced to
have every coordinate zero, while the bounded functional \(\mathfrak m\)
has the nonzero limit in (8.2).  The same argument applies to every subnet.
\(\square\)

The scalar and probability boundaries are therefore genuine quotients of
escaping source-tagged mass; they are not vector-valued divisor boundaries.

## 9. Finite certificate and adversarial checks

The producer and independent checker certify:

1. exact half-cyclotomic trace polynomials and exact trace-field norms for
   the inherited primitive periods \(1,3,4\);
2. the Mahler spectral heights
   \(3.0501161905\ldots\), \(8.9056092910\ldots\), and
   \(6.3595708754\ldots\);
3. four finite Abel rows for each orbit and a pressure-weighted three-orbit
   joint Gamma profile;
4. a non-H6 reciprocal Salem stress polynomial with two unit-circle
   conjugates;
5. rejection of the physical-multiplier-only height, the doubled Abel
   constant, a shape-one Gamma law, and all determinant/operator promotions.

The finite sample does not enumerate all primitive orbits and is not used to
prove dominated convergence.

## 10. Claim ceiling and next theorem

### Proved

1. the one-orbit Mahler-height packet asymptotic;
2. pressure-weighted all-orbit Abel interchange in the P51 safe half-plane;
3. local uniformity and holomorphy of the scalar boundary amplitude;
4. the joint pressure-height orbit law times \(\Gamma(2,1)\);
5. failure of norm and weak tagged-vector boundaries.

### Open

1. continuation of \(\mathcal A(s)\) toward a pressure-critical boundary;
2. a pressure pole, residue, or thermodynamic trace interpretation of
   \(S_{\mathcal H}(s)\);
3. a rational-prime von Mangoldt law retaining the prime-ideal source tags;
4. a Fredholm determinant or functional equation;
5. a Hilbert--P\'olya operator.

The next smallest non-micro problem is to treat

\[
\sum_\gamma e^{-s\widehat\ell_\gamma}\mathcal H_\gamma
\]

as a thermodynamic observable and determine whether it has a pressure-side
singularity or continuation.  P53 supplies its exact arithmetic coefficient
but no such continuation theorem.
