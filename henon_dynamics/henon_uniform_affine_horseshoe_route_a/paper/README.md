# Paper build

From this directory run `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
twice.  The release process checks deterministic SHA-256 output, embedded
fonts, layout warnings, and undefined references.  The three round PDFs record
the theorem draft, adversarial pass, and final claim-boundary pass.
