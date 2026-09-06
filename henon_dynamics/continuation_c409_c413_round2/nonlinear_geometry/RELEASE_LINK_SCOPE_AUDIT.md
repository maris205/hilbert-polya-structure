# C409–C413 release index, link, and scope audit

Runtime-clock checkpoint: 2026-09-06 16:17:53 UTC; the client calendar has moved to 2026-09-07, as already disclosed in the final build report.

Reviewer: `scout_nonlinear_return`, non-author of the release README, final build report, adjudication, and five evaluation records. The reviewer authored C412 and previously independently reviewed C410; this is not a new self-review or a new mathematical review of either paper. Automatic link scanning was delegated to the read-only `release_local_links` subagent, with its scope and limitations recorded separately below.

## Decision

**INDEX_SCOPE_AND_FINAL_PDF_MATCH_PASS.** The designated current release documents, registry entries, evaluation records, and five delivered PDFs are consistent. The initial all-tree Markdown scan found no unexpected missing local target, only the two explicitly reserved final sealing artifacts. The report's own inclusion in the automatic scan is confirmed in the closing addendum.

This is **not** a seal-complete, exact-payload-membership, Git-sync, target-Route-A, external-peer-review, or new all-page visual-QA certificate. The coordinator's subsequent ledger/manifest generation and actual integrity/Git receipts remain separate. No success of a future operation is inferred from this audit.

## 1. Actual semantic read scope

The reviewer read these documents completely, including the coordinator's last announced index revisions:

- Batch `README.md`: all 125 current lines, including `FIVE_COMPLETE_PAPERS`, the external current-state receipt location, the corrected conductor wording/source-path introduction, and the five-paper stop.
- `FINAL_BUILD_REPORT.md`: all 140 lines.
- `REVIEW_ADJUDICATION.md`: all 81 lines.
- The five actual 105-line YAML records, `evaluations/route_a/HCS-C409/2026-09-06.yaml` through `HCS-C413/2026-09-06.yaml`: all 525 lines, for consistency with the release index, not re-evaluation under the evaluator skill.
- `papers/C413_integral_trace/REVISION_RECORD.md`, including the newly appended actual R2 closure requested by the coordinator.

Restricted current-state/registry reads were:

- `../CURRENT_RESEARCH_STATE.md`, lines 1–35 only, stopping before the historical-selection header at line 36.
- `../docs/candidate_registry.md`, only the new C409–C413 section at lines 6–34.
- `../docs/obstruction_registry.md`, only the new C409–C413 section at lines 20–36, before the next historical section.

The final source hash list was read as a 50-entry file and its own digest checked. No earlier mathematical experiment, full evaluator, theorem checker, TeX build, source-copy comparison, or page-render inspection was rerun. No external source or URL was queried. The broad automatic Markdown scan described below is not a claim to have semantically reread all research documents in the tree.

## 2. Five actual final PDFs versus the final build table

For each PDF linked as the delivery entry in the current README, the reviewer ran read-only `pdfinfo main.pdf` and `sha256sum main.pdf` in its paper directory. Every page total, byte total, and SHA-256 agrees with `FINAL_BUILD_REPORT.md`:

| Paper | Actual pages | Actual bytes | Actual SHA-256 |
| --- | ---: | ---: | --- |
| C409 | 11 | 326878 | `94d0432495a8a38fbf159b316b462e28c40c7f5b6da65d8ace91d53b6fb5ccf4` |
| C410 | 13 | 408234 | `6b0ceb67ed7cb9db9f2a1bc35921f90c3534672efe5dd317262dd53db50c45ba` |
| C411 | 11 | 318511 | `881fa8f8d1a1d8ad71cfc1ecded18d3241a5d23e0ff4b0d3d120d5aabe329638` |
| C412 | 14 | 367848 | `66788e384cc8016240b17695decac08962f9289fef40a6782eeb108bd3ab699a` |
| C413 | 10 | 353053 | `60d9b0289b163216db7a217aeb06e8967053b00bc4f75ff7231eb3fa79ade552` |

The total is exactly 59 pages. All five are unencrypted letter-size PDF 1.5 files, matching the report. This metadata/hash check independently identifies the delivered bytes; it does not appropriate the coordinator's ten build executions or 59 actual page views as work performed by this reviewer.

`FINAL_SOURCE_SHA256SUMS` has exactly 50 entries and actual SHA-256
`3b94393fd4558ca18466a55efe003b08591b59e5645bc315038726300022b51d`, matching the build report. The list records the revised C410 normal-form source and revised C413 Section 5 hash, rather than their initial versions. The coordinator's separate verification of all input copies remains its own receipt, not a newly repeated test here.

## 3. Strict tuples and evaluation scope

The following tuples match four ways: each record's individual A0–A4 verdicts, its explicit `tuple` field, the batch README row, and the new candidate-registry row.

| Candidate | Exact tuple |
| --- | --- |
| C409 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` |
| C410 | `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` |
| C411 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` |
| C412 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` |
| C413 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` |

A read-only YAML parsing/comparison check confirmed:

- All five overall verdicts are `ROUTE_A_EXPLORATORY`.
- Every record has exactly the named nine A2 metrics, each literally `NOT_TESTABLE`: 45 of 45. None is a numeric zero or a passed target metric.
- All five A0 arithmetic-control statuses are `INCOMPLETE`; the source's analytic comparisons are not relabeled as a completed mandatory control panel.
- All 45 values in the five nine-field `scope_flags` mappings are actual Boolean `false`. All five separate `route_b_invocation_allowed` values are also Boolean `false`.
- All five retain `NO_BAD_EULER_OR_ROOT_NUMBER` and the same evaluator version/digest recorded in the release index.
- The declared artifact paths exist when resolved against the explicitly declared batch-root base. Each evaluation's separately relative `reference_routing` resolves to the existing `EVALUATION_SCOPE.md`.

The source-commit field is described by the registry as the research baseline, not as a claim that this not-yet-synchronized release is already inside that commit. The current-state section explicitly keeps seal/synchronization receipts pending. This audit does not read, alter, or certify Git refs.

The five source locks and corresponding registry boundaries remain aligned: C409's aggregated finite-prime series/actual FAD return clock; C410's generic inverse-image depth rather than forward period; C411's independent pair of ordinary clocks and joint rather than universal slice boundary; C412's integral monic Jacobian-`+1` family on rational periodic points; C413's integral single-map periodicity and fixed-level zeta, not a finite-count unrestricted-lattice zeta. No wrapper converts any of these source results to target Euler factors, root numbers, zero/divisor correspondence, or a Hilbert–Pólya operator.

## 4. Current source, historical evidence, and stopping point

The current README, final build report and adjudication correctly distinguish:

1. Actual non-author internal full-manuscript/source reviews, including their targeted confirmations.
2. Earlier author PDFs/logs and initial review hashes retained as historical snapshots.
3. The coordinator's current, revised-source final PDFs with the five hashes independently matched above.
4. Still-separate final payload membership/integrity and actual Git synchronization receipts.

C410's revised distinct-root paragraph is identified as the one selected optional edit; its unneeded optional descent parenthesis is not falsely listed as implemented. C413's revision record retains the historical R2 requirement and appends an actual closure pointing to `FINAL_BUILD_REPORT.md` with the same final PDF digest observed here. This closes a current-source/PDF discrepancy by a new receipt without pretending the earlier PDF was already current.

The stable `FIVE_COMPLETE_PAPERS` label does not claim a completed seal. Routing the actual seal/Git receipt to the batch-external current-state file avoids embedding a self-referential commit identifier into the self-hashed payload. The ledger excludes itself and the manifest; the manifest includes the ledger and excludes itself. These are stated rules, not proof of a future successful integrity check.

The release table has exactly C409–C413 and the paper tree has exactly five `main.tex` entry points. The finite-lattice inverse, cocycle and spectral-filter notes remain unnumbered. README, current-state entry and both new registries all stop this batch at C413 and do not authorize a sixth paper/C414 or an external submission. No inconsistent promotion or stopping-point defect was found.

## 5. Automatic all-new-tree Markdown link scan

This was a separate read-only subagent task over the entire `continuation_c409_c413_round2` tree, not only the files semantically read above. The initial scan covered all 45 existing `.md` files, including ignored-directory contents, before this audit report was created. It found:

| Item | Initial observed count |
| --- | ---: |
| Markdown files | 45 |
| Parsed link occurrences | 253 |
| External URL occurrences skipped | 110 |
| Local link occurrences checked | 143 |
| Unique normalized local targets | 75 |
| Existing local-link occurrences | 141 |
| Reserved pending occurrences | 2 |
| Unexpected missing local targets/occurrences | 0 |

The only missing targets were:

| Source occurrence | Resolved batch-root target | Classification |
| --- | --- | --- |
| `README.md:104` | `ARTIFACT_LEDGER.md` | `RESERVED_PENDING` |
| `README.md:105` | `MANIFEST.sha256` | `RESERVED_PENDING` |

Those exact two final artifacts were explicitly reserved by the task and are identified as last-generated files in README lines 104–110. Their absence at this pre-seal checkpoint is expected, not an accidental broken link. Their later content and exact membership must still be checked by the coordinator. The final rescan after this report's creation is recorded below.

### Method and limits

The scanner used read-only `python -B`, `os.walk(root, followlinks=False)`, and case-insensitive `.md` selection, independent of Git ignore rules. There were no `.markdown`, `.mdown`, `.mkd`, `.mkdn` or `.mdwn` files, and no encountered symlink files/directories. `markdown-it-py` 3.0.0 CommonMark tokens supplied links and images, with source offsets mapped to line numbers; an independent Mistune 3.1.3 AST cross-count also gave 253 links. Reference-style and angle-bracket destinations are handled. The actual dataset contained no reference definitions/usages, images, HTML tokens, or anchor-only links.

For each local destination, the scanner removed an unencoded query/fragment, URL-decoded the path, removed a trailing `:line` or `:line:column`, resolved relative paths against the containing Markdown file, performed lexical path normalization and tested existence. URI/protocol-relative external URLs, empty targets and internal-only anchors were skipped. Fourteen unique targets lie outside the scanned tree; only their existence was tested, without recursively scanning those external trees. Only the two exact batch-root ledger/manifest names are exempted as reserved missing targets.

This is an existence audit of parsed Markdown destinations. It does not validate heading fragments, numeric line ranges, external-URL availability, malformed Markdown, extension-specific wiki links, prose/backtick-only paths, or the semantic/mathematical correctness of the target. Code examples are not mistaken for actual links. The initial scanner rechecked all 45 input digests before returning and found no changes during its scan. No helper script or scan-output file was written by the subagent.

## 6. Bounded document snapshot and handoff

The following actual digests identify the coordinator-owned current documents read after its final announced edits:

```text
778319935527203686ba7e133edfea11000c2a8aa94c43311ee406658ebd4df2  README.md
e3eda6b644379d362ee0c56175af90c92991d6908beba86ab9de9b54b2cae9a4  FINAL_BUILD_REPORT.md
a383a71adcd1d11bda999c309675286aa9e3f8f09b6e43d14cb2c5090c09503c  REVIEW_ADJUDICATION.md
efda77684f60f3db361ef27ee149e20433b32d6c184933bb04793c5c41e0d792  papers/C413_integral_trace/REVISION_RECORD.md
```

No correction to a shared index, source, PDF, evaluation or Git object was made by this reviewer. The only authored file is this report. Its scoped findings allow the coordinator to proceed to the separately required ledger/manifest generation and actual receipt checks; they do not predeclare those operations complete.

## 7. Actual final scan including this report

After this report was created, the read-only subagent rescanned the whole tree and explicitly included it as the 46th Markdown file. The report contains zero parsed link destinations. The final observed counts remained 253 total link occurrences, 143 local occurrences, 110 external occurrences skipped, 75 unique local targets, 141 existing local occurrences, two `RESERVED_PENDING` occurrences and zero unexpected missing targets. The independent second parser again counted 253 links. All 46 input digests and the Markdown member set were stable during that scan.

The only pending occurrences remained `README.md:104` to `ARTIFACT_LEDGER.md` and `README.md:105` to `MANIFEST.sha256`. This receipt addendum introduces no link destinations; a final read-only count after its insertion likewise confirms the same 46-file and link totals. No self-containing hash is embedded here as a purported final seal.

Final bounded disposition: **INDEX_SCOPE_PDF_AND_LOCAL_LINK_AUDIT_PASS_WITH_TWO_RESERVED_SEAL_ARTIFACTS**. The coordinator may now perform the separately authorized sealing/receipt workflow. The seal and synchronization themselves are not certified by this report.
