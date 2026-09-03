# Code map

- `c332_moreau_play_producer.py` writes exact periodic-play receipts.
- `c332_moreau_play_checker.py` independently recomputes every clamp, chamber, path, variation, evaluator, and schema field without importing the producer.
- `c332_moreau_play_sympy_crosscheck.py` exhausts an exact rational grid for idempotence, order, nonexpansion, rate independence, feasibility, and variation.
- `c332_moreau_play_replay.py` performs two isolated byte replays.
- `c332_moreau_play_mutation.py` runs parser, semantic, nested-schema, and repaired-hash attacks.
- `c332_release_manifest.py` closes the 27-payload release ledger and fresh-builds every PDF twice.

Every executable refuses optimized Python.
