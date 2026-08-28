# Results

The canonical evidence contains 105 state rows: 3 origins, 8 nonzero
direct-braking states and 94 one-switch states.  Every exact rational branch
label and radicand is independently reconstructed; every radical time, switch
state, terminal state and off-curve HJB residual agrees to better than
`1e-70`.

- Producer: `C222_PRODUCER_PASS`
- Independent checker: `C222_CHECKER_PASS`, 2,278 assertions
- SymPy reconstruction: `C222_SYMPY_PASS`, 20 generic identities plus 105 row
  structure checks
- Canonical replay: `C222_REPLAY_PASS`, 105,431 bytes
- Hostile mutations: `C222_MUTATION_PASS`, 23 repaired-hash semantic/schema
  rejections plus one stale-hash rejection; both unknown-key mutations fail
- Evidence payload SHA-256:
  `5089209bbb8ff78167efe4005c974b1e06b139914c04370ce631540e391db5a0`
- Evidence file SHA-256:
  `f2b41252efa5b45c47c749da79c5139b81285640e0d5726d308164d5c8c76612`

The finite grid is regression evidence, not the proof of the continuum
theorem.  The sharp endpoint-moment interval provides the global lower bound.
