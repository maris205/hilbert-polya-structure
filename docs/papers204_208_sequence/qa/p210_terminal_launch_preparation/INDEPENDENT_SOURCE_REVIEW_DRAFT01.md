# Bounded independent infrastructure source read — one open ordering defect

Reader process:
`/root/p210_checkpoint_planner/terminal_outer_launcher/outer_source_safety_check`.
Scope: only the complete 304-line launcher, INPUT_CONTRACT.json and README.md.
No inspected program was imported/invoked; no edit, inventory or page-view was
performed. This is infrastructure source review, not manuscript review or a
native execution test. Launcher SHA256:
`59db5f6e2dbf3dfc0cc612efea679f608e188d6d575dc3627d8f19ae983b17fc`.

## Open finding OUTER-DRAFT01-ORDER

`builder_closure()` calls `manifest(BUILD_OUT)` before validating RESULT.json,
the complete native-command census, settled-stream flags, absence of native
command groups and absence of UNCLOSED.json. That manifest call hashes every
listed builder payload. A zero-return/reaped builder with a detached residual
native-command group can therefore cause builder-stream hashing before the
later rejection. Outer builder.stdout/builder.stderr files are not hashed on
that path, but the no-hashing-mutable-builder-payload invariant is violated.
The failure row's `streams_hashed=False` does not explain the prior internal
builder-payload hashes. Static success is not runtime-safety acceptance.

Before an executable revision, validate closure/schema without hashing those
payloads, then verify the complete manifest and ensure the RESULT bytes checked
for closure are exactly the bytes bound by that verified manifest. Preserve
the existing prohibition on outer stream hashing/sealing after failed closure.

## Scoped source checks without findings

The builder gets a new session/group and bounded 21600-second wait. Original
wait outcome/exit/exception remain separate from cleanup return. Abnormal wait
or any cleanup prevents outer stream hashes/sealing. The hard unbound gate is
before mkdir, runtime observation and native launch. The advertised 33 ordered
command labels, two builds, empty failures, NOT_VIEWED and noncompletion flags
are checked. Outer stream hashes and sealing occur only after builder_closure
succeeds. These source observations do not establish live process behavior.

Full correspondence with the actual writer's entire RESULT schema is not
established by this three-file review. The reader did not widen its scope to
the writer. The preparer has relayed the finding to the parent/root and left
the source unchanged under the parent's explicit hold pending coordination.
