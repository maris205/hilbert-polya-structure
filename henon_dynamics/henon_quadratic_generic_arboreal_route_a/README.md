# HCS-C393: Generic quadratic arboreal dynamics

The generic inverse tree of X²+1 has full binary Galois groups at every height, an exact cycle-index law and Galois-cover genus, and yields a rigorous zero limit for the proportion of periodic points modulo primes.

Read the [complete proof](proof/ANALYTIC_PROOF.md), [paper plan](PAPER_PLAN.md),
[source audit](SOURCE_AUDIT.md) and [final manuscript](paper/main.pdf).
The latter is delivered only after the release gate closes; its final hashes
are in `C393_RELEASE_MANIFEST.json`.

A transcendental generic basepoint is not every numerical specialization. Each fixed height has finitely many bad primes; no prime stays good at every height. The limiting argument fixes height before taking the prime limit, then sends height to infinity.

Strict tuple: `(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`;
overall `ROUTE_A_EXPLORATORY`. Scope `NO_BAD_EULER_OR_ROOT_NUMBER`.
Source theorems and classical dependencies are not target success or novelty certificates.

Build and verify: [reproducibility](REPRODUCIBILITY.md). Current evidence
contains exact finite regression data; infinite statements are proved separately.
