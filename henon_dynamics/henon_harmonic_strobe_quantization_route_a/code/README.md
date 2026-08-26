# C178 exact code

- `c178_harmonic_strobe_producer.py` generates the content-addressed exact
  ledger from the frozen oscillator and finite regression cutoffs.
- `c178_harmonic_strobe_checker.py` reconstructs every finite row and all
  claim-bearing metadata without importing producer code.
- `c178_sympy_crosscheck.py` separately verifies rotation, reversal,
  Hamiltonian, differential-operator commutator, Laguerre, cyclotomic, and
  irrational-angle identities, including the metaplectic \(2\pi\) sign and
  \(4\pi\) return.
- `c178_replay.py` regenerates the evidence in a temporary directory and
  requires byte identity.
- `c178_mutation.py` changes semantic fields, repairs the payload hash, and
  requires the separate checker to reject every mutation; it also tests one
  stale-hash mutation.
- `c178_release_manifest.py` closes the 27 payload files after the final PDF
  build and excludes its own content-addressed manifest.

Run the six commands from the package root in the order listed in the main
`README.md`.  Finite ledgers are regression sentinels, not proof of the
all-angle theorems.
