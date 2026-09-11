# Collision firewall for quartic inverse-span dynamics

Candidate literal map:

```text
X_p = {F_p-linear subspaces A of F_{p^4}}
J(A) = span_Fp(A^{-1}), with J(0)=0.
```

## Literal-system comparison

| Prior system/kill | Shared surface vocabulary | Decisive non-collision |
|---|---|---|
| P109 fixed-nilpotent subspace image | Same carrier type: a finite subspace lattice | P109 applies one fixed linear operator to a basis.  QIS applies field inversion to **every nonzero point** and then takes a span; rank is nondecreasing rather than nonincreasing, and recurrent states are scaled subfields rather than invariant/Jordan subspaces. |
| P97 sumset squaring / permanent Schur-square kill | Nonlinear set operation followed by algebraic closure | QIS is neither an additive sumset nor coordinatewise multiplication.  Its line image is a normal rational curve and its binary anomaly comes from the number `p+1` of projective points. |
| P102 norm/squaring | Inversion and multiplicative group quotients appear in formulas | The states here are all additive subspaces, not field elements or group-algebra units.  Scalar quotients count recurrent subspaces only after the global span map is analyzed. |
| P107/P124/P142 ideal dynamics | Lattice carrier and closure language | No ideals, colon, annihilator, valuation, min/max tent, or ideal exponent reduction occurs. |
| P125 quadratic shear | Nonlinear polynomial behavior over finite fields | Inversion is rational and the update consumes an entire projective subspace.  No triangular-coordinate clock or coefficient shear is used. |
| P137 rank feedback | Dimension/rank stratifies the transition graph | Dimension is an output monotone, not an input-selected exponent or feedback control.  The map has no rank-dependent branch in its definition. |
| P165 code support shortening | Subspaces and a closure after a pointwise diagnostic | QIS has no coordinates, support, puncturing, or shortening.  Its `K^x` Singer action is intrinsic to the field extension. |
| Generic power-map permanent kill | Recurrent scaled subfields are acted on by inversion | Only the already-classified recurrent core reduces to inversion on cyclic scalar quotients.  The transient map is a projective-span operation, and its sharp `p=2` layer is invisible to a generic group power map. |

Verdict: **no internal literal-system collision found**.

## Proof-engine comparison

The proof uses four ingredients:

1. cardinality gives `dim J(A) >= dim A`;
2. a rational-function independence lemma gives the exact image dimension of
   every projective line;
3. the published classification of subspaces whose patched inverse image is a
   subspace identifies equality cases;
4. Gaussian coefficients plus twisted Singer symmetry give cycles and fibres.

Ingredients 1 and 4 are elementary, but ingredient 3 is a strong direct-owner
dependency and ingredient 2 is closely aligned with published inverse-line
geometry.  Therefore the proof engine is **externally owner-thin even though it
is internally distinct**.

## Forbidden reframings

- Do not market the equality-case classification or inverse-line geometry as
  new.
- Do not enlarge from degree four to arbitrary extension degree without a new
  sharp height theorem; that would turn the paper into a parameter survey.
- Do not replace inversion by `x -> x^k` and claim the same system; that enters
  the generic power-map kill.
- Do not call the characteristic-two depth jump a computational conjecture:
  the plane-rank lemma proves it exactly.
- Do not allocate a P-number before an external owner decision accepts the
  residual dynamical contribution.
