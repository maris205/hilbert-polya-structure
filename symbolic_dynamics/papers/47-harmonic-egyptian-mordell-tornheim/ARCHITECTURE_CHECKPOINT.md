# Paper 47 isolated integration architecture checkpoint

Checkpoint date: `2026-08-18 UTC`

Status: `ARCHITECTURE_FROZEN_BEFORE_EXECUTION`

## Frozen input

The only research input is the immutable 15-file `preauthority/` tree.  Its
self-excluding manifest is `preauthority/SHA256SUMS.txt`, with SHA-256

```text
59f08523b58b32df0308b9416c9164a3a1745ee4c15a8c143c693a79ef7eb885
```

The copy is byte-identical to the independently audited source and is
read-only.  No authority tree, Git object, root README, mirror, Paper-46
result, target-zero table, or fitted datum is an input.

## Physically independent scientific lanes

`D` is a standalone direct lane.  It constructs ordered matrices and rows
only by the integer remainder test `(m*n) % (m+n) == 0`, retains loops, and
enumerates its own based closed walks and exact rational trace powers.

`P` is a standalone parameter lane.  It constructs support only from
coprime `(t,a,b)` triples, constructs full rows separately from divisors
`d | m^2, d < m`, and never evaluates D's divisibility predicate.  Its finite
second trace uses the termwise cutoff

```text
T = floor(N / ((a+b) max(a,b)))
```

and never extracts an infinite zeta factor.  The unrestricted versus
primitive Mordell--Tornheim identity is tested on its distinct rectangular
domain.

`X` strictly compares the independently serialized projections, including
support, loops, full rows, based-walk records, and exact traces.  Recursive
type equality precedes value equality, so Boolean, integer, and float
coercions are forbidden.

## Evidence and ownership boundaries

Finite exact computation is labeled `FINITE_EXACT_CONTROL`.  Infinite
endpoint, compactness, ideal, determinant-domain, and trace identities are
owned only by the frozen proof certificate and its read-only proof auditor.
The literature auditor separately enforces Tornheim, Mordell,
Bradley--Zhou, Tsumura, and Kalinin--Lupercio--Shkolnikov ownership; it gives
zero novelty credit to Egyptian parameterization and keeps
`STOP_DUPLICATE` outside Route.

## Mutations and consumers

`contracts/MUTATION_REGISTRY.json` freezes F01--F15 and governance controls.
For every theorem falsifier, the exact designated consumer key set and exact
rejection code are copied from the frozen theorem package.  Disposable
copies are physically mutated at typed JSON pointers.  D, P, X, A, and L
derive errors independently from the changed semantic object and do not read
the mutation registry.  Missing, extra, zero-return, wrong-code,
noncanonical, or exception outcomes are survivors.

Governance controls physically exercise duplicate keys at two depths,
noncanonical key order, missing/extra keys, list/scalar and Boolean/integer/
float attacks, check-map drift, coordinated report/ledger tampering, output
delete/rename/extra/symlink/unsafe paths, registry omission/extra/reorder and
consumer mismatch, Route tuple/Route-B/provenance matrices, pre-I/O lexical
and component-symlink rejection with an outside sentinel, exact CLI
totalization, hostile environment isolation, and mutation of the installed
auditor judged by an unchanged external auditor.

## Route and provenance

Two standalone Route-v0.2 validators recursively check the full object and
agree only on its canonical SHA-256.  State A uses exactly three pending
sentinels and forbids a paper manifest.  State B requires three identical,
nonzero, lowercase forty-hex commits and a physical self-excluding paper
manifest.  Mixed states reject.  The paper manifest excludes itself and the
pre-output seal.  The outer static manifest excludes only itself and
`outputs/`, and therefore binds the exact pre-output-seal path, regular-file
kind, mode, and hash.  The pre-output seal records only the independent base
inventory, never the outer-manifest hash.  This gives one acyclic outer root
that also binds candidate/output root modes.

Both validators check `authority_integration.status` before any normalization:
it must be an exact string equal to `PREAUTHORITY_INTEGRATION` in State A or
`PUBLICATION_SHAPED_AWAITING_ROOT_AUTHORIZATION` in State B.  DONE aliases and
Boolean/integer coercions are physical negatives in both states.

The State-B release edge is strictly downstream.  The seal binds the exact
smoke commit and a stable payload-tree hash over canonical sorted recursive
output rows excluding exactly `PAPER_MANIFEST.sha256`.  It forbids both a
paper-manifest hash and a full State-B tree hash.  After the seal is final,
the outer manifest binds it; after the outer manifest is final, the State-B
paper manifest binds that outer file.  Full State-B manifest/tree hashes are
reported only out of band and are never inputs to the seal or outer root.

## Transaction boundary

All runtime bytes are built twice in disposable sibling stages under hostile
unrelated working directories.  Every subprocess runs with isolated Python,
a minimal environment, disabled bytecode, and a hostile `PYTHONPATH` control.
The complete staged recursive namespace binds path, kind, mode, and regular
file hash.  Only after both reconstructions, mutations, Route audits, report,
ledger, `PRE_CERT`, and `FINAL` validation agree is one complete `outputs/`
directory atomically renamed.  A forced late failure happens immediately
before that rename; an exact rerun performs zero physical target writes.

The canonical candidate is never run in place and must retain zero output and
cache files.  It authorizes no authority, Git, README, mirror, registry,
publication, novelty, or priority action.
