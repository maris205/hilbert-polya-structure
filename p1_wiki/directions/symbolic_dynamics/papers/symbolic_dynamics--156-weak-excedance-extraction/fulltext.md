---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--156-weak-excedance-extraction"
canonical_tex: "symbolic_dynamics/papers/156-weak-excedance-extraction/main.tex"
canonical_pdf: "symbolic_dynamics/papers/156-weak-excedance-extraction/main.pdf"
source_sha256: "a698842b1877a27baaf79be35069a54a00ead9000b29c5bdd897a798de52ec63"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Weak-Excedance Extraction: Exact Images, Ferrers Fibres, and Fibonacci Right-Inverse Towers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/156-weak-excedance-extraction>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/156-weak-excedance-extraction/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/156-weak-excedance-extraction/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/156-weak-excedance-extraction/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/156-weak-excedance-extraction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a permutation $\pi=\pi_1\cdots\pi_n$, retain the letters satisfying $\pi_i\ge i$ and standardize them in their original order. We study the resulting rank-changing permutation map. If $\sigma\in\mathfrak S_m$ and $d(\sigma)=\max_i(i-\sigma_i)$, then $\sigma$ occurs from source rank $n$ if and only if $n\ge m+d(\sigma)$; a high-shift/low-tail section realizes every admissible rank. We also give an exact fibre formula for every target as a sum of deficient Ferrers-board completion counts. The only recurrent states are identities. On nonidentity targets, iterating the minimum-rank section produces an inverse ray whose rank and maximum drop evolve by $(m,d)\mapsto(m+d,m)$, hence by Fibonacci matrix powers. This is a local one-step minimality theorem, not a global minimum theorem for iterated preimages and not a maximum absorption clock. Classical weak-excedance, bounded-drop, tableau, Bruhat, and Bell-enumeration results are explicitly subtracted. An exact audit executes $3{,}689{,}489$ assertions, including explicit rank-boundary tests and a counterexample to a withdrawn pointwise clock claim.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Weak-Excedance Extraction:\
  Exact Images, Ferrers Fibres, and Fibonacci Right-Inverse Towers
```

## Markdown 正文

# Map, scope, and main theorem {#sec:setup}

Let $\mathfrak S_n$ be the permutations of $[n]$ in one-line notation. If $v$ is a word of distinct integers, write $\operatorname{std}(v)$ for its standardization. Define $$\label{eq:map}
 \mathsf W(\pi)=\operatorname{std}(\pi_i:\pi_i\ge i),
 \qquad \pi\in\mathfrak S_n,$$ where the retained letters stay in their original order. Position one is always retained, so [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is a self-map of $\mathfrak S_{\le N}=\bigsqcup_{1\le n\le N}\mathfrak S_n$ for every $N\ge1$. Put $$\label{eq:drop}
 d(\sigma)=\max_{1\le i\le m}(i-\sigma_i),
 \qquad \sigma\in\mathfrak S_m.$$ This is the classical maximum-drop statistic.

The static ownership boundary is deliberately broad. Excedance-set enumeration is due to Ehrenborg--Steingrímsson [@EhrenborgSteingrimsson2000]; bounded maximum drop and its enumerators are treated by Chung--Claesson--Dukes--Graham [@ChungClaessonDukesGraham2010] and Chen--Chen [@ChenChen2016]; permutation-tableau structure is developed by Steingrímsson--Williams [@SteingrimssonWilliams2005]; and Bergeron--Gagnon organize weak-excedance position/value classes through a Bruhat quotient [@BergeronGagnon2023]. All of those static statistics, distributions, and structures receive zero contribution credit here.

There is also an exact collision at the identity aggregate. Beyene--Backelin--Mantaci--Fufa, using the transposition-array interface of Baril [@Baril2007; @Baril2013], prove that permutations whose weak-excedance-letter subword is increasing are Bell-number enumerated [@BeyeneBackelinMantaciFufa2023 Theorem 27]. In the notation below this owns $$\label{eq:bell-owned}
 \sum_{m=1}^n |\mathsf W_n^{-1}(\mathrm{id}_m)|=B_n.$$ Equation [\[eq:bell-owned\]](#eq:bell-owned){reference-type="eqref" reference="eq:bell-owned"} and its transposition-array proof are not claimed. Our fibre formula retains both the target permutation and its rank, including nonidentity targets. Generic Ferrers-board matching is likewise background; the residual is the conjunction of the literal extraction map, its exact target obstruction and sections, its target-resolved fibres, and the dynamics of one canonical right inverse. A bounded exact-map search non-hit is not evidence of novelty, priority, or clearance.

For $n\ge m$, write $h=n-m$. For $A=\{a_1<\cdots<a_m\}$ and $P=\{p_1<\cdots<p_m\}$ contained in $[n]$, call $(A,P)$ *$\sigma$-admissible* if $$\label{eq:admissible}
 p_i\le a_{\sigma_i}\quad(1\le i\le m).$$

Let $B=[n]\setminus A$ and $Q=[n]\setminus P=\{q_1<\cdots<q_h\}$, and put $$\label{eq:completion}
 K(B,Q)=\prod_{j=1}^h
 \left(|\{b\in B:b<q_j\}|-(j-1)\right),$$ interpreted as zero if any factor is nonpositive; when $h=0$, the empty product is $1$.

[\[thm:main\]]{#thm:main label="thm:main"} Let $\sigma\in\mathfrak S_m$.

1.  [\[it:image\]]{#it:image label="it:image"} For every $n\ge m$, $$\label{eq:image}
     \sigma\in\mathsf W(\mathfrak S_n)\quad\Longleftrightarrow\quad
     n\ge m+d(\sigma).$$ Whenever $h=n-m\ge d(\sigma)$, the explicit right section is $$\label{eq:section}
     R_n(\sigma)=(\sigma_1+h,\ldots,\sigma_m+h,1,\ldots,h).$$ Thus $m+d(\sigma)$ is the exact minimum source rank.

2.  [\[it:fibre\]]{#it:fibre label="it:fibre"} For every source rank $n\ge1$, $$\label{eq:fibre}
     |\mathsf W_n^{-1}(\sigma)|
     =\begin{cases}
     0,&1\le n<m,\\
     \displaystyle\sum_{(A,P)\ \sigma\text{-admissible}}
     K([n]\setminus A,[n]\setminus P),&n\ge m.
     \end{cases}$$ This includes zero fibres. At the same rank $n=m$, the fibre has size one for $\sigma=\mathrm{id}_m$ and zero otherwise.

3.  [\[it:recurrent\]]{#it:recurrent label="it:recurrent"} $\mathsf W(\pi)=\pi$ if and only if $\pi$ is an identity. Every nonidentity step strictly lowers rank; hence the recurrent states of $\mathfrak S_{\le N}$ are $\mathrm{id}_1,\ldots,\mathrm{id}_N$.

4.  [\[it:tower\]]{#it:tower label="it:tower"} Suppose $\sigma$ is nonidentity, put $d=d(\sigma)>0$, and define $\sigma^{(0)}=\sigma$ and $$\label{eq:canonical}
     \sigma^{(t+1)}=R_{m_t+d_t}(\sigma^{(t)}),
     \qquad m_t=|\sigma^{(t)}|,\quad d_t=d(\sigma^{(t)}).$$ Then $$\label{eq:update}
     (m_{t+1},d_{t+1})=(m_t+d_t,m_t),
     \qquad \mathsf W(\sigma^{(t+1)})=\sigma^{(t)}.$$ With $F_0=0,F_1=1$, for every $t\ge1$, $$\label{eq:fibonacci}
     m_t=F_{t+1}m+F_t d,\qquad
     d_t=F_t m+F_{t-1}d.$$ Every edge of this inverse ray has minimum possible one-step source rank. If $\tau$ is the first hitting time of an identity, then $$\label{eq:tail-shift}
     \tau(\sigma^{(t)})=\tau(\sigma)+t.$$

Part [\[it:tower\]](#it:tower){reference-type="ref" reference="it:tower"} says *locally minimum*: each individual lift uses a minimum-rank preimage of its immediate target. It does not assert that the composite tower minimizes rank among all $t$-step preimages.

# Images and deficient completions {#sec:inverse}

Suppose $\pi\in\mathfrak S_n$ maps to $\sigma\in\mathfrak S_m$. Let $P=\{p_1<\cdots<p_m\}$ be its selected positions, and let $A=\{a_1<\cdots<a_m\}$ be its selected values. Standardization forces the entry at $p_i$ to be $a_{\sigma_i}$. Selection gives $$\label{eq:chain}
 i\le p_i\le a_{\sigma_i}.$$ Since only $h=n-m$ values lie outside $A$, the $j$th selected value satisfies $a_j\le h+j$. Applying this to [\[eq:chain\]](#eq:chain){reference-type="eqref" reference="eq:chain"} yields $$i\le h+\sigma_i,\qquad i-\sigma_i\le h.$$ Taking the maximum proves $d(\sigma)\le h$, hence necessity in [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

Conversely, suppose $h\ge d(\sigma)$ and use [\[eq:section\]](#eq:section){reference-type="eqref" reference="eq:section"}. Its first $m$ entries satisfy $\sigma_i+h\ge i$ and are therefore selected. Its final entry $j$ occurs at position $m+j>j$ and is deficient. Hence the selected word is exactly the shifted copy $(\sigma_1+h,\ldots,\sigma_m+h)$, whose standardization is $\sigma$. This proves the section identity and the sharp threshold.

If $n<m$, a rank-$n$ source cannot produce a rank-$m$ target, so the fibre is empty. Assume henceforth that $n\ge m$. Fix selected sets $A$ and $P$. The selected assignment is forced: $p_i$ receives $a_{\sigma_i}$. It consists of weak excedances exactly when [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"} holds. It remains to biject the complement values $B$ onto the complement positions $Q$ so that each value assigned at $q_j$ is strictly smaller than $q_j$.

Process $q_1,\ldots,q_h$ increasingly. At $q_j$ there are $|\{b\in B:b<q_j\}|$ eligible complement values. Every one of the $j-1$ previously assigned values is among them, because it was assigned at an earlier position $q_k<q_j$ and is smaller than $q_k$. Therefore the number of choices at step $j$ is precisely the $j$th factor of [\[eq:completion\]](#eq:completion){reference-type="eqref" reference="eq:completion"}. The product counts all deficient complement assignments, with a nonpositive factor correctly giving zero.

Every source determines one unique pair $(A,P)$ and one such complement assignment. Conversely, the forced selected assignment and any deficient completion give a unique source whose selected standardized word is $\sigma$. The classes are disjoint, so summing proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. When $n=m$, both complements are empty and $K(\varnothing,\varnothing)=1$. The sole pair $A=P=[m]$ is admissible exactly when $i\le\sigma_i$ for every $i$, which by equality of coordinate sums holds exactly for $\sigma=\mathrm{id}_m$. This proves the same-rank boundary.

Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is a Ferrers-board product in elementary form: at each increasing complement position, it counts the unused values lying strictly below the diagonal. Summing it over identity targets recovers the owned Bell aggregate [\[eq:bell-owned\]](#eq:bell-owned){reference-type="eqref" reference="eq:bell-owned"}; that consistency check does not transfer ownership of the rank- and target-resolved formula.

# Forward absorption and the canonical inverse ray {#sec:dynamics}

If $\mathsf W(\pi)$ has the same rank as $\pi\in\mathfrak S_n$, every position was selected, so $\pi_i\ge i$ for all $i$. But $\sum_i\pi_i=\sum_i i$; hence equality holds term by term and $\pi=\mathrm{id}_n$. Identities are fixed. Thus every nonidentity step strictly lowers positive integer rank, proving both absorption and the recurrent classification.

For a nonidentity $\sigma$, $d(\sigma)>0$: otherwise $\sigma_i\ge i$ for every $i$, and the preceding sum argument would make $\sigma$ an identity. The minimum-rank section in [\[eq:canonical\]](#eq:canonical){reference-type="eqref" reference="eq:canonical"} is therefore a genuine rank increase.

Apply Part [\[it:image\]](#it:image){reference-type="ref" reference="it:image"} with $h=d_t$. It gives the right-section identity in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} and proves that $m_t+d_t$ is the minimum rank of any one-step preimage of $\sigma^{(t)}$.

The first $m_t$ entries of the section have the form $\sigma^{(t)}_i+d_t$. Their drop is $$i-(\sigma^{(t)}_i+d_t)\le d_t-d_t=0.$$ The final low value $j$ occurs at position $m_t+j$ and has drop exactly $m_t$. Consequently $d_{t+1}=m_t$, while the rank is visibly $m_{t+1}=m_t+d_t$. This proves the resource update.

Writing the update as multiplication by $\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)$ and using its standard Fibonacci powers proves [\[eq:fibonacci\]](#eq:fibonacci){reference-type="eqref" reference="eq:fibonacci"} by induction. Finally, the lifted state makes one step to its immediate target and is nonrecurrent; therefore each lift increases the identity hitting time by exactly one, which proves [\[eq:tail-shift\]](#eq:tail-shift){reference-type="eqref" reference="eq:tail-shift"}.

For example, starting from $21$ gives resource pairs $$(m_t,d_t)=(2,1),(3,2),(5,3),(8,5),(13,8),\ldots.$$ The Fibonacci sequence here describes a chosen backward dynamical system. It does not by itself bound all forward orbits at a fixed rank.

# Exact control, exclusions, and declarations {#sec:control}

The accompanying deterministic verifier enumerates all $409{,}113$ permutations through rank nine, reconstructs the literal functional graph, and checks the image theorem in $99{,}451$ target/rank cells. It compares [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} with literal predecessor counts for all $6{,}985$ target cells through source rank seven, then separately checks $316{,}646$ cells with $n<m$ and all $46{,}233$ same-rank cells through target rank eight. It also recovers the owned Bell aggregate. Finally, it takes every one of the $46{,}225$ nonidentity targets through rank eight through six exact section lifts and checks [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}--[\[eq:tail-shift\]](#eq:tail-shift){reference-type="eqref" reference="eq:tail-shift"}. The frozen transcript records $3{,}689{,}489$ exact assertions and ends in `PASS`. These computations are falsification pressure, not proofs of the all-rank statements.

#### Limitations and withdrawn clock claims.

No maximum absorption clock is claimed. In particular, the tempting pointwise inequality $$\tau(\mathsf W(\pi))\le
 \max_{\rho\in\mathfrak S_{d(\pi)}}\tau(\rho)$$ is false: for $$\pi=(11,10,9,4,1,2,3,8,5,6,7)$$ one has $d(\pi)=4$, while $\mathsf W(\pi)=(5,4,3,1,2)$ has tail three and the maximum tail in $\mathfrak S_4$ is two. The verifier reproduces this counterexample. The paper also makes no global minimum-rank claim for $t$-step preimages and does not infer a fixed-rank maximum from the Fibonacci inverse ray. The broad carrier pattern "extract a subsequence and standardize" receives zero credit; the diagonal predicate, maximum-drop image obstruction, and deficient completion are the specific mechanisms used here.

#### Data availability.

The exact-control source and frozen transcript accompany the internal artifact. They use no external data, runtime network access, random sampling, or nonstandard Python package.

#### Ethics statement.

This mathematical study involves no human participants, animals, personal data, or field intervention.

#### Author contributions.

The anonymous author is responsible for the definitions, proofs, software, source audit, and manuscript.

#### Conflict of interest.

The author declares no conflict of interest.

#### Funding.

No external funding is declared.

#### External status.

This anonymous manuscript is an internal artifact under `HOLD_EXTERNAL`. Posting, submission, external circulation, and specialist or author contact remain unauthorized.
