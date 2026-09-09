# R9 E4 — integral coordinate interface and local-tameness source check

2026-09-10 UTC. Internal nonauthor reviewer: `/root/c429_e4_cover_review`.

Reviewed all 212 lines of [C2 REPORT.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round9/c2_integral_tame_flexibility/REPORT.md), SHA-256:

```text
d73e3cd3149bc695f5e8b331c3d05bad519630eb7fd8ce7889c97a9ba85f30ea
```

## Verdict

**PASS for the all-word coordinate-pair characterization, the same-set noncoordinate example, the conditional native nine-cycle implication, and the stated local-to-global applicability boundary. Zero mathematical or source-applicability must-fixes found.**

The existence of an integral tame lift of $\kappa=(5\ 9)(3\ 8)(6\ 7)$ remains **NOT CURRENTLY JUSTIFIED**. The report proves neither existence nor nonexistence for arbitrary tame words. Its source screen and auxiliary equivalence do not close the original question or supply another contract.

## 1. The coordinate-pair equivalence — lines 88–130

Here $M=(U,V)$ must already belong to $\operatorname{TA}_2(\mathbb Z)$, with its global integral tame inverse established. There is no restriction on its word length, degrees, coefficients or intermediate point sets. The reflection is $\rho_Q(u,v)=(u,Q(u)-v)$.

Necessity follows from $MK=\rho_QM$ evaluated at each of the nine points:

$$U(P_{\kappa(j)})=U(P_j),\qquad
V(P_j)+V(P_{\kappa(j)})=Q(U(P_j)).$$

If two different $\kappa$-orbits have the same $U$-level, their required sums must therefore coincide. This condition is not automatic from constancy on each exchanged pair, and the report explicitly imposes it. For a fixed point, the sum is $2V(P_j)$, so the fixed-point condition and its integer parity are also retained.

Let $u_1,\ldots,u_r$ be the distinct levels. Since the set is nonempty, $r\geq1$, and constancy on the six $\kappa$-orbits gives $r\leq6$. For any realizing $Q\in\mathbb Z[t]$, divide by

$$B(t)=\prod_{\ell=1}^r(t-u_\ell).$$

This polynomial is monic with integer coefficients. Polynomial long division therefore leaves a remainder $q\in\mathbb Z[t]$ of degree less than $r$, with $q(u_\ell)=Q(u_\ell)$. Distinct levels give uniqueness over $\mathbb Q$: the difference of two such remainders has $r$ distinct roots and degree less than $r$, hence vanishes. Thus the report's integer-coefficient test on the unique rational interpolant is necessary even when the initially realizing $Q$ has arbitrarily high degree.

Conversely, an integer-coefficient interpolant $q$ with the required common sums satisfies

$$\rho_q(M(P_j))=M(P_{\kappa(j)})$$

at every label. Conjugating by the already established $M^{-1}$ yields the required exact action on $C$. The map $\rho_q$ is itself an integral tame involution, so this is an actual tame conjugate, not merely a finite permutation or a pair of polynomial functions.

Repeated levels introduce no missing cases. Actual invertibility of $M$ prevents different points from having both the same $U$- and $V$-coordinates. For example, two distinct fixed points cannot share a level and satisfy the sum condition: it would force equal $V$-values. Multiple exchanged pairs at one level are allowed precisely when their sums agree. The proof neither assumes six distinct levels nor replaces integer interpolation by pairwise divisibility alone.

The equivalence is a complete criterion **after an actual coordinate pair has been supplied**. It is not a construction of that pair or a finite decision procedure for searching all tame words. No coordinate or tame-inverse condition has been dropped.

## 2. Evaluation, the noncoordinate example, and the native clock

The earlier accepted evaluation image is used with the unchanged point set. Its three parity fibers are $\{1,5,9\}$, $\{2,6,7\}$ and $\{3,4,8\}$. The specified $\kappa$ preserves each fiber, so permutation of components preserves the image ring inside $\mathbb Z^9$. The ideal $J_C$ is exactly the evaluation kernel. Thus $\kappa$ does induce an automorphism of $\mathbb Z[x,y]/J_C$; no ambient-lifting theorem follows from this statement.

Every first coordinate on $C$ belongs to $\{-1,0,1,2,3\}$. Consequently

$$b(t)=(t+1)t(t-1)(t-2)(t-3)$$

vanishes at each of those coordinates, and $U_0=x$ and $U_1=x+b(x)$ have exactly the same nine evaluations. The first is a tame coordinate, with companion $y$.

For any polynomial companion $V\in\mathbb Q[x,y]$ to the second, the Jacobian would be

$$\det D(U_1,V)=(1+b'(x))V_y.$$

The first factor is nonconstant of degree four and leading coefficient five. It is a nonunit in $\mathbb Q[x,y]$. If $V_y=0$, the determinant is zero; otherwise a product containing this nonunit cannot be a nonzero constant. A polynomial inverse would force the determinant to be a unit by the chain rule. Hence $U_1$ is not a polynomial coordinate even over $\mathbb Q$.

Only a necessary Jacobian condition is used; no converse Jacobian assertion is assumed. The example certifies loss of information about **chosen representatives** under evaluation. It does not say that all representatives of some desired values are noncoordinates, and it does not supply a $\kappa$-invariant coordinate: already $x(P_5)\ne x(P_9)$.

The nine points and the explicit $A,I$ match the accepted R7 data. Their restrictions are

$$a=(1\ 2\ 3)(4\ 5\ 6)(7\ 8\ 9),\qquad
i=(1\ 5)(3\ 8)(6\ 7).$$

Right-to-left multiplication gives $\kappa i=(1\ 9\ 5)$ and

$$\kappa ia=(1\ 2\ 3\ 9\ 7\ 8\ 5\ 6\ 4).$$

Thus a genuine required $K$ would give a least-period-nine orbit for the complete word $KIA$, with one word application per native tick. This remains conditional. The accepted two-shear obstruction is neither reproved nor promoted to an all-word obstruction here.

## 3. The original local-to-global theorem — lines 161–185

The original HTML's Theorem 3 and its complete proof were read, together with Proposition 1 and the equal-degree criterion. It gives

$$\operatorname{TA}_2(\mathbb Z)=
\bigcap_{\mathfrak p\in\operatorname{Spec}\mathbb Z}
\operatorname{TA}_2(\mathbb Z_{\mathfrak p}).$$

Its rank-one module hypothesis holds because $\mathbb Z$ is a PID. The groups share the ambient group $\operatorname{GA}_2(\mathbb Q)$. Here $\mathbb Z_{(p)}$ means localization, not the $p$-adic completion; the zero prime gives $\mathbb Q$. Coefficients of a common map and its unique inverse lying in every localization lie in $\mathbb Z$.

The proof lowers the degree of one fixed automorphism. For unequal degrees, its unique leading cancellation coefficient lies in every localization. For equal degrees, the two-generated leading-form module becomes globally free, permitting an affine degree reduction. Induction reaches the affine case. This is a tameness test for the common map, not a construction from separately chosen local maps. [Berson–Dubouloz–Furter–Maubach, Theorem 3 and proof](https://arxiv.org/html/1011.0976v1).

The report supplies neither that common candidate nor even local existence for this specific lift. Its distinction between $\exists M\,\forall\mathfrak p$ and $\forall\mathfrak p\,\exists M_{\mathfrak p}$ is valid. No convergence or stabilization of approximate words is proved or assumed.

## 4. Source-access scope

The fresh source checks were restricted to the cited primary leads; the author's two discovery batches were not rerun.

| Source | What this review actually obtained | Mathematical use allowed |
| --- | --- | --- |
| [Berson–Dubouloz–Furter–Maubach, arXiv:1011.0976v1](https://arxiv.org/html/1011.0976v1) | Original HTML theorem and complete proof, not just its abstract. | The exact common-map local-tameness criterion above. No new proof audit of every reference behind its degree-reduction criterion is claimed. |
| [Maubach's publication list](https://www.math.ru.nl/~maubach/publications.html) | The JPAA 216 (2012), 149–153 record and the Maubach–Rauf JPAA 219 (2015), 4708–4727 record. | Publication metadata, not a substitute for theorem text. |
| [Borisov–Gabber–Vasiu, arXiv:2609.00391](https://arxiv.org/abs/2609.00391) | Original record and abstract; its stated setting is affine spaces over finite fields. | This confirms the report's abstract-level scope distinction. No full theorem from the 2026 preprint was read or imported. |
| [Maubach–Rauf publisher DOI](https://doi.org/10.1016/j.jpaa.2015.03.003) | The DOI reopen and a direct publisher abstract-page reopen failed. | I do not claim a fresh read of its abstract or theorem. The report already imports no theorem from this source, so no proof depends on the unavailable material. |
| [Interpolation title-only lead](https://www.worldscientific.com/doi/10.1142/S1005386720000486) | Direct publisher open returned HTTP 403. | No theorem evidence; the report correctly excludes it. |

The report distinguishes a fully inspected theorem from abstract-only and failed-access leads. This review verifies the accessible mathematical interfaces and records its own access limits; it does not independently certify the historical count of the author's search calls. No literature-wide absence, priority or universal failure of integral flexibility follows from this bounded screen.

## Final coverage and disposition

The new proof-bearing claims have been checked completely: both directions of the all-word equivalence; repeated-level and fixed-point compatibility; monic integral division and rational uniqueness; the exact quotient-ring action; the same-$C$ Jacobian obstruction; native permutation multiplication; and the cited theorem's ring, common-map and quantifier conditions. The unchanged all-word existence problem remains visibly open rather than appearing as a concealed premise of a claimed construction.

The proof-writer, research-lit and repository batch guidance required this separation of proved interfaces, imported results and missing existence. Only the allocated review file was written. No mathematical program, old checker rerun, new agent, external-model/API upload, GPU task, PDF download/processing/build, author/shared edit or Git operation occurred. Primary HTML/record opens were the only external research actions.

**Final disposition: zero open must-fixes for the bounded auxiliary report; no actual general lift, no integer-nine-period closure, no additional contract or paper admission.** `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
