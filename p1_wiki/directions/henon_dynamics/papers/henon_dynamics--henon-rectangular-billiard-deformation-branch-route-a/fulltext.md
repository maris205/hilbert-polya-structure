---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rectangular-billiard-deformation-branch-route-a"
canonical_tex: "henon_dynamics/henon_rectangular_billiard_deformation_branch_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rectangular_billiard_deformation_branch_route_a/paper/main.pdf"
source_sha256: "acce690ff841547694d19b8d57005f30cfd4f1fe98ae40f8fab9d3ded6cd304e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rectangular-Billiard Branch Coefficients and Pairwise-Transverse Aspect Crossings

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rectangular_billiard_deformation_branch_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rectangular_billiard_deformation_branch_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rectangular_billiard_deformation_branch_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rectangular_billiard_deformation_branch_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Rectangular Dirichlet billiards provide a natural one-parameter deformation of the square half-wave trace, but their shell multiplicities change when lattice directions collide. We prove a complete source-side statement for every aspect $\alpha>0$. If $R_\alpha(E)=\#\{(m,n)\in\mathbb Z^2:m^2+\alpha^2n^2=E\}$, then the full Abel trace at $t=2\sqrt E$ has the canonical boundary coefficient $\alpha e^{i\pi/4}R_\alpha(E)/(8\pi E^{1/4})$ under $\epsilon^{3/2}$ normalization; negative time gives its conjugate. The proof uses the exact rectangular Poisson formula, a finite shell split, and an $\epsilon$-uniform summable tail; the simultaneous two-boundary pole at $\beta=4$, $E=4$ remains lower order. Writing $\beta=\alpha^2$, distinct absolute lattice directions collide exactly at positive rational values $\beta=(m'^2-m^2)/(n^2-n'^2)$; every pairwise collision is transverse, and irrational $\beta$ therefore has sign-only degeneracy. For $\beta=u/v$, every shell is a fibre $vm^2+un^2=N$. Exact ledgers through coordinate $24$ and four convergence rows are regression sentinels rather than proofs. The coefficient aggregates clean families and is not an isolated stability amplitude or a target divisor law. No arithmetic Euler, root-number, automorphy, Hilbert--Pólya, or Route-B claim is made.
author:
- 'Route-A structural certificate C167'
title: 'Rectangular-Billiard Branch Coefficients and Pairwise-Transverse Aspect Crossings'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid

**Keywords:** Abel half-wave trace; clean-family multiplicity; Poisson duality; rational collision stratum; boundary normalization; spectral geometry.

# Source family

For $\Re s>0$, separation of variables gives $$W_\alpha(s)=\sum_{j,k\ge1}e^{-\pi s\sqrt{j^2+k^2/\alpha^2}}.$$ Two-dimensional Poisson summation yields $$\begin{aligned}
W_\alpha(s)={}&\frac{\alpha s}{2\pi}\sum_{m,n\in\mathbb Z}
 (s^2+4(m^2+\alpha^2n^2))^{-3/2}-\frac14 \notag\\
&-\frac1{2(e^{\pi s}-1)}-\frac1{2(e^{\pi s/\alpha}-1)}. \tag{1}\end{aligned}$$ The dual series is locally normally convergent in the right half-plane.

# Canonical shell coefficient

Let $E>0$ be represented by the dual lattice and put $$R_\alpha(E)=\#\{(m,n)\in\mathbb Z^2:m^2+\alpha^2n^2=E\}.$$ At $t_E=2\sqrt E$ the complete trace satisfies $$\boxed{\lim_{\epsilon\downarrow0}\epsilon^{3/2}
 W_\alpha(\epsilon-it_E)=
 \frac{\alpha e^{i\pi/4}R_\alpha(E)}{8\pi E^{1/4}}.} \tag{2}$$ Negative time gives the complex conjugate. For a matching vector, $s^2+4E=\epsilon(\epsilon-2it_E)$; the principal power in (1) gives one copy of the coefficient in (2). Fixing $\alpha$ and $t_E$, all sufficiently large nonmatching terms are bounded by a constant times $(m^2+n^2)^{-3/2}$. This is summable on $\mathbb Z^2$, while the finite remainder stays bounded. Multiplication by $\epsilon^{3/2}$ kills both. The two boundary subtractions have at most simple poles and therefore also vanish after normalization. This remains true when both subtraction clocks coincide: they form a sum of simple poles rather than a second-order pole. At the hostile control $\beta=4$, $E=4$, the dual shell contains $(\pm2,0)$ and $(0,\pm1)$ while both boundary terms are singular. Their normalized contribution is still $O(\epsilon^{1/2})$, so (2) retains the full multiplicity four.

# Aspect collision law

Write $\beta=\alpha^2$. Distinct absolute representatives $(m,n)$ and $(m',n')$ collide only if $n^2\ne n'^2$, in which case $$\boxed{\beta=\frac{m'^2-m^2}{n^2-n'^2}>0.} \tag{3}$$ Thus every non-sign collision parameter is positive rational, and irrational $\beta$ has sign-only multiplicity. If $\beta=u/v$ in lowest terms, the complete shells are precisely the fibres $vm^2+un^2=N$.

At a collision $\beta_0$, the squared-energy and time separations obey $$\frac{d}{d\beta}(E_p-E_{p'})=n^2-n'^2\ne0,
\qquad
\left.\frac{d}{d\beta}(t_p-t_{p'})\right|_{\beta_0}
=\frac{n^2-n'^2}{\sqrt{E_0}}\ne0. \tag{4}$$ Multiple fibres have distinct $n^2$ slopes for distinct absolute representatives. Hence their pairwise crossings are transverse. Side interchange also gives the exact reciprocal-aspect identity $$W_\alpha(s)=W_{1/\alpha}(s/\alpha), \tag{5}$$ which transports the same source family with the corresponding clock rescaling.

Exact coordinate-$24$ ledgers and high-precision limits are sentinels only. Equation (3), not that ledger, proves the irrational no-collision statement; it does not imply a uniform irrational shell gap. Likewise $vm^2+un^2=N$ is an exact fibre classification, not a claimed universal divisor formula. The strict tuple is $$(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
 \texttt{A4\_NATURAL\_QUANTIZATION}). \tag{6}$$ The coefficient aggregates clean source families. We claim no isolated stability determinant, target trace/divisor/counting law, arithmetic local or Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** All claim-bearing code and data are included; no external dataset is used. **Ethics.** No human participants, animals, or sensitive personal data are involved. **Author contributions/CRediT.** Anonymous technical certificate; Conceptualization, Formal analysis, Software, Validation, and Writing are recorded at package level. **Competing interests.** None known. **Funding.** No external funding is reported. **AI-use disclosure.** An AI coding assistant supported proof planning, drafting, and code review. Packaged exact checks validate quantitative claims; the assistant was not treated as an external peer reviewer.
