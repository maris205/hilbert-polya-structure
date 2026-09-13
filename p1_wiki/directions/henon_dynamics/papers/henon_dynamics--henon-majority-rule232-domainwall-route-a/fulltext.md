---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-majority-rule232-domainwall-route-a"
canonical_tex: "henon_dynamics/henon_majority_rule232_domainwall_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_majority_rule232_domainwall_route_a/paper/main.pdf"
source_sha256: "b73ef51de80d48874af20a5b1eb8274718e8262104b9753ba5714926cd14685e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Domain-wall erosion and the complete periodic atlas of cyclic majority rule 232

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_majority_rule232_domainwall_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_majority_rule232_domainwall_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_majority_rule232_domainwall_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_majority_rule232_domainwall_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study the synchronous radius-one majority cellular automaton on every labelled binary cycle. Passing to domain walls gives the exact Boolean law $w_i'=w_i(1\oplus w_{i-1}\oplus w_{i+1})$: each finite wall block erodes by one site at either end per tick. This yields a complete periodic classification: all non-alternating states enter the fixed language in at most $\lfloor(n-1)/2\rfloor$ steps, while the two alternating words at even length form the unique nontrivial two-cycle. Fixed states are counted for every $n$ by a four-state de Bruijn trace, $\#\operatorname{Fix}(F_n)=L_n+2\cos(n\pi/3)$. Parity-twisted run matrices give exact transient-depth populations. These are finite-state, source-local results; they do not supply arithmetic data or a Hilbert--Pólya operator.
author:
- 'Route-A source-local dynamics study'
date: 30 August 2026
title: 'Domain-wall erosion and the complete periodic atlas of cyclic majority rule 232'
```

## Markdown 正文

trailerid \[\<C2512026083000000000000000000000\>\<C2512026083000000000000000000000\>\]

# Frozen dynamics

For $n\geq1$, let $X_n=\{0,1\}^n$ with indices modulo $n$, and define $$(F_nx)_i=\mathbf 1\{x_{i-1}+x_i+x_{i+1}\geq2\}.
 \label{eq:map}$$ The clock is one simultaneous update. Words are labelled: rotations and complements are not quotiented. The small cases $n=1,2$ are retained as degenerate faces, while the wall proof below is uniform; transient/recurrent labels are part of the definition, not inferred from a finite census.

# The wall reduction

Set $w_i=x_i\oplus x_{i+1}$. A site changes exactly when it is isolated, that is, when $w_{i-1}=w_i=1$. Taking the xor of two neighbouring updates in ([\[eq:map\]](#eq:map){reference-type="ref" reference="eq:map"}) gives the local identity $$w_i'=w_i(1\oplus w_{i-1}\oplus w_{i+1})\qquad\text{in }\mathbb F_2.
 \label{eq:wall}$$ The certificate checks all eight neighbourhoods. If a block $1^K$ is bounded by zeros, only its two endpoint walls disappear. Hence $$K(t)=\max\{K-2t,\,K\bmod2\}.
 \label{eq:erosion}$$ Blocks stay separated until one vanishes. The exceptional all-one wall word exists only for even $n$ and is the alternating pair.

Let $K_j$ be the finite wall-block lengths of $x$. If $x$ is not alternating, then $$\tau(x)=\max_j\left\lfloor K_j/2\right\rfloor
 \leq \left\lfloor\frac{n-1}{2}\right\rfloor .
 \label{eq:tau}$$ The bound is sharp: use $0\,1^{n-1}$ for odd $n$ and $0\,1^{n-2}\,0$ for even $n$ (both have even wall parity).

# Periodic states

When every wall block has length at most one, no symbol is isolated and the state is fixed. Conversely, a fixed state cannot contain $010$ or $101$. The all-one wall word is the only case not covered by the erosion lemma.

For every $n$, $\operatorname{Per}(F_n)$ consists of the fixed words avoiding $010$ and $101$, together with one temporal two-cycle when $n$ is even, represented by $0101\cdots$ and $1010\cdots$. There are no temporal periods greater than two.

Equation ([\[eq:erosion\]](#eq:erosion){reference-type="ref" reference="eq:erosion"}) sends every wall word containing a zero to a word with no adjacent ones, hence to a fixed state. The only wall word containing no zero is $1^n$; it is compatible with the xor constraint exactly when $n$ is even, and ([\[eq:map\]](#eq:map){reference-type="ref" reference="eq:map"}) exchanges its two lifts. This also excludes every other cycle.

# Exact fixed counts

The fixed language is a cyclic finite-type language with forbidden triples $010$ and $101$. On pair states $00,01,10,11$, its de Bruijn matrix is $$M=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
 \label{eq:M}$$ Closed walks give $a_n=\operatorname{tr}(M^n)$. A determinant calculation factors its characteristic polynomial as $$\chi_M(\lambda)=(\lambda^2-\lambda-1)(\lambda^2-\lambda+1).
 \label{eq:char}$$ Writing $L_0=2,L_1=1,L_{n+2}=L_{n+1}+L_n$ and $c_0=2,c_1=1,c_{n+2}=c_{n+1}-c_n$, we obtain $$\#\operatorname{Fix}(F_n)=a_n=L_n+c_n=L_n+2\cos(n\pi/3).
 \label{eq:fixed}$$ The first values are $2,2,2,6,12,20,30,46,74,122,200,324$.

# Transient-depth enumeration

For a run bound $m$, let $B_m$ have states $0,\ldots,m$ and entries $B_m[r,0]=1$, $B_m[r,r+1]=1$ for $r<m$. The parity-twisted matrix $B_m^{-}$ changes the latter entries to $-1$. Then $$E_{n,m}=\frac{\operatorname{tr}(B_m^n)+\operatorname{tr}((B_m^{-})^n)}2
 \label{eq:run}$$ counts cyclic wall words of even parity and maximum run at most $m$. Each wall word lifts to two labelled binary words. Therefore differences of $2E_{n,2t+1}$ and $2E_{n,2t-1}$ give the exact number entering the fixed set at time $t$; for even $n$ the all-one wall word is added separately as the two-cycle. This separates a genuine transient census from the recurrent periodic core. In particular, the transfer ledger is a cumulative identity with an explicit parity correction, not a relabelling of the two-cycle as a fixed point.

# Independent certificate and Route-A boundary

The integer producer records 64 fixed-count rows, 216 run-matrix rows, and an exhaustive state census through $n=14$. A producer-independent checker passes 1,855 assertions; an independent SymPy program passes 569 identities; a clean byte replay passes; and all 40 hostile mutations are rejected. The source commit, evaluator hash, fixed epoch, evidence payload, PDF, and file ledger are closed in the release manifest.

The strict Route-A tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, with overall verdict `ROUTE_A_REJECTED`; Route B is disabled. No target prime/zero table, arithmetic local datum, Euler factor, root number, automorphy statement, target divisor or functional equation, or Hilbert--Pólya operator is claimed. The frozen scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 S. Wolfram, "Statistical mechanics of cellular automata," *Rev. Mod. Phys.* 55 (1983), 601--644, [doi:10.1103/RevModPhys.55.601](https://doi.org/10.1103/RevModPhys.55.601). A. L. Toom, "Stable and attractive trajectories in multicomponent systems," in *Multicomponent Random Systems* (1980), 549--575, [doi:10.1007/978-1.4613-3044-2\_19](https://doi.org/10.1007/978-1-4613-3044-2_19).
