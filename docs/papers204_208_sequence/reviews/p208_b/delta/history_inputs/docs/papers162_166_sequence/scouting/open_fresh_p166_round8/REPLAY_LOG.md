# Frozen replay log

**Date:** 2026-09-03 UTC  
**Verifier:** `verify_scout.py`  
**Canonical stdout:** `CANONICAL.txt`  
**Assertions per replay:** `1,119,007`

Two fresh standard-library executions were compared directly with the frozen
canonical stdout:

```text
replay 1: diff byte match OK
replay 2: cmp  byte match OK
```

Frozen object hashes:

```text
592015efa9c0b710e138fc8bbee4d762619f0fb18a05dc406307ae3e6f1fef71  verify_scout.py
0191379719612959837d54b3a4c55100827cc9cbcd4bf0e9aacdaa15437a0f36  CANONICAL.txt
```

The canonical stream is 1,603 bytes and ends with
`GREEN_OWNER_THIN_MIP` / `HOLD_EXTERNAL`.  No author or prior-scout code is
imported by the verifier.
