# P212 independent non-lineage keyed-stdin source audit

Verdict: ACCEPT_EXACT_SOURCE_COMBINATION_ONLY_UNDER_ORDINARY_TRUSTED_BOOTSTRAP.
Current source findings: Blocker 0 / Major 0 / Minor 0.
This is an independent source/contract/frontier audit, not root reception,
runtime correctness, mathematical review, input authorization or a hermeticity proof.

## Authorship and exact combination

Auditor: /root/p212_stdin_nonlineage_source_audit. I contributed no P212 proof,
reviewed source, inherited source baseline or line-count erratum. I authored
only this new documentary audit directory. Parent supplied source locations
and identified the limited review and typo; I independently read the full new
sources and checked the complete changed dependency. This is actual process
separation, not a blind review or external specialist assessment.

The accepted combination is the immutable author source packet
p212_keyed_stdin_source_delta01 (55 payloads / 56 files), manifest
f076522fc7e120c46be0c57b60168784c38c32339e07f65b74e0012694ca1ee8,
together with p212_keyed_stdin_linecount_erratum01/ERRATUM.md
(b77fe4fea57429edd7090dbc88387ae2e9280c4be1ea2bd5d059f9bc936ac80b).
The erratum packet's seal is
7876c67cf7a4f436e746bf7ac282868dce74aa7c5ef31063725af815371c4007.

The inherited-baseline contributor's p212_keyed_stdin_source_audit01 is only
LIMITED_CURRENT_DELTA_REVIEW_BY_INHERITED_BASELINE_CONTRIBUTOR. Its seal
2bf279e75d81ad1383bb8eab451b7252bd2d4f0d395a74ccf92d01c1e6970aa6
is not used as independent full-source acceptance. The same reviewer's
line-count delta seal
405df307b2cba91ecb389c9942cacce85929aab7d67a116288f2b318a2c0996a
closes that Minor only. My verdict is based on the independent work below.

## Independent whole-source and delta evidence

All seven new programs were manually read completely: observe.py 436 lines /
22106 bytes; driver.js 1048 / 55092; outer_contract.py 747 / 41004;
python_runtime_probe.py 146 / 8600; node_runtime_probe.js 66 / 5001;
node_preload.js 147 / 10913; product_capture.js 89 / 5830.
Total: 2679 lines / 148546 bytes. All seven related prose documents, complete
ROLE_CLOSURE and SOURCE_ORIGIN, all three disabled interfaces, changed
CAPTURE_CONTRACT companion and complete 2160-line FRONTIER were read.

The own check_delta.cjs invocation (3fd564, exit 0) passed 7082 documentary
checks. It ran 19 actual diff -u comparisons, with Buffer stdout compared
directly to all 19 archived diff files, including timestamps. Eighteen actual
exit-1 changed diffs and one exit-0 empty outer-interface diff are expected.
All 19 entire old/new byte strings reconstruct in both directions: 69 hunks,
654 added / 277 deleted lines; old 5831 lines / 285595 bytes, new 6208 /
313551. The seven program subset is 32 hunks, 204 added / 44 deleted,
2519 old lines / 139752 bytes, 2679 new lines / 148546 bytes.
I also manually read all 19 complete diff bodies (1486 lines / 96926 bytes).

check_receipts.cjs (9c7519, exit 0) passed 803 further documentary checks:
32 actual archived source-display output fields (533879 bytes) equal exact
source renderings byte-for-byte. Numbered nl displays are compared against
the exact numbered rendering, not called raw unnumbered source files.
Unnumbered diff outputs are raw source diff bytes. The attached own delta
and initial pin outputs equal their complete original output fields.
This checks transport attachment and source correspondence, not semantics
of executed reviewed programs.

No claim is made to have freshly manually reread every whole old program:
all old/new bodies were independently whole-byte read/pinned/reconstructed,
all changes manually inspected, and relevant existing source gates fully read.
No unrelated mathematical, runtime, scientific or build gate was reopened.

## Stdin role, expected-key order and actual descriptor handoff

The selected literal path is
qa/p212_keyed_stdin_input01/empty.stdin under the fixed workspace root.
This is a new physical empty regular-file policy, not /dev/null equivalence.
The empty digest in code is a required future value, not an observed input.

outer_contract.py:155 and driver.js:313 enforce the stdin role iff this exact
path. The dedicated descriptors (outer:249; driver:613) require file kind,
stable comparison, exact physical resolution, full fourteen-field shape,
zero size, empty whole-content key and no symbolic-link substitution.
No general metadata/device exception is used.

The outer helper (outer:264) and inner helper (driver:629) independently
resolve and compare the bound chain, open with O_RDONLY | O_NOFOLLOW |
O_NONBLOCK, compare the same-fd expected physical/full key before the single
one-byte current-position read, retain the sentinel outcome before rejecting
a nonzero result, require zero returned bytes, then compare same-fd and
closing lexical/chain identities. Failures close the local descriptor and
retain a failed/unknown disposition to the extent record I/O succeeds.
The inner helper preserves the non-body-ancestor restriction at driver:641.

The helper returns the checked still-open descriptor itself. outer:627/641
passes that descriptor to Popen stdin; driver:709/710 passes the inner
helper descriptor as stdio[0]. There is no close-then-reopen path substitution
at these two handoffs. Parent cleanup occurs after completion/failure.
The snapshot paths dispatch the stdin role through these helpers
(outer:210; driver:388), so a generic whole-file read is not used instead.

Offset zero is expressly source-derived: each open creates a private new
open-file description at the beginning, the only position-changing read
returns zero, and no offset query is claimed. actual_offset_query remains
null. This inference is conditional on the ordinary trusted API semantics,
not evidence that any actual descriptor existed in this audit.
Linux documents fresh-open offset and shared-open-description semantics,
and successful read advances by the actual returned byte count.
[open(2)](https://man7.org/linux/man-pages/man2/open.2.html),
[read(2)](https://man7.org/linux/man-pages/man2/read.2.html).

Node's synchronous read refers to its documented current-position semantics
when position is null, and a numeric stdio entry refers to an already-open
parent descriptor. Python Popen accepts an existing descriptor for stdin.
These support the above source inference only; reference versions do not
attest installed binary/source equality.
[Node fs v22.22.2](https://raw.githubusercontent.com/nodejs/node/v22.22.2/doc/api/fs.md),
[Node child_process v22.22.2](https://raw.githubusercontent.com/nodejs/node/v22.22.2/doc/api/child_process.md),
[Python 3.10 subprocess](https://docs.python.org/3.10/library/subprocess.html).

product_capture.js:41 changes the literal Bash redirect to the selected
input. That initial redirect occurs inside the explicitly ordinary trusted
product/bootstrap boundary, before author-side checks. It is NOT an
independently pre-attested collector fd or protection against hostile startup.
The source contracts explicitly retain that boundary; the later descriptor
checks do not retroactively observe the collector's startup or original fd.

## Native fields, phases and preserved failure

observe.py:127-137 still requests native 0xFFF, records actual return/errno,
returned mask and all 256 raw bytes before the acceptance test. Full-field
decoding, expected-key-before-content, same-fd whole read and closing checks
remain in the unchanged protected core. observe.py:268-284 adds the dedicated
physical zero-byte role; no dummy birthtime or ctime substitution is added.
Outer full_stat and Python probe decoder protected bodies remain unchanged.

Linux UAPI defines 0x7ff basic statistics and 0x800 birth time, with their
combination 0xfff. Presence of a Node field name alone is not returned-mask
evidence. The separate actual native requirement is preserved.
[Linux v6.8 stat UAPI](https://raw.githubusercontent.com/torvalds/linux/v6.8/include/uapi/linux/stat.h).

The controlling old /dev observation returned 0x17ff, missing 0x800, and
stopped before the /dev/null leaf. That failure remains unsatisfied and is
not converted to success by this new source. Its original private runtime
body was not reopened; the permitted controlling source-selection and
failure-analysis/root evidence were used.

The lookup01/bodies01 phase distinction, body-role traversal restrictions,
prepared finite request graph, only the two declared help/version operations,
capture closure and source/probe/runtime/root-receipt roles remain bounded.
The new helpers add no extra host probe, fdinfo/lseek query or enabled phase.
The product collector is orchestration source, not a Node CLI program.

Native/error limits remain honest: inherited outer/probe error schemas do
not promise every exception retains all native raw bytes; observer whole-file
failure need not retain all body bytes. Record I/O or transport can itself
fail. Existing race, alias, process and ordinary-bootstrap limitations are
not repaired or hidden by this acceptance.

## Complete finite frontier and no self-receipt

Independent data comparison confirms 164 targets and 204 components:
110 required files, 32 optional files, 11 optional directories, five metadata
targets, five one-level memberships and one required absence. All five
whole membership records are unchanged, including all 292 exact names.
There are 159 wholly unchanged target rows, five removed/five added target
rows and eight removed/eight added exact components. This is a full-value
comparison, not a count-only or changed-path scan.

Changes replace /dev/null with the uncreated required empty-file target,
relocate both probes and the nearest package.json candidate, and name the
future new root source receipt. The unneeded /dev component is removed only
from the new frontier. All seven old closure-gap strings remain exact; the
eighth preserves the old failure and separate new-policy obligations.
The full new input ancestors and relevant source/package ancestors remain
explicit. No host pathname in that data was followed by this audit.

The author origin and ROLE_CLOSURE accurately distinguish old immutable
references, new source awaiting review and future receipt path roles.
The three interfaces stay disabled with unresolved keys null. The future
root receipt is not manufactured, used to certify its own bytes, or treated
as already observed. Old trust-prefix acceptance cannot automatically
authorize new relocated source prefixes.

The frontier intentionally is not a complete runtime dependency proof:
actual _ctypes/libffi DT_NEEDED, import and extension closure, loader/config
follow-through, Node builtins/lazy/native bindings and package ancestry
remain actual finite obligations. Unknown additional paths require a
separate explicit delta and root reception, not wildcard expansion.

## Exact line-count correction and remaining gates

I independently obtain 2519 + 204 - 44 = 2679 lines and 148546 bytes.
The frozen HANDOFF.md still says 2779; its digest remains
da09c9697133988256adec01aa4e5df66bc02aa99588edfef204a8471d9db9d8.
P212-KSI-F1 is closed only for the exact original-plus-erratum combination.
The wrong original is preserved, not silently repaired.

Both complete 95-line root erratum checkers were read. They differ only at
lines 35/36, changing the incorrect ./ manifest grammar and its label to
the actual bare-relative layout. The failed native 28125e is preserved;
the successful native 26e887 records 2613 checks and 65 documentary keys.
I independently checked all 65 whole key bodies and the exact complete
actual wc output, rather than rerunning or trusting the root checker.

This packet supplies the previously missing non-lineage full-source verdict;
root must still receive the exact originals and this evidence. Any physical
input creation/keying, live application, grant or observation requires a
separate explicit root step. Then actual native pre-probe keys, independently
received probe/runtime results, complete pre-Node/tool keys and staged
dependency closure remain required before build or operational use.
No observed input, live source application, probe, query, science, build,
Git/SSH or external action occurred here. HOLD_EXTERNAL remains unchanged.

