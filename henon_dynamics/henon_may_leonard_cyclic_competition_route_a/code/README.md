# Executable evidence: HCS-C358

Run from the package root with Python bytecode disabled:

```bash
python -B code/c358_may_leonard_producer.py
python -B code/c358_may_leonard_checker.py
python -B code/c358_may_leonard_sympy_crosscheck.py
python -B code/c358_may_leonard_replay.py
python -B code/c358_may_leonard_mutation.py
python -B code/c358_release_manifest.py
```

The producer writes exact rational receipts.  The checker imports no producer
module and reconstructs all rows independently.  The SymPy lane derives the
polynomial identities separately.  Replay compares two isolated outputs, and
the hostile suite applies repaired-hash and strict-parser attacks.  Every
entry point explicitly refuses `python -O` and `python -OO`.

The release program additionally rebuilds each revision PDF twice at epoch
`1788393600`, audits logs, fonts, extracted text and rasterization, verifies
the 27-payload ledger, and checks the self-excluded manifest.
