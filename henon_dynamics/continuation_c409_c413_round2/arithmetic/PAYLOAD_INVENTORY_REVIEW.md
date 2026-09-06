# Read-only payload inventory sanity review

Session date: 2026-09-07. Scope: only the current
henon_dynamics/continuation_c409_c413_round2 directory and descendants.
No old tree, temporary build directories outside this tree, or Git/global
state was scanned or changed for this inventory.

## Disposition and non-atomic boundary

No symlink, special file, orphan TeX section, or unexplained duplicate
manuscript entry point was found in the checked tree. Generated auxiliary
files and historical author-build artifacts are present and are classified
below. **This is not approval of a final exact payload-member list.**
The coordinator was generating final build evidence during the read, so
the observations are a sequence of read-only snapshots, not an atomic
sealed manifest. A file count of 193 occurred at one intermediate traversal;
it is deliberately not a final member count and excludes this later report.

The review used rg file listings including ignored/hidden paths, direct
TeX input/bibliography searches, ordinary directory/type enumeration,
read-only PDF hashes, and the actual author build receipts. No check script
was written or executed, no LaTeX build or mathematical experiment was
rerun, and nothing was deleted or moved.
C409/C411 sources and existing receipts remained frozen.

## 1. Source wiring and filesystem types

The five manuscript entry points and all their direct TeX inputs were
compared against the actual .tex file listing:

| Paper | Actual section files | Other TeX input | Result |
| --- | ---: | --- | --- |
| C409_wild_fad | 7 | none | All seven are included |
| C410_wild_cubic | 9, including abstract | math_commands.tex | All nine and the command file are included |
| C411_two_clock | 7 | none | All seven are included |
| C412_integer_henon | 9, including abstract and Appendix A | math_commands.tex | All nine and the command file are included |
| C413_integral_trace | 6, including abstract | none | All six are included |

Thus all 38 section files are wired into their intended entry point.
The 45 observed TeX files consist of those 38 sections, five main files
and two included command files. No unused section or stray duplicate TeX
manuscript was found. Each main file references its local references.bib;
no includeonly exclusion was found.

Two scoped type traversals, without following links outside this tree,
returned no symbolic links and no non-file/non-directory special objects.
This covers the observed tree, not files another process may create later.

## 2. Keep as actual manuscript or historical evidence

The following should not be treated as accidental cache merely because
they were generated:

- papers/C4xx.../main.pdf: the five coordinator-facing manuscript PDFs.
  Their current release hashes belong in the final coordinator ledger,
  not in this intermediate inventory.
- The source plans, citation audits/metadata, author build reports,
  reverse outlines, revision records, independent manuscript reviews and
  formal evaluator records: these state what was actually checked at each
  stage. Older pending language inside an explicitly initial-build receipt
  is historical, not a reason to silently rewrite it after freezing.
- papers/C410_wild_cubic/build_author/attempt1_failed.log: explicitly
  preserved in its BUILD_REPORT as the first failed compile evidence.
  It must not be misread as the final clean log.
- The author logs and bibliography logs under build_author/, author_build/,
  or directly in the paper directory: although regenerable in principle,
  they are also the actual runs cited by the author receipts. Preserve the
  cited historical copy if its receipt remains part of the delivered record.
- Each existing final_build/pass_a.log, pass_b.log,
  pass_a_console.log, pass_b_console.log and bibliography.blg:
  these are actual final-run evidence, not a substitute for the coordinator's
  eventual comparison certificate. Preserve them when that certificate cites
  them.
- final_build/pdfinfo.txt, fonts.txt and main.txt: generated final-snapshot
  inspections. They can be regenerated but currently identify the output
  actually examined; retain the versions associated with the final receipt.

At the later scoped listing, final_build evidence directories were visible
for C409, C411, C412 and C413. C410's final build was still a coordinator
task at the observed boundary. No conclusion about missing later files is
drawn from this intermediate state.

## 3. Duplicate PDFs: exact observed relationships

Two papers contain a separately preserved author PDF in addition to the
root-level manuscript PDF:

| Paths | Observed relationship | Interpretation |
| --- | --- | --- |
| C410_wild_cubic/main.pdf and build_author/main.pdf | Both SHA-256 9d16aa8a475bf2eca95ca95f768d62a8525b2f352afb868deea88c48114c745a | Intentional copy of the 13-page author build; the author receipt explicitly says its optional root-distinctness prose revision still needs the coordinator's fresh build |
| C412_integer_henon/main.pdf and author_build/main.pdf | Different: root 66788e384cc8016240b17695decac08962f9289fef40a6782eeb108bd3ab699a; author 4974c90cd98a0529d00baf16a47b789fdba3ac37d9be432d2e8a2c3e6a8f7659 | Historical author artifact versus later coordinator output, not an unexplained conflicting manuscript |

Retaining an author PDF and a later release PDF is defensible evidence
preservation. In particular, the currently byte-identical C410 pair must
not be taken as proof that its post-review source revision was rebuilt:
the build receipt expressly distinguishes that source-only revision.
Only the coordinator's later final-build record can close that step.

C409 and C411 have no separate preserved author-PDF file. Their main.pdf
files changed during the coordinator's final-build work while the author
receipt hashes remained the earlier actual snapshots. At the hash read,
the main files were:

~~~text
94d0432495a8a38fbf159b316b462e28c40c7f5b6da65d8ace91d53b6fb5ccf4  papers/C409_wild_fad/main.pdf
881fa8f8d1a1d8ad71cfc1ecded18d3241a5d23e0ff4b0d3d120d5aabe329638  papers/C411_two_clock/main.pdf
60d9b0289b163216db7a217aeb06e8967053b00bc4f75ff7231eb3fa79ade552  papers/C413_integral_trace/main.pdf
~~~

These are observations, not a final-hash certification. An old author
receipt is not supposed to describe an overwritten final PDF as if the
same bytes persisted. The final ledger should use the final output, while
the historical receipt remains explicitly historical.

## 4. PNG renders and extracted text

The observed PNGs are reproducible renderings, not additional scientific
figures or newly run data:

- C410_wild_cubic/build_author/page-01.png through page-13.png:
  the 13 page renders actually used by that author's all-page inspection.
- C412_integer_henon/author_build/classification_layout.png and
  certificates_layout.png: the two pages identified in the author's limited
  layout check.
- C409_wild_fad/author-preview-title.png and
  C411_two_clock/author-preview-title.png: the representative title-page
  author checks, not a claimed full-page inspection.

These 17 observed PNGs may be retained as historical visual evidence.
Their provenance should remain attached to their corresponding author
stage; they must not automatically be called renders of a later rebuilt
final PDF. Any later final-page render set should be identified separately
by the coordinator.

The author/final main.txt extractions are also regenerable views of a
specified PDF. Retaining the inspected copy supports a reading receipt;
an extraction is not itself a new manuscript source, proof, or visual QA.

## 5. Regenerable LaTeX working auxiliaries

The following classes are ordinary build state, not authored mathematical
content:

- main.aux: label and citation bookkeeping;
- main.out: hyperlink/bookmark bookkeeping;
- main.fls: recorder input/output list;
- main.fdb_latexmk: build-dependency cache;
- main.bbl: generated bibliography, reproducible from references.bib and
  the declared bibliography style/toolchain.

They occur directly in C409, C411 and C413, under C410/build_author, and
under C412/author_build. They need not be mistaken for final source files.
A coordinator may decide how much reproducible working state belongs in
the eventual payload, but **this review does not authorize or perform any
deletion**. Logs that are also cited evidence are distinguished in Section 2
rather than being swept into a blanket cache category.

The scouting proof/source reports and the small .py verification/probe
sources elsewhere in this continuation are deliberate research history,
not LaTeX auxiliaries. No mathematical checker was invoked and no negative
or priority-limited research file was excluded merely because it did not
become one of the five manuscripts.

## Final handoff limit

No cleanup was performed. No final membership, all-page visual, byte-
reproducibility or Git-cleanliness verdict is issued here. The coordinator
must choose and seal the final exact member list after all active build
work finishes, retaining clear historical-versus-final artifact labels.
