# Exact source-defined reconstruction recipe

## Controlling originals and output boundary

The accepted source is ../five_paper_terminal_gate_revision_01/four_completed.py:
715 lines, 40,576 bytes, SHA256
0d84acf3034af513bd57227d626e227c3f3d7d8462859c8678943d2da517f399.
Its run02 executed copy has the same bytes. The preparation seal is
3863616519c14cc2f70d92deced93d745978a34f7e90f78aed5f00dd12ca8238.

The actual child ../five_paper_terminal_component_run_02/checker.stdout has
5,733 bytes, SHA256 dade493f165bbc3c5f9b09233ec34215f0ec75199c3b26642513318327057b76.
It reports 10,270,582 checks and 142,784 file keys, but saves only their
SHA256 087b90f42ad1a55fef4daa2acb29cee4fca614736c862aa9aed5e2a65d628dc0,
not the full map. Its parent KNOWN_INPUTS_BEFORE/AFTER.json.gz each contain
3,266 keys and cannot replace the child universe. Those parent rows are
useful only as records for overlapping, independently selected paths.

## Source selection and cumulative counts

Counts below come from the actual independent data-only probe. They are
cumulative counts in this stated order, not disjoint package sizes.

| Phase | Complete selected-path count |
| --- | ---: |
| Preparation, fixed roles, aliases, selector sources | 140 |
| Completed-paper, frozen and review manifests/input roles | 19,074 |
| Six strict supplemental pairs | 22,547 |
| Four supplemental builds | 138,145 |
| P208/P209 reuse originals | 140,996 |
| P205 artifact/links | 141,005 |
| P207 artifact/links | 141,165 |
| P208 artifact/links | 141,547 |
| P209 artifact/links | 142,784 |

1. Follow main and verify_four: include the 14 preparation payloads plus seal,
   every REVISION_PROVENANCE input, ROOT_REUSE_BINDING, the 54 fixed inputs,
   all declared alias physical files, current_index, KEY_SELECTOR_PROVENANCE,
   LINK_PARSER_PROVENANCE and their explicitly named original sources.
2. Follow completion_artifacts: include four whole-paper manifests and all
   members, the three separately declared artifact packages, twelve physical
   freeze manifests, eight final review manifests, all eight INPUT_PINS.sha256
   workspace-relative members, scientific/frozen pins, censuses/deltas and
   preserved P204/P206 rejection roles. A manifest includes its own physical
   seal as an input and all declared nonself payloads.
3. Follow supplemental_pairs: for each of the six declared strict pairs,
   include its full package, INPUTS_BEFORE/AFTER rows, RESOURCE_NAMES and
   CONFIGURATION originals, each configuration file row, RESULT, producer,
   canonical and the two original verifier stdout files.
4. Follow supplemental_builds: include the full four-build package, both
   KNOWN_INPUTS gzip files and metadata; select every file row in all three
   decompressed groups. Group sizes are configuration 1,875 (1,760 files),
   runtime 3,095 (3,091 files), and tex 118,878 (113,733 files).
   Include ORIGINALS, LIBRARIES and CONSUMED_TEX before/after maps, source-only
   initial maps, both cold-source/PDF roles, exact page-view frames and the
   separate actual view record. The source selector's raw /usr/bin/ldd read
   is also a key. Directories and absent paths are state/membership, not files.
5. Follow reuse_208_209: include reuse result/native/output package,
   INPUT_PINS fixed inputs (128), six accepted packages, and all forty original
   ledger before/after pairs. Determine each interval's unique pair/build case
   from its declared package/launcher roots before applying exact role aliases.
   Include six pair and two build package closures, configuration originals,
   named runtime/interpreter/parent/user-root metadata and exact source/PDF/view
   roles. No old reuse program or selectors are run in this preparation.
6. Follow lifecycle_keys_and_links: P207 original/lifecycle each contribute
   1,197 ledger rows; P208 contributes 115,334 original and 115,403 lifecycle
   rows; P209 contributes 132,356 original and 132,377 lifecycle rows.
   Their field is all_consumed_inputs_rechecked except P208/P209 lifecycle,
   which uses all_current_read_inputs_rechecked. These six ledgers have only
   sha256 and bytes. P205's terminal result has no such complete ledger.
   Also include every complete_nonself declared manifest, its seal/members,
   every referenced original document and its resolved link targets.

The actual probe uses 93 distinct manifest bases and 180 calls to its explicit
JSON-metadata reader. The latter is not a total count of all files opened:
manifest text and Markdown reads are separate. It selects Markdown in the
four paper trees and eight review trees from their accepted full-manifest
.md names; it does not use rglob or a host inventory in this diagnostic.

## Link semantics are part of selection

First process the original artifact link rows, then every paper/review Markdown
document selected by the accepted full manifests. A ledger-only or recorded-link-
row-only union misses further documents and targets.

P205 removes /frozen_round[012]/ from each frozen document's logical origin.
P207/P208/P209 use the accepted per-document semantic_origin. P208/P209 retain
the exact modern parser exclusions for fenced, indented and inline code.

P209 initial artifact links marked explicit-frozen-link-map are typed roles,
not filesystem origins. Reconstruct them from FROZEN_LINK_MAP.json and
ROUND1_PROVENANCE.json / ROUND2_PROVENANCE.json: 243 + 259 + 298 = 800
occurrences, 779 unique rows, 71 documents. Apply the accepted initial
explicit_historical_aliases_used entry for each exact original target and
digest, then select that physical target. Never treat the semantic-origin
label as a pathname or apply a generic fallback.

An old documentary substitution is keyed by the full triple
(original absolute path, expected digest, case). Select the declared physical
file only for that role. Do not change unrelated current/scientific/runtime
paths sharing the original pathname.

## Rich map and membership remain a formal execution obligation

The accepted measured() file row is exactly
{sha256, bytes, resolved, symlink}, with symlink equal to raw readlink text
or null. Its key is the selected lexical absolute pathname, not automatically
the resolved pathname. Whole-map serialization is sorted compact JSON with
separators comma/colon and one terminal LF.

The four-build grouped snapshots use boolean symlink plus a separate link
field: when deriving a file-row candidate use link, not that boolean.
Keep complete recorded state schemas separately for directories, absences
and configuration. Original intervals have mixed two-, three- and four-field
schemas; do not assume every row is a complete measured() row. The probe's
partial/rich row counts are coverage diagnostics, not a validated old map.

The original READS includes every direct pin/raw input, manifest seal/member,
state file and link destination. STATES, TREES and MEMBERSHIPS are separate
obligations. A future actual exact-five execution must retain the exact
resource/configuration/TeX selector rules and before/final membership checks,
perform measured reads for the precise selected file universe and check its
full rich-map digest using only disclosed old documentary roles.
The current preparation does none of those host dependency checks.
A matching count alone must not be labelled rich-map equality or PASS.

## Exact old current-index role

Original absolute path:
/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md

The run02 parent before/after maps record:
sha256 329cb32f4764dd59b1a500a8c21ef7dd4b2d83c87dd781d9934a413142f2a914,
bytes 28714, resolved equal to that original path, symlink null.

The actual preserved physical file is:
/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/central_round2_p210/FINAL_THEOREM_CONTRACTS.md

central_round2_p210/PRESERVATION.actual.json records equal before/after/copy
pins and actual native-zero cp and cmp commands. The main source-reading
agent independently read the exact record and rehashed this named 28,714-byte
physical copy. This is run02's historical current_index role, not one of the
older declared FOUR_INPUTS alias cases. To reconstruct the historical digest,
retain the original key and resolved metadata while verifying its exact
preserved bytes separately. Current theorem-ceiling checks remain distinct.

The earlier version is instead SHA256
baa278de72e8d82075c094ec05e95118c3794057cbb70430a6c7f363b621059c,
17,599 bytes. Its three actual cases are:

- p208_a: qa/p208_round0_input_inspection_v2/historical_workspace_origins/docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md
- artifact_p208_initial and artifact_p208_lifecycle:
  qa/central_lifecycle_p209_20260907/before/FINAL_THEOREM_CONTRACTS.md

Those case-sensitive roles remain unchanged and cannot stand in for the
run02 329cb32f... current-index role. There is no generic current-index waiver.

## Preservation and authorization boundary

The saved probe source is exactly the previously executed inline source.
The saved native record includes the whole command, launch and both subsequent
native returns; exact stdout is also materialized without reformatting.
This package was written later with apply_patch at root's explicit request.
The separately saved current anchors are not contemporaneous execution pins.
No accepted historical source, receipt, failed evidence, paper, lifecycle,
central index or Git state was modified. OWNER_AMBER / HOLD_EXTERNAL.
