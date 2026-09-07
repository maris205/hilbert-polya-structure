# C414 final fresh-build and all-page inspection receipt

Status: **PASS — two fresh builds, identical PDFs, all nine final pages viewed**.
Actual execution date: 7 September 2026 UTC. Executor: the coordinator-delegated
current-team agent `scout_henon_arithmetic`, not the root coordinator personally
and not a human reviewer. This records the final build gate, separately from
the accepted mathematical/manuscript reviews and the later release seal.

## Final artifact

[main.pdf](main.pdf): **9 pages, 355,639 bytes**, unencrypted letter-size PDF 1.5.
Both fresh outputs and the delivered copy have SHA-256
`7c9502e4f76c5ba4fc7478e441e8a4b2e944bd4e1e9f211ac6e7a34be6ff7751`.
The a/b PDF `cmp` and the delivered/a `cmp` both exited 0. The main argument,
scope and references end on page 9; there is no appendix or selected venue
page cap. The author PDF is preserved at `build_author/main.pdf`, SHA-256
`23f41109cd6fa6f3c5f4eb209f1274ed4a45c77dd4ab34d3257dcd0d245267fe`.
Its historical hash is not the final PDF hash.

## Genuine clean inputs and commands

The actual `mktemp -d /tmp/c414-c415-c418-final.XXXXXX` invocation created
`/tmp/c414-c415-c418-final.S4SZJP`. This paper's two previously absent build
directories were:

```text
/tmp/c414-c415-c418-final.S4SZJP/C414_height_distribution/a
/tmp/c414-c415-c418-final.S4SZJP/C414_height_distribution/b
```

Only `main.tex`, `references.bib` and the seven TeX files in `sections/`
were copied into each directory. No PDF, auxiliary, bibliography output or
author cache was an input. There is no `math_commands.tex` for this paper.
All seven section files are actually included by `main.tex`. The nine
current inputs were compared individually with both copies: **18 source
`cmp` comparisons, all exit 0**. No manuscript input was edited during this
execution or after the comparisons.

In each directory the actual build command was:

```bash
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both invocations exited 0 after Latexmk's necessary bibliography/reference
passes. Shell `pipefail` preserved the build status while the complete console
was retained with `tee`; it was not inferred from a final line of output.
There was no failed final attempt or source repair. Pass a's PDF was copied
to the delivered `main.pdf` only after the a/b comparison passed.

Environment actually checked: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live
2022/dev/Debian), Latexmk 4.76, BibTeX 0.99d, Poppler `pdftoppm` 22.02.0.
The source epoch denotes 6 September 2026 00:00:00 UTC, displayed by
`pdfinfo` as 08:00:00 CST. This frozen PDF metadata date is not the actual
execution date or the article's printed date, which is 7 September 2026.

The compared source inputs had these SHA-256 values:

```text
1944b5a5b8275c8ce296bb59499a5ff5b84295b67d522c8081087a4746cc17b6  main.tex
f39b2c2588908287103bb78dd40b57195799d35f1f3bcbb9fccf2b5ec0cd7fb8  references.bib
abcd57bf98d12a0002a5dbe97f5167ac857c8a4c1ec2f432356405e892562642  sections/1_introduction.tex
1a154a3d6099066891b7afded962b9638c8d4d7b37aa3476729cf271fd40cd89  sections/2_statements.tex
ddd5b8bd28f98c7921d1491e144374b2727640f648a1525e72a49cb9728be4e0  sections/3_valleys.tex
13b55130f40796a37e5e852413c760e838db32a71414a6ca366396ef3fe1a5d1  sections/4_series.tex
9258a0bdeebb44174a581af790d7bf6e5767eb4f640252116ff034ca68dea6cb  sections/5_poles.tex
4e727afc7cd2ffb6ef45e62c50b6e011fa3c77f226042ac5ce9f36dfdb5f310a  sections/6_counting.tex
c1bbd439636798485fef145db5baf9de461f5d28b50c3e48d23d60dca28177c6  sections/7_scope.tex
```

## Final logs, text and fonts

Both final TeX logs and the final bibliography log had zero matches for
`Warning`, `Overfull`, `Underfull`, `undefined`, `Missing character`,
`multiply defined`, `LaTeX Error` and `Fatal error`. The a/b bibliography
logs also passed `cmp`. The searches' exit 1 means no matches; it is not
misreported as an exit-0 search. Ordinary first-pass reference warnings
remain in the unfiltered console logs and are resolved in the final logs.

`pdftotext -layout` produced [the final text](final_build/main.txt), with no
`??`, `[?]`, `[VERIFY]`, TODO, TBD, FIXME or PLACEHOLDER matches. All 21
font-object rows are embedded, subset Type 1 with Unicode maps; zero bad
font rows and no Type 3 fonts. The anonymous title page and the complete
reference list were also visibly checked.

Exactly eight genuine evidence files are retained in `final_build/`:

```text
4e9a2d7ee63ee7f17e7dcef91eaf4d2a34d968a973c50975ea7fe0b66a6aa385  bibliography.blg
4da3208727a7484ab117f72611df9421b59b2c2efa0dc670c7b6d85552aabe40  fonts.txt
fcce11ec480ab238d5238daba8bc7ea98f7899aa347554cbf55ea105dadc27ec  main.txt
b5fe47a08f95ca26c284af6afe8d95f12e4007f0ca9996ebdb71f5017c8f3fa2  pass_a.console.log
3b330994b7af99d4b0cf3162adadb28d037ccfc8914f2a04ebc15c4773ec83d2  pass_a.log
b5fe47a08f95ca26c284af6afe8d95f12e4007f0ca9996ebdb71f5017c8f3fa2  pass_b.console.log
3b330994b7af99d4b0cf3162adadb28d037ccfc8914f2a04ebc15c4773ec83d2  pass_b.log
be0221c2af8383b14bbf77a01eadabb7227eaddf9a31a4b641abb58684fa5561  pdfinfo.txt
```

## Every final page actually displayed

The actual render command, with the paths above, was:

```bash
pdftoppm -r 100 -png \
  /tmp/c414-c415-c418-final.S4SZJP/C414_height_distribution/a/main.pdf \
  /tmp/c414-c415-c418-final.S4SZJP/C414_height_distribution/page
```

All nine resulting `page-1.png` through `page-9.png` were individually
displayed and visually inspected in groups 1–3, 4–6 and 7–9.

| Page | Actual inspection result |
|---:|---|
| 1 | PASS: title, abstract and three contribution statements are legible. |
| 2 | PASS: source qualifications, section heading and height definitions fit. |
| 3 | PASS: piecewise multiplicities, all three theorems and floor asymptotic fit. |
| 4 | PASS: valley proof and paired forward/backward-height displays are unclipped. |
| 5 | PASS: census table and its full caption fit; sector formula is readable. |
| 6 | PASS: finite-lattice numerator, sector sum and convergence proof fit. |
| 7 | PASS: combined-residue factors, numbered displays and level-one paragraph fit. |
| 8 | PASS: double-pole continuation, boundary argument and counting estimates fit. |
| 9 | PASS: counting closure, scope and all four references are complete and legible. |

No page has clipping, overlapping text, missing glyphs, an unresolved
reference or an accidental blank page. Temporary build copies and final
renders are execution provenance, not delivered dependencies or new paper
figures. No mathematical script, frozen certificate or old-batch build was
rerun. The `paper-compile` and local final-release workflow determined these
checks; successful typesetting and byte identity do not prove mathematics,
priority, target arithmetic or a Hilbert–Pólya realization. Source files,
author-build evidence, global state, evaluation and Git were not changed.
