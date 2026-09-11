# P211 Round1: single actual documentary reception

2026-09-08 UTC. **PASS, physical/documentary scope only.** The root-authorized
sealed receiver02 was actually invoked once. Its actual native exit was 0;
the capture controller also returned actual tool exit 0. There was no retry,
receiver revision, recorder invocation, scientific execution, build, page
view or manuscript review. Whole-host/settings acceptance, the four root
placement operations and their original tool evidence, A's mathematics, and
final Round1 acceptance remain root-owned. Paper completion is false and
external release remains HOLD_EXTERNAL.

## Exact actual invocation and complete result

[RECEIVER_ATTEMPT.json](RECEIVER_ATTEMPT.json) records the actual argv, cwd,
four-variable environment, DEVNULL stdin, 900-second timeout, source and
interpreter pins, input seals and start time.
[RECEIVER_NATIVE.json](RECEIVER_NATIVE.json) adds the actual exit, complete
capture state, exception field, end time and raw stream byte pins.
[TOOL_NATIVE.json](TOOL_NATIVE.json) preserves the actual controller tool
request, running return (chunk fa1eb2, session 16768) and single completion
poll (chunk f5e1ac, exit 0), including its entire small stdout.

The complete receiver result is [receiver.stdout.raw](receiver.stdout.raw):
2,971,096 bytes, SHA-256
`a761df245e742562df8bbcb6165f33c4d64d457bd0f22b5cb3be92698c78b23d`.
It contains all 2,763 rich before/after input records and all 29 rich tree
inventories. The original JSON bytes, including nanosecond integers, were
captured directly; they were not round-tripped through JavaScript JSON.
[receiver.stderr.raw](receiver.stderr.raw) is empty, SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

[SCOPED_RESULT.json](SCOPED_RESULT.json) is only a small summary, not a
replacement for that complete raw result. Its historical pending package
seal field is intentionally unchanged: it was emitted before the actual
controller tool return and the final read-only reception. The completed
package's [SHA256SUMS](SHA256SUMS) is the later nonself manifest; no historical
pending producer/receiver record was rewritten to pretend earlier acceptance.

## Received physical scope

The actual receiver returned 108,176 checks and
`PASS_PHYSICAL_DOCUMENTARY_SCOPE_HOST_ACCEPTANCE_EXTERNAL_ROOT`, covering:

- 83 Round1 payloads and 84 files including its outer manifest;
- 119 actual native child records and all 238 raw child stdout/stderr streams;
- one original recorder root-invocation record and its complete raw streams;
- the entire 509-file execution package;
- 2,164 external files, the 2,255-path recorder key and the 2,763-path receiver
  key, with full rich before/after equality;
- all 29 recorded rich inventories and the ten precisely declared external
  empty directories, with no empty-directory pruning or broad waiver.

The exact accepted source is copied as
[EXECUTED_RECEIVER_SOURCE.py](EXECUTED_RECEIVER_SOURCE.py), 37,766 bytes,
SHA-256 `21d16d2560eeb68420a3c37c9a3fda98dcbcb0ea1043dc80cd36a81e24fef06e`.
The actually used capture controller is retained both as
[receive_once.py](receive_once.py) and as its raw pre-invocation snapshot
[EXECUTED_CONTROLLER_SOURCE.py](EXECUTED_CONTROLLER_SOURCE.py), 9,213 bytes,
SHA-256 `2d041499307cb5daa0dade28914aa24a69718a2dd034f4a744603eb6cbca2341`.
The controller's thirteen consumed originals have complete unchanged rich
keys in [CONTROLLER_INPUTS_BEFORE.json](CONTROLLER_INPUTS_BEFORE.json) and
[CONTROLLER_INPUTS_AFTER.json](CONTROLLER_INPUTS_AFTER.json).

## Input packages and subsequent read-only verification

[PREPARATION_INPUT_MANIFEST.sha256](PREPARATION_INPUT_MANIFEST.sha256) is an
exact byte copy of the complete eight-payload/nine-file receiver02 preparation
manifest: 686 bytes, SHA-256
`556f22fc196006bb4b7a800ca10af7e921666523495f16a8afd9d3f3f7dc3aa0`.
[EXECUTION_INPUT_MANIFEST.sha256](EXECUTION_INPUT_MANIFEST.sha256) is an exact
byte copy of the complete 508-payload/509-file execution manifest: 53,853 bytes,
SHA-256 `858999190e1e16f07752aa0c4a9e6ca967bf7b4dee61eaa3c33ee2b47f141c30`.
These copied manifests retain their original bases, explicitly recorded in
[INPUT_SEAL_ORIGINS.json](INPUT_SEAL_ORIGINS.json); their rows must not be
interpreted relative to this new receipt directory.

[VALIDATION_NATIVE.json](VALIDATION_NATIVE.json) preserves the actual complete
read-only verification request and tool return: chunk 54c442, exit 0,
13,763 checks. That check consumed the full raw JSON without executing the
receiver again; verified every current rich receiver/controller input;
verified all eight preparation and 508 execution payloads and their complete
file inventories; checked the exact executed source copies, entire native
request/return/raw binding, small summary and original controller tool
envelopes. It also checked nanosecond fields as exact Python integers against
current filesystem metadata. No scientific or submitted receipt source was
imported or executed by this verification.

The separately supplied root postcopy host record was read as all 992 original
bytes, SHA-256 `04a123c5c7e9bba267ce380d387be7e4789f4a777d9c62bb5b7ed2f418630c77`.
Its original path is in the attempt, native result and origin map. Neither
the receiver nor this receipt dereferences the 799 host referents or judges
the complete host/settings semantics. Reading a pinned root host JSON does
not constitute independent host acceptance.

## Ownership and preservation

Only this new reception directory was written. The source02 preparation,
original execution/frozen evidence, P211, A's accepted artifacts, failed
historical attempts and root/central files remain unmodified. I authored
A's review artifacts and the receiver, not the recorder; this is a scoped
independent-process documentary reception, not a new independent A/B review.
The received authority and no-retry contract are recorded in [PLAN.md](PLAN.md).
The completed nonself manifest covers the entire preparation/execution receipt,
including raw evidence and the actual read-only checks; preserve every member.
