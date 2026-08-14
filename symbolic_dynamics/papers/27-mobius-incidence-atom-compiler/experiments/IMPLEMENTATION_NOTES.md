# Implementation Notes — SD-C29

The candidate core and validation evaluator are deliberately separated.
sdc29_incidence_atom_compiler.py constructs the finite divisibility relation,
inverts its incidence zeta matrix by the poset recurrence, derives covers of
the bottom element, and builds \(q_n=Z E_n\mu\). It contains no prime
generator, primality call, factorization call, zeta-function evaluation, or
target-zero call.

sdc29_evaluator.py uses trial division and a direct scalar Möbius evaluator
only after the candidate is frozen. It checks that source covers agree with
ordinary rational primality and that the compiled kernel has the expected
arithmetic Möbius entries.

Finite matrices and determinants use SymPy exact integers/rationals. CSV
writers explicitly set LF line termination; the integrity audit rejects any
carriage-return byte. Weighted-Hilbert displays use 50-digit mpmath arithmetic,
but their theorem status comes from the analytic rank-one norm derivation, not
from numerical tolerance.

The canonical runner clears only this paper's results files, executes
generator/tests/analyzer twice with PYTHONHASHSEED=0, compares all code and
generated-result hashes, removes local caches, audits the strict pending
provenance schema, and freezes the final code/result SHA ledger. It performs no
Git operation.
