# Build and verification

Run from this directory:

```bash
python3 code/verify_weighted_heisenberg.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

This is exactly three `pdflatex` runs in total: one before BibTeX and two
after BibTeX.

Expected outputs:

- control terminus: `ALL WEIGHTED HEISENBERG CONTROLS PASS`;
- `main.pdf`: seven A4 pages in the Stage-2 draft;
- zero unresolved citations or cross-references;
- zero overfull/underfull box warnings;
- all fonts embedded and subset.

The source suppresses volatile PDF dates and trailer identifiers for stable
internal builds.  The code receipt is frozen in `code/verification_output.txt`.

The official two-round GPT-5.4/xhigh mathematical and package audits pass;
their PDFs remain historical pre-Stage-2.5 snapshots.  Stage-2.5 correction
round 1 added direct finite-Heisenberg neighbor citations and owner
subtraction.  Its source and re-verification receipt is
`stage2_5/CORRECTION_ROUND_1.md`; the current local `main.pdf` has SHA-256
`61398af7a4ab61ea3ace029ec315721d4a855bf8f60986c84b2fdc94d9bd0142`.
External release remains **HOLD**; this correction round does not itself close
the remaining authorship, disclosure, or specialist-release gates.
