# C73 code

```bash
python3 code/c73_generation_blocker_reliability.py
python3 code/c73_generation_blocker_reliability_checker.py
python3 code/c73_polynomial_crosscheck.py
python3 code/c73_generation_blocker_reliability_replay_checker.py
python3 code/c73_mutation_test.py
```

The producer derives the direction partition and computes every deletion and
importance value.  The checker independently tests projective determinants,
enumerates all retained-support ranks and minimal blockers, and recomputes
the monotone-game importance indices.  SymPy enumerates all block-failure
states and verifies the reliability and transversal polynomials; GAP checks
the order of the structural direct-product subgroup used in the symmetry
calculation.
