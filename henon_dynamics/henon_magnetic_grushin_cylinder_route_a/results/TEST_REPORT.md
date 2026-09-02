# Test report

- deterministic producer: PASS, 293 audited cells
- strict independent checker: PASS, 2,053 assertions
- SymPy cross-check: PASS, 750 identities
- isolated evidence replay: PASS, 2/2
- hostile mutation suite: PASS, 75/75 (54 evidence JSON, 21 evaluation YAML)

Heat traces are checked by direct summation of individual oscillator levels,
not by the producer's closed `1/(2sinh)` expression.  All nested keys, exact
types, canonical fractions, finite decimal strings, unique complete grids,
theorem/proof contracts, full integer spectral type, references, Route tuple,
and forbidden flags are locked.
The YAML gate uses a duplicate-rejecting safe loader, exact recursive
key/type/value validation, and semantic SHA-256
`e3ff56c62d1830a03a8a0b2a7d33acf73d6d997de4d9c872e6f6ff278d98adae`.
