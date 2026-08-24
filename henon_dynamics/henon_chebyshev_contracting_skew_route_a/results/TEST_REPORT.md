# Test report — HCS-C126

Run from the package root:

```text
python3 code/c126_chebyshev_skew_producer.py
python3 code/c126_chebyshev_skew_checker.py
python3 code/c126_sympy_crosscheck.py
python3 code/c126_replay.py
python3 code/c126_mutation.py
```

Final results:

- producer: `C126_PRODUCER_PASS`;
- independent checker: `C126_INDEPENDENT_CHECK_PASS`, 12 primitive and 12
  stability rows reconstructed;
- independent SymPy cross-check: `73` exact predicates;
- replay: canonical evidence is byte-identical;
- hostile audit: `18/18` mutations rejected.

The all-period proof is analytic and does not depend on the finite receipt
prefix.  The checker imports no producer code; the SymPy reconstruction uses a
third path for composition, derivative, and control identities.
