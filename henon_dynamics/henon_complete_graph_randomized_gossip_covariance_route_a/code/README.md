# Code lanes

- `c333_gossip_producer.py`: deterministic exact-rational evidence.
- `c333_gossip_checker.py`: strict producer-independent recomputation.
- `c333_gossip_sympy_crosscheck.py`: symbolic block and projector identities.
- `c333_gossip_replay.py`: two isolated byte-identical producer runs.
- `c333_gossip_mutation.py`: repaired-hash semantic, parser, and evaluator attacks.
- `c333_release_manifest.py`: 27-payload ledger, PDF, font, replay, and release gate.

Every entry point refuses optimized Python.  The checker imports no producer
module.  Run from the package root with `python -B code/<name>.py`.
