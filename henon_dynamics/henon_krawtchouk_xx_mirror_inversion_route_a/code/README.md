# HCS-C366 executable evidence

Run the producer, independent checker, symbolic lane, isolated replay,
hostile mutation suite, and release gate with CPython in ordinary mode.  Every
script refuses `-O` and `-OO`; the checker deliberately imports no producer
module.  Exact finite ledgers audit the convention and formulas, while the
continuum and all-size statements are proved in `THEOREM_PACKAGE.md`.

```bash
python -B code/c366_krawtchouk_xx_producer.py
python -B code/c366_krawtchouk_xx_checker.py
python -B code/c366_krawtchouk_xx_sympy_crosscheck.py
python -B code/c366_krawtchouk_xx_replay.py
python -B code/c366_krawtchouk_xx_mutation.py
python -B code/c366_release_manifest.py
```

The checker accepts explicit `--input` and `--evaluation` paths so hostile
tests can place both artifacts in an isolated directory. It recursively locks
leaf types as well as values and exact key/coordinate sets; Boolean, integer,
and floating-point leaves are never interchangeable.
