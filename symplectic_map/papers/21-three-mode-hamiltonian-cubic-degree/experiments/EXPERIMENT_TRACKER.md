# Analytic verification tracker

| ID | Check | Owner | Status | Artifact |
|---|---|---|---|---|
| A1 | gradients and inverse shears | author | planned | manuscript proof |
| A2 | all ℕ\(^6\) support rows | author | planned | proof package |
| A3 | two selector gaps (M_S,M_T) | author | planned | proof package |
| A4 | cone invariance split | author | planned | proof package |
| A5 | old-term induction/no cancellation | author | planned | proof package |
| A6 | visibility and exact degree | author | planned | proof package |
| A7 | PF, row-sum, characteristic polynomial | author | planned | manuscript proof |
| A8 | mod-5 irreducibility residues | author | planned | contained corollary |
| A9 | (g=7) boundary anti-example | author | planned | limitations section |

All statuses remain `planned` until a later source/build review records a
deterministic check.  There is no numerical result table.

## Evidence fields

Each tracker row has four mandatory evidence fields: source line range,
mathematical object, expected sign/equality, and reviewer disposition.  A row
cannot be marked complete merely because a formula appears in a draft.

| ID | Source object | Expected exact check | Failure action |
|---|---|---|---|
| A1 | (J_S,J_T) | (J^T\Omega J=\Omega) | stop; repair inverse or Hessian proof |
| A2 | eight gradient monomials in six rows | all rows in ℕ\(^6\) | stop; enumerate missing gradient |
| A3 | (M_S,M_T) | strict positivity on (g\ge8) cone | stop; do not add ad hoc gap |
| A4 | (C_g) and (H) | both coefficient cases | stop; retain symbolic split |
| A5 | support induction | unique selected row each step | stop; expose old-term collision |
| A6 | (C-A,e_3) | (U_3>U_2,U_1) | stop; degree not certified |
| A7 | row sums | (r_i<(g-1)^2) | stop; correct bound |
| A8 | χ and mod 5 | no roots for residues 2,3,4 | report algebraic exception |
| A9 | (g=7) | boundary wording exact | stop; remove false tie claim |

The tracker intentionally has no runtime, random seed, dataset, or hardware
column: those would misrepresent the analytic nature of this project.
