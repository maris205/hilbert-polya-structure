---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kac-ring-cycle-classification-route-a"
canonical_tex: "henon_dynamics/henon_kac_ring_cycle_classification_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kac_ring_cycle_classification_route_a/paper/main.pdf"
source_sha256: "fcae189301e758f8edaffe1078278ad74619be5f70ad7ee33336b0464ca4c71b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Cycle Classification for Every Finite Kac Ring

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kac_ring_cycle_classification_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kac_ring_cycle_classification_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kac_ring_cycle_classification_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kac_ring_cycle_classification_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every ring size and every binary marker configuration, we classify all cycles of the reversible finite Kac ring. The marker product $\eta$ is the only invariant needed: positive product gives two cycles of length $N$, while negative product gives one cycle of length $2N$. We derive all fixed counts, the Artin--Mazur zeta, and the finite Koopman determinant.
author:
- 'Route-A structural certificate C170'
title: Exact Cycle Classification for Every Finite Kac Ring
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Kac ring; marker configuration; exact period; primitive cycle; dynamical zeta; Koopman permutation; time reversal.

chinese-simplified

中文摘要

本文对任意环长和任意二元标记配置的可逆有限[Kac]{lang="en"}环给出完整周期分类。 所有动力信息只依赖标记乘积 $\eta$：正乘积产生两个长度为 $N$ 的周期，负乘积产生 一个长度为 $2N$ 的周期。由此严格导出所有时刻的不动点数、动力 $\zeta$ 函数、 有限维[Koopman]{lang="en"}行列式与反酉时间反演。

关键词：[Kac]{lang="en"}环；标记配置；精确周期；本原周期；动力 $\zeta$ 函数； [Koopman]{lang="en"}置换；时间反演。

# All-marker classification

On $X_N=\mathbb Z/N\mathbb Z\times\{\pm1\}$ let $$T(j,s)=(j+1,\varepsilon_j s),\qquad
\eta=\prod_{j=0}^{N-1}\varepsilon_j.$$ One circuit gives $T^N(j,s)=(j,\eta s)$. Since every return time is divisible by $N$, all states have exact period $N$ when $\eta=+1$ and exact period $2N$ when $\eta=-1$. Hence there are respectively two and one geometric cycles. With $L=N$ or $2N$ and $c=2N/L$, $$\#\operatorname{Fix}(T^n)=2N\,\mathbf1_{L\mid n},\quad
\zeta_T(z)=(1-z^L)^{-c},\quad
\det(I-zU_T)=(1-z^L)^c.$$ The eigenvalues of the counting-measure Koopman permutation are all $L$-th roots of unity, each with multiplicity $c$. The zeta exponent counts geometric cycles, whereas the fixed count uses all $2N$ labelled states; keeping those multiplicities separate prevents a factor-of-$L$ error. The two $N=1$ cases are included: positive product is the identity on two states, and negative product is one transposition.

# Gauge and reversal

Set $g_0=1$, $g_j=\prod_{r<j}\varepsilon_r$, and $q=g_js$. In $(j,q)$ coordinates the map advances the site, preserves $q$ away from the wrap, and sends $q$ to $\eta q$ at the wrap. If $\eta=+1$, reflection $j\mapsto-j$ reverses each cycle. If $\eta=-1$, define $\psi(j,+1)=j$ and $\psi(j,-1)=N+j$; the map becomes translation by one on $\mathbb Z/(2N)\mathbb Z$, reversed by $t\mapsto-t$. Pullback through the gauge yields an involution $R$ with $RTR=T^{-1}$. Thus $\Theta f=\overline{f\circ R}$ is antiunitary and $\Theta U_T\Theta=U_T^{-1}$. The permutation unitary is self-adjoint exactly when $L\le2$.

# Route-A decision and evidence boundary

  Gate   Verdict                  Reason
  ------ ------------------------ --------------------------------------
  A0     `FAIL`                   no intrinsic arithmetic origin
  A1     `WEAK`                   complete but finite reducible cycles
  A2     `FAIL`                   no target divisor comparison
  A3     `FAIL`                   no target global comparison
  A4     `NATURAL_QUANTIZATION`   same-clock permutation and reversal

The v0.2 overall verdict is `ROUTE_A_REJECTED`, because A0 fails; Route B is false. The paper is retained as theorem progress, not as a primary Hilbert--Pólya candidate.

The release ledger contains 48 class rows through $N=24$. An independent implementation exhausts all 2,046 marker words through $N=10$, covering 36,868 labelled states, 36,868 fixed-time checks, and 73,736 reversal identities. Its checker passes 114,056 assertions, SymPy passes 221 matrix and polynomial checks, byte replay is exact, and 17 hostile mutations are rejected. These are regression sentinels only; the all-size, all-marker result rests on the circuit and gauge proofs. Citation and reference registries each have population zero, and no novelty or priority claim is made.

#### Limitations.

The system is a finite, exactly reducible kinetic toy model. Its primitive cycles have no proved prime semantics. We make no target divisor, functional-equation, counting-law, arithmetic local-factor, Euler-factor, root-number, automorphy, or Hilbert--Pólya claim. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact evidence and deterministic code accompany this manuscript.

#### Ethics.

No human, animal, clinical, personal, or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.
