# P115 — Bounded Cartier-operator dynamics

Anonymous compact `amsart` author draft for the map

\[
\mathcal C\!\left(\sum_{j=0}^{n}c_jx^j\right)
=\sum_{pj\le n}c_{pj}^{1/p}x^j
\quad\text{on }\mathbb F_{p^a}[x]_{\le n}.
\]

The manuscript proves an exact bounded temporal and component package:

1. an explicit `F_p`-coordinate conjugacy to inverse Frobenius times finite
   nilpotent index-chain shifts, including weak components and attached trees;
2. every coefficient iterate;
3. every iterated image and every fibre, including empty fibres;
4. the core-entry CDF, every shell, sharp maximum depth, and deepest-shell size;
5. the inverse-Frobenius periodic core, fixed sequence, exact cycles, and zeta;
6. exact layerwise stabilization of the reverse depth defect along
   `n_L=floor(alpha*p^L)`;
7. recovery of `(p,a,n)` from phase size and the full fixed sequence.

The coefficient-chain lane proves the pointwise iterate, structural conjugacy,
and depth clock. A complementary `F_p`-linear factorization, which starts from
the iterate formula, recounts uniform fibres and the CDF by rank--nullity.
Fixed-subfield and divisor arguments then give the periodic census.

## Reproduce

Run from this directory:

```text
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The expected verifier terminus is:

```text
PASS: 2,259,162 exact assertions
```

The direct Cartier/section-operator definition and composition, finite-field
Frobenius theory, restriction-of-scalars linearization, and generic
cyclic--nilpotent functional-graph machinery are explicitly subtracted with
zero credit. The residual claim is only the exact bounded Cartier
specialization together with its lattice and recovery conjunction. This is an
internal author draft. External circulation, novelty, and priority remain
**HOLD**.
