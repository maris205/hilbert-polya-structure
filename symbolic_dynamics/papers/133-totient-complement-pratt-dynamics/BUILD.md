# Build record

## Round-0 isolated build

Date: 2026-08-31 UTC.

Only `main.tex` and `references.bib` were copied into the fresh directory
`/tmp/p133-round0-ogbipz` and built in four stages:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

| stage | status |
|---|---:|
| pdflatex 1 | 0 |
| bibtex | 0 |
| pdflatex 2 | 0 |
| pdflatex 3 | 0 |

The settled log and BLG contain no LaTeX/package warning, overfull or
underfull box, undefined citation/reference, multiply-defined label, or
actionable rerun request.  All three cited keys have matching `bibcite`
records.  Two disclosed bare `qquad` tokens found during the author-side
visual gate were repaired before this final isolated build.

## PDF audit

```text
pages=3
page_size=A4 (595.276 x 841.89 pt)
file_size=346509 bytes
fonts=28
nonembedded_fonts=0
pdf_sha256=bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b
round0_sha256=bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b
main_vs_round0_cmp=0
```

All three pages were rasterized and visually inspected.  No clipping,
collision, malformed formula, bad line break, or orphan bibliography page
was found.  The decoder and two-step phase displays contain spacing commands
rather than literal text.  `pdfinfo` reports blank Title, Subject, Keywords,
and Author metadata.  The visible author is `Anonymous`.

## Frozen source and control hashes

```text
3f62efbd5a23a5a0a811e92f4f975ba643cd4262b958c6c6ab0804920f602835  main.tex
3311a309139704fb8712bb152895ce5dec7e0ddbe087d44e4a20504976b83e2d  references.bib
841ed6f77091e0d0e6721c24dc334891f8bc3b54701717153da49ecbb391262a  code/verify.py
1c90aea14a3c45d084ec9cd6d86e951d3508494d94fa04afa6bd6ec12692b99d  code/verification_output.txt
bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b  main_round0_original.pdf
```

Round 0 is frozen and must not be overwritten.  External status is
`HOLD_EXTERNAL`.

## Round-1 support-only repair

Review A changed only `PAPER_PLAN.md` and `CLAIMS_EVIDENCE.md`; `main.tex`,
the bibliography, verifier, and canonical output are unchanged.  A fresh
verifier replay returned `cmp=0`.  A four-stage isolated build in
`/tmp/p133r1iso.jK4Tde` reproduced the reviewed PDF byte for byte.

`main.pdf`, `main_round0_original.pdf`, and `main_round1.pdf` are all three
A4 pages, 346,509 bytes, with SHA-256
`bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b`.
The settled log remains warning-, bad-box-, and undefined-reference-free;
all 28 font rows pass the embedding/subsetting/Unicode gate.  External status
remains `HOLD_EXTERNAL`.

## Round-B audit

The independent Round-B reviewer replayed the 4,774-assertion verifier,
repeated the isolated build, inspected all three pages, and confirmed that
`main.pdf`, `main_round0_original.pdf`, and `main_round1.pdf` remain
byte-identical at SHA-256
`bbb869d485230bc0165bbe49ff43929de61700c1e0acc960a541b64b23651d7b`.
No manuscript or PDF repair was requested.
