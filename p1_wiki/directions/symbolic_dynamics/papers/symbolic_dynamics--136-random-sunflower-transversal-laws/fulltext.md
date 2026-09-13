---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--136-random-sunflower-transversal-laws"
canonical_tex: "symbolic_dynamics/papers/136-random-sunflower-transversal-laws/main.tex"
canonical_pdf: "symbolic_dynamics/papers/136-random-sunflower-transversal-laws/main.pdf"
source_sha256: "39724907724bf2f0bcc2e03b0dd5fb74aefeff8fb9f9d9c4bdea1edf00131170"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Recorded-Transversal Laws on Rate-Weighted Sunflower Forests

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/136-random-sunflower-transversal-laws>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/136-random-sunflower-transversal-laws/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/136-random-sunflower-transversal-laws/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/136-random-sunflower-transversal-laws/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/136-random-sunflower-transversal-laws/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Consider the owned random-edge/random-vertex covering process, restricted to vertex-disjoint heterogeneous sunflowers with fixed positive edge rates. We derive the complete law of the full recorded transversal, without reducing it to a minimal transversal. For one sunflower, an inclusion--exclusion integral gives every selected-petal mask at arbitrary rates, and independent uniform marks refine that law to every actual vertex set. At unit rates, elementary symmetric polynomials give the complete selection-count probability generating function, mean, and variance; the maximal-count atom is resolved into its all-petal and final-core events. For a disjoint sunflower forest, the marked stopped laws factor; component choice counts add, hence their probability generating functions multiply. The covering algorithm, sunflower carrier, exponential/size-biased ordering, and independence of disjoint restrictions are prior or generic machinery and are not claimed as contributions. A finite exact-arithmetic program checks the formulas on a frozen bounded family.
author:
- Anonymous
bibliography:
- references.bib
title: 'Recorded-Transversal Laws on Rate-Weighted Sunflower Forests'
```

## Markdown 正文

# Positioning and contribution

Sunflowers, also called Delta-systems, are classical [@erdosrado1960]. Their transversals belong to a broad literature that includes extremal and approximation questions [@chvatalmcdiarmid1992]. More importantly for the present dynamics, the random covering algorithm is not new. Pitt gave its graph ancestor [@pitt1985], and @baryehuda2000 [Section 5.1 and Theorem 6] directly treats the Pitt rule for hypergraph vertex cover. In the unweighted setting, its vertex choice in the selected hyperedge is uniform. We therefore assign zero credit to the covering algorithm, its validity, and every approximation guarantee.

The ordering device is also owned background. Rate-proportional sampling without replacement is a Plackett--Luce/size-biased order [@plackett1975]; positive-rate independent exponentials and dissociation of restrictions to disjoint item sets are treated explicitly by @gnedin2026. We assign zero credit to the exponential representation, memorylessness, finite ranking probabilities, and generic forest independence. The same applies to inclusion--exclusion, beta integrals, elementary symmetric polynomials, tail-sum identities, and products of PGFs.

After this subtraction, the contribution is deliberately narrow: for the owned covering process restricted to vertex-disjoint heterogeneous sunflowers with fixed edge rates, we derive the complete recorded-transversal law and, at unit rates, the complete choice-count PGF and first two moments. The point is the closed conjunction of aggregate endpoint, actual-vertex refinement, choice-count law, and marked forest factorization for this carrier. We claim neither a new algorithm nor a general theory of random greedy hitting sets.

# Model and marked order

Fix positive integers $$m,c,p_1,\ldots,p_m$$ and positive real numbers $\lambda_1,\ldots,\lambda_m$. A sunflower has a core $C$ of size $c$, pairwise disjoint petals $P_i$ of size $p_i$, and edges $$E_i=C\mathbin{\dot\cup}P_i,\qquad i\in[m].$$ At each step, an active edge $E_i$ is chosen with probability proportional to its fixed rate $\lambda_i$. A vertex is then chosen uniformly from $E_i$ and added to the recorded set. A petal choice deletes only $E_i$; a core choice hits all remaining edges and stops the component. If every edge receives a petal choice, the process also stops. The endpoint is the full recorded set: previously selected petal vertices are retained, so the endpoint need not be a minimal transversal.

Write $$r_i=\frac{p_i}{c+p_i},\qquad
 q_i=\frac{c}{c+p_i}=1-r_i,
 \qquad
 \Lambda(A)=\sum_{i\in A}\lambda_i.$$ Let $X_i\sim\mathrm{Exp}(\lambda_i)$ independently. Independently of all clocks and one another, give edge $i$ a uniform mark $U_i\in E_i$. Sorting the $X_i$ and reading marks until the first core mark gives the original process. Indeed, the minimum clock has the required rate-proportional law, and after a petal deletion the residual clocks have the same law by memorylessness. The fixed-rate and independent-mark hypotheses are essential for this coupling. This representation is used only as owned machinery.

# The complete weighted endpoint law

For a proper subset $A\subsetneq[m]$, let $\pi(A)$ be the probability that exactly the edges in $A$ are recorded through petal vertices before a core vertex stops the component. Define $$\label{eq:integral-sum}
 I(A)=\sum_{B\subseteq A}
       \frac{(-1)^{|B|}}{\Lambda([m]\setminus A)+\Lambda(B)}.$$ Every denominator is positive because $A$ is proper.

[\[thm:weighted\]]{#thm:weighted label="thm:weighted"} For every proper $A\subsetneq[m]$, $$\label{eq:weighted-endpoint}
 \pi(A)=
 \left(\prod_{i\in A}r_i\right)
 \left(\sum_{j\notin A}q_j\lambda_j\right)I(A).$$ The remaining, all-petal endpoint has probability $$\label{eq:all-petal}
 \pi([m])=\prod_{i=1}^{m}r_i.$$ These $2^m$ masses are positive and sum to one.

Fix $A\subsetneq[m]$ and expose the time $t$ of the stopping core mark. For each $i\in A$, edge $i$ must carry a petal mark and satisfy $X_i<t$. For each edge outside $A$, no clock may ring before $t$, except that one such edge $j$ rings at $t$ and carries a core mark. Summing the latter density over $j\notin A$ gives $$\begin{aligned}
 \pi(A)
 &=\left(\prod_{i\in A}r_i\right)
   \left(\sum_{j\notin A}q_j\lambda_j\right)
   \int_0^\infty
   e^{-\Lambda([m]\setminus A)t}
   \prod_{i\in A}(1-e^{-\lambda_i t})\,dt.\label{eq:weighted-integral}\end{aligned}$$ Expanding the product in [\[eq:weighted-integral\]](#eq:weighted-integral){reference-type="eqref" reference="eq:weighted-integral"} and integrating each exponential gives [\[eq:integral-sum\]](#eq:integral-sum){reference-type="eqref" reference="eq:integral-sum"} and [\[eq:weighted-endpoint\]](#eq:weighted-endpoint){reference-type="eqref" reference="eq:weighted-endpoint"}. The only way to terminate without a core mark is for every mark to lie in its petal, proving [\[eq:all-petal\]](#eq:all-petal){reference-type="eqref" reference="eq:all-petal"}. The marked-clock construction partitions its probability space into these events, which proves normalization; the integral form proves positivity.

The aggregate law also resolves every actual vertex set, including at unequal rates.

[\[cor:vertices\]]{#cor:vertices label="cor:vertices"} Fix $A\subsetneq[m]$, vertices $x_i\in P_i$ for $i\in A$, and $y\in C$. Then $$\label{eq:actual-core}
 \mathbb P\!\left(
  R=\left\{y\right\}\cup\left\{x_i:i\in A\right\}
 \right)
 =\frac{\pi(A)}{c\prod_{i\in A}p_i}.$$ For $x_i\in P_i$ for every $i$, $$\label{eq:actual-all-petal}
 \mathbb P\!\left(R=\left\{x_1,\ldots,x_m\right\}\right)
 =\prod_{i=1}^{m}\frac{1}{c+p_i}.$$

Conditional on its category, every petal mark is uniform on its own $P_i$ and the stopping core mark is uniform on $C$. More formally, let $\mathcal F$ be the sigma-field generated by all clocks and all core-versus- petal category indicators. The event fixing $A$ and the terminal edge is $\mathcal F$-measurable; conditional on $\mathcal F$, the relevant within-category vertex identities remain mutually independent and uniform on $C$ or their respective petals. Dividing the aggregate mass by $c\prod_{i\in A}p_i$ proves [\[eq:actual-core\]](#eq:actual-core){reference-type="eqref" reference="eq:actual-core"}. In the all-petal event, edge $i$ selects a specified petal vertex with probability $1/(c+p_i)$; independence gives [\[eq:actual-all-petal\]](#eq:actual-all-petal){reference-type="eqref" reference="eq:actual-all-petal"}.

# Unit rates: choice-count PGF and moments

Assume throughout this section that $\lambda_i=1$. Let $T\in\left\{1,\ldots,m\right\}$ be the discrete number of selections, equivalently recorded vertices, at absorption. Thus $T$ is a choice count, not elapsed time in the exponential embedding. Let $e_t(r_1,\ldots,r_m)$ be the elementary symmetric polynomial, and put $$\label{eq:st}
 s_t=\frac{e_t(r_1,\ldots,r_m)}{\binom mt},\qquad 0\leq t\leq m,$$ with $s_0=1$.

[\[thm:stopping\]]{#thm:stopping label="thm:stopping"} For $0\leq t<m$, $$\label{eq:tail}
 \mathbb P(T>t)=s_t.$$ Consequently, $$\label{eq:mass}
 \mathbb P(T=t)=s_{t-1}-s_t\quad(1\leq t<m),
 \qquad
 \mathbb P(T=m)=s_{m-1}.$$ The maximal-count atom is the disjoint union of two mechanisms: $$\label{eq:top-atom}
 \mathbb P(T=m)
 =\prod_{i=1}^m r_i
  +\frac1m\sum_{j=1}^m q_j\prod_{i\ne j}r_i
 =\frac{e_{m-1}(r_1,\ldots,r_m)}{m}.$$ In particular, its first term is the all-petal endpoint, while its second term is a final core choice after $m-1$ petal choices.

At unit rates the clock order is a uniform random permutation of $[m]$, independent of the marks. The event $T>t$ says that the first $t$ distinct edges in this order all have petal marks. Averaging $\prod_{i\in A}r_i$ over the $\binom mt$ possible first-edge sets gives [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}, and differencing tails gives [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"} below the top atom. For $T=m$, either all $m$ marks are petals, or a unique edge $j$ is last in the uniform order, its mark is core, and all other marks are petals. This gives the first equality in [\[eq:top-atom\]](#eq:top-atom){reference-type="eqref" reference="eq:top-atom"}. Substituting $q_j=1-r_j$ reduces it to $m^{-1}\sum_j\prod_{i\ne j}r_i=e_{m-1}/m=s_{m-1}$.

[\[cor:moments\]]{#cor:moments label="cor:moments"} The probability generating function and first two moments are $$\begin{aligned}
 G(z)&=\sum_{t=1}^{m-1}(s_{t-1}-s_t)z^t+s_{m-1}z^m,
 \label{eq:pgf}\\
 \mathbb ET&=\sum_{t=0}^{m-1}s_t,\label{eq:mean}\\
 \mathbb ET^2&=\sum_{t=0}^{m-1}(2t+1)s_t,\label{eq:second}\\
 \mathop{\mathrm{Var}}(T)&=\sum_{t=0}^{m-1}(2t+1)s_t-
 \left(\sum_{t=0}^{m-1}s_t\right)^2.\label{eq:variance}\end{aligned}$$

Equation [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"} is the mass formula [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}. For every positive integer-valued $T\leq m$, $T=\sum_{t=0}^{m-1}\mathbf 1_{\{T>t\}}$ and $T^2=\sum_{t=0}^{m-1}(2t+1)\mathbf 1_{\{T>t\}}$. Taking expectations and using [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} proves [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}--[\[eq:variance\]](#eq:variance){reference-type="eqref" reference="eq:variance"}.

The heterogeneity is visible in every $e_t$: replacing the $r_i$ by their mean generally changes all terms of degree at least two and does not preserve the endpoint law.

# Disjoint sunflower forests

Let $H_1,\ldots,H_d$ be vertex-disjoint sunflower components, each with its own positive parameters and fixed edge rates. The global scheduler chooses among all active edges with probability proportional to their rates. Write $R_a,T_a$, and $G_a$ for the recorded endpoint, discrete choice count, and choice-count PGF in component $a$; write $R$ and $T$ for the forest quantities.

[\[thm:forest\]]{#thm:forest label="thm:forest"} For arbitrary positive fixed rates, $$\label{eq:forest}
 \mathcal L(R)=\bigotimes_{a=1}^d\mathcal L(R_a),
 \qquad
 T=\sum_{a=1}^dT_a,
 \qquad
 G_T(z)=\prod_{a=1}^dG_a(z).$$ Thus the endpoint mass of a forest endpoint is the product of the component masses from Theorem [\[thm:weighted\]](#thm:weighted){reference-type="ref" reference="thm:weighted"} and Corollary [\[cor:vertices\]](#cor:vertices){reference-type="ref" reference="cor:vertices"}; at unit rates each $G_a$ is given by [\[eq:pgf\]](#eq:pgf){reference-type="eqref" reference="eq:pgf"}.

Assign independent clocks and marks to every edge. Each local stopped marked history $(R_a,T_a)$ is a function only of the clocks and marks in $H_a$; hence these pairs are independent. Sorting all clock rings across components gives the global rate-proportional scheduler. Once a core mark stops one component, suppressing its later clocks does not change any local history. The forest records exactly the union of the local records and makes exactly the sum of their choices. Tensorization and multiplication of PGFs follow.

The theorem's content is only the fully marked stopped consequence for this process. Independence/dissociation of disjoint exponential-order restrictions is generic and receives no novelty credit.

Continuous elapsed absorption time is not analyzed here. If one equips the forest with the exponential embedding above and writes $S_a$ for component $a$'s continuous stopping time, then the whole forest completes at $S=\max_a S_a$, not at $\sum_a S_a$; no wall-clock convolution is claimed.

# Exact controls and limitations

The accompanying self-contained Python program uses only integers and `fractions.Fraction`. It performs no sampling or floating-point calculation. It recursively enumerates the process and compares every mass with the displayed formulas. The frozen scope is:

  lane                        parameter range                                                   inputs
  --------------------------- --------------------------------------------------------------- --------
  unit-rate aggregate         $c\in\{1,2,3\}$, $m\in\{1,\ldots,5\}$, $p_i\in\{1,\ldots,4\}$       4092
  weighted aggregate          $c\in\{1,2\}$, $m\in\{1,2,3\}$, $p_i,\lambda_i\in\{1,2,3\}$         1638
  unit-rate actual vertices   $c\in\{1,2\}$, $m\in\{1,2,3\}$, $p_i\in\{1,2,3\}$                     78
  two-component forests       three unit-rate and one weighted control                               4

These are falsification controls, not proofs. In particular, the program does not exhaust weighted vertex-resolved endpoints or arbitrary forests; those claims follow from the all-parameter arguments above. The bounded owner search located the direct process and ordering owners already subtracted, but did not locate this complete conjunction. That non-hit is not a novelty certificate, and a direct package owner would supersede the present positioning.

# Conclusion

On a heterogeneous sunflower, the marked size-biased order separates the recorded-transversal problem into a weighted endpoint integral, independent actual marks, and---at unit rates---an elementary-symmetric choice-count law. On vertex-disjoint components, these marked stopped laws tensorize. The result is a complete exact atlas for a sharply restricted owned process, not a new covering algorithm, ordering method, or independence principle.
