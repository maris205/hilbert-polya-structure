# Test report — HCS-C248

Commands run from the package directory:

```text
python3 -B code/c248_rs_producer.py
python3 -B code/c248_rs_checker.py
python3 -B code/c248_rs_sympy_crosscheck.py
python3 -B code/c248_rs_replay.py
python3 -B code/c248_rs_mutation.py
```

The independent checker reconstructs the certificate in 377 assertions; the
SymPy cross-check passes 90 exact symbolic identities; clean replay is byte
identical; and the hostile suite rejects 42/42 mutations, including repaired
payload hashes, altered coefficients, route/scope edits, citation edits,
unknown keys, and row reordering.  No floating-point operation is used by the
producer or checker.

The final release script additionally checks the three distinct revision PDFs,
the final-equals-round2 invariant, fixed-epoch double builds, embedded and
subsetted fonts, settled logs, text phrases, and manifest closure.
