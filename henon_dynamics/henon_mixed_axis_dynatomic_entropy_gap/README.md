# HCS-P60: Mixed-axis dynatomic entropy gap

P60 follows the exact physical half-entropy theorem of P59 into the algebraic
reflection closure. For odd `n=2m+1`, start the H6 recurrence on the vertex
symmetry line,

```text
q_0=X,  q_1=(1-6X^2)/2,
q_(j+1)=1-6q_j^2-q_(j-1),
```

and close on the other symmetry line with

```text
F_n(X)=q_(m+1)(X)-q_m(X).
```

The project proves

\[
\deg F_n=2^{(n+1)/2},\qquad F_d\mid F_n\quad(d\mid n, d,n\text{ odd}).
\]

The formal primitive M\"obius divisor therefore has degree

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}
   =2^{(n+1)/2}+O(n2^{n/6}),
\]

and formal entropy `(1/2)log(2)`. This strictly exceeds P59's physical
reflection entropy `(1/2)log(phi)` by `(1/2)log(2/phi)`.

Exact factorization for every odd period through 15 gives primitive quotient
degrees

```text
n:   1  3  5   7   9   11   13   15
D_n: 2  2  6  14  28   62  126  246
```

All eight closure polynomials are squarefree and all eight new quotients are
irreducible over `Q`. The period-nine quotient has exactly the P58 degree-28
coordinate-polynomial hash.

## Claim boundary

- **PROVED:** all-odd-period closure degree and divisibility sequence;
- **PROVED:** formal primitive degree law and formal entropy gap;
- **COMPUTER_CERTIFIED_EXACT:** reduced irreducible quotients through period
  15;
- **OPEN:** all-period reducedness/transversality and effectivity of the
  reflection dynatomic divisor;
- **OPEN:** a canonical incidence map from local-survivor necklaces to all
  algebraic roots and any uniform Galois-height pressure;
- **NOT CLAIMED:** rational-prime amplitudes, a completed determinant,
  Hilbert--P\'olya, or RH.

Route A remains `ROUTE_A_EXPLORATORY`; Route B is not authorized.

## Reproduce

```bash
bash code/run_c60.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The exact period-15 factorization is the slow step. The compiled manuscript is
[`paper/paper.pdf`](paper/paper.pdf).
