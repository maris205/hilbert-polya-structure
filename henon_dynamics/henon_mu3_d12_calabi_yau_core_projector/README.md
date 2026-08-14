# HCS-C52: dihedral Chow projector for the fourth Hénon moment

Status: **AMBER B0--B2 theorem package; release candidate**

Implementation commit: `208feef86365cd92ace8dad02904acff6623eeec`.

The mathematical packages, independently checked exact certificate,
manuscript, and Route-A record are present.  The release remains scoped to
the B0--B2 theorem below.

## Source object

Work over

\[
 K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,
\]

with the smooth fivefold inherited from C50--C51,

\[
 X=X_4\subset\mathbf P^7_K,
 \qquad
 C=\sum_{i=0}^{7}x_i^3=0,
 \qquad
 Q=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0=0.
\]

The relevant C51 packet is

\[
 O_4=H^5(X)(2),
\]

whose Hodge types are

\[
 (2,-1)^1+(1,0)^{83}+(0,1)^{83}+(-1,2)^1.
\]

C51 asked for a \(K\)-rational algebraic projector whose realizations are
induced by the same motivic correspondence, separating the rank-two
extreme pair from the rank-166 level-one part.  This does not presuppose a
computed strict compatible system.

## Locked amber theorem narrative

C52 does not promise that full \(2+166\) separation.  Its B0--B2 target is
one coherent dihedral middle-motive decomposition theorem:

1. the projective monomial source stabilizer is
   \[
   G_{\mathrm{mon}}\cong\operatorname{Dih}(C_{12}),
   \qquad |G_{\mathrm{mon}}|=24;
   \]
2. after the algebraic middle Chow--Künneth projector \(\pi_5\), the
   Reynolds graph average cuts out a \(K\)-rational rank-10 middle Chow
   summand and a rank-158 complement;
3. the rank-10 summand has untwisted Hodge ledger
   \[
   (4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1,
   \]
   so after one Tate twist it is of Calabi--Yau-threefold **Hodge type**
   \((1,4,4,1)\);
4. the complement is purely level one after the C51 normalization; and
5. no idempotent in the graph algebra
   \(\mathbf Q[G_{\mathrm{mon}}]\) can improve the split to \(2+166\).

The last statement is optimal only inside the declared graph algebra.  It
does not obstruct every algebraic correspondence.

## Why the middle projector is mandatory

The Reynolds average on all cohomology also retains ambient Tate classes.
With \(h=c_1(\mathcal O_X(1))\) and \(\int_Xh^5=6\), define

\[
 \pi_{2i}=\frac1{6}h^{5-i}\times h^i\quad(0\le i\le5),
 \qquad
 \pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i}.
\]

Define

\[
 e_G=\frac1{24}\sum_{g\in G_{\mathrm{mon}}}[\Gamma_g],
 \qquad
 \pi_{\mathrm{core}}=\pi_5e_G,
 \qquad
 \pi_{\mathrm{lev}}=\pi_5-\pi_5e_G
\]

Only \(\pi_{\mathrm{core}}\) and \(\pi_{\mathrm{lev}}\), after the
middle projector \(\pi_5\), may be assigned the middle ranks \(10\) and
\(158\); the raw Reynolds average \(e_G\) also retains ambient Tate pieces.

## Exact release evidence

Exact enumeration found 24 projective monomial maps with element
orders

\[
 1^1,\ 2^{13},\ 3^2,\ 4^2,\ 6^2,\ 12^4.
\]

The exact Cayley-ring character gives four one-dimensional
multiplicities \((4,1,3,3)\) and five two-dimensional multiplicities
\((7,8,6,8,7)\) in \(H^{3,2}\).  An independent exact checker has
reproduced B0--B2, with \(16/16\) semantic gates and \(44/44\)
mutation/transaction tests passing.  The full-project release manifest is
verified by the default runner.

## Stop/go boundary

- **GO for C52:** B0 source lock, B1 group/Chow identities, and B2 exact
  characteristic-zero representation calculation all pass.
- **STOP:** any mismatch in the group order, residue multiplier, character
  dimensions, projector category, or rank ledger kills the amber theorem.
- **HANDOFF TO C53:** full rank-10 Frobenius polynomials and any incidence
  correspondence beyond the graph algebra.

## Claim firewall

C52 does not claim:

- that \(G_{\mathrm{mon}}\) is the full automorphism group of \(X\);
- a rank-two algebraic projector;
- an actual Calabi--Yau threefold realizing the rank-10 summand;
- automorphy or a functional equation for that summand;
- a new Euler continuation domain;
- a Riemann divisor, RH statement, or Hilbert--Pólya operator;
- failure of all algebraic correspondences.

SOURCE_AUDIT.md records the checked primary locators and the
non-exhaustive novelty boundary.  No absolute novelty claim is authorized.

## Planning files

- `RESEARCH_QUESTION.md` fixes the exact question and theorem scope.
- `METHODOLOGY_BLUEPRINT.md` gives the B0--B2 proof architecture.
- `EXPERIMENT_PLAN.md` specifies exact reproducible controls.
- `IMPLEMENTATION_CHECKLIST.md` records the closed fail-closed release
  gates.
- `PAPER_PLAN.md` maps only the amber theorem to the manuscript.
- `../BATCH_PLAN_C52_C56.md` records the contingent five-paper batch.
- THEOREM_PACKAGE.md, DERIVATION_PACKAGE.md, and PROOF_PACKAGE.md state
  and prove the B0--B2 package.
- SOURCE_AUDIT.md and NARRATIVE_REPORT.md lock the claim firewall.
- paper/ contains the compiled release manuscript.
