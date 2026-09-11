# P207 terminal artifact audit and lifecycle-only closure

2026-09-06 UTC. **PASS_P207_TERMINAL_ARTIFACT_GATE / OWNER_AMBER /
HOLD_EXTERNAL**. The first full actual passing check and its later
lifecycle-only follow-up are distinct immutable executions. This report is
an artifact handoff for P207 alone, not a third manuscript review, a new
mathematical proof, or completion of the requested five-paper batch.

The auditor is `batch197_lzk_gate`, also the disclosed nonauthor manuscript
A reviewer and initial B artifact assessor. Root retains responsibility
for reading the original mathematical proofs, accepting the actual A/B
deltas and integrating the final lifecycle. No extra process-independent
review is claimed by reusing this process for artifact checks.

## Actual terminal attempts

The [read-only terminal checker](../audit_p207.py) is executed at its original
workspace path by [the exclusive raw-byte recorder](record_attempt.py),
under the recorded Python binary with `-I -B`. Each attempt has the exact
source snapshot, complete binary stdout/stderr, command/cwd/exit receipt,
before/after execution-input hashes and a four-file nonself seal.
The snapshots record the original executed script's bytes; the snapshot
path itself was not executed as a relocated checker.

| Attempt | Actual outcome | Complete stdout |
|---|---|---|
| [initial_01](initial_01/RECEIPT.json) | Exit 1; intake-path adapter failure | Empty; actual 941-byte traceback preserved |
| [initial_02](initial_02/RECEIPT.json) | Exit 0; 84,416 artifact checks | [404,195 raw bytes](initial_02/run.stdout) |
| [lifecycle_01](lifecycle_01/RECEIPT.json) | Exit 0; 84,417 artifact checks after status update | [404,448 raw bytes](lifecycle_01/run.stdout) |

The first attempt incorrectly requested A's nonexistent
`intake/REVIEW_SCOPE.md`, which is B's intake filename. Its exact source
SHA-256 is `86c5886bf726a04ea56b7fee73d63567cbd26d48c19fb1bea584e0dfdd0cb9d9`.
The sole correction selected A's actual `intake/FREEZE_PIN_CHECK.json`
while retaining B's actual intake path. No reviewed input was substituted,
no criterion was weakened, and no missing science hash was ignored.
The [original traceback](initial_01/run.stderr) and both complete source
snapshots preserve the failure and exact two-line replacement.

Both subsequent successful executions used the identical 72,341-byte
checker, SHA-256
`9adceca8055ce8d716e1567db36103c2c0c1af99c6ce476b15daf93b8ce08257`.
Their stderr streams are empty and their recorded checker, recorder and
Python binary hashes are stable before/after. Successful raw stdout hashes:

- `initial_02`: `23d09ddd34e522bf82feea6e69b86384b1bb5c9a2e29d5122047b3899ae5b104`.
- `lifecycle_01`: `644fd2bb2a2b630d6dc360d66812bd5756b78e9f000bca0b4b708a813932ee51`.

These are directly captured child bytes, not JSON reserializations or
tool-message text copied back into files. A failed attempt is not included
in a successful check count. Development-time inspection commands are not
mathematical or terminal-gate executions.

## Complete evidence actually checked

Each successful full output retains all 1,197 consumed input paths and
their byte counts/hashes, all rechecked at the end. The checker performs
89 named manifest-validation invocations, including the complete 614-entry
paper package, 79-entry terminal package, all three 105-file physical
freezes and final accepted A/B packages with 133/138 entries. The identical
freeze manifest is
`8d134689f8c07f9bcac65b4576a5bfca2e073ece6281f9d893148f12adb43f5d`.

The accepted A delta has zero current or resolved findings. Accepted B
has zero current open critical/major/minor findings and the real one
resolved Minor, P207-B-ART1. The documentary repair and unchanged
scientific inputs are checked against the accepted delta, its prior-open
record, initial report and actual build log. Current acceptance does not
erase its initial missed diagnostic or other stopped artifact checks.

All author, A and B canonical fields, record shapes and declared boxes
are inspected, including complete certificate/graph/trace output and
cross-representation checks. The canonical byte counts are 288,808,
37,971 and 1,558,382 respectively. Their archived per-run assertion counts
are 1,384,012, 1,326,321 and 2,158,999. Full original execution records,
source snapshots, raw-canonical comparisons and the existing root pairs
are checked. This audit imports or executes none of those mathematical
producers. Original nonisolated author/A records and the old root A pair
are retained; the separate controlled root A/B pairs are the indicated
reused reviewer pairs, not newly counted runs.

Earlier actual artifact outputs are also checked: A's 6,562-check output,
B's 12,845-check output, this process's initial 39,623-check B audit and
all 599 of its historical referents, and B's 5,258-check accepted delta
with all 727 consumed referents and its actual 23-command receipt.
Explicit historical aliases preserve the initial B report/findings/seal
and provisional helper. The 147,133-byte exact initial B audit stdout is
distinguished from its 147,134-byte archived JSON serialization with one
extra LF; the documented packaging repair is checked, not hidden.

Both actual terminal builds started from nine source inputs. Their full
commands, engine/settings, source hashes, logs, PDF reports and actual
output comparisons are checked. Both final PDFs have 407,557 bytes, seven
pages and SHA-256
`5e74fa6a334f1cbc23837632b364729d97111b231e1ef8c3fd6a40a8dbc78759`.
The real underfull-vbox badness-1038 diagnostic is present in each log;
the check does not suppress it or call the log warning-free. Root's seven
actual page attestations are validated, including the explicit affected
page-4 inspection. PNG hashes do not count as new viewing by this auditor.
Each build's 157 external TeX inputs and four supplementary runtime/style
files are contemporaneous post-build pins, not a historical hermetic
environment. The two recorded host symlinks are explicitly resolved and
rechecked; ordinary workspace artifact inputs must be regular nonsymlinks.

## Lifecycle-only difference and historical aliases

The initial passing result consumed the prior pending-status bytes. Before
root updated the lifecycle, this process preserved the exact two files in
[lifecycle_before](lifecycle_before/SHA256SUMS). The old full result and
its dependency map were never edited to describe later bytes.

After root changed only `PAPER_STATUS.md` and the whole-paper `SHA256SUMS`,
the unchanged checker produced the actual `lifecycle_01` PASS above. The
new [separate delta-check execution](lifecycle_alias_01/RECEIPT.json)
then ran the scoped [lifecycle checker/recorder](record_lifecycle_delta.py):
**19,026 read-only checks**, child exit zero, empty stderr. Its complete
[250,471-byte stdout](lifecycle_alias_01/run.stdout) has SHA-256
`98312b3e4d0fa6f8e7a4c4792172fe85c534119c8d7d26835980908cc049e49e`.
This is a separate actual artifact execution, not a third independent
reviewer or an independent mathematical proof.

That supplement checks both 1,197-key result maps in full. Exactly the
two keys below differ; the historical map is rechecked using precisely
the two disclosed before-file aliases, while the current map is rechecked
directly without those lifecycle aliases. All 1,212 consumed supplemental
inputs, including both full outputs, receipts, exact source snapshots and
before files, are rechecked at the end.

| Changed key | Before SHA-256 | After SHA-256 |
|---|---|---|
| `PAPER_STATUS.md` | `d9ecf124b5730176858619eb00a2ef711a00f5bdc9f8a2f6585d69b240bc0483` | `8cfb15f5c520bfa3601b41a464dfa02bf35e17ca7e60fd437f8e1a0502b8d578` |
| Whole-paper `SHA256SUMS` | `36ca84152edb74adbf971b5bf90daa50619f7c0ac853078ba494472c3b93c807` | `1d52015974faf842c50e9fc0a5ca481d4973af0c26b3c19c4b540ca5c6016a95` |

Both whole-paper manifests have the same ordered 614 paths and complete
current nonself coverage; only the `PAPER_STATUS.md` payload hash differs.
All page attestations and every scientific/build/source/canonical input
remain unchanged. The only added local link is the status file's link to
`P207_FINAL_QA.md`: the full link count changes from 415 to 416, and this
alone accounts for the extra full-audit check. Other than that link data,
the exact two input entries, the corresponding counts and execution
timestamps, every top-level full-result field is equal.

## Closure and limits

The directory-relative [nonself manifest](SHA256SUMS) covers every owned
file in this package, including each complete attempt seal, failed source,
failed output, both successful full outputs, lifecycle snapshots,
supplemental source/output/receipt and this report. The separately named
[auditor pin](AUDITOR_PINS.sha256) is workspace-root-relative and binds
`../audit_p207.py` without inventing a self-hashing manifest. Attempt
seals and historical receipts are immutable; the outer seal closes their
final collection. Root owns final central integration and private Git
synchronization, which are not claimed as performed by this report.

No new mathematics, source-only build or visual inspection was performed
by these artifact executions. Original proofs and actual accepted reviews
remain controlling. Recorded dependency verification does not establish a
hermetic historical interpreter/library environment. P207 remains within
the accepted narrow contract and its explicit limitations; no sharp global
clock, extra rank-family seat, global novelty clearance or external release
is added. P205 and P207 may be internally complete, but three requested
seats remain open and the five-paper terminal batch gate is still pending.
