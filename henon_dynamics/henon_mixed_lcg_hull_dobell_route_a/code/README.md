# Executable evidence

- c258_lcg_producer.py builds the exact modulus census, primitive-cycle
  ledgers, fixed counts, local valuation rows, and source-zeta receipts.
- c258_lcg_checker.py independently enumerates every affine parameter pair
  through modulus 96 and reconstructs every recorded identity.
- c258_lcg_sympy_crosscheck.py verifies affine iterates, cycle determinants,
  Koopman unitarity, and odd/dyadic valuation samples.
- c258_lcg_replay.py requires byte-identical evidence regeneration.
- c258_lcg_mutation.py recomputes payload hashes after each hostile semantic
  change and requires the checker to reject every change.
- c258_release_manifest.py closes the release ledger after the PDFs exist.

All finite-ring arithmetic is exact.  The census is a regression oracle for
the all-modulus proof, not a replacement for that proof.
