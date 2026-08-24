# C119 exact-code ledger

Run, from the package root:

```bash
python3 code/c119_fock_producer.py
python3 code/c119_fock_checker.py
python3 code/c119_sympy_crosscheck.py
python3 code/c119_replay.py
python3 code/c119_mutation.py
python3 code/c119_release_manifest.py
```

The checker independently reconstructs the matrix, singular values, eight
traces, Newton coefficients, and zero multiplicities. It does not import the
producer. The replay also regenerates the evidence in a temporary directory
and demands byte identity. No command accesses a network service.
