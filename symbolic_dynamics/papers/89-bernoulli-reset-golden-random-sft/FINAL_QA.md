# Final QA

Release audit date: 2026-08-28 UTC.

## Result

- Decision: **GO; INTERNAL FREEZE; EXTERNAL HOLD**
- Independent hostile audit: **2/2 rounds complete**
- Exact control: **66,787 integer/rational assertions, PASS**
- Floating diagnostics: **10, PASS**, not counted as exact evidence
- Build: explicit `pdflatex / bibtex / pdflatex / pdflatex`, all exits zero
- PDF: `main.pdf`, **6 A4 pages**, **320,648 bytes**, PDF 1.5
- Undefined references: 0
- Undefined citations: 0
- LaTeX warnings on final pass: 0
- Package warnings on final pass: 0
- Overfull boxes: 0
- Underfull boxes: 0
- Fonts: **24/24 embedded, subsetted, and Unicode-mapped**
- Bibliography: **5 cited keys / 5 entries**
- Source markers: no unresolved TODO, FIXME, XXX, `[VERIFY]`, `??`, or `[?]`
- Anonymous: author field and running heads contain only `Anonymous`
- Visual inspection: **6/6 pages** checked; no clipping, collision, broken
  equations, malformed bibliography names, or stray text
- SHA-256: `6782a62b934d40f7c1821cd161415a17e308cf4a78391886ecc6f2b639f04c0f`

## Mathematical release checks

- The model specifies the environment, the two adjacency matrices, the
  fibre, and the path-length convention before any entropy statement.
- The rank-one identity `E A^k E = F_(k+2) E` is proved for `k=0` and
  `k>=1`, then propagated through arbitrary products.
- Quenched entropy uses iid geometric reset gaps and an exact
  renewal-reward decomposition.  Initial and terminal matrix boundaries are
  `O(log n)` almost surely by an explicit longest-run bound.
- Annealed growth is derived from the exact finite-time mean-matrix identity,
  not from an exchange of asymptotic limits.
- The strict gap uses a nonconstant positive cycle gain with exact mean one;
  convergence of the Fibonacci generating function at the substituted point
  is checked.
- The renewal CLT states the classical input, checks all required moments,
  uses an explicit delayed clock from the almost-surely finite first reset,
  transfers the initial delay, unfinished-cycle, and matrix boundaries on the
  `sqrt(n)` scale, and derives the displayed variance rate.
- The finite-time annealed matrix power has been reverse-read in the rendered
  PDF; its exponent is `n` and contains no stray punctuation.
- Variance positivity is symbolic from the positive-probability `K=0` and
  `K=1` cycles.  The endpoint processes are kept outside the nondegenerate
  CLT.

## Ownership and risk checks

- General random matrix products, random-subshift thermodynamic formalism,
  renewal/regenerative limit theory, and the golden-mean shift have positive
  owners in the bibliography.
- The manuscript calls the residual result an exact two-matrix
  specialization and contains no absolute novelty or priority claim.
- The bounded search date and keywords are disclosed; collision risk remains
  medium because all ingredients are classical.
- The zero row of the reset matrix is acknowledged as a reason not to invoke
  stronger random Perron--Frobenius hypotheses.
- External posting or submission is not authorized until a separate expert
  literature and priority review clears the HOLD.
