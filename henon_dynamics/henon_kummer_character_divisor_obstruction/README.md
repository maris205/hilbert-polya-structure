# HCS-C39: Kummer character divisor obstruction

Status: `PROVED_ALL_PRIME_DIVISOR_OBSTRUCTION`.

C39 studies the smallest nonfunctorial survivor of C38: an intrinsic
three-channel permutation with eigenvalues \(1,\zeta_3,\zeta_3^2\).  A
virtual grading has multiplicities \(m=(m_0,m_1,m_2)\in\mathbf Z^3\).

## Main theorem

For every prime \(p\), freeze the critical-normalized local factor

\[
F_{p,m}(s)=\prod_{j=0}^{2}
  (1-\zeta_3^j p^{1/2-s})^{m_j}.
\]

If \(m\ne0\), zeros or poles of \(F_{p,m}\) approach \(s=1/2\) as
\(p\to\infty\).  Hence the all-prime divisor is not locally finite and
cannot belong to a nonzero meromorphic function near \(1/2\).  Exact
all-repetition supertrace cancellation is possible only for \(m=0\).

Thus channel permutation survives C38 algebraically but fails the raw
all-prime determinant gate.  This is stronger than a finite zero mismatch:
it is an interior divisor-accumulation theorem.

## Research extraction

- **Strongest positive result:** complete Fourier classification of all
  three-channel virtual repetition traces.
- **Strongest obstruction:** every nonzero virtual channel has an interior
  zero/pole accumulation at \(s=1/2\).
- **Open theorem:** determine whether an intrinsic conductor damping can make
  the prime assembly determinant class without inserting a fitted clock.
- **Reusable structure:** finite-character divisor accumulation theorem.
- **ROUND2_CLUE:** a viable graded assembly must decay with \(p\), not merely
  have zero superdimension or periodic trace cancellation.

## Route evaluation

`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED_RAW_KUMMER_PRODUCT`. Route B is not authorized.

## Reproduce

```bash
python -B code/c39_character_checker.py
python -B -m unittest code/test_c39.py
```

Paper: [`paper/paper.pdf`](paper/paper.pdf).
