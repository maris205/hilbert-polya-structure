# Root forward private-I/O scope clarification

node_preload03.js completed the actual builtin-only import probe successfully.
Before enabling any semantic application, root reviewed the exported-fs
guards and made a separate node_preload04.js: the root recorder's own
exclusive write helper explicitly enters its private-I/O scope, and denied
exported write wrappers allow only that root private scope to call their
original functions. This protects recorder internals that may call exported
fs helpers on different Node paths; it does not permit a receiver write.
These are the only two source deltas. No failed receiver execution motivated
the change; there has not yet been a receiver execution. Both older probe
failures and the successful version-03 sample remain intact.
