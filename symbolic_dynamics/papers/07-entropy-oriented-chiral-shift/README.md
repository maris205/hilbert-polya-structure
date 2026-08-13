# Entropy-Oriented Couplings of the Tensor-Prime Shift

Status: **GO A3 CHIRAL MOTION / STOP UNIFIED DIVISOR / ROUTE B LOCKED**

Candidate: **SD-C09**, the entropy-oriented anticommutator shift.

Research index: [Ra-1: Arithmetic Symbolic Dynamics](../../README.md)

Shared rules: [proposal](../../propose-symbolic-dynamics.md),
[Route A](../../skills/route-a-evaluator.md), and
[Route B](../../skills/route-b-evaluator.md).

Paper07 defines **SD-C09**, an exact noncommuting extension of the tensor-prime symbolic Euler transfer.

The tensor atoms are ordered intrinsically by entropy, `2 = p1 < p2 < ...`. On the atom Hilbert space,

```text
D_s e_n = p_n^{-s} e_n,
S e_n = e_{n+1},
L_s = (1/2){D_s, I+S}.
```

Successor edges mix unequal masses but always increase entropy, so they cannot enter a periodic word. For `Re(s)>1`,

```text
Tr L_s^r = sum_p p^{-rs},
det(I-zL_s) = product_p (1-zp^{-s}).
```

The chiral double lies in `S_3` on `1/3<Re(s)<2/3`, has exact `s <-> 1-s` determinant symmetry, is self-adjoint on the critical axis, and has genuine non-gauge spectral motion.

The limitation is equally exact: the coupling lies in a triangular radical. It changes singular values but not periodic traces, eigenvalues, or the Euler Fredholm divisor. All-order graded cancellation has the same ceiling: it contributes superdeterminant one.

The frozen controls make this limitation concrete: arbitrary forward-edge
phases and all 24 random DAGs retained the all-order ledger and showed
spectral motion. Only reverse/recurrent edges broke the ledger. The observed
positive-axis sign-change count was stable across cutoffs but grew
`O(T)`-like, not as a certified Riemann divisor.

```text
GO_A3_CHIRAL_MOTION / STOP_UNIFIED_DIVISOR / ROUTE_B_LOCKED
```

## Shareable artifacts

- [Paper PDF](main.pdf)
- [LaTeX source](main.tex)
- [Proof package](PROOF_PACKAGE.md)
- [Experiment report](EXPERIMENT_REPORT.md)
- [Route-A evaluation](evaluations/route_a/SD-C09/20260813T235900Z.yaml)
- [Compilation report](COMPILATION_REPORT.md)
- [Integrity manifest](PAPER_MANIFEST.sha256)
