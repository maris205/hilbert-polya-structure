---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-bitflip-noise-fourier-spectrum"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/paper/main.pdf"
source_sha256: "68afa38c9efd390ef5c1c199db1f516e3d31dc8d6e51042d5819879b1efec8c1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Bit-Flip Noise and Walsh Spectrum of a Frozen Hénon Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compute the exact Boolean spectrum of the full-core generation indicator on a frozen sixteen-label support. The indicator is one precisely when the pivot $S_9$ is present and at least two of four direction blocks are hit. Its truth table has 30400 ones. An integer Walsh--Hadamard transform has 1024 nonzero coefficients and maximum degree 10; a second transform gives the complete ordered-pair Hamming autocorrelation and hence the exact bit-flip noise polynomial. Independent mask-level checks, a ten-variable symbolic calculation, clean replay, and thirteen hostile mutations certify the receipt. This is a finite Boolean result, with scope firewall `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Exact Bit-Flip Noise and Walsh Spectrum of a Frozen Hénon Core'
```

## Markdown 正文

# Predicate and transform

For $A\subseteq L$, define $$F(A)=\mathbf1\{S_9\in A\}\,\mathbf1\{\text{$A$ meets at least two of }
 B_1,B_2,B_3,B_4\},$$ where $$B_1=\{S_1\},\ B_2=\{S_{16}\},\ B_3=\{S_7,S_{15}\},\quad
B_4=\{S_3,S_4,S_8,S_{11},S_{12}\}.$$ The six other labels do not affect $F$. We enumerate all 65536 masks and use the convention $$W(S)=\sum_{A\subseteq L}F(A)(-1)^{|A\cap S|}.$$

The Walsh table has 1024 nonzero entries, degree at most 10, and satisfies $$\sum_S W(S)^2=2^{16}\,30400.$$

The six dummy variables force every coefficient containing a dummy bit to vanish. The remaining ten-variable multilinear polynomial is a pivot times an inclusion--exclusion expression for at least two block hits. Expanding it over signs gives the 1024 active coefficients; the producer and independent symbolic script agree coefficient by coefficient. Parseval gives the stated energy identity.

# Bit-flip autocorrelation

For Hamming distance $h$, let $$C_h=\sum_{d_H(A,B)=h}F(A)F(B).$$ The exact vector for $h=0,\ldots,16$ is $$\begin{aligned}
(C_0,\ldots,C_{16})={}&(30400,445696,3068864,13137152,39054016,85341312,\\
&141543616,181366144,180954240,140539776,84251904,38278400,\\
&12756480,2943488,420480,28032,0).
\end{aligned}$$ It sums to $30400^2$. With independent bit flips of rate $\varepsilon$, the normalized agreement probability is equivalently $$2^{-16}\sum_h C_h\varepsilon^h(1-\varepsilon)^{16-h}
 =2^{-32}\sum_S W(S)^2(1-2\varepsilon)^{|S|}.$$

# Audit and limits

The receipt binds C73/C76/C78 evidence and manifests by SHA-256. Its canonical evidence hash is the concatenation of $$\begin{gathered}
\texttt{6fc49cad02956f463b1e37d017506f43}\\[-2pt]
\texttt{7edce6717414da74770ad94913ccefa1}.
\end{gathered}$$ The independent checker re-evaluates the generation predicate and the C78 distance-zero boundary for every mask. The symbolic check uses the explicit active coordinate order $(S_1,S_3,S_4,S_7,S_8,S_9,S_{11},S_{12},S_{15},S_{16})$ and integrates out the six dummies as a factor 64. No arithmetic/local, Euler-factor, root-number, automorphy, Burnside-ring/table-of-marks, or Hilbert--Polya statement is made.
