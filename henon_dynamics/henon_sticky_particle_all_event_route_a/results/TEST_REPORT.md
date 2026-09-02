# Test report

- deterministic producer: PASS
- strict producer-independent checker: PASS, 1,538 assertions
- exact SymPy cross-check: PASS, 255 identities
- isolated byte replay: PASS, 2/2
- hostile mutation suite: PASS, 66/66 (45 evidence JSON, 21 evaluation YAML)

The checker rejects duplicate JSON keys before ordinary deserialization,
nonfinite JSON constants, unknown/missing keys, duplicate/drop cell grids,
noncanonical rational strings, and exact-type confusion including JSON booleans
where integers are required.  It locks theorem/proof contracts, Route-A tuple,
scope flags, source/evaluator/date/epoch, references, and all expected cells.
The YAML gate uses a duplicate-rejecting safe loader, exact recursive
key/type/value validation, and semantic SHA-256
`54650acae7553edea8e073f2c0406aaa418659a4f5442898e515d4d29c8f3130`.
