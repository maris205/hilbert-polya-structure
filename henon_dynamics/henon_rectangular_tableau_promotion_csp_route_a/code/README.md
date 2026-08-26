# C187 executable contract

- `c187_tableau_csp_producer.py`: standard-library q-hook/cyclotomic producer.
- `c187_tableau_csp_checker.py`: independent polynomial quotient plus direct
  small-tableau enumeration, promotion, demotion and evacuation checker.
- `c187_sympy_crosscheck.py`: separate SymPy cyclotomic reconstruction.
- `c187_replay.py`: byte-for-byte producer replay.
- `c187_mutation.py`: semantic repaired-hash and stale-hash rejection suite.
- `c187_release_manifest.py`: self-excluded content-addressed release ledger.

No checker imports the producer.  The producer writes the canonical evidence;
the release script writes the manifest.  Both outputs are deterministic under
the checked source tree.

All programs use only package-local evidence and mathematical source data.
They do not read target zero tables, prime tables, arithmetic local data, Euler
factors, root numbers, automorphy data, or Route-B artifacts.
