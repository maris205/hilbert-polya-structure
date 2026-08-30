# Source and scope audit

- Candidate: `HCS-C240`.
- Source/code baseline: `489506cf92bfed721f94f22dd0444a60427f90a5`.
- Route evaluator: `flow_systems/skills/route-a-evaluator.md`, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Fixed epoch: `1788048000`.
- Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

The frozen object is the two-branch map
\(x\mapsto\{\lambda x+\delta\}\) on a half-open interval.  The only
parameters are the source-defined rational slopes \(1/2,2/3,3/4\) and
\(\delta\in[0,1)\).  All word compositions, candidate points, inequalities,
and endpoint equalities are evaluated with exact `Fraction` arithmetic.

The cited Laurent–Nogueira paper is used for the definition and established
rotation-number context.  Nogueira–Pires is used only for its stated finite
periodic-orbit bound for injective interval contractions.  Bugeaud–Conze is
context for contracting-mod-one and Farey/Hecke–Mahler structure.  None of
these citations is treated as a priority certificate for this finite receipt.

The release proves one fixed point per declared word and exact admissibility at
the finite cutoff.  It does not assert a global one-cycle theorem, a maximal
plateau classification, or completeness beyond length 12.  Endpoint equality
is part of the model: lower inequalities are closed, upper inequalities are
open, and \(\delta=1\) is outside the domain.

No target zero list, prime list, local arithmetic datum, Euler factor, root
datum, automorphy assertion, target divisor, or Hilbert–Pólya operator enters
the source, code, evidence, or paper.  The source-local derivative factor is
labelled as such and cannot be promoted to a target determinant.
