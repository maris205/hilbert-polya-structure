# HCS-C145: Rule-90 two-clock periodic geometry

This package proves, for all positive spatial lengths `L` and temporal periods
`n`,

```text
#Fix(F_L^n)=2^deg gcd(x^L+1,(x^2+1)^n+x^n) over F_2.
```

It includes even non-squarefree lengths, gives exact-period points and
primitive temporal cycles by Möbius inversion, and identifies fixed points
with labeled `L x n` spatiotemporal tori.  A complete `24 x 24` ledger freezes
aspect-ratio and divisor-history witnesses.

Run:

```bash
python3 code/c145_rule90_producer.py
python3 code/c145_rule90_checker.py
python3 code/c145_sympy_crosscheck.py
python3 code/c145_replay.py
python3 code/c145_mutation.py
python3 code/c145_release_manifest.py
```

Route-A verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall exploratory,
Route B false.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
