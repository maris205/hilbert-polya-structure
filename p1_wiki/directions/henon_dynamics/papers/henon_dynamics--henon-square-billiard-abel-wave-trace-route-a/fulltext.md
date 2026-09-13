---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-square-billiard-abel-wave-trace-route-a"
canonical_tex: "henon_dynamics/henon_square_billiard_abel_wave_trace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_square_billiard_abel_wave_trace_route_a/paper/main.pdf"
source_sha256: "dff63f8cb8eeb3828345eae930ca1e55528c021f57bddbf34232ca9831993839"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Abel Half-Wave Trace for Square-Billiard Clean Families

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_square_billiard_abel_wave_trace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_square_billiard_abel_wave_trace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_square_billiard_abel_wave_trace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_square_billiard_abel_wave_trace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We derive a two-dimensional Poisson formula for the genuine Dirichlet Abel half-wave trace of the unit square. Its nonaxis dual terms reorganize exactly by ordered positive primitive billiard directions and repetitions, retaining clean-family lengths and collisions. Exact shell ledgers and tail-bounded complex sentinels certify the formula. The result is a source trace and natural quantization, not an isolated-orbit determinant or target identity.
author:
- 'Route-A structural certificate C157'
title: 'An Abel Half-Wave Trace for Square-Billiard Clean Families'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid

**Keywords:** square billiard; Abel trace; half-wave operator; Poisson summation; clean families; primitive directions.

# Dirichlet Abel trace

For the unit-square Dirichlet Laplacian, set $$W_D(s)=\sum_{j,k\ge1}e^{-\pi s\sqrt{j^2+k^2}},\qquad \Re s>0.     \tag{1}$$ With the convention $\widehat f(m)=\int_{\mathbb R^2}f(x)e^{-2\pi i m\cdot x}\,dx$, radial transformation gives $$\widehat{e^{-\pi s|x|}}(m)
=\frac{2s}{\pi(s^2+4|m|^2)^{3/2}}.                              \tag{2}$$ For real positive $s$, Poisson summation and $\Theta=1+4/(e^{\pi s}-1)+4W_D$ yield $$W_D(s)=\frac{s}{2\pi}\sum_{m\in\mathbb Z^2}
(s^2+4|m|^2)^{-3/2}-\frac14-\frac1{e^{\pi s}-1}.                \tag{3}$$ The primal exponential sum and dual $|m|^{-3}$ sum converge locally normally. For $\Re s>0$, $s^2+4|m|^2$ avoids the nonpositive real axis, so the principal power is holomorphic; analytic continuation proves (3) on the half-plane.

# Primitive directions and repetitions

The dual zero mode is $1/(2\pi s^2)$ and the four axes contribute $$\frac{2s}{\pi}\sum_{r\ge1}(s^2+4r^2)^{-3/2}.                   \tag{4}$$ Every nonaxis vector is uniquely $(\pm ra,\pm rb)$ with $a,b\ge1$, $\gcd(a,b)=1$. Thus the interior is $$\frac{2s}{\pi}\sum_{\substack{a,b\ge1\\(a,b)=1}}\sum_{r\ge1}
\bigl(s^2+r^2L_{a,b}^2\bigr)^{-3/2},\qquad
L_{a,b}=2\sqrt{a^2+b^2}.                                      \tag{5}$$ Four sign lifts produce the coefficient in (5), while ordered coordinate swaps remain distinct. For $s=\epsilon-it$, its principal-power branch points occur at $t=\pm rL_{a,b}$; these are the square-billiard clean-family lengths with every repetition retained.

# Boundary strata and certified truncation

The Abel boundary contains four separately derived contributions:

1.  the $m=0$ Weyl term $1/(2\pi s^2)$;

2.  axis $-3/2$ branches at $t=\pm2r$;

3.  interior clean-family $-3/2$ branches at $t=\pm rL_{a,b}$;

4.  simple poles of $-1/(e^{\pi s}-1)$ at $s=2iq$, equivalently $t\in2\mathbb Z$.

Axis branches may coincide with boundary-subtraction poles, but their singularity types differ and no cancellation is asserted. In particular, the branch list is not presented as the complete boundary singular set.

For numerical verification, if the primal box is $1\le j,k\le J$, then $$|R_J|\le\frac{2q^{J+2}}{(1-q)^2},\qquad
q=e^{-\pi\Re(s)/\sqrt2}.                                      \tag{6}$$ For an integer max-norm cutoff $M\ge |s|$, subtract on the dual side $1/(8|m|^3)-3s^2/(64|m|^5)$ and add the exact Epstein sums $4\zeta(\alpha)\beta(\alpha)$ for $\alpha=3/2,5/2$. Taylor's theorem and the $8k$ points of max norm $k$ bound the accelerated tail by $$\frac{|s|^5}{2\pi3^{5/2}M^5}.                                 \tag{7}$$

# Certificate and Route-A boundary

Through squared norm $500$, the exact ledger contains $98$ primitive shells, $239$ ordered primitive directions, $161$ occupied dual shells, and $373$ ordered positive vectors. The first fourfold primitive collision is $$(1,8),(4,7),(7,4),(8,1),\qquad a^2+b^2=65.$$ At $s=0.9+0.4i$ and $s=1.3+0.7i$, two complex sentinels compare (1) against an Epstein-accelerated form of (3), with respective absolute differences $5.18\times10^{-13}$ and $3.92\times10^{-12}$, reported beside explicit analytic truncation bounds. The deterministic 55-digit centers are not interval-arithmetic outputs.

The tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_NATURAL\_QUANTIZATION})$. Although $W_D=\operatorname{Tr}e^{-s\sqrt{\Delta_D}}$ is a genuine source trace, the periodic sets are clean families. We claim no isolated-orbit determinant or stability amplitude, target trace/divisor/functional equation or counting law, arithmetic local/Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Declarations {#declarations .unnumbered}

**Data availability.** All claim-bearing data are the exact shell JSON and scripts in this C157 package; no external dataset is used. **Ethics.** The work uses no human participants, animals, or sensitive personal data. **Author contributions/CRediT.** This is an anonymous technical certificate with no individual authorship assignment; package provenance records Conceptualization, Formal analysis, Software, Validation, and Writing roles. **Competing interests.** None known. **Funding.** No external funding is reported. **AI-use disclosure.** An AI coding assistant supported drafting, derivation checks, and code review. Exact scripts and independent paths reproduce every quantitative claim; the assistant was not treated as an external peer reviewer.
