# Round 2 decision: reviewed auxiliary progress; automatic continuation

2026-09-09 UTC. Coordinator decision under the user's confirmed continuous
Hénon / Route-A authority. This is a saved research checkpoint, **not a stop**,
a five-paper completion, manuscript admission, or formal Route-A evaluation.
First-pass and previous-batch accepted artifacts were not reopened or edited.

## Outcome

**EIGHT_AUTHOR_LANES_COMPLETE; NINE_NONAUTHOR_REVIEWS_CLOSED;
ZERO_OPEN_MUST_FIXES_ON_REVIEWED_CLAIMS; ZERO_NEW_PAPERS; ROUND3_ACTIVE.**

The coordinator has read all nine final review reports completely, including
their source-applicability boundaries and correction readbacks. Final C4 NI
proof and D2 field/count proofs were read; the relevant A1/A3/B4 proof changes,
the producer algorithm and the independent E2 checker were also inspected.
This is current-team internal proof checking, not human peer review or evidence
of review by an independent model family. No full ARS review panel is claimed.

The original PC424-L, PC424-D, LG4 and all-level Fricke FGT questions are
unchanged and unclosed. The accepted increments below are useful intermediate
theorems and exact method boundaries. Their sizes do not turn them into separate
papers, and multiple approaches to one question do not create multiple slots.

## Claim-by-claim disposition

| Lane / evidence | Accepted precise output | Still missing |
| --- | --- | --- |
| [A1](a1_frobenius_finiteness/PROOF_PACKAGE.md), [E8](reviews/e8_dynamics_algebra/REVIEW.md) | Dynamics-algebra finite simple modules are exactly ordinary native cycles with scalar return; grade-zero cocenter is the polynomial coboundary quotient; nonzero grades are full-periodic-scheme **coinvariants**. Finite-quotient trace radicals are Frobenius-nilpotent with quotient-dependent exponents. | A global cocenter separation/Frobenius relation. Finite presentation, quotientwise nilpotence and the Leavitt control do not answer PC424-L. |
| [A2](a2_algebraic_transfer/REPORT.md), [E1](reviews/e1_periodic_graph/REVIEW.md) | For an actual native periodic transfer graph, `N <= D + d_T D^3` unless the polynomial is a coboundary modulo constants; all ordinary cycle sums remove that constant. Equations with `D=o(N^(1/3))` suffice. | Existence of that complexity bound from all orbit sums. `N` is actual periodic points, not the size of a full finite field. |
| [A3 pair](a3_wild_local_tower/PROOF_SUPPLEMENT.md), [E2](reviews/e2_local_as/REVIEW.md) | Exactly `(p,e)=(3,2)`: canonical local factor has cyclic splitting field of degree 9, with reduced AS class `2*s^(-4)+s^(-2)`. Independent alternate algorithm agrees. | Uniform all-prime/all-level local full inertia, and separately global cycle-quotient transitivity. |
| [A3 ramification](a3_wild_local_tower/PAIR_RAMIFICATION.md), [E6 pair](reviews/e6_pair_ramification/REVIEW.md) | From that accepted pair: distances `4/3,4`, lower breaks `(4,28)`, upper breaks `(4,12)`, field different 88 and power-order lattice index length 28. | No all-level break pattern or nested field tower follows. Polynomial discriminant 144 is not field different 88. |
| [A4](a4_wild_global_quotient/REPORT.md), [E4](reviews/e4_global_wild/REVIEW.md) | Full orbit-polynomial coefficients generate the generic cycle quotient; rank `(2^n-2^(n/p))/n`; point-component count `sum_j n/h_j`; even quotient-component degrees; exact fixed-point satellite identity; conditional surviving-edge graph bound. | Actual primitive-branch surviving connectivity/CUT. Full inertia on one small cycle does not give global cycle transitivity. A collision-supported cut is not a reducibility certificate. |
| [B1](b1_global_orbit_separation/PROOF_PACKAGE.md), [E7](reviews/e7_polynomial_invariants/REVIEW.md) | Exact fixed-degree all-modulus obstruction via an integer evaluation minor; all-degree invariant-polynomial tests equal separate-prime-power orbit incidence, with explicit denominator clearing. | Actual arithmetic separation of off-orbit integer targets and mixed-modulus time compatibility. The modulus-six control fails the all-level premise and is not an LG4 counterexample. |
| [B4](b4_local_period_degree/PROOF_SUPPLEMENT.md), [E6](reviews/e6_local_displacements/REVIEW.md) | For all odd primes and levels, `delta_j >= (p^j+1)(p-1)/p` and field different `d_L >= p^h-1+p^(e-1)(p-1)` when the root field has degree `p^h`. Excludes the same first-level field at higher levels and any fixed finite extension at unbounded levels. | Exclusion of varying, high-conductor proper cyclic subfields. The lower bound does not prove `h=e`. |
| [C4](c4_uniform_fricke/PROOF_SUPPLEMENT.md), [E5](reviews/e5_uniform_fricke/REVIEW.md) | NI: all exact native layers `n>=3` have their full geometric splitting normalization étale at Cayley, hence unramified along the irreducible singular-fibre divisor. Complete ordinary sheet counts are established by degree exhaustion. | Higher-layer transitivity/full wreath groups, smooth fold separation, sign-field exclusion and all-level FGT. No common infinite-tower étale neighborhood is asserted. |
| [D2](d2_fricke_layer_intersection/PROOF_PACKAGE.md), [E3](reviews/e3_fricke_intersections/REVIEW.md) | Actual FG2 characters; NI gives `J_N` among the base, cycle-sign quadratic and full `S_11` cycle splitting field. Distinct full wreath layers have only abelian entanglement under their displayed hypotheses. Ordinary cycle counts strictly increase from `r_2=11,r_3=24`. | Actual higher full groups, the occurrence of the sign field, stagewise intersections and compositum constants. Arithmetic and geometric relations remain separate. |

C4's independently accepted **ordinary-count** conclusion, not just its inertia
statement, now discharges D2 Proposition 7's count dependency. Thus distinctness
and `r_n>=5` are proved for all native layers `n>=2`. C4 NI also discharges
D2 Proposition 3's nodal input. It does not discharge the higher full-group
hypotheses of Propositions 4–5. Under NI, SF2 is equivalent only to the answer
`J_N=base` for every `N`; it is not a complete classification if SF2 fails.

## Actual corrections and evidence

- A1's final summary was corrected from coordinate rings to their coinvariants;
  the nonzero-grade Frobenius is the checked twisted norm, not coefficientwise
  Frobenius at a fixed level. E8 read back the final proof hash
  `cd2e845d479aac752e8397264f02b03df704f9e172f8d16fbcbdf81f4ea86dd3`.
- D2 narrowed the SF2 equivalence, repaired literal carriage-return bytes,
  included period two in the distinct-count condition, and reserved `p_2` for
  the phase squareclass while using `nu_n` for cardinalities. E3 checked the
  revised proofs and final hashes, including the later Proposition 7.
- C4's neighborhood wording distinguishes the higher étale germs from the
  ramified FG2 phase germs. E5 checked the final whole proof. Its source audit
  also subtracts Cantat's earlier Cayley deformation strategy; neither that
  strategy nor the classical count sequence is claimed as new here.
- The coordinator's weighted-polynomial displacement sharpening was adopted
  and proved by B4; E6 independently checked both the argument and every changed
  ramification bound. The older weaker proof was retained as a valid antecedent.
- E6's separate pair review checked both uniformizer tails, fixed coefficient
  field, ramification numbering and the lattice length identity. It binds
  `PAIR_RAMIFICATION.md` hash
  `6478ba42fa8b597f22a1b63558f251a839c1fca40cb0b7a5b2c157d3ae1b5973`.

All reviewer source and applicability limitations remain part of acceptance.
Classical interpolation, Bézout, representation theory, finite Galois theory,
ramification and dynamical counting inputs are subtracted, not relabelled as
independent paper contributions. No exhaustive global novelty certificate is
claimed. A3's [branch-preservation exploration](a3_wild_local_tower/BRANCH_PRESERVATION.md)
records an exact reformulation and elementary axis contacts, with BP expressly
unproved; it is not an additional whole-proof-reviewed uniform result.

## Execution ledger

| Actual mathematical execution | Fixed input / changed condition | Outcome |
| --- | --- | --- |
| [Author run 1](a3_wild_local_tower/execution.log) | `(3,2)`, Hensel precisions 128 then 512 within one allocated run | Exit 2. Discriminant 144 visible, but `512 <= 4*144+8`; AS test inconclusive. |
| [Author run 2](a3_wild_local_tower/execution_n1024.log) | Same pair, separately approved precision 1024 | Exit 0. Complete factor, determinant and negative AS coefficient evidence; approximately 1.88 CPU seconds. |
| [Independent E2](reviews/e2_local_as/independent_execution.log) | Same pair, separately approved precision 64, different factor-membership and trace algorithms | Exit 0. Same reduced class; no producer import, Hensel routine, Cramer or Bareiss determinant. |

The [independent checker](reviews/e2_local_as/check_alternate_trace.py) uses
the supplied coefficient certificate as data, then independently verifies
canonical membership by the exact divided-difference identity. It uses
`alpha/Tr(alpha)` with trace valuation 10; the positive final error exponent
certifies the whole negative part. Its input dependency and algorithmic
independence are both explicit in E2's complete review.

Total: **three executions, one parameter pair**. No other mathematical run,
old certificate rerun, GPU job, manuscript/PDF, formal evaluation, new model/API
upload or configuration change occurred. Proof deductions from this evidence
are not additional executions. The original exit-2 log remains inconclusive.

## Next actions already started

The actual round-3 allocation is recorded in
[CONTINUOUS_RUN.md](../CONTINUOUS_RUN.md). Eight bounded author/source tasks
continue the reduced coefficient, graph complexity, interlevel contact,
primitive collision, branch different, smooth fold, sign character and root
multiplicity problems. E1 has already received the first new nonauthor review.
No round-3 computation is preauthorized by this decision.

The continuous cadence overrides stopping at a round or five-paper checkpoint;
it does not waive source subtraction, full proof, independent checking, actual
PDF and release gates. This batch remains **0/5**. `NO_BAD_EULER_OR_ROOT_NUMBER`
and all evaluator/version boundaries remain unchanged. Routine exact-path Git
synchronization is authorized; this file records mathematical disposition, not
an assertion that a future commit or push has already happened.
