# Exact Control Results

Status: canonical run revalidated at final QA, 29 August 2026; external
release **HOLD**.

Run from this directory:

```text
python3 code/verify.py
```

The verifier is standard-library only. It uses integer matrices and exact
`fractions.Fraction` arithmetic, with no random sampling, floating point,
network access, or external package.

## Stored stdout

```text
positive-Heisenberg exact control: PASS
assertions=421285
literal_words=131071
histogram_slices=153
biased_cases=231
decomposition_words=24573
pressure_cases=297
lane_assertions=asymptotic_algebra:300,biased_moments:693,centered_decomposition:24612,conditional_moments:306,endpoints:600,extrema:430,gaussian_slice:306,literal_norm:131071,literal_normal_form:262142,pair_covariance:231,pressure_bounds:594
```

These exact bytes are stored in `code/verify.out`.

## Lane A — literal products and finite-word laws

1. **Normal form and norm.** For all binary words through length 16
   (131,071 words including the empty word), the script literally
   left-multiplies the two 3-by-3 integer generators. A separate scanner
   counts `X`, `Y`, and `Y`-before-`X` pairs. Full matrices,
   first-superdiagonal totals, and Frobenius identities are checked.
2. **Gaussian slices.** The 153 fixed-content histograms are compared with
   a separately constructed last-letter polynomial recurrence. Slice mass,
   conditional mean, and conditional variance are checked independently.
3. **Biased mixture.** For seven exact probabilities
   `0,1/7,1/3,1/2,2/3,6/7,1` and times through 32, all polynomial
   coefficients are mixed exactly. Mass, mean, and variance are compared
   with the closed formulas (231 parameter-time cases).

## Lane B — centered pairs and pressure bounds

1. **Independent variance route.** The shared-index pair-covariance formula
   is evaluated at all 231 biased parameter-time cases and compared both
   with the closed variance and with the finite distribution from Lane A.
2. **Centered decomposition.** For three interior rational probabilities
   and every word through length 12, 24,573 exact word instances compare the
   centered area with separately assembled linear and quadratic parts.
   Weight-square and polynomial residual identities control the CLT
   variance algebra.
3. **Extrema and pressure.** Exact maximum/zero-area probabilities and the
   two-sided exponential-moment bounds are checked for three probabilities,
   three rational tilt bases, and times through 32 (594 inequalities).
4. **Endpoints.** Pure-`X` and pure-`Y` products are checked through time
   100 for zero area, exact Frobenius norm, and letter counts.

## Evidence boundary

The exhaustive ranges are finite proof spikes. They do not prove the strong
law, CLT, norm limit, or pressure limit; those conclusions rest on the
symbolic arguments in `main.tex`. The program does not infer novelty from a
failed search. No assertion merely compares a value with an immediately
identical reassignment.
