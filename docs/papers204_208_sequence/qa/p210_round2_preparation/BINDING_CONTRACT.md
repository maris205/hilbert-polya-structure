# Actual final-B binding contract — interface only, currently unbound

This document is a required interface, **not** a reviewer decision, root
closure, existing final schema, execution receipt or permission to freeze.
There is deliberately no `FINAL_B_BINDING.json` in this preparation.
Neither source was executed even to test a refusal path.

Only after the same actual B accepts its precise response and root completes
final original/replay closure may root write a separate physical
`FINAL_B_BINDING.json` under the batch QA directory, outside this sealed
preparation. Its exact SHA256 and this preparation's independently checked
seal are explicit command arguments. The writer refuses missing/mismatched
binding or any failed semantic/key gate before creating Round2.

## Actual role pins, not predicted B filenames

The binding has the interface identity fields `schema`
(`p210-round2-actual-final-b-binding-v1`), `paper` (P210), `bound_by`
(/root), and `status` (`BOUND_AFTER_ACTUAL_B_ACCEPTANCE_AND_ROOT_FINAL_CLOSURE`).
Those required values describe the state root must actually establish;
this contract does not assert that it has occurred.

`roles` has exactly the following thirteen keys. Every value is exactly
`path` (absolute), `sha256`, and `bytes` (actual positive integer, at most
4 MiB). All files must be physical regular workspace files. The four
unspecified B-final/history filenames below are selected from actual files
inside `reviews/p210_b`, not invented here.

| Role key | Required actual source | New physical anchor under ROUND2_ACCEPTANCE |
|---|---|---|
| round1_manifest | Existing frozen_round1/SHA256SUMS | ROUND1_CORE_MANIFEST.sha256 |
| review_manifest | Actual final reviews/p210_b/SHA256SUMS | B_REVIEW_MANIFEST.sha256 |
| accepted_delta | Actual accepted B delta Markdown file | B_ACCEPTED_DELTA.md |
| initial_findings | Unchanged reviews/p210_b/FINDINGS.json | B_INITIAL_FINDINGS.json |
| current_findings | Actual accepted current B census JSON | B_CURRENT_FINDINGS.json |
| review_input_pins | Unchanged reviews/p210_b/INPUT_PINS.sha256 | B_INPUT_PINS.sha256 |
| response | Actual accepted batch P210_B_RESPONSE.md | ROOT_B_RESPONSE.md |
| root_final_closure | Separate actual root-final JSON under QA | ROOT_B_FINAL_CLOSURE.json |
| root_pair_manifest | Existing root_replays/p210_b_strict_pair_01/SHA256SUMS | ROOT_B_PAIR_MANIFEST.sha256 |
| prior_whole_manifest | Actual current paper PAPER_MANIFEST.sha256 | PRE_ROUND2_PAPER_MANIFEST.sha256 |
| prior_lifecycle | Actual current paper ROOT_LIFECYCLE.md | PRE_ROUND2_ROOT_LIFECYCLE.md |
| initial_review_manifest | Actual physically preserved initial B seal | B_INITIAL_REVIEW_MANIFEST.sha256 |
| initial_delta | Actual physically retained initial B DELTA.md bytes | B_INITIAL_DELTA.md |

The binding itself becomes the fourteenth small physical anchor. Combined
anchors are capped at 16 MiB; root evidence or host inventories are not copied
recursively. The actual final review manifest count is supplied separately as
`review_manifest_entries`, greater than407 and no more than10000. It is
not a guessed final count; every declared row and physical member is checked.

Manifest bytes retain their original referent bases, never the new anchor
directory: ROUND1_CORE_MANIFEST uses frozen_round1; both B review manifests
use reviews/p210_b (the initial one applies only its explicit DELTA history
role); ROOT_B_PAIR_MANIFEST uses root_replays/p210_b_strict_pair_01;
PRE_ROUND2_PAPER_MANIFEST uses the original paper directory; B_INPUT_PINS
uses the workspace root and names the actual reviewed Round1, not Round2.
The source checks these literal bases directly. The whole-paper role also
records its original base and all prior referent pins in new provenance.

The exact initial407 seal, initial findings/delta, Round1 seal and root
strict-pair seal are fixed from already existing originals. Accepted delta,
current census and final seal must differ from their initial pending versions.
The actual no-change response requires the other406 initial payloads,
including FINDINGS, to remain at their original paths. Accordingly,
`initial_review_aliases` is an object allowing only the `DELTA.md` key,
whose value is its exact physical review-relative retained path. No path
guess or scientific/runtime/Round1 alias is allowed. The initial seal's
physical path is supplied through its separate role above.

## Literal selectors into actual future-final originals

`selectors` maps the following26 semantic names to nonempty arrays of
literal JSON string keys/integer indices. No expression, code, callback,
automatic key search or source import is supported. The names below belong
to this adapter interface; they do **not** prescribe fields in B's or root's
actual output schemas.

The five `reviewer.` selectors read only the actual `current_findings`
role:

- `reviewer`: actual reviewer identity /root/p210_b_reviewer.
- `accepted_delta`: the actual accepted-state value supplied in
  `reviewer_acceptance_value` (true or a nonempty actual acceptance string).
  Root must verify that this value denotes actual acceptance of the exact
  response, not initial PASS_NARROW or pending status.
- `open_critical`, `open_major`, `open_minor`: integer zero each.

The twenty `root.` scalar selectors read only the actual
`root_final_closure` role:

- `paper`, `input_round`: P210 and integer1.
- `reviewer_delta_accepted`, `root_original_inspection_complete`,
  `root_replay_closure_complete`: actually true.
- `current_open_findings`: integer0.
- `unchanged_author_payloads`, `unchanged_round1_payloads`,
  `initial_review_payloads_preserved`: 489,508,407.
- `author_manifest_sha256`, `round1_manifest_sha256`: the fixed original seals.
- `review_manifest_entries`: the actual supplied complete final count.
- `review_manifest_sha256`, `delta_sha256`, `findings_sha256`,
  `current_findings_sha256`, `response_sha256`,
  `root_pair_manifest_sha256`, `prior_whole_manifest_sha256`,
  `prior_lifecycle_sha256`: the corresponding actual role hashes.
  `findings_sha256` specifically means the unchanged initial B findings.

The final selector, `root.evidence`, selects an actual root-evidence
absolute-path-to-SHA256 object with at least two entries. Every referent is
hashed; neither binding nor final closure may evidence itself. This reads
explicit evidence files, not nested host-key paths inside their JSON.

All comparisons are type-exact. The actual accepted delta Markdown must
also name the exact accepted response SHA256 and contain acceptance wording.
The binding is an explicit root attestation/mapping after original inspection;
a matching selector or digest alone is not a new manuscript review.

## Known Markdown origins

`markdown_origins` has exactly four keys: `accepted_delta`,
`initial_delta`, `response`, `prior_lifecycle`. Values are absolute
semantic source-document paths. The initial DELTA keeps its known original
`reviews/p210_b/DELTA.md` origin, not the later history directory.
The accepted DELTA uses its actual source path, or that same explicitly
documented original DELTA origin. Response and lifecycle use their actual
fixed source paths. No arbitrary prefix substitution is accepted.

The writer migrates all71 original Round1 link occurrences from their
already-recorded physical target roles. Only targets actually inside Round1
move to the corresponding copied Round2 core. External targets remain exact
old pinned files. New anchor targets are resolved at the known origin,
must be actual workspace files, and select a copied core/anchor only through
an exact (source path, current digest) role. No missing-link skip or generic
historical alias is provided. Unsupported actual final link layouts must be
inspected and explicitly revised before any execution.

## Native completion consumed by the later physical receiver

After a real root freezer command, the independent receiver additionally
requires the actual root completion file and explicit SHA256. Its documented
native envelope is `result.exit_code` plus the complete `result.output`
JSON string, matching the actual prior root recorder convention. Root must
store the real tool/native return there, not construct a success from the
expected524/525 counts. No such future completion exists in this preparation.

Missing now: actual same-B accepted delta/current census/final seal and exact
initial-history roles; actual root final closure and its field selectors/
evidence; root-written actual final binding; actual native freeze completion.
The submitted response and successful root strict pair do not fill those
remaining gates by themselves.
