# C360 executable lanes

Run from the package root:

```bash
python -B code/c360_berger_ricci_producer.py
python -B code/c360_berger_ricci_checker.py
python -B code/c360_berger_ricci_sympy_crosscheck.py
python -B code/c360_berger_ricci_replay.py
python -B code/c360_berger_ricci_mutation.py
python -B code/c360_release_manifest.py
```

The producer binds the strict evaluation YAML and writes canonical JSON.  The
checker independently reconstructs every row and imports no producer module.
The symbolic lane derives 26 identities, including both nonzero Type-I
blow-up coefficients.  Replay compares two isolated producer/checker runs byte
for byte.  Mutation repairs outer hashes after semantic corruption and also
attacks the explicit horizontal Ricci wall and JSON/YAML parsing.  Every executable
explicitly refuses optimized Python so no assertion can be stripped.
