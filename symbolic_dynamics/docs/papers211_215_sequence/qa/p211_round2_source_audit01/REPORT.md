# P211 Round2 infrastructure: independent source-only audit 01

Date: 2026-09-09 (task environment date). Auditor: /root/round211_finite_matching_scout.

## Decision and scope

**GO_SOURCE_RECEPTION_AND_BINDING_PREPARATION_ONLY. C=0 / M=0 / m=0 confirmed source-level findings. HOLD_OPERATIONAL remains.**

This is an independent infrastructure/source/provenance audit of the sealed preparation, not a P211 mathematical review, a runtime test, a freeze reception, or terminal acceptance. The auditor is not the author of these six operational programs and has not authored or mathematically reviewed the P211 manuscript. The preparation author discloses prior initial-build/freeze authorship and final-B reviewer status in the pinned lineage; no new scientific independence is inferred from that authorship.

The exact received preparation is [p211_round2_preparation01](../p211_round2_preparation01/HANDOFF.md): 22 payload files plus its seal, whose 1,998 bytes have SHA-256 `41a9e4a8203acee181b91e21e6985e521d43a1c303f7a697bfdb5d9306a60d21`. All 22 seal entries and all 164 original stable input pins passed independent native checks. Physical inventory contains exactly those 23 ordinary files and the one declared `terminal_build` subdirectory.

The scoped recommendation permits root to receive these exact source bytes and prepare new complete bindings. It does not grant execution authority or certify any future binding. All three received templates remain disabled and unmodified; future Round2, terminal QA, and execution directories were observed absent by the documentary checker.

## What was independently checked

All six new operational source files (1,674 lines; 92,209 bytes), all three disabled templates, HANDOFF, both plans, the freeze binding contract, the original infrastructure lineage, the three original root reception documents, and the accepted initial binding were read. The six original-to-new source diffs were freshly produced and completely read. Unchanged predecessor sections are covered through the complete new source plus complete exact diff, not a claim to have separately reread every predecessor file in a second full pass.

The source-only checks do not execute, import, AST-parse or compile submitted Python. An independently written [documentary JavaScript checker](audit_metadata.js) reads file metadata/JSON and compares bytes; it does not start children or write files. Its 924 documentary comparisons passed. The number is a metadata comparison count, not 924 runtime tests.

| Exact mapping | Independent observation |
| --- | --- |
| Round1 payload | 83 unchanged destinations and byte pins; 4,438,548 bytes; origins match the original Round1 source selection |
| Complete final B | All 39 original payload files plus B's own seal, unchanged under `review_b/`; 40 files, 6,079,604 bytes |
| Intended physical Round2 | Exact disjoint union: 123 payloads, 10,518,152 bytes; a future new outer seal makes 124 files |
| Terminal input selection | Exactly the same 9 live / Round1 / accepted initial-binding / prior-lock source pins; 20,508 bytes |
| Terminal templates | Identical except build number, corresponding exact cold output, and authorization build number; both disabled |
| Original accepted lock | Exactly 570,037 bytes, SHA-256 `1a879caa4d7bb68fd841e381f37d5ec3e31236ccd6c7b677dbd95492a92bbf87` |

Every intended source byte pin was independently checked without interpreting the manuscript or reviewer scientific content. The source manifests and full physical source tree inventories agree. All six preparation-native complete source stdout bodies equal current source bytes; all six independently reproduced complete diff stdout bodies equal the preparation's corresponding native originals, including their source headers.

All three complete inherited key JSON maps were parsed for every entry's prescribed layout and byte-pin schema: Round1 all-reads 2,255 entries (2,251 workspace / 4 host); Round1 all-external 2,164 workspace entries; whole-final-B root inputs 1,785 entries (984 workspace / 801 host). These are per-map counts, not a deduplicated host inventory. No host entry was dereferenced; schema census does not establish current host equality, current historical resolution, or complete reuse acceptance.

## Source guard assessment

1. **Freeze scope and physical provenance.** The recorder requires an enabled new root binding, the exact execution source/preparation/inventory pins, exact original source lineage, explicit accepted references, and the isolated Python/runtime/environment contract before the operational copy path. Three execution-directory input roles are fixed. Its source selection checks the complete 83+40 union, retained source seals, live-parent inventory and permitted metadata changes; copies target fresh paths, reject aliases/hardlinks, and are closed by byte/rich-metadata checks. The prospective native sequence has 32 live/Round1 byte comparisons, two copy commands, 123 source/destination byte comparisons and three manifest-check commands (160 native commands, of which 155 are byte comparisons); separate rich-metadata reads enforce source before/after equality. These are inspected prospective actions, not actions run by this audit. See [freeze.py](../p211_round2_preparation01/freeze.py).

2. **Complete inherited keys and mixed bases.** `resolve_original` and `inherited_keys` require every original key, not a sampled subset; per-map resolution key sets must equal their original sets. Workspace historical resolutions require the exact accepted physical byte pin and a bound acceptance reference. `HOST_SEPARATE_ROOT` is restricted to original non-workspace paths and a bound root precopy recheck reference. The six inherited mixed-base pin-list roles preserve original root-relative / absolute-host spellings; no copied-list rebasing is assumed. Markdown document origins and JSON schema/base/read-limit declarations remain explicit. Mandatory preparation and old Round1-execution external-tree inventories are checked. The declared five historical-tree empty-directory allowances are not a permission to invent a generic baseline. See the [binding contract](../p211_round2_preparation01/FREEZE_BINDING_CONTRACT.md).

3. **Host authority remains separate.** The recorder explicitly does not rehash the complete reused host key. It requires complete host-key/settings/precopy references and marks the postcopy complete-key/settings recheck pending separate root reception. Its result is not self-accepting and does not substitute a local recorder seal for root acceptance. This boundary is appropriate for the received source-only contract, but must remain explicit in the later execution receipt. Empty pending maps and null references are intentional disablement, not passed guard evidence.

4. **Exactly two fresh source-only builds.** The terminal builder admits build 1 or 2 only at its corresponding fresh `qa_final/cold_build_N`; validates the complete physical 124-file Round2 package and all nine selected-source pins; binds all five new adapter pins, all five actual predecessor adapter pins, the accepted initial binding, and the exact original lock. It constructs the expected new lock from the old lock allowing exactly `schema`, `status`, `code_observations`, and `terminal_derivation`, with host-key extension disabled; object equality rejects other changes. The old automatic dependency-discovery path is removed and the preparation helper is refusal-only. See [build_p211.py](../p211_round2_preparation01/terminal_build/build_p211.py) and [terminal PLAN](../p211_round2_preparation01/terminal_build/PLAN.md).

5. **Build closure is not terminal acceptance.** The existing owned-session/unknown-launch fail-closed behavior is retained; no native handle is not treated as a settled successful process, and unclosed cases must not acquire a successful seal. Exact ENV8, complete configuration/key snapshots, the three cold-cwd absence roles, nine source-only copies, native passes, diagnostics/font checks, all-page render retention, and end-of-build source/Round2 rechecks remain explicit. FLS records are not promoted into a mid-pass byte-consumption proof. Two-build comparison, diagnostic reception and actual all-page visual inspection are still root obligations; retained page files remain not viewed / not accepted by the source audit. See [build_core.py](../p211_round2_preparation01/terminal_build/build_core.py) and [launch_build.py](../p211_round2_preparation01/terminal_build/launch_build.py).

These conclusions are source inspection, not an execution proof of every branch. No new generic runtime discovery or baseline is requested by this audit.

## Required downstream gates

Before freeze execution, root must receive this exact audit and preparation, fill a **new** root-owned binding without editing any pending template, resolve every inherited original key at its correct physical version, bind all external tree/list/document/JSON roles and accepted references, and establish actual complete reused host-key and settings precopy checks. Exact operational source/runtime/tool pins and invocation must be bound separately.

After any future freeze, root must receive the whole physical 124-file package, native records and pre/post metadata, perform the separate complete host/settings postcopy checks, and issue physical Round2 acceptance. Only then may root separately bind and authorize the two exact fresh terminal builds with four-field-only lock adaptation and current cold-cwd settings. Both build originals, exact pair comparisons, diagnostics, and actual all-page views require final reception. This report grants none of those future acceptances.

## Evidence, diagnostics and limits

[NATIVE_READS.json](NATIVE_READS.json) retains 24 actual original read/shape/map request-result records. [NATIVE_DIFFS.json](NATIVE_DIFFS.json) retains six complete fresh diffs and the initial limited-output freeze diff, which was truncated and not counted as complete; the full-budget replacement is retained separately. Native diff exit 1 means actual source changes, not a failed scientific test. Combined outer displays also limited some complete read output; needed sections were reread or displayed to completion.

[NATIVE_CHECKS.json](NATIVE_CHECKS.json) retains four actual documentary requests/results, including all 924 independent comparisons and their actual byte pins. [INPUTS.sha256](INPUTS.sha256) pins the 187 external ordinary files (23 preparation + 164 original stable inputs); its base is the workspace root, unlike this packet's directory-relative nonself outer seal. The checker additionally read this packet's own retained diff file, which is covered by the outer seal rather than being mislabeled external.

An early informal source-line total accidentally included the 463-line batch index; this was corrected immediately before any finding and has no remaining effect. A further bounded third-eye delegation failed with the native response `collab spawn failed: agent thread limit reached`; no child was created and no extra review is claimed. These diagnostics are preserved rather than converted into passed evidence.

The project research skill's phase and artifact gates governed the audit: source-only authority was kept separate from execution, scientific review, physical freeze acceptance and terminal acceptance. No public/external mutation, specialist contact, Git operation, binding, operational copy/build/render, or P212 scientific/proof/review read occurred. Only this audit directory was written. No manuscript or preparation source was changed.
