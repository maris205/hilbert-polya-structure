---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-open-tasep-matrix-ansatz-phase-route-a"
canonical_tex: "henon_dynamics/henon_open_tasep_matrix_ansatz_phase_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_open_tasep_matrix_ansatz_phase_route_a/paper/main.pdf"
source_sha256: "de7b60deeec219b80591d5a225e1cf9d14ce3f48bd14728edbefd7982747e5dd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Open TASEP: Matrix-Ansatz Stationarity and an All-Boundary Phase Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_open_tasep_matrix_ansatz_phase_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_open_tasep_matrix_ansatz_phase_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_open_tasep_matrix_ansatz_phase_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_open_tasep_matrix_ansatz_phase_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give one source-locked theorem for the continuous-time open totally asymmetric exclusion process (TASEP). Particles enter a finite binary chain at rate $\alpha$, hop right at unit rate, and leave at rate $\beta$. The DEHP relation $DE=D+E$ evaluates every finite configuration word, yields a closed ballot-number normalization $Z_L$, and forces the exact current $J_L=Z_{L-1}/Z_L$. We retain the equal-rate divided-difference limit and all zero-rate and small-size faces. The analytic large-$L$ statement separates low-density, high-density, maximal-current, coexistence, and critical regimes; finite exact rows are explicitly regression sentinels and are not used as numerical proof of that limit. A rational producer, an independent generator/nullspace checker, symbolic identities, clean replay, and hostile mutation tests accompany the paper. The source theorem has no arithmetic owner, so its strict Route-A outcome is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'Open TASEP: Matrix-Ansatz Stationarity and an All-Boundary Phase Atlas'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen process and contribution

For $L\geq 1$ let $\eta=(\eta_1,\ldots,\eta_L)\in\{0,1\}^L$, with $\eta_i=1$ denoting an occupied site. An empty first site receives a particle at rate $\alpha$, each adjacent pattern $10$ changes to $01$ at unit rate, and an occupied last site is removed at rate $\beta$. The physical clock is continuous time and the bulk rate is normalized to one. The empty $L=0$ chain is retained as a one-state boundary.

The paper makes a single finite-to-asymptotic move. It first proves the finite generator and its DEHP stationary vector for every positive $(\alpha,\beta)$, then states the all-parameter phase atlas and separately closes the singular faces. The executable ledger checks rational instances only; it does not replace the analytic thermodynamic argument.

# Generator and matrix product

For a test function $f$, the generator is $$\begin{aligned}
(\mathcal Lf)(\eta)
={}&\alpha(1-\eta_1)\{f(\eta^{1+})-f(\eta)\}\nonumber\\
&+\sum_{i=1}^{L-1}\eta_i(1-\eta_{i+1})
 \{f(\eta^{i,i+1})-f(\eta)\}\nonumber\\
&+\beta\eta_L\{f(\eta^{L-})-f(\eta)\}.
\label{eq:generator}\end{aligned}$$ Here $\eta^{1+}$ fills site one, $\eta^{L-}$ empties the last site, and $\eta^{i,i+1}$ performs the indicated hop.

[\[prop:dehp\]]{#prop:dehp label="prop:dehp"} Let $D,E$ satisfy $DE=D+E$ and let $$\langle W|E=\alpha^{-1}\langle W|,\qquad
D|V\rangle=\beta^{-1}|V\rangle .$$ For a word with $D$ at occupied sites and $E$ at empty sites, put $$w(\eta)=\langle W|\prod_{i=1}^{L}
[\eta_iD+(1-\eta_i)E]|V\rangle,\qquad
Z_L=\sum_{\eta}w(\eta).$$ If $\alpha,\beta>0$, then $\pi(\eta)=w(\eta)/Z_L$ is the unique stationary law of [\[eq:generator\]](#eq:generator){reference-type="eqref" reference="eq:generator"}, and the current is the same through every bond.

#### Proof sketch.

In the stationarity sum, a bulk gain--loss pair is replaced by $DE-D-E$, which vanishes. The two remaining boundary terms are removed by the two boundary eigenvector identities. Positive injection and extraction make the finite directed graph irreducible, so the stationary vector is unique. The same cancellation applied to a bond gives a common current. No infinite matrix truncation is needed: recursively strip a left $E$, a right $D$, or replace a $DE$ pair by $D+E$.

# Closed normalization and finite current

Writing $x=\beta^{-1}$ and $y=\alpha^{-1}$, the exact finite normalization is $$Z_0=1,\qquad
Z_N=\sum_{p=1}^{N}
\frac{p(2N-1-p)!}{N!(N-p)!}\,
\frac{x^{p+1}-y^{p+1}}{x-y}\quad(N\geq1).
\label{eq:Z}$$ At $x=y$ the quotient is its continuous value $(p+1)x^p$. Thus $$J_L=\frac{Z_{L-1}}{Z_L}\quad(L\geq1),
\qquad J_1=\frac{\alpha\beta}{\alpha+\beta}.
\label{eq:current}$$ The producer evaluates [\[eq:Z\]](#eq:Z){reference-type="eqref" reference="eq:Z"} in exact rational arithmetic. The regression grid includes the equal-rate diagonal and all three critical boundary pieces (including their corner): $$\alpha,\beta\in\left\{\tfrac14,\tfrac12,\tfrac34,1,\tfrac32\right\}.$$

\>0

# Phase and boundary atlas

For unit bulk hopping, the analytic thermodynamic current is $$J=\begin{cases}
\alpha(1-\alpha),&\alpha<\min(\beta,\frac12)
       \quad\text{(low density)},\\
\beta(1-\beta),&\beta<\min(\alpha,\frac12)
       \quad\text{(high density)},\\
\frac14,&\alpha>\frac12,\ \beta>\frac12
       \quad\text{(maximal current)}.
\end{cases}$$ The line $0<\alpha=\beta<1/2$ is the coexistence (shock) line in the positive-rate interior; it has the same current but no single selected bulk density. Its endpoint $(\alpha,\beta)=(0,0)$ is excluded from coexistence and is handled by the zero-rate boundary theorem below. The faces $\alpha=1/2,\beta>1/2$ and $\beta=1/2,\alpha>1/2$ are critical and retain finite-size corrections. Their intersection $\alpha=\beta=1/2$ is the multicritical phase-boundary junction and has the same bulk density and current with finite-size critical corrections.

  parameters             closed class                   stationary description
  ---------------------- ------------------------------ --------------------------------------------------
  $\alpha>0,\ \beta>0$   all $2^L$ states               unique DEHP law
  $\alpha=0,\ \beta>0$   empty word                     unique empty state
  $\alpha>0,\ \beta=0$   full word                      unique full state
  $\alpha=\beta=0$       $0^{L-k}1^k,\ 0\leq k\leq L$   simplex on $L+1$ absorbers; affine dimension $L$
  $L=0$                  one state                      zero generator

On the double-zero face the table lists $L+1$ absorbing extreme points. Their normalized stationary family is the simplex on those absorbers, of affine dimension $L$; the linear (unnormalized) nullspace has one basis direction per absorber.

\>1

# Exact audit and Route-A boundary

The release ledger contains 200 positive-rate rows (five-by-five rational rates for each of $L=0,1,2,3,4,5,6,8$) and 40 zero-rate rows. It stores every finite configuration weight, $Z_L$, every bond current, and the exact stationary residual. The independent checker reconstructs the generator and uses exact SymPy nullspaces through $L=4$; larger rows are covered by the irreducibility theorem. A separate SymPy program checks all short-word quadratic identities, [\[eq:Z\]](#eq:Z){reference-type="eqref" reference="eq:Z"}, the equal-rate limit, and symbolic stationarity. Clean replay is byte-identical, and repaired-hash, stale-hash, schema, and overclaim mutations are rejected.

The finite matrix-product/current theorem and the source-cited phase atlas are exact, but they do not create a primitive orbit clock or an arithmetic target. The strict Route-A tuple is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)},$$ with `ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.

The finite ledger is not numerical evidence for the thermodynamic limit and no priority or novelty claim is made. The literal scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; no target primes, zeros, Euler factors, root numbers, automorphy, target divisor, or Hilbert--Polya operator is introduced.

# Source note {#source-note .unnumbered}

The open-boundary recursion and phase diagram follow the source account of Derrida, Domany, and Mukamel [@DDM1992]. The matrix formulation, normalization, current, and profiles follow Derrida, Evans, Hakim, and Pasquier [@DEHP1993]. These citations are metadata anchors, not claims of priority for this package.

9 B. Derrida, E. Domany, and D. Mukamel, *An exact solution of a one-dimensional asymmetric exclusion model with open boundaries*, Journal of Statistical Physics 69 (1992), 667--687. DOI: 10.1007/BF01050430. B. Derrida, M. R. Evans, V. Hakim, and V. Pasquier, *Exact solution of a 1D asymmetric exclusion model using a matrix formulation*, Journal of Physics A: Mathematical and General 26 (1993), 1493--1517. DOI: 10.1088/0305-4470/26/7/011.

# Declarations {#declarations .unnumbered}

**Data and code.** All finite rows and audit scripts are shipped with the package and use exact rational arithmetic. **Limitations.** The finite ledger does not prove the $L\to\infty$ phase theorem. **Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized. **AI-use disclosure.** Generative tools assisted drafting and code generation; deterministic internal checks validate the displayed artifact.
