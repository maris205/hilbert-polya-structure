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

Final deterministic artifact digests before the frozen manifest are:

- paper PDF: `93593889bd04bbdaa62741f90d03f6005bba5d1f9ebdf9dd77058167244580a1`;
- producer certificate: `98b9ed10433f5cc7eb56aa04f397caa1ebfbc03acc904552618bd06f30370a1e`;
- independent replay: `cbda105cfdac815d66e5cccc7e6558bbd12f0bc10cdb1e5ebd12b1ff0670e3e8`.

The final frozen manifest contains **39 artifacts** and verifies unchanged
under the default read-only release runner.
