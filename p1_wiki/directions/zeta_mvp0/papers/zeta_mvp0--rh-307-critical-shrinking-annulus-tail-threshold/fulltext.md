---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-307-critical-shrinking-annulus-tail-threshold"
canonical_tex: "zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold/main.pdf"
source_sha256: "ca5ed91a79bf170e1da2e9b5b97a97f3a10f90c331dde406959d884518b75812"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Critical Shrinking-Annulus Threshold at the Minimal Tail Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-307-critical-shrinking-annulus-tail-threshold/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The minimal tail-absorbed clock is shorter than the slope-four clock, but its noisy tail is only logarithmically small on the target circle. We determine how rapidly an auxiliary radius may separate from that circle. If $\rho_\sigma=Re^{\eta_\sigma}$ and $h_\sigma=\lceil a_*\log(1/\sigma)\rceil$, the mass-and-cap noisy-tail scale is $e^{a_*L_\sigma\eta_\sigma}/L_\sigma$. For $\eta_\sigma=c\log L_\sigma/L_\sigma$, the sharp information-class threshold is $c_*=1/a_*=\log(10/7)$. A diagonal multiset consisting of repeated $q$-atoms saturates all three regimes. The result controls the tail only; the moving head remains open.
author:
- Bin Wang
date: July 2026
title: 'The Critical Shrinking-Annulus Threshold at the Minimal Tail Clock'
```

## Markdown 正文

# Minimal clock and moving radius

Put $$q=\frac12,\quad R=\frac75,\quad
 a_*=\frac1{\log(1/(qR))}=\frac1{\log(10/7)},\quad
 L_\sigma=\log(1/\sigma),\quad
 h_\sigma=\lceil a_*L_\sigma\rceil.$$ Let $\rho_\sigma=Re^{\eta_\sigma}$, where $\eta_\sigma\downarrow0$, and assume $\rho_\sigma<\rho_*$. For complement traces satisfying $|\tau_{\sigma,n}|\le4\sigma^{-1}q^n$, define their tail logarithm beyond $h_\sigma$.

# Threshold theorem

[\[thm:threshold\]]{#thm:threshold label="thm:threshold"} For $X=H^\infty(\rho_\sigma)$ or $H^2(\rho_\sigma)$, the noisy tail obeys $$\|S_\sigma^{\ge h_\sigma}\|_X
 \le C\frac{\exp(a_*L_\sigma\eta_\sigma)}{L_\sigma}$$ for all sufficiently small $\sigma$, with $C$ independent of $\sigma$. The deterministic target tail is smaller: $$\|T^{\ge h_\sigma}\|_X
 \le C'
 \frac{\sigma^{1-a_*\log(q_*/q)}
 \exp(a_*L_\sigma\eta_\sigma)}{L_\sigma}.$$ If $$\eta_\sigma=c\frac{\log L_\sigma}{L_\sigma},$$ then the noisy scale is $L_\sigma^{a_*c-1}$. Thus it vanishes for $c<c_*=1/a_*$, is of constant order for $c=c_*$, and grows for $c>c_*$. Here $$c_*=\log(10/7)=0.3566749439387324\ldots.$$ These three orders are sharp in the mass-and-cap information class.

Put $x_\sigma=q\rho_\sigma=qR e^{\eta_\sigma}$. The geometric bounds are $$\|S_\sigma^{\ge h}\|_{H^\infty}
 \le\frac{4\sigma^{-1}x_\sigma^h}{h(1-x_\sigma)},\qquad
 \|S_\sigma^{\ge h}\|_{H^2}
 \le\frac{4\sigma^{-1}x_\sigma^h}
 {h\sqrt{1-x_\sigma^2}}.$$ Since $(qR)^{a_*L_\sigma}=\sigma$, the first estimate follows; the ceiling changes only a bounded factor. The target proof is identical with $48(q_*\rho_\sigma)^h$ and $$(q_*R)^{a_*L_\sigma}
 =\sigma^{1-a_*\log(q_*/q)}.$$ The remaining exponent is $0.0531384836\ldots>0$.

For sharpness, take $N_\sigma=\lfloor\sigma^{-1}/q^2\rfloor$ copies of the atom $q$ on a diagonal operator. Its squared mass is at most $\sigma^{-1}$ and its trace powers are $N_\sigma q^n$, asymptotic to the upper envelope. The first tail coefficient gives the same lower order in both norms, while the geometric estimates give the matching upper order.

# Protocol and boundary

The computation evaluates $c=c_*/2,c_*,3c_*/2$ at $\sigma=10^{-80}$, records $\eta_\sigma$, $\rho_\sigma$, and the normalized tail scale, and verifies that every reported radius remains below $\rho_*$. At the critical row the normalized model scale equals one by definition; this means $\Theta(1)$, not convergence of the actual tail to one.

The repeated-$q$ diagonal is a saturation model for the available mass-and-cap information, not the measured noisy spectrum. The theorem does not control the moving head and does not prove actual annular nonconvergence. Gates A--E remain false/open.
