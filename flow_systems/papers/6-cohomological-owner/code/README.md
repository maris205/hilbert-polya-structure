# Deterministic control code

The code uses only the Python standard library and exact integer or rational
arithmetic.

## Files

- `cohomological_owner_controls.py` computes Möbius/closed-point counts,
  reconstructs fixed-point and cohomological trace ledgers, emits finite
  Koopman multiplicity witnesses, records the lifted Frobenius divisor, and
  writes the typed ownership certificate plus SHA-256 manifest.
- `test_cohomological_owner_controls.py` contains ten unit tests covering
  arithmetic identities, artifact consistency, cutoff guards, frequency
  occurrence, positive-weight invariance, and zero-mode multiplicity growth.

The finite tables are regression controls.  They do not prove the infinite
spectral-type statements, which are established in `../notes/proof_audit.md`.

Run through the canonical entry point:

```bash
bash ../experiments/reproduce.sh
```

The implementation reads no Riemann-zero table, target-prime table, fitted
boundary condition, random seed, network response, or floating-point root.
