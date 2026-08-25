# C141 results

## Headline result

For \(F(z)=z^2-6\), the two inverse branches on \(\mathbb D_4\) define a trace-class \(m=2\) Hardy operator with

\[
\operatorname{Tr}\mathcal L_2^n
=\sum_{F^n(p)=p}\frac1{\Lambda_n(p)(\Lambda_n(p)-1)}
\]

at every period. All periodic points are exhausted by inverse words. The Fredholm determinant is entire, while its displayed primitive product is proved absolutely convergent for \(|u|<4\) and begins at stability index \(k=2\).

## Exact evidence prefix

- periods: 1–6; rooted periodic points: 126; primitive orbits: 23;
- traces: `1/12`, `7/720`, `239/257472`, `1255703/13810694400`, `235072563599/26491011084499968`, and `655398850662090042240821783/756396676602907446734765701632000`;
- determinant coefficients through degree six are stored exactly in the evidence;
- \(m=0\): traces \(2^n\), determinant \(1-2u\);
- \(m=1\): zero traces, determinant \(1\).

Evidence SHA-256: `50fc0cd938850df871f054e865a8dbbaec732bd715caa21acd064a764c657665`.

## Progress over the prior gate

This is the first package in the series that combines a single nonlinear complex polynomial, intrinsic inverse branches, unconditional Hardy nuclearity, all-period point exhaustion, and a nontrivial stability-weighted trace ladder. It is not a target-facing result.

Strict verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; Route B false.
