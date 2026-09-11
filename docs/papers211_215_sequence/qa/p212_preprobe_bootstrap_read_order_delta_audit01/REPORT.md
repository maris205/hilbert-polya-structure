# Independent audit of the root-authored pre-read correction

Disposition: ACCEPT_SOURCE_DELTA_ONLY. PSA-F1 is CLOSED for the corrected
426-line source only. There are zero current open observer-source findings
within the manually reviewed finite-observation contract. This is not runtime
acceptance, dependency closure, observer execution or an authorization grant.

Accepted source:
68789ec6ecb134c714bd5b3d552ab4ff1d3433b8f416b78eddcd0b1046bac4e1
(426 lines, 21,323 bytes). Root delta manifest:
9e9e371cf1cf4a69ab49c2785cfa9544626b1e9fad234f50eb56e04e8bb4a103.
The old source 59f7e5060f338a224442ea3e38efffa9c4685e28ab52bf87750d25fb87dc57f5
and [original OPEN finding](../p212_preprobe_bootstrap_source_audit01/FINDINGS.json)
remain frozen. Original audit seal:
7bb9d6e0be690fcd200e2686797bd7de0bc111479656235a06ae9df36550fd18.

## Independent disposition and exact causal check

The reviewer did not author either this observer or the root's three-hunk
correction. Prior private-Git observer and P212 amendment authorship remains
disclosed in the [original audit](../p212_preprobe_bootstrap_source_audit01/REPORT.md);
this delta acceptance does not independently accept that old self-authored
code. I reuse my own preceding source review to check another author's
actual correction, not label my own source an independently accepted fix.

The complete corrected source was read as text in two native ranges,
1-220 and 221-460. The independent actual diff has exactly three hunks
and exit 1 means differences were found, not a failed test. A separate
literal comparison of the already retrieved ASCII source strings confirms
that the three unique substitutions produce the entire corrected source.
No interpreter or AST parsed either source.

At new lines 221 and 270, whole_file gains expected and its sole caller
passes before['stat'], the final resolved-path key obtained by resolve.
At line 229, stable(expected, before) runs before SHA initialization (230)
and the only os.read (234). It follows the pure non-None/regular-kind/size
check (227-228). Those checks consume no content, so this placement closes
the required pre-read ordering even though the new comparison is not
literally the first statement after native(fd) at 226.

For the original finite counterexample, expected=A and the opened fd=B.
If B is not a bounded regular file, the existing guard raises before reading.
If B is a bounded regular file but any of the 13 stable fields differs from A,
the new comparison raises before reading. native has already retained the
actual fd event; finally closes the fd. No target body has been consumed by
this branch. A native error/missing mask likewise stops before the loop.
If the keys match under the contract's atime-excluding policy, the existing
bounded complete-read path proceeds. Same-fd post-read stable/size checks
(247-249), the caller's post-return check (271), resolution brackets,
cross-pass content/membership comparison and closing controls all remain.

The full corrected source and exact three-hunk comparison disclose no other
code change. Native layout/masks, literal controls/frontier, lexical/resolved
alias logic, absence semantics, path-bracketed name-only directory
membership, first-failure stops, finite ceilings and always-false attestation/
author-probe/closure claims retain the original reviewed scope.
Membership is not upgraded to a directory-fd promise. No atomic namespace,
continuous identity, hostile-platform or observer-bootstrap-self-attestation
guarantee is inferred. The explicitly accepted ordinary bootstrap assumption
remains the trust boundary.

## Documentary correction, not another observer-source defect

The root's frozen RESPONSE.md says that no Node operation occurred.
That is historically overbroad. Its DOCUMENTARY_CHECKS_NATIVE contains two
actual Node documentary source-text/hash commands: first failure at the
incorrect MANIFEST.sha256 basename, then the corrected SHA256SUMS check.
Both originals were read here; neither runs the observer or parses Python.

Root additionally disclosed a third Node documentary hash/sealing command
and explicitly superseded the broad sentence. Its raw return is not among
the seven delta files, so this reviewer records that third command as an
author disclosure, not a third independently inspected native original.
[AUTHOR_CLARIFICATION.md](AUTHOR_CLARIFICATION.md) preserves this distinction.
The corrected claim is no P212 observer, author probe, Python source parse/
test, operational Node/P212 query or build execution. This wording correction
does not modify the frozen source or frontier, nor erase the first failed
documentary attempt. This audit invokes no Python or Node process itself.

SOURCE_READ_NATIVE in the delta contains the original 425-line source read,
not the corrected source. Its complete JSON was actually read and its
embedded output equals the old source. Corrected-source evidence here is
the reviewer's own two complete native reads, not a mislabeled author read.

## Integrity and remaining HOLD boundaries

The six root-delta payload hashes passed; all seven delta input pins passed;
the original 17 payloads and original audit's nine payloads passed unchanged.
All 36 original documentary inputs also passed. This packet directly pins
53 unique documentary inputs (all seven delta files, ten old-audit files,
and 36 original inputs), with 2,074,852 total bytes and identical before/after
SHA256 output. These are documentary hashes, not native runtime field keys.

[READS_NATIVE.json](READS_NATIVE.json) retains 23 actual documentary commands
including the full source/diff/JSON reads and checks. [TEXT_COMPARISON.json](TEXT_COMPARISON.json)
records the in-memory literal source-text comparison. [READ_SCOPE.md](READ_SCOPE.md)
states reuse and exclusions. [FINDINGS.json](FINDINGS.json) closes only PSA-F1
against the exact corrected source.

FRONTIER remains 164 targets/204 literal components, with its seven declared
closure gaps intact. Exact current libffi and _ctypes ELF dependencies,
Python normal/error imports and startup states, six Node builtin sources/
lazy/native effects, current configuration-driven paths, native masks and
actual field values remain unreceived. No host configuration, dependency,
proc/environment/credential state was queried. No observer/probe/driver,
Python source parser/test, Git/SSH, build or external phase was invoked.

Root must still inspect the actual final originals, issue its distinct
source receipt if satisfied, and separately authorize any finite observation.
Even a future successful observation is not author-probe permission or
operational closure. This audit grants no execution and preserves all such
HOLD boundaries.
