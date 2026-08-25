# C144 hostile audit

The mutation harness rewrites semantic fields and repairs the payload hash,
then requires the independent checker to reject each altered artifact.  It
rejects changes to the substitution lock, recurrence and minimality flags,
aperiodicity statement, period certificates, language complexities and
hashes, approximant periods and defect rows, zeta coefficients, Route-A tuple,
scope flags, and nonclaims.  A separate stale payload hash is also rejected.

Result: 36 repaired-hash mutations plus one stale-hash mutation rejected.
This tests semantic enforcement rather than only transport integrity.
