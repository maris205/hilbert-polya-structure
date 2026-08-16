# Code

`c77_ownership_firewall.py` certifies channel-diagonal trace summability,
trace-exponential determinant products, the universal rank-one lemma, exact
rational cyclic-block determinants, singleton energies and powers,
dependency hashes, and claim mutations.

`independent_check.py` does not import the primary module.  It reconstructs
the channel determinant numerically and the finite source blocks by a
separate rational elimination implementation.

`test_c77.py` runs twelve operator-firewall tests under both normal and
optimized Python.

Run `bash code/run_c77.sh` from the project directory or its parent.
