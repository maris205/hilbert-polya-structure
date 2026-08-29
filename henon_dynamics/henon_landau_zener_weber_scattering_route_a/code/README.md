# Code map

* `c224_landau_zener_producer.py` writes the canonical JSON receipt.  It uses
  exact `Fraction` parameters, 80-digit mpmath for the Gamma phase and a fixed
  2048-step RK4 finite-window control.
* `c224_landau_zener_checker.py` reconstructs schema, Weber/scattering
  formulae, derivatives, matrix entries, and every finite-window row without
  importing producer functions.
* `c224_landau_zener_sympy_crosscheck.py` independently checks the scalar
  Weber signs, Pauli algebra, SU(2) invariants, monotonicity and sign gauge.
* `c224_landau_zener_replay.py` runs a clean producer subprocess and compares
  canonical bytes.
* `c224_landau_zener_mutation.py` attacks repaired semantic hashes, nested and
  unknown keys, and a stale hash.
* `c224_release_manifest.py` closes the 27-file payload, PDF and source locks.

No script reads external arithmetic data or imports a target table.  The
finite RK4 output is a control, not an exact finite-time claim.
