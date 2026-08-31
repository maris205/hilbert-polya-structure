# C262 results

## Analytic result

The two-step periodic Hill equation has one exact all-sign `SL(2,R)`
monodromy and discriminant.  Elliptic, hyperbolic, scalar parabolic, and
Jordan parabolic dynamics, integer iterates, growth rates, order swaps, and
all zero/negative/zero-duration faces are completely classified.

## Executable receipt

- 900 all-sign grid rows (`k1,k2` in six values; durations in five values);
- class ledger: 416 elliptic, 384 hyperbolic, 36 plus-identity, and 64
  plus-Jordan grid rows;
- six exact identity/Jordan/hyperbolic boundary witnesses;
- 19,849 independent power-series/matrix assertions;
- 289 exact SymPy identities;
- clean-process byte replay;
- 41/41 repaired-hash semantic mutation rejections.

Hashes are sealed in the release manifest after deterministic paper build.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```

The receipt tests formulas and edge cases; it does not turn a finite grid
into a continuum proof or a target determinant.
