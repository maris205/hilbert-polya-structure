# C424 actual initial-build history

2026-09-09 UTC. This records real author typesetting, not either of the
two required nonauthor manuscript review/revision rounds and not final
deterministic release verification.

Environment: pdfTeX1.40.22 (TeX Live2022/dev/Debian), LaTeX2e2021-11-15,
latexmk4.76, BibTeX0.99d. The logs retain full exact version strings.
Both builds used `SOURCE_DATE_EPOCH=1788912000`, `FORCE_SOURCE_DATE=1`,
`TZ=UTC`, `LC_ALL=C`, with PDF creation dates, trailer ID and pTeX
source metadata suppressed by the document preamble.

| Actual build | Invocation | Outcome and retained evidence |
| --- | --- | --- |
| First compiled baseline | `bash scripts/build.sh build/round0` | Exit0; 3 pdfLaTeX passes, 2 BibTeX passes; 21pages,463406bytes. All references/citations resolved at convergence. One final10.79245pt overfull horizontal box in AppendixB prose. Full log/PDF/info/fonts/text/hash retained in `build/round0/`; exact prebuild source snapshot and resulting PDF/log copies in `baseline/round0/`. |
| Local layout repair | `bash scripts/build.sh build/round0_layout1` | Exit0; 3 pdfLaTeX passes,2 BibTeX passes; 21pages,463423bytes. No final Warning/Error/Overfull/Underfull messages. Only manuscript change: the long code predicate in AppendixB was put in display form. All math statements, cycle tables and evidence files unchanged. Complete logs/diagnostics in `build/round0_layout1/`. |

There were **zero failed compilation attempts**. Initial-pass undefined
cross-references, citations and changing longtable widths were ordinary
multipass convergence messages; they are preserved in the console logs,
not relabeled as final errors or erased. The first baseline's real
nonfatal overflow is explicitly retained.

First baseline PDF SHA-256:
`95857f7d412d72830ca309733c99519cdb21bb48a53702a3c58ced490989f52d`.

Current initial-draft PDF SHA-256:
`3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b`.

The current PDF has22 font entries, all Type1, embedded, subset and with
Unicode mappings. Its Author metadata is blank; the visible title page
says Anonymous Authors. No PDF JavaScript, encryption, form, or external
manuscript upload is present.

Author preflight read the complete1107-line extracted PDF text and viewed
all21 individually rendered pages at1250-pixel long-edge resolution.
Cover/theorems, all five tables, displayed formulas, multi-page code,
continuation headers and bibliography are readable with no observed
clipping or collision. Renderings are in `build/round0_layout1/pages/`.
This is initial author preflight, not a substitute for the coordinator's
post-review final all-page audit.

No map, graph or mathematical certificate was executed during either build.
Only the format-only receipt renderer read stored fields; the manuscript
directly typesets the pre-existing producer/checker files.

Two actual nonauthor manuscript review/revision passes, their adjudication,
and two fresh byte-compared final builds remain outstanding coordinator
gates. These two builds are of different source versions and are **not**
presented as the final identical-source deterministic build pair.
