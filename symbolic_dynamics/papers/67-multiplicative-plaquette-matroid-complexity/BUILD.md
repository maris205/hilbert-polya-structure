# Build and verification

From this package directory:

```sh
export SOURCE_DATE_EPOCH=1787616000
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` is not installed in the frozen environment, so the explicit
`pdflatex -> bibtex -> pdflatex x2` sequence is authoritative.

Run the deterministic companion control with:

```sh
python3 code/verify_plaquette_matroid.py
```

It must terminate with `ALL CHECKS PASS`.  Its live output must be
byte-identical to both
`code/verify_plaquette_matroid.out` and
`build/verify_plaquette_matroid.current.out`.

## Expected artifact gate

- PDF: `main.pdf`
- document class: journal-neutral `amsart`, 11 pt, A4
- bibliography: 11 cited and metadata-verified entries
- required warnings: zero undefined references/citations and zero overfull
  boxes
- fonts: all embedded and subset
- author PDF metadata: empty
- control dependency: Python 3 standard library only

The exact modular controls are regression evidence only; all infinite and
arbitrary-size results are proved in the manuscript.

## Review and release status

Two earlier independent cross-agent review rounds and two subsequent official
`gpt-5.4 xhigh` rounds are complete.  The official Round-2 proof audit returned
mathematics **PASS** and identified one stale release-trail defect; the latter
is resolved by synchronizing all QA and hash records to the canonical PDF.
No numerical reviewer score was supplied or invented.

The official-review PDFs remain historical pre-Stage-2.5 snapshots.  After
Stage-2.5 correction round 1, the current local corrected artifact is
`main.pdf`, with SHA-256
`ed2ffeedc97cc82d006bf540468ef7bf9c1655cad3f4600fb393f8d6451fc7da`.
The source changes and re-verification receipt are recorded in
`stage2_5/CORRECTION_ROUND_1.md`.  A clean build with the declared epoch
reproduces this current artifact byte-for-byte.

This remains an anonymous internal draft.  External release is **HOLD**;
Stage-2.5 correction round 1 does not itself certify completion of the full
integrity, authorship, or specialist-release gates.
