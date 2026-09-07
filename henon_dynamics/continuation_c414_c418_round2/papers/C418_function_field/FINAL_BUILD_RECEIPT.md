# C418 final fresh-build and all-page inspection receipt

Status: **PASS — two fresh builds, identical PDFs, all nine final pages viewed**.
Actual execution date: 7 September 2026 UTC. Executor: the coordinator-delegated
current-team agent `scout_henon_arithmetic`, not the root coordinator personally
and not a human reviewer. This is a final build/visual gate, separate from
the closed mathematical/manuscript reviews and the later release seal.

## Final artifact

[main.pdf](main.pdf): **9 pages, 341,957 bytes**, unencrypted letter-size PDF 1.5.
Both fresh outputs and the delivered copy have SHA-256
`03ed775fb021192104288bdbac99cd2b5b044906c6dfcf63b51a2dc1f84bd525`.
The a/b PDF `cmp` and the delivered/a `cmp` both exited 0. The argument
and scope finish on page 9, followed by both references; there is no
appendix or selected venue page cap. The author PDF remains at
`build_author/main.pdf`, SHA-256
`0c9d6c53a422b8a8733cfaab68afdc0b60daedec57c46468973e63e1d844ac6e`.
Its historical hash is not the final PDF hash.

## Genuine clean inputs and commands

The actual `mktemp -d /tmp/c414-c415-c418-final.XXXXXX` invocation created
`/tmp/c414-c415-c418-final.S4SZJP`. This paper's two previously absent build
directories were:

```text
/tmp/c414-c415-c418-final.S4SZJP/C418_function_field/a
/tmp/c414-c415-c418-final.S4SZJP/C418_function_field/b
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
was retained with `tee`; it was not inferred from a final output line.
There was no failed final attempt or source repair. Pass a's PDF was copied
to the delivered `main.pdf` only after the a/b comparison passed.

Environment actually checked: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live
2022/dev/Debian), Latexmk 4.76, BibTeX 0.99d, Poppler `pdftoppm` 22.02.0.
The source epoch denotes 6 September 2026 00:00:00 UTC, displayed by
`pdfinfo` as 08:00:00 CST. This frozen metadata date is not the actual
execution date or the printed article date, which is 7 September 2026.

The compared source inputs had these SHA-256 values:

```text
dade97cf4fbf9ddb22cd35d3766242d100b666eb1cbc81937c0d8ce7d8de7084  main.tex
21284d37d84251e0530839c58c4194d2e4cac12cdd8ddf871b37da450ec6284b  references.bib
1072ab97376e6af235818a5b6709145ccf8f5dd877ba4ddd9a13f6a391cff995  sections/1_introduction.tex
5acf2c7e22a428b7db896f1e2d18e153de8b10847ef99fa8af08904a01bba319  sections/2_atlas.tex
aba8abbd23791cbd65313b10af779e0009085b415c0aba1dd3b6b35cc702926a  sections/3_rigidity.tex
9e9ba15b02b6ebb5f3dd14dd2451976f3d4e7c83d10ccffb8fdb39c223faa85d  sections/4_graph.tex
3ff5268060984a44198bf41eea82715c28b57f7df168670a0972cc3a1814b70e  sections/5_exhaustion.tex
cefda173fc4768d59c76d2872df9ed208ec3e2687ff84cbce4ace8e21c8d6aa2  sections/6_bounds.tex
9de374757f3bebc856e1b1368a80282037ef548dc659a28d0fdd0bbf18f69017  sections/7_scope.tex
```

## Final logs, text and fonts

Both final TeX logs and the final bibliography log had zero matches for
`Warning`, `Overfull`, `Underfull`, `undefined`, `Missing character`,
`multiply defined`, `LaTeX Error` and `Fatal error`. The a/b bibliography
logs also passed `cmp`. The searches' exit 1 means no matches; it is not
misreported as an exit-0 search. Ordinary first-pass reference warnings
remain in the unfiltered console logs and are resolved in the final logs.

`pdftotext -layout` produced [the final text](final_build/main.txt), with no
`??`, `[?]`, `[VERIFY]`, TODO, TBD, FIXME or PLACEHOLDER matches. All 20
font-object rows are embedded, subset Type 1 with Unicode maps; zero bad
font rows and no Type 3 fonts. The anonymous title and the full two-item
reference list were also visibly checked.

Exactly eight genuine evidence files are retained in `final_build/`:

```text
a4630bbf295d7118387f0e49a72545c3b604ee72956279749f7a6799494fd3da  bibliography.blg
9dc0dd3e02eb6d6f41d7eb8833da27ce7dd7edb431026f9b9fd9f4d5484fe481  fonts.txt
d9c2c9d95fb6a14bfc5bc2502d46af9afe817e86d406d9bf965adc5c3d86fc23  main.txt
a9228b90bb8c4d0b3bcbbc05b42c71caa2987bd03579d7f65607da0c4b0d6b1f  pass_a.console.log
d71d41674083d23ac230bb8483b13e3192074aea97a337f6a057e034473acbaa  pass_a.log
a9228b90bb8c4d0b3bcbbc05b42c71caa2987bd03579d7f65607da0c4b0d6b1f  pass_b.console.log
d71d41674083d23ac230bb8483b13e3192074aea97a337f6a057e034473acbaa  pass_b.log
4767a542a1b512d4aa1b8d893ff743dbbc55aaab6936f0940af7c070d56b6d60  pdfinfo.txt
```

## Every final page actually displayed

The actual render command, with the paths above, was:

```bash
pdftoppm -r 100 -png \
  /tmp/c414-c415-c418-final.S4SZJP/C418_function_field/a/main.pdf \
  /tmp/c414-c415-c418-final.S4SZJP/C418_function_field/page
```

All nine resulting `page-1.png` through `page-9.png` were individually
displayed and visually inspected in groups 1–2, 3–5 and 6–9.

| Page | Actual inspection result |
|---:|---|
| 1 | PASS: two-line title, abstract and quantified nonconstant family fit. |
| 2 | PASS: source/conjugacy comparison and cycle-atlas setup are legible. |
| 3 | PASS: uniqueness up to sign, reconstruction, seven-row atlas and sharp-bound theorem fit. |
| 4 | PASS: finite-pole/common-degree proofs, centered-parameter argument and sign equations fit. |
| 5 | PASS: all sixteen edge entries, wide signed-label formula and injectivity statement fit. |
| 6 | PASS: graph reconstruction and five least-state cases are legible. |
| 7 | PASS: sign lift, period reasoning and all parameter-collision cases fit. |
| 8 | PASS: three equality-locus cycles, return/zeta identities and scope opening fit. |
| 9 | PASS: scope closure and both complete references fit; remaining white space is an ordinary final-page ending. |

No page has clipping, overlap, missing glyphs, an unresolved reference or
an accidental blank page. Temporary build copies and final renders are
execution provenance, not delivered dependencies or new paper figures.
No mathematical script, frozen certificate or old-batch build was rerun.
The `paper-compile` and local final-release workflow determined these checks;
typesetting and byte identity do not prove mathematics, priority, target
arithmetic or a Hilbert–Pólya realization. Sources, author-build evidence,
global state, evaluations and Git were unchanged.
