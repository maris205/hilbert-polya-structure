# Paper Plan

## Working title

**Tensor-Atom Exterior Transfer for Full Shifts: Möbius Supertrace and a
Critical-Strip Obstruction**

## One-sentence contribution

Tensor-factorization homology canonically fixes the Euler orientation of the
SD-C07 transfer object in \(\Re s>1\), but natural symbolic reversal,
group inversion, and the first critical-strip Schatten regularization all
fail to produce the completed Riemann divisor.

## Paper type and scope

- Type: concise theory paper with exact computational certificates.
- Main system family: Symbolic Dynamics only.
- Target length: about 10 A4 pages through the conclusion, plus references
  and a compact proof/scope appendix.
- Review loop: omitted by explicit project directive.
- Candidate policy: retain SD-C07; do not assign SD-C08.

## Claims--evidence matrix

| Claim | Evidence | Main location |
|---|---|---|
| Factorization homology gives \(\mu\) and odd atoms | crosscut proof, exact \(N\le512\) audit | Sections 3 and 7 |
| Exterior transfer fixes determinant orientation | Fredholm/Berezinian theorem, coefficient ledger | Section 4 |
| Honest Koszul lift cancels to vacuum | equivariant chain calculation | Section 5 |
| Natural dualities miss \(1-s\) | reversal and group-completion propositions | Section 6 |
| First shared Schatten regularization destroys low traces | \(\mathcal S_q\) theorem and \(\det_3\) expansion | Section 6 |
| No A3 upgrade | G4 audit and absent Gamma/continuation | Section 8 |

## Section plan

1. **Abstract.** Positive A2 theorem, strongest obstruction, \(N=512\)
   exact result, and explicit no-RH boundary.
2. **Introduction.** Start from Paper04's A0--A2 chain, state the orientation
   and completion questions, preview the asymmetric outcome, show Figure 1.
3. **Related work and claim boundary.** Exterior automata, signed symbolic
   homology, divisor Möbius topology, and regularized determinants.
4. **Tensor-divisor factorization homology.** Full-shift monoid, crosscut
   theorem, atom parity, homological supertrace.
5. **Exterior transfer and Koszul cancellation.** Keep the zero-differential
   exterior module, odd Berezinian, and honest Koszul resolution separate.
6. **Three duality tests.** Stable/unstable reversal, group completion, and
   adversarial paired \(\det_3\).
7. **Exact experiment and controls.** \(N=512\), parity controls, shifted/
   additive/free-mixing controls, finite dual-phase drift.
8. **Route-A outcome and next conjecture.** G0--G4 table, no SD-C08, bold
   symbolic half-density hypothesis.
9. **Conclusion.** A2 orientation solved; A3 completion isolated.
10. **Appendix.** Proof details, experimental protocol, and scope audit.

## Figure plan

| ID | Type | Content | Source | Priority |
|---|---|---|---|---|
| Figure 1 | Pure TikZ hero map | SD-C07 source branching into exterior success, reversal failure, group-inversion failure, and adversarial \(\det_3\) stop | figures/grading_duality_map.tex | HIGH |
| Table 1 | Theorem comparison | exterior module vs honest Koszul vs reversal vs group completion vs \(\det_3\) | manual LaTeX | HIGH |
| Table 2 | Exact controls | canonical and adversarial finite metrics | results/summary.json | HIGH |

## Figure 1 caption draft

Starting from the same tensor-prime full-shift source, the exterior branch
fixes the determinant orientation in the Euler half-plane. Natural symbolic
reversal preserves \(s\), while group inversion sends \(s\) to \(-s\).
Even after granting a target-centered half-density, the first paired
regularized determinant is zero-free and deletes repetitions \(r=1,2\).
Thus the stage reaches A2 but stops at A3.

## Citation plan

- Introduction: Paper04 full-shift/tensor background; Bowen--Lanford.
- Related work: Béal; Putnam; Deeley; Rota; Priddy; Proietti--Yamashita.
- Duality: Kim--Lee--Park; Kaminker--Putnam.
- Regularization background: Ruelle's Fredholm extension.

Every bibliography entry is fetched or verified from a primary publication
record. No citation is generated from memory alone.

## Writing policy

The paper treats the positive construction boldly but keeps determinant
types separate. It does not call the exterior transfer object a nontrivial
Koszul homology, does not import zeta continuation, and does not promote a
finite symmetry or regularized no-go into Route-A credit.
