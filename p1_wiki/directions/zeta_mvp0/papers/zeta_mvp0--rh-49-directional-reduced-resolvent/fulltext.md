---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-49-directional-reduced-resolvent"
canonical_tex: "zeta_mvp0/papers/RH-49-directional-reduced-resolvent/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-49-directional-reduced-resolvent/main.pdf"
source_sha256: "7e5e8e8952136b6971a77ca2e99421cc7ad5e71f0e8cadc11925032e8eebaed8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Residue-Deflated Directional Resolvents at a Quadratic Critical Fold A Quarter-Power Stable-Rank Bridge for Intrinsic Riesz Identification

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-49-directional-reduced-resolvent>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-49-directional-reduced-resolvent/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-49-directional-reduced-resolvent/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-49-directional-reduced-resolvent/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-49-directional-reduced-resolvent/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The intrinsic Riesz-identification theorem for the small-noise folded-Gaussian quadratic map reduces its only remaining mesh gate to a mixed directional resolvent gain. On each Perron or negative-parity contour one must combine a Hilbert--Schmidt action on the detail-to-coarse coupling with an operator-norm action on the coarse-to-detail coupling, or use the symmetric placement. The global reduced resolvent is neither required nor expected to be uniformly bounded, but the mixed norm is still difficult to certify directly.

  We prove an exact stable-rank reduction. If $B$ and $C$ are the two Haar cross channels and $\ell_B^{(2)},\ell_C^{(2)}$ are their normalized Hilbert--Schmidt directional gains, then $$\min\{\ell_B^{(2)}\ell_C^{(\infty)},
          \ell_B^{(\infty)}\ell_C^{(2)}\}
   \le
   \ell_B^{(2)}\ell_C^{(2)}
   \min\!\left\{
   \frac{\left\lVert B\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert},
   \frac{\left\lVert C\right\rVert_{\mathfrak S_2}}{\left\lVert C\right\rVert}
   \right\}.$$ For the canonical cell-average folded-Gaussian operator we then prove the critical-endpoint estimates $$\left\lVert B\right\rVert_{\mathfrak S_2}=O(h\sigma^{-3/2}),
   \qquad
   \left\lVert B\right\rVert\ge c h\sigma^{-5/4},$$ uniformly once $h/\sigma$ is sufficiently small. Consequently the selected square root of stable rank is $$\frac{\left\lVert B\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert}=O(\sigma^{-1/4}).$$ Thus a purely Hilbert--Schmidt directional product of order $O(\sigma^{-\delta})$ implies the previous mixed condition with $\gamma=1/4+\delta$. Every strict $n\sigma^2\to\infty$ schedule is preserved whenever $\delta\le1/4$; uniform or polylogarithmic Hilbert--Schmidt gains leave a full quarter-power margin.

  We also give the exact rank-one residue-deflation identity and a primal/adjoint residual certificate for finite matrices. A five-scale binary64 audit reaches dimension $40960$. The outgoing coupling has fitted powers $-0.49526$ in Hilbert--Schmidt norm and $-0.25000$ in operator norm, giving a stable-rank exponent $0.24526$. The eight-node full Hilbert--Schmidt directional sum has no observed growth, while the direct mixed and stable-rank-transferred candidates have growth exponents $0.19162$ and $0.20371$, respectively. These computations are floating diagnostics, not validated asymptotic upper bounds. The remaining analytic task is now a Hilbert--Schmidt range-action estimate and a hard-cutoff transfer, not a global resolvent theorem. No arithmetic trace formula, zeta-zero identification, self-adjoint spectral realization, or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Residue-Deflated Directional Resolvents at a Quadratic Critical Fold\
  A Quarter-Power Stable-Rank Bridge for Intrinsic Riesz Identification
```

## Markdown 正文

**Keywords:** reduced resolvent; Riesz projection; stable rank; Hilbert--Schmidt operator; Haar coupling; critical fold; small noise; Galerkin approximation.

**MSC 2020:** 47A10; 47B10; 65R20; 37M25; 47A55.

# Introduction {#sec:introduction}

Let $E_n$ denote orthogonal averaging on the $n$ equal cells of $[0,1]$, and let $$G_{n,\sigma}=E_n\mathcal K_\sigma E_n$$ be the canonical cell-average Galerkin compression of the folded-Gaussian transfer operator associated with the first quadratic band-merging map. The preceding intrinsic-identification theorem compared the finite matrix's own Perron-plus-parity weighted Riesz term with the compression of the continuum term [@WangIntrinsic2026]. Its exact Schur formula begins quadratically in the adjacent Haar couplings and gives $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-2}\sigma^{-3-\gamma})
 \label{eq:rh48-bound}$$ provided a normalized mixed directional gain is $O(\sigma^{-\gamma})$, uniformly over all dyadic refinements.

The threshold in [\[eq:rh48-bound\]](#eq:rh48-bound){reference-type="eqref" reference="eq:rh48-bound"} is sharp at the level of that ledger. If $n(\sigma)\asymp\sigma^{-p}$, every strict $p>2$ schedule survives exactly when $\gamma\le1/2$. The mixed quantity is substantially weaker than a global resolvent norm, but one of its two factors is still an operator norm. Direct numerical estimation therefore produces only lower candidates, while a deterministic upper appears to require a large sparse singular-value certificate.

This paper removes that operator-norm factor from the analytic premise. The replacement is a stable-rank multiplier depending only on the two fixed Haar couplings. The endpoint geometry of the quadratic fold then selects the better coupling and costs exactly one quarter power of the noise width.

## Main results {#main-results .unnumbered}

The paper has four analytic components.

1.  **Exact residue deflation.** For a simple eigenvalue $\lambda$, with Riesz projection $P$, $$R^\circ(z)
      =(z-T)^{-1}-\frac{P}{z-\lambda}
      =(z-T+\lambda P)^{-1}(\mathrm I-P).$$ The same lifted shift gives the adjoint action without forming a dense resolvent.

2.  **Stable-rank norm placement.** The mixed RH-48 gain is at most the product of the two normalized Hilbert--Schmidt gains times $$\min\left\{\frac{\left\lVert B\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert},
                   \frac{\left\lVert C\right\rVert_{\mathfrak S_2}}{\left\lVert C\right\rVert}\right\}.$$ This statement is exact and does not contain a global resolvent norm.

3.  **Critical-fold quarter power.** For the outgoing detail-to-coarse channel $B$, a packet supported in the target endpoint layer produces an output on the source scale $x=\sqrt\sigma\,\xi$. The resulting lower bound is $\left\lVert B\right\rVert\gtrsim h\sigma^{-5/4}$, while the Gaussian derivative envelope gives $\left\lVert B\right\rVert_{\mathfrak S_2}=O(h\sigma^{-3/2})$. Hence the selected stable-rank factor is $O(\sigma^{-1/4})$.

4.  **Hilbert--Schmidt closure theorem.** If the sum of the two branchwise Hilbert--Schmidt gain products is $O(\sigma^{-\delta})$, then the RH-48 exponent is $\gamma=1/4+\delta$. The full strict $p>2$ mesh range survives for $\delta\le1/4$.

The distinction between theorem and evidence is important. The quarter-power coupling estimate is analytic for the canonical cell-average kernel. The Hilbert--Schmidt directional gain itself is not proved uniformly in $\sigma$, and the stored sparse matrices retain an eight-sigma hard cutoff that requires a separate transfer estimate. The finite computations show that both missing layers are plausible; they do not replace them.

# Folded-Gaussian operator and the RH-48 gate {#sec:setup}

Let $$f(x)=1-u_{\rm c}x^2,
 \qquad 0\le x\le1,
 \label{eq:quadratic-map}$$ where $u_{\rm c}>0$ is the first band-merging parameter. Put $$\phi_\sigma(t)=\frac{1}{\sqrt{2\pi}\sigma}
 e^{-t^2/(2\sigma^2)}$$ and define the conditioned folded kernel $$k_\sigma(x,y)
 =\frac{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))}
 {Z_\sigma(x)},
 \label{eq:folded-kernel}$$ where the denominator is the integral of the numerator over $0\le y\le1$. The Markov operator on observables is $$(\mathcal K_\sigma v)(x)=\int_0^1k_\sigma(x,y)v(y)\,dy.
 \label{eq:markov-operator}$$ It is compact and strongly positive for every fixed $\sigma>0$.

Let $$W_n=\operatorname{Ran}(E_{2n}-E_n),
 \qquad
 V_{2n}=V_n\oplus W_n.$$ Relative to this orthogonal Haar split, write $$G_{2n,\sigma}
 =\begin{pmatrix}A&B\\C&D\end{pmatrix},
 \label{eq:haar-blocks}$$ where $$A=G_{n,\sigma},\quad
 B=E_n\mathcal K_\sigma(E_{2n}-E_n),\quad
 C=(E_{2n}-E_n)\mathcal K_\sigma E_n.
 \label{eq:cross-couplings}$$ The identities in [\[eq:cross-couplings\]](#eq:cross-couplings){reference-type="eqref" reference="eq:cross-couplings"} use the exact nesting $E_nE_{2n}=E_n$.

For a branch $s\in\{+,-\}$, let $\Gamma_s$ be its fixed peripheral contour. The top-left fine resolvent is the Schur inverse $$S_s(z)=E_n(z-G_{2n,\sigma})^{-1}E_n
       =(z-A-B(z-D)^{-1}C)^{-1},$$ and put $R_{A,s}(z)=(z-A)^{-1}$. Define $$\begin{aligned}
 \ell_{B,s}^{(2)}
 &=\sup_{z\in\Gamma_s}
   \frac{\left\lVert S_s(z)B\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}},
 &
 \ell_{B,s}^{(\infty)}
 &=\sup_{z\in\Gamma_s}
   \frac{\left\lVert S_s(z)B\right\rVert}{\left\lVert B\right\rVert},
 \label{eq:left-gains}\\
 \ell_{C,s}^{(2)}
 &=\sup_{z\in\Gamma_s}
   \frac{\left\lVert CR_{A,s}(z)\right\rVert_{\mathfrak S_2}}{\left\lVert C\right\rVert_{\mathfrak S_2}},
 &
 \ell_{C,s}^{(\infty)}
 &=\sup_{z\in\Gamma_s}
   \frac{\left\lVert CR_{A,s}(z)\right\rVert}{\left\lVert C\right\rVert}.
 \label{eq:right-gains}\end{aligned}$$ Zero couplings may be assigned zero gain. The mixed and purely Hilbert--Schmidt sums are $$\begin{aligned}
 \mathcal L_{n,\sigma}
 &:=\sum_{s\in\{+,-\}}
 \min\left\{
 \ell_{B,s}^{(2)}\ell_{C,s}^{(\infty)},
 \ell_{B,s}^{(\infty)}\ell_{C,s}^{(2)}
 \right\},
 \label{eq:mixed-gain}\\
 \mathcal F_{n,\sigma}
 &:=\sum_{s\in\{+,-\}}
 \ell_{B,s}^{(2)}\ell_{C,s}^{(2)}.
 \label{eq:hs-gain}\end{aligned}$$ The condition in the preceding paper was a dyadically uniform upper for $\mathcal L_{n,\sigma}$. Our purpose is to replace it by an upper for $\mathcal F_{n,\sigma}$.

# Exact rank-one residue deflation {#sec:deflation}

The peripheral projection norm grows logarithmically in the small-noise limit [@WangLogConditioning2026]. It is therefore essential to remove the selected pole exactly before interpreting a reduced solve.

[\[prop:deflated-resolvent\]]{#prop:deflated-resolvent label="prop:deflated-resolvent"} Let $T$ be a bounded operator, let $\lambda\ne0$ be a simple isolated eigenvalue, and let $P$ be its Riesz projection. Put $Q=\mathrm I-P$. For $z\ne0,\lambda$ in the relevant resolvent sets, $$R^\circ(z)
 :=(z-T)^{-1}-\frac{P}{z-\lambda}
 =(z-T+\lambda P)^{-1}Q
 =Q(z-T+\lambda P)^{-1}.
 \label{eq:deflated-identity}$$ Moreover, $$R^\circ(z)^*
 =Q^*(\overline z-T^*+\overline\lambda P^*)^{-1}.
 \label{eq:deflated-adjoint}$$

Since $TP=PT=\lambda P$, the space splits algebraically into the invariant ranges of $P$ and $Q$. On $PH$, the operator $T-\lambda P$ vanishes, while on $QH$ it equals $T$. Therefore $$(z-T+\lambda P)^{-1}
 =z^{-1}P+(z-T)^{-1}Q.$$ Multiplication by $Q$ gives [\[eq:deflated-identity\]](#eq:deflated-identity){reference-type="eqref" reference="eq:deflated-identity"}; taking adjoints gives [\[eq:deflated-adjoint\]](#eq:deflated-adjoint){reference-type="eqref" reference="eq:deflated-adjoint"}.

For a normalized right/left eigenpair $Tr=\lambda r$, $T^*\ell=\overline\lambda\ell$, $\langle\ell,r\rangle=1$, one has $P=r\otimes\ell$. Thus a matrix-free primal action is obtained from $$(z-T+\lambda r\otimes\ell)x
 =b-r\langle\ell,b\rangle,
 \label{eq:primal-deflated-solve}$$ and the adjoint action from $$(\overline z-T^*+\overline\lambda\ell\otimes r)y
 =c-\ell\langle r,c\rangle.
 \label{eq:adjoint-deflated-solve}$$ These are the systems used in the numerical audit.

The branchwise deflation removes the pole enclosed by the current contour. The opposite peripheral eigenvalue remains in the complement but stays a fixed distance from that contour. Rank-two deflation is possible, but it is not required for the identities or computations below.

# Stable-rank transfer of the norm placement {#sec:stable-rank}

For a nonzero Hilbert--Schmidt operator $X$, define its square root of stable rank by $$\kappa(X):=\frac{\left\lVert X\right\rVert_{\mathfrak S_2}}{\left\lVert X\right\rVert}
 =\sqrt{\operatorname{sr}(X)}.
 \label{eq:sqrt-stable-rank}$$

[\[thm:stable-rank-bridge\]]{#thm:stable-rank-bridge label="thm:stable-rank-bridge"} For every adjacent Haar split for which $B,C\ne0$, $$\boxed{
 \mathcal L_{n,\sigma}
 \le
 \mathcal F_{n,\sigma}\min\{\kappa(B),\kappa(C)\}.}
 \label{eq:stable-rank-bridge}$$ The inequality applies equally to full or residue-reduced directional resolvents.

For each branch and every contour node, $$\left\lVert S_s(z)B\right\rVert
 \le\left\lVert S_s(z)B\right\rVert_{\mathfrak S_2}.$$ After dividing by $\left\lVert B\right\rVert$ and taking the supremum, $$\ell_{B,s}^{(\infty)}
 \le\ell_{B,s}^{(2)}\kappa(B).
 \label{eq:left-stable-transfer}$$ Likewise, $$\ell_{C,s}^{(\infty)}
 \le\ell_{C,s}^{(2)}\kappa(C).
 \label{eq:right-stable-transfer}$$ Insert [\[eq:left-stable-transfer\]](#eq:left-stable-transfer){reference-type="eqref" reference="eq:left-stable-transfer"} and [\[eq:right-stable-transfer\]](#eq:right-stable-transfer){reference-type="eqref" reference="eq:right-stable-transfer"} into the two alternatives in [\[eq:mixed-gain\]](#eq:mixed-gain){reference-type="eqref" reference="eq:mixed-gain"}, take their minimum, and sum over the two branches.

The theorem contains no bound for $S_s$, $R_{A,s}$, or either reduced resolvent on the whole ambient space. All nonnormality remains inside the two Hilbert--Schmidt range actions. The price is the stable rank of one fixed coupling, which can be studied geometrically.

# Critical endpoint packet and the quarter power {#sec:endpoint}

The better coupling is $B$, which differentiates in the target variable and exits through the quadratic critical source. We first record the endpoint scaling of the conditioned kernel.

## The endpoint profile

Let $x=\sqrt\sigma\,\xi$ and $y=1-\sigma s$. Since $$f(\sqrt\sigma\,\xi)=1-u_{\rm c}\sigma\xi^2,$$ the rescaled first Gaussian in [\[eq:folded-kernel\]](#eq:folded-kernel){reference-type="eqref" reference="eq:folded-kernel"} has center clearance $u_{\rm c}\xi^2$. Put $$q(\xi,s)
 :=\frac{\phi_1(u_{\rm c}\xi^2-s)}
 {\Phi(u_{\rm c}\xi^2)},
 \qquad \xi,s\ge0,
 \label{eq:endpoint-profile}$$ where $\Phi$ is the standard normal distribution function.

[\[lem:endpoint-scaling\]]{#lem:endpoint-scaling label="lem:endpoint-scaling"} On every compact subset of $[0,\infty)^2$, $$\begin{aligned}
 \sigma k_\sigma(\sqrt\sigma\,\xi,1-\sigma s)
 &\longrightarrow q(\xi,s),
 \label{eq:kernel-scaling}\\
 \sigma^2\partial_y k_\sigma(
 \sqrt\sigma\,\xi,1-\sigma s)
 &\longrightarrow-\partial_s q(\xi,s).
 \label{eq:kernel-derivative-scaling}\end{aligned}$$ The convergence admits Gaussian majorants after multiplication by any fixed compactly supported function of $s$.

The integral of the first Gaussian in [\[eq:folded-kernel\]](#eq:folded-kernel){reference-type="eqref" reference="eq:folded-kernel"} tends to $\Phi(u_{\rm c}\xi^2)$. The folded companion has center near $-1$ in the physical $y$-coordinate and is $O(e^{-c/\sigma^2})$ on the displayed scale. Thus the denominator converges locally uniformly to the denominator in [\[eq:endpoint-profile\]](#eq:endpoint-profile){reference-type="eqref" reference="eq:endpoint-profile"}. The numerator gives $$\sigma\phi_\sigma(
 1-\sigma s-(1-u_{\rm c}\sigma\xi^2))
 =\phi_1(u_{\rm c}\xi^2-s).$$ Differentiation in $y=1-\sigma s$ contributes the second factor $\sigma^{-1}$, proving [\[eq:kernel-derivative-scaling\]](#eq:kernel-derivative-scaling){reference-type="eqref" reference="eq:kernel-derivative-scaling"}. Since $\Phi(u_{\rm c}\xi^2)\ge1/2$, the Gaussian numerator and its polynomial derivatives provide the claimed majorants.

## A normalized Haar packet

Let $h=1/n$, and for the $j$-th coarse target cell put $$\psi_{j,h}(y)
 =h^{-1/2}
 \left(mathbf1_{[jh,jh+h/2)}(y)
 -\mathbf1_{[jh+h/2,(j+1)h)}(y)\right).
 \label{eq:haar-wavelet}$$ The functions $\psi_{j,h}$ form an orthonormal basis of $W_n$.

Choose a nonnegative $A\in C_c^\infty((0,\infty))$ with $\left\lVert A\right\rVert_2=1$, and define $$a_\sigma(y)=\sigma^{-1/2}
 A\!\left(\frac{1-y}{\sigma}\right).
 \label{eq:target-envelope}$$ If $y_j=(j+1/2)h$, set $$c_{j,h,\sigma}=\sqrt h\,a_\sigma(y_j),
 \qquad
 w_{h,\sigma}
 =\frac{\sum_jc_{j,h,\sigma}\psi_{j,h}}
 {\left(\sum_j|c_{j,h,\sigma}|^2\right)^{1/2}}.
 \label{eq:haar-packet}$$ When $h/\sigma\to0$, the denominator tends to one by a Riemann sum.

Define the limiting output profile $$F_A(\xi)
 :=\int_0^\infty A(s)\partial_s q(\xi,s)\,ds.
 \label{eq:limit-output}$$ At $\xi=0$, $$\partial_s q(0,s)=-2s\phi_1(s),$$ so $F_A(0)<0$. Gaussian decay gives $F_A\in L^2(0,\infty)$, and hence $\left\lVert F_A\right\rVert_2>0$.

[\[thm:endpoint-lower\]]{#thm:endpoint-lower label="thm:endpoint-lower"} There are $a_0,c,\sigma_0>0$ such that, whenever $0<\sigma<\sigma_0$ and $0<h/\sigma<a_0$, the outgoing Haar coupling $$B_{n,\sigma}=E_n\mathcal K_\sigma(E_{2n}-E_n)$$ satisfies $$\boxed{
 \left\lVert B_{n,\sigma}\right\rVert
 \ge c h\sigma^{-5/4}.}
 \label{eq:B-operator-lower}$$ More precisely, the packets in [\[eq:haar-packet\]](#eq:haar-packet){reference-type="eqref" reference="eq:haar-packet"} obey $$\frac{\sigma^{5/4}}{h}
 \left\lVert B_{n,\sigma}w_{h,\sigma}\right\rVert
 \longrightarrow\frac14\left\lVert F_A\right\rVert_{L^2(0,\infty)}
 \label{eq:packet-limit}$$ as $\sigma\to0$ and $h/\sigma\to0$.

For a smooth function $g$, the symmetric Haar difference on one cell is $$\int_{jh}^{jh+h/2}g(y)\,dy
 -\int_{jh+h/2}^{(j+1)h}g(y)\,dy
 =-\frac{h^2}{4}g'(y_j)
 +O\!\left(h^4\sup_{I_j}|g'''|\right).
 \label{eq:haar-first-moment}$$ Apply this with $g(y)=k_\sigma(x,y)$. Because the coefficient $c_{j,h,\sigma}h^{-1/2}$ equals $a_\sigma(y_j)$, summing [\[eq:haar-first-moment\]](#eq:haar-first-moment){reference-type="eqref" reference="eq:haar-first-moment"} gives $$(\mathcal K_\sigma w_{h,\sigma})(x)
 =-\frac h4\int_0^1
 a_\sigma(y)\partial_yk_\sigma(x,y)\,dy
 +r_{h,\sigma}(x),
 \label{eq:packet-expansion}$$ where $$\left\lVert r_{h,\sigma}\right\rVert_2
 =o(h\sigma^{-5/4}).
 \label{eq:packet-remainder}$$ Indeed, on the compact support selected by $A$, target derivatives of order three have scale $O(\sigma^{-4})$, the number of active cells is $O(\sigma/h)$, and the source output is concentrated on a layer of width $O(\sqrt\sigma)$. The Taylor remainder relative to the main term is $O((h/\sigma)^2)$. Midpoint replacement in the sum has the same relative order. Outside the critical source layer the Gaussian majorant is exponentially small.

Now use $y=1-\sigma s$, $x=\sqrt\sigma\,\xi$, and [\[lem:endpoint-scaling\]](#lem:endpoint-scaling){reference-type="ref" reference="lem:endpoint-scaling"}. Dominated convergence gives $$\sigma^{3/2}
 \int_0^1a_\sigma(y)\partial_yk_\sigma(
 \sqrt\sigma\,\xi,y)\,dy
 \longrightarrow- F_A(\xi)
 \label{eq:packet-profile-convergence}$$ in the rescaled $L^2(d\xi)$ space. Since $dx=\sqrt\sigma\,d\xi$, the leading term in [\[eq:packet-expansion\]](#eq:packet-expansion){reference-type="eqref" reference="eq:packet-expansion"} has physical $L^2(dx)$ norm $$\frac h4\sigma^{-3/2}\sigma^{1/4}\left\lVert F_A\right\rVert_2
 =\frac h4\sigma^{-5/4}\left\lVert F_A\right\rVert_2.$$ Finally, cell averaging in the source changes this profile by relative size $O(h/\sqrt\sigma)=o(1)$. This proves [\[eq:packet-limit\]](#eq:packet-limit){reference-type="eqref" reference="eq:packet-limit"}; positivity of its limit yields [\[eq:B-operator-lower\]](#eq:B-operator-lower){reference-type="eqref" reference="eq:B-operator-lower"} for sufficiently small $h/\sigma$ and $\sigma$.

The lower bound is a critical-fold effect. A normalized target packet has width $\sigma$; Gaussian differentiation costs $\sigma^{-1}$, while the quadratic preimage of the endpoint has source width $\sqrt\sigma$. The resulting $L^2$ gain is the quarter power in [\[eq:B-operator-lower\]](#eq:B-operator-lower){reference-type="eqref" reference="eq:B-operator-lower"}.

## Hilbert--Schmidt upper and stable rank

The target derivative envelope proved previously is $$\left\lVert \partial_yk_\sigma\right\rVert_{L^2([0,1]^2)}
 =O(\sigma^{-3/2})
 \label{eq:kernel-y-envelope}$$ [@WangSmallNoiseMesh2026]. Cellwise Poincaré--Wirtinger now gives the matching Hilbert--Schmidt estimate.

[\[prop:B-hs-upper\]]{#prop:B-hs-upper label="prop:B-hs-upper"} For every $n\ge1$, $$\left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \le\frac{h}{\pi}
 \left\lVert \partial_yk_\sigma\right\rVert_{L^2([0,1]^2)}
 =O(h\sigma^{-3/2}).
 \label{eq:B-hs-upper}$$

Since $E_{2n}-E_n$ is an orthogonal subprojection of $\mathrm I-E_n$, $$\left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \le\left\lVert \mathcal K_\sigma(\mathrm I-E_n)\right\rVert_{\mathfrak S_2}.$$ The kernel on the right is the target-variable cell-averaging error. Applying the one-dimensional Poincaré inequality on every target cell and then integrating over the source proves the first inequality. Use [\[eq:kernel-y-envelope\]](#eq:kernel-y-envelope){reference-type="eqref" reference="eq:kernel-y-envelope"} for the second.

[\[cor:quarter-stable-rank\]]{#cor:quarter-stable-rank label="cor:quarter-stable-rank"} There are $C,a_0,\sigma_0>0$ such that $$\boxed{
 \kappa(B_{n,\sigma})
 =\frac{\left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}}
 {\left\lVert B_{n,\sigma}\right\rVert}
 \le C\sigma^{-1/4}}
 \label{eq:B-stable-rank}$$ whenever $0<\sigma<\sigma_0$ and $h/\sigma<a_0$. The same constant is valid at every finer dyadic level.

Divide [\[eq:B-hs-upper\]](#eq:B-hs-upper){reference-type="eqref" reference="eq:B-hs-upper"} by [\[eq:B-operator-lower\]](#eq:B-operator-lower){reference-type="eqref" reference="eq:B-operator-lower"}. Replacing $h$ by $2^{-j}h$ only decreases $h/\sigma$, so the estimate is uniform over all $j\ge0$.

No estimate for $\kappa(C)$ is needed. The minimum in [\[thm:stable-rank-bridge\]](#thm:stable-rank-bridge){reference-type="ref" reference="thm:stable-rank-bridge"} automatically selects the outgoing channel.

# Quarter-power closure of intrinsic identification {#sec:closure}

We can now replace the mixed directional premise of RH-48 by a purely Hilbert--Schmidt premise.

[\[cond:hs-gain\]]{#cond:hs-gain label="cond:hs-gain"} There are $C<\infty$, $\delta\ge0$, $\sigma_0>0$, and $n_0(\sigma)$ such that the two contours lie in the required resolvent sets and $$\sup_{j\ge0}\mathcal F_{2^jn,\sigma}
 \le C\sigma^{-\delta}
 \label{eq:hs-gain-condition}$$ for $0<\sigma<\sigma_0$ and $n\ge n_0(\sigma)$.

[\[thm:hs-closure\]]{#thm:hs-closure label="thm:hs-closure"} Assume [\[cond:hs-gain\]](#cond:hs-gain){reference-type="ref" reference="cond:hs-gain"}, and suppose $n$ is large enough that $h/\sigma<a_0$ from [\[cor:quarter-stable-rank\]](#cor:quarter-stable-rank){reference-type="ref" reference="cor:quarter-stable-rank"}. Then $$\sup_{j\ge0}\mathcal L_{2^jn,\sigma}
 =O(\sigma^{-1/4-\delta}).
 \label{eq:mixed-from-hs}$$ Consequently the intrinsic identification defect satisfies $$\boxed{
 \left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-2}\sigma^{-13/4-\delta}).}
 \label{eq:identification-quarter-bound}$$ Every strict schedule $n(\sigma)\sigma^2\to\infty$ retains the anchored bulk-square theorem whenever $\delta\le1/4$.

Apply [\[thm:stable-rank-bridge\]](#thm:stable-rank-bridge){reference-type="ref" reference="thm:stable-rank-bridge"} and [\[cor:quarter-stable-rank\]](#cor:quarter-stable-rank){reference-type="ref" reference="cor:quarter-stable-rank"} at each dyadic level: $$\mathcal L_{2^jn,\sigma}
 \le C\sigma^{-1/4}\mathcal F_{2^jn,\sigma}.$$ This proves [\[eq:mixed-from-hs\]](#eq:mixed-from-hs){reference-type="eqref" reference="eq:mixed-from-hs"}. The exponent in the notation of [\[eq:rh48-bound\]](#eq:rh48-bound){reference-type="eqref" reference="eq:rh48-bound"} is $$\gamma=\frac14+\delta.
 \label{eq:gamma-delta}$$ Insert [\[eq:gamma-delta\]](#eq:gamma-delta){reference-type="eqref" reference="eq:gamma-delta"} into [\[eq:rh48-bound\]](#eq:rh48-bound){reference-type="eqref" reference="eq:rh48-bound"} to obtain [\[eq:identification-quarter-bound\]](#eq:identification-quarter-bound){reference-type="eqref" reference="eq:identification-quarter-bound"}. The previous threshold $\gamma\le1/2$ is equivalent to $\delta\le1/4$.

[\[cor:polylog\]]{#cor:polylog label="cor:polylog"} If, for a fixed $m$, $$\sup_{j\ge0}\mathcal F_{2^jn,\sigma}
 =O((\log(1/\sigma))^m),
 \label{eq:polylog-hs}$$ then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O\!\left(
 n^{-2}\sigma^{-13/4}(\log(1/\sigma))^m
 \right),
 \label{eq:polylog-identification}$$ and every schedule $n\sigma^2\to\infty$ makes this lower order than the anchored one-step Hilbert--Schmidt clock $n^{-1}\sigma^{-3/2}$.

The ratio of [\[eq:polylog-identification\]](#eq:polylog-identification){reference-type="eqref" reference="eq:polylog-identification"} to the anchored clock is $$\frac{\sigma^{1/4}(\log(1/\sigma))^m}{n\sigma^2},$$ which tends to zero.

The significance of [\[thm:hs-closure\]](#thm:hs-closure){reference-type="ref" reference="thm:hs-closure"} is not merely a relaxed numerical test. Hilbert--Schmidt actions can be audited by block residuals, trace estimators, and low-rank tail bounds, whereas an operator-norm upper requires control of every input direction. The difficult nonnormal geometry has been moved into an average-energy gate with a quantified quarter-power allowance.

# A posteriori primal and adjoint certificates {#sec:certificate}

We record the deterministic finite-matrix certificate suggested by the deflated systems. It is elementary but useful because it separates the computed directional action from the remaining reduced-inverse budget.

[\[thm:residual-upper\]]{#thm:residual-upper label="thm:residual-upper"} Let $$A_\lambda(z)=z-T+\lambda P,
 \qquad Q=\mathrm I-P,$$ and suppose $\left\lVert A_\lambda(z)^{-1}\right\rVert\le M$. For a Hilbert--Schmidt source operator $E$ and any approximation $X$, define $$\mathcal E=QE-A_\lambda(z)X.$$ Then $$\left\lVert R^\circ(z)E\right\rVert_{\mathfrak S_2}
 \le\left\lVert X\right\rVert_{\mathfrak S_2}+M\left\lVert \mathcal E\right\rVert_{\mathfrak S_2}.
 \label{eq:residual-upper}$$ For an observation $F$, solve the adjoint problem with approximation $Y$ and residual $$\mathcal D=Q^*F^*-A_\lambda(z)^*Y.$$ Then $$\left\lVert FR^\circ(z)\right\rVert_{\mathfrak S_2}
 \le\left\lVert Y\right\rVert_{\mathfrak S_2}+M\left\lVert \mathcal D\right\rVert_{\mathfrak S_2}.
 \label{eq:dual-residual-upper}$$

By [\[prop:deflated-resolvent\]](#prop:deflated-resolvent){reference-type="ref" reference="prop:deflated-resolvent"}, $$A_\lambda(z)(R^\circ(z)E-X)=\mathcal E.$$ Apply the ideal property of the Hilbert--Schmidt norm. The adjoint statement follows from [\[eq:deflated-adjoint\]](#eq:deflated-adjoint){reference-type="eqref" reference="eq:deflated-adjoint"}; moreover $FR^\circ(z)=((R^\circ(z))^*F^*)^*$.

After division by certified lower bounds for $\left\lVert B\right\rVert_{\mathfrak S_2}$ and $\left\lVert C\right\rVert_{\mathfrak S_2}$, [\[eq:residual-upper\]](#eq:residual-upper){reference-type="eqref" reference="eq:residual-upper"} and [\[eq:dual-residual-upper\]](#eq:dual-residual-upper){reference-type="eqref" reference="eq:dual-residual-upper"} bound the two factors in $\mathcal F_{n,\sigma}$. A validated reduced-inverse upper $M$ may grow with $\sigma$; sufficiently small outward residuals still make its contribution negligible. Sparse Grushin and primal--dual residual machinery from the preceding finite-matrix work can supply this layer [@WangSparseGrushin2026; @WangPrimalDual2026].

For a continuous contour, node bounds can be transported over an arc by the usual resolvent identity. If $M_0\ge\left\lVert A_\lambda(z_0)^{-1}\right\rVert$ and $|z-z_0|M_0<1$, then $$\left\lVert A_\lambda(z)^{-1}\right\rVert
 \le\frac{M_0}{1-|z-z_0|M_0}.
 \label{eq:arc-transport}$$ Thus the remaining computer-assisted proof has a finite checklist: enclose the eigenfactors, certify one deflated inverse budget at the contour nodes, bound primal and adjoint Hilbert--Schmidt residual blocks, and transport over the intervening arcs.

# Five-scale numerical audit {#sec:numerics}

The computation tests three distinct statements. They must not be merged into one evidence level.

1.  The sparse Haar blocks $B$ and $C$ are materialized exactly from the stored binary64 matrix. Their Frobenius norms are direct sums of squares. Matrix-free power iteration gives operator-norm candidates.

2.  Four deterministic Rademacher probes estimate the normalized Hilbert--Schmidt actions on eight nodes of each Perron and parity contour. Each branch pole is removed by [\[eq:primal-deflated-solve\]](#eq:primal-deflated-solve){reference-type="eqref" reference="eq:primal-deflated-solve"}.

3.  Matrix-free primal/adjoint singular iteration estimates the two mixed placements at the empirically worst real contour node. These ratios are diagnostics, not certified singular-value uppers.

At every noise level the fine resolution is fixed at $N\sigma=20.48$, so the coarse resolution is $n\sigma=10.24$. The largest matrix has dimension $40960$. GMRES uses relative tolerance $2\times10^{-10}$.

::: {#tab:audit}
                $\sigma$     $N$   $\kappa_B$ cand.   full HS sum   transferred   direct mixed   max GMRES
  ---------------------- ------- ------------------ ------------- ------------- -------------- -----------
               $10^{-2}$    2048             2.9203        4.4076       12.8714         4.5434          23
    $4\!\times\!10^{-3}$    5120             3.6474        4.6473       16.9507         6.0494          29
    $2\!\times\!10^{-3}$   10240             4.3227        4.2154       18.2220         6.9431          32
               $10^{-3}$   20480             5.1280        4.1833       21.4524         7.6162          37
    $5\!\times\!10^{-4}$   40960             6.0878        3.9630       24.1260         8.1287          41

  : Five-scale directional audit. "Transferred" is the full Hilbert--Schmidt branch sum multiplied by the selected floating stable-rank candidate. "Direct mixed" sums the two branchwise mixed candidates at the selected real nodes.
:::

## The quarter-power coupling law

The fitted powers are $$\begin{aligned}
 \left\lVert B\right\rVert_{\mathfrak S_2}&\sim\sigma^{-0.4952635},
 &\left\lVert B\right\rVert_{\rm cand}&\sim\sigma^{-0.2500047},
 \label{eq:B-numeric-powers}\\
 \kappa_B^{\rm cand}&\sim\sigma^{-0.2452588},
 &\kappa_C^{\rm cand}&\sim\sigma^{-0.4996294}.
 \label{eq:stable-numeric-powers}\end{aligned}$$ The maximum log residual in the fit for $\kappa_B$ is $1.35\times10^{-3}$. Thus the minimum in [\[thm:stable-rank-bridge\]](#thm:stable-rank-bridge){reference-type="ref" reference="thm:stable-rank-bridge"} selects $B$ at every scale and reproduces the analytic quarter-power mechanism to within $0.0048$ in exponent.

The operator statement remains floating: evaluating $\left\lVert Bv\right\rVert$ on a power iterate gives a lower candidate for $\left\lVert B\right\rVert$, and binary64 rounding has not been enclosed. The analytic theorem, not the regression, is the source of the asymptotic upper [\[eq:B-stable-rank\]](#eq:B-stable-rank){reference-type="eqref" reference="eq:B-stable-rank"}.

## Hilbert--Schmidt and mixed gains

The sum of the two full Hilbert--Schmidt products is $$4.4076,\quad4.6473,\quad4.2154,\quad4.1833,\quad3.9630.$$ Its fitted $\sigma$-power is $+0.04155$, so the nonnegative candidate growth exponent is zero. The residue-deflated sum has whole-range growth exponent $0.06786$, but the last three levels decrease slightly. This is strong evidence for a bounded Hilbert--Schmidt gate, not a proof of [\[cond:hs-gain\]](#cond:hs-gain){reference-type="ref" reference="cond:hs-gain"}.

The direct mixed branch sum has growth exponent $0.19162$, falling to $0.11373$ on the last three levels. The stable-rank-transferred full candidate has exponent $0.20371$. Both are well below the RH-48 critical exponent $1/2$. Maximum relative GMRES residuals stay below $2.0\times10^{-10}$, branch leakage below $3.0\times10^{-13}$, and the largest iteration count is 41.

![Quarter-power directional-resolvent audit. (a) Exact sparse Haar Frobenius norms and floating operator candidates. (b) The outgoing $B$-channel stable-rank factor follows $\sigma^{-1/4}$, whereas the $C$ channel follows $\sigma^{-1/2}$. (c) Eight-node full and residue-deflated Hilbert--Schmidt products. (d) Direct mixed and stable-rank-transferred candidates compared by slope with the RH-48 $\sigma^{-1/2}$ boundary.](<../../../../../zeta_mvp0/papers/RH-49-directional-reduced-resolvent/figures/directional_reduced_resolvent.pdf>){#fig:audit width="\\textwidth"}

# What is proved and what remains {#sec:boundary}

The present result changes the next gate in a material way.

Proved operator algebra

:   Exact rank-one residue deflation, primal/adjoint range-action identities, the stable-rank norm-placement inequality, and the a posteriori residual upper.

Proved endpoint analysis

:   For the canonical cell-average folded-Gaussian family, the outgoing Haar coupling has Hilbert--Schmidt upper $O(h\sigma^{-3/2})$, operator lower $\Omega(h\sigma^{-5/4})$, and square-root stable rank $O(\sigma^{-1/4})$.

Conditional small-noise theorem

:   A dyadically uniform Hilbert--Schmidt directional gain of order $\sigma^{-\delta}$ implies the RH-48 mixed condition with $\gamma=1/4+\delta$. The entire strict $p>2$ range survives for $\delta\le1/4$.

Floating evidence

:   Five-scale exact-Haar Frobenius sums, Hutchinson-GMRES range actions, and power-iteration operator candidates. None is an interval enclosure.

Two analytic tasks remain.

1.  **Hilbert--Schmidt range-action upper.** Prove [\[cond:hs-gain\]](#cond:hs-gain){reference-type="ref" reference="cond:hs-gain"}, ideally with $\delta=0$ or a polylogarithmic loss. The residue-deflated formulation suggests combining a two-pole decomposition with smoothing on the coupling ranges rather than controlling the global reduced resolvent.

2.  **Stored sparse transfer.** Transfer the canonical endpoint packet and Hilbert--Schmidt estimates to the eight-sigma cutoff, row-renormalized sparse matrices with validated error. Previous cutoff and Euclidean bridge bounds provide the natural starting point [@WangHaar2026; @WangSmallNoiseMesh2026].

If either step fails, the failure is now localized. A negative result for the Hilbert--Schmidt gate would show genuine energy growth on the two coupling ranges; it would not be confused with the already known global residue conditioning. A failure of sparse transfer would identify the hard cutoff, not the underlying critical-fold operator, as the obstruction.

## No Hilbert--Pólya or arithmetic claim

All objects in this paper arise from one explicit noisy quadratic transfer operator and its Galerkin compressions. The result does not construct a self-adjoint Hilbert--Pólya operator, identify any eigenvalue with a zero of the Riemann zeta function, prove a prime-power trace identity, derive a $T\log T$ counting law, or imply the Riemann hypothesis. It advances one operator-theoretic mesh gate inside the existing dynamical program.

# Reproducibility {#sec:reproducibility}

The archive contains:

-   , implementing exact dense deflation, stable-rank transfer, residual ledgers, and the critical endpoint profile;

-   , the eight-node residue-deflated Hilbert--Schmidt audit;

-   , the matrix-free primal/adjoint singular audit;

-   , the exact sparse Haar Frobenius and operator-candidate audit;

-   machine-readable certificates, source hashes, tests, and the figure used in [1](#fig:audit){reference-type="ref" reference="fig:audit"}.

The complete archive and replay instructions are available in the project repository [@WangDirectionalCode2026].

# Conclusion

The mixed directional gate from intrinsic Riesz identification admits a strictly simpler sufficient condition. An exact stable-rank inequality replaces the operator-norm range action by a second Hilbert--Schmidt action, and the quadratic critical endpoint charges only $\sigma^{-1/4}$ for that replacement. Therefore a Hilbert--Schmidt gain may itself grow by another quarter power before the strict $p>2$ mesh range is lost.

The numerical evidence is unusually coherent: the two coupling norms split into the predicted half- and quarter-power exponents, the full Hilbert--Schmidt directional product stays flat, and two independent mixed diagnostics remain well below the critical half-power slope. The maze has therefore narrowed from a global nonnormal resolvent problem to a concrete Hilbert--Schmidt range-action theorem plus a sparse cutoff transfer. Those are the next gates; they are not silently assumed here.
