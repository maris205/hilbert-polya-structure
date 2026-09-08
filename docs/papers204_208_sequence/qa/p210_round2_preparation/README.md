# P210 Round2 — sealed-source preparation, not a freeze

**UNBOUND / NOT EXECUTED / NO ROUND2 OR P210 ACCEPTANCE.**
This preparation adapts the already accepted441-line Round1 freezer and the
actual separate169-line `qa/inspect_p210_round1.py`. The latter is not in
the old preparation directory. No old program, new freezer/receiver, or
refusal path was imported or executed. `OWNER_AMBER / HOLD_EXTERNAL` remain.

The [external final-B binding contract](BINDING_CONTRACT.md) is an interface
only. No FINAL_B_BINDING.json or future PASS record is created here. The
current task permits useful source/data preparation while the actual B
decision and root final closure remain separate. The submitted no-change
response is not acceptance of itself.

## Exactly one carried core, small real anchors

[The freezer](freeze_p210_round2.py) has487 lines,31,719 bytes, SHA256
`781ac952b7de74947c202aa021f95a90a05dc496c430bd701da6538675c0316f`. Twelve original read/manifest/raw-copy/scanner
helpers are AST-identical. Four existing functions change, four are added
and three A-specific gates are replaced. `write_new` changes only its
Round1/2 diagnostic wording. [The complete669-line source diff](FREEZER_SOURCE_DELTA.diff)
discloses the actual change; it is not described as a five-constant adaptation.

[The separate physical receiver](inspect_p210_round2.py) has333 lines,
21,317 bytes, SHA256
`3d85e59cef7c4b33c66bedf5ea3f05bb6042ea7e7a2560ba7c3883bd4c766754`. All eight original read/manifest/native
helpers are AST-identical. Only its existing main changes; four bounded
binding/link helpers are added. See [its complete343-line diff](RECEIVER_SOURCE_DELTA.diff).
It never imports the freezer.

Existing Round1 really has508 payloads/509 physical files, seal
`be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0`.
Its core totals88,483,763 bytes. The future plan is exactly:

- Copy all508 Round1 payloads **once**, retaining all489 author bytes,
  earlier maps, A anchors, earlier freezer source and provenance unchanged.
- Add13 small actual B/initial/root/prior-live role anchors plus the actual
  externally supplied binding itself:14 anchors, at most16 MiB combined.
- Add this executed freezer's source identity and one new provenance JSON.

That gives524 nonself payloads/525 physical files, not an existing output.
The separate receiver would compare all523 source/copy byte pairs directly,
verify exact complete memberships/inputs, rebuild every carried/new link,
and run five manifest checks plus one raw author-manifest comparison.
Those six anticipated native commands are not new science.

Neither source recursively copies the paper, entire B package, runtime,
host-key inventory or TeX trees. Existing final B/59-file root-pair package
members are checked as files; nested120k host-ledger paths are not expanded.
The disk gate counts this one core copy, actual anchor/source bytes and
32 MiB metadata/failure margin before any target mkdir. Baseline free space
was approximately824.6 MB; that observation is not a promise of future space.

## Existing data actually checked

[BASELINE.actual.json](BASELINE.actual.json) preserves the actual standalone
read-only command and complete native exit0 return at2026-09-07 17:02:16 UTC.
It checked the entire508-file Round1, initial407-file B and59-file root pair,
all71 carried Markdown link occurrences and their actual current targets.
It did not execute project code. B's actual recorded baseline was still
INITIAL_PENDING_ROOT_RESPONSE, accepted_delta=false, root_response_reviewed=false.

[INPUT_PINS.json](INPUT_PINS.json) contains20 existing immutable direct keys.
The observed old live lifecycle/whole-manifest hashes in the baseline are
not frozen as future-current values: the final actual binding must supply
the then-correct pre-Round2 documentary roles. B final/history filenames,
accepted count and JSON field selectors likewise are not predicted.

[STATIC_CHECK.json](STATIC_CHECK.json) records the separate actual
parse/compile-only, exact AST/diff, input/package/link and raw-existing-byte
checks. It is not a run of either entrypoint, a behavioral refusal test,
a final binding preflight, new science or paper acceptance.
[PROVENANCE.json](PROVENANCE.json) records scope, authorship and exact changes.

## Preservation and failure behavior

All real binding semantics, zero-open counters, exact accepted response,
complete initial407/final B and original59 pair roles, unchanged author/core,
complete1496-entry old whole manifest, every link and disk-space gate precede
the first TARGET.mkdir. Only an initially absent physical frozen_round2 is
permitted. Copies use exclusive creation and complete Python bytes equality.
The initial DELTA alone may use an exact supplied B history path; the other406
initial payloads, including FINDINGS, stay at their original paths, as the
actual no-change response requests.

The old Round1 map is historical data, not the current whole-paper map.
Its71 roles are migrated individually; no generic origin or alias heuristic
is introduced. The new pre-Round2 ROOT_LIFECYCLE and PAPER_MANIFEST are exact
physical anchors with their original PAPER-relative referent basis.
No live lifecycle, whole manifest, review, freeze or control index is edited.
Root must finish physical reception before a later live lifecycle/whole update.

Failure before creation writes no target. Partial new output after creation
is preserved with an exclusive ROUND2_FAILURE.json if no seal exists.
Nothing is rolled back, deleted, overwritten or automatically retried.
A failure after a seal leaves that sealed tree untouched. The receiver's
actual failed commands/known keys remain in its full native failure output;
an output directory alone never proves success.

## Future root commands — disabled until actual binding

After actual B acceptance/root closure, root must independently inspect all
source/originals/seals and supply real values for every placeholder below.
These are command shapes, not execution records. Both use cwd
`/root/autodl-tmp/symbolic_dynamics`, exact ENV4 and system Python3.10.

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC \
  /usr/bin/python3.10 -I -S -B \
  -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/210-weakly-increasing-run-aggregation/frozen_round2/never_created_freezer_cache \
  /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_round2_preparation/freeze_p210_round2.py \
  freeze-round2-after-accepted-b --final-b-binding ACTUAL_ABSOLUTE_FINAL_B_BINDING_PATH \
  --expected-final-b-binding-sha256 ACTUAL_BINDING_SHA256 --expected-preparation-sha256 ACTUAL_PREPARATION_SHA256
```

Only following that actual successful native command:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC \
  /usr/bin/python3.10 -I -S -B \
  -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_round2_root_reception/never_created_receiver_cache \
  /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_round2_preparation/inspect_p210_round2.py \
  inspect-round2 --final-b-binding ACTUAL_ABSOLUTE_FINAL_B_BINDING_PATH \
  --expected-final-b-binding-sha256 ACTUAL_BINDING_SHA256 --expected-preparation-sha256 ACTUAL_PREPARATION_SHA256 \
  --freeze-completion ACTUAL_ABSOLUTE_NATIVE_COMPLETION_PATH --expected-freeze-completion-sha256 ACTUAL_NATIVE_COMPLETION_SHA256
```

The receiver only creates the initially absent
`qa/p210_round2_root_reception`; no other output path is accepted.
Root preserves actual outer commands, complete native streams and exits.
The receiver is documentary/physical integration, not an independent B review.

The symbolic-dynamics skill determined the actual-acceptance phase gate,
exact dependency-sensitive adapter, failed-history preservation and external
hold. An attempted bounded independent helper allocation hit the thread limit;
no additional independent review is claimed. One combined exploratory diff
display was truncated, then replaced by complete exact diff artifacts and
bounded checks. No truncated display is claimed as a full review.
The first static command actually failed because the saved freezer diff
omitted one trailing blank context line; its complete native exit1 remains
in [STATIC_DIAGNOSTIC_01.actual.json](STATIC_DIAGNOSTIC_01.actual.json).
Only the unsealed diff artifact was corrected to exact difflib bytes; neither
487-line freezer nor333-line receiver changed. The separate final static
command checks the corrected diff and all declared data, not a relabelled
first attempt.

All-size theorem limits remain unchanged. Physical Round2, terminal source-only
build pair, actual every-page views, complete P210 artifact closure and the
first exact-five terminal gate remain distinct obligations. No Git or external
action was performed here.
