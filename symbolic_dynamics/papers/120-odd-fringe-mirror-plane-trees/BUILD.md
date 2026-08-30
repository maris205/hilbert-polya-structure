# Round-two build record — P120

Status: **PASS / ANONYMOUS REVIEW-B REPAIR / EXTERNAL HOLD**.

This is the compilation record after Reviewer B repairs, not final QA,
release approval, or a package hash seal.

## Environment and commands

The environment does not provide `latexmk`.  The repository-standard
equivalent four-stage build is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The exact control is run separately with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

## Settled result

- exact verifier: **PASS**;
- assertions/states: **1,155,278 / 82,501**;
- fresh verifier stdout: byte-identical to the stored **619-byte** canonical
  transcript;
- LaTeX/BibTeX build: **PASS**;
- artifacts: `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`, and
  `main_round2.pdf`;
- round-zero PDF: **378,895 bytes**; round-one PDF: **380,490 bytes**;
  round-two/current PDF: **380,615 bytes**, byte-identical to one another;
- pages: **5 A4 pages**; Conclusion and References both occur on page 5;
- settled LaTeX/package warnings: **0**;
- settled BibTeX warnings/errors: **0**;
- undefined references/citations and multiply-defined labels: **0**;
- overfull/underfull boxes and rerun requests: **0**;
- bibliography closure: **9/9** cited keys, with no uncited entry;
- both closest preprints render their arXiv identifiers in the PDF;
- fonts: **30/30** embedded, subsetted, and Unicode-mapped;
- PDF metadata: empty Author, no creation/modification date, no forms,
  JavaScript, encryption, or page rotation;
- unresolved text sentinels (`??`, `[?]`, `[VERIFY]`, `TODO`, `FIXME`,
  `internal draft`): **0**;
- visual inspection: all **5/5** rendered pages checked; both tables remain at
  their source locations, equations are legible, and no clipping or overlap
  was observed.

Round one defines the induced vertex transport, separates the empty lane,
states formal-series uniqueness in `Q[[x]]`, makes both preprint identifiers
visible, and adds a full exact resultant audit.  Round two translates the
Claesson et al. fixed census from edge size to the present vertex order and
replaces the invalid parity comparison by the exact order-four and order-six
count separation.  No checksum manifest, Git operation, external posting,
submission action, novelty declaration, or priority claim was produced.
External release remains **HOLD**.
