# Results

The canonical ledger contains 4 parameter cases, 32 excitation blocks, 64
time-dependent propagator cases, 4 vacuum energies and 7 boundary records.
It covers resonance, positive and negative detuning, negative coupling and
the simultaneous zero-coupling/zero-detuning limit.

- Producer: `C223_PRODUCER_PASS`
- Independent checker: `C223_CHECKER_PASS`, 1,100 assertions, including a
  direct 10-dimensional finite-Fock commutator and block extraction
- SymPy reconstruction: `C223_SYMPY_PASS`, 13 generic identities plus 96 row
  structure checks
- Canonical replay: `C223_REPLAY_PASS`, 108,885 bytes
- Hostile mutations: `C223_MUTATION_PASS`, 24 repaired-hash semantic/schema
  rejections plus one stale-hash rejection; both unknown-key mutations fail
- Evidence payload SHA-256:
  `a6e6b23fe5b6a65c84827096443135ba7624e54fb5955adf4008d6eaf85b688c`
- Evidence file SHA-256:
  `ac6f6bc8f6ae3fbf4dbae6aa6212e280f403d1a8c9af9b63f61e079dbfe9f848`

The finite grid is regression evidence only.  The infinite block theorem
comes from exact conservation and the generic Pauli-square calculation.
