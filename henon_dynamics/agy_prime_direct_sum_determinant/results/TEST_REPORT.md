# HCS-C28 test report

The release suite covers regression, mutation, independence, and portability
properties.  It verifies the source locks, gamma-star arithmetic, normalized
character limit contract, sharp Schatten boundary, P073 all-prime
obstruction, complete C24 census, Möbius identity, chronology/repetition
firewalls, determinant terminology, payload integrity, and Route-B denial.

Mutation tests must reject changes to decisive theorem fields even when the
JSON remains syntactically valid.  In particular they cover the trace-class
threshold, P073 character, normalized determinant limit, Fredholm product,
repetition rule, source lock, scope, and certificate payload hash.

The independent checker is also run from a temporary working directory and
must produce the same semantic report.  Its integer determinant backend is
fuzzed against SymPy on random small matrices during audit.  Python bytecode
generation is disabled by the release runner so a replay leaves no hidden
`__pycache__` state.

Run the complete read-only release replay with:

```bash
bash code/run_c28.sh
```

During an intentional release preparation, refresh the artifact manifest
explicitly, then run the normal verifier:

```bash
bash code/run_c28.sh --refresh-manifest
bash code/run_c28.sh
```

## Audit counts

- independent decisive gates: **32/32 pass**;
- regression and mutation tests: **21/21 pass**;
- Bareiss random exact-arithmetic comparisons: **12,000/12,000 pass**;
- producer/checker output from repository and temporary working directories:
  semantically identical;
- two consecutive isolated default runners: pass with an unchanged manifest
  digest;
- payload SHA and all four upstream source hashes: pass.

The final manifest entry count and release artifact digests are recorded by
the frozen release replay after the manuscript and Route-A record are added.
