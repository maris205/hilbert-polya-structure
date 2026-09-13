---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-315-root-of-unity-moment-packet-isolation"
canonical_tex: "zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation/main.pdf"
source_sha256: "cbd53c16adcc2b05c9842fc694897c81c7612ee3114b5f26a10cbd5b7aceda03"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Root-of-Unity Packets that Isolate a Single Power Moment

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-315-root-of-unity-moment-packet-isolation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a genuine finite normal spectrum that changes one prescribed power moment without changing any lower moment. The packet consists of a complete root set of a real monomial equation, repeated with integer multiplicity. Its entire moment sequence, radius, rank, and squared mass are explicit. This supplies the triangular atom needed for exact finite-prefix spectral realization, while making no identification with the actual noisy operator.
author:
- Bin Wang
date: July 2026
title: 'Root-of-Unity Packets that Isolate a Single Power Moment'
```

## Markdown 正文

# Packet definition

Fix $d,L\ge1$ and $w\in\mathbb R\setminus\{0\}$. Let $$\mathcal P_d(w,L)=
 \{\mu:\mu^d=w/(dL)\},$$ with every root repeated $L$ times. Since the defining polynomial has real coefficients, the multiset is closed under complex conjugation.

The packet has rank $dL$, radius $$r_d=(|w|/(dL))^{1/d},$$ and power sums $$p_n(\mathcal P_d)=0\quad(d\nmid n),
 \qquad
 p_{md}(\mathcal P_d)=\frac{w^m}{(dL)^{m-1}}.$$ In particular, $p_n=0$ for $n<d$ and $p_d=w$. Its squared spectral mass is $$M_2=dLr_d^2.$$

Write the roots as $r_de^{i(\theta+2\pi j)/d}$. The roots-of-unity sum vanishes unless $d$ divides $n$. At $n=md$, summing and multiplying by $L$ gives $Ld(w/(dL))^m$, which is the stated formula. The geometric quantities are immediate.

For $q>0$, if $$L\ge\frac{|w|}{dq^d},$$ then every packet root satisfies $|\mu|\le q$.

The packet is an unweighted finite spectrum with integer multiplicities, not merely a positive moment measure. It is nevertheless synthetic: no theorem identifies it with eigenvalues of the noisy transfer operator. Gates A--E remain false/open.
