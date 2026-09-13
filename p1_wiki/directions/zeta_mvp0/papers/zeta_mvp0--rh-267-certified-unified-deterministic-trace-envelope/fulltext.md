---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-267-certified-unified-deterministic-trace-envelope"
canonical_tex: "zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope/main.pdf"
source_sha256: "72d2c4772529a6857bccfbaf24f71cc6320dc36ea35fcabf65c33deaab713784"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Certified Unified Envelope for Deterministic Numerator Traces

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-267-certified-unified-deterministic-trace-envelope/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove a single all-order geometric envelope for the Hardy-scaled deterministic numerator coefficients. If $q_*=(r_H\lambda)^{-1}=0.7008752258547757\ldots$, then $|a_n|<48q_*^n$ for every $n\ge2$. The constant follows from three Arb-certified residue classes of the reduced trace powers. This is a deterministic target theorem, not a uniform moving-cloud or quotient theorem.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: A Certified Unified Envelope for Deterministic Numerator Traces
```

## Markdown 正文

# Parity formula and trace residues

For odd $n\ge3$, RH-263 gives $a_n=q_*^n/(1+\lambda^{-n})$, so $|a_n|<q_*^n$. For even $n=2m$, $$a_{2m}=r_H^{-2m}\left[2\operatorname{tr}(T^m)+
 \frac{x_m^2(1-2x_m)}{1-x_m^2}\right],\qquad x_m=\lambda^{-m}.
 \label{eq:even}$$ The endpoint fraction has modulus at most $x_m^2$: indeed $x_m\le\lambda^{-1}<\sqrt3-1$ implies $|1-2x_m|\le1-x_m^2$.

Let $m=3k+j$, $j\in\{1,2,3\}$. The RH-13 nuclear certificate [@WangRH13] gives $$|\operatorname{tr}T^m|\le\nu_j q_3^k,
 \quad
 \nu_1<4.623248864,\quad\nu_2<2.930978,\quad\nu_3<0.806064,$$ and $q_3\lambda^6<0.801254<1$.

For $m=3k+j$, $$|a_{2m}|\le\bigl(1+2\nu_j\lambda^{2j}\bigr)q_*^{2m}.$$

Divide [\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"} by $q_*^{2m}=r_H^{-2m}\lambda^{-2m}$. The endpoint term contributes at most one. The trace term is at most $2\nu_j\lambda^{2j}(q_3\lambda^6)^k$, which is bounded by its $k=0$ value.

# Certified unified theorem

The 100-, 150-, and 200-decimal Arb replays certify $$1+2\nu_1\lambda^2<27.054,\quad
 1+2\nu_2\lambda^4<47.538,\quad
 1+2\nu_3\lambda^6<37.062.$$

For every integer $n\ge2$, $$\boxed{|a_n|<48q_*^n.}$$

The odd case has constant one. The lemma and the three strict residue bounds give the even case.

The order-2--28 atlas has observed ratios between $0.825$ and $1.048$, but these finite values are only a cross-check and are not used in the proof. The theorem supplies a deterministic all-order envelope, not a moving-cloud coefficient bridge or a uniform quotient tail. The obligation vector remains $(0,0,0,1,1)$ and Gates A--E remain false/open.
