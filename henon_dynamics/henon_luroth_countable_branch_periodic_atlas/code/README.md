# C241 code contract

* `c241_luroth_producer.py` deterministically emits the exact/90-digit JSON
  receipt for branches, words, necklaces, weighted cutoffs, limits, and formal
  primitive products.
* `c241_luroth_checker.py` independently reconstructs every fraction, itinerary,
  convergence label (including divergence at \(s=1/2\)), theorem/provenance
  lock, and route tuple.
* `c241_luroth_sympy_crosscheck.py` verifies affine identities, multipliers,
  telescoping, and finite formal series in exact SymPy rationals.
* `c241_luroth_replay.py` checks byte-identical clean regeneration.
* `c241_luroth_mutation.py` runs 56 hostile mutations, including repaired-hash
  semantic mutations.
* `c241_release_manifest.py` reruns all gates and closes the 27-file payload
  ledger (28 physical files including the self-excluded manifest).

All scripts use the frozen baseline `489506cf92bfed721f94f22dd0444a60427f90a5`,
evaluator SHA
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`, and
scope `NO_BAD_EULER_OR_ROOT_NUMBER`.
