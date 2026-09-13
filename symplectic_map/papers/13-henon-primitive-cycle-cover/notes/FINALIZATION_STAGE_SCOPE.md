# Paper 13 Local Anonymous Finalization-Stage Scope

## State and effect

- Candidate: henon_primitive_cycle_cover_v1
- Date: 2026-08-16 UTC
- Current state: FINALIZATION_STAGE_LOCKED / PENDING_INDEPENDENT_FINALIZATION_REVIEW / NO_RELEASE
- Eventual effect, only after every gate: LOCAL_ANONYMOUS_RELEASE_ONLY
- Existing release candidate: paper/main.pdf
- Submission, upload, external messages, identity release, and supplementary archive: false

This scope does not self-authorize release. It freezes every current manuscript, figure, build output, PDF, receipt, review, and governance input. A fresh role-separated gate reviewer must return exact verdict FINALIZATION_STAGE_PASS before a final-release manifest may be written. A separate terminal reviewer must then return both exact verdicts FINAL_INTEGRITY_PASS and RELEASE_CONFIRMED before the already existing anonymous PDF is designated for local release.

No role in this stage may edit, replace, rebuild, copy into the project, rename, move, clean, truncate, or delete paper/main.tex, paper/references.bib, paper/figures/architecture.tex, any existing project build output, either project PDF snapshot, or any prior artifact.

## Frozen input receipt

The lock author rehashed exactly the 31 files in the final publication lock integrity-role allowlist plus the independent draft-integrity review, for 32 frozen inputs. All are regular non-symlink files.

| Project-relative path | SHA-256 | Bytes | Role |
|---|---|---:|---|
| experiments/manuscript_lock.json | 488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd | 9154 | canonical M5 manuscript lock |
| experiments/publication_lock.json | 5fd33a907d4b324c6b56fdb3b70af1315475f44f077d27ba84a17653514a69cb | 22380 | canonical publication-stage lock and integrity authority |
| notes/CITATION_VERIFICATION.md | 08d310cb4c5b8e14810bf06e79e988ecf28b9ef2825868b7f7edfeccdce0e71b | 27784 | closed bibliography metadata and attribution authority |
| notes/CLAIMS_EVIDENCE_MATRIX.md | 21537ed1ed04abf7e3e1dc7d089a105fc36eb5815d164e1cae840f8c56464890 | 13041 | PC1/PC2, C1-C20, anti-claim, and evidence-boundary authority |
| notes/INDEPENDENT_DRAFT_INTEGRITY_REVIEW.md | 328f971a54a4cff6f1d45139f6409159157b5b2158890296c9b464487b9ebde3 | 11960 | independent DRAFT_INTEGRITY_PASS review |
| notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md | aaa77a37a8d8a8fccedd18073f346312b1ea0245447bbf1b0f5c60095809848c | 22525 | independent Round-1 manuscript review |
| notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md | 10e7e5ef1ca92a348c70495bb9c631e02af055c27c017d219e46736d35a028fd | 17090 | independent Round-2 MANUSCRIPT_REVIEW_PASS review |
| notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md | a1213f19a6da5531f411e3a7c63ef0f746a6577f021dd360cfc874463b8dec1c | 19231 | independent PUBLICATION_STAGE_PASS gate review |
| notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md | 3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98 | 15574 | independent RESULT_AWARE_HANDOFF_PASS |
| notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md | 83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e | 15344 | independent SOURCE_LOCK_PASS |
| notes/MANUSCRIPT_REVISION_R1.md | 44f081e3f9497c460ed3101dee5b7ba007bfe6022ded1abe8e0391202b8e2725 | 6120 | Round-1 bounded revision receipt |
| notes/NOVELTY_ASSESSMENT.md | bde37eb93989989d2c55c81b13c6919a9ba367c6f2d7ca2320335fd0df155c6a | 20383 | bounded positioning, preserved dissent, and forbidden-priority-language authority |
| notes/PROOF_PACKAGE.md | 9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9 | 25766 | sole source-proof authority when conjoined with SOURCE_LOCK_PASS |
| notes/PUBLICATION_STAGE_SCOPE.md | 17f56f7f12333803bc8b27a22e27bc33535dbf777483d8da22f34dee17b04e72 | 25352 | publication-stage integrity contract |
| notes/RESEARCH_QUESTION.md | 18ccf35df9b0f3b73636044c9400f3d79e8f213af365fb33504fa3524f6fd287 | 12301 | family, notation, PC1/PC2, boundary, and nonclaim authority |
| notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md | 265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307 | 16992 | M5 result-aware proof-to-writing scope |
| paper/BUILD_RECEIPT_R0.json | 1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548 | 4942 | canonical Round-0 build receipt |
| paper/BUILD_RECEIPT_R1.json | 5480ab22ebc7c9676395f9309baae15aa406f73f0cfa3e4901f288fb3e94ca51 | 5445 | canonical Round-1 build receipt |
| paper/DRAFT_ARTIFACT_MANIFEST.json | a4ff87715f0849c039764be2bf5bce4880d2214551d02cc455c003edc860665e | 15322 | canonical anonymous reviewed-draft artifact manifest |
| paper/PAPER_PLAN.md | 3dd625590a16e0fe64f475e5913a3d5f1b9eac9b2883e136f389c049ae5d0911 | 39066 | stable independently message-reviewed publication blueprint |
| paper/figures/architecture.tex | eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9 | 3185 | authorized definition-and-theorem diagram source |
| paper/main.aux | dcd56fb868640a1207f8f7c2c9d9b9b3d9de460078b89098e0d934c28ddb7592 | 16780 | current Round-1 LaTeX auxiliary output |
| paper/main.bbl | 1664a96990b3415b471194395b4d4e0d37ccb318013f50bf0e41cd0cd4dd1c9d | 8037 | current Round-1 rendered bibliography output |
| paper/main.blg | 401ed26512f413fbdbfab267da368164e702c87c2a425eb8afc92f08a2d2a61c | 918 | current Round-1 BibTeX log |
| paper/main.log | 998ff0432beb546b56300d41a6a7b5295265de217127c0232a2b1b88b50e9c7b | 38628 | current Round-1 pdfLaTeX log |
| paper/main.out | 838757a680eeb5ef6b3115a65e94801212acb9659c8ae2465e3184db40920af0 | 12541 | current Round-1 bookmark output |
| paper/main.pdf | 4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09 | 519969 | current anonymous reviewed draft PDF |
| paper/main.tex | f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce | 80689 | revised anonymous manuscript source |
| paper/main_round0.pdf | f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d | 517616 | preserved Round-0 PDF snapshot |
| paper/main_round1.pdf | 4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09 | 519969 | preserved Round-1 PDF snapshot |
| paper/references.bib | 005edd30410ffd8b9b9851e9008636aed9bcddba3195af550bd6daed0529a19b | 8175 | revised closed bibliography source |
| results/INDEPENDENT_RESULT_REVIEW.json | a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a | 4462 | bounded sealed-result integrity disposition only |

The draft manifest is 15,322 bytes at SHA-256 a4ff87715f0849c039764be2bf5bce4880d2214551d02cc455c003edc860665e. The draft-integrity review is 11,960 bytes at SHA-256 328f971a54a4cff6f1d45139f6409159157b5b2158890296c9b464487b9ebde3 and has exact verdict DRAFT_INTEGRITY_PASS. Round 2 remains MANUSCRIPT_REVIEW_PASS at SHA-256 10e7e5ef1ca92a348c70495bb9c631e02af055c27c017d219e46736d35a028fd.

The frozen revised sources are paper/main.tex at f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce, paper/references.bib at 005edd30410ffd8b9b9851e9008636aed9bcddba3195af550bd6daed0529a19b, and paper/figures/architecture.tex at eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9. The existing paper/main.pdf and paper/main_round1.pdf are byte-identical, each 519,969 bytes at SHA-256 4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09.

## Closed read and write authority

All arrays in experiments/finalization_lock.json are path-exact, unique, closed, and nontransitive. Embedded paths and hashes grant no access. Source-lock, code, preexecution, refine-log, runtime, raw-result, network, web, external metadata, other-paper, and unlisted project content are forbidden.

The lock author reads the 32 frozen inputs and may reread only the two active author paths. It writes exactly notes/FINALIZATION_STAGE_SCOPE.md and experiments/finalization_lock.json, then stops. It may not act as the finalization gate reviewer or terminal integrity reviewer.

The gate reviewer reads exactly the 32 frozen inputs plus the scope and lock, 34 files. Its sole project write is notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md. Any failed gate is zero-write and fail-closed. A passing review must end with exact verdict FINALIZATION_STAGE_PASS.

After that pass, the release-manifest author reads exactly those 34 files plus the gate review, 35 files, and writes only paper/FINAL_RELEASE_MANIFEST.json. It does no compilation.

After a valid canonical release manifest, the terminal reviewer reads exactly those 35 files plus that manifest, 36 files, and writes only paper/reviews/final_integrity_review.md. Since paper/reviews is absent now, creating it is authorized only as the necessary parent for that one file. Its final inventory must contain exactly one file and zero other entries.

The only project file writes in the whole stage are the two lock-author files, the gate review, the release manifest, and the terminal review. No existing project artifact modification or deletion is authorized.

## Gate review

The gate reviewer rehashes all 32 frozen inputs and both author outputs after author stop; strictly validates all JSON with duplicate-key and nonfinite rejection; verifies canonical bytes, self-hash exclusion, path safety, symlink absence, DRAFT_INTEGRITY_PASS, MANUSCRIPT_REVIEW_PASS, the one-revision review DAG, both build receipts, revised source hashes, and current PDF equality.

It also verifies all role lists, exact writes, temporary-build limits, external prohibitions, R100 firewall, theorem-evidence firewall, future-path absence, and continued absence of /root/autodl-tmp/symplectic_map/paper. It rehashes the scope and lock immediately before its sole PASS write.

## Final release manifest

paper/FINAL_RELEASE_MANIFEST.json must be strict sorted compact canonical UTF-8 JSON on one newline-terminated line with schema P13_FINAL_RELEASE_MANIFEST_V1. It contains 35 lexicographically path-sorted bindings for the 32 frozen inputs, scope, lock, and gate review; excludes its own SHA-256 and bytes; binds the existing paper/main.pdf as the sole release candidate; and records state LOCAL_ANONYMOUS_RELEASE_CANDIDATE_PENDING_FINAL_INTEGRITY_REVIEW.

It records exact project inventory, the terminal-review path as absent, zero source/build mutation, zero scientific computation, and no release effect before terminal review.

## Two isolated temporary builds

Only the terminal reviewer may invoke two separate:

    mktemp -d /tmp/p13-paper13-final-XXXXXXXX

Each returned root must be a non-symlink directory owned by the reviewer, resolve as a direct child of /tmp, match prefix /tmp/p13-paper13-final-, and start empty. Each root may contain exactly three frozen source copies: main.tex, references.bib, and figures/architecture.tex. Their hashes are checked before use. It may then contain only six derived files: main.aux, main.bbl, main.blg, main.log, main.out, and main.pdf.

Each root uses working-directory-local copies, environment TZ=UTC, SOURCE_DATE_EPOCH=1786838400, FORCE_SOURCE_DATE=1, and exactly:

1. pdflatex -interaction=nonstopmode -halt-on-error main.tex
2. bibtex main
3. pdflatex -interaction=nonstopmode -halt-on-error main.tex
4. pdflatex -interaction=nonstopmode -halt-on-error main.tex

latexmk, Biber, shell escape, network tooling, unexpected temp files, and every project build write are forbidden. Both temporary PDFs must be byte-identical to one another and to both paper/main.pdf and paper/main_round1.pdf at the frozen hash and size.

Each temp root may be recursively removed only after exact revalidation of its recorded path, direct /tmp parent, prefix, ownership, non-symlink status, and limited inventory. Absence is verified after cleanup. If safe cleanup fails, no broader deletion is allowed; the exact retained temp root and inventory must be disclosed in the terminal review.

## Terminal audit and verdicts

Before and after the two builds, the terminal reviewer rehashes all 36 project inputs and confirms no drift. It audits the source/review/revision/build/receipt/manifest DAG, project inventory, all PDF pages, fonts, metadata, title, anonymous byline, text, reference boundary, figure/table inventory, logs, warnings, citations, and references.

The sealed quality record is 27 A4 pages, 25 mathematical-content pages plus two reference pages, 30 embedded fonts, exact safe title, anonymous byline, empty identity metadata, zero undefined references/citations, zero missing glyphs, zero overfull or underfull boxes, zero BibTeX warnings/errors, and exactly eight nonblocking hyperref PDF-string warnings.

Builds, PDFs, receipts, manifests, and integrity checks are reproducibility evidence only and never theorem evidence. R100 stays count one, sealed, not rerunnable, and not invocable. No science or theorem recomputation is authorized.

On complete success, paper/reviews/final_integrity_review.md binds all hashes and inventories, discloses cleanup or retained temp roots, and ends with the following two exact nonempty lines in order:

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED

Any mismatch, drift, unsafe path, unexpected artifact, identity clue, missing verdict, or authority expansion means no release.

## Release boundary and cleanup binding

The conjunction of FINALIZATION_STAGE_PASS, a valid canonical release manifest, FINAL_INTEGRITY_PASS, and RELEASE_CONFIRMED designates only the already existing paper/main.pdf at the frozen hash as LOCAL_ANONYMOUS_RELEASE_ONLY. It creates no PDF or release copy and grants no camera-ready, submission, upload, preprint, repository, email, announcement, supplementary archive, acknowledgment, funding, author identity, affiliation, ORCID, or external-distribution authority.

The transient mistaken workspace-root paper path and its empty parent were removed. At lock time /root/autodl-tmp/symplectic_map/paper is absent. Gate and terminal reviewers must confirm it remains absent; this grants no sibling access.
