# HCS-C171: Ehrenfest hypercube trace and Krawtchouk compression

This package proves for every \(d\geq1\) the complete spectrum of the
coordinate-flip Ehrenfest operator, its power traces and determinant, every
vertex return probability, odd-time vanishing, and an exact reversible
Hamming-weight compression from dimension \(2^d\) to \(d+1\).

## Explicit progress

- Walsh eigenvalue \(1-2j/d\) with multiplicity \(\binom dj\).
- Exact \(\operatorname{Tr}(P_d^n)\) and \(\det(I-zP_d)\) for all \(d,n\).
- Exact return law and bipartite odd-time obstruction.
- Reversible birth--death lumping with symmetric Jacobi similarity and simple
  Krawtchouk spectrum containing every distinct source eigenvalue.
- Natural finite self-adjoint contraction, but no same-clock Hamiltonian lift.

Start with [the proof package](THEOREM_PACKAGE.md), inspect the
[evidence report](results/RESULTS.md), and read the independent
[compiled paper](paper/main.pdf).  Reproduce the artifact with the commands in
`EXPERIMENT_PLAN.md`.

Route-A verdict:
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`.
The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
