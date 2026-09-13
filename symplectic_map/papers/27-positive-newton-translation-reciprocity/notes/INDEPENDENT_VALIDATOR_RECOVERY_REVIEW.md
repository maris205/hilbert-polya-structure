# Independent Recovery-Validator Review — Paper 27

## Authority, frozen subjects, and separation

This sole aggregate static-review artifact is authorized by
`B07-E0306-P27-PROBE-RECOVERY-VALIDATOR-TRIPLE-STATIC-PASS-CONSUMPTION-AND-AGGREGATE-AUTHORIZATION`.
The authorizing ledger has 1,585,980 bytes, 18,623 LF bytes, mode 0644,
link count one, SHA-256
`0e0978a4caa2ae8a9a6dfdf5b5c52705e90c53d5a8aec9624729e70b99a95d5f`,
and terminal
`BATCH07_P27_PROBE_RECOVERY_VALIDATOR_TRIPLE_STATIC_PASS_AGGREGATE_AUTHORIZED`.

The frozen recovery validator source is
`papers/27-positive-newton-translation-reciprocity/notes/BUILD_VALIDATOR_RECOVERY.py`:
398,310 bytes, 9,366 LF bytes, mode 0644, link count one, SHA-256
`6665d3452009a715982a1b549b8c4413001916794cbb0b1fef2062e38e3f4817`,
and terminal `# BATCH07_P27_BUILD_VALIDATOR_RECOVERY_AUTHOR_STOP`.
The frozen one-way lock is
`papers/27-positive-newton-translation-reciprocity/notes/VALIDATOR_LOCK_RECOVERY.md`:
64,169 bytes, 1,173 LF bytes, mode 0644, link count one, SHA-256
`5601233185ca0d880f8e38a8b9ec2fdd174d95aebceb692d3c020d29f5c5f1be`,
and terminal `BATCH07_P27_VALIDATOR_LOCK_RECOVERY_AUTHOR_STOP`.
Both are strict UTF-8/LF, have no BOM, CR, or NUL, and have exactly one
terminal LF.

The canonical source/control frame has 108 rows, 16,816 framing bytes, 108
LF bytes, and SHA-256
`f58de02a111328638fae4f372699362e7cb55f6f21f1e4076d00be6cdba94aff`.
The five exact mode-0644 link-one runtime controls are:

- recovery profile: 62,863 bytes, 1,181 LF,
  `ac1651c8ef5522f76f52b98a9deb300d5409c489d6e3ae4fa58e9d6e3fc4c985`;
- dependency lock: 30,145 bytes, 215 LF,
  `66c96cc6b40658370cc129e3bf828bcd08a7e69f7f2462ebea084cc77ce6ed17`;
- dependency review: 12,687 bytes, 231 LF,
  `b37e361c1cb8e7340c7a2e4af5b207de40df935ced707043c63c1e0f7017df35`;
- recovery profile aggregate review: 15,279 bytes, 306 LF,
  `c39970d11af0d0a7b0e46dde61485eb6629bb0d560541989a984b4982d597202`;
- static-source review: 31,760 bytes, 704 LF,
  `7745af4b80e4e5ff35134e9279b7d2493f9b063bac0110bab115199bae3114ae`.

V1, V2, and parser auditor P received the exact frozen bytes and separate
scopes.  They wrote nothing, accessed no build pathname or stopped build
namespace, did not import, compile, AST-parse, py-compile, or execute the
validator or parser, and neither saw nor relied on another report.  The
author-side sanity auditor filled none of these three roles.

## Complete separated report V1 — derivation, identity, and parser review

### V1 authority and physical identity

V1 independently reproduced the E0305 ledger as 1,578,959 bytes, 18,558 LF,
mode 0644, link count one, SHA-256
`66c0485dd1e92c684f2ae29b58054a7d574e39d7d67a0149cc32984359a1702d`,
with its exact authorizing terminal.  It reproduced both frozen artifact
identities and terminals above and all five runtime-control identities.
Verdict: PASS.

### V1 source and lock derivation

The GNU context-three POSTFAIL-to-RECOVERY source diff has exactly eleven
hunks.  Its zero-context rendering has twenty separated hunks and 29 old/29
new changed lines.  The changes are exhausted by deterministic provenance;
three recovery namespace bindings; source, copy, lock, profile,
profile-review and author-terminal bindings; the two PROFILE and
PROFILE_REVIEW identity tuples; all validator-copy consumers; and the final
source terminal.  No parser, handler, predicate, failure tag, write branch,
or security algorithm changes.

V1 located the seventeen recovery-validator basename consumers at source
lines 23, 24, 451, 456, 457, 1474, 1486, 8086, 8087, 8089, 8090, 8103,
8104, 8238, 8240, 8301, and 8303.  Together they cover the source/copy
constants, exact evidence sets, capacity and mode functions, evidence read,
cache and report rows, census, and terminal/ultimate rebinds.  The complete
`_parse_validator_stdout` block is byte-for-byte equal to the frozen
POSTFAIL block.

The lock's zero-context diff has twenty-two separated hunks, 39 old and 44
new changed lines.  It is limited to authorized identity, provenance,
control, name-frame, and future-review-terminal prose.  All executable and
security semantics and the total-parser regression baseline remain inherited.
Verdict: PASS.

### V1 active/stale fence and one-way binding

Recovery source active counts for namespace, validator basename, lock,
profile, and profile-review are exactly `3/17/1/1/1`.  Source occurrences of
the postfail namespace, corresponding source/lock/profile/review basenames,
and postfail terminals are all zero.  In the recovery lock, the old source
and old lock basenames each occur once, only in the explicit immutable
derivation-history paragraph; old build namespace, profile, profile review,
and author terminal occur zero times.  The inherited successor launcher
argv0 is a declared frozen launcher identity, not a runtime build namespace.

The lock's sole machine frame exactly binds source bytes, LF, mode, link
count, SHA-256, and terminal.  The source embeds neither its own physical
hash, the lock hash, nor a future review identity; therefore the direction is
source to lock and contains no physical identity cycle.

V1 independently recomputed all sorted name frames:

- final evidence root: 16 names, 189 bytes,
  `281f6009d76f29f562eda5035460cc386b7e9847a015ebd1cd2c5070c52c0313`;
- root-0 ABSENT: 8 names, 103 bytes,
  `72b0a3948e4c178327e5ce944f2e6887ce26b22a23d9a5a376d762719f8e4a8b`;
- root-1 ABSENT: 12 names, 142 bytes,
  `3351f3d984004a4d71522d88438d0de223a6339b80bd5f00ce8fe53e39e4850b`.

Verdict: PASS.

### V1 parser structure and regression matrix

`MODE_ARITY`, `MODE_HANDLERS`, and `VALIDATOR_RESULT_FIELDS` each have the
same 15 modes.  Static argv expansion is
`2+16+22+10+6+2+2+2+2+2+2+2+1+2+1=74`.  The result table has 90 ordered
field occurrences and 52 distinct names, exactly partitioned into 29
canonical-decimal, six symbolic, one warning-hex, and sixteen SHA-bearing
names.  `root`, `stage`, `checkpoint`, `id`, `dependencies`, and
`disposition` each have one total name-first branch; invalid-only branch
count is zero, and no legal seventh field reaches the fail-closed
`UNVALIDATED` fallback.

V1 statically closed the canonical r0/r1, eight-checkpoint, sixteen-ID,
unsigned-decimal, `87/86`, `benign-underfull-only`, lowercase-hex,
warning-hex, recorder-pair, cross-manifest-pair, and expected-subset positive
classes.  It also closed these exact negative suffix families:

- mode/framing/ASCII/prefix: `_MODE`, `_FRAMING`, `_ASCII`, `_PREFIX`;
- missing, empty, duplicate, or reordered field: `_FIELD_<name>`;
- leading-zero, signed, or nondigit decimal: `_DECIMAL_<name>`;
- symbolic values: `_ROOT`, `_STAGE`, `_CHECKPOINT`, `_ID`,
  `_DEPENDENCIES`, `_DISPOSITION`;
- warning, structured recorder, and structured manifest values:
  `_WARNING_HEX`, `_RECORDER_HASHES`, `_MANIFEST_HASHES`;
- ordinary hash and caller subset mismatch: `_HASH_<name>` and
  `_EXPECTED_<name>`.

Verdict: PASS.  V1 findings are Blocker=0, Major=0, Minor=0, Ambiguity=0.

VALIDATOR_RECOVERY_V1_PASS

## Complete separated report V2 — full security-semantics review

### V2 identity and bounded delta

V2 independently reproduced the E0305 ledger, source, lock, recovery profile,
profile-review, dependency lock/review, static-source review, and source-trio
identities.  It reproduced the eleven context-three source hunks, twenty
zero-context source hunks with 29 old/29 new lines, byte-identical parser
block, and twenty-two lock hunks with 39 old/44 new lines.  It found no
algorithm, parser, or security-predicate delta beyond the authorized recovery
bindings.  Verdict: PASS.

### V2 path, descriptor, resource, and trust boundaries

Governed paths use component-wise held chains opened with
`O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC`, or the shared identity pool.  Leaves use
no-follow stat/open-at, complete pre/post stat keys, held-descriptor rehash,
and pathname rebind.  Receipt guards bind descriptors 1 and 2 to the sole
mode-0600 link-one empty receipt files and validate non-append state, offsets,
readback, fsync, absent status, and exact stage inventory.

The stable `/proc/self/fd` census permits only 0/1/2, guard, chain, read, and
scan descriptors.  The soft `RLIMIT_NOFILE` range is 1024 through 4096.  The
held CPython 3.12 target and `/proc/self/exe` are bound by inode, size, and
SHA-256.  The lock correctly treats the outer launcher, pre-main loader and
modules, and cross-process single-writer continuity as external trust
premises rather than claiming validator self-authentication.  Verdict: PASS.

### V2 first-touch and E001 handoff

The corrected profile retains the full seven-descriptor `/`-through-`build`
chain, performs opening and terminal no-follow absolute rewalks, and uses the
freshly rebound terminal parent to lstat/open the literal leaf and match the
held created child.  There is exactly one relative mkdir, with mode 0700,
link count two, current owner, empty inventory, and child/parent fsync.  It
contains no cleanup, retry, rename, chmod, stage, or root creation.

The receipt-free exception applies only to first evidence-directory creation
and ends permanently at physical ledger binding.  E001 and every later row
restore the FD-scrub launcher, isolated environment, exclusive receipts,
installed validator copy, and complete validator predicates.  First-touch
imports only `errno`, `os`, `stat`, and `sys`; validator imports are the nine
frozen standard-library modules, with no dynamic import, builtin evaluation
or compilation, subprocess, shell, network, or repair branch.  Verdict: PASS.

### V2 dependency, roots, receipts, manifests, and evidence

The embedded dependency frame remains 87 rows, 23,408 bytes, 87 LF, with its
frozen hash, 87 logical paths, 86 unique final targets, and two frozen
symlink chains.  ABSENT and REPLAY perform complete no-follow rebind and
rehash.  Root-state universes, five raw manifests, eleven snapshots,
recorder/BibTeX sets, transition immutability, exclusive destinations, and
frozen-manifest rebinds remain complete.

SOURCEFINAL, STAGEINV, CROSS, and EVIDENCE retain their initial, terminal, or
ultimate checks.  CROSS covers eight raw pairs, three recorder projections,
five manifest projections, and the complete PDF semantic summary.  EVIDENCE
revalidates both final stages, cross cache, evidence-root regulars and child
directories, and the empty in-flight X010 state.  Verdict: PASS.

### V2 publication and PDF semantics

Log, AUX, BBL, BLG, and bibliography predicates close the 20-key reference
set, sentinel, 24--28 proof-content pages, warning-only-underfull disposition,
and rejection of error, overfull, rerun, shell-escape, and unlisted control
lines.  PDFTEXT closes page count, reference page, title, Anonymous/Abstract,
eight headings, modules, clauses, fixtures, boundary cases, conclusion, 20
references, provenance, and email firewall.

PDFRAW closes the PDF header and terminal EOF; direct and object-stream
objects; classic xref or XRef stream; reachability; Catalog and Page tree;
Resources; sole Contents stream; stream-role partition; action and semantic
token rejection; bounded Flate decoding; and complete Type1 clear/eexec,
CharStrings, Subrs, glyph execution, and FontName binding.  Verdict: PASS.

### V2 emission and failure semantics

Terminal recomputation precedes PASS.  Hold, runtime, source/copy, control,
identity, and receipt checks occur before and after emission.  Partial write,
failure after emission, guard failure, and caught exception all force nonzero
status; stdout text alone can never constitute success.  Snapshot and
manifest writes remain exact direct-child, `O_EXCL|O_NOFOLLOW`, mode 0600,
fsynced, reread, and hash-verified operations.  Verdict: PASS.

### V2 stale-name and parser counterexample census

V2 independently reproduced recovery source counts `3/17/1/1/1`, zero old
active source names and terminals, historical-only old lock names, the three
name frames, 15 modes, 74 argv rows, 90 occurrences, 52 names, six total
symbolic branches, and no legal seventh UNVALIDATED field.  It rejected
invalid symbolic, decimal, hash, warning, structured pair, prefix, field,
framing, and expected-subset counterexamples.  `manifest_sha256` correctly
enters the structured five-pair branch for CROSS and the generic hash branch
for SOURCEFINAL.  Accepted invalid counterexamples: zero.  Verdict: PASS.

V2 findings are Blocker=0, Major=0, Minor=0, Ambiguity=0.

VALIDATOR_RECOVERY_V2_PASS

## Complete separated report P — parser-matrix audit

### P authority and physical identities

P independently reproduced the E0305 ledger, POSTFAIL source, RECOVERY source,
and RECOVERY lock identities and final terminals.  It rechecked them at the
end and found no drift.  Verdict: PASS.

### P common mode tables and exact argv rows

The three mode tables have these identical fifteen keys:
`ABSENT`, `REPLAY`, `SNAPSHOT`, `MANIFEST`, `RECORDER`, `R033LIVE`, `BIB`,
`LOGBIB`, `PDFINFO`, `PDFTEXT`, `PDFRAW`, `SOURCEFINAL`, `CROSS`,
`STAGEINV`, and `EVIDENCE`.

The per-mode arity, static argv-row count, and result-field count are:

| Mode | Arity | Argv rows | Result fields |
|---|---:|---:|---:|
| ABSENT | 2 | 2 | 4 |
| REPLAY | 2 | 16 | 5 |
| SNAPSHOT | 4 | 22 | 5 |
| MANIFEST | 3 | 10 | 5 |
| RECORDER | 3 | 6 | 9 |
| R033LIVE | 3 | 2 | 4 |
| BIB | 5 | 2 | 4 |
| LOGBIB | 7 | 2 | 12 |
| PDFINFO | 3 | 2 | 4 |
| PDFTEXT | 3 | 2 | 5 |
| PDFRAW | 2 | 2 | 8 |
| SOURCEFINAL | 1 | 2 | 4 |
| CROSS | 1 | 1 | 10 |
| STAGEINV | 2 | 2 | 5 |
| EVIDENCE | 2 | 1 | 6 |

`ROOT_CONFIG` has two distinct root/stage pairs; `ROOT_STATES` has eight
checkpoints; SNAPSHOT, MANIFEST, and RECORDER maps have 22, 10, and 6 rows;
the remaining root maps each have two.  The comprehension expansion is
therefore exactly 74 unique argv rows.  Verdict: PASS.

### P result fields and handler emitters

The ordered per-mode field counts sum to 90.  There are exactly 52 distinct
names: 29 decimal; six symbolic; `warning_bytes_hex`; and sixteen
SHA-bearing names.  Independent extraction from every handler return produced
the same 90 occurrences and 52 names in the same per-mode positions.  The
lock's fifteen canonical PASS-vector field sequences also match exactly.
Thus no handler emits an unclassified seventh symbolic field.  Verdict: PASS.

### P total symbolic dispatch and positive matrix

The six name-first branches for `root`, `stage`, `checkpoint`, `id`,
`dependencies`, and `disposition` each occur exactly once; invalid-only branch
count is zero.  Valid domains are r0/r1; the eight `R020` through `R050`
pre/post checkpoints; sixteen snapshot/manifest/recorder IDs; `87/86`; and
`benign-underfull-only`.

The lock contains one canonical PASS vector per mode.  Its generic hash,
three recorder pairs, five CROSS manifest pairs, decimals, r0/r1 variants,
eight checkpoints, and sixteen IDs all satisfy the exact source grammar.  No
positive vector reaches `UNVALIDATED`.  Verdict: PASS.

### P negative matrix and exact tags

P independently established these outcomes:

- `root=r2`, `stage=r2`, truncated checkpoint/ID, `86/86`, and `benign`
  reach `_ROOT`, `_STAGE`, `_CHECKPOINT`, `_ID`, `_DEPENDENCIES`, and
  `_DISPOSITION`;
- leading-zero, signed, or nondigit decimals reach `_DECIMAL_<field>`;
- 63/65-digit or uppercase hashes reach `_HASH_<field>`;
- invalid warning hex reaches `_WARNING_HEX`, while an empty token reaches
  `_FIELD_warning_bytes_hex`;
- missing, reordered, unequal, miscounted, or single-digest recorder and
  CROSS manifest structures reach `_RECORDER_HASHES` and `_MANIFEST_HASHES`;
- wrong prefix/mode or missing/extra complete field reaches `_PREFIX`;
  duplicate/reordered/empty fields reach the exact `_FIELD_<name>`;
- CR, NUL, control/high byte, missing LF, or extra LF reaches `_FRAMING`;
  unknown parser mode reaches `_MODE`; and caller subset mismatch reaches
  `_EXPECTED_<name>`.

P compared the complete parser function block, including its separating LF,
between POSTFAIL and RECOVERY and obtained byte equality.  No parser table,
function, or handler-dispatch diff hunk exists.  Verdict: PASS.

P findings are Blocker=0, Major=0, Minor=0, Ambiguity=0.

VALIDATOR_RECOVERY_PARSER_AUDIT_PASS

## Aggregate disposition and scope limit

V1, V2, and P independently return Blocker=0, Major=0, Minor=0,
Ambiguity=0.  Their exact identities, bounded recovery delta, one-way lock,
control and name frames, total parser, full security baseline, counterexample
search, and nonexecution facts agree.  One report cannot waive, cure, or
outvote a finding in another; there is no finding to waive.

This is a static PASS only.  It authorizes no validator import or execution,
runtime parser microtest, evidence/root/build pathname access or creation,
compiler, BibTeX, PDF action, release, Paper 28 action, network access, or
external effect.  A later physical-freeze ledger event must bind this exact
artifact and separately authorize an exact microtest plan before any selected
parser byte may execute.  All failed and stopped predecessor artifacts remain
immutable history and are not retroactively cured.

BATCH07_P27_VALIDATOR_RECOVERY_REVIEW_PASS
