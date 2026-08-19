# C69 exact certificate code

- `c69_defect_splitting.py` binds the upstream bytes and produces the exact
  retraction, complement lattice, and presentation certificate.
- `c69_defect_splitting_checker.py` independently rebuilds every matrix and
  verifies all congruences, determinants, products, orders, and Smith factors.
- `c69_snf_crosscheck.py` repeats the matrix and Smith calculations in SymPy.
- `c69_defect_splitting_replay_checker.py` runs the checker in a clean process.
- `c69_mutation_test.py` requires the checker to reject hostile semantic
  mutations.

Run all five commands from the project directory with Python 3.
