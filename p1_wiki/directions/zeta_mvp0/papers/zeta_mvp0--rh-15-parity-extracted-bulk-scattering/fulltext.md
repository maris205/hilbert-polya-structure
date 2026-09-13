---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-15-parity-extracted-bulk-scattering"
canonical_tex: "zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/parity-extracted-bulk-scattering.pdf"
source_sha256: "b4e25d14c5ffa3d742a73eb18186b30fbd34526274890e834c6050859a046b13"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parity-Extracted Bulk Scattering at a Quadratic Band-Merging Map: Exact Endpoint Poles, Resonance-Cloud Necessity, and Geometric Finite-Section Scaling

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/parity-extracted-bulk-scattering.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the algebraic band-merging parameter of $f_u(x)=1-u x^2$, the zero-noise Perron operator has the peripheral pair $1,-1$. Gaussian noise moves the parity mode to a resonance $\lambda_-(\sigma)>-1$. After removing both peripheral factors, every fixed Taylor coefficient of the noisy Hilbert--Schmidt determinant has a deterministic limit. The unresolved question is whether these coefficients assemble into a genuine bulk determinant limit.

  We first identify the target exactly. Let $S=f^2$ on one mixing component, let $E_{1,n}$ be the even $\beta=1$ trace of its analytic circle lift, and put $a_n=\lambda^{-n}$, where $\lambda=2u_{\mathrm c}(u_{\mathrm c}-1)$. The physical flat trace, including the orbifold branch point, satisfies $$P_{2n}=2E_{1,n}
   -\frac{2a_n}{1+a_n}
   -\frac{a_n^2}{1-a_n^2}.$$ The validated reduced-sector bound $r_1<1/3$ therefore yields the sharp law $$P_{2n}=2-2\lambda^{-n}+\lambda^{-2n}+O(3^{-n}).$$ Exponentiating the exact trace identity gives a convergent endpoint $q$-product factorization of the parity-centered determinant: $$\boxed{
   \widehat D_{0,\mathrm{bulk},2}(z)
   =\frac{\mathcal G(z)}{1-z^2/\lambda}},
   \qquad
   \mathcal G(z)\ne0\quad(|z|<\lambda).$$ Thus $z=\pm\sqrt\lambda$ are genuine simple poles. In particular, the entire noisy bulk determinants cannot converge locally uniformly on any disk containing either pole. The negative leading moments also rule out every fixed finite-resonance realization of the deterministic edge: a growing resonance cloud is necessary.

  The canonical finite section of the pole is $$\Pi_N(q)=1+q+\cdots+q^N=\frac{1-q^{N+1}}{1-q},
   \qquad q=z^2/\lambda.$$ It has $2N$ reciprocal resonances at radius $\lambda^{-1/2}$ and phases $\pm k\pi/(N+1)$, and its radially scaled limit is $(e^s-1)/s$. Sparse Gaussian computations down to $\sigma=10^{-4}$ resolve an outer cloud of fourteen eigenvalues. Their phase root-mean-square error from the $N=7$ geometric grid is $0.01124$ radians, while their mean radius moves toward $\lambda^{-1/2}=0.7718445\ldots$. The radially centered cloud factor follows the finite geometric model. These spectral-cloud statements are floating-point evidence and motivate a precise scattering conjecture; the trace reconstruction, endpoint poles, normal-family obstruction, and finite-section model are analytic results.
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
  **Parity-Extracted Bulk Scattering**\
  **at a Quadratic Band-Merging Map:**\
  Exact Endpoint Poles, Resonance-Cloud Necessity,\
  and Geometric Finite-Section Scaling
```

## Markdown 正文

**Keywords:** transfer operator; regularized determinant; flat trace; resonance cloud; finite-section scattering; quadratic map; small noise; spectral condensation; boundary layer.

**MSC 2020:** 37E05; 37D25; 47A55; 47B10; 65P30.

# Introduction {#sec:introduction}

Small noise can approximate every fixed periodic coefficient and still fail to approximate the analytic object assembled from all periods. This is the central difficulty in taking a simultaneous small-noise/long-cycle limit. For the quadratic band-merging map, the difficulty is visible but unusually structured. Deterministic dynamics has two cyclic components, hence a parity eigenvalue $-1$. Positive Gaussian noise makes the Markov operator strongly mixing and turns that eigenvalue into a long-lived negative resonance.

The preceding sequence of papers separated the relevant mechanisms. Exact Markov counts and fixed-length Gaussian localization produced the physical flat traces and exposed a logarithmic localization horizon [@WangLongCycle2026]. Collet--Eckmann weighted-zeta theory proved an unconditional parity-centered trace gap [@WangFlatTrace2026]. An analytic circle lift then isolated the postcritical factors, and a validated Wiener--Taylor calculation proved their noncancellation [@WangPostcritical2026; @WangValidatedGap2026]. Finally, coupled critical-value boundary layers corrected the parity splitting to $$\label{eq:parity-law-intro}
 1+\lambda_-(\sigma)
 =C_*\sqrt\sigma+o(\sqrt\sigma).$$ This boundary-layer law was established in @WangBoundaryLayer2026.

After these steps, the finite-noise parity-extracted determinant has no remaining ambiguous peripheral factor. For each fixed $m\ge2$, its trace coefficient converges to the deterministic parity-centered flat trace. It is tempting to infer convergence of the whole determinant. The first result of this paper is that this temptation is only locally correct: the exact deterministic target is meromorphic, not entire, and its first singularities are two endpoint poles at $\pm\sqrt\lambda$.

The poles explain the numerical spectrum. A finite-noise determinant is entire, so it cannot converge normally through a deterministic pole. As the noise decreases, more bulk eigenvalues gather near the reciprocal circle $|\mu|=\lambda^{-1/2}$. Their phases are close to the roots-of-unity grid generated by a geometric polynomial. The cloud is therefore not an arbitrary collection of fitted eigenvalues: it survives a spatial-resolution audit and matches the only canonical finite section considered here. The claim that it is the actual finite-noise pole-resolution mechanism remains the scattering conjecture formulated below.

## Main results and status {#main-results-and-status .unnumbered}

1.  The physical component flat trace is reconstructed exactly from the even $\beta=1$ circle trace. This is a new Lefschetz/orbifold identity, distinct from the earlier Perron-weight identity.

2.  Combining that identity with the validated reduced-sector bound gives $$P_{2n}=2-2\lambda^{-n}+\lambda^{-2n}+O(3^{-n}).$$

3.  The full physical determinant factors into one reduced Fredholm determinant and three explicit endpoint $q$-products. After Perron/parity extraction, $$\widehat D_{0,\mathrm{bulk},2}(z)
      =\mathcal G(z)/(1-z^2/\lambda),
      \qquad \mathcal G\ne0\quad(|z|<\lambda).$$

4.  Coefficientwise noisy convergence is unconditional, but no locally uniform entire limit can cross $\pm\sqrt\lambda$. This is a normal-family obstruction, not a numerical inference.

5.  The negative leading even moments cannot arise from any fixed finite multiset of limiting resonances. A growing cloud or an infinite-dimensional spectral edge is mathematically necessary.

6.  The exact geometric pole section $\Pi_N$ has quantized reciprocal resonances and the scaled profile $(e^s-1)/s$. This is an analytic model theorem.

7.  Sparse computations with as many as $204800$ states identify the effective degrees $3,3,4,5,5,6,7$ as $\sigma$ decreases from $10^{-2}$ to $10^{-4}$. Agreement of the noisy cloud with the geometric model is an ordinary floating-point diagnostic. The asymptotic noisy scattering law is stated as a conjecture and route map.

# The deterministic and noisy objects {#sec:setup}

Let $u=u_{\mathrm c}$ be the root in $(1,2)$ of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and set $$\label{eq:constants}
 r=u_{\mathrm c}-1,
 \qquad
 \lambda=2u_{\mathrm c}r.$$ Then $$\label{eq:critical-orbit}
 0\longmapsto1\longmapsto-r\longmapsto r\longmapsto r,$$ and $$\label{eq:numerical-constants}
 \lambda=1.678573510428322\ldots,
 \quad
 \sqrt\lambda=1.295597742522085\ldots,
 \quad
 \lambda^{-1/2}=0.771844506346038\ldots.$$

Write $f(x)=1-u_{\mathrm c}x^2$. Every periodic point is repelling. Its physical flat trace is $$\label{eq:physical-trace}
 P_m=\sum_{f^mp=p}\frac1{|1-(f^m)'(p)|}.$$ The deterministic parity-centered coefficients are $$\label{eq:centered-coefficients}
 c_m=P_m-1-(-1)^m.$$ They define the second-regularized bulk germ $$\label{eq:deterministic-bulk}
 \widehat D_{0,\mathrm{bulk},2}(z)
 =\exp\left[-\sum_{m\ge2}\frac{c_mz^m}{m}\right].$$

For $\sigma>0$, let $\mathcal K_\sigma$ be the row-normalized Gaussian Markov operator on $[-1,1]$. It is Hilbert--Schmidt, with simple Perron root one and simple real parity resonance $\lambda_-(\sigma)$. Removing those two eigenvalues from its second regularized determinant gives $$\begin{aligned}
 D_{\sigma,\mathrm{bulk},2}(z)
 &=\prod_{\mu\in\operatorname{spec}_{\mathrm{bulk}}(\mathcal K_\sigma)}
 (1-z\mu)e^{z\mu}
 \label{eq:noisy-product}\\
 &=\exp\left[-\sum_{m\ge2}\frac{c_{\sigma,m}z^m}{m}\right],
 \qquad
 c_{\sigma,m}=\operatorname{tr}\mathcal K_\sigma^m-1-\lambda_-(\sigma)^m.
 \label{eq:noisy-traces}\end{aligned}$$ For each fixed noise this is entire [@Simon2005].

## The circle-lift input

Let $S=f^2$ on the central component $[-r,r]$. The cosine cover $$\label{eq:cosine-cover}
 \pi(\theta)=-r\cos\theta$$ semiconjugates $S$ to an analytic expanding degree-two circle map $F$. Let $E_{1,n}$ denote the flat trace of the even deck sector of the analytic transfer operator with weight $(F')^{-1}$, and let $D_{1,+}$ be its Fredholm determinant. The Perron eigenvalue gives $$\label{eq:perron-deflation}
 D_{1,+}(w)=(1-w)\widetilde D_{1,+}(w),
 \qquad
 E_{1,n}=1+\operatorname{tr}(\mathcal T_{1,0}^n).$$

The validated result of @WangValidatedGap2026 is $$\label{eq:validated-radius}
 r(\mathcal T_{1,0})
 \le0.329642076293171<\frac13,$$ and $\widetilde D_{1,+}$ is zero-free for $$\label{eq:certified-disk}
 |w|<R_{\mathrm{cert}}=3.0335933180\ldots>\lambda^2.$$ This is a computer-assisted theorem based on directed Arb arithmetic. We use it as a proved input; no new interval calculation is claimed here.

# Exact reconstruction of the physical flat trace {#sec:trace-reconstruction}

Define the physical component trace $$\label{eq:component-physical}
 p_n=\sum_{S^nx=x}\frac1{|1-(S^n)'(x)|}.$$ The distinction between $p_n$ and the Perron-weight trace is concentrated at the fixed-point denominator and at the branch endpoint $r$.

[\[thm:physical-reconstruction\]]{#thm:physical-reconstruction label="thm:physical-reconstruction"} For every $n\ge1$, with $a_n=\lambda^{-n}$, $$\label{eq:component-reconstruction}
 \boxed{
 p_n=E_{1,n}-\frac{a_n}{1+a_n}.}$$ Consequently the full-map traces are $$\begin{aligned}
 P_{2n}
 &=2E_{1,n}
 -\frac{2a_n}{1+a_n}
 -\frac{a_n^2}{1-a_n^2},
 \label{eq:even-reconstruction}\\
 P_{2n+1}
 &=\frac{\lambda^{-(2n+1)}}{1+\lambda^{-(2n+1)}}.
 \label{eq:odd-reconstruction}\end{aligned}$$

Let $x\ne r$ be fixed by $S^n$, and let its two circle lifts be $\theta,-\theta$. Put $a=D_n(\theta)^{-1}$, where $D_n=(F^n)'$. If $F^n\theta=\theta$, both lifts occur in the ordinary fixed set. Their combined contribution to the even $\beta=1$ sector is $$\frac12\left(\frac a{1-a}+\frac a{1-a}\right)
 =\frac1{D_n-1}.$$ The interval multiplier is positive and equals $D_n$, so this is exactly the physical contribution in [\[eq:component-physical\]](#eq:component-physical){reference-type="eqref" reference="eq:component-physical"}.

If $F^n\theta=-\theta$, both lifts occur in the deck-twisted fixed set. Their even-sector contribution is $$\frac12\left(\frac a{1+a}+\frac a{1+a}\right)
 =\frac1{D_n+1}.$$ The interval multiplier is now $-D_n$, and this again equals $|1-(S^n)'(x)|^{-1}$.

Only the branch point differs. The lift $\theta=\pi$ belongs to both fixed sets and has inverse multiplier $a_n=\lambda^{-n}$. Its even circle contribution is $$\label{eq:circle-branch}
 \frac12\left(\frac{a_n}{1-a_n}+\frac{a_n}{1+a_n}\right)
 =\frac{a_n}{1-a_n^2}.$$ The interval multiplier of $S^n$ at $r$ is $\lambda^{2n}$, so the required physical contribution is $$\label{eq:interval-branch}
 \frac{a_n^2}{1-a_n^2}.$$ Subtracting [\[eq:circle-branch\]](#eq:circle-branch){reference-type="eqref" reference="eq:circle-branch"} and adding [\[eq:interval-branch\]](#eq:interval-branch){reference-type="eqref" reference="eq:interval-branch"} changes the trace by $-a_n/(1+a_n)$, proving [\[eq:component-reconstruction\]](#eq:component-reconstruction){reference-type="eqref" reference="eq:component-reconstruction"}.

The map $f$ bijects the two component fixed sets and preserves their cyclic multipliers. Their only common point is $r$. Hence $P_{2n}=2p_n$ minus one copy of [\[eq:interval-branch\]](#eq:interval-branch){reference-type="eqref" reference="eq:interval-branch"}, which gives [\[eq:even-reconstruction\]](#eq:even-reconstruction){reference-type="eqref" reference="eq:even-reconstruction"}. An odd iterate fixes only $r$; since $f'(r)=-\lambda$, its contribution is [\[eq:odd-reconstruction\]](#eq:odd-reconstruction){reference-type="eqref" reference="eq:odd-reconstruction"}.

The earlier postcritical identity reconstructed the Perron weight $|(S^n)'|^{-1}$ by a cancellation between the even $\beta=1$ and odd $\beta=2$ sectors. Here the fixed-point denominator is retained, so the even $\beta=1$ sector alone supplies every nonbranch physical contribution. The two formulas solve different trace problems.

# Sharp physical coefficients {#sec:sharp-coefficients}

The exact endpoint fractions now turn the certified circle-sector gap into a sharp physical asymptotic.

[\[thm:sharp-physical\]]{#thm:sharp-physical label="thm:sharp-physical"} As $n\to\infty$, $$\label{eq:sharp-even}
 \boxed{
 P_{2n}
 =2-2\lambda^{-n}+\lambda^{-2n}+O(3^{-n}).}$$ The odd trace is exactly [\[eq:odd-reconstruction\]](#eq:odd-reconstruction){reference-type="eqref" reference="eq:odd-reconstruction"}. Therefore $$\label{eq:centered-root-rate}
 \lim_{n\to\infty}
 \frac{c_{2n}}{\lambda^{-n}}=-2,
 \qquad
 \limsup_{m\to\infty}|c_m|^{1/m}=\lambda^{-1/2}.$$

Nuclearity and [\[eq:validated-radius\]](#eq:validated-radius){reference-type="eqref" reference="eq:validated-radius"} give $$\label{eq:E-one-decay}
 E_{1,n}=1+O(3^{-n}).$$ Expand the two explicit terms in [\[eq:even-reconstruction\]](#eq:even-reconstruction){reference-type="eqref" reference="eq:even-reconstruction"}: $$\begin{aligned}
 -\frac{2a_n}{1+a_n}
 &=-2a_n+2a_n^2+O(a_n^3),\\
 -\frac{a_n^2}{1-a_n^2}
 &=-a_n^2+O(a_n^4).\end{aligned}$$ Since $\lambda^{-3}<1/3$, substitution proves [\[eq:sharp-even\]](#eq:sharp-even){reference-type="eqref" reference="eq:sharp-even"}. Dividing by $\lambda^{-n}$ gives the first limit in [\[eq:centered-root-rate\]](#eq:centered-root-rate){reference-type="eqref" reference="eq:centered-root-rate"}. The even subsequence then has root rate $\lambda^{-1/2}$, while [\[eq:odd-reconstruction\]](#eq:odd-reconstruction){reference-type="eqref" reference="eq:odd-reconstruction"} has the smaller rate $\lambda^{-1}$.

The leading negative sign is decisive. It will force a cloud rather than a finite set of limiting resonances.

# Endpoint products and the first bulk poles {#sec:factorization}

Set $$\label{eq:b-d-definitions}
 b_n=\frac{\lambda^{-n}}{1+\lambda^{-n}},
 \qquad
 d_n=\frac{\lambda^{-2n}}{1-\lambda^{-2n}}.$$ Define three endpoint factors as analytic germs at zero: $$\begin{aligned}
 \mathcal A(w)
 &=\exp\left(\sum_{n\ge1}\frac{b_nw^n}{n}\right),
 \label{eq:A-definition}\\
 \mathcal B(w)
 &=\exp\left(\frac12\sum_{n\ge1}\frac{d_nw^n}{n}\right),
 \label{eq:B-definition}\\
 \mathcal C(z)
 &=\exp\left(-\sum_{\substack{m\ge1\\m\ \mathrm{odd}}}
 \frac{b_mz^m}{m}\right).
 \label{eq:C-definition}\end{aligned}$$ Geometric expansion of $b_n$ and $d_n$ gives the convergent products $$\begin{aligned}
 \mathcal A(w)
 &=\prod_{k\ge1}(1-w/\lambda^k)^{(-1)^k},
 \label{eq:A-product}\\
 \mathcal B(w)
 &=\prod_{k\ge1}(1-w/\lambda^{2k})^{-1/2},
 \label{eq:B-product}\\
 \mathcal C(z)
 &=\prod_{k\ge1}
 \left(\frac{1-z/\lambda^k}{1+z/\lambda^k}\right)^{(-1)^{k-1}/2}.
 \label{eq:C-product}\end{aligned}$$ Fractional powers denote the branches equal to one at the origin.

Let $$\label{eq:raw-flat-determinant}
 D_f(z)=\exp\left[-\sum_{m\ge1}\frac{P_mz^m}{m}\right]$$ be the physical flat determinant germ.

[\[thm:physical-factorization\]]{#thm:physical-factorization label="thm:physical-factorization"} As analytic germs, and hence throughout their common continuation, $$\label{eq:raw-factorization}
 \boxed{
 D_f(z)
 =D_{1,+}(z^2)\mathcal A(z^2)\mathcal B(z^2)\mathcal C(z).}$$ Consequently $$\label{eq:bulk-full-factorization}
 \boxed{
 \widehat D_{0,\mathrm{bulk},2}(z)
 =e^{P_1z}\widetilde D_{1,+}(z^2)
 \mathcal A(z^2)\mathcal B(z^2)\mathcal C(z).}$$

By [\[eq:component-reconstruction\]](#eq:component-reconstruction){reference-type="eqref" reference="eq:component-reconstruction"}, the component physical determinant is $$\label{eq:component-determinant}
 \exp\left[-\sum_{n\ge1}\frac{p_nw^n}{n}\right]
 =D_{1,+}(w)\mathcal A(w).$$ In the full map, two component copies contribute at every even length, while the common branch point is removed once. Therefore the even part of $\log D_f$ is the logarithm of [\[eq:component-determinant\]](#eq:component-determinant){reference-type="eqref" reference="eq:component-determinant"} at $w=z^2$ plus $\tfrac12\sum d_nz^{2n}/n$, which gives $\mathcal B(z^2)$. The exact odd trace [\[eq:odd-reconstruction\]](#eq:odd-reconstruction){reference-type="eqref" reference="eq:odd-reconstruction"} gives $\mathcal C(z)$. This proves [\[eq:raw-factorization\]](#eq:raw-factorization){reference-type="eqref" reference="eq:raw-factorization"}.

The parity baseline exponentiates to $1-z^2$, while the regularized bulk series omits the linear term $P_1z$. Hence $$\label{eq:bulk-vs-raw}
 \widehat D_{0,\mathrm{bulk},2}(z)
 =e^{P_1z}\frac{D_f(z)}{1-z^2}.$$ Insert [\[eq:perron-deflation\]](#eq:perron-deflation){reference-type="eqref" reference="eq:perron-deflation"} and [\[eq:raw-factorization\]](#eq:raw-factorization){reference-type="eqref" reference="eq:raw-factorization"} to obtain [\[eq:bulk-full-factorization\]](#eq:bulk-full-factorization){reference-type="eqref" reference="eq:bulk-full-factorization"}.

The first factor of [\[eq:A-product\]](#eq:A-product){reference-type="eqref" reference="eq:A-product"} is a denominator. Write $$\label{eq:A-deflated}
 \mathcal A(w)=\frac{\mathcal A_*(w)}{1-w/\lambda},
 \qquad
 \mathcal A_*(w)=\prod_{k\ge2}(1-w/\lambda^k)^{(-1)^k}.$$

[\[thm:bulk-poles\]]{#thm:bulk-poles label="thm:bulk-poles"} There is a function $\mathcal G$, holomorphic and nonzero on $|z|<\lambda$, such that $$\label{eq:pole-factorization}
 \boxed{
 \widehat D_{0,\mathrm{bulk},2}(z)
 =\frac{\mathcal G(z)}{1-z^2/\lambda}.}$$ In particular, $z=\pm\sqrt\lambda$ are actual simple poles, and the Taylor series in [\[eq:deterministic-bulk\]](#eq:deterministic-bulk){reference-type="eqref" reference="eq:deterministic-bulk"} has exact radius $\sqrt\lambda$.

Set $$\label{eq:G-definition}
 \mathcal G(z)=e^{P_1z}\widetilde D_{1,+}(z^2)
 \mathcal A_*(z^2)\mathcal B(z^2)\mathcal C(z).$$ By [\[eq:certified-disk\]](#eq:certified-disk){reference-type="eqref" reference="eq:certified-disk"}, the reduced Fredholm determinant is nonzero for $|z|<\lambda$. In that disk, the next factor of $\mathcal A_*$ can vanish only at $z^2=\lambda^2$, while the first singularities of $\mathcal B(z^2)$ and $\mathcal C(z)$ also lie on $|z|=\lambda$. Their defining exponential series show that all three endpoint factors are holomorphic and nonzero in the open disk. Equation [\[eq:pole-factorization\]](#eq:pole-factorization){reference-type="eqref" reference="eq:pole-factorization"} follows from [\[eq:bulk-full-factorization\]](#eq:bulk-full-factorization){reference-type="eqref" reference="eq:bulk-full-factorization"} and [\[eq:A-deflated\]](#eq:A-deflated){reference-type="eqref" reference="eq:A-deflated"}. Nonvanishing of $\mathcal G$ prevents cancellation. The exact Taylor radius also follows from the poles, consistently with [\[eq:centered-root-rate\]](#eq:centered-root-rate){reference-type="eqref" reference="eq:centered-root-rate"}.

# What noisy convergence can and cannot mean {#sec:noisy-obstruction}

The square-root parity law [\[eq:parity-law-intro\]](#eq:parity-law-intro){reference-type="eqref" reference="eq:parity-law-intro"} completes the coefficientwise bridge left conditional in the long-cycle paper.

[\[prop:coefficient-bridge\]]{#prop:coefficient-bridge label="prop:coefficient-bridge"} For every fixed $m\ge2$, $$\label{eq:coefficient-bridge}
 c_{\sigma,m}\longrightarrow c_m
 \qquad(\sigma\downarrow0).$$ Consequently every fixed Taylor coefficient of $D_{\sigma,\mathrm{bulk},2}$ converges to the corresponding coefficient of $\widehat D_{0,\mathrm{bulk},2}$.

Fixed-length Gaussian localization gives $\operatorname{tr}\mathcal K_\sigma^m\to P_m$ [@WangLongCycle2026]. Equation [\[eq:parity-law-intro\]](#eq:parity-law-intro){reference-type="eqref" reference="eq:parity-law-intro"} gives $\lambda_-(\sigma)^m\to(-1)^m$. Insert both limits in [\[eq:noisy-traces\]](#eq:noisy-traces){reference-type="eqref" reference="eq:noisy-traces"}. A Taylor coefficient of fixed degree depends on only finitely many trace coefficients.

Coefficient convergence determines a unique germ but does not give a normal family through the poles.

[\[thm:normal-obstruction\]]{#thm:normal-obstruction label="thm:normal-obstruction"} Let $R>\sqrt\lambda$. No sequence $\sigma_j\downarrow0$ can make $D_{\sigma_j,\mathrm{bulk},2}$ converge locally uniformly to a finite holomorphic function on $|z|<R$. In fact, for every $\sigma_0>0$, the family $\{D_{\sigma,\mathrm{bulk},2}:0<\sigma<\sigma_0\}$ is not locally bounded on that disk.

If a locally uniform limit $D$ existed, convergence of derivatives at zero and [\[prop:coefficient-bridge\]](#prop:coefficient-bridge){reference-type="ref" reference="prop:coefficient-bridge"} would make its Taylor germ equal to $\widehat D_{0,\mathrm{bulk},2}$. The identity theorem would then give $D=\widehat D_{0,\mathrm{bulk},2}$ throughout the punctured disk obtained by removing $\pm\sqrt\lambda$. But $D$ is bounded near each of those two points, whereas [\[thm:bulk-poles\]](#thm:bulk-poles){reference-type="ref" reference="thm:bulk-poles"} makes the right-hand side unbounded along the punctured neighborhood. If the stated small-noise family were locally bounded, Montel's theorem applied to any sequence $\sigma_j\downarrow0$ would provide such a locally convergent subsequence [@Conway1978], giving the same contradiction.

Thus the deterministic target is unique inside its Taylor disk, but an unrenormalized entire limit across the first spectral edge is ruled out. This is the precise negative answer to the naive version of the question posed at the end of the boundary-layer analysis.

## Why finitely many resonances cannot repair the pole

Put $$\label{eq:threshold-alpha}
 \alpha=\lambda^{-1/2}.$$

[\[prop:finite-no-go\]]{#prop:finite-no-go label="prop:finite-no-go"} There is no finite multiset $\{\mu_1,\ldots,\mu_M\}$ with $|\mu_j|\le\alpha$ such that $$\label{eq:finite-model}
 c_m=\sum_{j=1}^M\mu_j^m+o(\alpha^m)
 \qquad(m\to\infty).$$

Apply [\[eq:finite-model\]](#eq:finite-model){reference-type="eqref" reference="eq:finite-model"} to $m=2n$ and divide by $\alpha^{2n}=\lambda^{-n}$. Terms with $|\mu_j|<\alpha$ vanish. For the remaining terms put $\zeta_j=(\mu_j/\alpha)^2$, so $|\zeta_j|=1$. By [\[eq:centered-root-rate\]](#eq:centered-root-rate){reference-type="eqref" reference="eq:centered-root-rate"}, $$\label{eq:unit-moment-contradiction}
 \sum_{|\mu_j|=\alpha}\zeta_j^n\longrightarrow-2.$$ Take Cesàro means in $n$. Each unit complex number contributes zero unless $\zeta_j=1$, in which case it contributes one. The left mean therefore converges to a nonnegative integer, whereas the right mean converges to $-2$. This contradiction proves the claim.

The sign in the sharp trace law therefore forces an increasing number of edge resonances, a noncompact limiting spectral measure, or an equivalent scattering description. Convergence of a fixed finite list of eigenvalues is structurally incapable of producing the deterministic pole.

# The canonical geometric scattering model {#sec:geometric-model}

The degree-$N$ Taylor section of the pole germ is the geometric polynomial $$\label{eq:geometric-section}
 \Pi_N(q)=1+q+\cdots+q^N
 =\frac{1-q^{N+1}}{1-q},
 \qquad q=\frac{z^2}{\lambda}.$$

[\[thm:geometric-resolution\]]{#thm:geometric-resolution label="thm:geometric-resolution"} The zeros of $\Pi_N(z^2/\lambda)$ are the reciprocals of the $2N$-point cloud $$\label{eq:ideal-cloud}
 \mu_{N,k}^{\pm}
 =\lambda^{-1/2}
 \exp\left(\pm\frac{ik\pi}{N+1}\right),
 \qquad 1\le k\le N.$$ This cloud has zero first moment and its second-regularized determinant is exactly the finite section: $$\label{eq:geometric-det-two}
 \sum_{k=1}^N\bigl(\mu_{N,k}^++\mu_{N,k}^-\bigr)=0,
 \qquad
 \prod_{k=1}^N\prod_{\epsilon\in\{+,-\}}
 (1-z\mu_{N,k}^{\epsilon})e^{z\mu_{N,k}^{\epsilon}}
 =\Pi_N(z^2/\lambda).$$ Moreover, for every fixed $s\in\mathbb C$, $$\label{eq:scattering-limit}
 \frac1{N+1}\Pi_N\!\left(e^{s/(N+1)}\right)
 \longrightarrow
 \mathcal S(s):=\frac{e^s-1}{s},$$ with the removable value $\mathcal S(0)=1$. The convergence is locally uniform in $s$.

The nontrivial $(N+1)$st roots of unity are $e^{2\pi ik/(N+1)}$, $1\le k\le N$. Taking both square roots and then reciprocals gives [\[eq:ideal-cloud\]](#eq:ideal-cloud){reference-type="eqref" reference="eq:ideal-cloud"}. The polynomial formed from these reciprocal roots has constant term one and the same degree and zeros as $\Pi_N(z^2/\lambda)$, so the ordinary product equals $\Pi_N$. Because that polynomial is even, its linear coefficient, which is the negative first moment of the cloud, vanishes. The exponential regularizers therefore multiply to one, proving [\[eq:geometric-det-two\]](#eq:geometric-det-two){reference-type="eqref" reference="eq:geometric-det-two"}. For the scaling law, insert $q=e^{s/(N+1)}$ in [\[eq:geometric-section\]](#eq:geometric-section){reference-type="eqref" reference="eq:geometric-section"}: $$\frac1{N+1}\Pi_N(q)
 =\frac{e^s-1}{(N+1)(e^{s/(N+1)}-1)}.$$ The denominator tends to $s$ locally uniformly, proving [\[eq:scattering-limit\]](#eq:scattering-limit){reference-type="eqref" reference="eq:scattering-limit"}.

The phase spacing in [\[eq:ideal-cloud\]](#eq:ideal-cloud){reference-type="eqref" reference="eq:ideal-cloud"} is not fitted. It is forced by the canonical entire resolution of one simple pole. The only model parameters left for a noisy cloud are its effective degree and its radial center.

[\[conj:noisy-scattering\]]{#conj:noisy-scattering label="conj:noisy-scattering"} There are integers $N_\sigma\to\infty$ and radii $r_\sigma\to\lambda^{-1/2}$, together with errors $\varepsilon_{\sigma,k}$ satisfying $$\max_{1\le k\le N_\sigma}|\varepsilon_{\sigma,k}|\longrightarrow0,$$ such that the outer parity-extracted Gaussian resonances can be labeled $$\label{eq:noisy-cloud-conjecture}
 \mu_{\sigma,k}^{\pm}
 =r_\sigma
 \exp\left[
 \pm i\left(\frac{k\pi}{N_\sigma+1}+\varepsilon_{\sigma,k}\right)
 \right],
 \quad 1\le k\le N_\sigma,$$ with $$\label{eq:degree-conjecture}
 N_\sigma
 =\frac{\log(1/\sigma)}{2\log\lambda}+O(1).$$ If $C_\sigma(z)$ is the second-regularized product over this cloud, then $$\label{eq:noisy-scattering-conjecture}
 \frac{C_\sigma\!\left(
 r_\sigma^{-1}e^{s/[2(N_\sigma+1)]}\right)}
 {C_\sigma(r_\sigma^{-1})}
 \longrightarrow\frac{e^s-1}{s}$$ locally uniformly in $s$. After division by $C_\sigma$, the remaining determinants form a normal family and continue the nonzero factor $\mathcal G$.

Only [\[thm:geometric-resolution\]](#thm:geometric-resolution){reference-type="ref" reference="thm:geometric-resolution"} is a theorem here. The three clauses of [\[conj:noisy-scattering\]](#conj:noisy-scattering){reference-type="ref" reference="conj:noisy-scattering"}---cloud quantization, logarithmic effective degree, and residual normality---are kept explicitly outside the theorem layer.

# Sparse resonance-cloud audit {#sec:numerics}

The numerical work tests the geometric mechanism independently of the deterministic derivation. Folding by $x\mapsto|x|$, midpoint nodes $x_i=(i+1/2)/d$ give row weights $$\label{eq:matrix-weights}
 K_{ij}\propto
 \exp\left[-\frac{(x_j-f(x_i))^2}{2\sigma^2}\right]
 +
 \exp\left[-\frac{(-x_j-f(x_i))^2}{2\sigma^2}\right].$$ Destinations beyond eight standard deviations are omitted and every retained row is normalized exactly. We keep $d\sigma\simeq20.48$ and use ARPACK to resolve the 80 largest-modulus eigenvalues. NumPy, SciPy, and Matplotlib provide the implementation [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007].

At each noise level, the Perron and parity modes are removed first. Among positive-imaginary bulk eigenvalues, the outer cloud is selected at the largest of the first twelve successive radial gaps (hence using at most the first thirteen candidates). This determines $N_\sigma$ before any comparison with the expected phases $k\pi/(N_\sigma+1)$.

## Cloud growth and quantization

gives the main diagnostics. The phase error is $$\label{eq:phase-rms}
 \left[
 \frac1{N_\sigma}\sum_{k=1}^{N_\sigma}
 \left(arg\mu_{\sigma,k}
 -\frac{k\pi}{N_\sigma+1}\right)^2
 \right]^{1/2}.$$

::: {#tab:cloud}
            $\sigma$      $d$   $N_\sigma$   cloud size   mean radius   phase RMS
  ------------------ -------- ------------ ------------ ------------- -----------
           $10^{-2}$     2048            3            6      0.607841     0.07933
    $4\times10^{-3}$     5120            3            6      0.670849     0.07773
    $2\times10^{-3}$    10240            4            8      0.705958     0.02431
           $10^{-3}$    20480            5           10      0.696908     0.02184
    $5\times10^{-4}$    40960            5           10      0.708586     0.04522
    $2\times10^{-4}$   102400            6           12      0.724468     0.02636
           $10^{-4}$   204800            7           14      0.730269     0.01124

  : Automatically selected outer resonance clouds. The threshold radius is $\lambda^{-1/2}=0.7718445063\ldots$.
:::

At the smallest noise the expected positive phases are $k\pi/8$, $1\le k\le7$. The observed values differ by only $0.01124$ radians in root-mean-square. The largest bulk modulus is $0.7570231$, and the mean radius remains below the threshold. Thus phase quantization is already sharper than radial convergence.

![Exact target and noisy pole resolution. Top left: the physical centered trace and its two endpoint terms; the remaining reduced-sector contribution decays faster. Top right: the deterministic bulk determinant diverges at $\sqrt\lambda$, while the pole-removed factor stays regular. Bottom left: noisy bulk spectra after Perron/parity extraction; open circles mark the selected clouds and crosses mark the $N=7$ geometric phases. Bottom right: the effective degree grows on the half-logarithmic localization scale.](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/figures/exact_pole_resonance_cloud.pdf>){#fig:pole-cloud width="\\textwidth"}

The tested cloud is stable under spatial refinement. At $\sigma=0.001$, changing $d\sigma$ from $10.24$ to $30.72$ leaves $N_\sigma=5$ at every resolution. The mean-radius spread is $1.87\times10^{-5}$, and the bulk-radius spread is $1.50\times10^{-5}$.

## Radially centered scattering

Let $\bar r_\sigma$ be the mean selected radius and let $C_\sigma$ be the product over the selected conjugate cloud. We evaluate the ratio in [\[eq:noisy-scattering-conjecture\]](#eq:noisy-scattering-conjecture){reference-type="eqref" reference="eq:noisy-scattering-conjecture"} at $s=-2,-1,-1/2,0,1/2,1,2$. Radial centering is essential: at finite noise the cloud lies inside its limiting circle, so centering directly at $\sqrt\lambda$ mixes radial drift with phase scattering.

![Radially centered outer-cloud products. Solid curves are the noisy clouds, color-matched dotted curves are the exact finite geometric sections, and the dashed curve is their $N\to\infty$ limit $(e^s-1)/s$. The approach to the universal curve is limited primarily by the small effective degrees.](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/figures/geometric_scattering_collapse.pdf>){#fig:scattering width="82%"}

For $\sigma=10^{-4}$, the maximum discrepancy from the exact $N=7$ finite section is $0.0198$ on $|s|\le1$ and $0.0761$ on $|s|\le2$. This comparison uses no phase or amplitude regression after the radial mean and the automatically selected integer $N_\sigma$ are fixed.

## Approach inside the pole

For determinant values, conjugate-complete ARPACK eigenpairs are multiplied and the exactly computable second trace supplies a residual $m=2$ correction. The deterministic comparison curve comes from [\[eq:bulk-full-factorization\]](#eq:bulk-full-factorization){reference-type="eqref" reference="eq:bulk-full-factorization"}, not a periodic truncation.

![Noisy bulk determinant diagnostics at fixed real targets. Dashed horizontal lines are the exact deterministic factorization. Convergence is clear well inside the pole and slows sharply as $z$ approaches $\sqrt\lambda=1.2956\ldots$.](<../../../../../zeta_mvp0/papers/RH-15-parity-extracted-bulk-scattering/figures/bulk_determinant_pole_approach.pdf>){#fig:determinant-convergence width="82%"}

At $\sigma=10^{-4}$ the absolute discrepancies are $2.49\times10^{-4}$ at $z=0.5$, $4.85\times10^{-3}$ at $z=0.9$, and $1.08$ at $z=1.2$. The last value is not evidence against coefficient convergence; it is the expected nonuniformity near a pole whose effective section has degree only seven.

## Numerical status

All eigenvalues, cloud selections, phase errors, determinant values, resolution checks, software versions, and source hashes are archived. The test suite checks the exact branch correction, reconstruction against the independent physical periodic data, the reduced circle traces, geometric zeros, scattering profile, synthetic cloud selection, row stochasticity, and pole removal.

The sparse eigenvalues are ordinary double-precision calculations. ARPACK values near the 80-eigenvalue cutoff may omit one member of a nearly degenerate pair; determinant diagnostics therefore retain only complete conjugate pairs and correct the exact second trace. The outer cloud is far above that cutoff and is stable under spatial refinement. None of these computations is presented as interval validation.

# A proof route for noisy bulk scattering {#sec:route-map}

The exact pole theorem narrows the remaining analysis to three operator estimates. Together they form a concrete route to [\[conj:noisy-scattering\]](#conj:noisy-scattering){reference-type="ref" reference="conj:noisy-scattering"}.

#### 1. Effective-rank control.

The distinguished deterministic orbit approaches the state boundary at distance $\asymp\lambda^{-m}$. For the two-step component time $n=m/2$, the equality $\lambda^{-2n}\asymp\sigma$ gives $$\label{eq:rank-clock}
 n\sim\frac{\log(1/\sigma)}{2\log\lambda}.$$ A proof must turn this geometric horizon into upper and lower bounds $N_\sigma=\log(1/\sigma)/(2\log\lambda)+O(1)$ for the dimension of the endpoint transfer block. This is a singular-value or approximation-number problem, not another parity-eigenvalue calculation.

#### 2. Shift-block reduction.

After the two RH-14 boundary layers are extracted, the endpoint block should be reduced by a Feshbach or Grushin map to a finite unilateral shift plus a small remainder. The characteristic polynomial of that shift is precisely $\Pi_{N_\sigma}(z^2/\lambda)$. Norm control of the remainder on the $N_\sigma^{-1}$ spectral scale would prove both radial rigidity and the phase grid in [\[eq:noisy-cloud-conjecture\]](#eq:noisy-cloud-conjecture){reference-type="eqref" reference="eq:noisy-cloud-conjecture"}.

#### 3. Residual normality.

Let $C_\sigma$ be the resulting cloud determinant. One needs local bounds for $$\label{eq:residual-family}
 \frac{D_{\sigma,\mathrm{bulk},2}(z)}{C_\sigma(z)}$$ on compact subsets of $|z|<\lambda$. Montel compactness and the exact Taylor germ would then identify every subsequential limit with the nonzero factor $\mathcal G$. This is exactly the estimate missing from coefficientwise convergence.

These steps also specify falsification criteria. If $N_\sigma$ does not obey [\[eq:rank-clock\]](#eq:rank-clock){reference-type="eqref" reference="eq:rank-clock"}, if phase errors fail to shrink, or if the residual family is not locally bounded, then the geometric scattering model is wrong even though the deterministic pole theorem remains valid.

# Conclusion

The parity-extracted determinant problem does not end in a conventional entire small-noise limit. The exact physical trace reconstruction shows why: the deterministic bulk target has the noncanceled factor $$\frac1{1-z^2/\lambda},$$ and therefore two simple poles at $\pm\sqrt\lambda$. This proves the sharp physical coefficient law, rules out normal convergence through the first spectral edge, and shows that finitely many limiting resonances cannot carry the required negative moments.

Finite noise resolves the poles through a growing complex cloud. At the smallest computed noise, fourteen resonances lie near the radius $\lambda^{-1/2}$ and the phases $\pm k\pi/8$. After radial centering, their determinant follows the exact geometric finite section whose scaling limit is $(e^s-1)/s$. The data therefore support a scattering continuation rather than an eigenvalue-by-eigenvalue limit.

The next theorem is now sharply formulated: derive the logarithmic effective rank, reduce the endpoint block to a finite shift, and prove normality after cloud extraction. No assertion about zeta zeros, Hilbert--Pólya, or the Riemann hypothesis is needed at this stage; the present result is an operator and determinant statement at one explicit quadratic map.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript, source, tests, exact reconstruction tables, sparse spectra, cloud selections, scattering data, determinant diagnostics, figures, and machine-readable summary are archived with this paper [@WangBulkScatteringCode2026].
