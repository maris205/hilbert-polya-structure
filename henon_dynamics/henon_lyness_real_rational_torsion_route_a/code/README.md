# Independent implementation lanes

- c390_lyness_producer.py: Fraction recurrence, Jacobian products, canonical
  complete cycles, rational Machin/cosine witnesses and denominator grid.
- c390_lyness_checker.py: no producer import, no SymPy; verifies scalar
  recurrence, reversed recurrence, dual derivatives, full canonical support,
  strict rational types, independently bracketed pi/cosine bounds and YAML.
- c390_lyness_sympy_crosscheck.py: symbolic identities and 90-digit quartic
  Abel quadrature; those numerical integrals are not interval certificates.
- c390_lyness_replay.py: two distinct working-directory byte reconstructions.
- c390_lyness_mutation.py: repaired-hash semantics and actual JSON/YAML attacks.
- c390_release_manifest.py: exact ledger and release reconstruction;
  --write is subject to the same gates as nonwrite.

Every executable rejects optimized Python, so assert-based verification
cannot be silently bypassed with -O or -OO.
