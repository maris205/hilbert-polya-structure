# Independent bounded release-link and PDF audit

2026-09-06. Reviewer: current-team nonlinear-return scout, independently
checking the coordinator's assembled release. A separate current-team
nonaffine-characteristic reviewer performed the read-only five-PDF metadata
subcheck. This is an internal artifact audit, not peer review.

## Actual scope and method

The audit covers every Markdown document under
`henon_dynamics/continuation_c407_c408_round3`, and only the newly added
C407/C408 paragraphs of these three shared files:

- `henon_dynamics/CURRENT_RESEARCH_STATE.md`: added lines 68--90 at audit time.
- `henon_dynamics/docs/candidate_registry.md`: added lines 6--32.
- `henon_dynamics/docs/obstruction_registry.md`: added lines 20--40.

The shared-file boundaries were obtained from actual `git diff --unified=0`,
not from a whole-registry historical scan. The reviewer read the complete
new README, final-build report, batch plan, and those added paragraphs for
delivery/status consistency. Proof text was not re-reviewed in this task.

`rg --files` supplied the new-tree Markdown inventory. A read-only Node
stdin audit masked fenced and inline code, extracted the inline Markdown
destinations, resolved local paths relative to each source file, and used
filesystem existence/type checks. A separate syntax scan found no scoped
reference-link definitions, HTML href/src links, image links, or local
anchor-only destinations requiring another parser path. The actual local
links had no fragment targets. This records the syntax present in these
files; it is not a claim to implement an arbitrary Markdown renderer.

The completed initial audit command exited 0 and printed every source,
line, destination, resolved target, and status. It covered 28 new-tree
Markdown files plus the three shared-file additions: 31 documents in all.
There were 82 local-link occurrences and 51 unique resolved local targets.
Of these, 77 occurrences existed and five occurrences referred to three
explicitly reserved targets; there were zero unexpected broken paths.
The excluded external-link occurrence count was 46. No external URL was
fetched or revalidated in this release audit.

| Initial scope | Documents | Local occurrences | Unique targets | Existing occurrences | Reserved occurrences | Unexpected broken |
|---|---:|---:|---:|---:|---:|---:|
| Entire new tree, before this report | 28 | 66 | 48 | 61 | 5 | 0 |
| Three shared-file additions | 3 | 16 | 12 | 16 | 0 | 0 |
| Combined, with targets deduplicated | 31 | 82 | 51 | 77 | 5 | 0 |

The initial three reserved targets were exactly:

- `PAYLOAD_FILES.txt`: two occurrences, in README and final-build report.
- `MANIFEST.sha256`: two occurrences, in the same two documents.
- `reviews/RELEASE_LINK_AUDIT.md`: the README's one self-target, before
  this report was written.

Only the first two are intentionally deferred until this audit finishes.
Their future existence and correctness are not inferred from a reserved
link. The coordinator owns their generation and the subsequent exact
member/hash verification. The post-write recheck is recorded below.

## Five PDF targets and independent metadata receipt

The nonaffine-characteristic reviewer read the full 90-line README and
106-line final-build report and executed `realpath -e`, `stat -c`, and
`sha256sum` on all five PDF targets. Those three batched commands each
exited 0, as did five separate `pdfinfo` calls. Every resolved target was
a regular file; `stat` and `pdfinfo` agreed on byte sizes. The exact targets
below are relative to `/root/autodl-tmp/hilbert-polya-structure/henon_dynamics`:

| Paper | Actual resolved target relative to the Hénon directory | Pages | Bytes |
|---|---|---:|---:|
| C404 | `continuation_c404_c408_round2/henon_resonance/paper/main.pdf` | 10 | 373654 |
| C405 | `continuation_c404_c408_round2/arithmetic_forms/paper/main.pdf` | 10 | 355317 |
| C406 | `continuation_c404_c408_round2/critical_delta/paper/main.pdf` | 13 | 403808 |
| C407 | `continuation_c407_c408_round3/arithmetic_candidate/paper/main.pdf` | 13 | 411706 |
| C408 | `continuation_c407_c408_round3/cluster_boundary/paper/main.pdf` | 12 | 374170 |

The corresponding actual SHA256 values were:

```text
C404 99c58e5805bb4e5b70e5f86505dc60dd8f79df76ea0011ac901127456e10a3cc
C405 9b6801db5237ef523fded18797ec7508a06762bd79fd1c32f0074ddbfa9290c3
C406 43f04734234a9e21e41ad0eaff5e199c642935228475c4207e7a4cee14bec1a9
C407 12cecce888926bcce1b89999c043eeff5c182253dedcba0e7827d387e0d849be
C408 9d94e32bff36110a16822b7cc9c784ff1c200caa72f888ca71aa5c48b7620621
```

All five page counts match the README. Their sum is
`10 + 10 + 13 + 13 + 12 = 58`, with 33 reused pages and 25 new pages.
The new C407/C408 byte counts and hashes match the new final-build report
exactly. The three old hashes above are present read-only measurements,
not a claim to rebuild, reseal, or newly prove the old papers.

All five actual `pdfinfo` results reported A4 pages (595.276 by 841.89
points), PDF 1.5, no encryption, no forms, and no JavaScript. This subcheck
did not rerun final builds, compare the build pairs again, or repeat the
coordinator's all-page visual QA. Its exact metadata receipt was returned
to this reviewer and the root coordinator without writing other files.

## Status inconsistency found and closed

The initial completion paragraph of `BATCH_PLAN.md` said all preceding
gates were complete, while the preceding gate list included sealing and
read-only manifest verification. Those operations were intentionally still
pending. The reviewer reported this wording inconsistency promptly and
did not modify the coordinator's file.

The coordinator narrowed the completion statement to manuscript review,
builds, and page QA, and explicitly assigned sealing/Git completion to its
remaining work with a CURRENT link. The reviewer reread affected lines
98--105 and verified that clarification; the added CURRENT link was
included in the successful 82-occurrence scan. No PDF, theorem, or source
change was needed. No unresolved delivery/status inconsistency was found
in the inspected README/report/plan completion and shared additions.

## Boundary of the conclusion

This audit checks local destinations, delivered PDF metadata, and the
specified current completion wording. It does not certify external URLs,
mathematical correctness, journal acceptance, a worldwide novelty search,
full historical registry consistency, old-manifest integrity, build
reproducibility in another environment, or the not-yet-generated release
manifest. No source or PDF was edited, no experiment or build was rerun,
and no Git or sealing operation was performed. The only reviewer-owned
write is this report, using `apply_patch`.

## Post-write self-target check

After creating this report, the same read-only audit was actually rerun
and exited 0. The inventory then comprised 29 new-tree Markdown files
including this report, plus the same three shared additions: 32 documents.
The 82 local-link occurrences and 51 unique targets were unchanged.
There were 78 existing occurrences, four deliberately reserved occurrences
to exactly `PAYLOAD_FILES.txt` and `MANIFEST.sha256`, and zero unexpected
broken paths. Within the new tree the split was 62 existing plus four
reserved; all 16 links in the shared additions existed. The README's
self-target to this report now exists. The 46 external-link occurrences
remained excluded.

The new report's whitespace check produced no findings. Remaining
coordinator work is to generate the two named reserved files and check
their exact membership and hashes; this audit does not predeclare that
future check successful. The bounded release-link/PDF audit has no
remaining blocker.
