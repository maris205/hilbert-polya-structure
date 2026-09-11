# P212 driver revision02 — response to the same source reviewer

2026-09-09 UTC. Author: /root/round211_finite_matching_scout.
Status: SOURCE_ONLY_REVISION_SUBMITTED / SAME_REVIEWER_DELTA_PENDING /
HOLD_OPERATIONAL. This author does not decide whether DQD-S1 is closed.

## Exact target and scope

The original reviewed preparation01 remains unchanged: driver938 lines /
49,231 bytes, SHA256
fc61b463fbb8cb6c09887f12a85152e9e345c242ec0c3693621f396c42066381,
old package seal bbb6bed92196fcb2876db00dc83f0aad41f630f3d738f292f2047e91222d7917.

This new-only [driver.js](driver.js) is978 lines /51,293 bytes, SHA256
57ce0d5815e3b0d051925dd351030d26067eb796a47f7058cf8f3a08c5e90032.
The actual full [DRIVER.diff](DRIVER.diff) is SHA256
c390010877b2f6c1d185cc701d9b9d3e62fde9c924699661fbbc9314b49ba414.
It retains real diff exit1 and timestamp headers, not a synthesized test.
The new disabled companion is byte-identical to the old2599-byte original
(SHA2562f4c78bf3900c919112b70cc6ddfc195b576589cd0f35869df0367c2e2e938c0);
actual cmp returned exit0. There is no enabled binding.

The fixed four older companions and19/53 source-plan contexts are unchanged.
All operational paths except this new SELF/default-companion directory remain
literal and unchanged. The patch does not implement an outer entry, new
queries, host discovery, runtime sampling or a build.

## DQD-S1 — acknowledged and addressed in source; acceptance pending

The review's witness is valid for the old source: q and h tagged body with
content:null could reach readPinned(q,expected) through receiveRef or the
query-result bootstrap, before the eventual full-set rejection.

The repair has two deliberately separate parts:

1. fileForPurpose (358–376) validates an explicit allowed purpose; the lexical
   descriptor must be file/symlink of exactly that role; the separately bound
   referent must be a canonical regular-file descriptor of that same role;
   full declared stat and content channels must agree. Non-body purposes
   require nonnull complete {bytes,sha256} pins on both descriptors.
2. requireBodyRead (378–382) requires bodies phase AND the nonnull accepted
   complete-set capability containing both lexical and resolved spellings.
   It does not inspect an expected-pin argument and cannot be satisfied by
   supplying one. All body-byte entry points use it before open/read.

readPinned (383–413) first checks the purpose descriptor and, for body,
the full-set capability. Then it validates any explicit expected pin and
requires the entire chosen pin. resolveBound observes the complete bound
component chain; non-body reads reject any body-role alias/ancestor in that
chain before opening. The original O_RDONLY/O_NOFOLLOW/O_NONBLOCK handle,
regular fstat, complete byte count/hash and stable before/after handle checks
remain unchanged.

The old witness now stops in fileForPurpose before resolveBound/open:
a body descriptor cannot serve receipt or query_result purpose. Retagging only
the lexical q fails on h's referent role; null content on either non-body side
fails the pre-read pin guard. A body-tagged intermediate alias/ancestor fails
the full-chain non-body guard. Passing an expected pin supplies none of these
missing role/content/capability predicates.

## Complete returned-set transition

Both capability objects start null (240). validateQueryInputs first asserts
that closed state (722). Its38 exact query contexts still decode every
stdout/stderr/result, but all114 reference reads now use query_result purpose
(729–730): full non-body pins and referent/chain checks precede bytes.

The existing complete schema/event/native/raw-line reconstruction remains.
Every ordered body authorization must still match its exact query label,
line index, raw line hex, delimiter and lexical path, with a positive finite
max_bytes. For each record, fileForPurpose(body) now checks both body roles,
regular target, matching metadata/content; resolveBound validates its entire
actual alias chain before the capability opens (781–785).
The final all-body-descriptor loop rejects any unreturned extra body role and
checks its descriptor too (787–790). No first-body bytes are read by any of
these checks; fileForPurpose is descriptor-only, resolveBound reads metadata
and symlink text only.

Only after every loop succeeds, lines792–793 save a copy of the complete
ordered body_requests and install the accepted lexical/resolved set. Those
are the only post-initialization capability assignments. A throw anywhere
earlier leaves the body-byte channel closed.

captureBody begins with fileForPurpose, requireBodyRead and equality to the
saved request at the exact index (797–799), before even its output directory
is created and before the source handle opens at809. The existing ordered
copy loop and duplicate handling remain. snapshot's pre-pinned-body rehashes
are allowed only after the full-set transition and only for paths in that
set; unknown first-body content is still not read by snapshot. The final
complete source reread explicitly uses body purpose/capability (933).

This is source-level control-flow reasoning, not an executed mutation test.
The complete ingress/byte-open coverage is in
[READ_ENTRY_COVERAGE.md](READ_ENTRY_COVERAGE.md).

## Unchanged boundaries, including DQD-O1

DQD-O1 is accepted as a disclosed nonblocking outer-key obligation, not
implemented here. The selected fixed binding file is still the one initial
raw workspace read before descriptors exist (894). Its initial bytes,
lexical/resolved identity and required before/after agreement must be covered
by the separate pre-started outer key. No circular full self-hash is inserted
in that binding, and the inner final snapshot is not claimed to cover it.

All original broader-session/product/runtime limits remain:
pre-start Node/bootstrap/tool/configuration key, exact original product
request/yield/poll/final envelopes, broader owned-session/member/intervention
reception and outer manifest require a separate received implementation.
The detached-group observation is unchanged and not promoted into that
missing implementation. The outer mechanism remains unimplemented/HOLD.

The fixed19 name tuples,53 proposals, four no-generation flags, environment,
query cwd,120-second policy, unknown/unclosed behavior, no automatic retry/
kill/cleanup, source-first semantic frontiers and null lock are unchanged.
No new query/body request, format-generation option, source edge, native tool,
host inventory or manuscript content is introduced. The historical section05
execution prose and later source/profile re-reception obligation remain.

## Evidence and authorship

The author read the entire original938-line driver,253-line staged contract,
all fixed companions, disabled interface and source provenance/pins/native
record, and the same reviewer's exact FINDINGS/REPORT/READ_SCOPE plus independent
context report. Selected complete native read strings, real diff/cmp and
original-preservation hashes are retained in this packet. Broad orientation
display truncation is not advertised as complete source evidence; the complete
source read strings and subsequent bounded relevant rereads remain available.

There were zero driver/emitter/helper runs, imports, AST/syntax/mutation checks,
host queries/inventories/body scans, Python/TeX/BibTeX/build/science/view/Git
operations. Source-only string collation and native workspace text/hash/diff
commands are not driver tests. The supplied disabled companion was copied as
text with apply_patch and compared raw, never executed.

The symbolic-dynamics-research workflow required this dependency-scoped,
new-only delta and the same nonauthor reviewer's actual acceptance. Please
receive this exact source/diff/response, assess the full ingress coverage and
record acceptance or remaining findings separately without changing the old
audit. Root must independently receive the actual delta decision before any
further gate. No author source PASS, reviewer acceptance, operational grant,
paper completion or external action is asserted.
