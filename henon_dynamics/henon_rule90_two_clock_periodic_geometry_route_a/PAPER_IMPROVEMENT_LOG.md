# C145 paper improvement log

No external reviewer transport or numeric review score was used.  Two direct
internal theorem/scope audits were performed, repaired, and recompiled.

## Round 0 to round 1

Findings:

- The small-circumference convention was implicit when the two Rule-90
  neighbors coincide.
- The multiplication-kernel proof asserted uniqueness without displaying the
  degree argument and its zero-degree boundary case.
- The witness table's short domain labels could be misread as unbounded
  minimum claims.

Repairs:

- Stated that both neighbor summands are retained and cancel over `F_2` for
  `L=1,2`.
- Added the injection proof `g | (r-r')` and the `deg g=0` case.
- Rewrote every row with its exact `<=24` domain and explicitly denied an
  unbounded minimum claim.

## Round 1 to round 2

Findings:

- Möbius inversion needed an explicit justification for possibly noninvertible
  Rule-90 maps.
- Exhaustiveness of each same-area search group was implicit.

Repairs:

- Observed that `F_L^n u=u` itself places `u` on a cycle whose least period
  divides `n`, regardless of global invertibility.
- Stated that every eligible divisor pair of each area is enumerated in the
  frozen search box.

Final audit: no unresolved critical, major, or minor issue remains within the
frozen claim scope.  The final paper makes no external-independence claim.
