# Hostile mutation audit

`c246_tcp_aimd_mutation.py` applies 36 no-op-guarded edits to beta, (a),
(rho), the (2a/rho) factor, moments, q-product coefficients, occupation
wording and Markov flag, reward skeleton, boundary rows, metadata, route tuple,
scope firewall, and unknown keys.  Repaired hashes do not mask semantic edits:
the independent checker rejects all 36/36, including one stale-hash case.
