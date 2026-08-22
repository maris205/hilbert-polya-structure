# C106 code map

* `c106_variational_lattice.py`: exact producer; writes the canonical evidence JSON.
* `c106_variational_lattice_checker.py`: independent semantic checker; reconstructs gradients, Jacobians, monodromy and controls.
* `c106_sympy_crosscheck.py`: symbolic symplectic/reversor/period-two cross-check.
* `c106_replay_checker.py`: canonical-byte replay and scope check.
* `c106_mutation_test.py`: ten hostile semantic mutations; all must be rejected.

All calculations use `fractions.Fraction` or exact SymPy rationals. No random seed or external numerical file is used.
