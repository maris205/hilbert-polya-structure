# Exact future P211 Round2 freeze binding contract

This is a source/schema contract, not an executed binding or acceptance.
Every path in the freeze schema is workspace-root-relative unless a field
explicitly says absolute. Byte pins are exactly {bytes, sha256}; rich source
read records additionally preserve stat identity/metadata. Read freeze.py
fully; this prose does not replace its guards or the root's original reads.

## Initial root-owned execution state

The literal directory is docs/papers211_215_sequence/qa/p211_round2_execution01.
It must be newly created by separately authorized root placement and contain
exactly three ordinary files: freeze.py, BINDING.json and
ROOT_INVOCATION_ATTEMPT.json. Physical frozen_round2 and paper/qa_final must
both still be absent. Source preparation does not create any of them.

BINDING.json must have schema p211-round2-root-binding-v1, enabled true and
the actual root authority decision
AUTHORIZE_PHYSICAL_P211_ROUND2_FROM_ACCEPTED_FINAL_B. Its record references an
actual separately created root decision. It binds the exact prepared/executed
source bytes, complete preparation seal and inventory, actual accepted
Round1 source, and every required receipt role. Supplied pending null/empty
fields are deliberate blockers, not generic defaults.

The attempt JSON is exactly the dictionary enforced in main(): argv is
/usr/bin/python3.10 -I -S -B followed by the new absolute freeze.py,
--binding and new absolute BINDING.json; cwd is the physical workspace;
environment has only PATH=/usr/bin:/bin, LANG=C.UTF-8, LC_ALL=C.UTF-8, TZ=UTC;
stdin is subprocess.DEVNULL; source_pin and binding_pin name actual bytes.
No command is authorized just because its literal form appears here.

## Whole source, dependency and history resolution

external_inputs is a complete distinct list of physical_path/pin/roles rows
for immutable workspace files this invocation depends on. This includes
every selected external tree member, every acceptance/origin/version-map
reference, the entire preparation package, and all workspace referents of
the inherited keys and copied input pin lists. Outputs cannot be dependencies.

external_trees lists exact root/files/empty_directories/manifest and an actual
accepted_scope_reference. Nonself manifest membership is exact, including
the manifest itself as a tree member. There is no recursive catch-all
selection or ignored directory. The complete accepted R1 execution and
the whole final preparation are mandatory. Other actual dependency scopes
are separately explicit; inventories with unlisted empty directories fail.

inherited_input_keys contains exactly:

| Role | Actual immutable key | Entry interpretation |
|---|---|---|
| round1_all_reads | p211_round1_execution01/READ_INPUTS_AFTER.json | Direct bytes/SHA plus full original context |
| round1_all_external | p211_round1_execution01/EXTERNAL_REFERENCES.json | The original row's pin field |
| whole_final_b_root_inputs | p211_b_final_root/INPUTS.json | Direct bytes/SHA plus full original context |

Every original key entry must have exactly one resolution. All original
entries, including full rich fields, are preserved unchanged in
INHERITED_ORIGINAL_KEYS.json. Content re-resolution does not falsely claim
that a historical inode/time field describes a new physical historical copy.

Resolution rows have kind, physical_path and accepted_resolution_reference:

- WORKSPACE_FILE: the original logical spelling resolves inside the
  workspace, and the exact original byte pin equals a fully consumed
  external file. A changed physical location requires an actual accepted
  historical mapping. Never refresh an original hash to current mutable
  index bytes. Unchanged paths may have a null resolution reference.
- HOST_SEPARATE_ROOT: the original spelling is absolute outside the
  workspace and remains literal. The reference must be one of the actual
  complete root precopy rechecks. The recorder records the entire original
  row but does not claim to dereference all its host fields/settings.

The host_reuse_boundary requires complete_host_key_references,
accepted_settings_references and precopy_recheck_references, all nonempty
actual original references. Complete reused host-key rehash by the recorder
is false; a separate root postcopy whole-key/settings recheck is mandatory.
Root must actually check all imported code/data/parameters/canonical/settings,
full native/ELF/configuration/link/member fields and accepted build-key
dependencies—not merely hash a receipt whose prose says they passed.

The recorder's own smaller runtime set is a separate guard:
recorder_runtime_file_pins explicitly binds every selected resolved module/
mapping dependency before any native copy; observed imports/maps must be
covered. Native_tool_pins covers exactly cp, cmp, sha256sum and python3.10
under their source-declared absolute paths. The full before/after read
closure also includes every such actually read file. This is not an
OS-hermetic, transient-dlopen or child-wide runtime trace claim.

## Original pin-list and document semantics

pin_list_bases has exactly one row for every copied .sha256 input list.
For the current six lists, base is the workspace root; each original
absolute path keeps its absolute meaning. Every listed digest has a full
byte pin and one explicit resolution, with no duplicates or omitted path.
Do not execute sha256sum -c from the frozen destination on input-pin lists.
Only package SHA256SUMS manifests use directory-relative bases.

document_origins names every copied Markdown, its unchanged original
document path, actual accepted origin reference and complete ordered local
links. The bounded inline Markdown syntax is the accepted recorder's syntax;
unsupported reference links fail. Copied targets use the source inventory's
original-document map. External file and directory targets are explicitly
consumed and have accepted physical-resolution references. Directory links
have complete exact nonempty trees and no generic empty-directory waiver.

json_pin_bases names every copied JSON and records original_document, base,
accepted_origin_and_schema_reference and the actual scope_note. These are
metadata about already received native/scientific/result schemas. No generic
recursive JSON walk or destination rebasing constitutes semantic validation.
Root retains all original per-schema key and provenance obligations.

The 123 selection rows remain exactly those of INTENDED_INVENTORY.json:
83 accepted R1 payloads; B40 under review_b; no outer self row. R1's old outer
manifest is bound externally. The new outer manifest is newly generated
from sorted exact destination names only after 123 native/raw copy checks.
Unchanged inner A/B manifests are separately natively checked at their
own copied directories.

## Reception, failures and completion

The source uses exclusive creation, exact ordinary trees, whole original
and destination byte/metadata before/after closure, distinct destination
inodes and nlink=1. Only the live paper root's size, mtime, ctime and link
count may differ after adding the one literal frozen directory; every
descendant must remain unchanged. Existing frozen_round0/1 subtrees are
only literal prunes from live scope, not omitted external dependencies.

Each command retains actual argv/cwd/env/tool key, attempt timestamp, native
exit or explicit exception, complete available stdout/stderr and their
actual hashes. A timeout or unknown launch prevents success; no successful
seal is invented. Any partial attempt and partial Round2 remain for root
inspection, with no removal or resume path.

No root execution manifest is written by freeze.py. Root must first retain
the encompassing native tool/session/completion and raw streams, then build
and check the complete actual execution nonself manifest. Root/independent
reception must directly check original evidence and full host/settings
postcopy keys before an acceptance record. The child's success status is
only PHYSICAL_P211_ROUND2_CREATED_PENDING_ROOT_RECEPTION.
