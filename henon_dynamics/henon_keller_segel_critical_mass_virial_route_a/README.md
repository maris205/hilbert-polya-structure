# HCS-C363: Keller--Segel critical-mass virial atlas

This package derives the two-dimensional parabolic--elliptic Keller--Segel
mass threshold from two independent identities: free-energy scaling and the
exact second-moment virial law.  It adds a finite supercritical classical
persistence bound, the full translated critical stationary family, its
infinite-moment caveat, and the radial cumulative equation.

The source commit is
`05ca5f96b2c69a6ad6ba153d1084df750d7722c0`; the fixed epoch is
`1788480000`; the scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

Run from this directory:

```bash
python -B code/c363_release_manifest.py
python -B code/c363_release_manifest.py --write
```

The release admits exactly 27 payloads and keeps its manifest self-excluded.
Main outputs are `THEOREM_PACKAGE.md`,
`results/c363_keller_segel_evidence.json`, `paper/main.pdf`, and
`C363_RELEASE_MANIFEST.json`.
