# HCS-C47 — A Fourth-Order Graded Hénon Determinant

The normalized Galois root from HCS-C45 is not an ordinary local determinant:
HCS-C46 proves exact fractional divisor orders.  This project constructs the
operator category in which those dimensions are legitimate.

All Galois-conjugate Hénon sector blocks are assembled in a graded finite
algebra at each prime, equipped with its field-degree-normalized positive
trace and associated supertrace.  The global block operator \(X_s\) satisfies

\[
X_s\in L^q
\quad\Longleftrightarrow\quad
q\operatorname{Re}s>2.
\]

It is therefore \(\tau\)-trace class only on
\(\operatorname{Re}s>2\), but belongs to
\(L^4(\mathcal M,\tau)\) exactly on the C45 half-plane
\(\operatorname{Re}s>1/2\).  The normalized Euler germ has the exact operator
formula

\[
\mathcal G(s)
=\exp\!\left(-\ell_1(s)-\frac{\ell_2(s)}2-
                  \frac{\ell_3(s)}3\right)
 \det_{4,\tau,\mathrm{gr}}(I-X_s).
\]

Here \(\det_{4,\tau,\mathrm{gr}}\) is the ratio of the two
\(\tau\)-trace-associated
fourth-order determinants in the positive and negative grades.  The
\(\ell_n\) are convergent sums of **local** supertraces; outside the
corresponding \(L^1\) domains they are not global semifinite traces of
\(X_s^n\).  Thus C45 is a genuine fourth-order regularized graded determinant
with three explicit low-order counterterms.  It is not an ordinary Fredholm
determinant on the proved half-plane as one approaches the Riemann critical
abscissa from the right.

This \(\tau\)-determinant is not a classical Hilbert-space Fredholm
determinant.  With the canonical Hilbert trace, the same blocks satisfy
\(X_s\in S^q\) exactly when \(q\operatorname{Re}s>3\), and the unnormalized
trace recovers the ordinary Galois norm rather than its field-degree root.

## Route A

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_EXPLORATORY`, scoped as
`REGULARIZED_GRADED_DETERMINANT`.  Route B remains closed.

## Next gate

The determinant order is controlled by the first three chronological moments.
HCS-C48 geometrizes the second moment as a genus-four curve trace and tests
whether the Euler/regularized-determinant half-plane moves from
\(\operatorname{Re}s>1/2\) to \(\operatorname{Re}s>1/3\).  For the present
positive-ideal block, such a larger domain would require order six and five
counterterms, not order three; a lower order would require a different
compressed operator.
