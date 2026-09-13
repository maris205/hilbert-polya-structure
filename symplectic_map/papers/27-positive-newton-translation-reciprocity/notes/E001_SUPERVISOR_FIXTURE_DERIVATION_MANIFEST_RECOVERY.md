# E001 Supervisor Fixture Derivation Manifest Recovery

## 0. Control status

This file is an inert derivation manifest. It is not a fixture, not source code, not a
test hook, not an execution plan, and not authority to create or run a derived file.
It records a deterministic byte transformation that a separately authorized future
materializer could apply to one sealed normalized V8 byte string. No derived output
is present here.

Control identifier: E001-SUPERVISOR-FIXTURE-DERIVATION-MANIFEST-RECOVERY

Control parent: E0331

Control scope: one future disposable, synthetic, no-build supervisor fixture program

Control encoding: strict ASCII

Control line ending: LF only

Control terminal policy: exactly one terminal LF

## 1. Sealed parent identity

The controlling E0331 ledger identity is:

- device: 2431
- inode: 12439253869
- mode: 0644
- link count: 1
- uid: 0
- gid: 0
- byte count: 1848081
- LF count: 20661
- SHA256: 72d732c9834c7670f22160e73c0391c668f40d271e4fdf1aba986b24217c6b30
- terminal:
  BATCH07_P27_PROBE_RECOVERY_E001_SUPERVISOR_BINDER_V8_DUAL_STATIC_PASS_CONSUMED_AND_ACTOR_DERIVATION_HOST_CONTROL_AUTHORIZED

The sealed normalized V8 marker byte identity declared by E0331 is:

- byte count: 251414
- LF count: 6839
- SHA256: 34449280b51dae17eeb5eb841296e99d25512867185525fec39dc73a39dfc076
- double-quote marker count: 0
- dollar marker count: 0
- backtick marker count: 0

These values are declarations, not observations made by this control. Authorship of
this control does not read, stat, hash, normalize, import, parse, compile, evaluate,
or execute E0331, the V8 file, the V8 marker, a payload, or a fixture. A future
materializer MUST independently prove the complete identities above before it may
derive bytes. Any mismatch is a hard failure with no output.

## 2. Frozen objects and notation

The following notation is descriptive and non-executable.

- B is the exact normalized V8 byte string having the identity in Section 1.
- len(X) is the number of bytes in byte string X.
- lf(X) is the number of 0x0a bytes in X.
- sha(X) is lowercase SHA256 of X.
- slice(B,a,b) is the half-open byte slice beginning at a and ending before b.
- concat(X,Y) is byte concatenation.
- count(X,Y) is the count of non-overlapping exact occurrences of X in Y.
- before(X,Y) means the end offset of X is not greater than the start offset of Y.
- P[r] is the exact preimage byte slice selected for replacement record r.
- Q[r] is the exact postimage byte string defined for replacement record r.
- D[r] is len(Q[r]) minus len(P[r]).
- O[r] is the start offset of P[r] in B.
- I is the future synthetic fixture byte string, if separately authorized.
- A is the inserted synthetic adapter byte block defined by the future materializer
  from the closed adapter grammar in Section 8.
- K is the future scenario-data block defined by the closed scenario table in
  Section 9.

All offsets are offsets in B, never in a partially transformed byte string. All
replacements are applied conceptually in descending O[r] order. This prevents an
earlier length change from shifting a later preimage.

## 3. Normative prohibitions

The transformation described here MUST NOT:

1. modify B, E0331, any production source, any production test, any build output,
   any evidence object, any stage object, any old object, or any payload;
2. create a production branch, environment-controlled production branch, hidden
   hook, test-only production export, optional production callback, or production
   dependency;
3. import or execute a production build artifact from the future fixture;
4. use a production build path, evidence path, source path, payload path, report
   path, lock path, socket path, pid path, or temporary path as fixture data;
5. send a signal to a process not created inside the same synthetic fixture run;
6. name or probe an extant production process group;
7. depend on network access, package installation, a repository build, or generated
   production data;
8. claim to validate a kernel or host premise that cannot be injected mechanically;
9. infer missing anchors, repair malformed bytes, normalize a second time, accept a
   near match, or write partial output;
10. materialize a fixture under authority of this manifest alone.

The only allowed future output is one new disposable program at an explicitly
synthetic no-build destination selected outside every production, build, evidence,
source, stage, old, and payload tree. The default spelling, if separately
authorized, is:

  /tmp/p27-e001-synthetic-supervisor/fixture.mjs

The parent directory MUST be newly created for one fixture run and MUST contain only
synthetic disposable data.

## 4. Exact anchor model

### 4.1 Why preimages are byte expressions

This manifest is authored under a no-access rule for B. It therefore does not copy
or guess source text. Each preimage is nevertheless exact: P[r] is a frozen slice of
the single hash-bound B, selected by the deterministic raw-byte locator below. A
locator is not a fuzzy pattern. It either returns one half-open byte interval or
fails closed.

### 4.2 Raw-byte lexical locator

The future locator is limited to byte scanning. It MUST NOT import, parse, compile,
or evaluate B. It recognizes only the following ASCII lexical facts:

- LF is 0x0a.
- ASCII space and horizontal tab are trivia.
- single-quoted strings are scanned with backslash escape accounting.
- double-quoted strings and backtick strings are forbidden by the sealed marker
  census and cause failure if observed.
- line comments end at LF.
- block comments end at the first following star-slash byte pair.
- balanced parentheses, brackets, and braces are counted only outside strings and
  comments.
- identifier bytes are A-Z, a-z, 0-9, underscore, and hash, with a non-digit first
  byte.
- member and call expressions are bounded only by balanced delimiter depth and the
  nearest comma, semicolon, LF statement boundary, or closing delimiter at the same
  depth.

No JavaScript grammar decision beyond these lexical boundaries is permitted.

### 4.3 Locator tuple

Every P[r] is selected by this tuple:

  (sealed_sha, lexical_region_kind, containing_function_ordinal,
   call_or_literal_family, family_ordinal, left_boundary_rule,
   right_boundary_rule)

The ordinals are zero-based among candidates in increasing byte offset. A tuple is
valid only when all of these conditions hold:

- sha(B) equals the sealed SHA256;
- the candidate interval is nonempty;
- the exact candidate bytes occur once in B;
- the locator run returns the same interval in two independent implementations;
- the interval is outside comments and outside the contents of unrelated strings;
- every expected syntactic neighbor recorded by the applicable replacement class
  is present;
- no two selected intervals overlap.

The future anchor lock report MUST record, for every r, O[r], len(P[r]), lf(P[r]),
sha(P[r]), the first at most 32 bytes as lowercase hex, the last at most 32 bytes as
lowercase hex, and count(P[r],B). The required occurrence count is exactly 1 for
every replacement record. The report is validation metadata, not an additional
derived program and is not authorized by this manifest.

### 4.4 Unique-anchor proof

Uniqueness is proved by exact bytes, not by a function name alone:

1. Bind B by byte count, LF count, and SHA256.
2. Locate each candidate by its locator tuple.
3. Extract P[r] from B.
4. Require count(P[r],B) = 1.
5. Require the second independent locator to return the same O[r] and length.
6. Require the expected predecessor and successor lexical classes.
7. Reject zero candidates, multiple candidates, or differing intervals.

Because B is hash-bound and each extracted P[r] has exact-occurrence count one, the
pair (sha(B), P[r]) identifies one interval. The ordinal is a selection aid, not the
uniqueness proof.

### 4.5 Overlap and order proof

Let R be the complete replacement-record set after all censuses. Sort R by O[r]
ascending and require for every adjacent pair x,y:

  O[x] + len(P[x]) <= O[y]

Equality is allowed; intersection is not. Then construct I by copying untouched
spans of B and substituting Q[r], or equivalently by applying substitutions in
strict descending O[r] order. Both construction methods MUST produce equal bytes.
If they do not, fail closed and produce no fixture.

## 5. Replacement record schema

Every concrete replacement instance has these mandatory fields:

- record id;
- preimage: P[r] = slice(B,O[r],O[r]+len(P[r]));
- required exact occurrence count in B: 1;
- application order: descending O[r], with record id as a non-operative display
  tiebreaker; equal O[r] is forbidden;
- postimage: Q[r], defined by its replacement class;
- length delta: D[r] = len(Q[r]) - len(P[r]);
- LF delta: lf(Q[r]) - lf(P[r]);
- changed-byte class from Section 7;
- containment reason explaining why the bytes exist only in future I;
- semantic seam from Section 9, when applicable;
- expected neighboring lexical classes;
- preimage and postimage SHA256 values in the future anchor lock report.

A record without every field is invalid. A replacement family expands to one record
per selected interval. The expanded record set, not merely the family name, is the
unit checked by the materializer.

## 6. Ordered replacement families

The following family order is normative for census and display. Actual byte
application order remains descending O[r]. Each expanded preimage has exact
occurrence count 1.

### R000: synthetic adapter insertion seam

- Preimage bytes: P[R000], the exact unique zero-width boundary immediately after
  the last import declaration and its terminating LF, represented for locking by
  the full nonempty import-line predecessor plus its terminal LF.
- Occurrence count: 1.
- Display order: 000.
- Postimage bytes: Q[R000] is the same locked predecessor bytes followed by A and
  one LF.
- Length delta: len(A) + 1.
- Changed-byte class: C1 adapter-only insertion.
- Production effect: none; insertion occurs only while constructing new I from
  copied B and never touches B or a production path.

R000 fails if there is no import, if the last import boundary is ambiguous, or if A
would split a token, string, comment, or statement.

### R010: production path and locator literal neutralization

- Preimage bytes: each exact single-quoted string token selected by the complete
  negative path census in Section 11, including quote delimiters.
- Occurrence count: 1 for each expanded record R010.n.
- Display order: increasing original token offset.
- Postimage bytes: one exact single-quoted synthetic token from Section 10 having
  the same semantic role and no production substring.
- Length delta: exact synthetic token length minus exact preimage token length.
- Changed-byte class: C2 synthetic literal substitution.
- Production effect: none; no file in a production tree is changed or referenced.

No selected path token may be left unchanged. Node built-in module specifiers and
language protocol words are not path tokens and are handled by the allowlist.

### R011: production evidence and payload data neutralization

- Preimage bytes: each exact single-quoted non-path data token identified by the
  negative data census in Section 11.
- Occurrence count: 1 for each expanded record R011.n.
- Display order: increasing original token offset.
- Postimage bytes: an exact synthetic label, digest, context, report fragment, or
  opaque byte spelling from Sections 9 and 10.
- Length delta: len(Q[R011.n]) - len(P[R011.n]).
- Changed-byte class: C2 synthetic literal substitution.
- Production effect: none; all future inputs are generated inside the disposable
  synthetic directory.

### R020: clock read redirection

- Preimage bytes: each exact callee atom at a deadline-relevant monotonic or wall
  clock read callsite selected by lexical call-family census.
- Occurrence count: 1 for each expanded record R020.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001ClockNow.
- Length delta: 13 minus len(P[R020.n]).
- Changed-byte class: C3 callee-only adapter redirection.
- Production effect: none; e001ClockNow exists only in inserted A in future I.

The argument bytes, parentheses, assignment target, comparison, and surrounding
branch bytes MUST remain byte-identical.

### R021: timer scheduling redirection

- Preimage bytes: each exact callee atom at a supervisor deadline timer scheduling
  callsite.
- Occurrence count: 1 for each expanded record R021.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001SetTimer.
- Length delta: 12 minus len(P[R021.n]).
- Changed-byte class: C3 callee-only adapter redirection.
- Production effect: none; synthetic scheduler state is local to future I.

### R022: timer cancellation redirection

- Preimage bytes: each exact callee atom at a matching deadline timer cancellation
  callsite.
- Occurrence count: 1 for each expanded record R022.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001ClearTimer.
- Length delta: 14 minus len(P[R022.n]).
- Changed-byte class: C3 callee-only adapter redirection.
- Production effect: none; no production timer API is modified.

### R030: child spawn redirection

- Preimage bytes: each exact callee atom that creates the supervised child or its
  recovery child.
- Occurrence count: 1 for each expanded record R030.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001Spawn.
- Length delta: 9 minus len(P[R030.n]).
- Changed-byte class: C3 callee-only adapter redirection.
- Production effect: none; e001Spawn can create only in-memory synthetic child
  handles unless the separately authorized runner permits a child under the same
  disposable directory.

Arguments and options MUST remain unchanged except for tokens independently covered
by R010 or R011.

### R031: process signal redirection

- Preimage bytes: each exact callee atom at a signal-delivery callsite used by the
  supervisor or recovery path.
- Occurrence count: 1 for each expanded record R031.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001Signal.
- Length delta: 10 minus len(P[R031.n]).
- Changed-byte class: C3 callee-only adapter redirection.
- Production effect: none; the adapter accepts only handles created by e001Spawn and
  rejects every numeric or external process identity.

### R032: process-group existence redirection

- Preimage bytes: each exact callee atom at a process-group probe or group-absence
  decision input callsite.
- Occurrence count: 1 for each expanded record R032.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001GroupProbe.
- Length delta: 14 minus len(P[R032.n]).
- Changed-byte class: C3 callee-only adapter redirection.
- Production effect: none; group state is a synthetic table owned by A.

This family tests only the existing group-absence logic. It does not claim that a
real operating-system group is absent.

### R040: raw stdout source redirection

- Preimage bytes: each exact member-expression receiver atom that binds or consumes
  the supervised child's stdout stream.
- Occurrence count: 1 for each expanded record R040.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001RawStdout.
- Length delta: 14 minus len(P[R040.n]).
- Changed-byte class: C4 stream-receiver adapter redirection.
- Production effect: none; chunks are fixed synthetic byte arrays.

The event name, listener body, buffer accounting, LF handling, and report logic MUST
remain byte-identical.

### R041: raw stderr source redirection

- Preimage bytes: each exact member-expression receiver atom that binds or consumes
  the supervised child's stderr stream.
- Occurrence count: 1 for each expanded record R041.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001RawStderr.
- Length delta: 14 minus len(P[R041.n]).
- Changed-byte class: C4 stream-receiver adapter redirection.
- Production effect: none; stderr cannot alias stdout in A.

### R042: child exit and close event source redirection

- Preimage bytes: each exact receiver atom for child exit, error, or close event
  observation.
- Occurrence count: 1 for each expanded record R042.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001ChildEvents.
- Length delta: 15 minus len(P[R042.n]).
- Changed-byte class: C4 stream-receiver adapter redirection.
- Production effect: none; event delivery is a deterministic synthetic queue.

### R050: report write redirection

- Preimage bytes: each exact callee atom that opens, writes, appends, renames, or
  commits the supervisor report.
- Occurrence count: 1 for each expanded record R050.n.
- Display order: increasing callsite offset.
- Postimage bytes: the role-specific identifier e001ReportOpen,
  e001ReportWrite, e001ReportAppend, e001ReportRename, or e001ReportCommit.
- Length delta: len(Q[R050.n]) - len(P[R050.n]).
- Changed-byte class: C5 file-operation adapter redirection.
- Production effect: none; A rejects every path outside the fresh synthetic root.

### R051: report close redirection

- Preimage bytes: each exact callee atom that closes or finalizes a report stream or
  descriptor.
- Occurrence count: 1 for each expanded record R051.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001ReportClose.
- Length delta: 15 minus len(P[R051.n]).
- Changed-byte class: C5 file-operation adapter redirection.
- Production effect: none; close success and mechanically injectable close faults
  apply only to synthetic handles allocated by A.

### R060: handshake input redirection

- Preimage bytes: each exact receiver or callee atom from which the supervisor gets
  a child-ready or recovery-ready handshake.
- Occurrence count: 1 for each expanded record R060.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001Handshake.
- Length delta: 13 minus len(P[R060.n]).
- Changed-byte class: C6 protocol-input adapter redirection.
- Production effect: none; only fixed synthetic protocol bytes are admitted.

### R061: context source redirection

- Preimage bytes: each exact callee or receiver atom used to obtain the expected,
  wrong, or opposite supervisor context.
- Occurrence count: 1 for each expanded record R061.n.
- Display order: increasing callsite offset.
- Postimage bytes: ASCII identifier e001Context.
- Length delta: 11 minus len(P[R061.n]).
- Changed-byte class: C6 protocol-input adapter redirection.
- Production effect: none; contexts are fixed labels with no production identity.

### R070: scenario selector literal

- Preimage bytes: the exact unique existing default-mode literal token at the
  supervisor entry boundary, selected only if its substitution cannot change a
  branch operator or add a branch.
- Occurrence count: 1.
- Display order: 070.
- Postimage bytes: exact single-quoted token 'E001_SCENARIO_FROM_ARGV'.
- Length delta: 25 minus len(P[R070]).
- Changed-byte class: C2 synthetic literal substitution.
- Production effect: none; the selector is interpreted only by A in future I.

If no existing default-mode literal can carry a selector without modifying the
production branch/function skeleton, R070 is omitted and A MUST derive the scenario
only from an existing argument already passed at R030. Adding a new production-side
scenario branch is forbidden.

### R080: fixture terminal insertion

- Preimage bytes: the exact final nonempty LF-terminated line of B.
- Occurrence count: 1.
- Display order: 080.
- Postimage bytes: the same exact line, followed by one LF-delimited inert fixture
  terminal comment held inside A's allowed trailer grammar.
- Length delta: exact trailer length plus 1.
- Changed-byte class: C7 synthetic identity trailer.
- Production effect: none; trailer exists only in future I.

R080 is forbidden if B lacks exactly one terminal LF or if adding a comment would
alter an unterminated token. The fixture trailer spelling is:

  E001_SYNTHETIC_SUPERVISOR_FIXTURE_END

The language-specific comment delimiter MUST be copied from a unique existing line
comment delimiter in B. No executable statement may be added in R080.

## 7. Changed-byte-class allowlist

Only these future I changes relative to B are allowed:

- C1: one adapter-only insertion after the last import declaration;
- C2: complete replacement of a selected single-quoted production data or path
  token by a single-quoted explicitly synthetic token;
- C3: callee identifier or member-receiver atom substitution at a mechanically
  injectable operating-system boundary;
- C4: receiver atom substitution for synthetic raw stream or child event sources;
- C5: callee identifier substitution for synthetic report operations;
- C6: receiver or callee substitution for synthetic handshake and context inputs;
- C7: one inert terminal identity comment.

All other byte changes are forbidden. In particular, these production-side byte
classes MUST be identical between B and I outside A:

- branch keywords and conditional operators;
- comparison, boolean, arithmetic, and bitwise operators;
- catch and finally structure;
- return, throw, break, and continue statements;
- function, class, and method declarations;
- function parameter lists;
- variable binding names, except the exact boundary atoms selected above;
- protocol state-transition labels after R011 neutralization;
- buffer length checks and overflow arithmetic;
- deadline and sticky-deadline predicates;
- recovery dispatch conditions;
- report truncation checks;
- ordering of signal, close, report, and recovery actions;
- import and export statement bytes;
- public API names and arities.

## 8. Closed synthetic adapter grammar

A is permitted to contain only the following declarations and fixed data. The exact
formatting style, declaration keyword, quote style, semicolon style, and LF style
MUST be copied from unique prevailing forms in B. A MUST be delimited by inert line
comments bearing these ASCII labels:

  E001_SYNTHETIC_ADAPTER_BEGIN
  E001_SYNTHETIC_ADAPTER_END

Allowed declaration names are exactly:

- e001ClockNow
- e001SetTimer
- e001ClearTimer
- e001Spawn
- e001Signal
- e001GroupProbe
- e001RawStdout
- e001RawStderr
- e001ChildEvents
- e001ReportOpen
- e001ReportWrite
- e001ReportAppend
- e001ReportRename
- e001ReportCommit
- e001ReportClose
- e001Handshake
- e001Context
- e001Scenario
- e001SyntheticRoot
- e001SyntheticState

No adapter name may be exported. No adapter declaration may be inserted into an
existing production function. A can be referenced only by the exact replacement
records in Section 6.

The adapter contract is:

1. e001ClockNow returns the next integer in a scenario's declared time sequence and
   repeats the final integer after exhaustion.
2. e001SetTimer records a callback and deadline in an in-memory queue. It does not
   call a host timer unless the future runner explicitly chooses the real-time
   conformance scenario, which is outside this manifest.
3. e001ClearTimer marks only a synthetic timer as cleared.
4. e001Spawn returns a synthetic child handle whose stdout, stderr, exit, error, and
   close channels are distinct.
5. e001Signal accepts only a synthetic child handle token created during the same
   run. It records the requested signal and returns or faults as declared.
6. e001GroupProbe reads only the synthetic group's declared state.
7. e001RawStdout and e001RawStderr are separate raw-byte emitters. Neither may
   decode, normalize, merge, reorder, or append LF.
8. e001ChildEvents emits only the declared ordered event sequence.
9. report adapters allocate only in-memory handles or paths below
   e001SyntheticRoot. They enforce root containment before every operation.
10. e001ReportClose can return success, callback error, synchronous error, premature
    close, or duplicate-close observation only as declared by the scenario.
11. e001Handshake returns declared opaque bytes and context labels.
12. e001Context returns one of the exact context labels in Section 9.
13. e001Scenario accepts only an exact scenario id from Section 9 and rejects every
    other value before any spawn, signal, or file operation.
14. e001SyntheticState is created afresh for each run and is never shared.

A MUST NOT contain dynamic import, eval, Function construction, network access,
shell invocation, package loading, repository lookup, production path lookup,
environment-variable fallback, random input, current process enumeration, numeric
PID signaling, process-group signaling, or recursive filesystem traversal.

## 9. Closed scenario and injection table

The future fixture accepts exactly one scenario per run. Each scenario changes only
adapter return values, byte chunks, event order, or synthetic fault results. It does
not add a branch to copied production logic.

### S00 handshake success

- Scenario id: E001-HANDSHAKE-OK
- Handshake byte chunks, lowercase hex: 453030312d52454144590a
- Context: E001-CONTEXT-EXPECTED
- Exit: code 0, signal absent
- Purpose: exercise the existing successful ready handshake.

### S01 handshake malformed

- Scenario id: E001-HANDSHAKE-MALFORMED
- Handshake byte chunks, lowercase hex: 453030312d4e4f542d52454144590a
- Context: E001-CONTEXT-EXPECTED
- Exit: code 0, signal absent
- Purpose: exercise existing handshake rejection.

### S02 separate raw streams and LF boundaries

- Scenario id: E001-RAW-SPLIT-LF
- stdout chunks, lowercase hex in order: 6f75742d41 ; 0a6f75742d42 ; 0a
- stderr chunks, lowercase hex in order: 6572722d41 ; 0a6572722d42 ; 0a
- Exit: code 0, signal absent
- Purpose: prove stdout/stderr separation and raw LF preservation across chunk
  boundaries.

The two emitter objects MUST have unequal identities. No chunk may be converted to
text before it reaches copied production logic.

### S03 explicit nonzero exit

- Scenario id: E001-EXIT-NONZERO
- stdout chunks: empty
- stderr chunks, lowercase hex: 73796e7468657469632d6661696c0a
- Exit: code 23, signal absent
- Purpose: exercise nonzero exit handling without a signal.

### S04 explicit signal exit

- Scenario id: E001-EXIT-SIGNAL
- stdout chunks: empty
- stderr chunks: empty
- Exit: code absent, signal E001-SYNTHETIC-SIGTERM
- Purpose: exercise signal classification without sending a host signal.

### S05 sticky deadline

- Scenario id: E001-DEADLINE-STICKY
- Clock sequence: 1000, 1001, 1010, 1010, 1011, 1012
- Declared deadline: 1010
- Child event after deadline: exit code 0 at synthetic time 1011
- Purpose: prove that once the existing deadline state is set, a later nominal exit
  cannot erase it.

### S06 stdout overflow

- Scenario id: E001-OVERFLOW-STDOUT
- stdout chunk: one synthetic byte array whose length is exactly the existing limit
  plus 1, generated in A without a production data literal
- stderr chunks: empty
- Purpose: exercise existing stdout overflow accounting and termination.

The existing limit value and arithmetic bytes MUST remain unchanged.

### S07 stderr overflow

- Scenario id: E001-OVERFLOW-STDERR
- stdout chunks: empty
- stderr chunk: one synthetic byte array whose length is exactly the existing limit
  plus 1, generated in A without a production data literal
- Purpose: exercise existing stderr overflow accounting and termination.

### S08 supervisor loss

- Scenario id: E001-SUPERVISOR-LOSS
- Handshake: absent
- Child event sequence: synthetic supervisor-channel close, child remains pending
- Group probe: present before close, absent after copied cleanup dispatch
- Purpose: exercise existing supervisor-loss handling.

This is a protocol-level injected loss. It does not claim to emulate a crashed host
kernel, real parent death, or reparenting semantics.

### S09 report truncation

- Scenario id: E001-REPORT-TRUNCATED
- Report write result: accepts the existing maximum report length minus 1 and then
  returns premature completion
- Close result: success
- Purpose: exercise existing truncated-report detection.

The truncation point is derived from the unchanged production bound; it is not a
replacement of that bound.

### S10 wrong context

- Scenario id: E001-CONTEXT-WRONG
- Context: E001-CONTEXT-WRONG
- Opposite-context flag: false
- Purpose: exercise existing wrong-context rejection.

### S11 opposite context

- Scenario id: E001-CONTEXT-OPPOSITE
- Context: E001-CONTEXT-OPPOSITE
- Opposite-context flag: true
- Purpose: exercise the distinct existing opposite-context path.

### S12 recovery dispatch

- Scenario id: E001-RECOVERY-DISPATCH
- Primary handshake: malformed
- Primary exit: code 71, signal absent
- Recovery handshake: E001 ready bytes
- Recovery exit: code 0, signal absent
- Purpose: exercise the existing transition from primary failure to recovery
  dispatch and successful recovery consumption.

The primary and recovery synthetic child handles MUST be distinct. The copied
recovery predicate and dispatch ordering MUST remain unchanged.

### S13 close callback fault

- Scenario id: E001-CLOSE-CALLBACK-FAULT
- Report close result: callback error with synthetic code E001_CLOSE_CALLBACK
- Child exit: code 0, signal absent
- Purpose: exercise an existing asynchronous close-fault path.

### S14 close synchronous fault

- Scenario id: E001-CLOSE-SYNC-FAULT
- Report close result: synchronous error with synthetic code E001_CLOSE_SYNC
- Child exit: code 0, signal absent
- Purpose: exercise an existing synchronous close-fault path if such a callsite is
  present and mechanically redirectable.

If B has no synchronous close callsite, this scenario MUST be reported as statically
unavailable and MUST NOT be synthesized by adding a production branch.

### S15 process group absent

- Scenario id: E001-GROUP-ABSENT
- Group probe sequence: present, absent, absent
- Signal result after absence: synthetic ESRCH-equivalent result
- Purpose: exercise existing group-absence idempotence and recovery logic.

This scenario validates only branch behavior given an injected absence result. The
host premise that a real group is absent remains static and unclaimed.

### S16 report commit fault after close

- Scenario id: E001-COMMIT-AFTER-CLOSE-FAULT
- Close result: success
- Commit or rename result: synthetic code E001_COMMIT_CLOSED
- Purpose: exercise an existing mechanically injectable post-close report fault if
  the corresponding callsite exists.

If the callsite is absent, the scenario is statically unavailable. No callsite may
be added.

## 10. Synthetic path and data dictionary

Every R010 postimage MUST be one of these exact absolute or relative synthetic
tokens, with a decimal suffix added only to distinguish two roles:

- /tmp/p27-e001-synthetic-supervisor
- /tmp/p27-e001-synthetic-supervisor/child
- /tmp/p27-e001-synthetic-supervisor/recovery-child
- /tmp/p27-e001-synthetic-supervisor/report.bin
- /tmp/p27-e001-synthetic-supervisor/report.tmp
- /tmp/p27-e001-synthetic-supervisor/handshake.bin
- /tmp/p27-e001-synthetic-supervisor/context.bin
- /tmp/p27-e001-synthetic-supervisor/group.state
- synthetic-input.bin
- synthetic-output.bin
- synthetic-report.bin
- synthetic-close.state

Every R011 postimage MUST be one of these exact synthetic labels or a lowercase hex
byte string listed in Section 9:

- E001-SYNTHETIC
- E001-CONTEXT-EXPECTED
- E001-CONTEXT-WRONG
- E001-CONTEXT-OPPOSITE
- E001-SYNTHETIC-SIGTERM
- E001_CLOSE_CALLBACK
- E001_CLOSE_SYNC
- E001_COMMIT_CLOSED
- E001-HANDSHAKE-OK
- E001-HANDSHAKE-MALFORMED
- E001-RAW-SPLIT-LF
- E001-EXIT-NONZERO
- E001-EXIT-SIGNAL
- E001-DEADLINE-STICKY
- E001-OVERFLOW-STDOUT
- E001-OVERFLOW-STDERR
- E001-SUPERVISOR-LOSS
- E001-REPORT-TRUNCATED
- E001-CONTEXT-WRONG
- E001-CONTEXT-OPPOSITE
- E001-RECOVERY-DISPATCH
- E001-CLOSE-CALLBACK-FAULT
- E001-CLOSE-SYNC-FAULT
- E001-GROUP-ABSENT
- E001-COMMIT-AFTER-CLOSE-FAULT

No postimage may contain a production hash, inode, device number, path component,
basename, report content, payload fragment, source fragment, build label, evidence
label, stage label, or old-object label, except the immutable V8 input SHA recorded
as manifest metadata and never passed to copied production logic.

## 11. Complete negative path and data census

The future raw-byte scanner MUST examine every single-quoted string token in B and
classify it into exactly one of these disjoint classes:

- L0 language or protocol punctuation with no path or data identity;
- L1 Node built-in module specifier;
- L2 public protocol state label required for branch-skeleton equivalence;
- L3 production build path or build locator;
- L4 production evidence path or evidence locator;
- L5 production source path or source locator;
- L6 production payload path or payload locator;
- L7 production report, lock, pid, socket, temporary, stage, or old path;
- L8 production digest, identity, report fragment, context, payload data, or opaque
  evidence token;
- L9 already explicit synthetic token from Sections 9 or 10.

L3 through L7 MUST expand to R010 records. L8 MUST expand to R011 records. L0, L1,
and L2 may remain only when a second negative scanner proves that they contain none
of the forbidden production substrings and are not absolute or repository-relative
paths. L9 is allowed only inside A or K; an L9 token already in B is an unexpected
condition and causes failure.

The negative scanners MUST reject any unclassified token and MUST search at least
for these case-sensitive and case-folded path concepts:

- build
- evidence
- source
- payload
- fixture
- stage
- old
- report
- lock
- socket
- pid
- probe
- batch
- repository-root spellings
- absolute POSIX path prefix
- dot-relative path prefix
- parent-relative path prefix

Finding a concept does not by itself authorize replacement. It requires exact token
classification. A token whose replacement would alter an import/export statement,
public API, branch label, or production function skeleton causes failure rather
than a guessed rewrite.

After all replacements, scan all of I, excluding only the immutable identity prose
inside inert adapter boundary comments, for every R010 and R011 preimage. The count
of each MUST be zero. Also scan I for every forbidden production substring and
absolute path root identified by the census. Any surviving match causes deletion of
the incomplete temporary output and failure.

## 12. Import and API equality

The following equality is mandatory outside the delimited A block:

1. Extract raw byte slices for every import declaration in B using LF and balanced
   delimiter scanning.
2. Extract the same slices from I after accounting for the R000 insertion offset.
3. Require equal declaration count, equal order, and byte-for-byte equality.
4. Extract every export declaration, exported name, function declaration name,
   parameter-list slice, class method name, and top-level invocation arity by the
   same non-evaluating lexical scanner.
5. Require equal count, equal order, and byte-for-byte equality outside allowed
   callee or receiver atoms.
6. Require no e001 adapter name to appear in an import, export, parameter list, or
   public property key.

Node built-in imports remain exactly as in B. The adapter does not replace an import
specifier. If a mechanically injectable boundary cannot be redirected without
changing an import declaration, that boundary remains static.

## 13. Process, spawn, signal, and stream callsite map

The future callsite lock report MUST provide one row for every relevant B callsite:

  source offset | containing function ordinal | family | original callee SHA256 |
  argument-list SHA256 | disposition | replacement record | scenario coverage

Allowed dispositions are:

- REDIRECTED: exactly one R020 through R061 record covers the boundary atom;
- STATIC_HOST_PREMISE: no safe mechanical injection is possible;
- PURE_LOGIC_UNCHANGED: copied logic consumes an already redirected result;
- OUT_OF_SCOPE: callsite is demonstrably unrelated to supervisor behavior.

At minimum, the census families are:

- child spawn;
- recovery spawn;
- direct process signal;
- process-group signal or probe;
- stdout subscription and consumption;
- stderr subscription and consumption;
- child error, exit, and close observation;
- clock read;
- timer set and clear;
- report open, write, append, rename, commit, and close;
- handshake input;
- context input.

Every family candidate must have a disposition. Every REDIRECTED row must name one
replacement record, and every replacement record in R020 through R061 must be named
by one row. Argument-list SHA256 MUST be identical before and after transformation,
except for separately locked R010/R011 literal tokens inside that list. Signal
callsite mapping additionally requires that no numeric host PID or negative process
group identifier can reach e001Signal.

## 14. Branch and function skeleton equivalence

The equivalence check uses a non-evaluating lexical skeleton. It removes comments,
string contents, numeric literal contents, trivia, and the complete A block, then
replaces every allowed C2 through C6 changed atom by the marker X. It retains:

- all keywords;
- braces, parentheses, brackets, commas, semicolons, colons, and question marks;
- every operator;
- declaration boundaries;
- function names and parameter counts;
- branch nesting and order;
- catch and finally nesting;
- return and throw positions;
- callsite argument counts.

The resulting skeleton for B MUST equal the resulting skeleton for I byte for byte.
Additionally require:

- equal function count outside A;
- equal branch-keyword count outside A;
- equal catch and finally counts outside A;
- equal return and throw counts outside A;
- equal maximum brace, bracket, and parenthesis depth outside A;
- equal ordered list of function ordinals containing recovery dispatch;
- equal ordered list of overflow comparisons;
- equal ordered list of deadline comparisons;
- equal ordered list of report truncation comparisons.

Any difference means the future fixture is not a derivation under this manifest.

## 15. Mechanically injectable versus static premises

Mechanically injectable under this manifest:

- ready and malformed handshake bytes;
- separate raw stdout and stderr chunking;
- LF placement across chunk boundaries;
- zero and nonzero exit codes;
- declared synthetic signal exits;
- deterministic clock reads and timer queue delivery;
- sticky deadline observations;
- stdout and stderr overflow inputs;
- protocol-level supervisor channel loss;
- short report writes and truncation results;
- expected, wrong, and opposite context values;
- primary failure and recovery-child dispatch inputs;
- callback, synchronous, premature, and post-close report faults when the matching
  production callsite already exists;
- synthetic process-group present and absent results.

Static and unclaimed host or syscall premises:

- actual kernel process-group disappearance;
- PID reuse and process-group id reuse;
- real signal permission failure;
- uncatchable signal delivery timing;
- scheduler fairness and host timer precision;
- kernel pipe capacity and atomic-write boundaries;
- filesystem durability, journal ordering, and power-loss behavior;
- real descriptor exhaustion;
- real disk-full, quota, mount, inode, and permission failures;
- operating-system parent death, reparenting, and session semantics;
- cross-platform signal-name and exit-status normalization;
- real close syscall interruption or kernel-level delayed writeback;
- hostile concurrent mutation by another process.

No scenario may be described as covering a static premise. A static premise can be
listed in a future report only as STATIC_HOST_PREMISE.

## 16. Inert derivation algorithm

The following marker-delimited text is pseudocode. It is intentionally not valid
JavaScript, shell, Python, or another executable language.

E001_DERIVATION_PSEUDOCODE_BEGIN

REQUIRE separate materialization authority
REQUIRE input byte string identity equals Section 1 in all fields
REQUIRE input has exactly one terminal LF
REQUIRE double_quote_count = 0
REQUIRE dollar_count = 0
REQUIRE backtick_count = 0

SCAN input bytes with two independent raw-byte lexical locators
BUILD complete literal census from Section 11
BUILD complete boundary-callsite census from Section 13
CLASSIFY every literal and every boundary callsite
EXPAND R010 and R011 once per required literal token
EXPAND R020 through R061 once per safely redirectable boundary atom
SELECT R000 and R080 unique boundaries
SELECT R070 only if the existing default-mode literal rule is satisfied

FOR EACH expanded record r
  LOCK O[r], P[r], len(P[r]), lf(P[r]), sha(P[r])
  REQUIRE count(P[r],B) = 1
  DEFINE Q[r] only from Sections 6, 8, 9, and 10
  LOCK len(Q[r]), lf(Q[r]), sha(Q[r])
  LOCK D[r] = len(Q[r]) - len(P[r])
  LOCK changed-byte class and containment reason
END FOR

SORT records by O ascending
REQUIRE every adjacent interval is disjoint
REQUIRE every required family is present or marked STATIC_HOST_PREMISE
REQUIRE no production literal survives the negative census

CONSTRUCT candidate one time by untouched-span copying
CONSTRUCT comparison candidate one time by descending-offset replacement
REQUIRE candidates are byte equal
REQUIRE branch and function skeleton equivalence
REQUIRE import and API equality
REQUIRE complete one-to-one callsite mapping
REQUIRE synthetic-root containment
REQUIRE changed bytes belong only to C1 through C7
REQUIRE candidate strict ASCII and LF only
REQUIRE candidate has exactly one terminal LF
COMPUTE candidate byte count, LF count, and SHA256
REQUIRE identity recomputation by independent implementation is equal

IF any REQUIRE fails
  CREATE no final output
  REMOVE only the explicitly named incomplete synthetic temporary object
  REPORT failure without payload bytes
END IF

E001_DERIVATION_PSEUDOCODE_END

## 17. Future identity derivation

The future fixture identity is deliberately not materialized in this control. Its
exact byte count, LF count, and SHA256 cannot be known without constructing A, K,
and the expanded replacement registry from sealed B, an operation prohibited during
authorship.

The future materializer MUST record:

- input byte count: 251414
- input LF count: 6839
- input SHA256: 34449280b51dae17eeb5eb841296e99d25512867185525fec39dc73a39dfc076
- expanded replacement count: FUTURE_EXACT_VALUE
- sum of length deltas: FUTURE_EXACT_VALUE
- sum of LF deltas: FUTURE_EXACT_VALUE
- future byte count: 251414 plus sum of length deltas
- future LF count: 6839 plus sum of LF deltas
- future SHA256: FUTURE_EXACT_VALUE
- future terminal LF count: exactly 1
- future encoding: strict ASCII

The FUTURE_EXACT_VALUE fields are fail-closed placeholders, not wildcards. They MUST
be replaced by computed values before any future output is accepted. A placeholder
remaining in a validation record invalidates the output.

The byte-count and LF-count equations MUST be checked before hashing. SHA256 MUST be
computed twice by independent implementations over the exact final bytes. The two
digests and all counts MUST agree.

## 18. Fail-closed validation matrix

The future derivation MUST stop without a final fixture if any of these occurs:

- E0331 identity is not independently established exactly;
- B identity differs in byte count, LF count, SHA256, terminal LF policy, or marker
  census;
- a locator has zero or multiple candidates;
- two independent locators disagree;
- an extracted preimage occurs other than exactly once;
- replacement intervals overlap;
- a postimage is outside the closed dictionary or adapter grammar;
- a production literal survives;
- an import or export byte changes;
- a public API name or arity changes;
- a production function or branch is added, deleted, or reordered;
- a production comparison or state transition changes;
- a callsite lacks a disposition;
- a redirected callsite lacks a one-to-one replacement record;
- a static host premise is represented as mechanically tested;
- stdout and stderr share an emitter identity;
- a stream adapter decodes or normalizes raw bytes;
- a signal adapter can accept a host PID or group id;
- a report adapter accepts a path outside the synthetic root;
- a scenario id is unknown;
- a required scenario needs a missing production callsite;
- a close-fault path would require a new copied-production branch;
- candidate bytes contain non-ASCII or non-LF line endings;
- candidate lacks exactly one terminal LF;
- byte-count, LF-count, or SHA256 recomputation disagrees;
- an identity placeholder remains;
- a final destination is not a fresh disposable no-build synthetic path.

Failure handling may remove only an explicitly named incomplete temporary object
inside the fresh synthetic directory. It may not delete, rewrite, rename, chmod,
chown, or touch any other object.

## 19. Manifest statistics

This control defines:

- 18 ordered replacement-family identifiers: R000, R010, R011, R020, R021, R022,
  R030, R031, R032, R040, R041, R042, R050, R051, R060, R061, R070, and R080;
  R070 is conditional, so 17 are mandatory and at most 18 are active;
- 7 allowed changed-byte classes;
- 17 closed synthetic scenarios, S00 through S16;
- 20 allowed adapter declaration names;
- 12 exact synthetic path/data path tokens;
- 25 synthetic label dictionary entries representing 23 distinct spellings;
- 10 negative literal classes, L0 through L9, with L7 covering multiple path roles;
- 20 minimum atomic boundary-callsite types when grouped event, timer, and report
  operations are counted separately;
- 13 explicitly listed static host/syscall premise classes;
- 27 listed primary fail-closed validation conditions, each with all stated
  identity and destination subconditions.

The authoritative concrete replacement count is not guessed here. It is the size of
the future expanded unique-anchor registry after the mandatory full census.

## 20. Non-production containment argument

The derivation cannot affect production when followed exactly because:

1. B is read-only input and is never a write destination.
2. Every changed byte is emitted only into a new future I at a fresh synthetic path.
3. Every production build, evidence, source, payload, report, and locator literal is
   removed from I by complete census and negative scan.
4. Every external boundary used for a scenario is redirected to an unexported local
   adapter in I.
5. Adapter signals are handle-scoped and cannot address host PIDs or groups.
6. Adapter files are root-contained under one disposable synthetic directory.
7. Imports, exports, public APIs, production function skeletons, and production
   branches remain equal outside the delimited adapter.
8. No production hook, branch, export, or dependency is introduced.
9. Host-only premises remain static and are never converted into unsafe probes.
10. Any ambiguity, mismatch, unclassified literal, unsupported seam, or validation
    difference yields no final fixture.

## 21. Authorship disposition

This control recovers only an inert, exact derivation contract. It creates no
fixture and grants no execution authority. The E0331 and V8 identities in Section 1
remain the sole sealed input identities. Their unchanged status is asserted only by
identity equality to the supplied ledger declaration; this authorship performed no
prohibited access to re-observe them.

BATCH07_P27_E001_SUPERVISOR_FIXTURE_DERIVATION_MANIFEST_RECOVERY_AUTHOR_STOP
