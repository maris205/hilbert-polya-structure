# Derivation package

## 1. Topological source

For a fixed prime \(p\), failure of admissibility means that every residue
modulo \(p^2\) contains at least one occupied coordinate. Such failure has a
finite cylinder witness: choose one occupied coordinate for each of the
\(p^2\) residues. Hence the failure set is open and the admissible set for
that prime is closed. Intersecting over all primes shows that \(X_{\rm sf}\)
is closed in the compact full shift. It is shift invariant because translation
permutes residue classes modulo \(p^2\).

Thus \((X_{\rm sf},\sigma)\) is a compact metrizable \(\mathbb Z\)-system and
\(0^{\mathbb Z}\in X_{\rm sf}\) is fixed.

## 2. Window-synchronizing CRT system

Fix \(x^{(1)},x^{(2)}\in X_{\rm sf}\) and a window
\([-L,L]\). For each \(j\in[-L,L]\) and
\(i\in\{1,2\}\), choose a distinct rational prime \(p_{j,i}\). Admissibility
gives a missing residue

\[
a_{j,i}\in
\left(\mathbb Z/p_{j,i}^2\mathbb Z\right)
\setminus
\left(\operatorname{supp}(x^{(i)})\bmod p_{j,i}^2\right).
\]

The \(2(2L+1)\) moduli \(p_{j,i}^2\) are pairwise coprime. The Chinese
remainder theorem therefore solves

\[
n+j\equiv a_{j,i}\pmod{p_{j,i}^2}
\qquad
(j\in[-L,L],\ i\in\{1,2\}).
\]

Choose a nonnegative representative \(n=n_L\). Since the residue
\(a_{j,i}\) is missing from the support,

\[
x^{(i)}_{n_L+j}=0
\qquad
(j\in[-L,L],\ i\in\{1,2\}).
\]

Hence \(\sigma^{n_L}x^{(1)}\) and \(\sigma^{n_L}x^{(2)}\) agree on an
arbitrarily long central zero block.

## 3. Proximality

Use the standard product metric

\[
d_X(x,y)=\frac13\sum_{k\in\mathbb Z}2^{-|k|}|x_k-y_k|.
\]

Agreement on \([-L,L]\) implies

\[
d_X(x,y)\le \frac{2^{1-L}}{3}\longrightarrow0.
\]

Applying this to the shifts produced above yields

\[
\inf_{n\ge0}d_X(\sigma^n x^{(1)},\sigma^n x^{(2)})=0.
\]

Every pair is proximal, so \(X_{\rm sf}\) is proximal.

## 4. Passage through a factor

Let \(y_1,y_2\in Y\) and choose lifts \(x_1,x_2\) under the surjection
\(\pi\). Given \(\varepsilon>0\), uniform continuity of \(\pi\) supplies
\(\delta>0\) such that

\[
d_X(u,v)<\delta\Longrightarrow d_Y(\pi u,\pi v)<\varepsilon.
\]

Source proximality gives an \(n\ge0\) with
\(d_X(\sigma^n x_1,\sigma^n x_2)<\delta\). Equivariance then gives

\[
d_Y(S^n y_1,S^n y_2)
=d_Y(\pi\sigma^n x_1,\pi\sigma^n x_2)<\varepsilon.
\]

Thus every lawful factor is proximal.

## 5. Periodic-orbit separation

Set \(y_0=\pi(0^{\mathbb Z})\). Equivariance makes \(y_0\) fixed.

Suppose \(y\) is periodic of least period \(r\).

- If \(r=1\) and \(y\ne y_0\), the pair \((y,y_0)\) remains at the fixed
  positive distance \(d_Y(y,y_0)\), contradicting proximality.
- If \(r>1\), every pair \((S^k y,S^{k+1}y)\) is distinct. The finite minimum

  \[
  \delta_r=\min_{0\le k<r}d_Y(S^k y,S^{k+1}y)
  \]

  is positive. For every \(n\),

  \[
  d_Y(S^n y,S^n(Sy))\ge\delta_r,
  \]

  again contradicting proximality.

Therefore \(y_0\) is the unique periodic point.

## 6. Fixed-point ledger and determinant

Since \(y_0\) is fixed and no other periodic point exists,

\[
\#\operatorname{Fix}(S^m)=1
\qquad(m\ge1).
\]

Substitution into the Artin--Mazur definition gives

\[
\begin{aligned}
\zeta_{\rm AM,Y}(z)
&=\exp\left(\sum_{m\ge1}\frac{z^m}{m}\right)\\
&=\exp(-\log(1-z))\\
&=\frac1{1-z},
\end{aligned}
\]

first as a formal identity and analytically for \(|z|<1\). Thus

\[
D_{\rm AM,Y}(z)=1-z.
\]

On the periodic core \(K_{\rm per}=[1]\), so

\[
\operatorname{tr}(K_{\rm per}^m)=1,
\qquad
\det(I-zK_{\rm per})=1-z.
\]

## 7. Primitive/repetition decomposition

There is exactly one primitive orbit \(\mathcal O_0=\{y_0\}\) of length one.
Its Euler factor is

\[
(1-z)^{-1}.
\]

The terms \(z^r/r\) in the logarithm are repetitions of this same orbit.
They cannot supply an infinite primitive support indexed by rational primes.
The obstruction occurs before clock weights or analytic continuation are
considered.

## 8. Repair classification

For any finite prime set \(P_0\), the finite-constraint source contains the
nonzero periodic point

\[
x_n=\mathbf 1_{\{n\equiv1\pmod Q\}},
\qquad Q=\prod_{p\in P_0}p^2.
\]

Its support occupies only residue one modulo every \(p^2\) in \(P_0\). Thus
the first row below is an exact all-finite-sets obstruction, not an inference
from the modulus-four example alone.

| Proposed repair | Mathematical effect | Same contract? |
|---|---|---|
| Keep only finitely many prime-square exclusions | admits nonzero periodic points | no: changed source |
| Add a periodic factor by product/extension | imports an external ledger | no: changed source and direction |
| Induce or return to a subset | changes time and primitive type | no |
| Use a noncontinuous or nonequivariant map | leaves topological factor category | no |
| Use a measure or aperiodic zeta | changes determinant owner | no |
| Use the one-point factor | retains singleton ledger | yes, but trivial |
| Use the identity factor | retains singleton ledger | yes, but no repair |

## 9. Route derivation

- A0 remains `A0_FAIL`: prime-square arithmetic is inserted explicitly.
- A1 remains `A1_FAIL`: every factor has only one trivial primitive orbit.
- A2 remains `A2_ANALYTIC_DETERMINANT`: \(1-z\) is exact but trivial.
- A3 remains `A3_FAIL`: no completed divisor, functional equation,
  \(T\log T\) growth, or same-ledger Weil compression appears.
- A4 remains `A4_FAIL`: the periodic-core matrix is not a full spectral lift.

Therefore Route A is rejected and Route B remains forbidden.
