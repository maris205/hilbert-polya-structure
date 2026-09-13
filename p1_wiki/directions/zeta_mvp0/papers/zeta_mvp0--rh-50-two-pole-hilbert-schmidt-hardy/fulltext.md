---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-50-two-pole-hilbert-schmidt-hardy"
canonical_tex: "zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/main.pdf"
source_sha256: "106c3a96f2b38f07543c70e0859665ae9ba427386d79f57168e85c49558b9f74"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Pole Hilbert--Schmidt Hardy Energies for Small-Noise Range Resolvents Directional Stein Certificates and a Global-Contraction No-Go

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The preceding quarter-power bridge reduced intrinsic peripheral identification for the folded-Gaussian quadratic map to a Hilbert--Schmidt range-resolvent gate. We replace contour solves by an intrinsic time-domain quantity after removing the Perron and negative-parity poles simultaneously. If $$N=T-\lambda_+P_+-\lambda_-P_-,
   \qquad Q=\mathrm I-P_+-P_-,$$ and $U$ embeds the coarse Haar space into the fine one, define $$\mathcal E_B(r)^2
   =\sum_{m\ge0}r^{-2m}
   \frac{\left\lVert U^*N^mQUB\right\rVert_{\mathfrak S_2}^2}{\left\lVert B\right\rVert_{\mathfrak S_2}^2}.$$ Whenever $\operatorname{spr}(N)<r<d_\Gamma:=\inf_{z\in\Gamma}|z|$, we prove the exact Hardy estimate $$\sup_{z\in\Gamma}
   \frac{\left\lVert U^*(z-N)^{-1}QUB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}
   \le
   \frac{\mathcal E_B(r)}{\sqrt{d_\Gamma^2-r^2}},$$ with a symmetric right-range statement. The energies are traces of positive controllability and observability Gramians satisfying discrete Stein equations. A positive Stein supersolution is therefore a deterministic finite-matrix certificate; no global inverse norm or one-step operator contraction is required.

  We also prove why the latter global route is unavailable. The deterministic Koopman operator is an isometry on the stationary $L^2$ space, including the orthogonal complement of the Perron and parity modes. Finite-time small-noise convergence implies that, for every fixed $m$, the norm of the compressed $m$-step noisy operator on this complement tends to one. Thus no noise-uniform fixed-step contraction $q<1$ can close the problem. This no-go leaves directional Gramians untouched.

  For the postcritically finite quadratic map, differentiating the rounded square-root spike profile sharpens the previous envelope to $$\left\lVert \pi_\sigma'\right\rVert_2+\left\lVert g_\sigma'\right\rVert_2
   =\Theta(\sigma^{-1}).$$ Together with an exact block residue identity, this explains the observed $O(\sqrt{\sigma})$ departure of the fine peripheral residues from the outgoing coupling range. A five-scale exact-Haar audit reaches dimension $40960$. At Hardy radius $r=0.85$, the left energies lie between $1.39$ and $1.68$, the right energies between $1.69$ and $2.36$, and the largest direct two-pole bulk product between $1.83$ and $2.31$. The fitted growth exponents are $0$, $0.0844$, and $0$, respectively. These are truncated Hutchinson diagnostics, not validated uniform upper bounds. Conditional on polylogarithmic dyadic Hardy energies and peripheral-factor conditioning, the RH-49 Hilbert--Schmidt gate follows and its strict $n\sigma^2\to\infty$ mesh range is preserved. No arithmetic trace formula, zeta-zero identification, self-adjoint spectral realization, or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Two-Pole Hilbert--Schmidt Hardy Energies for Small-Noise Range Resolvents\
  Directional Stein Certificates and a Global-Contraction No-Go
```

## Markdown 正文

**Keywords:** reduced resolvent; Hardy energy; Stein equation; controllability Gramian; Hilbert--Schmidt operator; Koopman isometry; small noise; Haar coupling.

**MSC 2020:** 47A10; 47B10; 47A55; 37A30; 65R20.

# Introduction {#sec:introduction}

Let $E_n$ be orthogonal averaging on the $n$ equal cells of $[0,1]$, and let $$G_{n,\sigma}=E_n\mathcal K_\sigma E_n$$ be the exact cell-average Galerkin compression of the conditioned folded-Gaussian Markov operator associated with the first quadratic band-merging map. The previous two papers isolated the remaining small-noise mesh obstruction in two steps. First, an exact Schur identity showed that the difference between the intrinsic fine and coarse peripheral Riesz terms starts quadratically in the adjacent Haar couplings [@WangIntrinsic2026]. Second, a stable-rank inequality replaced the mixed Hilbert--Schmidt/operator-norm gate by a purely Hilbert--Schmidt directional product at the cost of one quarter power of $\sigma$ [@WangDirectional2026].

In the notation of the latter paper, it remains sufficient to prove $$\sup_{j\ge0}\mathcal F_{2^jn,\sigma}
 =O((\log(1/\sigma))^a)
 \label{eq:rh49-gate}$$ for some fixed $a$, or more generally $O(\sigma^{-\delta})$ with $\delta\le1/4$. The quantity $\mathcal F_{n,\sigma}$ is a product of two normalized Hilbert--Schmidt resolvent actions on the adjacent coupling ranges. It is strictly weaker than a global reduced-resolvent norm, but a direct contour-by-contour proof still obscures the mechanism that might keep it small.

This paper moves that gate from the frequency domain to the time domain. Both peripheral poles are removed at once, after which the reduced resolvent has an ordinary Laurent expansion about the origin. Weighted Cauchy--Schwarz turns the expansion into a square-summable directional energy. The same square sum is a Gramian trace, so the infinite contour problem has a positive Stein certificate.

## Main results {#main-results .unnumbered}

The analytic content has five parts.

1.  **Simultaneous two-pole decomposition.** If $P_+$ and $P_-$ are the Perron and parity Riesz projections, then $$(z-T)^{-1}
      =\frac{P_+}{z-\lambda_+}
       +\frac{P_-}{z-\lambda_-}
       +(z-N)^{-1}Q.$$ This identity removes both residues without choosing a branch.

2.  **Directional Hardy upper.** For every $r$ strictly between the bulk spectral radius and the minimum contour modulus, one weighted square sum controls every contour node with the explicit factor $(d_\Gamma^2-r^2)^{-1/2}$.

3.  **Positive Stein certificate.** The left and right energies are trace pairings with controllability and observability Gramians. Any positive semidefinite supersolution of the corresponding Stein inequality gives a rigorous upper. Nonnormal transient growth is retained rather than replaced by a spectral-radius heuristic.

4.  **Fixed-step contraction no-go.** In the deterministic stationary geometry, the Koopman operator is an isometry on the full Perron/parity complement. Hence a noise-uniform contraction after any fixed number of steps is incompatible with the small-noise limit. A proof must exploit the special coupling ranges or a time scale increasing with $1/\sigma$.

5.  **Sharp spike derivative and residue ledger.** The rounded one-sided square-root profiles have $L^2$ derivative scale $\sigma^{-1}$, not the earlier coarse $\sigma^{-3/2}$ envelope. The exact block eigenvector identity then makes the fine-side peripheral residue negligible relative to the outgoing Hilbert--Schmidt coupling.

The theorem boundary is equally important. We do not prove a noise-uniform bound for the Hardy energies. The five stored scales strongly suggest a plateau, but the sums are truncated at time $64$, the Hilbert--Schmidt norms are estimated with eight deterministic Rademacher probes, and the spectral data are binary64. The contribution of the paper is a new exact certificate target, a rigorous obstruction to the most obvious global shortcut, and an analytic explanation of why the residues are not the observed gate.

# Folded-Gaussian operator and adjacent Haar channels {#sec:setup}

Let $$f(x)=1-u_{\rm c}x^2,
 \qquad 0\le x\le1,
 \label{eq:map}$$ where $u_{\rm c}=1.543689012692076\ldots$ is the first band-merging parameter. Put $$\phi_\sigma(t)=\frac{1}{\sqrt{2\pi}\sigma}
 e^{-t^2/(2\sigma^2)}$$ and define the conditioned folded kernel $$k_\sigma(x,y)
 =
 \frac{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))}
 {Z_\sigma(x)},
 \qquad
 Z_\sigma(x)=\int_0^1
 \{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))\}\,dy.
 \label{eq:kernel}$$ The Markov operator on observables is $$(\mathcal K_\sigma v)(x)=\int_0^1k_\sigma(x,y)v(y)\,dy.
 \label{eq:markov}$$ For every fixed $\sigma>0$, it is compact and strongly positive on $L^2([0,1])$.

The two simple peripheral branches are $$\begin{aligned}
 \mathcal K_\sigma\mathbf1&=\mathbf1,
 &
 \mathcal K_\sigma^*\pi_\sigma&=\pi_\sigma,
 \label{eq:perron-factors}\\
 \mathcal K_\sigma h_\sigma&=\lambda_-(\sigma)h_\sigma,
 &
 \mathcal K_\sigma^*g_\sigma&=\lambda_-(\sigma)g_\sigma,
 \label{eq:parity-factors}\end{aligned}$$ where $\lambda_-(\sigma)\to-1$. We use the normalizations $\int\pi_\sigma=1$ and $\int h_\sigma g_\sigma=1$. The small-noise boundary-layer and conditioning laws for these factors were obtained in [@WangBoundaryLayer2026; @WangLogConditioning2026].

Let $$V_n=\operatorname{Ran}E_n,
 \qquad
 W_n=\operatorname{Ran}(E_{2n}-E_n),
 \qquad
 V_{2n}=V_n\oplus W_n.$$ Write $U:V_n\to V_{2n}$ and $W:W_n\to V_{2n}$ for the canonical isometric embeddings. Relative to this split, $$T:=G_{2n,\sigma}
 =
 \begin{pmatrix}
  A&B\\ C&D
 \end{pmatrix},
 \qquad
 A=G_{n,\sigma},
 \label{eq:block}$$ where $$B=U^*TW=E_n\mathcal K_\sigma(E_{2n}-E_n),
 \qquad
 C=W^*TU=(E_{2n}-E_n)\mathcal K_\sigma E_n.
 \label{eq:couplings}$$ The left range resolvent appearing in RH-49 is $$U^*(z-T)^{-1}UB,$$ while the right range resolvent is $$C(z-A)^{-1}.$$ The harmless identification of $B$'s domain with $W_n$ is understood.

# Exact simultaneous removal of the two peripheral poles {#sec:two-pole}

The following algebra is valid on any complex Banach space. It is stated for two simple branches, but the proof works for every finite semisimple cluster.

[\[prop:two-pole\]]{#prop:two-pole label="prop:two-pole"} Let $T$ be bounded, and let $\lambda_+\ne\lambda_-$ be simple isolated eigenvalues with Riesz projections $P_+$ and $P_-$. Put $$P_{\rm per}=P_++P_-,
 \qquad
 Q=\mathrm I-P_{\rm per},
 \qquad
 N=T-\lambda_+P_+-\lambda_-P_-.
 \label{eq:N-def}$$ Then $$P_sP_t=\delta_{st}P_s,
 \qquad
 N P_s=P_sN=0,
 \qquad
 NQ=QN=TQ.$$ For every $z$ outside the displayed spectral components and the bulk spectrum, $$\boxed{
 (z-T)^{-1}
 =
 \frac{P_+}{z-\lambda_+}
 +\frac{P_-}{z-\lambda_-}
 +(z-N)^{-1}Q.}
 \label{eq:two-pole-resolvent}$$

Riesz projections of disjoint spectral components commute and annihilate one another [@Kato1995]. The algebraic direct sum $$\operatorname{Ran}P_+\oplus\operatorname{Ran}P_-\oplus\operatorname{Ran}Q$$ is invariant under $T$. On the first two summands, $T$ acts as $\lambda_+$ and $\lambda_-$, while $N$ vanishes. On $\operatorname{Ran}Q$, $N=T$. Inverting each diagonal restriction gives [\[eq:two-pole-resolvent\]](#eq:two-pole-resolvent){reference-type="eqref" reference="eq:two-pole-resolvent"}.

Branchwise deflation is sufficient for a contour solve, because the opposite pole stays a fixed distance from the selected contour. The time-domain expansion below is cleaner after simultaneous deflation: all peripheral terms are explicit residues, and the remaining operator has the measured bulk radius near $0.7$, rather than an eigenvalue near $-1$.

Apply [\[prop:two-pole\]](#prop:two-pole){reference-type="ref" reference="prop:two-pole"} separately to the fine operator $T$ and the coarse operator $A$. We denote the resulting objects by $$(P_{f,\pm},Q_f,N_f)
 \quad\text{and}\quad
 (P_{c,\pm},Q_c,N_c).$$ For a contour $\Gamma$, set $$d_\Gamma=\inf_{z\in\Gamma}|z|.
 \label{eq:dGamma}$$ The fixed Perron and parity circles used in the program both have $d_\Gamma$ close to $0.95$.

# Directional Hilbert--Schmidt Hardy energies {#sec:hardy}

[\[def:energies\]]{#def:energies label="def:energies"} For $r>0$, define $$\begin{aligned}
 \mathcal E_B(r)^2
 &:=
 \sum_{m=0}^{\infty}r^{-2m}
 \frac{
 \left\lVert U^*N_f^mQ_fUB\right\rVert_{\mathfrak S_2}^2
 }{\left\lVert B\right\rVert_{\mathfrak S_2}^2},
 \label{eq:left-energy}\\
 \mathcal E_C(r)^2
 &:=
 \sum_{m=0}^{\infty}r^{-2m}
 \frac{
 \left\lVert CN_c^mQ_c\right\rVert_{\mathfrak S_2}^2
 }{\left\lVert C\right\rVert_{\mathfrak S_2}^2}.
 \label{eq:right-energy}\end{aligned}$$ When a coupling vanishes, its normalized energy is assigned the value zero.

These quantities retain all nonnormal transient growth on the two relevant ranges. They do not ask how $N_f^m$ or $N_c^m$ acts on unrelated directions.

[\[thm:hardy-upper\]]{#thm:hardy-upper label="thm:hardy-upper"} Assume $$\operatorname{spr}(N_f)<r<d_\Gamma.
 \label{eq:hardy-window}$$ Then $$\boxed{
 \sup_{z\in\Gamma}
 \frac{
 \left\lVert U^*(z-N_f)^{-1}Q_fUB\right\rVert_{\mathfrak S_2}
 }{\left\lVert B\right\rVert_{\mathfrak S_2}}
 \le
 \frac{\mathcal E_B(r)}{\sqrt{d_\Gamma^2-r^2}}.}
 \label{eq:left-hardy-upper}$$ Similarly, if $\operatorname{spr}(N_c)<r<d_\Gamma$, then $$\boxed{
 \sup_{z\in\Gamma}
 \frac{
 \left\lVert C(z-N_c)^{-1}Q_c\right\rVert_{\mathfrak S_2}
 }{\left\lVert C\right\rVert_{\mathfrak S_2}}
 \le
 \frac{\mathcal E_C(r)}{\sqrt{d_\Gamma^2-r^2}}.}
 \label{eq:right-hardy-upper}$$

For $|z|>\operatorname{spr}(N_f)$, the Laurent series converges in operator norm: $$U^*(z-N_f)^{-1}Q_fUB
 =
 \sum_{m=0}^{\infty}z^{-m-1}
 U^*N_f^mQ_fUB.$$ The triangle inequality in $\mathfrak S_2$, followed by weighted Cauchy--Schwarz, gives $$\begin{aligned}
 \frac{\left\lVert U^*(z-N_f)^{-1}Q_fUB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}
 &\le
 \sum_{m\ge0}|z|^{-m-1}
 \frac{\left\lVert U^*N_f^mQ_fUB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}\\
 &\le
 \mathcal E_B(r)
 \left(
 \sum_{m\ge0}\frac{r^{2m}}{|z|^{2m+2}}
 \right)^{1/2}\\
 &=
 \frac{\mathcal E_B(r)}{\sqrt{|z|^2-r^2}}.\end{aligned}$$ Taking the supremum and using $|z|\ge d_\Gamma$ proves [\[eq:left-hardy-upper\]](#eq:left-hardy-upper){reference-type="eqref" reference="eq:left-hardy-upper"}. The right statement is identical.

[\[cor:bulk-product\]]{#cor:bulk-product label="cor:bulk-product"} If the same radius $r$ is admissible for both fine and coarse bulks, then the product of the two normalized bulk range actions on $\Gamma$ is at most $$\frac{\mathcal E_B(r)\mathcal E_C(r)}{d_\Gamma^2-r^2}.
 \label{eq:bulk-product-upper}$$

The condition $\operatorname{spr}(N)<r$ guarantees convergence, but the right side of [\[eq:left-hardy-upper\]](#eq:left-hardy-upper){reference-type="eqref" reference="eq:left-hardy-upper"} is not estimated by replacing $\left\lVert N^mX\right\rVert$ with $\operatorname{spr}(N)^m\left\lVert X\right\rVert$. Such a replacement is false for nonnormal operators without a potentially large prefactor. The energy stores the actual directional transients.

# Stein equations and positive certificates {#sec:stein}

The Hardy energies are standard input--output energies in discrete-time systems theory [@ZhouDoyleGlover1996; @HornJohnson2013]. This interpretation is useful here because positivity converts an infinite sum into an auditable matrix inequality.

Let $$X_B=Q_fUB,
 \qquad
 Y_B=U^*.
 \label{eq:XY}$$ For $\operatorname{spr}(N_f)<r$, define the controllability and observability Gramians $$\begin{aligned}
 G_B(r)
 &:=
 \sum_{m\ge0}r^{-2m}
 N_f^mX_BX_B^*(N_f^*)^m,
 \label{eq:controllability}\\
 O_B(r)
 &:=
 \sum_{m\ge0}r^{-2m}
 (N_f^*)^mY_B^*Y_BN_f^m.
 \label{eq:observability}\end{aligned}$$ In finite dimensions these are positive semidefinite matrices. In the Hilbert-space setting they are positive operators whenever the indicated trace pairings are finite.

[\[prop:gramian\]]{#prop:gramian label="prop:gramian"} The Gramians satisfy the Stein equations $$\begin{aligned}
 G_B
 &=X_BX_B^*+r^{-2}N_fG_BN_f^*,
 \label{eq:controllability-stein}\\
 O_B
 &=Y_B^*Y_B+r^{-2}N_f^*O_BN_f.
 \label{eq:observability-stein}\end{aligned}$$ Moreover $$\boxed{
 \mathcal E_B(r)^2
 =
 \frac{\operatorname{tr}(Y_BG_BY_B^*)}{\left\lVert B\right\rVert_{\mathfrak S_2}^2}
 =
 \frac{\operatorname{tr}(X_B^*O_BX_B)}{\left\lVert B\right\rVert_{\mathfrak S_2}^2}.}
 \label{eq:energy-trace}$$ The right energy has the same representation with $X=Q_c$, $Y=C$, and $N=N_c$.

Separating the $m=0$ term from each series gives the Stein equations. For the first trace identity, cyclicity of the trace yields $$\operatorname{tr}(Y_BG_BY_B^*)
 =
 \sum_{m\ge0}r^{-2m}
 \operatorname{tr}\!\left(
  Y_BN_f^mX_BX_B^*(N_f^*)^mY_B^*
 \right),$$ which is the numerator in [\[eq:left-energy\]](#eq:left-energy){reference-type="eqref" reference="eq:left-energy"}. Moving $X_B$ instead of $Y_B$ gives the observability identity. The manipulations are legitimate for nonnegative trace-class partial sums and then by monotone convergence [@Simon2005].

[\[thm:stein-certificate\]]{#thm:stein-certificate label="thm:stein-certificate"} Let $X$ be a Hilbert--Schmidt source, let $\operatorname{spr}(N)<r$, and suppose $H\ge0$ satisfies $$H-r^{-2}NHN^*\ge XX^*.
 \label{eq:stein-super}$$ Then the exact controllability Gramian $$G=\sum_{m\ge0}r^{-2m}N^mXX^*(N^*)^m$$ satisfies $0\le G\le H$. Consequently every bounded observation $Y$ obeys $$\sum_{m\ge0}r^{-2m}\left\lVert YN^mX\right\rVert_{\mathfrak S_2}^2
 \le\operatorname{tr}(YHY^*).
 \label{eq:stein-trace-upper}$$

Iterating [\[eq:stein-super\]](#eq:stein-super){reference-type="eqref" reference="eq:stein-super"} gives, for every $M\ge0$, $$H\ge
 \sum_{m=0}^{M}r^{-2m}N^mXX^*(N^*)^m
 r^{-2M-2}N^{M+1}H(N^*)^{M+1}.$$ The last term is positive. Discard it and let $M\to\infty$. The partial sums increase strongly to $G$, proving $G\le H$. Pairing with $Y^*Y$ and taking traces gives [\[eq:stein-trace-upper\]](#eq:stein-trace-upper){reference-type="eqref" reference="eq:stein-trace-upper"}.

For a computed Hermitian candidate $H$, interval arithmetic may certify the minimum eigenvalue of $$H-r^{-2}NHN^*-XX^*$$ to be nonnegative and may upper-bound $\operatorname{tr}(YHY^*)$. This is a complete directional Hardy certificate. It does not require a validated upper for $\left\lVert (z-N)^{-1}\right\rVert$, $\left\lVert N\right\rVert$, or any singular value of the global resolvent.

# Sharp rounded-spike derivatives {#sec:derivatives}

The left peripheral factors carry the one-sided square-root singularities of the deterministic postcritical density. RH-47 used the direct Gaussian row estimate $\left\lVert \pi_\sigma'\right\rVert_2+\left\lVert g_\sigma'\right\rVert_2
=O(\sigma^{-3/2})$, which is sufficient for spatial compression but is not the intrinsic scale of a rounded square-root spike [@WangLogConditioning2026].

At the critical endpoint, the established microscopic profile is $$\sqrt{\sigma}\,\pi_\sigma(1-\sigma\xi)\longrightarrow R(\xi),
 \qquad
 -\sqrt{\sigma}\,g_\sigma(1-\sigma\xi)\longrightarrow R(\xi),
 \label{eq:R-limit}$$ where $$R(\xi)
 =
 \rho_{\rm c}\int_0^\infty
 \frac{\phi_1(u_{\rm c}q^2-\xi)}
 {\Phi(u_{\rm c}q^2)}\,dq,
 \qquad
 R(\xi)\sim\frac{\rho_{\rm c}}{2\sqrt{u_{\rm c}\xi}}.
 \label{eq:R}$$ Here $\Phi$ is the standard normal distribution function and $\rho_{\rm c}>0$ is the deterministic central density at the critical point [@WangBoundaryLayer2026; @WangLogConditioning2026].

[\[lem:C1-profile\]]{#lem:C1-profile label="lem:C1-profile"} The convergence in [\[eq:R-limit\]](#eq:R-limit){reference-type="eqref" reference="eq:R-limit"} holds in $C^1_{\rm loc}([0,\infty))$ after rescaling. Equivalently, for every fixed $L<\infty$, $$\begin{aligned}
 \sup_{0\le\xi\le L}
 \left|
 \sigma^{3/2}\pi_\sigma'(1-\sigma\xi)+R'(\xi)
 \right|&\longrightarrow0,
 \label{eq:pi-C1}\\
 \sup_{0\le\xi\le L}
 \left|
 \sigma^{3/2}g_\sigma'(1-\sigma\xi)-R'(\xi)
 \right|&\longrightarrow0.
 \label{eq:g-C1}\end{aligned}$$

The proof of the profile theorem writes the endpoint contribution as a Gaussian integral over the critical source scale $x=\sqrt{\sigma}\,q$. After multiplication by $\sqrt{\sigma}$, its integrand converges to the integrand in [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"}. Differentiation in the rescaled target variable $\xi$ multiplies the Gaussian by the linear factor $u_{\rm c}q^2-\xi$. On every compact $\xi$-interval this differentiated integrand is bounded by an integrable polynomial times a Gaussian, uniformly in small $\sigma$. Differentiation under the integral and dominated convergence are therefore valid. Contributions from sources outside the critical window have Gaussian tails, and the regular eigenfactor convergence used in the original profile theorem is uniform on the window. The stationary and signed equations differ only by the limiting sign and $\lambda_-(\sigma)\to-1$, giving [\[eq:pi-C1\]](#eq:pi-C1){reference-type="eqref" reference="eq:pi-C1"}--[\[eq:g-C1\]](#eq:g-C1){reference-type="eqref" reference="eq:g-C1"}.

The standard finite postcritical spike decomposition also gives the differentiated majorant $$|\pi_\sigma'(s\pm t)|+|g_\sigma'(s\pm t)|
 \le C(t+\sigma)^{-3/2},
 \qquad 0\le t\le\delta,
 \label{eq:derivative-majorant}$$ on the singular side of each spike $s$. To see the scale directly, the singular part is a Gaussian rounding of $t_+^{-1/2}$; differentiating and rescaling $t=\sigma\xi$ gives $\sigma^{-3/2}$ times a profile with tail $(1+\xi)^{-3/2}$. The uniformly bounded-variation remainder contributes only $O(\sigma^{-1/2})$ in $L^2$. The finite-spike decomposition for this postcritically finite map is part of the tower/spike construction in [@Misiurewicz1981; @KellerNowicki1992; @Baladi2000; @WangBoundaryLayer2026].

[\[thm:sharp-derivative\]]{#thm:sharp-derivative label="thm:sharp-derivative"} For the stationary and signed parity densities of [\[eq:perron-factors\]](#eq:perron-factors){reference-type="eqref" reference="eq:perron-factors"}--[\[eq:parity-factors\]](#eq:parity-factors){reference-type="eqref" reference="eq:parity-factors"}, $$\boxed{
 \left\lVert \pi_\sigma'\right\rVert_{L^2}
 +\left\lVert g_\sigma'\right\rVert_{L^2}
 =\Theta(\sigma^{-1})}
 \qquad(\sigma\downarrow0).
 \label{eq:sharp-derivative}$$

For the upper bound, square [\[eq:derivative-majorant\]](#eq:derivative-majorant){reference-type="eqref" reference="eq:derivative-majorant"} and integrate: $$\int_0^\delta(t+\sigma)^{-3}\,dt
 =O(\sigma^{-2}).$$ There are only finitely many spike neighborhoods, and the regular remainder is lower order. Hence both derivative norms are $O(\sigma^{-1})$.

For the lower bound, $R$ is nonconstant because $R(\xi)\sim c\xi^{-1/2}$. Choose $L$ such that $\int_0^L|R'(\xi)|^2\,d\xi>0$. By [\[lem:C1-profile\]](#lem:C1-profile){reference-type="ref" reference="lem:C1-profile"} and $y=1-\sigma\xi$, $$\int_{1-\sigma L}^{1}|\pi_\sigma'(y)|^2\,dy
 =
 \sigma^{-2}
 \int_0^L|R'(\xi)+o(1)|^2\,d\xi
 \ge c\sigma^{-2}.$$ The same argument applies to $g_\sigma$, proving the matching lower bound.

# Peripheral residues on the coupling ranges {#sec:residues}

The two-pole bulk is useful only if the explicit residue actions do not reintroduce a power-law loss. The outgoing channel has a particularly simple exact identity.

Let $r=(r_c,r_d)^T$ and $\ell=(\ell_c,\ell_d)^T$ be a normalized fine right/left eigenpair for the block matrix in [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"}: $$Tr=\lambda r,
 \qquad
 T^*\ell=\overline{\lambda}\ell,
 \qquad
 \langle\ell,r\rangle=1.$$ Then $P=r\otimes\ell$.

[\[prop:residue-identity\]]{#prop:residue-identity label="prop:residue-identity"} The coarse-to-coarse block of the residue followed by $B$ is $$\boxed{
 U^*PUB
 =
 r_c\otimes
 \bigl((\overline{\lambda}-D^*)\ell_d\bigr).}
 \label{eq:residue-block}$$ Consequently $$\left\lVert U^*PUB\right\rVert_{\mathfrak S_2}
 =
 \left\lVert r_c\right\rVert\,
 \left\lVert (\overline{\lambda}-D^*)\ell_d\right\rVert.
 \label{eq:residue-factor}$$

The detail component of the left eigenvector equation is $$B^*\ell_c+D^*\ell_d=\overline{\lambda}\ell_d.$$ Thus $B^*\ell_c=(\overline{\lambda}-D^*)\ell_d$. Since $$U^*PUB=r_c\ell_c^*B,$$ substitution proves [\[eq:residue-block\]](#eq:residue-block){reference-type="eqref" reference="eq:residue-block"}. The Hilbert--Schmidt norm of a rank-one operator is the product of its factor norms.

We next record the coupling scale needed to normalize [\[eq:residue-factor\]](#eq:residue-factor){reference-type="eqref" reference="eq:residue-factor"}. RH-49 proved the upper half. The lower half follows by applying the same Haar Taylor expansion on an interior rectangle, where conditioning is exponentially close to one.

[\[prop:B-two-sided\]]{#prop:B-two-sided label="prop:B-two-sided"} There are $a_0,c,C,\sigma_0>0$ such that $$c h\sigma^{-3/2}
 \le\left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \le C h\sigma^{-3/2}
 \label{eq:B-two-sided}$$ whenever $0<\sigma<\sigma_0$ and $h/\sigma<a_0$.

The upper bound is the target-cell Poincaré estimate $$\left\lVert B\right\rVert_{\mathfrak S_2}
 \le\frac{h}{\pi}
 \left\lVert \partial_yk_\sigma\right\rVert_{L^2([0,1]^2)}
 =O(h\sigma^{-3/2})$$ proved in RH-49. For the lower bound, choose a source interval on which $f(x)$ stays a fixed distance from both target endpoints. There $Z_\sigma(x)=1+O(e^{-c/\sigma^2})$, and each row is an ordinary Gaussian up to an exponentially small term. Hence $$\int\!\!\int_{\rm interior}
 |\partial_yk_\sigma(x,y)|^2\,dy\,dx
 \ge c\sigma^{-3}.$$ For a normalized Haar wavelet on a target cell, Taylor expansion about the cell midpoint gives $$\langle k_\sigma(x,\cdot),\psi_{j,h}\rangle
 =-\frac{h^{3/2}}4
 \partial_yk_\sigma(x,y_j)
 +O\!\left(
 h^{5/2}\sup_{\text{cell}}|\partial_y^2k_\sigma|
 \right).$$ Summing the squared coefficients over cells converts the leading term to a constant multiple of $h^2\left\lVert \partial_yk_\sigma\right\rVert_2^2$. Source cell averaging and the Taylor remainder are relative $O(h/\sigma)$ on a slightly smaller interior rectangle. Taking $a_0$ small absorbs both errors and yields the lower bound.

[\[cor:fine-residue\]]{#cor:fine-residue label="cor:fine-residue"} Suppose the fine left Perron and parity factors inherit the rounded-spike detail estimate $$\left\lVert \ell_d\right\rVert=O(h\sigma^{-1})
 \label{eq:left-detail}$$ uniformly in the intrinsic cell-average regime. Then, for either peripheral branch, $$\frac{\left\lVert U^*P_{f,\pm}UB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}
 =O(\sqrt{\sigma}).
 \label{eq:left-residue-small}$$ The estimate [\[eq:left-detail\]](#eq:left-detail){reference-type="eqref" reference="eq:left-detail"} holds for the compressed continuum factors by [\[thm:sharp-derivative\]](#thm:sharp-derivative){reference-type="ref" reference="thm:sharp-derivative"} and cellwise Poincaré. It holds for the intrinsic factors whenever their standard Galerkin factor transfer is uniform at this detail scale.

The peripheral right factors have uniformly bounded $L^2$ norm, and $\left\lVert D\right\rVert$ and $|\lambda|$ are uniformly bounded. Therefore [\[prop:residue-identity\]](#prop:residue-identity){reference-type="ref" reference="prop:residue-identity"} and [\[eq:left-detail\]](#eq:left-detail){reference-type="eqref" reference="eq:left-detail"} give a numerator $O(h\sigma^{-1})$. Divide by the lower bound in [\[eq:B-two-sided\]](#eq:B-two-sided){reference-type="eqref" reference="eq:B-two-sided"}.

The derivative law [\[eq:sharp-derivative\]](#eq:sharp-derivative){reference-type="eqref" reference="eq:sharp-derivative"}, the block identity [\[eq:residue-block\]](#eq:residue-block){reference-type="eqref" reference="eq:residue-block"}, and the compressed-continuum estimate are analytic. A dyadically uniform transfer of [\[eq:left-detail\]](#eq:left-detail){reference-type="eqref" reference="eq:left-detail"} to the finite matrix's own left eigenvectors is a separate factor-stability statement. The numerical audit below tests exactly this transfer; it is not silently promoted to a theorem.

On the right, the Perron residue vanishes exactly: $$CP_{c,+}=0,
 \label{eq:right-perron-zero}$$ because the coarse Perron right vector is constant and $C\mathbf1=0$. For the parity branch the elementary bound $$\frac{\left\lVert CP_{c,-}\right\rVert_{\mathfrak S_2}}{\left\lVert C\right\rVert_{\mathfrak S_2}}
 \le\left\lVert P_{c,-}\right\rVert
 \label{eq:right-parity-projector}$$ shows that polylogarithmic intrinsic projector conditioning is sufficient. Thus the bulk Hardy energies, rather than an unavoidable residue power, are the remaining gate.

# Why fixed-step global contraction cannot work {#sec:no-go}

It is tempting to seek constants $m\ge1$ and $q<1$ such that the noisy operator contracts the complete two-pole complement by $q$ after $m$ steps. The deterministic limit rules this out in the natural stationary Hilbert geometry.

Let $\mu_0$ be the deterministic invariant probability measure on the folded state space, and let $$(U_0v)(x)=v(f(x))
 \label{eq:koopman}$$ be the deterministic Koopman operator. Let $h_0$ be the component-sign observable, so that $U_0h_0=-h_0$. Define $$\mathcal H_0^\circ
 =
 \{\mathbf1,h_0\}^{\perp}
 \subset L^2(\mu_0).
 \label{eq:H0}$$

[\[prop:isometry\]]{#prop:isometry label="prop:isometry"} The Koopman operator $U_0$ is an isometry on $L^2(\mu_0)$, the subspace $\mathcal H_0^\circ$ is invariant, and $$\left\lVert U_0^m|_{\mathcal H_0^\circ}\right\rVert=1
 \qquad\text{for every }m\ge0.
 \label{eq:isometry-complement}$$

Invariance of $\mu_0$ gives $$\left\lVert U_0v\right\rVert_{L^2(\mu_0)}^2
 =
 \int|v\circ f|^2\,d\mu_0
 =
 \int|v|^2\,d\mu_0.$$ Thus $U_0^*U_0=\mathrm I$. The constant function is a unit-modulus eigenvector, and $U_0h_0=-h_0$. For an isometry, every unit-modulus eigenvector $e$ satisfies $U_0^*e=\overline{\lambda}e$. Hence the orthogonal complement of $\mathbf1$ and $h_0$ is invariant. Restricting an isometry to an invariant nonzero subspace remains an isometry, proving [\[eq:isometry-complement\]](#eq:isometry-complement){reference-type="eqref" reference="eq:isometry-complement"}.

Let $\mu_\sigma=\pi_\sigma(x)\,dx$ be the noisy stationary probability, and regard $\mathcal K_\sigma$ as a contraction on $L^2(\mu_\sigma)$. This contraction follows from Jensen's inequality and stationarity. Normalize $h_\sigma$ in $L^2(\mu_\sigma)$, and let $Q_\sigma^\circ$ be the orthogonal projection onto $\{\mathbf1,h_\sigma\}^{\perp}$.

[\[thm:no-go\]]{#thm:no-go label="thm:no-go"} For every fixed integer $m\ge1$, $$\boxed{
 \lim_{\sigma\downarrow0}
 \left\lVert
 Q_\sigma^\circ\mathcal K_\sigma^mQ_\sigma^\circ
 \right\rVert_{L^2(\mu_\sigma)\to L^2(\mu_\sigma)}
 =1.}
 \label{eq:no-go}$$ In particular, there do not exist fixed $m$, $q<1$, and $\sigma_0>0$ for which the displayed norms are bounded by $q$ for all $0<\sigma<\sigma_0$.

Jensen's inequality and orthogonality give the upper bound $1$. For the lower bound, choose a nonzero continuous $v\in\mathcal H_0^\circ$ and normalize it in $L^2(\mu_0)$. Strong stochastic stability gives $\mu_\sigma\to\mu_0$, while the boundary-layer theorem gives $h_\sigma\to h_0$ away from a layer of vanishing $\mu_\sigma$-mass. Therefore $$v_\sigma
 :=
 \frac{Q_\sigma^\circ v}
 {\left\lVert Q_\sigma^\circ v\right\rVert_{L^2(\mu_\sigma)}}
 \longrightarrow v$$ in the varying stationary $L^2$ geometry. For every fixed $m$, the conditioned Gaussian kernels form an approximate identity along the deterministic orbit, so $\mathcal K_\sigma^mv\to U_0^mv$ uniformly for continuous $v$. The same holds for $v_\sigma-v$ after the two scalar peripheral corrections. By [\[prop:isometry\]](#prop:isometry){reference-type="ref" reference="prop:isometry"}, $U_0^mv\in\mathcal H_0^\circ$ and $\left\lVert U_0^mv\right\rVert_{L^2(\mu_0)}=1$. Hence $$\left\lVert
 Q_\sigma^\circ\mathcal K_\sigma^mQ_\sigma^\circ v_\sigma
 \right\rVert_{L^2(\mu_\sigma)}
 \longrightarrow1,$$ which proves the lower bound.

[\[thm:no-go\]](#thm:no-go){reference-type="ref" reference="thm:no-go"} concerns a fixed number of steps and the entire complement. It does not exclude:

-   a mixing time $m=m(\sigma)$ tending to infinity;

-   an anisotropic strong norm not uniformly equivalent to stationary $L^2$;

-   contraction after restriction to the two Haar coupling ranges;

-   a bounded directional Gramian despite unit global norm.

The last possibility is exactly the route measured by $\mathcal E_B(r)$ and $\mathcal E_C(r)$.

# Conditional closure of the RH-49 gate {#sec:closure}

We now state precisely what remains sufficient. Let $\Gamma_+$ and $\Gamma_-$ be the fixed peripheral contours. Assume their distance from both peripheral eigenvalues, when evaluated on the contour, is bounded below uniformly for small $\sigma$.

[\[cond:hardy-control\]]{#cond:hardy-control label="cond:hardy-control"} There exist a radius $r<\min_s d_{\Gamma_s}$, fixed exponents $a_B,a_C,a_P\ge0$, and $C<\infty$ such that, at every required dyadic level, $$\begin{aligned}
 \operatorname{spr}(N_f),\operatorname{spr}(N_c)&<r,
 \label{eq:uniform-radius}\\
 \mathcal E_B(r)&\le C(\log(1/\sigma))^{a_B},
 \label{eq:polylog-left}\\
 \mathcal E_C(r)&\le C(\log(1/\sigma))^{a_C},
 \label{eq:polylog-right}\\
 \left\lVert P_{c,-}\right\rVert
 +\mathfrak r_{f,+}+\mathfrak r_{f,-}
 &\le C(\log(1/\sigma))^{a_P},
 \label{eq:polylog-projectors}\end{aligned}$$ where $$\mathfrak r_{f,s}
 =
 \frac{\left\lVert U^*P_{f,s}UB\right\rVert_{\mathfrak S_2}}{\left\lVert B\right\rVert_{\mathfrak S_2}}.$$

[\[thm:closure\]]{#thm:closure label="thm:closure"} Under [\[cond:hardy-control\]](#cond:hardy-control){reference-type="ref" reference="cond:hardy-control"}, the RH-49 purely Hilbert--Schmidt directional quantity satisfies $$\sup_{j\ge0}\mathcal F_{2^jn,\sigma}
 =
 O((\log(1/\sigma))^a)
 \label{eq:F-polylog}$$ for some fixed $a$ depending only on $a_B,a_C,a_P$. Consequently the RH-49 quarter-power bridge gives $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =
 O\!\left(
 n^{-2}\sigma^{-13/4}(\log(1/\sigma))^a
 \right),
 \label{eq:identification}$$ and every strict schedule $$n(\sigma)\sigma^2\longrightarrow\infty
 \label{eq:mesh}$$ preserves the intrinsic-identification conclusion.

For either contour, insert the two-pole decomposition [\[eq:two-pole-resolvent\]](#eq:two-pole-resolvent){reference-type="eqref" reference="eq:two-pole-resolvent"} into the left and right range actions. The bulk terms are bounded by [\[thm:hardy-upper\]](#thm:hardy-upper){reference-type="ref" reference="thm:hardy-upper"}. The fine residue terms are bounded by $\mathfrak r_{f,+}+\mathfrak r_{f,-}$, multiplied by uniform contour denominators. On the right, the Perron term vanishes by [\[eq:right-perron-zero\]](#eq:right-perron-zero){reference-type="eqref" reference="eq:right-perron-zero"}, and the parity term is bounded by [\[eq:right-parity-projector\]](#eq:right-parity-projector){reference-type="eqref" reference="eq:right-parity-projector"}. Therefore each normalized left and right Hilbert--Schmidt gain is polylogarithmic, and so is their finite sum of products $\mathcal F_{n,\sigma}$. The quarter-power theorem of RH-49 then gives [\[eq:identification\]](#eq:identification){reference-type="eqref" reference="eq:identification"}; its slowly varying closure preserves every strict schedule [\[eq:mesh\]](#eq:mesh){reference-type="eqref" reference="eq:mesh"}.

[\[cor:rounded-closure\]]{#cor:rounded-closure label="cor:rounded-closure"} If the dyadic intrinsic factor transfer in [\[eq:left-detail\]](#eq:left-detail){reference-type="eqref" reference="eq:left-detail"} holds, then $\mathfrak r_{f,+}+\mathfrak r_{f,-}=O(\sqrt{\sigma})$ and the fine residue part of [\[cond:hardy-control\]](#cond:hardy-control){reference-type="ref" reference="cond:hardy-control"} is automatic. The remaining analytic tasks are the left/right Stein supersolutions and a polylogarithmic coarse parity projector bound.

# Five-scale numerical audit {#sec:numerics}

The experiment uses the same exact Haar nesting and sparse row-normalized folded-Gaussian matrices as RH-49. At each noise scale the finest dimension is selected by $$N\sigma=20.48.
 \label{eq:resolution}$$ Both fine and coarse Perron/parity modes are computed in binary64 and biorthogonalized. Eight deterministic Rademacher probes estimate each Hilbert--Schmidt power norm. The powers $$m=0,\ldots,64$$ are accumulated simultaneously for four Hardy radii $0.82,0.85,0.88,0.90$. Eight nodes are used on each peripheral circle. The table reports the primary radius $r=0.85$.

::: {#tab:hardy}
    $\sigma$       $N$   $\mathcal E_B(0.85)$   $\mathcal E_C(0.85)$   max bulk product   bulk radius
  ---------- --------- ---------------------- ---------------------- ------------------ -------------
    $0.0100$    $2048$               $1.5019$               $1.6897$           $1.8574$      $0.6747$
    $0.0040$    $5120$               $1.6793$               $2.1520$           $2.3036$      $0.7179$
    $0.0020$   $10240$               $1.3946$               $2.0999$           $1.8338$      $0.7363$
    $0.0010$   $20480$               $1.4723$               $2.0188$           $1.9618$      $0.7391$
    $0.0005$   $40960$               $1.4748$               $2.3583$           $1.8543$      $0.7480$

  : Five-scale two-pole Hardy audit. The energies are truncated Hutchinson estimates through time $64$, and the bulk radii are binary64 eigensolver candidates. None of the displayed values is an interval upper.
:::

Power-law regression against $\sigma$ gives $$\begin{aligned}
 \mathcal E_B(0.85)&:\quad
 \text{\(\sigma\)-power }+0.02132,
 &
 \text{growth exponent }0,
 \label{eq:left-fit}\\
 \mathcal E_C(0.85)&:\quad
 \text{\(\sigma\)-power }-0.08442,
 &
 \text{growth exponent }0.08442,
 \label{eq:right-fit}\\
 \max_\Gamma(\text{bulk product})&:\quad
 \text{\(\sigma\)-power }+0.01873,
 &
 \text{growth exponent }0.
 \label{eq:product-fit}\end{aligned}$$ The fitted left and right tail bases differ from the independently computed fine bulk radii by less than $0.007$ and $0.008$, respectively. At time $64$, every left normalized power is below $4.0\times10^{-9}$, and every right normalized power is below $1.5\times10^{-8}$. This agreement is evidence that the stored horizon has entered the asymptotic bulk tail, but it is not an interval enclosure of the omitted infinite sum.

The normalized residue actions have fitted vanishing powers $$0.52752\quad\text{(left Perron)},\qquad
 0.55003\quad\text{(left parity)},\qquad
 0.93624\quad\text{(right parity)}.
 \label{eq:residue-fits}$$ The right Perron action is zero to rounding error, below $2.6\times10^{-15}$ at every level. The first two powers closely match the $\sqrt{\sigma}$ mechanism in [\[cor:fine-residue\]](#cor:fine-residue){reference-type="ref" reference="cor:fine-residue"}; the right parity power is consistent with a transition-layer leakage of order $\sigma$ up to slowly varying conditioning.

![Two-pole Hardy-energy audit. (a)--(b) Left and right normalized bulk powers through time $64$. (c) The $r=0.85$ truncated energies and the largest direct bulk gain product remain on a narrow five-scale plateau. (d) Fine Perron/parity and coarse parity residue actions leave the coupling ranges; the coarse Perron action is an exact algebraic zero and is omitted.](<../../../../../zeta_mvp0/papers/RH-50-two-pole-hilbert-schmidt-hardy/figures/two_pole_hardy_energy.pdf>){#fig:hardy width="\\textwidth"}

## What the computation does and does not say

The direct contour products in [1](#tab:hardy){reference-type="ref" reference="tab:hardy"} use the same truncated Laurent sums as the power ledger. The Hardy upper candidates are larger, between approximately $3.4$ and $5.7$ for the separate left/right actions, because Cauchy--Schwarz intentionally discards phase cancellation. That loss is acceptable: only a polylogarithmic upper is needed.

Three validation layers remain absent.

1.  The eight-probe Hutchinson quantities are estimators, not deterministic Hilbert--Schmidt uppers.

2.  The tail after $m=64$ is not enclosed, even though the observed decay base lies well below $r=0.85$.

3.  The sparse hard cutoff, eigenfactors, and bulk radii are not enclosed by interval arithmetic at all five scales.

# What is proved and the next gate {#sec:boundary}

The current state can be summarized without a global resolvent claim.

Exact operator algebra

:   Two-pole decomposition, Hardy upper, Gramian trace identities, and positive Stein supersolution certificates.

Exact negative result

:   No fixed number of noisy steps can contract the complete stationary Perron/parity complement by a noise-uniform factor below one.

Small-noise analysis

:   The rounded square-root left factors have sharp derivative scale $\Theta(\sigma^{-1})$, the outgoing coupling has two-sided Hilbert--Schmidt scale $\Theta(h\sigma^{-3/2})$, and the exact residue block is controlled by the left detail factor.

Conditional closure

:   Polylogarithmic dyadic Hardy energies and peripheral-factor conditioning imply the RH-49 gate and preserve the strict $n\sigma^2\to\infty$ identification range.

Floating evidence

:   Five-scale power sums, tail fits, direct Laurent products, and residue actions through dimension $40960$. These are diagnostics, not validated asymptotic bounds.

The next paper-level target is therefore concrete: construct positive low-complexity supersolutions for the left and right Stein equations, uniformly over dyadic refinement. A useful candidate should exploit three features already visible in the data:

1.  the coupling sources are localized and smoothing;

2.  the two-pole bulk tail decays at a base below $0.75$ on all stored scales;

3.  the deterministic isometric directions are nearly invisible to the coupling ranges, even though they prevent global contraction.

A failed Stein ansatz would also be informative: its positive residual would identify which spatial or temporal sector carries the missing energy. This is substantially more localized than failure of a global pseudospectral bound.

## No arithmetic or Hilbert--Pólya conclusion

Every operator in this paper is generated by one explicit noisy quadratic dynamical system and its cell-average compressions. The results do not construct a self-adjoint Hilbert--Pólya operator, identify an eigenvalue with a Riemann-zeta zero, prove a prime-power trace formula, derive a $T\log T$ counting law, or imply the Riemann hypothesis. They close one operator-theoretic reduction and identify the next rigorous certificate inside the existing spectral program.

# Reproducibility {#sec:reproducibility}

The archive contains:

-   , implementing exact two-pole deflation, Hardy bounds, discrete Gramians, and Stein supersolution checks;

-   , the five-scale exact-Haar power and residue audit;

-   , composing the analytic and floating evidence ledger;

-   , reproducing [1](#fig:hardy){reference-type="ref" reference="fig:hardy"};

-   , checking the exact algebra, Hardy inequality, Gramian identities, supersolution logic, archived slopes, tail decay, residue suppression, and source hashes;

-   , containing the full and smoke pilots, theorem certificate, dependency manifest, summary, and archive verification.

From this directory, the principal commands are

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q

    OPENBLAS_NUM_THREADS=16 OMP_NUM_THREADS=16 \
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_two_pole_hardy_pilot.py

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_hardy_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py

The full pilot is the expensive step. Rebuilding the certificate, figure, tests, manuscript, and archive from the stored full pilot is inexpensive.
