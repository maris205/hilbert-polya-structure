# C243 code contract

`c243_dimer_producer.py` freezes the nonlinear two-mode Hamiltonian and emits
fixed-point, Bloch-pole, energy-level, elliptic-period, separatrix, and
self-trapping criterion rows.  `c243_dimer_checker.py` independently rebuilds
the 14 fixed points, 8 pole rows, 13 level rows and 5 criterion rows.

`c243_dimer_sympy_crosscheck.py` checks Hamilton/Bloch identities, the quartic
reduction, roots, pitchfork, sech homoclinic and three independent elliptic
quadratures.  Replay checks bytes and the repaired-hash mutation suite rejects
28/28 hostile edits.  No target arithmetic data are read.
