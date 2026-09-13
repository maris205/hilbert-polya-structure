# Paper Plan

**Title**: Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies  
**Author**: Anonymous  
**Type**: proof-first mathematics / algebraic-dynamics theory  
**Date**: 2026-08-22  
**Page contract**: 26.0 substantive pages target; hard band 24–29 pages from Abstract through Conclusion, excluding references and any appendix  
**Section count**: 8 main sections after the abstract (§0 is separate and not counted in the 8)

## Claims-Evidence Matrix

| Claim id | Locked claim | Proof ledger location | Permitted qualifier |
|---|---|---|---|
| T0 | Main theorem: fixed family \(F_g=T\circ S\) on \(\mathbb A^6\), exact degree recurrence, \(\lambda_1(F_g)=\rho(C_g)\), and cubic Perron subfamilies | §1.2–§1.3, §§3–7, §8.3 | Only for algebraically closed \(K\) of characteristic zero, integer \(g\ge 8\), and the fixed displayed potentials; no genericity, priority, or classification language |
| L1 | \(S\) and \(T\) are polynomial automorphisms with subtraction inverses; the six-by-six Jacobian blocks preserve the standard symplectic form | §3.1–§3.3 | Formal identity for the displayed maps; the inverse and symplecticity check is independent of the degree induction |
| L2 | The complete six-row \(\mathbb N^6\) support ledger yields the displayed \(A_g\) matrix | §3.4 | Use only the frozen six-coordinate monomials; no omitted support rows |
| L3 | Exactly two selector gaps occur: \(M_S=g-2-2x-2y\) and \(M_T=(2g-6)x+(g-6)y-6\); no third face appears | §4.1 | On the cone \(x,y\ge 1\), \(x+y<(g-3)/2\), with \(g\ge 8\) |
| L4 | \(C_g=B_gA_g\) preserves the cone by the exact normalized tests \(X'-1\), \(Y'-1\), \(H_2=2H\) with the \(g=8,\dots,11\) vs. \(g\ge 12\) split | §4.2–§4.3 | No numerical sampling; all cone checks stay symbolic |
| L5 | The phase/carry induction gives \(v_{n+1}=A_g u_n\) and \(u_{n+1}=C_g u_n\), with positive characteristic-zero semiring no-cancellation | §5.1–§5.4 | Characteristic zero only; no positive-characteristic specialization or half-step matrix drift |
| L6 | \(C_g-A_g\) is entrywise positive, \(q_3\) is visible, and \(\deg(F_g^n)=e_3^{\mathsf T}C_g^n\mathbf 1\) for \(n\ge 0\) | §6.1–§6.2 | Visible coordinate is \(q_3\) only; no max-over-rows shortcut |
| L7 | Perron-Frobenius gives \(\lambda_1(F_g)=\rho(C_g)\), and the row-sum bound yields \(\rho(C_g)<(g-1)^2\) | §6.3 | Positive primitive matrix only; bound is strict for \(g\ge 8\) |
| L8 | \(\chi_{C_g}(t)\) has the stated form, and the mod-5 no-root table gives the cubic Perron subfamilies for residues \(2,3,4\) | §7.1–§7.3 | Arithmetic corollary only; no global priority, genericity, or entropy claim |
| L9 | \(g=7\) is a strict-cone boundary with no selector tie, and the Papers 12–20 collision/limitations statement is bounded | §8.1–§8.3 | Boundary anti-example only; novelty wording stays local and bounded |

Proof order is locked: L1 \(\rightarrow\) L2 \(\rightarrow\) L3 \(\rightarrow\) L4 \(\rightarrow\) L5 \(\rightarrow\) L6 \(\rightarrow\) L7 \(\rightarrow\) L8 \(\rightarrow\) L9. The manuscript must not reorder these steps.

## Structure

### §0 Abstract — 0.5 pp
- Goal: state the exact family, the exact degree recurrence, the Perron root conclusion, and the cubic Perron subfamily corollary in one self-contained paragraph.
- Must mention the fixed three-mode Hamiltonian shear family in \(\mathbb A^6\), the exact degree identity \(\deg(F_g^n)=e_3^{\mathsf T}C_g^n\mathbf 1\), and the \(\rho(C_g)\) conclusion.
- Must not mention genericity, priority, entropy, periodic points, or empirical evidence.
- Transition: end by promising a proof ledger, not a heuristic story.

### §1 Introduction — 3.0 pp
- Goals:
  - open with the exact family \(F_g=T\circ S\) and the problem of exact degree growth;
  - say why canonical Hamiltonian shears are narrower than the broader affine-triangular class;
  - state the main theorem in full before any related-work context.
- Required content:
  - the potentials \(V=q_1^2q_2^2q_3^2+q_1^g\) and \(W=p_1^2p_2^2p_3^2+p_3^g\);
  - the headline matrices \(A_g\), \(B_g\), \(C_g=B_gA_g\);
  - a short preview of the cone/selector/induction/spectral chain.
- Order of claims in text:
  - theorem statement;
  - the four proof phases;
  - the precise scope exclusions.
- Proof-vs-appendix decision: all of this stays in the main body; no appendix material is needed here.
- Narrative transition: after the theorem box, the paper freezes terminology and collision boundaries.

### §2 Bounded related work, collision screen, and terminology — 2.0 pp
- Subsections:
  - §2.1 context-only citation paragraph with exactly two verified references;
  - §2.2 bounded collision screen against Papers 12–20;
  - §2.3 canonical vs. affine-triangular terminology boundary.
- Goals:
  - define the comparison class only as context;
  - state that the novelty claim is local and bounded to the locked internal screen;
  - make the anti-claim list visible before the proof starts.
- Proof-vs-appendix decision: the collision table stays in the main body because it constrains the claim wording; no appendix move.
- Narrative transition: once the scope is frozen, the manuscript can state the exact family and its gradients.

### §3 Exact family, gradients, inverses, symplectic blocks, and support ledger — 4.5 pp
- Subsections:
  - §3.1 notation in \(\mathbb A^6\), the two potentials, and the maps \(S,T,F_g\);
  - §3.2 explicit gradients and subtraction inverses;
  - §3.3 six-by-six Jacobian block form with \(H_V\) and \(H_W\) at the intermediate \(P\);
  - §3.4 complete \(\mathbb N^6\) support ledger and the \(A_g,B_g\) matrices.
- Required equations:
  - the full gradient rows for \(\nabla V\) and \(\nabla W\);
  - the inverse formulas \(S^{-1}(q,p)=(q,p-\nabla V(q))\) and \(T^{-1}(q,p)=(q-\nabla W(p),p)\);
  - the block Jacobians \(J_S\), \(J_T\), and the symplectic identity \(J^\mathsf T\Omega J=\Omega\);
  - the six-row support table and the exact order \((q_1,q_2,q_3,p_1,p_2,p_3)\).
- Theorem/lemma order:
  - L1 first;
  - then L2;
  - no selector discussion before the support ledger is frozen.
- Proof-vs-appendix decision: none of L1-L2 may be moved out of the main body.
- Narrative transition: after the support rows are frozen, the only remaining issue is which faces win on the cone.

### §4 Selector gaps and cone invariance — 5.0 pp
- Subsections:
  - §4.1 derive exactly the two selector gaps \(M_S\) and \(M_T\) and explicitly rule out a third face;
  - §4.2 derive \(C_g=B_gA_g\) and the normalized tests \(X'-1\), \(Y'-1\), \(H_2=2H\);
  - §4.3 prove the two-case split \(8\le g\le 11\) versus \(g\ge 12\);
  - §4.4 record the \(g=7\) boundary audit as a non-tie.
- Required equations:
  - \(M_S=g-2-2x-2y\);
  - \(M_T=(2g-6)x+(g-6)y-6\);
  - \(X'-1\), \(Y'-1\), and \(H_2=2H\);
  - the exact cone \(x,y\ge 1\), \(x+y<(g-3)/2\).
- Theorem/lemma order:
  - L3 first;
  - then L4;
  - the boundary note comes after the cone proof, not before.
- Proof-vs-appendix decision: these selector and cone arguments must stay visible in the main body; no appendix deferral.
- Narrative transition: once the cone is invariant, the phase-labeled carry induction can close without accidental old-term ties.

### §5 Phase/carry induction and characteristic-zero no-cancellation — 5.0 pp
- Subsections:
  - §5.1 define \(u_n\) and \(v_{n+1}\) as phase-labeled degree/support vectors;
  - §5.2 prove \(v_{n+1}=A_g u_n\) and \(u_{n+1}=C_g u_n\);
  - §5.3 state the characteristic-zero positive-semiring no-cancellation lemma;
  - §5.4 show old-term dominance and exclude any half-step matrix drift.
- Required equations:
  - \(v_{n+1}=A_g u_n\);
  - \(u_{n+1}=C_g u_n\);
  - the carried-term inequalities used to show strict dominance;
  - the semiring statement that selected coefficients stay positive and cannot cancel in characteristic zero.
- Theorem/lemma order:
  - L5 is the whole section;
  - no degree identity yet, only the exact recurrence and the no-cancellation mechanism.
- Proof-vs-appendix decision: all induction and semiring steps remain in the main body; appendix is forbidden for theorem-critical content.
- Narrative transition: after uniqueness and no-cancellation are fixed, visibility turns growth into an exact degree row.

### §6 Visibility, exact degree, and Perron bound — 3.5 pp
- Subsections:
  - §6.1 prove \(C_g-A_g\) is entrywise positive and isolate \(q_3\) visibility via \(U_3-U_2\) and \(U_3-U_1\);
  - §6.2 state and prove \(\deg(F_g^n)=e_3^{\mathsf T}C_g^n\mathbf 1\) for \(n\ge 0\);
  - §6.3 apply Perron-Frobenius and the row-sum bound to get \(\rho(C_g)<(g-1)^2\).
- Required equations:
  - \(C_g-A_g\);
  - the two visibility inequalities for \(U_3-U_2\) and \(U_3-U_1\);
  - the exact degree identity;
  - the row sums \(g+19\), \(2g+13\), \(5(g-1)\).
- Theorem/lemma order:
  - L6 first;
  - then L7.
- Proof-vs-appendix decision: the exact degree identity and the PF bound stay in the main text; no appendix rescue.
- Narrative transition: once the visible row is certified, the remaining algebra is the cubic characteristic polynomial and its residue test.

### §7 Characteristic polynomial and mod-5 cubic Perron subfamilies — 1.5 pp
- Subsections:
  - §7.1 display \(\chi_{C_g}(t)\);
  - §7.2 present the mod-5 no-root table for residues \(2,3,4\) and invoke Gauss’s lemma;
  - §7.3 explain that “cubic Perron” refers only to the degree-three algebraic-integer Perron root in those subfamilies.
- Required equations:
  - \(\chi_{C_g}(t)=t^3-(2g+11)t^2+(g^2-16g+19)t-9(g-1)^2\);
  - the residue table and the no-root check.
- Theorem/lemma order:
  - L8 is the entire section.
- Proof-vs-appendix decision: the residue table must appear in the main text because it is the checkable input to the corollary; appendix is optional only for redundant line-by-line arithmetic.
- Narrative transition: after the algebraic corollary, the paper closes with the boundary audit, bounded novelty statement, and explicit limits of scope.

### §8 Boundary audit, limitations, anti-claims, and conclusion — 1.0 pp
- Subsections:
  - §8.1 record the exact \(g=7\) boundary wording: strict-cone boundary, no selector tie;
  - §8.2 state the limitations and hard anti-claims;
  - §8.3 deterministic handoff and next-stage permissions.
- Required content:
  - the \(g=7\) audit must say the seed sits on the boundary and that the S gap is positive;
  - the Papers 12–20 collision wording must remain bounded and local;
  - the conclusion must restate the theorem without broadening it.
- Theorem/lemma order:
  - L9 closes the proof ledger;
  - then the conclusion.
- Proof-vs-appendix decision: no theorem-critical content is allowed outside the main body; if a typesetting appendix exists, it may only repeat redundant arithmetic.
- Narrative transition: the paper ends by re-stating the exact theorem and then stopping.

### Page-feasibility check

Allocated pages sum to 26.0:

- §0 Abstract — 0.5
- §1 Introduction — 3.0
- §2 Bounded related work, collision screen, and terminology — 2.0
- §3 Exact family, gradients, inverses, symplectic blocks, and support ledger — 4.5
- §4 Selector gaps and cone invariance — 5.0
- §5 Phase/carry induction and characteristic-zero no-cancellation — 5.0
- §6 Visibility, exact degree, and Perron bound — 3.5
- §7 Characteristic polynomial and mod-5 cubic Perron subfamilies — 1.5
- §8 Boundary audit, limitations, anti-claims, and conclusion — 1.0

This is within the locked 24–29 page band and targets the center of the range.

## Collision, novelty, and anti-claim policy

- Novelty wording is bounded to the local internal collision screen against Papers 12–20 only.
- If any collision were found later, the wording changes; the theorem does not.
- The manuscript must not claim:
  - genericity, arbitrary dimensions/supports/words/coefficients, or positive characteristic;
  - entropy, topological entropy, arithmetic entropy, periodic-point counting, trace/multiplier theory, torus, conjugacy, or classification results;
  - universal non-conjugacy, absolute novelty, firstness, priority, or optimality;
  - CAS output, numerical output, datasets, experiments, or empirical evidence as proof.
- The canonical Hamiltonian gradient shear class must remain distinct from the broader affine-triangular class.

## Visual / table plan

No figures. No plots. No hero graphic. This is a proof-first paper; tables are used only as proof ledgers.

Tables to include in the manuscript:

| Table | Purpose | Status |
|---|---|---|
| Claims-Evidence Matrix | Lock each theorem claim to its proof ledger location and qualifier | main body |
| Support-row ledger | Record the six gradient/support rows and the \(A_g,B_g\) transfer | main body |
| Selector / cone ledger | Show the exact two selector gaps and the cone split | main body |
| Collision / anti-claim ledger | Record the bounded Papers 12–20 screen and the forbidden wording | main body |
| Mod-5 residue table | Audit the cubic Perron subfamilies via the no-root check | main body |

No empirical visuals, no architecture figure, and no data panel should appear.

## Citation plan

Exactly two bibliography entries are authorized, both for terminology and context only:

| Citation | Verified record | Allowed role | Forbidden role |
|---|---|---|---|
| Blanc–van Santen | arXiv:1912.01324, *Dynamical degrees of affine-triangular automorphisms of affine spaces* | one sentence defining the larger affine-triangular comparison class | proof of the Paper 21 theorem, priority, genericity, or classification |
| Shao–Sun | arXiv:2509.14584, *Dynamical degrees of affine-triangular automorphisms in dimension four* | one sentence noting dimension-four algebraic-degree context | proof of the Paper 21 theorem, priority, genericity, or classification |

The bibliography must contain only these two citations. No other source is authorized in the manuscript plan.

## Proof-page feasibility and theorem-drift checklist

The manuscript is feasible if, and only if, the following stays true while drafting:

- [ ] The exact title remains unchanged.
- [ ] The paper stays on the fixed family \(F_g=T\circ S\) in \(\mathbb A^6\).
- [ ] The proof order remains L1 through L9.
- [ ] The selector ledger stays exactly two-faced.
- [ ] The cone proof stays symbolic and uses the \(g=8,\dots,11\) / \(g\ge 12\) split.
- [ ] The phase induction keeps \(v_{n+1}=A_g u_n\) and \(u_{n+1}=C_g u_n\) visible.
- [ ] The exact degree identity stays \(e_3^{\mathsf T}C_g^n\mathbf 1\); no alternative observable is introduced.
- [ ] The \(g=7\) note stays a boundary anti-example, not a selector tie.
- [ ] The mod-5 corollary stays arithmetic only.
- [ ] No genericity, positive characteristic, entropy, periodic, trace, torus, conjugacy, classification, or priority claim appears anywhere.
- [ ] No CAS, numerical, dataset, figure, or experiment language appears anywhere.
- [ ] No theorem-critical proof is pushed into an appendix.

## Deterministic writing and next-stage permissions

Handoff protocol:

1. Freeze this plan as the only author-written artifact in this stage.
2. Draft the manuscript section-by-section in the locked order above.
3. Keep every theorem-critical step in the main body.
4. Stop after the first clean full draft; do not expand scope.

Next-stage permissions:

- allowed after an independent plan review only: manuscript drafting that follows this plan exactly;
- not allowed from this stage: manuscript file creation, bibliography expansion, figures, code, experiments, datasets, CAS runs, builds, uploads, transport, or publication.

This plan is a writing contract, not a manuscript.
