# Round 6 A4 — one specified primitive-branch bridge

2026-09-10 UTC. Exclusive author `/root/c429_a4_witt_local_data`. Frozen before substantial proof. Only this file may be written; all prior artifacts and sources remain read-only.

## Original question and accepted inputs

Preserve PC424-D: for every odd prime $p$ and every $e\geq1$, classify the geometric irreducible components of the reduced native dynatomic curve of $f_c(x)=x^2+c$ at period $n=p^e$. One application of $f_c$ is one native tick. The accepted full-local theorem and eventual local quotient tower are inputs, not subjects for another proof or paper.

The accepted [R4 proof](../../continuation_round4/a4_global_quotient_after_full_inertia/REPORT.md), SHA-256 `a1eeb7f2e2c1300a9354abc8406714acc6254d5e33bfd4bc3ecf8b9b18ae5dcc`, and its complete [E4 review](../../continuation_round4/reviews/e4_chebyshev_blocks/REVIEW.md), SHA-256 `0ffbcf1bba68b88eafca3fc1c96f83bbfa2885a531eb9507f5066a0f48b0f753`, have been read. They reduce geometric point irreducibility to the cycle quotient being a field, but do not prove the latter. At $p=3$, $n=3^e$, $e\geq2$, their Chebyshev-plus-infinity reconnection group preserves the explicit pair

$$S_e=\{C_e,\iota C_e\},\qquad C_e:\ x_j=2\cos(2\pi2^j/3^{e+1}).$$

Here $\iota$ is simultaneous sign complementation in the infinity coding. This is not an invariant pair for the entire special-fiber monodromy group. Scalar arbitrary-edge-deletion budgets were already excluded in R3 and are not retried.

## Frozen single bridge lemma

Follow the real characteristic-zero native cycle $C_e$ from $c=-2$ in the increasing real parameter direction as long as its periodic roots continue as distinct real points. Let $a_e$ be its first terminal parameter, if it is well-defined without a singular continuation ambiguity. The proposed bridge is:

**(RB)** For every $e\geq2$, $a_e$ is a genuinely primitive finite period-$3^e$ branch parameter; with labels transported from $c=-2$ along the real interval, its local quotient inertia transposes $C_e$ with a sheet outside $S_e$. For the selected prime above $3$ and compatible mixed-characteristic transport, this branch action survives as a crossing inertia action of the characteristic-$3$ cycle quotient.

The phrase “survives” is an obligation, not an appeal to characteristic-zero specialization. A sufficient precise version is an isolated reduction of the selected primitive branch label, or a proved local vanishing-cycle statement for its actual colliding cluster whose action crosses the transported pair. The prime, transport, and any collision hypotheses must be stated in a completed proof. A real branch edge alone is insufficient.

## Status, method, and scope

**NOT CURRENTLY JUSTIFIED** at freeze. Test only (RB), using actual real kneading/primitive-branch geometry and its $3$-adic local reduction. First prove or locate the characteristic-zero edge and its incidence; then establish or expose the missing arithmetic survival step. If the proposed first-terminal construction is ambiguous or does not cross, give that exact failure and a justified residual formulation. The original all-prime/all-level component question is not replaced by this selected prime-three bridge, even if the bridge succeeds.

Primary-source inspection is targeted to the required branch and labeling statements; no broad literature census. No mathematical execution, extra agent, external model, Git/shared-state edit, manuscript, or PDF. The proof-writer and research-lit skills, together with the repository batch workflow, are used only for this bounded proof/source task. No paper admission or target-arithmetic promotion is claimed.

## Source-controlled refinement of the selected parameter

Before claiming a proof of (RB), the actual primary monodromy construction supplies a better specified parameter. The real first-terminal proposal is **not proved or refuted here**; its identification of the arriving sheet and complex branch labels would itself require additional real-dynamical arguments. It is superseded for this bounded attempt by the following explicit successor-ray parameter, not silently identified with it.

Among the two necklaces in $S_e$, let $V_e$ be the one with more one-symbols, and let $v_e=v_1\cdots v_n$ be its lexicographically maximal cyclic representative. Set

$$\theta_e=.\overline{v_1\cdots v_n}\in\mathbb Q/\mathbb Z,$$

and define $\alpha_e$ to be the landing point of the quadratic parameter ray $R(\theta_e)$. The new precise single lemma is:

**(SB)** For all $e\geq2$, the simple primitive local quotient monodromy at this specified $\alpha_e$ crosses $S_e$, and the same labeled connection survives at a prime above $3$ under compatible specialization.

Its characteristic-zero statement and its arithmetic survival statement will receive separate verdicts. The first can be checked using the maximal-itinerary successor construction in Doyle et al., §§9.2–9.6. The second requires new arithmetic evidence; non-reality of $\alpha_e$ or existence of its conjugate is not such evidence. This is the sole finite-parameter connection pursued after the refinement.

## Outcome and dependency map

**Characteristic-zero crossing: PROVABLE AS STATED, as a specific application of classical primitive-ray monodromy. Arithmetic survival in (SB): NOT CURRENTLY JUSTIFIED. Original PC424-D: unchanged and unresolved.**

The concrete advance beyond R4 is an explicitly specified finite branch label $\alpha_e$, uniformly for all $e\geq2$, with a proved endpoint outside its displayed pair. The remaining claim is no longer “find some primitive edge.” It is an arithmetic specialization assertion about this exact label, or its exact local point germ. There is no claim that one successful edge would connect all the other R4 classes.

Dependencies are: R4's accepted sign necklace and complement pair; the elementary weight count below; the source-owned maximal-ray/primitive-monodromy theorem; then a separate, as yet unverified, $3$-adic isolation or fold condition. Full local inertia and eventual local quotient stabilization enter only through the already accepted global reduction. Neither proves the new arithmetic conditions.

## 1. A uniform primitive crossing with a specified parameter

Use the source's binary itinerary convention throughout; interchanging its two symbols interchanges the two members of $S_e$ and does not change the construction of its majority-one member. Let $q=3^{e+1}=3n$.

**Lemma 1 (weights).** The two necklaces in $S_e$ have respectively $(n-1)/2$ and $(n+1)/2$ one-symbols.

**Proof.** The accepted order computation in R4 says that the orbit of $2$ on primitive $q$th roots, modulo inversion, has $n$ elements. Its cosine signs can therefore be counted using the integers

$$1\leq a\leq(q-1)/2,\qquad 3\nmid a.$$

There are $n$ of them. The positive cosine values correspond exactly to $a<q/4$, so their number is $t-\lfloor t/3\rfloor$, where $t=\lfloor q/4\rfloor$. If $n=4r+1$, then $t=3r$ and that number is $2r=(n-1)/2$. If $n=4r+3$, then $t=3r+2$ and it is $2r+2=(n+1)/2$. These exhaust the odd integers $n$. Complementation interchanges the counts. $\square$

**Proposition 2 (the selected characteristic-zero edge).** For every $e\geq2$, $\theta_e$ has exact doubling period $n$, its landing parameter $\alpha_e$ is a non-real primitive period-$n$ parabolic parameter, and the finite quotient inertia at $\alpha_e$ exchanges

$$V_e=[v_1\cdots v_{n-1}0]\quad\text{and}\quad
W_e=[v_1\cdots v_{n-1}1],\qquad W_e\notin S_e.\tag{EDGE}$$

Here brackets denote native cyclic classes. The local quotient ramification index is two in characteristic zero. The conjugate parameter supplies another classical edge with the same two endpoints, but no claim of distinct reduction is made.

**Proof, Step 1: symbolic primitivity.** The accepted necklace $V_e$ has exact period $n$, so its periodic binary expansion defines an angle of exact doubling period $n$. A nonconstant lexicographically maximal cyclic word ends in zero: if its trailing block of ones were nonempty, rotating this block in front of its leading block of ones would increase the word. Thus $v_n=0$.

The word $v_e$ has $(n-1)/2\geq4$ zeros. Replacing its last zero by one leaves at least one zero and creates a unique longest cyclic run of ones. Indeed the leading run of a maximal word has maximal length among its runs; the replacement extends it by at least one, possibly joining it to the last existing run, while leaving every other run no longer than the old maximum. A proper power would repeat each longest run at least twice. The successor word consequently still has exact period $n$.

**Step 2: actual branch, not a formal combinatorial edge.** Buff–Tan Lei, Lemmas 4.2–4.3, identifies the kneading sequence of a maximal periodic angle as $v_1\cdots v_{n-1}?$ and proves that its parameter ray lands at a primitive component root unless the word has just one zero. The latter exception is excluded by Step 1. Their Proposition 4.4 proves that the two itineraries obtained by replacing the star by zero and one are interchanged by the local loop. Its proof includes the smooth local form $c-\alpha_e=\delta^2$ at a native period-$n$ point. Passing to native cycles gives (EDGE) and the quotient ramification index two. These existence and monodromy statements are classical, not new theorems of this report.

**Step 3: crossing the specified cut.** Cyclic shift preserves the number of ones. The endpoint $W_e$ has $(n+3)/2$ ones, whereas the only weights in $S_e$ are $(n-1)/2$ and $(n+1)/2$. Thus $W_e$ is outside $S_e$. Since $V_e$ has a majority of ones, some cyclic run contains at least two consecutive ones, so its maximal representative begins with $11$. Doyle et al., Lemma 9.5, then makes $\alpha_e$ non-real. In particular it is not $0$, $-2$, or the real small-cycle parameter. Complex conjugation gives the same kneading sequence and hence the same unordered endpoints, as in their Remark 9.13. $\square$

The characteristic-zero labels are compatible with R4: use the slit exterior $\mathbb C\setminus(\mathcal M\cup R(0))$, where the source constructs a trivialized periodic cover, and approach $c=-2$ along the negative real ray. Its binary labels specialize to the real signs, with a possible simultaneous exchange of the two symbols. The unordered pair $S_e$ is unaffected. The ray $R(\theta_e)$ lies in this same slit exterior, so (EDGE) is an edge in that fixed labeled graph, not an independently relabeled abstract transposition. This does **not** yet supply characteristic-$3$ nearby-fiber transport.

## 2. The exact isolated-label arithmetic obligation

Let $\Delta_n(c)=\Delta_{n,n}(c)$ be the classical primitive branch polynomial. Its leading coefficient is a power of two up to sign, so all its roots are integral at primes over $3$. Write $T_n$ for its distinct characteristic-zero roots. It is important to use this primitive polynomial, not the full multiplier polynomial with its already known wild satellite collisions.

Choose a number field containing $T_n$ and a prime $\mathfrak p$ above $3$, and normalize $v_{\mathfrak p}(3)=1$. For the selected complex root $\alpha_e$, this choice means fixing an embedding of its algebraic field into the chosen $3$-adic algebraic closure; it is not determined by its complex ray angle. Then

$$v_{\mathfrak p}(\Delta_n'(\alpha_e))
=\sum_{\beta\in T_n\setminus\{\alpha_e\}}
 v_{\mathfrak p}(\alpha_e-\beta)\geq0.\tag{CONTACT}$$

The equality follows by differentiating the factorization of $\Delta_n$, with unit leading coefficient. Each summand is nonnegative by integrality. Thus this valuation is zero **if and only if** the selected branch root is alone in its residue class. This is an exact condition on the explicitly specified label, not a total-discriminant deletion allowance.

The unproved isolation condition is

$$v_{\mathfrak p}(\Delta_n'(\alpha_e))=0.\tag{U}$$

Under this unit condition, the isolated-branch specialization argument of Doyle et al., Proposition 8.1 and Corollary 8.3, retains the selected primitive edge in the common labeled monodromy-graph argument. Its hypotheses apply to the cycle quotient model: it is finite flat, has reduced special fiber and is generically separable, including when $3\mid n$. The extra tame restriction in their separate point-cover comparison is not imported. Consequently (U), together with that specialization's compatible fiber identification, is a sufficient route for retaining (EDGE). It still gives only this crossing, not graph transitivity.

No proof of (U) for this $\alpha_e$ at any suitably compatible prime over $3$, uniformly in $e$, has been obtained. Nor has a positive valuation been proved for the actual selected label. The pair $\alpha_e,\overline{\alpha_e}$ need not have different reductions merely because it consists of two non-real complex conjugates. The known full small-cycle inertia, its eventual quotient tower, and R4's Chebyshev singleton do not determine any contact term in (CONTACT) for this new parameter. The ray angle specifies an algebraic root but does not evaluate its $3$-adic branch contacts.

## 3. A local fold interface that allows other branch labels to collide

An isolated branch value is sufficient but stronger than necessary. The following direct germ criterion specifies an alternative arithmetic obligation for the same $\alpha_e$.

Choose a native period-$n$ parabolic point $\beta_e$ above $\alpha_e$ in characteristic zero, and put

$$G(x,c)=f_c^{\circ n}(x)-x,\qquad H(x,c)=f_c^{\circ m}(x)-x,
\qquad m=n/3.$$

The point and parameter are integral at the chosen prime: integrality of $\alpha_e$ was noted above, and $\beta_e$ satisfies the monic polynomial $G(x,\alpha_e)$. Let $R$ be a complete strictly henselian discrete valuation extension containing them, with residue characteristic three. Subscripts on $G$ denote partial derivatives.

**Lemma 3 (unit-fold criterion).** Suppose

$$H(\beta_e,\alpha_e)\in R^\times,\qquad
G_c(\beta_e,\alpha_e)\in R^\times,\qquad
G_{xx}(\beta_e,\alpha_e)\in R^\times.\tag{FOLD}$$

Then the completed integral point germ at the reduction of $(\beta_e,\alpha_e)$, and the corresponding completed cycle quotient germ, have local parameter form

$$R[[u]]\longrightarrow R[[w]],\qquad u=c-\alpha_e\longmapsto w^2.$$

In particular their characteristic-three special germs have one tame branch of degree two. Its inertia interchanges the two local cycle sheets which coalesce at $\alpha_e$. With compatible transport of these sheets, this is precisely the local crossing (EDGE). The lemma does not assert that (FOLD) holds for the actual $\alpha_e$.

**Proof.** At the characteristic-zero parabolic point, $G=G_x=0$. Translate $z=x-\beta_e$, $u=c-\alpha_e$. The unit $G_c$ permits formal implicit solution of $G=0$ as $u=h(z)$ over $R$, with $h(0)=h'(0)=0$. Twice differentiating this identity at zero gives

$$h''(0)=-G_{xx}(\beta_e,\alpha_e)/G_c(\beta_e,\alpha_e)\in R^\times.$$

Because $2$ is a unit, $h(z)=z^2A(z)$ with $A(0)\in R^\times$. Strict henselianity and formal Hensel lifting provide a square root of $A(z)$ in $R[[z]]$. The change $w=z\sqrt{A(z)}$ is invertible and gives $u=w^2$.

The first condition in (FOLD) says that the reduced point still has native period $n$: its period divides $n$, and every proper divisor of $n=3^e$ divides $m$. It also makes $H$ a unit in the germ, so $\Phi_n=G/H$ defines the same germ. The constant group $C_n$ acts freely on this residual orbit. Its free quotient is an étale torsor, even in residue characteristic three; at a chosen geometric point it induces an isomorphism of completed point and quotient germs. The form just proved therefore applies to the quotient. Reducing it gives $k[[u]]\to k[[w]],u=w^2$, with the asserted tame inertia. $\square$

This criterion is explicitly calculable in the native orbit, without any division by $n$. Put $x_j=f_{\alpha_e}^{\circ j}(\beta_e)$ and

$$D_0=1,\qquad D_j=\prod_{i=0}^{j-1}2x_i,\qquad D_n=1.$$

Every $x_i$ and $D_j$ is a unit: the factors are integral and their product $D_n$ is one. The chain rule gives the exact formulas

$$G_c(\beta_e,\alpha_e)=\sum_{j=1}^{n}D_j^{-1},\qquad
G_{xx}(\beta_e,\alpha_e)=\sum_{j=0}^{n-1}\frac{D_j}{x_j}.\tag{SUMS}$$

The first is obtained from $Q_{j+1}=2x_jQ_j+1$, $Q_0=0$, by division by $D_{j+1}$ and telescoping. The second follows by differentiating $\prod_{j=0}^{n-1}2f_c^{\circ j}(x)$ with respect to $x$ at fixed $c$. Characteristic-zero simple ramification makes both expressions nonzero there, but does not make their reductions nonzero. No uniform nonvanishing modulo $\mathfrak p$ has been proved for these two explicit sums or for the residual-period test. If a unit fails, this criterion is inconclusive; it does not prove disappearance of the actual branch.

## 4. Exact control against an unjustified survival inference

The distinction between a characteristic-zero primitive-looking fold and its special normalization is real, even for a normal finite flat integral model with reduced, generically separable special fiber. This control is not a quadratic dynatomic curve and is not a counterexample to (SB) or PC424-D.

Over $\mathbb Z_3$, consider

$$\mathcal X:\quad y^2=(c-2)^2+3.$$

It is a finite flat degree-two cover of the parameter line. Its characteristic-zero branch parameters are the two non-real conjugates $2\pm\sqrt{-3}$, each with simple ramification and the same sheet transposition. Both reduce to $c=2$. The total model is regular: away from the closed point $y=c-2=0$ one of the derivatives $2y,-2(c-2)$ is a unit locally; at that closed point the defining equation has a nonzero linear term $-3$ in the ambient maximal ideal modulo its square. Thus the quotient local ring there is regular of dimension two.

The special fiber is

$$y^2=(c-2)^2,$$

the reduced union of two lines. Its normalization is the disjoint union of two copies of the parameter line, both unramified. The two characteristic-zero branch transpositions therefore supply no special crossing. Their product around the colliding pair is the identity. For $D(c)=(c-2)^2+3$, each chosen branch root satisfies $v_3(D'(\alpha))=1/2$, so the precise isolation condition fails.

This defeats only the inference “a non-real conjugate pair of simple crossing folds automatically leaves a crossing after odd-characteristic reduction.” It neither identifies the contacts of $\alpha_e$ nor rules out a nontrivial vanishing-cycle contribution in its actual cluster. No conservation-of-discriminant or degree argument replaces that missing local information.

## 5. Source subtraction, final gap, and handoff

The actual primary passages inspected were:

- [Buff–Tan Lei, author manuscript](https://www.math.univ-toulouse.fr/~buff/Preprints/Irreducibility/Irreducibility.pdf), Lemmas 4.2–4.3 and §§4.3–4.5, including the full Proposition 4.4 proof: maximal-angle kneading, primitive landing, a common exterior labeling, and the simple-fold interchange. The published chapter is *Frontiers in Complex Dynamics* (2014), pp. 49–72. The uniform successor mechanism is entirely source-owned; its application to the R4 pair is the auxiliary increment.
- [Doyle et al., author-hosted primary manuscript](https://www.dpmms.cam.ac.uk/~hk439/reduction.pdf), complete Proposition 8.1 proof and Corollary 8.3, plus §§9.2–9.6: isolated-section specialization, exact primitive cycle labels, non-real conjugate edges and successors. Its leading-coefficient/unit statement in the Corollary 8.4 proof justifies (U). These are quotient-model theorems, not a wild point-cover theorem. Browser retrieval was intermittent; the indicated passages were also read through a read-only PDF-to-text stream without creating a source file.

The targeted searches were for these specific branch/kneading statements and their reduction interface, with an arXiv metadata fallback. Unrelated iterated-preimage monodromy hits were not used. No broad recent-literature census or exhaustive absence claim is made. The elementary implicit-function/Hensel fold calculation and the normal two-sheet collision control are explicit supporting arguments, not new source-priority claims.

The exact residual missing connection is now: **for the specified $\alpha_e=\operatorname{landing}(R(\theta_e))$, uniformly for $e\geq2$, prove (U), or prove (FOLD) with compatible nearby-fiber transport, or determine its actual colliding-cluster inertia and show that it crosses the transported pair.** None of these arithmetic assertions has been established. The real-terminal proposal (RB) remains unassessed, not falsely refuted or identified with $\alpha_e$.

Even a proof of this one arithmetic bridge would only break R4's particular pair; the rest of the global quotient still has to be connected, and other odd primes remain within the original question. Therefore the full (SB) and original PC424-D remain **NOT CURRENTLY JUSTIFIED**. No fifth-contract, paper, or target-arithmetic promotion follows. The skills required this explicit separation of proved classical-geometry application, conditional local interface, countercontrol and missing arithmetic. Only this exclusive report was written. Mathematical executions, extra agents, external models, old-artifact edits, Git/shared-state operations and PDF builds: zero.
