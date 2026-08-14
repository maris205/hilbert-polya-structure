# HCS-P59: A half-entropy law for Hénon reflection orbits

P59 solves the physical reflection-counting problem isolated by P58.  On the
frozen four-state H6 survivor, time reversal is the symbol involution
`rho=(0,2,1,3)`, and the adjacency matrix satisfies `A=P A^T P`.

Exact half-word transfer formulas and divisor-sensitive Möbius inversion give
closed expressions for every primitive reversible cycle.  Odd periods have
one reflection class.  Even periods split into edge--edge and vertex--vertex
classes; the P58 families satisfy

```text
A8 = 00000021 : vertex--vertex,
B8 = 00000231 : edge--edge.
```

If `C_n` counts all primitive survivor cycles and `R_n` counts the reversible
ones, then

\[
C_n\sim\frac{\varphi^n}{n},\qquad
R_n=\Theta(\varphi^{n/2}),
\]

so

\[
h_{\rm refl}=\frac12\log\varphi,
\qquad h_{\rm full}=\log\varphi.
\]

Thus physical reflection cycles are exponentially sparse, with
`R_n/C_n=O(n varphi^(-n/2))`.  The result is all-period and analytic, not a
finite numerical trend.

## Status

- **PROVED:** the exact H6 time-reversal involution;
- **PROVED:** odd and both even-axis fixed-word formulas;
- **PROVED:** all-period primitive reflection Möbius formulas;
- **PROVED:** reflection entropy is exactly half the full survivor entropy;
- **NUMERICALLY CERTIFIED:** primary and independent enumerations through
  periods 16 and 12 agree with every formula;
- **OPEN:** the algebraic reflection dynatomic count and Galois-height
  pressure;
- **OPEN:** rational-prime amplitudes, a completed determinant, and every
  Hilbert--Pólya operator gate.

Route A gains an analytic A1 result for the reflection subsystem but remains
overall `ROUTE_A_EXPLORATORY`; Route B is not authorized.

## Reproduce

```bash
bash code/run_c59.sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The manuscript is [`paper/paper.pdf`](paper/paper.pdf).
