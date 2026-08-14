# Compilation report — Paper 29 / SD-C31

Audit date: 2026-08-14 UTC

## Deliverable

- Title: *Functorial Counterterms at the Hilbert--Schmidt Boundary: Finite-Scheme Ambiguity and Generic Mixed-Gram Residues*
- Final artifact: `main.pdf`
- SHA-256: `a42da7b24f195b4eda0bd02e2a58299767fc4df1962acb7bdfe36d97347bc9f7`
- Size: 453,372 bytes
- Format: 17 pages, A4 (595.276 x 841.89 pt), PDF 1.5
- Engine: pdfTeX 1.40.22; bibliography processed with BibTeX 0.99d and `plainnat`
- Manuscript inventory: 202-word abstract, 12 numbered sections including appendices, 15 numbered theorem-like environments, 3 vector figures, and 2 tables

The international-format PDF contains the English abstract.  `NARRATIVE_REPORT.md` additionally preserves the Traditional Chinese abstract requested for the research record.

## Reproducible build

From this directory, the clean build sequence is:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final source-stable pass produced a 17-page, 453,372-byte PDF. Compilation terminated normally; the PDF hash above binds the delivered bytes.

## Mechanical audit

| Gate | Result |
|---|---|
| LaTeX errors, undefined control sequences, fatal or emergency stops | PASS: none |
| LaTeX/package warnings, undefined citations/references | PASS: none |
| Overfull or underfull boxes | PASS: none |
| Citation parity | PASS: 18 unique cited keys and 18 bibliography entries; no missing or orphan key |
| Placeholder scan | PASS: no `[?]`, `TODO`, `TBD`, `FIXME`, `UNVERIFIED`, or placeholder leakage in extracted PDF text |
| PDF page occupancy | PASS: every one of the 17 pages contains substantive extracted text |
| Fonts | PASS: all 28 reported font resources are embedded, subset Type 1 fonts; no Type 3 font |
| Raster-content audit | PASS: `pdfimages -list` reports no raster images; all three figures are native TikZ/vector content |
| PDF safety | PASS: not encrypted; no form and no JavaScript |
| Page geometry | PASS: all pages are unrotated A4 |
| Source control bytes | PASS: no forbidden ASCII control bytes and no CRLF endings in writer-owned Markdown, TeX, or BibTeX sources |

## Visual audit

Every page of the final 17-page PDF was rendered and inspected.  The title/status box, equations, theorem blocks, bibliography, appendices, captions, and page furniture are legible and unclipped.  The three figures have no label collisions.  The exact-audit table now begins inside Section 8, and the route ledger is fixed inside Section 9.  The final declarations occupy page 17 without a blank spill page.

## Scientific and ownership audit

- The theorem is explicitly limited to reference-independent quadratic schemes and the additive, pair-local, linear-Gram counterterm class.  A universal claim for bare naturality or nonlocal filtered-tower invariants is marked **OPEN**.
- The manuscript distinguishes the nonexistent ordinary quadratic trace, the independently valid third-regularized determinant `det3`, and the newly declared scheme-dependent functional `D_ren`.
- The factor relating two `D_ren` schemes is a zero-free exponential of a quadratic polynomial in the auxiliary variable, so it does not change that auxiliary divisor.  This is not presented as an ordinary Fredholm determinant or as `det2`.
- Reflection under `s \leftrightarrow 1-s` is claimed only for a reflection-symmetric finite-part prescription.
- The route is frozen as `(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_FAIL,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`, with `ROUTE_A_REJECTED`; Route B remains locked and target-zero data are absent.
- The mixed-Gram residual is called generic rather than arithmetic-selective.  No printed numeric atom label is queried as an oracle.

## Canonical exact evidence

Only the authority result package is canonical manuscript evidence:

- independent evaluator: 602/602 checks passed;
- unit suite: 23/23 tests passed;
- row census, in frozen order (baseline/control/schemes/grid/determinant/route/comparison/raw): 76/47/15/49/4/5/7/7;
- baseline cutoffs 12, 18, and 30: 76 mixed/fourth-order pairs, all nonzero mixed and positive fourth order;
- mutated-cover/composite-only/generic-DAG/random-inventory controls: respectively 3/2/4/9 surviving mixed pairs, with the same positive fourth-order counts;
- finite-scheme coefficient grid: 49 cases and zero selective solutions;
- two fresh runs: 30 artifacts compared byte for byte and identical;
- integrity audit: PASS; SHA ledger: all 32 entries PASS.

Frozen authority hashes:

| Artifact | SHA-256 |
|---|---|
| `results/SHA256SUMS.txt` | `c146a7f3b8deb26a4eafa494ddfcb9269987b6898c197d2fb32768d7b6aae1df` |
| `results/double_run_certificate.json` | `7d788be24f16d7efbe52c25d199d9cb5815d096c3e30394dbc36f9e416195ec6` |
| `results/integrity_audit.json` | `d7cf8bd141407f4e814569d9af762c831f2e93b344914c186f9057fe8cd5faa6` |
| `results/summary.json` | `031336a6ab87a85c1bc5f81f5df09aa578c1f168df7902fdb665f848da75c0cc` |

The earlier `/tmp` prototype aggregate is retained only as research input and is not treated as canonical evidence.

## Process boundary

Per instruction, no review loop was run.  Objective compilation, source, citation, font, control-byte, scientific-scope, and full-document visual audits were completed.  No Git operation was performed, and no experiment, result, evaluator, manifest, repository-level documentation, or mirror file was modified by the writer.
