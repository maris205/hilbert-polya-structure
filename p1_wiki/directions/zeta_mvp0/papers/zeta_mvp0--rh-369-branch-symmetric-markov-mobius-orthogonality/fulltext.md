---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-369-branch-symmetric-markov-mobius-orthogonality"
canonical_tex: "zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality/main.pdf"
source_sha256: "069ef17b8e61f65ce7e8cfe1cb822ddef7a7728b787de36039aa5f15b3f78ac1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A branch-symmetric Markov family on the RH-366 graph: exact Möbius orthogonality and covariance

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-369-branch-symmetric-markov-mobius-orthogonality/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We derive, rather than geometrically select, a one-parameter Markov/Gibbs family on the primitive four-state graph used by RH-366. In the state order $(--,-+,+-,++)$, put $q=1-t$ and $$P_t=\begin{pmatrix}
   t&0&q&0\\
   1&0&0&0\\
   0&t&0&q\\
   0&1&0&0
   \end{pmatrix},\qquad 0<t<1.$$ Its stationary law, centered sign variance, and all-lag covariance are exact: the odd covariances vanish and the variance-one covariance at lag $2k$ is $(-q)^k$. Each fixed parameter gives a mixing Markov measure, so the finite-state Chebyshev--Borel--Cantelli argument yields Möbius orthogonality almost surely, simultaneously for all continuous observables. The weighted finite variance has an exact even-shift expansion and a geometric bound. The Parry law is the single member $t=\varphi^{-1}$; the open interval adds non-Parry measures but no canonical arithmetic coupling. All statements are fixed-parameter, and no uniform endpoint theorem, operator trace, zero model, or RH implication is claimed.
author:
- RH research program
date: August 2026
title: |
  A branch-symmetric Markov family on the RH-366 graph:\
  exact Möbius orthogonality and covariance
```

## Markdown 正文

# Frozen graph and derived data type

The source package [@HenonMobius2026] freezes the state order $$(--,-+,+-,++)$$ and the adjacency matrix $$A=\begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.
 \tag{1}$$ The first coordinate of a state is the scalar sign observable $$e=(-1,-1,+1,+1)^{\mathsf T}. \tag{2}$$ The graph and its Hénon conjugacy are inherited inputs; they are not reconstructed from the finite calculations below.

For $0<t<1$, let $q=1-t$ and define the row-stochastic matrix $$P_t=\begin{pmatrix}
 t&0&q&0\\
 1&0&0&0\\
 0&t&0&q\\
 0&1&0&0
 \end{pmatrix}. \tag{3}$$ Every positive entry of $P_t$ lies on an edge of (1), and every edge of (1) receives a positive probability. Thus (3) is a new derived symbolic family, not a source claim that the Hénon geometry chooses a parameter.

[\[prop:mixing\]]{#prop:mixing label="prop:mixing"} Put $d=1+q=2-t$. The unique stationary row vector of $P_t$ is $$\pi_t=\frac{(1,q,q,q^2)}{d^2}. \tag{4}$$ Moreover, $$\det(\lambda I-P_t)=(\lambda-1)(\lambda+q)(\lambda^2+q). \tag{5}$$ Consequently $P_t$ is primitive and its nontrivial spectral radius is $\sqrt q<1$.

Multiplying the row in (4) by (3) gives the same row, and its entries sum to one. The directed support is the primitive graph (1); in fact a direct multiplication gives $A^4>0$, and all the corresponding entries of $P_t^4$ are positive for $0<t<1$. This proves primitivity and uniqueness of the stationary law. Expanding the determinant in (5) gives the stated factorization. The eigenvalue $1$ is simple, while the other three eigenvalues are $-q$ and $\pm i\sqrt q$.

# Exact observable and covariance

Let $\nu_t$ be the stationary Markov measure on $\Sigma_A$ associated with $P_t$. With $e$ from (2), direct multiplication gives $$m_t=\pi_t e=-\frac{t}{d},\qquad
 v_t=\pi_t(e-m_t{\bf 1})^2=\frac{4q}{d^2}. \tag{6}$$ Since $q>0$, define the centered variance-one observable $$F_t=\frac{e-m_t{\bf 1}}{\sqrt{v_t}}
 =(-\sqrt q,-\sqrt q,q^{-1/2},q^{-1/2})^{\mathsf T}. \tag{7}$$

[\[prop:cov\]]{#prop:cov label="prop:cov"} For every $k\geq0$, $$\operatorname{Cov}_{\nu_t}(F_t,F_t\circ\sigma^{2k+1})=0,\qquad
 \operatorname{Cov}_{\nu_t}(F_t,F_t\circ\sigma^{2k})=(-q)^k. \tag{8}$$ For the raw sign, the even covariance is $v_t(-q)^k$ and the odd covariance is zero.

The stationary covariance formula for a state observable is $$\operatorname{Cov}_{\nu_t}(F_t,F_t\circ\sigma^\ell)
 =\pi_t\operatorname{diag}(F_t)P_t^\ell F_t. \tag{9}$$ Using (3), (4), and (7), one obtains the two exact identities $$P_t^2F_t=-qF_t,\qquad
 \pi_t\operatorname{diag}(F_t)P_tF_t=0. \tag{10}$$ For even $\ell=2k$, (9)--(10) give $(-q)^k$. For odd $\ell=2k+1$, factor out $(-q)^k$ and use the second identity in (10).

For $\varphi=(1+\sqrt5)/2$, the RH-366 Parry matrix is exactly (3) at $$t=\varphi^{-1},\qquad q=\varphi^{-2}. \tag{11}$$ Thus (8) recovers the RH-366 covariance. The theorem is new only in the parameterized non-Parry family and in the fixed-parameter quantifier; it does not rebrand the Parry calculation as a physical spectral result.

# Fixed-parameter Möbius orthogonality

[\[thm:as\]]{#thm:as label="thm:as"} For every fixed $t\in(0,1)$ there is a set $E_t\subset\Sigma_A$ with $\nu_t(E_t)=1$ such that, for every $\omega\in E_t$ and every $f\in C(\Sigma_A)$, $$\frac1N\sum_{n\leq N}\mu(n)f(\sigma^n\omega)\longrightarrow0. \tag{12}$$ Under the frozen Hénon conjugacy, the same statement holds for continuous observables on the local survivor.

It is enough first to treat a centered locally constant function $g$. The primitive finite-state chain has exponential mixing, so there are constants $C_g<\infty$ and $0<\rho_t<1$ such that $$\left|\operatorname{Cov}_{\nu_t}\bigl(g\circ\sigma^i,g\circ\sigma^j\bigr)\right|
 \le C_g\rho_t^{|i-j|}. \tag{13}$$ With $T_N(\omega)=\sum_{n\le N}\mu(n)g(\sigma^n\omega)$ and $|\mu(n)|\le1$, (13) implies $$\mathbb E_{\nu_t}|T_N|^2\le C'_g N. \tag{14}$$ Chebyshev's inequality at $N=k^2$ gives a summable bound for $\nu_t\{|T_{k^2}|>\epsilon k^2\}$. Borel--Cantelli yields $T_{k^2}/k^2\to0$ almost surely. Between consecutive squares there are $O(k)$ bounded summands, so the convergence holds for all $N$.

Take a countable dense family of centered cylinder functions with rational values and intersect the corresponding full-measure sets. Uniform approximation extends the conclusion to all centered continuous functions. For a general $f$, subtract its $\nu_t$-mean. The remaining constant term is a multiple of $\sum_{n\le N}\mu(n)=o(N)$, by the prime number theorem.

The set $E_t$ and the constants in (13)--(14) depend on the fixed parameter. No common full-measure set over uncountably many $t$, and no estimate uniform as $t\downarrow0$ or $t\uparrow1$, is asserted.

# Möbius-weighted variance

Define $$S_{N,t}(\omega)=\sum_{n\le N}\mu(n)F_t(\sigma^n\omega),
 \qquad V_{N,t}=\operatorname{Var}_{\nu_t}(S_{N,t}). \tag{15}$$ The covariance table gives the exact identity $$V_{N,t}
 =\sum_{n\le N}\mu(n)^2
 +2\sum_{k=1}^{\lfloor(N-1)/2\rfloor}(-q)^k
   \sum_{n\le N-2k}\mu(n)\mu(n+2k). \tag{16}$$

[\[prop:bound\]]{#prop:bound label="prop:bound"} For every $N\ge1$ and $0<t<1$, $$0\le V_{N,t}\le \left(1+2\sum_{k\ge1}q^k\right)N
 =\frac{2-t}{t}\,N. \tag{17}$$ Equivalently, $$\left\|\frac{S_{N,t}}N\right\|_{L^2(\nu_t)}
 \le\sqrt{\frac{2-t}{tN}}. \tag{18}$$

Nonnegativity is the variance definition. In (16), bound the diagonal by $N$, each inner correlation by $N$, and sum the geometric absolute values. The $L^2$ estimate is the square root of (17) divided by $N$.

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Assume the ordinary fixed-shift two-point correlations $$\frac1N\sum_{n\le N}\mu(n)\mu(n+2k)\longrightarrow0
 \quad\text{for every fixed }k\ge1. \tag{19}$$ Then, for every fixed $t\in(0,1)$, $$\frac{V_{N,t}}N\longrightarrow\frac6{\pi^2}. \tag{20}$$

The squarefree density gives $N^{-1}\sum_{n\le N}\mu(n)^2\to6/\pi^2$. For the off-diagonal part of (16), first retain finitely many $k$ and use (19). The remaining tail is bounded uniformly in $N$ by $2\sum_{k>K}q^k$, which tends to zero as $K\to\infty$. This proves (20).

Equation (20) is not an unconditional two-point Chowla theorem. It is a conditional consequence recorded to identify exactly which arithmetic input would be needed for the variance density. The unconditional theorem is (16)--(18).

# Parameter boundaries and route decision

At $t=0$, the branch choices disappear and the chain is a deterministic period-four system; at $t=1$, the stationary law collapses and $v_t=0$, so $F_t$ is undefined. Also, the nontrivial spectral radius $\sqrt{1-t}$ tends to one as $t\downarrow0$, while the entries $q^{-1/2}$ in (7) diverge as $t\uparrow1$. These are genuine reasons to keep the theorem pointwise on the open interval.

The stationary entropy rate, included only as a structural diagnostic, is $$h(t)=\frac{-t\log t-(1-t)\log(1-t)}{2-t}. \tag{21}$$ Its maximum occurs at the Parry point (11); this does not select a canonical parameter for the arithmetic problem.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Route            Verdict and boundary
  ---------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Route A          `GO`. The derived family has exact stationary, mixing, covariance, almost-sure fixed-parameter Möbius, and finite-variance theorems.

  Route B          `STOP_SCOPED`. The parameter is externally chosen; no canonical arithmetic coupling, determinant, prime-power trace, zeta-zero model, or physical Gate is supplied.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

No Hilbert--Pólya operator is constructed, no Riemann zero is identified, and the Riemann hypothesis is not addressed.

# Executable audit and overlap ledger

The package checks stationarity, the centered $P_t^2$ eigenidentity, the vanishing one-step covariance, positivity of $P_t^4$, and the characteristic covariance table at rational parameters $1/2$, $2/3$, and $3/4$. It also compares (16) with an independent finite double sum through $N=14$. These are exact finite checks, not asymptotic fits.

The overlap is narrow. RH-366 supplies the graph, sign observable, Parry specialization, and the proof template for almost-sure orthogonality. RH-369 supplies the non-Parry branch-symmetric family and its parameter identities. RH-367 and the PCF parity factor are not used as a continuum operator or as an arithmetic trace. Gates A--E remain false/open.

9 Source package, *Möbius correlations on a certified Hénon survivor*, commit `34490443f50cfe9af9ff93888e51e7e7e534a5a7`, 2026. RH-366, *Möbius orthogonality, adaptive encoding, and Parry covariance*, repository release, 2026. H. Davenport, On some infinite series involving arithmetical functions (II), *Quart. J. Math.* 8 (1937), 313--320. T. Tao, The logarithmically averaged two-point Chowla and Elliott conjectures, *Forum Math. Pi* 3 (2015), e2.
