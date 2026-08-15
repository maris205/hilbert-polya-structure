# HCS-C57 compilation report

Status: **PASS; official paper build against the exact
`PREFREEZE_CODE_RESULTS_PASS` machine evidence; full-project release pending**

## Build

- Engine: pdfLaTeX 1.40.22 through latexmk 4.76.
- Command: `latexmk -C main.tex`, followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
  main.tex`.
- Build environment: `SOURCE_DATE_EPOCH=1786838400`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- Exit status: zero.
- PDF: `paper/main.pdf`.
- Total pages: 24 A4 pages.
- The conclusion and Appendix A begin on page 16; references begin on page 24.
- File size: 537984 bytes.
- PDF SHA-256:
  `60bdbcbb1a9ddc03ac6a142d22142821860545026fb9dfa21a8001960c7d0200`.
- Final stabilized LaTeX log SHA-256:
  `ddbbf698c8b0c3b1167f708ec32fe0e92b4ba47d4d6af8c3b5f379425886884b`.

No conference page limit is asserted. The project uses a single-column
mathematical-article format. The in-tree PDF named above is the authoritative
paper artifact; no claim of byte-for-byte invariance across arbitrary output
directories or TeX installations is made.

## Paper-source lock

- Source set: 17 TeX files and `paper/references.bib` (18 files total).
- Digest definition: SHA-256 of the lexicographically ordered `sha256sum`
  lines, evaluated from the C57 project root.
- Paper-source SHA-256:
  `3c2b0a3a3908368ea5efa35f22fb124796e43f5666328c94d3bee0682fd9c10e`.
- All 18 integrated source files are byte-identical to the independently
  reviewed candidate whose source aggregate was
  `783e7810b7a3fa4dca7de384b97ab0f623663ea80247c6d1220f71997185fda5`;
  the two aggregate conventions differ only because one hashes absolute
  candidate-path lines and the other hashes project-relative path lines.
- No source byte changed during the official build.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- LaTeX/package/pdfTeX warnings after the final stabilized pass: 0.
- BibTeX warnings: 0.
- Duplicate PDF destinations or multiply defined labels: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Rerun requests: 0.
- Stale section files: 0; every one of the 15 files in `paper/sections/` is
  input by `paper/main.tex`.
- Static source inventory: 96 unique labels, 108 reference uses with none
  missing, 26 citation uses over exactly 6 bibliography keys, and 122 balanced
  environment pairs.
- Bibliography: 6 entries, all cited.
- Text extraction: PASS, with 1321 lines, 9314 whitespace-delimited tokens,
  and 75541 bytes.
- Extracted-text SHA-256:
  `0d91dd71471e5131a554320bf8dfef94b9a0b378b56b8f3a261d99061b3f1877`.
- Residual `TODO`/`FIXME`/`XXX`/`[VERIFY]` markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.
- Doubled cross-reference wording such as “Equation equation”: 0.
- Ghostscript null-device parse: PASS.
- Generated auxiliaries remaining in `paper/`: 0.

## Exact machine-evidence lock

- Machine status: `PREFREEZE_CODE_RESULTS_PASS`.
- Payload SHA-256:
  `72e498b544599dbb8c7c56b2fd999ed8be80bdb0abd19393b5e47ddf60ae4574`.
- Canonical schema SHA-256:
  `4c4675b71556867a5699574b5f3f54aa40551c76a14e22ac21c62370add61cc4`.
- Schema-file SHA-256:
  `81942b5f8012071cbc1bd24f8a85e04a2e7fea10b3f5cb8e8ca3014c6e822f72`.
- Certificate SHA-256:
  `3078baf167d2344982d9f93811f1fd59a8258c8178ecce4decbd2b054b16092f`.
- Independent-check SHA-256:
  `fb0afb77f130fb2d0a792af8d949e5c1a8e1b7864525dd62f1d1a41d99a79bcf`.
- Scoped 28-entry, self-excluding code/results-manifest SHA-256:
  `864c05b18e0bdcafbc5b5e3206840a1b25afa355b9737ebcc9d1806e33fcec5d`.
- Independent checker: G0--G7 (8/8) pass; 535 of 535 rebound and
  structural mutations are rejected; the hostile suite has 33 tests.
- Code/results inventory: 18 code files and 11 result files, or 29 live files
  including the scoped manifest.

The scoped manifest remains the exact machine-lane identity. Paper and
full-project identities are separate, external layers and do not replace it.
The paper build does not rewrite any code, result, certificate, or evidence
archive.

## PDF checks

- `pdfinfo` parses the file as unencrypted PDF 1.5 with 24 A4 pages, no forms,
  and no JavaScript.
- Title and anonymous-author metadata are present and correct.
- All 31 fonts are embedded and subsetted Type 1 fonts.
- No Type 3 font occurs.
- Fresh raster inspection covered pages 1, 3, 5, 6, 15, 16, and 22--24:
  title and abstract, field diagram, source contract, sharp degree theorem,
  gate firewall, data/code availability, conclusion, source ledger, machine
  envelope, evidence table, and bibliography.
- A 24-page raster comparison with the independently reviewed clean build has
  zero mismatches. Its extracted text is also byte-identical to the official
  build.
- Long digests, the project-relative supplement path, and all evidence-table
  filenames are complete, breakable, unclipped, and text-extractable.

## Mathematical and scope checks visible in the paper

- The equality clause explicitly retains the nonzero 2-primary Brauer
  hypothesis; it does not classify arbitrary degree-36 number fields.
- The complete alternatives are kept separate:
  `Z/2 -> U1` of index 36 and `(Z/2)^2 -> U3` of index 720. Both force
  `36 | [K intersect L : Q] | [L : Q]`, while only the first attains equality.
- For arbitrary finite, possibly non-Galois `L/Q`, the paper defines
  `G_L`, `H_L`, and `N_L`, proves the inflation isomorphism, and separately
  uses the number-field Hochschild--Serre bridge.
- The embedded subgroup `U1+` and its fixed field are distinguished from an
  abstract copy of `S6`.
- The raw eliminant, its leading coefficient, the monic normalization, the
  scaled line roots, the carrier subtop coefficient, and the restriction
  variable use one consistent convention.
- G6 ends at the determinant-defined quartic and rank calculation. G7 contains
  degree exhaustion, the norm-divisor identity, unramifiedness, and the
  separate nonzero-class comparison.
- The paper does not claim a rational point, absence of rational points,
  rationality, stable rationality, a Hasse failure, weak approximation, local
  evaluation, or a Brauer--Manin obstruction.
- It does not claim a complete bad-prime Picard--Artin package, local Euler
  factors, conductor, root number, motive, VHS, Calabi--Yau realization,
  automorphy, dynamical theorem, Riemann-hypothesis statement, or generic
  resolver priority.

This report records the official paper build. Its own digest, the final
formal-package digest, the Route-record digest, and the full-project manifest
digest remain external to their respective hashed objects to avoid self-hash
cycles.
