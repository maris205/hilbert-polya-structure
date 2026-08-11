# Repository update: HCS-C31

Add `henon_bowen_pressure_gate/` as the certified resolution of the positive
instability-roof signal on the local \(H_6\) horseshoe.

The new package proves

\[
0.277980<h_*<0.277987,
\qquad
P_{\Sigma_A}(-h_*\tau_{\rm ad})=0,
\]

using all 1,156 chronological length-13 cylinders, outward rational interval
arithmetic, and exact Collatz--Wielandt inequalities on a 714-vertex
higher-block graph.  It also proves an explicit adapted/Euclidean roof
coboundary, local maximality, the sharpened expansion bound
((\sqrt{17}+\sqrt{13})/2), and the Hausdorff-dimension interpretation.

The previous finite-cycle value \(0.277982981676189\ldots\) lies inside the
independent pressure bracket and is therefore consistent, to certified
resolution, with ordinary Bowen geometry.  C31 does not claim equality or
convergence of those finite sections.  The strict Route-A record is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED` for that interpretation.

The release includes a producer, independently written checker, 30
regression/adversarial tests, a fail-closed runner, complete certificate,
paper source, and compiled PDF.
