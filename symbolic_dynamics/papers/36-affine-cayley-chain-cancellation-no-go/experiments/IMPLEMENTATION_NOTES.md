# SD-C38 implementation notes

## Process separation

`source_generator.py` imports the byte-preserved neutral `source_core.py`.
`evaluate_results.py` imports only the semantically identical evaluator helper
whose extra blank terminal line is removed for authority exact-EOF, and
independently reconstructs every decisive object. The firewall parses AST
imports and identifiers; string-literal policy descriptions do not count as
candidate oracles.

## Independent methods

- source affine multiplication versus evaluator right-action recurrence;
- source free reduction helper versus evaluator independent stack reduction;
- source finite path-chain matrices versus evaluator rebuilt incidence and
  closed-path columns;
- evaluator Gauss-Jordan rational rank and direct boundary composition;
- exact fractions for all trace coefficients and damping weights.

## Prototype boundary

The prototype aggregate `499b1a...` is never copied into authority results.
The authority regenerates its own 19-payload scientific aggregate. The bridge
certificate verifies prototype file hashes and the frozen 33 semantic checks.

## Execution

Fresh A and B use distinct initially absent result directories. Cold C begins
after a cache purge and uses a third initially absent directory. Run A is
published only after payload hashes and captured stage stdout agree across all
three runs.

The scientific pipeline is Python-standard-library only. PyYAML is scoped to
Route-A sealing and integrity audit and is separately version-locked.

## Metadata boundary

The Stage-1 SHA ledger excludes the Route YAML. Its scientific fields are
fixed, while the three paired provenance fields and freeze note may change in
metadata-only Stage 2. The strict auditor accepts only all-pending or one
identical lowercase 40-hex triple. It never reads the root paper manifest.

The idempotence harness copies the authority tree to an isolated temporary
root, tests pending and dummy-sealed Route cards with a manifest both present
and absent, and requires the 43-entry ledger and integrity JSON to remain
byte-identical. It restores no authority file because all mutations occur only
inside the temporary copy.

## Scope

Finite word and chain computations certify implementations and controls. They
do not replace the infinite contractibility, marker, trace-class, or
all-orders supertrace proofs.
