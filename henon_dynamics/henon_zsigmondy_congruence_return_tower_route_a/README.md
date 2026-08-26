# HCS-C179: Zsigmondy congruence-return tower

For coprime integers \(a>b\geq1\), this package studies the source-defined
finite dynamics

\[
R_{a,b,N}(x)=ab^{-1}x\quad\hbox{on}\quad
U_N=(\mathbb Z/N\mathbb Z)^\times ,\qquad (N,ab)=1,
\]

with marked point \(1\).  A prime \(p\) is a primitive divisor of
\(a^n-b^n\) exactly when that marked point first returns at time \(n\) on
the \(p\)-fiber.  The existence statement and its two exception families
are the classical Zsigmondy theorem, explicitly attributed rather than
claimed new.  The new package-level increment is one uniform dynamical
ledger: exact lifting to every \(p^k\), the full cycle/zeta/determinant and
reversor law on every admissible finite fiber, and a comparison of two
natural globalizations.

The disjoint union of finite fibers has fixed ledger \(a^n-b^n\) and source
zeta \((1-bz)/(1-az)\).  The profinite inverse-limit translation has no
positive-time fixed point and source zeta \(1\).  Their incompatibility is a
no-go for selecting a unique global determinant owner from the finite-fiber
data alone; it is not a claim that every possible enlarged construction is
impossible.

Route-A verdict:

`(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL,
A4_NATURAL_QUANTIZATION)`; overall `ROUTE_A_EXPLORATORY`; Route B remains
unauthorized.  A0 is weak, not passed: rational primes arise intrinsically
as first-return moduli, but there is no selected global prime-orbit owner and
no logarithmic prime clock.

## Reproduce

```bash
python3 code/c179_zsigmondy_return_producer.py
python3 code/c179_zsigmondy_return_checker.py
python3 code/c179_sympy_crosscheck.py
python3 code/c179_replay.py
python3 code/c179_mutation.py
python3 code/c179_release_manifest.py
```

The paper is `paper/main.pdf`.  The release contains 27 content-addressed
payload files plus the self-excluded manifest.  The scope literal is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
