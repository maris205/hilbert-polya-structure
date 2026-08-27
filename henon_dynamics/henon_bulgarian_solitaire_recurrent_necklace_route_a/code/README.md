# C190 executable contract

- `c190_bulgarian_necklace_producer.py`: exact combination-word producer,
  fixed/period/cycle/zeta/spectrum ledger, and reflection checks.
- `c190_bulgarian_necklace_checker.py`: producer-independent Cartesian-product
  words plus descending-recursion enumeration of all 215,307 partitions and
  their full functional graphs.
- `c190_sympy_crosscheck.py`: separate symbolic partition/binomial/Möbius,
  determinant, trace, Burnside, and N=8 matrix reconstruction.
- `c190_replay.py`: byte-for-byte producer replay.
- `c190_mutation.py`: 118 semantic repaired-hash and one stale-hash rejection.
- `c190_release_manifest.py`: self-excluded content-addressed release ledger.

No checker imports the producer.  The producer writes canonical evidence; the
release script writes the manifest.  The finite partition census is a
regression oracle and is never promoted to an all-parameter proof.

All programs use only package-local evidence and declared mathematical source
data.  They do not read target zero or prime tables, arithmetic local data,
Euler factors, root numbers, automorphy data, Hilbert--Polya inputs, or Route-B
artifacts.
