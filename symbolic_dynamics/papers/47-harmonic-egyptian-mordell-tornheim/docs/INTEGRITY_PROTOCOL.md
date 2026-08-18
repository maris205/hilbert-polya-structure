# Integrity protocol

1. Validate the absolute integration root, every component kind, the exact
   static seal, immutable preauthority bytes, CLI arity, and output target
   before caller-selected I/O.
2. Invoke D and P independently from hostile unrelated working directories.
3. Strictly compare type and value, run proof/source/type/independence/
   literature audits, physical mutation suites, and two Route validators.
4. Reconstruct the report and result ledger mechanically from canonical
   artifacts.  `PRE_CERT` emits the integrity certificate; `FINAL`
   reconstructs it byte-for-byte and validates the exact recursive tree.
5. Build twice, require byte identity, then atomically rename the whole
   staged `outputs/` directory.  Never overwrite an unequal existing tree.
6. A forced late failure exits 86 before target I/O.  A byte-identical rerun
   performs zero replacements and does not change target or parent metadata.

The self-excluding outer static manifest includes the complete pre-output
seal as an ordinary path/kind/mode/hash row.  The seal does not contain the
outer-manifest hash; it binds only the seal-independent base inventory and
the disposable smoke certificates.  This is the immutable acyclic release
root.  Physical root-mode, seal-mode, seal-field, and seal-byte changes are
negative controls.

The release order is topological: finalize the seal, generate the outer
manifest once, and only then generate State B.  The seal never records a
State-B paper-manifest hash or full State-B tree hash.  Its only State-B byte
certificate is
`sha256(canonical(sorted recursive output rows))` for the exact domain that
excludes only `PAPER_MANIFEST.sha256`; each row binds path, kind, mode, and a
regular-file hash.  The seal also binds the exact disposable smoke commit.
The downstream State-B paper manifest excludes itself and the seal, includes
`STATIC_TREE_MANIFEST.json`, and thereby binds the finalized outer root.
Fresh full State-B tree and paper-manifest hashes are out-of-band evidence and
must never feed back into either seal or outer-manifest domain.

State A forbids `PAPER_MANIFEST.sha256` and uses exact pending provenance.
State B requires equal nonzero forty-hex commits and a physical manifest
excluding itself and `PREOUTPUT_STATIC_SEAL.json`.  Symlinks, FIFOs, sockets,
devices, unsafe paths, empty extra directories, mode drift, host tokens, raw
duplicate JSON keys, and Python scalar coercions are all fatal.
Before Route normalization, both independent validators require the authority
status to be an exact string: `PREAUTHORITY_INTEGRATION` in State A and
`PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION` in State B.
