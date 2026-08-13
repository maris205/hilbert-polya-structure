# HCS-C40: Kummer Schatten phase diagram and clock obstruction

Status: `PROVED_ANALYTIC_DETERMINANT_NONCANONICAL_CLOCK`.

C40 applies the only direct convergence repair left by C39.  On
\(\mathcal H=\bigoplus_p\mathbf C^3\), let

\[
T_\sigma=\bigoplus_p p^{-\sigma}U_p,
\]

where each \(U_p\) is a three-channel unitary Kummer permutation.

## Main theorem

For \(0<q<\infty\),

\[
T_\sigma\in\mathcal S_q
\quad\Longleftrightarrow\quad \sigma q>1.
\]

Thus `compact iff sigma>0`, `Hilbert--Schmidt iff sigma>1/2`, and
`trace class iff sigma>1`.  In the trace-class region the ordinary Fredholm
determinant exists.  At and below \(\sigma=1\), it does not.

The positive determinant is not a H\'enon/Kummer promotion.  The unramified
three-channel system has Artin conductor exponent zero at every \(p\ne3\),
so it supplies no intrinsic \(p^{-\sigma}\) decay.  The damping is an
external second clock chosen to force convergence.

## Research extraction

- **Strongest positive result:** exact all-prime Schatten phase diagram and
  an ordinary determinant for every \(\sigma>1\).
- **Strongest obstruction:** the only source-native conductor is supported
  at the finite bad-prime set and cannot generate the required decay.
- **Open theorem:** build a genuinely arithmetic cubic object whose local
  Frobenius data include intrinsic square-root normalization.
- **Reusable structure:** fixed-rank prime-block Schatten criterion.
- **ROUND2_CLUE:** replace artificial damping by a geometric Kummer
  cohomology object, accepting that its global function may be an
  elliptic/Hecke \(L\)-function rather than \(\zeta\).

## Route evaluation

`(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FORMAL_HINT)` with overall
`ROUTE_A_EXPLORATORY_NONCANONICAL`. Route B is not authorized.

## Reproduce

```bash
python -B code/c40_schatten_checker.py
python -B -m unittest code/test_c40.py
```

Paper: [`paper/paper.pdf`](paper/paper.pdf).
