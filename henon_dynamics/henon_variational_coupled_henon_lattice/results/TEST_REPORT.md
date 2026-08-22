# Test report (C106)

Commands run from the package directory's repository root:

```text
python code/c106_variational_lattice.py
  PREFREEZE_G3_PASS, evidence_sha256=3c3c512f021a8bb4ba094ed8dc14a9635346f566ef404fd6f799dbf7340d1f9b
python code/c106_variational_lattice_checker.py
  C106_INDEPENDENT_CHECK_PASS
python code/c106_sympy_crosscheck.py
  C106_SYMPY_CROSSCHECK_PASS, identities=9
python code/c106_replay_checker.py
  C106_REPLAY_PASS
python code/c106_mutation_test.py
  C106_MUTATION_TEST_PASS, rejected=11/11
```

All exact identities use \(\mathbb Q\); no tolerance-based acceptance is used. The checker verifies the canonical evidence bytes, model parameters, orbit states, cycle closure, Jacobian symplecticity, exact primitive, determinants, reversor samples, monodromy polynomial and Route-A/nonclaim boundary.
