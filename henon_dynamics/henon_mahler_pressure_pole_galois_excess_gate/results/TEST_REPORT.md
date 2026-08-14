# Test report

Date: 2026-08-14

Command:

```bash
bash code/run_c54.sh
```

Final results:

- producer: PASS;
- certificate core digest:
  `3bdcd45ef20c117f70706641d56d28e0ee4dd7bad2144a658789a4a681f0ef4d`;
- dependency locks recomputed: 8/8;
- independent checker: PASS;
- exact orbit rows reconstructed independently: 3/3;
- finite logarithmic-derivative identities: 3/3;
- adversarial mutations rejected: 12/12;
- unit tests: 10/10 PASS in 0.839 seconds;
- conditional theorem promotion: rejected;
- generated project `__pycache__`: none retained.

The checker is independent of the producer module.  It reconstructs the
three trace-root heights, pressure residue interval, core digest, source
hashes and claim firewall from separately written formulas.  Mutations test
the excess sign, physical pole, residue, conditional status, exact witnesses,
cohomological obstruction, dependency lock and Route-B promotion.

Two fail-closed implementation defects were found and corrected before this
report: one mistyped inherited hash and one loss of multiprecision caused by
constructing constants before setting `mpmath` precision.  Neither survived
the independent checker.
