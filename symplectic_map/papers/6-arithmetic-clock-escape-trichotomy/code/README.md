# Additive capacity audit implementation

This package is a deliberately small, standard-library-only implementation of
the version-2 proof, scope, provenance, and exact-control ledgers.  It does not
enumerate primes, read prime or Riemann-zero data, solve periodic orbits, call a
numeric logarithm, fit parameters, or compare approximate values.

The implementation has two execution levels:

1. `python -m compileall -q code` and `pytest` are noncandidate development
   checks.  They use formal labels and the frozen exact boundary controls only.
2. `python code/scripts/run_registered_audit.py` is the single registered
   audit.  It fails closed unless `results/CODE_REVIEW.md` contains exactly one
   valid independent deployment authority bound to both the source-lock hash
   and the reviewed code-tree hash, and unless final Paper-3/Paper-4 upstream
   bindings are present.

The registered command must not be run during pre-execution implementation.
An independent code reviewer should first inspect the source lock, proof and
scope ledgers, every executable module, and the tests.  The authority format is
defined in `capacity_audit.review_gate`; explanatory prose must not repeat the
authority prefix because duplicate occurrences fail closed.

Both upstream terminal packages are now frozen in
`experiments/upstream_bindings.json`.  The binding names and hashes the actual
Paper-3/Paper-4 source locks, proof packages, final result manifests, terminal
pipeline states, final integrity records, approved PDFs, and independent
Round-2 reviews.  The upstream validator checks those bytes and their terminal
pipeline semantics rather than accepting the binding's status text as
evidence.  Installing the Paper-4 hashes changed the reviewed code tree, so the
previous independent authority is intentionally stale and the registered
command remains closed until a fresh independent review binds the new tree.

Machine output is a dependency/provenance audit, not an automated proof of
Hermite--Lindemann or the valuation theorem.  The mathematical proof remains in
`notes/PROOF_PACKAGE.md` and has already received an independent pre-execution
attack.
