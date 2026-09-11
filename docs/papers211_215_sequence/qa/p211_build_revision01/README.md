# P211 build revision 01 — BLD-I1

Status: **REVISION_READY_PENDING_INDEPENDENT_REAUDIT_AND_ROOT_BINDING**.
This directory is a narrow new version of the initial-build preparation,
not a compiled manuscript or an accepted build. BLD-I1 remains Major/open
in the immutable original independent report until its auditor issues a
separate revision verdict.

## Exact corrected branch

The original [independent report](../p211_build_independent_audit/REPORT.md)
was read completely. It correctly identifies that an exception before
Popen returns leaves proc=None while the old recorder defaulted settled=True.
The old path could finalize a failed artifact without knowing writer outcome;
it did not falsely upgrade that failure into a successful build.

The new `build_core.py` starts settled=False. Only a returned native handle
followed by actual owned-session settlement can set it true. A no-handle
exception records `NO_NATIVE_HANDLE_UNKNOWN_LAUNCH`,
`native_handle_received: false`, `launch_outcome: UNKNOWN_NO_NATIVE_HANDLE`,
`native_exit_code: null`, and `streams_settled: false` in UNCLOSED.json.
It retains ATTEMPT and any raw bytes but raises before final stream hashes,
INPUTS_AFTER, or RECEIPT. No known-prelaunch exception exemption was added:
conservatively uncertain paths remain unknown. An unrelated finalization
exception still leaves the preexisting missing-receipt guard in force.

The existing production inner/outer UNCLOSED and incomplete-attempt checks
and the core native seal refusal are unchanged. A missing returned handle
therefore cannot obtain a production failed-subtree seal through this branch.
There is no broader process-containment or OS-tracing claim.

## Versioned delta, not historical replacement

Only this new directory was written. The original
`p211_build_preparation/` retains all 891 payloads under manifest SHA-256
`5fa2620b27e04f0d07f9b72434f801a948e95d7df884d2e46a915c42028bd042`.
The independent old report and its 50-payload manifest
`394ade8814a31fae9b02bab1f2d4415d1b8257c7485a991df0b89bbe69f0ca64`
are unchanged. Exact baseline/source/report/interpreter pins are in
`DOCUMENTARY_AUDIT.json`; the original archive was not copied.

Complete actual five-file native unified diffs are preserved in
`diagnostic_capture01/commands/diff_*/stdout.raw`, with actual exits,
before/after inputs and separate stderr. The complete current five
operational sources and their physical executed copies are retained.

- `build_core.py`: new PREP location, named BASELINE_PREP, the narrow
  no-handle settlement correction and explicit outcome fields.
- `launch_build.py`: diagnostic diff baseline changed to the exact final
  original five files, rather than the first original failed version.
- `static_checks.py`: the settled historical-record check explicitly points
  to original diagnostic_capture05.
- `prepare_build.py` and `build_p211.py`: byte-for-byte unchanged from the
  original final version; actual diff exits are both 0.
- `infrastructure_fixture.py`: new standalone infrastructure test/capture
  code, not an imported production dependency.

No ENV8, source graph, future-cwd binding, four-command order, dependency
selector, BibTeX/FLS role or PDF-measurement redesign was made. Original
[build-plan scope and limits](../p211_build_preparation/README.md) continue
to apply subject to this explicit BLD-I1 correction and the new paths/pins.

## Actual focused regression

`infrastructure_capture01/` contains the real enclosing fixture process
receipt, executed two-file fixture/core snapshots and separate raw streams.
The actual enclosing Python process exited 0 with a known handle, an empty
owned-session membership at settlement and no intervention. The actual
product-tool launch also returned completed exit 0 directly, without a
yielded session; its exact envelope is in `NATIVE_TOOL_ENVELOPES.json`.

The fixture adds a real sys.addaudithook callback that raises BaseException
at the `subprocess.Popen` event before a native handle returns. The callback
records its exact event/argv/environment; the traceback binds the actual
event to /usr/lib/python3.10/subprocess.py:1735. That installed source places
the audit event before both native creation branches. The fixture does not
explicitly fork, detach, create an escaped writer or test an unkillable child.

The refused call remains in
`cases/unknown_launch/commands/refused_before_handle/` with ATTEMPT and
UNCLOSED, no SPAWNED/RECEIPT/INPUTS_AFTER and no final stream-pin field.
Its raw stream files are retained. The refusal subtree, cases parent and
outer capture each demonstrably reject native seal. That UNCLOSED marker
and missing receipt are deliberately not rewritten or discharged.

The separate known-settlement fixture launches exactly one ordinary Python
child writing `known stdout\n` and `known stderr\n`. It returns native 0,
captures both exact byte streams, has empty settled session membership and
requires no intervention. Its ordinary native subtree can be sealed.
This is a positive known-handle test, not a timeout/kill or escape test.

The successful fixture assertions do not imply that a general unknown
writer is settled. A **documentary** snapshot of this controlled test package
is permitted only because the actual enclosing fixture completed and its
known session is quiescent. `DOCUMENTARY_SHA256SUMS` therefore records a
post-fixture evidence snapshot; it is not the native SHA256SUMS of the
intentionally UNCLOSED subtree, and it does not bypass the production seal.
There is intentionally no top-level native SHA256SUMS and no native seal at
the refusal subtree, cases parent or infrastructure capture.

## New candidate lock and exact root gate

The new static/data diagnostic and 25 native configuration-discovery
commands completed successfully with no TeX compilation, bibliography run,
science or rendering. Actual diagnostic product session 55993 completed
with exit 0; raw native records and exact tool envelopes are retained.

The only proposed lock for this version is
`discovery01/DEPENDENCY_LOCK.candidate.json`, SHA-256
`bb89d966250b0552a47784a5c4aa0d2aaf5b36bc9057fc177a5e552b9bf042ec`.
It has 840 path spellings / 795 file entries, 33 selected ELF inputs and
three future-cwd ABSENT roles. Its current configuration equals the new
candidate. Compared with the old entries, only the observed
`prepare_build.py` path moved to this new version; there are no other
entry-content changes. Current five operational code pins match both the
candidate and physical diagnostic execution snapshots. All nine physical
manuscript sources remain byte-identical to the original candidate.

Root must read the complete current five operational files, standalone
fixture, actual diffs, this delta and native evidence, then receive the same
independent auditor's separate revision verdict. Only then may root create
a separate exact initial binding and actual root-read receipt. The binding
must point to this new adapter and new candidate with actual byte/hash pins;
the original binding cannot authorize changed code. The intentionally
rejected `BINDING.pending.json` remains pending. Existing exact ENV8,
isolated Python flags, new output/no-retry restriction and three absolute
future `inner/source_only` absence bindings are unchanged. The fixture is
not authorized as a production dependency or a substitute for that gate.

## Documentary audit and limits

`DOCUMENTARY_AUDIT.json` plus its native tool envelope record an independent
read-only check of all original 891 payloads, all three current native
sub-manifests, 34 completed native attempt/receipt/raw-stream pairs and the
one deliberately incomplete unknown attempt. It checks the actual enclosing
fixture receipt/quiescence, all native seal refusals, current source/code/
configuration keys and the precise old-to-new configuration delta. It did
not import operational code or run TeX/science.

The original independent report is only read and pinned here, not relabelled.
The producer's correction and tests are not independent acceptance.
Project and paper-compile skills were used for the preserved-log/source/
configuration obligations; the task restriction keeps compilation, cleanup,
install/retry/source-fix, rendered-page viewing, manuscript A/B review and
terminal acceptance out of scope. External actions remain HOLD_EXTERNAL.
