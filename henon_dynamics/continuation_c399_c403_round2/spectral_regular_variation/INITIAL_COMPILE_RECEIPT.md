# C403 initial manuscript compilation receipt

Date: 2026-09-05. Outcome: `INITIAL_COMPILE_PASS`; complete 11-page
mathematical manuscript produced, with the final author-side TeX/Bib input
set frozen for non-author review. This is not the coordinator's final
two-fresh-directory deterministic-build or all-page visual gate.

## Delivered files and exact current state

- `PAPER_PLAN.md`: exact contract, proof dependencies, ownership, and writing scope.
- `paper/main.tex`, `paper/math_commands.tex`, and nine modular section files:
  complete mathematical manuscript; no placeholder proofs or new experiments.
- `paper/references.bib`: all four cited entries.
- `paper/BIBLIOGRAPHY_CHECK.md`: verified metadata, consulted passages,
  version qualifications, and explicit access limits.
- `paper/CITATION_AND_CLAIM_MAP.md`: all eleven actual citation contexts,
  all bibliography entries, and theorem/claim/proof navigation.
- `paper/SOURCE_SHA256SUMS.txt`: the twelve actual TeX/Bib compilation inputs.
- `paper/main.pdf`: 11 pages, 350553 bytes, PDF 1.5, A4.
- `paper/build_initial/`: actual final compiler log, BibTeX log, generated
  bibliography and cross-reference files, and extracted PDF text.

The standing assumptions include positive measurable slow variation and
both local upper and lower bounds. The body preserves the exact all-real-q
threshold, the q<1 argument, the positive congruence, the N-independent tail
bound, and the distinction between absolute and relative eigenvalue error.
Classical LCM eigenvalue asymptotics and their source ownership remain
explicitly external mathematical inputs.

## Actual build environment and commands

Working directory:

```text
/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/continuation_c399_c403_round2/spectral_regular_variation/paper
```

Tool versions actually queried:

- Latexmk 4.76, 20 November 2021.
- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian.
- BibTeX 0.99d, TeX Live 2022/dev/Debian.

The command `date -u -d '2026-09-05 00:00:00' +%s` returned
`1788566400`. The fresh initial directory was allocated by:

```sh
mktemp -d /tmp/c403-initial.XXXXXX
```

Actual returned directory: `/tmp/c403-initial.7sYfLV`.
The compilation command was:

```sh
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/c403-initial.7sYfLV main.tex
```

Actual execution sequence:

1. First invocation in the fresh directory: exit 0 after the necessary
   LaTeX/BibTeX/rerun cycle; 11 pages. Ordinary first-pass unresolved
   cross-references were resolved by latexmk. The completed initial log
   retained table underfull-box warnings and a math-token bookmark warning.
2. The table was changed to ragged-right cells and the N-containing bookmark
   was given a plain-text PDF-string alternative. Same command, same initial
   directory, exit 0; the final log had none of those warnings.
3. Coordinator reading found a literal `^{,q}` typo in the ideal-convergence
   display. It was changed to `^q`; the full TeX scan found only that one
   occurrence before correction and none afterward. Same command, same
   initial directory, exit 0; final output 11 pages, 350553 bytes.

The last two invocations were incremental corrections in the initial
directory. They are not represented as independent fresh builds or a
determinism test. No mathematical calculation or source experiment was
rerun during this process.

The TeX fixes `\date{5 September 2026}` and, when available, uses
`\pdfinfoomitdate=1`, `\pdftrailerid{}`, and
`\pdfsuppressptexinfo=15`. The PDF has no creation/modification date in
the inspected `pdfinfo` output. These settings prepare reproducibility;
the final byte-comparison gate remains with the coordinator.

## Actual initial verification

Commands successfully run on the actual generated output include:

```sh
pdfinfo /tmp/c403-initial.7sYfLV/main.pdf
pdffonts /tmp/c403-initial.7sYfLV/main.pdf
pdftotext -layout /tmp/c403-initial.7sYfLV/main.pdf /tmp/c403-initial.7sYfLV/main.txt
rg -n 'Warning|Overfull|Underfull|undefined|^!' /tmp/c403-initial.7sYfLV/main.log /tmp/c403-initial.7sYfLV/main.blg
rg -n -F '^{,' . -g '*.tex'
sha256sum -c SOURCE_SHA256SUMS.txt
```

The two final `rg` checks returned exit 1 with no matches: this is the
expected no-match result, not a compiler failure. The hash check returned
exit 0 with all twelve listed inputs `OK`.

`pdfinfo` reports 11 unencrypted A4 pages, no JavaScript, no form, and PDF
version 1.5. `pdffonts` lists 21 font resources: all Type 1, embedded,
subsetted, and carrying Unicode maps; no Type 3 fonts or unembedded fonts
were present. Text extraction exited 0 and produced 4681 whitespace-delimited
tokens under `wc -w`; this count includes mathematical extraction artifacts
and is not represented as a prose word count. The title, main theorem,
cross-references, bibliography, and relevant mathematical statements were
checked in the extracted text.

Initial representative-page renders were made at 110 dpi with `pdftoppm`:
printed pages 1, 2, 8, and 11 were visually inspected for title/abstract,
the theorem and source-comparison table, the full ideal proof, and the
declarations/bibliography. All were legible with no clipping or overlaps.
After the one-character exponent correction, printed page 8 was rendered
again from the final PDF and visually checked. The other three inspected
pages were not changed by that correction. This is a representative initial
check, not an assertion that the final all-page visual inspection has run.

Generated PDF/log/BibTeX/auxiliary files were copied from the actual build
directory; no compiler output or numerical evidence was fabricated.

## Frozen hashes

The twelve individual compilation-input hashes are in
`paper/SOURCE_SHA256SUMS.txt`. The ledger itself has SHA-256:

```text
46dc6bb27d5f7f66bc2d517893fefb1df472a57d64960fa1aba3ea63dc50e9dd
```

Other delivered hashes at this freeze:

| File | SHA-256 |
|---|---|
| `paper/main.pdf` | `83ed1a84dffe7696596b31d3752c620e472a959afae4aed8faaee044379501fd` |
| `PAPER_PLAN.md` | `f688f8cbc50e97d79341d7a5379f6a79cc4c50e373a491f378130b668fcff039` |
| `paper/BIBLIOGRAPHY_CHECK.md` | `3d385e04e5de77050ca3d5ddf63cb7e30e8d9c117f7822aaf5e077365f83e4c7` |
| `paper/CITATION_AND_CLAIM_MAP.md` | `eedd652c2de1a0a463e232d664dc9e28e0a4bc385179240671808a02003027b0` |
| `paper/build_initial/main.log` | `c64eeb919c88d2050b81db3683ee172b825cdee93e6ae3b4a93b8b575e180917` |
| `paper/build_initial/main.blg` | `0654f7cf49d8e91529c49f5f482a5fe3ebf625ab099390ea528b07957fe893f4` |
| `paper/build_initial/main.bbl` | `d302adcea933eaee608f5c01a0f3c1059e2eb449646b646192b6cea095dfa780` |
| `paper/build_initial/main.aux` | `d5e482bb15c10e281a3d55c5d6799f7afad8a26dc2a4fdebdbcd10808a33099f` |
| `paper/build_initial/main.txt` | `f1b95b8ba6d4b4602680e790f3a5e196cce5bc90b6325101ac03954211365657` |

The frozen upstream proof, contract, source audit, independent proof review,
and batch plan were rehashed after writing; all matched the values in
`PAPER_PLAN.md`. No upstream file was changed. No shared index, formal
evaluation, CURRENT file, or Git state was mutated by this author.

## Handoff and remaining gates

Author-side implementation is complete. The coordinator has assigned the
C401 author, a different agent, to the independent full-manuscript check.
The eleven-context citation map is supplied for a 100% internal citation
check; it is not itself that completed review. The original proof review
does not automatically certify the new TeX text.

The coordinator retains the final two-empty-directory deterministic builds,
byte comparison, final logs/fonts/text checks, all-page visual QA, shared
evaluation/index/manifest work, and Git operations. Any real review finding
must be corrected and checked on the affected input version.

The `paper-plan` → `paper-write` → `paper-compile` skills structured the
complete claim-driven exposition and actual compilation. ARS fidelity and
completeness guidance influenced source attribution and truthful draft
declarations. No journal-specific criteria were supplied
(`NOT_CALIBRATED`, `criteria_binding_unavailable`); no full external
research pipeline, external expert peer review, author attestation, or
journal submission is claimed.
