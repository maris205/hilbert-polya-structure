# Nullity-feedback Jordan-power focused scout

Final scout status: `KILL_INTERNAL_P137_PLUS_ROOT_OWNER`  
Paper number allocated: no  
External lifecycle: `HOLD_EXTERNAL`

## Files

- `SCOUT.md`: decision, theorem signal, exact signatures, and threshold test.
- `DERIVATION_PACKAGE.md`: independent formula derivation and all boundaries.
- `PROOF_PACKAGE.md`: concise proofs of the correct mathematical ceiling.
- `THEOREM_CONTRACT.md`: explicitly unpromoted candidate contract.
- `OWNER_SEARCH_LOG.md` and `OWNER_AUDIT.md`: bounded public search and
  subtraction.
- `COLLISION_GATE.md`: P103/P109/P115/P137 and current-batch firewall.
- `verify_scout.py`: standalone standard-library exact verifier.
- `CANONICAL.txt`: frozen deterministic stdout.

## Replay

Environment used: Python 3.12.3.

```sh
python3 -B verify_scout.py
```

Two fresh invocations were compared byte-for-byte with `CANONICAL.txt`; both
matched.  The transcript reports `7,124,325` assertions and `RESULT=PASS`.

Frozen transcript SHA-256:

`d82af7bbe1f682bc2bc1b5adbd6e03e8fefa29b72149e6baab435c496ac8a07d`

The verifier is falsification evidence, not experimental proof and not an
ownership claim.
