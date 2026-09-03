# Code map

- `c346_skorokhod_producer.py` emits canonical rational event, fixed-point,
  Picard and threshold receipts.
- `c346_skorokhod_checker.py` independently parses and reconstructs every
  active-set LCP, path fixed point, time-change control, contraction row,
  threshold witness, evaluator field and scope lock without importing the
  producer.
- `c346_skorokhod_sympy_crosscheck.py` exhausts a larger exact coupling/state
  grid and checks inverse, contraction and sharp-wall identities.
- `c346_skorokhod_replay.py` makes two isolated byte-identical reproductions.
- `c346_skorokhod_mutation.py` runs stale/repaired-hash, nested-schema and
  strict JSON/YAML attacks.
- `c346_release_manifest.py` reruns all lanes and closes deterministic PDF and
  27-payload release gates.

Every executable refuses optimized Python.
