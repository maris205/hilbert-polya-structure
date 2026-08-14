# HCS-C53 release test report

The safe runner performs four layers of validation:

1. deterministic producer replay;
2. an independent exact \(\mathbf Q(\rho)\) checker with recursive schema and
   frozen full-payload gates;
3. targeted rehashed mutations, including chronology, phase, determinant,
   Galois orbit, Reynolds/field-transfer denominators, twist conventions,
   Frobenius convention, characteristic/local-polynomial integrality,
   reciprocity pairing, split/inert/Artin scope, duplicate JSON keys, and
   type-smuggling attacks;
4. a strict full-project manifest, byte identity of the root and archived
   Route-A records, and atomic-promotion rollback tests after moves one, two,
   and three, as well as a transaction with a missing initial target.

Current release baseline: **20/20 checker gates PASS** and **63/63 targeted
tests PASS**.  The default executable is `./code/run_c53.sh`; it regenerates
the certificate and independent check under a temporary directory, compares
them byte-for-byte with the release copies, checks the Route-A archive, and
verifies the full-project manifest without modifying stable bytes.
