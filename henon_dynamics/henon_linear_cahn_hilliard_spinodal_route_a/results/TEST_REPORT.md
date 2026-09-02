# C304 test report

The final release gate runs, in order:

1. deterministic producer;
2. producer-independent strict checker;
3. independent SymPy cross-check;
4. two-run isolated byte replay;
5. repaired-hash hostile mutation suite;
6. semantic and byte checks on the Route-A YAML;
7. fresh fixed-epoch double builds of the three round variants, plus the
   byte-identity check that makes final the Round-2 alias;
8. log-warning, embedded/subset-font, page-count, PDF-text-sentinel, and
   rasterization checks;
9. exact 27-payload manifest closure and self-exclusion.

Expected command sentinels are `C304_PRODUCER_PASS`, checker `PASS`, SymPy
`PASS`, replay `PASS`, mutation `PASS 72/72`, and
`C304_RELEASE_MANIFEST_PASS`. The checker explicitly rejects optimized
Python; other scripts are released for the documented ordinary `python -B`
commands only.
