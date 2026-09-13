---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-56-growing-horizon-hard-space-barrier"
canonical_tex: "zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/main.pdf"
source_sha256: "b662ac98ef01ee24b20929fb42e9efec6c13e15a9c903b77ff8cc2c839a488cd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Growing-Horizon Strong-Space Barriers for Directional Hardy Energies An Optimized Exponent No-Go and a Mixed Haar-Channel Overlap Route

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The remaining analytic premise in the intrinsic small-noise identification program is a dyadically uniform budget for two directional Hardy energies. The natural next attempt combines an initial Hilbert-space segment with a postcritical tower/spike spectral gap after a growing mixing horizon. We derive the sharp exponent ledger for that attempt.

  If entering the strong space costs $\sigma^{-p}$, the strong tail decays as $\theta^m$, and the Hardy radius is $r>\theta$, optimization over the switching horizon gives $$\mathcal E(r)=O(\sigma^{-\alpha}),
   \qquad
   \alpha=p\frac{\log(1/r)}{\log(1/\theta)}.$$ The standard folded-Gaussian strong-space black box costs $p=1$ in each direction. RH-54 allows a combined exponent at most $1/4$. At $r=0.85$, the common decay rate would therefore have to satisfy $$\theta\le r^8=0.2724905250\ldots.$$ This requirement is incompatible with the deterministic rates that the global route must accommodate: the physical trace law has edge $\lambda^{-1/2}=0.7718445063\ldots$. More directly, a new Arb contour certificate proves that the deterministic central analytic sector has a genuine two-step resonance of modulus greater than $0.1578803$. Any uniform one-step global tail estimate whose square contains this sector must therefore have rate greater than $0.3973415>r^8$. This is a no-go for the stated black-box norm route, not a lower bound on the actual directional energies.

  We then give the route that survives. For a diagonalizable bulk $N=\sum_j\mu_jP_j$, normalized source $X$, and observation $Y$, $$\mathcal E(r)
   \le
   \sum_j\frac{\left\lVert YP_jX\right\rVert_{\mathfrak S_2}}
   {\sqrt{1-|\mu_j/r|^2}}.$$ Thus the unresolved theorem is a mixed source--resonance--observation overlap budget, not a smaller global spectral radius or a complete eigenbasis condition number. A deterministic all-column five-scale audit has left/right energies at most $1.76031$ and energy divided by the radial Hardy clock at most $1.09463$; production-resolution truncated evidence remains below $2.35829$. These binary64 computations support the overlap route but prove no uniform asymptotic bound. Stage A1 and unconditional intrinsic identification remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Growing-Horizon Strong-Space Barriers for Directional Hardy Energies\
  An Optimized Exponent No-Go and a Mixed Haar-Channel Overlap Route
```

## Markdown 正文

**Keywords:** Hardy energy; growing horizon; transfer operator; strong--weak norm; Riesz overlap; Haar coupling; small noise; route no-go.

**MSC 2020:** 47A10; 47B65; 37D25; 37M25; 65R20.

# Introduction

The fixed-noise intrinsic determinant and its dyadic continuum limit are rigorous. The active problem is to identify the finite matrix's own Perron/parity-deflated bulk uniformly as the Gaussian width tends to zero. RH-48 reduced that problem to directional reduced resolvents, RH-49 moved both actions into the Hilbert--Schmidt class, and RH-50 converted the contour problem into two time-domain Hardy energies [@WangIntrinsic2026; @WangDirectional2026; @WangHardy2026]. Subsequent work proved exact growing-horizon Stein tails, uniform peripheral residues, factor-aware cutoff transfer, and strong--weak adaptive Riesz stability [@WangStructuredStein2026; @WangFactorTransfer2026; @WangHardyTail2026; @WangFactorAware2026; @WangRieszCutoff2026].

Only the analytic Stage A1 Hardy budget remains. With the notation defined below, RH-54 needs $$\mathcal E_B(r)=O(\sigma^{-\alpha_B}),
 \qquad
 \mathcal E_C(r)=O(\sigma^{-\alpha_C}),
 \qquad
 \alpha_B+\alpha_C\le\frac14.
 \label{eq:rh54-budget}$$ Uniform or polylogarithmic bounds would be ideal.

The obvious dynamical proof has two clocks. One propagates the special Haar source in a weak or Hilbert norm until smoothing and mixing place it in the postcritical strong space. The other applies a strong-space spectral gap to the remaining tail. Because the Hardy sum weights time $m$ by $r^{-m}$, a growing switching time is not free. This paper computes that cost before attempting a long tower proof.

The answer is useful but negative: the available isotropic Gaussian entrance power is too expensive by a large margin. Crucially, this does not conflict with the observed bounded-looking energies. The black-box proof discards the fact that the source and observation are adjacent Haar channels. The correct next object is their mixed overlap with the growing resonance cloud.

## Main contributions {#main-contributions .unnumbered}

1.  We prove an exact two-stage Hardy splitting inequality and optimize the switching horizon, including the factor $r^{-M}$.

2.  We derive a critical common-rate criterion. Two standard $\sigma^{-1}$ strong prefactors fit the quarter-power budget only if $\theta\le r^8$.

3.  We separate three radii that cannot be interchanged: the validated central analytic-sector radius, the deterministic physical edge, and a finite-noise bulk-radius diagnostic.

4.  We prove a modal mixed-overlap Hardy upper. It retains precisely the source and observation information destroyed by global norm bounds.

5.  We audit inherited deterministic all-column Hardy traces, production directional traces, and certified finite-matrix tail mechanisms. No fitted five-scale law is promoted to an asymptotic theorem.

# Directional Hardy problem

Let $T=G_{2n,\sigma}$ be the exact fine cell-average matrix and let $V_{2n}=V_n\oplus W_n$ be the adjacent orthogonal Haar split. Write $U$ for the coarse embedding and $$T=\begin{pmatrix}A&B\\C&D\end{pmatrix},
 \qquad
 B=U^*TW,
 \qquad
 C=W^*TU.$$ Remove the simple Perron and parity branches intrinsically. Thus $$\begin{aligned}
 N_f&=T-\lambda_{f,+}P_{f,+}-\lambda_{f,-}P_{f,-},
 &Q_f&=I-P_{f,+}-P_{f,-},\\
 N_c&=A-\lambda_{c,+}P_{c,+}-\lambda_{c,-}P_{c,-},
 &Q_c&=I-P_{c,+}-P_{c,-}.\end{aligned}$$ For a fixed radius above both bulk spectra, define $$\begin{aligned}
 \mathcal E_B(r)^2
 &=\sum_{m\ge0}r^{-2m}
 \frac{\left\lVert U^*N_f^mQ_fUB\right\rVert_{\mathfrak S_2}^2}{\left\lVert B\right\rVert_{\mathfrak S_2}^2},
 \label{eq:left-energy}\\
 \mathcal E_C(r)^2
 &=\sum_{m\ge0}r^{-2m}
 \frac{\left\lVert CN_c^mQ_c\right\rVert_{\mathfrak S_2}^2}{\left\lVert C\right\rVert_{\mathfrak S_2}^2}.
 \label{eq:right-energy}\end{aligned}$$ RH-50 proves that these energies control the normalized range resolvents. RH-52 proves the two-sided adjacent coupling scale $$\left\lVert B\right\rVert_{\mathfrak S_2},\left\lVert C\right\rVert_{\mathfrak S_2}
 =\Theta(h\sigma^{-3/2})
 \label{eq:coupling-scale}$$ uniformly once $h/\sigma$ is small. It also closes every peripheral residue appearing outside [\[eq:left-energy\]](#eq:left-energy){reference-type="eqref" reference="eq:left-energy"}--[\[eq:right-energy\]](#eq:right-energy){reference-type="eqref" reference="eq:right-energy"}. Hence no residue power is hidden in the question studied here.

The radius used in the computational branch is $$r=0.85,
 \label{eq:r-value}$$ while the peripheral contours have minimum modulus close to $0.95$.

# Two-stage growing-horizon estimate

We first state the abstract inequality without imposing a particular strong space.

[\[thm:two-stage\]]{#thm:two-stage label="thm:two-stage"} Let $0<\theta<r<1$ and let $(d_m)_{m\ge0}$ be nonnegative. Suppose that for some integer $M\ge0$, $$d_m\le a_m\quad(0\le m<M),
 \qquad
 d_{M+k}\le S\sigma^{-p}\theta^{M+k}\quad(k\ge0).
 \label{eq:two-stage-premise}$$ Then $$\boxed{
 \sum_{m\ge0}r^{-2m}d_m^2
 \le
 \sum_{m=0}^{M-1}r^{-2m}a_m^2
 +
 \frac{S^2\sigma^{-2p}(\theta/r)^{2M}}
 {1-(\theta/r)^2}.}
 \label{eq:two-stage-upper}$$ If $a_m\le A$ uniformly and $$M(\sigma)
 =\frac{p}{\log(1/\theta)}\log\frac1\sigma+O(1),
 \label{eq:optimized-M}$$ then the corresponding Hardy energy is $$O(\sigma^{-\alpha}),
 \qquad
 \boxed{
 \alpha=p\frac{\log(1/r)}{\log(1/\theta)}.}
 \label{eq:alpha}$$

Split the series immediately before $M$. Substitution of [\[eq:two-stage-premise\]](#eq:two-stage-premise){reference-type="eqref" reference="eq:two-stage-premise"} in the second part gives $$\sum_{k\ge0}r^{-2(M+k)}S^2\sigma^{-2p}\theta^{2(M+k)}
 =\frac{S^2\sigma^{-2p}(\theta/r)^{2M}}
 {1-(\theta/r)^2},$$ which proves [\[eq:two-stage-upper\]](#eq:two-stage-upper){reference-type="eqref" reference="eq:two-stage-upper"}. Under the uniform initial bound, the first part is at most $A^2r^{-2M}/(r^{-2}-1)$, up to an immaterial endpoint factor. Equation [\[eq:optimized-M\]](#eq:optimized-M){reference-type="eqref" reference="eq:optimized-M"} balances the strong entrance scale with the decay clock. Finally $$r^{-M(\sigma)}
 =\sigma^{-p\log(1/r)/\log(1/\theta)}O(1),$$ giving [\[eq:alpha\]](#eq:alpha){reference-type="eqref" reference="eq:alpha"} after taking a square root.

The factor $\theta^M$ in the tail premise is favorable: it grants the global decay clock before the switching time is selected. A weaker estimate of the form $S\sigma^{-p}\theta^k$ after the switch can only increase the Hardy cost, so the obstruction below applies a fortiori to that version.

The theorem is deliberately phrased in terms of the actual directional sequence. A dynamical strong-space proof would obtain its tail premise by first estimating a normalized source in $\mathcal B$, then using a deflated strong-space power bound. The next statement records the resulting necessary rate for this *proof ledger*.

[\[cor:critical-rate\]]{#cor:critical-rate label="cor:critical-rate"} Suppose the left and right applications of [\[thm:two-stage\]](#thm:two-stage){reference-type="ref" reference="thm:two-stage"} have entrance powers $p_B,p_C$ and use one common decay rate $\theta$. To meet [\[eq:rh54-budget\]](#eq:rh54-budget){reference-type="eqref" reference="eq:rh54-budget"}, it is necessary and sufficient at the scalar-ledger level that $$\theta
 \le r^{4(p_B+p_C)}.
 \label{eq:critical-general}$$ For the standard Gaussian strong-space powers $p_B=p_C=1$ and $r=0.85$, $$\boxed{
 \theta\le r^8
 =0.272490525039062\ldots.}
 \label{eq:r8}$$

Sum [\[eq:alpha\]](#eq:alpha){reference-type="eqref" reference="eq:alpha"} in the two directions and require the result to be at most $1/4$. Rearranging gives $\log(1/\theta)\ge4(p_B+p_C)\log(1/r)$, equivalent to [\[eq:critical-general\]](#eq:critical-general){reference-type="eqref" reference="eq:critical-general"}.

## Where the unit strong prefactor enters

The folded-Gaussian transfer maps a weak $L^1$ density into the standard BV/spike strong space with norm $O(\sigma^{-1})$ [@WangRieszCutoff2026]. A proof that treats each normalized Haar channel through this isotropic black-box map therefore carries the strong prefactor $$O(\sigma^{-1})
 \label{eq:standard-entrance}$$ per direction. The separate $L^1\to L^2$ smoothing norm is $O(\sigma^{-1/2})$, but multiplying it into [\[eq:standard-entrance\]](#eq:standard-entrance){reference-type="eqref" reference="eq:standard-entrance"} would double-count the output in the two-stage Hardy sequence. This does not prove that the *normalized* physical channel has strong norm $\Theta(\sigma^{-1})$; it identifies the available isotropic upper after the special Haar cancellation is discarded.

That qualifier matters. A better anisotropic norm or a direct estimate of the normalized coupling range could reduce $p_B$ or $p_C$. The no-go below applies to the standard factorized black-box route, not to every possible strong-space argument.

# Why global strong rates cannot close this ledger

There are three distinct spectral quantities in the preceding papers.

First, the central component square has a validated analytic transfer sector with the global upper $$\operatorname{spr}(\mathcal T_{1,0})
\le0.329642076293171
 \label{eq:central-radius}$$ [@WangValidatedGap2026]. This is a computer-assisted theorem in an analytic Wiener realization. It is not the one-step physical noisy bulk radius in [\[eq:left-energy\]](#eq:left-energy){reference-type="eqref" reference="eq:left-energy"}.

For the present exponent question an upper is not an obstruction; a lower is needed. We therefore augment the RH-13 certificate. Its $50$-coordinate Taylor block and analytic truncation satisfy $$\left\lVert\mathcal T_{1,0}-M\right\rVert_{\ell^1\to\ell^1}
 \le\varepsilon
 =0.000523774672228\ldots.
 \label{eq:sector-tail}$$

[\[thm:sector-resonance\]]{#thm:sector-resonance label="thm:sector-resonance"} Let $$\Gamma_{\rm sec}:=\{z\in\mathbb C:|z-0.2078803|=0.05\}.$$ The deterministic reduced even analytic sector has exactly one eigenvalue, counted with algebraic multiplicity, in $$|w-0.2078803|<0.05.
 \label{eq:sector-circle}$$ Consequently $$\operatorname{spr}(\mathcal T_{1,0})>0.1578803,
 \qquad
 \sqrt{\operatorname{spr}(\mathcal T_{1,0})}>0.3973415407>r^8.
 \label{eq:sector-lower}$$

At $512$-bit precision, Arb isolates exactly one eigenvalue of the active $25\times25$ finite Taylor block in [\[eq:sector-circle\]](#eq:sector-circle){reference-type="eqref" reference="eq:sector-circle"}; its enclosure is centered at $0.2078802977224652710775\ldots$. The full $50\times50$ Taylor truncation has the same nonzero spectrum and only additional zero modes. On $128$ equally spaced circle nodes, directed complex-ball inversion for this full matrix gives maximum $\ell^1$ resolvent norm $108.312568$. Every point of the circle is within $\delta=0.002454123$ of a node. The resolvent identity therefore gives the full-circle bound $$\sup_{z\in\Gamma_{\rm sec}}
 \left\lVert(z-M)^{-1}\right\rVert_1
 \le\frac{108.312568}{1-\delta(108.312568)}
 <147.527090.$$ Multiplication by [\[eq:sector-tail\]](#eq:sector-tail){reference-type="eqref" reference="eq:sector-tail"} is below $0.077271<1$. The operator-valued Rouché theorem, equivalently the Riesz-projector homotopy for $M+t(\mathcal T_{1,0}-M)$, preserves the enclosed algebraic multiplicity [@Kato1995]. The modulus and square-root lower bounds follow from the left edge of the circle. All finite eigenvalues, inverse nodes, the covering step, and scalar comparisons are outward rounded.

Second, exact physical flat traces have root rate $$\rho_{\rm edge}
 =\lambda^{-1/2}
 =0.771844506346038\ldots,
 \label{eq:edge}$$ and the deterministic bulk germ has genuine poles at $z=\pm\sqrt\lambda$ [@WangBulkScattering2026]. A growing cloud is mathematically necessary for any finite-resonance resolution of that edge, although its detailed noisy quantization remains conjectural.

Third, finite-noise matrices have ordinary computed spectral radii. They are diagnostics at selected $(n,\sigma)$, not replacements for either [\[eq:central-radius\]](#eq:central-radius){reference-type="eqref" reference="eq:central-radius"} or [\[eq:edge\]](#eq:edge){reference-type="eqref" reference="eq:edge"}.

[\[prop:black-box-no-go\]]{#prop:black-box-no-go label="prop:black-box-no-go"} Assume that a putative global one-step strong-space estimate has a deterministic two-step restriction containing the analytic sector of [\[thm:sector-resonance\]](#thm:sector-resonance){reference-type="ref" reference="thm:sector-resonance"}. At $r=0.85$, a two-direction application of the standard $p_B=p_C=1$ ledger then cannot satisfy the RH-54 quarter-power budget. Indeed, compatibility forces $\theta^2>0.1578803$, so the smallest certified one-step rate is already larger than the critical value $r^8$. For orientation, insertion of the resonance center and the physical edge gives $$\begin{aligned}
 \theta=\sqrt{0.2078802977\ldots}:
 &\qquad \alpha_B+\alpha_C=0.41385\ldots>\frac14,
 \label{eq:sector-cost}\\
 \theta=\rho_{\rm edge}:
 &\qquad \alpha_B+\alpha_C=1.25511\ldots>\frac14.
 \label{eq:edge-cost}\end{aligned}$$

The exact threshold is [\[eq:r8\]](#eq:r8){reference-type="eqref" reference="eq:r8"}. If a uniform one-step estimate $\left\lVert N^{m}\right\rVert\le C\theta^m$ (in a space containing the analytic sector) were available, its restriction to two steps would force $\theta^2\ge\operatorname{spr}(\mathcal T_{1,0})>0.1578803$. The lower bound in [\[eq:sector-lower\]](#eq:sector-lower){reference-type="eqref" reference="eq:sector-lower"} then contradicts the threshold; substitution in [\[eq:alpha\]](#eq:alpha){reference-type="eqref" reference="eq:alpha"} gives the two orientation values.

The proposition does not show that $\mathcal E_B$ or $\mathcal E_C$ diverges, and it does not turn the RH-15 scattering conjecture into a theorem. It says that a proof which replaces the channel by the full Gaussian entrance norms and then replaces the tail by one global strong rate has already spent too much of the exponent budget. A proof must retain directional cancellation at the entrance, in the tail, or both.

# Mixed resonance-overlap route

The Hardy energy is an input--output quantity. A global power norm estimates it only after maximizing the input and output independently. The following elementary theorem avoids that loss.

[\[thm:overlap\]]{#thm:overlap label="thm:overlap"} Let $N$ be a diagonalizable matrix with $$N=\sum_{j=1}^J\mu_jP_j,
 \qquad
 \max_j|\mu_j|<r,
 \label{eq:modal-decomposition}$$ where the spectral projections need not be orthogonal. For a Hilbert--Schmidt source $X$ and bounded observation $Y$, put $Z_j=YP_jX$. Then $$\boxed{
 \left(\sum_{m\ge0}r^{-2m}\left\lVert YN^mX\right\rVert_{\mathfrak S_2}^2\right)^{1/2}
 \le
 \sum_{j=1}^J
 \frac{\left\lVert Z_j\right\rVert_{\mathfrak S_2}}
 {\sqrt{1-|\mu_j/r|^2}}.}
 \label{eq:overlap-upper}$$

Equation [\[eq:modal-decomposition\]](#eq:modal-decomposition){reference-type="eqref" reference="eq:modal-decomposition"} gives $YN^mX=\sum_j\mu_j^mZ_j$. Apply Minkowski's inequality in the Hilbert space $\ell^2(\mathbb N_0;\mathfrak S_2)$ and sum each geometric sequence: $$\left\|(r^{-m}YN^mX)_{m\ge0}\right\|_{\ell^2(\mathfrak S_2)}
 \le\sum_j\left\lVert Z_j\right\rVert_{\mathfrak S_2}
 \left(\sum_{m\ge0}|\mu_j/r|^{2m}\right)^{1/2}.$$ This is [\[eq:overlap-upper\]](#eq:overlap-upper){reference-type="eqref" reference="eq:overlap-upper"}.

For a simple mode $P_j=v_j\otimes w_j$ with $\langle w_j,v_j\rangle=1$, $$\left\lVert YP_jX\right\rVert_{\mathfrak S_2}
 =\left\lVert Yv_j\right\rVert_2\,\left\lVert X^*w_j\right\rVert_2.
 \label{eq:mixed-mode}$$ The product in [\[eq:mixed-mode\]](#eq:mixed-mode){reference-type="eqref" reference="eq:mixed-mode"} is the desired mixed Haar-channel quantity. Bounding it by $\left\lVert Y\right\rVert\left\lVert P_j\right\rVert\left\lVert X\right\rVert_{\mathfrak S_2}$ would return to the global conditioning problem and lose the mechanism.

[\[cond:overlap\]]{#cond:overlap label="cond:overlap"} For both the fine left triple and coarse adjoint right triple, there are spectral or Riesz-block decompositions such that the corresponding right sides of [\[eq:overlap-upper\]](#eq:overlap-upper){reference-type="eqref" reference="eq:overlap-upper"} are $$O(\sigma^{-\alpha_B})
 \quad\text{and}\quad
 O(\sigma^{-\alpha_C}),
 \qquad
 \alpha_B+\alpha_C\le\frac14,
 \label{eq:overlap-budget}$$ uniformly over every required dyadic level.

If [\[cond:overlap\]](#cond:overlap){reference-type="ref" reference="cond:overlap"} holds at one fixed $r<\min_s d_{\Gamma_s}$, then the RH-54 Stage A1 premise holds with the same exponents. In particular, a uniform or polylogarithmic overlap sum closes the Hardy part of intrinsic identification.

Apply [\[thm:overlap\]](#thm:overlap){reference-type="ref" reference="thm:overlap"} to the normalized source and observation in each of [\[eq:left-energy\]](#eq:left-energy){reference-type="eqref" reference="eq:left-energy"}--[\[eq:right-energy\]](#eq:right-energy){reference-type="eqref" reference="eq:right-energy"}, then invoke the RH-50 Hardy resolvent upper and the RH-54 composition theorem.

## Blocks, clouds, and nonnormality

Diagonalizability is used only to display the target transparently. A Riesz block $N_j$ contributes the corresponding block Hardy norm $\left(\sum_{m\ge0}r^{-2m}\left\lVert YN_j^mP_jX\right\rVert_{\mathfrak S_2}^2\right)^{1/2}$. Jordan blocks add polynomial factors in $m$, which remain summable while the block radius is strictly below $r$. The theorem needed next may therefore group resonances into endpoint/interior annuli or cloud sectors. It need not validate every individual eigenvector of a large nonnormal matrix.

This is also why a sum of individual binary64 eigenvector condition numbers is a poor numerical proxy. It is gauge-sensitive near clustered modes and can be enormous even when the invariant block response is small. Riesz blocks or time-domain all-column traces are the stable diagnostics.

# Deterministic and production audits

The calculations have three evidence levels.

## Deterministic all-column audit

RH-51 and RH-53 use dense exact-Haar matrices with $N\sigma=5.12$. Every source column is propagated; no Hutchinson estimator is used. The exact dense Hardy energy is obtained from a Lyapunov solve, while the complete infinite tail has a deterministic block certificate. The inherited values are listed in [1](#tab:all-column){reference-type="ref" reference="tab:all-column"}.

::: {#tab:all-column}
    $\sigma$   $N$   bulk radius   radial clock   left $\mathcal E$   right $\mathcal E$
  ---------- ----- ------------- -------------- ------------------- --------------------
        0.16    32       0.22555        1.03718             0.90396              1.00265
        0.08    64       0.46217        1.19152             1.16256              1.26528
        0.04   128       0.57418        1.35620             1.33383              1.48454
        0.02   256       0.65648        1.57424             1.40958              1.63399
        0.01   512       0.67466        1.64398             1.46807              1.76031

  : Deterministic binary64 all-column audit at $r=0.85$. The radial clock is $[1-(\rho/r)^2]^{-1/2}$. The maximum energy divided by that clock is $1.09463$.
:::

The largest relative excess of the deterministic finite-horizon plus tail upper over the dense Lyapunov energy is $4.94\times10^{-4}$. Thus the finite-matrix tail mechanism is not the observed wall.

## Production-resolution directional evidence

RH-50 holds $N\sigma=20.48$ and reaches $N=40960$. At $r=0.85$, the left truncated energies lie between $1.39465$ and $1.67934$ and the right values between $1.68967$ and $2.35828$. Fitted tail bases range upward toward approximately $0.742$, remaining below $r$. These values use eight deterministic Rademacher probes and stop at time $64$. They are evidence, not all-column uppers or asymptotic bounds.

![Hardy route audit. (a) The standard two-direction strong-space ledger crosses the quarter-power budget at $\theta=r^8$, below the deterministic physical edge. (b) Dense all-column energies track a modest radial Hardy clock. (c) Production-resolution truncated directional energies remain small over five scales. (d) Growing-horizon block tails are sharp. Panels (b)--(d) are binary64 diagnostics.](<../../../../../zeta_mvp0/papers/RH-56-growing-horizon-hard-space-barrier/figures/growing_horizon_hard_space_barrier.pdf>){#fig:audit width="\\textwidth"}

## Outward-rounded audits

A 256-bit Arb execution evaluates [\[eq:r8\]](#eq:r8){reference-type="eqref" reference="eq:r8"}, the deterministic-edge ledger, and the radial Hardy clock. It encloses $$r^8=0.2724905250390625\ldots$$ and certifies both $r^8<0.28$ and the edge two-direction power $1.25510731191013\ldots>1/4$. Separately, the 512-bit certificate in [\[thm:sector-resonance\]](#thm:sector-resonance){reference-type="ref" reference="thm:sector-resonance"} encloses the finite Taylor eigenvalue and every node of the analytic contour homotopy. Neither audit encloses a production folded-Gaussian noisy eigenproblem.

# Program consequence

The Stage A map is now sharper.

Global fixed-step $L^2$ contraction

:   Already impossible by the deterministic Koopman isometry in RH-50.

Growing-horizon standard strong black box

:   Quantitatively obstructed by [\[prop:black-box-no-go\]](#prop:black-box-no-go){reference-type="ref" reference="prop:black-box-no-go"}: its standard entrance powers require an unrealistically small global rate.

Deterministic finite-matrix tail

:   Closed by RH-53. It converts any verified contracting block into a full all-column Hardy upper.

Directional overlap route

:   Viable. The missing analytic theorem is [\[cond:overlap\]](#cond:overlap){reference-type="ref" reference="cond:overlap"}, preferably for invariant endpoint/interior or cloud-sector Riesz blocks.

Stage A1

:   Open. The present paper marks a failed norm route and a narrower positive target; it does not prove a uniform Hardy budget.

Stage A4 intrinsic identification

:   Still conditional on Stage A1. RH-52 through RH-55 have closed the residue, tail, factor, and adaptive Riesz interfaces, so they need not be revisited.

The next paper should retain the adjacent Haar vanishing moment before strong-space inflation. Two concrete decompositions are natural:

1.  split the source and observation into critical-endpoint and regular interior packets and prove square-summed transport estimates;

2.  group the physical edge into angular cloud sectors and bound the invariant mixed Riesz-block responses without diagonalizing each mode.

The first route is closer to existing Gaussian/Haar derivative estimates; the second interfaces more directly with the deterministic pole geometry.

## No arithmetic or Hilbert--Pólya conclusion

Nothing in this paper supplies an arithmetic trace formula, von Mangoldt or prime-power weights, a zeta-zero spectral identity, a canonical self-adjoint operator, or a $T\log T$ counting law. No Riemann-hypothesis conclusion is drawn. The independent TPC twin-prime branch is not an assumption here.

# Reproducibility and theorem boundary

The archive contains the scalar algebra in , inherited all-column and production ledgers, an Arb scalar audit, tests, hashes, and the figure. Principal commands are

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_hardy_barrier_pilot.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_exponent_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_sector_resonance.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_hardy_barrier_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The two-stage inequality, exponent optimization, critical-rate criterion, and modal-overlap upper are analytic. The inherited finite matrices and their eigendata are binary64. Arb validates only the scalar formulas. The barrier is a no-go for one explicitly stated proof ledger, and the overlap condition remains a target rather than a theorem for the physical family.
