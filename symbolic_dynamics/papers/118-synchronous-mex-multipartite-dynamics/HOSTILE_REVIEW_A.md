# Hostile Review A — P118

Status: independent nonauthor review. External dissemination, novelty,
priority, and submission remain **HOLD**. I reviewed the complete paper-local
package, `main.tex`, the seven-page `main.pdf`, all formulas and proofs, the
bibliography, and the canonical verifier/transcript. I did not edit the
manuscript or consult another review.

## Provisional verdict

**MAJOR REVISION, but no counterexample found to the stated theorem
package.** The two fibre formulas, recurrent targets, quotient preimages,
closed recurrent fibres, and basin/layer formulas survive independent
reconstruction, including `k=1` and the canonical `u=0` edge. The main
defect is a false sentence in the quotient-exhaustion proof: it omits the
case in which the least missing retained value equals the original mex.
That gap is repairable by a short case split and does not change the
classification. Related-work subtraction also needs one direct synchronous
Grundy neighbor.

Severity count: **C: 0; M: 2; m: 3.**

## Independent reconstruction

One literal graph round is part-monochromatic because all vertices in a part
have the same open neighborhood. The quotient is therefore

`T(y)_i = mex{y_j : j != i}`.

If `g=mex{y_1,...,y_k}`, deleting coordinate `i` lowers the mex below `g`
exactly when `y_i<g` and that value occurs uniquely. This proves the stated
support-reduction lemma.

The inclusion--exclusion fibre formula correctly imposes every target
absence first and then excludes failure of each lower-colour presence
condition. The support formula is equivalent: `y_i=r` requires the support
of named colour `r` to lie in `{i}`, while `y_i>r` requires that support not
to lie in `{i}`. Fixing all supports leaves independent onto maps within
each labelled part. These are genuinely different enumerations of the same
fibre.

The recurrent list also reconstructs. The fixed states are the permutations
of `0,...,k-1`. For every injection of `0,...,m-1`, the two vectors filling
the other coordinates by `m` and `m+1` swap. The injections for different
`m` are disjoint, so the number of primitive two-cycles is
`sum_(m=0)^(k-2) k!/(k-m)!`.

For first images of the original graph, a repeated value must be the maximum:
two target conditions with the same value make that colour globally absent,
which rules out a larger target. This image restriction is exactly what
places the second graph iterate in the recurrent list. The three closed
fibre products and the three quotient-preimage descriptions follow from the
same absence/presence conditions. Finally, summing first-image masses over
recurrent targets gives depths at most one, while summing over quotient
preimages gives complete orbit basins and depth-two mass.

## Critical issues

None found.

## Major issues

### M1 (mathematics): Theorem 4.2's exhaustion proof omits `m=g`

After one quotient update, let `S` be the retained unique values below the
original mex `g`, and let `m=mex(S)`. The proof claims that a second use of
the lemma retains `0,...,m-1` and fills every remaining coordinate by `m`.
This is false when `m=g`: the first image already contains all lower values
once and contains `g` in every other coordinate, so it is already an
`x^-` state. Its next image is the corresponding `x^+`, filled by `g+1`,
not by `g`.

An explicit quotient counterexample is

`y=(0,2,3,3)`, `g=1`, `T(y)=(0,1,1,1)`, and
`T^2(y)=(0,2,2,2)`.

Here the retained set is `{0}` and `m=g=1`. Thus the printed second-step
sentence predicts the wrong value. The theorem remains true: `T(y)` is
already `x^-`, so the orbit has entered the recurrent list after one round.

Required repair: split the proof into `m<g` and `m=g`. In the first case the
second image is `x^-` (or a permutation when one coordinate remains). In the
second case the first image is already `x^-` (or a permutation), and direct
substitution supplies its next partner. Also say explicitly that the indexed
pairs are disjoint before using the injection count.

### M2 (owner scope): synchronous Grundy protocol work is missing

The paper correctly gives full prior credit to
[Hedetniemi--Jacobs--Srimani (2003)](https://doi.org/10.1016/S0020-0190(03)00299-0):
their Algorithm 2.1 uses the same local mex value, shifted by one, under a
serial central daemon. The manuscript also cites synchronization-avoiding
and dynamic-colouring algorithms. It omits
[Faghih--Bonakdarpour--Tixeuil--Kulkarni (2018)](https://doi.org/10.23638/LMCS-14(1:12)2018),
which explicitly treats synchronous timing models and includes distributed
Grundy-colouring protocol synthesis as a case study. That paper does not
appear to own this unconditional all-vertex mex rule or the multipartite
functional graph, but it directly owns part of the claimed synchronous
Grundy neighborhood and must be subtracted.

Recent synchronous distributed colouring is also a heavily occupied generic
class; for current context see, for example,
[Fuchs--Kuhn, OPODIS 2025](https://doi.org/10.4230/LIPIcs.OPODIS.2025.23).
It is not a direct owner of the displayed quotient. A bounded search found
no source giving the exact complete-multipartite `T`, its two-cycles, the
part-sensitive fibres, or its basins. This remains a bounded non-hit, not a
novelty conclusion.

Required repair: add and explicitly deduct the 2018 synchronous Grundy
neighbor, retain Hedetniemi et al. as the closest literal local-rule owner,
and keep the residual restricted to this concrete synchronous
complete-multipartite conjunction.

## Minor issues

### m1 (mathematics): the `k=1` proof invokes a lemma with `k>=2`

Theorem 4.4 is stated for every `k>=1`, but its proof invokes the
repeated-maximum lemma, whose hypothesis is `k>=2`. The conclusion is true
at `k=1`: the graph is edgeless, every colouring has first image `(0)`, and
that quotient state is fixed. Add this one-line case before applying the
lemma.

### m2 (traceability): theorem numbers in `CLAIMS_EVIDENCE.md` are stale

The two-round global recurrence is Theorem 4.4, supported by Lemma 4.3, not
“Theorem 4.3.” The global/orbitwise layer result is Theorem 6.2, not
“Theorem 6.1.” Correct these anchors so the claim map points to the actual
PDF statements.

### m3 (package record): `BUILD.md` is unfinished

The build record says final page/byte/diagnostic metrics are recorded after
compilation, but supplies none. The existing PDF is seven clean, legible A4
pages and the settled log I inspected contains no warning, error,
undefined-reference, overfull, or underfull diagnostic. Fill the record or
remove the placeholder sentence before release.

## Boundary and formula audit

- `k=1`: the only recurrent quotient state is `(0)`; its first-image fibre is
  `q^a`, and the graph depth profile is `(D0,D1,D2)=(1,q^a-1,0)`. Both
  general fibre formulas, the fixed-target product, quotient preimage, and
  basin formulas reduce to these values.
- `u=0` in the `x^+` product: `R` has at least two nonempty parts because
  `m<=k-2`. Hence the zero powers in `Q_{>=2}` have their intended
  combinatorial values, and the formula counts occurrence of colour `m` in
  at least two `R`-parts correctly.
- Larger palettes: `q>=Delta+1>=k`, so every quotient mex remains inside
  the palette and the high-colour exponential has nonnegative multiplicity.
- The fixed, minus, and plus quotient preimage sets (6.1)--(6.3) reconstruct
  directly from the support-reduction lemma; no missing high-colour case was
  found.
- The global layer identities and orbitwise basin identities have the
  correct one-round time offset.

## Exact controls

- Fresh canonical verifier: **PASS**, 201,922 assertions over fifteen
  parameter lanes.
- Fresh stdout versus `code/verification_output.txt`: **byte-identical**.
- Independent quotient exhaustion through `k<=5` and palettes `k,k+1,k+2`:
  **PASS**, 30,136 states; this also isolated the proof counterexample above.
- The verifier includes `k=1`, enlarged palettes, and canonical `u=0`
  lanes.
- Seven-page visual inspection: no clipped formula, unreadable table, or
  evident layout defect.

## Mandatory resolution before circulation

1. Repair Theorem 4.2 with the missing `m=g` branch and explicit disjointness.
2. Split off `k=1` before using the repeated-maximum lemma.
3. Expand owner subtraction to the 2018 synchronous Grundy protocol work.
4. Correct the claim-map theorem anchors and finish the build record.
5. Keep external status **HOLD** pending independent ownership clearance.

