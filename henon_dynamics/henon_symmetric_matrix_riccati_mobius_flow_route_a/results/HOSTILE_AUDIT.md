# C309 hostile audit

The adversarial suite targets the errors most likely to survive a visually
plausible derivation: reversing the vector field, dropping the `lambda=-1`
limit eigenspace, treating all data as forward global, moving or deleting a
pole, replacing a Loewner denominator, miscounting a center block, promoting
the finite lift to `A4_PASS`, and unlocking Route B.

It also submits a stale payload hash, duplicate top-level JSON key, `NaN`,
and a top-level array.  All 34 attacks must fail after any altered semantic
payload has received a freshly repaired hash.  Passing the suite therefore
tests content rather than hash staleness alone.

The audit does not claim that finite testing proves the matrix theorem.  The
analytic proof remains authoritative.
