# Two-round substantive improvement log

## Round 0 — original theorem draft

The original paper fixed the `gamma_phi/2` convention, solved the density
matrix, gave the four Liouvillian eigenvalues, derived the normalized Choi
matrix, and proved the exact PPT/entanglement-breaking inequality and the
unique faithful-thermal threshold.

Artifact: `paper/main_round0_original.pdf`.

## Round 1 — dynamical and boundary closure

The first revision added the sharp trace-norm contraction coefficient
`max(exp(-Gamma1 t),exp(-Gamma2 t))`; used it to rule out nonconstant
recurrence for positive population damping; and separated the pure-dephasing,
unitary, identity, faithful thermal, and two one-sided amplitude-damping
faces.  During hostile review, the zero-generator corner was corrected from a
two-dimensional to a four-dimensional Liouvillian kernel.

Artifact: `paper/main_round1.pdf`.

## Round 2 — evidence and inference firewall

The second revision added the exact 124-row evidence matrix, independent
checker/SymPy/replay/mutation chains, source-owner boundaries, collisions with
C223/C224/C237/C243/C297/C298, and explicit counterexamples to the inference
“finite determinant implies arithmetic determinant.”  It states the complete
Route-A tuple and locks Route B under the frozen scope.

Artifact: `paper/main_round2.pdf`, byte-identical to `paper/main.pdf`.
