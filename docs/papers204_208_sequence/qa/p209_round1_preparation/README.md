# P209 Round1 freezer preparation

Status: `PREPARED_NOT_EXECUTED`. No freezer invocation, scientific program,
build, comparison of scientific canonicals, review, accepted delta or Round1
was produced by this task. Root owns full source inspection, actual A-delta
acceptance/closure, later execution and its complete command/output receipt.
This preparer is the P209 manuscript author and is not a P209 reviewer.
Only infrastructure, artifact schemas and documentary metadata were inspected.

## Exact source provenance and current files

The complete current 156-line `qa/freeze_p209_round0.py` was read and copied
exactly to `original_snapshot/freeze_p209_round0.py`. Its SHA256 is
`95473c820d305410ae042eed50c288fef02244e6ab41234648db641f0dd7866a`.
Actual `cmp --` against both that live source and the immutable Round0
`FREEZE_ADAPTER.py` returned 0 with empty output.

The current `freeze_p209_round1.py` is 420 lines, SHA256
`e62f11c0eaed932c364fe2bd44f37cc9a92a4819739fc51d306f41c01a2b0096`.
`ADAPTATION.diff` is the full actual ordinary unified diff against the exact
original source: 29,725 bytes, expected diff exit 1, SHA256
`edb3ff8c8f5e2eb65daa69893d3a538939f6c69600bda08c05b24095cb9d873e`.
This is a disclosed role/acceptance/layout/dependency adapter, not a claim
that the two freezer implementations are identical.

`ACCEPTANCE_INPUT_CONTRACT.json` describes the required future root record;
it is explicitly a schema, not an actual acceptance record. Its current
SHA256 is `e44808e7a5ad6048a14777de2a884f879523a18a558b03c7c7be5c42f8f3257c`.
`PREPARATION_CHECKS.json` retains the actual source-copy/diff commands and
full static-only Python command/output. The freezer itself was not invoked,
including for a refusal-path test.

## Explicit core and manifest roles

The source is the exact 1,989 referents of
`papers/209-ordered-fibre-threading/frozen_round0/SHA256SUMS`, whose SHA256 is
`0f77871539b374027ab42910471cc74cefcd570e214a8242ac0a30c7a83e70ba`.
Each referent is copied directly to the same relative path in `frozen_round1`.
There is no recursive copy of the live paper and no nested `frozen_round0`.

This preserves all 1,985 author payloads, their inner manifests, the exact
`AUTHOR_MANIFEST.sha256` alias, `ROOT_ADOPTION.md`, and the historical Round0
`FREEZE_ADAPTER.py` and `FROZEN_LINK_MAP.json`. The author's original live
`SHA256SUMS` and alias retain SHA256
`9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e`.
Neither live file is overwritten or relabelled as a complete live-paper seal.
The live `PAPER_STATUS.md` and its frozen historical wording stay unchanged.
The complete live-author and Round0 sets are checked, not inferred from counts.

The new freezer is named `ROUND1_FREEZE_ADAPTER.py`; new metadata is
`ROUND1_PROVENANCE.json`. Those names do not overwrite historical core files.
The new root `SHA256SUMS` alone is the complete nonself Round1 manifest.
The old Round0 manifest is copied as an explicitly scoped ancestry anchor,
not represented as the new complete Round1 seal.

## Nine physical acceptance anchors

All paths below are fixed under the current batch unless stated otherwise.
The destination names are beneath `frozen_round1/ROUND1_ACCEPTANCE/`.
All sources must exist and match the actual measured root acceptance record
before any Round1 directory is created.

| Physical anchor | Original input and role |
|---|---|
| `ROUND0_CORE_MANIFEST.sha256` | Paper `frozen_round0/SHA256SUMS`; the 1,989 core referents only |
| `A_REVIEW_MANIFEST.sha256` | `reviews/p209_a/SHA256SUMS`; complete accepted A manifest, interpreted against its original review directory |
| `A_DELTA.md` | `reviews/p209_a/DELTA.md`; the actual new reviewer acceptance |
| `A_INITIAL_FINDINGS.json` | `reviews/p209_a/FINDINGS.json`; unchanged zero historical census, not current acceptance |
| `A_INPUT_PINS.sha256` | `reviews/p209_a/INPUT_PINS.sha256`; exact 1,989 Round0 payloads plus its manifest at workspace-relative paths |
| `ROOT_RESPONSE.md` | `P209_A_RESPONSE.md`; exact response actually accepted by A |
| `ROOT_DELTA_CLOSURE.actual.json` | `qa/P209_A_ROOT_DELTA_INSPECTION.actual.json`; root's actual audited acceptance |
| `ROOT_PAIR_MANIFEST.sha256` | `qa/root_replays/p209_a_strict/root_a_pair_01/SHA256SUMS` |
| `ROOT_LAUNCHER_MANIFEST.sha256` | `qa/root_replays/p209_a_strict/launcher_root_a_pair_01/SHA256SUMS` |

The complete accepted review and root pair/launcher trees are checked twice;
their full original-path/payload-hash mappings are retained in the new
provenance. They are clearly pinned external inputs, not wholesale nested
copies. Thus new A acceptance/finding sidecars are also covered by the final
review manifest without inventing a future filename or hash here.

Original A `FINDINGS.json` and `REPORT.md` remain immutable. In particular,
the old `INITIAL_REVIEW` phase and `NOT_YET_SUBMITTED_OR_ASSESSED` wording
do not have to change. Current acceptance and zero-open status are bound
through the new actual DELTA and measured root closure, not by rewriting
the initial census. Root must actually inspect those new records; a prepared
schema or an initial zero count does not establish current acceptance.

## Exact future root-acceptance schema

The fixed input is `qa/P209_A_ROOT_DELTA_INSPECTION.actual.json`. Root agreed
to emit it only after the actual original/delta/replay closure. Required
fields are described in full by `ACCEPTANCE_INPUT_CONTRACT.json`:

- `schema`: `p209-a-root-delta-closure-v1`.
- `status`: `ROOT_ACCEPTED_A_DELTA_ORIGINAL_CLOSURE_PASS`.
- `paper`: `P209`; `input_round`: 0.
- True `reviewer_delta_accepted`, `root_original_inspection_complete`, and
  `root_replay_closure_complete`.
- `current_open_findings`: 0; `unchanged_author_payloads`: 1985;
  `unchanged_round0_payloads`: 1989.
- `author_manifest_sha256` and `round0_manifest_sha256`: the exact existing
  author/Round0 digests stated above.
- Actual measured `review_manifest_entries`, `review_manifest_sha256`,
  `delta_sha256`, `findings_sha256`, `response_sha256`,
  `root_pair_manifest_sha256`, and `root_launcher_manifest_sha256`.
  `findings_sha256` binds the original historical census.
- `historical_input_aliases`: a list of exact rows described below.

No not-yet-existing acceptance hash is supplied by preparation. Extra root
fields may be retained, but they cannot substitute for required fields.
The freezer additionally checks the actual closed pair/launcher receipts:
two original-box runs, three completed raw comparisons, the existing A
canonical SHA256
`9dd6229968748e2caf0e3fe74b802603b6dc51f37704bdf098dbdfb969433b36`,
no canonical adoption, and complete seals. These are artifact checks of
root's actual execution, not new mathematical runs or a new reviewer.

## Historical dependency mapping and the known Git receipt

An alias row has exactly `original_path`, `sha256`, and `physical_path`.
Paths are absolute. The original path and old hash must be an exact external
dependency in immutable Round0 `FROZEN_LINK_MAP.json`. The physical file
must exist, be a canonical nonsymlink workspace path with the same bytes,
and have a complete nonself manifest in its parent directory. Duplicates,
unused aliases and changes outside that exact old key are refused.

Root identified one current documentary change. The exact known row is:

```json
{
  "original_path": "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md",
  "sha256": "af1754c9d6095c0f943b75fe7b9819ebd2b7c4db9609930ca7feccf2934786da",
  "physical_path": "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/central_lifecycle_p209_a/GIT_SYNC_RECEIPT.before.md"
}
```

This is an already existing historical mapping, not a future acceptance
record. Root's three-payload recovery package has manifest SHA256
`21c8b0fb99e1579d6af82d7da8926e1586715563d4607fbf8bc0727c59702ecb`.
Its full receipt and scope were read and all three payloads checked here.
The prior bytes were recovered by root from an actual pushed Git object;
preparation performed no Git command and does not call this an original-time
physical snapshot. Current static inspection found exactly this one mismatch
among the 132 historical external pins.

Each actually used alias is physically copied, ordered by original path,
to `ROUND1_HISTORICAL_ALIASES/NNN_original-basename`. For this one-control
case the file is `001_GIT_SYNC_RECEIPT.md`. The unchanged old link map remains
historical; the new provenance remaps the 243 core links to Round1 core or
these exact physical old-control copies. Copied control Markdown retains
its original document origin. Newly checked navigation targets are explicitly
not claimed to be historical target-body identities. The snapshot source,
its complete parent seal and the current original digest are separately pinned.

The precise payload rule is **2,000 + the number of actually used historical
alias copies**: 1,989 core, nine acceptance anchors, new adapter/provenance,
and those old-control copies. The currently known one-alias case is therefore
**2,001 payloads**. No future Round1 manifest hash is claimed.

## Preparation evidence and superseded prototype

Current static inspection actually passed, exit 0: Python AST parsing,
original source identity, standard-library-only imports, no dynamic code
execution or recursive tree copy, acceptance/link validation preceding first
target creation, nine explicit anchors, dynamic payload accounting and
preserved initial-census wording. Round1 was absent. The full command and
actual output are in `PREPARATION_CHECKS.json`; no freezer refusal path was run.

`superseded_pre_alias/` preserves the exact earlier 385-line source, full
diff, contract and static-check record. That unexecuted prototype assumed
zero physical historical aliases and incorrectly required changing initial
`FINDINGS.delta_status`. Both assumptions were corrected on root's explicit
instructions before sealing this preparation. Its earlier static PASS was
only a syntax/copy/control-flow result, not acceptance or a valid freeze.
No prototype created a directory or ran scientific code.

## Later root invocation and failure boundary

Root must first read all current source/diff/schema lines, verify this complete
preparation manifest, and complete actual A acceptance and root closure.
The following is a later command, **not executed by the preparer**:

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/frozen_round1/never_created_freezer_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_round1_preparation/freeze_p209_round1.py freeze-round1-after-accepted-a
```

Missing or inconsistent acceptance refuses before target creation. No existing
freeze is overwritten. Any partial-copy failure remains in its newly created
directory with failure facts and no inferred acceptance; source/root artifacts
are not rolled back or deleted. A complete seal is written only after all
copied bytes, mapped targets, original source pins and manifest sets pass.
If an error occurs after a seal exists, it is reported without mutating that
seal. Root must retain actual stdout/stderr/exit and independently close the
result before assigning distinct B.

Only the new Round1 directory can be written by an actual later invocation.
The live paper, historical author seal/alias, ROOT_ADOPTION, PAPER_STATUS,
Round0, accepted review and central indexes stay unchanged. This is an
unchanged-core adapter: a manuscript/scientific revision needs a separately
disclosed scope, not relaxed pins here. No runtime-replay validity, compiler
quality, page view, B acceptance or terminal completion is inferred from file
copying. The project research skill enforces these evidence and authorship
boundaries; external actions remain `OWNER_AMBER / HOLD_EXTERNAL`.
