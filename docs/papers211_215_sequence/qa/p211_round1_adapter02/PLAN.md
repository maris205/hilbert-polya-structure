# P211 Round1 adapter02 — bounded empty-directory source correction

2026-09-08 UTC. Status: SOURCE_READY_PENDING_ROOT_RECEPTION_AND_BINDING.
Owner: /root/round211_rational_scout/relation_primary_sources.
Only this new adapter02 directory is authored. No recorder was imported or
invoked; no physical Round1, execution directory, binding, science, build,
page view, central index or Git operation was created or performed here.

## Actual failure and immutable predecessor

Root's actual [entry-preflight failure](../p211_round1_binding_root/ENTRY_PREFLIGHT_FAILED01_NATIVE.json)
returned native exit 1, chunk 0d92db, at invoke.py line 93 while checking
the complete p211_a_initial_01 external tree. The exact failure-record pin is
fc09863dc261e90834f03134d2ac953f2d0807af623d29749b4ed6e18e14f575.
This is a controller preflight failure, not a recorder or copy attempt.
Root reports failure before CONTROL/EXEC creation. Our separate recorded
ls also observed both frozen_round1 and p211_round1_execution01 absent.
No cleanup, ignored subtree or replacement of failed evidence was attempted.

The complete accepted [adapter01](../p211_round1_adapter01/PLAN.md) remains
unchanged and sealed under
a8b177ff6c92c630b82868d2ac537cbd49f6461b7e1f50b31f328bab09495fb8.
Its 35,397-byte freeze.py, hash
50c32a6fa4c703275cb55535bc56507ba5bdbb909fb57ed31ffc6d3ff9566ab2,
is the immediate source predecessor. The full three-file native
[diff](DERIVATION.diff) and [actual diff returns](DERIVATION_NATIVE.json)
bind source/schema/pending changes. Their exit 1 means ordinary file
differences, not a failed freeze.

## Exact correction and binding schema v2

[freeze.py](freeze.py) adds a keyword-only empty_directories=() inventory
argument. Only verify_external_trees supplies it, after requiring the exact
five tree fields and exact ordered empty-directory list for the literal root.
Every other root must explicitly bind []; missing, duplicate, shortened,
extra, reordered or rebased lists fail. The source and
[BINDING.schema.json](BINDING.schema.json) hard-code exactly these lists:

| Root under docs/papers211_215_sequence/qa/ | Exact relative empty directories |
|---|---|
| root_replays/p211_a_initial_01 | child01/commands |
| root_replays/p211_a_pair_01 | child01/commands; child02/commands |
| p211_runtime_preparation | discovery01/empty_probe_capsule; discovery02/empty_probe_capsule; tests01/existing_cache; tests02/existing_cache; tests02/fixture_initial/child01/commands; tests02/fixture_pair/child01/commands; tests02/fixture_pair/child02/commands |

These ten names were explicitly supplied by root. This preparation has not
claimed a fresh filesystem acceptance of those directories. Root's revised
binding must include all three roots if its execution scope requires all ten;
the recorder's per-root support does not invent an additional global tree
selection or relax the complete externally consumed file-key obligation.

Each declared empty must physically exist as an ordinary non-symlink
directory, have no children, avoid file/path-ancestor collisions, and appear
as a rich directory row. Expected directory membership is exactly file
ancestors plus empty-directory ancestors plus the named empty nodes.
No empty directory is pruned, omitted, treated as a file pin or inserted into
SHA256SUMS. Unlisted siblings, special files, dangling paths and symlinked
parents remain rejected. Both external-tree passes repeat these checks, and
the existing complete rich before/after equality remains mandatory.

Author-live, A, Round0, new-frozen and Markdown directory-link inventory
calls are unchanged and retain strict ancestor-only membership. Root
separately confirmed that its sole bound external-directory Markdown target
has 28 files and no extra empty directories; we did not open that binding.
The inventory result now additionally records declared_empty_directories,
including [] for strict calls. This is an explicit output-field addition,
not a relaxation or rewrite of any older result.

The source PREPARATION literal changes to adapter02 and the binding identity
changes to p211_round1_binding_v2. The execution target remains the still
unused p211_round1_execution01. [BINDING_PENDING.json](BINDING_PENDING.json)
changes only its schema identifier: enabled remains false, external_trees
and all actual authority/pin/selection fields remain null. It is deliberately
not an executable binding and must not be filled in after sealing.

## Preserved behavior and root-owned next action

The exact author32, complete dynamically bound final A, 17 acceptance roles,
old 727/660 metadata resolutions, all manifest/link/origin logic, physical
separate copies, native raw records, failure preservation, isolated
/usr/bin/python3.10 -I -S -B invocation and separate complete host/settings
rechecks remain unchanged. For root's supplied N=50 final A payloads,
the old native command formula is still 32 + 2 + 83 + 2 = 119. This is a
source-level count, not an observed invocation or read of final A here.
No author, A, scientific verifier or canonical body was opened in this task.

Root owns full source reception, the new exact v2 binding, revised controller,
pre-copy host/settings checks, actual recorder invocation, complete native
return, post-copy root reception and execution seal. The earlier binding01
and failed controller evidence must remain immutable; this package neither
edits nor reads the actual binding selection. No new mandatory paper gate
or manuscript verdict is introduced.

## Actual static evidence and limits

The actual [static run](NATIVE_STATIC_CHECKS.json) returned exit 0 with
202 checks and 14 pinned source/metadata inputs. It parses/compiles AST
without executing either recorder; compares every unchanged function and
the entire normalized old/new recorder; checks the exact source/schema
lists, strict call sites, directory-record/emptiness guards, immutable root
failure, preserved metadata counts and disabled pending template.
It is not a filesystem exercise or full JSON-schema-engine validation.
[INPUTS.sha256](INPUTS.sha256) extends the exact preparation input pins to
18 explicit source/metadata/instruction files; it follows no scientific
referents from the accepted old metadata ledgers.

A separate process-separated [static source inspection](INDEPENDENT_STATIC_RECEPTION.json)
found no blocking code/schema mismatch in the final three source/schema/
pending originals. Its actual returned pins are preserved; it ran neither
recorder and gave no manuscript, binding-completeness or execution verdict.
This preparer cannot independently certify its own infrastructure.

[Native preparation reads](NATIVE_PREPARATION_READS.json) preserve the
selected actual request/return envelopes, including the absence check.
The first combined display was truncated; full source/schema returns were
subsequently read. A source-generation orchestration attempt stopped at
an unavailable structuredClone helper before any tool write; the exact
error and scope are retained in that record. No native exit was invented
for that orchestration error. All earlier sealed files remain untouched.

This infrastructure-only correction adds no P211 theorem, manuscript,
proof repair, scientific verifier or canonical contribution and does not
start B. Earlier disclosed infrastructure and manuscript-reading familiarity
remain in the contribution record. OWNER_AMBER / HOLD_EXTERNAL.
