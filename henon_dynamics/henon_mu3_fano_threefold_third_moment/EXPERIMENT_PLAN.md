# Exact experiment plan

## E1. Chronological zero fibre

For each registered split prime, count \(Z_{p,3}\) by a terminal-step
dynamic program.  The state is `\(start, current_endpoint, phase_residue\)`;
the closing term is added only as \(\rho x_5x_0\).  No averaged transition
matrix is allowed.

## E2. Projective geometry

Count \(S,Q_\rho,X_\rho\) using a disjoint “last nonzero coordinate equals
one” normalization.  Independently count \(Q_\rho\) via the even--odd
bilinear formula.

## E3. Trace reconstruction

For every prime record

\[
A_p=\#S-(1+p+p^2+p^3+p^4),
\]

\[
B_p=(1+p+p^2+p^3)-\#X,
\]

and verify

\[
Z=p^5-p^2-A_p-pB_p.
\]

Check the Jacobi formula \(A_p=20p^2+pa_p\), the exact divisibility
\(p\mid B_p\), and the rational formula for \(C_{p,3}\).

## E4. Smoothness certificate

Rebuild the recurrence (D.2)--(D.3), the normalized equations (E.1), the
polynomial (R(t)), and the rational resultant.  Do not accept a JSON
constant without recomputing it.

For every split divisor of the projection denominator, compute an exact
modular Groebner basis and retain a checkable reduction certificate.  Test
both cubic roots through the explicit isomorphism, not through duplicate
brute force.

## E5. Mutation tests

The checker must reject at least these mutations:

* \(2\sum x_i^3\mapsto3\sum x_i^3\);
* reversal or permutation of chronological variables;
* \(\rho x_5x_0\mapsto x_5x_0\);
* \(p^{-2}\mapsto p^{-3}\) in \(C_{p,3}\);
* \(d_p=(p-1)/2\mapsto p-1\);
* \(+pB_p\) in place of \(-pB_p\);
* rank \(40\mapsto20\);
* rounding \(C_{p,3}\);
* claiming the finite scan proves all-prime smoothness;
* calling the classical Hilbert determinant the normalized root.

## E6. Analytic replay

Machine-check the four moment ranges separately and verify that the
counterterms \(\ell_1,\ldots,\ell_7\) converge on \(\Re s>1/4\).  Record
that the positive normalized trace has \(L^8\), while classical Hilbert
Schatten membership still has the threshold \(q\Re s>3\).
