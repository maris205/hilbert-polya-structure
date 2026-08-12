# Compilation report

- **Status:** SUCCESS
- **Compiler:** `latexmk -pdf` with `pdflatex`
- **PDF:** `main.pdf`
- **Total length:** 9 pages
- **Main body through conclusion:** page 8; the references begin later on the same page
- **Appendix:** page 9
- **Requested 6--10 page range:** YES
- **PDF size:** 380,213 bytes
- **PDF SHA-256:** `251a48c1705a350504afbf9a23d2a0b069db61855475cf5341318bd6c7220a27`
- **Undefined references:** 0
- **Undefined citations:** 0
- **LaTeX/package warnings:** 0 in the final `main.log`
- **Overfull boxes:** 0
- **Underfull boxes:** 0
- **Stale section files:** 0
- **TODO/FIXME/VERIFY markers:** 0
- **Font embedding:** all fonts embedded and subsetted

## Content checks

- The local proof records the exact \(p=19\) Newton edge, the residual
  factorization, the Hill valuation comparison, and the resulting
  weight-two parity row.
- Kummer rank nine is proved from the \(S_9\)-orbit of pair rows and an
  independent norm/sign-field square-class comparison; irreducibility of
  \(F_{18}\) is not substituted for this argument.
- The standard quadratic wreath embedding is explicitly separated from the
  Hénon-specific maximality result.
- The note cites the local C33 theorem/certificate, the foundational Paper-5
  Hénon manuscript, Arai (2007), Barquero-Sanchez--Calvo-Monge (2023), and a
  standard local-fields reference.
- The Route-A tuple remains
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` with overall
  `ROUTE_A_REJECTED`.

## Rebuild

```bash
cd henon_dynamics/henon_maxwell_hill_wreath_monodromy/paper
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
