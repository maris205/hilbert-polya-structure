# C405 initial compilation receipt

2026-09-06. Status: **initial manuscript compiled; independent manuscript
review and final release builds pending**. This receipt does not claim a
final deterministic double build or submission readiness.

## Scope and frozen inputs

The assigned write area was arithmetic_forms/paper/ only. The accepted
plan, proof, source audit, finite evidence and previous independent review
were read in full; none was modified. The final read-only hashes still are:

| Frozen input | SHA-256 |
|---|---|
| ../PROOF_PACKAGE.md | eacbacec1c5a37506a32563b7c774f634557825bde9dde130368b39e6a78ac14 |
| ../SOURCE_AUDIT.md | a861bbeba6e14775123276d6b9eade326b32520f3d6b3da54b4aadb82b998cf7 |
| ../BOUNDED_RECEIPTS.md | b6de665b9c36d0bdd185fb4e2136a246df0ab45e5ab9c711f69a54502f2c9bc3 |
| ../PAPER_PLAN.md | cb9777a133210be7c920f594af59c8d8b9cd6115991009dae2f5466f808ee764 |

The paper-write and paper-compile skills, their required writing-principles
and venue-checklist references, and the repository batch workflow were
read. The explicit pure-mathematics contract superseded ML page quotas,
experimental sections and mandatory old external-model review. All complete
proofs are in the PDF, and the manuscript uses plain article with an anonymous
author block. No prior paper directory existed, so no backup or cleanup was
needed. All source edits used apply_patch. One initial patch orchestration
call failed before execution because of quoting; the subsequent split
patches created the source files. That was not a TeX compile failure.

## Environment and actual commands

Working directory for the following commands:

```text
/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/continuation_c404_c408_round2/arithmetic_forms/paper
```

Available tools: /usr/bin/pdflatex, latexmk, bibtex, pdfinfo, pdftotext,
pdffonts and pdftoppm. Versions observed:

- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
- LaTeX2e 2021-11-15 patch level 1;
- latexmk 4.76, 20 November 2021;
- BibTeX 0.99d.

First command, with its unedited combined output in initial_compile.log:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee initial_compile.log
```

The pipeline returned 0 and the log ends with all targets up to date.
This first pipeline did not enable pipefail, so its shell status alone is
not presented as an independently captured latexmk exit status. The log
records four successful pdfLaTeX passes and three BibTeX passes, ending at
11 pages and 355280 bytes. Normal first-pass undefined-reference/citation
and rerun messages resolved automatically. One real layout warning remained:
an overfull hbox of 3.87007 pt in the reproducibility paragraph, caused by
the unbreakable script filename.

The paragraph was rephrased, bibliography type was set to the conventional
small size so the last reference did not occupy a page alone, and the
logarithmic example's nonmultiplicativity sentence was made explicit using
the elementary 2,3,6 comparison. No main theorem was changed.

Second command, with unedited output in initial_compile_fix.log:

```sh
set -o pipefail
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee initial_compile_fix.log
```

This command exited 0 with pipefail enabled. The log records two successful
pdfLaTeX passes and one BibTeX pass, then all targets up to date. It produces
the stable initial PDF identified below. No source or PDF changes were made
after this build; only this receipt and the bibliography/claim record were
added.

## Result and checks

- PDF: main.pdf, **10 pages, 355317 bytes**, A4, PDF 1.5.
- All proofs are in the main body; there is no appendix. The conclusion
  ends on page 10 and all six references also fit on page 10.
- Final main.log and main.blg: no warnings, overfull boxes, underfull boxes,
  undefined references, undefined citations or TeX errors. The command
  `rg -n 'Warning|Overfull|Underfull|undefined|^!' main.log main.blg`
  exited 1 with no matches, as expected for a clean scan.
- PDF text scan for `??`, `[?]` and `[VERIFY]`: no matches.
- Source scan for TODO/FIXME/XXX/verification placeholders and inflated
  stock claims: no matches.
- pdffonts reported 19 font entries, all embedded, subset and Unicode-mapped.
- All eight section files are referenced by main.tex; bibliography keys
  match the six distinct cited works. The citation/claim record includes
  exact access scopes and the preparer's reverse-outline check.
- Initial visual spot check: pages 1, 8 and 10 were rendered with
  pdftoppm at a 1600-pixel maximum dimension and actually inspected. Title,
  abstract, maximal-domain proof, equations and bibliography were legible,
  with no clipping or overlap observed on those pages. These three pages
  are not an all-page final QA claim. Temporary renders are under
  /tmp/c405-initial-preview.Ibhp0P/ and are not manuscript payloads.

No numerical evidence was rerun. No final double build, manifest, C-series
evaluation, Git mutation or global index modification was performed by
this writer. Git status/diff checks were read-only.

## Initial artifact bindings

| Artifact | SHA-256 |
|---|---|
| main.pdf | 9b6801db5237ef523fded18797ec7508a06762bd79fd1c32f0074ddbfa9290c3 |
| main.tex | 53a73373cf85ecc654fe7a1ee1a0dd129400db45f1c3bf2c7c6faff643cb967e |
| math_commands.tex | f6da7cc997c448634577ec39b6a2ffd54aae4cd3f99746ddf896b670a0d5e29a |
| references.bib | b974b2e2f28020263b1b06c34c4ff6bf7321218215d7dcb77ee32e41933755b7 |
| sections/0_abstract.tex | 3fb7e9b05f2eab62329fea7a9129ceb46434ef2d661a9f306c42e2023d873a39 |
| sections/1_introduction.tex | 52e407fd196c74277d0854a1374deae95fa532ca6687214b5bf072fb8804a1ba |
| sections/2_product_forms.tex | 7066bf7a990be52c23b15a084007c40f7de5c3be48c36ca7ea810a9bea367354 |
| sections/3_variational.tex | 00afb318f3dc3c954d4684951aa267e7368003f9395c91e00fd2751dbde16ab5 |
| sections/4_critical.tex | 4ed718e09f38bbbe6f13df2f703a7b8fc51e5e8114e67d802ca14a07435931e0 |
| sections/5_summable.tex | c2ef5d4e0c7df624dc02d7f02e9848b63a4af4ff18fb66ff644bcb6f84a4e725 |
| sections/6_examples.tex | 9148d7e3a328a1745a24e45f832a5af152ef54b712f9d4b62234c5acc496c15b |
| sections/7_conclusion.tex | 5f865ee21522f56726705f0143e67c8ae308b56a19900aeac4a9d290c4bdae8c |

The exact command

```sh
sha256sum main.tex math_commands.tex references.bib sections/*.tex | sha256sum
```

returned `94360d34b9ee40525e9a20a95713a737d6b3d29968c93d769d5ee4dd252e66a1`.
This binds the ordered source-hash listing, not a tar archive or a single
flattened TeX file. Byte integrity does not establish correctness or novelty.

## Handoff

The coordinator is to arrange a genuinely different agent's review of this
actual text, then any affected correction and final deterministic builds
in two fresh directories with full final-page QA. This initial writing task
stops at this handoff. No mathematical or citation blocker was identified
by the preparer, but the independent manuscript-review gate remains open.
