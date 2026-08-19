# C66 verification entry points

Run from this project directory:

```text
python code/c66_mark_snf.py
python code/c66_mark_snf_checker.py
python code/c66_snf_crosscheck.py
python code/c66_mark_snf_replay_checker.py
python code/c66_mutation_test.py
```

The producer and checker bind C64 `c64_mark_evidence.json`, the C64
prefreeze manifest, and C65 `c65_defect_evidence.json` by SHA-256.  The
producer and checker use separate Smith-form implementations; the cross-check
uses SymPy's integer Smith form as a third implementation.
