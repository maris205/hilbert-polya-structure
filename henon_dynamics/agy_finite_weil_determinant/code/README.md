# HCS-C27 code

Run the exact release with:

```bash
bash code/run_c27.sh
```

The producer reads the source-locked C24, C25, and C26 certificates and
writes `results/c27_certificate.json`.  It implements Thomas's finite Weil
character formula directly over finite fields, reconstructs local Weil
polynomials from power traces, preserves later-on-the-left chronology, and
runs the finite arithmetic census.

`c27_independent_check.py` is deliberately separate and does not import the
producer.  `test_c27.py` includes mutation tests for chronology reversal,
transpose/averaging substitutions, branchwise character multiplication,
incorrect repetition weights, even-prime leakage, finite-cutoff promotion,
and loss of the integral symplectic conjugacy obstruction.

All character values use the exact basis `(1,G_p)` with
`G_p^2=Legendre(-1,p)*p`; floating-point values are not used for decisions.

The release runner regenerates both JSON certificates and checks all 40
versioned project artifacts against the already frozen SHA-256 manifest. It
does not rewrite that manifest. After an intentional release change, a
maintainer reviews the diff and explicitly refreshes it with:

```bash
python code/c27_hash_manifest.py --write
```

The independent JSON serializes repository-relative source paths, so its
content does not depend on the location of the clone.
