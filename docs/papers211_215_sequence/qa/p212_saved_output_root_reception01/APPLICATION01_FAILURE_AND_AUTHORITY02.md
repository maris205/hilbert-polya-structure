# Actual first application failure and separately scoped second authority

The actual initial01 application (a1504b/session 6703, e6e205/exit 1)
is failed and immutable: 21 payloads / 22 files, seal 2034 bytes,
3f3f6198cea51a2a0cf9e10b848f7a3b4393930474b82022525770d68e9ee7b0.
All three native commands and complete original streams are retained.
The receiver stdout has zero bytes; its stderr has 1298 bytes and records
Node's SyncWriteStream reaching fs.writeSync while writing its final receipt
at receiver line 832. Root's version-04 guard erroneously denied that standard
output operation as if it were an ordinary filesystem write. The observed
events contain the four actual read paths, four declared Module loads and
the denied writeSync event. No successful semantic receipt was emitted, and
root does not adopt or reconstruct a missing receipt from this failure.

Root fully reviewed a narrowly separate node_preload05.js. It changes only
the exact new runtime-binding/capture locators, removes writeSync from the
blanket forbidden ordinary-write list, and permits that exported operation
ONLY on the already owned descriptors 1 and 2, recording the actual stream
and returned byte count. All ordinary-file write operations and all other
descriptor writes remain forbidden. The Node builtin implementation and
eight resolved maps, actual file/loader/configuration/settings key, three
submitted imports, four input paths, receiver source, parameters and saved
scientific bytes are unchanged. The actual version-04 builtin-only discovery
is reused under those complete keys; no source string or host referent is
learned from the failed application. Its old lock is not modified.

run_semantics02.py differs from the first controller only in its exact own
source/runtime-binding/output names. A separate documentary preparer must
check both entire source deltas, the whole immutable failure package and
all original keys before emitting NODE_RUNTIME_LOCK02.json (only the explicit
preload option field changes) and RUNTIME_BINDING02.json. The original
six-field BINDING.json stays unchanged because all its four inputs are the
same. No first binding, controller, source, failure or accepted seal changes.

Under this separate root decision, after that actual documentary gate passes,
ONE explicitly invoked initial02 saved-output application is authorized.
This is not automatic retry by the driver, an extra scientific producer,
a canonical adoption or an independent manuscript review. Any new failure
must again be preserved. No broader source/runtime permission, carrier-size
change, Git operation, external action or paper completion is authorized.
OWNER_AMBER / HOLD_EXTERNAL.
