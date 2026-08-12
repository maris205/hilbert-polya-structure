# R401-VAL-L3-BT-S0 branch-tube implementation smoke

Prototype status: `PASS_NON_LICENSING_BRANCH_TUBE_SMOKE`  
Licensing: `NON_LICENSING`  
Milestone status: `null`  
Theorem status: `null`  
Final status: `null`

The pinned CAPD multiprecision `SolutionCurve` integrated the accepted A4.12
primary boxes S000, S025, and S050 at 128 and 256 bits.  Each complete
normalized period was covered by 64 closed dyadic phase cells.

- jobs passing: `6/6`;
- largest rigorous upper endpoint of `r_-^2`: `0.000112458090377377848522484092281515416322490332`;
- smallest rigorous lower endpoint of `0.04^2-r_-^2`: `0.00148754190962262215147751590771848458367245756`;
- CAPD commit: `731079217a9254ea2948d742df2b170895effe7f`.

This is an implementation smoke for the distinguished branch only.  It does
not show that an arbitrary return starting with small slow radius remains in
the tube, does not make the Poincare section complete modulo time translation,
and does not close a global shell, `delta_tr`, trace-formula, arithmetic,
zeta-zero, Hilbert--Polya, or RH gate.
