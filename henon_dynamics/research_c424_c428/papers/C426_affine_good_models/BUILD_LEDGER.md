# C426 initial manuscript build ledger

2026-09-09 UTC. These are initial drafting builds, not either of the
coordinator's two future fresh final-release builds and not manuscript
review rounds. All build commands ran locally; no mathematical program
or previously frozen certificate was executed.

## Fixed settings

Every compilation used `SOURCE_DATE_EPOCH=1788912000`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, `latexmk -pdf
-interaction=nonstopmode -halt-on-error -outdir=... main.tex`.
The preamble sets `pdfinfoomitdate=1`, an empty `pdftrailerid`, and
`pdfsuppressptexinfo=15`. Engine: pdfTeX 1.40.22, TeX Live 2022/dev/Debian;
latexmk 4.76; BibTeX 0.99d. Class: anonymous English 11pt article,
one-inch margins, letter paper. No venue-specific page cap applies.

## Actual compile attempts

| Attempt | Actual result | Persistent output and change |
| --- | --- | --- |
| `initial_01` | Exit 0; 10 pages, 343663 bytes; three pdfLaTeX passes and two BibTeX passes driven by latexmk. Final log has one 0.98972pt overfull hbox in the combined setup equation, with no unresolved references/citations. | `builds/initial_01/compile.log`, `main.log`, `main.pdf` and pre-fix `source.tar` retained. No failed compile. |
| `initial_02` | Exit 0; 10 pages, 343673 bytes; three pdfLaTeX passes and two BibTeX passes. Final `main.log` has no Warning, Overfull, Underfull or undefined matches. | The only source change moved the parameter hypotheses from the setup display to its preceding sentence. `builds/initial_02/` retains the full compilation transcript, final log, PDF, extracted text and all ten rendered page images. |

The cumulative transcripts intentionally retain expected undefined
reference/citation warnings from early passes, which latexmk resolved.
A diagnostic `rg` on the clean final log returned exit 1 because it had
no matches; that is not a compile failure. There were two successful
latexmk invocations, zero failed invocations, six engine passes and four
BibTeX passes in total. No unchanged mathematical certificates were rerun.

## Actual initial checks

- `pdfinfo`: 10 pages, 343673 bytes, 612 by 792 pt, unencrypted, no
  JavaScript, empty author, no CreationDate/ModDate reported.
- `pdffonts`: all 20 listed font resources embedded; all are Type 1,
  with no Type 3 resources.
- `pdftotext -layout`: extracted real text. No `??`, `[?]`, `VERIFY`,
  `TODO` or `FIXME` marker was found in text or manuscript sources.
- All ten `pdftoppm` page renderings were actually viewed. Table,
  formula breaks, page boundaries and bibliography show no clipping
  or collisions. Proof continuations across pages remain readable.
- Main body and scope statement end on page 10; references also begin
  on page 10. There is no appendix because every new proof is in the
  main body. No artificial page limit is imposed.

## Preserved hashes and baseline

First PDF SHA-256:
`26622000de85131a618542ca3eaa0acbc7f9189cdfd1dc1ba64deede792e0479`.

Clean first-manuscript PDF SHA-256:
`85677da439f31f1c2faea804430c8f395a2aaa235a0d20696e0a97a8ca08ed38`.

The clean `main.pdf` is a byte copy of `builds/initial_02/main.pdf`.
`builds/initial_01/source.tar` preserves the actual pre-layout-fix
source (SHA-256 `44969364d4bb3937add58f121613b1381f5930d2cfb565d269283407e1ea0c85`).
`builds/initial_02/source.tar` preserves the clean first-manuscript
source, bibliography, source audit and this ledger. Their existence
and hashes are checked at handoff. The baseline is not a fabricated
review revision: no manuscript reviewer has yet requested changes.

The author stops writing this paper at handoff. Two actual nonauthor
manuscript reviews, adjudicated revisions, formal evaluation and the
two fresh deterministic final builds remain for coordinator scheduling.

## Subsequent actual round-one revision

The preceding entries remain the historical first-manuscript record.
After the coordinator's actual first manuscript review, its three
minor corrections were implemented and one fresh build was run in
`builds/round1_revised/`: exit 0, three engine and two BibTeX passes,
10 pages, 343725 bytes, clean final log, all 20 fonts embedded.
All ten revised page images were actually viewed. Its PDF SHA-256 is
`d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db`.
The current `main.pdf` and `main_round1.pdf` are copies of that file;
`main_round0_original.pdf` retains the unchanged reviewed baseline.
See `PAPER_IMPROVEMENT_LOG.md` and `reviews/round1/source_changes.diff`
for the full evidence. Across the initial and round-one stages there
are three successful latexmk invocations, zero failed invocations,
nine engine and six BibTeX passes. Zero mathematical executions were
added. The final-build pair and round-two review are not complete.
