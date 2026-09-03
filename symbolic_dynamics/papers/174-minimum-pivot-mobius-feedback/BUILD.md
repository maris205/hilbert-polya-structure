# P174 Round-0 build and verification ledger

**Artifact:** `papers/174-minimum-pivot-mobius-feedback`  
**Status:** `AUTHOR_ROUND0_PASS / PROVISIONAL_AMBER / HOLD_EXTERNAL`  
**Build date:** 2026-09-03 UTC

## Independent verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p174.py
decision: AUTHOR_ROUND0_PASS
external status: PROVISIONAL_AMBER / HOLD_EXTERNAL
complete parameter boxes: 69
parameters: every 2<=k<=p for p=2,3,5,7,11,13,17,19
assertions: 131,018,555
verifier SHA-256: 261f4640f986e47ed00b332d06d5639cedba4969d9df770f50a0878046a12b32
stdout SHA-256: 1faac49f7cb9cdfb7be13caf1a533f36a07851cdff1a9a955b85a3ec593e0646
stdout bytes: 24,534
stdout lines: 1,149
fresh process replays: 2/2
byte-identical replay/output match: yes
```

The verifier imports no scouting or manuscript module.  For each complete
carrier it constructs every edge and checks projective injectivity, the
forced pivot-labelled inverse, `im(M)`, `im(M^2)`, every tail and period,
`M^4=M^2`, fixed and two-periodic points, every target fibre and pivot set,
the full fibre-size distribution, and its mass identity.  It separately
checks the three edges at `(p,k)=(2,2)` and records one edge SHA-256 per box.

Two fresh Python 3.12.3 processes produced byte-identical transcripts.  The
canonical transcript is `verification_output.txt`.  Enumeration supplies
falsification pressure; the uniform proof in `main.tex` establishes the
theorem.

## Canonical build

Toolchain:

```text
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
```

`latexmk` is not installed, so the equivalent explicit settling sequence was
used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained canonical logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  The settled LaTeX and
BibTeX logs contain zero warnings, bad boxes, unresolved citations or
references, rerun requests, or fatal errors.

Two additional builds ran in distinct fresh temporary directories initially
containing only `main.tex` and `references.bib`.  Their retained final logs
are `build_cold1_settled.log`, `build_cold1_bibtex.log`,
`build_cold2_settled.log`, and `build_cold2_bibtex.log`.  Both settled PDFs
match the canonical PDF byte for byte; the three settled pdflatex logs are
themselves byte-identical.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
round-copy byte match: yes
cold-build byte matches: 2/2
pages: 4
bytes: 321,139
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: c1865f487b633477b41ffda5a6a03c0974516c3cea0f30160077e93c3157ec58
font rows: 25
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

All four pages were rendered at 144 dpi and inspected.  The theorem,
displayed formulae, proofs, exact-control table, references, page numbers,
and visible lifecycle line are legible and contained in the A4 page box.
There is no clipping, collision, missing glyph, or malformed table.  The
visible byline and running heads are anonymous.  PDF title, author, subject,
keywords, creator, and producer metadata fields are blank.

## Frozen core hashes

```text
d0013650ec6087ebbaf279a861ebbb6863eb3f348d335c398d820017c6d1da1b  main.tex
b5bab0cc46779f4ebd91e23f2455341b176c31037f48040766088a24d5029a1f  references.bib
261f4640f986e47ed00b332d06d5639cedba4969d9df770f50a0878046a12b32  verify_p174.py
1faac49f7cb9cdfb7be13caf1a533f36a07851cdff1a9a955b85a3ec593e0646  verification_output.txt
c1865f487b633477b41ffda5a6a03c0974516c3cea0f30160077e93c3157ec58  main.pdf
c1865f487b633477b41ffda5a6a03c0974516c3cea0f30160077e93c3157ec58  main_round0_original.pdf
```

## Round boundary

This directory is the author-side Round-0 freeze.  It contains no hostile
Review A or B and makes no external-release decision.  The mathematical
package is exact as stated, but its value/owner status is only
`PROVISIONAL_AMBER / HOLD_EXTERNAL`: the clock is shallow, the order is
artificial, and a general adaptive-section owner may still kill the residual
pivot law.

## Final Round-2 review freeze

The historical section above records the immutable author Round 0.  Review A
returned no finding after 161,536 independent assertions.  Review B passed
4,755,152 assertions and its sole minor canonical-image source repair was
implemented and delta-accepted.

```text
main.tex SHA-256: 5d1790a4fc0f15a79e3632646783598cc3d97da61fca11735c20f881c58df958
references.bib SHA-256: 18b4f989c2bb17ef4c53a2685214b3d2e111924bcca997efb43aca640ecc1066
final PDF pages: 4
final PDF bytes: 321,776
final PDF SHA-256: b428c24be406d8c2cef9c1d6fc5a2630495f2eed54473ed1dec7b1120444ff7f
main.pdf == main_round2.pdf: yes
Round-2 settled warnings/errors: 0
```

Two final temporary directories, each initialized with only `main.tex` and
`references.bib`, reproduced the Round-2 PDF byte for byte.  Their settled
LaTeX and BibTeX logs are retained as `build_final_cold{1,2}_*.log` and have
no warning or error.  The regenerated package manifest is recorded at batch
closeout.  The lifecycle remains `PROVISIONAL_AMBER / HOLD_EXTERNAL`.
