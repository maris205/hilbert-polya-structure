# Paper 14 — Functorial Tensor Characters and Möbius Bar Codes

## Outcome

Paper 14 closes the standard functorial integer/abelian-character search and
replaces it with the source-locked symbolic candidate **SD-C16**.

The negative result is exact: on the tensor monoid of finite full shifts,
every abelian monoidal charge is a valuation sum, every coherent cocycle on
the thin tensor-divisor category is a coboundary, every regular
entropy-derived character is only a vertical translation of the Dirichlet
variable, and a pure presentation shuffle is invisible to any functorial
determinant.  Therefore no such character can be nonzero on tensor atoms and
vanish on every composite.

The positive replacement is a one-vertex countable signed edge shift whose
edges are nonempty ordered words of nonunit full-shift objects.  With
entropy roof and reduced-bar sign, its raw weighted adjacency sum is

\[
F_{\mathrm{bar}}(s)=\frac{\zeta(s)-1}{\zeta(s)},
\qquad \Re s>\sigma_{\mathrm{bar}},
\quad \zeta(\sigma_{\mathrm{bar}})=2,
\]

and its canonical scalar determinant satisfies

\[
D_{\mathrm{bar}}(s,1)=1-F_{\mathrm{bar}}(s)=\frac1{\zeta(s)}.
\]

Endpoint-first finite incidence cancellation extends the coefficient-grouped
formula to `Re(s)>1`, and the canonical roof derivative produces
`Lambda_tensor = mu_tensor * h`.  Neither `mu_tensor` nor `Lambda_tensor` is
an input weight.

The same construction returns the reciprocal partition sum for every
weighted inventory.  This is a decisive **PROVES_TOO_MUCH** control, and the
primitive cycles of the bar-code shift are factorization necklaces rather
than primes.

## Route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Paper 15 obligation

Test whether a canonical sign-reversing involution, quotient grammar, or
bar-to-Koszul reduction can act **before primitive cyclic reduction** so that
one atom class and its repetitions survive while composite histories cancel.
Otherwise prove that the bar cancellation is only universal algebraic
inversion and cannot become an orbitwise Euler realization.

## Contents

- `main.pdf` — compiled paper.
- `main.tex`, `sections/`, `references.bib` — manuscript source.
- `SOURCE_LOCK.md` — frozen object, domains, data rules, and claim boundary.
- `PROOF_PACKAGE.md`, `DERIVATION_PACKAGE.md` — theorem and calculation ledger.
- `PREREGISTRATION.md` — predeclared numerical and control protocol.
- `LITERATURE_AUDIT.md` — bounded prior-art and novelty audit.
- `FIGURE_SPEC.md`, `figures/` — the single pure-TikZ figure.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md` — concise research narrative and plan.
