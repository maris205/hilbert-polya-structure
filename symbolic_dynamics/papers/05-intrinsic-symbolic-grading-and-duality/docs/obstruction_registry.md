# Obstruction Registry

## Inherited active obstructions

### SD-O04 — positive mixed-cycle obstruction

Positive recurrent mixing of two distinct tensor atoms creates a mixed
primitive word and a forbidden composite-mass contribution. Paper-05
rechecks all 28 pairs among the first eight atoms; signs not derived from a
chain complex do not repair the temporal ledger.

### SD-O05 — ungraded Fredholm-continuation obstruction

For SD-C07,
\(\det(I-L_s)=\zeta(s)^{-1}\) on \(\Re s>1\). Scalar continuation of this
identity is not a holomorphic trace-class continuation through a zeta zero.

## Paper-05 obstructions

### SD-O06 — honest Koszul cancellation

Let \(A=\mathbb C[x_p:p\ {\rm tensor\ atom}]\) and let
\(K=A\otimes\Lambda V\) be its standard Koszul resolution, with total-mass
transfer \(T_s\) commuting with the differential. In the Euler half-plane,

\[
  \operatorname{Str}(T_s^r)=1\quad(r\geq1),\qquad
  \operatorname{sdet}(I-zT_s)=1-z.
\]

Thus the one-particle odd Berezinian and exterior-Fock Möbius determinant
are valid graded data types, but inserting them into the complete exact
Koszul complex cancels every non-vacuum prime contribution. Coordinatewise
selection of only the favorable sector is not a same-object completion.

### SD-O07 — symbolic reversal preserves the spectral parameter

Canonical time reversal of the two-sided full shift reverses symbolic time
while preserving the entropy potential. It therefore yields two copies
with weight \(p^{-s}\), schematically \(L_s\oplus L_s\), rather than a
stable/unstable pair \(L_s\oplus L_{1-s}\). Declaring the second weight to
be \(p^{-(1-s)}\) adds a centered normalization absent from the symbolic
source.

### SD-O08 — tensor inversion has the wrong center and no odd orientation

The Grothendieck group of the tensor monoid is
\(\mathbb Q_{+}^{\times}\cong\bigoplus_p\mathbb Z\). Its intrinsic inversion
\(q\mapsto q^{-1}\) sends \(s\mapsto -s\), not \(s\mapsto1-s\). Moreover,
for every monoidal parity character
\(\epsilon:G\to\mathbb Z/2\),

\[
  \epsilon(g^{-1})=-\epsilon(g)=\epsilon(g).
\]

Inversion is therefore parity-even. Moving its fixed center from \(0\) to
\(1/2\) requires an extra half-density/Tate-type datum and is not available
in SD-C07.

### SD-O09 — critical-strip regularization deletes the decisive traces

For the diagonal atom transfer,

\[
 L_s\in S_q\iff q\Re s>1,\qquad
 L_{1-s}\in S_q\iff q(1-\Re s)>1.
\]

The first integer Schatten order with a common open strip is \(q=3\), on
\(1/3<\Re s<2/3\). Even if an \(s\leftrightarrow(1-s)\) pairing is granted
adversarially, the paired determinant

\[
 D_3(s)=\det{}_3(I-L_s)\det{}_3(I-L_{1-s})
\]

is zero-free throughout its defining strip, and

\[
 \log D_3(s)
 =-\sum_{r\ge3}\frac1r\sum_p
   \left(p^{-rs}+p^{-r(1-s)}\right).
\]

Regularization removes the prime and prime-square traces \(r=1,2\).
Restoring them would require counterterms with no common nuclear domain.
Hence this formal reflection symmetry supplies no A3 promotion.
