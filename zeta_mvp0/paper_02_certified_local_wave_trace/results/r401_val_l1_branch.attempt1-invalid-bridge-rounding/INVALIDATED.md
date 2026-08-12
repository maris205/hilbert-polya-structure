# Invalidated L1 production attempt

This attempt passed all 202 CAPD/Krawczyk jobs and all 202 independent
arithmetic replays, but it is **not** the accepted branch-gluing certificate.

The decimal bridge boxes were the exact mathematical hulls of the decimal
primary boxes.  CAPD then parsed and constructed the primary and bridge boxes
in separate outward-rounded operations.  The checker found 89 printed
coordinate containments displaced by roughly one final MPFR/formatting ULP.
Consequently the stronger archived gate

`actual bridge X contains both actual adjacent primary X boxes`

was false, even though the discrepancy was many orders of magnitude below
the Krawczyk margins.

No tolerance was applied after seeing the result.  The replacement protocol
pre-freezes a rational `1e-18` padding on every side of every bridge hull and
reruns both precisions.  The complete frozen inputs for this failed attempt
are retained in `frozen_inputs/`.
