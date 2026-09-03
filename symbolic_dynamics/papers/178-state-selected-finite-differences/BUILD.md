# P178 build and verification record

**Artifact:** anonymous AMS short note, Round 2 dual-review freeze  
**Settled date:** 2026-09-03 UTC  
**External state:** `OWNER_THIN / HOLD_EXTERNAL`

## Toolchain

- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- BibTeX 0.99d (TeX Live 2022/dev/Debian)
- Python 3.12.3
- Poppler `pdfinfo` / `pdffonts` 22.02.0

The installed environment has no `latexmk` executable, so the explicit
settling sequence below is the canonical build.

## Exact verifier

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 verify_p178.py
cmp -s verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 verify_p178.py)
~~~

Two fresh executions matched byte for byte. The settled transcript records:

- result: `PASS`;
- assertions: `44,689`;
- literal arrows: `3,156`;
- exhaustive literal primes: \(2,3,5\);
- modular flag/anchor primes: \(2,3,5,7,11,13,17,19\);
- edge digest:
  `35a2ac173151700d2840526791cd3d2c743f4660f1075bea7e924cfd12de1a89`;
- transcript SHA-256:
  `cc5443ae10945425723343fb1fc0116915ed96f51116a3463b23c0d7ce8d974f`.

The program imports no project, paper, or scouting module. Its direct-tuple
literal census is separately organized from the discovery verifier, but it
remains author-side evidence rather than process-independent review.

## PDF build

~~~sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The corresponding logs are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and
`build_pdflatex_3.log`. The settled final pass has no warning, unresolved
reference or citation, bad box, rerun request, or error.

## Frozen Round-0 artifact

- pages: 3;
- page box: A4, 595.276 by 841.89 points;
- bytes: 294,428;
- PDF version: 1.5;
- encryption: none;
- forms and JavaScript: none;
- metadata Title, Subject, Keywords, Author, Creator, and Producer: empty;
- font rows: 24;
- embedded/subsetted/Unicode-mapped font rows: 24/24/24.

The PDF was rendered at 150 dpi into `qa_round0/page-{1,2,3}.png`.
All three pages were inspected. The theorem continuation, piecewise fibre
formula, anchored-lift proof, Jordan calculation, references, running heads,
and page numbers are legible and inside the page box.

Two isolated source-only cold builds, each initialized with only `main.tex`
and `references.bib`, reproduced the settled PDF byte for byte. The frozen
`main_round0_original.pdf` is also byte-identical to `main.pdf`.

## Frozen Round-0 hashes

~~~text
d89e740fa45a8ad21a1244c504ec3288cce1e887f7ca2dd14febe4822e7b3603  main.tex
87dbf2eb892006705a842eb2f698c98c2d27f7c164cff478fe4043e4764c9bae  references.bib
741809992a81b3ae635bd6569684e6b4e28ce725c50ef574b9cc3dcb749cef79  verify_p178.py
cc5443ae10945425723343fb1fc0116915ed96f51116a3463b23c0d7ce8d974f  verification_output.txt
b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce  main_round0_original.pdf
~~~

## Round-1 documentation repair

The first hostile review found no mathematical defect and one provenance
Minor.  All author-control descriptions now say “paper-local author-side” or
an equivalent phrase, reserving process independence for hostile reviewers.
No theorem source changed, so the deterministic Round-1 PDF is byte-identical
to Round 0:

~~~text
d89e740fa45a8ad21a1244c504ec3288cce1e887f7ca2dd14febe4822e7b3603  main.tex
15dfd47bbcc1bc187e48909a11d7d832286526d3b7efa43a393650f1d44f1e6e  verify_p178.py
cc5443ae10945425723343fb1fc0116915ed96f51116a3463b23c0d7ce8d974f  verification_output.txt
b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce  main.pdf
b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce  main_round1.pdf
~~~

The author verifier replays byte-identically.  Reviewer A independently
checks 53,524 assertions (including the `GF(4)` scope guard), and Reviewer B
checks 36,899; both close with zero findings.  Round 2 intentionally retains
the unchanged theorem bytes:

~~~text
main.pdf/main_round0_original.pdf/main_round1.pdf/main_round2.pdf:
b637423674d7ec40f0e1e316a60f92b1dc5cc3d30061c8cbd444c8aaab5e76ce
two final source-only cold builds: byte-identical PASS
final visual pages inspected: 3/3 PASS
~~~

See `FINAL_QA.md`; external status remains `HOLD_EXTERNAL`.
