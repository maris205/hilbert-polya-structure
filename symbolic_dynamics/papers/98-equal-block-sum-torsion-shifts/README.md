# P98 — Equal-block-sum torsion shifts

Internal Route-A short paper on the finite-field subshift

\[
\sum_{j=0}^{r-1}x_{i+j}=\sum_{j=r}^{2r-1}x_{i+j}.
\]

The paper proves an affine residue-class normal form, identifies the
companion polynomial $(z^r-1)^2/(z-1)$, and gives every fixed count in every
characteristic. Möbius inversion then supplies the complete temporal cycle
census and finite Artin–Mazur zeta. The result includes nonprime fields and
all torsion endpoints.

## Frozen residual claims

- $|X_{q,r}|=q^{2r-1}$ and $\sigma^r(a,d)=(a+d,d)$.
- The repeated-root fixed dimension
  $D_r(n)=\min(2p^a-1,p^b)+(\gcd(r_0,n_0)-1)\min(2p^a,p^b)$.
- Exact shift order 1 for $r=1$ and $pr$ for $r>1$.
- Every least-period count, finite zeta, and recovery of $(q,r)$ from the
  fixed sequence.
- Explicit subtraction of algebraic-shift, companion-network, repeated-root,
  and general zeta ownership.

## Reproduce

~~~bash
python code/verify_equal_block_sum.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The exact program uses polynomial gcds, literal matrix ranks, and full state
enumeration over prime and nonprime fields. External circulation remains
**HOLD**.
