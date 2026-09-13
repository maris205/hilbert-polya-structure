---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-random-order-assembly-stopping-time"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time/paper/main.pdf"
source_sha256: "da58d560cbe47b2a2f59ebcb84f15dd5c3f4c9b8c0d74e86a1ed90dd0bac97db"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Random-Order Prefix Assembly of a Frozen Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_random_order_assembly_stopping_time/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the first prefix of a uniformly random ordering of the sixteen named labels whose generated subgroup is the full finite core. Exhaustive closure enumeration and a pivotal-label counting identity give the exact distribution over all $16!=20922789888000$ permutations. The stopping time ranges from 3 to 16, with exact mean $36499/3960\approx9.2169$. An independent closure checker, a symbolic factorial generating check, clean replay, and fifteen hostile mutations certify the receipt. This is a finite named-support result under the firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Random-Order Prefix Assembly of a Frozen Hénon Core'
```

## Markdown 正文

# Stopping rule

Let $\pi$ be a permutation of $L=\{S_1,\ldots,S_{16}\}$ and $A_k(\pi)=\{\pi_1,\ldots,\pi_k\}$. Define $$T(\pi)=\min\{k:\Phi(A_k(\pi))=Q\}.$$ The C75 point-set closure gives 25 inclusion-minimal full-core supports, all of size three, but larger prefixes can be the first full prefix when their last label is pivotal.

For a full-core support $S$ of size $k$, let $$p(S)=\#\{\ell\in S:\Phi(S\setminus\{\ell\})\ne Q\}.$$ Then $$N_k=\#\{\pi:T(\pi)=k\}
 =\sum_{|S|=k,\,\Phi(S)=Q}p(S)(k-1)!(16-k)!.$$

Choose the first $k$ labels to be $S$, choose a pivotal label $\ell$ to be last within that prefix, order the other $k-1$ labels arbitrarily, and order the remaining $16-k$ labels arbitrarily. The preceding prefix is not full, and every permutation with stopping time $k$ is counted exactly once.

# Exact distribution

The stopping counts for $k=3,\ldots,16$ are $$\begin{array}{c|r}
\toprule
k&N_k\\\midrule
3&934053120000\\
4&1641059481600\\
5&1927502438400\\
6&1927328256000\\
7&1807490764800\\
8&1671222067200\\
9&1556813260800\\
10&1467573811200\\
11&1398684672000\\
12&1348868505600\\
13&1319170406400\\
14&1307674368000\\
15&1307674368000\\
16&1307674368000\\
\bottomrule
\end{array}$$ They sum to $16!$. The probability generating function $G(z)=\sum_kN_kz^k/16!$ satisfies $G(1)=1$ and $$G'(1)=\mathbb E[T]=\frac{36499}{3960}.$$ For example, $\Pr[T=3]=5/112$ and $\Pr[T\geq15]=3/16$.

# Audit and scope

The producer binds C76/C78 and the frozen C81 receipt, reconstructs the C75 closure table, and computes every full-support and pivotal pattern. The independent checker repeats this route and verifies all factorial-weighted counts, reduced probabilities, survival counts, and the expectation. A SymPy polynomial check independently recovers the stopping counts. The canonical evidence hash is the concatenation of $$\begin{gathered}
\texttt{033f42f0eea2518f7cb269dd465d82d4}\\[-2pt]
\texttt{871a729d2b93679fcd9f3af38cf9ca28}.
\end{gathered}$$ No arithmetic/local, Euler-factor, root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya conclusion is asserted.
