# Implementation Notes — SD-C30

The candidate core accepts only a finite topologically ordered poset relation
and numeric source labels. It computes the incidence zeta inverse, primitive
idempotents, source covers, weighted transpose, native Gram matrix, chiral
blocks, positive metrics, and orthogonal atom blocks. It contains no prime
predicate, factorization routine, target coefficient table, zeta-zero call,
or fitted spectral information.

The evaluator is a separate frozen module. It supplies the standard integer
divisibility downset, a relation mutation that promotes 6 to an atom, a
composite-only divisibility subposet, and a deterministic seeded locally
finite DAG. The latter three are PROVES_TOO_MUCH controls, not alternate
candidates.

All claim-bearing matrix identities, rational coefficients, Laurent
expressions, characteristic polynomials, and metric certificates use exact
SymPy arithmetic. The twelve common-t samples are explicitly nongating. Every
CSV writer sets LF line termination. The integrity audit rejects carriage
returns, non-text control bytes, local caches, route-schema drift, missing
artifacts, target-zero use, and mismatched pending provenance.

The canonical runner clears only this paper-local results directory. It runs
the generator, 61-test suite, and analyzer twice under PYTHONHASHSEED=0,
compares byte hashes, removes caches, audits integrity, and freezes a SHA-256
ledger. It performs no Git operation.
