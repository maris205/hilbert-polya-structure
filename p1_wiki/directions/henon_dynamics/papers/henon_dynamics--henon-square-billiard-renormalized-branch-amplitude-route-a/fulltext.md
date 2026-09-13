---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-square-billiard-renormalized-branch-amplitude-route-a"
canonical_tex: "henon_dynamics/henon_square_billiard_renormalized_branch_amplitude_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_square_billiard_renormalized_branch_amplitude_route_a/paper/main.pdf"
source_sha256: "bbbc665cb388e4ee4cdc88622106722b238d007251e651b0016be6c6382d59c5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Renormalized Branch Amplitudes for the Square-Billiard Abel Trace

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_square_billiard_renormalized_branch_amplitude_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_square_billiard_renormalized_branch_amplitude_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_square_billiard_renormalized_branch_amplitude_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_square_billiard_renormalized_branch_amplitude_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the Dirichlet half-wave trace $W_D$ of the unit square, we prove that every nonzero source lattice shell admits a canonical full-trace normalization. At $t_N=2\sqrt N$, $\epsilon^{3/2}W_D(\epsilon-it_N)$ tends to $e^{i\pi/4}r_2^{\rm src}(N)/(8\pi N^{1/4})$; negative time gives its complex conjugate. This advances the earlier branch-location theorem by extracting a finite coefficient from the complete trace, including times where the boundary subtraction has a coincident simple pole. The proof fixes the phase with the principal branch, splits off finitely many shells, and uniformly dominates the infinite remainder by the summable two-dimensional $|m|^{-3}$ tail. Exact shells through $N=800$ and high-precision convergence rows are regression sentinels, not the proof. The coefficient is aggregate clean-family multiplicity, not an isolated stability amplitude or target divisor law, and no arithmetic Euler or Hilbert--Pólya claim is made.
author:
- 'Route-A structural certificate C162'
title: 'Renormalized Branch Amplitudes for the Square-Billiard Abel Trace'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid

**Keywords:** square billiard; Abel half-wave trace; clean family; branch singularity; boundary normalization; Poisson summation.

# Exact source trace

For $\Re s>0$, the unit-square Dirichlet trace is $$W_D(s)=\operatorname{Tr}e^{-s\sqrt{\Delta_D}}
=\sum_{j,k\ge1}e^{-\pi s\sqrt{j^2+k^2}}.$$ C157 established the exact principal-branch Poisson representation $$W_D(s)=\frac{s}{2\pi}\sum_{m\in\mathbb Z^2}
(s^2+4|m|^2)^{-3/2}-\frac14-\frac1{e^{\pi s}-1}.              \tag{1}$$ The dual series is locally normally convergent in the right half-plane.

# Canonical full-trace limit

Let $N\ge1$, $t_N=2\sqrt N$, and $r_2^{\rm src}(N)=\#\{m\in\mathbb Z^2:|m|^2=N\}$. Then $$\boxed{\lim_{\epsilon\downarrow0}\epsilon^{3/2}
W_D(\epsilon-it_N)=
\frac{e^{i\pi/4}r_2^{\rm src}(N)}{8\pi N^{1/4}}.}            \tag{2}$$ At $-t_N$ the limit is the complex conjugate. Indeed the spectral coefficients are real, so $W_D(\overline{s})=\overline{W_D(s)}$ throughout the right half-plane; the principal dual representation in (1) has the same conjugation symmetry.

For a matching vector, with $s=\epsilon-it_N$, $s^2+4N=\epsilon(\epsilon-2it_N)$. Its normalized contribution tends to $$\frac{-it_N}{2\pi}(-2it_N)^{-3/2}
=\frac{e^{i\pi/4}}{8\pi N^{1/4}},                            \tag{3}$$ where the phase is fixed by the principal power. Multiplication by the number of matching vectors gives the right side of (2).

The infinite remainder requires a uniform argument. Fix $t_N$ and $0<\epsilon\le1$. Choose $R$ so that $4|m|^2\ge2(t_N^2+1)$ for $|m|\ge R$. Then $$|s^2+4|m|^2|\ge4|m|^2-|s|^2\ge2|m|^2,$$ so the tail is dominated uniformly by a constant times $\sum_{m\ne0}|m|^{-3}<\infty$. The finitely many nonmatching shells stay bounded. Dominated convergence and $\epsilon^{3/2}$ kill all these terms. If $t_N$ is even, the subtraction term in (1) can have a simple pole, but its normalized size is only $O(\epsilon^{1/2})$. More precisely, this coincidence means $N=k^2$ and $t_N=2k$, whence $$-\frac1{e^{\pi(\epsilon-i2k)}-1}
=-\frac1{\pi\epsilon}+\frac12+O(\epsilon).$$ After multiplication by $\epsilon^{3/2}$ the pole is $-\epsilon^{1/2}/\pi+O(\epsilon^{3/2})$ and vanishes. The Weyl zero-mode is bounded at $t_N\ne0$, and the constant term is also killed. This proves a limit for the full trace, not just one summand.

# Certificate and boundary

Exact reconstruction through $N=800$ finds 270 occupied shells and 2520 nonzero lattice vectors; 28 occupied square norms coincide with simple-pole times. The shell $N=65$ retains the first four ordered positive primitive directions. Local high-precision rows at $N=1,2,5,13,65$ check convergence but are not the proof. For each shell, the exact ledger separately records the four axis vectors when $N$ is a square and all nonaxis sign lifts; gcd reduction of every nonaxis vector retains its primitive direction and repetition. Their total is exactly $r_2^{\rm src}(N)$ in (2), so no multiplicity is inferred from floating data.

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_NATURAL\_QUANTIZATION})$: $\sqrt{\Delta_D}$ is a natural self-adjoint source operator, but the coefficient aggregates positive-dimensional clean families. We claim no isolated stability determinant, target trace/divisor/counting law, arithmetic local/Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** All claim-bearing data and code are included; no external dataset is used. **Ethics.** No human participants, animals, or sensitive personal data are involved. **Author contributions/CRediT.** Anonymous technical certificate; Conceptualization, Formal analysis, Software, Validation, and Writing are recorded at package level. **Competing interests.** None known. **Funding.** No external funding is reported. **AI-use disclosure.** An AI coding assistant supported derivation planning, drafting, and code review. Packaged independent checks validate quantitative claims; the assistant was not treated as an external peer reviewer.
