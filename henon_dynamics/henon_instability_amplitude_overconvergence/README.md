# HCS-C44: instability-amplitude compiler and critical overconvergence

For the certified (H_6) survivor, one primitive instability Euler factor
has the exact logarithmic derivative

\[
\partial_s\log(1-|\Lambda_\gamma|^{-s})
=\sum_{r\ge1}\ell_\gamma|\Lambda_\gamma|^{-rs}.
\]

At (s=1/2+it), this is precisely the von Mangoldt prime-power atom if
(|\Lambda_\gamma|=p).  The local compiler is therefore exact.

The global hostile check is negative.  The inherited uniform expansion
constant (J_*=(\sqrt{17}+\sqrt{13})/2) implies absolute convergence for

\[
\Re s>\frac{\log\varphi}{\log J_*}=0.35598\ldots,
\]

including the critical line.  By the prime number theorem, the all-prime
absolute von Mangoldt mass diverges at (\Re s=1/2).  Hence the raw
instability clock cannot support an all-prime termwise bridge, even though
every individual repetition has the right formula.

## Reproduce

```bash
bash code/run_c44.sh
cd paper && pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Status: `ROUTE_A_REJECTED` for the raw clock.  The pressure-normalized roof is
the next distinct candidate.
