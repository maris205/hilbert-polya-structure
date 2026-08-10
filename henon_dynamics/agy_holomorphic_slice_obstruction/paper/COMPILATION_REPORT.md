# Compilation report

## Outcome

- Status: **PASS**
- Build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- Build driver: latexmk 4.76
- Output: `main.pdf`
- PDF size: 370,426 bytes
- PDF SHA-256: `b47e2d0191a763fbf11d63582b897dc89691982959bbc0e1a109dcc4f3e630f1`
- Format: A4, PDF 1.5

## Pagination and structure

- Total length: 17 pages.
- Main article, including the conclusion: pages 1--12.
- References begin on page 13.
- Appendices A--C occupy pages 13--17.
- The source is modular: eight numbered sections, three appendices, the
  abstract, and the shared mathematics commands are each included exactly
  once. No stale section source was found.

## TeX and bibliography audit

- Fatal TeX errors: 0.
- LaTeX/package warnings: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Undefined citations: 0.
- Undefined references: 0.
- Multiply defined labels: 0.
- Bibliography records: 8.
- Rendered bibliography items: 8.
- Every bibliography record is cited, and no uncited record is retained.
- `references.bib` SHA-256:
  `e5482b54ed383b1e176e0c855d3ff8b579bd0facdf7a8c36d66dd34c7c1c77f3`.

The bibliography contains only the source-audited AGY, two
Bandtlow--Jenkinson, Thomas, Hilgert, Bonet--G\'omez-Collado--Jornet--Wolf,
Gurevich--Hadani, and Folland records.

## PDF audit

- Fonts used: 25.
- Fonts embedded: 25/25.
- Text extraction succeeded on all 17 pages.
- The title, abstract, numbered sections, references, appendices, displayed
  formulas, exact integer tables, and reproduction commands were present in
  the extracted text.
- The main body ends on page 12; there is no blank spill page before the
  references.

## Claim-integrity checks performed before the final build

- AGY attribution is limited to the published branch grammar, real
  estimates, roof, and inverse-Jacobian inputs. The factorization
  `A_gamma = B_gamma^T = P C_gamma` is explicitly identified as the present
  algebraic deduction from that grammar and later-on-the-left chronology.
- The compact-parameter holomorphy proof explicitly fixes
  `x0 in Delta subset p_P(D) subset Omega`, chooses
  `-sigma_0 < a_0 < min_K Re(s)`, and uses `q_gamma(x0) >= 2` to obtain one
  summable majorant on each compact parameter set.
- Forward Rauzy order, transposed inverse-branch order, and operator-factor
  order are distinguished explicitly.
- The two-return example is labeled only as a contravariant matrix-order
  sentinel, since the two cyclic products have the same characteristic
  polynomial.
- The length-650, three-return noncyclic reversal is the spectral chronology
  sentinel; its forward and reversed exact reciprocal-polynomial
  coefficients are both recorded.
- Reproducibility counts are synchronized to 14 independent checks, 21
  regression/mutation tests, and three Perron examples. The two principal
  JSON artifact hashes recorded in Appendix C match the released manifest.
- Route-A conclusions and all Hilbert--P\'olya scope limitations are stated
  as negative/conditional results rather than upgraded claims.
- AI-assistance disclosure is present in Appendix C.

## Cleanup

After the successful build and audits, `latexmk -c` was run and the remaining
generated `.bbl` and captured build log were removed. The paper directory now
retains only the LaTeX/BibTeX sources, this report, and the final PDF; no
`.aux`, `.blg`, `.fdb_latexmk`, `.fls`, `.log`, or `.out` files remain.
