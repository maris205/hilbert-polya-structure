# Independent Build-Profile Review — Paper 27 Probe-Recovery

## Authority and frozen subject

This is the sole aggregate review artifact authorized by
`B07-E0303-P27-PROBE-RECOVERY-CORRECTED-PROFILE-DUAL-PASS-CONSUMPTION-AND-AGGREGATE-AUTHORIZATION`.
Its authorizing ledger has 1,557,569 bytes, 18,404 LF bytes, mode 0644,
link count one, SHA-256
`8489a8ea139709aa1fd6c4003f7138d55392ad9aad6ec5f1b4b42f03c512ebd2`,
and terminal
`BATCH07_P27_PROBE_RECOVERY_CORRECTED_PROFILE_DUAL_PASS_AGGREGATE_AUTHORIZED`.

The reviewed subject is
`papers/27-positive-newton-translation-reciprocity/notes/BUILD_PROFILE_RECOVERY.md`:

- bytes: 62,863
- LF bytes: 1,181
- mode: 0644
- link count: one
- SHA-256: `ac1651c8ef5522f76f52b98a9deb300d5409c489d6e3ae4fa58e9d6e3fc4c985`
- terminal: `BATCH07_P27_BUILD_PROFILE_RECOVERY_AUTHOR_STOP`, standalone once
- encoding: strict UTF-8/LF, with no BOM, CR, or NUL and exactly one terminal LF

The canonical source/control manifest at review time has 105 rows, 16,302
framing bytes, 105 LF bytes, and SHA-256
`1357ebac2377b55edcbb6c5577fc5387c7853d3d22315bf157a7815168b30c69`.
The corrected profile's canonical row is exactly the path above followed by
bytes 62863, LF 1181, integer mode 644, link count 1, and the profile SHA-256.

The embedded first-touch record begins at profile line 544 and ends at line
695.  The marker-delimited raw record has 5,174 bytes, 150 LF bytes, and
SHA-256
`ecc6ed4e2227d1fa84943013b6d28d03f261ee0f9d0d09268f0c57b22c25a4cf`.
The sealed harness has 5,173 bytes, 149 LF bytes, and SHA-256
`b7e5754f2f8a6a31c58316f848eaaebaec2ecb241b14a700cf0b287fc01fb1fe`.
Its last byte is `0x29`; its single-quote, dollar, and backtick counts are all
zero.

Q1 and Q2 received only the exact frozen ledger/profile bytes and their
separate scopes.  Each performed a zero-write, build-blind static review.
Neither reviewer received, requested, or relied on the other's report.  No
embedded code or validator was imported, compiled, AST-parsed, or executed;
no build pathname was listed, probed, stated, read, or modified.

## Complete separated report Q1 — invariant and lifecycle review

### Q1 identity evidence

Q1 independently reproduced the E0302 ledger identity: 1,551,533 bytes,
18,342 LF bytes, mode 0644, link count one, SHA-256
`40d4d95869649daa8453c51aec5f84cf23a0ebb5ec5ae1bee218ff831a2f380a`,
and terminal
`BATCH07_P27_PROBE_RECOVERY_CORRECTED_PROFILE_PHYSICAL_FREEZE_DUAL_REREVIEW_AUTHORIZED`.
Q1 independently reproduced the profile identity, encoding, line-1181 author
terminal, marker lines, raw record identity, sealed harness identity, final
byte, and three forbidden-character counts stated above.  Verdict: PASS.

### Q1 E0301 descriptor correction

The harness retains `held_fds` for `/` and all six literal components through
terminal rewalk, final leaf inspection, and the success emission.  Ordinary
descent never closes an earlier held descriptor.  `rewalk_chain()` starts
from a fresh `/`, opens every component with the frozen directory flags, and
compares `st_dev`, `st_ino`, `st_mode`, `st_uid`, and `st_gid` against the
corresponding held descriptor.  One full rewalk immediately precedes the
leaf-absence decision.  A second full rewalk follows mkdir, child/parent
fsync, drift checks, and empty-inventory checks.  Through that second
rewalk's build descriptor, the harness no-follow lstats and no-follow opens
the literal leaf; both results must match the held child on device, inode,
type/mode, uid, gid, and link count before a final empty-inventory check.
Verdict: PASS.

### Q1 descriptor and exception lifecycle

An exception during initial descent reaches the outer `finally`, which closes
all obtained held descriptors in reverse order.  `rewalk_chain()` catches
`BaseException`, closes every fresh descriptor it obtained, and re-raises.
After mkdir, nested `finally` suites separately close the terminal leaf,
final-rewalk chain, and child; the outer `finally` closes the held chain.
Any close or check exception prevents status zero and therefore cannot be
accepted as success.  Every cleanup action is descriptor-local: none deletes,
renames, chmods, truncates, or otherwise repairs the evidence leaf.  A failure
after mkdir preserves the directory and permanently stops.  Verdict: PASS.

### Q1 absence, sole mkdir, fsync, and terminal rebind

The leaf is checked only relative to the held build-parent descriptor with
`follow_symlinks=False`, and only `ENOENT` is accepted.  The harness contains
exactly one mkdir call, relative to that held parent, with requested mode
0700 under inherited umask 077.  The created leaf is reopened no-follow and
must be a mode-0700 directory with link count two, current effective uid/gid,
and empty inventory.  Child and parent are fsynced; held identities and empty
inventory are checked again.  The terminal full-chain rewalk rebinds the
absolute namespace and the literal leaf as described above.  There is no
retry, fallback, cleanup, rename, chmod, stage creation, certified-root
creation, or stopped namespace in the harness.  Verdict: PASS.

### Q1 single-writer premise and remaining interval

The profile explicitly freezes a single-writer premise from the final
source/control/tool preflight through physical ledger post-binding.  Only the
governed launcher chain may mutate, rename, unlink, mount over, or replace a
literal ancestor, the build parent, or the recovery leaf.  The held chain and
terminal absolute rewalk detect namespace changes up to the final check; the
explicit premise governs the unavoidable interval from that check through
ledger binding.  The profile does not claim that an advisory directory lock
can exclude a hostile writer.  A contrary external mutation invalidates the
run permanently.  Verdict: PASS.

### Q1 argv, environment, umask, and output

The first-touch Python invocation is fixed as
`/root/miniconda3/bin/python3 -S -B -P -c`; the harness requires
`sys.argv == ["-c"]`, the exact workspace cwd, the exact ten-key isolated
environment, and inherited umask 077.  It imports only `errno`, `os`, `stat`,
and `sys`, and does not import or execute the recovery validator.  Success has
one fixed positional printable-ASCII grammar with canonical decimal dynamic
fields and equal device values.  The controlling shell requires status zero,
empty stderr, one LF-terminated accepted stdout line, full positional
validation, and exact replay.  The first-touch creates no receipt or temporary
file and permits no later receipt backfill.  Verdict: PASS.

### Q1 E001 handoff

The receipt-free precedence is limited to first creation of the evidence
directory and expires permanently at physical bootstrap ledger binding.
Beginning with E001, the frozen wrapper, Section 3 capsule, three exclusive
mode-0600 receipts, no-overwrite, first-failure, and no-retry requirements all
resume.  E001 installs only the already independently reviewed recovery
validator with mode 0500.  No receipt exception extends to E001 or a later
row.  E010, A000, root 0, root 1, and cross-root gates remain closed and
strictly ordered.  Verdict: PASS.

### Q1 inherited four-level invariants

1. Source, tool, and dependency: the exact source trio, static-source review,
   complete 87/86 dependency closure, compiler/BibTeX/administrative-tool
   identities, isolated environments, per-command dependency rebind, and
   prohibition on new dependencies remain complete.  Verdict: PASS.
2. Root lifecycle and containment: strict two-root ordering, nine-item
   initialization, four fixed publication commands, per-command receipts,
   snapshots, five raw manifests, root-0-first-failure behavior, no fifth
   run or repair, no cross-root copy, and write containment remain complete.
   Verdict: PASS.
3. Publication and PDF: the 20-key bibliography, 24--28 proof-content pages,
   sentinel/reference equality, warning/error closure, PDF 1.5, portrait and
   metadata constraints, embedded Type1/font checks, raw/decoded provenance
   token, anonymity, and visible-content requirements remain complete.
   Verdict: PASS.
4. Cross-root, evidence, and governance: eight raw equalities, three recorder
   projections, five manifest projections, prohibition on any other
   normalization, build evidence, validator/lock review, runtime microtest,
   fresh build review, separate release-integrity gate, and Paper 28 closure
   remain complete.  Verdict: PASS.

### Q1 active and historical name fence

Q1 reproduced nine active occurrences of `recovery-6103a9df0c3d`, all in
the governed recovery protocol.  It reproduced one occurrence of the stopped
postfail namespace, confined to the explicitly immutable-history paragraph.
Successor/postfail and earlier root names occur only as declared history or
in the inherited frozen E0280 argv0; none is an active runtime namespace.
Recovery profile, validator, lock, profile review, validator review, build
evidence, and build-review basenames agree.  No stale active basename,
terminal, cleanup, release, external-effect, or Paper 28 authority remains.
Verdict: PASS.

Q1 findings: Blocker=0; Major=0; Minor=0; Ambiguity=0.

PROFILE_RECOVERY_Q1_PASS

## Complete separated report Q2 — adversarial review

### Q2 identity evidence

Q2 independently reproduced the same E0302 ledger identity, profile identity,
strict encoding, sole author terminal, raw-record identity, sealed-harness
identity, final byte, and forbidden-character counts.  Verdict: PASS.

### Q2 ancestor rename or replacement

The complete seven-descriptor chain from `/` through `build` remains held to
the success emission.  Opening and terminal full rewalks independently bind
the literal absolute path and compare every component's device, inode,
type/mode, uid, and gid.  A replacement cannot silently convert the held
detached namespace into the governed literal namespace.  Verdict: PASS.

### Q2 leaf race

Only one relative mkdir follows accepted absence.  The held child matches its
initial no-follow lstat.  The terminal rewalk's freshly rebound build
descriptor is then used to no-follow lstat and no-follow open the literal
leaf; both identities must match the held child across device, inode,
type/mode, uid, gid, and link count, followed by another empty-inventory
check.  Verdict: PASS.

### Q2 symlink, mount, and rebind attack surface

All directory opens use `O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC`, and leaf stats do
not follow symlinks.  The two absolute rewalks expose component replacement
before their checks.  Rename, unlink, mount-over, and replacement after the
terminal check are explicitly prohibited throughout physical ledger binding
by the single-writer premise; a violation is permanent invalidation rather
than an accepted run.  Verdict: PASS.

### Q2 terminal-check-to-ledger interval

The single-writer premise begins at final source/control/tool preflight and
continues without a gap through physical ledger post-binding.  It explicitly
covers all literal ancestors, the build parent, and the recovery leaf.  The
profile accurately distinguishes this governance premise from a nonexistent
hostile-writer lock.  Verdict: PASS.

### Q2 descriptor and exception lifecycle

Rewalk exceptions close the fresh chain; nested `finally` suites close the
terminal leaf, final rewalk, child, and held chain.  A close or predicate
exception cannot yield status zero.  Any failure after mkdir leaves the
created directory in place and opens no retry, cleanup, repair, or alternate
branch.  Verdict: PASS.

### Q2 bootstrap circularity

Only the first evidence-directory creation is exempt from the receipts and
installed validator copy that cannot yet exist.  Direct ledger binding ends
that exception permanently.  E001 and every later row again require the full
capsule, receipt, installed-copy, and validator rules.  Verdict: PASS.

### Q2 argv, cwd, environment, and umask

The frozen Python options, exact `sys.argv`, workspace cwd, ten-key isolated
environment, and inherited umask 077 are all tested.  The inherited E0280 FD
scrub and soft-limit launcher retains its frozen argv0.  Verdict: PASS.

### Q2 stdout, stderr, and status grammar

Success produces one fixed-position ASCII/LF frame.  Every dynamic number is
canonical decimal and the two device values must agree.  The controller
requires status zero, empty stderr, full positional validation, and exact
stdout replay.  No failure line can be confused with accepted success.
Verdict: PASS.

### Q2 cleanup, retry, and fallback search

The sealed harness has one mkdir and no unlink, remove, rmdir, rename, chmod,
repair, retry, fallback, stage creation, or certified-root creation branch.
All `finally` work is limited to closing process-local descriptors.  Verdict:
PASS.

### Q2 receipt leakage

First-touch output is captured in memory and physically bound directly in
the next ledger event.  It creates no receipt or temporary file, and no later
receipt may backfill it.  E001 and every later row regain their three
exclusive receipt files.  Verdict: PASS.

### Q2 namespace and basename fence

Q2 reproduced nine active recovery namespace occurrences and one stopped
postfail occurrence confined to immutable history.  There is no stale active
postfail profile, review, lock, evidence, build-review basename, or terminal.
The frozen successor dependency/static-source controls and E0280 argv0 are
explicit inherited exceptions, not active build namespaces.  Verdict: PASS.

### Q2 validator and profile gates

The dual aggregate, recovery validator/lock independent review, isolated
runtime parser microtest, and dual-reviewed first-touch plan all precede any
build touch.  The future validator is required to retain the total 15-mode
parser and all predecessor predicates while rebinding every active recovery
identity.  Verdict: PASS.

### Q2 release scope

Build evidence, independent build review, and a separately authored and
reviewed release-integrity gate remain ordered after successful builds.
Paper 28 remains closed, and any eventual release is local with no external
effect.  Verdict: PASS.

### Q2 inherited four-level semantics

Source/tool/dependency closure; root initialization, snapshots and write
containment; log/bibliography/PDF/anonymity acceptance; cross-root
determinism, evidence, independent review and release governance all remain
complete.  Verdict: PASS.

Q2 findings: Blocker=0; Major=0; Minor=0; Ambiguity=0.

PROFILE_RECOVERY_Q2_PASS

## Aggregate disposition

The reports are independently all-zero and agree on every frozen identity,
the E0301 race correction, the single-writer boundary, first-touch/E001
handoff, active-name fence, inherited invariant, and downstream authority
gate.  Neither report waives, cures, or outvotes a finding from the other;
there is no finding to waive.  Aggregate findings are Blocker=0, Major=0,
Minor=0, Ambiguity=0.

This PASS authorizes no validator byte, parser execution, build-path probe or
creation, PDF action, release action, Paper 28 action, or external effect.  A
later physical-freeze ledger event must bind this exact file before any such
next authority can be considered.  The failed pre-correction profile and its
two Blocker reports remain immutable history and are not retroactively cured.

BATCH07_P27_INDEPENDENT_BUILD_PROFILE_RECOVERY_REVIEW_PASS
