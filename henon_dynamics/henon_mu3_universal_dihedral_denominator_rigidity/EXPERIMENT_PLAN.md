# HCS-C54 exact experiment plan

**Problem:** classify universal source symmetry and ordinary realization of the
rational split exponent.

**Method thesis:** exhaustive phase recurrence plus fixed-\(\ell\)
semisimplification and two-weight
rigidity proves that the source group is \(\operatorname{Dih}(C_{3n})\) and
the complete split-local factor is ordinary exactly when \(n\mid4\).

**Date:** 2026-08-14.

Terminology: “ordinary” means an actual finite-rank compatible realization
with integral multiplicities, not \(p\)-adic or Newton-polygon ordinarity.

## Claim map

| Claim | Why it matters | Minimum convincing evidence | Blocks |
|---|---|---|---|
| C1: full projective monomial source group is \(\operatorname{Dih}(C_{3n})\) | replaces sampled subgroups by a universal classification | symbolic closure proof, explicit generators, exhaustive count | B1, B2 |
| C2: ordinary split-factor realization iff \(n\mid4\) | classifies exactly when the rational exponent becomes an actual system | K0 identity, weight separation, divisor table, direct-copy converse | B3 |
| C3: no \(n=3\) central source sector clears both rails | closes the symmetry-projector loophole | exact Cayley/Fermat characters and rational orbit blocks | B4 |
| C4: split-invisible rational classes do not clear denominators | closes the quadratic-twist loophole without false injectivity | restriction-zero theorem plus explicit virtual kernel example | B5 |

## Paper storyline

The main paper must prove C1--C4.  The appendix carries the full recurrence
algebra, character reconstruction details, exact replay schema, and optional
full-Fermat-diagonal refinement.  Fixed-prime trace tables, all-\(n\)
smoothness experiments, and global-root speculation are intentionally cut.

## Block B1: universal group enumeration

- **Claim tested:** C1.
- **Why:** a constructed subgroup is not a full stabilizer theorem.
- **Object:** the ideal \((C_n,Q_{n,\rho})\) and all normalized dihedral
  supports.
- **Checks:** derive recurrence; compute the alternating closure sum; enumerate
  all \(q\)-lifts; verify exact support sequence.
- **Controls:** symbolic proof; finite exact scan \(2\le n\le64\); independent
  brute force at \(n=2,3,4\).
- **Success criterion:** exactly \(n\) even rotations, \(n\) odd reflections,
  and three phase lifts per support; total \(6n\).
- **Failure interpretation:** any extra support or missing lift invalidates
  fullness or the proposed presentation.
- **Paper target:** main group theorem and Appendix A.
- **Priority:** MUST-RUN.

## Block B2: rational group form

- **Claim tested:** C1's rational-form component.
- **Why:** Galois does not fix the geometric automorphisms individually.
- **Object:** \(M_n,r,s\) over \(K/\mathbf Q\).
- **Checks:** recompute \(\delta(r),\delta(s)\); verify \(\delta^2=1\);
  solve fixed-point congruences; distinguish Reynolds and transfer.
- **Controls:** exactly two fixed elements for \(2\le n\le256\).
- **Success criterion:** rank \(6n\), two rational geometric elements, all
  \(6n\) graphs in the Reynolds sum, transfer denominator two.
- **Failure interpretation:** a constant-group result or denominator merger
  breaks rational descent.
- **Paper target:** rational-form section.
- **Priority:** MUST-RUN.

## Block B3: denominator rigidity

- **Claim tested:** C2.
- **Why:** total rank alone falsely accepts the third row.
- **Object:** ranks \(e_n,o_n\), split trace identity, and fixed-\(\ell\)
  semisimple K0 classes after restriction.
- **Checks:** verify \(o_n=2(e_n-3)\); derive \(n\mid24\); emit every divisor
  row; construct the direct-copy converse.
- **Controls:** scan \(2\le n\le512\); mandatory negative control collapsing
  the weights, which must falsely accept \(n=3\) and therefore be rejected.
- **Success criterion:** survivors exactly `[2, 4]` on separate rails; full
  local logarithm matched in the converse.
- **Failure interpretation:** an extra survivor signals rank arithmetic or
  scope corruption; a rejected \(n=4\) signals the rational exponent was
  mis-normalized.
- **Paper target:** central arithmetic theorem and main table.
- **Priority:** MUST-RUN.

## Block B4: exact third-row character

- **Claim tested:** C3.
- **Why:** a central source projector might in principle isolate integral
  multiplicities even when whole-rail ranks fail.
- **Object:** \(G_3=\operatorname{Dih}(C_9)\), the Cayley quotient
  \(R_{1,-1}\), and the Fermat packet.
- **Checks:** enumerate 18 elements; form 27 monomials and seven relations;
  include \(\det M_g/\det A_g\); verify relation stability and group law;
  reconstruct characters and coefficient-field orbit blocks.
- **Controls:** a scalar-lift mutation, residue-ratio omission, one-trace
  mutation, and illegal splitting of \(U_1,U_2,U_4\).
- **Success criterion:** quotient dimension 20; exact trace vectors and
  decompositions in Theorem D; no nonzero block with both multiplicities
  divisible by three.
- **Failure interpretation:** a character mismatch reopens the projector
  loophole and blocks release.
- **Paper target:** exact equivariant section and Appendix B.
- **Priority:** MUST-RUN.

## Block B5: counterpacket and scope firewall

- **Claim tested:** C4 and all negative claims.
- **Why:** restriction from \(\mathbf Q\) has a nontrivial virtual kernel,
  but that kernel must not be mistaken for a denominator repair.
- **Object:** fixed-\(\ell\), finite-dimensional continuous semisimple
  compatible-system Grothendieck groups, unramified outside a common finite
  set, and the quadratic character \(\chi_{K/\mathbf Q}\).
- **Checks:** encode restriction-zero consequence; exhibit
  \(\mathbf1-\chi_{K/\mathbf Q}\); require the class to be nonzero over
  \(\mathbf Q\) but to have restricted class and rank zero; scan theorem
  vocabulary for forbidden promotions.
- **Success criterion:** actual invisible classes vanish; virtual kernel is
  allowed but cannot alter \(K\)-ranks/isotypes; all exclusion flags remain
  false.
- **Failure interpretation:** claiming restriction injectivity is mathematically
  false; allowing kernel classes to change \(K\)-data invalidates C2--C3.
- **Paper target:** counterpacket and limitations sections.
- **Priority:** MUST-RUN.

## Run order and milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | lock category and source | equation-line and normalization controls | no full-PGL wording | CPU seconds | silent category widening |
| M1 | prove/enforce universal group | B1 plus independent small-row brute force | exact \(6n\) count | CPU minutes | shared recurrence bug |
| M2 | certify rational form | B2 | two rational points in every row | CPU seconds | confusing constant group with group form |
| M3 | certify iff theorem | B3 | survivors `[2,4]`; \(n=3\) total-rank trap rejected | CPU seconds | collapsing weights |
| M4 | close equivariant loopholes | B4 and B5 | exact characters, orbit blocks, kernel caveat | CPU minutes | residue orientation or descent-data error |
| M5 | release hardening | mutations, rollback-atomic exception tests, deterministic replay, manifest | all gates pass | CPU minutes | stale or partially promoted artifacts; no power-loss atomicity claim |

No GPU, external dataset, stochastic seed, or human evaluation is required.

## Risks and mitigations

- **Risk:** “full” is read as full PGL automorphism group.
  **Mitigation:** define `PMonStab` in every theorem-bearing artifact.
- **Risk:** all-\(n\) equation algebra is promoted to all-\(n\) motives.
  **Mitigation:** machine-separate `all_n_equation_theorem`,
  `certified_packet_rows`, and conditional rows.
- **Risk:** a total-rank calculation hides the two-weight obstruction.
  **Mitigation:** mandatory negative control and rail-specific divisibilities.
- **Risk:** the standard Fermat rational form is conflated with the
  \(M_3\)-twisted form.
  **Mitigation:** state the common-group theorem over \(K\), and gate the
  rational twist caveat.
- **Risk:** a split identity is called global.
  **Mitigation:** include the inert polynomial identity and explicit false
  flags for global root, FE, automorphy, and RH.

## Final checklist

- [x] Main theorem claims are explicit and bounded.
- [x] Novelty is isolated from HCS-C53 descent.
- [x] The universal proof is symbolic rather than a finite scan.
- [x] Both pure rails are protected.
- [x] The common-group and counterpacket caveats are explicit.
- [x] Final scoped release-candidate producer/checker hashes are inserted.
- [x] Manuscript is compiled and audited only after hash insertion.
