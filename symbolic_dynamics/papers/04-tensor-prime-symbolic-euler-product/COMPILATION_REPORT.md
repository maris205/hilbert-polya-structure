# Compilation Report

## Final exploratory build

- Status: **SUCCESS**
- Compiler: pdfTeX 3.141592653-2.6-1.40.22
- Build sequence:

  ```bash
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  bibtex main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  ```

- Current PDF: `main.pdf`
- Pages: **10**
- Page size: **A4**
- PDF size: **520,367 bytes**
- SHA-256:
  `990f4b5efb96252fc1b7f27471aa405b1d7637fb5fa9dfc00b70080b73a5a302`
- Undefined references: **0**
- Undefined citations: **0**
- LaTeX warnings: **0** on the final pass
- Overfull boxes: **0**
- Underfull boxes: **0**
- Fonts embedded and subset: **YES** for every font reported by `pdffonts`
- PDF metadata author: **Anonymous Authors**
- PDF encrypted: **NO**

## Reproducibility checks

- Exact experiment rerun: **SUCCESS**
- Unit tests: **4/4 PASS**
- Main cutoffs: `32,64,128,256`
- At `N=256`: 54/54 atoms recovered; UFD, zeta, Möbius, and von
  Mangoldt prefix metrics all `1.000`
- Positive no-mixing controls: **28/28 PASS** at every cutoff
- Candidate reads prime table: **NO**
- Candidate reads Riemann zeros: **NO**

## Scope checks

- Symbolic Dynamics is the only primary family.
- Tensor atoms and temporal primitive orbits are explicitly separated.
- The Fredholm theorem is stated only for `Re(s)>1`.
- Scalar meromorphic continuation is not presented as operator continuation.
- Gamma factor, functional equation, Weil compression, RH, and
  Hilbert–Pólya claims are absent.
- `route_b_invocation_allowed` is `false`.

Per the project directive for exploratory stages, no external or multi-round
paper-review loop was run.  Formula derivation, exact controls, tests, source
checks, compilation, font checks, and visual inspection were completed.
