---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-relative-lind-essential-ladder"
canonical_tex: "henon_dynamics/henon_relative_lind_essential_ladder/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_relative_lind_essential_ladder/paper/paper.pdf"
source_sha256: "d79b494152b8ea42c97c338e75d04698b546f2e97403cc9688021574d07a09fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Infinite Essential-Singularity Ladder beyond the Local Hénon--Lind Counterterm

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_relative_lind_essential_ladder>)
- [规范 TeX](<../../../../../henon_dynamics/henon_relative_lind_essential_ladder/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_relative_lind_essential_ladder/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_relative_lind_essential_ladder/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_relative_lind_essential_ladder/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The odd reflection-packet Euler product of the full Hénon horseshoe and the Lind zeta of the full two-shift reverse action admit a unique local relative counterterm at their common entropy boundary. We determine what happens after that first cancellation. Writing $\Phi(x)=2x/(1-2x^2)$, we prove the exact regrouping $$\log\mathcal Z_{\rm orb}(t,1)=\sum_{m\ge1}c_m\Phi(t^m),\qquad
   c_m=\frac1m\prod_{\substack{p\mid m\\p\ {\rm odd}}}(1-p).$$ Every coefficient $c_m$ is nonzero. The locally normalized relative germ therefore continues, on punctured branches, as $$\log C_{\rm rel}(t)=H_{\rm rel}(1-\sqrt2t)
   -\sum_{m\ge2}c_m\Phi(t^m),$$ where $H_{\rm rel}$ is explicit and regular on the positive corridor. For every $m\ge2$, the point $\rho_m=2^{-1/(2m)}$ is an exponential essential singularity, and $\rho_m\nearrow1$. Thus the first-boundary counterterm is locally exact but cannot globalize to a meromorphic finite-state or holomorphic trace-class Fredholm determinant on the unit disk. A punctured-domain infinite-rank model remains open; no arithmetic trace or Route-B claim is made.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  An Infinite Essential-Singularity Ladder beyond the\
  Local Hénon--Lind Counterterm
```

## Markdown 正文

# The local bridge and the global question

For the full two-shift with reverse flip, @KimLeePark2003 [Example 4.3] give $$\label{eq:lind}
 \zeta_{\rm flip}(t)=(1-2t^2)^{-1/2}
 \exp\!\left(\frac{2t+3t^2}{1-2t^2}\right).$$ The conjugate full Hénon horseshoe [@DevaneyNitecki1979] also carries the different odd marked-reflection product $$\label{eq:packet-product}
 \mathcal Z_{\rm orb}(t,1)=\prod_{\substack{n\ge1\\n\ {\rm odd}}}(1-t^n)^{-D_n},$$ where $D_n$ is the number of primitive marked reflection words of period $n$. This product is not the full infinite-dihedral Lind zeta.

Put $u=1-\sqrt2t$. The preceding local comparison proves that $$\label{eq:counterterm}
 C_{\rm rel}(t)=u^{1/2}e^{-3/(4u)}
 \frac{\zeta_{\rm flip}(t)}{\mathcal Z_{\rm orb}(t,1)}$$ extends holomorphically and nonvanishingly across $u=0$ on a local branch. The power $1/2$ and exponential coefficient $3/4$ are unique. The present paper asks whether this local germ can be a meromorphic determinant on the whole unit disk.

# A scalar-channel regrouping

Let $$\label{eq:Phi}
 \Phi(x)=\frac{2x}{1-2x^2}.$$ All odd reflection words have generating function $\Phi(t)$, and primitive dilation Möbius inversion gives $$\label{eq:primitive}
 E(t):=\sum_{\substack{n\ge1\\n\ {\rm odd}}}D_nt^n
 =\sum_{\substack{k\ge1\\k\ {\rm odd}}}\mu(k)\Phi(t^k).$$ Taking the logarithm of [\[eq:packet-product\]](#eq:packet-product){reference-type="eqref" reference="eq:packet-product"}, first in its disk of absolute convergence, yields $$\label{eq:repetition}
 \log\mathcal Z_{\rm orb}(t,1)=\sum_{r\ge1}\frac1rE(t^r).$$

[\[thm:channels\]]{#thm:channels label="thm:channels"} For $|t|<2^{-1/2}$, $$\label{eq:channels}
 \log\mathcal Z_{\rm orb}(t,1)=\sum_{m\ge1}c_m\Phi(t^m),$$ where $$\label{eq:cm}
 c_m=\frac1m\sum_{\substack{k\mid m\\k\ {\rm odd}}}k\mu(k)
 =\frac1m\prod_{\substack{p\mid m\\p\ {\rm odd}}}(1-p).$$ In particular, $c_m\ne0$ for every $m\ge1$.

Insert [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"} into [\[eq:repetition\]](#eq:repetition){reference-type="eqref" reference="eq:repetition"} and group terms with $m=kr$. The coefficient of $\Phi(t^m)$ is $$\sum_{\substack{k\mid m\\k\ {\rm odd}}}\frac{\mu(k)}{m/k}
 =\frac1m\sum_{\substack{k\mid m\\k\ {\rm odd}}}k\mu(k).$$ The sum is multiplicative on the odd radical of $m$, giving the Euler product in [\[eq:cm\]](#eq:cm){reference-type="eqref" reference="eq:cm"}. Every factor $1-p$ is nonzero.

The decomposition is more than a coefficient identity: each $m$ is now an independent rational singular channel.

# Continuation after the first cancellation

The $m=1$ channel is precisely $\Phi(t)=2t/(1-2t^2)$. Direct substitution into [\[eq:lind\]](#eq:lind){reference-type="eqref" reference="eq:lind"} gives the following exact regular remainder.

[\[prop:relative\]]{#prop:relative label="prop:relative"} Set $$\label{eq:Hrel}
 H_{\rm rel}(u)=-\frac12\log(2-u)
 -\frac{3(2u-3)}{4(u-2)}.$$ On every compatible branch that begins at the origin and avoids the stated singular points, $$\label{eq:relative-cont}
 \log C_{\rm rel}(t)=H_{\rm rel}(1-\sqrt2t)
 -\sum_{m\ge2}c_m\Phi(t^m).$$ The series is normally convergent on compact subsets of $|t|<1$ that avoid the zeros of $1-2t^{2m}$, $m\ge2$.

The logarithm of [\[eq:counterterm\]](#eq:counterterm){reference-type="eqref" reference="eq:counterterm"} is $$\tfrac12\log u-\frac{3}{4u}+\log\zeta_{\rm flip}(t)
 -\log\mathcal Z_{\rm orb}(t,1).$$ Because $1-2t^2=u(2-u)$, subtracting the $m=1$ channel gives exactly $$\tfrac12\log u+\log\zeta_{\rm flip}(t)-\frac{3}{4u}-\Phi(t)
 =H_{\rm rel}(u).$$ This proves [\[eq:relative-cont\]](#eq:relative-cont){reference-type="eqref" reference="eq:relative-cont"} in the initial disk and hence by continuation. Also $|c_m|\le1$. On a compact set with $|t|\le r<1$, all sufficiently large terms satisfy $|\Phi(t^m)|\ll r^m$; the finitely many earlier denominators are bounded away from zero. This proves normal convergence off the punctures.

Notice that [\[eq:Hrel\]](#eq:Hrel){reference-type="eqref" reference="eq:Hrel"} is regular throughout the positive interval $0<t<1$. All later positive singularities therefore come from the packet channels, not from the source Lind factor.

# The infinite essential-singularity ladder

For $m\ge1$, define $$\label{eq:rho}
 \rho_m=2^{-1/(2m)},\qquad v_m=1-t/\rho_m.$$ Then $1-2t^{2m}=2mv_m+O(v_m^2)$ and $2t^m=\sqrt2+O(v_m)$.

[\[thm:ladder\]]{#thm:ladder label="thm:ladder"} For each $m\ge2$, the continuation in [\[eq:relative-cont\]](#eq:relative-cont){reference-type="eqref" reference="eq:relative-cont"} has $$\label{eq:principal}
 \log C_{\rm rel}(t)=
 -\frac{c_m}{\sqrt2\,m}\frac1{1-t/\rho_m}
 +G_m(t),$$ where $G_m$ is holomorphic near $\rho_m$. Consequently $C_{\rm rel}$ has an exponential essential singularity at every $\rho_m$, and $$\label{eq:ladder-limit}
 2^{-1/4}=\rho_2<\rho_3<\cdots<1,\qquad \rho_m\longrightarrow1.$$

At the positive point $\rho_m$, the equation $1-2\rho_m^{2j}=0$ holds only when $j=m$. Hence all channels except the $m$th are holomorphic there. The local expansion above gives $$\Phi(t^m)=\frac{1}{\sqrt2\,m}\frac1{v_m}+O(1).$$ Insert this into [\[eq:relative-cont\]](#eq:relative-cont){reference-type="eqref" reference="eq:relative-cont"}. By [\[eq:cm\]](#eq:cm){reference-type="eqref" reference="eq:cm"}, $c_m\ne0$, so exponentiating the nonzero simple pole in [\[eq:principal\]](#eq:principal){reference-type="eqref" reference="eq:principal"} produces an essential singularity. Monotonicity and the limit in [\[eq:ladder-limit\]](#eq:ladder-limit){reference-type="eqref" reference="eq:ladder-limit"} are immediate.

The $m=1$ singularity is exactly the one removed by the unique P71 counterterm. The theorem says that this cancellation is genuinely local: it reveals, rather than removes, all later channels.

# Determinant obstruction and scope

[\[cor:no-det\]]{#cor:no-det label="cor:no-det"} The relative continuation $C_{\rm rel}$ is not meromorphic on the unit disk. In particular, it cannot equal a finite-dimensional determinant or a quotient of holomorphic trace-class Fredholm determinants on that disk.

A meromorphic function has only poles as isolated nonremovable singularities. By [\[thm:ladder\]](#thm:ladder){reference-type="ref" reference="thm:ladder"}, $C_{\rm rel}$ has infinitely many isolated essential singularities inside the disk. Finite-dimensional determinants are holomorphic polynomials, and a quotient of holomorphic Fredholm determinants is meromorphic.

This is an object-specific obstruction, not a prohibition on every operator model. A transfer operator may live on a slit or punctured domain, use an infinite singular counterterm, or fail to be trace class at the ladder. No such model is constructed here. Nor do the channel indices $m$ carry rational-prime or von-Mangoldt semantics. Route A gains an exact global analytic obstruction but no arithmetic advance; Route B remains unauthorized.

# Executable certificate

The certificate verifies [\[eq:cm\]](#eq:cm){reference-type="eqref" reference="eq:cm"} in divisor-sum and Euler-product forms, compares [\[eq:channels\]](#eq:channels){reference-type="eqref" reference="eq:channels"} coefficientwise with the primitive Euler product through degree 48, and records the first 24 singular channels. An independent implementation reconstructs 64 channels without importing the main module. Eight tests pass in normal and optimized modes, six dependencies are hash-locked, and 25 claim mutations are rejected. The finite ledger certifies the algebra; [\[thm:channels,thm:ladder\]](#thm:channels,thm:ladder){reference-type="ref" reference="thm:channels,thm:ladder"} prove the all-$m$ statements.
