# C256 results

## Analytic result

The cubic first integral exhausts every bounded classical real KdV traveling
profile.  Three simple roots give the translated `cn^2` family; a lower
double root gives the `sech^2` homoclinic; every remaining root topology has
only bounded constants.  Speed, fundamental period, first two period moments,
Galilean covariance, soliton/harmonic limits, and the fundamental-circle
clock are exact.

## Executable receipt

- 12 ordered rational-root periodic rows;
- 3 soliton, 3 harmonic, and 6 Galilean boundary rows;
- 90 working decimal digits and 75 printed significant digits;
- 602 independent-checker assertions, including root-regularized period and
  two-moment quadratures plus independent elliptic nodes;
- 245 SymPy identities over the cubic, `cn^2`, soliton, and Galilean grids;
- clean-process byte replay;
- 49/49 repaired-hash semantic mutation rejections.

Evidence payload SHA-256:
`1ff32a11f166f6a3f17fe14613878d2c7c3d123d1e33a13c5d857392a9d2be92`.

Evidence-file SHA-256:
`0cdf43e788abc9c76374e2b2ceea00c0388420902c92fafb2861f89686860bb4`.

Final PDF SHA-256:
`803a7637889627a99cd962a97ad1798719424a33b6e9d6bdbcd828cb5b5d186e`.

## Decision

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```

Finite receipts verify formulas and conventions, not the continuum theorem
by enumeration.  No arbitrary-solution classification, stability theorem,
target determinant, arithmetic local data, or Hilbert--Pólya claim follows.
