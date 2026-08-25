# C141 theorem package

## Theorem (quadratic inverse-branch trace package)

Let \(F(z)=z^2-6\), let \(\mathbb D_4=\{|z|<4\}\), and use the principal square root on \(D(6,4)\) to define \(\psi_\pm(z)=\pm\sqrt{z+6}\). On \(H^2(\mathbb D_4)\), set

\[
(\mathcal L_m f)(z)=\sum_{\epsilon=\pm}(\psi_\epsilon'(z))^m f(\psi_\epsilon(z)),\qquad m=0,1,2.
\]

Then:

1. **Strict geometry and trace class.** Each branch maps \(\overline{\mathbb D}_4\) into \(\{|z|\le\sqrt{10}\}\), the two images lie in \(\{\Re z\ge\sqrt2\}\) and \(\{\Re z\le-\sqrt2\}\), and \(|\psi_\epsilon'|\le q=1/(2\sqrt2)\). In particular \(\mathcal L_2\) is trace class and
   \[
   \|\mathcal L_2\|_1\le
   2\frac{1/8}{1-\sqrt{10}/4}=\frac1{4-\sqrt{10}}.
   \]

2. **All-period exhaustion.** Every root of \(F^n(z)-z\) lies in \(\mathbb D_4\), is simple, and is the unique fixed point of exactly one rooted inverse word of length \(n\). Consequently there are \(2^n\) rooted periodic points and
   \[
   P_n=\frac1n\sum_{d\mid n}\mu(d)2^{n/d}
   \]
   primitive forward orbits of exact period \(n\).

3. **Weighted trace identity.** If \(\Lambda_n(p)=(F^n)'(p)\), then for every \(n\ge1\),
   \[
   \operatorname{Tr}\mathcal L_m^n
   =\sum_{F^n(p)=p}\frac{\Lambda_n(p)^{-m}}{1-\Lambda_n(p)^{-1}}.
   \]
   Thus
   \[
   \operatorname{Tr}\mathcal L_2^n
   =\sum_{F^n(p)=p}\frac1{\Lambda_n(p)(\Lambda_n(p)-1)}.
   \]

4. **Control ladder.** For every \(n\ge1\),
   \[
   \operatorname{Tr}\mathcal L_0^n=2^n,
   \qquad \operatorname{Tr}\mathcal L_1^n=0,
   \]
   so \(\det(I-u\mathcal L_0)=1-2u\) and \(\det(I-u\mathcal L_1)=1\). Hence \(m=2\) is the first member of this frozen ladder retaining nontrivial multiplier data.

5. **Primitive stability product.** The Fredholm determinant \(D_2(u)=\det(I-u\mathcal L_2)\) is entire. In the proved raw-product domain \(|u|<4\),
   \[
   D_2(u)=\prod_{[p]\ \mathrm{primitive}}\prod_{k=2}^{\infty}
   \left(1-u^{\ell(p)}\Lambda_p^{-k}\right),
   \]
   and this product is absolutely convergent. No raw-product convergence is asserted outside \(|u|<4\).

## Proof

For \(z\in\overline{\mathbb D}_4\), \(|z+6|\le10\) and \(|z+6|\ge2\). The principal square-root formula gives the real-part bounds and \(|\psi_\epsilon'|=1/(2|z+6|^{1/2})\le q\). With \(e_j(z)=(z/4)^j\),

\[
M_{(\psi_\epsilon')^2}C_{\psi_\epsilon}
=\sum_{j\ge0}
\big[(\psi_\epsilon')^2(\psi_\epsilon/4)^j\big]\otimes e_j^*.
\]

The coefficient functional has norm one and the vector has Hardy norm at most \((1/8)(\sqrt{10}/4)^j\). Summation proves item 1.

If \(|z|>3\), then \(|F(z)|\ge |z|^2-6>|z|\); hence a periodic point has \(|z|\le3\). Each length-\(n\) inverse word is a \(q^n\)-contraction of the closed owner disk into its interior, so it has one fixed point. A periodic point selects a unique sign at each inverse step. This gives all \(2^n\) roots, and their inverse multipliers have modulus below one, so the roots are simple. Möbius inversion gives item 2.

For a strict disk self-map \(\phi\), weight \(g\), and fixed point \(p\), conjugating \(p\) to zero makes the weighted composition matrix triangular with diagonal \(g(p)\phi'(p)^j\). Its nuclear trace is therefore \(g(p)/(1-\phi'(p))\). Expanding \(\mathcal L_m^n\) over words and applying the chain rule gives item 3.

Write \(P_n=F^n-z\). It is monic of degree \(2^n\), \(P_n'(p)=\Lambda_n(p)-1\), and Lagrange interpolation gives \(\sum_{P_n(p)=0}1/P_n'(p)=0\). Substituting in item 3 proves item 4.

Finally put \(\mu_p=\Lambda_p^{-1}\) for a primitive orbit. Regroup the absolutely convergent trace logarithm and use
\[
\frac{\mu_p^{2r}}{1-\mu_p^r}=\sum_{k\ge2}\mu_p^{kr}.
\]
The start \(k=2\) is forced by the weight. Since there are at most \(2^n/n\) primitive length-\(n\) orbits and \(|\mu_p|\le q^n\), the sum of absolute values of the factor deviations has majorant
\[
\sum_{n\ge1}\frac{|u|^n4^{-n}}{n(1-q^n)},
\]
which converges locally uniformly for \(|u|<4\). The product agrees with the
Fredholm determinant near zero and therefore on that disk by the identity
theorem. Trace class makes the Fredholm determinant entire, independently of
the smaller raw-product domain.

## Exact prefix

For \(n=1,\ldots,6\), the primitive counts are \(2,1,2,3,6,9\), and

\[
\operatorname{Tr}\mathcal L_2^n=
\left(\frac1{12},\frac7{720},\frac{239}{257472},
\frac{1255703}{13810694400},
\frac{235072563599}{26491011084499968},
\frac{655398850662090042240821783}{756396676602907446734765701632000}\right).
\]

The evidence JSON contains all six period polynomials and the exact Newton coefficients of \(D_2\) through degree six.
