---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-320-escaping-packet-endpoint-energy-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction/main.pdf"
source_sha256: "6cbbb5308f04f24ec5987af9a9b407a93c701ab66978c16033a094cee115021f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Escaping Spectral Packets and the Missing Endpoint-Energy Tightness

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-320-escaping-packet-endpoint-energy-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct genuine finite spectra whose moments converge exactly at every fixed order and whose logarithms converge on every strict annulus, while the endpoint $H^2$ norm stays bounded below. The construction adds a single escaping root-of-unity packet to the exact prefix spectra. Its mass fits the archived inverse-noise cap after reparametrization. This proves that the coarse modulus, mass, fixed-order, and interior-annulus axioms do not decide endpoint convergence. It does not prove that the actual noisy family follows the counterexample.
author:
- Bin Wang
date: July 2026
title: 'Escaping Spectral Packets and the Missing Endpoint-Energy Tightness'
```

## Markdown 正文

# Escaping packet construction

Let $\mathcal S_{K-1}$ be an RH-316 spectrum matching the deterministic moments through order $K-1$, chosen with the controlled multiplicities of RH-317. Its endpoint mismatch coefficient at order $K$ is real. Choose a sign aligned with that coefficient and add the RH-315 $K$-packet with selected moment $$w_K=\pm Kq_*^K.$$ Put $R=7/5$, $s=q_*/q$, and take $L_K=\lceil s^K\rceil$. This places the packet in $|\mu|\le q$. It changes no moment below $K$, while its endpoint logarithmic coefficient at order $K$ is exactly $\pm1$.

There is a sequence of finite conjugate spectra and noise labels $\sigma_K$ such that:

1.  the squared mass is at most $\sigma_K^{-1}$;

2.  every fixed power sum eventually equals the deterministic anchor;

3.  the logarithmic mismatch tends to zero in $H^\infty(\rho)$ and $H^2(\rho)$ for every $\rho<\rho_*$;

4.  the endpoint $H^2(\rho_*)$ norm is at least one.

Moreover $\log(1/\sigma_K)=K\log(q_*/q)+O(\log K)$.

The prefix property and packet invisibility give the fixed moments. The packet radius and squared mass are $$r_K=q_*L_K^{-1/K}\le q,\qquad
 B_K=KL_Kr_K^2=Kq_*^2L_K^{1-2/K}=\Theta(Ks^K).$$ Combine it with the $O(s^K)$ prefix mass and define $\sigma_K$ as the reciprocal of one plus the total mass. This proves both the mass cap and the stated logarithmic clock. On a strict radius, the first packet coefficient is $(q_*\rho)^K$ and the coefficient at order $mK$ is $$\frac{(q_*\rho)^{mK}}{mL_K^{m-1}}.$$ Their $H^\infty$ coefficient sum and $H^2$ energy both vanish. The prefix mismatch vanishes by RH-319 when $R<\rho<\rho_*$. For a smaller radius, apply that result first at any intermediate $\rho'$ with $\max\{R,\rho\}<\rho'<\rho_*$ and then restrict the norm. At the endpoint, choose the packet sign to align with the pre-existing order-$K$ mismatch; that single coefficient then has modulus at least one.

# Exact tightness criterion

Let $$e_{\sigma,n}=(\tau_{\sigma,n}-a_n)\rho_*^n/n.$$

The endpoint mismatch tends to zero in $H^2$ if and only if $$e_{\sigma,n}\to0\quad\text{for every fixed }n$$ and $$\lim_{N\to\infty}\limsup_{\sigma\downarrow0}
 \sum_{n>N}|e_{\sigma,n}|^2=0.$$

This is the standard finite-head plus uniformly tight-tail characterization of norm convergence in $\ell^2$ under the Taylor-coefficient isometry.

The repository has neither actual fixed-order complement transport nor the tail-tightness estimate. The synthetic counterexample proves logical insufficiency only, not actual noisy nonconvergence. Gates A--E remain false/open.
