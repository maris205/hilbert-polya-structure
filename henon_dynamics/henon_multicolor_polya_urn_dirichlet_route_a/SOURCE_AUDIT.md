# Source and scope audit

- Candidate: HCS-C263, classical multicolor Eggenberger--Pólya urn.
- Baseline/source commit: `98782afe1e754c311ad0736f72ce09dcc7c85c77`.
- Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Clock: one draw, replacement, and reinforcement update.
- Positive-reinforcement normalization: `alpha_i=a_i/c` on the active face.
- Zero-reinforcement policy: iid categorical draws; no `alpha` is defined.
- Arithmetic origin: none.  The color labels and masses are source-defined.
- Determinant convention: none; no target or Fredholm determinant.
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`; all forbidden-data flags are false.

Primary source metadata were checked against the Wiley record for Eggenberger
and Pólya (1923), DOI `10.1002/zamm.19230030407`, and the Annals of Statistics
record for Blackwell and MacQueen (1973), DOI
`10.1214/aos/1176342372`.  These references establish context, not a workspace
literature-priority claim.

The closest local stochastic owners are C171 (Ehrenfest), C194 (Holte
carries), and C253 (fixed-population Moran absorption).  C263 is distinct:
its population mass grows, its histories are exchangeable, and its directing
measure is Dirichlet.  Counts `N_i(n)`, normalized masses `P_i(n)`, and the
`c=0` iid probabilities are never conflated.
