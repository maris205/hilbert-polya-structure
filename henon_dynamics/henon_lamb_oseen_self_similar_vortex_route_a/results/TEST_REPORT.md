# Test report

All commands were run from the package root with `PYTHONDONTWRITEBYTECODE=1` and `TZ=UTC`.

| Gate | Result |
|---|---|
| `python -B code/c299_lamb_oseen_producer.py` | `C299_PRODUCER_PASS`; 213 cells; stable payload and file hashes |
| `python -B code/c299_lamb_oseen_checker.py` | `PASS (1195 assertions; producer import forbidden)` |
| `python -B code/c299_lamb_oseen_sympy_crosscheck.py` | `PASS (31 symbolic identities)` |
| `python -B code/c299_lamb_oseen_replay.py` | byte-for-byte `PASS` |
| `python -B code/c299_lamb_oseen_mutation.py` | `PASS 84/84` |
| strict evaluation parser | duplicate keys, anchors, aliases, merge keys, timestamp coercion, type changes, and tuple/scope mutations rejected |
| three PDF rounds | 3/3/4 pages; distinct hashes; settled logs; embedded subset fonts |
| six isolated PDF rebuilds | each pair byte-identical to its archived round |
| extracted text and raster audit | all contracts and all 10 pages pass |
| closed-world ledger | 27 manifest payloads and 28 physical files |

The checker independently recomputes field, moment, norm, trajectory, boundary, metadata, and evaluation receipts.  It enforces exact row-key ledgers, full nonclaim/boundary/reference trees, and canonical rational strings, and it does not import the producer.  Evidence mutations repair the canonical payload digest before checking whenever the attack is semantic, so rejection does not reduce to detecting a stale checksum.
