# C415 final fresh-build and all-page inspection receipt

Status: **PASS — two fresh builds, identical PDFs, all eleven final pages viewed**.
Actual execution date: 7 September 2026 UTC. Executor: the coordinator-delegated
current-team agent `scout_henon_arithmetic`, not the root coordinator personally
and not a human reviewer. The nonauthor manuscript gate, including R1, was
closed before this execution; this receipt does not replace that review.

## Final artifact

[main.pdf](main.pdf): **11 pages, 388,061 bytes**, unencrypted A4 PDF 1.5.
Both fresh outputs and the delivered copy have SHA-256
`f99a764cef94525d88acb427e9d89040a6ab2ba98c2c3b7ce7f72f79e94f20cf`.
The a/b PDF `cmp` and the delivered/a `cmp` both exited 0. The main
argument, scope and all five references end on page 11; there is no
appendix or selected venue page cap. The author PDF at
`build_author/main.pdf` was preserved. Its current affected-R1 hash happens
to equal the final hash; no author PDF or cache was used in either fresh build.

## Genuine clean inputs and commands

The actual `mktemp -d /tmp/c414-c415-c418-final.XXXXXX` invocation created
`/tmp/c414-c415-c418-final.S4SZJP`. This paper's two previously absent build
directories were:

```text
/tmp/c414-c415-c418-final.S4SZJP/C415_degree_2p/a
/tmp/c414-c415-c418-final.S4SZJP/C415_degree_2p/b
```

Only `main.tex`, `math_commands.tex`, `references.bib` and the nine TeX
files in `sections/` were copied into each directory. No PDF, auxiliary,
bibliography output or author cache was an input. All nine section files
and the macro file are actually included by `main.tex`. The twelve current
inputs were compared individually with both copies: **24 source `cmp`
comparisons, all exit 0**. No manuscript input was edited during this
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
The pinned source epoch is 6 September 2026 00:00:00 UTC. This paper's
unchanged preamble already suppresses PDF dates, trailer IDs and the
specified pdfTeX metadata; no suppression was added during final execution.
The printed article date is 7 September 2026. The preamble does not
constitute evidence that a build used prior outputs.

The compared source inputs had these SHA-256 values:

```text
1cf7305d705045cdc75bd75a62071b59f1e574edb8ed20fcaf7dee085cec9bab  main.tex
80d91ef1fd11269635dac0b85d6cd6d113871abc810b05e7ea7d7ae9bbcf7f48  math_commands.tex
9f1c7948fef2a4ac6e8483267a356447915c731c9c25cba2b6d4eee6238dccca  references.bib
1b11c0d81e2d565c6aa138c5cfa0a630f5b6c0ad3287ed29b92a91cedbd75e3b  sections/0_abstract.tex
9aaccd5d1165dbb1c8ed20093e8b1663108be3425fc1faa05cba87ea9c049e3c  sections/1_introduction.tex
1125e37e77b09ee34c54aedc67650d4efa3b5fa208fd4893762f196f473c910c  sections/2_setup.tex
40960a62f0414eeaa7b4e6c4b13bc305bd906c946530a00b3fac1e36ebcdc28c  sections/3_count_conversion.tex
29e3e70d2f1de3c3d2d23932bc315e24cbcdae5974134c5e8ca97e0f6c8dc0b3  sections/4_high_support.tex
a9127aa1b0dac92a7f2c9a70890be3aaaea1bfefa40749de4ab14625a4a84b30  sections/5_perfected_ring.tex
1df90c48ab6fa12a504693d7684ed8de37b21ed4399d82d2326ea7443a4aa512  sections/6_low_support.tex
6d8ad6bfa6772e101f56b671d7c8c40910a513f7157cad435a2567382e7b6457  sections/7_zeta.tex
fd8333304100cfb07c594bb6e5974ae98ea0537857e8410dd18f000a6d0b0e21  sections/8_scope.tex
```

## Final logs, text and fonts

Both final TeX logs and the final bibliography log had zero matches for
`Warning`, `Overfull`, `Underfull`, `undefined`, `Missing character`,
`multiply defined`, `LaTeX Error` and `Fatal error`. The a/b bibliography
logs also passed `cmp`. The searches' exit 1 means no matches; it is not
misreported as an exit-0 search. Ordinary first-pass reference warnings
remain in the unfiltered console logs and are resolved in the final logs.

`pdftotext -layout` produced [the final text](final_build/main.txt), with no
`??`, `[?]`, `[VERIFY]`, TODO, TBD, FIXME or PLACEHOLDER matches. All 26
font-object rows are embedded, subset Type 1 with Unicode maps; zero bad
font rows and no Type 3 fonts. The anonymous title and complete five-item
bibliography were also visibly checked.

Exactly eight genuine evidence files are retained in `final_build/`:

```text
15ef78ef320736474c3a8b7779ad4bec38d7232b4eb019015237dc3cdd74f2c2  bibliography.blg
e86c967226e8616356675f30e1bfa195b203d6958e6434a673ff5bf99f5d57cf  fonts.txt
fa26c51d75446616fae1dfb21bcde72bd72144cfdc2cf237f3d2089ccd7c7171  main.txt
b674fbfb619e89913727caf763cdf56906a190c7f2247316ec0b2501e0c2355c  pass_a.console.log
0c660000825789d91c6aad2fb503ef1e6f935cfb4d58bc55565b2dab82777a49  pass_a.log
b674fbfb619e89913727caf763cdf56906a190c7f2247316ec0b2501e0c2355c  pass_b.console.log
0c660000825789d91c6aad2fb503ef1e6f935cfb4d58bc55565b2dab82777a49  pass_b.log
4bd70cae9458c53a8f84e587c3f7b393d892e9417e68a98ab711109213127f7e  pdfinfo.txt
```

## Every final page actually displayed

The actual render command, with the paths above, was:

```bash
pdftoppm -r 100 -png \
  /tmp/c414-c415-c418-final.S4SZJP/C415_degree_2p/a/main.pdf \
  /tmp/c414-c415-c418-final.S4SZJP/C415_degree_2p/page
```

All eleven resulting `page-01.png` through `page-11.png` were individually
displayed and visually inspected in groups 1–3, 4–6, 7–9 and 10–11.

| Page | Actual inspection result |
|---:|---|
| 1 | PASS: title, abstract, keywords and quantified family setup are legible. |
| 2 | PASS: both formula branches, boxed count and degree-state table fit. |
| 3 | PASS: source comparison, inverse/equalizer formulas and leading coefficients fit. |
| 4 | PASS: count-conversion proof, quotient basis and reducedness paragraph fit. |
| 5 | PASS: strict-gap bounds and high-support induction are unclipped. |
| 6 | PASS: recurrence closure, perfected-ring union and operator identities fit. |
| 7 | PASS: mixed-monomial bound and fractional-exponent lemma are legible. |
| 8 | PASS: fractional expansion, semilinear state and polynomial descent fit. |
| 9 | PASS: coefficient descent, main-theorem closure and zeta product fit. |
| 10 | PASS: product theorem continuation, radial orders and natural-boundary proof fit. |
| 11 | PASS: support example, corrected finite-expression paragraph and all five references fit. |

The final R1 wording is visibly present on page 11: the perfected-ring
calculation uses finite algebraic expressions and each iterate lies at a
finite denominator level; it does not call the ring finite. No page has
clipping, overlap, missing glyphs, an unresolved reference or an accidental
blank page. Temporary build copies and renders are provenance, not delivered
dependencies or new figures. No mathematical script, frozen certificate
or old-batch build was rerun. The `paper-compile` and local final-release
workflow determined these checks; typesetting and byte identity do not prove
mathematics, priority, target arithmetic or a Hilbert–Pólya realization.
Sources, author evidence, global state, evaluations and Git were unchanged.
