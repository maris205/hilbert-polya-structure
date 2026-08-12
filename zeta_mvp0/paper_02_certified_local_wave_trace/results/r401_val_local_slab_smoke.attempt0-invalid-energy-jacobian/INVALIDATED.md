# Invalidated certificate attempt

This archive is preserved for audit history and is **not a passing proof
result**.

The producer used the midpoint energy gradient in the first Krawczyk
Jacobian row.  In particular it printed `J[0,2]=[0,0]` even though the root
box had `P_minus in [-8e-5,8e-5]` and the exact derivative is
`dK/dP_minus=P_minus`.  Hence the archived matrix did not enclose
`D_xF(X,E)` and its Krawczyk inclusion was invalid.

The defect was independently identified during the L1 audit.  It is fixed in
the frozen L1 source; no hashes, transcripts, margins, or checker status in
this directory may be cited as a proof milestone.
