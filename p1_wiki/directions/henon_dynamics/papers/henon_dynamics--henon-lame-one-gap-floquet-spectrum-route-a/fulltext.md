---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lame-one-gap-floquet-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_lame_one_gap_floquet_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lame_one_gap_floquet_spectrum_route_a/paper/main.pdf"
source_sha256: "edc9f7fb3ab68b1d500b7683001764bec7fb8f5b01134f122eca9f2211485ef9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Complete One-Gap Spectrum of the Degree-One Lamé Hamiltonian

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lame_one_gap_floquet_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lame_one_gap_floquet_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lame_one_gap_floquet_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lame_one_gap_floquet_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove the complete real-line spectrum of the degree-one Lamé operator in a fixed Jacobi convention. Three explicit band-edge modes, a skew third-order commuting operator, and its cubic algebraic relation yield two bands, one finite open gap, and pure absolute continuity. \>0 The free-modulus and soliton limits, threshold resonance, translations, and all real-convention boundaries are closed explicitly. \>1 Finite exact receipts are separated from the infinite Floquet proof, and the source, collision, and Route-A boundaries are audited.
author:
- 'Route-A source-local certificate HCS-C340'
date: 3 September 2026
title: 'The Complete One-Gap Spectrum of the Degree-One Lamé Hamiltonian'
```

## Markdown 正文

trailerid \[\<C3402026090300000000000000000000\>\<C3402026090300000000000000000000\>\]

# Operator convention and band-edge modes

Fix $m=k^2\in(0,1)$ and write $K=K(m)$. On $L^2(\mathbb R)$ let $$\label{eq:H}
 H_m=-D^2+u(x),\qquad D=\frac{d}{dx},\qquad
 u(x)=2m\operatorname{sn}^2(x\mid m),$$ with domain $H^2(\mathbb R)$. The real potential is smooth, bounded, and has period $2K$. Hence the stated realization is self-adjoint and bounded below. All Floquet multipliers below are measured over $2K$.

The Jacobi differential identities are $$\begin{aligned}
 \operatorname{sn}''&=-(1+m)\operatorname{sn}+2m\operatorname{sn}^3,\label{eq:sn}\\
 \operatorname{cn}''&=(2m\operatorname{sn}^2-1)\operatorname{cn},\qquad
 \operatorname{dn}''=(2m\operatorname{sn}^2-m)\operatorname{dn}.\label{eq:cndn}\end{aligned}$$ Consequently $$\label{eq:edges}
 H_m\operatorname{dn}=m\operatorname{dn},\qquad H_m\operatorname{cn}=\operatorname{cn},\qquad
 H_m\operatorname{sn}=(1+m)\operatorname{sn}.$$ Over one potential period, $\operatorname{dn}$ is periodic while $\operatorname{cn}$ and $\operatorname{sn}$ are antiperiodic. These formulas identify three edges, but by themselves do not prove that all higher gaps close.

# Commuting operator and spectral curve

Set $$\label{eq:A}
 A=-4D^3+\{6u-4(1+m)\}D+3u'.$$ For $\theta\in[-\pi,\pi)$ define $$H^j_\theta=\{f\in H^j([0,2K]):
 f^{(\ell)}(2K)=e^{i\theta}f^{(\ell)}(0),\ 0\leq\ell<j\}.$$ The closed fiber realization of [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"} has $$\label{eq:A-domain}
 D(A_\theta)=H^3_\theta([0,2K]).$$ The coefficient of $D$ has derivative $6u'$. Since all coefficients are $2K$-periodic, every endpoint product in the Green boundary form cancels: the common phase $e^{i\theta}$ cancels its conjugate. Three integrations by parts therefore show $A_\theta^*=-A_\theta$; equivalently, the adjoint boundary form imposes the same three quasi-periodic conditions. Direct use of [\[eq:sn\]](#eq:sn){reference-type="eqref" reference="eq:sn"} gives the two identities $$\begin{aligned}
 u''&=3u^2-4(1+m)u+4m,\label{eq:stationary}\\
 (u')^2&=2u^3-4(1+m)u^2+8mu.\label{eq:first}\end{aligned}$$ Differentiating [\[eq:stationary\]](#eq:stationary){reference-type="eqref" reference="eq:stationary"} and expanding differential-operator products, with [\[eq:first\]](#eq:first){reference-type="eqref" reference="eq:first"} for the zeroth-order remainder, proves $$\label{eq:curve}
 [A,H_m]=0,\qquad
 A^2=-16(H_m-m)(H_m-1)(H_m-1-m).$$ The first integral is essential here; the stationary second-order equation alone leaves an arbitrary integration constant and does not prove the second identity in [\[eq:curve\]](#eq:curve){reference-type="eqref" reference="eq:curve"}.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For every $0<m<1$, $$\label{eq:spectrum}
 \sigma(H_m)=[m,1]\cup[1+m,\infty),$$ and the spectrum is purely absolutely continuous. Thus $(1,1+m)$ is the only finite open gap and every higher folded-zone gap is closed.

Let $$R(E)=(E-m)(E-1)(E-1-m).$$ Floquet decomposition realizes $H_m$ as the direct integral of self-adjoint quasi-periodic operators with domain $H^2_\theta$ on $[0,2K]$. The operator $A_\theta$ has domain [\[eq:A-domain\]](#eq:A-domain){reference-type="eqref" reference="eq:A-domain"} and is skew-adjoint there. A fiber eigenfunction is smooth by its second-order ODE, lies in $H^3_\theta$, and is therefore in $D(A_\theta)$. If $H_m\psi=E\psi$ in a fiber, then [\[eq:curve\]](#eq:curve){reference-type="eqref" reference="eq:curve"} gives $$-\|A\psi\|^2=-16R(E)\|\psi\|^2.$$ Therefore a spectral energy must satisfy $R(E)\ge0$.

Conversely, suppose $R(E)>0$. On the two-dimensional solution space of $H_m\psi=E\psi$, equation [\[eq:curve\]](#eq:curve){reference-type="eqref" reference="eq:curve"} gives distinct eigenvalues $\pm4i\sqrt{R(E)}$ for $A$. Because $A$ commutes with period monodromy, its one-dimensional eigenspaces are Bloch lines. Real coefficients make the two Bloch solutions complex conjugates. If one has multiplier $\lambda$, the other has multiplier $\bar\lambda$. Their Wronskian is nonzero and constant; translating it by $2K$ multiplies it by $\lambda\bar\lambda$. Hence $|\lambda|=1$, placing $E$ in the spectrum. The three roots of $R$ follow by closure and agree with [\[eq:edges\]](#eq:edges){reference-type="eqref" reference="eq:edges"}. The condition $R(E)\ge0$ is exactly [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"}.

For a real one-dimensional periodic Schrödinger operator, Floquet fibers have analytic nonconstant band functions; the direct integral therefore has neither eigenvalues nor singular-continuous spectrum. Its spectrum is purely absolutely continuous [@Kuchment]. Since the second allowed interval extends from $1+m$ to infinity without another excluded chamber, all higher folded-zone contacts are closed. This is an analytic completeness proof, not a finite coefficient inference.

The argument through [\[eq:curve\]](#eq:curve){reference-type="eqref" reference="eq:curve"} is the *commuting spectral-curve owner* of revision round zero.

\>0

# Endpoint and equivalence atlas

At $m=0$, equation [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} becomes the free operator $-D^2$ with spectrum $[0,\infty)$; the finite gap has closed. This face also explains why the infinitely many folded free contacts are not open gaps.

As $m\uparrow1$, one has $K(m)\to\infty$ and, locally on the line, $$u(x)\longrightarrow2\tanh^2x=2-2\operatorname{sech}^2x.$$ The lower band $[m,1]$ collapses to the $L^2$ level $1$, and the upper band tends to $[2,\infty)$. For the unshifted potential $-2\operatorname{sech}^2x$, the zero solution is a threshold resonance, not an additional $L^2$ eigenstate; after adding $2$ it sits at threshold $2$.

Changing $k$ to $-k$ leaves $m=k^2$ and the operator unchanged. A spatial translation is unitary conjugacy and changes no band. Complex $m$, or real $m\notin[0,1]$, lies outside the frozen real self-adjoint Jacobi convention. These statements are the *modulus boundary owner* added in revision round one.

\>1

# Finite receipts and Route-A boundary

The executable ledger contains all 199 reduced rational moduli $p/q$ with $0<p<q\le25$. It stores exact edges, gap widths, cubic coefficients, sign chambers, and fiber labels. The checker reconstructs each fraction and each root. An independent SymPy lane composes [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"} with [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} and reduces every coefficient using both [\[eq:stationary\]](#eq:stationary){reference-type="eqref" reference="eq:stationary"} and [\[eq:first\]](#eq:first){reference-type="eqref" reference="eq:first"}. These receipts catch sign and convention errors; only the Floquet/Wronskian proof establishes every real energy and every higher gap.

The nearest workspace owners are different: C262 treats a piecewise-constant square-wave Hill transfer matrix; C327 treats a singular Kronig--Penney delta comb; C221 and C231 use nonperiodic soliton/front Hessians. None owns the smooth elliptic one-gap theorem.

The conservative Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ The source-native self-adjoint Hamiltonian and its unitary time evolution support A4. They do not create rational-prime data, an arithmetic orbit dictionary, a target Euler product, root number, automorphy, target divisor or functional equation, target zero match, or a Hilbert--Polya operator. Route B remains false. This is the *finite evidence and route firewall* of the final revision.

# Source boundary {#source-boundary .unnumbered}

This paper is a source-local reconstruction, not a priority claim. Ince's papers own the periodic Lamé analysis; NIST DLMF supplies an authoritative identity index; Kuchment supplies the general Floquet direct-integral and periodic absolutely-continuous spectral theorem. The checked JSON grid and release gates are new implementation receipts and are not attributed to those sources.

9 E. L. Ince, "The Periodic Lamé Functions," DOI [10.1017/S0370164600020058](https://doi.org/10.1017/S0370164600020058). E. L. Ince, "Further Investigations into the Periodic Lamé Functions," DOI [10.1017/S0370164600020071](https://doi.org/10.1017/S0370164600020071). NIST Digital Library of Mathematical Functions, Chapter 29, <https://dlmf.nist.gov/29>. P. Kuchment, "An overview of periodic elliptic operators," *Bulletin of the American Mathematical Society* 53 (2016), 343--414, DOI [10.1090/bull/1528](https://doi.org/10.1090/bull/1528).
