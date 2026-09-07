# C415 author handoff

Status: **COMPLETE AUTHOR DRAFT / AUTHOR BUILD PASS**.
Date: 7 September 2026. This is not the nonauthor manuscript review or
the coordinator's final two-fresh-build release certificate.

## Deliverable and scope

The anonymous English mathematical article is `main.tex`, with one
abstract file and eight substantive section files, `math_commands.tex`,
five-entry `references.bib`, and `CITATION_AUDIT.md`. The author PDF is
`main.pdf`, an exact copy of `build_author/main.pdf`.

The complete frozen C415 theorem is in Theorem 1.1. The count conversion
is Proposition 3.1; the high-support state is Proposition 4.2; the
perfected mixed-monomial bound is Lemma 5.1; the integral/fractional
expansions, semilinear state and descent are Lemma 6.1 and Propositions
6.2–6.3. Theorem 7.1 proves the native zeta product and natural boundary
for every positive integral power. No proof rests solely on a scout
file or executable certificate.

Preserved quantifiers: all odd p, all q=p^e with e>=3, every degree-2p
g over F_q, every a in F_q^*, all geometric affine-plane points, every
positive S-iterate, ordinary points rather than unproved scheme lengths.
The c=0 face, q=p^3, mixed perfected remainders, non-prime-field
coefficients and actual polynomial descent are explicit. The root-order
index in the analytic proof is r>=1 and is separate from a and
w=p^{v_p(n)}.

## Author verification actually performed

The build command was run from this paper directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build_author main.tex
```

It exited 0. There were three author-build invocations: the initial
complete draft; an affected rebuild after a local wording clarification
and rendered bibliography locators; and an affected rebuild after using
the standard small bibliography font to avoid a nearly empty spill page.
These are ordinary author revisions in the same build directory, **not
two independent fresh release builds**. Bootstrap undefined-reference
warnings in early LaTeX passes were resolved by latexmk/BibTeX; they are
not described as failures of the final log.

The actual final checks were:

```sh
rg -n 'Warning|Overfull|Underfull|undefined|multiply defined|LaTeX Error|Fatal error' build_author/main.log build_author/main.blg
pdfinfo build_author/main.pdf
pdffonts build_author/main.pdf
pdftotext -layout build_author/main.pdf build_author/main.txt
rg -n '\\cite|\\nocite|^@' sections references.bib
rg -n 'TODO|FIXME|PLACEHOLDER|TBD|\\input|\\include' main.tex math_commands.tex sections
```

Results:

- The final LaTeX/BibTeX diagnostic search returned no matches (rg exit 1,
  the expected no-match status), with no errors, unresolved references,
  multiply defined labels, font warnings, overfull boxes or underfull boxes.
- The PDF is 11 A4 pages, 388,043 bytes, PDF 1.5, unencrypted, with
  `Anonymous Authors` metadata and no JavaScript.
- Every listed font is embedded and subsetted; all have Unicode mapping.
  No Type 3 or unembedded font is listed.
- The full initial PDF text was read, followed by the affected final
  Jacobian paragraph and complete rendered bibliography. All citations
  resolve to the five actual entries. No `nocite` or placeholder is used.
- Raster previews of every page of the complete draft were visually read.
  Final changed pages 4 and 11 were rendered and visually reread after
  the affected edits. The two formula branches, degree blocks, fractional
  powers, product, support table and bibliography are legible and not
  clipped. The earlier intermediate 12-page preview was not retained as
  the delivered PDF; files in `build_author/` are author working artifacts.

The raster commands actually used were:

```sh
pdftoppm -scale-to 1200 -png build_author/main.pdf build_author/page
pdftoppm -scale-to 1200 -f 11 -l 12 -png build_author/main.pdf build_author/finalpage
pdftoppm -scale-to 1200 -f 4 -l 4 -png build_author/main.pdf build_author/finalpage
pdftoppm -scale-to 1200 -f 11 -l 11 -png build_author/main.pdf build_author/finalpage
```

The second command belongs to the intermediate bibliography-spill check;
the final document is 11 pages. No mathematical census, frozen certificate,
training run, external model API, or old-batch build was run.

## Reverse outline and citation closure

The section sequence was read back from the compiled text:

1. Exact family, complete formula, high/low partition, source subtraction.
2. One map and one clock, explicit inverse, equalizer, operator meanings.
3. Conditional all-period conversion, finite quotient and ordinary count.
4. Uniform strict gaps and every term in the high-support induction.
5. Concrete finite perfection, coefficient semilinearity and arbitrary mixed tail.
6. Fractional exceptional term, invariant, descent and leading coefficient.
7. Normalized native zeta, absolute interchange and dense nonintegral orders.
8. Theorem-derived q=27 comparison and explicit exclusions.

The main theorem is near the front and every promised proof appears in
the body. No page quota or decorative figure was imposed. The support
comparison table serves the coefficient partition. The bibliography
preserves Bridy's actual journal year, the exact BCH preprint version,
the Stacks tag, and C404's non-journal internal status. C405 is not an
actual dependency and was not inserted merely because its identifier
appeared in the outline citation line; the coordinator was informed.

The `paper-write` skill influenced the claim/evidence mapping and
reverse-outline pass; `paper-compile` influenced the real log, PDF text,
font and visual checks. The frozen batch's anonymous mathematical-article
format overrides those skills' unrelated venue examples. This author
work and its checks are AI-assisted and are not human peer review.

## Exact delivered hashes (SHA256)

```text
1cf7305d705045cdc75bd75a62071b59f1e574edb8ed20fcaf7dee085cec9bab  main.tex
80d91ef1fd11269635dac0b85d6cd6d113871abc810b05e7ea7d7ae9bbcf7f48  math_commands.tex
1b11c0d81e2d565c6aa138c5cfa0a630f5b6c0ad3287ed29b92a91cedbd75e3b  sections/0_abstract.tex
9aaccd5d1165dbb1c8ed20093e8b1663108be3425fc1faa05cba87ea9c049e3c  sections/1_introduction.tex
1125e37e77b09ee34c54aedc67650d4efa3b5fa208fd4893762f196f473c910c  sections/2_setup.tex
40960a62f0414eeaa7b4e6c4b13bc305bd906c946530a00b3fac1e36ebcdc28c  sections/3_count_conversion.tex
29e3e70d2f1de3c3d2d23932bc315e24cbcdae5974134c5e8ca97e0f6c8dc0b3  sections/4_high_support.tex
a9127aa1b0dac92a7f2c9a70890be3aaaea1bfefa40749de4ab14625a4a84b30  sections/5_perfected_ring.tex
1df90c48ab6fa12a504693d7684ed8de37b21ed4399d82d2326ea7443a4aa512  sections/6_low_support.tex
6d8ad6bfa6772e101f56b671d7c8c40910a513f7157cad435a2567382e7b6457  sections/7_zeta.tex
7154680b0fca627a029a6a5e98b612244491d3bc99d16059bf2bff8f8f695f5c  sections/8_scope.tex
9f1c7948fef2a4ac6e8483267a356447915c731c9c25cba2b6d4eee6238dccca  references.bib
6c4fb0aad2a660ea95f43ec8d1b658f01ac9c11e19e6b743bc8fe6c7db8aeb51  CITATION_AUDIT.md
05a1218006fec9142d7a1387dce44c53cb17ee4976fb99f3bd3d235070a3ea1f  main.pdf
05a1218006fec9142d7a1387dce44c53cb17ee4976fb99f3bd3d235070a3ea1f  build_author/main.pdf
5fed3aafb6d3b0ec67c5c7c6e925e415f457de7e211a70f9f5a1d8d5e2065fbd  build_author/main.log
15ef78ef320736474c3a8b7779ad4bec38d7232b4eb019015237dc3cdd74f2c2  build_author/main.blg
```

Only `papers/C415_degree_2p/` was written during authorship. The frozen
research tree, other paper sources, evaluations, global state, numbering,
and Git were not modified. Next gate: independent internal review of the
actual manuscript, then coordinator-owned affected fixes and final fresh
builds. No sixth paper or Route B work is authorized by this handoff.

## R1 affected revision after nonauthor manuscript review

The coordinator's actual-manuscript review found the mathematics and
completeness to pass and requested one local precision change in the
last paragraph of `sections/8_scope.tex`. The phrase describing the
perfected ring as a “finite algebraic device” could incorrectly suggest
that the ring itself is finite or finitely generated. Its definition as
an infinite union was already correct in Section 5.

Only that final paragraph was changed. It now reads:

> The result therefore consists of one full coefficient-family
> classification and its native analytic consequence. The calculation
> in the perfected ring uses only finite algebraic expressions, with
> each iterate lying at a finite denominator level. Its descent
> returns the calculation to ordinary polynomials and ordinary points.

All theorem statements, equations, proofs and other source files remain
unchanged. The historical hashes and checks above describe the original
author handoff and have intentionally not been rewritten.

One further affected author invocation (the fourth author invocation
overall) of the same `latexmk -pdf -interaction=nonstopmode -halt-on-error
-file-line-error -outdir=build_author main.tex` command exited 0. The
log selected only the changed section as an input trigger and produced
11 pages, 388,061 bytes. The final LaTeX/BibTeX diagnostic search again
had no matches for Warning, Overfull, Underfull, undefined, multiply
defined, LaTeX Error or Fatal error (rg exit 1 is the no-match status).

The affected last page was extracted with
`pdftotext -f 11 -l 11 -layout build_author/main.pdf -`, read, and
rendered with `pdftoppm -scale-to 1200 -f 11 -l 11 -png
build_author/main.pdf build_author/r1page`. The reviewer-requested
sentence appears correctly, and the author visually checked that page.
The current PDF was copied to `main.pdf`, and the cached complete text
was regenerated. No mathematical script or full proof rerun occurred.

Current affected SHA256 values:

```text
fd8333304100cfb07c594bb6e5974ae98ea0537857e8410dd18f000a6d0b0e21  sections/8_scope.tex
f99a764cef94525d88acb427e9d89040a6ab2ba98c2c3b7ce7f72f79e94f20cf  main.pdf
f99a764cef94525d88acb427e9d89040a6ab2ba98c2c3b7ce7f72f79e94f20cf  build_author/main.pdf
d88bb777bfee1fe1c6ba93f6ef33dd5d57b00ddff9044b3386eda3191bcf554a  build_author/main.log
15ef78ef320736474c3a8b7779ad4bec38d7232b4eb019015237dc3cdd74f2c2  build_author/main.blg
```

The nonauthor reviewer owns the final R1 closure. The coordinator also
confirmed that C405 is unrelated and amended the tentative citation line
as a source-only clarification, without changing the admitted contract.
Final fresh double builds and release sealing remain coordinator gates.
