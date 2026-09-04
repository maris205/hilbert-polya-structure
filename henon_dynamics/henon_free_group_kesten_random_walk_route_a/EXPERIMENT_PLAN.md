# Exact-evidence and validation plan

## Frozen grid

- Degrees: \(D=4,6,8,10\), corresponding to ranks \(d=2,3,4,5\).
- Radial dynamic-programming ledger: every parity-compatible radius through time 32.
- Return, first-return, and renewal ledgers: half-times 0–64 or 1–64 as applicable.
- Parameter ledger: exact rational \(\rho^2\), speed, CLT variance, return and escape probabilities.
- Rank-one ledger: \(D=2\), half-times 0–64.

## Independent gates

1. Producer constructs the canonical JSON and self-excluding payload hash.
2. Checker independently reconstructs the radial recurrence and Catalan sequence without importing producer code, locks every nested row, and validates raw plus semantic YAML hashes.
3. SymPy checks the cavity quadratic, Schur complement, resolvent moments, Catalan renewal coefficients, return mass, drift and variance.
4. Replay rebuilds byte-identical evidence in two isolated temporary directories.
5. Hostile suite repairs payload hashes after semantic mutations and attacks JSON/YAML parsers, coordinate completeness, Route-A semantics, and the firewall.
6. Release refuses optimized Python, rebuilds every PDF twice in fresh directories at the fixed epoch, and validates text, raster, fonts, manifests, and file closure.

Finite evidence is regression-only.  It does not prove pure absolute continuity, transience, the strong law, or the CLT.
