# C124 exact experiment plan

## Goal

Certify the joint orbit--operator bridge and its translation-blindness limit
without floating-point tolerances or external data.

## Gates

1. **Source lock:** freeze (A,t,B,c,W), the radius-three bidisc, one-edge
   clock, and (D_H(z)=\det(I-z\mathcal L)).
2. **Geometry:** prove strict interior, contraction, and pairwise branch-image
   separation by rational inequalities.
3. **Orbit owner:** enumerate all rooted closed words and primitive necklaces
   through period eight as a replay prefix; prove the word-to-cycle statement
   for every period.
4. **Global operator:** prove the graph-directed Hardy operator trace class via
   compact interior inclusion and total-degree truncation.
5. **Trace/Fredholm theorem:** reconstruct eight exact power traces and Taylor
   coefficients, while proving the formulas for every positive power.
6. **Finite sections:** independently assemble polynomial matrices through
   total degree three and compare their power traces with the graded formula.
7. **Negative control:** move the translations to ((-3/2,0,3/2)), preserve
   separation, and prove that cycle coordinates change while determinant data
   do not.
8. **Falsification:** require the independent checker to reject mutations of
   geometry, graph, weights, traces, orbit ledger, control, verdict, or scope.
9. **Release:** byte replay, deterministic double LaTeX build, embedded-font
   check, rendered-page inspection, and content-addressed manifest closure.

## Success and failure

Success is an exact internal dynamical theorem with the strict tuple
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.  A source Fredholm determinant without a
target divisor match is not an A2 pass.  Any compiler warning, unrejected
hostile mutation, or translation-sensitivity overclaim blocks release.
