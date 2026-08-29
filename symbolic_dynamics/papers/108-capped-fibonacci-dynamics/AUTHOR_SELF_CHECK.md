# Author self-check — P108

Status: author-stage only; two independent hostile reviews and final QA are
still required.  External release remains **HOLD**.

## Mathematical boundary checks

- The exact iterate is stated only with the special `t=0` convention
  separated; for `t>=1` both Fibonacci coefficients are defined as used.
- At `t=1`, the first weighted form is `y`, so the CDF correctly counts
  `(0,0)` plus every state with `y=a`.
- The two fixed points are counted once in the positive-time CDF: `(0,0)` is
  the separate `+1`, while `(a,a)` lies in the half-plane count.
- `(1,0)` is the slowest nonzero state and realizes the exact Fibonacci
  threshold, including `a=1`; plateau endpoints, rather than every jump
  location, are Fibonacci caps.
- The fibre branch `v=a` has `u+1` preimages; below-diagonal states have
  none.  The fibre sum is exactly `(a+1)^2`.
- The zeta has two fixed factors and no hidden cycles because every nonzero
  state reaches `(a,a)`.

## Evidence checks

- Literal forward iteration and direct reverse-fibre enumeration have
  different failure modes.
- The canonical author-stage run passes 67,475,970 exact assertions over
  every state through cap 220.
- The four cited DOI records were checked against publisher search results;
  Fibonacci, saturated-control, and zeta background is owner-subtracted.

No author-side final seal, external owner clearance, or priority claim is
made here.
