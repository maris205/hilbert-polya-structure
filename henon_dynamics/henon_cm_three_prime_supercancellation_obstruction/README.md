# HCS-C42: three-prime cohomological supercancellation obstruction

Status: `PROVED_FINITE_COHOMOLOGY_LOCAL_RIGIDITY`.

C42 performs the local compatibility test selected by C41.  At a good prime,
allow an arbitrary integral virtual combination of

- the degree-zero Tate factor \((1-T)^{-1}\);
- the CM elliptic factor \((1-a_pT+pT^2)^{-1}\);
- the degree-two Tate factor \((1-pT)^{-1}\).

Write the exponents as \((A,B,C)\in\mathbf Z^3\).

## Main theorem

If this virtual factor equals the Riemann local factor \((1-T)^{-1}\) at
just \(p=5,7,11\), then

\[
(A,B,C)=(1,0,0).
\]

Indeed, the first logarithmic coefficients give

\[
A+5C=1,
\quad A-4B+7C=1,
\quad A+11C=1,
\]

whose determinant has absolute value \(24\).  Therefore every nontrivial use of the cubic
CM \(H^1\) factor changes the local Riemann ledger.  Exact
supercancellation can return to zeta only by deleting the new geometry.

## Scope

This is a complete no-go for this finite three-generator Euler-factor
category.  It does not classify infinite-rank complexes, non-Euler global
scattering determinants, or a genuinely new H\'enon trace formula with
prime-dependent coefficients.

## Research extraction

- **Strongest positive result:** a three-prime exact local rigidity theorem.
- **Strongest obstruction:** the only Riemann-matching virtual class is the
  undecorated \(H^0\) zeta factor.
- **Open theorem:** construct a source-native infinite/local-complex object
  outside the finite Tate-plus-CM span, or prove such objects also reduce.
- **Reusable structure:** first-logarithmic-coefficient rank test for virtual
  Euler factors.
- **ROUND2_CLUE:** any future bridge must introduce genuinely new
  prime-dependent trace functions, not fixed finite combinations of
  \(1,a_p,p\).

## Route evaluation

`(A1_WEAK, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED_FINITE_CUBIC_COHOMOLOGY`.  The limited Route-B audit stops
at B1 and records a formal B4 local-trace mismatch for every nontrivial class.

## Reproduce

```bash
python -B code/c42_rigidity_checker.py
python -B -m unittest code/test_c42.py
```

Paper: [`paper/paper.pdf`](paper/paper.pdf).
