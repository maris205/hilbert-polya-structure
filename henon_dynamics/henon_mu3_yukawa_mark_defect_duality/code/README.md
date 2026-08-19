# C68 verification entry points

```text
python code/c68_defect_duality.py
python code/c68_defect_duality_checker.py
python code/c68_snf_crosscheck.py
python code/c68_defect_duality_replay_checker.py
python code/c68_mutation_test.py
```

The producer uses an explicit Euclidean Smith reduction and a direct
congruence-lattice basis.  The checker uses a separate exact reduction path;
the cross-check uses SymPy's integer Smith form.
