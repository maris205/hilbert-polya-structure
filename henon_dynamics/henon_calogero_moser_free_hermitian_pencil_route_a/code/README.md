# C196 executable contract

- `c196_calogero_moser_producer.py`: exact Gaussian-rational Hermitian,
  commutator, trace, and energy ledgers plus deterministic LAPACK pencil and
  scattering sentinels.
- `c196_calogero_moser_checker.py`: producer-independent realified-Jacobi
  spectra, polynomial spectral projectors, centered-difference velocities,
  exact rational reconstruction, and semantic source/scope validation.
- `c196_sympy_crosscheck.py`: separate exact matrix powers, characteristic
  polynomials, generic three-particle sign/factor identities, and symbolic
  inverse-atlas sign.
- `c196_replay.py`: byte-for-byte producer replay.
- `c196_mutation.py`: 135 semantic repaired-hash and one stale-hash rejection,
  including unknown-key injections at every finite-regression nesting level.
- `c196_release_manifest.py`: self-excluded content-addressed release ledger.

No checker imports the producer.  The producer uses Hermitian LAPACK
eigenvectors; the checker instead realifies each complex matrix and uses a
hand-written Jacobi method, obtains intercepts from polynomial projectors,
and obtains velocities from centered differences.  SymPy is a third exact
path.

The 18 finite systems are regression oracles only.  None of the programs
reads target zero or prime tables, arithmetic local data, Euler factors, root
numbers, automorphy data, target divisors, Hilbert--Polya inputs, or Route-B
artifacts.
