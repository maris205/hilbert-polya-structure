# HCS-C47: classification of repetition-compatible scalar labels

Let \(R(X)\in\mathbb Q(X)^\times\) be a functorial scalar label rule for a
primitive multiplier, and require exact compatibility with every repetition:

\[
R(X^r)=R(X)^r.
\]

The project proves

\[
\boxed{R(X)=X^k\quad(k\in\mathbb Z).}
\]

The proof uses divisors on \(\mathbb P^1\): any finite nonzero zero or pole
would generate infinitely many iterated square roots, so support is confined
to \(0\) and \(\infty\); the square law fixes the scalar constant.  Combined
with C46, every rational repetition-compatible H6 label remains an algebraic
unit and cannot be a rational prime.

The continuous positive classification is \(R(X)=X^c\), \(c\in\mathbb R\).
Therefore C45's pressure label \(X^{h_*}\) is the precise surviving scalar
candidate and is not silently covered by the rational no-go.

## Reproduce

```bash
bash code/run_c47.sh
cd paper && pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The rational scalar lane is `ROUTE_A_REJECTED`; the pressure-power lane
remains exploratory.
