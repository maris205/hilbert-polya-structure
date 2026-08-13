# HCS-C48 — Genus-Four Hénon Second Moment

The second Galois-normalized chronological moment of the full finite-field
Hénon kernel is the Frobenius trace of an explicit smooth genus-four curve.
For every prime (p>3), (p\equiv1\pmod3), and an order-three
\(\rho\in\mathbf F_p^\times\), put

\[
X_\rho:\quad
\rho r^3(t^3+u^3)+\rho^2s^3t^2u-s^3tu^2=0
\quad\subset\quad\mathbf P^1\times\mathbf P^1.
\]

This is a smooth curve of bidegree \((3,3)\), hence genus four.  If
\(a_p=p+1-\#X_\rho(\mathbf F_p)\), then the exact descended second moment is

\[
C_{p,2}=-14-2a_p,
\qquad
c_{p,2}=-\frac{28+4a_p}{p-1}.
\]

The Weil bound gives \(c_{p,2}=O(p^{-1/2})\).  Together with the exact first
moment and the uniform higher-moment bound, this extends the normalized Hénon
Euler germ from \(\Re s>1/2\) to \(\Re s>1/3\).  In the operator model it is
a sixth-order regularized graded determinant relative to the normalized
semifinite trace \(\tau\), with five explicit chronological counterterms.
Here ``sixth-order'' is the least fixed integer order forced by
\(L^q(\mathcal M,\tau)\)-membership of the inherited graded block; it is not
a statement about classical Hilbert-space Schatten membership or a
classification of unrelated regularization schemes.

The two trace categories have different sharp thresholds.  For the normalized
semifinite trace,

\[
X_s\in L^q(\mathcal M,\tau)\iff q\Re s>2,
\]

so an unregularized \(\tau\)-associated analytic determinant exists only on
\(\Re s>2\).  On the underlying Hilbert direct sum,

\[
X_s\in S^q(\mathcal H)\iff q\Re s>3,
\]

and classical trace class begins only on \(\Re s>3\).  That classical trace
removes the factor \(1/d_p\): its local determinant is the ordinary Galois
norm \(N_p=G_p^{d_p}\), not the canonical normalized root \(G_p\).

## Route A

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_EXPLORATORY_GENUS4_THIRD_ABSCISSA`.  This is not a
functional equation, a continuation through \(\Re s=1/3\), or an RH proof.

## Next gate

The third chronological moment is now the first wall.  Its projective
stratification leads to a \((2,3)\) threefold in \(\mathbf P^5\).  The next
batch should isolate its middle cohomology and test whether it supplies a
second square-root gain, potentially moving the germ to \(\Re s>1/4\).
