# HCS-C46: all-period integral Hénon monodromy units

For the autonomous integral Hénon map (H_6), set (x_i=6q_i).  Every
period-(n) fixed scheme is then defined over (\mathbb Z) by

\[
x_i^2+x_{i-1}+x_{i+1}-6=0.
\]

These monic cyclic equations form a Gröbner basis with square-free standard
monomials, so the fixed algebra is finite free of rank (2^n).  The
chronological derivative steps are

\[
J_i=\begin{pmatrix}-2x_i&-1\\1&0\end{pmatrix}\in SL_2.
\]

Consequently every return trace is an algebraic integer and every multiplier
is an algebraic unit.  This is an all-period theorem covering every geometric
periodic point, not just the real survivor.  Exact sentinels through period
10 recover the fixed-point multiplier quartic

\[
X^4-4X^3-22X^2-4X+1.
\]

The theorem gives genuine arithmetic structure but no rational-prime label;
it deliberately leaves ( |\Lambda|^{h_*} ) outside its conclusion.

## Reproduce

```bash
bash code/run_c46.sh
cd paper && pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```
