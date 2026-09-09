# E4 Round 6 — specified primitive branch and arithmetic survival interfaces

2026-09-10 UTC. Internal nonauthor reviewer: `/root/c429_e4_cover_review`.

Reviewed all 171 lines of [A4 REPORT.md](/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/continuation_round6/a4_primitive_branch_bridge/REPORT.md), SHA-256:

```text
5f248eabe14108c7e7ee0a3a6f3ef7b5d882ed2f9b163f2cc1c562754ac56846
```

## Verdict and exact scope

**PASS for the characteristic-zero crossing, CONTACT, the conditional isolated-label and unit-fold interfaces, SUMS, and the collision control. Zero mathematical or source-applicability must-fixes found.**

| Statement | Verdict |
| --- | --- |
| Lemma 1 and Proposition 2, including common labels and non-reality, lines 53–78 | Proved auxiliary application for every $e\geq2$. |
| CONTACT and $(U)$ as a sufficient isolated-label route, lines 82–98 | Identity and conditional implication valid; actual $(U)$ unproved. |
| Lemma 3 and SUMS, lines 104–140 | Conditional fold theorem and exact identities valid; actual FOLD unproved. |
| Normal finite-flat collision control, lines 144–158 | Valid control against the stated inference, not a dynatomic counterexample. |
| Real-terminal $(RB)$, full $(SB)$ and PC424-D | Respectively unassessed, unproved, and unresolved. No new contract or paper admission. |

The reviewed R4 necklace, pure-cycle identification and infinity involution are inputs. I reread the prior E4 review and the relevant R4 labeling/incidence passages; I did not reopen the accepted all-level local-inertia proof. The replacement of the real-terminal proposal by the specified ray landing is visible at lines 31–41, not a proof of the original real-terminal assertion.

## 1. The actual characteristic-zero edge

For $q=3n$, primitive residues modulo inversion have representatives $1\leq a\leq(q-1)/2$ with $3\nmid a$. Their number is $n$. Positive cosine values correspond to $a<q/4$, with no equality case. If $n=4r+1$, their count is $3r-r=2r$; if $n=4r+3$, it is $(3r+2)-r=2r+2$. Complementing signs therefore gives exactly the two weights $(n-1)/2$ and $(n+1)/2$. This verifies Lemma 1 without a finite-period sample.

The majority-one member has exact symbolic period $n$ by the accepted R4 coding, hence its angle has exact doubling period $n$. A maximal nonconstant cyclic word starts in a longest run of ones and ends in zero. Otherwise moving its trailing nonempty one-run to the beginning would increase the leading run. There are $(n-1)/2\geq4$ zeros. Flipping the last zero either lengthens the leading cyclic one-run or joins it to the preceding one-run; all unaffected runs remain no longer than its original length. The new longest run is unique, and a zero remains. Thus the successor cannot be a proper power. The argument handles a trailing zero-run of length one as well as longer zero-runs.

[Buff–Tan Lei, Lemmas 4.2–4.3 and Proposition 4.4](https://www.math.univ-toulouse.fr/~buff/Preprints/Irreducibility/Irreducibility.pdf) supplies the maximal-angle kneading identity, primitive landing outside the one-zero exception, and interchange of the two indicated itineraries. Its local degree-two statement applies at a point of native period $n$. Passing to cyclic classes does not identify the two endpoints: their weights differ. These are classical inputs, not new monodromy theorems.

In this application the successor has $(n+3)/2$ ones, outside the pair's two weights. Since the selected word has more ones than zeros, it has a cyclic adjacent pair of ones; its maximal representative consequently begins with $11$. The kneading identity transfers those initial symbols to the landing angle. Doyle's Lemma 9.5 then gives non-reality, and Remark 9.13 gives the conjugate edge with the same unordered endpoints. No distinct-reduction conclusion follows.

**The common-label check passes.** Both sources trivialize over the same slit exterior: the difference between removing the positive real ray and removing $[0,\infty)$ lies inside the Mandelbrot set. On the negative parameter ray, the dynamic partition separates the positive and negative real periodic points, with the zero-labeled side containing the positive external ray. Thus its itinerary is the real-sign itinerary, up to the simultaneous symbol conversion already allowed in R4. Continuation along $c<-2$ to $-2$ is unbranched on these cycles: their endpoint multipliers are $\pm2^n\ne1$, and zero never becomes periodic on that interval. The source ray to $\alpha_e$ is in this same trivialization. Therefore EDGE uses R4's pair, not a separately conjugated abstract transposition. This remains a characteristic-zero identification only.

## 2. CONTACT and the wild-period cycle quotient

The primitive branch polynomial is separable in characteristic zero and has a unit leading coefficient at 3. Writing it as $a\prod_{\beta\in T_n}(c-\beta)$ gives

$$\Delta_n'(\alpha_e)=a\prod_{\beta\ne\alpha_e}(\alpha_e-\beta).$$

Every root is integral, so every contact valuation is nonnegative. The derivative valuation is zero precisely when all the other reductions differ from that of $\alpha_e$. Multiplicities are not silently discarded: the characteristic-zero squarefreeness is essential here and is available. The embedding/prime choice in line 84 is also essential; the complex angle alone does not choose it.

[Doyle et al., Proposition 8.1 and Corollary 8.3](https://api.repository.cam.ac.uk/server/api/core/bitstreams/17388c5b-06f8-4235-afed-8ae9a331c5f3/content) retain isolated branch inertia using compatible fiber paths. The finite branch set of the cycle quotient is the primitive set, with infinity added in the projective model. Integral finite roots do not meet infinity. Thus $(U)$ isolates the selected section among all quotient branch sections; collisions with satellite point-cover values are not an omitted quotient branch condition. The corollary's global irreducibility conclusion additionally requires connectivity, which one crossing edge does not establish.

The model hypotheses really hold here. For the actual integral quotient, normality follows from the accepted model results; its finite dominant normal model over the regular two-dimensional parameter base is Cohen–Macaulay and flat. The special fiber is reduced, and generic separability of the point cover passes to its quotient algebra. None of this requires dividing by $n$ or commuting invariants with arbitrary nonflat reduction. The applicable restriction is odd residue characteristic for the quadratic family, not $3\nmid n$. The separate point-cover comparison requiring $p\nmid n$ is not used.

Locally, an isolated primitive value leaves only one degree-two ramification point in its quotient germ; the other germs are unramified. The normal finite-flat local argument in Corollary 5.4 retains the tame degree and smooth special germ. Proposition 8.1's proof then supplies the compatible labeled inertia comparison. The report uses this conditional interface, not the corollary's unproved global connectivity hypothesis.

No actual contact of the selected $\alpha_e$ is computed or proved to vanish. The text correctly leaves $(U)$ open and does not infer it from non-reality, conjugation, the Chebyshev singleton or full local point inertia.

## 3. FOLD, including the completed quotient germ

At the chosen characteristic-zero native parabolic point, $G=G_x=0$ exactly in $R$. After translating by the integral point, the unit $G_c$ gives a formal implicit solution $u=h(z)$ over $R$. The constant and linear terms vanish, and differentiation gives

$$G_c h''(0)+G_{xx}=0.$$

Hence $h(z)=z^2A(z)$ with $A(0)=-G_{xx}/(2G_c)$ a unit. Since 2 is invertible and $R$ is strictly henselian, $A(0)$ has a square root in $R$; formal Hensel lifting extends it to a square root of $A(z)$. The change $w=z\sqrt{A(z)}$ has invertible linear term and yields exactly $u=w^2$, with no surviving unit factor or division by $n$.

The first FOLD condition is doing separate work. The residual period divides $n$, and every proper divisor of $n=3^e$ divides $m$. Thus $H$ being a unit is equivalent here to retaining native period $n$. It also identifies the dynatomic germ with the germ of $G$, because $\Phi_n=G/H$ for this prime-power period.

At this residual orbit the constant group $C_n$ has trivial stabilizers. Its free action on an invariant neighborhood is a finite étale torsor even when $3\mid n$: the constant group scheme is étale, unlike $\mu_n$ in this characteristic. Over the chosen strictly henselian local quotient, this torsor splits into its $n$ point factors. The completed ring at any selected orbit point is therefore the completed quotient ring. No invariant-averaging formula is involved.

Reduction gives the single normal local cover $k[[u]]\to k[[w]]$, $u=w^2$. Its tame inertia swaps the two local cycle sheets. The same complete integral germ contains the two characteristic-zero sheets coalescing at the chosen point, so with the stipulated compatible transport it is EDGE. Other branch values may collide in other point germs without invalidating this local calculation. A global fiber-label identification is still required to describe this action relative to the transported pair.

This proves the stated conditional lemma, not FOLD for the actual ray landing. Failure of one sufficient unit condition does not prove disappearance of the edge.

## 4. SUMS and the collision control

All native orbit coordinates are integral, and $D_n=\prod_{j=0}^{n-1}2x_j=1$. Each factor, every $x_j$, and every partial product $D_j$ is therefore a unit. For the parameter derivatives $Q_j=\partial_c f_c^{\circ j}(\beta_e)|_{c=\alpha_e}$, one has $Q_0=0$ and $Q_{j+1}=2x_jQ_j+1$, hence

$$\frac{Q_{j+1}}{D_{j+1}}-\frac{Q_j}{D_j}=D_{j+1}^{-1}.$$

Telescoping gives $G_c=D_n\sum_{j=1}^nD_j^{-1}$, the first formula since $D_n=1$. Differentiating the product for $D_n$ at fixed $c$ gives

$$G_{xx}=D_n\sum_{j=0}^{n-1}\frac{\partial_xx_j}{x_j}
=\sum_{j=0}^{n-1}\frac{D_j}{x_j}.$$

The indices and factors of 2 in SUMS are correct. Characteristic-zero simple point ramification gives nonzero values there, not units at the selected 3-adic prime.

For the control, write $t=c-2$. The ring $\mathbb Z_3[t,y]/(y^2-t^2-3)$ is finite free of rank two. Its generic curve is smooth. In the special fiber, the only point where both relative derivatives vanish is $(t,y)=(0,0)$. At the corresponding point of the total space, $-3$ survives in the ambient maximal ideal modulo its square, so the quotient is regular of dimension two. Elsewhere a derivative is a unit locally. The total model is therefore regular and normal.

Its special fiber is the reduced union $y=t$ and $y=-t$, with generically separable degree-one maps. Normalization separates these into two unramified copies of the base. In characteristic zero the two simple branch values are $2\pm\sqrt{-3}$, and $v_3(D'(\alpha))=v_3(\pm2\sqrt{-3})=1/2$. Both swap the two sheets, but their product is the identity. The example satisfies the advertised model safeguards and defeats only automatic survival under collision. It is not a counterexample to a dynatomic assertion.

## Source access, coverage and handoff

Fresh primary reads covered Buff–Tan Lei's complete Lemmas 4.2–4.3, §§4.3–4.4 and complete Proposition 4.4 proof; Doyle's complete Proposition 8.1/Corollary 8.3 proofs, Corollary 5.4 with its setup/proof, Remark 6.1 and Propositions 6.2–6.4, the Corollary 8.4 unit statement, and the required §§9.1–9.6 passages. Theorem 3.17, Theorem 3.22 and Proposition 3.25 were checked for the polynomial and branch interfaces. Browser retrieval failed; the primary PDFs were read through read-only PDF-to-text streams. This is not a fresh full proof audit of every underlying Morton, Bousch, Douady–Hubbard or Green–Matignon source, nor a literature-wide priority search.

The no-defect coverage comprises all new proof-bearing sections: weights and endpoint incidence; common characteristic-zero labels; derivative contacts and integral model hypotheses; formal fold and free quotient; derivative sums; and the explicit collision control. The declared missing arithmetic statements are not concealed premises of a claimed unconditional theorem. Statistics, experiments, venue alignment and calibration are outside this theoretical review.

The repository batch workflow and proof-writer/research-review condition discipline governed this bounded internal check. Relevant ARS theoretical-methodology guidance was read inline; no full reviewer panel, cross-model review or calibration is claimed. Only this allocated review file was written. Mathematical programs, old checker reruns, new agents, author/shared edits, Git operations, external-model/API uploads and manuscript/PDF builds: zero.

**Final disposition:** the specific characteristic-zero crossing and both conditional arithmetic interfaces are safe auxiliary exports. Actual $(U)$, actual FOLD, a colliding-cluster replacement, and full $(SB)$ remain unproved; $(RB)$ remains unassessed. Even a successful single crossing would not establish the remaining graph connectivity or original all-prime PC424-D. `NO_BAD_EULER_OR_ROOT_NUMBER` is unchanged.
