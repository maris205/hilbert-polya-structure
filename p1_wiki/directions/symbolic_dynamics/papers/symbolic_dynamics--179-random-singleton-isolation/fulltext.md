---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--179-random-singleton-isolation"
canonical_tex: "symbolic_dynamics/papers/179-random-singleton-isolation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/179-random-singleton-isolation/main.pdf"
source_sha256: "94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Random Singleton Isolation on Set Partitions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/179-random-singleton-isolation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/179-random-singleton-isolation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/179-random-singleton-isolation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/179-random-singleton-isolation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/179-random-singleton-isolation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On a set partition of $[n]$, choose a uniform label and split it from its block as a singleton. We determine this absorbing chain without recursion. The label maps are commuting idempotents, and the transition matrix is diagonalizable with eigenvalue $s/n$ occurring once for every partition having $s$ singleton blocks. For arbitrary initial block sizes we give the all-time absorption distribution as an all-but-one coupon formula. More finely, we give every labelled source--target probability as an exact-support sum and count, for every target, both distinct predecessors and labelled predecessor/action pairs. The impossible $n-1$ singleton layer and all small boundaries are included. Generic partition, coupon, and semigroup-walk ingredients receive zero contribution credit; status is `OWNER_AMBER / HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: Random Singleton Isolation on Set Partitions
```

## Markdown 正文

# The chain and its subtraction boundary

Fix an integer $n\ge1$, and let $\mathcal P_n$ be the set of partitions of $[n]=\{1,\ldots,n\}$. For $i\in[n]$, define $E_i\pi$ by removing $i$ from its block and installing $\{i\}$ as a singleton; if $\{i\}$ is already a block, do nothing. The chain has transition operator $$\label{eq:P}
 P=\frac1n\sum_{i=1}^n E_i,$$ where the same notation denotes the linearization on the basis $\mathcal P_n$.

Set partitions and restricted-growth encodings are classical. More specifically, Knopfmacher--Mansour--Wagner use the local operation of removing a marked element and making it a singleton in a bijective argument [@KMW2010]; that local move receives zero credit here. Stark constructs different arborescence chains generating set partitions, including variants excluding singleton blocks [@Stark2024]. Brown's general work owns semigroup-walk diagonalization technology [@Brown2000]. Accordingly, partition lattices, associated Bell numbers, coupon occupancy, commuting idempotents, and generic spectral technology are background. The retained object is the conjunction, for the literal fixed-$n$ chain [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"}, of the complete spectrum, arbitrary-source absorption law, every-target kernel, and two inverse censuses. A literal or equivalent owner triggers withdrawal; the present bounded non-hit is not a novelty certificate.

The nearest internal carrier collision is P169: it also uses labelled set partitions, but applies a deterministic cyclic successor transfer that preserves block number and supports nontrivial cycles. P110 instead joins a partition with a cyclic relabelling and therefore coarsens. Neither is the support-only singleton-isolation refinement studied here, nor supplies its all-but-one coupon law, labelled target kernel, or inverse counts. Generic refinement, Bell-number, and spectral shells consequently receive no credit.

Write $s(\pi)$ and $b(\pi)$ for the numbers of singleton and total blocks. Let $D_m$ count partitions of $[m]$ with no singleton blocks, with $D_0=1$ and $D_1=0$. We use $S(t,r)$ for a Stirling number of the second kind, including $S(0,0)=1$.

[\[lem:support\]]{#lem:support label="lem:support"} The maps $E_i$ are commuting idempotents. Hence a label history acts only through its support $A\subseteq[n]$, via $E_A=\prod_{i\in A}E_i$. For an initial block $B$, the resulting blocks inside $B$ are the singletons $\{i\}$ for $i\in A\cap B$, together with $B\setminus A$ when that set is nonempty. In particular, a one-label residual remains as a singleton even when that label was never selected.

Idempotence is immediate. If $i\ne j$, extracting $i$ and $j$ from their old blocks leaves the same residual blocks in either order, including the case in which both labels started together. This proves commutation. The block description follows by extracting every label of $A\cap B$; the unextracted residual remains one block whenever it is nonempty, including when its size is one.

The discrete partition $\widehat 0$ is absorbing. Every other state has a nonsingleton block; selecting a label in it strictly increases the singleton set, and no move can reverse that increase. Thus $\widehat0$ is the unique recurrent state.

# Complete spectrum

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The matrix $P$ is diagonalizable over $\mathbb Q$. For $0\le s\le n-2$, the eigenvalue $s/n$ has multiplicity $$\label{eq:mult}
 m_s=\binom ns D_{n-s}.$$ The eigenvalue $1$ has multiplicity one, and there is no eigenvalue $(n-1)/n$. For $n=1$, the spectrum consists only of $1$.

Each linearized $E_i$ is diagonalizable because its minimal polynomial divides $x(x-1)$. A commuting family of diagonalizable operators is simultaneously diagonalizable, so their average $P$ is diagonalizable.

Order $\mathcal P_n$ compatibly with refinement. Every $E_i\pi$ either equals $\pi$ or is strictly finer, so $P$ is triangular. Exactly the $s(\pi)$ choices of a singleton label fix $\pi$; its diagonal entry is therefore $s(\pi)/n$. To make a partition with exactly $s$ singleton blocks, choose their labels and partition the complement with no singleton blocks, giving [\[eq:mult\]](#eq:mult){reference-type="eqref" reference="eq:mult"}. The value $s=n-1$ is impossible: the remaining label is also a singleton. At $s=n$ there is only $\widehat0$, proving all claims.

# All-time laws

Let the initial partition $\pi$ have blocks $B_1,\ldots,B_k$ of sizes $b_1,\ldots,b_k$. For variables $b_1,\ldots,b_k$, let $e_m(b)$ denote the $m$th elementary symmetric polynomial. Let $T$ be the absorption epoch, with $T=0$ when $\pi=\widehat0$.

[\[thm:absorb\]]{#thm:absorb label="thm:absorb"} For every integer $t\ge0$, $$\label{eq:absorb}
 \Pr_\pi(T\le t)=\frac1{n^t}\sum_{m=0}^{k}
 e_m(b_1,\ldots,b_k)(n-m)!S(t,n-m).$$

Let $M$ be the set of labels missing from the first $t$ samples. By Lemma [\[lem:support\]](#lem:support){reference-type="ref" reference="lem:support"}, absorption occurs exactly when $|M\cap B_j|\le1$ for every old block. The number of admissible missing sets of size $m$ is $e_m(b)$: choose $m$ old blocks and one missing label in each. For fixed $M$, the histories having exactly the complementary support are the surjections $[t]\twoheadrightarrow[n]\setminus M$, counted by $(n-m)!S(t,n-m)$. Summing and dividing by $n^t$ proves the formula, including $t=0$.

We next retain the labels of the target. For $M\subseteq[n]$, put $$\label{eq:q}
 q_t(M)=\frac{(n-|M|)!S(t,n-|M|)}{n^t}.$$ Given $\pi$ and $\sigma$, call $M$ *admissible* if, in every old block $B$ of $\pi$, either

(a) $\sigma$ has one nonsingleton block $C\subseteq B$, all other labels of $B$ are singleton, and $M\cap B=C$; or

(b) $\sigma$ is discrete on $B$, and $|M\cap B|\le1$.

If $\sigma$ does not refine $\pi$, or has two nonsingleton blocks inside an old block, there are no admissible sets. Denote the resulting explicit family by $\mathcal M_\pi(\sigma)$.

[\[thm:kernel\]]{#thm:kernel label="thm:kernel"} For all $t\ge0$ and $\pi,\sigma\in\mathcal P_n$, $$\label{eq:kernel}
 P^t(\pi,\sigma)=\sum_{M\in\mathcal M_\pi(\sigma)}q_t(M).$$ Consequently $\sigma$ is eventually reachable from $\pi$ exactly when it has the blockwise extraction form above. It is reachable at exact time $t$ exactly when some admissible $M$ also satisfies $n-|M|=0=t$ or $1\le n-|M|\le t$.

A history with missing set $M$ has exact support $[n]\setminus M$, hence probability $q_t(M)$. Lemma [\[lem:support\]](#lem:support){reference-type="ref" reference="lem:support"} says that its endpoint is $\sigma$ precisely for the displayed blockwise alternatives. Distinct missing sets describe disjoint history events, proving [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}. The positivity criterion is exactly the positivity criterion for $S(t,n-|M|)$.

Formula [\[eq:absorb\]](#eq:absorb){reference-type="eqref" reference="eq:absorb"} is recovered by summing [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} at $\widehat0$, but its elementary-symmetric compression retains the geometry of every initial block size.

# Complete one-step inverse census

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} Fix a target $\sigma$ with $s=s(\sigma)$ and $b=b(\sigma)$. If $s=0$, it has no one-step predecessor. If $s>0$, the number of distinct predecessor partitions is $$\label{eq:predstates}
 1+s(b-s)+\binom{s}{2},$$ whereas the number of labelled pairs $(\rho,i)$ satisfying $E_i\rho=\sigma$ is $$\label{eq:actions}
 sb.$$

The acted-on label must be singleton in the output, proving the zero case. For $s>0$, a predecessor is either $\sigma$ itself, merges one of its $s$ singletons with one of its $b-s$ nonsingleton blocks, or merges two singleton blocks. These disjoint constructions give [\[eq:predstates\]](#eq:predstates){reference-type="eqref" reference="eq:predstates"}. For a labelled pair, first choose the output singleton $i$. Its predecessor is either unchanged or obtained by merging $\{i\}$ with any one of the other $b-1$ blocks: exactly $b$ choices per $i$. This proves [\[eq:actions\]](#eq:actions){reference-type="eqref" reference="eq:actions"}; when two singletons are merged the same predecessor state correctly supports two different actions.

For $n=1$, the sole state has $s=b=1$: it is recurrent, is already absorbed, and has one predecessor and one labelled action. Thus every formula above includes the smallest boundary. The proof is exact for all $n$; the accompanying exhaustive program only checks finite boxes and provides no empirical or novelty evidence.
