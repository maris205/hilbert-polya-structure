# Exact static audit

This package audits source-lock v3 for
`algebraic_exact_action_clock_obstruction_v1`.  It has no candidate
periodic-orbit solver and never substitutes the inherited parameter.  Its
execution order is fail closed:

1. validate and hash the v3 source lock;
2. scan the executable for network, process, floating-fit, and dynamic-import
   machinery;
3. verify that the written proof retains every repaired dependency;
4. run normalization, endpoint, pole, logarithm-edge, multivalued-gauge, and
   post-processing controls;
5. only after the controls pass, verify the Hénon one-form, type-1,
   recurrence-multiplicity, projective-infinity, and denominator ledgers.

After independent code review, run from this paper directory:

```bash
pytest -q --junitxml=results/pytest.xml
python code/scripts/run_static_audit.py --project-root .
python code/scripts/build_result_manifest.py --project-root .
```

All logarithmic counterexamples are symbolic provenance labels.  The code
does not numerically evaluate a logarithm, read a prime list, access
Riemann-zero data, make a network request, or compare approximate targets.
The static output can check an implementation; the all-period conclusion
comes only from the proof and Hermite--Lindemann.
