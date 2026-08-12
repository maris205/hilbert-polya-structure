# C34 exact code

- `c34_producer.py` replays the frozen C33 object, derives the degree-18
  radical polynomial, the (19)-adic Newton certificate, the relation
  module, and the full wreath conclusion.
- `c34_checker.py` imports no producer code.  It independently reconstructs
  nine fail-closed gates from the source-locked C33 certificate.
- `test_c34.py` checks deterministic production, theorem fingerprints,
  semantic scope, type-strict JSON behavior, and adversarial rehashed
  mutations.
- `c34_hash_manifest.py` verifies the authored release inventory and hashes.
- `run_c34.sh` performs an isolated read-only replay by default.  Use
  `--refresh-manifest` only while deliberately preparing a new release.

The \(p=19\) argument does not use Dedekind factorization of the power-basis
order.  Both implementations reconstruct the translated coefficient
valuations, unit residues, residual polynomial, residue gcd, and the
splitting-field weight-two parity descriptor.
