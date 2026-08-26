# Paper 12 deterministic controls

`generate_controls.py` builds eleven deterministic CSV ledgers for the frozen
`P12-9` control family. The ten v2 ledgers retain their exact bytes. The v4
ledger, `orbitwise_standardization_h1_controls.csv`, adds 3,252 rows of exact
common-cycle `Z`-action algebra: 9 model rows, 90 basepoint rows, 3,151 strict
automorphism rows, and 2 negative rows. The full package is 3,486 body rows.
`test_controls.py` provides at least 96 meaningful unit and fail-closed tests.

The implementation uses only the Python standard library. Exact combinatorial,
integer, set, schema, and symbolic checks have zero tolerance. The sole
`1e-12` absolute tolerance is confined to the displayed `log`/`sqrt` period
values and their scale comparisons; `.15g` is the frozen printed format.

The v4 finite linear algebra computes the actual and standardized degree-one
dimensions (`1` and `m`), the rank-one diagonal, the one-dimensional full
symmetry invariant space, the strict automorphism count `n^m m!`, a nonzero
coboundary with zero cycle sums, and exact zero-isotropy potential recovery.
It also rejects mixed cycle lengths and the reverse topology/comparison
direction, and recovers the transitive case at `m=1`.

These finite cyclic-time and finite-topology models are witnesses and
falsifiers. They do not prove the real, infinite-`Q`, choice, source, or
topology theorems. Packet rows are schematic and never replace the source
proof. `LABEL-SWAP` intentionally records the `PROVES_TOO_MUCH`
arithmetic-specificity boundary.

Run the complete contract from the paper directory with:

```bash
./experiments/reproduce.sh
```

Strict read-only verification alone is:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/generate_controls.py \
  --output-dir results --verify-only
```
