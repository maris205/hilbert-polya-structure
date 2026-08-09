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

The 2026-08-09 A4.15-integrated draft compiles to a 31-page `main.pdf`, with
33 cited and 33 present bibliography keys, no undefined references or
citations, and no unresolved verification markers.  The PDF has SHA-256
`f8fb4838e410a5127c99411e78978d9a7f7e33309d00ae02c397909046d09808`;
all fonts are embedded.  The only overfull box is a nonmaterial 1.55 pt
bibliography line.  An earlier secondary-agent release-blocking review first
returned `REVISE`; after the unique-oriented-crossing and CRR clean-orbit
repairs, its read-only re-review returned `ACCEPT`.  This PDF remains a
working manuscript artifact, not a frozen journal release.

The draft keeps five evidentiary layers separate:

1. the analytic trace theorem for each fixed
   `0 < delta < delta_tr`, where `delta_tr > 0` is not quantitative;
2. the A4.12--A4.13 local-box computer-assisted theorem on
   `0 <= epsilon <= 0.101`;
3. the R401-SC computation at `delta = 0.01`, which is a numerical
   diagnostic and does not establish `0.01 < delta_tr`.
4. the A4.14 six-tree result on S000/S025/S050, which is an accepted
   implementation certificate;
5. the A4.15 all-slab result, which closes 102 local-complement trees but
   does not supply the phase/global cover needed to quantify `delta_tr`.

In particular, A4.12--A4.15 certify one branch and its reduced-root
uniqueness only inside the declared local box.  They do not close the
phase/global cover or any prime-time, zeta-zero, Hilbert--Polya, or RH gate.

No external figure file is required by the current draft.  The proof
architecture and evidence summaries are rendered as native LaTeX tables and
boxes so that the source remains compilable before publication figures are
frozen.
