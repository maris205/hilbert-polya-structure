# Terminal coverage strengthening: actual hash-only checks

2026-09-05 UTC. QA_INFRASTRUCTURE_ONLY / NOT_RESEARCH_REVIEW.
Only the auditor and these new QA records are changed. No accepted paper,
review, canonical, manifest, frozen snapshot, old captured stdout, recovery
index or Git state is changed. P203 is not added to the terminal registry.

Auditor SHA-256 after this change:
`c258dffb329bfbca9de738fbba153adfa69f483d8423af9edb1dac39653f1d9f`.

## Confirmed gaps before the change

The old `parse_manifest` validated each listed row but did not require every
recursive file to appear. The old paper gate required certain top-level
payload entries, not an exact complete directory inventory. Nested review
`qa/SHA256SUMS` rows were parsed, but top-level `QA_SHA256SUMS` was only
hashed as a file and never expanded. Consequently P199 B, P200 A and P200 B
each had 17 cold-build/visual payload files whose hashes the old review gate
did not check. Independent read-only expansion found all 51 actual payloads
correct; the gap was in the auditor, not corruption of those artifacts.

Frozen-round directories were not required or explicitly bound to live and
round-labelled source/PDF bytes by the old paper gate. The full-batch global
PDF/package manifests were checked only for existence, not row hashes or
the exact current terminal-paper target set.

## Implemented checks

1. `recursive_files` inventories all regular files and rejects symlinks or
   other nonregular artifacts anywhere in the covered subtree.
   `complete_manifest` requires exact recursive file coverage excluding only
   that manifest itself, while preserving every original row/hash/safety
   check. Paper packages and `qa_final` use it.
2. `review_manifest_gate` retains exact top-level coverage, expands every
   permitted nested `SHA256SUMS`, explicitly parses the accepted top-level
   `QA_SHA256SUMS` serialization, and requires the union of manifest files
   and verified payloads to equal the entire recursive review file set.
   Input-pin lists are not repurposed as coverage manifests.
3. `frozen_round_gate` requires all three stages and their source, bibliography,
   verifier and canonical. The documented old core-only freezes remain
   explicit: P197 stages 0/1/2 and P199/P200 stages 1/2. P199/P200 stage 0
   is `round0_snapshot`; other stages use `frozen_roundN`. Modern full
   freezes require their own manifest/PDF, and every existing internal
   manifest receives complete hash/coverage checks. Internal PDFs must match
   their round-labelled PDFs; Round2 core and PDF must match live artifacts.
   An explicitly `ACCEPTED_NO_CHANGE` A/B delta additionally binds the two
   adjacent stages and PDFs. An actual accepted repair is not silently
   overwritten by a universal old/live-equality assumption. Round1/2 receipts
   are added to required paper payloads; existing review pin/delta gates
   remain in force.
4. `global_manifest_gate` requires five distinct registry targets in each
   manifest, actually validates their hashes from repository-relative paths,
   and rejects missing/extra/duplicate/wrong targets. The exact expected
   targets are each terminal paper's `main_round2.pdf` and `SHA256SUMS`.
   The entire repository is not incorrectly treated as one package inventory.
5. The full-batch banner derives paper IDs from `PAPERS`; the external label
   is `OWNER_AMBER/HOLD_EXTERNAL`, not the obsolete P197--P201 range. The
   main cardinality failure now says five retained terminal packages are
   required. The registry still contains only P197/P199/P200/P202; P203
   must not enter until its real terminal package is ready.

The previous narrowly pinned P202 status/intake compatibility, all replay
requirements, severity tests, accepted-delta conditions, metadata/build
checks and the five-terminal-package condition are preserved.

## Real structural checks, not invented terminal reruns

`COVERAGE_HASH_AUDIT.txt` is the actual stdout of an execution importing the
updated auditor with `python -B` and calling only its hash/coverage/freeze
functions. The executed operations were:

```python
for number, directory in audit.PAPERS.items():
    audit.complete_manifest(directory)
    audit.complete_manifest(directory / "qa_final")
    audit.frozen_round_gate(number, directory)
    for suffix in ("a", "b"):
        review = audit.SEQ / "reviews" / f"p{number}_{suffix}"
        audit.review_manifest_gate(review)
        audit.recursive_files(review)
```

It also actually parsed the two retained three-paper subset manifests and
confirmed that the full global gate rejects the current four-paper terminal
registry. Those historical subset checks are not represented as a five-paper
global result. The two full-batch global files are presently absent, as
expected while the fifth terminal package is incomplete.

The run passed 8,577 mechanical checks. Exact paper manifest sizes are
81/140/116/184; all four final QA inventories contain 32 files. All twelve
frozen stages pass their applicable core/hash/manifest/PDF checks. Recursive
review file counts for 197 A/B, 199 A/B, 200 A/B and 202 A/B are respectively
23/32, 25/28, 28/28 and 44/41. No recursive payload is missing from the
expanded verified inventory, and no symlink was found.

No author or review mathematical verifier, PDF compilation, source-only
cold build, or full terminal replay is executed by this structural run.
Its status is `STRUCTURAL_PASS_NOT_TERMINAL_REPLAY`. The parent will perform
the newly strengthened full P202 and eventual five-paper terminal audits;
their increased assertion totals must come from those actual runs. Existing
captured audit outputs retain their original counts and code-version scope.

## In-memory rejection controls

Focused controls, without modifying any material file, verified rejection
of an unlisted recursive file, a corrupted legacy QA payload digest, frozen
code drift, a missing global target, and an extra rejected-paper target.
The positive/missing/extra five-target set tests used a temporary in-memory
registry and mocked manifest rows; they are parser tests, not real global
hash attestations or registration of a fifth paper. No persistent registry
or evidence was changed. The real current four-paper gate remains blocked.
