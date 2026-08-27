# C191 code

- `c191_sinkhorn_producer.py` creates the canonical exact evidence ledger.
- `c191_sinkhorn_checker.py` independently reconstructs matchings, support
  strata, scalings, iterations and local spectra.
- `c191_sympy_crosscheck.py` supplies a separate symbolic/Ryser path.
- `c191_replay.py` requires byte-identical isolated reproduction.
- `c191_mutation.py` attacks semantic fields after repairing the payload hash
  and also checks one stale-hash control.
- `c191_release_manifest.py` closes the 27-payload release ledger while
  excluding itself.

The producer honors `C191_OUTPUT` for isolated replay.  All rational evidence
uses `fractions.Fraction`; finite patterns and iterates are regression oracles,
not all-matrix proofs.
