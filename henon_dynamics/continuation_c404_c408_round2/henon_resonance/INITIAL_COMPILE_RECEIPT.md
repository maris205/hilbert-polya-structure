# C404 initial manuscript and compile receipt

Date: 2026-09-06. This is the author's initial compilation and limited
visual QA, not the coordinator's final two-fresh-build release receipt.
The manuscript is [paper/main.pdf](paper/main.pdf), with entry point
[paper/main.tex](paper/main.tex). It contains the abstract, seven body
sections, complete proofs, one bounded exact-check table, and four
actually cited bibliography entries. There is no proof-only appendix.

## Actual build

The source directory did not contain an earlier manuscript. A fresh
temporary directory was created with mktemp using the pattern
/tmp/c404-initial.XXXXXX, returning /tmp/c404-initial.nDqXIn;
the new TeX tree was copied there. From that directory, each attempt used:

~~~sh
set -o pipefail
SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex \
  2>&1 | tee attempt-N.stdout.log
~~~

The actual filenames substituted 1 and 2 for N. The source uses fixed
manuscript date text and omits PDF creation/modification dates and the
generated trailer identifier.

Attempt 1 exited **12**: two align rows in the degree recurrence had
single backslashes instead of TeX line breaks, causing the amsmath
“Multiple \label's” error. No PDF was produced. The two line endings
were corrected; no formula, hypothesis, or theorem was changed.
Attempt 2 exited **0** after the normal BibTeX and cross-reference
passes, producing **10 pages, 373654 bytes**. Intermediate first-pass
unresolved references cleared normally; the final TeX and BibTeX logs
have no warning or unresolved-reference entries.

The produced PDF was copied back to paper/main.pdf. Its SHA-256 is:

~~~text
99c58e5805bb4e5b70e5f86505dc60dd8f79df76ea0011ac901127456e10a3cc
~~~

## Actual checks and retained artifacts

- The final main.log and main.blg were scanned for Warning, Overfull,
  Underfull, undefined, Error, and Missing character. There were zero
  matches; rg therefore returned its normal no-match exit code 1.
- pdfinfo reports ten A4 pages, PDF 1.5, no encryption, and the
  anonymous author metadata.
- pdffonts lists 24 font rows, all embedded and all Type 1.
- pdftotext -layout succeeded. A source scan found all four bibliography
  keys cited, no missing citation key, no uncited bibliography entry,
  no missing label, and no duplicate label.
- Raster previews of actual PDF pages **1, 7, and 10** were opened and
  inspected: the opening theorem context, analytic equations, final
  disclosures, and bibliography were legible without clipping or
  overlapping text. This is explicitly not an all-page visual check.
- The scoped git diff --check returned zero. No Git index or
  registry/evaluation/CURRENT state was changed by this work.

paper/initial_build/ retains both attempt stdout logs, the failed
attempt's TeX log, the successful final main.log, main.blg, main.fls,
main.bbl, main.aux, extracted main.txt, pdfinfo.txt, and pdffonts.txt.
RUNTIME_INPUTS.sha256 lists the existing files named by the final TeX
recorder, with ./ normalized; it is not a claim that the recorder
inventories every executable or operating-system input. The eleven
author-controlled TeX/BibTeX inputs are separately bound by
paper/SOURCE_INPUTS.sha256.

The engine was pdfTeX 3.141592653-2.6-1.40.22
(TeX Live 2022/dev/Debian); latexmk 4.76; BibTeX 0.99d.
The manuscript-level citation locations, metadata provenance, and
full-text access limitations are recorded in
[paper/SOURCE_VERIFICATION.md](paper/SOURCE_VERIFICATION.md).

## Frozen upstream evidence preserved

After writing and compiling, the upstream hashes remain exactly:

~~~text
0c59a129ba1dfbb3f22c527c40f4065cf8748cc570a302f0b3ba801a98289ea6  PROOF_PACKAGE.md
d5288bd5375cfd29d4d9219736cd91d17cc77dce62859a70a2ea9def9497f611  SOURCE_AUDIT.md
ccc71e0ac0409a7ae3df53233b3e06df743e98f58d6bc89df5bf58b0c58b72e1  exact_checks.py
5ec4a3e13fa0adfeb9868ad202edd92f65d3d13e8acca44b79495c89b893aa99  exact_results.json
9faaa817df30c4a87ccda58136a5aff2e41b5de912797ee33c3578c90cd0285b  CHECK_RECEIPT.md
~~~

No old exact census or sealed experiment was rerun during manuscript
preparation. The full-text counterexample expansion explains a frozen
example rather than claiming a new numerical run.

## Handoff and pending gates

The coordinator was notified that the actual TeX/BibTeX body and initial
PDF are ready for non-author claim, notation, citation, and reverse-outline
review. At this receipt's creation those reviews, final two-directory
deterministic compilation, all-page visual QA, actual Route-A evaluation,
and any release/registry actions remain the coordinator's separate gates.
Initial compilation success does not assert those gates have passed.

The scoped paper-writing, compilation, and ARS source-discipline skills
guided the modular full-proof layout, version-specific citations, bounded
claims, and explicit failure record. Pure-mathematics scope overrides old
ML-template quotas and prescribed external-model calls. No human peer
review or external-model certification is represented as performed.
