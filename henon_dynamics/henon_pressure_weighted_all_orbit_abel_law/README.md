# HCS-P53: Pressure-weighted all-orbit Abel law

HCS-P53 closes the principal theorem left open by HCS-P52.  For every
primitive orbit \(\gamma\) in the certified H6 survivor, let

\[
b_{\gamma,n}=\log|N_{F_\gamma/\mathbb Q}\beta_{\gamma,n}|,
\qquad
\mathcal H_\gamma=\log M(f_{\lambda_\gamma}),
\]

where \(\beta_{\gamma,n}\) is the inversion-fixed half-cyclotomic packet
and \(\mathcal H_\gamma\) is the Mahler spectral height of the signed
multiplier.  The project proves

\[
b_{\gamma,n}
=\frac{\varphi(n)}2\mathcal H_\gamma
+O_\gamma\!\left(\sqrt n(1+\log n)^2\right).
\]

Together with the uniform P51 orbit envelope, this yields the locally
uniform all-orbit boundary law

\[
\lim_{\tau\downarrow0}\tau^2
\sum_\gamma e^{-s\widehat\ell_\gamma}
\sum_{n\ge3}b_{\gamma,n}e^{-\tau n}
=\frac3{\pi^2}\sum_\gamma
e^{-s\widehat\ell_\gamma}\mathcal H_\gamma
\]

throughout the certified P51 half-plane
\(\Re s>\log(2\phi)/(h_*\log J_*)\), numerically
\(\Re s>3.125206884004728\ldots\).

For every real \(\sigma\) in that half-plane, the joint orbit and scaled
cyclotomic-index probability converges to

\[
\pi_\sigma\otimes\Gamma(2,1),
\qquad
\pi_\sigma(\gamma)\propto
e^{-\sigma\widehat\ell_\gamma}\mathcal H_\gamma.
\]

The positive tagged divisor vectors still have no norm- or weakly
convergent boundary subnet.  The theorem is scalar and pressure-safe; it
does not continue the amplitude to a pressure singularity and does not
construct a rational-prime trace, determinant, or operator.

## Status

- **PROVED:** one-orbit Mahler-height packet asymptotic;
- **PROVED:** pressure-weighted all-orbit Abel interchange in the P51 safe
  half-plane;
- **PROVED:** locally uniform complex-\(s\) limit and joint
  orbit--index product law;
- **REFUTED:** norm or weak boundary in the source-tagged Banach space;
- **OPEN:** pressure-critical continuation, von Mangoldt trace, determinant,
  and Hilbert--P\'olya operator.

Route A remains
`(A1_WEAK, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` with
overall `ROUTE_A_EXPLORATORY`.  Route B is not authorized.

## Reproduce

```bash
bash code/run_c53.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The compiled manuscript is [`paper/paper.pdf`](paper/paper.pdf).
