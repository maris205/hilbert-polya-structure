# C246 reproducibility code

`c246_tcp_aimd_producer.py` emits exact square-perpetuity moments, a finite
q-product prefix, generator coefficients, stationary Markov-renewal/Palm
occupation metadata, and a rational hazard-reward skeleton for 27 parameter
tuples.  `c246_tcp_aimd_checker.py` independently reconstructs every value;
`c246_tcp_aimd_sympy_crosscheck.py` checks the hazard, (2a/\rho) square
completion, exponential Laplace factor, generator, continuous Laplace-generator,
and reward identities;
`c246_tcp_aimd_replay.py` checks byte equality; and
`c246_tcp_aimd_mutation.py` rejects 36 hostile mutations.

For beta>0 the jump skeleton is stationary Markov, not iid regenerative.  The
q-product is source-local probability data, never an Euler factor.  All scripts
are deterministic with `PYTHONDONTWRITEBYTECODE=1`; sidecars are excluded.
