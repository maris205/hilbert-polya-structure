# Author self-check — P107

Status: author-stage only; two independent hostile reviews and final QA are
still required.  External release remains **HOLD**.

## Mathematical boundary checks

- `e=0` and `e=a` form a two-cycle for every `a>=1`, `r>=2`; neither is
  counted as an odd-iterate fixed point.
- The interior solution `e=ra/(r+1)` is integral exactly when `(r+1)|a`.
- Negative and positive deviations clip on opposite parities; the depth
  formula includes the final update into `a`.
- The CDF formulas count only interior negative/positive states and add the
  endpoints and possible resonant fixed state exactly once.
- In a CRT product, depth is the maximum coordinate depth.  Odd fixed count
  is zero if any prime exponent is nonresonant; the even fixed count is the
  recurrent-set size.
- `(B-A)/2` is integral: either some factor of `B` is even, or all factors
  are three and `B-A=3^s-1`.

## Evidence checks

- Coordinate and literal divisor-ideal lanes use different representations.
- The canonical author-stage run passes 212,843 exact assertions.
- The output file records every stated range; finite enumeration is not used
  as proof of the quantified formulas.
- Bibliographic DOI strings were checked against publisher/Crossref search
  results; commutative-algebra and annihilating-ideal material is explicitly
  assigned zero novelty credit.

No author-side final seal, external owner clearance, or priority claim is
made here.
