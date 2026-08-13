# HCS-C47 derivation package

## Why the category changes

C46 proves that the local normalized root has fractional divisor orders.  A
normalized matrix trace over all Galois sectors assigns exactly such
fractional dimensions.  The question is whether the global prime block lies
in a determinant ideal on the C45 half-plane.

## Positive trace versus supertrace

The algebra carries a positive trace \(\tau\), which controls Schatten norms,
and a signed functional \(\operatorname{str}(A)=\tau(\Gamma A)\), which
encodes the augmentation ratio.  Cancellation in the supertrace cannot be
used to claim positive trace-class membership.

Globally, \(\operatorname{str}(A)\) is applied only when \(A\in L^1\).
The low-order functions \(\ell_n\) are instead convergent sums of the
finite-dimensional local supertraces.  This local cancellation is legitimate,
but it does not turn \(X_s^n\) into an \(L^1\) operator.

Exact block dimensions give

\[
\tau_p(I)=(8p+4)/3.
\]

Thus \(p^{-s}W_p\) contributes order \(p^{1-q\Re s}\) to the \(L^q\)
quasinorm, and the exact threshold is \(q\Re s>2\).

This is the noncommutative \(L^q\) threshold for the field-degree-normalized
trace.  With the canonical Hilbert trace the block dimension is of order
\(p^2\), so \(X_s\in S^q\) exactly when \(q\Re s>3\).  The corresponding
ordinary trace gives \(C_{p,n}\), not the normalized coefficient
\(c_{p,n}=C_{p,n}/d_p\).

## Why order four appears

At \(\Re s>1/2\), the block is in \(L^4\) but in no uniformly smaller
integer Schatten ideal.  The trace logarithm from repetition four onward is
therefore an honest \(L^1\) series.  Repetitions one through three are the
canonical regularization counterterms.  Their independent scalar convergence
was already proved in C45.  Recombining the local head series and the
trace-class global tail reproduces the full Hénon Euler logarithm exactly.

## Decision

The normalized Hénon Euler germ is a genuine fourth-order regularized graded
determinant.  It is not an ordinary Fredholm determinant on the proved
half-plane near the critical abscissa.  A positive Fuglede--Kadison-type
determinant, where defined, retains modulus rather than the analytic phase.
This upgrades A2 while leaving the A3 continuation and functional-equation
gates open.
