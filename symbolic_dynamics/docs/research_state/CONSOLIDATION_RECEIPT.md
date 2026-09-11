# History consolidation receipt — 2026-09-05

Scope: repository-backed session recovery, authorized by the user's request
to reorganize history after switching models and the standing Git-sync request.
This is not a new paper batch, scientific review acceptance, or public release.

Research-completion baseline: `76146ba17eb15beccfc38e625427f8da726db919` (P192–P196).

## Changes

- Added a concise root state index and an AGENTS recovery pointer.
- Added a history/exception ledger and a 190-row representative PDF index.
- Saved the pre-consolidation artifact snapshot and its read-only inventory tool.
- Added the missing P197–P201 pipeline recovery record: Stage 1 incomplete,
  two selected candidates, two pending candidate gates, fifth slot open.
- Updated the README's stale latest-batch heading, historical status caveat,
  and outdated fifty-paper directory label.
- Prepared the original 50 non-cache current-batch files for a scoped WIP
  Git checkpoint, with the new recovery record alongside them.

## Checks performed

- Three separate read-only inventory tasks covered the paper/Git inventory,
  research history/counting conventions, and unfinished current batch.
- Two cross-readers checked the new state documents. Their wording corrections
  were incorporated: SELECT versus central freeze; available historical corpus
  versus missing P51–P56; pending source-link records for all four candidates;
  P49/P50 audit holds; split-layout Git links.
- All 190 representative PDF hashes matched the snapshot.
- All 50 pre-consolidation WIP file hashes matched the snapshot.
- All 20 records in the P192–P196 canonical PDF manifest passed.
- The new index has 190 unique paper IDs, 180 tracked baseline PDF paths, and
  ten explicitly unlocated P57–P66 paths.

The inventory audit did not recompile or re-prove all historical papers.
One incomplete replacement-algebra control was run read-only and failed with
`ValueError: negative shift count`; it remains labelled failed WIP.

## Preserved open work

P51–P56 installed manuscripts were not found; P57–P66 and their P62–P66 batch
archive were not found in Git history; older P49/P50 writer/pre-run audit holds
were not resolved. None of these are silently closed by the history checkpoint.
The active five-paper research batch also remains unfinished.

The checkpoint commit can be found by its subject:
`Document symbolic-dynamics recovery state and checkpoint P197-P201 scouting`.
Its final commit ID and push result are reported after Git synchronization;
this receipt does not self-reference a future commit hash.
