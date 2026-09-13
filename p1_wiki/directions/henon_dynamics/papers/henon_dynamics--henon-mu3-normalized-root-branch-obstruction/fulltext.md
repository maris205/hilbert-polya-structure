---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-normalized-root-branch-obstruction"
canonical_tex: "henon_dynamics/henon_mu3_normalized_root_branch_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_normalized_root_branch_obstruction/paper/main.pdf"
source_sha256: "911205c562c8cdf7703cf840264448c27bcd735ef7654fb62fa54b99ae3fc6c1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Fractional-Divisor Obstruction for a Normalized Hénon Determinant

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_normalized_root_branch_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_normalized_root_branch_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_normalized_root_branch_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_normalized_root_branch_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_normalized_root_branch_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The field-degree-normalized Galois norm of a finite-field Hénon determinant defines a canonical Euler germ on $\operatorname{Re}s>1/2$. We test whether its local roots are ordinary rational determinant ratios. At the first split prime $p=7$, exact cyclotomic sector arithmetic and real-subfield resultants give $N_7=P_{18}^2/(49P_{12}^2)$, where $P_{18}$ and $P_{12}$ are coprime and squarefree. Since the normalizing field degree is three, the local root has orders $\pm2/3$. It is neither rational nor single-valued meromorphic across its unit-circle divisor and cannot be an ordinary finite-dimensional graded determinant. The half-plane germ reaching the Riemann critical abscissa from the right survives. The result forces a precise operator-category pivot: any determinant realization must use a normalized trace admitting fractional projection dimensions.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
date: 13 August 2026
title: 'A Fractional-Divisor Obstruction for a Normalized Hénon Determinant'
```

## Markdown 正文

# Introduction

An analytic logarithm may define a perfectly canonical germ even when its exponential has fractional divisor orders after continuation. This distinction becomes unavoidable in the Hénon Galois descent constructed in the preceding stage. For each split prime, the complete rational norm $N_p(z)$ is divided logarithmically by $d_p=[\mathbf Q(\zeta_p)^+:\mathbf Q]$. The resulting Euler product reaches $\operatorname{Re}s>1/2$, but it is an ordinary determinant only if every valuation in $\operatorname{div}N_p$ is divisible by $d_p$.

We settle that gate negatively at $p=7$.

[\[thm:main\]]{#thm:main label="thm:main"} Let $N_7$ be the rational Galois norm of the conjugate-paired $\mu_3$ Hénon augmentation factor. Then $$N_7(z)=\frac{P_{18}(z)^2}{49P_{12}(z)^2},$$ where $P_{18}$ and $P_{12}$ are squarefree and coprime in $\mathbf Q[z]$. Hence $N_7$ is not a cube, and the origin branch $$G_7(z)=\exp\!\left(\frac13\operatorname{Log}_0N_7(z)\right)$$ has local orders $\pm2/3$. It does not extend through any local divisor point as a single-valued meromorphic scalar function.

The theorem does not refute the half-plane germ. It identifies the precise reason an ordinary determinant is the wrong category. Normalized traces in finite or semifinite algebras can assign fractional dimensions to projections; C47 tests whether that mechanism realizes the full Hénon germ.

# Exact sector descent

Let $\zeta=\zeta_7$, choose $\rho=2$, and let $T=U_7^2$. For the three eigenspaces $H_k$ of the coordinate permutation, set $$D_k(z)=\det(I-zT\mid H_k).$$ Exact arithmetic in $\mathbf Q(\zeta)$ gives $D_2=D_1$. Let $\theta=\zeta+\zeta^{-1}$, with $$m(\theta)=\theta^3+\theta^2-2\theta-1.$$ The conjugate-paired sector factors $$q_k(\theta,z)=D_k(z)\overline{D_k(z)}$$ belong to $\mathbf Q(\theta)[z]$. Their explicit reductions are recorded in [6](#sec:polynomials){reference-type="ref" reference="sec:polynomials"}. Since the augmentation factor is $(D_0/D_1)^2$, the paired factor equals $(q_0/q_1)^2$.

All operations retain the two-step kernel chronology. Conjugation pairs the additive character; it does not average a transition matrix or alter the prime clock.

# Resultants and divisor multiplicities

Because $m$ is monic, taking the norm from $\mathbf Q(\theta)$ is equivalent to a resultant in $\theta$. Exact elimination gives $$\operatorname{Res}_{\theta}(m,q_0)=P_{18}/49,
 \qquad
 \operatorname{Res}_{\theta}(m,q_1)=P_{12}/7.$$ Consequently $$\label{eq:norm}
 N_7(z)=\frac{P_{18}(z)^2}{49P_{12}(z)^2},
 \qquad N_7(0)=1.$$

The numerator and denominator of [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"} have degrees $36$ and $24$. Their difference $12$ agrees with the general ordinary-norm formula $2(p-1)$.

[\[prop:gcd\]]{#prop:gcd label="prop:gcd"} The polynomials $P_{18}$ and $P_{12}$ are squarefree and mutually coprime over $\mathbf Q$.

Reduction modulo five preserves both degrees. Direct Euclidean algorithms in $\mathbf F_5[z]$ give $$\gcd(P_{18},P_{12})=gcd(P_{18},P_{18}')
 =\gcd(P_{12},P_{12}')=1.$$ A common factor or repeated factor over $\mathbf Q$ would give one after reduction at a degree-preserving good prime. Thus the three rational gcds are one.

Every finite zero of $N_7$ now has valuation two and every finite pole valuation minus two. The finite points lie on $|z|=1$: before Galois descent the factors are characteristic polynomials of unitary sector blocks, and [\[prop:gcd\]](#prop:gcd){reference-type="ref" reference="prop:gcd"} excludes cross-sector cancellation. At infinity the valuation is $-12$, which is divisible by three and does not affect the finite-divisor obstruction.

# Proof of the branch theorem

Here $d_7=3$. A cube in $\mathbf C(z)$ has divisor valuations divisible by three. The exact finite valuations $\pm2$ supplied by [\[prop:gcd\]](#prop:gcd){reference-type="ref" reference="prop:gcd"} prove that $N_7$ is not a cube. Near a zero $\alpha$, $$G_7(z)=(z-\alpha)^{2/3}h(z),
 \qquad h(\alpha)\ne0,$$ and a pole gives order $-2/3$. A single-valued meromorphic function has integral local order. This proves [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

The obstruction is stronger than the statement that a convenient rational formula was not found. It is invariant under rational re-expression of the norm and is already present at the first split prime. Any ordinary finite-dimensional determinant ratio has integral local orders and therefore cannot equal $G_7$.

It would be incorrect, however, to infer a global natural boundary. The origin branch remains holomorphic on $|z|<1$, and the C45 prime product remains holomorphic on $\operatorname{Re}s>1/2$. Cross-prime monodromy, global cancellation, and alternative operator categories have not been classified.

# Route-A decision

The C45 analytic germ and the source-native two-step quantization survive. The ordinary C45 norm supplies the rational determinant underlying A2, while its normalized-log root supplies the improved Euler germ. The root's own ordinary determinant promotion fails exactly, and there is no functional equation, Gamma factor, or continued scalar divisor. The frozen evaluation is $$\begin{aligned}
 \mathrm{A1}&=\mathrm{WEAK},
 &\mathrm{A2}&=\mathrm{ANALYTIC\_DETERMINANT},\\
 \mathrm{A3}&=\mathrm{FAIL},
 &\mathrm{A4}&=\mathrm{NATURAL\_QUANTIZATION}.\end{aligned}$$ Overall: `STOP_ORDINARY_DETERMINANT_PROMOTION`. Route B is not authorized.

The conclusion is useful rather than merely negative. Fractional orders are exactly what a normalized trace on a finite algebra can encode. C47 therefore keeps the Hénon dynamics fixed and changes only the determinant category, testing whether a legitimate graded normalized-trace determinant reproduces the C45 germ.

# Frozen polynomials {#sec:polynomials}

The real paired sector reductions are $$\begin{aligned}
7q_0={}&-15\theta^2z^5-26\theta^2z^4-26\theta^2z^3-26\theta^2z^2-15\theta^2z\\
&-3\theta z^5-10\theta z^4-19\theta z^3-10\theta z^2-3\theta z\\
&+7z^6+31z^5+61z^4+72z^3+61z^2+31z+7,\\
7q_1={}&4\theta^2z^2+5\theta z^2+7z^4-12z^2+7.\end{aligned}$$

The norm polynomials are $$\begin{aligned}
P_{18}(z)={}&49z^{18}+147z^{17}+147z^{16}-14z^{15}-133z^{14}-63z^{13}
+71z^{12}\\
&+104z^{11}+50z^{10}+13z^9+50z^8+104z^7+71z^6\\
&-63z^5-133z^4-14z^3+147z^2+147z+49,\\
P_{12}(z)={}&7z^{12}-21z^{10}+35z^8-41z^6+35z^4-21z^2+7.\end{aligned}$$
