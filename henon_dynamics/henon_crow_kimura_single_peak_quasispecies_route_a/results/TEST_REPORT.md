# HCS-C336 test report

All commands below pass under ordinary Python and explicitly refuse optimized
Python:

```bash
python -B code/c336_crow_kimura_producer.py
python -B code/c336_crow_kimura_checker.py
python -B code/c336_crow_kimura_sympy_crosscheck.py
python -B code/c336_crow_kimura_replay.py
python -B code/c336_crow_kimura_mutation.py
```

Observed sentinels:

```text
C336_PRODUCER_PASS rows=30 payload=794da3d0207a60ff7b7cad893be71c8dce16b6a990914219a75b56cd3697e311
C336 independent Crow-Kimura checker: PASS assertions=644
C336 SymPy cross-check: PASS identities=681
C336 byte replay: PASS sha256=b4102f835b4fc68165c6fa94f657166d56977b10c86ea9959361d2aa67025f8a bytes=112694
C336 hostile mutation suite: PASS 70/70
```

The checker imports no producer code.  The SymPy lane directly constructs
small full hypercube matrices and independently checks their characteristic
polynomials, while Sturm counts certify the secular intervals.  Replay runs
the producer twice into isolated paths and compares both bytes with the
checked-in evidence.
