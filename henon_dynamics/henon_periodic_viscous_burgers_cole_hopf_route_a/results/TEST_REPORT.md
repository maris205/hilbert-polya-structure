# Validation report

All commands below are run from the C195 package root.

## Exact certificate

```text
$ python3 code/c195_burgers_producer.py
C195_PRODUCER_PASS: cases=24, generator residual rows=24, spectrum cells=408

$ python3 code/c195_burgers_checker.py
C195_CHECKER_PASS: assertions=1490

$ python3 code/c195_burgers_sympy_crosscheck.py
C195_SYMPY_PASS: checks=129, selected_cases=9

$ python3 code/c195_burgers_replay.py
C195_REPLAY_PASS: bytes=199419

$ python3 code/c195_burgers_mutation.py
C195_MUTATION_PASS: repaired=22/22, stale=1/1
```

The checker is implementation-independent of the producer: it imports no producer
code, regenerates the case family, and uses separately written complex/Laurent
operations. This is producer independence, not external peer review.

## Paper and release

The final closure records three content-distinct PDFs, final/round-2 byte identity,
a fixed-epoch two-fresh-directory byte-reproducibility check, embedded fonts, a clean
warning/bad-box/missing-glyph scan, text extraction, all-page visual inspection, and
a self-excluded 27-payload manifest. Exact hashes and page counts are recorded in
`paper/COMPILE_REPORT.md` and `C195_RELEASE_MANIFEST.json`.

## Evidence boundary

The 24 finite rows test the executable algebra only. The all-parameter theorem is
proved analytically in `THEOREM_PACKAGE.md`.
