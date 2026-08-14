# HCS-P52: Totient Abel law and tagged-mass escape

HCS-P52 resolves the first boundary problem left by HCS-P51 on the exact
primitive period-four Hénon orbit.  For

\[
L=289+24\sqrt{145},\qquad
\beta_n=L^{-\varphi(n)/2}\Phi_n(L),\qquad n\ge3,
\]

the source-tagged packet divisor \(D_n\) has mass

\[
\|D_n\|_{\rm tag}=\log\beta_n
=\frac{\varphi(n)}2\log L+O_L(1),
\]

with the explicit uniform correction smaller than \(0.001735\).  The
elementary average order of Euler's totient function therefore gives the
exact Abel boundary law

\[
\lim_{u\uparrow1}(1-u)^2
\sum_{n\ge3}\|D_n\|_{\rm tag}u^n
=\frac{3\log L}{\pi^2}
=1.9330777456585248\ldots .
\]

There is also a canonical escape profile.  With \(u=e^{-\tau}\), normalize
the packet mass and place its \(n\)th atom at \(\tau n\).  The resulting
probability measures converge weakly to Gamma\((2,1)\), with density
\(xe^{-x}\,dx\).

The positive scalar boundary does **not** lift to the original tagged divisor
space.  The vectors

\[
\tau^2\sum_{n\ge3}e^{-\tau n}D_n
\]

have norms tending to the positive Abel constant, while every fixed tagged
coordinate tends to zero.  They have no norm- or weakly-convergent subnet.
Thus the Gamma law is a scaled-index compactification of escaping mass, not a
lossless prime-ideal boundary value.

## Status

- **PROVED:** uniform totient packet asymptotic;
- **PROVED:** scalar Abel boundary constant;
- **PROVED:** Gamma\((2,1)\) scaled-index escape profile;
- **REFUTED:** norm or weak convergence in the original tagged \(\ell^1\)
  space;
- **OPEN:** pressure-weighted all-orbit boundary interchange, a
  von-Mangoldt trace, a Fredholm determinant and a Hilbert--Pólya operator.

Route A is
\((\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
\mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\mathrm{A4\_FORMAL\_HINT})\)
with overall **ROUTE_A_EXPLORATORY**.  Route B is not authorized.

## Reproduce

```bash
bash code/run_c52.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The compiled article is [paper/paper.pdf](paper/paper.pdf).  The producer
certificate is [results/c52_certificate.json](results/c52_certificate.json),
and the separate verifier emits
[results/c52_independent_check.json](results/c52_independent_check.json).
