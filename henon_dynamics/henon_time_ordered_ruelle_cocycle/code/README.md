# Code and reproducibility

The T1--T4/orbitwise-scalar-T5 implementation is deterministic.  All pass/fail decisions in the
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
- `c22_t4_producer.py` certifies the all-period instability bounds and
  convergence domain, exact primitive/repetition bookkeeping, common
  two-letter base and projective complex domains, and orbitwise scalar trace
  obstruction.
- `c22_t4_independent_check.py` reconstructs those results without importing
  the producer.
- `test_c22_t4.py` contains domain, chronology, multiplicity, trace, and scope
  mutation tests.

## Clean run

From the project root, prepare the locked environment once:

```bash
python -m pip install -r requirements.txt
```

Then run the complete T1--T3 producer/checker/test chain:

```bash
./code/run_c22.sh
```

The wrapper executes the following explicit commands:

```bash
python code/c22_producer.py
python code/c22_independent_check.py
pytest -q code/test_c22.py
```

Run the T4/orbitwise-scalar-T5 chain separately with

```bash
./code/run_c22_t4.sh
```

which executes

```bash
python code/c22_t4_producer.py
python code/c22_t4_independent_check.py
pytest -q code/test_c22_t4.py
```

The complete released verification is therefore

```bash
./code/run_c22.sh
./code/run_c22_t4.sh
sha256sum -c results/ARTIFACT_HASHES.sha256
```

The producer uses the physical convention

\[
H_a(q,p)=(1-aq^2-p,q)
\]

and multiplies later Jacobians on the left.  No code calls a
frequency-averaged Hénon map or separately canonicalizes parameter and state
necklaces.  Reversal remains equality metadata and is not quotiented out of
the Euler orbit set.

The released JSON artifacts are hash-bound by their independent checkers.  A
finite operator section is deliberately absent.  Orbitwise scalar
denominator cancellation is exactly obstructed; aggregate scalar
representations remain unexcluded, and the authorized graded exterior
nuclear complex remains open.
