# Batch 06 — Paper 23 Candidate Review R1 Family-Sign Correction

## Immutable source binding

This correction is an append-only protocol correction to the immutable review
`BATCH_06_PAPER23_CANDIDATE_REVIEW_R1.md`, bound exactly as follows:

- SHA-256: `a3c9815c2d851c8791a259c4e46a4d33663f06e6ab4faa58a981f89f7ebf3ae7`
- Bytes: `21915`
- LF: `394`
- Candidate ID: `hamiltonian_quartic_spectral_escape_v1`
- Public title: **Four-Mode Hamiltonian Product Shears Beyond Cubic Collapse: Exact Degree Growth and Quartic Perron Subfamilies**

The bound R1 remains immutable. This file corrects only its family-sign specification and the unsupported sign-generalization sentence. Where those two points conflict, this correction is controlling.

## Corrected and frozen candidate family

Let (K) be a field of characteristic zero, let (g\ge10), and set

\[
V_g(q)=q_1^2q_2^2q_3^2q_4^2+q_1^g+q_2^{g-1},
\]

\[
W_g(p)=p_1^2p_2^2p_3^2p_4^2+p_3^{g-1}+p_4^g.
\]

The candidate is frozen to the **two-phase positive-sign** shears

\[
S_{V_g}^{+}(q,p)=(q,p+\nabla V_g(q)),
\qquad
T_{W_g}^{+}(q,p)=(q+\nabla W_g(p),p),
\]

in the exact composition order

\[
\boxed{F_g=T_{W_g}^{+}\circ S_{V_g}^{+}.}
\]

Thus the first phase updates (p) by addition of (\nabla V_g(q)), and the second phase updates (q) by addition of (\nabla W_g) evaluated at the updated (p).

The minus-sign first shear printed in the bound R1 is not the frozen candidate family. It is corrected here to (p+\nabla V_g(q)).

## Explicit withdrawal of the sign-generalization sentence

The bound R1's statement that changing standard shear signs does not change the degree calculation is withdrawn in full as an authorization or theorem claim. It must not be cited to replace a no-cancellation proof, to change either phase's sign, or to enlarge the candidate family.

In particular, this R1 gate does **not** cover:

- (S(q,p)=(q,p-\nabla V_g(q)));
- (T(q,p)=(q-\nabla W_g(p),p));
- simultaneous subtraction in both phases;
- independently chosen or parameter-dependent signs;
- arbitrary signed coefficients in either potential;
- any positive-characteristic field.

Each such variant is an anti-claim unless it receives a separate exact-degree, no-cancellation, field-boundary, novelty, and protocol review.

## Positive-sign no-cancellation certificate

For the corrected family, no-cancellation is supported directly by coefficient positivity rather than by an unproved sign-invariance assertion.

The gradient components are

\[
\begin{aligned}
\partial_{q_1}V_g&=2q_1q_2^2q_3^2q_4^2+gq_1^{g-1},\\
\partial_{q_2}V_g&=2q_1^2q_2q_3^2q_4^2+(g-1)q_2^{g-2},\\
\partial_{q_3}V_g&=2q_1^2q_2^2q_3q_4^2,\\
\partial_{q_4}V_g&=2q_1^2q_2^2q_3^2q_4,
\end{aligned}
\]

and

\[
\begin{aligned}
\partial_{p_1}W_g&=2p_1p_2^2p_3^2p_4^2,\\
\partial_{p_2}W_g&=2p_1^2p_2p_3^2p_4^2,\\
\partial_{p_3}W_g&=2p_1^2p_2^2p_3p_4^2+(g-1)p_3^{g-2},\\
\partial_{p_4}W_g&=2p_1^2p_2^2p_3^2p_4+gp_4^{g-1}.
\end{aligned}
\]

All displayed coefficients are positive integers. Starting from the coordinate polynomials, whose coefficients are (0) or (1), every coordinate of (S_{V_g}^{+}), (T_{W_g}^{+}), and every iterate (F_g^n) is obtained using only addition and multiplication of polynomials with nonnegative integer coefficients. Inductively, every monomial coefficient in every iterate lies in (\mathbf Z_{\ge0}).

If several substitution paths produce the same monomial, their contributions add to a positive integer; no contribution is subtracted. Because (K) has characteristic zero, the canonical image of every positive integer in (K) is nonzero. Therefore neither a selected leading monomial nor a tied contribution can disappear by coefficient cancellation in the corrected positive-sign family.

This argument is specific to the frozen coefficient/sign pattern. In positive characteristic, coefficients (2), (g), or (g-1), or sums of positive integer contributions, can vanish modulo the characteristic. Positive characteristic therefore remains outside the theorem.

## Degree data unchanged under the corrected family

The correction changes the erroneous family description, not the exponent supports used by the accepted positive-sign candidate. Put

\[
h=g-1,\qquad k=g-2.
\]

The selected first- and second-phase exponent matrices remain

\[
A_g=
\begin{pmatrix}
h&0&0&0\\
0&k&0&0\\
2&2&1&2\\
2&2&2&1
\end{pmatrix},
\qquad
B_g=
\begin{pmatrix}
1&2&2&2\\
2&1&2&2\\
0&0&k&0\\
0&0&0&h
\end{pmatrix}.
\]

Their exact product remains

\[
C_g=B_gA_g=
\begin{pmatrix}
h+8&2k+8&6&6\\
2h+8&k+8&6&6\\
2k&2k&k&2k\\
2h&2h&2h&h
\end{pmatrix}.
\]

The four selector wall functionals remain

\[
\begin{aligned}
L_1(u)&=ku_1-2u_2-2u_3-2u_4,\\
L_2(u)&=-2u_1+(k-1)u_2-2u_3-2u_4,\\
L_3(u)&=-8u_1-6u_2+(g-7)u_3+(2g-8)u_4,\\
L_4(u)&=-6u_1-4u_2+(2g-6)u_3+(g-6)u_4.
\end{aligned}
\]

At the ordinary seed, their phase-correct strict margins remain

\[
g-8,\qquad g-9,\qquad 3g-29,\qquad 3g-22.
\]

They are (2,1,1,8) at (g=10), while at (g=9) they are (1,0,-2,5). Hence the accepted (g\ge10) selector threshold is unchanged.

The invariant-cone proof obligation is unchanged: the eventual manuscript must provide a symbolic certificate that its cone contains the ordinary seed, that all four walls are strict there, and that (C_g\mathcal K\subseteq\operatorname{int}\mathcal K) for every (g\ge10). The positive-sign certificate above removes coefficient cancellation as a competing failure mode; it does not replace the cone inequalities.

The first (q)-degree vector remains

\[
C_g\mathbf1=(3g+23,\ 3g+24,\ 7g-14,\ 7g-7)^T,
\]

so first-step (q_4) visibility is unchanged. The all-iterate claim

\[
\deg(F_g^n)=e_4^TC_g^n\mathbf1
\]

retains exactly the same symbolic invariant-cone and visibility proof obligation as in the bound R1.

## Characteristic polynomial and modular certificate unchanged

The corrected positive signs do not alter (C_g). Its characteristic polynomial remains

\[
\boxed{
\begin{aligned}
\chi_{C_g}(t)
={}&t^4-(4g+10)t^3+(-2g^2-26g+45)t^2\\
&+(12g^3-70g^2+126g-72)t
+9(g-1)^2(g-2)^2.
\end{aligned}}
\]

For (g\equiv3\pmod5), it still reduces to

\[
t^4+3t^3+4t^2+1.
\]

Its values at (0,1,2,3,4) remain (1,4,2,4,3), so it has no linear factor. The bound R1's hand calculation excluding a product of two monic quadratics is unaffected. Thus the reduction is irreducible over (\mathbf F_5), the integer characteristic polynomial is irreducible over (\mathbf Q), and the positive Perron root has algebraic degree four for (g=13,18,23,\ldots).

Because (C_g) is strictly positive for (g\ge10), the Perron–Frobenius conclusion is unchanged once the exact positive-sign degree recurrence and (q_4) visibility are proved.

## Scores, search, and collision conclusions unchanged

The correction narrows the reviewed object to the originally frozen positive-sign candidate and supplies the missing coefficientwise no-cancellation reason. It does not introduce a new candidate, source, theorem, or portfolio claim. The R1 scores therefore remain:

| Dimension | Corrected R1 score | Gate |
|---|---:|---|
| Novelty / portfolio differentiation | **7.8 / 10** | PASS |
| Standalone-paper potential | **8.3 / 10** | PASS |
| Proof plausibility | **9.1 / 10** | PASS |

The six bounded public-search batches and 24 exact queries recorded in the bound R1 remain the complete R1 query log. All source URLs, arXiv/DOI identifiers, access-level labels, cutoff (2026	ext{-}08	ext{-}24) UTC, omission boundaries, and nonpriority wording remain unchanged.

The collision conclusions also remain unchanged:

- Papers 12–19 have no direct theorem collision with the frozen four-mode positive-sign family.
- Papers 20–22 share the selector-to-matrix-to-Perron proof grammar.
- Paper 22 remains the closest internal neighbor because its common unit sector causes cubic spectral collapse.
- Support-rank and common-kernel reasoning remain explanatory and explicitly nonnovel.
- Blanc–van Santen remains the general weak-Perron realization neighbor.
- Shao–Sun remains the recent affine-triangular degree-four neighbor at abstract/metadata access level.
- The bounded search found no direct match to the complete positive-sign four-spike (BA)/visibility/quartic/modulo-(5) package, but establishes no absolute priority.

The standalone 26-content-page plan and all original STOP conditions remain in force.

## Corrected anti-claims and release boundary

In addition to the bound R1 anti-claims, the manuscript must now state unambiguously that:

1. the theorem concerns exactly (S_{V_g}^{+}), followed by exactly (T_{W_g}^{+});
2. subtraction variants and arbitrary sign variants are not covered;
3. no degree invariance under sign changes is asserted;
4. coefficientwise no-cancellation is proved only from the frozen positive integer coefficients and the characteristic-zero field;
5. positive-characteristic variants are not covered;
6. any future change to a sign, coefficient pattern, phase order, or field requires a new exact proof and a new review rather than an editorial substitution.

Writing or release must STOP if the family is printed with a minus sign, if (F_g) is composed in the opposite order, or if the positive-coefficient induction is replaced by an unsupported statement that signs do not matter.

This correction creates no Paper 23 project, changes no original review or ledger, and has no external effect.

PAPER23_CANDIDATE_GATE_PASS_R1_CORRECTED
