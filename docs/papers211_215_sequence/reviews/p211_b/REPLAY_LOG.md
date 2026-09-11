# P211 B actual initial production, strict pair and original reception

2026-09-09 UTC. This log receives completed original executions; it does
not claim that the reporting reviewer launched them again. Native receipt
timestamps are retained verbatim, including their 2026-09-08 UTC execution
times; the review/index documents are dated 2026-09-09. No timestamp or
tool envelope has been rewritten to make those dates identical.

All `qa/` paths below are relative to docs/papers211_215_sequence. Full
absolute paths, cwd, argv, environment, deadlines and real native outputs
remain in the linked originals. Scientific output is finite evidence,
not an all-n proof or manuscript acceptance.

## 1. Source gate and exact immutable capsule

Root's [PREPARATION_RECEPTION](../../qa/p211_b_root_reception/PREPARATION_RECEPTION.md)
received 19 preparation payloads / 866,505 bytes, the entire 552-line
source, 330-line schema, 361-line deductive proof and source/build record.
Actual reception made 2,318 checks over 161 consumed paths before any B
producer invocation. All 84 Round1 and 50 external original pins matched.
The unchanged 20-file preparation, including its 1,713-byte manifest,
occupies 868,218 bytes. Its manifest SHA256 is
`7a55db3d72952dac3bf77ea0f0bf82989606296684561ef468ea67ca2ff9850f`.

| Capsule item | Bytes | SHA256 |
| --- | ---: | --- |
| verify.py | 26,482 | `6888ea1df1c20e4786c3582a61fcc5c7d6c8901d9e322d16dc50b047786c5fa7` |
| parameters.json | 1,374 | `214b1832a5aae184bd0617334307d87cdcb51f29d2b41983593bdae2d5fc2cac` |

Only `itertools,json,math,sys` are submitted ordinary imports, with no
helper or earlier implementation import. The accepted supported capsule
uses absolute `verify.py --parameters ABS_PARAMETERS`, system Python
3.10 with -I -S -B and optimize zero. Initial and pair retain the same
122-file runtime, complete bounded configuration, ENV4
`PATH=/usr/bin:/bin; LANG=C.UTF-8; LC_ALL=C.UTF-8; TZ=UTC`, distinct absent
caches, and science/native/envelope deadlines 300/60/900 seconds. This is
bounded source/runtime evidence, not OS hermeticity or continuous tracing.

## 2. One real initial invocation, then exclusive canonical adoption

[Initial BINDING.json](../../qa/p211_b_initial_binding/BINDING.json)
has 90,952 bytes and SHA256
`ba7f9fb4b13b236d189be61da87860f802e478d9d91e17dd6e2368812c9099ed`.
The actual [production tool envelope](../../qa/p211_b_initial_binding/PRODUCTION_TOOL_INVOCATION.json)
records outer invocation chunk `8ec89c`, session 36780, followed by
`fb1694` with exit 0. Its command is env-i with the above ENV4 and Python
flags, the initial-specific never-created outer cache, the pinned
`p211_runtime.py outer`, exact initial binding path/hash, and distinct
`qa/root_replays/p211_b_initial_01` attempt path.

The complete original execution tree has 77 payloads plus its 7,585-byte
nonself manifest, SHA256
`eac19aad71c6c9385e110670954d48f055939bf1d8d6efe6108da81375d1f0ff`.
The seven actual native commands are the two source copies, ldd-before,
one science child, ldd-after, and the launcher/recorder envelope commands.
Their whole ATTEMPT/RECEIPT objects and exact stdout/stderr files were
received. Stage payload counts are child01 10, launcher 14, outer 14,
recorder 35; nested manifests are separately retained in the outer count.

[INITIAL_RUNTIME_NATIVE01](../../qa/p211_b_root_reception/INITIAL_RUNTIME_NATIVE01.json)
is the real whole-original reception: native `edd077`, exit 0,
199,871 checks / 377 paths, one actual science invocation and one full
raw comparison in that reception. The root saved-output receiver then
completed session 51116 (`6ee098` then `ec8f4f`, exit 0) and made
169,604 complete semantic checks. See
[INITIAL_SEMANTIC_NATIVE01](../../qa/p211_b_root_reception/INITIAL_SEMANTIC_NATIVE01.json).
It read every saved field rather than importing a submitted producer.

Only after these checks did root exclusively create the formerly absent
canonical from the actual raw file. The original
[ADOPTION result](../../qa/p211_b_initial_binding/ADOPTION/RESULT.json),
attempt, native cmp streams/receipt and actual adoption tool envelope are
in the closed initial-binding directory. No normalization, hand-written
transcript, conversion of an old pilot or overwrite occurred.

Canonical path: `reviews/p211_b/CANONICAL.json`.
Actual initial raw path:
`qa/root_replays/p211_b_initial_01/recorder/commands/03_verify_01/stdout.raw`.
Both are 3,053,387 bytes, SHA256
`10daa982cc755162b09c4e1e4783343f4ea25ca4c464e2123693e2156b810658`.

## 3. Separately bound strict pair: two children and three native cmps

[Pair BINDING.json](../../qa/p211_b_pair_binding/BINDING.json) has
104,136 bytes, SHA256
`ab8dd9cfe74af47941b793bb8118bce6061a72616757e7339ecfe29232e15d41`.
The complete [initial-to-pair delta](../../qa/p211_b_pair_binding/EXACT_INITIAL_TO_PAIR_DELTA.json)
has only six changed top-level keys: attempt, canonical, mode,
provenance_inputs, root_canonical_policy and schema. The actual
key spellings are retained in the JSON and the B intake output; these
changes do not change science, carriers, import closure or deadlines.

The [actual pair production envelope](../../qa/p211_b_pair_binding/PRODUCTION_TOOL_INVOCATION.json)
records chunk `aead3f`, session 13277, then `214ffb`, exit 0. It uses the
pair-specific binding/hash and cache/attempt paths. The two real science
outputs are the pair tree's recorder commands `03_verify_01/stdout.raw`
and `03_verify_02/stdout.raw`. Commands `04_canonical_1`,
`04_canonical_2` and `05_pair` are the three actual native cmp operations.
All completed with exit 0 and empty comparison streams. Every science
stderr is also empty. Owned process groups settled with no remaining
active members or signals; the complete native receipts preserve PIDs,
time bounds, cwd, ENV4, stream bytes/hashes and settlement observations.

The tree has 104 payloads and a 10,346-byte nonself manifest, SHA256
`8b356ea1d927128c0a31719448d2e1d80daa9dce3645d55095539150135571b6`.
It contains 11 native commands. Child01 and child02 each have 10 payloads;
launcher/outer each 14 and recorder 51, plus nested manifests.

[PAIR_RUNTIME_NATIVE01](../../qa/p211_b_root_reception/PAIR_RUNTIME_NATIVE01.json)
records actual `1f65ee`, exit 0, 357,231 checks / 423 paths, two actual
science children and all three real comparisons. Separate whole-output
semantics receipts are
[PAIR_SEMANTIC_NATIVE01](../../qa/p211_b_root_reception/PAIR_SEMANTIC_NATIVE01.json)
(session 26656, `2425e5` then `655d60`) and
[PAIR_SEMANTIC_NATIVE02](../../qa/p211_b_root_reception/PAIR_SEMANTIC_NATIVE02.json)
(session 49762, `484da1` then `b616dd`). Both ended at exit 0 and each
performed 169,825 full semantic checks. Both raw outputs are exactly the
canonical bytes, not merely mathematically equivalent JSON.

## 4. Complete counters and retained scientific content

Every one of the three actual B invocations reports the same 32,766
named checks: 32,763 carrier-level calls plus three global hand attacks.
Internal helper preconditions are not retroactively counted as named
checks. All seven complete carriers total 2,353 states/targets/edges.
Per-carrier counts and image/zero-fibre censuses are in [REPORT.md](REPORT.md).

The 12 category totals in the actual saved output are 4,713; 2,353;
4,706; 2,382; 2,360; 2,730; 1,044; 2,730; 7,059; 2,289; 384; 13,
in B01--B12 order. For a carrier of M states, image size I, whole table
count L, sum S of image `(R+2)` epochs and total O kernel options, the
exact call counts are
`[1+2M, M, 2M, L+M, 1+M, M+I, S, M+I, 3M, I+O, I+1, 1+[n>1]]`.
In particular B09 is 3M: two incoming-description checks per source,
one count check per image target, and one zero-fibre check per nonimage
target. The root receiver matches that actual call census.

Full schema coverage retains identity through duplicate final composition
tables, every state record, complete target fibres including zeros,
per-label death data, every kernel option including zero-completion ones,
separate rank bins and all signed Laurent coefficients. The decoder
does not obtain its candidate sources by scanning the literal arrow list.
Finite successes neither establish priority nor replace the all-n proof.

## 5. Binding closure and B's actual whole-document intake

The [closure native envelope](../../qa/p211_b_binding_closure/NATIVE01.json)
contains actual `28ef1f`, exit 0, 2,660 checks / 512 paths. All 297/317
rich binding inputs and whole execution trees matched. The closed
initial binding has 15 payloads plus its 1,322-byte manifest SHA256
`a7c68514c1b763c54ebbe048d47c1629e686d451dbc2e0bd8872653789c8daa5`.
The pair binding has seven payloads plus its 608-byte manifest SHA256
`8a81457aa96c3c24e3af7ad4773b754f9dffd246731a1026e77793ce509c20b6`.
This additive closure did not change any preparation, source or canonical.

B subsequently ran only its new read-only [receive_documents.py](receive_documents.py),
not a producer, runtime controller, root semantic receiver or build.
The real invocation was `/usr/bin/python3.10 -I -S -B
docs/papers211_215_sequence/reviews/p211_b/receive_documents.py` from
the workspace root: `4fd92f`, session 90450, then `f3a330`, exit 0.
The full [native envelope](evidence/DOCUMENTARY_INTAKE_NATIVE01.json)
retains the complete output (tool-reported 74,519 tokens), not a re-created
success result. It records 515 full-byte read paths, both whole binding
keys, every execution file, all 18 original native commands, complete
manifest membership, and exact original receipt-to-raw comparisons.

It strictly JSON-parsed all JSON files and all three scientific stdout
files, recursively visiting every key/value, without recomputing graph or
formula content. The canonical alone contains 21,286 objects, 139,965
object keys, 27,108 arrays, 192,059 integers, 7,059 booleans, 7,904 nulls
and 2,984 string values. These are structural node counts, not proof
checks. Whole canonical serialization and all three complete raw/parsed
equalities were checked. The 1,658,754 documentary checks add no B
scientific invocation and do not independently certify B-authored infra.
Root's separately accepted full semantic and runtime evidence is reused.

B fully read the final 6,299-byte
[P211_B_RUNTIME_RECEPTION](../../qa/P211_B_RUNTIME_RECEPTION.md), SHA256
`9eb3526c549ce314eccf7e7d7f1a1a5d749352659e0d49167459747e46071638`.
Its complete key is in that documentary intake. Its final index-control
capture paragraph was received; neither that newer receipt nor the newer
indexes is falsely assigned to historical private Git ref 7d43cb32.

## 6. Failures, limits and still-pending exact response

No B scientific invocation failed or was discarded; there are exactly
three actual producer invocations, all received. Original pilot/prelock
and earlier build failures remain where they were, not silently reused
as this pair. Preparation's guessed paths, wrong archived JSON-field
lookup and display-truncated reads remain historical failures/limits.
The reporting turn's early expected-but-not-yet-created runtime receipt
probe and an overly broad truncated filename discovery are retained in
evidence/FINAL_REVIEW_NATIVE_READS01.json; neither is credited as a
successful complete artifact check. Later exact paths were actually read.

No source was imported or compiled before its exact binding. Reporting
performed no further scientific run, new build, page render or root view.
Source-only build reuse retains the full old key and separately attributed
audit, not a smaller hash substitute. Final report recommendation is not
an accepted delta; exact response reception and same-reviewer decision
remain next, followed by root's complete package/round gates.
