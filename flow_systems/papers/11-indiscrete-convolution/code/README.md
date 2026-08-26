# Paper 11 deterministic controls

`indiscrete_convolution_controls.py` is a Python-standard-library generator
and strict verifier for finite analogues of the locked Paper-11 objects. The
models use a nonempty finite indiscrete unit set and a finite cyclic time
group with the discrete topology. They are deterministic witnesses and
falsification controls, not proofs of `P11-1`--`P11-10`.

The generator covers:

- the product topology and exhaustive Hausdorff-open classification;
- continuous factorization through time for finite `T0` targets, plus a
  non-`T0` negative;
- measurable factorization for finite countably separated targets, plus a
  non-separated negative;
- ambient support closure and time projection;
- exact Gaussian-integer convolution and involution against the cyclic group
  algebra;
- intentional wrong-time-sign and wrong-source/range failures;
- source-fibre regular matrices at every unit;
- the zero Hausdorff-open diagnostic;
- strict extra functions in the fully discrete proxy;
- trivial, transitive, and nontransitive action-blindness controls; and
- independently crossed prime, composite, arbitrary labels and periods.

The raw unit-dependent probe used to detect the source/range error is
explicitly outside the licensed global function algebra. It detects a
convention error and supplies no actual-owner algebra claim. Likewise, the
fully discrete proxy is a separately typed modeling control.

Generate or verify:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B indiscrete_convolution_controls.py \
  --output-dir ../results
PYTHONDONTWRITEBYTECODE=1 python3 -B indiscrete_convolution_controls.py \
  --output-dir ../results --verify-only
```

`--verify-only` is read-only and fail-closed. It rejects any active-lock or
Phase-2-gate drift, implementation-file drift, artifact byte/size/row drift,
manifest-metric drift, missing artifact, unexpected artifact, or generated
name occupied by a non-file.

The implementation has no network path, randomness, external dependency,
external dataset, target-zero input, fitted parameter, or timestamp. Run the
complete test and two-generation protocol through
`../experiments/reproduce.sh`.
