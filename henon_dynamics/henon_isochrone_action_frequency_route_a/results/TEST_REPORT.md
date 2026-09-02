# Test report

## Functional checks

- Producer: `C295_PRODUCER_PASS`; deterministic sorted finite JSON, no nonfinite constants.
- Independent checker: `C295 independent checker: PASS (11254 assertions; strict duplicate-rejecting JSON/YAML, exact algebraic reconstruction, direct quadratures)`; it also recursively locks the complete boundary/source/nonclaim contracts.
- SymPy: `C295_SYMPY_PASS (1099 symbolic/exact checks; circular boundary, Vieta integrals, action-frequency map, closure grid, escape and Kepler limits)`.
- Replay: two isolated nested output paths reproduce the canonical evidence byte for byte.
- Mutation: `C295_MUTATION_PASS 87/87`.

## Mathematical controls

Every orbit cell independently verifies the exact action inversion, \(E_c\leq E<0\), \(J_r\geq0\), radial frequency, reciprocal period, frequency ratio, circular condition, turning-point polynomial, orbit class, and closure class.  Noncircular cells additionally undergo direct 90-digit period integration; noncircular \(\ell>0\) cells undergo direct apsidal integration.

## Serialization controls

JSON parsing rejects duplicate keys and `NaN`/infinite constants.  Canonical boundary statements, all bibliographic fields, and all nonclaims are recursively locked by exact type and value.  YAML parsing rejects duplicate and non-string keys, merge keys, anchors, aliases, schema drift, implicit date coercion, wrong scalar types, and any semantic change through a locked canonical semantic hash.

## Build and release controls

The release script requires exact 27-file payload membership plus one self-excluded manifest, no sidecars, distinct substantive round PDFs, two isolated byte-identical builds per round, settled warning-free logs, embedded/subset fonts, expected page counts and text sentinels, final-PDF equality, and complete file hashes.
