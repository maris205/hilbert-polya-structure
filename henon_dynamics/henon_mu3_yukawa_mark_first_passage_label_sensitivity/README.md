# HCS-C92 first-passage label sensitivity

C92 resolves the exact labelwise sensitivity of the C88 first-passage time
for all twenty subgroup targets.  For each target and each of the sixteen
named labels it records the pivotal permutation count, the rank-resolved
law, and the induced first-passage contribution.  The efficiency identities
recover the C88 first and second moments without sampling.

Evidence SHA-256:
`902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812`.

The independent checker, SymPy cross-check, clean replay, and 12/12 hostile
mutations pass.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This is an exact finite sensitivity certificate.  It makes no arithmetic or
local-data, Euler-factor, root-number, automorphy, full Burnside/table-of-
marks, or Hilbert--Polya operator claim.
