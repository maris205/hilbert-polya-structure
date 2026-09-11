# Four-component run02 receiver — independent static review

Current reviewed root source: **425 lines / 29,214 bytes**, SHA256
`a8070d6ff76e5fe6de148d53b279fbea7d8ee5580b1a57208c7e66c1a6434df8`.
The [current source snapshot](receive_four_component02.after_root_corrections.py)
and [before-correction snapshot](receive_four_component02.before_root_corrections.py)
are both physically retained. The original snapshot is 29,026 bytes, SHA256
`68f656ddb94532224b85531f4b7a626f3169c8253cc37b0ddce82da48bbdbf7b`.
Root, not this reviewer, applied the corrections. No receiver, launcher,
checker or scientific program was executed or imported by this review.

The [initial actual static review](STATIC_REVIEW_BEFORE.actual.json) passed
70 conditions over 52 named documentary inputs, native exit 0
(`569ccb`). It reads all 20 actual wrapper payload files and decodes the two
complete compressed 3,266-key ledgers as data, without rereading their host
files or regenerating current host trees. The [complete native return](STATIC_NATIVE_RETURN_BEFORE.actual.json)
is preserved, including the exact source of the executed static-only checker.

The [current-source delta review](STATIC_REVIEW_CURRENT.actual.json) passed
10 conditions, native exit 0 (`ced873`); its [complete native return](STATIC_NATIVE_RETURN_CURRENT.actual.json)
includes the full inline static command and stdout. It proves complete raw
source equality after exactly the stated corrections, preserves the complete
source diff, and tests the corrected predicates against actual original data.
Only `main` and `original_native` changed between the two snapshots.
No current receiver execution or PASS is inferred from these static results.

## Corrections closed in the current root source

1. The native 20-item checksum output now joins with actual LF, not literal
   backslash followed by n. The old spelling would mismatch the actual
   `1c8942` output; the corrected spelling equals all 20 actual output lines.
2. The canonical read-map serialization now ends in LF. The old literal
   backslash-n suffix was internally reproducible but not the intended encoding.
3. The parent receipt now explicitly requires zero integer `new_reviews`,
   `p210_accepted=False`, `five_paper_acceptance=False`, and
   `owner=OWNER_AMBER`, in addition to its existing zero science/build/view checks.

These were pre-execution source corrections, not failed scientific runs.
The ordinary textual diff returned 1 because the snapshots differ; its full
content is retained in the current static result. The generic exception status
`FAIL_ROOT_WRAPPER_RECEPTION_NO_ACCEPTANCE` remains an explicit failure,
contains no old P208/P209 success identity, and does not grant acceptance.

## Actual schema, scope and count findings

- The actual outer session is 21492. Launch stdout is empty; PROGRESS01 contains
  one heartbeat, and completion contains five more plus the final JSON. All six
  heartbeat objects agree with the native record, owner 770811 and actual
  start/end interval. The root completion is integer native 0. Cleanup records
  the owned group ABSENT without a signal or unresolved probe.
- The actual successful wrapper seal is
  `7eda9f4c4452d3d1dc0656ca592cef8e7783a120ccada3fd671cc2238aaf6ebe`:
  20 payloads / 21 physical files. All 20 payload keys and the complete native
  checksum stdout were checked as documentary originals.
- Scoped group names and rich keys exactly match the recorded inputs:
  launcher preparation 6, component preparation 15, fixed inputs 54, root
  binding/current theorem index 3, adaptation inputs 75.
- The 3,266 known names equal the union of 3,134 runtime names selected from
  the existing recorded keys by the original discovery rules, 63 consumed early
  parent module/map names, and those five scoped groups. Overlap is intentional;
  these counts must not be added as disjoint groups. The current receiver still
  has to discover and hash the actual present host resources on execution.
- Both complete compressed ledgers decode to equal 3,266-entry rich-key maps,
  with exact canonical JSON/LF encoding, zero gzip mtime and matching metadata.
  Scoped and configuration BEFORE/AFTER data also agree.
- There are **13 declarations, 18 declared cases and 14 actually used alias roles**.
  All used roles have the exact allowed original-path/hash/case → physical-path
  mapping. Four unused lifecycle cases are listed in the static result; they are
  neither undeclared aliases nor missing rows.
- The actual child result is 10,270,582 checks / 142,784 reread file keys,
  with 20 child raw comparisons and 6,312 local links. This review receives that
  exact original result and never re-expands its 142,784-key work.
- The receiver itself prescribes **13** complete Python raw comparisons:
  two executed-source copies, three wrapper BEFORE/AFTER byte pairs, and eight
  unchanged selector/contract copies. This is separate from the child's 20,
  and neither count denotes new native cmp commands.
- Failure preservation has 53 original input pins and eight exact unchanged
  copies. The original failure remains native 1 at 8,940,156 completed checks,
  caused by the typed `explicit-frozen-link-map` role being treated as a path.
  No prior failure or snapshot is rewritten or relabelled PASS.

No additional concrete field/membership/comparison mismatch was found in the
current `a807…` source within this bounded review. The accepted old receiver's
runtime/configuration helpers are retained; the actual launcher source was read
completely. The static findings do not substitute for root's full current-source
read, actual receiver execution, current 3,266-key revalidation or final return.

No root source, run02 output, failed run01, prior preparation, central control,
paper or frozen tree was modified by this reviewer. P210 acceptance and first
exact-five acceptance remain separate. `OWNER_AMBER / HOLD_EXTERNAL` remains.
