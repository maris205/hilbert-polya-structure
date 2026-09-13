Deterministic Paper24 R0 build executed exactly once in two fresh private roots and is blocked.

Private roots:
- A: `/tmp/paper24-r0-A.XFAQMa`
- B: `/tmp/paper24-r0-B.l1C9sP`

Pre-build frozen source identities verified exactly before invocation:
- `paper/main.tex` sha256 `1008cfa8c691d06645b79f33de00044df45e97a18b6d5a0f6ded2431f1df8f4e`, bytes `67011`, LF `1707`
- `paper/math_commands.tex` sha256 `8c3f90e67d48b1773f5582b21e8bd6f805a22e40ea23a5bbeffb40ab7da7298e`, bytes `605`, LF `20`
- `paper/references.bib` sha256 `4acd9cad4609fabfea4c8b4504a6fde11ff7de8b0a2952b6723678f10093af0b`, bytes `3556`, LF `118`

Exact command sequence run once in each root under clean environment `PATH=/usr/bin:/bin SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C LANG=C`:
1. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

Exit vectors:
- A: `(0,0,0,0)`
- B: `(0,0,0,0)`

Source-copy verification:
- copied files in A and B match the frozen source hashes exactly
- copied files in A and B are distinct inodes with no links

Cross-root output verification:
- `main.aux` sha256 `535f3fb6d581498c45af930b2fe13d8ec12d123882e22926aa31549553ea4cf1`, bytes `13644`
- `main.bbl` sha256 `b35208ffdf905fb0d3f00780b0f736d41019e2c10d1c1a88413b9c0f2d028855`, bytes `3371`
- `main.blg` sha256 `04c5f77a905bc8c317bebcf22ba7bbb97d3908ea8d8fe8862e98737046987535`, bytes `900`
- `main.log` sha256 `92a3dcda5a39c783c68560823ba2a88310259ae298acae02d99b11396d7132aa`, bytes `28838`
- `main.out` sha256 `02184e2312424c5bcbbb39d8151afde7bd567334dc9c77d8d22965871900013d`, bytes `6374`
- `main.pdf` sha256 `4bbea924e62369c7756200accb1320f4bc114998ed057081923f995b50a482bb`, bytes `491590`
- all six listed outputs are byte-identical between A and B and nonempty

Checks that passed:
- exact 9 rendered bibliography items
- PDF structurally readable and text-extractable
- fonts embedded
- PDF metadata: Title `Forced Period-Two Selector Exchange in Two-Mode Hamiltonian Product Shears`; Author empty; Creator empty; Producer empty; CreationDate absent; ModDate absent
- visible `Anonymous` present on page 1
- no visible date near the title
- no undefined citation/reference, no multiply-defined label, no final rerun-needed warning, no TeX error, no missing glyph, no internal-path or build-path leakage
- exactly 3 rendered tables, no `Table 4`, zero figures

Acceptance failures:
1. Final-pass overfull box remains. The deterministic final log records:
   - `Overfull \hbox (39.23778pt too wide) detected at line 1628`
2. The pagination/content-page requirement failed. `pdfinfo` reports `Pages: 23`, while the `References` heading first appears on page `22`. Therefore references do not begin only after `26` full content pages, and the required exact `26.0` content pages are not met.
3. The exact visible-title check failed under deterministic text extraction. Page 1 begins with the split lines
   - `Forced Period-Two Selector Exchange in Two-Mode Hamiltonian`
   - `Product Shears`
   so the exact full title string does not appear as one contiguous extracted first-page line.

Disposition required by the failure contract:
- no success artifacts were persisted into `paper/`
- the two private build roots are retained untouched for evidence
- this blocker note is the only project write

R0_BLOCKED
