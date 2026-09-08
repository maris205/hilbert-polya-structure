# C421 baseline manuscript and compilation receipt

2026-09-08 UTC. Author-stage handoff only: **BASELINE_READY_FOR_NONAUTHOR_REVIEW**.
The admitted mathematical contract is unchanged. This report does not
claim completion of either new manuscript review round, final deterministic
release builds, formal evaluation, sealing, Git integration or submission.

## Frozen baseline

- Title: *Integral periodic orbits of a cubic three-term recurrence*.
- [Review baseline PDF](main_round0_original.pdf): **18 pages, 473,416 bytes**.
- SHA-256: `7fcfe7c00da4590cc44565d2343a5d3e37f233c5ece4798971891e9f145b5e1d`.
- [Current PDF](main.pdf) and [build output](build_baseline/main.pdf) are
  byte-identical to that review baseline at this handoff.
- Main body: pages 1–13; references: page 14; typeset appendix: pages 15–18.
- Format: anonymous English 11pt `article`, letter paper, one-inch margins.
  No journal/conference is selected and no artificial page limit applies.
- [Frozen source snapshot](baseline_source/main.tex) and
  [source hashes](BASELINE_SOURCE_SHA256SUMS.txt) identify all 17 TeX/Bib
  production files, including the table-include index. The listing's
  separately preserved primary Python source retains its historical hash.

The baseline includes eight substantive sections, an abstract, three
standalone exact tables, six verified bibliography entries and the entire
139-line primary certifier as a typeset listing. The complete independent
finite algorithm is specified in the main text, including both signs,
zero-coefficient interval cases, inverse stopping, forward reconstruction,
family proposal rules and full directed-state-set comparison.

## Claim-to-page transcription check

| Required content | Actual location |
| --- | --- |
| Exact map, inverse, invariant, native scalar/triple clock | §§1–2, pages 1–3 |
| All ten family/exception rows, guards and levels | Table 2, page 3 |
| Parameter-free difference identity and high-coordinate F4 channel | §3, page 4 |
| All five extremal centers, signed normalization and every exclusion | §4, pages 4–7 |
| Residual `1 <= D <= 100`, `-3D-1 <= x_i <= 3D-1` | Corollary 4.2, page 7 |
| Forward certificate, exact seed ranges, exit-or-return stopping proof | §5.1, pages 7–8 |
| Independent inverse two-sign construction and complete comparison | §5.2, pages 8–9 |
| Exact historical seed partition and both sporadic words | §5.3, pages 9–10 |
| All least-period degeneracies and oriented cyclic identifications | §6, pages 10–11 |
| Nine exact level-count tests with derivations | Proposition 7.1 and proof, pages 11–12 |
| Native fixed counts, finite level zeta, no all-level finite-count claim | Corollary 7.2 and following paragraph, page 12 |
| Scope, integer/singular-point convention, no target arithmetic, AI disclosure | §8, page 13 |
| Assertion caveat, evidence provenance/hashes and complete primary listing | Appendix A, pages 15–18 |

## Skills and outline gate

The complete batch outline had a real independent review and coordinator
approval before this author drafted TeX. This is not a claim that the
per-paper plan received an additional review. The `paper-writing` phases
were followed in scope through planning, substantive table preparation,
section-by-section writing and real compilation. `paper-plan`,
`paper-figure`, `paper-write`, `paper-compile`, `paper-writing` and the
required writing/citation references were read in full. Under the batch
override, current-team internal review replaces legacy model/MCP examples;
no model switch, paid external review, upload or fabricated experiment
was performed. The two improvement rounds remain separate, future gates.

The figure phase produced exact LaTeX tables from accepted theorem and
execution data. No plot or image was needed. It did not perform a new
parameter scan. The signed proof is in the main body instead of being
relegated to a local Markdown link. The primary source listing is read
directly from the preserved supplement during compilation.

## Actual compilation attempts

Prerequisites were present: `/usr/bin/pdflatex`, `/usr/bin/latexmk`,
`/usr/bin/bibtex`, `/usr/bin/pdftotext`, `/usr/bin/pdfinfo`,
`/usr/bin/pdffonts`, `/usr/bin/pdftoppm`, and the `lmodern` package.
No package installation or old build cleanup was needed.

Each attempt used the following command from this package directory,
with pipe failure propagation enabled:

```bash
bash -o pipefail -c 'env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build_baseline main.tex 2>&1 | tee build_baseline/compile_console.log'
```

The build directory was newly created for this manuscript. The epoch is
8 September 2026 00:00:00 UTC. Recorded software: latexmk 4.76;
pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
BibTeX 0.99d. These settings were recorded, but this single baseline
build is **not** represented as a completed two-directory byte-reproducibility
test. That final release gate remains coordinator-owned.

| Attempt | Actual exit | Result and scoped repair |
| --- | ---: | --- |
| 1 | 12 from latexmk, following pdflatex exit 1 | No PDF. The unchanged Python comment's UTF-8 `§` was unsupported by `listings`. Added a LaTeX-only literate mapping; the Python bytes were not edited. Also allowed a long appendix path to break and made the ownership table's first column ragged-right. |
| 2 | 0 | First complete real 18-page PDF produced. One 30.16414pt text-line overfull and eight math-heading PDF-string warnings remained. Preserved this actual PDF as `main_first_success.pdf`; rewrote the long scalar-word sentence and supplied text alternatives for four math headings. |
| 3 | 0 | Clean review baseline: 18 pages, no warnings or over/underfull boxes in the final TeX log. No mathematical statement or historical code changed in these formatting repairs. |

All three actual console and terminal TeX logs are preserved as
`build_baseline/compile_attempt{1,2,3}_{console,tex}.log`.
The final files are also available as
[compile console](build_baseline/compile_console.log) and
[TeX log](build_baseline/main.log). Intermediate unresolved references
in earlier latexmk passes are retained in their console logs; they were
resolved by the normal bibliography/cross-reference passes and are not
suppressed.

The [first successful PDF](main_first_success.pdf) is 473,408 bytes,
SHA-256 `0a9ae2aa7e1e9dc454ffd084559fcb0e8b066df557eda82c5e0e32b62c9811b4`.
It is a pre-cleanup build artifact, not an invented review-round PDF.

## New manuscript checks actually performed

- Complete [PDF text](build_baseline/main.txt), 863 lines, read from
  beginning through the final listing line. Text SHA-256:
  `6afe19910ece781d972d0322f0e0989d2c24bae45645fe9bc5f614abfcde8475`.
- Final TeX log: zero `Warning:`, `Overfull`, `Underfull` or `Error`
  matches; `rg` returned 1 because there were no matches.
- PDF text: zero `??`, `[?]`, `VERIFY`, `TODO`, `PLACEHOLDER` or tested
  generic-hype markers; `rg` returned 1 because there were no matches.
- All six bibliography keys are cited; the final BibTeX/LaTeX run has
  no undefined citation/reference or duplicate-label warning.
- All ten section files, three table files, math macros and source
  listing are reached by `main.tex` or its included sections. The
  `figures/latex_includes.tex` file is a deliberate include index,
  not an extra table set included a second time.
- `pdffonts` reports all 24 font records embedded, subsetted and
  Unicode-mapped. `pdfinfo` confirms 18 nonencrypted letter-size pages
  and a nonempty 473,416-byte PDF.
- **All 18 pages visually inspected** from generated page PNGs under
  `build_baseline/visual/`. Theorem table, signed formulas, interval
  conditions, counts, references, hashes and all 139 code lines are
  present without clipping or overlap. A higher-resolution page-6
  render confirmed the complete signed-normalization heading and formulas.
- Frozen production source snapshot: all 17 files compared bytewise
  with the baseline source tree; comparison command exit 0.
- The saved source hash list was checked with `sha256sum -c`: all
  17 entries passed. A read-only local Markdown target scan covered
  58 links across the package's notes and copied evidence: zero missing
  targets, exit 0. External URLs were not re-fetched by this local check.

These are author-stage production checks. They do not count as either
required nonauthor full-manuscript review, do not assign a publication
score, and do not certify formal target arithmetic.

## Preserved mathematical evidence

All 16 initially copied evidence files passed a bytewise `cmp` against
the original accepted proof-stage tree. A subsequent navigation check
found two repository-context links in the copied coordinator source audit
that needed deeper relative paths. Only those two link destinations were
rebased, with the difference explicitly checked. The other 15 files,
including every proof, certifier, raw cycle output, execution summary and
proof-review report, still pass exact comparison. The original source
audit and every other old source file remain untouched. The rebased
source audit has the same scientific and attribution text, and both
new destinations exist.

The six historical hashes listed in Appendix A were independently read
from the copied files with `sha256sum` and exactly match the accepted
identifiers in [EVIDENCE_PREPARATION.md](EVIDENCE_PREPARATION.md).
Both raw JSONL outputs are complete. Their 25,851 mathematical records
were not re-enumerated or semantically rechecked in this writing turn;
the full independent semantic comparison remains the accepted historical
execution documented in the supplement.

The [supplement instructions](supplement/README.md) explain its directory
layout and safe scratch-copy reproduction. Historical draft/candidate
headers remain historical bytes, not current admission judgments.
No old mathematical test was rerun merely to generate a new PASS.

## Pending handoff gates

1. A nonauthor reads the complete actual baseline TeX/Bib/PDF text and
   compares its transcription with the accepted proof; retain the full
   first-round review and implement any real corrections in a new version.
2. A second actual review/revision/recompile pass; preserve true resulting
   PDFs without inventing a change or increasing score for a clean review.
3. Coordinator-controlled formal evaluation and final two-fresh-directory
   builds, byte comparison, final-page visual checks, payload ledger,
   manifest, failure-path release-checker tests and read-only sealing check.

Only this allocated C421 package was written. No global status, old
frozen package, evaluator, Git index, commit, remote, external service
or journal-submission state was changed.
