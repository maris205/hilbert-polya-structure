# P168 Review B incidence control

This is the second, independently implemented B-side falsification lane for
P168.  It is retained separately from `../p168_b/` and imports neither the
author verifier nor Review A/B code.

The carrier representation and enumeration are intentionally different from
the other controls:

- a subspace is a frozenset of normalized projective points, not an RREF
  basis;
- planes are generated as joins of projective point pairs;
- hyperplanes are generated as kernels of normalized coordinate functionals;
- complete graphs are reconstructed in different quotient-field models for
  `p=2` and `p=5`;
- trace kernels, scalar transitivity, component structure, and every target
  fibre at times 1 through 6 are checked directly;
- the closed counting formulas are swept over every prime through 97.

The canonical run reports 73,983 assertions.  Two fresh processes produced
byte-identical output.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_incidence.py > replay.txt
cmp replay.txt CANONICAL.txt
sha256sum -c SHA256SUMS
```

This bounded computation is falsification evidence only.  The all-prime
result rests on the manuscript proof, and the external status remains
`HOLD_EXTERNAL`.
