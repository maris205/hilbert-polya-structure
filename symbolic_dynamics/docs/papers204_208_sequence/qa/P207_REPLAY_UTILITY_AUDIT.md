# P207 root-replay utility — actual code audit and accepted delta

2026-09-06 UTC. Utility auditor: `batch197_fifth_scout`.

**Outcome:** the concrete utility issues below were communicated to root,
root implemented the scoped changes, and the auditor accepted the actual
controlled replay's utility/dependency evidence after a read-only delta
check. This acceptance is **not** a P207 mathematical verdict, manuscript
Review B, accepted manuscript delta, or terminal paper acceptance.

This document is the auditor's only workspace write for this task. Root
owns the utility edits and both actual replay pairs. The auditor did not
execute the P207 author or reviewer checker, did not write their outputs,
and did not modify either replay directory or either review package.

## Scope and original inputs

The audit used the full [artifact-role contract](../ARTIFACT_CONTRACT.md)
and [project workflow](../../research_state/WORKFLOW.md), the original
and revised root utility, and the actual root replay receipts. It checked
A's canonical top-level schema and status/count fields, manifest names,
and directory/file-name coverage only. It did **not** inspect P207's
manuscript mathematics, proof package, A checker implementation,
claim-by-claim review, or finding contents.

The inspected canonical schema has `status` as a string, equal to `PASS`,
and `assertions` as an integer, equal to 1,326,321. These are parser and
execution-record fields, not an independent mathematical validation.

During the first inspection A's final manifest had not yet appeared.
After its actual seal, the name-only check found 118 directory-relative
nonself entries, no duplicate/missing/extra names or absolute/parent
escapes, and 106 input-pin names all under the expected physical Round0.
The separate context pin-list contains 10 referent names. The initially
absent final manifest was a sealing-stage observation, not a persistent
finding. Absence of a manuscript DELTA at that initial-review stage was
also not treated as an error or filled with an empty template.

## Initial concrete issues and root's response

Line references in this section refer to the preserved
[old utility snapshot](root_replays/p207_a/harness_input.py), not to
renumbered lines in the revised live utility.

| Initial issue | Concrete effect and audit boundary | Implemented response and follow-up check |
| --- | --- | --- |
| Lines 46–49 inherited unrecorded Python settings | `PYTHONOPTIMIZE` and user-site settings were not neutralized by `-B`/safe-path alone. This was a reproducibility risk, not a claim that the old A pair actually ran with optimization. | Runs and the runtime probe now use `-I -B`; the probe requires optimize 0, enabled assertions, isolation, no user site and ignored Python environment. The controlled receipt records the flags and a successful probe command. |
| Lines 62–63 checked dependencies only before the pair | The actual context pin-list's 10 referents were not checked by the helper; package snapshots do not rehash external freeze/context referents. Root's separate 106+10 checks supplied pre-state evidence but not a helper post-check. | The controlled helper checks package, freeze input pins and context pins before and after both executions. All six corresponding commands in the controlled receipt exited 0. |
| Listed hashes were checked without exact manifest/freeze coverage | `sha256sum -c` alone cannot establish nonself completeness or that input pins identify the intended physical review round. This was a helper gap; the actual A package's 118 names were complete in the separate audit. | The helper rejects duplicate/incomplete nonself package names and requires the exact physical Round0 set for A or Round1 set for B. Controlled structural results are 118 package entries and 106 reviewed inputs. |
| JSON/command exceptions could bypass a final failure receipt | An invalid JSON producer output or command-launch exception could leave captured logs without the promised final receipt. No such failure was fabricated or attributed to the successful old run. | The execution/parsing body now captures exceptions, records failure details and a traceback, and reaches the receipt-writing path. This path was inspected statically; no deliberate failure execution was run by the auditor. |
| Output path guard only excluded the current review subtree | A mistaken new output path under another review or frozen input could still have been accepted. The actually selected QA output was safe, and exclusive creation already prevented existing-file overwrite. | The helper now accepts only the exact P207 review package paths and output descendants of this batch's `qa/root_replays`. The actual controlled output satisfies this restriction. |

The initial audit also confirmed three mechanisms that needed no repair:
the actual A schema matched the parser, manifest/input-pin working
directories matched their documented relative-path roles, and all three
comparisons used actual raw bytes through `cmp`. The receipt already
identified root reproduction as distinct from another independent review.
The revised receipt strengthens that boundary with an explicit
`role_limit`: replay/dependency integrity only, not a manuscript delta
or terminal acceptance. It also validates a strictly positive integer
assertion count rather than only truthiness.

One read-only diagnostic was actually run during the initial audit:

```bash
env PYTHONOPTIMIZE=1 PYTHONSAFEPATH=1 PYTHONDONTWRITEBYTECODE=1 python -B -c 'import sys; print({"optimize":sys.flags.optimize,"debug_assertions_enabled":__debug__,"safe_path":sys.flags.safe_path})'
```

It returned optimize 1, assertions disabled, and safe-path true. This was
a tiny interpreter-settings probe, **not** a P207 checker execution or a
test proving anything about P207 mathematics. The auditor also parsed
the utility syntax in memory; no compiled file was created.

## Preserved old pair and actual controlled pair

The [old receipt](root_replays/p207_a/RECEIPT.json) remains unchanged and
records a genuinely successful old-harness pair. It must not be relabeled
as having controls that were added later. Root retained its tool snapshot
and made a **new** [controlled pair](root_replays/p207_a_controlled/RECEIPT.json)
under a separate output directory. The auditor read those actual receipts;
it did not generate a third pair or claim a fresh numerical execution.

| Recorded evidence | Old pair | Controlled pair |
| --- | --- | --- |
| Receipt UTC | 2026-09-06T07:46:21.072892+00:00 | 2026-09-06T07:48:54.142663+00:00 |
| Producer runs | Two, each 1,326,321 assertions and `PASS` | Two, each 1,326,321 assertions and `PASS` |
| Raw comparisons | Three `cmp` exits 0 | Three `cmp` exits 0 |
| Recorded commands | 9, all exit 0 | 14, all exit 0 |
| Package unchanged | true | true |
| Receipt pass | true under the old helper | true under the controlled helper |
| Explicit controlled runtime / exact coverage | Not claimed retroactively | `-I -B`, runtime probe, 118 package entries, 106 freeze inputs |

Each controlled producer stdout is 37,971 bytes with empty stderr.
The controlled receipt has `failure: null`; every recorded command also
has empty stderr. Its successful pre/post context checks cover the actual
10-entry context list identified above. The follow-up audit accepted
these utility controls and the existing successful execution record,
not the underlying mathematical claims.

## Exact receipt and tool-snapshot pins

These hashes were actually calculated read-only while preparing this
durable record. Root receipts and tool snapshots were not rewritten.

| Artifact, relative to this QA directory | SHA-256 |
| --- | --- |
| `root_replays/p207_a/RECEIPT.json` | `cf2207321274159265a43e3e7d556fa7942b43e1827bf624d3d8d7608854ce30` |
| `root_replays/p207_a/harness_input.py` | `514126afd55e772123763c858cf29dc7a6d8fdd6cf681dbe50ed9b21383d983f` |
| `root_replays/p207_a_controlled/RECEIPT.json` | `ec44f534b50dfdcf1c2a10a696ce51a6322d171468f6bf37a5ce059d5ceaafaf` |
| `root_replays/p207_a_controlled/harness_input.py` | `26679467ce3a39d460c3799406194b82ab78c806ec2902662f7f7399c626b075` |
| `replay_p207_review.py` at this acceptance | `26679467ce3a39d460c3799406194b82ab78c806ec2902662f7f7399c626b075` |

The controlled snapshot, live utility at acceptance, and the controlled
receipt's own recorded harness hash agree. The old receipt's harness hash
likewise matches its separately retained old snapshot. Future utility
changes require a new scoped check; this record does not silently attach
an old replay to changed code.

## Follow-up decision and remaining boundary

**UTILITY_DELTA_ACCEPTED_FOR_RECORDED_CONTROLLED_PAIR.** The concrete
initial flags are handled for the actual controlled pair; no new blocker
was found in the permitted utility/receipt scope. This is a static code
and existing-evidence audit, not exhaustive security testing or a new
execution of the P207 checker.

At this handoff the auditor has done no P207 mathematical review or proof
authorship and has not begun manuscript B. B requires a separate actual
assignment after the reviewer-accepted A delta and physical pinned
Round1 exist. This audit cannot substitute for either prerequisite.
