# Executable evidence plan

## Frozen inputs

- baseline commit `7fbe9db30cc460a82883533d7cfb2edd988c5b65`
- date `2026-09-02`, epoch `1788307200`
- Route-A evaluator v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- scope `NO_BAD_EULER_OR_ROOT_NUMBER`

## Coverage

The six exact rational scenarios cover sequential binary collision,
simultaneous three-cluster collision, disjoint simultaneous contacts,
initial coincidences, no collision, and a cascade.  The producer uses an
event loop and PAVA.  The checker imports no producer code: it enumerates
every contiguous partition, minimizes the weighted square error, derives
event candidates from block-line intersections, and compares the complete
cell grids.

The symbolic pass checks barycentric energy identities, ordering, block
constancy, telescoping energy, and weak-event residues.  Replay writes two
isolated outputs.  Hostile tests cover stale and repaired hashes, duplicate
raw JSON keys, missing/extra rows and keys, noncanonical fractions, bool/int
confusion, and theorem/proof/route/scope mutations.

The evaluation YAML has its own hostile gate: a duplicate-rejecting safe
loader preserves the date as a string, enforces the exact recursive
key/type/value tree, and checks canonical semantic SHA-256
`54650acae7553edea8e073f2c0406aaa418659a4f5442898e515d4d29c8f3130`.
Twenty-one attacks cover raw duplicate top/nested keys, unknown or missing
keys, tuple/verdict/Route-B changes, bool/int confusion, scope drift, axis
drift, and a non-object root.

Release additionally demands three distinct substantive PDF rounds, two
fresh two-pass LuaLaTeX builds per round under the fixed epoch, byte identity,
settled warning freedom, embedded/subset fonts, page and extracted-text
contracts, and the exact 28-file physical ledger.
