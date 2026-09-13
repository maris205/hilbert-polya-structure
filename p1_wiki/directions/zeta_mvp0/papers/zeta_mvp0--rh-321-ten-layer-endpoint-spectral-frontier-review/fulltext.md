---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-321-ten-layer-endpoint-spectral-frontier-review"
canonical_tex: "zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review/main.pdf"
source_sha256: "4fb82c86c9563fdd9908e77d59c0b474e7743a4654d6ecf3cd6cfaa12ad2722d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ten Layers of the Endpoint Spectral-Realizability Frontier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-321-ten-layer-endpoint-spectral-frontier-review/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-312--RH-321 resolve the synthetic endpoint spectral class without promoting it to the actual noisy operator. The deterministic endpoint is a universal logarithm plus an analytic remainder, its best degree-$N$ Hardy error is $N^{-1/2}$, and complete root-of-unity packets realize every finite prefix as a genuine integer-multiplicity normal spectrum. The least rank and squared mass grow like $(q_*/q)^N$, yielding the sharp endpoint law $E_{\rm spec}(M)^2\sim\log(q_*/q)/\log M$ and the optimal strict-annulus rates. An escaping packet then proves that fixed moments and every strict annulus can converge while endpoint $H^2$ fails. Thus actual coefficient transport and endpoint energy tightness remain the precise missing inputs. This batch is therefore a scoped spectral-realizability route stop, not a reopening input. The typed ledgers stay four of five and Gates A--E remain open.
author:
- Bin Wang
date: July 2026
title: 'Ten Layers of the Endpoint Spectral-Realizability Frontier'
```

## Markdown 正文

# Endpoint analytic structure

RH-312 proves $$-\sum_{n\ge2}\frac{a_n\rho_*^n}{n}w^n
 =\log(1-w)+w+H_{\rm reg}(w),$$ where $H_{\rm reg}$ is analytic past the unit circle. RH-313 splits the logarithm into orthogonal even and odd channels, and RH-314 gives the exact best degree-$N$ error $$E_N^2=\sum_{n>N}n^{-2}\sim N^{-1}.$$ These are deterministic Hardy theorems, not noisy convergence.

# Genuine finite spectral realizability

RH-315 introduces the packet formed from all roots of $z^d=w/(dL)$. It has zero moments below $d$, moment $w$ at order $d$, and integer multiplicities. RH-316 recursively realizes every deterministic prefix by a finite conjugate spectrum in $|\mu|\le q$. RH-317 proves that the optimal rank and squared mass both obey $$\Theta(s^N),\qquad s=q_*/q=1.4017504517\ldots.$$

RH-318 converts that complexity clock into the exact endpoint extremal law $$E_{\rm spec}(M)^2\sim\frac{d}{\log M},
 \qquad d=\log s=0.3377217783\ldots.$$ In particular the actual mass cap implies the class-sharp universal lower-rate bound $$\liminf_{\sigma\downarrow0}\log(1/\sigma)
 \|g_\sigma\|_{H^2(\rho_*)}^2\ge d,$$ whose corresponding norm lower scale still tends to zero.

# Strict annuli versus endpoint energy

RH-319 uses the same finite spectra to attain, for every $1.4<\rho<\rho_*$, $$\Theta_\rho\left(M^{-\kappa(\rho)}/\log M\right),
 \qquad
 \kappa(\rho)=
 \frac{\log(1/(q_*\rho))}{\log(q_*/q)}.$$ This upgrades RH-306 from abstract coefficient saturation to genuine normal spectral power sums.

RH-320 adds one escaping packet to an exact prefix. Every fixed moment and every strict-annulus logarithm converge, the inverse-noise mass cap is respected after reparametrization, but one endpoint coefficient stays of order one. Therefore endpoint convergence requires exactly: $$e_{\sigma,n}\to0\text{ for each fixed }n,
 \qquad
 \lim_{N\to\infty}\limsup_{\sigma\downarrow0}
 \sum_{n>N}|e_{\sigma,n}|^2=0.$$ Neither input is proved for the actual complement.

# Typed frontier

  branch                          head   bridge   tail   target   boundary   score
  ------------------------------ ------ -------- ------ -------- ---------- -------
  noisy modulus spectrum           1       0       1       1         1         4
  graded monodromy counterloop     1       1       0       1         1         4

The weighted cross-branch glue remains false and the complete count is zero. Synthetic normal matrices do not fill the missing actual bridge coordinate.

The direct route reopens only with actual fixed-order complement transport and endpoint energy tightness, equivalently actual endpoint $H^2$ convergence. The typed route reopens with the joint first-alias boundary-layer trace law identified after RH-311. No finite-prefix or synthetic realization substitutes for either input.

The direct statement is the RH-320 $\ell^2$ tightness criterion. The typed statement is the RH-310 first-alias obligation, unchanged by the present synthetic constructions.

No Gate-A determinant identification is completed. Gates B--E remain false/open. The batch constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or zeta-divisor equality, and does not imply RH.
