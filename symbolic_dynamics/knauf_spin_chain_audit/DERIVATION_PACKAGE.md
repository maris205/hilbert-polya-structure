# Derivation Package: Knauf's Arithmetic Recursion

## 1. Problem Setup and Target Quantity

The binary recursion generates positive integers \(h_k(\sigma)\).  Define the
finite multiplicity

\[
\varphi_k(n)=\#\{\sigma\in\{0,1\}^k:h_k(\sigma)=n\},
\]

so

\[
Z_k(s)=\sum_{n\ge1}\varphi_k(n)n^{-s}.
\]

The audit asks which parts of the limiting zeta quotient are endogenous and
which require an additional number-theoretic observable.

## 2. Assumptions and Modeling Choices

1. The recurrence is used exactly as stated in the primary source.
2. The numerical grid contains preregistered real and complex values on both
   sides of \(\operatorname{Re}s=2\).  Theorem-level convergence comparisons
   are restricted to \(\operatorname{Re}s>2\); the other locked points are
   boundary/continuation benchmarks only.
3. No zero table is loaded, and no parameter is fitted.
4. The Liouville function is recorded as extra data unless it is derived from
   a frozen symbolic cocycle.

## 3. Notation

\[
Z(s)=\frac{\zeta(s-1)}{\zeta(s)},\qquad
\widetilde Z_k(s)=
\sum_{\sigma}\lambda(h_k(\sigma))h_k(\sigma)^{-s}.
\]

The primary source notes the finite-depth identity
\(\varphi_k(n)=\varphi(n)\) in its stated stable range, where
\(\varphi\) is Euler's totient.

## 4. Derivation

Grouping the binary configurations by their integer value gives

\[
Z_k(s)=\sum_n\varphi_k(n)n^{-s}.
\]

In the stable finite range, \(\varphi_k(n)=\varphi(n)\).  The classical
Dirichlet-series identity

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)}
\qquad(\operatorname{Re}s>2)
\]

explains the exact unsigned limit once convergence of the finite
multiplicities is controlled.

The signed observable proposed in the source is

\[
\widetilde Z_k(s)
=\sum_n\lambda(n)\varphi_k(n)n^{-s}.
\]

Its formal limiting target can be written

\[
\widetilde Z(s)
=\frac{Z(2s)Z(2s-1)}{Z(s)}
=\frac{\zeta(s)\zeta(2s-2)}
{\zeta(2s)\zeta(s-1)}.
\]

This identity clarifies why the Riemann divisor enters, but it does not prove
that the signed finite sums converge in the desired half-plane.  Nor does it
turn \(Z_k\) into a primitive-periodic-orbit determinant.

## 5. Main Result

**PROVED (primary-source theorem):** the unsigned symbolic/arithmetic
recursion has the exact limit \(\zeta(s-1)/\zeta(s)\) in the proved
half-plane.

**OPEN / not inherited:** the wider signed convergence and a canonical
Fredholm periodic-orbit determinant for the same recursion.

## 6. Interpretation

This candidate shows that natural low-complexity symbolic recursion can
generate a zeta quotient without a prime table.  It also exposes two distinct
missing bridges:

1. the Liouville phase is arithmetically appended rather than derived as an
   intrinsic cocycle;
2. a Dirichlet partition function is not automatically a dynamical
   determinant with a primitive/repetition ledger.

## 7. Scope and Limitations

The source's link to a special regular graph and a Ramanujan bound is recorded
only in ROUND2_CLUES.md, because developing that graph as a separate primary
system would violate the session scope.  Numerical finite-depth convergence
cannot certify the unproved half-plane.
