# Hostile review — P83

**Verdict: GO** for the theorem-bearing internal paper after the corrections
listed below.  The standing prohibition on public posting or priority claims
in `README.md` is unchanged.

Audit date: 2026-08-28 UTC.

## Formula-by-formula audit

- The prescribed first-return multiplicities are
  `f_n(c)=c*C_(n-1)`, so the Catalan generating function gives
  `F_c(z)=c(1-sqrt(1-4z))/2`, radius `R=1/4`, boundary value `c/2`,
  and derivative `c/sqrt(1-4z)`.
- At `c=1`, `F_1(R)<1`, hence the loop shift is transient and its entropy
  radius is `R`.  At `c=2`, `F_2(R)=1` but the first-return mean diverges,
  hence null recurrence.  For `c>=3`, the unique positive solution of
  `F_c(r)=1` is `r=(c-1)/c^2<R`; its finite derivative and strict radius gap
  give positive recurrence and, in the loop-shift criterion used here,
  strong positive recurrence.
- For `c>=3`, individual loop weights `r^|gamma|` sum to one and have mean
  `(c-1)/(c-2)`.  The stationary renewal tower is therefore a probability;
  its entropy per mean excursion is `-log r`, and Kac normalization gives
  `mu([o])=(c-2)/(c-1)`.  At `c=1` the weights have deficient mass, while at
  `c=2` they have infinite mean, so neither endpoint supports this maximal
  probability.
- Private internal vertices make the first-return code circular, so the
  formal identity `zeta=1/(1-F_c)` is valid coefficientwise.  Every fixed
  count is finite.  Logarithmic coefficient extraction gives exactly
  `P_n(1)=binom(2n,n)/2` and `P_n(2)=4^n/2`.
- For `c>=3`, the zero of `1-F_c` at `r` is simple.  Positivity gives no
  singularity inside `|z|<r`; equality in the triangle inequality on
  `|z|=r`, using the positive `z` and `z^2` coefficients, forces `z=r`.
  Thus the claimed smallest-modulus pole is unique.

## Corrections applied

1. Defined the base cylinder `[o]` for the edge presentation.
2. Added the mass/finite-mean normalization argument at all three recurrence
   regimes and the renewal-tower entropy computation for the maximal law.
3. Added the proof that the positive pole is the unique singularity of
   smallest modulus.
4. Restored four missing backslashes before `\qquad`; the previous source
   compiled but printed the letters `qquad` as math variables.

## Reproducibility and release checks

- Deterministic control: **PASS — 1,369 exact assertions**.
- Boundary sequences checked through the script's advertised range; the
  printed first eight values are `[1,3,10,35,126,462,1716,6435]` at `c=1`
  and `[2,8,32,128,512,2048,8192,32768]` at `c=2`.
- Four-stage build (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`): all exits
  zero.
- Final PDF: **4 A4 pages, 285,219 bytes**.
- Log scan: no undefined references/citations, LaTeX errors, overfull or
  underfull boxes, fatal errors, or rerun requests.
- Fonts: **22/22 embedded, subsetted, and Unicode-mapped**.
- Visual inspection: all four pages clean; no clipping, collision, or stray
  `qquad` text.

## Surviving scope boundaries

This is a countable-state edge shift, not a compact finite-alphabet shift.
The zeta identity is asserted as a formal power series.  The parameter is an
integer `c>=1`; maximal-entropy probability and strong positive recurrence
are asserted only for `c>=3`.  General countable-Markov recurrence/MME theory
and circular-code zeta theory remain explicitly cited prior machinery; no
priority claim is made.
