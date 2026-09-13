---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-3-parity-resolved-band-merging-spectrum"
canonical_tex: "zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum/parity-resolved-band-merging-spectrum.pdf"
source_sha256: "5d9cf065571a2877301abc7c1eabdc3e75670f56615d9fca2454ba5a690acc3c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parity-Resolved Dynamics at a Quadratic Band-Merging Parameter: Peripheral Spectrum, Periodograms, and Two-Step Sequential Stability

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum/parity-resolved-band-merging-spectrum.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-3-parity-resolved-band-merging-spectrum/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $f_u(x)=1-u x^2$ and let $u_{\mathrm c}$ be the first band-merging parameter, characterized by $$u_{\mathrm c}^3-2u_{\mathrm c}^2+2u_{\mathrm c}-2=0,
      \qquad u_{\mathrm c}=1.543689012692\ldots.$$ The invariant interval of $f_{u_{\mathrm c}}$ has a genuine period-two decomposition $X=C\cup H$ with $f_{u_{\mathrm c}}(C)=H$ and $f_{u_{\mathrm c}}(H)=C$ modulo their common endpoint. Consequently the Koopman operator has the eigenfunction $s=\mathbf 1_C-\mathbf 1_H$ with eigenvalue $-1$, and the raw map is ergodic but not mixing. Under an explicit two-step component spectral-gap hypothesis on an adapted density space, the Perron--Frobenius peripheral spectrum is exactly $\{1,-1\}$.

  We give the exact parity-resolved operator decomposition under that hypothesis, for $n\ge1$: $$P^n=\Pi_+ +(-1)^n\Pi_-+R^n,
      \qquad \|R^n\|\le K\vartheta^n,$$ where $\Pi_+g=h\int g$ and $\Pi_-g=sh\int sg$, with $s=\mathbf 1_C-\mathbf 1_H$. Hence every sufficiently regular real observable has covariance $$\operatorname{Cov}_\mu(\phi,\phi\circ f_{u_{\mathrm c}}^n)
      =a_\phi^2(-1)^n+O(\vartheta^n),
      \qquad a_\phi=\int\phi s\,d\mu.$$ Its observable spectral measure contains an atom of mass $a_\phi^2$ at frequency $1/2$ (angular frequency $\pi$), in addition to the mean atom at zero and an analytic absolutely continuous remainder. We also prove that finite empirical discrete periodograms along almost every orbit converge weakly to this measure.

  For non-autonomous dynamics, the correct primitive object is the two-step block operator $Q_n=P_{2n}P_{2n-1}$. We prove an abstract adiabatic tracking theorem for a moving rank-two projector bundle and a parity-preserving sequential Birkhoff theorem under explicit uniform block memory-loss and paired-mean assumptions. Pairing consecutive iterates cancels the $-1$ mode and yields $L^2$ and almost-everywhere convergence without imposing an incompatible one-mode estimate. The exact geometry, parity eigenmode, ordinary Birkhoff theorem, and pathwise periodogram limit for each fixed bounded real observable are unconditional. Exponential operator remainders are stated under the component-gap hypothesis, and application of the sequential theorem to a prescribed nearby quadratic schedule remains conditional on verifying a common or moving two-phase bundle and uniform product estimates.
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
  **Parity-Resolved Dynamics at a Quadratic Band-Merging Parameter:**\
  Peripheral Spectrum, Periodograms, and Two-Step Sequential Stability
```

## Markdown 正文

**Keywords:** quadratic map; band merging; Perron--Frobenius operator; Koopman spectrum; peripheral eigenvalue; periodogram; sequential dynamical system; adiabatic tracking.

**MSC 2020:** 37E05; 37A30; 37M25; 47A35; 47B33.

# Introduction

At a mixing parameter, exponential memory loss is naturally expressed by a transfer-operator decomposition with a single peripheral eigenvalue $1$. At a band-merging parameter the geometry is different: two cyclic components are exchanged by one iterate and mixed only by the square of the map. On an adapted density space the Perron--Frobenius operator then has peripheral eigenvalues $1$ and $-1$, while the Koopman operator has the corresponding eigenfunctions $\mathbf 1$ and $s$. No claim is made that the full Koopman operator spectrum consists only of these points. Dropping the $-1$ eigenmode changes correlations, single-time density limits, and spectral measures.

This distinction refines a proposed sequential Birkhoff theorem for logarithmically drifting quadratic maps [@WangSequential2026]. That manuscript records that all first-return times at the limiting parameter are even, whereas a later one-mode raw estimate suppresses the resulting parity coordinate. At the constant schedule $u_n\equiv u_{\mathrm c}$, the parity observable alternates forever, so the estimate must be replaced by a two-mode formulation. The Birkhoff conclusion may nevertheless survive because Cesàro averaging cancels the alternating term.

The broader prime-dynamics program was introduced in @Wang2026Published, and the exact band-merging geometry was isolated in the rigorous reformulation of the prime-sieve correspondence [@WangReformulation2026]. The present paper develops the operator and spectral consequences of that geometry. It is logically independent of finite-stage sieve admissibility and of the inverse prime-kneading parameter studied in @WangPrimeSpectrum2026. No arithmetic or Riemann-zero assertion is used.

Periodic decompositions and root-of-unity peripheral modes for quasi-compact transfer operators are classical [@Baladi2000]; so are the Herglotz representation and the spectral measure of a stationary observable [@CornfeldFominSinai1982]. Sequential memory loss and limit theorems have been developed for several classes of time-dependent interval maps [@ConzeRaugi2007; @AiminoEtAl2015], while strong--weak stability of isolated operator clusters is governed by perturbation results such as @KellerLiverani1999. The contribution here is not a new general cyclic spectral theorem. It is the exact diagnosis of the period-two mode at this algebraic band-merging parameter, its explicit consequence for orbit periodograms, and a two-step sequential architecture which separates contraction transverse to a rank-two bundle from the unresolved dynamics inside that bundle.

## Main results {#main-results .unnumbered}

Let $P$ be the Perron--Frobenius operator of $f_{u_{\mathrm c}}$ relative to Lebesgue measure, let $h$ be the invariant density, and let $U\phi=\phi\circ f_{u_{\mathrm c}}$ be the Koopman isometry on $L^2(\mu)$, $d\mu=h\,dx$. The results are:

1.  The band-merging map has a two-cycle partition $C,H$. Unconditionally, with $s=\mathbf 1_C-\mathbf 1_H$, $$Us=-s,
            \qquad P(sh)=-sh.$$ Under [\[ass:component-gap\]](#ass:component-gap){reference-type="ref" reference="ass:component-gap"}, the Perron--Frobenius peripheral spectrum is exactly $\{1,-1\}$ and the rest contracts exponentially.

2.  Under the same component-gap hypothesis, every regular real observable admits the orthogonal decomposition $$\phi=m_\phi+a_\phi s+\psi,$$ and $$\operatorname{Cov}_\mu(\phi,\phi\circ f_{u_{\mathrm c}}^n)
            =a_\phi^2(-1)^n+O(\vartheta^n).$$ Thus its spectral measure is $$\sigma_\phi
            =m_\phi^2\delta_0+a_\phi^2\delta_{1/2}
             +w_\psi(t)\,dt,$$ where $w_\psi$ is nonnegative and real analytic.

3.  For every fixed bounded real observable and $\mu$-almost every initial point, the finite DFT periodogram measures converge weakly to $\sigma_\phi$. The parity atom, when its mass is nonzero, is therefore a pathwise spectral feature, not merely an operator-level formalism.

4.  For a sequence of parity-preserving maps, uniform exponential memory loss is imposed on the two-step block products, rather than on the raw one-step maps. Under a common paired-mean hypothesis, pairing one observation from each phase cancels the alternating mode, and the combined Birkhoff average converges in $L^2$ and almost everywhere to that common limit. At the constant schedule the limit is the equal component average.

5.  More generally, if $Q_n=P_{2n}P_{2n-1}$ is equipped with a moving rank-two projector bundle $E_n=\operatorname{Ran}\Pi_n$ and the complementary products contract, then the non-autonomous density tracks $E_n$ with an explicit convolution bound. A logarithmic schedule has summable parameter increments, but its internal two-dimensional cocycle must still be analyzed: convergence $Q_n\to P_{u_{\mathrm c}}^2$ alone does not decide whether the parity mode persists or decays.

The exact Markov geometry, invariant component measures, parity eigenmode, Birkhoff limit, and pathwise periodogram theorem for each fixed bounded real observable apply unconditionally to the algebraic Misiurewicz map by classical interval-map theory [@Misiurewicz1981; @Young1992; @deMeloVanStrien1993; @Baladi2000]. The strong operator remainder and analytic spectral-density statements are conditional on [\[ass:component-gap\]](#ass:component-gap){reference-type="ref" reference="ass:component-gap"}; a tower construction is a standard route to that hypothesis, but the present paper does not build the required interval density space from scratch. The sequential results are likewise abstract theorems with explicit hypotheses. We do not assert that an arbitrary one-sided logarithmic schedule lies in a single uniform tower-supporting parameter set.

# Exact band-merging geometry

Let $$\label{eq:quadratic-family}
    f_u(x)=1-u x^2,
    \qquad 0<u\le2.$$

The following proposition is recalled from @WangReformulation2026; its short calculation is reproduced for self-containment.

[\[prop:geometry\]]{#prop:geometry label="prop:geometry"} The polynomial $$\label{eq:uc-polynomial}
    F(u)=u^3-2u^2+2u-2$$ has a unique zero $u_{\mathrm c}$ in $(1,2)$. Put $b=u_{\mathrm c}-1$. Then $$\label{eq:critical-orbit}
    0\longmapsto1\longmapsto-b\longmapsto b\longmapsto b.$$ On $X=[-b,1]$, define $$J_L=[-b,0],\qquad J_0=[0,b],\qquad J_1=[b,1].$$ Up to common endpoints, $$\label{eq:markov-images}
    f_{u_{\mathrm c}}(J_L)=J_1,
    \qquad f_{u_{\mathrm c}}(J_0)=J_1,
    \qquad f_{u_{\mathrm c}}(J_1)=J_L\cup J_0.$$ The transition matrix is $$\label{eq:markov-matrix}
    A=
    \begin{pmatrix}
        0&0&1\\
        0&0&1\\
        1&1&0
    \end{pmatrix},
    \qquad \operatorname{spec}(A)=\{0,\sqrt2,-\sqrt2\}.$$

One has $F(1)=-1$, $F(2)=2$, and $$F'(u)=3\left(u-\frac23\right)^2+\frac23>0.$$ Thus the zero is unique. Equation $F(u_{\mathrm c})=0$ is equivalent to $1-u_{\mathrm c}b^2=b$, while $1-u_{\mathrm c}=-b$, proving [\[eq:critical-orbit\]](#eq:critical-orbit){reference-type="eqref" reference="eq:critical-orbit"}. On $[-b,0]$ the map is increasing from $b$ to $1$; on $[0,b]$ it is decreasing from $1$ to $b$; and on $[b,1]$ it is decreasing from $b$ to $-b$. This proves [\[eq:markov-images\]](#eq:markov-images){reference-type="eqref" reference="eq:markov-images"}. Finally, $$\det(\lambda I-A)=\lambda(\lambda^2-2),$$ which gives [\[eq:markov-matrix\]](#eq:markov-matrix){reference-type="eqref" reference="eq:markov-matrix"}.

Define, modulo the common endpoint $b$, $$\label{eq:cyclic-components}
    C=[-b,b],
    \qquad H=[b,1].$$

[\[cor:period-two\]]{#cor:period-two label="cor:period-two"} The map satisfies $$\label{eq:component-swap}
    f_{u_{\mathrm c}}(C)=H,
    \qquad f_{u_{\mathrm c}}(H)=C.$$ Moreover $f_{u_{\mathrm c}}^2$ is topologically mixing on each component with respect to its Markov partition. Thus the raw Markov system has period exactly two.

The image relations follow from [\[eq:markov-images\]](#eq:markov-images){reference-type="eqref" reference="eq:markov-images"}. Squaring $A$ separates the state $J_1$ from the two states $J_L,J_0$; the restriction to $\{J_L,J_0\}$ is the positive matrix with every entry equal to $1$. More explicitly, $$f_{u_{\mathrm c}}^2(J_L)=f_{u_{\mathrm c}}^2(J_0)=C.$$ On $H$, put $c_H=u_{\mathrm c}^{-1/2}$. Since $u_{\mathrm c}b^2=1-b<1$ and $u_{\mathrm c}>1$, one has $b<c_H<1$. Split $$H_0=[b,c_H],
    \qquad H_1=[c_H,1].$$ Then $f_{u_{\mathrm c}}^2(H_0)=f_{u_{\mathrm c}}^2(H_1)=H$. Thus both two-step component graphs have full branches and are aperiodic and mixing; see @LindMarcus1995 [Chapter 4].

The critical orbit is finite and lands on the repelling fixed point $b$: indeed $F(3/2)<0$ gives $u_{\mathrm c}>3/2$, hence $b>1/2$ and $|f_{u_{\mathrm c}}'(b)|=2u_{\mathrm c}b>3/2$. The component critical orbits also terminate there: $$0\xmapsto{f_{u_{\mathrm c}}^2}-b\xmapsto{f_{u_{\mathrm c}}^2}b,
    \qquad
    c_H\xmapsto{f_{u_{\mathrm c}}^2}1\xmapsto{f_{u_{\mathrm c}}^2}b.$$ Thus the two component maps are nonflat Misiurewicz maps. Classical results give an absolutely continuous invariant probability measure and exponential correlation estimates on each mixing component of the square for standard Hölder or tower-regular observable classes [@Misiurewicz1981; @Young1992; @deMeloVanStrien1993]. An operator-norm formulation requires an adapted tower or weighted space which accommodates the postcritical singularities of the invariant density; it need not be ordinary $BV(X)$.

[\[prop:component-measures\]]{#prop:component-measures label="prop:component-measures"} The map $f_{u_{\mathrm c}}$ has a unique absolutely continuous invariant probability measure $\mu$. It is ergodic and not mixing. One has $$\mu(C)=\mu(H)=\frac12.$$ The probability measures $$\label{eq:component-measures}
    \mu_C=2\mu|_C,
    \qquad \mu_H=2\mu|_H$$ are the two mixing absolutely continuous invariant measures of $f_{u_{\mathrm c}}^2$, and $$(f_{u_{\mathrm c}})_*\mu_C=\mu_H,
    \qquad (f_{u_{\mathrm c}})_*\mu_H=\mu_C.$$

The Misiurewicz results just cited give unique mixing absolutely continuous invariant probabilities $\nu_C$ and $\nu_H$ for the two primitive components of $f_{u_{\mathrm c}}^2$. Component interchange implies that $(f_{u_{\mathrm c}})_*\nu_C$ is an absolutely continuous $f_{u_{\mathrm c}}^2$-invariant probability on $H$, hence equals $\nu_H$ by uniqueness; similarly $(f_{u_{\mathrm c}})_*\nu_H=\nu_C$. Therefore $\mu=(\nu_C+\nu_H)/2$ is $f_{u_{\mathrm c}}$-invariant. Conversely, any absolutely continuous $f_{u_{\mathrm c}}$-invariant probability restricts, after normalization, to $\nu_C$ and $\nu_H$, and the interchange forces equal weights. Thus $\mu$ is unique, $\mu_C=\nu_C$, $\mu_H=\nu_H$, and [\[eq:component-measures\]](#eq:component-measures){reference-type="eqref" reference="eq:component-measures"}--[\[eq:component-swap\]](#eq:component-swap){reference-type="eqref" reference="eq:component-swap"} follow. A measurable $f_{u_{\mathrm c}}$-invariant set has square-map-invariant intersections with both components. Component ergodicity and the interchange then force its measure to be $0$ or $1$, proving ergodicity. Nonmixing follows from the nontrivial eigenfunction constructed below.

# The Perron--Frobenius peripheral spectrum is $\{1,-1\}$

Let $m$ denote Lebesgue measure on $X$, write $d\mu=h\,dm$, and let $P$ be the Perron--Frobenius operator of $f_{u_{\mathrm c}}$ relative to $m$: $$\int_X \chi\,Pg\,dm
    =\int_X (\chi\circ f_{u_{\mathrm c}})g\,dm.$$ We isolate the exact operator input needed below.

[\[ass:component-gap\]]{#ass:component-gap label="ass:component-gap"} There is a Banach space $\mathcal B\hookrightarrow L^1(m)$ of signed densities such that multiplication by $\mathbf 1_C,\mathbf 1_H$ and the operator $P$ are bounded on $\mathcal B$, and $h\in\mathcal B$. Put $$h_C=2h\mathbf 1_C,
    \qquad h_H=2h\mathbf 1_H.$$ There exist $M<\infty$ and $0<\rho<1$ such that, for $D\in\{C,H\}$ and every $g\in\mathcal B$ supported in $D$, $$\label{eq:component-gap}
    \left\|(P^2)^n g-h_D\int_Dg\,dm\right\|_{\mathcal B}
    \le M\rho^n\|g\|_{\mathcal B}.$$

A mixing exponential-tail tower for each component is a standard route toward [\[ass:component-gap\]](#ass:component-gap){reference-type="ref" reference="ass:component-gap"} [@Young1992; @Baladi2000]. Passing from a tower operator to the precise interval-density norm in the assumption requires a specified quotient or weighted-space construction. We therefore retain [\[ass:component-gap\]](#ass:component-gap){reference-type="ref" reference="ass:component-gap"} explicitly instead of identifying it with ordinary $BV$ decay.

All spectral statements below are understood on the complexification $\mathcal B_{\mathbb C}$ of the signed-density space.

Set $$\label{eq:parity-sign}
    s=\mathbf 1_C-\mathbf 1_H.$$ The value at $b$ is irrelevant because $\mu$ is nonatomic.

[\[thm:pf-decomposition\]]{#thm:pf-decomposition label="thm:pf-decomposition"} Under [\[ass:component-gap\]](#ass:component-gap){reference-type="ref" reference="ass:component-gap"}, define $$\label{eq:peripheral-projectors}
    \Pi_+g=h\int_Xg\,dm,
    \qquad
    \Pi_-g=sh\int_Xsg\,dm.$$ Then $\Pi_+$ and $\Pi_-$ are mutually annihilating rank-one spectral projectors, $$\label{eq:pf-eigenvectors}
    Ph=h,
    \qquad P(sh)=-sh,$$ and, for every $n\ge1$, $$\label{eq:pf-power-decomposition}
    P^n=\Pi_+ +(-1)^n\Pi_-+R^n,
    \qquad
    R=P(I-\Pi_+-\Pi_-).$$ There exist $K<\infty$ and $0<\vartheta<1$ such that $$\label{eq:remainder-decay}
    \|R^n\|_{\mathcal B\to\mathcal B}\le K\vartheta^n.$$ In particular, the peripheral spectrum of $P$ is exactly $\{1,-1\}$, and both eigenvalues are algebraically simple.

The component interchange and invariance give $$P(h\mathbf 1_C)=h\mathbf 1_H,
    \qquad P(h\mathbf 1_H)=h\mathbf 1_C.$$ Adding and subtracting yields [\[eq:pf-eigenvectors\]](#eq:pf-eigenvectors){reference-type="eqref" reference="eq:pf-eigenvectors"}. The corresponding left eigenfunctionals are $$\ell_+(g)=\int g\,dm,
    \qquad
    \ell_-(g)=\int sg\,dm,$$ because $s\circ f_{u_{\mathrm c}}=-s$ almost everywhere. Since $$\int sh\,dm=\mu(C)-\mu(H)=0,
    \qquad
    \int s^2h\,dm=1,$$ the formulas in [\[eq:peripheral-projectors\]](#eq:peripheral-projectors){reference-type="eqref" reference="eq:peripheral-projectors"} are normalized projectors and $\Pi_+\Pi_-=\Pi_-\Pi_+=0$.

For $g=g_C+g_H$, [\[eq:component-gap\]](#eq:component-gap){reference-type="eqref" reference="eq:component-gap"} gives $$(P^2)^ng
    =h_C\int_Cg\,dm+h_H\int_Hg\,dm
      +O_{\mathcal B}(\rho^n\|g\|_{\mathcal B}).$$ The main term equals $(\Pi_++\Pi_-)g$. One further application of the bounded operator $P$ changes it to $(\Pi_+-\Pi_-)g$. Thus the even and odd remainders decay geometrically. Because $P$ commutes with the spectral projectors, while $R\Pi_\pm=\Pi_\pm R=0$, this is precisely [\[eq:pf-power-decomposition\]](#eq:pf-power-decomposition){reference-type="eqref" reference="eq:pf-power-decomposition"}--[\[eq:remainder-decay\]](#eq:remainder-decay){reference-type="eqref" reference="eq:remainder-decay"}, after adjusting the constant and taking $\sqrt\rho\le\vartheta<1$. Finally, the $1$-eigenspaces of $P^2$ on the two mixing components are spanned by $h_C,h_H$. On their span, $P$ is the component-swap matrix, whose eigenvalues $1,-1$ are simple. No other peripheral eigenvalue remains.

[\[rem:koopman-pf\]]{#rem:koopman-pf label="rem:koopman-pf"} For the Koopman isometry $U\phi=\phi\circ f_{u_{\mathrm c}}$ on $L^2(\mu)$, $$U\mathbf 1=\mathbf 1,
    \qquad Us=-s.$$ For the Lebesgue-reference Perron--Frobenius operator, the right eigenvectors are $h$ and $sh$, not generally $\mathbf 1$ and $s$. The statement $Ps=-s$ is therefore usually false; it becomes valid only for the transfer operator normalized relative to $\mu$.

# Parity-resolved correlations and observable spectra

The following formula is the correct replacement for a one-step raw mixing estimate.

[\[thm:parity-correlation\]]{#thm:parity-correlation label="thm:parity-correlation"} Let $\phi,\chi$ be real observables such that $\phi h\in\mathcal B$ and $\chi\in L^\infty(\mu)$. Then, for every $n\ge0$, $$\label{eq:two-mode-correlation}
\begin{split}
    \int_X\phi\,(\chi\circ f_{u_{\mathrm c}}^n)\,d\mu
    &={\left(\int_X\phi\,d\mu\right)}
      {\left(\int_X\chi\,d\mu\right)}\\
    &\quad+(-1)^n
      {\left(\int_X\phi s\,d\mu\right)}
      {\left(\int_X\chi s\,d\mu\right)}
      +O\!\left(\vartheta^n
        \|\phi h\|_{\mathcal B}\|\chi\|_\infty\right).
\end{split}$$

By transfer duality and [\[thm:pf-decomposition\]](#thm:pf-decomposition){reference-type="ref" reference="thm:pf-decomposition"}, $$\int_X\phi\,(\chi\circ f_{u_{\mathrm c}}^n)\,d\mu
    =\int_X\chi\,P^n(\phi h)\,dm.$$ For $n\ge1$, the $\Pi_+$ term is the product of the ordinary means, the $\Pi_-$ term is the alternating product of the two parity means, and the $R^n$ term is bounded by [\[eq:remainder-decay\]](#eq:remainder-decay){reference-type="eqref" reference="eq:remainder-decay"} and the $L^1$ embedding of $\mathcal B$. The case $n=0$ follows directly after enlarging the implicit constant.

Taking $\phi=\chi=s$ gives $$\label{eq:parity-nondecay}
    \int_Xs\,(s\circ f_{u_{\mathrm c}}^n)\,d\mu=(-1)^n.$$ Thus no estimate of the form $$\left|\int\phi\,(\chi\circ f_{u_{\mathrm c}}^n)\,d\mu
    -\int\phi\,d\mu\int\chi\,d\mu\right|
    \le C\vartheta^n$$ can hold for all regular observables.

For a real observable $\phi\in L^2(\mu)$, set $$\label{eq:observable-components}
    m_\phi=\int_X\phi\,d\mu,
    \qquad
    a_\phi=\int_X\phi s\,d\mu,
    \qquad
    \psi=\phi-m_\phi-a_\phi s.$$ Since $\mathbf 1$ and $s$ are orthonormal in $L^2(\mu)$, this is the orthogonal decomposition $$\label{eq:observable-decomposition}
    \phi=m_\phi\mathbf 1+a_\phi s+\psi,
    \qquad
    \langle\psi,\mathbf 1\rangle=\langle\psi,s\rangle=0.$$

[\[cor:covariance\]]{#cor:covariance label="cor:covariance"} If $\phi h\in\mathcal B$ and $\phi\in L^\infty(\mu)$, then $$\label{eq:covariance-decomposition}
    \operatorname{Cov}_\mu(\phi,\phi\circ f_{u_{\mathrm c}}^n)
    =a_\phi^2(-1)^n+r_\phi(n),
    \qquad
    |r_\phi(n)|\le K_\phi\vartheta^n,$$ where $$r_\phi(n)=\int_X\psi\,(\psi\circ f_{u_{\mathrm c}}^n)\,d\mu.$$

Apply [\[thm:parity-correlation\]](#thm:parity-correlation){reference-type="ref" reference="thm:parity-correlation"} to $\psi$. The cross terms with $\mathbf 1$ vanish by centering. The cross terms with $s$ vanish exactly: for example, $$\int_Xs\,(\psi\circ f_{u_{\mathrm c}}^n)\,d\mu
    =\int_X\psi\,P^n(sh)\,dm
    =(-1)^n\int_X\psi s\,d\mu=0.$$ The remaining parity term is $a_\phi^2(-1)^n$.

## The observable spectral measure

We use the frequency circle $\mathbb T=\mathbb R/\mathbb Z$ and normalized Haar measure $dt$. Although the Koopman operator of a noninvertible interval map is an isometry rather than a unitary operator, the stationary correlation sequence is positive definite. Herglotz' theorem, equivalently the unitary natural extension, therefore defines a unique finite positive measure $\sigma_\phi$ by $$\label{eq:spectral-measure-definition}
    \widehat\sigma_\phi(n)
    :=\int_{\mathbb T}e^{2\pi i nt}\,d\sigma_\phi(t)
    =\int_X\phi\,(\phi\circ f_{u_{\mathrm c}}^n)\,d\mu,
    \qquad n\ge0,$$ with negative coefficients given by conjugation.

[\[thm:spectral-measure\]]{#thm:spectral-measure label="thm:spectral-measure"} Under the hypotheses of [\[cor:covariance\]](#cor:covariance){reference-type="ref" reference="cor:covariance"}, $$\label{eq:spectral-decomposition}
    \sigma_\phi
    =m_\phi^2\delta_0+a_\phi^2\delta_{1/2}
      +w_\psi(t)\,dt,$$ where $$\label{eq:continuous-density}
    w_\psi(t)=\sum_{n\in\mathbb Z}r_\phi(n)e^{-2\pi i nt},
    \qquad r_\phi(-n)=\overline{r_\phi(n)}.$$ The function $w_\psi$ is nonnegative and real analytic. In angular frequency, the atom at $1/2$ is the atom at $\pi$.

The Fourier coefficients of $m_\phi^2\delta_0$ are $m_\phi^2$, and those of $a_\phi^2\delta_{1/2}$ are $a_\phi^2(-1)^n$. The remainder coefficients in [\[eq:covariance-decomposition\]](#eq:covariance-decomposition){reference-type="eqref" reference="eq:covariance-decomposition"} decay exponentially in both directions, so the Fourier series [\[eq:continuous-density\]](#eq:continuous-density){reference-type="eqref" reference="eq:continuous-density"} converges absolutely in a complex strip and defines a real-analytic function. It is nonnegative because it is the Radon--Nikodym density of the positive spectral measure of the orthogonal component $\psi$.

Exponential decay is stronger than is needed for absolute continuity. Summability of $r_\phi(n)$ already gives a continuous density; the tower gap upgrades it to analyticity.

[\[cor:left-symbol-spectrum\]]{#cor:left-symbol-spectrum label="cor:left-symbol-spectrum"} Let $\ell=\mathbf 1_{J_L}$, assume $\ell h\in\mathcal B$ as in the Markov-adapted tower construction, and put $q=\mu(J_L)$. Then $$m_\ell=q,
    \qquad a_\ell=q,$$ and therefore $$\label{eq:left-symbol-spectrum}
    \sigma_\ell=q^2\delta_0+q^2\delta_{1/2}
      +w_\ell(t)\,dt,
    \qquad w_\ell=w_{\ell-q-qs}.$$ Centering $\ell$ removes the zero-frequency atom but leaves the parity atom unchanged. For the parity observable itself, $\sigma_s=\delta_{1/2}$ exactly.

The set $J_L$ lies in $C$, so $s=1$ on $J_L$ modulo endpoints. Hence $\int\ell s\,d\mu=\int\ell\,d\mu=q$. The last assertion follows from $s\circ f_{u_{\mathrm c}}=-s$.

# Pathwise convergence of finite periodograms

The spectral measure above is recovered from almost every single orbit. Let $T=f_{u_{\mathrm c}}$, let $\phi\in L^\infty(\mu)$ be real-valued, and define the unitary DFT of the first $N$ observations by $$\label{eq:orbit-dft}
    \widehat\phi_{N,x}(j)
    =\frac1{\sqrt N}\sum_{n=0}^{N-1}
      \phi(T^nx)e^{-2\pi ijn/N},
    \qquad 0\le j<N.$$ The associated finite measure on $\mathbb T$ is $$\label{eq:orbit-periodogram}
    \mathcal I_{N,x}
    =\frac1N\sum_{j=0}^{N-1}
      |\widehat\phi_{N,x}(j)|^2\,\delta_{j/N}.$$ Discrete Parseval gives $$\label{eq:periodogram-mass}
    \mathcal I_{N,x}(\mathbb T)
    =\frac1N\sum_{n=0}^{N-1}|\phi(T^nx)|^2.$$

[\[thm:pathwise-periodogram\]]{#thm:pathwise-periodogram label="thm:pathwise-periodogram"} For $\mu$-almost every $x$, $$\label{eq:pathwise-weak-limit}
    \mathcal I_{N,x}\mathop{\Longrightarrow}\sigma_\phi.$$ If $\|\phi\|_{L^2(\mu)}>0$, then for almost every $x$ the mass $\mathcal I_{N,x}(\mathbb T)$ is positive for all sufficiently large $N$, and the corresponding normalized probability measures converge weakly to $\sigma_\phi/\|\phi\|_2^2$.

For every fixed integer $r\ge0$, discrete Wiener--Khinchin gives $$\label{eq:periodogram-fourier-coefficient}
    \widehat{\mathcal I_{N,x}}(r)
    =\frac1N\sum_{n=0}^{N-1}
      \phi(T^nx)\phi(T^{n+r\bmod N}x).$$ At most $r$ summands wrap around the endpoint. Since $\phi$ is bounded, their total contribution is $O_\phi(r/N)$. The remaining average differs by $o(1)$ from the Birkhoff average of the integrable observable $$x\longmapsto\phi(x)\phi(T^rx).$$ The map $T$ is ergodic by [\[prop:component-measures\]](#prop:component-measures){reference-type="ref" reference="prop:component-measures"}, so for almost every $x$ the right-hand side of [\[eq:periodogram-fourier-coefficient\]](#eq:periodogram-fourier-coefficient){reference-type="eqref" reference="eq:periodogram-fourier-coefficient"} converges to $\widehat\sigma_\phi(r)$. Intersecting the full-measure sets over the countably many $r$ handles all nonnegative coefficients; the negative coefficients follow by conjugation. Equation [\[eq:periodogram-mass\]](#eq:periodogram-mass){reference-type="eqref" reference="eq:periodogram-mass"} and Birkhoff give convergence of the total masses. Density of trigonometric polynomials in $C(\mathbb T)$ now proves weak convergence.

When $N$ is even, the parity mode lies exactly in the bin $j=N/2$. When $N$ is odd it leaks across the grid, with its largest concentration near the closest bins, but [\[thm:pathwise-periodogram\]](#thm:pathwise-periodogram){reference-type="ref" reference="thm:pathwise-periodogram"} shows that the leaked mass still converges weakly to the atom at $1/2$. The theorem concerns measure convergence; it does not claim pointwise consistency of individual unsmoothed periodogram ordinates.

# Why Birkhoff averages survive the $-1$ mode

The missing parity mode invalidates one-step mixing and one-step convergence of general densities, but it does not invalidate Cesàro convergence.

[\[prop:alternating-expectations\]]{#prop:alternating-expectations label="prop:alternating-expectations"} Let $g\in\mathcal B$ be a probability density and let $\phi$ be bounded. For every $n\ge0$, $$\label{eq:alternating-expectation}
    \int_X\phi\circ f_{u_{\mathrm c}}^n\,g\,dm
    =m_\phi+(-1)^na_\phi\int_Xsg\,dm
      +O\!\left(\vartheta^n\|g\|_{\mathcal B}\|\phi\|_\infty\right).$$ Unless $a_\phi=0$ or the initial phase masses are balanced, the expectation has two alternating limits rather than one.

For $n\ge1$, insert [\[eq:pf-power-decomposition\]](#eq:pf-power-decomposition){reference-type="eqref" reference="eq:pf-power-decomposition"} into $$\int\phi\circ f_{u_{\mathrm c}}^n\,g\,dm
    =\int\phi\,P^ng\,dm.$$ The case $n=0$ follows directly after enlarging the implicit constant.

[\[prop:paired-autonomous\]]{#prop:paired-autonomous label="prop:paired-autonomous"} For every $\phi\in L^1(\mu)$, for $\mu$-almost every $x$, $$\label{eq:paired-birkhoff}
\begin{split}
    \frac1{2N}\sum_{n=0}^{2N-1}\phi(f_{u_{\mathrm c}}^nx)
    &=\frac12\left(
       \frac1N\sum_{j=0}^{N-1}\phi(f_{u_{\mathrm c}}^{2j}x)
       +\frac1N\sum_{j=0}^{N-1}\phi(f_{u_{\mathrm c}}^{2j+1}x)
      \right)\\
    &\longrightarrow
      \frac12\left(\int\phi\,d\mu_C+
                    \int\phi\,d\mu_H\right)
      =\int\phi\,d\mu.
\end{split}$$ If $\phi\in L^\infty(\mu)$ and $\phi h\in\mathcal B$, the $L^2(\mu)$ variance is $O_\phi(N^{-1})$.

If $x\in C$, the even iterates are governed by the mixing system $(C,f_{u_{\mathrm c}}^2,\mu_C)$ and the odd iterates by its transported copy on $H$; for $x\in H$ the roles reverse. Birkhoff's theorem on each component proves the almost-everywhere limit. For the variance, summing [\[eq:covariance-decomposition\]](#eq:covariance-decomposition){reference-type="eqref" reference="eq:covariance-decomposition"} over a block of $2N$ observations gives a parity contribution $$\frac{a_\phi^2}{(2N)^2}
    \left|\sum_{n=0}^{2N-1}(-1)^n\right|^2=0,$$ while the exponentially summable remainder contributes $O_\phi(N^{-1})$.

Thus the correct logic is $$\text{two-step component mixing}
    \;\Longrightarrow\;
    \text{paired Ces\`aro convergence},$$ not one-step raw mixing. The next sections formulate the same mechanism for non-autonomous operators.

# A moving rank-two bundle for two-step operators

Let $P_n=P_{u_n}$ be Markov transfer operators and group them into $$\label{eq:block-operators}
    Q_n=P_{2n}P_{2n-1}.$$ At the limiting parameter, $Q_*=P_{u_{\mathrm c}}^2$ has a two-dimensional $1$-eigenspace, even though the eigenvalues $1$ and $-1$ of $P_{u_{\mathrm c}}$ are individually simple. This rank-two cluster is the stable object for perturbation theory.

We state a strong--weak abstract theorem. Let $$\mathcal B_s\hookrightarrow\mathcal B_w\hookrightarrow L^1(m),
    \qquad |g|_w\le C\|g\|_s.$$ For $n\ge0$, let $\xi_n$ be a block parameter and let $\Pi_n\in\mathcal L(\mathcal B_s)\cap\mathcal L(\mathcal B_w)$ be a rank-two projector, with both operator norms bounded uniformly in $n$. For $n\ge1$, assume that $Q_n\in\mathcal L(\mathcal B_s)$ commutes with $\Pi_n$, and put $$\label{eq:block-remainder}
    E_n=\operatorname{Ran}\Pi_n,
    \qquad
    R_n=Q_n(I-\Pi_n).$$

[\[ass:rank-two-gap\]]{#ass:rank-two-gap label="ass:rank-two-gap"} The following bounds hold with constants independent of the allowed sequence.

1.  Every orbit $g_n=Q_n\cdots Q_1g_0$ with $g_0\in\mathcal B_s$ satisfies $$\sup_{n\ge0}\|g_n\|_s\le C\|g_0\|_s.$$

2.  For some $0<\rho<1$, all $1\le j\le n$ and $v\in\mathcal B_s$, $$\label{eq:sequential-remainder-contraction}
            |R_nR_{n-1}\cdots R_jv|_w
            \le C\min\bigl\{|v|_w,
                     \rho^{n-j+1}\|v\|_s\bigr\}.$$

3.  For the block parameters $\xi_n$ in a metric space, there is $0<\eta\le1$ such that $$\label{eq:projector-holder}
            |(\Pi_n-\Pi_{n-1})v|_w
            \le C\delta_n^\eta\|v\|_s,
            \qquad
            \delta_n=d(\xi_n,\xi_{n-1}),$$ while $\|\Pi_n-\Pi_{n-1}\|_{\mathcal B_s\to\mathcal B_s}$ is uniformly bounded.

The product estimate [\[eq:sequential-remainder-contraction\]](#eq:sequential-remainder-contraction){reference-type="eqref" reference="eq:sequential-remainder-contraction"} is a genuine cocycle hypothesis. It does not follow merely because each autonomous $Q_n$ has a spectral gap. In applications it must be proved from a matched inducing construction, a cone/minorization argument, or a sequential Lasota--Yorke and covering theorem.

[\[thm:rank-two-tracking\]]{#thm:rank-two-tracking label="thm:rank-two-tracking"} Under [\[ass:rank-two-gap\]](#ass:rank-two-gap){reference-type="ref" reference="ass:rank-two-gap"}, let $$g_n=Q_n\cdots Q_1g_0,
    \qquad z_n=(I-\Pi_n)g_n.$$ Then $$\label{eq:rank-two-tracking}
    |z_n|_w
    \le C\rho^n\|z_0\|_s
      +C\|g_0\|_s\sum_{j=1}^n
        \min\{\delta_j^\eta,\rho^{n-j+1}\}.$$ If, in addition, $$\label{eq:strong-projector-holder}
    \|(\Pi_n-\Pi_{n-1})v\|_s
    \le C\delta_n^\eta\|v\|_s,$$ then the sharper bound $$\label{eq:strong-rank-two-tracking}
    |z_n|_w
    \le C\rho^n\|z_0\|_s
      +C\|g_0\|_s\sum_{j=1}^n
        \rho^{n-j+1}\delta_j^\eta$$ holds.

Since $Q_n$ commutes with $\Pi_n$, $$\begin{aligned}
    z_n
    &=(I-\Pi_n)Q_ng_{n-1}\\
    &=R_nz_{n-1}
      +R_n(\Pi_{n-1}-\Pi_n)g_{n-1}.\end{aligned}$$ Iterating this identity gives the exact formula $$z_n=R_n\cdots R_1z_0
      +\sum_{j=1}^n R_n\cdots R_j
       (\Pi_{j-1}-\Pi_j)g_{j-1}.$$ The strong norms of the $g_{j-1}$ are uniformly bounded by (B1). For each summand, the first entry in the minimum in [\[eq:sequential-remainder-contraction\]](#eq:sequential-remainder-contraction){reference-type="eqref" reference="eq:sequential-remainder-contraction"}, together with [\[eq:projector-holder\]](#eq:projector-holder){reference-type="eqref" reference="eq:projector-holder"}, gives $C\delta_j^\eta\|g_0\|_s$; the second gives $C\rho^{n-j+1}\|g_0\|_s$ using the uniform strong projector bound. Taking the better of the two proves [\[eq:rank-two-tracking\]](#eq:rank-two-tracking){reference-type="eqref" reference="eq:rank-two-tracking"}. Under [\[eq:strong-projector-holder\]](#eq:strong-projector-holder){reference-type="eqref" reference="eq:strong-projector-holder"}, apply the exponentially contracting branch of [\[eq:sequential-remainder-contraction\]](#eq:sequential-remainder-contraction){reference-type="eqref" reference="eq:sequential-remainder-contraction"} directly to obtain $C\rho^{n-j+1}\delta_j^\eta\|g_0\|_s$, which proves [\[eq:strong-rank-two-tracking\]](#eq:strong-rank-two-tracking){reference-type="eqref" reference="eq:strong-rank-two-tracking"}.

## Logarithmic schedules

For the rest of this subsection, take the product metric $$d((a,b),(a',b'))=|a-a'|+|b-b'|.$$ Suppose the block parameter is $$\xi_n=(u_{2n-1},u_{2n})$$ and the schedule is genuinely specified by $$\label{eq:log-schedule}
    u_n=u_*-c\,[\log(n+n_0)]^{-\beta},
    \qquad \beta>0,\quad n_0>1.$$ The offset and the increment have different scales: $$\label{eq:offset-increment}
    |u_n-u_*|=O((\log n)^{-\beta}),
    \qquad
    |u_{n+1}-u_n|
    =O\!\left(\frac1{n(\log n)^{\beta+1}}\right).$$ An envelope bound $|u_n-u_*|\le C(\log n)^{-\beta}$ alone does not imply the increment estimate.

[\[cor:log-tracking\]]{#cor:log-tracking label="cor:log-tracking"} Define $$\operatorname{dist}_w(g,E)=\inf_{e\in E}|g-e|_w.$$ For the explicit schedule [\[eq:log-schedule\]](#eq:log-schedule){reference-type="eqref" reference="eq:log-schedule"}, $$\label{eq:weak-log-tracking}
    \operatorname{dist}_w(g_n,E_n)
    =O\!\left(
      n^{-\eta}(\log n)^{1-\eta(\beta+1)}
    \right)$$ under [\[eq:rank-two-tracking\]](#eq:rank-two-tracking){reference-type="eqref" reference="eq:rank-two-tracking"}. Under the strong estimate [\[eq:strong-rank-two-tracking\]](#eq:strong-rank-two-tracking){reference-type="eqref" reference="eq:strong-rank-two-tracking"}, $$\label{eq:strong-log-tracking}
    \operatorname{dist}_w(g_n,E_n)
    =O\!\left(
      n^{-\eta}(\log n)^{-\eta(\beta+1)}
    \right).$$ If, in addition, $$\|\Pi(\xi)-\Pi(\xi_*)\|_{s\to w}
    \le C d(\xi,\xi_*)^\eta,$$ where $\Pi_n=\Pi(\xi_n)$, $\Pi_*=\Pi(\xi_*)$, and $E_*=\operatorname{Ran}\Pi_*$, then $$\label{eq:limit-bundle-rate}
    \operatorname{dist}_w(g_n,E_*)
    =O((\log n)^{-\beta\eta}).$$

The mean-value theorem applied to [\[eq:log-schedule\]](#eq:log-schedule){reference-type="eqref" reference="eq:log-schedule"} gives $\delta_n=O(n^{-1}(\log n)^{-\beta-1})$. In [\[eq:rank-two-tracking\]](#eq:rank-two-tracking){reference-type="eqref" reference="eq:rank-two-tracking"}, split the sum at $n-L_n$ with $L_n$ proportional to $\log n$. The old terms are exponentially small, while the last $L_n$ terms are bounded by $L_n\delta_n^\eta$, giving [\[eq:weak-log-tracking\]](#eq:weak-log-tracking){reference-type="eqref" reference="eq:weak-log-tracking"}. A geometric convolution with a regularly varying sequence is of the order of its final term, proving [\[eq:strong-log-tracking\]](#eq:strong-log-tracking){reference-type="eqref" reference="eq:strong-log-tracking"}. Finally, $$\begin{aligned}
    \operatorname{dist}_w(g_n,E_*)
    &\le |(I-\Pi_*)g_n|_w\\
    &\le |(I-\Pi_n)g_n|_w
      +|(\Pi_n-\Pi_*)g_n|_w,\end{aligned}$$ and (B1) plus projector continuity gives the rate in [\[eq:limit-bundle-rate\]](#eq:limit-bundle-rate){reference-type="eqref" reference="eq:limit-bundle-rate"}.

The theorem deliberately stops at the rank-two bundle. The frozen restriction $\Pi_nQ_n|_{E_n}$ is not itself the non-autonomous internal cocycle. The relevant transport is $$\label{eq:internal-bundle-cocycle}
    B_n=\Pi_nQ_n\Pi_{n-1}|_{E_{n-1}}
    :E_{n-1}\longrightarrow E_n.$$ In moving frames $V_n:\mathbb C^2\to E_n$, one must analyze the products of $$M_n=V_n^{-1}\Pi_nQ_nV_{n-1}.$$ Only when the parity direction forms a covariant one-dimensional subbundle does this reduce to scalar multipliers $\zeta_n$; in that special case persistence may be governed by products $\prod_n\zeta_n$ and conditions such as summability of $1-|\zeta_n|$. In general the matrices need not commute. Operator convergence $Q_n\to Q_*$ does not decide the internal cocycle.

# A parity-preserving sequential Birkhoff theorem

We now give a clean situation in which the rank-two bundle has fixed phase coordinates and a full Birkhoff theorem follows. Let $X=X^0\sqcup X^1$ modulo the reference measure. Let $T_n:X\to X$ be nonsingular maps with transfer operators $P_n$, and put $$\Phi_n=T_n\circ\cdots\circ T_1,
    \qquad \Phi_0=\operatorname{id}.$$

[\[ass:block-memory\]]{#ass:block-memory label="ass:block-memory"} The following conditions hold.

1.  Every map swaps the phases: $$T_n(X^i)\subset X^{1-i}\quad\text{modulo }m,
            \qquad i\in\{0,1\}.$$ Hence $Q_n=P_{2n}P_{2n-1}$ preserves densities supported in each $X^i$.

2.  There are Banach spaces $\mathcal B_i$ of signed densities supported in $X^i$, continuously embedded in $L^1$, with $Q_n:\mathcal B_i\to\mathcal B_i$. For every allowed normalized initial density $g_{0,i}\in\mathcal B_i$, $$\label{eq:sequential-density-bound}
            \sup_{n\ge0}\|Q_n\cdots Q_1g_{0,i}\|_{\mathcal B_i}
            \le C\|g_{0,i}\|_{\mathcal B_i}.$$

3.  For every zero-mass $v\in\mathcal B_i$ and all $n\ge j$, $$\label{eq:block-memory-loss}
            \|Q_nQ_{n-1}\cdots Q_jv\|_1
            \le C\rho^{n-j+1}\|v\|_{\mathcal B_i},
            \qquad 0<\rho<1.$$

4.  The block observables used below satisfy $$\label{eq:block-multiplier-bound}
            \sup_n\|G_n\|_\infty\le\|\phi\|_\infty,
            \qquad
            \sup_n\|M_{G_n}\|_{\mathcal B_i\to\mathcal B_i}\le C_\phi,$$ where $M_{G_n}v=G_nv$.

5.  For each allowed initial density conditioned on phase $i$, and each observable $\phi$ under consideration, the conditional paired means $c_{n,i}$ defined in [\[eq:paired-means\]](#eq:paired-means){reference-type="eqref" reference="eq:paired-means"} converge to a common value $m_*(\phi)$, independent of $i$ and of that initial density.

Here is a concrete sufficient condition for the last clause. Let $g_{n-1,i}$ be the conditional density at the beginning of block $n$. Suppose there are limiting densities $h_*^0,h_*^1$ such that $$\label{eq:phase-density-convergence}
    \|g_{n-1,i}-h_*^i\|_1
    +\|P_{2n-1}g_{n-1,i}-h_*^{1-i}\|_1
    \longrightarrow0.$$ Then, for bounded $\phi$, transfer duality gives (S5) with $$\label{eq:limiting-paired-mean}
    m_*(\phi)
    =\frac12\left(
      \int_X\phi h_*^0\,dm+
      \int_X\phi h_*^1\,dm
    \right).$$

For $y$ at the beginning of block $n$, define $$\label{eq:paired-observable}
    G_n(y)=\frac12\left[
      \phi(T_{2n-1}y)
      +\phi(T_{2n}T_{2n-1}y)
    \right].$$ If $Y_{n-1}=\Phi_{2n-2}(x)$, then $$\label{eq:pairing-identity}
    \frac1{2M}\sum_{r=1}^{2M}\phi(\Phi_r(x))
    =\frac1M\sum_{n=1}^M G_n(Y_{n-1}).$$ For an initial law conditioned on phase $i$, let $$\label{eq:paired-means}
    c_{n,i}=\mathbb E_i[G_n(Y_{n-1})].$$ The dependence of $c_{n,i}$ on the fixed conditioned initial density is suppressed in the notation.

[\[thm:sequential-birkhoff\]]{#thm:sequential-birkhoff label="thm:sequential-birkhoff"} Under [\[ass:block-memory\]](#ass:block-memory){reference-type="ref" reference="ass:block-memory"}, for every allowed bounded observable $\phi$ and every initial probability density in $\mathcal B_0\oplus\mathcal B_1$, $$\label{eq:sequential-l2}
    \frac1N\sum_{r=1}^N\phi(\Phi_r)
    \longrightarrow m_*(\phi)$$ in $L^2(\nu_{g_0})$ and $\nu_{g_0}$-almost everywhere, where $d\nu_{g_0}=g_0\,dm$. Quantitatively, for even $N=2M$ and either initial phase, $$\label{eq:sequential-l2-bound}
    \left\|
      \frac1{2M}\sum_{r=1}^{2M}\phi(\Phi_r)-m_*(\phi)
    \right\|_{L^2}
    \le
    \frac{C_{\phi,g_0}}{\sqrt M}
    +\frac1M\sum_{n=1}^M|c_{n,i}-m_*(\phi)|.$$ If $|c_{n,i}-m_*(\phi)|=O((\log(n+1))^{-\kappa})$, then the deterministic bias in [\[eq:sequential-l2-bound\]](#eq:sequential-l2-bound){reference-type="eqref" reference="eq:sequential-l2-bound"} is $O((\log(M+1))^{-\kappa})$.

Condition on an initial phase $i$. Let $g_{m-1,i}$ be the density of $Y_{m-1}$ in that phase. The signed density $$v_{m,i}=(G_m-c_{m,i})g_{m-1,i}$$ has zero mass and uniformly bounded $\mathcal B_i$ norm by [\[eq:sequential-density-bound,eq:block-multiplier-bound\]](#eq:sequential-density-bound,eq:block-multiplier-bound){reference-type="ref" reference="eq:sequential-density-bound,eq:block-multiplier-bound"}. More explicitly, transfer duality gives $$\begin{aligned}
    &\operatorname{Cov}_i(G_m(Y_{m-1}),G_n(Y_{n-1}))\\
    &\quad=\int_X(G_n-c_{n,i})
      Q_{n-1}\cdots Q_m
      \bigl[(G_m-c_{m,i})g_{m-1,i}\bigr],dm.\end{aligned}$$ Thus [\[eq:block-memory-loss\]](#eq:block-memory-loss){reference-type="eqref" reference="eq:block-memory-loss"} gives, for $n>m$, $$\label{eq:paired-covariance}
    |\operatorname{Cov}_i(G_m(Y_{m-1}),G_n(Y_{n-1}))|
    \le C_{\phi,g_0}\rho^{n-m}.$$ Summing the diagonal terms and the geometric covariance tail yields $$\label{eq:paired-variance}
    \operatorname{Var}_i\left(
      \frac1M\sum_{n=1}^M G_n(Y_{n-1})
    \right)
    \le\frac{C_{\phi,g_0}}{M}.$$ The triangle inequality between the random average, its expectation, and $m_*(\phi)$ proves [\[eq:sequential-l2-bound\]](#eq:sequential-l2-bound){reference-type="eqref" reference="eq:sequential-l2-bound"}. Clause (S5) and Cesàro convergence prove the $L^2$ limit.

For almost-everywhere convergence, take $M_j=j^2$. Chebyshev's inequality, [\[eq:paired-variance\]](#eq:paired-variance){reference-type="eqref" reference="eq:paired-variance"}, and Borel--Cantelli show that the paired average minus its expectation converges to zero along $M_j$ almost surely. Since $M_{j+1}/M_j\to1$ and $G_n$ is uniformly bounded, the gaps between successive squares are filled by the standard interpolation estimate. The conditional expectations converge to $m_*(\phi)$, proving the full paired limit. The two initial phases cover a general density, and an unpaired final observation changes an odd-length average by $O_\phi(N^{-1})$.

If, beyond [\[ass:block-memory\]](#ass:block-memory){reference-type="ref" reference="ass:block-memory"}, the phase-coordinate analysis supplies the quantitative paired-mean estimate $$\label{eq:paired-mean-rate}
    |c_{n,i}-m_*(\phi)|
    =O((\log(n+1))^{-\beta\zeta}),
    \qquad \zeta>0,$$ so [\[eq:sequential-l2-bound\]](#eq:sequential-l2-bound){reference-type="eqref" reference="eq:sequential-l2-bound"} becomes $$\label{eq:log-birkhoff-rate}
    \left\|
      \frac1N\sum_{r=1}^N\phi(\Phi_r)-m_*(\phi)
    \right\|_{L^2}
    =O\!\left(N^{-1/2}+(\log N)^{-\beta\zeta}\right).$$ For any prescribed $\beta>0$, if the corresponding schedule satisfies [\[ass:block-memory\]](#ass:block-memory){reference-type="ref" reference="ass:block-memory"} and [\[eq:paired-mean-rate\]](#eq:paired-mean-rate){reference-type="eqref" reference="eq:paired-mean-rate"}, the argument gives almost-everywhere convergence; the probabilistic step itself imposes no threshold $\beta>1$. This is not an assertion that every logarithmic quadratic schedule satisfies those hypotheses. A threshold can arise from a weaker covariance estimate with a nonsummable drift error, but it is not caused by the parity mode itself.

# What is, and is not, proved for nearby quadratic schedules

At the constant schedule $u_n\equiv u_{\mathrm c}$, the phase swap (S1) and the common paired limit (S5) follow from the exact component interchange and mixing. If [\[ass:component-gap\]](#ass:component-gap){reference-type="ref" reference="ass:component-gap"} is realized on component Banach spaces stable under the multipliers in (S4), it also supplies (S2)--(S3) and the exponential covariance bound, so [\[thm:sequential-birkhoff\]](#thm:sequential-birkhoff){reference-type="ref" reference="thm:sequential-birkhoff"} applies. Independently, [\[prop:paired-autonomous\]](#prop:paired-autonomous){reference-type="ref" reference="prop:paired-autonomous"} gives the autonomous almost-everywhere Birkhoff limit without the component-gap assumption; its quantitative $O(N^{-1})$ variance estimate uses that assumption. For a nonconstant schedule in the quadratic family, parameter convergence by itself is insufficient. A concrete application of [\[thm:rank-two-tracking,thm:sequential-birkhoff\]](#thm:rank-two-tracking,thm:sequential-birkhoff){reference-type="ref" reference="thm:rank-two-tracking,thm:sequential-birkhoff"} requires all of the following.

1.  The actual parameters must lie in a common matched inducing or tower set with uniform expansion, distortion, and tail data. The existence of a positive-measure Benedicks--Carleson-type set accumulating at $u_{\mathrm c}$ does not imply that a prescribed sequence lies in it.

2.  Mixed blocks $P_bP_a$, not only autonomous squares $P_u^2$, must possess a uniformly isolated rank-two cluster. Keller--Liverani stability [@KellerLiverani1999] is a natural tool once the strong--weak estimates and branch matching have actually been established.

3.  Arbitrary products of the complementary block operators must satisfy [\[eq:sequential-remainder-contraction\]](#eq:sequential-remainder-contraction){reference-type="eqref" reference="eq:sequential-remainder-contraction"} or [\[eq:block-memory-loss\]](#eq:block-memory-loss){reference-type="eqref" reference="eq:block-memory-loss"}. Separate spectral gaps for each frozen block do not imply this cocycle estimate.

4.  A fixed or covariantly moving phase label must be constructed. For $u\ne u_{\mathrm c}$, the exact sets $C,H$ in [\[eq:cyclic-components\]](#eq:cyclic-components){reference-type="eqref" reference="eq:cyclic-components"} need not be swapped, and their boundaries may move or cease to define two invariant phases.

5.  The internal $2\times2$ bundle cocycle must be analyzed. If a covariant parity line exists, its scalar multiplier may persist or decay; in the general case the full matrix product controls the outcome.

These are substantive verification tasks. They are the hypotheses not captured by a one-mode raw estimate. The present results identify the required operator architecture and prove the conclusions once that architecture is available; they do not claim that every logarithmically cooled quadratic schedule satisfies it.

# Conclusion

The first quadratic band-merging parameter is a period-two, not a mixing, raw dynamical system. Unconditionally, its Koopman dynamics contain the parity eigenvalue $-1$, producing an atom at frequency $1/2$ for every observable with $a_\phi\ne0$, and in particular $\sigma_s=\delta_{1/2}$. Under the explicit two-step component spectral-gap hypothesis, the Perron--Frobenius decomposition contains exactly the two peripheral modes $1,-1$; after removing them, the remaining correlations decay exponentially and give an analytic absolutely continuous spectral density. For each fixed bounded real observable, finite orbit periodograms converge weakly to the observable spectral measure without requiring that gap.

The same observation clarifies the sequential logic. Consecutive iterates must be paired, or equivalently the cocycle must be studied through $Q_n=P_{2n}P_{2n-1}$. The two-step complement can mix while the rank-two projector bundle retains phase information. Under uniform block memory loss and the common paired-mean hypothesis, paired Birkhoff averages converge in $L^2$ and almost everywhere; under the moving-projector hypotheses, the adiabatic lag is controlled by adjacent parameter increments, while comparison with the limiting statistics is controlled by the larger parameter offset.

The main theoretical boundary is now explicit. The exact geometry, parity eigenmode, ergodicity, Birkhoff limit, and pathwise periodogram limit at $u_{\mathrm c}$ for each fixed bounded real observable are unconditional. Exponential operator-norm remainders require the stated component gap. A non-autonomous quadratic application further requires a verified matched tower, a rank-two block bundle, sequential complement contraction, and an analysis of the internal two-dimensional cocycle. Until those ingredients are supplied, a numerical cooling schedule cannot be promoted to an operator-spectral theorem merely because its parameters approach $u_{\mathrm c}$.

# Data and code availability {#data-and-code-availability .unnumbered}

All results are analytic and no numerical data are used. The manuscript source and verified PDF are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-3-parity-resolved-band-merging-spectrum>.

# Acknowledgements {#acknowledgements .unnumbered}

The author thanks colleagues whose comments motivated a separate treatment of the period-two mode. AI-assisted tools were used for auxiliary typesetting and proof auditing; all mathematical statements and conclusions are the responsibility of the author.

# Disclosure statement {#disclosure-statement .unnumbered}

The author reports no competing interests.
