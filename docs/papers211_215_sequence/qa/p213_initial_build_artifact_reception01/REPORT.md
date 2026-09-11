# P213 initial-build artifact reception (author-side)

Outcome: the fresh confirmation **run02 is accepted at the initial-build artifact scope**, subject to root reception of this packet. The earlier run01 missing-prepin finding is preserved, not retroactively repaired. No current unknown TeX-recorder input or unresolved final build diagnostic remains in run02. This is not Round0, a manuscript review, either terminal build, scientific verification, or paper completion.

## Exact executions and provenance

- Run01: root grant and consumption in ../p213_initial_build_binding01; actual launch 69f435 (session 25156), sole completion a6ba5f, exit 0. Its effective request uses the original preparation BUILD_REQUEST.sh plus the five MKTEX*=0 variables, as recorded by ACTUAL_NATIVE.json.
- Run02: separate root grant P213_INITIAL_CONFIRMATION_BUILD_02, consumed before submission; launch 171d81 (session 98918), sole completion dde165, exit 0. The effective script is ../p213_initial_build_binding02/BUILD_REQUEST.sh, SHA256 de6e52469695e1e326100660c5bd988ddc387e5dd5c50cc9e88264d6b8339b9d. Its only source changes are the two exact binding/output path substitutions. GRANT.json, CONSUMPTION.json, LAUNCH_NATIVE.json and COMPLETION_NATIVE.json agree on the effective request; root preflight 8a87ce checked the new script, all 223 inputs, output absence and free space before launch.
- The inner REQUEST_AND_BINDING.sha256 intentionally still hashes the original preparation script/request. It is historical preparation provenance, **not** the identity of the actual run02 script/request. The outer grant/native envelope supplies the latter.
- Both use a clean 13-variable environment, no shell escape, five disabled TeX generation switches, a fixed source-only copy of nine inputs, four build steps (TeX/BibTeX/TeX/TeX), and fixed diagnostics/render commands. This is the agreed ordinary trusted-bootstrap scope, not hostile execution confinement or a complete process/syscall read attestation.

The current batch lifecycle README/AUTHORSHIP changes are outside these nine sources. No unchanged-live claim is made for those documentary files.

## Full artifact and snapshot checks

Each run contains 165 ordinary files and 13 subdirectories, with no symlinks in the inspected output tree. Sizes are 4,304,353 bytes (run01) and 4,304,613 bytes (run02). All 150 text files per run were read in full by bounded fixed-file reads; their complete native outputs are retained and compared byte-for-byte to their current files. The extra seven binding02 text reads are in the second capture. All 330 artifact hashes are in ARTIFACTS.sha256. No PDF/PNG was substituted into the manuscript.

The read-only ARTIFACT_CHECK.js validates:

- all nine live/cold source hashes and exact live-to-cold source bytes; all eight source-guard stdout/stderr pairs per run;
- all selected 222/223 runtime guard rows, before and after, plus current full 223 input hashes;
- all eight before/after product snapshots for four build steps, exact PRESENT/ABSENT partition over eight possible products, every present product hash, and exact on-disk snapshot members;
- each preceding after-snapshot equals the next before-snapshot; BibTeX preserves pass1 AUX/LOG/FLS/PDF and adds only BBL/BLG; pass2/pass3 preserve BBL/BLG; pass2/pass3 AUX bytes stabilize; all six pass3 products equal the final source-only products;
- all 15 recorded step requests and zero supervisor statuses per run, with empty step stderr and controller stdout/stderr; request bodies are preserved in full (the checker asserts exact four build argv and common supervisor/cwd framing for all 15);
- every ordered record from the three genuine TeX recorder files per run, rather than treating inherited BibTeX FLS snapshots as fresh BibTeX recordings;
- final-product/page pins, seven-page extracted text without ??, [?] or [VERIFY], 17 Type1/Builtin fonts marked embedded/subset/Unicode, and 92 raw Buffer.equals comparisons including both final PDFs and all seven PNG pairs.

The fixed diagnostic/render argv were also read completely: pdfinfo main.pdf; pdffonts main.pdf; pdftotext -layout main.pdf -; the literal awk diagnostic expression from BUILD_REQUEST.sh; and page-indexed pdftoppm -singlefile -png -r 150 calls. These checks do not assign a fabricated native child exit status: the stored statuses are supervisor returns.

## Ordered TeX inputs and the historical missing prepin

FLS_ORDERED.tsv preserves every raw input/output path and order (1,504 records total). Both runs have 246 / 253 / 253 records. In each run/pass, 50 source INPUT occurrences cover the eight TeX sources; references.bib is instead the BibTeX database role.

| Run/pass | Presealed runtime INPUT | Generated-before INPUT | Earlier same-pass AUX INPUT | OUTPUT | PWD | Missing prepin |
|---|---:|---:|---:|---:|---:|---:|
| 01/pass1 | 190 | 0 | 1 | 3 | 1 | 1 |
| 01/pass2, pass3 (each) | 190 | 7 | 1 | 3 | 1 | 1 |
| 02/pass1 | 191 | 0 | 1 | 3 | 1 | 0 |
| 02/pass2, pass3 (each) | 191 | 7 | 1 | 3 | 1 | 0 |

The seven generated-before occurrences are three AUX reads before its overwrite and four BBL reads; the final AUX read follows the recorded same-pass AUX output. Pass1's initial AUX/BBL are correctly absent. There are 73 / 74 / 74 distinct normalized INPUT paths per run, including sources and generated files.

Historical finding AR-01: line 23 in every run01 FLS reads /usr/share/texlive/texmf-dist/fonts/map/fontname/texfonts.map, absent from the original 222-item selected runtime seal. Root subsequently authorized only this additional fixed public-file stat/read/hash. Native dbc5ae / f78eaa / d1a35b record a 3,524-byte regular public-domain file, SHA256 d9693993efdc7d0b9ab3df777589995d43e24eeae95f12b6a230a19caadeaa42. Its complete post-build body is preserved as texfonts.map.POSTBUILD.txt. Twelve active aliases cover circle/lcircle/lcirc fonts and their w variants; no active include or alias for the consumed CM/AMS fonts appears. These present-day contents and old timestamps do **not** prove the run01 pre-build body.

Root addressed the affected dependency prospectively with the fresh run02 grant: its 223-item manifest is the old 222 unchanged entries plus this exact map, SHA256 35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530. Preflight, archived before/after checks, current hashes, and all ordered run02 FLS records agree. AR-01 remains a historical run01 gap, superseded for initial-build acceptance only by the new complete confirmation. No third build was requested or run.

BibTeX used the pass1-generated main.aux, presealed plain.bst, and declared references.bib. Its AUX declares only \bibstyle{plain} and \bibdata{references}, with no nested \@input; BLG names those roles, reports three used entries and warning$ -- 0. Generated BBL contains exactly boccara2002, fukuda2023 and nishinari1998. BibTeX does not supply a separate recorder here: these are complete recorded top-level BibTeX roles, not a claimed syscall closure. Selected runtime files are not all necessarily consumed; the accepted bootstrap boundary remains unchanged.

## Complete negative diagnostic dispositions

CHECK_RESULT.json contains each diagnostic's original file, line, full wrapped message and disposition for both log and stdout, for all three TeX passes in each run. Counts below are warning messages per log; stdout is a duplicate stream, not an additional warning count.

| Pass, each run | Reference warnings | Citation warnings | General rerun/undefined warnings | Final disposition |
|---|---:|---:|---:|---|
| 1 | 37 | 3 | 2 | 42 total, all resolved by pass3 |
| 2 | 0 | 3 | 2 | 5 total, all resolved by pass3 |
| 3 | 0 | 0 | 0 | No remaining warning |

Pass1's “No file main.aux.” and “No file main.bbl.” are expected cold generated-file absences. There are no overfull/underfull boxes, missing-character diagnostics or fatal errors. The sole final diagnostic grep/awk match is main.log:3, “file:line:error style messages enabled.” It announces the error-message format and is not an error. BibTeX has zero warnings/errors. All final references/citations settle, and both final PDFs are exactly 225,140 bytes.

Root personally viewed all seven run01 pages and recorded their page-specific disposition in ../p213_initial_build_binding01/INITIAL_PAGE_VIEWS.md. Root identity c7f825 in ../p213_initial_build_binding02/IDENTITY_NATIVE.json and this reception's eight raw comparisons prove the entire final PDF and all seven rendered PNGs unchanged between runs. Reusing those actual views is therefore a byte-identical-view reuse, not a new visual inspection by this author-side agent.

## Check development, failed evidence and read limitations

Final full check c9f592 exited 0, producing complete 70,483-character JSON retained in CHECK_RESULT.json and native wrapper in NATIVE_CHECKS.json. Two failed checker versions/native outputs are retained, not overwritten: 58df65 rejected a hand-entered expected count of 39 versus the actual full census of 42 first-pass warnings; 8729ea then rejected relative run02 capture paths before explicit workspace resolution. The respective source versions are ARTIFACT_CHECK.failed01.js and ARTIFACT_CHECK.failed02.js. Neither failure executed TeX, changed sources or opened an unknown host file.

Earlier orchestration/read problems are disclosed: an early-EOF code-host failure lost transient lookup state; a subsequent missing-lookup TypeError followed four successful binding reads; full fixed-file discovery and 300 later reads recovered actual artifacts. A resumed skill-reference lookup used the wrong relative path (187912, exit 2); the actual linked docs/research_state/WORKFLOW.md was then read completely (ad5550). Large recovery-index/combined FLS displays were truncated and are not claimed as full displays; all selected instruction files and build log bodies were read in full, and complete captures, not truncated displays, feed the check. An initial apply_patch request failed formatting validation before writing the checker. The TSV's six provisional unknown labels were corrected to historical-missing-prepin/run02 selected-runtime before this packet was sealed. Prior runtime-resolution negative outputs remain in the original frozen packet.

This packet uses the project research skill's changed-dependency rule and paper-compile's full diagnostics/fonts/page requirements. It performs no generic cleanup, retry loop, package installation, new scientific run, grant, PDF adoption, Round0 freeze, reviewer assignment, Git action or external release. This author/proof contributor is ineligible for P213 manuscript reviewers A/B. Root's next authorized milestone remains its own reception followed by the controlled physical Round0 and process-separated review workflow; no paper count changes here.
