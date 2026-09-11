# Documentary closure, not a scientific gate

The actual standard-library audit is
[documentary_audit.py](documentary_audit.py). It does not import or execute
a finite-system implementation. Its first actual run is preserved in
`commands/documentary_audit_01/`: complete argv/cwd, before/after explicit
code pins, raw stdout/stderr, runtime description and exit zero. The full
JSON stdout is authoritative; `commands/documentary_audit_summary/` is a
separate captured display transformation, not a second independent audit.

The actual first result is `PASS_DOCUMENTARY_STRUCTURE_WITH_EXPLICIT_LIMITATIONS`:

- 13 successful physical-snapshot manifests, 42 file rows, all recorded
  before/copy/after hashes and sizes matching the preserved physical bytes.
- Four complete content-search records, with exact scope reconstruction,
  argv coverage, raw-stream lengths and equal before/after source pins.
- 49 completed wrapper-command records checked for invocation consistency,
  complete raw-stream hashes and unchanged explicitly supplied pins.
- 6,543 distinct recorded `(absolute path, SHA256)` references: 43 have
  exact physical-copy mappings, 6,458 matched later current bytes, and 42
  known protected inputs were deliberately not reopened. The later check
  reported no additional unresolved historical byte keys.
- The exact old Git-receipt bytes are bound to the actual root recovery
  receipt, not a mutable-path exception or a fresh at-time-snapshot claim.

The 42 skipped protected references are **not** resolved/cleared references.
The 6,458 later byte matches are **not** physical at-time snapshots. The
first run excludes its own then-active wrapper result, which did not yet
exist. Final complete-payload sealing covers that result and subsequent
documentary artifacts once they exist; a seal does not make an operation
independent or retroactively re-run the structural auditor.

A second actual run of the unchanged auditor is preserved separately in
`commands/documentary_audit_02/`, again exit zero, empty stderr and no
structural errors. It checked 51 completed wrapper records, including the
first audit and its separate summary, while excluding only its own then-
active wrapper. It found 6,545 distinct path/hash keys: 43 exact physical
mappings, 6,460 later current byte matches, and the same 42 protected keys
not reopened. The extra keys are documentary inputs, not new scientific
sources. There were no additional unresolved keys or changed explicit
command pins. This is a same-author documentary recheck, not an independent
review, and it preserves all first-run bytes and limitations.

Three real adverse records survive: the 42-path v1 discovery scope failure,
the failed first nearby snapshot with its partial copied payload, and the
primary PDF's substantive UNAVAILABLE preflight. The late missing-jq utility
failure is also disclosed. See [SCOPE_FAILURE.md](SCOPE_FAILURE.md) and
[FAILED_SNAPSHOT_01.md](FAILED_SNAPSHOT_01.md). There is no P208/P209 reviewer-
eligibility assertion, whole-source-corpus archival claim or hermeticity claim.

## Final nonself seal

After all payloads are present, the auditor's `--write-seal` mode writes
`SHA256SUMS` with every physical file under this lane except the manifest
itself, including hidden skill copies, preserved partial failure contents,
original raw command/search returns, source PDFs/text and existing Python
cache bytes. It immediately checks directory coverage and each digest.
`--verify-seal` performs the same check without writing files. The final
tool return supplies the actual payload count and seal digest; no count or
future PASS is invented in advance inside this document.

The payload seal certifies complete directory byte coverage at that final
check. It does not validate CTM proofs, owner subtraction, source-page
integrity, universal source-input capture, a candidate gate or a paper seat.
No central index, manuscript, review, Git object or external system is changed.
