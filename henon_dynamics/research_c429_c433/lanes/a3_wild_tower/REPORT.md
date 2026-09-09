# A3: PC424-D wild tower — frozen question and proof attempt

2026-09-09 UTC. Current-team author `/root/c429_a3_wild_tower`.

## Frozen original question and success boundary

The actual [original PC424-D contract](../../../research_c424_c428/positive_characteristic/FROZEN_CONTRACTS.md) asks for the geometric irreducible components of

$$
\overline\Phi_{p^e}(x,c)=
\overline{\frac{f_c^{\circ p^e}(x)-x}{f_c^{\circ p^{e-1}}(x)-x}},
\qquad f_c(x)=x^2+c,
$$

over $k=\overline{\mathbb F}_p$, for **every odd prime $p$ and every $e\geq1$**, on the entire affine $(x,c)$-plane. The bar means reduction of the integral polynomial; the object is the reduced geometric curve. One application of $f_c$ is one native tick. The pair $(3,1)$ is included. Local scheme lengths, ordinary point counts, normalization and cyclic orbit quotients remain distinct.

The task's phrase “local multiplicity tower” describes a prospective method, not the original conclusion. This distinction was reported to the coordinator before substantial proof work. Success requires an all-$(p,e)$ irreducibility theorem or a uniform complete alternative component mechanism with all exceptions. Local ramification formulas, short towers and conditional expressions in unknown Galois data do not close this question. If that global bridge remains missing, the disposition is **NOT CURRENTLY JUSTIFIED / UNCLOSED**, not a new paper or universal impossibility claim.

## Source subtraction and proposed route

The complete R5 contracts, proof/gaps, disposition and source audit were read, followed by the original contract/scout/source records and R4 trace-blindness proof/source records. Inherited results include the uniformly simple fibre $c=0$, generic exact period $p^e$, reducedness and absence of vertical components, and the component formula in unknown cycle-orbits and stabilizer rotation images. R4's exact multiplication/cyclic-trace blindness is inherited, not reproved as new work.

The prospective route is to identify a wild local germ whose full ramification tower forces an actual inertia permutation rotating a native $p^e$-cycle by a unit modulo $p$; this still needs global cycle transitivity. A local length computation alone does not supply either condition. Before using ramification formulas, all hypotheses will be matched to the specific quadratic family, not a generic Nottingham-group element.

No mathematical program is allocated or planned at freeze. Any future diagnostic requires a written finite input set, discriminating claim, cost bound and coordinator allocation before execution. No old programs/builds, shared files, Git, evaluators, manuscripts/PDFs or external-model uploads may be changed/run.

## Assumptions, notation and dependency map

Fix arbitrary odd $p$ and $e\geq1$, and put $n=p^e$, $m=p^{e-1}$ and $k=\overline{\mathbb F}_p$. The following proof device makes a tame base change; it does not change the original family or clock:

$$
R=k[[s]],\quad K=k((s)),\quad
\lambda=1+s,\quad c=\frac14-\frac{s^2}{4},\quad
x=z+\frac\lambda2.
$$

Then $f_c(x)-\lambda/2=P_s(z)=\lambda z+z^2$. Write

$$
Q_e(z,s)=\frac{P_s^{\circ n}(z)-z}{P_s^{\circ m}(z)-z}\in R[z].
$$

The proof below depends on one external classical input: for $g(z)=z+z^2$,

$$
\operatorname{ord}_z(g^{\circ p^j}(z)-z)
=1+\frac{p^{j+1}-1}{p-1}\qquad(j\geq0).
\tag{1}
$$

This is the odd-characteristic case $a_1=1,a_2=0$ of Lindahl–Rivera-Letelier, [Proposition 4.4 and Definition 3.4](https://arxiv.org/html/1311.4478v3#S4.SS2). It is source-owned, not a new all-tower theorem here. The remaining dependencies are the inherited generic separability/exact-period result, coprime Hensel factorization, and elementary cyclic Galois actions.

The same source's Theorem C already gives, for this exact family $\lambda=1+s$ and every odd $p$, the unique small native $p^e$-cycle and its optimal slope $(p-1)/p$ for all $e\geq1$. Those conclusions are subtracted together with (1). Steps 1–3 below are an applicability reconstruction, not a new small-cycle theorem. The interface newly assembled in this batch is the explicit Artin–Schreier extraction and its compatibility with the canonical local factor; no literature-novelty claim is made for that extraction.

## Proved auxiliary interface: the parabolic cluster, not its full inertia

**Claim.** There is a canonical monic factor $M_e(z,s)\in R[z]$ of $Q_e$, of degree $n$, reducing to $z^n$. Its generic roots are $n$ distinct points forming one ordinary native $n$-cycle. Every root $\alpha$ satisfies

$$
v_s(\alpha)=\frac{p-1}{p}.
\tag{2}
$$

The splitting-field Galois group of this factor over $K$ is a subgroup $H_e\leq C_n$ of order $p^{h_e}$ with $1\leq h_e\leq e$. The number of its irreducible factors over $K$ is $p^{e-h_e}$. In particular the local factor is irreducible when $e=1$; the argument does not determine $h_e$ for $e>1$.

**Step 1: special-fibre length.** Subtracting (1) at $j=e$ and $j=e-1$ gives

$$
\operatorname{ord}_z Q_e(z,0)=p^e=n.
\tag{3}
$$

This is the length at the single ordinary fixed point $(x,c)=(1/2,1/4)$ in this special fibre, not $n$ distinct points. Since $Q_e$ is monic, its reduction is $z^n V(z)$ with $V(0)\ne0$. Coprime Hensel factorization over $R$ produces unique monic factors $M_e,N_e$ with reductions $z^n,V$, respectively. Thus $M_e$ has degree $n$, and all its roots have positive valuation; the other roots have valuation zero.

**Step 2: ordinary generic cycle.** The rational map $k(c)\hookrightarrow k(s)$ given above is injective. The generic separability and coprimality with $f_c^{\circ m}-x$ proved in R5 therefore survive this extension and completion. Hence the $n$ roots of $M_e$ are distinct and have exact ordinary period $n$. The map $P_s$ preserves positive valuation, and its inverse on its periodic roots is $P_s^{\circ(n-1)}$. Thus its action on this root set is a permutation whose every cycle has length $n$. A set of cardinality $n$ has exactly one such cycle.

**Step 3: valuation.** If $v_s(a)>0$, then $P_s(a)=a(\lambda+a)$ has the same valuation as $a$. Consequently all $n$ roots in this cycle have a common valuation $r$. Evaluation at $z=0$, cancelling the simple linear zeros of the numerator and denominator over $K$, gives

$$
Q_e(0,s)=\frac{\lambda^n-1}{\lambda^m-1}
=s^{n-m}.
$$

Since $N_e(0,s)$ is a unit, the product of the $n$ roots of $M_e$ has valuation $n-m$. Therefore $nr=n-m$, proving (2). This reconstructs the relevant optimal-cycle consequence directly from (1); no global irreducibility is inferred from it.

**Step 4: exactly what Galois theory gives.** The local Galois action commutes with the native permutation $\sigma=P_s$ and preserves this one cycle. The centralizer of one $n$-cycle is its cyclic group: a commuting permutation is determined by the image of one point, which determines all its subsequent images. The splitting group therefore acts faithfully as a subgroup $H_e\leq\langle\sigma\rangle$. Every orbit has size $|H_e|$, so every irreducible factor has that degree and there are $n/|H_e|$ factors.

For any root, the finite extension $K(\alpha)/K$ has ramification index divisible by $p$, since its value group contains $(p-1)/p$. Thus its degree $|H_e|$ is divisible by $p$, giving $h_e\geq1$. When $e=1$, this forces $H_1=C_p$. When $e>1$, it does not exclude any $h_e\in\{1,\ldots,e\}$. All roots lie in any one root's field (they are its iterates), consistently with each irreducible factor defining the same cyclic splitting field. The residue field is algebraically closed, so the whole splitting group is inertia. $\square$

**First-level ramification check, not tower closure.** At $e=1$, normalize the extension valuation so $v_L(s)=p$ and $v_L(\alpha)=p-1$. Then

$$
v_L(\sigma\alpha-\alpha)
=v_L(s\alpha+\alpha^2)=2(p-1).
$$

If $b$ is the lower break of its order-$p$ automorphism, expansion in a uniformizer gives $v_L(\sigma a-a)=v_L(a)+b$ whenever $p\nmid v_L(a)$. Applying this with $a=\alpha$ gives $b=p-1$. For $h_e>1$, the value $v_L(\alpha)=p^{h_e-1}(p-1)$ is divisible by $p$, so this particular leading-term inference cannot be repeated without new information. This calculation does not identify the full higher ramification filtration.

## Exact A4 handoff and remaining bridge

The useful output supplied to A4 is the explicit place, tame coordinate, and canonical degree-$n$ native-cycle polynomial $M_e$. Its coefficients are in $K$, and its generic algebra $E_e=K[z]/(M_e)$ is a finite étale cyclic torsor algebra; it need not be a field. Its native invariant algebra is exactly $K$, because after separable closure the action is transitive on its $n$ points.

A4 supplied a rational first Artin–Schreier coordinate. For $\alpha=[z]\in E_e$, define

$$
w=\frac{\alpha^{n-1}}{M_e'(\alpha)},\qquad
y=-\sum_{i=0}^{n-1}(i\bmod p)\,\sigma^i(w),\qquad
a_0=y^p-y.
\tag{4}
$$

Lagrange interpolation gives $\sum_i\sigma^i(w)=1$; shifting the sum gives $\sigma y-y=1$. Hence $a_0\in E_e^{\langle\sigma\rangle}=K$. These identities remain valid if $E_e$ is disconnected. Thus (4) is a concrete local series target rather than an undefined choice of a Witt class.

If the class of $a_0$ in $K/\{u^p-u:u\in K\}$ is nonzero, then the local Galois character maps onto $C_p$. Since that character is the projection of $H_e\leq C_{p^e}$ modulo $p$, it follows that $H_e=C_{p^e}$. Equivalently, a nonzero reduced negative-power term of $a_0$ with exponent prime to $p$ suffices. A4 owns the general AS/Witt/source verification; the algebraic compatibility with this local cluster is established above.

**Unproved local obligation:** show that the explicitly defined class in (4) is nonzero for every odd $p$ and every $e>1$, or determine its exact vanishing pattern. No such Laurent-series cancellation theorem or normalized-branch calculation is proved here. The special-fibre length $p^e$ and slope $(p-1)/p$ alone do not give it. Even a positive solution would force full rotation only over the global native-cycle orbit containing this parabolic cluster.

**Unproved global obligation:** establish transitivity of the global Galois action on all native $p^e$-cycles, or classify its distinct cycle-orbits. R5's component formula remains

$$
\#\operatorname{Irr}(\overline\Phi_{p^e})
=\sum_jp^{e-h_j},
$$

with undetermined cycle-orbits and stabilizers. Neither (1) nor (4) settles that global datum. Other parabolic cycles and other parameter fibres are not excluded or replaced by the chosen fixed-point neighbourhood.

## Source verification and bounded execution

The research-lit skill was used local-first. No relevant dynatomic/ramification PDF was found in the selected Hénon paths; root `papers/` belongs to the symbolic stream and was not read. No Zotero/Obsidian tools or usable `arxiv_fetch.py` were found in the checked paths, so ordinary primary-source browsing was used. No PDF download or local page audit is claimed.

Actual new primary-source access: Lindahl–Rivera-Letelier, *Optimal cycles in ultrametric dynamics and minimally ramified power series*, [arXiv:1311.4478v3](https://arxiv.org/html/1311.4478v3), dated 2015-05-26. Read the introduction through Theorem C, Definition 3.4, Lemmas 3.5–3.6 and Proposition 4.4's odd-prime proof, Proposition 5.1 and its relevant proof, and Proposition 5.3 statement. The higher-step implication uses the cited established ramification theorem, not a claimed independent reproof. The source does not identify the local Galois inertia of this parameter degeneration or establish PC424-D's global component classification.

Also rechecked Doyle et al., [arXiv:1703.04172v2, Proposition 7.1 and full proof](https://arxiv.org/html/1703.04172v2#S7): its hypotheses include $n>3$, so its wild-collision singularity conclusion applies here only when $p^e>3$ and excludes $(p,e)=(3,1)$. Within that applicable range, singularity alone does not decide the normalized branches. The original $c$-neighbourhood in A4's $(3,1)$ example is smooth; its ramified $s^2$ pullback can be singular, which must not be attributed to this proposition. None of the A3 derivation above depends on singularity. Kallal–Kirkpatrick, [arXiv:1611.01077v3](https://arxiv.org/html/1611.01077v3), was opened as a nearby ramification lead; no theorem from it is used.

Actual search strings, without recency filters: `site:arxiv.org minimally ramified quadratic power series z+z2 odd characteristic ramification numbers`; `site:arxiv.org dynatomic curves parabolic point characteristic p local equation p power`; `"dynatomic" "local" "irreducibility" "characteristic p"`; `"quadratic" "optimal cycles" "Galois"`; `"Lindahl" "Rivera-Letelier" "irreducible"`; `"equal characteristic" "periodic points" "ramification index"`; `"positive characteristic" "periodic points" "finite extension" "quadratic"`. The final two tested whether a local-field period bound could force $h_e=e$; no applicable primary theorem was verified. Search hits not listed as used sources were not promoted to proof evidence.

Mathematical program executions: **0**. No old reruns, new factorization census, builds, manuscripts/PDFs, formal evaluation, shared-index/Git writes or external-model upload. The root coordinator was informed of the contract correction and the actionable local interface as soon as they were obtained. This is author work, not independent review or a novelty certificate.

## Disposition

**NOT CURRENTLY JUSTIFIED / ORIGINAL PC424-D UNCLOSED / NO ADMISSION PROPOSED.** All original parameters and ordinary native-clock quantifiers survive unchanged. The minimal-ramification formula, unique small cycle and optimal slope are source-owned; the AS extraction interface sharpens the next test but is not a replacement paper. Remaining work is the exact AS class/nonbranching obligation plus the independent global cycle-transitivity obligation, or a different proof that genuinely bypasses them.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
