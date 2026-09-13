---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-325-moving-order-duhamel-composition-criterion"
canonical_tex: "zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion/main.pdf"
source_sha256: "196d8f671c828b398098cc5ce315f308509ddcdff5511636a3d647d3626e3b80"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Moving-Order Duhamel Composition: Retained Paths and the Trace-Observation Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-325-moving-order-duhamel-composition-criterion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-324 proves a sharp $O(\sigma)$ physical-to-affine error for one endpoint leg, but a local bound is not yet a moving-order trace theorem. We give the missing abstract composition ledger. For nonautonomous Markov kernels, a retained-coordinate path telescope bounds the full path-law error by the seed error plus the conditional row errors evaluated against the correctly transported incoming laws. Thus $O(k)$ phase-matched $O(\sigma)$ legs would produce $O(k\sigma)=o(kR^{-2k})$ on the natural first-alias clock. A two-state example proves that accuracy at one fixed seed is not composable under phase transport. For weighted traces we state the exact operator Duhamel criterion and derive the sharp stability window $\gamma<1-\log R/\log\lambda=0.3503698834\ldots$. Finally, a cyclic-shift Markov family has row and retained-path error $2/n\to0$, zero endpoint error, and trace gap one. Hence Markov contraction alone cannot control a growing trace observation. The second physical leg, observation norms, parity, neighboring shell, and joint first-alias trace law remain open.
author:
- Bin Wang
date: July 2026
title: |
  Moving-Order Duhamel Composition:\
  Retained Paths and the Trace-Observation Gap
```

## Markdown 正文

# Retained-path Markov composition

Let $X_0,\ldots,X_m$ be standard Borel spaces. For $1\le j\le m$, let $P_j$ and $Q_j$ be Markov kernels from $X_{j-1}$ to $X_j$. They represent the physical and affine rows. Given entrance probabilities $\mu$ and $\nu$ on $X_0$, define the retained-coordinate path laws $$\begin{aligned}
 \mathcal P(dx_0\cdots dx_m)
 &=\mu(dx_0)\prod_{j=1}^mP_j(x_{j-1},dx_j),\label{eq:path-P}\\
 \mathcal Q(dx_0\cdots dx_m)
 &=\nu(dx_0)\prod_{j=1}^mQ_j(x_{j-1},dx_j).\label{eq:path-Q}\end{aligned}$$ All $L^1$ distances below are unhalved; total variation is one half of them. Put $\nu^P_{j}=\nu P_1\cdots P_j$, with $\nu^P_0=\nu$.

[\[thm:path-duhamel\]]{#thm:path-duhamel label="thm:path-duhamel"} The full path laws satisfy $$\boxed{
 \|\mathcal P-\mathcal Q\|_1
 \le \|\mu-\nu\|_1
 +\sum_{j=1}^m
 \int_{X_{j-1}}
 \|P_j(x,\cdot)-Q_j(x,\cdot)\|_1\,d\nu^P_{j-1}(x).}
 \label{eq:path-bound}$$ Every marginal of the path, including the final $X_m$ law, obeys the same upper bound. In particular, if the $j$th row error is uniformly at most $\varepsilon_j$, then $$\|\mathcal P-\mathcal Q\|_1\le\|\mu-\nu\|_1+\sum_{j=1}^m\varepsilon_j.
 \label{eq:sup-bound}$$

First compare the physical path started from $\mu$ with the same physical path started from $\nu$. Because $x_0$ is retained and all later factors are probability kernels, this difference has $L^1$ norm exactly $\|\mu-\nu\|_1$.

Starting now from $\nu$, telescope through the hybrid path laws whose first $j$ rows are physical and whose remaining rows are affine. The $j$th hybrid difference contains the signed row $P_j-Q_j$. The prefix has $x_{j-1}$ marginal $\nu^P_{j-1}$, while the affine suffix has total mass one for every retained $x_j$. Tonelli's theorem therefore makes the norm of this hybrid difference exactly the $j$th integral in [\[eq:path-bound\]](#eq:path-bound){reference-type="eqref" reference="eq:path-bound"}. The triangle inequality proves the path bound. Marginalization is an $L^1$ contraction, and [\[eq:sup-bound\]](#eq:sup-bound){reference-type="eqref" reference="eq:sup-bound"} follows.

The retained coordinate is essential: it prevents cancellations between different source rows before their conditional errors are measured. The incoming law is also essential; it is the physical prefix transport of the reference entrance law, not an arbitrarily reused local seed.

[\[prop:phase-counterexample\]]{#prop:phase-counterexample label="prop:phase-counterexample"} There are two-state Markov kernels $T,P,Q$ and a seed $\delta_0$ such that $$\|\delta_0P-\delta_0Q\|_1=0,
 \qquad
 \|\delta_0TP-\delta_0TQ\|_1=2.
 \label{eq:phase-counterexample}$$

Let $T$ send both states to state $1$, let $P$ be the identity, and let $Q$ send both states to state $0$. At the original seed, both $P$ and $Q$ return $\delta_0$. After $T$, the incoming law is $\delta_1$; $P$ returns $\delta_1$ and $Q$ returns $\delta_0$, whose $L^1$ distance is two.

This is the exact finite obstruction to iterating a phase-matched estimate without proving how the phase and profile enter the next row.

# The natural-clock consequence

Use the archived clock and radius $$k_\sigma=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad R=1.4,
 \qquad
 \theta=\frac{\log R}{\log\lambda}
 =0.6496301165394707\ldots .
 \label{eq:clock}$$ Then $R^{-2k_\sigma}=\Theta(\sigma^\theta)$.

[\[cor:markov-clock\]]{#cor:markov-clock label="cor:markov-clock"} Suppose $m_\sigma=O(k_\sigma)$, the entrance error is $o(k_\sigma R^{-2k_\sigma})$, and every transported row in [\[thm:path-duhamel\]](#thm:path-duhamel){reference-type="ref" reference="thm:path-duhamel"} has error $O(\sigma)$ with a common constant. Then $$\|\mathcal P_\sigma-\mathcal Q_\sigma\|_1
 =O(k_\sigma\sigma)
 =o(k_\sigma R^{-2k_\sigma}).
 \label{eq:markov-negligible}$$ The same holds for every marginal.

The theorem gives $O(m_\sigma\sigma)=O(k_\sigma\sigma)$. Dividing by the target leaves $O(\sigma^{1-\theta})\to0$ because $\theta<1$.

This corollary is deliberately conditional. RH-324 proves the required phase-matched $O(\sigma)$ scale only for the first physical endpoint leg. It does not prove a common bound for all transported rows or the second critical physical leg.

# Operator products and trace observations

Markov path control is not yet trace control. Let $B_0,\ldots,B_m$ be Banach spaces with $B_m=B_0$, and let $A_j,G_j:B_{j-1}\to B_j$ be bounded operators. Suppose a linear observation $\mathfrak t$ on endomorphisms of $B_0$ obeys $$|\mathfrak t(H)|\le T\|H\|.
 \label{eq:observation-bound}$$

[\[thm:operator-duhamel\]]{#thm:operator-duhamel label="thm:operator-duhamel"} The exact identity $$A_m\cdots A_1-G_m\cdots G_1
 =\sum_{j=1}^m
 A_m\cdots A_{j+1}(A_j-G_j)G_{j-1}\cdots G_1
 \label{eq:duhamel-identity}$$ implies $$\left|\mathfrak t(A_m\cdots A_1-G_m\cdots G_1)\right|
 \le\sum_{j=1}^m W_j\delta_j,
 \label{eq:operator-bound}$$ where $$\begin{aligned}
 \delta_j&=\|A_j-G_j\|,\nonumber\\
 W_j&=T
 \prod_{\ell=j+1}^m\|A_\ell\|
 \prod_{\ell=1}^{j-1}\|G_\ell\|.
 \label{eq:weights}\end{aligned}$$ Consequently a first-alias trace replacement follows if $\sum_jW_j\delta_j=o(k_\sigma R^{-2k_\sigma})$.

Equation [\[eq:duhamel-identity\]](#eq:duhamel-identity){reference-type="eqref" reference="eq:duhamel-identity"} is the finite product telescope. Apply [\[eq:observation-bound\]](#eq:observation-bound){reference-type="eqref" reference="eq:observation-bound"}, submultiplicativity, and the triangle inequality term by term.

[\[thm:power-window\]]{#thm:power-window label="thm:power-window"} Assume $m_\sigma=O(k_\sigma)$, $\delta_j=O(\sigma)$ uniformly, and $$\max_jW_j=O(\sigma^{-\gamma}).
 \label{eq:weight-growth}$$ Then [\[eq:operator-bound\]](#eq:operator-bound){reference-type="eqref" reference="eq:operator-bound"} is $O(k_\sigma\sigma^{1-\gamma})$. It is $o(k_\sigma R^{-2k_\sigma})$ whenever $$\boxed{
 \gamma<\gamma_*:=1-\theta
 =0.3503698834605293\ldots .}
 \label{eq:gamma-threshold}$$ At $\gamma=\gamma_*$ the majorant is only of target order, while for $\gamma>\gamma_*$ this argument does not decay relative to the target.

The ratio of the Duhamel majorant to the target has power $$\frac{k_\sigma\sigma^{1-\gamma}}
 {k_\sigma\sigma^\theta}
 =\sigma^{1-\theta-\gamma}.$$ Its exponent is positive precisely below [\[eq:gamma-threshold\]](#eq:gamma-threshold){reference-type="eqref" reference="eq:gamma-threshold"}.

RH-18 proves only the lower bound $\operatorname{cond}(D_k^{\rm G})\ge\sigma^{-1/4+o(1)}$. The exponent $1/4$ lies below $\gamma_*$ by $$\gamma_*-\frac14=0.1003698834605293\ldots .
 \label{eq:quarter-slack}$$ If a relevant stability weight had a matching quarter-power *upper* bound, this scalar budget would remain compatible. No such upper bound or identification with the actual trace observation is archived.

# A dimension-free trace bound is false

Let $S_n$ be the cyclic shift on $n\ge2$ states and put $$P_n=I_n,
 \qquad
 Q_n=\left(1-\frac1n\right)I_n+\frac1nS_n.
 \label{eq:trace-example}$$ Both matrices are Markov and preserve the uniform law. Let $\Pi_n^P(i,j)=n^{-1}P_n(i,j)$ and $\Pi_n^Q(i,j)=n^{-1}Q_n(i,j)$ denote their one-step retained path laws.

[\[prop:trace-counterexample\]]{#prop:trace-counterexample label="prop:trace-counterexample"} For the pair [\[eq:trace-example\]](#eq:trace-example){reference-type="eqref" reference="eq:trace-example"}, $$\max_i\|P_n(i,\cdot)-Q_n(i,\cdot)\|_1=\frac2n,
 \qquad
 \|\Pi_n^P-\Pi_n^Q\|_1=\frac2n,
 \label{eq:row-path-small}$$ and the endpoint marginals are identical, but $$|\operatorname{Tr}P_n-\operatorname{Tr}Q_n|=1.
 \label{eq:trace-gap}$$ Thus no dimension-free bound converts Markov row or path $L^1$ error into trace error.

Each row moves mass $1/n$ from its diagonal entry to the next state, giving row distance $2/n$. Averaging the rows against the uniform entrance law gives the same retained one-step path distance. Both kernels preserve that uniform law, so the endpoint error is zero. Since $S_n$ has zero diagonal, $$\operatorname{Tr}Q_n=n\left(1-\frac1n\right)=n-1,$$ which proves [\[eq:trace-gap\]](#eq:trace-gap){reference-type="eqref" reference="eq:trace-gap"}.

The reproduction table uses $m_\sigma=\lceil2k_\sigma\rceil$, local constant one, and model growth $\sigma^{-\gamma}$:

    $\sigma$     $\gamma=0$   $\gamma=1/4$   $\gamma=\gamma_*$   $\gamma=0.4$
  ------------ ------------ -------------- ------------------- --------------
   $10^{-4}$       0.080321       0.803212            2.024463       3.197646
   $10^{-8}$       0.003187       0.318677            2.024463       5.050691
   $10^{-12}$      0.000126       0.126436            2.024463       7.977582

The entries are majorant-to-target ratios computed from the exact exponents; they are not fitted estimates of the physical operator.

RH-325 proves composition criteria and explicit counterexamples. It does not show that every physical leg meets the Markov hypotheses, control the second critical leg, bound the actual trace observation, combine parity with the neighboring shell, or prove the joint first-alias matching law. It does not prove divergence when the sufficient majorant fails. No full-trace replacement is obtained. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or zeta-divisor equality, and does not imply RH.

RH-326 should now derive the parity-renormalized first-alias packet identity without discarding the transported phase or the sign needed for later joint cancellation.
