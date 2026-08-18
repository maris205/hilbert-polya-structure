# Integrity and transaction protocol

## Trust anchor

`PREOUTPUT_STATIC_SEAL.json` is the sole pre-output seal.  It hashes
`STATIC_TREE_MANIFEST.json`, whose recursive rows bind every static path, node
kind, mode, and regular-file hash while excluding both itself and the seal.
The seal enumerates all 18 frozen input objects (17 source files plus their
manifest), fixes contract and namespace counts, and records disposable smoke
observations.

The frozen external auditor checks the exact seal object, recursive static
tree, every mode and byte, complete input map, cache/symlink/nonregular-node
hygiene, and frozen preauthority manifest hash.  Its own eight-mutation test
runs against copies, never against the canonical candidate.

## Pre-I/O gate

Before creating a staging directory or opening a caller-selected runtime
path, the transactional parent validates its resolved package root, the
lexical and resolved `outputs/` target, every existing ancestor, absence of
symlinks, cache hygiene, and the frozen external audit.  Every later staged
path must be a safe POSIX-relative member of the contract namespace.

Subprocesses run with `python -I -B`, a minimal environment, cache writes
disabled, an unrelated CWD, a hostile `PYTHONPATH`, and paired naive/isolated
module-shadow controls.

## Build and commit

The parent constructs two full stages, including evaluators, comparator,
proof/source/type/independence audits, Route card, two Route audits, 20-instance
mutation results, eight external-auditor mutation results, canonical report,
result ledger, integrity certificate, and (State B only) paper manifest.  The
two exact trees must be byte-identical.  A derived opposite provenance state
must also pass, while five mixed-state Route mutations must fail in both Route
auditors.

The result ledger covers the exact pre-certificate tree except itself.  In
`PRE_CERT`, the integrity auditor independently reruns and reconstructs the
source packet, exact comparison, proof/source/type/independence audits,
complete mutation records, two full-object Route audits, canonical report, and
ledger, then emits the certificate.  In `FINAL`, it reconstructs that stored
certificate byte for byte and validates the complete recursive final tree.
The State-B paper manifest excludes itself and
`PREOUTPUT_STATIC_SEAL.json`, eliminating the former manifest/seal cycle.
Both recorded final-tree hashes cover canonical recursive rows strictly below
`outputs/` and never cover the seal or any static-root byte.  The final smoke
includes a seal-byte mutation control proving that the output-tree hash is
unchanged while the frozen auditor rejects the altered seal.

After all validation, forced late failure returns `86` without touching the
target.  Otherwise an absent `outputs/` is installed by one atomic rename.  If
an exact tree already exists, the parent returns success with zero physical
target writes.  An unequal existing tree is a hard stop; no replacement or
partial repair occurs.
