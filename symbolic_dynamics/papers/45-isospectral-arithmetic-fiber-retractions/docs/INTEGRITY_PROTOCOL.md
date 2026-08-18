# Integrity, namespace, and chronology protocol

The declared runtime namespace is exactly the eight paths listed in the
frozen experiment contract.  Each installed leaf is a regular mode-`0444`
file; the installed `results` directory is mode `0555`.  No symlink,
non-regular leaf, undeclared descendant, absolute path, parent segment,
Python cache, auxiliary file, host token, or environment-derived expected
value is legal.

The driver constructs a deterministic State A/State B ledger inside the
declared `integrity_audit.json`.  State A contains all eight pending
path/kind/mode/hash/size/mtime entries.  State B records the six non-circular
payloads with actual regular-file mode, SHA-256, size, and canonical mtime;
the integrity record and manifest are explicitly listed as self-excluding
cycle boundaries.  Provenance records the frozen contract/schema/registry,
Route, integration contract, four source-manifest seals, and both evaluator
output seals.  The verdict is PASS iff every strict integrity Boolean is
true and the state closure is exact.

The `PRE_CERT` phase is output-free and checks every frozen source manifest.
The `FINAL` phase refuses to start unless `PRE_CERT` passes in the same
process.  Evaluator output embargoes are enforced with temporary sandboxes:
A cannot resolve B's tree or output, and B cannot resolve A's tree or
output.  Only sealed projections are copied into the comparator sandbox.

The root CLI argument is mandatory.  Execution additionally requires the
exact mode-`0444` `.paper45-disposable-root.json` marker and a root strictly
below `/tmp`; the result-free sealed candidate deliberately has no marker.
Every temporary workspace chooses `/tmp` explicitly and child environments
replace hostile `TMPDIR`, `TMP`, and `TEMP`.  Subprocesses start in their own
process groups; timeout handling kills and waits for the entire group.  The
implementation also ignores untrusted cache, tolerance, and expected-value
variables, and disables Python bytecode in every child.
