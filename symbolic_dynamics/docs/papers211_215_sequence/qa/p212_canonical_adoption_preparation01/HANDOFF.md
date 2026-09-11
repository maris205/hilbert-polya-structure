# P212 canonical-adoption source-only handoff

2026-09-09 UTC. **READY_FOR_ROOT_SOURCE_RECEPTION_ONLY; HOLD_ADOPTION / HOLD_PAIR**.
Author: P212 verifier/manuscript contributor, not independent review.

The new package contains [adopt_canonical.py](adopt_canonical.py), its disabled
[adoption binding](ADOPTION.disabled.json), the byte-exact disabled original
[pair template](PAIR.disabled.json), [adoption plan](PLAN.md) and separate
[strict-pair plan](PAIR_PLAN.md). Root must fully read these originals and the
accepted native/source/semantic/runtime evidence before any new approval.

The helper is 12766 bytes, SHA-256
b83151f6091ff1260e62634be7c370bcd8d73ec4c9037fb25d9ccb70457c5aca.
Its 148177-byte [whole workspace input inventory](WORKSPACE_INPUTS.json) is
9ed644f2f5b6dea4be8af585c9657121914968e1b44cedb76340991b28b32cb1:
416 file pins, 11 exact trees and 20149659 original bytes. Full accepted
semantic/runtime packets have 92/14 payloads; exact complete manifests and
all contained actual source, bindings, locks, native records, failed attempts
and saved input maps are unchanged. Host paths in those maps are data only.

Actual verification: 9566 workspace assertions passed twice; the complete
148177-byte native stdout was byte-identical between runs and equals the
saved inventory. A separate [47-check preparation-binding pass](PREPARATION_RESULT.json)
is backed by [BINDING_NATIVE03.json](BINDING_NATIVE03.json). The actual
CHECK_NATIVE02 command 1 ran native cmp on original pending and copied disabled
pair bindings and exited zero with empty output. Whole current helper text
was read, retained and checked against its exact complete source bytes.
Original full source/binding/reception reads remain in ORIGINAL_READS_NATIVE.json.

No submitted source was imported/compiled/executed, no adoption helper was
run, no host/runtime probe or science occurred, and both canonical spellings
remain absent. No operational authority has been manufactured. Existing
P212 build preparation and all P211/other-paper packets were not changed.

Root's next bounded step is source/evidence reception and an independently
owned exact adoption authority/binding plus actual adoption-runtime/native
capture checks. This package does not provide those host/runtime checks.
Successful adoption can only copy the accepted 12501943-byte raw initial
stdout to formal CANONICAL.json by exclusive xb/fsync and one actual raw cmp.
Partial failures must remain preserved; never overwrite or automatically retry.
Only after complete actual adoption reception may a distinct approved runtime
pair produce two fresh stdout streams and perform three real raw comparisons.
Neither gate supplies independent review, paper completion or external release.

The closing native receipt binds the then-complete 14 preseal payloads;
SHA256SUMS additionally binds that receipt as the fifteenth payload. Final
manifest verification is performed after sealing, with no subsequent payload
mutation. No historical evidence, manuscript, batch index or recovery index
was edited by this author preparation; root retains milestone-index ownership.
