# Refinement report

## Initial direction

The round switched from compact quaternionic dynamics to the modular
one-cusp scattering system.  The first proposal aimed to test the attractive
chain

```text
totient double-coset ledger
  -> denominator sojourn clock
  -> closed primitive-orbit zeta
  -> one Riemann xi divisor
```

The arithmetic first arrow is classical and correct.  The unexamined step was
the change from an open double coset to a closed hyperbolic conjugacy class.

## Reviewer-driven changes

### Round 1

- froze PSL/SL sign and orientation conventions;
- separated the bare totient ratio from the full gamma-completed scattering
  coefficient;
- added exact conjugacy and even Gauss cyclic witnesses;
- replaced “unique repair” by “canonical stable homogenization.”

### Round 2

- introduced the positive family
  `[[1,m],[n,1+mn]]`;
- proved the arbitrary scaled denominator-function square-law theorem;
- derived the exact Chebyshev defect and stable Selberg limit;
- scoped the Euler-product corollary to final-monodromy denominator-only
  norms;
- made the divisor theorem global and limited it to affine changes and entire
  zero-free factors;
- listed untested local, endpoint, cohomological, groupoid, and multi-cusp
  constructions.

### Release hardening

- added a six-artifact independent checker at 110 digits;
- added unit, import-independence, and mutation-rejection tests;
- wrote the Route-A YAML, proof package, source audit, manuscript, and
  registries;
- compiled and visually inspected a nine-page PDF.

## Final position

The resulting project is stronger as a negative theorem than the initial
positive conjecture.  Modular scattering retains genuine arithmetic content,
but the exact closed-orbit compatibility test fails for an entire function
class rather than at a few numerical examples.  The stable positive closure
identifies where the construction goes: back to the classical Selberg clock.
