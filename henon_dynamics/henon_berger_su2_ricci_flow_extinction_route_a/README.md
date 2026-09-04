# HCS-C360: Berger SU(2) Ricci-flow extinction atlas

This package classifies the complete positive Berger-metric phase portrait for
unnormalized Ricci flow, including exact endpoint times, ancient versus
finite-backward branches, Type-I round extinction with nonzero scaled-curvature
limits, all three curvature-sign walls, and volume-normalized convergence.  It is an independent theorem-scale Route-A
test, not a fragment of another paper.

The canonical source commit is
`05ca5f96b2c69a6ad6ba153d1084df750d7722c0`; the frozen clock is geometric
Ricci-flow time.  The scope is exactly `NO_BAD_EULER_OR_ROOT_NUMBER`.

Run the complete release gate from this directory:

```bash
python -B code/c360_release_manifest.py
python -B code/c360_release_manifest.py --write
```

The first command is read-only.  The second rewrites only the self-excluded
manifest after all producer, independent-checker, symbolic, replay, hostile,
optimized-refusal, PDF, and payload-membership lanes pass.

Main outputs are `THEOREM_PACKAGE.md`,
`results/c360_berger_ricci_evidence.json`, `paper/main.pdf`, and
`C360_RELEASE_MANIFEST.json`.
