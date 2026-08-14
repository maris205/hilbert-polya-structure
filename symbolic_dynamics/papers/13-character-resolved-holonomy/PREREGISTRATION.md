# Paper13 Preregistration

## Research question

Can the canonical Bloch decomposition of a positive-cone `Z`-extension keep
the tensor-prime Euler ledger in Fourier degree zero while producing an
intrinsic, arithmetic-selective transverse determinant response?

## Frozen hypotheses

1. **H1 -- lifted ledger.** Every mixed base closed path has strictly positive
   cocycle charge, so no mixed path is periodic in the `Z`-lift.
2. **H2 -- resolved determinant.** For `Re(s)>1`, every Bloch fiber is trace
   class and its Fredholm determinant is analytic in `(s,z,w)`.
3. **H3 -- exact zero mode.** The degree-zero coefficient of every power trace
   is `sum_p p^(-rs)`, hence the zero mode of the trace-log is exactly the
   reciprocal Euler product.
4. **H4 -- character visibility.** For the frozen real points `s>1` and
   `0<z<2^s`, the nonzero Fourier coefficients are nonvanishing and the
   finite-fiber determinant generically changes with `theta` once recurrent
   cross amplitudes are nonzero.  No claim is made at exceptional complex
   cancellations or at `z=0`.
5. **H5 -- holonomy trilemma.** Requiring inverse labels on reversed edges
   returns every adjacent two-cycle to charge zero and contaminates the
   ledger at power two.  Coboundary phases are gauge-trivial.  Positive
   charges preserve the zero mode but break inverse time reversal.
6. **H6 -- specificity test.** If matched composite, random, shuffled, or
   random-positive-charge controls reproduce the response, it is marked
   `PROVES_TOO_MUCH` and cannot upgrade A3 or Route B.

## Exact smallest case

For two masses `x,y`, symmetric cross amplitude `a=(x+y)/2`, and common
positive character `w`,

```text
det(I-z L(w)) = (1-zx)(1-zy) - z^2 a^2 w^2.
```

The constant `w` coefficient is the pure-loop determinant, while the first
transverse term is the charged two-edge return.  With inverse charges
`w,w^(-1)`, the same mixed term moves into Fourier degree zero.

## Frozen experiment matrix

- atom cutoffs: `N in {2,3,4,8,16,32,64,128}`;
- exact path powers: `r=1,...,12` for `N<=5`;
- complex source points: `s in {1.25,1.5,2,1.5+0.75i}`;
- determinant variable: `z in {0.15,0.35,0.6}` when the trace-log branch is
  used;
- characters: `theta=2*pi*j/1024`, all `j`, with no best-character selection;
  Fourier coefficients are extracted from the determinant continuant as
  polynomials, so the grid is a visualization/check rather than an aliased
  coefficient estimator;
- controls: tensor primes; the first `N` composite integers; a prime
  permutation from `random.Random(13013)`; a sorted size-`N` sample without
  replacement from `range(2,16*N+2)` using `random.Random(13014)`; forward
  DAG; inverse charges; entropy/rank coboundaries; entropy-roof twist; and 32
  directed positive-charge fields generated with seeds `15000,...,15031`,
  independently uniform on `{1,2,3}` for every directed cross edge;
- arithmetic: exact integers/rationals or symbolic polynomials where
  possible; numerical determinants use binary64 and selected 80-digit
  confirmation points.

## GO / STOP rules

- `GO_CHARACTER_RESOLUTION` requires H1--H4 with the same frozen object.
- The frozen response statistic is the normalized nonconstant coefficient
  energy of the finite determinant polynomial,

  ```text
  E = sqrt(sum_(m>=1) |d_m|^2) / |d_0|,
  D_N(s,z,w)=sum_m d_m w^m,
  ```

  reported at every frozen point and summarized at
  `(N,s,z)=(32,1.5,0.35)`.
- `GO_ARITHMETIC_SELECTIVITY` additionally requires `E>10^(-8)` for the
  tensor-prime inventory and exact polynomial collapse `E=0` (numerically at
  most `10^(-12)`) for every composite, shuffled, random-increasing, and
  positive-random-charge control, consistently at `N=16,32,64`.
- `STOP_ARITHMETIC_SELECTIVITY` fires if the response is generic across
  inventories or charge fields.
- `STOP_TIME_REVERSAL` fires if inverse/reversal labels create the predicted
  degree-zero two-cycle.
- `NOT_TESTABLE` applies if any determinant, Fourier coefficient, charge,
  branch, or cutoff convention changes after inspecting results.

No Riemann-zero, target crossing, or fitted spectral data are authorized.
All target-zero error/count fields in Route-A evaluation remain
`not_applicable`.
