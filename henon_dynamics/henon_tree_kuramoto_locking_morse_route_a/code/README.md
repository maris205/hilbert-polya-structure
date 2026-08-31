# Exact-code contract

All scripts use only source-local tree synchronization data.  They never load
prime tables, target zeros, target arithmetic local data, or Route-B inputs.

- `c259_kuramoto_producer.py` enumerates every labeled Prüfer tree for
  `2 <= N <= 7`, constructs rational cut-flow test rows, and writes the
  content-addressed evidence JSON.
- `c259_kuramoto_checker.py` independently decodes every Prüfer word,
  reconstructs subtrees, cut sums, branch counts and Morse histograms.
- `c259_kuramoto_sympy_crosscheck.py` derives the incidence, quotient-Hessian
  congruence and determinant identities in a fresh symbolic implementation.
- `c259_kuramoto_replay.py` requires two fresh producer runs to equal the
  released evidence byte for byte.
- `c259_kuramoto_mutation.py` rehashes hostile semantic changes and requires
  the independent checker to reject every one.
- `c259_release_manifest.py` reruns all gates and seals the 27 release
  payloads while excluding its own manifest.

Run from the repository root with `python3 -B`.  The fixed build epoch is
`1788048000`, and the scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
