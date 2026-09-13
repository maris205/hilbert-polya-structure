# Batch 07 fresh charter audit

Audit disposition: PASS
Auditor role: fresh, independent `batch07_charter_auditor`
Audit date: 2026-08-28 UTC
Controlling subgate: `BATCH07_CHARTER_FRESH_AUDIT_REQUIRED`
Broad workflow stage: `BATCH07_PAPER27_CANDIDATE_DISCOVERY_OPEN`

## Restricted read boundary and procedure

This audit was performed after Batch 06's independently audited local closure
and before any Batch 07 candidate artifact.  I read `BATCH_07_STATUS.md` and
exactly these eight paths in its Frozen Start Manifest:

1. `BATCH_05_FINAL_AUDIT.md`
2. `BATCH_05_IDEA_REPORT.md`
3. `BATCH_05_STATUS.md`
4. `BATCH_06_FINAL_AUDIT.md`
5. `BATCH_06_IDEA_REPORT.md`
6. `BATCH_06_STATUS.md`
7. `README.md`
8. `docs/candidate_registry.md`

The only additional filesystem observation permitted by the charter-audit
instruction was a no-follow enumeration of the immediate children of the
workspace `papers` directory, solely to test whether a `27-*` directory was
already present.  No symlink target was followed.  No other `papers` content,
project file, PDF content, temporary root, closed root, future root, or
unlisted file was read or probed.  Hash, byte, LF, mode, link-count, encoding,
and marker checks used read-only local tools and isolated `python -I -B`
stdin execution.  There was no network, build, compile, BibTeX run, numerical
or CAS run, scientific script, GPU/data operation, cache creation, copy,
cleanup, external message, upload, submission, hosting, repository push,
identity disclosure, or other external effect.  This review is the sole
authorized write and was created with one `apply_patch` invocation after the
all-zero census below.

## Authorization, scope, and gate precedence

The Material Passport records the user's exact instruction
`good， 开始下一轮，就这样来` after Batch 06 reached independently audited
local closure and paused before Paper 27.  In the immediately preceding
five-paper cadence, that continuation authorizes the next five positions,
Papers 27--31.  The charter does not expand beyond those positions, and it
requires one-at-a-time formal opening; a number is consumed only after two
fresh, mutually independent candidate PASS reviews and formal project
creation.

The passport's `BATCH07_PAPER27_CANDIDATE_DISCOVERY_OPEN` is the broad phase
label.  E0001's `next_gate: BATCH07_CHARTER_FRESH_AUDIT_REQUIRED` is the
immediate controlling subgate and is narrower.  The final charter paragraph
and queue prohibit every candidate-review artifact, idea report, project
directory, and downstream lifecycle until this fresh audit passes.  Thus the
two labels are hierarchical rather than competing authorities; ambiguity is
zero.

The current passport is `OPEN_CANDIDATE_DISCOVERY`, with terminal
dispositions `0 / 5`, local anonymous release passes `0 / 5`, and current
external effect `none`.  Read-only public primary-source/bibliographic lookup
is the only expressly permitted discovery activity.  Upload, transport,
hosting, push, submission, messaging, identity disclosure, new GPU or
empirical work, broad parameter/prime/modulus scans, and unregistered
scientific execution are explicitly unauthorized.  Headline claims must use
proof, counterexample, and exact symbolic reasoning only.

## Frozen identity verification

The eight live manifest inputs were independently rehashed at the audit
opening and again immediately before this review write.  Every input is a
regular non-symlink file, mode `0644`, link count `1`, strict UTF-8, LF-only,
without BOM or NUL, and has exactly one terminal LF.  The measured identities
are:

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `BATCH_05_FINAL_AUDIT.md` | 17,937 | 325 | `3e583ac5a989a689b93da3a6a6a74ac42e37f2caaa2b6601c7ca14e37d46de3e` |
| `BATCH_05_IDEA_REPORT.md` | 54,677 | 1,067 | `e697b0b5e252a42b08363548316ffdea620dec57f7970d106b06e7f6b54cfa46` |
| `BATCH_05_STATUS.md` | 63,905 | 925 | `296cbbbde7df633de5f995285b3878477487f5ac8ac1032077cac1aa35bf4e1e` |
| `BATCH_06_FINAL_AUDIT.md` | 25,301 | 436 | `8f28253a94918a6ab0c6934ce167c3d6129deadc50e7f41d46136dce8b19c1f3` |
| `BATCH_06_IDEA_REPORT.md` | 675,259 | 12,068 | `2e097d928bbe695866653c47aace6215358e0187326044e8eb548fddd3cd1ef3` |
| `BATCH_06_STATUS.md` | 616,461 | 9,095 | `5c95ac0f195ae7de935b0c2cc902ebcf6df15f0cb7292835d1c51ea208d45609` |
| `README.md` | 9,594 | 41 | `415bc57e4d2e87bcf078b969c7edf0c769f436d1ff41cfca1619f37540222cda` |
| `docs/candidate_registry.md` | 17,936 | 41 | `27f43be37659125f6a9ed2183772325da83acea1239aed22fe71d9494a54b77b` |

The charter itself, `BATCH_07_STATUS.md`, is independently confirmed as a
regular mode-`0644`, link-one, strict-UTF-8/LF file of 20,052 bytes and 376
LF, with SHA-256
`2f720b0783569d118f17122613584915a7315ae61b27454b46fbb807852c1bb9`.
It has no BOM, NUL, or CR byte and exactly one terminal LF.

Using the charter's canonical framing (one UTF-8 line per lexicographically
sorted path, `path<TAB>bytes<TAB>LF<TAB>mode<TAB>nlink<TAB>sha256<LF>`), the
eight rows recompute to exactly 830 bytes and eight LF, with aggregate
SHA-256
`f65af0d49a23cabf2b278df212d688fdd45c3c557152f394f9123070eeafdd33`.
The aggregate is self-excluding and therefore remains unchanged when the
charter dashboard is created.  Independent `sha256sum`, OpenSSL SHA-256, and
isolated Python digest results agree on every listed identity.

## Batch 06 current state versus audit-opening snapshots

The live `BATCH_06_STATUS.md` header and closure tail report
`COMPLETE_LOCAL_BATCH06` / `BATCH06_CLOSED`, with current live identity
616,461 bytes, 9,095 LF, and SHA-256
`5c95ac0f195ae7de935b0c2cc902ebcf6df15f0cb7292835d1c51ea208d45609`.
The live `BATCH_06_IDEA_REPORT.md` identity is 675,259 bytes, 12,068 LF, and
SHA-256
`2e097d928bbe695866653c47aace6215358e0187326044e8eb548fddd3cd1ef3`.

`BATCH_06_FINAL_AUDIT.md` records the smaller identities consumed at that
audit opening: STATUS 613,682 bytes / 9,043 LF /
`3efa38f369d9efa3e2e3a6bb7f8492cff7b122ea11d798f3cfb3a7cc207e0ae6`, and
IDEA 672,431 bytes / 12,016 LF /
`ba36bdbcba7de936860e5b1b01c6eabaf68973b263747d265207b620a9619ddc`.
Those are historical audit-opening snapshots, not the Batch 07 inputs.  The
later B06 closure prose that temporarily transcribed 9,019 and 11,992 LF is
explicitly corrected as historical, non-authoritative, and non-consumed.  The
two inherited malformed hash tokens, the duplicated descriptive terminal-gate
sentence, and their corrections are likewise explicitly dispositioned in the
append-only B06 ledgers and cannot control an active transition.  The larger
current identities in the manifest therefore correctly control this start.

## Inherited terminal boundary

The B06 status, B06 idea report, B06 final audit, README, and registry agree on
the following five closed states:

| Paper | Terminal disposition | Effect carried into Batch 07 |
|---:|---|---|
| 22 | `COMPLETE_LOCAL_FINAL_REVIEW_PASS` | local anonymous only |
| 23 | `TERMINAL_LOCAL_EVIDENCE_RECOVERY_BLOCKED` | source/PDF retained; no release |
| 24 | `TERMINAL_LOCAL_R1_BUILD_BLOCKED` | source/PDF retained; no release |
| 25 | `COMPLETE_LOCAL_FINAL_REVIEW_PASS` | local anonymous only |
| 26 | `TERMINAL_LOCAL_R0_AUTHORITY_BOUNDARY_BLOCKED` | no realized build/PDF/release |

The B06 blockers are terminal boundaries, not active Batch 07 findings: Paper
23's evidence-history failure cannot be recovered; Paper 24's missing
time-indexed R1 checkpoint cannot be backfilled; and Paper 26's permanent
authority boundary prevents any realized build or release.  No B06 success or
blocker grants downstream authority, retry, relabel, replacement, or reuse in
Batch 07.

## Queue and Paper 27 preexistence

The five queue rows are exactly Papers 27, 28, 29, 30, and 31.  Their project
path cells are respectively `absent until candidate dual-PASS`, `absent`,
`absent`, `absent`, and `absent`; their effects are all `none`.  Paper 27 is
at `CANDIDATE_DISCOVERY_OPEN`, while Papers 28--31 are explicitly queued
serially behind the independently reviewed terminal disposition of the
immediate predecessor.  No candidate ID, public title, project directory,
source-design file, manuscript, lock, build root, PDF, release artifact,
README row, or registry row is authorized for Paper 27.

The no-follow immediate-child check of workspace `papers` found no directory
whose name matches `27-*`, and no symlink immediate child was followed.  This
check did not enumerate or inspect nested project files and did not probe any
temporary, closed, or future build root.  The inherited README and registry
contain the five B06 rows only; neither contains an unauthorized Paper 27
row or candidate identifier.

## Candidate gate and proof-first boundary

Paper 27 can consume a number and open a project only after two fresh,
mutually independent reviews pass all nine conjunctive requirements:

1. an exact public-safe headline theorem with family, assumptions,
   conclusion, equality cases, and failure boundary;
2. a bounded primary-source search through the decision date, with query log,
   limitations, novelty at least `7.5 / 10`, and no absolute priority claim;
3. standalone mathematical value at least `7.5 / 10` after predecessor
   absorption and direct-collision deductions;
4. proof confidence at least `9.0 / 10`, with a complete proof spine, literal
   formula checks, field/scheme qualifications where relevant, and adversarial
   counterexamples;
5. a direct collision matrix against Papers 12--26 and the closest verified
   published or current primary sources;
6. explicit anti-claims, excluded regimes, equality walls, and assumption-
   failure examples;
7. no headline dependence on an empirical run, numerical fit, CAS
   certificate, broad finite search, or unverifiable computation;
8. a credible anonymous 22--30 content-page proof-first article after
   governance, paths, hashes, and discovery narrative are removed; and
9. exact noncollision with the five candidates intended for this batch.

R1 independently assesses theorem size, current literature, collision, and
proof plausibility.  R2 independently rederives theorem-critical algebra and
attacks every assumption without reading R1's private reasoning.  A PASS
review is the reviewer's only write and is allowed only at an all-zero finding
census.  Failure is `FAIL / WRITE NOTHING`; corrections are separately named
immutable records.  No candidate, conjecture, or computation-dependent result
is promoted; a failed or borderline candidate is `STOP` without consuming
Paper 27.

The four discovery lanes are separated and require multiple candidates,
killed-collision records, counterexamples, and at most two proof-credible
finalists per lane.  Read-only scouting may be parallel, but formal projects
remain serial.  The proof-first pilot explicitly checks gradients/maps,
selector inequalities, invariant cones or fans, carry terms, leading-form
noncancellation, coordinate visibility, spectral/recurrence formulas, and a
sharp boundary or counterexample.  Exact fixtures may expose a false claim
but never establish a true headline theorem; GPU hours are zero by design.

## Serial lifecycle and authority consumption

After dual candidate PASS and formal opening, one paper proceeds alone through
the following ordered gates:

1. exact ten-file proof/citation/novelty source-design author stop;
2. fresh independent `SOURCE_DESIGN_PASS`;
3. strict-canonical source lock and fresh `SOURCE_LOCK_PASS`;
4. proof-only article plan and fresh `PAPER_PLAN_PASS`;
5. publication-stage scope and fresh independent scope review;
6. publication lock and fresh `PUBLICATION_LOCK_PASS`;
7. exact anonymous source trio and formal source review, with a fresh reviewer
   and separately frozen revision after any repair;
8. a source-bound build-profile mechanical/semantic gate only when a custom
   harness is genuinely necessary, otherwise the standard deterministic
   profile;
9. one-shot two-root deterministic R0, independent R1, and at most one
   explicitly bounded source-revision window;
10. deterministic R1 rebuild and fresh independent R2, or a terminal blocker
    for any missed time-indexed evidence obligation;
11. finalization scope, lock, lifecycle-DAG validation, and independent review;
12. exclusive raw-byte local candidate copy and release manifest;
13. two fresh terminal rebuilds with exact receipt comparison; and
14. a sole terminal-integrity review by a role distinct from source, build,
    finalization, and release roles, followed only then by exact cleanup.

No downstream authority is inherited from a predecessor PASS.  A blocker
writes no PASS artifact.  Once a number is consumed, a terminal blocker closes
that numbered project and forbids retry, replacement candidate, alternate
project, or relabeling under the same number.  The maximum effect is
`LOCAL_ANONYMOUS_RELEASE_ONLY` unless separately and explicitly authorized by
the user.

## Deterministic build, one-shot, and cache safeguards

The charter requires every authorization to name exact allowed paths and two
fresh mode-`0700` roots whose nonexistence is checked immediately before first
creation.  Future paths are never pre-created or inspected.  `PATH`,
`SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, `TZ`, `LC_ALL`, and `LANG` are pinned;
executable path, stat identity, and hash are captured before the first build
command.  Each root receives exact frozen source bytes and one frozen command
sequence.  Retry, extra command, package installation, network, alternate
builder, root reuse, and post-hoc evidence repair are forbidden.

Invocation-time source-trio hashes, raw command statuses, logs, opening and
closing manifests, and cross-root comparisons are mandatory.  Later output
equality cannot backfill a missing pre-command observation.  Compiler,
`py_compile`, import-cache, and bytecode-cache creation are forbidden;
administrative Python must use an isolated fresh process with
`PYTHONDONTWRITEBYTECODE=1` and direct script/stdin execution, with cache scans
before and after every phase.  Any cache byte is a hard action-history
failure, and deleting it cannot cure the history.

JSON must be recursively canonicalized and independently round-tripped, with
unsafe integers, duplicate keys, non-finite values, stale aliases, and
unreachable claims rejected by hostile tests.  PDF review covers raw bytes,
objects and decoded streams, dates, fonts, security, pages, visual rendering,
theorem text, citations, and the anonymous metadata/provenance firewall.
Warnings are not silently reclassified as success.  Failure evidence is
quarantined and preserved; authorized cleanup uses exact no-follow targets
only.

## Append-only and machine-event schema

`BATCH_07_STATUS.md` is the controlled dashboard.  Its passport and queue
change only at validated transitions; historical events remain immutable.
`BATCH_07_IDEA_REPORT.md` is absent at this gate and may be created only after
Paper 27 dual PASS, append-only thereafter.  Every author stop freezes a
regular-file, non-symlink universe with safe POSIX relative paths, SHA-256,
bytes, LF count, mode, link count, and a self-excluding aggregate.

All later ledger additions must be physical EOF appends bound to the
pre-append parent hash and byte offset.  Textual-anchor insertion is forbidden
and a unique monotone event identifier is the only active transition
authority.  Human prose never overrides machine fields; any typo, duplicate,
stale counter, or superseded hash is historical and non-authoritative only
after an explicit append-only disposition names the exact error and canonical
replacement.  Reviewers author none of the artifact under review; an
all-zero PASS is their only permitted write.

E0001 is a complete genesis transition.  Its fields are internally present
and consistent: `event_id: B07-E0001-CHARTER`, `seq: 1`,
`event_time: 2026-08-28T11:59:24Z`, genesis parent sentinel
`null-new-ledger`, identical pre/post self-excluding aggregate
`f65af0d49a23cabf2b278df212d688fdd45c3c557152f394f9123070eeafdd33`,
author `batch07-primary-charter-author`, pending fresh-charter reviewer,
the exact eight opening paths, created path `BATCH_07_STATUS.md`, consumed
authority `user-explicit-next-five-round-2026-08-28`, controlling next gate
`BATCH07_CHARTER_FRESH_AUDIT_REQUIRED`, terminal field value
`BATCH07_CHARTER_OPEN`, `authoritative: true`, `historical: false`, and
`supersedes: none`.  The required machine keys
`event_id`, `seq`, `parent_ledger_sha256`, `pre_manifest_sha256`,
`post_manifest_sha256`, `author_role`, `reviewer_role`, `opening_paths`,
`created_paths`, `consumed_authority`, `next_gate`, `terminal_marker`,
`authoritative`, `historical`, and `supersedes` each occur in the transition
block.  Duplicate event IDs or terminal markers, sequence gaps/reversals,
non-EOF appends, stale parent hashes, invalid manifests, and paths outside an
allowlist invalidate a transition and open no authority.

The charter's terminal marker value is an event field, not an exact-line
terminal marker.  Counting only complete lines in `BATCH_07_STATUS.md` finds
exactly one `BATCH07_CHARTER_OPEN` line, at the physical EOF; the field
occurrence is deliberately not counted as a second exact-line marker.

## Closure and Paper 32 boundary

Batch 07 may close only after Papers 27--31 each have an independently
reviewed terminal disposition, whether local anonymous release PASS or a
terminal non-release blocker.  A fresh cross-paper auditor must then read
exactly the five project trees plus the four named Batch 07 summary/index
documents, without protected/future-root access, build, or external effect.
Only an all-zero census permits that auditor alone to create
`BATCH_07_FINAL_AUDIT.md` with its unique terminal marker.  Any finding
requires `FAIL / WRITE NOTHING`, an explicit parent append-only disposition,
and a fresh distinct retry.  A later bounded closure transition may freeze the
trees, README, and registry, report release and terminal counts separately,
and set the paired local-closure markers.  Paper 32 or any later batch is
forbidden without new explicit user authority.

## Finding census

All checks below were completed within the restricted read boundary.  A
historical B06 typo, duplicate descriptive line, stale LF transcription, or
smaller audit-opening identity is not an active finding because the consumed
ledgers explicitly mark it non-authoritative/non-consumed and preserve the
canonical replacement.

| Finding category | Count |
|---|---:|
| Authorization and Papers 27--31 scope | 0 |
| Current B05/B06 identity, bytes, LF, mode, nlink, UTF-8 | 0 |
| 830-byte / 8-LF manifest framing and aggregate | 0 |
| B06 current-versus-audit-opening distinction | 0 |
| Five inherited B06 terminal states or effects | 0 |
| Queue project/ID/title/path leakage | 0 |
| Paper 27 direct-child preexistence or symlink-following | 0 |
| Permission, no-write, or external-effect violation | 0 |
| Candidate-gate threshold, proof, or role defect | 0 |
| Serial lifecycle or downstream-authority defect | 0 |
| One-shot, deterministic-build, cache, or evidence-safeguard defect | 0 |
| Append-only, correction, or machine-event-schema defect | 0 |
| Closure, final-audit, or Paper 32 boundary defect | 0 |
| Charter marker multiplicity/placement | 0 |
| Charter UTF-8/LF/mode/nlink/byte/hash identity | 0 |
| Hidden mutation, forbidden read, or unlisted-path access | 0 |
| Unresolved historical duplicate, typo, or stale prose after disposition | 0 |

Severity census: Blocker `0`; Major `0`; Minor `0`; Ambiguity `0`.

## Conclusion

The frozen charter is internally coherent, the eight inherited inputs and
self-excluding aggregate are exact, Batch 06's current closure is correctly
distinguished from its audit-opening snapshots, and no Paper 27 object or
identifier has been created.  The broad discovery label is subordinate to the
fresh-charter-audit controlling subgate.  All candidate, lifecycle, build,
cache, append, correction, closure, anonymity, and no-external-effect limits
are explicit and enforceable.  No active finding remains, so this sole review
artifact is the authorized all-zero PASS and no downstream authority is
created by it.

BATCH07_CHARTER_REVIEW_PASS
