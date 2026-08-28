# HCS-C213 — circular telegraph Fourier and essential-norm atlas

This package freezes the velocity-jump process on the circle
\(\mathbb T_{2\pi}\): \(\dot x=cv\) with \(v\in\{+1,-1\}\) flipping at rate
\(\lambda\), for \(c,\lambda\geq0\).  Its source-owned theorem gives every
Fourier block, the exact matrix exponential (including the critical Jordan
case), the telegraph equation, the sharp spectral-abscissa gap, stationary
boundaries, and the essential-norm obstruction.

The finite receipt contains 25 rational parameter pairs, seven Fourier modes,
and four physical times.  These rows are regression witnesses only; the
all-mode statements are proved from the block identity and high-frequency
limit.  A gap is explicitly a spectral-abscissa gap, not a claim of
constant-free \(L^2\) operator-norm decay at non-normal or critical blocks.

## Reproduce

```text
python3 code/c213_telegraph_producer.py
python3 code/c213_telegraph_checker.py
python3 code/c213_telegraph_sympy_crosscheck.py
python3 code/c213_telegraph_replay.py
python3 code/c213_telegraph_mutation.py
python3 code/c213_release_manifest.py
```

The manuscript is [paper/main.pdf](paper/main.pdf); the exact receipt is
`results/c213_telegraph_evidence.json`.  Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`, and Route B is not authorized.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
