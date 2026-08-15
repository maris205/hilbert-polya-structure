# Hostile review round 1

## Decision

Minor revision.

## Strongest counterargument

The claimed obstruction could appear to be an artifact of the chosen
integral coordinate `x=6q`: Weil height is coordinate-dependent, so a flat
pressure in one coordinate would not automatically rule out a differently
normalized coordinate pressure.

## Resolution

Added a fixed-rescaling corollary.  For every fixed nonzero algebraic `c`,
`h(c*alpha)<=h(alpha)+h(c)`, so the weight remains uniformly bounded in
period and the pressure remains `(1/2)log(2)`.  The claim remains scoped:
period-dependent scaling and the extensive weight `n*h` are different.

## Other attacks

- Minimal-polynomial conjugates leave the divisor: rejected because the
  minimal polynomial divides the rational integral primitive polynomial.
- Root multiplicity contaminates the count: rejected by P62 squarefreeness.
- Numerical roots prove the limit: rejected; the exact sandwich proves it.
- The theorem covers `s=s_n`: rejected; the statement says fixed real `s`.
