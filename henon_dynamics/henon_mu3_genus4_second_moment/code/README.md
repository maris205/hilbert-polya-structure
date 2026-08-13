# HCS-C48 exact computation

This directory certifies the genus-four interpretation of the second
chronological moment without replacing the ordered four-step phase by an
averaged matrix.  For every split control prime through 199, the producer
computes the same zero fibre by two separate constructions:

1. an exact terminal-step dynamic program in the frozen phase
   \(2\sum x_i^3+x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0\);
2. exact point counting on the explicit \((3,3)\) curve in
   \(\mathbf P^1\times\mathbf P^1\), followed by the projective direction
   identity.

The checker is independently implemented: it eliminates a different phase
variable, partitions the two projective lines into disjoint affine/infinity
charts, and normalizes direct \(\mathbf P^3\) controls by the last rather than
the first nonzero coordinate.  It also checks the four affine Jacobian systems,
the exact moment identity

\[
C_{p,2}=-14-2a_p,
\qquad a_p=p+1-\#X(\mathbf F_p),
\]

the integer Weil gate \(a_p^2\le64p\), the \(\Re s>1/3\) Euler domain, and the
minimal sixth-order regularized graded determinant in \(L^q(M,\tau)\).
The certificate separately freezes the classical threshold
\(X_s\in S^q(\mathcal H)\iff q\Re s>3\): ordinary Hilbert trace class starts
only at \(\Re s>3\) and does not implement the field-degree-normalized root.
Thus the sixth-order object is explicitly a semifinite \(\tau\)-associated
graded determinant, not a classical Fredholm determinant.

Run `./code/run_c48.sh` from the project directory.  It regenerates both JSON
artifacts into a temporary directory, requires byte identity with the frozen
results, runs the isolated mutation suite, and verifies the release manifest.
Use `./code/run_c48.sh --refresh-manifest` only when intentionally freezing a
new complete artifact set.
