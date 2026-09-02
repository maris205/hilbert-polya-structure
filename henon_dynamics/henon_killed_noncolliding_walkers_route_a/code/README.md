# Code lanes

- `c306_walkers_producer.py`: deterministic canonical JSON atlas with
  payload self-hash.
- `c306_walkers_checker.py`: independent reconstruction of generators,
  spectra, matrix exponentials, determinants, QSD/Doob identities, strict
  JSON/YAML trees and types; it does not import the producer and refuses
  `python -O`.
- `c306_walkers_sympy_crosscheck.py`: exact characteristic-polynomial and
  phase-type resolvent lane.
- `c306_walkers_replay.py`: two isolated fresh outputs versus archive bytes.
- `c306_walkers_mutation.py`: repaired-hash semantic attacks, stale-hash
  control, parser attacks, bool/float traps, and optimized-Python control.
- `c306_release_manifest.py`: all gates, deterministic paper builds, visual
  render checks, closed-world ledger, and manifest writer.

The producer and checker intentionally duplicate the mathematical
construction rather than sharing executable implementation code.
