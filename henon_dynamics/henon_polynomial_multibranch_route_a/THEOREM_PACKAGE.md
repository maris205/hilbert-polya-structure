# Theorem package (finite pilot)

## Definition 1 — primitive branch necklace

For \(w\in\{0,1,2\}^n\), call \(w\) primitive when it is not a repetition
of a shorter word. Its necklace representative is the lexicographically
least cyclic rotation. Let \(\mathcal P_n\) be the resulting set.

## Definition 2 — branch matrices and transfer

With \(\sigma=(9,-3,24)=(P'(-2),P'(0),P'(3))\), set

\[
B_j=\begin{pmatrix}\sigma_j&-1\\1&0\end{pmatrix},
\qquad
A_{ij}=B_j,\quad i,j\in\{0,1,2\}.
\]

Thus \(A\) is a 6 by 6 block matrix. For a word \(w=w_0\cdots w_{n-1}\),
write \(B_w=B_{w_{n-1}}\cdots B_{w_0}\).

## Proposition — exact finite trace decomposition

For every \(1\le n\le6\),

\[
 \operatorname{Tr}(A^n)=
 \sum_{d\mid n}d\sum_{[w]\in\mathcal P_d}
 \operatorname{Tr}(B_w^{\,n/d}).
\]

The factor \(d\) counts the distinguished starting positions of a primitive
necklace. The certificate verifies the identity over the integers for every
\(n\le6\).

## Proposition — finite determinant/Newton consistency

If \(D(z)=\det(I-zA)=\sum c_kz^k\), then the recorded coefficients satisfy

\[
 k c_k=-\sum_{j=1}^k c_{k-j}\operatorname{Tr}(A^j)
\]

for \(1\le k\le6\), with coefficients beyond the actual degree interpreted as
zero. This is a finite-dimensional algebraic identity, not a claim that
\(D\) is the Fredholm determinant of the polynomial Hénon map.

## Status boundary

The statements above concern the frozen symbolic pilot and are fully checked.
The geometric implications “every pilot word is a Hénon orbit” and “the
finite determinant is a source-native Fredholm determinant” are intentionally
not included in the theorem package.
