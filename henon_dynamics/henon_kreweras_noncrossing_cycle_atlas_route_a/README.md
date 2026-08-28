# HCS-C209 - ordinary Kreweras noncrossing cycle atlas

This package freezes one finite dynamical system and closes its complete cycle
ledger.  The state space is `NC(n)`, the noncrossing partitions of a labelled
n-gon; one tick is the ordinary Kreweras complement
`K(pi)=cycles(p_pi^(-1) c)`.  We record the exact order boundary, every fixed
count, least-period populations, cycles, finite zeta, Koopman
determinant/spectrum, rank duality, and polygon-reflection reversors.

The all-n fixed formula is source-derived from the type-A Kreweras CSP.  It is
not claimed as a new CSP theorem.  Direct enumeration (`n<=8`) and exact
q-polynomial arithmetic (`n<=12`) are independent regression evidence; the
closed formula table extends to `n<=24`.

## Reproduce

From this directory:

```bash
python code/c209_kreweras_producer.py
python code/c209_kreweras_checker.py
python code/c209_sympy_crosscheck.py
python code/c209_replay.py
python code/c209_mutation.py
python code/c209_release_manifest.py
```

The expected payload hash is printed by each relevant command and is also
stored in `C209_RELEASE_MANIFEST.json` after release closure.

## Route-A boundary

```text
scope: NO_BAD_EULER_OR_ROOT_NUMBER
tuple: (A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

The finite permutation unitary is a source-native diagnostic only.  No target
prime/zero table, local arithmetic, Euler factor, root number, target divisor,
functional equation, or Hilbert-Polya claim is present.

## Files

* `THEOREM_PACKAGE.md` - frozen definitions, theorem, proof/evidence boundary,
  and attribution.
* `code/` - independent producer, checker, symbolic audit, replay, mutation
  harness, and release-manifest builder.
* `results/` - machine-readable evidence and audit reports.
* `paper/` - the three-round deterministic manuscript build.
* `evaluations/route_a/HCS-C209/` - evaluator tuple and evidence links.
