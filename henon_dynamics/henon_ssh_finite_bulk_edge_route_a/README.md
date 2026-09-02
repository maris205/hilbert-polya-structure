# HCS-C318: finite SSH bulk--edge atlas

This package gives a complete source-local theorem for the balanced finite
Su--Schrieffer--Heeger chain.  Its central finite-size advance is sharp:
the periodic bulk becomes topological at `w/v>1`, whereas an open chain of
`M` cells has a strictly hyperbolic edge pair exactly when
`w/v>(M+1)/M`.  The package also fixes the characteristic-polynomial
prefactor, edge-vector convention, critical taper, ring parity, every
one-hopping face, `M=1`, a boundary-safe propagator, and a mode-resolved
quench corollary with an explicit finite-grid caveat.

The periodic statement distinguishes the continuum gap `|v-w|` from the
finite sampled gap.  For odd `M` the latter is
`sqrt(v^2+w^2-2vw cos(pi/M))`; hence an odd critical ring remains sampled-
gapped even though the continuum symbol closes.

The evidence contains 55 open-chain polynomial rows, 33 exact rational edge
witnesses, 11 threshold rows, 70 periodic rows with 595 momentum cells, 33
boundary rows, 30 propagator rows with 180 entries, and six quench rows:
7,161 scalar leaves in total.  A producer-independent checker executes
10,948 checks; SymPy closes 9,181 identities; isolated replay is byte exact;
and 53 hostile repaired-hash/parser mutations are rejected.

The strict Route-A result is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`

with overall verdict `ROUTE_A_REJECTED`.  The Hermitian SSH Hamiltonian is a
natural source quantization, but it contains no arithmetic-local owner,
Euler product, target functional equation, target zero match, or
Hilbert--Pólya construction.  Route B remains locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

From this directory:

```bash
python -B code/c318_ssh_producer.py
python -B code/c318_ssh_checker.py
python -B code/c318_ssh_sympy_crosscheck.py
python -B code/c318_ssh_replay.py
python -B code/c318_ssh_mutation.py
python -B code/c318_release_manifest.py
```

The human-facing result is `paper/main.pdf`; the exact theorem is also
recorded in `THEOREM_PACKAGE.md`.  `C318_RELEASE_MANIFEST.json` is the final
content-addressed ledger.
