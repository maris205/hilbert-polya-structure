# C122 — adaptive-feedback Hénon automorphism

This package freezes the three-dimensional polynomial map

\[
G(x,y,a)=\left(x^2+a-y,\ x,\ \frac a2+3x-\frac12\right).
\]

The third coordinate is an evolving parameter driven by the present Hénon
state.  The package certifies its polynomial inverse, constant Jacobian
determinant `1/2`, two algebraic fixed points, and the oriented primitive
two-cycle

\[
(1,-1,-3)\longleftrightarrow(-1,1,1).
\]

The gain-zero and neighboring-gain controls show that the named cycle is not
inherited from an unforced parameter coordinate.  This remains a low-period
certificate: the tangent monodromy is not a transfer/Fredholm determinant and
no complete orbit atlas is claimed.  There is no prime-like target
correspondence, target-divisor match, or analytic bridge.  The canonical
verdict is `A1_WEAK / A2_FAIL / A3_FAIL / A4_FAIL`, overall
`ROUTE_A_EXPLORATORY`.  The literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python3 code/c122_adaptive_producer.py
python3 code/c122_adaptive_checker.py
python3 code/c122_sympy_crosscheck.py
python3 code/c122_replay.py
python3 code/c122_mutation.py
python3 code/c122_release_manifest.py
```

The compiled paper is [paper/main.pdf](paper/main.pdf), and the content ledger
is [C122_PREFREEZE_MANIFEST.json](C122_PREFREEZE_MANIFEST.json).
