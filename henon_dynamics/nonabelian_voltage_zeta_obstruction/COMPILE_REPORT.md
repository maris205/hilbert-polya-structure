# Compilation and release check

Date: 2026-08-07

## Manuscript build

The manuscript was rebuilt from paper/main.tex with the deterministic
sequence

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

latexmk is not installed in this environment, so the equivalent manual
four-pass build was used. The final artifact is paper/main.pdf:

- 13 pages;
- 307,906 bytes;
- 12 bibliography records, all cited;
- no undefined citations or cross-references;
- no overfull or underfull boxes in the final log;
- no unresolved TODO, FIXME, VERIFY, ??, or [?] marker in the
  extracted PDF text.

The title page, theorem pages, exact ledgers, and the final bibliography page
were visually inspected after compilation. In particular, the chronology
tables and the exact-conductor Schrödinger lemma are not clipped.

## Executable verification

The release test command

~~~bash
cd code
python -m unittest -v test_voltage_zeta.py
~~~

passes all nine tests. The exact producer and independent checker are separate
implementations. Symbolic determinant identities, finite-group products, and
cycle decompositions are exact; floating-point tower rows are explicitly
labelled as illustrations and are not used to prove the asymptotic theorem.

## Release boundary

Compilation success is not evidence for Hilbert--Pólya. The formal Route-A
record remains ROUTE_A_REJECTED; the PDF is released as a scoped obstruction
paper.
