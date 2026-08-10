# HCS-C26 exact results

The result bundle separates exact production, independent replay, and
human-readable scope:

- `c26_certificate.json` — source graph, frozen state-4 branch, exact
  `B`, `R`, `x0`, `S(x0)`, `S(x0)^(-4)`, registered coefficient floors,
  exact positive-prefix complex-cone constants, scalar Perron/characteristic
  trace examples, the conditional point-evaluation hypothesis chain, and a
  finite non-proof decoder sentinel;
- `c26_independent_check.json` — independent reconstruction with fourteen
  checks, including a finite-difference projective derivative;
- `RESULTS.md` — mathematical result and limitations;
- `VALIDATION_REPORT.md` — independent-check interpretation;
- `TEST_REPORT.md` — regression and mutation coverage;
- `MATERIAL_PASSPORTS.md` — lineage and evidence labels;
- `ARTIFACT_HASHES.sha256` — integrity manifest.

Regenerate and verify everything with:

```bash
./code/run_c26.sh
```

The exact arithmetic verifies an application witness and the algebraic
inputs to the theorem.  It does not by itself prove boundedness or nuclearity
of a function space, reprove C24/C25, or construct a determinant.  The
accompanying theorem package separately proves the concrete scalar/vector
Bergman statements and the ordinary scalar Fredholm determinant.
