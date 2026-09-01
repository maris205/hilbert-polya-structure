# P151 exact control transcript

Run from this directory with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p151.py
```

Frozen standard output:

```text
P151 unequal-spider exact verifier
literal_profiles=1360
fixed_mass_profiles=190026
inverse_profiles=37440
continuants=400
equal_arm_owned_control=504
excursion_moments=400
fixed_mass_extrema=760104
inverse_boundary=149760
literal_transform=524816
moments=10448
assertions=1446432
arithmetic=integer_and_Fraction_only
enumeration_is_not_proof=1
external_status=HOLD_EXTERNAL
PASS
```

The 1,446,432 assertions comprise:

- 400 continuant-recurrence and closed-coefficient checks;
- 524,816 literal state-recursion/marked-transform coefficient and mass checks;
- 10,448 endpoint, mean, and variance derivative checks;
- 400 additional single-excursion moment checks sharing the continuant
  derivative engine (not an independent implementation);
- 760,104 fixed-mass inequality and equality-class checks;
- 149,760 primitive-ray, dilation, and mean-scale checks; and
- 504 equal-arm collapse checks retained as an owned-background control.

All arithmetic is exact `int` or `fractions.Fraction`.  No pseudorandom seed,
floating-point tolerance, external package, or network access is used.  The
profile bounds are finite counterexample pressure only; the manuscript's
proofs establish the all-parameter statements.
