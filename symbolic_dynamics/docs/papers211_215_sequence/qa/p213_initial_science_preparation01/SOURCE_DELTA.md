# P213 compile-wrapper source delta map — author declaration

Baseline:
../p213_minimal_observer_enabled_preparation01/observe.proposed.py.txt,
SHA256 6cdc550357b0b6f8322ecc8e22d2fca9ff1d22ee5d9a46caf0c191fcc81ff25d.
Baseline binding SHA256:
0847eecba05b8038c623be0001c48defc240d86d3f63ea112520b91e8f49e156.
Baseline capture SHA256:
da71d93c5fd8c587ecbdeec339e054b6c6c0aa56a5c682b901a1c3c038b8705d.

The original accepted material remains unchanged. This author is not an
independent reviewer of the inherited source or of this proposal.

## Exact source reuse

The baseline fragment from its BINDING-is-None gate through process_points
is copied as plain source. Within that fragment only two source areas
change: 26 literal wrapper failure codes are appended to FAILURE_CODES,
and both early/helper failure-envelope destinations change from stdout
to stderr. The collector function bodies themselves are unchanged:
need, failure, same_tree, tuple_tree, frozen, attribute, loader_id,
module_snapshot, launch_snapshot, path_ok, launch_allowed, binding_entries,
module_delta, mapped_paths, missing_or_null, module_roles, raw_maps,
map_roles, canonical, full_stat, points, key_file and process_points;
the ObserverFailure class body is unchanged. Reusing failure's body does
not claim its global allowed-code vocabulary is unchanged.

In particular, key_file, points, copied/tagged snapshots, qualified loader
policies and proc-exe check-before-follow ordering are not reimplemented.
The old 99-code vocabulary is preserved and extended by the 26 new names,
not replaced by exception args or arbitrary class/text export.
COLLECTOR_REUSE_CHECK.json records plain-text equality checks, not a Python
parser, compilation, test or independent source audit.

The baseline final RESULT/main/serialization block is replaced, rather
than portrayed as an unchanged collector. Five new function bodies are
output_points, output_unchanged, load_science, boundary and same_boundary. The new top-level
flow invokes the existing science bytes and writes a separate FD 3 result.
This enumeration is descriptive; independent review must read exact source.

## Binding delta

Every occurrence of the old observer pathname in the literal is replaced
by the exact future wrapper pathname, including direct-script file roles
and argv/orig_argv. The identifier changes; one mandatory verify.py role
is appended; bounds.files becomes 70; a science block declares the accepted
byte pin, compile mechanism and new 64 MiB science-output cap. No other
module, loader, source/cache/package, native-map, optional-absence, flag,
encoding or inherited numeric bound changes. All actual observation fields
remain null; no accepted probe data is pasted into the new binding.

The BINDING.proposed.json document is converted to a Python literal with
only structural indentation and JSON null/boolean spelling conversion;
it is not a runtime import or JSON loader. The exact inline dictionary
must be independently checked against that document as source data.

## Changed runtime/capture behavior

The fixed 70-file list is keyed twice; load_science adds one separately
recorded exact-byte read before compile. The previous rule "one pass;
no new key after closing" becomes "before pass; science; after pass;
then closing with no new keys." Total successful file-read limit remains
64 MiB across both passes and the source load. File equality is checked
before adding after-only closing points.

The wrapper adds pre/post science boundaries, an exact compile/exec
globals contract, descriptor checks and separate control emission.
Scientific stdout is not replaced, read back or reconstructed. Early
failure text moves to stderr, whereas late failure data is best-effort
FD 3 output only after the descriptor safety gate. Native nonzero or
partial capture always prevents acceptance.

Each capture changes the script role and capture directory, adds a third
fresh file, maps child FD 3 from parent FD 5, closes unused child FDs 4/5,
and records the new native-exit label. Initial, replay01 and replay02 are
three separately disabled variants; only their fixed fresh directory
differs. No already-used directory is recycled or deleted.

## Independent obligations and limits

The new code is authored here but not executed, compiled, AST/syntax
parsed, imported or independently accepted. The minimal next independent
gate must check the exact source/literal/request/capture combination,
particularly compiler/global semantics, unchanged ordinary output,
source-buffer/key identity, second-pass boundary ordering, sidecar
failure/close behavior and complete raw-reception requirements.

This does not reopen accepted mathematical proofs or enlarge the finite
box. It also does not claim that old source acceptance or old probe
reception accepts the new mechanism. Any actual runtime change/unknown
or failure returns to the affected source/policy gate; no discovery loop
or automatic second operational attempt is authorized.
