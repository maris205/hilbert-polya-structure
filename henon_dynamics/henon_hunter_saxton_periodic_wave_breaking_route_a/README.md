# HCS-C324: periodic Hunter--Saxton wave breaking

This package proves the complete pre-breaking characteristic theorem for every nonconstant periodic `C2` datum in the once-integrated Hunter--Saxton equation.  It identifies both endpoints of the maximal classical interval, the full first-breaking label set, the exact characteristic Jacobian, energy conservation, and the universal slope rate `-2/(T_plus-t)`.  It does not select a weak continuation.

Finite receipts cover 12 single harmonics and six deliberately asymmetric two-harmonic profiles.  The asymmetric profiles separate the minimum-controlled future endpoint from the maximum-controlled past endpoint.  The independent checker performs 3,857 checks, SymPy closes 1,508 exact identities, two isolated replays are byte-identical, and 60 hostile mutations are rejected.

The Route-A tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, the overall verdict is `ROUTE_A_REJECTED`, and Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c324_hunter_saxton_producer.py
python -B code/c324_hunter_saxton_checker.py
python -B code/c324_hunter_saxton_sympy_crosscheck.py
python -B code/c324_hunter_saxton_replay.py
python -B code/c324_hunter_saxton_mutation.py
python -B code/c324_release_manifest.py
```

The readable artifact is `paper/main.pdf`; `C324_RELEASE_MANIFEST.json` is the content-addressed ledger.
