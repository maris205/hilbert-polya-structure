# P212 B dependency-only proposal: stable source handoff

Status: PROPOSED_NOT_APPLIED / NOT_EXECUTED.

Root requested only JSON/factorial dependency removal after reading the
original complete scientific source and documentation. The proposed changes
are in verify.proposed.py.txt, OUTPUT_PLAN.proposed.md and
OUTPUT_SCHEMA.proposed.md. FULL_DIFF.patch is the complete actual native
unified diff for those three proposed replacements. No other live-file
replacement is proposed. SERIALIZER_PROOF.md gives the supported domain,
escaping, deterministic-equality, unchanged-wire and factorial deductions.

The proposed checker is 481 lines, SHA256
3129ed2e32862addc39f90ceb00a9a3862ba0b11a3037da1549ff8d358f2395d.
The proposed plan is
0925199239249c54b8f7634a88ad2ddfa059d2d044fdfb32918b7c534c03d792;
the proposed schema is
d38b058fb9dbd84e795e62429d017bfed9279f82ebcbfc37f62e5066eeb40344.

No graph, orbit, catalogue, anchor, recurrence, finite bound, predicate name,
field schema, stdout/stderr control or scientific assumption changes.
The full carriers remain n=1..4. The first-size 5/6/5 families remain
deductive-only. The check still distinguishes bool/int and normalizes
tuple/list as JSON. Only itertools and sys remain imported; this is a
documentary source fact, not proof of their builtin/runtime status.

Before creating the proposal, the complete original twelve-payload B source
package plus its original seal was physically copied to original_source12/.
The directory was previously absent. Actual mkdir d258f0 and copy 40a5af
returned exit 0 without sessions. Strict original seal check 12cf32 returned
all twelve OK. Actual recursive byte comparison 5774ea returned exit 0 with
empty output: all thirteen original files match the untouched live source
tree. The preserved original seal remains
31390d1c48e6b78a5e911ef2a9e6c135dd905a7d257cf9f2f563a09b39eae500.

The original scientific source remains
e485026cdeaa20fcc235ded3b32c5431fd4d15d03962d6af201d4830d6ad1b85,
440 lines. Its original twelve-payload seal, SOURCE_READY.md and
FINDINGS_SOURCE.json are retained unchanged, as historical source-stage
evidence. Neither this agent nor this proposal applies changes to live B.
Root applies only after full source/diff/proof reception and creates an
additive current-input record rather than overwriting the original seal.

The actual diff commands returned expected exit 1 (differences found), not
execution failures: d1d99b (verifier), fe5764 (plan), 71fe40 (schema).
Their full output, including file timestamps, is preserved in FULL_DIFF.patch.
Source preparation used ordinary file copying, textual substitution,
apply_patch, source reads, diff and hashing only. No proposed or historical
scientific source was imported, parsed, compiled or executed; no runtime,
module, linkage or host query was made.

The old plan's lines 12–15 explicitly request startup/import/configuration
and native-extension/loader closure. The proposed plan only updates the
dependency statement and does not silently waive that older scope. Root's
separate ordinary-runtime task at qa/p212_b_execution_preparation01 must
provide an explicit accepted policy/binding override before any invocation.
This proposal grants none. No canonical, replay, build, view or final B
verdict follows from the source-only zero manuscript findings.

The enclosing nonself manifest includes all proposal payloads and all thirteen
preserved original files. It excludes itself. No author, frozen manuscript,
central index, Git or external manuscript state changed. HOLD_EXTERNAL.
