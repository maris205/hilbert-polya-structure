# Research question and decision rule

For the positive Lyness map

\[
F(x,y)=\left(y,\frac{1+y}{x}\right),
\]

can one obtain an exact periodic-orbit zeta and a natural operator lift that
make it a viable Route-A candidate?

The question is deliberately two-sided.  A valid progress result may be an
exact obstruction rather than a positive zeta formula.

## Hard gate

1. Compute (F,F^2,\ldots,F^5) as rational maps, without relying on a
   finite orbit sample.
2. Classify every least period in the positive quadrant.
3. Decide whether the classical Artin--Mazur coefficients
   (\#\operatorname{Fix}(F^n)) are finite.
4. Prove or refute the ordinary trace-class Fredholm determinant for the
   natural Koopman operator.
5. Record A0--A4 without importing any arithmetic target.

## Decision

The hard gate passes as an obstruction theorem.  The map has exact order
five, one fixed point, and uncountably many exact period-five points.  Thus
the classical Artin--Mazur series already fails at (n=5).  The invariant
measure yields a natural order-five unitary Koopman operator with five
infinite-dimensional eigenspaces, so it is noncompact and has no ordinary
trace-class Fredholm determinant.  The final tuple is

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`.

This is explicit model elimination, not a target-spectrum construction.
