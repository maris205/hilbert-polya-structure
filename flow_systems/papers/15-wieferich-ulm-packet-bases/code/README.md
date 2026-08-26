# Paper 15R control sources

This directory contains the two deterministic Python subjects used by the sole
reproduction entry, `../experiments/reproduce.sh`.  Source presence is not an
execution receipt, and neither file is an authority for a theorem beyond the
frozen Paper 15R control scope.

## `generate_controls.py`

The generator accepts exactly one of these interfaces:

```text
python3 -B code/generate_controls.py --verify-only --input-dir DIRECTORY
python3 -B code/generate_controls.py --generate --output-dir DIRECTORY
```

`--verify-only` opens the package, repository, and input roots through
no-follow directory capabilities.  Link/type/nlink safety is resolved before
cache-name classification.  It inventories the complete `code`, `experiments`,
and selected result trees before verification, independently parses every CSV
and the canonical JSON manifest, re-derives all arithmetic and semantic rows,
verifies the 14 authority bindings, the current design review, the historical
implementation-gate provenance, and the six implementation bindings, then
takes the same metadata inventory again.  It reconstructs the exact nodes
`A,D,R,G,I,C,M,V` and twelve edges from the existing semantic blocks and
requires the unique topological order; `dag` is not a manifest key.  It has no
repair mode and performs no write.

`--generate` is available only to an admitted reproduction worker.  FD 9 must
be a duplicate capability for the exact fresh, empty, mode-0700 generation
root named by the five `P15R_GENERATION_*` variables.  The subject authenticates
the package and authority inputs before creating the nine fixed basenames with
`O_CREAT|O_EXCL|O_NOFOLLOW`; no path fallback is accepted.  The bytes are a
pure function of checked-in source bytes and frozen integer arithmetic.  No
clock, host, PID, absolute path, network value, or random value enters an
artifact.

The future generated package is eight CSV files followed by `manifest.json`.
The CSV total is exactly 120 data rows, including exactly 35 registered
negative rows.  Canonical CSV uses UTF-8, the frozen header order, minimal CSV
quoting, and one terminal LF.  Canonical JSON uses UTF-8, sorted keys, two-space
indentation, and one terminal LF.  Each generated regular file is finalized
mode 0444.

## `test_controls.py`

The oracle has exactly 173 literal `test_*` methods:

```text
10 + 10 + 14 + 9 + 10 + 12 + 12 + 5 + 18 + 10 + 35 + 28 = 173
```

It independently parses the checked-in, fresh-A, and fresh-B roots and derives
the mathematical comparisons without importing the generator.  Each of the 35
semantic-negative methods executes the frozen seven-stage chain on a typed
atomic delta: parse seed, apply the real forward delta, serialize/reparse the
post-state, join the persisted negative, obtain a typed rejection before
detector translation, apply the printed inverse to the parsed post-state, and
test every excluded receipt coordinate against both the rejected post-state
and accepted inverse.  S02/S03 recompute their raw valuations; the owner cases
apply the supplied matrix over the complete finite block; EO/FK/TC/SG/owner/PC
predicates use closed independent primitives.  The selected metadata
comparator validates one immutable ten-coordinate receipt and creates distinct
deep `Q_mode` and `Q_mtime` clones before invoking the subject comparator.

The 28 package-negative methods use a T-only frozen method/P-ID-to-detector
registry as the independent expected oracle.  The expected token is never
serialized in a mutation descriptor or sent over RPC.  Each method sends only
a typed mutation description over its child-unique FD 4 endpoint; the guardian
creates a method-owned synthetic repository, proves a baseline generation and
verification, performs one typed mutation, and runs a new admitted generator
or copied-wrapper child.  The oracle requires status 1, empty stdout, and the
single exact expected detector line; cleanup expectations are independently
derived rather than echoed from observed output.  P27 executes five serial
variants and P28 executes two.

The literal 173-name tuple is distinct from discovery.  Both the suite runner
and its own registry test require exact name, order, uniqueness, and callable
membership, not only aggregate family counts.  The top oracle is admitted only with the exact
`STDIO_SOURCE_RPC_AUDIT_BARRIER` descriptor set.  FD 3 is read and compiled in
memory and closed before `SOURCE_READY`; FD 4 is the guardian RPC endpoint; FD
5 is the P-owned authenticated audit endpoint.  It neither forks nor imports
project code.  Each worker stream chunk is at most 1,024 decoded bytes, and the
oracle enforces an exact ceiling of 16,777,216 decoded bytes for stdout and,
independently, 16,777,216 decoded bytes for stderr; overflow is an infrastructure
failure and is never truncated into a detector result.

## Current state

These sources were authored under the sole third implementation-remediation
attempt.  Only lexical/AST/in-memory static reconstruction was permitted; the
project was not imported or executed.  The hook/custody profile hash is static
non-evidence, the current profile is unaccepted, and no successful platform
preflight, generation, 173-test suite, cleanup, or execution receipt is claimed
here.
