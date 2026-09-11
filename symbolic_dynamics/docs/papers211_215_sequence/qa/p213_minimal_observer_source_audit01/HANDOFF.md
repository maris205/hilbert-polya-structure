# P213 minimal observer source audit — original frozen handoff

Verdict: HOLD_SOURCE_TWO_OPEN_FINDINGS_BINDING_UNRESOLVED.
Two Major/open findings, 0 Critical, 0 Minor; no finding is closed here.

- P213-MOS-F01: observe.py 338–342 follows /proc/self/exe with os.stat
  before validating the saved target/cwd against the finite binding.
- P213-MOS-F02: failure() at 109–113 treats every exact RuntimeError's
  first constructor argument as an observer-owned internal code.

See the complete [report](REPORT.md) and machine-readable [finding census](FINDINGS.json).
Both are source-semantic findings, not observed runtime incidents.
BINDING=None and the capture's unconditional exit remain intentional,
unmodified safeguards; no nonexistent exact binding is accepted.

The exact original observer is 438 lines/21,437 bytes, SHA-256
97198b16d87c504a2574a773133f8a4574d01f1751d810146b1237bb6359e65b.
The capture is 40 lines/1,734 bytes, SHA-256
1591b239781196ef8e31db64f17cfe51d3c707d1297f6756f0d072acb8aec1d2.
All 23 source payloads/24 files/421,765 bytes retain the source seal
5517fa99464c02c5d21170a133b0f5a6d540f18ca549dd6296503f2fc0d29d55.

Actual independent documentary checks 325ce1 and 1540ea each returned
3,420 checks, 33 complete keys, nine input pins, 19 raw archived-body
pairs/107,836 bytes and 28 selected native records/166,059 output bytes.
Their entire 34,803 stdout bytes compare raw-equal, SHA-256
8007e9a8b255ec90f625f5c5fa28eff006336bd8bf0fc183cb0b2f25ea77a07a.

Actual author-documentary replay 728134 returned 2,189 checks; its complete
9,855 stdout bytes equal the author's original bd7a37 raw bytes, SHA-256
587999b245cfb156f5f3f393ac30db039ef2ce4c29e78d41ba3353ef38a333eb.
This was an ordinary bounded Node document/JSON/string check, never execution
of the reviewed Python/Bash, observer/capture, science or archived requests.

Closing native f9ac8e returned 4,725 checks across 51 complete keys
(18 then-existing audit files plus 33 source/input documents), eight raw
comparisons, exact source line anchors and unchanged two-open census.
All 33 source/input keys match the first independent check; every selected
original author 19/22-key entry also matches its counterpart. The later
handoff/readback/nonself seal are received by
the final physical inventory, not included in that earlier 51-key claim.

The exact full module/launch rows demanded by source01 are not supplied by
the design inputs or documentary archive-name authority. A finite
source-only proposal may retain explicit root choices and historical names
with per-field provenance while leaving unavailable rows unresolved.
A collection-oriented finite-allowlist contract is only a possible
separately commissioned new-only design/source delta; it cannot silently
replace current exact-row comparisons or waive path/mechanism/cache gates.

The reviewer did not author this observer/capture/design or P213 proof.
Prior P213 design/source/title review familiarity is fully disclosed.
The separate child fresh10 lane contributes no review verdict to this audit.

Author and auditor original failures are retained, including the author's
wrong input filename, the auditor's truncated structural preview and three
failed direct GNU opens. No source change, host/private/proc/env/config
observation, Python/Bash syntax/AST/import/test, scientific run, capture
allocation, build/view, Git/SSH or external manuscript action occurred.

Root should receive this immutable original before commissioning one new-only
repair. The same reviewer can then assess exact repaired source/binding
bytes in a separate delta package; only that future acceptance may close
these original findings for its exact source combination. This report does
not authorize a probe or independently receive any future runtime data.
Root owns batch-first central integration. HOLD_EXTERNAL.
