# HCS-C281 — product-sphere Ricci-flow singularity atlas

This replacement release freezes a genuinely geometric-PDE owner.  On

\[
M=\prod_{i=1}^m S^{d_i},\qquad
g(0)=\bigoplus_{i=1}^m a_i g_{S^{d_i}},
\]

with arbitrary positive integers `d_i` and positive scales `a_i`, the
unnormalized Ricci flow is solved exactly and its first singularity is
classified without genericity assumptions.  The package retains every tied
collapse, every `d_i=1` flat clock, the all-torus face, the full-versus-partial
collapse dichotomy, the pointed Type-I blowup, and the precise
volume-normalized time conjugacy.

The headline is a nonlinear evolution of Riemannian metrics.  It is not a
heat-trace, zeta, determinant, or Schatten paper.  The strict Route-A tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`,

with overall `ROUTE_A_REJECTED` and scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic data are used.

Start with [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md), then run the commands in
[code/README.md](code/README.md).  The final paper is
[paper/main.pdf](paper/main.pdf).
