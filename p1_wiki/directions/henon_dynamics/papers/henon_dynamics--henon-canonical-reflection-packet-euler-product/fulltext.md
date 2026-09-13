---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-canonical-reflection-packet-euler-product"
canonical_tex: "henon_dynamics/henon_canonical_reflection_packet_euler_product/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_canonical_reflection_packet_euler_product/paper/paper.pdf"
source_sha256: "b548bfaad36cfe37e88bd02b8594b726563043cf5c831006ab27004e94fc887e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Canonical Reflection-Packet Euler Product and Its Essential Boundary Singularity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_canonical_reflection_packet_euler_product>)
- [规范 TeX](<../../../../../henon_dynamics/henon_canonical_reflection_packet_euler_product/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_canonical_reflection_packet_euler_product/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_canonical_reflection_packet_euler_product/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_canonical_reflection_packet_euler_product/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Odd reflection packets in the full Hénon horseshoe admit a unique normalized linear sampler invariant under symbolic coboundaries. We promote that sampler to a canonical packet-mean Euler product. Its logarithmic derivative has an exact primitive/repetition divisor law, and the product converges in an explicit disk. In the unweighted case its radius is $2^{-1/2}$ and $$\log\mathcal Z_0(z)
   =\frac{1}{\sqrt2(1-\sqrt2z)}+G(z),$$ where $G$ is analytic near the positive boundary point. Consequently the Euler product has an exponential essential singularity there, rather than a meromorphic pole. We distinguish this restricted packet object from the standard Lind zeta of the full infinite-dihedral action and from an orbit-resolved weighted determinant. The result is an exact Route-A analytic germ and an exact obstruction to one naive Fredholm promotion; it supplies no rational-prime trace or operator.
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
  A Canonical Reflection-Packet Euler Product\
  and Its Essential Boundary Singularity
```

## Markdown 正文

# Canonical data and source boundary

Consider the area-preserving Hénon map $H(x,y)=(6-x^2-y,x)$. The inherited hyperbolic coding identifies its real chain-recurrent set with the full two-shift and intertwines a reversor with sequence reversal [@DevaneyNitecki1979; @Arai2007]. For odd $n$, let $A_n$ denote the primitive marked reflection packet. Its exact cardinality is $$\label{eq:Dn}
 D_n=|A_n|=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}.$$ The preceding canonical-sampler theorem proves that $$\label{eq:bn}
 b_n(f)=\frac{1}{nD_n}\sum_{\omega\in A_n}\sum_{j=0}^{n-1}
 f(\sigma^j\omega)$$ is the unique normalized real linear sampler on these cycles that annihilates every coboundary. In particular, $$\label{eq:gauge}
 b_n(f+u-u\circ\sigma)=b_n(f)$$ exactly at each finite period.

There is already a standard zeta theory for flip systems. A flip and the shift generate an action of the infinite dihedral group, and the Lind zeta is defined by fixed-point counts for all finite-index subgroups. The exact decomposition in @KimLeePark2003 combines a square root of the ordinary shift zeta with odd and even flip fixed-point series; matrix extensions appear in @Ryu2019. Our object below is deliberately narrower: it uses only the odd primitive packet in [\[eq:Dn\]](#eq:Dn){reference-type="eqref" reference="eq:Dn"} and the aggregate mean [\[eq:bn\]](#eq:bn){reference-type="eqref" reference="eq:bn"}. We do not identify it with the Lind zeta.

# The packet-mean Euler product

For bounded continuous $f$, define $$\label{eq:product}
 \mathcal Z_f(z,s)=\prod_{\substack{n\ge1\\n\ \mathrm{odd}}}
 \left(1-z^n e^{-sn b_n(f)}\right)^{-D_n}.$$ One sufficient absolute-convergence condition is $$\label{eq:safedisk}
 \sqrt2\,|z|e^{|s|\lVert f\rVert_\infty}<1,$$ because $D_n\le2^{(n+1)/2}$. Thus [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} defines a nonzero analytic germ. Equation [\[eq:gauge\]](#eq:gauge){reference-type="eqref" reference="eq:gauge"} makes it exactly cohomology invariant in this disk.

[\[thm:ledger\]]{#thm:ledger label="thm:ledger"} In the disk of absolute convergence, $$\begin{aligned}
 \log\mathcal Z_f(z,s)
 &=\sum_{\substack{n\ge1\\n\ \mathrm{odd}}}D_n
   \sum_{r\ge1}\frac{z^{nr}e^{-srn b_n(f)}}{r},\label{eq:log}\\
 [z^m]\,z\partial_z\log\mathcal Z_f(z,s)
 &=\sum_{\substack{n\mid m\\n\ \mathrm{odd}}}
 nD_ne^{-sm b_n(f)}.\label{eq:logder}\end{aligned}$$

Expand $-\log(1-w)=\sum_{r\ge1}w^r/r$ in [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}; absolute convergence justifies rearrangement. Differentiation multiplies the $(n,r)$ term by $nr$, and collecting $m=nr$ gives [\[eq:logder\]](#eq:logder){reference-type="eqref" reference="eq:logder"}.

The divisor condition in [\[eq:logder\]](#eq:logder){reference-type="eqref" reference="eq:logder"} distinguishes a primitive packet of length $n$ from its $r$-fold repetition. It does not retain the distribution of individual orbit weights within $A_n$: all factors at one period receive the common mean $b_n(f)$. This mean-field firewall becomes the next research gate.

# The unweighted entropy boundary

Set $s=0$ and write $\mathcal Z_0(z)=\mathcal Z_f(z,0)$. The primitive generating series can be summed exactly.

[\[prop:Dseries\]]{#prop:Dseries label="prop:Dseries"} For $|z|<2^{-1/2}$, $$\label{eq:Dseries}
 D(z):=\sum_{\substack{n\ge1\\n\ \mathrm{odd}}}D_nz^n
 =\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}
 \mu(k)\frac{2z^k}{1-2z^{2k}}.$$ Its radius is $R=2^{-1/2}$, and near the positive point $R$, $$\label{eq:Dprincipal}
 D(z)=\frac{1}{\sqrt2(1-\sqrt2z)}+G_1(z)$$ with $G_1$ analytic.

Substitute [\[eq:Dn\]](#eq:Dn){reference-type="eqref" reference="eq:Dn"}, put $n=km$, and interchange the absolutely convergent sums. Since $m$ is odd, $$\sum_{m\ \mathrm{odd}}2^{(m+1)/2}z^{km}
 =\frac{2z^k}{1-2z^{2k}},$$ which proves [\[eq:Dseries\]](#eq:Dseries){reference-type="eqref" reference="eq:Dseries"}. The $k=1$ term satisfies $$\label{eq:partialfraction}
 \frac{2z}{1-2z^2}
 =\frac{1}{\sqrt2(1-\sqrt2z)}
  -\frac{1}{\sqrt2(1+\sqrt2z)}.$$ Every $k\ge3$ term is analytic in a neighborhood of $R$. Positivity of $D_n$ and the pole in [\[eq:partialfraction\]](#eq:partialfraction){reference-type="eqref" reference="eq:partialfraction"} give the radius.

[\[thm:essential\]]{#thm:essential label="thm:essential"} There is a function $G$, analytic near $R=2^{-1/2}$, such that $$\label{eq:logprincipal}
 \log\mathcal Z_0(z)=\frac{1}{\sqrt2(1-\sqrt2z)}+G(z).$$ Consequently $\mathcal Z_0$ has an essential singularity at $R$.

The $r=1$ part of [\[eq:log\]](#eq:log){reference-type="eqref" reference="eq:log"} is $D(z)$. For $r\ge2$, the series $$\sum_{n\ \mathrm{odd}}D_n\sum_{r\ge2}\frac{z^{nr}}r$$ is analytic for $|z|<2^{-1/4}$, which strictly contains a neighborhood of the positive point $R$. Combine this with [\[prop:Dseries\]](#prop:Dseries){reference-type="ref" reference="prop:Dseries"}. Exponentiating [\[eq:logprincipal\]](#eq:logprincipal){reference-type="eqref" reference="eq:logprincipal"} gives a nonvanishing analytic factor times the exponential of a simple pole, and hence an essential singularity.

This theorem is an analytic obstruction to calling [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} a meromorphic Fredholm determinant at its entropy boundary. It is not a no-go theorem for a separately renormalized relative determinant.

# Exact audit and route status

The accompanying implementation computes $D_n$ through period $41$ by Möbius inversion and independently by divisor subtraction. It expands the Euler product through order $41$ and recovers [\[eq:logder\]](#eq:logder){reference-type="eqref" reference="eq:logder"} from the coefficient identity $zZ'= (zZ'/Z)Z$. Eight tests pass in normal and optimized modes; five upstream artifacts are hash locked and 25 hostile mutations are rejected.

The strongest positive result is the exact canonical Euler germ and its repetition law. The strongest obstruction is the essential boundary singularity. Route A records an A2 certified prefix and partial A3 analytic structure, but no prime semantics. No rational-prime labels, von Mangoldt amplitudes, transfer operator, self-adjoint generator, or completed Riemann determinant has been constructed; Route B is not authorized. The next minimal theorem is to compare [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} with the orbit-resolved exponential moment. Its first missing invariant is within-period variance.
