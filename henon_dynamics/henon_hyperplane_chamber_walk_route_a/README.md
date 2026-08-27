# HCS-C192 — hyperplane chamber walks

This package freezes the Brown--Diaconis face-semigroup chamber walk for every
finite real hyperplane arrangement and every probability measure on its faces.
The source-owned theorem gives the complete flat-indexed spectrum, Möbius
multiplicities, exact stationary sampler, uniqueness criterion, and mixing
bounds.  Elementary linear algebra then records the characteristic polynomial,
`det(I-zK)`, and all power traces.

The package makes one deliberately sharp distinction.  Brown--Diaconis give a
weighted without-replacement exact stationary sampler and a with-replacement
chamber-hitting stopping construction.  The latter supports the coupling bound,
but this package does **not** assert the additional independence required by the
strict definition of a strong stationary time.

Finite coordinate and braid arrangements are regression oracles only.  They do
not prove, enlarge, or claim priority for the all-arrangement theorem.

## Frozen release facts

- candidate: `HCS-C192`
- date: `2026-08-27`
- source commit: `4d7b214759f7ff982c0b19e662918acd307e0f58`
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route A: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`
- overall: `ROUTE_A_REJECTED`; Route B is false
- primary source: Brown--Diaconis, *Annals of Probability* 26 (1998),
  DOI `10.1214/aop/1022855884`

## Reproduction

```bash
python3 code/c192_hyperplane_producer.py
python3 code/c192_hyperplane_checker.py
python3 code/c192_sympy_crosscheck.py
python3 code/c192_replay.py
python3 code/c192_mutation.py
python3 code/c192_release_manifest.py
```

The final paper is `paper/main.pdf`.  The three content-distinct paper rounds
are retained alongside the LaTeX source.  `C192_RELEASE_MANIFEST.json` hashes the
other 27 payload files and excludes itself.
