# P212 section05 source-amendment integration map

ADVISORY_ONLY / AUTHOR_CONTRIBUTION / NOT_INDEPENDENT_AUDIT.
I authored the proposed execution-status prose. This map identifies affected
existing bindings; it supplies no acceptance, executable amendment, gate
implementation, host check or operational authority.

Changing the 804-byte section05 to the exact proposed 1,237-byte text would
invalidate the current eight-source profile **before even the contract
help/version phase**. Revision02 driver reads every fixed source pin before
phase dispatch. Merely changing the frontier would instead fail its immutable
whole-companion hash. The required amendment is therefore a coordinated source
delta, not an in-place one-line pin refresh.

## Exact eight-source identity

All eight current files and the corresponding physical source-preparation
originals are in [INPUT_RICH_PINS.json](INPUT_RICH_PINS.json). Current source
total is 19,659 bytes. Exact proposed05 would add 433 bytes, giving 20,092
bytes over the same eight filenames if no other file changes. This last
total is arithmetic on source bytes, not build or runtime evidence.

| Relative source | Current bytes | Current SHA-256 |
|---|---:|---|
| `main.tex` | 1463 | `da04d4ca19ed94ce2fae1d181f238b0e1ae944ca09a714a30c6bb0e11f375d8a` |
| `math_commands.tex` | 243 | `3ebb1fd506f17810d19531cee9333b52617ee5a5f9231df6307936e0a392f938` |
| `references.bib` | 1927 | `9ad7c6bebc1aeef3a9d0e3f0703e876f2e1a634c5bf2d7f46297cfa7d5d1cf38` |
| `sections/01_setup.tex` | 4249 | `44ca562e26d6e8c6c5d92f33245e0a26f1a2cbbd2d5caf204352437d343cc04b` |
| `sections/02_returns.tex` | 4937 | `7185cd89b09569bc2977e71a5a74ea6c65b5a734a18905e8b11a592985be9002` |
| `sections/03_period_set.tex` | 1537 | `45f2e69dbe9d9f4418a439c407fd77309513fb515b12b38ab64bb421f12df490` |
| `sections/04_census.tex` | 4499 | `4f4e2db96c6f2fd9734f0ed29d1dedc759daef2d87e02d68890deb5f0cf4b353` |
| `sections/05_scope.tex` | 804 | `6f0d84102903eb21dffb52095b9b78f257550a4c6d2ec22c8add6a3a4cdd3a1c` |

Proposed05 SHA-256:
`44ab0ee97ab09a7bd0d68ddaf116d74f43314f69ef00821a77b67282d851012d`.
The sealed [prose proposal](../p212_execution_scope_delta_preparation01/HANDOFF.md)
and its old/new/diff originals remain unchanged.

## Typed existing consumer map

All paths below are relative to `docs/papers211_215_sequence/qa/`.
“Invalidated” means unusable as a **current changed-source** key; it never
means that an old accepted result or historical snapshot should be edited.

| Type / exact consumer | Literal dependency | Required future handling |
|---|---|---|
| Original physical provenance: `p212_author_source_reception/source_preparation_original/sections/05_scope.tex` and `SOURCE_PREP_MANIFEST.sha256` | Old 804-byte source/hash; original source package and source-preparation checks | Preserve forever as historical source. Create a distinct amended eight-file physical capsule; never replace this old original. |
| Initial plan: `p212_initial_build_preparation01/PLAN.md`, `SOURCE_GRAPH.json` | Eight raw-equal current/original pairs; `source_pins["sections/05_scope.tex"]`; `total_bytes=19659`; original source root and no-edit policy | New graph/role mapping must distinguish old historical original, proposed physical capsule and final live source. Old graph is not a new current-source graph. |
| Initial disabled proposal: `p212_initial_build_preparation01/BINDING.disabled.json` | `source_root` and all eight `source_pins` | Preserve disabled original. Any later actual build binding must use amended source bytes and separately completed runtime/build prerequisites. |
| Initial raw input lists: `p212_initial_build_preparation01/INPUT_PINS.json`; `p212_initial_build_source_audit01/ORIGINAL_PINS.json`, `INPUTS.sha256`; `p212_initial_build_source_root01/INPUTS.json` | Current05 and old physical05 both pinned to old bytes; whole packages pinned elsewhere | Old lists remain evidence at their own time. A current recheck needs explicit old-to-physical mapping, not replacing entries inside sealed lists. |
| Initial documentary checker: `p212_initial_build_source_audit01/inspect_source02.js` lines 101--110, 133--142 | Reads current and original under same graph pin, raw-compares, insists on 19,659 total and old original manifest | Its archived PASS does not assert equality after a manuscript change. Do not run it unchanged against amended live source or relax it in place. |
| Initial root reception: `p212_initial_build_source_root01/receive_audit.js`, `RECEPTION.md` | Accepted exact source graph, original native cmps, input sets | Preserve old acceptance; separately receive affected exact delta. The receipt expressly requires this before current Round0. |
| Frontier emitter and declarative data: `p212_build_dependency_source_preparation01/query_frontier.js`, `QUERY_FRONTIER.json` | Embedded `profile.source_graph_path`, `paper_root`, `source_pins`, `source_files=8`, `source_bytes=19659` | New complete profile bytes and exact source graph/capsule roles. New whole-file hashes follow even if all 19 contexts/53 proposals remain identical. |
| Frontier plan/checker: `p212_build_dependency_source_preparation01/PLAN.md`, `inspect_preparation.js` lines 35--44, 79, 104--116; `PREPARATION_RESULT.json` | Pins 28 originals, requires raw current/original equality, reconstructs emitter from complete profile, records old70-key and 19,659-byte result | Retain original plan/checker/output. An amended source receipt must disclose the old/new graph distinction and exact prospective data; do not retrospectively amend archived results. |
| Plan audit input surfaces: `p212_build_dependency_source_audit01/INPUTS.sha256` (75), `INPUT_PINS.json` | Includes eight current/eight physical sources and complete initial/frontier packages | Historical accepted audit remains scoped to old bytes. New changed-source applicability needs exact delta reception, not a rewritten old PASS. |
| Original driver source/preparation: `p212_dependency_query_driver_preparation01/driver.js`, `SOURCE_INPUT_PINS.sha256` (30), `STAGED_CAPTURE_AND_CLOSURE.md` | Fixed frontier hash and eight live hashes; contract explicitly prohibits silently reusing old profile pins after prose changes | Original driver and Major/open history remain untouched. Operative derivative is based on accepted revision02, not this superseded implementation. |
| Operative revision02: `p212_dependency_query_driver_revision02/driver.js` lines 20--23, 471--485, 903--908 | Whole frontier SHA `762645257c2bea4f1d5c081de471cdee9eeb2b00dd312aab48d7dd4ed59cad1f`; loop reads every `frontier.profile.source_pins` before `snapshot`/phase work | Future derivative must bind new exact companion paths/hashes while preserving all algorithm/context/ENV/body-read guards. Even contract-only entry must await final matching source and separate authority. |
| Fixed companion set: same driver's `OLD_COMPANIONS` | `QUERY_FRONTIER.json` plus `INTERFACE.disabled.json`, `CAPTURE_CONTRACT.json`, `SELECTOR_OBLIGATIONS.json` complete immutable hashes | Copy/preserve whole companions as explicitly selected; only justified content/path changes. Three nonprofile companion contents need not change solely for section05. A new driver hash requires new exact source reception. |
| Driver audit/delta pin sets | `p212_dependency_query_driver_source_audit01/INPUTS.sha256` (40), nested `context_contract/INPUTS.sha256` (17); revision02 `MATERIAL_SOURCE_INPUTS.sha256` (19), `REVIEW_INPUTS.sha256` (6), `SAME_REVIEWER_DECISION_PINS.sha256` (9); same-reviewer `INPUT_PINS.sha256` (40), `DELTA_ACCEPTANCE.json` | The six-input decision fixes revision02 SHA `57ce0d5815e3b0d051925dd351030d26067eb796a47f7058cf8f3a08c5e90032`. Retain that accepted decision as historical input; it cannot silently certify a changed driver/frontier. |
| Joint root receiver: `p212_dependency_source_root01/receive_source02.js` lines 96--132, `RESULT.json`, `close_source.js` lines 19--23, `RECEPTION.md` | Receives eight pin lists, four exact companions, raw eight-source pairs, 19,659 total and 150 rich inputs | Existing receipt authorizes no operation and names old exact bytes. The future changed-source receipt must follow exact amendment originals; do not re-run unchanged checker expecting old-source equality or alter old150-key output. |
| Outer supervisor WIP: `p212_dependency_query_outer_preparation01/outer_contract.py` | `DRIVER`/ `DRIVER_SHA=57ce...90032`; `RECEIPT` / `RECEIPT_SHA=d850...655ca2`; requires entire inner descriptors equal outer `BOUND`; controller references exact outer source | Author confirms unfrozen. Its final source must explicitly select the amended driver path/hash and the future accepted amendment receipt/authority. No prior or current draft hash is approval. |
| Outer preload WIP: `p212_dependency_query_outer_preparation01/node_preload.js` | Exact DRIVER path in argv, loader allowlist and final require-cache census; complete outer originals/inner binding | Coordinate same successor driver path before freeze; changed final source gets its own pin. No algorithm or query expansion follows merely from section05. |
| Future bindings, not observed files | Disabled driver fields `driver_pin`, `inputs`, `receipts.plan_source/driver_source`, `controller.outer_entry_source/outer_request_record`; outer `inner_binding`, `inputs`, four receipt roles and external nonself descriptor | All must bind the actually accepted successor source/companions/capsule/final-live roles before startup. No future destination was probed or assumed present/absent here. |

The seven-substitution `SOURCE_PROFILE_DELTA.json` names the same eight
filenames and unchanged article/plain/package roles; its filename-list
semantics do not change from prose alone. It still is only a historical
partial adapter specification. Source content, literal totals and all
transitive hashes cannot be treated as unchanged on that basis.

## Historical literal-hash inventory and limits

[LITERAL_HASH_OCCURRENCES.json](LITERAL_HASH_OCCURRENCES.json) enumerates every
one of the 76 files returned by the bounded exact-old-hash search over
`docs/papers211_215_sequence/qa` before this map existed. It includes
source/pin objects and archived native echoes; a text occurrence alone is not
an operative consumer. Files under author/runtime/canonical/strict-pair
receptions are preserved historical broad provenance. Changing prose neither
changes accepted scientific output nor makes old full-input maps current.
Where a later task needs such a map, distinguish the affected documentary
surface and retain the original historical referent; do not silently reuse a
changed whole key.

This is not a claim of arbitrary repository-wide dependency completeness or
an OS/runtime key. Direct source references were followed through the named
current initial-plan/frontier/driver/outer chain. Full code bodies were not
audited anew and no submitted program was run.

## Existing amendment boundary, not a new gate hierarchy

1. Preserve old05 and all sealed packages. Receive the exact proposed prose
   and unchanged seven-source identities; an independent reviewer must not
   be this proposal author.
2. Prepare one explicitly scoped successor physical capsule/profile/frontier
   and derivative driver, with complete literal diffs and fixed companions.
   Final live target and physical provenance roles must be separate, with
   no fallback from a stale live pin to a convenient capsule.
3. Coordinate the successor driver and receipt roles with the still-unfrozen
   outer source. Root's eventual source acceptance then controls exact live
   application and the already-required startup/binding boundaries.
4. Only after those existing prerequisites may any operation be considered.
   This map does not enable help/version, lookup, body capture, build,
   scientific execution, manuscript review or publication.

The original proposal and integration map are author-side work. The project
skill's change-sensitive verification rule drives this map; it does not turn
the map into an independent audit or create recursively expanding gates.
