# C82 theorem package

Let `W(S)=sum_A F(A)(-1)^{|A cap S|}`.  The exact transform has 1024 nonzero
coefficients and degree at most ten because six coordinates are dummy and the
active predicate is a pivot times a degree-six block-hit polynomial.  Parseval
gives

```text
sum_S W(S)^2 = 2^16 * 30400.
```

For Hamming distance `h`, the ordered-pair correlation is
`C_h=sum_{d_H(A,B)=h}F(A)F(B)`.  The second Walsh transform of `W(S)^2`,
divided by `2^16`, gives the listed nonnegative integer `C_h` values.  The
receipt records the equivalent bit-flip noise polynomial identities, but makes
no claim about a stochastic dynamical system beyond this finite truth table.
