# C277 results

- Theorem status: `PROVABLE_AS_STATED`.
- Exact receipt: 24 scalar cells, 192 spectral cells, six composition
  witnesses, 96 long-time mode cells, 35 smoothing cells, and 25 Schatten
  cells.
- Main advance: for `0<beta<1`, the memory solution is positive and
  contractive but not a semigroup; at fixed positive time and within the
  declared `theta>=0` domain, `A^theta S_beta(t)` is bounded iff `theta<=1`,
  and it lies in `S_p` exactly for `p>1/2`.  For `theta<0` it is also bounded
  because `A>=I`, but that case is outside the smoothing domain.
- Long time: `t^beta S_beta(t) -> A^{-1}/Gamma(1-beta)` in operator norm.
- The `beta=1` heat face is all-order smoothing with norm `exp(-t)`.
- Route A: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, rejected;
  Route B disabled; scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

Final hashes and executable counts are frozen in the release manifest.
