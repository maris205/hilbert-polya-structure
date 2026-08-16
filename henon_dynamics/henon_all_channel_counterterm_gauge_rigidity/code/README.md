# Reproduction code

Run the complete P74 executable package from the project root:

    bash code/run_c74.sh

The producer replays the P72 coefficient formula, checks the weighted
root-of-unity filter, verifies both primary-factor residuals through degree
96 with exact rational arithmetic, builds finite-jet gauge witnesses, locks
the P72 and P73 proof/certificate/PDF hashes, and runs a mutation audit.  The
independent checker reconstructs the divisor coefficients without importing
the producer.  Unit tests run under both normal and optimized Python.

The finite checks certify implementation signs and artifact integrity.  The
infinite convergence and rigidity arguments are in `PROOF_PACKAGE.md` and
the paper.
