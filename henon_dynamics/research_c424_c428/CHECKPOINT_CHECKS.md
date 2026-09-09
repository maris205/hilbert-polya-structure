# First-pass checkpoint: read-only verification receipt

2026-09-08 UTC. This is a research checkpoint, not a sealed release or
completed five-paper package. No mathematical program is rerun here.
The two actual mathematical executions and their independent scopes are
recorded in the AM1 author and review receipts.

## Scope and current receipt state

Final selected proof/certificate integrity, read-only Git preservation
and the prose-link check have now completed. The source and mathematical judgments are in
[ADMISSION_DECISIONS.md](ADMISSION_DECISIONS.md); a hash comparison is
not another mathematical review. There is no package manifest, PDF
build, formal Route-A evaluation, seal, commit, fetch or push in this
checkpoint workflow.

The link check covered the batch's Markdown prose, excluding fenced
code, indented code and inline-code spans, and the newly changed current
state prefix. It checks local path existence only, not full CommonMark
parsing, remote link availability or proof correctness. Earlier broad
matching treated an indented mathematical `[2](-4+3i)` as a link; that
false-positive was recorded and the matching scope corrected. It is not
an Adler mathematical failure.

The inherited eight untracked directories and prior sealed payload are
outside the write scope. The expected tracked modification is solely
the C424–C428 prefix of `../CURRENT_RESEARCH_STATE.md`; new batch files
remain untracked. Cached `origin/main` equality is not a fresh remote
state check. Actual outputs follow.

## Selected reviewed-byte integrity

Actual execution used `node --input-type=module`, Node `v22.22.2`,
`node:fs.readFileSync` and `node:crypto.createHash('sha256')`, with
explicit expected constants from the final review/admission records.
Fourteen files were checked:

- AM1 analytic proof, class theorem, finite contract, author script and
  exact result;
- AM1 independent script, exact result, substantive review and closure;
- Adler integrated theorem, smooth report, singular proof, reducible
  proof and whole-contract review.

The first diagnostic reported thirteen matches and one mismatch. The
coordinator had mistyped the **expected** AM1 result digest in the inline
check, omitting a `3`; the actual file digest still matched the existing
author and independent receipts. No payload was changed. That checker
set its process exit code to 1; the enclosing multi-command shell later
returned 0 from its last Git query, which is not counted as a successful
integrity check.

Only the failed comparison was repeated with the correct literal
`44ccf0f5d062587eb07d2837c455a9c3843c3ce0b9e0c8df033d2223d227196a`.
Its actual digest matched, the tool returned exit code **0**, and the
thirteen already matching comparisons were not rerun. Final outcome:
all fourteen selected reviewed bytes agree with their recorded versions.
This was a diagnostic transcription repair, not a mathematical failure
or rerun. The classification proof and all author/reviewer files stayed
unchanged.

## Git scope and whitespace

The actual read-only commands were `git rev-parse HEAD`,
`git status --short --branch`, `git diff --numstat --
henon_dynamics/CURRENT_RESEARCH_STATE.md`, and the complete scoped
`git diff`. HEAD is still
`2895b07238d4cef2ed35faaad251e4cfceb08ec1`. The coordinator inspected the
entire diff: only the new C424–C428 prefix and the preceding batch's
heading label change; its earlier body is untouched. The numstat is
35 added lines / 1 removed line.

Status has one tracked modification, that current-state file, the new
untracked `research_c424_c428/`, and exactly the same eight inherited
untracked directories. Nothing is staged. No Git write or new remote
query ran. A separately returned `git diff --check --
henon_dynamics/CURRENT_RESEARCH_STATE.md` completed with exit code **0**
and no output. This whitespace check does not claim to validate the new
untracked mathematical files or Markdown syntax.

## Prose-link and final documentation check

After `CHECKPOINT_DOCUMENTATION_REVIEW.md` was created and its author
stopped writing, the coordinator read that entire report. Its bounded
documentation-consistency conclusion is PASS with zero required changes;
it honestly identifies its earlier singular-proof authorship and does
not claim independent mathematical re-review or fresh hash computation.
Its statement that the prose scan was then pending is its dated cutoff,
now closed by the actual execution below. No retrospective report edit
or another documentation round is needed.

The coordinator then ran a single final `node --input-type=module`
read-only prose-link scan. It traversed all **34 batch Markdown files**
and the **one changed current-state prefix**, removed fenced/indented
code and inline-code spans, located Markdown prose links, ignored remote
schemes and anchors, resolved relative paths against each source directory,
and tested local path existence. Actual result, tool exit code **0**:

```json
{
  "check": "local_prose_link_existence",
  "batch_markdown_files": 34,
  "current_state_prefixes": 1,
  "checked_local_links": 124,
  "missing": [],
  "symlinks": []
}
```

This excludes broken local targets in that explicit prose-matching scope;
it is not full CommonMark validation or external-URL verification. The
present receipt update only records these actual results and closes its
pending wording; it adds no new prose-link target and changes no proof,
source, certificate or reviewed mathematical input. No mathematical or
PDF build was rerun. All required first-pass checkpoint actions are now
closed, while the five-paper research objective still lacks four contracts.
