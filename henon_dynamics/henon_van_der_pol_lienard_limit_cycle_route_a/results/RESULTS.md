# C249 results

The analytic atlas contains eight parameter rows: two negative-damping
time-reversed rows, the \(\mu=0\) harmonic-center boundary, and five positive
rows with one attracting cycle.  Five DOP853 probes on
\(\Sigma=\{x=0,y>0\}\) isolate the return fixed point.  Their periods range
from 6.2871112673 (\(\mu=0.1\)) to 10.2035236706 (\(\mu=4\)); the transverse
Floquet multiplier ranges from 0.5330692600 to
\(1.2754744\times10^{-25}\).  Energy-balance residuals are below
\(5.4\times10^{-12}\).

The producer-independent checker passes 264 assertions, the SymPy
cross-check passes 81 identities, clean byte replay passes, and the hostile
suite rejects 40/40 repaired-hash mutations.  These are reproducibility gates
for the displayed receipt, not replacements for the Liénard theorem.

The route tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`; all scope flags are false and Route B is disabled.
