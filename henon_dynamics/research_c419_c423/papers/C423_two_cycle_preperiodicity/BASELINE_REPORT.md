# C423 author baseline and source-transcription receipt

2026-09-08 UTC. Coordinator-authored manuscript under the approved
batch plan. First independent manuscript review is assigned separately;
no first/second review, final reproducibility pair or release is claimed.

## Actual products and builds

Ten production TeX/Bib files contain the whole nonexternal proof.
The six sections include the abstract; the single table is exact source
scope data. There is no mathematical program or new experiment.

| Version | Actual PDF | Pages / bytes | SHA-256 |
| --- | --- | --- | --- |
| First complete author baseline | builds/baseline/main.pdf | 6 / 317235 | 8bc2b3041dba090489bc03edca5b435a47c899bb25c887cad30a272ab46b1ffa |
| Author-polished review input | builds/author_polished/main.pdf | 6 / 317245 | b0aa1ace124faa50d14ff50873a5acaa70c5691c01772cd96cd74bd03626f408 |

The command was latexmk -pdf -interaction=nonstopmode -halt-on-error
-file-line-error -outdir=builds/baseline main.tex, then the same command
with outdir builds/author_polished after the three edits below.
Both commands exited 0. Each latexmk invocation performed three
pdflatex passes and two BibTeX passes. Early-pass undefined labels
resolved normally; both final main.log/main.blg pairs have no
Warning, Overfull, Underfull, undefined or leading error marker.
The read-only rg search exited 1 because it found no matches.

Environment: latexmk 4.76 (20 November 2021), pdfTeX
3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian; article 11pt,
Latin Modern, plainnat bibliography. Baseline compilation used the
inherited environment, including its CST timestamp; deterministic UTC
release settings will be recorded separately. The first PDF has 20
font rows, all Type 1, embedded/subset/Unicode. No final build-pair
identity is inferred from these different author inputs.

All ten first-baseline source files were copied byte-preservingly into
snapshots/baseline/ before any further edit. The three author corrections
were: define f explicitly in the abstract; order Lemma 4.1's words as
for every prime there exists a parameter; qualify the table's
strict-weight cases by the cited theorem regimes. No proof/table answer
changed. These are author polishing, not independent improvement rounds.

The author read the entire first PDF's extracted text and actually
viewed all six 90-dpi page renderings in builds/baseline/page-1.png
through page-6.png. No clipping, overlap or missing mathematical symbol
was observed. The source table is readable. The polished PDF's final
log was checked; this report does not claim another all-page visual
inspection of that changed version or the future final release.

Two initial JavaScript attempts to create the manuscript had string
delimiter errors and executed no patch or compiler. The corrected
patches created the actual files before either compilation. These
orchestration errors are not mathematical executions.

## Verified bibliography, theorem access and limits

During manuscript preparation the coordinator directly reopened:

- Lee–Nam's primary arXiv record and v2 HTML, verifying full title,
  Jungin Lee and GyeongHyeon Nam, first submission 18 September 2025,
  v2 dated 11 October 2025, arXiv identifier and DOI.
- The Ghioca–Hsia primary publisher record, verifying full title,
  Dragos Ghioca and Liang-Chung Hsia, Acta Arithmetica 222 (2026),
  1–26, DOI 10.4064/aa241119-28-10 and online date 11 December 2025.

The complete relevant source statements had already been actually read
in the coordinator's CP9 admission review. This preparation reopened
the Lee–Nam introductory weights and Theorem 1.5 in full. Two targeted
finds for later theorem/remark text returned internal errors; a later
two-position open failed with a connection error. Those failures are
not claimed as new body access. The accepted prior reading of Theorem
2.1 and Remark 4.5 remains explicitly identified in
../../continuation_round9/CP9_ADMISSION_REVIEW.md.

The original Ghioca–Hsia theorem proof remains unread in this work;
its height statement is used as stated and attributed in Lee–Nam.
The BibTeX entries were assembled from the verified primary records
under the shared citation-discipline fallback, not hallucinated from
memory and not presented as a successful DBLP/Crossref resolver call.
No fresh search query, source-PDF save, paid reviewer or upload occurred
in this manuscript-preparation source check. The research-pass search
counts remain distinct from these later direct opens.

## Remaining gates

Two actual nonauthor full-manuscript reviews with genuine responses and
versions, formal Route A evaluation, final fresh deterministic builds,
every-final-page visual inspection and exact release sealing remain.
The accepted CP9 proof review is not relabeled as a review of new TeX.
NO_BAD_EULER_OR_ROOT_NUMBER and the fixed-example boundary are unchanged.
