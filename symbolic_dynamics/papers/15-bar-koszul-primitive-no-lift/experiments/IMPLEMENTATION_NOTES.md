# SD-C17 Implementation Notes

## Reproduction

Run from this paper-project directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/sdc17_bar_koszul_experiment.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code pytest -q -p no:cacheprovider \
  code/test_sdc17_bar_koszul_experiment.py
sha256sum -c results/SHA256SUMS.txt
```

The generator rewrites only `results/`. It requires the Python standard
library; `pytest` is required only for the test suite. It performs no network
request and loads no prime table, zero table, or external dataset.

## Exact implementations

- Necklace enumeration canonicalizes cyclic rotations and tests least period
  independently of the determinant identity.
- The `p^2q^2` ledger stores target-degree primitives and lower-degree
  repetitions in separate rows with exact `Fraction` log weights.
- The `S_3` certificate computes fixed points directly for representatives
  of all three conjugacy classes and recovers irreducible multiplicities by
  character inner products.
- Stirling numbers are computed recursively; cyclic partitions are generated
  independently and grouped by their number of blocks.
- The contractible block is evaluated from explicit `2 x 2` differential and
  homotopy matrices; zero supertraces are computed from matrix powers.
- Rational controls use frozen local `random.Random` instances and store
  deterministic hashes of exact fractions.

## Artifact discipline

CSV writers use an explicit LF line terminator. JSON keys are sorted. The
checksum ledger contains both code files and every result artifact other than
the ledger itself, with paths resolved from the paper-project root.

No numerical approximation supports a theorem statement. The finite
certificates are exact; the all-degree Stirling identity is a mathematical
formula stated in the manuscript, while the computation is a bounded
independent check through the frozen cutoff.

Bytecode and pytest cache creation are disabled in the reproduction commands
so the shareable directory remains cache-free.
