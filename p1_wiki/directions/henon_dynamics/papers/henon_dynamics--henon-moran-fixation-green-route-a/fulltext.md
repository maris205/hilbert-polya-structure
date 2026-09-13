---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-moran-fixation-green-route-a"
canonical_tex: "henon_dynamics/henon_moran_fixation_green_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_moran_fixation_green_route_a/paper/main.pdf"
source_sha256: "dedc51445f187c12512f34418dcc75ca3c5ff5a859b5bfdd9a54ab9bbd293acb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Fixation and Green Kernels for a Finite Moran Process

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_moran_fixation_green_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_moran_fixation_green_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_moran_fixation_green_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_moran_fixation_green_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close an exact finite-state atlas for a continuous-time Moran birth--death process with selection ratio $\rho$ and event scale $\beta$. Fixation, occupation, absorption time, and reversible weights are rational for rational inputs. This is source-local probability; no arithmetic origin or spectral operator is claimed.
author:
- 'Route-A source-local certificate HCS-C253'
date: 30 August 2026
title: Exact Fixation and Green Kernels for a Finite Moran Process
```

## Markdown 正文

trailerid \[\<C2532026083000000000000000000000\>\<C2532026083000000000000000000000\>\]

# Model

Let $X_t\in\{0,\ldots,N\}$ count one type in a fixed population. For $1\le i\le N-1$, set $$\lambda_i=\beta\rho\,\frac{i(N-i)}N,\qquad
\mu_i=\beta\,\frac{i(N-i)}N. \tag{1}$$ The endpoints $0$ and $N$ absorb. The transient generator $Q$ has $Q_{i,i+1}=\lambda_i$, $Q_{i,i-1}=\mu_i$, and $Q_{ii}=-(\lambda_i+\mu_i)$.

# Fixation theorem

Let $u_i$ be the probability of absorption at $N$. The backward equation is $$\lambda_i(u_{i+1}-u_i)+\mu_i(u_{i-1}-u_i)=0,\quad u_0=0,\ u_N=1.$$

For $\rho\ne1$, $u_i=(1-\rho^{-i})/(1-\rho^{-N})$; for $\rho=1$, $u_i=i/N$.

Successive differences have ratio $\rho^{-1}$; summing the geometric progression and taking the neutral limit gives the formula. Positivity of all transient rates and finiteness of the state space imply absorption almost surely.

# Green kernel and time

Define $G=(-Q)^{-1}$ and $t_i=\sum_{j=1}^{N-1}G_{ij}$. Then $G_{ij}$ is expected occupation time and $$\lambda_i(t_{i+1}-t_i)+\mu_i(t_{i-1}-t_i)=-1,\quad t_0=t_N=0. \tag{2}$$ All entries are rational for rational $(N,\rho,\beta)$. The factorization separates population selection from the arbitrary event-time scale, so the Green kernel is not a fitted schedule.

# Reversibility and boundaries

With $w_1=1$ and $$\frac{w_{i+1}}{w_i}=\rho\,\frac{i(N-i)}{(i+1)(N-i-1)}, \tag{3}$$ one has $w_i\lambda_i=w_{i+1}\mu_{i+1}$. The $\rho=1$ face is neutral; $\beta=0$ freezes the chain, and $N=1$ has no transient block.

  rows   sizes      selection     recorded object
  ------ ---------- ------------- -----------------------
  2      3,8        neutral       fixation, Green, time
  4      4,6,7,10   mixed         fixation, full Green
  2      5,9        weak/strong   fixation, full Green

  : Receipt coverage.

# Executable certificate

The producer emits eight exact rows, including every Green matrix through $N=10$. The independent checker closes 220 assertions; SymPy closes ten identities; replay is byte-identical and hostile mutation rejects 23/23. Three fixed-epoch manuscript rounds use embedded fonts and a content-addressed manifest. Decimal values are presentation checks only. Every rational recurrence is checked before decimal conversion, including the neutral limit and the no-inversion boundary faces.

# Route-A boundary

The strict evaluator tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`. The arithmetic origin is `none`; no primitive target orbit or determinant convention is defined. The verdict is `ROUTE_A_REJECTED`, with `route_b_invocation_allowed: false`, under `NO_BAD_EULER_OR_ROOT_NUMBER`. Fixation is a population probability, not a target arithmetic matching law.

# Conclusion

The finite Moran generator supplies both a closed selection formula and an exact occupation kernel. Explicit frozen and singleton faces preserve the A0 stopping boundary.

9 P. A. P. Moran, "Random processes in genetics," Math. Proc. Cambridge Philos. Soc. 54 (1958). W. J. Ewens, *Mathematical Population Genetics*, Springer, 2004. J. R. Norris, *Markov Chains*, Cambridge Univ. Press, 1997.
