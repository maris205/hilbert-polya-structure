# Paper 29: bounded directional-degree literature supplement

Date: 2026-09-05. This supplements, without modifying, [the 294-line cancellation literature audit](PAPER29_CANCELLATION_LITERATURE_20260905.md). The higher-degree report and all author proofs are unchanged. Scope: exact forward/backward degree-recurrence comparisons, two explicit counterbaselines, and the applicability of the nearest primary sources. This is not a candidate PASS or a mathematical review of the author's cancellation lemmas.

## 1. Result

**Directional recurrence-order asymmetry does not rescue the broad novelty headline.** The earlier fixed-support complex triangular baseline already has forward minimal eventual order \(L+1\) and backward order one, with both first dynamical degrees equal to six. The initial suggestion that its two orders might coincide is false: different coordinates dominate in opposite directions. Section 3 proves the inverse calculation.

**Requiring real parameters does not rescue that headline either.** A fixed polynomial symplectic conjugate of a real \(SL_2\) family gives the same order pair in fixed affine four-space. Section 4 gives exact formulas, a real algebraic sequence \(t_L\uparrow2\), and a support check valid for every \(t\ne0\).

The nearest published directional examples include:

- A birational three-dimensional monomial map whose forward degree sequence has no constant-coefficient recurrence, whereas its inverse degree sequence satisfies a third-order recurrence: Bedford–Kim (2008), following Hasselblatt–Propp.
- A polynomial automorphism of \(\mathbb C^3\) with forward minimal order one and backward minimal order two, but different exponential growth rates: Déserti, arXiv:1602.04642v4.

Neither is a direct theorem for the specified polynomial symplectic family. Together with the elementary controls, however, they prevent treating directional asymmetry, real realization, fixed dimension, and constant growth as four separate general innovations.

The remaining candidate contribution must be the **single joint exact theorem**: all-parameter forward/backward ordinary-degree formulas for the displayed two-gradient-shear family, including its nonlinear critical-orbit resonance classification, its genuinely growing subdominant modes, and its specified positive-prehit real critical branch. No first-in-literature claim, numerical novelty score, or nonconjugacy theorem is supplied here.

## 2. New author input being compared

The inspected input is [the inverse/real-parameter author proof](PAPER29_CANCELLATION_INVERSE_REAL_PROOF_V1_20260905.md), for the same map

\[
P=p+x^3+2xy,\quad Z=z+x^2,\quad
X=x+P^2,\quad Y=y+\delta Z^6.
\]

Let \(m(\epsilon)\) be the first positive hit of \(-1/2\) by
\(r_0=0\), \(r_{j+1}=\epsilon/(1+2r_j)^4\). The supplement asserts

\[
D^-_\delta(t)=
\begin{cases}
\dfrac{1+2t}{1-6t},&m(-\delta)=\infty,\\[6pt]
\dfrac{1+2t-24t^L}{(1-6t)(1-16t^L)},
&m(-\delta)<\infty,\quad L=m(-\delta)+2.
\end{cases}
\]

Together with the forward result, it asserts common growth rate six and eventual recurrence orders determined separately by the tests at \(\delta\) and \(-\delta\). It also constructs algebraic \(a_m\) such that

\[
a_1=1,\qquad a_*<a_m<a_{m-1},\qquad
a_m\downarrow a_*=\frac{4^4}{5^5},
\]

and \(u\mapsto1-a_m/u^4\), starting at one, remains positive until its first zero at time \(m\). For \(\delta_m=-a_m/2\), the asserted forward/backward order pair is \((m+3,1)\); changing the sign exchanges the pair. The uniqueness is for this positive-prehit branch, not for all real resonant parameters.

These are author-proof inputs to the literature comparison. Their scientific acceptance depends on the separate proof review, not on this report. In particular, no finite line specialization substitutes for the multivariate ordinary-degree argument.

## 3. Correction: the complex triangular control is already directional

Use \((x,p,u,v)\) with symplectic form \(dx\wedge dp+du\wedge dv\). Recall

\[
H(x,p)=(p,p^6-x),\qquad
T_a(u,v)=(au+v^2,a^{-1}v),
\]

\[
\Psi(x,p,u,v)=(x+u^2,p,u,v-2up),\qquad
G_a=\Psi^{-1}(H\times T_a)\Psi.
\]

All maps are polynomial symplectic automorphisms. The previous audit proved, when \(a^3\) has exact order \(L\ge2\),

\[
\deg G_a^n=6^n+4-3\mathbf1_{L\mid n}\qquad(n\ge1),
\]

with minimal eventual characteristic polynomial \((T-6)(T^L-1)\).

For the inverse, put \(w=v-2up\) and write

\[
H^{-n}(x+u^2,p)=(Q^-_n,P^-_n),\qquad
T_a^{-n}(u,w)=(U^-_n,V^-_n).
\]

Since \(H^{-1}(x,p)=(x^6-p,x)\), direct induction gives, for every \(n\ge1\),

\[
\deg Q^-_n=2\cdot6^n,\qquad
\deg P^-_n=2\cdot6^{n-1}.
\]

The inverse triangular iterates have \(\deg U^-_n\le4\) after substituting \(w\), and \(V^-_n=a^nw\) has degree two. Hence

\[
G_a^{-n}=
\bigl(Q^-_n-(U^-_n)^2,\ P^-_n,\ U^-_n,
V^-_n+2U^-_nP^-_n\bigr).
\]

The first coordinate has degree \(2\cdot6^n\): its two terms have degrees \(2\cdot6^n\) and at most eight, with strict inequality already at \(n=1\). The fourth coordinate has degree at most \(2\cdot6^{n-1}+4<2\cdot6^n\). Thus

\[
\boxed{\deg G_a^{-n}=2\cdot6^n\qquad(n\ge1).}
\]

The inverse minimal eventual characteristic polynomial is \(T-6\). The true zeroth degree is one, so its full generating series is \((1+6t)/(1-6t)\); the all-indices annihilator has an additional factor \(T\). This initial-term issue does not affect the eventual comparison.

Therefore a single fixed-support family already realizes

\[
(\operatorname{ord}_{\rm ev}d^+,\operatorname{ord}_{\rm ev}d^-)
=(L+1,1),\qquad
\lambda_1(G_a)=\lambda_1(G_a^{-1})=6.
\]

The forward additive residual is bounded. This control does **not** reproduce the candidate's \(T^L-16\) subdominant modes. It does invalidate any assertion that the original control was necessarily order-symmetric.

## 4. A real, fixed-support directional control

This control was proposed during the present author/audit discussion and checked directly here. It is not represented as a published construction or as a new research result.

Define

\[
\chi(u,v)=(u,v+u^2),\qquad
A_t(u,v)=(tu-v,u),\qquad
T_t=\chi^{-1}A_t\chi,
\]

and use the same \(H,\Psi\) to set
\(\mathcal G_t=\Psi^{-1}(H\times T_t)\Psi\).
All factors preserve the corresponding standard symplectic forms; \(A_t\) has determinant one. This is one algebraic real-parameter family of polynomial symplectic automorphisms of \(\mathbb A^4\).

For any integer \(n\), write

\[
A_t^n=\begin{pmatrix}a_n&b_n\\c_n&e_n\end{pmatrix},\qquad
U_n=a_nu+b_n(w+u^2),\qquad
V_n=c_nu+e_n(w+u^2)-U_n^2.
\]

Then

\[
\mathcal G_t^n=
\bigl(Q_n-U_n^2,\ P_n,\ U_n,\ V_n+2U_nP_n\bigr),
\]

where \((Q_n,P_n)=H^n(x+u^2,p)\). If \(b_n\ne0\), then \(\deg U_n=2\), since \(w+u^2=v-2up+u^2\) has a nonzero quadratic part. If \(b_n=0\), then \(a_n\ne0\), by invertibility, and \(\deg U_n=1\). In either case \(\deg V_n\le4\).

For \(n\ge1\), the product \(2U_nP_n\) strictly dominates \(V_n\), and the fourth coordinate dominates all other coordinates. Therefore

\[
\deg\mathcal G_t^n=6^n+\deg U_n.
\]

In negative time the preceding inverse-Hénon calculation applies, while \(\deg U_{-n}\le2\), \(\deg V_{-n}\le4\). Its first coordinate again strictly dominates, giving \(\deg\mathcal G_t^{-n}=2\cdot6^n\).

Choose, for each \(L\ge3\),

\[
t_L=2\cos(\pi/L),\qquad
b_n=-\frac{\sin(n\pi/L)}{\sin(\pi/L)}.
\]

Thus \(b_n=0\) exactly when \(L\mid n\), and

\[
\boxed{
\deg\mathcal G_{t_L}^n=6^n+2-\mathbf1_{L\mid n},\qquad
\deg\mathcal G_{t_L}^{-n}=2\cdot6^n\quad(n\ge1).
}
\]

The forward Fourier coefficients at every \(L\)-th root of unity are nonzero: the coefficient at one is \(2-1/L\), and the others are \(-1/L\). Its minimal eventual polynomial is \((T-6)(T^L-1)\), while the inverse has \(T-6\). Both growth rates are six. The real algebraic parameters satisfy \(t_L\uparrow2\), so even monotone real realization accumulating at a finite endpoint is available in an elementary control.

Literal fixed support can also be checked. In one step set

\[
U=tu-v+2up-u^2,\qquad P=p^6-x-u^2.
\]

Then

\[
\mathcal G_t=(p-U^2,\ P,\ U,\ u-U^2+2UP).
\]

Its expanded coordinate monomial counts are \((11,3,4,16)\). Every nonzero coefficient is a nonzero constant times \(1,t\), or \(t^2\). This identity was checked by exact symbolic expansion; in particular support is identical for all \(t\ne0\), including every \(t_L\ge1\). No exclusion of finitely many periods is needed for this chosen formula.

Again the forward residual is bounded, taking only values one and two. The candidate's strictly growing residual remains a distinction from this precise control. No general impossibility theorem about other real polynomial symplectic controls is claimed.

## 5. Primary-source comparisons and their exact limits

### 5.1 Bedford–Kim 2008: nonrecurrent in one direction, recurrent in the other

In the section “Example of Hasselblatt and Propp,” Bedford–Kim give

\[
f(x_1,x_2,x_3)=(x_2/x_1,x_3/x_1,x_1),\qquad
f^{-1}(x_1,x_2,x_3)=(x_3,x_1x_3,x_2x_3).
\]

They prove that \(\deg(f^n)\) satisfies no constant-coefficient linear recurrence, while the inverse sequence satisfies
\(d^-_n=d^-_{n-1}+d^-_{n-2}+d^-_{n-3}\).
This is a stronger directional recurrence-existence contrast than two finite unequal orders. But \(f\) is rational, not polynomial; its polynomial inverse is not an affine-space polynomial automorphism, because its own inverse has denominators. The example is in dimension three and does not establish equal directional growth rates or the candidate's four-dimensional symplectic statement. [Bedford–Kim, *Linear recurrences in the degree sequences of monomial mappings*, ETDS 28 (2008), 1369–1375, example on p. 1374](https://deserti.perso.math.cnrs.fr/biblio/BedfordKim_linearrecurrencesinthedegreesequencesofmonomialmappings.pdf).

### 5.2 Déserti: an explicit polynomial-automorphism order contrast

Remark 3.2 of arXiv v4 gives

\[
f(z_0,z_1,z_2)=(z_0^2+z_1+z_2,z_0^2+z_1,z_0),
\]

with \(\deg f^n=2^n\) and \(\deg f^{-n}=2^{\lfloor(n+1)/2\rfloor}\). [Déserti, *Degree growth of polynomial automorphisms and birational maps: some examples*, arXiv:1602.04642v4, Section 3.1](https://arxiv.org/pdf/1602.04642).

From those explicit sequences, the forward minimal eventual polynomial is \(T-2\), and the backward one is \(T^2-2\): both \(\sqrt2\) and \(-\sqrt2\) have nonzero coefficients in the inverse sequence. This minimality calculation is an inference here. The rates are respectively \(2\) and \(\sqrt2\); the map is three-dimensional, not a standard symplectic four-dimensional map. Thus the example already supplies exact directional degree asymmetry in polynomial automorphisms, but not the candidate's whole joint theorem.

### 5.3 Inverse-degree bounds and dual dynamical degrees are different statements

Section 3.1 of Déserti also recalls
\(\deg f^{-1}\le(\deg f)^{d-1}\) and the reverse inequality, and derives comparisons of bounded, polynomial, and exponential growth. [Same primary paper, equation (3.1) and Proposition 3.1](https://arxiv.org/pdf/1602.04642).

Applying the inequalities to iterates gives bounds between directional exponential rates. It does not give equal generating functions or equal minimal recurrence orders. Similarly, graph transposition on \(\mathbb P^d\) exchanges the mixed degrees \(d_p(f^{-n})\) and \(d_{d-p}(f^n)\): swap the two graph projections in their intersection-number definition. Taking roots gives \(\lambda_p(f^{-1})=\lambda_{d-p}(f)\). This elementary explanation identifies what profile duality means; it does not determine the exact recurrence denominators. In particular, the two controls above already have equal \(\lambda_1\) and unequal eventual orders.

### 5.4 Recent-window check

The recent primary hit *The Trouble With Deautonomising Higher Order Maps* was published 2026-06-11. Its stated subject is deautonomisation, nonconfined singularities, and ultradiscrete calculations of singularity multiplicities. Its abstract/introduction does not assert the fixed-four-dimensional polynomial-symplectic directional recurrence classification sought here. It is an adjacent singularity-growth source, not a direct covering theorem. [Willox–Grammaticos–Ramani, MPAG 29, article 28 (2026)](https://link.springer.com/article/10.1007/s11040-026-09563-1).

The previously verified Nguyen and rational-surface sources remain applicable as described in the original audit; their full texts were not reopened to manufacture a new review stage.

## 6. Narrowed assessment

| Proposed emphasis | What has already been deducted | Assessment |
|---|---|---|
| Unequal forward/backward exact recurrence behavior | Bedford–Kim; Déserti | Established phenomenon |
| Unbounded forward order and inverse order one at equal growth rate in fixed symplectic \(\mathbb A^4\) | Section 3's complex control | Elementary control already supplies it |
| The same phenomenon at real algebraic parameters in one fixed-support family | Section 4's real \(SL_2\) control | Real realization alone is also insufficient |
| Exact all-parameter two-gradient-shear formulas, strictly growing subdominant modes, and the stated nonlinear real critical branch | Not reproduced by either bounded-residual control; general conceptual precedents remain | A joint, family-specific contribution to assess after proof review; not a novelty PASS |

The useful contrast is between the controls' \(T^L-1\) and the candidate's \(T^L-16\), together with the actual all-parameter calculation. Do not separate “fixed dimension,” “real branch,” “directional asymmetry,” and “constant dynamical degree” into four claims of general innovation. Do not claim that the controls disprove the candidate's formulas, or that the candidate has been proved nonconjugate to all product constructions.

## 7. Bounded query record and evidence status

Three query groups were used; the listed strings are actual searches from this supplement. Primary examples above were then read at the cited source sections. This was a targeted extension, not a new broad survey.

| Group | Query |
|---|---|
| Exact directional recurrence | `"polynomial automorphism" "inverse" "degree sequence" recurrence` |
| Exact directional recurrence | `"symplectic" "degree growth" "inverse" polynomial` |
| Exact directional recurrence | `"degree sequences" "forward" "backward" automorphism` |
| Existing inverse examples | `"polynomial automorphisms" "degree growth" "inverse"` |
| Existing inverse examples | `"birational maps" "inverse" "linear recurrence" degree` |
| Existing inverse examples | `"degree growth" "asymmetry" automorphism` |
| Real/recent boundary | `"real" "polynomial automorphism" "degree" "recurrence"` |
| Real/recent boundary | `"symplectic" "inverse" "degree sequence" 2024 2025 2026` |
| Real/recent boundary | `"degree growth" "inverse" "recurrence" after:2026-03-05 before:2026-09-06` |

Some exact-phrase searches produced mostly unrelated graph-degree results; absence of a relevant hit is not treated as evidence of originality. Publication dates were checked at the primary source. The June 2026 paper is genuinely inside the recent six-month window; recently crawled older papers were not relabeled as 2026 publications.

The `research-lit` and `novelty-check` workflows guided the bounded claim/source comparison and the explicit baseline challenge. No prescribed cross-model MCP review was available or fabricated. No subagent was started for this supplement. Only this new local report was written; the prior 294-line report and the author proof inputs were preserved.
