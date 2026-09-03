# HCS-C336: Crow--Kimura single-peak full finite-genome spectrum

This package proves the exact projective nonlinear flow and complete spectrum
of the finite binary Crow--Kimura mutation operator with a rank-one master-
sequence fitness spike.  It retains every Hamming multiplicity, locates all
remaining roots by strict secular interlacing, identifies the projective gap,
and closes zero-selection, zero-mutation and one-locus boundaries.

## Reproduce

```bash
python -B code/c336_crow_kimura_producer.py
python -B code/c336_crow_kimura_checker.py
python -B code/c336_crow_kimura_sympy_crosscheck.py
python -B code/c336_crow_kimura_replay.py
python -B code/c336_crow_kimura_mutation.py
python -B code/c336_release_manifest.py
```

The checker is producer-independent.  Replay is isolated and byte exact; the
mutation lane repairs hashes after semantic attacks.  The release command
also performs fresh fixed-epoch builds of all three manuscript rounds, text,
font and raster checks, optimized-Python refusal and the exact 27-payload
ledger.

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route tuple:

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.

Overall verdict: `ROUTE_A_REJECTED`; Route B is not authorized.
