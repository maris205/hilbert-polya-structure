---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--68-complete-bipartite-homshift-conjugacies"
canonical_tex: "symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies/main.tex"
canonical_pdf: "symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies/main.pdf"
source_sha256: "60cca40aa4a91db684e0d628fa4799bf1ce4f98af806e4bcfbc09d6a32dddc83"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Product Classification and Phase Rigidity for Complete-Bipartite Hom-Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/68-complete-bipartite-homshift-conjugacies/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $K_{m,n}$ be the complete bipartite graph with nonempty parts of sizes $m$ and $n$, and let $X_{m,n}^{(d)}=\operatorname{Hom}(\mathbb Z^d,K_{m,n})$. We give a complete conjugacy classification inside this two-sided family: for every $d\geq 1$, $X_{m,n}^{(d)}$ and $X_{r,s}^{(d)}$ are topologically conjugate as $\mathbb Z^d$-systems if and only if $mn=rs$. Sufficiency is implemented by an explicit radius-one dimer code. The code uses the configuration's intrinsic checkerboard phase to pair sites in one coordinate direction, so it commutes with every translation and has an equally local inverse.

  For $d\geq1$ we also determine the finite-dependence obstruction for every subgroup action. Every finitely dependent probability carried by the hom-shift has deterministic checkerboard phase. Consequently an $L$-invariant finitely dependent probability exists exactly when $L$ lies in the even-parity subgroup, and no finitely dependent probability has full support on both phase components. Exact finite-pattern and finite-index periodic-point formulae accompany these results. Finally, for an arbitrary one-site potential we compute the pressure and the unique full-action equilibrium state. These statements isolate which information is removed by two-sided dimer recoding and which information remains rigid under translation invariance.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 25 August 2026'
title: 'Product Classification and Phase Rigidity for Complete-Bipartite Hom-Shifts'
```

## Markdown 正文

# Introduction

Graph-homomorphism shifts form a concrete class of nearest-neighbour shifts of finite type. Their mixing behaviour can reflect detailed graph geometry [@ChandgotiaMarcus2018], and even apparently elementary target graphs can retain global information. A complete bipartite target is the cleanest example: every valid configuration chooses one of two checkerboard orientations, after which all colours at distinct sites are unconstrained. That phase description and its maximal-entropy consequence are publicly recorded in lecture notes on hom-shifts [@Chandgotia2019Lectures]. They are background here, not a paper claim.

The elementary phase picture leaves a less elementary coding question. Does a conjugacy remember the two part sizes separately, or only their product? A symbol permutation remembers the unordered pair $\{m,n\}$, but a two-sided block code can pair adjacent sites and move information between the two parity classes. We prove that this extra memory collapses the classification precisely to $mn$. The construction is explicit and works for every $\mathbb Z^d$ action with $d\geq1$.

The same global phase has a different effect on stochastic dependence. A finitely dependent process makes sufficiently remote coordinates independent, whereas the phase variable is copied unchanged at all sites of one lattice parity. This forces the phase to be deterministic without any invariance assumption. Subgroup invariance can therefore coexist with finite dependence exactly when the subgroup preserves parity. This sharp dichotomy is not an application of the four-cycle-free obstruction of @ChandgotiaThorat2026: $K_{m,n}$ contains four-cycles whenever $m,n\geq2$.

The paper establishes four linked contracts with a definite hierarchy. The central contract is the product conjugacy classification and its explicit two-sided dimer code. The intrinsic-phase lemma is the mechanism supporting that code. Exact pattern and entropy formulae, the finite-dependence dichotomy, one-site pressure and equilibrium, and periodic data are complementary packages that delimit and test the central classification.

1.  We count every globally extendible finite pattern from the single checkerboard phase and obtain $h_{\rm top}(X_{m,n}^{(d)})=\frac12\log(mn)$.

2.  We construct mutually inverse radius-one dimer codes and prove $$X_{m,n}^{(d)}\cong X_{r,s}^{(d)}\quad\Longleftrightarrow\quad mn=rs.$$

3.  We classify the subgroups supporting invariant finitely dependent probabilities and separate "carried by $X$" from "having support equal to $X$".

4.  We compute all finite-index fixed-point counts and the pressure and equilibrium state for every one-site potential.

One-sided hom-shift conjugacy uses a different coding category and is studied through Williams-type amalgamation methods by @BealBlockGorman2025. Our dimer inverse uses a neighbour on the opposite side of the origin and should not be read as a statement about that category. More generally, this paper classifies only the displayed complete-bipartite family; it does not classify arbitrary hom-shifts or arbitrary bipartite targets.

records the exact phase and pattern structure. proves the dimer classification. treats finite dependence, and [5](#sec:pressure){reference-type="ref" reference="sec:pressure"} gives the thermodynamic package. Periodic data and the source boundary appear in [\[sec:periodic,sec:scope\]](#sec:periodic,sec:scope){reference-type="ref" reference="sec:periodic,sec:scope"}.

# Phase decomposition and exact pattern counts {#sec:phase}

Fix disjoint sets $A$ and $B$ with $|A|=m$ and $|B|=n$. The graph $K_{m,n}$ has vertex set $A\sqcup B$ and every edge joins $A$ to $B$. Write $$X_{m,n}^{(d)}=\{x\in(A\sqcup B)^{\mathbb Z^d}:x_v\sim x_{v+e_i}
 \text{ for all }v\in\mathbb Z^d,\ 1\leq i\leq d\}.$$ Let $$\chi(v)=v_1+\cdots+v_d\pmod 2,
 \qquad \mathcal E=\ker\chi,
 \qquad \mathcal O=\mathbb Z^d\setminus\mathcal E.$$

[\[lem:phase\]]{#lem:phase label="lem:phase"} Every $x\in X_{m,n}^{(d)}$ has exactly one of the following orientations: $$x_{\mathcal E}\subset A,\quad x_{\mathcal O}\subset B,
\qquad\text{or}\qquad
x_{\mathcal E}\subset B,\quad x_{\mathcal O}\subset A.$$ If $\omega(x)=1$ in the first case and $-1$ in the second, then $\omega(\sigma^v x)=(-1)^{\chi(v)}\omega(x)$.

Choose the part containing $x_0$. Along every nearest-neighbour edge the part changes. The parity of the length of a lattice path from $0$ to $v$ is $\chi(v)$, so the part at $v$ is forced and is independent of the chosen path. Translation by an odd vector exchanges the two parity classes, while translation by an even vector preserves them.

[\[prop:patterns\]]{#prop:patterns label="prop:patterns"} The number $N_{m,n}(F)$ of patterns on a finite set $F$ that extend to $X_{m,n}^{(d)}$ satisfies $N_{m,n}(\varnothing)=1$. For nonempty $F$ it is $$N_{m,n}(F)=
 m^{|F\cap\mathcal E|}n^{|F\cap\mathcal O|}
 +n^{|F\cap\mathcal E|}m^{|F\cap\mathcal O|}.
 \tag{2.1}\label{eq:finite-count}$$ In particular, $$h_{\rm top}(X_{m,n}^{(d)})=\frac12\log(mn).
 \tag{2.2}\label{eq:entropy}$$

The empty restriction is unique. If $F$ is nonempty, the two alternatives in [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"} are disjoint on $F$. In the first phase the sites in $F\cap\mathcal E$ have $m$ choices and those in $F\cap\mathcal O$ have $n$ choices; the second phase reverses the roles. Every such restriction extends: choose arbitrary symbols from the phase-prescribed target part at every site outside $F$. Completeness of the bipartite target makes the resulting global configuration valid. Summing the two phase counts proves [\[eq:finite-count\]](#eq:finite-count){reference-type="eqref" reference="eq:finite-count"}.

Take rectangular Følner boxes. They are connected and their two parity classes have sizes $|F|/2+O(1)$. Applying [\[eq:finite-count\]](#eq:finite-count){reference-type="eqref" reference="eq:finite-count"}, taking $|F|^{-1}\log$, and passing to the limit gives [\[eq:entropy\]](#eq:entropy){reference-type="eqref" reference="eq:entropy"}.

The global choice of phase contributes only a bounded factor, while each even--odd pair contributes $mn$ choices. Importantly, disconnected pieces of $F$ cannot choose phases independently: global extendibility couples them through [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"}. The conjugacy in the next section makes that pairing local.

Let $X^+$ be the phase component with $A$ on $\mathcal E$, and let $X^-$ be the other component. Although neither component is invariant under the full $\mathbb Z^d$ action, both are invariant under the subgroup $\mathcal E$.

[\[prop:phase-full\]]{#prop:phase-full label="prop:phase-full"} As an $\mathcal E$-system, $X^+$ is conjugate to the full shift $(A\times B)^{\mathcal E}$. The map is $$\Theta_+(x)_v=(x_v,x_{v+e_1}),\qquad v\in\mathcal E.
 \tag{2.3}\label{eq:phase-pair}$$ The component $X^-$ has the same full-shift model after translating the anchors by $e_1$.

The edges $(v,v+e_1)$ with $v\in\mathcal E$ are disjoint and cover $\mathbb Z^d$. Consequently [\[eq:phase-pair\]](#eq:phase-pair){reference-type="eqref" reference="eq:phase-pair"} records every input coordinate exactly once. Conversely, an arbitrary labelling of $\mathcal E$ by $A\times B$ can be unpacked independently on these dimers and gives a valid point of $X^+$, because every lattice edge joins an $A$ symbol to a $B$ symbol. Packing and unpacking are continuous and commute with translations in $\mathcal E$. For $X^-$, the $A$-anchors form the coset $e_1+\mathcal E$; translating this coset back to $\mathcal E$ gives the identical construction.

An odd translation exchanges $X^+$ and $X^-$. It follows that every full-action invariant probability is the equal mixture of an $\mathcal E$-invariant probability on one component and its odd translate. This observation will turn the equilibrium problem into the ordinary full-shift variational problem on the dimer alphabet.

# The dimer conjugacy classification {#sec:conjugacy}

Let $K_{r,s}$ have parts $A'$ and $B'$. The main construction needs only a bijection between two dimer alphabets.

[\[thm:classification\]]{#thm:classification label="thm:classification"} For $d\geq1$ and positive integers $m,n,r,s$, the following are equivalent.

1.  $X_{m,n}^{(d)}$ and $X_{r,s}^{(d)}$ are topologically conjugate as $\mathbb Z^d$-systems.

2.  $mn=rs$.

When $mn=rs$, there is a conjugacy whose local rule and inverse local rule have memory set contained in $\{-e_1,0,e_1\}$ (equivalently, radius one). At a site $v$, membership in a target part selects which one of the two $e_1$-neighbours is inspected together with $v$.

Suppose first that $mn=rs$ and fix a bijection $$f:A\times B\longrightarrow A'\times B'.$$ For $x\in X_{m,n}^{(d)}$ define $y=\Phi_f(x)$ sitewise. If $x_v\in A$, write $$f(x_v,x_{v+e_1})=(a'_v,b'_v)
 \quad\text{and set}\quad y_v=a'_v.
 \tag{3.1}\label{eq:dimer-a}$$ If $x_v\in B$, then $x_{v-e_1}\in A$; write $$f(x_{v-e_1},x_v)=(a'_{v-e_1},b'_{v-e_1})
 \quad\text{and set}\quad y_v=b'_{v-e_1}.
 \tag{3.2}\label{eq:dimer-b}$$ Thus each $A$-site anchors the oriented dimer $(v,v+e_1)$ and both output symbols are obtained from the same application of $f$. The dimers partition the lattice because the $A$-sites form exactly one parity class. Moreover $y_v\in A'$ exactly when $x_v\in A$, so adjacent output symbols lie in opposite target parts. Hence $y\in X_{r,s}^{(d)}$.

The rule uses membership in $A$, which is visible in the input symbol, and not an absolute choice of lattice parity. Therefore translating the input translates the anchored dimers and $\Phi_f\sigma^u=\sigma^u\Phi_f$ for every $u\in\mathbb Z^d$. Continuity is immediate from [\[eq:dimer-a\]](#eq:dimer-a){reference-type="eqref" reference="eq:dimer-a"}--[\[eq:dimer-b\]](#eq:dimer-b){reference-type="eqref" reference="eq:dimer-b"}. Repeating the same construction with $f^{-1}:A'\times B'\to A\times B$ gives a map $\Phi_{f^{-1}}$. On every anchored dimer the two maps apply $f$ and then $f^{-1}$, so both compositions are the identity. This proves sufficiency.

Conversely, topological entropy is invariant under topological conjugacy. By [\[prop:patterns\]](#prop:patterns){reference-type="ref" reference="prop:patterns"}, a conjugacy forces $\frac12\log(mn)=\frac12\log(rs)$, hence $mn=rs$.

Pairing all geometric edges $(v,v+e_1)$ using a fixed parity origin would not commute with odd translations. Equations [\[eq:dimer-a\]](#eq:dimer-a){reference-type="eqref" reference="eq:dimer-a"} and [\[eq:dimer-b\]](#eq:dimer-b){reference-type="eqref" reference="eq:dimer-b"} instead let the configuration select the anchors. The phase cocycle from [\[lem:phase\]](#lem:phase){reference-type="ref" reference="lem:phase"} is exactly what makes the dimerization translation-equivariant.

[\[cor:many-presentations\]]{#cor:many-presentations label="cor:many-presentations"} For every $q\geq1$, all systems $X_{m,n}^{(d)}$ with $mn=q$ are conjugate. Whenever $q$ has distinct unordered factor pairs, this gives presentations with different part sizes; for example, $X_{2,6}^{(d)}\cong X_{3,4}^{(d)}$.

The conclusion is deliberately two-sided. The one-sided category lacks the same symmetric access to the dimer containing a site and is governed by one-sided amalgamation theory [@BealBlockGorman2025].

# Finite dependence under subgroup actions {#sec:fd}

A probability $\mu$ on $(A\sqcup B)^{\mathbb Z^d}$ is $k$-dependent if the coordinate sigma-algebras over finite sets $U,V$ are independent whenever $\mathop{\mathrm{dist}}(U,V)>k$. It is finitely dependent if it is $k$-dependent for some $k$. We say that $\mu$ is carried by $X$ when $\mu(X)=1$; this does not mean that its topological support equals $X$.

[\[thm:fd\]]{#thm:fd label="thm:fd"} Let $d\geq1$ and let $\mu$ be a finitely dependent probability carried by $X_{m,n}^{(d)}$.

1.  The phase $\omega$ is $\mu$-almost surely constant.

2.  Consequently $\operatorname{supp}\mu$ is contained in one phase component, so no finitely dependent probability has support equal to all of $X_{m,n}^{(d)}$.

3.  For a subgroup $L\leq\mathbb Z^d$, an $L$-invariant finitely dependent probability carried by $X_{m,n}^{(d)}$ exists if and only if $L\leq\mathcal E$. When $L\leq\mathcal E$, it may be chosen $0$-dependent with full support on either phase component.

Assume that $\mu$ is $k$-dependent and set $I_v=\mathbf 1_{\{x_v\in A\}}$. For every even vector $u\in\mathcal E$, the phase lemma gives $I_u=I_0$ on all of $X_{m,n}^{(d)}$. Choose $u\in\mathcal E$ with $\lVert u\rVert_1>k$. Then $I_0$ and $I_u$ are independent, but they are equal almost surely. If $p=\mathbb P(I_0=1)$, this gives $$p=\mathbb P(I_0=1,I_u=1)=p^2.$$ Thus $p\in\{0,1\}$ and the phase is deterministic. The two phase components are disjoint clopen sets, so the support assertion follows.

If $L$ contains an odd vector $\ell$, then $\sigma^\ell$ exchanges the two phases. An $L$-invariant law would assign them equal probabilities, which contradicts deterministic phase. Hence $L\leq\mathcal E$ is necessary.

For sufficiency, fix one phase. Give all sites in its $A$ parity class independent samples from a fully supported probability on $A$, and give all sites in its $B$ parity class independent samples from a fully supported probability on $B$. All coordinates are independent, so the law is $0$-dependent. Every element of $\mathcal E$, and hence every element of $L$, preserves the two parity classes. The law is $L$-invariant and its support is the chosen phase component.

For $d\geq2$, @ChandgotiaThorat2026 prove a broad nonexistence theorem for hom-shifts into finite four-cycle-free graphs. Complete bipartite graphs with both parts of size at least two sit outside that hypothesis. Here the outcome is instead mixed: full $\mathbb Z^d$ invariance is impossible for finite dependence, while the index-two even subaction admits an independent law.

# One-site pressure and equilibrium states {#sec:pressure}

Let $\varphi:A\sqcup B\to\mathbb R$ be a one-site potential and abbreviate $$Z_A(\varphi)=\sum_{a\in A}e^{\varphi(a)},
 \qquad
 Z_B(\varphi)=\sum_{b\in B}e^{\varphi(b)}.$$ Write $q_A(a)=e^{\varphi(a)}/Z_A(\varphi)$ and define $q_B$ analogously.

In statistical-mechanics terms, $X_{m,n}^{(d)}$ is a hard-constraint spin system; its checkerboard orientation is a two-valued sector variable, and $e^{\varphi}$ supplies the single-site activities. Conditioning on a sector removes all residual interactions because the target is complete bipartite, so the remaining spins form independent parity-wise products. The full translation action exchanges the two sectors and therefore forces their equal mixture at equilibrium. For a non-complete bipartite target, conditioning on phase would generally leave constraints between neighbouring dimers, so this reduction would no longer be an independent-spin model.

[\[thm:pressure\]]{#thm:pressure label="thm:pressure"} For every $d\geq1$, $$P_{X_{m,n}^{(d)}}(\varphi)
 =\frac12\bigl(\log Z_A(\varphi)+\log Z_B(\varphi)\bigr).
 \tag{5.1}\label{eq:pressure}$$ There is a unique equilibrium state invariant under the full $\mathbb Z^d$ action: $$\mu_\varphi=\frac12\left(
 \bigotimes_{v\in\mathcal E}q_A\otimes\bigotimes_{v\in\mathcal O}q_B
 +
 \bigotimes_{v\in\mathcal E}q_B\otimes\bigotimes_{v\in\mathcal O}q_A
 \right),
 \tag{5.2}\label{eq:eqstate}$$ where in the second product the symbols $q_A,q_B$ are assigned to the parity classes on which their alphabets occur. At $\varphi=0$, this is the unique full-action measure of maximal entropy.

For every nonempty finite $F$, the weighted sum over globally extendible patterns is $$Z_A(\varphi)^{|F\cap\mathcal E|}Z_B(\varphi)^{|F\cap\mathcal O|}
 +Z_B(\varphi)^{|F\cap\mathcal E|}Z_A(\varphi)^{|F\cap\mathcal O|}.
 \tag{5.3}\label{eq:weighted-count}$$ On rectangular Følner boxes the two parity densities tend to $1/2$. Taking normalized logarithms proves [\[eq:pressure\]](#eq:pressure){reference-type="eqref" reference="eq:pressure"}.

We include the uniqueness argument because it records the role of full-action invariance. By [\[prop:phase-full\]](#prop:phase-full){reference-type="ref" reference="prop:phase-full"}, conditioning on one phase identifies the even-subgroup action with the full shift on $A\times B$. Under this identification, the potential accumulated on one dimer is $\varphi(a)+\varphi(b)$. The full-shift variational problem therefore has partition sum $$\sum_{(a,b)\in A\times B}e^{\varphi(a)+\varphi(b)}
 =Z_A(\varphi)Z_B(\varphi).$$ Its unique equilibrium law is the Bernoulli product with one-dimer marginal $q_A\times q_B$. Indeed, if $p$ is an arbitrary probability on $A\times B$ with marginals $p_A,p_B$, then $$\begin{aligned}
 H(p)+\sum_{a,b}p(a,b)(\varphi(a)+\varphi(b))
 &\leq H(p_A)+H(p_B)
   +\sum_a p_A(a)\varphi(a)+\sum_b p_B(b)\varphi(b)\\
 &\leq \log Z_A(\varphi)+\log Z_B(\varphi).\end{aligned}$$ Equality in the first line forces independence within a dimer, and the two finite-alphabet Gibbs equalities force $p_A=q_A$ and $p_B=q_B$. For an arbitrary invariant process on the dimer full shift, entropy rate is at most the entropy of its one-dimer marginal; equality forces independence across the $\mathcal E$-sites. Thus the dimer Bernoulli law is the unique optimizer.

Every full-action invariant probability gives mass $1/2$ to each phase, since an odd translation exchanges them. Entropy and potential average for the index-two subaction both scale by two relative to their per-$\mathbb Z^d$ values, and the finite phase mixture contributes zero entropy density. Thus the unique dimer Bernoulli equilibrium on one component and its odd translate must occur with equal weights. This is precisely [\[eq:eqstate\]](#eq:eqstate){reference-type="eqref" reference="eq:eqstate"}, and its variational value is the right-hand side of [\[eq:pressure\]](#eq:pressure){reference-type="eqref" reference="eq:pressure"}.

The phase mixture in [\[eq:eqstate\]](#eq:eqstate){reference-type="eqref" reference="eq:eqstate"} is long-range dependent: knowing the target part at one site determines it at every site of the same parity. Thus the equilibrium state is compatible with [\[thm:fd\]](#thm:fd){reference-type="ref" reference="thm:fd"}: it is not finitely dependent, even though each conditional product measure is $0$-dependent.

# Finite-index periodic data {#sec:periodic}

For a finite-index subgroup $L\leq\mathbb Z^d$, let $$\operatorname{Fix}_L(X)=\{x\in X:\sigma^\ell x=x\text{ for every }\ell\in L\}.$$

[\[prop:fix\]]{#prop:fix label="prop:fix"} If $L\not\leq\mathcal E$, then $\operatorname{Fix}_L(X_{m,n}^{(d)})$ is empty. If $L\leq\mathcal E$ and $q=[\mathcal E:L]$, then $$|\operatorname{Fix}_L(X_{m,n}^{(d)})|=2(mn)^q.
 \tag{6.1}\label{eq:fix}$$

An odd period would identify a site with a site in the opposite target part, which is impossible. This proves the first assertion. If $L\leq\mathcal E$, the finite quotient $\mathbb Z^d/L$ has $q$ even cosets and $q$ odd cosets. In one phase, the even cosets have $m$ independent colour choices and the odd cosets have $n$ independent choices, giving $(mn)^q$ configurations. The opposite phase gives another disjoint set of the same size.

Equations [\[eq:entropy\]](#eq:entropy){reference-type="eqref" reference="eq:entropy"} and [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"} show that the usual entropy and every finite-index fixed-point count depend on $(m,n)$ only through $mn$. These invariants therefore agree with, but do not construct, the conjugacies in [\[thm:classification\]](#thm:classification){reference-type="ref" reference="thm:classification"}. The construction supplies the missing mechanism and also explains why the agreement is exact: it recodes one $A$ choice and one $B$ choice as a single dimer symbol.

\@lYY@ Question & Invariant or obstruction & Proof engine\
Conjugacy & product $mn$ & intrinsic dimer block code plus entropy\
Finite dependence & deterministic phase & equality of remote parity events\
Subgroup invariance & $L\leq\mathcal E$ & phase cocycle and parity-wise iid law\
Thermodynamics & $Z_A(\varphi)Z_B(\varphi)$ & weighted pattern sum and Gibbs inequality\
Periodic data & $2(mn)^{[\mathcal E:L]}$ & bipartite quotient count\

# Source boundary and limitations {#sec:scope}

The results above are intentionally narrow. The checkerboard phase and the maximal-entropy product picture for complete-bipartite targets are already visible in public hom-shift lectures [@Chandgotia2019Lectures]; the paper uses them as input structure. General mixing questions for hom-shifts are treated by @ChandgotiaMarcus2018. The recent finite-dependence theorem of @ChandgotiaThorat2026 owns the four-cycle-free obstruction, while our target graphs contain four-cycles. Finally, @BealBlockGorman2025 work in one-sided and tree settings, where conjugacy is organized by one-sided amalgamation rather than the two-sided intrinsic dimer code used here.

Within that subtraction, the manuscript's mathematical load is the product classification with an explicit inverse, together with the exact subgroup finite-dependence and pressure contracts. The finite-pattern, entropy, MME, and phase statements are retained because they close proofs and make the boundaries of the stronger results transparent; none is presented as an isolated headline.

There are three limitations. First, completeness of the bipartite target is essential: it makes colours on different sites independent after the phase is fixed. For a non-complete bipartite graph, a dimer alphabet does not automatically remove constraints between neighbouring dimers. Second, the classification is internal to the family $\{X_{m,n}^{(d)}\}$; it does not say which unrelated SFTs may be conjugate to one of these systems. Third, a bounded source search is not a substitute for a specialist literature audit. Accordingly this draft makes no priority statement and remains on hold for external release.

The companion deterministic control enumerates small finite tori and shapes, distinguishes global restrictions from merely locally admissible disconnected patterns, checks the dimer map and its inverse for $X_{2,6}^{(2)}\cong X_{3,4}^{(2)}$ and the singleton-part boundary $X_{1,6}^{(2)}\cong X_{2,3}^{(2)}$. It also checks the minimal target $K_{1,1}$ and verifies [\[eq:finite-count\]](#eq:finite-count){reference-type="eqref" reference="eq:finite-count"} and [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"} in finite cases. Those computations are regression tests only; every infinite-system assertion is proved above.

# Conclusion

Complete-bipartite hom-shifts retain a global checkerboard phase but allow complete freedom within each phase. A translation-equivariant dimerization converts that freedom into the alphabet $A\times B$, proving that the product $mn$, rather than the two part sizes separately, classifies the family up to two-sided $\mathbb Z^d$ conjugacy. The same phase that enables the code obstructs finite dependence under every subgroup containing an odd translation. Weighted pattern counts then give the full one-site pressure and the unique full-action equilibrium state, while finite quotients give matching periodic data.

The argument suggests a concrete next question without changing the claim of this paper: identify bipartite target graphs for which an intrinsic matching or tiling of the source lattice produces an invertible recoding, and determine which residual inter-dimer constraints survive. Completeness makes that question exactly solvable here.
