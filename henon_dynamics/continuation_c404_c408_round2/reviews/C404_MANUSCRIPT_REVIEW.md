# C404 independent internal manuscript review

Date: 2026-09-06. Reviewer: coordinating agent `/root`, not the author
of the C404 proof package or manuscript. The existing non-author proof
review is `wild_dynamics/CROSS_REVIEW_HENON_RESONANCE.md`; this review
checks the actual newly typeset article, not only that earlier report.

Disposition: **0 blocking mathematical defects; 0 required manuscript
corrections; 0 open actionable citation issues**. No rewrite was made
merely to create a revision history. Final deterministic rebuilding and
all-page visual QA are separate, still-required release gates.

## Actual material read and version binding

All 772 lines of the eleven author inputs were read: `main.tex`,
`math_commands.tex`, `references.bib`, abstract and sections 1--7.
The complete manuscript source-verification record, initial-build
receipt, source audit and bounded exact-check receipt were also read.
This includes the actual full proof, all four bibliography entries and
all five citation contexts; it is not an abstract-level review.

The eleven inputs are bound by `henon_resonance/paper/SOURCE_INPUTS.sha256`,
whose SHA-256 is

    9194635d7564b1762efdf781a68a2a282e30a0598131fb86ad8d1adfda347f8d

The coordinator ran `sha256sum -c SOURCE_INPUTS.sha256` in the paper
directory: all eleven entries OK, exit 0. The reviewed initial PDF is
10 pages, SHA-256

    99c58e5805bb4e5b70e5f86505dc60dd8f79df76ea0011ac901127456e10a3cc

This hash identifies the draft; it is not substituted for a proof check.
`SOURCE_VERIFICATION.md` is bound to
`22956080ca09717e88b3fbfa6084c0c9fefa0715df4ac862b278428c46bed5d3`.
The initial compile receipt is bound to
`e8f4b2ff1643a691860497fd6a356f2e50c8a6215304ee2d269e7ac09514ee3b`.

## Mathematical claim audit

| Actual claim | Verification and boundary |
|---|---|
| Full coefficient/period family | Theorem 1.1 explicitly retains coefficients in F_q, a nonzero, 2<=m<q and p not dividing m; no hidden monicity assumption on g. |
| One dynamical owner | The inverse formula and commutation imply S^n=H^{-n}Phi^n; postcomposition by H^n identifies the equalizer schemes, not just point sets. |
| Operator algebra | T and U act on F_q[x,y]; U(f)=f^q is not extended incorrectly to arbitrary algebraic-closure coefficients. Delta is only a linear operator. |
| One-step leading term | Lower-degree input terms have substituted degree at most q(D-1); the first binomial term is strictly higher and nonzero. |
| Entire p-tower | D_j remains congruent to m modulo p, so induction applies at every level. The coefficient b^j mbar^(j-1) is preserved correctly. |
| General period | The commuting-operator factorization has exactly s noncanceling equal-degree terms; integer degrees and residue-field scalars are distinguished. |
| Finite quotient | Actual graded leading monomials x^(q^n), y^d are coprime; the explicit S-polynomial standard representation and rectangle basis give the full length. |
| Infinity and reducedness | The two actual leading forms have no common projective point, and the literal Jacobian determinant is a^n. Ordinary geometric points are therefore justified. |
| Zeta product | The telescoping divisibility identity, absolute interchange bound and locally uniform logarithmic convergence have the correct signs and exponents. |
| Every positive power | Dominated convergence gives the fractional radial order sigma_a; M sigma_a lies strictly between zero and one for all sufficiently high levels. Dense such roots exclude meromorphic continuation across any arc. |
| Nonalgebraicity | A square-free algebraic equation has only finitely many finite singular/branch locations, incompatible with the proved natural boundary. |
| Direct vector-group exclusion | A finite subgroup of an additive vector group has p-power size, while N_1=qm does not. The manuscript explicitly leaves finite quotients and other groups unclassified. |
| Out-of-hypothesis example | The characteristic-two literal expansion has unique degree 44, first equation degree 64 and nonzero Jacobian. The stated 2816 versus 2944 discrepancy follows without extrapolation. |
| Finite evidence | All five table rows and their coefficient fields match the archived receipt. F4 arithmetic is not Z/4Z; the absent secondary extension-field Groebner run is explicitly disclosed. |

The conclusion excludes only a finite product/quotient of polynomial
characteristic-zero determinants for this exact nonrational zeta. It
does not claim to exclude all infinite-dimensional realizations or
arbitrary changes of variable.

## Source ownership and actual citations

The four entries and five uses match the scoped source records:
algebraic-group dynamics owns the general distorted-count mechanism;
Bridy's cited results are one-dimensional; dynamically affine and
Kummer results are not applied to an unconstructed quotient; Cox--Little--
O'Shea is a classical polynomial-ideal pointer with the special argument
written in the article. The new 2020 incollection metadata is explicitly
separated from the actually read 2019 arXiv v1 theorem locators. No
unread publisher text is represented as inspected. The book's complete
chapter was not obtained, and no invented page locator is given.

The source check is bounded, not a global novelty certificate. The
paper's own claimed increment remains the nonlinear coefficient-uniform
all-period calculation. The zeta corollary is not a second paper.

## Reverse outline and scope adjudication

The abstract and first theorem state the result before the technical
lemmas. Sections 2--4 establish the owner, leading terms and ordinary
count; section 5 proves the analytic consequence; section 6 gives
controls and exclusions; the conclusion states remaining questions
and reproducibility. Every substantive claim in the abstract has its
full proof in the PDF source. There is no reliance on a missing appendix
or a table as evidence for an infinite theorem.

Native S-periods are not ordinary H-periods or Hasse--Weil counts of
a fixed variety. No rational-prime owner, target Euler factor, root
number, automorphy statement, target zero match or Hilbert--Polya
operator is claimed. The anonymous/AI/internal-review disclosure does
not fabricate institutional or human-peer-review provenance.

The `research-review` framework is used with the current team's
internal non-author review under the repository's pure-mathematics
workflow. No old prescribed model, external review API, ML score,
GPU experiment or fixed rewrite quota was used. Mathematical/source
review is complete for this unchanged draft. Final byte reproducibility,
fonts/text and every-page visual inspection remain separate evidence.
