# C238 reproducibility code

`c238_friction_producer.py` writes the deterministic evidence receipt.  It
uses exact rational turning maps and 90-decimal phase/time values for the
maximal-monotone Coulomb inclusion
\(\dot x=v,\ \dot v=-\omega^2x-c\,\xi,\ \xi\in\mathrm{Sign}(v)\).

`c238_friction_checker.py` independently rederives the stick set, release
direction, half-cycle count, general first-turn phase, finite capture time,
harmonic face, and energy ledger; it never imports the producer.  The SymPy
script checks the mode equations and identities, replay checks byte equality
in two fresh temporary trees, and the mutation suite rejects 28/28 stale or
hash-repaired hostile edits, including the exterior-rest center-sign and
partial-arc naming fields.

All scripts are deterministic under `PYTHONDONTWRITEBYTECODE=1`.  No target
arithmetic data or Hilbert–Pólya object is read or claimed.
