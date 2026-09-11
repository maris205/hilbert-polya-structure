# P212 native-mask failure: bounded source diagnosis

2026-09-09 UTC. SOURCE/DATA-ONLY DIAGNOSIS; NOT A SOURCE ACCEPTANCE,
IMPLEMENTED FIX, EXECUTION GRANT, RUNTIME RECEIPT OR INDEPENDENT AUDIT.

The current honest disposition is **HOLD_FINITE_OBSERVATION_ERRORS**.
Removing `/dev/null` only from the initial frontier would contradict the
accepted downstream sources. The narrower prospective alternative is an
explicitly keyed empty regular-file stdin dependency, retaining the complete
native `0xFFF`/fourteen-field requirement; its exact affected surface and
unresolved behavioral obligation are in [OPTIONS.md](OPTIONS.md). Nothing in
this packet selects, creates, observes or enables that alternative.

## What was received, and what was not

The [actual launch return](../p212_preprobe_observation_root01/ACTUAL_OBSERVER_NATIVE.json)
contains native exit 78, chunk `d55ac5`. The allowed
[root summary of the private original](../p212_preprobe_observation_root01/INITIAL_RAW_INTAKE_NATIVE.json)
reports three completed controls and three observed initial targets, followed
by the fourth target `/dev/null` failing during pass 1. Its last native event
is for ancestor `/dev`, return 0, errno 0, returned mask 6143 (`0x17ff`).
There were no closing controls and no second pass. The first three targets
are `/`, `/bin`, `/bin/bash` by the literal ordered frontier, not by a count
transplant. No `/dev/null` leaf result is reported. Its field support therefore
remains unknown here; the failure cannot be called an observed null-device
birthtime failure.

The root summary keys stdout as 375,140 bytes,
`979196b97bec96c31d2cd22ec9890824366776025613f4fe024a626e7bf27995`,
and stderr as zero bytes. This analyst did not read either private file or
any captured host body. All actual-observation statements above are explicitly
attributed to the supplied summary, not a fresh private-raw reception.
Nested archived reader/launch command strings were read as data, never run.

The [received observer source](../p212_preprobe_bootstrap_read_order_delta01/observe.py)
has SHA256 `68789ec6ecb134c714bd5b3d552ab4ff1d3433b8f416b78eddcd0b1046bac4e1`.
In `native` (lines 119–148), the whole event/raw buffer is retained before
the check `(mask & 0xFFF) == 0xFFF`. For the summarized mask,
`0x17ff & 0x0fff = 0x07ff`: the required `0x0800` birthtime bit is absent.
The extra bit does not satisfy that conjunction. The source throws before
constructing its fourteen decoded values. There is no justified zero,
ctime substitute or decoding of unsupported birthtime in this analysis.

## Exact dependency chain

| Source/role | Literal obligation and consequence |
|---|---|
| [Frontier](../p212_preprobe_bootstrap_preparation01/FRONTIER.json) | `/dev/null` is target 4: `mode=metadata`, archived-path origin, native-validation/component role, `max_bytes=0`, `capture_hex=false`, `max_members=0`, `expected_names=null`. `/dev` is a permitted component, not a target. No other literal target lies under `/dev`. |
| Observer `resolve` / `observe_target`, lines 157–201 / 256–295 | Resolves `/` then `/dev` then the leaf using `native` on each component. The null character-kind assertion is later at line 267. Metadata mode authorizes no device bytes or membership. |
| [Python author probe](../p212_trusted_product_source_delta01/python_runtime_probe.py), lines 91–112 | Requires a finite sorted unique validation list containing `SELF`, `/`, **and `/dev/null`**; every listed path requests/requires `0xFFF` and produces all fourteen integers. Null is not an optional illustrative sample under this source. The probe does not itself component-walk `/dev`; the independent bootstrap key and later resolvers do. |
| [Outer wrapper](../p212_trusted_product_source_delta01/outer_contract.py), `full_stat`, `descriptor`, `observe`, `resolve`, `snapshot` | `full_stat` requires `0xFFF` before returning all fourteen integers for path or fd. Each nonabsent descriptor requires both full `lstat` and `stat` dictionaries. `resolve` visits every explicitly bound ancestor; `snapshot` does this before Node starts. Thus `/dev` must be present in the binding to resolve mandatory null, even though the mandatory top-level list does not separately spell `/dev`. |
| Outer validation / main, lines 445–454, 475–476, 494–498, 550–568 | Requires `/dev/null` with character kind; requires each complete inner descriptor equal the outer descriptor; prepared request says `BOUND_/dev/null`; resolves, opens and native-fstats the null fd, checks character kind and stable metadata, then supplies that actual fd to `Popen(stdin=...)`. |
| [Inner driver](../p212_execution_scope_source_amendment01/driver.js), lines 222–340, 342–359, 416–450, 560–562, 601–686 | Full fourteen-field descriptor/BigInt shape, explicit null input and character kind, complete ancestor resolution, separate null open/fstat, stable handle comparison, and `spawn(..., stdio:[nullFd,outFd,errFd])`. The policy, before/after configuration records and attempt record also name null. This applies to the present help/version contract and is not permission to run later phases. |
| [Capture companion](../p212_execution_scope_source_amendment01/companions/CAPTURE_CONTRACT.json), `commands.stdin` | Explicitly requires actual bound `/dev/null` character-device identity. Driver `oldCompanions` requires the entire companion bytes and fixed hash, not just selected semantic fields. A derivative driver cannot silently retain this old companion as its new stdin contract. |

The complete frontier was read as data using a lossless path/template
rendering: every target parameter, all permitted components, all membership
names and all closure gaps were emitted. That is not a host read or a proof
that the proposed frontier is exhaustive. The original 164/204 counts are
only cross-checks; the source paths above establish the dependency.

## Fourteen fields versus comparison projections

All sources use `dev, ino, mode, nlink, uid, gid, rdev, size, blksize, blocks,
atimeNs, mtimeNs, ctimeNs, birthtimeNs`. Stable comparison excludes **only
atimeNs**. The observer's ancestor identity projection contains
`dev, ino, mode, uid, gid, rdev, birthtimeNs`; the outer and inner identity
projections contain the first six of those, without birthtime. Those narrower
comparisons occur **after** full capture/shape checks. In particular, the
outer native mask check still rejects unavailable ancestor birthtime.
The [source contract](../p212_trusted_product_source_delta01/SOURCE_CONTRACT.md)
explicitly retains all fourteen original fields even for ancestors, and
[runtime preparation](../p212_trusted_product_source_delta01/RUNTIME_PREPARATION.md)
requires independent native/Node field comparison and HOLD on unsupported
birthtime. Thus this is an existing contractual overconstraint relative to
the narrower ancestor comparison, not an accidental observer-only frontier
extension. That distinction does not prove birthtime is scientifically
necessary or authorize weakening its accepted evidence contract.

The standalone [Node probe](../p212_trusted_product_source_delta01/node_runtime_probe.js)
does not directly stat/open null and does not start children. Its regular
receipt checks and runtime enumeration do not establish native birthtime-mask
support. The [preload](../p212_trusted_product_source_delta01/node_preload.js)
checks three integer stdio descriptors and exact help/version vectors; it
does not itself attest their null origin. The actual inner open/guard matters.

The [original root decision](../p212_trusted_product_boundary_root01/DECISION.json)
fixes Python/Node/outer argv prefixes but no stdin field. The
[product collector](../p212_trusted_product_source_delta01/product_capture.js)
builds its quoted `exec` request without stdin redirection. By contrast, the
actual [observer request](../p212_preprobe_observation_root01/REQUEST.json)
explicitly contains `</dev/null` in the ordinary trusted shell prefix.
Do not conflate these three facts or treat later metadata as startup
attestation.

## Evidence and authorship limits

[INPUT_SHA256SUMS](INPUT_SHA256SUMS) pins 23 exact selected inputs.
[READS_NATIVE.json](READS_NATIVE.json) preserves actual workspace reads,
hashes, complete frontier data rendering and navigation failures/caps. Early
summary/control reads occurred before their first explicit hash; the driver
and capture companion first explicit hashes were collected after their
targeted/full reads. No universal before-read endpoint claim is made.
The full observer, Python/Node probes, outer, preload and collector were read;
the 978-line driver was read by the stated affected source paths, not claimed
as a new whole-driver acceptance. A capped navigation search and nonexistent
`outer_preload.js` guess are preserved, not promoted to complete evidence.

The [first documentary check](FIRST_DOCUMENT_CHECK_NATIVE.json) succeeded
before two final clarification sentences in OPTIONS were tightened. The
[final documentary check](CHECK_NATIVE.json) is a separate actual workspace
data operation, not an observer/probe execution or source-correctness test.

Only this new analysis directory was written. No private/host/environment/
configuration observation, operational Node/Python/probe/source-parse/AST/
syntax test, child query, science, build, Git/SSH or external action occurred.
Ordinary documentary Node did run on workspace data and is recorded; saying
“no Node executed” would be false. The project research skill required
resuming the affected evidence gate and preserving old failures, not starting
another batch. This analyst's source contribution disqualifies them from an
independent audit of any future implementation using it. All old packets and
the old strict `/dev` key remain frozen and UNSATISFIED. Author probes,
operational phases and external action remain held.
