# C124 theorem package

## Frozen construction

Let

\[
A=\begin{pmatrix}3/16&-1/32\\1/4&0\end{pmatrix},\qquad
\phi_j(z)=Az+(t_j,0),\qquad (t_0,t_1,t_2)=(-2,0,2).
\]

The admissibility and weights are

\[
B=\begin{pmatrix}1&1&0\\1&0&1\\1&0&0\end{pmatrix},\quad
c=(1/2,1/3,1/5),\quad
W=B\operatorname{diag}(c).
\]

### Theorem 1: strict interior and strong separation

Every branch maps the closed radius-three bidisc strictly into the open
radius-three bidisc.  The first-coordinate image radius is (21/32), the
second-coordinate radius is (3/4), and the greatest first-coordinate extent
is (85/32<3).  Adjacent first-coordinate centers are distance (2) apart,
so their closed image discs have gap

\[
2-2(21/32)=11/16>0.
\]

Hence the three branch images are pairwise disjoint.

### Theorem 2: all-period primitive coding

Every admissible cyclic word (w) has exactly one fixed point of its affine
composition because the linear part is (A^{|w|}), whose eigenvalues are
(8^{-|w|}) and (16^{-|w|}).  Strong separation makes the itinerary unique.
Therefore primitive cyclic words modulo rotation correspond bijectively to
primitive geometric cycles, including their rooted phases and repetitions.
There are infinitely many, for example the primitive family (0^k12).

### Theorem 3: trace-class Hardy owner

On

\[
\mathcal H=\bigoplus_{i=0}^2 H^2(\mathbb D_3^2),\qquad
(\mathcal L f)_i(z)=\sum_jB_{ij}c_j f_j(\phi_j(z)),
\]

the operator (mathcal L) is trace class.  Indeed every branch image lies in
a concentric smaller bidisc.  Truncation by total monomial degree has a tail
bounded by a geometric factor with multiplicity growing only linearly, hence
the singular-value majorant is summable.  A finite sum of these composition
blocks remains trace class.

For an affine word of length (n), translations lower total degree and do not
alter the diagonal graded blocks.  Summing the symmetric-power traces gives

\[
\operatorname{Tr}C_{\phi_w}
=\sum_{r,s\ge0}8^{-rn}16^{-sn}
=\frac1{(1-8^{-n})(1-16^{-n})}.
\]

### Theorem 4: all-order trace and Fredholm identities

For every (n\ge1),

\[
\boxed{\operatorname{Tr}\mathcal L^n
=\frac{\operatorname{Tr}W^n}
{(1-8^{-n})(1-16^{-n})}.}
\]

The numerator is the exact weighted sum over all rooted admissible closed
words of length (n).  Consequently

\[
D_H(z)=\det(I-z\mathcal L)
=\prod_{r,s\ge0}\det(I-z8^{-r}16^{-s}W),
\]

an entire, normally convergent product.  Since

\[
\Delta(u)=\det(I-uW)=1-u/2-u^2/6-u^3/30,
\]

this is also a fully explicit product of cubic factors.  Grouping rooted words
by primitive cycle and repetition yields

\[
\log D_H(z)=-\sum_{[\gamma]}\sum_{m\ge1}
\frac{(c_\gamma z^{\ell_\gamma})^m}
{m\det(I-A^{m\ell_\gamma})}.
\]

### Theorem 5: exact translation-blindness control

Replace the translations by ((-3/2,0,3/2)).  Their branch images remain
strictly separated, now with gap (3/16).  The word (012) moves to different
rational phase points, but (A,B,c,W), every power trace, and the complete
Fredholm determinant are unchanged.  Therefore this determinant cannot recover
branch translations or orbit locations.

## Progress over prior gate

- Relative to C119, the same global determinant owner now has infinitely many
  nontrivial primitive cycles and is derived from their rooted trace sums.
- Relative to C123, the result is all-period and infinite-dimensional rather
  than a period-six word atlas plus a degree-four moment operator.
- The remaining obstruction is explicit: no target divisor, target functional
  equation, counting law, arithmetic correspondence, or natural quantization
  is tested.
