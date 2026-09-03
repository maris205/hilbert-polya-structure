# Code map

- `c348_rwre_producer.py`: canonical exact evidence producer.
- `c348_rwre_checker.py`: producer-independent complete ledger and schema checker.
- `c348_rwre_sympy_crosscheck.py`: independent symbolic identities.
- `c348_rwre_replay.py`: two-isolated-directory byte replay.
- `c348_rwre_mutation.py`: repaired-hash and strict-parser hostile suite.
- `c348_release_manifest.py`: final 27-payload release gate and manifest writer.

Every executable refuses optimized Python because assertions and explicit checks
are part of the audit contract.  The producer and checker share no imports.
