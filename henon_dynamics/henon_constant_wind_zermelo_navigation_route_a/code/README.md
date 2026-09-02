# C305 code lanes

- `c305_zermelo_producer.py`: canonical all-chamber evidence.
- `c305_zermelo_checker.py`: producer-independent reconstruction of every
  invariant, root, time interval, control, HJB probe, and exact YAML tree;
  rejects optimized Python.
- `c305_zermelo_sympy_crosscheck.py`: exact quadratic, root, scaling, HJB,
  and cone-boundary identities.
- `c305_zermelo_replay.py`: two isolated byte-identical producer runs.
- `c305_zermelo_mutation.py`: repaired-hash semantic attacks and hostile
  JSON/YAML syntax/type attacks.
- `c305_release_manifest.py`: complete PDF and 27-payload release gate.

The documented runtime is ordinary `python -B`; no other script is claimed
to support optimized `python -O` semantics.
