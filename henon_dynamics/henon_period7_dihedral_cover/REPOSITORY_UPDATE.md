# HCS-C20 repository update

**Release state:** verified; pending source commit and provenance binding

## Added project

`henon_dynamics/henon_period7_dihedral_cover/` contains:

- the exact derivation and selected-prime good-reduction proof;
- a ten-page compiled manuscript;
- an exact producer, a separately implemented finite-field checker, and
  mutation-based regression tests;
- machine-readable geometric and arithmetic certificates;
- Route-A, review, integrity, and source-audit records; and
- the next breadth-first cross-period research question.

## Repository-level updates

The H\'enon research index, candidate registry, obstruction registry, related
programs map, and HCS-C19 successor roadmap now point to HCS-C20.  The new
obstruction entry records that ordinary cohomology of the oriented cover
adds phase labels but no new Frobenius eigenvalues.

## Verification

Before release, the following commands are required to pass from the project
directory:

```bash
python code/c20_producer.py --output results/c20_certificate.json
python code/c20_independent_check.py \
  --certificate results/c20_certificate.json \
  --output results/c20_independent_check.json
python -m unittest discover -s code -p 'test_c20.py' -v
```

The final source commit will be written into this record and the Route-A YAML
in a follow-up provenance commit, then both commits and the annotated release
tag will be pushed by SSH.

Final pre-commit verification on 2026-08-08:

- producer regenerated `c20_certificate.json` successfully;
- certificate SHA-256:
  `7ee43e3253aff15ec00d78b9633c3d3362e71cd5a880cd3e928e7f322abb2681`;
- independent polynomial-quotient checker: `PASS (136 checks)`;
- regression suite: `9 tests`, all passed in `83.638s`; and
- manuscript: 10 pages, clean final LaTeX log, all fonts embedded.
