---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-elephant-random-walk-phase-transition-route-a"
canonical_tex: "henon_dynamics/henon_elephant_random_walk_phase_transition_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_elephant_random_walk_phase_transition_route_a/paper/main.pdf"
source_sha256: "dec39678f848a3b1c9ff39e4662d82d5201cb753f07d897d6b9d424bdfc97c7a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Elephant Random Walk Across Its Full Phase Diagram: Exact Moments, Boundary Martingales, and Limit Laws

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_elephant_random_walk_phase_transition_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_elephant_random_walk_phase_transition_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_elephant_random_walk_phase_transition_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_elephant_random_walk_phase_transition_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a boundary-complete account of the one-dimensional elephant random walk for every memory parameter $p\in[0,1]$ and initial bias $q\in[0,1]$. Exact recurrences yield the first two moments; the singular cases $p=0$ and $p=3/4$ receive separate martingale and harmonic formulas. The diffusive, critical, and superdiffusive limits are stated with exact constants, and the first four moments of the superdiffusive limit expose the deterministic and two-point endpoints at $p=1$. A content-addressed exact computation audits finite identities but is explicitly not offered as proof of an asymptotic theorem.
author:
- 'HCS-C316 theorem-and-evidence package'
date: '3 September 2026 --- revision round 2'
title: |
  The Elephant Random Walk Across Its Full Phase Diagram:\
  Exact Moments, Boundary Martingales, and Limit Laws
```

## Markdown 正文

# Model and finite laws

Let $X_1\in\{-1,1\}$ satisfy $\Pr(X_1=1)=q$. Given $\mathcal F_n=\sigma(X_1,\ldots,X_n)$, choose $K$ uniformly in $\{1,\ldots,n\}$ and set $X_{n+1}=X_K$ with probability $p$ and $X_{n+1}=-X_K$ otherwise. Put $$S_n=\sum_{j=1}^nX_j,\qquad a=2p-1,\qquad b=2q-1,
 \qquad G_n(c)=\prod_{j=1}^{n-1}\left(1+\frac cj\right).$$ The model originates with Schütz and Trimper [@schutz]; the martingale phase analysis used below follows Bercu [@bercu].

[\[thm:finite\]]{#thm:finite label="thm:finite"} For every $n\geq1$, $$\begin{aligned}
 \Pr(X_{n+1}=1\mid\mathcal F_n)&=\frac12\left(1+\frac{aS_n}{n}\right),
 &\mathbb E(X_{n+1}\mid\mathcal F_n)&=\frac{aS_n}{n},\label{eq:kernel}\\
 \mathbb ES_n&=bG_n(a).\label{eq:mean}\end{aligned}$$ Furthermore, with $H_n=\sum_{j=1}^n j^{-1}$, $$\label{eq:second}
 \mathbb ES_n^2=
 \begin{cases}
 \displaystyle\frac{2aG_n(2a)-n}{2a-1},&a\neq\tfrac12,\\[5pt]
 nH_n,&a=\tfrac12.
 \end{cases}$$ If $p>0$, $M_n=S_n/G_n(a)$ is a martingale. At $p=0$ instead, $S_2=0$ and $\widetilde M_n=(n-1)S_n$, $n\geq2$, is a martingale.

Averaging the signed copy over $K$ proves [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}. Hence $$\mathbb E(S_{n+1}\mid\mathcal F_n)=\left(1+\frac an\right)S_n,
 \quad
 \mathbb E(S_{n+1}^2\mid\mathcal F_n)=\left(1+\frac{2a}{n}\right)S_n^2+1.$$ Iteration gives [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}; variation of constants gives [\[eq:second\]](#eq:second){reference-type="eqref" reference="eq:second"}, with the resonant sum equal to $H_n$ when $2a=1$. For $p>0$, divide the first recurrence by $G_{n+1}(a)=(1+a/n)G_n(a)$. At $p=0$, this product vanishes after its first factor, but direct substitution of $a=-1$ gives $\mathbb E[nS_{n+1}\mid\mathcal F_n]=(n-1)S_n$; also $X_2=-X_1$.

\>0

# The complete phase transition

[\[thm:phase\]]{#thm:phase label="thm:phase"} The following alternatives exhaust $p\in[0,1]$.

1.  If $p<3/4$, then $S_n/\sqrt n\Rightarrow N(0,(3-4p)^{-1})$.

2.  If $p=3/4$, then $S_n/\sqrt{n\log n}\Rightarrow N(0,1)$.

3.  If $p>3/4$, then $S_n/n^{2p-1}\to L$ almost surely and in $L^4$. Writing $b=2q-1$, $$\begin{aligned}
     \mathbb EL&=\frac b{\Gamma(2p)},&
     \mathbb EL^2&=\frac1{(4p-3)\Gamma(4p-2)},\\
     \mathbb EL^3&=\frac{2pb}{(2p-1)(4p-3)\Gamma(6p-3)},&
     \mathbb EL^4&=\frac{6(8p^2-4p-1)}{(8p-5)(4p-3)^2\Gamma(8p-4)}.\end{aligned}$$ At $p=1$, $S_n=nX_1$ and $L=X_1$: the limit is deterministic for $q\in\{0,1\}$ and two-point for $0<q<1$.

#### Proof architecture.

For $p>0$, center the martingale from Theorem [\[thm:finite\]](#thm:finite){reference-type="ref" reference="thm:finite"}. Its increments are bounded by a deterministic multiple of $G_n(a)^{-1}$. The predictable quadratic-variation sum is governed by $\sum_{j\leq n}G_j(a)^{-2}$: it has power growth for $a<1/2$, logarithmic growth for $a=1/2$, and a finite limit for $a>1/2$. The martingale central limit theorem (bounded increments give its Lindeberg condition) yields the first two assertions and their constants. The $p=0$ normalization in Theorem [\[thm:finite\]](#thm:finite){reference-type="ref" reference="thm:finite"} supplies the omitted endpoint of the diffusive case. For $a>1/2$, fourth-moment summability gives almost-sure and $L^4$ convergence. Finally, $G_n(a)/n^a\to1/\Gamma(a+1)$ and the exact recurrences through order four give the displayed moments; details follow the martingale derivation in [@bercu]. No finite table is substituted for this argument.

#### What changes at the threshold.

The exact identity $\mathbb ES_n^2=nH_n$ already records the logarithm at $p=3/4$. Above the threshold the random limit retains the initial bias only in odd moments. At $p=1$ it reduces to the remembered first sign, which is why a blanket claim of nondegeneracy would be false.

\>1

# Exact evidence and Route-A boundary

The evidence file is generated using rational arithmetic on 35 frozen $(p,q)$ pairs. It contains every position law for $1\leq n\leq14$ (490 time slices and 3,410 positive-mass cells), 453 conditional martingale identities, four direct full-history enumerations through $n=8$, and nine four-moment ledgers. An independent checker reconstructs all rows, validates 14,914 scalar leaves, and locks every parsed Route-A YAML value with both a byte hash and a canonical semantic digest. Separate symbolic, replay, mutation, and optimized-mode gates prevent a self-consistent producer error from closing the package.

Finite enumeration is regression evidence only. It neither proves a central limit theorem nor establishes literature priority. The nearest repository collisions are the exchangeable Pólya urn, an iid Sparre--Andersen walk, and the recursive Quicksort limit; none has this signed full-memory kernel and its $3/4$ transition.

The Route-A decision is $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FAIL}).$$ There is no rational-prime carrier, deterministic primitive-orbit ledger, zeta/divisor bridge, target functional equation, or natural unitary, scattering, or Hamiltonian lift. The overall verdict is `ROUTE_A_REJECTED`; Route B is locked. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, we assert no target arithmetic local data, Euler factors, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Pólya operator.

# Revision certificate: exact finite structure {#revision-certificate-exact-finite-structure .unnumbered}

This original round contains the exact kernel, both moment branches, and the repaired $p=0$ martingale.

# Revision certificate: complete phase and endpoint theorem {#revision-certificate-complete-phase-and-endpoint-theorem .unnumbered}

This round adds the diffusive, critical, and superdiffusive laws, fourth moments, and the $p=1$ endpoint classification.

# Revision certificate: evidence, collisions, and scope closure {#revision-certificate-evidence-collisions-and-scope-closure .unnumbered}

This final round adds the independent finite audit and the complete Route-A and nonclaim boundary.

9 G. M. Schütz and S. Trimper, "Elephants can always remember," *Phys. Rev. E* 70 (2004), DOI: 10.1103/PhysRevE.70.045101. B. Bercu, "A martingale approach for the elephant random walk," *J. Phys. A* 51 (2018), DOI: 10.1088/1751-8121/aa95a6.
