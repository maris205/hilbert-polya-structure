---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-23-physical-packet-complement-feshbach"
canonical_tex: "zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/physical-packet-complement-feshbach-closure.pdf"
source_sha256: "fe877ee6ab2285d1407cbdbf013c4f065acc10dfc5b2bc7d16c81b8994a84f6f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Physical Packet--Complement Feshbach Closure at a Quadratic Band-Merging Map: Complex Spectral Targets, Resolvent Compensation, and a Nonuniform Conditioning Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/physical-packet-complement-feshbach-closure.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the first algebraic band-merging parameter of $f_u(x)=1-u x^2$, a scalar antisymmetric critical-branch channel does not provide the self-energy required by the physical small-noise spectral edge. We therefore replace that local channel by the full complement of a canonical packet projection in the Perron/parity-extracted physical two-step operator. The first correction is conceptual: if $K_{\mathrm b,\sigma}r_\sigma=\mu_\sigma r_\sigma$, then the exact two-step target is the complex number $\nu_\sigma=\mu_\sigma^2$. The positive quantity $|\mu_\sigma|^{2k}$ is only the modulus of a $k$-cycle target and is not, in general, an eigenvalue.

  Let $V,W$ be a biorthogonal packet pair, $WV=\mathrm I$, and put $P=VW$, $Q=\mathrm I-P$, and $A=K_{\mathrm b,\sigma}^2$. For every exact eigenpair $Ar=\nu r$, with $\alpha=Wr$ and $q=Qr$, we prove the exact block closure $$(\nu\mathrm I-WAV)\alpha=WAq,
   \qquad
   (\nu Q-QAQ)q=QAV\alpha.$$ When the external block is invertible, elimination gives the Feshbach matrix, its determinant factorization, and $$\|(\nu Q-QAQ)^{-1}\|
   \ge \frac{\|q\|}{\|QAV\alpha\|}.$$ For a simple eigenvalue with $\ell^*r=1$, the compressed resolvent has residue $(Wr)(\ell^*V)$; its trace $\omega=\ell^*Pr$ is invariant under packet-coordinate and eigenvector gauges. Thus a small right packet projection need not make the physical pole invisible in a nonnormal problem.

  A seven-scale sparse audit, with $n\sigma=20.48$ and dimensions up to $204800$, finds exact block-equation residuals below $1.32\times10^{-13}$. Independent complex GMRES solves converge in $20$--$56$ iterations and reconstruct $q$ to relative error at most $2.08\times10^{-8}$. As $\sigma$ decreases from $10^{-2}$ to $10^{-4}$, $\|Pr\|$ falls from $0.351$ to $0.0646$, while the complement-resolvent lower bound rises from $5.25$ to $37.5$ and the eigenvalue condition number from $9.21$ to $151$. Nevertheless $|\ell^*Pr|$ remains between $1.18$ and $1.62$, and $\|Pr\|$ times the resolvent lower bound remains between $1.84$ and $2.42$. The full complement self-energy is still $21\%$ of the physical target scale at the smallest noise. These are floating-point diagnostics, not asymptotic theorems. They rule out neglecting the complement on the computed range but leave a viable renormalized, nonuniform Feshbach route: contour-wise block solves followed by determinant and root-count control.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **Physical Packet--Complement Feshbach Closure** **at a Quadratic Band-Merging Map:**\
  Complex Spectral Targets, Resolvent Compensation,\
  and a Nonuniform Conditioning Barrier
```

## Markdown 正文

**Keywords:** Gaussian transfer operator; Feshbach map; Schur complement; compressed resolvent; oblique projection; nonnormal spectrum; quadratic map; spectral approximation.

**MSC 2020:** 37E05; 37D25; 47A10; 47A55; 47B65; 65F10; 65F15; 65P30.

# Introduction {#sec:introduction}

The small-noise spectrum of a Gaussian perturbation of a quadratic band-merging map has been organized through a sequence of deterministic, finite-rank, and sparse-operator reductions. A deterministic two-step bulk determinant has an exact endpoint pole, while Gaussian noise resolves a nonnormal resonance cloud [@WangBulkScattering2026]. Endpoint singular values supply a half-logarithmic resolution clock, and a boundary word gives an exact time-ordered cycle [@WangEndpointRank2026; @WangTimeOrdered2026]. Riccati packet propagation and a conditioned critical profile then insert the exact noisy operator into the cycle [@WangGaussianReturn2026].

Later layers tested how that packet cycle should be closed. A one-branch closure misses an order-one critical sibling, while an unconstrained time lift merely produces Floquet copies of physical eigenvalues [@WangComplement2026]. Resolving both critical branches gives an exact two-channel factorization and an almost rank-one bright return [@WangSectorBranch2026]. Peripheral biorthogonalization constructs a valid packet projection but cannot attenuate an eigenvalue by a coordinate normalization; moreover, retaining two independent labels around the whole cycle becomes ill-conditioned as their histories merge [@WangBiorthogonal2026]. The scalar Schur self-energy of the remaining local dark coordinate can then be computed exactly, but it has the wrong sign or insufficient magnitude at all seven archived scales [@WangDarkSchur2026].

That local no-go result specifies the next object rather than ending the construction. The missing excursion may pass through the entire packet-complement space. The corresponding Feshbach map is spectral-parameter dependent and retains every bright--external--bright path. The present paper constructs and audits that full complement for a canonical physical packet projection.

There is also a target issue that must be fixed before the larger Schur problem is meaningful. The outer bulk resonance is complex. If a one-step resonance is $\mu_\sigma$, then the exact two-step eigenvalue is $\mu_\sigma^2$, and the exact $k$-fold return eigenvalue is $\mu_\sigma^{2k}$. Replacing the latter by the positive number $|\mu_\sigma|^{2k}$ preserves only its modulus. A radius match can be a useful asymptotic diagnostic, but it is not an exact spectral closure.

The advantage of working at the exact complex target is that the block algebra is completely rigid. Once $P$ is an idempotent packet projection, the physical eigenvector splits uniquely as $r=Pr+Qr$. Its two block equations identify the self-energy without fitting a phase, weight, or pole. The same decomposition yields an exact determinant identity and a compressed-resolvent formula. This separates what is proved by linear algebra from what is only observed in finite-precision small-noise data.

## Main results and logical status {#main-results-and-logical-status .unnumbered}

1.  **Correct complex target.** For a physical bulk resonance $\mu_\sigma$, the exact two-step target is $\nu_\sigma=\mu_\sigma^2$. A positive return radius is exact only when the accumulated phase vanishes modulo $2\pi$.

2.  **Exact packet--complement closure.** For every finite-dimensional operator, every biorthogonal packet pair, and every exact eigenpair, we derive the two coupled block equations. This theorem does not assume normality, orthogonality, or weak coupling.

3.  **Feshbach determinant and resolvent identities.** Whenever the external shifted block is invertible, its Schur complement gives an exact determinant factorization and $W(z\mathrm I-A)^{-1}V=F(z)^{-1}$. The corresponding bounded-operator statement holds on the common resolvent set; determinant claims require the usual Fredholm hypotheses.

4.  **External-resolvent lower bound.** The physical exterior $q$ and its packet forcing give a computable lower bound on the complement resolvent. Hence the known eigenmode can diagnose a conditioning barrier without forming the inverse.

5.  **Gauge-invariant pole visibility.** At a simple physical eigenvalue, the trace residue of the compressed resolvent is $\ell^*Pr$. It is invariant under every invertible packet coordinate change and under reciprocal left/right eigenvector scaling.

6.  **Seven-scale physical closure.** The exact block identities hold to ordinary double-precision residuals of order $10^{-13}$, and independent shifted solves reconstruct the physical exterior. This validates the finite-dimensional implementation of the full-complement mechanism; it does not independently discover the eigenvalue used in the closure.

7.  **Nonuniform compensation diagnostic.** Right packet capture decreases while the external-resolvent lower bound and physical eigenvalue condition number increase. The packet pole residue nevertheless remains order one. Log--log exponents reported below are finite-range regressions, not small-noise laws.

8.  **Route comparison.** Merging the final critical dark coordinate barely changes the audited quantities. Keeping both labels at every slice adds no pole visibility but causes severe Gram growth. A single-label route gives a closer direct root while increasing external dependence and reducing the pole residue.

The resulting implication map is $$\label{eq:intro-map}
 \boxed{
 \begin{gathered}
 \text{physical complex resonance}
 \Longrightarrow
 \text{exact packet--complement Feshbach closure},\\
 \text{small }\|Pr\|
 \not\Longrightarrow
 \text{small compressed-resolvent residue},\\
 \text{static packet compression}
 \not\Longrightarrow
 \text{exact physical target on the audited grids},\\
 \text{full complement}
 \Longrightarrow
 \text{non-negligible, increasingly conditioned correction},\\
 \text{contour-wise Feshbach determinant control}
 \Longrightarrow?\
 \text{predictive physical root count}.
 \end{gathered}}$$ The first four lines are established exactly or data-conditionally below. The final arrow is the next operator problem.

# Physical bulk operator and the complex target {#sec:physical-operator}

Let $u_{\mathrm c}$ be the root in $(1,2)$ of $$\label{eq:critical-parameter}
 u^3-2u^2+2u-2=0,
 \qquad
 u_{\mathrm c}=1.543689012692076\ldots,$$ and define $$\label{eq:quadratic-map}
 f(x)=1-u_{\mathrm c}x^2.$$ For noise $\sigma>0$, the folded row-normalized Gaussian kernel on $[0,1]$ is $$\begin{aligned}
 P_\sigma(x,y)
 &=\frac{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))}{Z_\sigma(x)},
 \label{eq:kernel}\\
 Z_\sigma(x)
 &=\int_0^1\{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))\}\,dy,
 \label{eq:normalizer}\\
 \phi_\sigma(t)&=\frac{1}{\sqrt{2\pi}\sigma}
 e^{-t^2/(2\sigma^2)}.
 \label{eq:normal-density}\end{aligned}$$ Write $\mathcal K_\sigma$ for the corresponding backward Markov operator. At fixed positive noise it is Hilbert--Schmidt, while its square is trace class [@Baladi2000]. The numerical work uses the midpoint discretization of [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}.

Let $r_0,r_-$ be the right Perron and parity modes and let $\ell_0,\ell_-$ be their biorthogonal left modes. With $$\label{eq:peripheral-data}
 R=(r_0,r_-),
 \qquad L=(\ell_0,\ell_-),
 \qquad L^*R=\mathrm I_2,$$ the physical bulk projector and one-step bulk operator are $$\label{eq:bulk-projector}
 \Pi_{\mathrm b}=\mathrm I-RL^*,
 \qquad
 K_{\mathrm b,\sigma}=\Pi_{\mathrm b}\mathcal K_\sigma\Pi_{\mathrm b}.$$ On an exact spectral discretization this is equivalently obtained by subtracting the two peripheral rank-one components. The physical two-step operator studied here is $$\label{eq:A-definition}
 A_\sigma=K_{\mathrm b,\sigma}^2.$$

Suppose the selected outer bulk mode satisfies $$\label{eq:physical-eigenpair}
 K_{\mathrm b,\sigma}r_\sigma=\mu_\sigma r_\sigma,
 \qquad
 \ell_\sigma^*K_{\mathrm b,\sigma}
 =\mu_\sigma\ell_\sigma^*,
 \qquad
 \ell_\sigma^*r_\sigma=1.$$ Then $$\label{eq:two-step-target}
 A_\sigma r_\sigma=\nu_\sigma r_\sigma,
 \qquad
 \boxed{\nu_\sigma=\mu_\sigma^2}.$$ This is the spectral parameter used in every Feshbach solve below.

If $k=k_\sigma$ is the component-cycle period, the exact return multiplier is $$\label{eq:return-target}
 \nu_\sigma^k=\mu_\sigma^{2k}
 =|\mu_\sigma|^{2k}e^{i\varphi_\sigma},
 \qquad
 \varphi_\sigma=\arg(\mu_\sigma^{2k}).$$ Thus $|\mu_\sigma|^{2k}$ is a radius target, not an exact return eigenvalue unless $\varphi_\sigma=0$ modulo $2\pi$. For example, at $\sigma=10^{-4}$, $$\begin{aligned}
 \mu_\sigma
 &=-0.6978952321+0.2933022111i,
 &k&=8,
 &\varphi_\sigma&=-0.0824912054.
 \label{eq:complex-example}\end{aligned}$$ The phase is small but nonzero. Treating the positive radius as an exact root would therefore build an avoidable error into the closure.

# Canonical packet and complementary projection {#sec:packet}

The packet space is built from the branch histories already used in the time-ordered Gaussian return. Let $$\label{eq:histories}
 H_j=(h_j^-,h_j^+),
 \qquad j=0,\ldots,k-1,$$ denote the two propagated label histories, with $j=k-1$ the final critical slice. At every regular slice we retain the normalized bright history $$\label{eq:bright-history}
 b_j=\frac{\widehat h_j^-+\widehat h_j^+}
 {\|\widehat h_j^-+\widehat h_j^+\|},
 \qquad
 \widehat h_j^\pm=\frac{h_j^\pm}{\|h_j^\pm\|},
 \qquad 0\le j\le k-2.$$ At the critical slice the two branch supports are disjoint and both normalized profiles are retained. The raw synthesis matrix is therefore $$\label{eq:raw-packet}
 V_0=(b_0,\ldots,b_{k-2},\widehat h_{k-1}^- ,
 \widehat h_{k-1}^+),
 \qquad m=k+1.$$

The canonical Perron/parity-compatible pair from [@WangBiorthogonal2026] is $$\label{eq:canonical-pair}
 V=\Pi_{\mathrm b}V_0,
 \qquad
 G=V_0^*\Pi_{\mathrm b}V_0,
 \qquad
 W=G^{-1}V_0^*\Pi_{\mathrm b},$$ whenever $G$ is invertible. It obeys $$\label{eq:pair-identities}
 WV=\mathrm I_m,
 \qquad L^*V=0,
 \qquad WR=0.$$ Define the oblique packet and external projectors $$\label{eq:P-Q}
 P=VW,
 \qquad Q=\mathrm I-P.$$ Then $$\label{eq:projector-identities}
 P^2=P,
 \qquad Q^2=Q,
 \qquad PQ=QP=0,
 \qquad P+Q=\mathrm I.$$ No orthogonality is asserted. In particular, $\|Pr\|^2+\|Qr\|^2$ need not equal $\|r\|^2$.

For route comparison we also use four raw packet variants:

1.  merge the final critical pair into one bright coordinate;

2.  keep only the left label at every slice;

3.  keep only the right label at every slice;

4.  retain both labels at every slice.

Each variant is passed through the same canonical construction [\[eq:canonical-pair\]](#eq:canonical-pair){reference-type="eqref" reference="eq:canonical-pair"}. Thus differences in the audit arise from the packet range rather than an inconsistent dual normalization.

[\[prop:gauge\]]{#prop:gauge label="prop:gauge"} Let $S\in\mathbb C^{m\times m}$ be invertible and define $$\label{eq:gauge-pair}
 V'=VS,
 \qquad W'=S^{-1}W.$$ Then $P'=V'W'=P$ and $Q'=Q$. For every operator $A$ and every spectral parameter where it is defined, the reduced matrix, self-energy, and Feshbach matrix transform by similarity: $$\begin{aligned}
 W'AV'&=S^{-1}(WAV)S,
 \label{eq:gauge-reduced}\\
 W'AQ(zQ-QAQ)^{-1}QAV'
 &=S^{-1}\!\left[WAQ(zQ-QAQ)^{-1}QAV\right]S,
 \label{eq:gauge-self-energy}\\
 F'(z)&=S^{-1}F(z)S.
 \label{eq:gauge-feshbach}\end{aligned}$$

The projector identity follows immediately from $VS S^{-1}W=VW$. The three similarity identities then follow by direct substitution.

Consequently the ambient quantities $Pr$, $Qr$, $PAQr$, and the spectrum of the reduced Feshbach matrix are packet-gauge invariant. Coordinate norms such as $\|Wr\|$ are not, so the main numerical conclusions below use ambient physical ratios whenever possible.

# Exact Feshbach algebra {#sec:feshbach}

We first state the finite-dimensional algebra in a form that allows $P$ to be oblique. Let $A\in\mathbb C^{n\times n}$, let $V\in\mathbb C^{n\times m}$ and $W\in\mathbb C^{m\times n}$ satisfy $WV=\mathrm I_m$, and define $P,Q$ by [\[eq:P-Q\]](#eq:P-Q){reference-type="eqref" reference="eq:P-Q"}. The direct-sum coordinates are $$\label{eq:direct-sum-coordinates}
 x=V\alpha+q,
 \qquad
 \alpha=Wx,
 \qquad
 q=Qx\in\operatorname{Ran}Q.$$

For $z\in\mathbb C$, define the external shifted block on $\operatorname{Ran}Q$ by $$\label{eq:external-block}
 D_Q(z)=\left.(zQ-QAQ)\right|_{\operatorname{Ran}Q}.$$ Whenever $D_Q(z)$ is invertible, define $$\begin{aligned}
 \Sigma(z)&=WAQ D_Q(z)^{-1}QAV,
 \label{eq:self-energy}\\
 F(z)&=z\mathrm I_m-WAV-\Sigma(z).
 \label{eq:feshbach-map}\end{aligned}$$

[\[thm:feshbach\]]{#thm:feshbach label="thm:feshbach"} If $D_Q(z)$ is invertible, then $$\label{eq:compressed-resolvent}
 W(z\mathrm I_n-A)^{-1}V=F(z)^{-1}$$ whenever either side is defined. Moreover, $$\label{eq:restricted-determinant}
 \det(z\mathrm I_n-A)=\det_{\operatorname{Ran}Q}D_Q(z)\,\det F(z).$$ Equivalently, for $z\ne0$ and the full-space matrix $D(z)=z\mathrm I_n-QAQ$, $$\label{eq:full-determinant}
 \boxed{
 \det(z\mathrm I_n-A)
 =z^{-m}\det D(z)\det F(z)}.$$

In the coordinates [\[eq:direct-sum-coordinates\]](#eq:direct-sum-coordinates){reference-type="eqref" reference="eq:direct-sum-coordinates"}, $z\mathrm I_n-A$ has the block representation $$\label{eq:block-matrix}
 \begin{pmatrix}
 z\mathrm I_m-WAV & -WAQ\\
 -QAV & D_Q(z)
 \end{pmatrix}.$$ Block Gaussian elimination by the invertible lower-right block gives $F(z)$ as the upper-left Schur complement. The inverse block formula gives [\[eq:compressed-resolvent\]](#eq:compressed-resolvent){reference-type="eqref" reference="eq:compressed-resolvent"}, and the block determinant formula gives [\[eq:restricted-determinant\]](#eq:restricted-determinant){reference-type="eqref" reference="eq:restricted-determinant"} [@Zhang2005; @SjoestrandZworski2007]. On $\operatorname{Ran}P$, the full-space matrix $z\mathrm I_n-QAQ$ acts as $z\mathrm I$. Therefore $\det D(z)=z^m\det_{\operatorname{Ran}Q}D_Q(z)$, which yields [\[eq:full-determinant\]](#eq:full-determinant){reference-type="eqref" reference="eq:full-determinant"}.

The elimination and compressed-resolvent identities hold for bounded operators wherever the block inverses exist. Fredholm determinant factorizations require the corresponding trace-class or determinant-class hypotheses [@GohbergKrein1969; @Baladi2000]. This paper proves the exact finite-dimensional identities used in the computation; it does not claim a uniform small-noise Fredholm limit.

The physical eigenmode gives an especially direct form of the same identity.

[\[thm:eigenmode-closure\]]{#thm:eigenmode-closure label="thm:eigenmode-closure"} Suppose $$\label{eq:abstract-eigenpair}
 Ar=\nu r.$$ Set $$\label{eq:alpha-q}
 \alpha=Wr,
 \qquad
 q=Qr,
 \qquad
 r=V\alpha+q.$$ Then $$\begin{aligned}
 (\nu\mathrm I_m-WAV)\alpha&=WAq,
 \label{eq:packet-closure}\\
 (\nu Q-QAQ)q&=QAV\alpha.
 \label{eq:external-closure}\end{aligned}$$ If $D_Q(\nu)$ is invertible, then $$\begin{aligned}
 q&=D_Q(\nu)^{-1}QAV\alpha,
 \label{eq:q-resolvent}\\
 F(\nu)\alpha&=0.
 \label{eq:feshbach-null}\end{aligned}$$ In particular, if $\alpha\ne0$, the physical eigenvalue is a zero of the Feshbach determinant.

Apply $W$ and $Q$ to $Ar=\nu r$ and substitute $r=V\alpha+q$. Since $WV=\mathrm I_m$, $Wq=0$, $QV=0$, and $Qq=q$, the two results are precisely [\[eq:packet-closure\]](#eq:packet-closure){reference-type="eqref" reference="eq:packet-closure"} and [\[eq:external-closure\]](#eq:external-closure){reference-type="eqref" reference="eq:external-closure"}. Invertibility of $D_Q(\nu)$ gives [\[eq:q-resolvent\]](#eq:q-resolvent){reference-type="eqref" reference="eq:q-resolvent"}; substitution into [\[eq:packet-closure\]](#eq:packet-closure){reference-type="eqref" reference="eq:packet-closure"} gives [\[eq:feshbach-null\]](#eq:feshbach-null){reference-type="eqref" reference="eq:feshbach-null"}.

[\[cor:resolvent-lower-bound\]]{#cor:resolvent-lower-bound label="cor:resolvent-lower-bound"} Under the invertibility assumption of [\[thm:eigenmode-closure\]](#thm:eigenmode-closure){reference-type="ref" reference="thm:eigenmode-closure"}, if $QAV\alpha\ne0$, then $$\label{eq:resolvent-lower-bound}
 \boxed{
 \|D_Q(\nu)^{-1}\|
 \ge
 \frac{\|q\|}{\|QAV\alpha\|}}.$$

Take norms in [\[eq:q-resolvent\]](#eq:q-resolvent){reference-type="eqref" reference="eq:q-resolvent"}.

The lower bound uses one physical forcing vector and may be much smaller than the full operator norm. Growth of the bound is therefore a genuine conditioning warning, whereas boundedness of the same diagnostic would not prove a uniformly bounded resolvent.

For the data audit we report the ambient, packet-gauge-invariant self-energy ratio $$\label{eq:physical-self-energy-ratio}
 \eta_{\mathrm{phys}}
 =\frac{\|VWAq\|}{{|\nu|\,\|Pr\|}}
 =\frac{\|PAq\|}{{|\nu|\,\|Pr\|}}.$$ It measures the correction in the physical packet range relative to the target action. It is not assumed to be perturbatively small.

# Compressed-resolvent pole and nonnormal visibility {#sec:residue}

The norm of $Pr$ alone does not determine whether the packet compression sees a physical pole. The left eigenvector enters the residue.

[\[prop:compressed-pole\]]{#prop:compressed-pole label="prop:compressed-pole"} Let $\nu$ be a simple eigenvalue of $A$, with $$\label{eq:left-right-normalization}
 Ar=\nu r,
 \qquad
 \ell^*A=\nu\ell^*,
 \qquad
 \ell^*r=1.$$ Then, in a punctured neighborhood of $\nu$, $$\label{eq:compressed-laurent}
 W(z\mathrm I-A)^{-1}V
 =\frac{(Wr)(\ell^*V)}{z-\nu}+H(z),$$ where $H$ is analytic. The trace residue is $$\label{eq:spectral-packet-weight}
 \boxed{
 \omega=\operatorname{tr}\!\left((Wr)(\ell^*V)\right)=\ell^*Pr}.$$ It is invariant under the packet gauge [\[eq:gauge-pair\]](#eq:gauge-pair){reference-type="eqref" reference="eq:gauge-pair"} and under every reciprocal rescaling of $r$ and $\ell^*$ preserving $\ell^*r=1$.

The resolvent Laurent expansion at a simple eigenvalue is $$\label{eq:resolvent-laurent}
 (z\mathrm I-A)^{-1}=\frac{r\ell^*}{z-\nu}+\widetilde H(z).$$ Compression gives [\[eq:compressed-laurent\]](#eq:compressed-laurent){reference-type="eqref" reference="eq:compressed-laurent"}. Cyclicity of the trace gives $\operatorname{tr}((Wr)(\ell^*V))=\ell^*VWr=\ell^*Pr$. Under a packet gauge, the residue matrix is transformed by similarity; under an eigenvector gauge, its two factors are scaled reciprocally.

With $\|r\|=1$, define the usual simple-eigenvalue condition number $$\label{eq:eigenvalue-condition}
 \kappa_\nu=\|\ell\|\,\|r\|=\|\ell\|.$$ Then $$\label{eq:weight-upper-bound}
 |\omega|\le\|\ell\|\,\|Pr\|=\kappa_\nu\|Pr\|.$$ Thus decreasing right capture can coexist with an order-one residue when the left eigenvector grows. This is standard nonnormal spectral geometry [@Kato1995; @StewartSun1990; @TrefethenEmbree2005]; no self-adjoint interpretation is available at this stage.

We also record the empirical compensation statistic $$\label{eq:compensation}
 C_{\mathrm{res}}=\|Pr\|
 \frac{\|Qr\|}{\|QAV\alpha\|}.$$ Unlike $\omega$, this is not a pole residue. It combines the packet capture with the one-vector lower bound in [\[eq:resolvent-lower-bound\]](#eq:resolvent-lower-bound){reference-type="eqref" reference="eq:resolvent-lower-bound"}. Its near constancy in the computed tail is evidence for a nonuniform compensation mechanism, not a theorem relating it to $\omega$.

# Numerical protocol and reproducibility {#sec:numerics}

All code, tests, input hashes, tables, and figure data are archived with the paper [@WangPhysicalFeshbachCode2026]. The primary calculation uses ordinary complex double precision. No interval enclosure or computer-assisted proof is claimed.

## Sparse physical eigensystem

At each of seven noise scales, the folded midpoint dimension is chosen so that $$\label{eq:resolution-density}
 n\sigma=20.48.$$ The sparse row-normalized matrix is built directly from [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}. Twenty right and twenty left ARPACK modes are computed. The Perron and parity modes are identified, biorthogonalized, and removed as in [\[eq:bulk-projector\]](#eq:bulk-projector){reference-type="eqref" reference="eq:bulk-projector"}. The selected positive-imaginary outer mode is matched to the archived physical cloud from [@WangBulkScattering2026]. Its one-step right and left residuals and the resulting two-step residual are retained in the output table.

## Packet and exact closure

Packet windows use six local Gaussian standard deviations by default. The branch histories are propagated by the exact sparse two-step bulk action, assembled according to [\[eq:raw-packet\]](#eq:raw-packet){reference-type="eqref" reference="eq:raw-packet"}, and passed through [\[eq:canonical-pair\]](#eq:canonical-pair){reference-type="eqref" reference="eq:canonical-pair"}. We then compute $$\label{eq:numerical-closure-data}
 \alpha=Wr,
 \qquad Pr=V\alpha,
 \qquad q=Qr,
 \qquad f_Q=QAV\alpha,$$ and evaluate both sides of [\[eq:packet-closure\]](#eq:packet-closure){reference-type="eqref" reference="eq:packet-closure"} and [\[eq:external-closure\]](#eq:external-closure){reference-type="eqref" reference="eq:external-closure"} independently. The nearest eigenvalue of the static reduced matrix $WAV$ is also recorded, but it is not substituted for the full Feshbach root.

## Independent shifted solve

To test the resolvent reconstruction rather than merely rearranging the known vector $q$, we solve $$\label{eq:gmres-system}
 (\nu\mathrm I-QAQ)\widetilde q=f_Q$$ with complex GMRES [@SaadSchultz1986; @Saad2003]. The ambient form in [\[eq:gmres-system\]](#eq:gmres-system){reference-type="eqref" reference="eq:gmres-system"} acts as $\nu\mathrm I$ on $\operatorname{Ran}P$ and as $D_Q(\nu)$ on $\operatorname{Ran}Q$. The parameters are relative tolerance $2\times10^{-8}$, restart length $80$, and at most $20$ restart cycles. We compare $\widetilde q$ with the exterior $q$ obtained from the physical eigenvector.

## Robustness and tests

At every scale we evaluate all five packet models described in [3](#sec:packet){reference-type="ref" reference="sec:packet"}. At $\sigma=10^{-3}$ and $10^{-4}$ we also repeat the baseline closure for packet half-widths $$\label{eq:window-widths}
 4.5,\ 5,\ 6,\ 7,\ 8$$ local standard deviations. Six unit tests verify complementary oblique projections, the dense determinant identity, the compressed-resolvent formula, exact eigenmode closure, the resolvent lower bound, packet-gauge covariance, and packet-model ranks on independent matrices. The implementation uses NumPy, SciPy, and Matplotlib [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007].

# Seven-scale physical closure {#sec:seven-scale}

gives the principal diagnostics. The packet rank is $k+1$, increasing from $4$ to $9$, while the ambient dimension increases by a factor of one hundred.

## Complex target and exact block residuals

The re-extracted one-step resonances agree with the archived cloud to at most $3.24\times10^{-15}$. The maximum one-step right and left eigenvector residuals are $3.21\times10^{-15}$ and $3.90\times10^{-15}$, respectively; the maximum two-step residual is $3.81\times10^{-15}$. Thus the target $\nu=\mu^2$ is internally consistent at the matrix level.

Across the seven scales, the normalized residual in [\[eq:packet-closure\]](#eq:packet-closure){reference-type="eqref" reference="eq:packet-closure"} is at most $$\label{eq:max-packet-residual}
 3.05\times10^{-14},$$ and that in [\[eq:external-closure\]](#eq:external-closure){reference-type="eqref" reference="eq:external-closure"} is at most $$\label{eq:max-external-residual}
 1.32\times10^{-13}.$$ These numbers verify the exact algebra in floating point. They should not be read as continuum error bounds.

The nearest eigenvalue of the static matrix $WAV$ remains separated from $\nu$: the distances across the seven scales are $$\label{eq:direct-distance-list}
 0.2481,\ 0.1362,\ 0.1058,\ 0.0900,\ 0.0510,\ 0.0471,\ 0.0521.$$ At $\sigma=10^{-4}$ the smallest singular value of $\nu\mathrm I-WAV$ is $0.0206$. The direct packet compression approaches the physical target over part of the range but does not close it. In contrast, the full self-energy gives the exact null equation $F(\nu)\alpha=0$ whenever the external solve is admitted.

![Physical target and exact closure. Top left: the selected one-step resonance remains complex. Top right: the phase of the $k$-fold return is generally nonzero, so a positive radius is not the exact target. Bottom left: the static packet matrix approaches but misses the complex two-step target. Bottom right: the full external self-energy closes the physical eigenmode to roundoff-scale residuals and is not negligible.](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/figures/physical_eigenmode_closure.pdf>){#fig:physical-closure width="\\textwidth"}

## The complement remains physical-sized

The ratio $\eta_{\rm phys}$ decreases from $0.829$ at the coarsest noise to $0.211$ at the smallest noise, but it is neither tiny nor monotone. At $\sigma=10^{-4}$, $$\label{eq:smallest-self-energy}
 \frac{\|PAq\|}{|\nu|\,\|Pr\|}=0.2111552.$$ Dropping the complement is therefore not a controlled small correction on the computed range. This statement is data-conditional: seven points do not rule out a different eventual asymptotic regime.

The independent shifted solves all return GMRES information code zero. They require $20$--$56$ iterations. The maximum true relative residual is $1.15\times10^{-8}$, and the maximum error relative to the eigenmode exterior is $$\label{eq:max-gmres-error}
 2.08\times10^{-8}.$$ Thus the observed exterior is reproduced by a genuine matrix-free resolvent calculation rather than only by substituting the known eigenvector into the block identity. Finite-precision convergence is strong evidence that the sampled shifted matrices are solvable, not an interval proof of invertibility.

![Independent complement solves. Left: GMRES remains convergent at all seven scales, although iteration count and elapsed time grow. Right: the true residual and the error against the physical eigenmode exterior remain at the prescribed $10^{-8}$ scale.](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/figures/shifted_solve_validation.pdf>){#fig:gmres width="\\textwidth"}

# Resolvent compensation and finite-range scaling {#sec:scaling}

The dominant trend is not a small complement but a redistribution of spectral visibility. The normalized right eigenvector moves out of the packet range: $\|Pr\|$ decreases by a factor $5.43$, and $\|Qr\|/\|Pr\|$ increases by a factor $5.79$. Simultaneously, the one-vector resolvent lower bound increases by a factor $7.15$, while the simple-eigenvalue condition number increases by a factor $16.4$.

The compressed pole does not disappear. Its gauge-invariant trace residue stays in $$\label{eq:weight-range}
 1.181\le |\ell^*Pr|\le1.619,$$ and the compensation statistic stays in $$\label{eq:compensation-range}
 1.841\le C_{\rm res}\le2.423.$$ The inequalities [\[eq:weight-upper-bound\]](#eq:weight-upper-bound){reference-type="eqref" reference="eq:weight-upper-bound"} allow this behavior because $\kappa_\nu$ grows much faster than $\|Pr\|$ decreases.

![Nonnormal compensation. Top left: right packet capture decreases. Top right: both the physical eigenvalue condition and the complement- resolvent lower bound grow. Bottom left: the compressed pole residue and $\|Pr\|R_{\rm lb}$ remain order one. Bottom right: the external forcing relative to $\|Pr\|$ stabilizes near $0.41$.](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/figures/resolvent_compensation_scaling.pdf>){#fig:compensation width="\\textwidth"}

For orientation only, we fit $y=C\sigma^a$ by ordinary least squares in log--log coordinates. reports the selected slopes.

::: {#tab:scaling-fits}
  diagnostic          $a$ (all)   $R^2$ (all)   $a$ (tail)   $R^2$ (tail)
  ----------------- ----------- ------------- ------------ --------------
  $\|Pr\|$            $+0.3805$      $0.9871$    $+0.4242$       $0.9997$
  $\|Qr\|/\|Pr\|$     $-0.3944$      $0.9900$    $-0.4298$       $0.9997$
  $\kappa_\nu$        $-0.6238$      $0.9889$    $-0.6771$       $0.9981$
  $R_{\rm lb}$        $-0.4355$      $0.9978$    $-0.4347$       $0.9996$
  $|\ell^*Pr|$        $-0.0598$      $0.8939$    $-0.0401$       $0.5899$

  : Finite-range log--log regressions. "All" uses seven points on $10^{-4}\le\sigma\le10^{-2}$; "tail" uses four points with $\sigma\le10^{-3}$. These fits are descriptive and are not asserted as asymptotic exponents.
:::

The near cancellation between the tail exponents for $\|Pr\|$ and $R_{\rm lb}$ explains the stable product in [\[eq:compensation-range\]](#eq:compensation-range){reference-type="eqref" reference="eq:compensation-range"}. It does not prove either exponent or their equality. In particular, the largest computation still has fixed positive noise and a finite matrix.

The lower-bound growth has one rigorous finite-data implication: any uniform resolvent bound proposed for these seven discretizations must be at least $37.52$. It does not, by itself, establish divergence as $\sigma\to0$. The correct conclusion is a *nonuniform conditioning barrier on the observed route*, not an asymptotic no-go theorem.

# Packet-route comparison {#sec:routes}

The packet range is not unique, so the closure must be tested against reasonable alternatives. compares all five models at the two tail scales. Every model satisfies the exact block equations to approximately $10^{-13}$ or better; the discriminating quantities are conditioning, direct-root distance, pole residue, and external-resolvent lower bound.

::: {#tab:route-comparison}
   $\sigma$   model               rank   $\kappa(G)$   $d_{\rm dir}$   $|\ell^*Pr|$   $R_{\rm lb}$
  ----------- ----------------- ------ ------------- --------------- -------------- --------------
   $10^{-3}$  branch complete        7        $1.27$       $0.09005$        $1.493$        $13.80$
              critical bright        6        $1.27$       $0.09005$        $1.493$        $13.80$
              left label             6        $1.19$       $0.02941$        $1.136$        $17.24$
              right label            6        $1.19$       $0.02922$        $1.116$        $17.15$
              all labels            12      $336.83$       $0.08979$        $1.494$        $13.80$
   $10^{-4}$  branch complete        9        $1.12$       $0.05213$        $1.619$        $37.51$
              critical bright        8        $1.12$       $0.05213$        $1.619$        $37.51$
              left label             8        $1.08$       $0.00586$        $1.229$        $48.84$
              right label            8        $1.08$       $0.00600$        $1.219$        $48.80$
              all labels            16     $1750.81$       $0.05205$        $1.619$        $37.51$

  : Packet-route comparison. $\kappa(G)$ is the canonical complement Gram condition number, $d_{\rm dir}=\operatorname{dist}(\nu,\operatorname{spec}(WAV))$, and $R_{\rm lb}$ is [\[eq:resolvent-lower-bound\]](#eq:resolvent-lower-bound){reference-type="eqref" reference="eq:resolvent-lower-bound"}.
:::

![Packet-route audit at the two tail scales. The fully label-resolved route reproduces the baseline spectral visibility but incurs rapid Gram growth. Single-label packets place a direct reduced root much closer to the target, at the cost of a smaller compressed pole residue and a larger external-resolvent lower bound.](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/figures/packet_route_comparison.pdf>){#fig:route-comparison width="\\textwidth"}

The comparison marks three distinct routes.

#### Final critical dark coordinate.

The branch-complete and critical-bright rows agree to the displayed digits. Thus deleting only the final local dark coordinate has negligible effect on these physical closure diagnostics. This is consistent with the local dark-channel no-go result of [@WangDarkSchur2026]. It does not show that every antisymmetric component of the full complement is irrelevant.

#### All-label route.

Keeping both labels around the entire cycle gives essentially the same $d_{\rm dir}$, residue, and lower bound as the baseline. Its Gram condition number, however, increases from $336.8$ to $1750.8$ between the two tail scales, and its analysis norm reaches $29.6$. This reproduces the branch-memory collapse identified in [@WangBiorthogonal2026]. The fully label-resolved packet is therefore marked as a conditioning dead end for the present canonical construction: it adds no observed spectral visibility while making the dual much less stable.

#### Single-label routes.

At $\sigma=10^{-4}$, a single-label direct root is almost nine times closer to $\nu$ than the baseline direct root. This is attractive but not a closure theorem. The trace residue drops by about $24\%$, and the external resolvent lower bound rises from $37.5$ to about $48.8$. The route is therefore *closer but riskier*: it improves a static eigenvalue metric while relying more heavily on the omitted space.

The branch-complete packet is retained as the clean baseline. It keeps the two locally stable critical supports, merges histories only after they have lost label separation, and avoids the severe all-label dual.

## Window robustness

varies the packet half-width. At $\sigma=10^{-3}$ the diagnostics are effectively saturated once the window reaches five local standard deviations. At $\sigma=10^{-4}$, over the full range $4.5$--$8$, the spreads relative to the baseline six-width value are approximately $$\begin{aligned}
 \|Pr\| &: 2.2\%,
 &|\ell^*Pr| &: 4.9\%,
 &R_{\rm lb} &: 3.6\%,
 &\eta_{\rm phys} &: 9.7\%.
 \label{eq:window-spreads}\end{aligned}$$ The direct-root distance is more sensitive, with a spread of about $20\%$. The full closure diagnostics are therefore substantially more robust than the static reduced root.

![Packet-window robustness. At $\sigma=10^{-3}$ the diagnostics saturate above five local standard deviations. At $\sigma=10^{-4}$ the right capture, compressed pole residue, and normalized resolvent lower bound vary moderately over the full window range.](<../../../../../zeta_mvp0/papers/RH-23-physical-packet-complement-feshbach/figures/packet_window_robustness.pdf>){#fig:window-robustness width="\\textwidth"}

# Scope and next operator target {#sec:scope}

This paper closes one algebraic gap and exposes one analytic gap. The algebraic gap was the absence of a physical full-complement formula. It is now exact: for a known physical eigenpair, the packet defect is precisely the external self-energy action, and the external component is precisely a shifted complement solve. The analytic gap is uniform control of that solve as the noise decreases and the dimension grows.

Three distinctions are essential.

#### Validation is not spectral prediction.

The eigenmode closure starts from a computed physical eigenpair. It proves that the Feshbach mechanism and its implementation are correct and measures the otherwise hidden complement terms. It does not independently locate $\nu$. Prediction requires evaluating $F(z)$ away from a known root and controlling its determinant on a contour.

#### Finite-range growth is not asymptotic divergence.

The observed slopes are remarkably consistent, but neither the continuum limit $n\to\infty$ nor the small-noise limit $\sigma\to0$ is proved here. Spectral approximation of nonnormal operators can be delicate [@Chatelin1983; @TrefethenEmbree2005]. Uniform inverse bounds, projector convergence, and discretization errors must be established before the finite-range regressions can become theorems.

#### A physical pole is not a self-adjoint spectrum.

The construction concerns a nonnormal Markov/transfer operator and its Feshbach reduction. It does not produce a self-adjoint generator, a $T\log T$ counting law, a prime-power trace formula, the Riemann zeros, or the Riemann hypothesis. Any connection to a Hilbert--Pólya program would require those additional structures and is outside the claims of this paper.

The route map after the present audit is $$\label{eq:route-map}
 \boxed{
 \begin{array}{rcl}
 \text{positive radius as exact target} &:& \text{rejected algebraically},\\
 \text{single local dark self-energy} &:& \text{rejected on archived data},\\
 \text{all-label packet dual} &:& \text{marked ill-conditioned},\\
 \text{static direct packet root} &:& \text{useful diagnostic, not closure},\\
 \text{full physical complement} &:& \text{exact and numerically viable},\\
 \text{uniform small-complement theory} &:& \text{unsupported on this range},\\
 \text{renormalized contour Feshbach map} &:& \text{next open route}.
 \end{array}}$$

The next computation should choose a contour $\Gamma$ around the physical target and solve the block system $$\label{eq:next-block-solve}
 (z\mathrm I-QAQ)X(z)=QAV,
 \qquad z\in\Gamma,$$ for all packet columns. This yields the full matrix self-energy $$\label{eq:next-self-energy}
 \Sigma(z)=WAQX(z)$$ and hence $\det F(z)$ on the contour. A predictive result then requires:

1.  stable block solves and an error estimate for $\Sigma(z)$;

2.  a winding-number or argument-principle count for $\det F(z)$;

3.  comparison with the full operator determinant or a certified Rouché bound;

4.  a resolution study separating matrix error from small-noise conditioning.

This next stage is falsifiable. Failure of contour solvability, loss of a stable winding number, or uncontrollable discretization growth would mark a new dead end. Success would turn the present eigenmode validation into an independent finite-dimensional spectral predictor.

# Conclusion {#sec:conclusion}

The full packet complement, rather than the single local dark coordinate, is the correct exact level for closing the physical two-step eigenmode. At that level the target must remain complex. The resulting oblique Feshbach algebra gives exact block equations, determinant and compressed-resolvent identities, a computable external-resolvent lower bound, and a gauge-invariant pole residue.

The numerical picture is coherent but nonperturbative. Right packet capture shrinks, complement and eigenvalue conditioning grow, and the full self-energy remains physical-sized. Yet the compressed pole residue and a projection--resolvent compensation statistic remain order one, while independent shifted solves continue to converge. The route has therefore not ended; it has changed from a uniformly small correction problem into a renormalized, nonuniform resolvent problem.

The next decisive layer is contour-wise. Only after the complete $z$-dependent self-energy has been computed and its determinant zeros have been counted independently can the packet construction claim predictive spectral closure. The present paper supplies the exact algebra, the conditioning diagnostics, and the route map needed for that test.

# Data and code availability {#data-and-code-availability .unnumbered}

Source code, unit tests, CSV tables, JSON metadata with source hashes, and all figures are contained in the RH-23 directory of the public repository [@WangPhysicalFeshbachCode2026]. The committed CSV files reproduce the tables, fits, and figures without rerunning the largest sparse eigensystems.
