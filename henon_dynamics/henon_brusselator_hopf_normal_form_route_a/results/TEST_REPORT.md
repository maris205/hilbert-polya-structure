# C311 test report

| lane | result |
|---|---|
| producer | 12 `A` rows / 55 linear probes / 827 leaves |
| independent checker | 742 checks, PASS |
| SymPy derivation | 13 identities including derived `G21`, PASS |
| isolated replay | byte-identical, PASS |
| hostile mutation | 26/26 rejected |
| release | exact 27-payload manifest and deterministic PDFs |

Finite probes verify conventions and arithmetic simplification; they do not
replace the global-existence or Hopf proofs.
