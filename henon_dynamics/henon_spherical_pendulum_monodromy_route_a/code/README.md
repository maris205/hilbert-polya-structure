# C244 code contract

'c244_pendulum_producer.py' emits a deterministic JSON receipt with seven
critical rows and eight regular root/quadrature rows.  The producer uses only
the frozen Hamiltonian and rational sentinels.

'c244_pendulum_checker.py' independently reconstructs the schema, cubic,
discriminant, critical curve, roots, endpoint-cancelled period/angle/action
integrals, and the matrix-column monodromy convention.
'c244_pendulum_sympy_crosscheck.py' repeats the algebra and checks the
original action integral.  'c244_pendulum_replay.py' checks byte identity;
'c244_pendulum_mutation.py' runs 34 repaired-hash semantic attacks.
'c244_release_manifest.py' closes the 27 payload files and fixed-epoch PDF
contract.

All scripts are safe to run with python -B and
PYTHONDONTWRITEBYTECODE=1.
