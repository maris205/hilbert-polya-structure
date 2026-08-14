# HCS-P58: Physical tails do not control Hénon Galois excess

P58 tests the most natural continuation of the P57 incidence ladder: use the
stable linearization at the negative fixed point to predict the next Galois
excess discrepancies.  The test reveals a precise interface obstruction.
The linearization controls one selected physical embedding, whereas the
Galois excess is an all-conjugate sum.

The exact period-eight reflection closures split into two fields:

\[
\deg F_{A_8}=12,\qquad \deg F_{B_8}=6.
\]

Both are irreducible and totally real.  At period nine, `A9` and `B9` are the
two extreme physical embeddings of one irreducible totally real degree-28
trace field.  Exact integer-product estimates give

\[
\Delta_6=-185.5524168765\ldots<0,
\qquad
\Delta_7=300.0665139420\ldots>0.
\]

The stable eigenvalue at the negative fixed point is positive and below
`2/sqrt(17)`, so the physical tail is exponentially localized.  This fact
does not control the number or magnitude of the nonphysical trace
embeddings.  Consequently physical fixed-point linearization alone cannot
prove an asymptotic law for `Delta_m`; a symmetry-resolved
reflection-ensemble theorem is an independent obligation.

## Status

- **PROVED:** exact vertex--vertex, edge--edge, and vertex--edge reflection
  closures at periods eight and nine;
- **PROVED:** irreducible totally real trace fields of degrees 12, 6, and 28;
- **PROVED:** rational isolation of the physical `A8`, `B8`, `A9`, and `B9`
  embeddings;
- **PROVED:** `Delta_6<0<Delta_7` by exact integer products;
- **PROVED:** exponential localization of the selected physical
  negative-fixed-point tail;
- **PROVED INTERFACE OBSTRUCTION:** that one-embedding tail estimate does not
  compile the all-conjugate Galois excess;
- **OPEN:** a uniform primitive reflection-ensemble count/height theorem;
- **OPEN:** unrestricted Hölder realization, a full Galois determinant,
  arithmetic primes, and every Hilbert--Pólya operator gate.

Route A remains exploratory:
`(A1_WEAK, A2_ANALYTIC_DETERMINANT [physical subsystem only],
A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)`.  Route B is not authorized.

## Reproduce

```bash
bash code/run_c58.sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The manuscript is [`paper/paper.pdf`](paper/paper.pdf).
