# C414–C418 final builds and every-page inspection

Status: **FIVE_FINAL_PDFS_VERIFIED**, 61 pages. Actual execution
and integration date: 7 September 2026 UTC. All five actual
manuscript gates were closed before these fresh builds. This
report records build/visual completion, not the later release seal.

## Final artifacts

| Paper | Pages | Bytes | Embedded Type 1 font rows | SHA256 of both final builds and delivered PDF |
|---|---:|---:|---:|---|
| [C414](papers/C414_height_distribution/main.pdf) | 9 | 355639 | 21 | `7c9502e4f76c5ba4fc7478e441e8a4b2e944bd4e1e9f211ac6e7a34be6ff7751` |
| [C415](papers/C415_degree_2p/main.pdf) | 11 | 388061 | 26 | `f99a764cef94525d88acb427e9d89040a6ab2ba98c2c3b7ce7f72f79e94f20cf` |
| [C416](papers/C416_discrete_sine/main.pdf) | 15 | 338853 | 20 | `31259d5c108bcf05b3fa1313a919d7559a9bdfbcd0f5deec56f5ba67e1167a55` |
| [C417](papers/C417_integral_cubic/main.pdf) | 17 | 392206 | 20 | `b0f62d97bea170e9b03cc42a7da1c7f5503ba09cadef906a5201993bafa39e5b` |
| [C418](papers/C418_function_field/main.pdf) | 9 | 341957 | 20 | `03ed775fb021192104288bdbac99cd2b5b044906c6dfcf63b51a2dc1f84bd525` |

All PDFs are unencrypted, version 1.5, with anonymous authorship.
C415 is A4 with approximately one-inch margins; the other four
are letter size. No journal/conference or venue page cap has been
selected. Counts are descriptive, not submission-format claims.

## Genuine clean builds and recorded extra stabilization

The coordinator delegated the mechanical final build and all-page
visual work to two current-team agents with disjoint paper paths:

- scout_henon_arithmetic: C414, C415 and C418, in fresh root
  `/tmp/c414-c415-c418-final.S4SZJP`;
- scout_nonlinear_return: C416 and C417, in fresh root
  `/tmp/c416-c417-final.56a6rZ`.

Each root was created by `mktemp -d`. Every paper had two
previously absent source/build directories, `<paper>/a` and
`<paper>/b`. Only its TeX/Bib inputs and included section files
were copied; no author PDF, auxiliary, generated bibliography or
cache was a build input. In each of ten directories the command was:

```bash
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

All ten invocations exited 0, with full consoles retained and
pipefail preserving the compiler status. Every a/b PDF pair
was byte-identical. C417 pass a nevertheless retained one
label-rerun warning in its last TeX log, while pass b and both
PDFs were stable. After explicit coordinator authorization,
one same-epoch `pdflatex -interaction=nonstopmode -halt-on-error
main.tex` invocation stabilized that pass-a log. It exited 0,
removed the warning and changed no PDF byte or source input.
The original warning log and both original/extra consoles are
preserved. It is not disguised as a third fresh build or as a
source repair. No cause for Latexmk's different stopping behavior
is claimed solely from the observed warning.

Actual environment: pdfTeX 3.141592653-2.6-1.40.22, TeX Live
2022/dev/Debian, Latexmk 4.76, BibTeX 0.99d and Poppler 22.02.0.
The frozen epoch denotes 6 September 2026 00:00 UTC; local
PDF-info display uses 08:00 CST. That metadata date is distinct
from execution/article dates. C415's already existing preamble
suppresses PDF dates/trailer metadata; no such setting or warning
suppression was added during final builds.

## Independent coordinator integration check

The coordinator read all five complete final receipts, then ran
one separate read-only integration check on the actual current
files and both temporary source/build copies. It exited 0:

- All **55** source inputs (50 TeX files, five bibliographies)
  match both source-only copies: **110** byte comparisons.
- All five delivered PDFs match both final build outputs, their
  stated byte lengths, page counts and SHA256 identities.
- The ten final TeX logs and seven retained bibliography logs
  contain no Warning, Overfull, Underfull, undefined, Missing
  character, multiply defined, LaTeX Error or Fatal error.
- Direct final PDF text extraction equals the retained final text
  and also equals direct extraction from the preserved author PDF
  for each paper. There are no unresolved-reference or placeholder
  matches. Metadata byte changes are not manuscript-text changes.
- Fresh font listings have 21/26/20/20/20 rows, all embedded
  subset Type 1 fonts with Unicode maps; no Type 3 fonts.

The 55 source identities are in
[FINAL_SOURCE_SHA256SUMS](FINAL_SOURCE_SHA256SUMS), SHA256
`98c25ebee2c1f38e85bd0d5416ad333cfbeee2124cb5732aeea3db2107d85a95`.
This check did not rebuild the papers or rerun mathematical proofs.
Historical author/review PDF hashes remain valid earlier snapshots;
the table above identifies the final deliverables.

## All 61 final pages actually viewed

Both delegated executors rendered the exact final bytes with
`pdftoppm -r 100 -png` in temporary locations and individually
displayed every page. The coordinator did not personally view
all 61 images; the complete per-page observations and actual
execution provenance are in these receipts, all read in full:

| Paper | Pages actually displayed | Complete receipt |
|---|---|---|
| C414 | 1–9 | [Final build/visual receipt](papers/C414_height_distribution/FINAL_BUILD_RECEIPT.md) |
| C415 | 1–11 | [Final build/visual receipt](papers/C415_degree_2p/FINAL_BUILD_RECEIPT.md) |
| C416 | 1–15 | [Final build/visual receipt](papers/C416_discrete_sine/FINAL_BUILD_RECEIPT.md) |
| C417 | 1–17 | [Final build/visual receipt](papers/C417_integral_cubic/FINAL_BUILD_RECEIPT.md) |
| C418 | 1–9 | [Final build/visual receipt](papers/C418_function_field/FINAL_BUILD_RECEIPT.md) |

No clipped equation, listing or table; overlapping text; missing
glyph; accidental blank page; unresolved reference; or detached
caption remains. Particular checks covered C414's combined poles
and floor asymptotic, C415's corrected finite-expression wording,
C416's full endpoint/core tables, C417's seven templates and three
certificate listings, and C418's atlas and fourteen-point table.
Final temporary images are inspection artifacts, not new scientific
figures or delivered dependencies. Retained author PNGs remain
historical artifacts and were not substituted for final renders.

## Completion boundary

The selected paper-compile and local batch workflow determined
fresh-build, log/font/text and all-page checks. Complete source
proofs and nonauthor review, not typography, support mathematical
claims. These checks do not certify worldwide novelty, human
peer review, target Euler factors, root numbers, a target divisor
or a Hilbert–Pólya realization. Formal evaluator consistency,
exact payload sealing and actual Git synchronization have their
own records. No sixth paper or external publication is authorized.

