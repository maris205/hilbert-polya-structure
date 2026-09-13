---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-directed-edge-reinforced-dirichlet-environment-route-a"
canonical_tex: "henon_dynamics/henon_directed_edge_reinforced_dirichlet_environment_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_directed_edge_reinforced_dirichlet_environment_route_a/paper/main.pdf"
source_sha256: "01264b40aa52ba65889a6465e24e4b3c8210573bc31803a044e97883e573950c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Directed Linear Reinforcement Is an Independent-Row Dirichlet Environment

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_directed_edge_reinforced_dirichlet_environment_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_directed_edge_reinforced_dirichlet_environment_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_directed_edge_reinforced_dirichlet_environment_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_directed_edge_reinforced_dirichlet_environment_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite strongly connected directed multigraph with a nonempty outgoing row at each vertex and positive weights on labelled arcs, we give a convention-complete theorem for linear directed edge reinforcement. Its exact path law is a product of vertex-wise rising factorials and equals the annealed law of independent Dirichlet transition rows. We derive the posterior after every history and prove almost-sure transition, vertex-occupation and labelled-edge-occupation limits. Loops, parallel arcs, deterministic rows and the one-vertex Pólya boundary are included. Undirected ERRW, infinite graphs, arithmetic targets and Route B are excluded.
author:
- 'Source-local theorem package HCS-C342'
date: 3 September 2026
title: 'Directed Linear Reinforcement Is an Independent-Row Dirichlet Environment'
```

## Markdown 正文

# Frozen model

Let $G=(V,E)$ be a finite strongly connected directed multigraph in which every vertex has at least one outgoing arc. Each arc is labelled, including parallel arcs, and has $\alpha_e>0$. Write $\alpha_v=\sum_{e:e^-=v}\alpha_e>0$. Starting at $x_0$, define labelled arc and departure counts by $N_e(t)$ and $N_v(t)=\sum_{e:e^-=v}N_e(t)$. From $v=X_t$ choose $e$ with $e^-=v$ according to $$\mathbb P(e\mid\mathcal F_t)=
 \frac{\alpha_e+N_e(t)}{\alpha_v+N_v(t)}.                 \tag{1}$$ Only the augmented process containing the counts is asserted to be Markov.

[\[thm:main\]]{#thm:main label="thm:main"} For every legal labelled arc path $\gamma=(e_1,\ldots,e_m)$, $$\mathbb P(\gamma)=\prod_{v\in V}
 \frac{\prod_{e:e^-=v}(\alpha_e)_{N_e(\gamma)}}
      {(\alpha_v)_{N_v(\gamma)}}.                        \tag{2}$$ Independently sample each row $$\omega(v,\cdot)\sim\operatorname{Dirichlet}
 ((\alpha_e)_{e^-=v}).                                   \tag{3}$$ Then the reinforced path law equals the annealed law of the Markov chain that, conditional on $\omega$, selects labelled arc $e$ with probability $\omega_e$. After any history $\gamma$, the rows remain independent and $$\omega(v,\cdot)\mid\gamma\sim\operatorname{Dirichlet}
 ((\alpha_e+N_e(\gamma))_{e^-=v}).                       \tag{4}$$ Almost surely every vertex is visited infinitely often and $$\frac{N_e(t)}{N_{e^-}(t)}\to\omega_e,\qquad
 \frac{N_v(t)}t\to\pi_\omega(v),\qquad
 \frac{N_e(t)}t\to\pi_\omega(e^-)\omega_e,               \tag{5}$$ where $\pi_\omega$ is the unique stationary law of $K_\omega(v,w)=\sum_{e:v\to w}\omega_e$.

# Exact path law and mixture

At the $r$-th departure from $v$, the denominator in (1) is $\alpha_v+r$. When arc $e$ is selected for the $s$-th time, its numerator is $\alpha_e+s$. Multiplication and grouping by departure vertex gives (2), including loops and labelled parallel arcs. Thus legal paths with the same start and the same outgoing labelled counts at every vertex have equal probability.

For positive $(\alpha_1,\ldots,\alpha_d)$, direct integration of the Dirichlet density gives $$\mathbb E\prod_i\omega_i^{n_i}
 =\frac{\Gamma(\sum_i\alpha_i)}
        {\Gamma(\sum_i\alpha_i+\sum_i n_i)}
   \prod_i\frac{\Gamma(\alpha_i+n_i)}{\Gamma(\alpha_i)}
 =\frac{\prod_i(\alpha_i)_{n_i}}
        {(\sum_i\alpha_i)_{\sum_i n_i}}.                 \tag{6}$$ Given $\omega$, a path has probability $\prod_e\omega_e^{N_e(\gamma)}$. Independence of rows and (6) reproduce (2), proving equality of every finite-dimensional law without invoking an abstract representation theorem.

\>0

# Posterior, moments and almost-sure limits

The likelihood in row $v$ is $\prod_{e:e^-=v}\omega_e^{N_e(\gamma)}$. It changes each prior exponent $\alpha_e-1$ to $\alpha_e+N_e(\gamma)-1$, proving (4) and preserving row independence. The posterior mean is exactly (1). For arcs $e\ne f$ leaving $v$, (6) with one or two unit increments yields $$\mathbb E\omega_e=\frac{\alpha_e}{\alpha_v},\qquad
\operatorname{Var}(\omega_e)=
\frac{\alpha_e(\alpha_v-\alpha_e)}{\alpha_v^2(\alpha_v+1)},\qquad
\operatorname{Cov}(\omega_e,\omega_f)=
-\frac{\alpha_e\alpha_f}{\alpha_v^2(\alpha_v+1)}.         \tag{7}$$ Different rows are independent.

A positive-parameter Dirichlet draw has every coordinate positive almost surely. Conditional on almost every $\omega$, the source graph's strong connectivity therefore makes $K_\omega$ a finite irreducible kernel, with unique $\pi_\omega(v)>0$. The finite-state Markov ergodic theorem gives, simultaneously for the finitely many vertices and labelled arcs, $$t^{-1}N_v(t)\to\pi_\omega(v),\qquad
t^{-1}N_e(t)\to\pi_\omega(e^-)\omega_e$$ with conditional probability one. Integrating over $\omega$ preserves probability one. Division by the positive vertex limit proves the first limit in (5), and positivity also proves infinitely many visits.

#### Round-one posterior and limit closure.

This revision adds conjugacy, all row moments, conditional irreducibility and the full almost-sure learning and occupation theorem.

\>1

# Boundaries, evidence and firewall

An outdegree-one row is the Dirichlet point mass at one. On one vertex, several labelled loops give the classical Pólya urn; one loop is deterministic. The zero-loop singleton is excluded, even under a vacuous strong-connectivity convention, because its normalization and Dirichlet row are undefined. Parallel arcs remain separate Dirichlet coordinates, although they are summed when forming $K_\omega$. Without strong connectivity, only rows visited infinitely often in an eventual recurrent class are learned; unvisited rows retain their priors. A zero initial weight changes support and is excluded.

The exact receipt enumerates every legal path through length eight on three frozen graphs, including loops and parallel arcs, and independently checks Dirichlet moments and rational stationary flows. Producer-independent, SymPy, two-directory replay and repaired-hash mutation lanes validate the implementation. Enumeration is not the proof of (5).

C263 owns a single Pólya urn, C181 deterministic rotor routing, and C338 fixed-conductance Wilson stacks. Undirected ERRW has a different mixing law; its magic formula is not used. The Route-A tuple is all FAIL. We claim no arithmetic local data, target Euler factor, root number, automorphy, target divisor, target zero match, Hilbert--Pólya operator, or Route-B invocation.

#### Round-two boundary and release closure.

This revision closes every frozen boundary, exact-evidence ownership, collision separation, source provenance and negative Route-A claim.

# Source lineage

The directed reinforcement/RWRE correspondence is due to Enriquez and Sabot, *C. R. Math.* 335 (2002), 941--946, [doi:10.1016/S1631-073X(02)02580-3](https://doi.org/10.1016/S1631-073X(02)02580-3). Partial exchangeability follows the lineage of Diaconis and Freedman, *Ann. Probab.* 8 (1980), 115--130, [Project Euclid](https://projecteuclid.org/euclid.aop/1176994828). Sabot and Tournier provide an authoritative overview, [doi:10.5802/afst.1542](https://doi.org/10.5802/afst.1542). Our positive finite-graph specialization is reconstructed directly and makes no priority claim.
