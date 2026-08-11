# HCS-C30 exact code release

## Producer

`c30_producer.py` source-locks the C25, C26, and C29 artifacts and reconstructs
three noncommuting chronological actions without importing a transition
average:

- raw covariant homology \(B(t)\), used only as a convention control;
- genuine forward Rauzy lengths \(B(t)^{-\mathsf T}\);
- transfer inverse branches, obtained by reversing each raw path phase and
  applying \(B(t)^{\mathsf T}\).

It checks all cyclic phases of C1, C2, and \(W_{24}\), creates canonical exact
Farkas descriptors, and emits the roof, repetition, operator, flat-trace,
Route-A, and pivot contract in canonical JSON.  Runtime paths, platform
versions, and caller environment fields are excluded from the payload.

## Independent checker

`c30_independent_check.py` imports no producer code.  It independently loads
the upstream sources, reimplements integer matrix inversion and chronology,
reconstructs every phase and descriptor, verifies the payload digest, and
uses recursive type-strict schema comparison.  Unknown keys and JSON numeric
coercions fail closed.

## Tests

`test_c30.py` covers deterministic output, all-phase census, raw convention
controls, exact representative rows, final identity products, Farkas
primitivity, roof and trace decisions, source locks, rehashed semantic
mutations, strict numeric types, malformed JSON, an AST import firewall,
uncached checker CLI success/failure, and exact unimodular inverse fuzzing.

Final gate and test counts are recorded in `../results/TEST_REPORT.md`.

## Reproduce the release

From any working directory:

```bash
/absolute/path/to/rauzy_inverse_roof_trace_obstruction/code/run_c30.sh
```

The default invocation is read-only: it verifies the existing manifest,
recomputes the JSON artifacts in a private temporary directory, runs the test
suite, compares the outputs byte-for-byte, and verifies the manifest again.
All Python calls use isolated mode and an isolated bytecode cache.

An intentional release refresh is separate:

```bash
/absolute/path/to/rauzy_inverse_roof_trace_obstruction/code/run_c30.sh --refresh-manifest
```

The refresh option is the only path that replaces official JSON artifacts or
writes the manifest.
