# HCS-P54: A physical pressure pole and the Galois-excess gate

HCS-P54 takes the Mahler-height amplitude isolated in HCS-P53 and separates
its pressure-critical part from its genuinely arithmetic obstruction.  For
every primitive orbit \(\gamma\) of the certified mixing H6 survivor,

\[
\mathcal H_\gamma=\log M(f_{\lambda_\gamma})
=\ell_\gamma+E_\gamma,
\qquad
\ell_\gamma=\log\Lambda_\gamma,
\qquad E_\gamma\ge0.
\]

The physical first-repetition amplitude

\[
\mathcal A_{\rm phys}(s)
=\frac3{\pi^2}\sum_\gamma
\ell_\gamma e^{-s h_*\ell_\gamma}
\]

is the primitive part of the logarithmic derivative of the normalized
suspension zeta.  Parry--Pollicott's source theorem and a normally convergent
repetition tail therefore give a meromorphic germ at \(s=1\) with

\[
\operatorname*{Res}_{s=1}\mathcal A_{\rm phys}(s)
=\frac3{\pi^2h_*}
\in
(1.093445200412297389\ldots,
 1.093472735186032499\ldots).
\]

This is an all-period theorem, not an extrapolation from the three finite
orbits in the certificate.

The same exact rows expose the missing bridge.  Period four has
\(E_4=0\), whereas periods one and three have

\[
E_1=\operatorname{arcosh}(\sqrt7-1)>0,
\qquad
E_3=\operatorname{arcosh}(21\sqrt5-19)>0.
\]

Consequently the full Mahler height cannot be a constant multiple of the
instability roof, even modulo a periodic coboundary.  Defining the positive
excess abscissa \(\sigma_{\rm Gal}\) gives an exact three-regime gate:

- if \(\sigma_{\rm Gal}<1\), the physical pole is the full-amplitude pole;
- if \(\sigma_{\rm Gal}=1\), an additional weighted thermodynamic theorem is
  required to determine the boundary behavior;
- if \(\sigma_{\rm Gal}>1\), the positive defining excess series loses
  convergence before the physical pressure line.

Under the explicit **conditional** hypothesis that one real Hölder
observable has periodic sums \(E_\gamma\), the two-parameter weighted zeta
theorem completes the full simple pole and computes its residue.  That
Hölder realization is not proved here.

## Status

- **PROVED:** canonical nonnegative splitting
  \(\mathcal H_\gamma=\ell_\gamma+E_\gamma\);
- **PROVED:** physical primitive pressure pole and certified residue interval;
- **PROVED:** no constant pressure retuning modulo a coboundary;
- **PROVED:** excess-abscissa trichotomy for the positive defining series;
- **CONDITIONAL_THEOREM:** full pole under one exact Hölder periodic-sum
  realization of \(E_\gamma\);
- **OPEN:** such a realization, an asymptotically additive replacement, or a
  direct determination of \(\sigma_{\rm Gal}\);
- **OPEN:** rational-prime trace, completed determinant, and Hilbert--Pólya
  operator.

Route A is
`(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only],
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)` with overall
`ROUTE_A_EXPLORATORY`.  The full Galois-weighted candidate has no A2 pass.
Route B is not authorized.

## Reproduce

```bash
bash code/run_c54.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The final manuscript is [`paper/paper.pdf`](paper/paper.pdf).  Exact results,
independent checks, hostile reviews, source provenance and the claim firewall
are retained in `results/` and `notes/`.
