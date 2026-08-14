# Methodology blueprint

## Inputs

- the P60 odd mixed-axis closure/divisibility theorem;
- the P61 reversor-tangency lemma;
- Arai's certified hyperbolic plateau;
- Devaney--Nitecki's full-shift large-parameter theorem;
- Friedland--Milnor's algebraic fixed-point count.

## Compiler

```text
linear parameter conjugacy
  -> connected hyperbolic continuation from a full-shift anchor
  -> 2^n distinct real fixed points
  -> compare with total complex multiplicity 2^n
  -> all complex periodic points are real and simple
  -> apply to mixed-axis closure roots
  -> totally real, squarefree, effective primitive divisors
```

## Validation layers

1. exact symbolic parameter conjugacy and rational endpoint comparison;
2. source-scope audit separating imported theorems from new deductions;
3. exact recurrence and Möbius quotient reconstruction;
4. Sturm real-root counts and squarefreeness through odd period 13;
5. independent binary-word and high-precision root checks;
6. dependency hashes and adversarial mutation rejection;
7. Route-A and Route-B fail-closed evaluation.

## Non-promotion rule

All-period total reality is an algebraic/dynamical theorem.  It is not
evidence for rational-prime labels or Riemann spectral matching unless a new
source-native arithmetic trace is proved.
