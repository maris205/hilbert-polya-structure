# HCS-C56 exact code/results lane

This directory implements the prefreeze machine certificate for the
degree-27 line field of the released HCS-C55 cubic surface.  It does not
promote the C56 project, paper, or Route record.

The producer source-locks C55 implementation commit
`e5661e80da6f7de53f574f97f768744095ba8ae0` and provenance commit
`0b0a48db257a4b8bd4af905ab9c9cafba4a4d8be` through committed Git objects,
replays the committed C55 checker, and only then imports the ordered cubic
coefficients.  Singular performs the exact producer computations.  The
checker does not import producer code: it uses SymPy with
`SYMPY_GROUND_TYPES=python`, custom integer convolution and `Fraction`
long division, and a separate Picard-lattice enumeration.

The fixed machine result group is:

- `results/c56_certificate.json`
- `results/c56_schema.json`
- `results/c56_check_report.json`
- `results/scoped_hash_manifest.json`

`run_all.sh --refresh-prefreeze` builds and verifies all four files in a
private same-filesystem staging directory, runs the hostile test suite, and
uses rollback-atomic grouped promotion.  Plain `run_all.sh` is non-mutating:
it regenerates temporary artifacts, compares them byte-for-byte with the live
group, verifies the scoped manifest, and rejects any extra scoped artifact.

Requirements in the validated environment are Python 3.12, SymPy 1.14 with
the pure-Python ground-type gate, and Singular 4.2.1.  Optimized Python and
the `PYTHONOPTIMIZE` environment variable are rejected.  No `/tmp`
reconnaissance digest is theorem evidence.
