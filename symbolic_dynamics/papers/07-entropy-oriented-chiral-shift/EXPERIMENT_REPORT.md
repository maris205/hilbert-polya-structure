# Paper07 Experiment Report

## Outcome

SD-C09 passes its exact finite-prefix ledger and non-gauge-motion tests.  It
does **not** pass a unified-divisor test.  The decisive positive fact is that
entropy-oriented successor edges change singular/chiral data while remaining
outside every periodic word.  The decisive negative fact is that arbitrary
forward DAGs, shuffled masses, composites, random integers, and randomized
forward endpoint phases do the same thing.  Thus the mechanism is a useful
symbolic construction but, by itself, proves too much for an RH divisor.

No Riemann-zero data were loaded or fitted.

## Exact ledger and graph audit

For opaque variables `x0,...,x3`, symbolic algebra verified through power 8

```text
Tr L^r = sum_j x_j^r,
det(I-zL) = product_j (1-z x_j).
```

All eight identities and the determinant identity are exact.  The directed
five-state successor graph has exactly five based closed walks at every
length 1 through 8, all pure loops and no mixed walk.  With reverse successor
edges, the length-two census changes to 7 closed walks, 4 mixed, and the exact
trace defect is

```text
(x0^2 + 2*x0*x1 + 2*x1^2 + 2*x1*x2 + x2^2)/2.
```

The bidirectional determinant therefore fails the Euler ledger.

## Gauge and endpoint controls

For a frozen dense complex random `K` of size 7,

```text
D_(1/2+it)K = U_t D_(1/2)K,
B_t = diag(U_t,I) B_0 diag(U_t,I)^*.
```

The maximum residuals over seven heights were:

| check | maximum residual |
|---|---:|
| left-phase identity | `6.05e-16` |
| chiral conjugacy | `8.56e-16` |
| singular values | `8.89e-16` |
| chiral eigenvalues | `2.67e-15` |

Hence noncommutation of `K` is irrelevant in the one-sided ansatz.

For `N=8`, heights `0 <= t <= 40`, and 801 frozen samples:

| alpha | Schatten-4 fourth-power range | max singular-value L2 shift | motion |
|---:|---:|---:|:---:|
| 0 | `1.11e-15` | `6.73e-16` | no |
| 0.125 | `0.637983` | `0.163529` | yes |
| 0.25 | `1.053252` | `0.300095` | yes |
| 0.5 | `1.395631` | `0.420600` | yes |
| 0.75 | `1.139314` | `0.267696` | yes |
| 0.875 | `0.713287` | `0.143503` | yes |
| 1 | `2.22e-15` | `5.62e-16` | no |

The endpoint controls are gauge-trivial.  The symmetric average has strict
motion, already certified exactly at `N=2` by the nonconstant polynomial

```text
||L_t||_4^4 = c^2/24 + 25*sqrt(6)*c/144 + 433/576,
c = cos(t log(3/2)).
```

## Finite determinant, reflection, and exact crossing

For `N=8`, seven symmetric heights gave zero antiunitary-conjugation and
block-determinant residual at binary64 display precision; the reflection
scalar residual was at most `1.83e-18`.  Also `Tr B_t=0`, and

```text
det_3(I-B_t) = det(I-B_t) exp(Tr(B_t^2)/2),
```

where the exponential is strictly positive.  Therefore the two finite
determinants have the same `z=1` crossings.

For atoms 2 and 3,

```text
det(I-L_t^*L_t) = (3-2*sqrt(6)*cos(t log(3/2)))/24,
t = (2*pi*k +/- acos(sqrt(6)/4))/log(3/2).
```

The recurrence/dense determinant audit over 20 cases had maximum absolute
error `4.03e-16`; the numerical `N=2` roots agree with the exact family to
`5.69e-14` or better.

## Frozen sign-change census

The positive-axis sign-changing bracket counts were identical at all eight
cutoffs.  The validation grid obtained the same counts.

| cutoff N | last atom | T=20 | T=40 | T=80 | T=160 | T=320 | step-halving stable |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 2 | 3 | 3 | 5 | 11 | 21 | 41 | yes |
| 3 | 5 | 3 | 5 | 11 | 21 | 41 | yes |
| 4 | 7 | 3 | 5 | 11 | 21 | 41 | yes |
| 8 | 19 | 3 | 5 | 11 | 21 | 41 | yes |
| 16 | 53 | 3 | 5 | 11 | 21 | 41 | yes |
| 32 | 131 | 3 | 5 | 11 | 21 | 41 | yes |
| 64 | 311 | 3 | 5 | 11 | 21 | 41 | yes |
| 128 | 719 | 3 | 5 | 11 | 21 | 41 | yes |

The first five roots at `N=128` are

```text
2.8250629465839407
12.1389759734344801
17.7846409577422873
28.4611870662899581
33.7066984259288109
```

At 150-decimal precision, the first-root changes are `3.516e-13`,
`3.660e-38`, and `1.734e-100` for `8 -> 16 -> 32 -> 64`; the displayed
`64 -> 128` change is below the retained precision.  This is extremely fast
numerical cutoff stabilization, not a proof of exact stabilization.

The count grows linearly in these windows and inherits the exact periodic
two-atom mechanism.  It is not the Riemann--von Mangoldt law.  The scan does
not detect even-multiplicity tangencies and is not an argument-principle
certification.

## Adversarial controls

All four inventory controls retain the triangular ledger and show motion:

| inventory | Schatten-4 range | Route-A interpretation |
|---|---:|---|
| entropy-ordered tensor atoms | `1.395631` | passes intrinsic-source definition |
| shuffled same atoms | `1.690239` | destroys entropy order |
| composites only | `0.411788` | fails tensor-atom source |
| matched-count random integers | `0.466588` | fails tensor-atom source |

Random endpoint phases on forward edges also retain the **all-order** ledger
exactly and show range `1.060955`.  This corrects the weaker expectation that
random phases might fail only at high order: triangularity makes every
forward-edge phase trace-invisible.  It is a `PROVES_TOO_MUCH` control.

All 24 frozen random upper-DAG seeds showed singular motion.  Their
Schatten-4 ranges had mean `3.474582`, minimum `0.434125`, and maximum
`11.056002`, while an exact opaque four-state random DAG retained trace powers
1 through 8 and the full determinant product.  This is the strongest
specificity warning.

## Virtual-character rigidity context

The pure-power language has a total-dimension-minimal `3|0` realization
`rho(a_i)=E_ii`.  A common strictly upper-triangular radical makes the
matrices noncommuting without changing any word trace or determinant.  A
nontrivial `4|1` graded realization copies one scalar character in even and
odd parity, cancelling it at every word.  Each construction passed all 3,279
words of length at most 7 and the exact Berezinian product.

The ordinary singular spectra nevertheless move strongly with the radical
or graded scale.  The positive connected rank-one control preserves pure
powers but leaks mixed traces (maximum `0.093061`); 32 trace-normalized random
signed controls had mean pure RMS error `0.637742` and mixed RMS leakage
`0.202913`.  Strict nilpotents and truncated free-group regular traces give
zero on pure words, so they cannot supply the required value one.

This context proves that cyclic traces and (super)determinants see the
semisimple/virtual ledger but not nonnormal radical geometry.  It supports
the SD-C09 rigidity interpretation; it is not a second promoted candidate.

## Claim boundary and next experiment

```text
exact Euler ledger:                         PROVED
universal one-sided no-motion identity:     PROVED
symmetric successor chiral motion:          PROVED
finite exact crossing family:               PROVED
cutoff sign-change stability:                NUMERICAL_OBSERVATION
single continued Euler/chiral determinant:  OPEN
Riemann-von Mangoldt counting law:           REFUTED for the N=2 mechanism;
                                             OPEN for a distinct infinite object
completed-xi divisor / Hilbert-Polya claim:  NOT ESTABLISHED
```

The next smallest same-family test is an analytic infinite-cutoff theorem for
the continuant `det(I-L_t^*L_t)`: prove locally uniform convergence and
classify its real zero count, then determine whether that object has any
source-internal relative-determinant bridge to the Euler Fredholm product.
No Route-B promotion is authorized.

## Artifacts

- `code/sdc09_successor_experiment.py`
- `code/virtual_character_context.py`
- `code/test_sdc09_successor_experiment.py`
- `results/sdc09_results.json`
- `results/virtual_character_results.json`

Verification: `7 passed in 2.03s`.
