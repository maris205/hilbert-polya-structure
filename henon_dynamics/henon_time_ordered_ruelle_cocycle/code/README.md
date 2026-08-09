# Code and reproducibility

The T1--T3 implementation is deterministic.  All pass/fail decisions in the
producer use exact `Fraction` arithmetic; irrational square roots are bounded
by integer-square-root enclosures at a frozen decimal scale.

## Files

- `c22_producer.py` builds the common-geometry certificate, joint primitive
  ledger, all-branch protocol-sector enclosures, finite-field witness, and T3
  symbolic controls.
- `c22_independent_check.py` imports neither the producer nor an earlier Hénon
  project.  It reconstructs every gate from the serialized artifact.
- `test_c22.py` contains regression and mutation tests, including the failure
  of separate parameter/state canonicalization.

## Clean run

From the project root, prepare the locked environment once:

```bash
python -m pip install -r requirements.txt
```

Then run the complete producer/checker/test chain:

```bash
./code/run_c22.sh
```

The wrapper executes the following explicit commands:

```bash
python code/c22_producer.py
python code/c22_independent_check.py
pytest -q code/test_c22.py
```

The producer uses the physical convention

\[
H_a(q,p)=(1-aq^2-p,q)
\]

and multiplies later Jacobians on the left.  No code calls a
frequency-averaged Hénon map or separately canonicalizes parameter and state
necklaces.  Reversal remains equality metadata and is not quotiented out of
the Euler orbit set.

The released JSON artifacts are hash-bound by the independent checker.  A
finite operator section is deliberately absent at T1--T3; the complex/nuclear
operator is the next hard gate.
