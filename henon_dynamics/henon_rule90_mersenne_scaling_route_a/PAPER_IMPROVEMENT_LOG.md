# C150 paper improvement log

No external reviewer transport or numeric score was used.  Both rounds were
internal theorem, boundary, and presentation audits followed by compilation.

## Round 0 to round 1

Findings:

- The first draft stated image size without proving the multiplication-kernel
  dimension in the non-Laurent quotient.
- “Order `L`” was too strong; the identity proves only order dividing `L`.
- The exact-period table did not explicitly distinguish points from cycles.

Repairs:

- Added monomial clearance and the `gcd(x^L+1,(x+1)^2)` proof.
- Replaced exact-order language by “order dividing `L`.”
- Added Möbius inversion before division by the period.

## Round 1 to round 2

Findings:

- Equality of the periodic set and image had only one inclusion written.
- The power-of-two control asserted nilpotency without proving uniqueness of
  the periodic state.
- “Every divisor occurs” could be inferred from the divisor ledger.

Repairs:

- Added the converse `a^n u=u => u in im(a)`.
- Added the periodic-state argument for a nilpotent map.
- Added the explicit nonclaim that realized periods may be a proper subset of
  the divisors of `L`.

Final internal audit: no unresolved issue remains inside the frozen scope.
