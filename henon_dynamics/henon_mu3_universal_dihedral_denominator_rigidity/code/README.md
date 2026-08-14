# HCS-C54 exact certificate code

This lane produces and independently checks the exact certificate for the
universal projective-monomial symmetry and split-denominator rigidity
theorems.  It uses exact integer and `Q(rho)` arithmetic only; no Frobenius
prime, floating point, or heuristic random sample enters a theorem gate.

Run the frozen artifacts without changing them:

```bash
./code/run_c54.sh
```

Refresh the certificate, independent check, persistent scoped manifest, and
full-project manifest as one rollback-safe transaction:

```bash
./code/run_c54.sh --refresh-results --refresh-manifest
```

`--refresh-results` is rejected unless `--refresh-manifest` is also present.

The producer performs the finite exact mutation guards.  The checker has its
own group, parity, divisor, Cayley quotient, character, and counterpacket
logic; it rejects duplicate JSON keys, unknown envelope keys, and exact-type
changes before accepting all 36 semantic gates.  The checker classifies every
scalar leaf into 198 exact semantic locks, 876 exact-derived leaves, or four
explicit chronology-only nonsemantic hashes; every semantic leaf is
mutation-tested after both digest locks are rebound.  The unit suite includes
targeted hostile mutations and rollback tests after promotion moves 1, 2, and
3, including a target that was absent before the transaction.

The C53 source lock reads its Route from the frozen provenance commit with
`git show`, verifies the committed Route hash, parses the release tuple, and
checks the implementation, certificate, payload, independent-check, and
code/results-manifest hashes exactly.  No live Route substring is trusted.

`c54_atomic_promote.py` is rollback-atomic and exception-safe for this local
four-file update protocol.  It does **not** claim crash consistency or
power-loss atomicity.  `results/CODE_RESULTS_HASHES.sha256` deterministically
binds exactly the seven release code files and four release result files; both
manifest files are excluded from that 11-entry scope.  The full-project
manifest inventories the complete frozen project, including the persistent
scoped manifest, root documentation, manuscript and compiled PDF,
byte-identical root and archived Route-A records, code, and results.  LaTeX
build intermediates, extracted `main.txt`, Python caches, and the full-project
manifest itself are excluded.  The default runner reconstructs both JSON
artifacts in a temporary directory, checks Route-A byte identity, and verifies
both manifests without modifying stable bytes.
