# Candidate Registry

## SD-C11 — holomorphic reflection double

- Family: **Symbolic Dynamics**, exclusively.
- Atoms: internally generated tensor-indecomposable full shifts F_p,
  entropy ordered by log(p).
- Base grammar: recurrent bidirectional nearest-neighbor chain inherited
  from SD-C10, with identity atom loops.
- Channels: plus and minus; every step changes channel.
- Transfer:

  \[
  C_s=\begin{pmatrix}0&T_s^+\\T_{1-s}^-&0\end{pmatrix}.
  \]

- Cocycles: disjoint directed-positive alphabets in the frozen object.
- Reflection: channel swap plus alphabet exchange, J C_s J=C_(1-s).
- Regularization: det_3 on 1/3<Re(s)<2/3.
- Data firewall: no Riemann-zero data, target-root comparison, fitting, or
  post-hoc rescaling.

### Exact accomplishments

1. Odd finite-prefix traces vanish, and
   Phi_2(C_s^(2r))=2 sum_p p^(-r) in the identity sector.
2. The common Schatten strip is 1/q<Re(s)<1-1/q; q=3 is the first integer.
3. The exact regularized product is

   \[
   \det{}_3(I-zC_s)=\prod_p(1-z^2/p)e^{z^2/p}.
   \]

4. The product has exact reflection symmetry and is independent of s.
5. A cross-atom pair moves by a cosh factor only when p differs from q, in
   which case it is a mixed generalized-ledger term.

At infinite atom count, the quadratic trace 2 sum_p 1/p is divergent and is
not claimed as an honest trace. It is exactly the term removed by det_3.

### Specificity boundary

Shared positive labels preserve sterility. All positive inventories do.
All 32 random cross-atom pairings create motion by introducing mixed atom
pairs. All 24 random upper-DAG controls preserve the cyclic determinant
while moving singular geometry. Hence neither reflection sterility nor
nonnormal motion is an arithmetic divisor selector.

### Route status

    (A0_ANALYTIC_ARITHMETIC_ORIGIN,
     A1_PASS_ANALYTIC,
     A2_ANALYTIC_DETERMINANT,
     A3_PARTIAL_ANALYTIC_STRUCTURE,
     A4_FAIL)

    ROUTE_A_EXPLORATORY
    GO_REFLECTION_RIGIDITY / STOP_VERTICAL_DIVISOR
    route_b_invocation_allowed: false

Canonical provisional evaluation:
evaluations/route_a/SD-C11/20260813T133745Z.yaml. Commit fields remain
WORKTREE_PENDING_FINAL_COMMIT until the root agent performs the two-stage
freeze.
