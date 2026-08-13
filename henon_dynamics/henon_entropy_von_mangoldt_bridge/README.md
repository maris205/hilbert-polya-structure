# HCS-C43: entropy--von Mangoldt bridge on the Hénon survivor

This project returns from the exhausted finite CM branch to the autonomous
all-period Hénon chronology.  For the certified four-state survivor of

\[
H_6(q,p)=(1-6q^2-p,q),
\]

the exact marked period count is (N_n=\operatorname{tr}(A^n)), with
Perron root (\varphi).  If (E_n) is the exact-period marked count and
(P_n=E_n/n) the primitive-orbit count, then the prime number theorem gives

\[
E_n\sim\vartheta(\varphi^n),\qquad
P_n\sim(\log\varphi)\pi(\varphi^n).
\]

Thus the intrinsic entropy clock aligns the Hénon marked chronology with
von Mangoldt mass without reading or fitting a prime table.  The result is a
real positive structural bridge, but it is only a mass law: it supplies no
individual orbit--prime correspondence, weighted Riemann determinant, or
operator.

## Reproduce

```bash
bash code/run_c43.sh
cd paper && pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

## Status

- strongest positive result: `PROVED` entropy--PNT mass bridge;
- strongest obstruction: no source-native individual prime labels;
- open theorem: construct or rule out such a label while preserving
  repetitions and amplitudes;
- Route A: `ROUTE_A_EXPLORATORY`;
- Route B: not authorized.
