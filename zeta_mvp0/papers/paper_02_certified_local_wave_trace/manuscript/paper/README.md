# Paper 02 LaTeX draft

This directory contains the modular working manuscript for **A Local
Relative Gutzwiller Trace and a Certified Fast Branch for a Clock-Preserving
H\'enon Schr\"odinger Pair**.

Build from this directory with `latexmk` when available:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The current server does not provide `latexmk`; the verified fallback build
is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The 2026-08-07 draft compiles to a 31-page `main.pdf`, with 33 cited and 33
present bibliography keys, no undefined references, and no undefined
citations.  A secondary-agent release-blocking review first returned
`REVISE`; after adding the unique-oriented-crossing lemma and correcting the
CRR clean-orbit wording, its read-only re-review returned `ACCEPT`.  The PDF
is a working manuscript artifact, not a frozen journal release.

After accepting the bounded A4.14 representative-complement certificate, a
fresh four-pass build retained 31 pages and incorporated the six-tree result
only in the scope, conclusion, and reproducibility layers.  The resulting
PDF has SHA-256
`b5687e8a715f3c431916933298c647c58650d9ca1c4a5dcea008bdb8fc4c938a`;
all fonts are embedded.  The only overfull box is a nonmaterial 1.55 pt
bibliography line.

The draft keeps three evidentiary layers separate:

1. the analytic trace theorem for each fixed
   `0 < delta < delta_tr`, where `delta_tr > 0` is not quantitative;
2. the A4.12--A4.13 local-box computer-assisted theorem on
   `0 <= epsilon <= 0.101`;
3. the R401-SC computation at `delta = 0.01`, which is a numerical
   diagnostic and does not establish `0.01 < delta_tr`.
4. the A4.14 six-tree result on S000/S025/S050, which is an accepted
   implementation certificate and not an all-slab complement theorem.

In particular, the A4.12--A4.13 interval certifies only the selected branch
inside its frozen primary boxes and guarded bridges.  It does not close the
root complement, phase/global cover, or any prime-time, zeta-zero,
Hilbert--Polya, or RH gate.

No external figure file is required by the current draft.  The proof
architecture and evidence summaries are rendered as native LaTeX tables and
boxes so that the source remains compilable before publication figures are
frozen.
