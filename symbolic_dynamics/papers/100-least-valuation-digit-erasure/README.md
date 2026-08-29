# P100 — Least-valuation digit erasure

Internal Route-A short paper on the absorbing map

\[
E(0)=0,\qquad E(x)=x-p^{v_p(x)}
\]

on the standard representatives of $\mathbb Z/p^r\mathbb Z$.

The paper proves that the hitting time of zero is exactly the base-$p$ digit
sum. It derives the full transient-depth polynomial, every layer,
nilpotency depth, moments, fixed-base central/local limits, and parameter
recovery. Every member has the same periodic sequence and zeta, making the
rigidity of the transient profile the central dynamical contrast.

## Frozen residual claims

- $\tau(x)=s_p(x)$ and maximum depth $(p-1)r$.
- $\sum_xu^{\tau(x)}=(1+u+\cdots+u^{p-1})^r$, including an exact coefficient
  formula, symmetry, and unimodality.
- Exact mean/variance and owner-subtracted iid lattice limits.
- $\operatorname{Fix}(E^n)=1$ and $\zeta_E=(1-z)^{-1}$ for all parameters.
- The coefficient of $u$ and the polynomial degree recover $(p,r)$.
- The binary specialization is Wegner's classical rightmost-one clearing
  step and is explicitly subtracted from the residual claim.

## Reproduce

~~~bash
python code/verify_digit_erasure.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

External circulation and priority language remain **HOLD**.
