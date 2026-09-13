---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-22-dark-channel-schur-self-energy"
canonical_tex: "zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/dark-channel-schur-self-energy.pdf"
source_sha256: "af7e8266a64ddc35efab94727f5bcd05c6050d80fc4421dba8db9826c32af0bc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dark-Channel Schur Self-Energy in Critical-Branch Returns at a Quadratic Band-Merging Map: Exact Target-Coupling Laws, a Local No-Go Theorem, and a Nested-Complement Route

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/dark-channel-schur-self-energy.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the first algebraic band-merging parameter of $f_u(x)=1-u x^2$, an exact Gaussian return compressed to the two critical branches is almost rank one. Peripheral biorthogonalization does not supply the attenuation needed to match the physical bulk edge, so the next candidate is the spectral-parameter self-energy of the local antisymmetric branch. We test that candidate exactly at the reduced-matrix level and obtain a sharp local no-go result.

  For a bright/dark return $$M=\begin{pmatrix}a&b\\c&d\end{pmatrix},$$ we prove $$\det(\zeta\mathrm I-M)
   = (\zeta-d)\left(\zeta-a-\frac{bc}{\zeta-d}\right).$$ If $\tau$ is a prescribed return eigenvalue, the unique required coupling product is $$p_{\rm req}=(\tau-a)(\tau-d).$$ Moreover $bc/p_{\rm req}$ is exactly the signed fraction of the required self-energy supplied at $\tau$. It is invariant under every diagonal bright/dark gauge. For real $d<\tau<a$, attenuation requires $bc<0$. Even when $p=p_{\rm req}$, the companion root $a+d-\tau$ must also lie in the target disk. Finally, if $|bc|/|a-d|^2<1/4$, Rouché's theorem confines the bright root to $$|\lambda_{m b}-a|<\frac{2|bc|}{|a-d|}.$$

  Seven archived noise scales satisfy $d<\tau_{\rm bulk}<a$. Six have the wrong coupling sign. The only sign-compatible point, $\sigma=10^{-3}$, has $bc/p_{\rm req}=5.5894\times10^{-5}$. Across all seven scales the magnitude coverage is below $0.135$, its maximum has the wrong sign, the small-coupling parameter is below $0.031$, and $|\tau_{\rm bulk}-d|/|\tau_{\rm bulk}|$ lies between $0.976$ and $1.056$. Thus there is no local dark-pole resonance. At $\sigma=10^{-4}$, the exact $2\times2$ root gives one-step radius $0.78970586$, whereas the physical bulk edge is $0.75702308$. Four peripheral/biorthogonal variants and a three-density discretization audit preserve the conclusion. These are ordinary floating-point diagnostics, not interval enclosures.

  The negative result is local. We prove a nested Schur identity showing how an external complement replaces $a,b,c,d$ by spectral-parameter-dependent entries involving $(\zeta\mathrm I-E)^{-1}$. That larger complement can change the sign, provide a near pole, or add a direct bright--external--bright excursion. It is therefore the next precise and falsifiable operator target.
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
  **Dark-Channel Schur Self-Energy in Critical-Branch**\
  **Returns at a Quadratic Band-Merging Map:**\
  Exact Target-Coupling Laws, a Local No-Go Theorem,\
  and a Nested-Complement Route
```

## Markdown 正文

**Keywords:** Gaussian transfer operator; Schur complement; self-energy; bright and dark channels; Feshbach map; non-normal spectrum; quadratic map; spectral approximation.

**MSC 2020:** 37E05; 37D25; 47A10; 47A55; 47B65; 65F15; 65P30.

# Introduction {#sec:introduction}

The small-noise spectrum of a Gaussian perturbation of a quadratic band-merging map has been organized through a sequence of exact and numerical reductions. The deterministic two-step bulk determinant has an exact endpoint pole, and Gaussian noise resolves a growing spectral cloud [@WangBulkScattering2026]. Endpoint singular values produce a half-logarithmic resolution clock, while a boundary word produces an exact time-ordered cycle determinant [@WangEndpointRank2026; @WangTimeOrdered2026]. Riccati packets and a conditioned critical profile then insert the exact Gaussian operator into that cycle [@WangGaussianReturn2026].

The first completion attempt used a single critical branch. It failed for a useful reason: the sibling critical branch has order-one mass, and an unconstrained time lift merely replicates each physical eigenvalue by Floquet rotations [@WangComplement2026]. Resolving both branches gives an exact two-channel factorization and an almost rank-one bright return [@WangSectorBranch2026]. A relative cubic phase and a positive half-weight can both reproduce a one-branch modulus in the symmetric model, but radius agreement alone does not derive either mechanism.

The next test was biorthogonal. Perron/parity-compatible synthesis and analysis maps can be constructed exactly, but coordinate normalization acts by similarity and cannot halve a physical eigenvalue. The dual half-sum is a coordinate projector, not an attenuation. In addition, the two branch histories become nearly parallel, making an exact dark dual increasingly ill-conditioned [@WangBiorthogonal2026]. That paper identified a spectral-parameter bright/dark Schur complement as the next legitimate object.

The present paper performs that test. There is a particularly simple advantage: once a $2\times2$ matrix has been constructed, its local Schur self-energy is not heuristic. It is the exact rational function $bc/(\zeta-d)$. Consequently one can ask three decisive questions without fitting a phase or an attenuation:

1.  what product $bc$ is required to place the physical return target in the spectrum;

2.  whether the observed product has the correct sign and magnitude;

3.  whether the scalar dark pole is close enough to amplify a small coupling.

All three questions have exact algebraic answers.

The answer for the archived local branch matrices is negative. This does not reverse the earlier deterministic or numerical results. It identifies the level at which the missing correction cannot live: the single local antisymmetric branch profile. The same algebra also shows precisely how the route can continue. If the rest of the bulk complement is retained, its resolvent renormalizes all four bright/dark entries. The correct next test is therefore a larger, genuinely spectral-parameter-dependent complement self-energy.

## Main results and logical status {#main-results-and-logical-status .unnumbered}

1.  **Exact scalar Schur law.** We factor the characteristic determinant into a dark factor and a scalar bright Schur function. No normality, symmetry, or perturbative assumption is used.

2.  **Target-coupling identity.** The unique product placing $\tau$ in the local spectrum is $p_{\rm req}=(\tau-a)(\tau-d)$. The ratio $\chi=bc/p_{\rm req}$ obeys $\Sigma_d(\tau)=\chi(\tau-a)$ and $F_b(\tau)=(1-\chi)(\tau-a)$.

3.  **Sign and companion-root obstructions.** For real $d<\tau<a$, one must have $bc<0$. If the target condition is imposed, the other root is $a+d-\tau$; target inclusion need not imply target spectral radius.

4.  **Channel-gauge invariance.** Under every nonzero diagonal rescaling of bright and dark coordinates, $a,d$, the product $bc$, and the scalar Schur function are unchanged. Thus the coupling deficit cannot be repaired by renormalizing either channel.

5.  **Nonresonant small-coupling theorem.** If $|bc|/|a-d|^2<1/4$, one root remains in an explicit disk of radius $2|bc|/|a-d|$ about $a$. Separately, $|\Sigma_d(\zeta)|=|bc|/|\zeta-d|$ makes the possible scalar resonance completely explicit.

6.  **Seven-scale local no-go audit.** Six of seven archived products have the wrong sign. The sole sign-compatible product supplies $5.5894\times10^{-5}$ of the required coupling. The largest magnitude coverage is $0.13457$ and has the wrong sign. These statements concern the archived finite matrices, not an unproved continuum limit.

7.  **Peripheral and resolution robustness.** Raw, biorthogonal, bulk-projected, and bulk-biorthogonal matrices preserve the deficit at $\sigma=10^{-3}$ and $10^{-4}$. Recomputing at three values of $n\sigma$ preserves the relevant signs. No validated-rounding or pseudospectral enclosure is claimed.

8.  **Nested-complement identity.** Eliminating an external block $E$ gives exact effective entries $a_E(\zeta),b_E(\zeta),c_E(\zeta),d_E(\zeta)$. This separates the failed local mechanism from the still-open full-complement mechanism and defines the next calculation.

The resulting implication diagram is $$\label{eq:intro-diagram}
 \boxed{
 \begin{gathered}
 \text{local two-profile dark channel}
 \not\Longrightarrow
 \text{physical bulk attenuation},\\
 \text{channel normalization}
 \not\Longrightarrow
 \text{missing self-energy},\\
 \text{external-complement resolvent}
 \Longrightarrow?
 \text{physical effective determinant}.
 \end{gathered}}$$ The first two non-implications are established at the stated reduced and data-conditional levels. The final arrow remains open.

# Gaussian return and the physical target scale {#sec:setup}

Let $u_{\mathrm c}$ be the root in $(1,2)$ of $$\label{eq:cubic-parameter}
 u^3-2u^2+2u-2=0,
 \qquad
 u_{\mathrm c}=1.543689012692076\ldots,$$ and set $$\label{eq:quadratic-map}
 f(x)=1-u_{\mathrm c}x^2.$$ On the folded interval $[0,1]$, the row-normalized noisy kernel is $$\begin{aligned}
 P_\sigma(x,y)
 &=\frac{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))}{Z_\sigma(x)},
 \label{eq:kernel}\\
 Z_\sigma(x)
 &=\int_0^1\{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))\}\,dy,
 \label{eq:normalizer}\\
 \phi_\sigma(t)&=\frac{1}{\sqrt{2\pi}\sigma}
 e^{-t^2/(2\sigma^2)}.
 \label{eq:normal-density}\end{aligned}$$ Write $\mathcal K_\sigma$ for the backward Markov operator and $\mathcal T_\sigma=\mathcal K_\sigma^2$ for the two-step operator. At every fixed $\sigma>0$, $\mathcal K_\sigma$ is Hilbert--Schmidt and $\mathcal T_\sigma$ is trace class.

The archived branch calculation chooses a component period $k_\sigma$ from the endpoint-resolution clock, constructs two normalized critical profiles, and compresses one complete $k_\sigma$-component return. In left/right coordinates this gives a real matrix $B_\sigma$. Introduce the orthogonal Hadamard matrix $$\label{eq:hadamard}
 U=\frac{1}{\sqrt2}
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}$$ and define the bright/dark matrix $$\label{eq:bright-dark-matrix}
 M_\sigma=U^*B_\sigma U
 =\begin{pmatrix}a_\sigma&b_\sigma\\
                  c_\sigma&d_\sigma\end{pmatrix}.$$ Here $a_\sigma$ is the direct symmetric return, $d_\sigma$ is the local antisymmetric return, and $b_\sigma,c_\sigma$ are directional couplings. The labels "bright" and "dark" refer to these coordinates; $a_\sigma$ and $d_\sigma$ are entries, not generally eigenvalues.

Let $\rho_{\rm bulk}(\sigma)$ be the archived one-step radius of the Perron/parity-extracted physical bulk cloud. The corresponding return-scale target is $$\label{eq:target-return}
 \tau_\sigma=\rho_{\rm bulk}(\sigma)^{2k_\sigma}.$$ The exponent is essential. Comparing $a_\sigma$ directly with $\rho_{\rm bulk}$ would mix a $2k_\sigma$-step return amplitude with a one-step radius. Throughout the paper, Schur algebra is performed at the return scale; one-step radii are taken only after the roots are found.

The number $\rho_{\rm bulk}$ is a reproducible finite-section diagnostic of the physical bulk edge. This paper does not assume or prove that it is an exact eigenvalue of a limiting operator. The local no-go statement is: given this archived target and these archived compressed matrices, the local dark self-energy cannot account for their discrepancy.

# Exact scalar Schur algebra {#sec:scalar-schur}

We first work over $\mathbb C$ and suppress the noise index. Let $$\label{eq:generic-matrix}
 M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
 \qquad p=bc.$$

For $\zeta\ne d$, define $$\label{eq:self-energy}
 \Sigma_d(\zeta)=\frac{p}{\zeta-d},
 \qquad
 F_b(\zeta)=\zeta-a-\Sigma_d(\zeta).$$ The pole $d$ belongs to the eliminated scalar dark block.

[\[prop:determinant-factorization\]]{#prop:determinant-factorization label="prop:determinant-factorization"} For every $\zeta\ne d$, $$\label{eq:determinant-factorization}
 \det(\zeta\mathrm I-M)=(\zeta-d)F_b(\zeta).$$ Equivalently, the polynomial identity $$\label{eq:characteristic-polynomial}
 \det(\zeta\mathrm I-M)=(\zeta-a)(\zeta-d)-p$$ holds for all $\zeta\in\mathbb C$.

Expand the $2\times2$ determinant. Factoring $\zeta-d$ away from its zero gives [\[eq:determinant-factorization\]](#eq:determinant-factorization){reference-type="eqref" reference="eq:determinant-factorization"}. The polynomial identity extends across $\zeta=d$ without asserting that $F_b$ itself is regular there.

This elementary identity is the decisive simplification. It converts the question "can the local dark channel move the bright return to $\tau$?" into a scalar equality.

[\[thm:target-coupling\]]{#thm:target-coupling label="thm:target-coupling"} Let $\tau\ne d$ and define $$\label{eq:required-product}
 p_{\rm req}=(\tau-a)(\tau-d).$$ Then the following are equivalent:

1.  $\tau\in\operatorname{spec}(M)$;

2.  $F_b(\tau)=0$;

3.  $p=p_{\rm req}$.

If also $\tau\ne a$, put $$\label{eq:coverage-ratio}
 \chi(\tau)=\frac{p}{p_{\rm req}}.$$ Then $$\begin{aligned}
 \Sigma_d(\tau)&=\chi(\tau)(\tau-a),
 \label{eq:coverage-self-energy}\\
 F_b(\tau)&=(1-\chi(\tau))(\tau-a),
 \label{eq:coverage-schur}\\
 \det(\tau\mathrm I-M)&=p_{\rm req}-p.
 \label{eq:coverage-determinant}\end{aligned}$$ Thus $\chi$ is exactly the signed self-energy coverage at the target, not a fitted diagnostic.

By [\[eq:characteristic-polynomial\]](#eq:characteristic-polynomial){reference-type="eqref" reference="eq:characteristic-polynomial"}, $\det(\tau\mathrm I-M)=p_{\rm req}-p$, proving the equivalences and [\[eq:coverage-determinant\]](#eq:coverage-determinant){reference-type="eqref" reference="eq:coverage-determinant"}. Dividing $p=\chi(\tau-a)(\tau-d)$ by $\tau-d$ gives [\[eq:coverage-self-energy\]](#eq:coverage-self-energy){reference-type="eqref" reference="eq:coverage-self-energy"}; subtracting it from $\tau-a$ gives [\[eq:coverage-schur\]](#eq:coverage-schur){reference-type="eqref" reference="eq:coverage-schur"}.

[\[cor:sign-obstruction\]]{#cor:sign-obstruction label="cor:sign-obstruction"} Assume $a,d,\tau,p\in\mathbb R$ and $$\label{eq:target-ordering}
 d<\tau<a.$$ Then $p_{\rm req}<0$. In particular, $p\ge0$ cannot place $\tau$ in the spectrum. If $a>d$ and $p>0$, the root continuously attached to $a$ at $p=0$ lies strictly above $a$.

The two factors in [\[eq:required-product\]](#eq:required-product){reference-type="eqref" reference="eq:required-product"} have opposite signs. For the last statement, the real roots are $$\label{eq:real-roots-positive-p}
 \lambda_\pm=\frac{a+d\pm\sqrt{(a-d)^2+4p}}{2},$$ and $\sqrt{(a-d)^2+4p}>a-d$.

The target condition has a second, often overlooked consequence.

[\[prop:companion-root\]]{#prop:companion-root label="prop:companion-root"} If $p=p_{\rm req}$, then $$\label{eq:companion-factorization}
 \det(\zeta\mathrm I-M)
 =(\zeta-\tau)\bigl(\zeta-(a+d-\tau)\bigr).$$ Consequently $\tau$ can be the spectral-radius target only if $$\label{eq:companion-condition}
 |a+d-\tau|\le |\tau|.$$ For positive real roots this reduces to $a+d\le2\tau$.

Once one root is $\tau$, the trace identity says that the other is $a+d-\tau$. The spectral-radius condition is immediate.

Thus the required product is necessary and sufficient for target *inclusion*, but it need not be sufficient for target *dominance*. This distinction becomes visible in the archived data.

## Gauge invariance within the bright/dark splitting

Let $D=\operatorname{diag}(\alpha,\beta)$ with $\alpha\beta\ne0$. The channel-preserving coordinate change $M_D=D^{-1}MD$ gives $$\label{eq:diagonal-gauge}
 M_D=
 \begin{pmatrix}
 a&\alpha^{-1}\beta b\\
 \beta^{-1}\alpha c&d
 \end{pmatrix}.$$

[\[prop:gauge-invariance\]]{#prop:gauge-invariance label="prop:gauge-invariance"} Under [\[eq:diagonal-gauge\]](#eq:diagonal-gauge){reference-type="eqref" reference="eq:diagonal-gauge"}, $a,d,p=bc$, $\Sigma_d$, $F_b$, and $p_{\rm req}$ are invariant.

The two off-diagonal scale factors cancel in their product. Every stated quantity depends only on $a,d,p$ and the spectral parameter.

This is narrower than invariance under an arbitrary similarity. A general similarity can mix what is called bright and dark. Once the physical symmetric/antisymmetric splitting [\[eq:hadamard\]](#eq:hadamard){reference-type="eqref" reference="eq:hadamard"} has been fixed, however, changing the normalization of either channel cannot alter the coupling deficit. This complements the biorthogonal gauge theorem of [@WangBiorthogonal2026].

# Nonresonance and a small-coupling root bound {#sec:bounds}

For a scalar dark block the resolvent estimate is an equality: $$\label{eq:scalar-resolvent-bound}
 |\Sigma_d(\zeta)|
 =\frac{|p|}{|\zeta-d|}.$$ Therefore a small product can have an order-one effect only if the target is close to the dark pole. The ratio $$\label{eq:pole-distance-ratio}
 \delta_{\rm pole}(\tau)=\frac{|\tau-d|}{|\tau|}$$ is a natural return-scale nonresonance diagnostic when $\tau\ne0$.

Away from resonance, a direct root bound is available. It is useful because it does not expand a square root or choose a branch.

[\[thm:root-disk\]]{#thm:root-disk label="thm:root-disk"} Suppose $a\ne d$ and $$\label{eq:small-coupling-parameter}
 \varepsilon=\frac{|p|}{|a-d|^2}<\frac14.$$ Then $M$ has exactly one eigenvalue $\lambda_a$ in $$\label{eq:root-disk}
 |\zeta-a|<r,
 \qquad
 r=\frac{2|p|}{|a-d|}.$$ In particular, $$\label{eq:root-shift-bound}
 |\lambda_a-a|<\frac{2|p|}{|a-d|}.$$ The other eigenvalue is similarly confined about $d$.

On the circle $|\zeta-a|=r$, the reverse triangle inequality gives $$\label{eq:rouche-lower}
 |(\zeta-a)(\zeta-d)|
 \ge r(|a-d|-r).$$ Writing $r=2\varepsilon|a-d|$ yields $$\label{eq:rouche-comparison}
 r(|a-d|-r)
 =2\varepsilon(1-2\varepsilon)|a-d|^2
 >\varepsilon|a-d|^2=|p|,$$ where the strict inequality is equivalent to $\varepsilon<1/4$. Also $r<|a-d|/2$, so the disk contains $a$ but not $d$. Rouché's theorem shows that $(\zeta-a)(\zeta-d)-p$ and $(\zeta-a)(\zeta-d)$ have the same number of zeros there, namely one. The argument about $d$ is identical.

[\[cor:necessary-scale\]]{#cor:necessary-scale label="cor:necessary-scale"} Under the hypotheses of [\[thm:root-disk\]](#thm:root-disk){reference-type="ref" reference="thm:root-disk"}, if a desired target obeys $|\tau-a|>2|p|/|a-d|$, then the eigenvalue continuously attached to $a$ cannot equal $\tau$.

This theorem is deliberately elementary. It does not attempt a pseudospectral bound for a large non-normal complement. Its role is to settle the scalar local channel before such complications arise [@Kato1995; @StewartSun1990; @TrefethenEmbree2005].

# Exact nested-complement route {#sec:nested-schur}

The local no-go theorem would be a global dead end only if the local dark profile exhausted the complement. It does not. The exact algebra for the larger problem makes the distinction explicit.

Let a finite-dimensional return be ordered as bright, local dark, and external complement: $$\label{eq:three-block-matrix}
 \mathcal M=
 \begin{pmatrix}
  a&b&B\\
  c&d&R\\
  C&S&E
 \end{pmatrix}.$$ Here $B,R$ are rows, $C,S$ are columns, and $E$ acts on an arbitrary finite-dimensional external space. Whenever $\zeta\mathrm I-E$ is invertible, write $$\label{eq:external-resolvent}
 G_E(\zeta)=(\zeta\mathrm I-E)^{-1}$$ and define $$\begin{aligned}
 a_E(\zeta)&=a+B G_E(\zeta)C,
 \label{eq:a-effective}\\
 b_E(\zeta)&=b+B G_E(\zeta)S,
 \label{eq:b-effective}\\
 c_E(\zeta)&=c+R G_E(\zeta)C,
 \label{eq:c-effective}\\
 d_E(\zeta)&=d+R G_E(\zeta)S.
 \label{eq:d-effective}\end{aligned}$$

[\[thm:nested-schur\]]{#thm:nested-schur label="thm:nested-schur"} For every $\zeta$ in the resolvent set of $E$, $$\begin{aligned}
 \det(\zeta\mathrm I-\mathcal M)
 &=\det(\zeta\mathrm I-E)
 \det\begin{pmatrix}
 \zeta-a_E(\zeta)&-b_E(\zeta)\\
 -c_E(\zeta)&\zeta-d_E(\zeta)
 \end{pmatrix}.
 \label{eq:nested-determinant}\end{aligned}$$ If also $\zeta\ne d_E(\zeta)$, then $$\begin{aligned}
 \det(\zeta\mathrm I-\mathcal M)
 &=\det(\zeta\mathrm I-E)\,[\zeta-d_E(\zeta)]
 F_{b,E}(\zeta),
 \label{eq:nested-scalar-factorization}\\
 F_{b,E}(\zeta)
 &=\zeta-a_E(\zeta)
 -\frac{b_E(\zeta)c_E(\zeta)}{\zeta-d_E(\zeta)}.
 \label{eq:nested-bright-function}\end{aligned}$$

Write $\zeta\mathrm I-\mathcal M$ as a $2\times2$ block matrix with the first two coordinates in the upper-left block and $\zeta\mathrm I-E$ in the lower-right block. Block Gaussian elimination gives the determinant of $\zeta\mathrm I-E$ times its Schur complement. Multiplying the off-diagonal blocks produces exactly [\[eq:a-effective\]](#eq:a-effective){reference-type="eqref" reference="eq:a-effective"}--[\[eq:d-effective\]](#eq:d-effective){reference-type="eqref" reference="eq:d-effective"}. Applying [\[prop:determinant-factorization\]](#prop:determinant-factorization){reference-type="ref" reference="prop:determinant-factorization"} to the resulting effective $2\times2$ matrix proves the second factorization. See [@Zhang2005; @HornJohnson2013; @SjoestrandZworski2007] for the general Schur and Grushin frameworks.

Relative to the original direct entry $a$, the full bright self-energy is $$\label{eq:full-self-energy}
 \Sigma_{\rm full}(\zeta)
 =B G_E(\zeta)C
 +\frac{b_E(\zeta)c_E(\zeta)}{\zeta-d_E(\zeta)}.$$ The first term is a direct bright--external--bright excursion. The second is a dark excursion whose entrance, exit, and pole have all been dressed by the external resolvent. The failed local model is obtained by deleting $E,B,C,R,S$, leaving only $bc/(\zeta-d)$.

The external block can change the conclusion in three mathematically distinct ways:

1.  $B G_E C$ can supply attenuation without passing through the local dark profile;

2.  $b_Ec_E$ can acquire a different sign or phase from $bc$;

3.  a pole of $G_E$ or a zero of $\zeta-d_E(\zeta)$ can provide genuine resonant amplification.

Therefore failure of the scalar local channel does not imply failure of the full complement. It says exactly which terms in [\[eq:full-self-energy\]](#eq:full-self-energy){reference-type="eqref" reference="eq:full-self-energy"} must be measured next.

For bounded operators the same elimination identity holds wherever the required resolvents exist. Determinant statements require the usual trace- class or Fredholm hypotheses [@GohbergKrein1969; @Baladi2000]. We do not claim those uniform hypotheses in the small-noise limit here.

# Numerical protocol and reproducibility {#sec:numerics}

The primary calculation reads the committed RH-20 and RH-21 matrices rather than rebuilding the expensive Gaussian operator. This makes the Schur audit fast and exactly reproducible from its declared inputs. The optional resolution audit rebuilds six sparse matrices from the original operator. All scripts, tests, source hashes, tables, and figure data are archived with the paper [@WangDarkSchurCode2026].

## Seven-scale audit

For each archived row we perform the following steps:

1.  read $k_\sigma$, $\rho_{\rm bulk}$, and the four entries of $M_\sigma$;

2.  form $\tau_\sigma=\rho_{\rm bulk}^{2k_\sigma}$;

3.  compute $p_\sigma=b_\sigma c_\sigma$ and $p_{{\rm req},\sigma}=(\tau_\sigma-a_\sigma)
     (\tau_\sigma-d_\sigma)$;

4.  evaluate the exact Schur function, both eigenvalues, the channel-gauge invariants, the pole distance, and the root-disk bound;

5.  convert the root attached to $a_\sigma$ back to a one-step radius by taking the $2k_\sigma$-th root.

The determinant and coverage identities are checked numerically. Their maximum residual over the seven-scale and peripheral tables is $6.94\times10^{-18}$.

## Peripheral variants

At $\sigma=10^{-3}$ and $10^{-4}$ we audit four matrices from RH-21: raw Euclidean, raw biorthogonal, Perron/parity-bulk Euclidean, and Perron/parity-bulk biorthogonal. Each left/right matrix is transformed by the same fixed $U$ in [\[eq:hadamard\]](#eq:hadamard){reference-type="eqref" reference="eq:hadamard"} before the Schur diagnostics are applied. This tests whether the conclusion is an artifact of one packet normalization or peripheral projection.

## Resolution audit

For $\sigma=10^{-3}$ and $10^{-4}$, we independently rebuild the sparse row-normalized Gaussian matrix at $$\label{eq:grid-densities}
 n\sigma\in\{10.24,15.36,20.48\}.$$ The packet windows, component period, critical profile construction, and physical target are held fixed. This is a discretization-stability check, not a proof of convergence as $n\to\infty$ or $\sigma\to0$.

The implementation uses NumPy and Matplotlib [@HarrisEtAl2020; @Hunter2007]. Unit tests verify the exact determinant, target, gauge, root-disk, and nested-complement identities on independent real and complex matrices.

# Seven-scale local no-go result {#sec:seven-scale}

contains the decisive return-scale data. Every row has $d<\tau<a$, so [\[cor:sign-obstruction\]](#cor:sign-obstruction){reference-type="ref" reference="cor:sign-obstruction"} requires a negative product. Only $\sigma=10^{-3}$ has that sign.

Several conclusions follow directly.

#### Sign.

Six values of $p$ are positive while all seven required products are negative. Their self-energies push the bright root upward rather than attenuating it. The sole sign-compatible point is $\sigma=10^{-3}$.

#### Magnitude.

At $\sigma=10^{-3}$, $$\label{eq:sign-compatible-ratio}
 \frac{p}{p_{\rm req}}=5.589424987\times10^{-5}.$$ The actual bright-root displacement is only $2.46796\times10^{-5}$ of the required displacement $\tau-a$. Across all seven rows, $|p/p_{\rm req}|$ ranges from $1.588\times10^{-5}$ to $0.13457$. The maximum occurs at $\sigma=5\times10^{-4}$ with the wrong sign.

#### No scalar resonance.

The pole-distance ratio [\[eq:pole-distance-ratio\]](#eq:pole-distance-ratio){reference-type="eqref" reference="eq:pole-distance-ratio"} lies in $$\label{eq:pole-distance-range}
 0.97574\le\delta_{\rm pole}(\tau)\le1.05520.$$ Thus the target is roughly one target modulus away from $d$ at every scale. The scalar denominator does not amplify the observed product enough to change the conclusion.

#### Small coupling.

The parameter $\varepsilon=|p|/|a-d|^2$ lies between $3.97\times10^{-6}$ and $3.10\times10^{-2}$, so [\[thm:root-disk\]](#thm:root-disk){reference-type="ref" reference="thm:root-disk"} applies to every row. The exact local root moves by at most $8.37\%$ of the required return displacement in the audit; that largest motion again has the wrong sign.

#### Companion root.

If the observed product were replaced by $p_{\rm req}$, the target would be the leading root only at the last three scales. At the first four scales, including the sole sign-compatible point, the companion $a+d-\tau$ has larger modulus. Target inclusion would still fail to close the local spectral radius.

![Diagnostic coupling homotopy $p(s)=(1-s)p+s p_{\rm req}$. At $\sigma=10^{-3}$, replacing the observed product by $p_{\rm req}$ inserts the physical target as the lower root while the root attached to $a$ ends at the larger companion root. At $\sigma=10^{-4}$ the target is the leading root and the tracked branch reaches it. The interpolation visualizes the companion obstruction; it is not proposed as a physical deformation.](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/figures/required_coupling_homotopy.pdf>){#fig:coupling-homotopy width="\\textwidth"}

![Seven-scale Schur audit. Top left: signed coupling coverage; only one point has the required sign. Top right: magnitude coverage, colored by sign compatibility. Bottom left: the exact local Schur root stays close to the direct bright entry and above the physical edge. Bottom right: root motion is small while the dark pole remains nonresonant.](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/figures/local_dark_schur_no_go.pdf>){#fig:local-no-go width="\\textwidth"}

converts the return-scale algebra back to one-step radii. The exact local root exceeds the physical edge by between $0.02964$ and $0.12348$. At the smallest noise, $$\begin{aligned}
 \rho_{\rm local}&=0.7897058595,
 &\rho_{\rm bulk}&=0.7570230790,
 &\rho_{\rm local}-\rho_{\rm bulk}&=0.0326827805.
 \label{eq:smallest-radius-gap}\end{aligned}$$ The local self-energy changes the direct-bright radius only in the seventh decimal place there.

[\[cor:data-no-go\]]{#cor:data-no-go label="cor:data-no-go"} For each of the seven archived matrices, the observed scalar local dark self-energy fails to place $\tau_{\rm bulk}$ at the leading bright root. At six scales the target sign condition already fails. At the remaining scale the coupling magnitude and companion-root conditions fail by the amounts stated above.

Combine [\[thm:target-coupling,cor:sign-obstruction,prop:companion-root\]](#thm:target-coupling,cor:sign-obstruction,prop:companion-root){reference-type="ref" reference="thm:target-coupling,cor:sign-obstruction,prop:companion-root"} with [\[tab:seven-scale-coupling\]](#tab:seven-scale-coupling){reference-type="ref" reference="tab:seven-scale-coupling"}. The root and radius statements are direct evaluations of the same $2\times2$ characteristic polynomial.

The qualifier "data-conditional" is important. It is an exact conclusion about the supplied decimal matrices and target values, supported but not converted into a continuum theorem by the floating-point calculations.

# Peripheral and discretization robustness {#sec:robustness}

## Four peripheral/biorthogonal reductions

gives the two tail-scale audits. At $\sigma=10^{-3}$ all four products have the correct negative sign but cover only $5.59\times10^{-5}$ to $1.13\times10^{-4}$ of the requirement. At $\sigma=10^{-4}$ all four products are positive and therefore have the wrong sign. Biorthogonalization and Perron/parity extraction change the direct bright return, but they do not promote the local dark correction to the required scale.

::: {#tab:peripheral-audit}
  $\sigma$    compression                  $p/p_{\rm req}$   local radius   radius gap
  ----------- ------------------- ------------------------ -------------- ------------
  $10^{-3}$   raw Euclidean          $5.5894\times10^{-5}$     $0.791254$   $0.052112$
              raw biorthogonal       $6.2686\times10^{-5}$     $0.783898$   $0.044756$
              bulk Euclidean         $1.1308\times10^{-4}$     $0.761115$   $0.021974$
              bulk biorthogonal      $1.0524\times10^{-4}$     $0.761319$   $0.022178$
  $10^{-4}$   raw Euclidean         $-1.5877\times10^{-5}$     $0.789706$   $0.032683$
              raw biorthogonal      $-1.6305\times10^{-5}$     $0.788348$   $0.031325$
              bulk Euclidean        $-1.6986\times10^{-5}$     $0.782483$   $0.025460$
              bulk biorthogonal     $-1.7148\times10^{-5}$     $0.782493$   $0.025470$

  : Peripheral/biorthogonal Schur audit. The radius gap is the exact local Schur-root radius minus the archived physical bulk radius.
:::

![Robustness under four entrance/exit choices. Bulk extraction narrows the direct radius gap, but the local dark self-energy remains nearly invisible. At $\sigma=10^{-4}$ every local coupling has the wrong sign.](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/figures/peripheral_schur_robustness.pdf>){#fig:peripheral-robustness width="\\textwidth"}

The bulk projection is still useful: at $\sigma=10^{-3}$ it reduces the radius gap from $0.05211$ to about $0.0221$. The point is not that peripheral extraction does nothing. The point is that the remaining local dark Schur correction is orders of magnitude too small to finish the job.

## Three-density sign audit

The products at $\sigma=10^{-3}$ remain negative as $n\sigma$ increases through $10.24,15.36,20.48$, with $$\label{eq:resolution-ratio-dense}
 \frac{p}{p_{\rm req}}
 =5.5463\times10^{-5},\quad
  5.5782\times10^{-5},\quad
  5.5894\times10^{-5}.$$ At $\sigma=10^{-4}$ the product remains positive, giving signed ratios $$\label{eq:resolution-ratio-small}
 -2.5812\times10^{-5},\quad
 -1.3063\times10^{-5},\quad
 -1.5877\times10^{-5}.$$ The magnitude is not monotone at the smaller noise, but the sign obstruction and order-of-magnitude deficit are stable.

![Three-density recomputation. The symlogarithmic vertical scale shows both the tiny observed product and the much larger negative required product. At $\sigma=10^{-3}$ the signs agree but the magnitudes do not; at $\sigma=10^{-4}$ the signs disagree at all three resolutions.](<../../../../../zeta_mvp0/papers/RH-22-dark-channel-schur-self-energy/figures/resolution_sign_audit.pdf>){#fig:resolution-audit width="\\textwidth"}

This check addresses a narrow numerical concern: the products are small, so their sign should not be inferred from one grid alone. It does not replace interval arithmetic, a norm-resolvent convergence theorem, or a uniform conditioning estimate [@Chatelin1983].

# What the negative result does and does not say {#sec:scope}

The local no-go result eliminates one mechanism: $$\label{eq:failed-mechanism}
 \text{direct bright return}
 \longrightarrow
 \text{one local antisymmetric profile}
 \longrightarrow
 \text{direct bright return}.$$ It does not eliminate the deterministic endpoint pole, the endpoint-rank clock, the observed Gaussian cloud, the exact branch factorization, or the possibility of a larger complement self-energy. In particular, it makes no statement about the Riemann hypothesis or a Hilbert--Pólya operator.

Three tempting overinterpretations should be avoided.

#### A tiny dark eigenvalue is not itself the obstruction.

The relevant quantity is not $d$ alone but $bc/(\tau-d)$. A tiny $d$ could still matter if $\tau$ approached it or if $bc$ were sufficiently large. The audit separately shows that neither happens locally.

#### Target inclusion is not target spectral radius.

Replacing $p$ by $p_{\rm req}$ puts $\tau$ in the spectrum by construction. At four scales the companion root remains larger. Any effective determinant argument must control all nearby roots, not fit one scalar equation.

#### The full complement is not a scalar dark mode.

In [\[eq:full-self-energy\]](#eq:full-self-energy){reference-type="eqref" reference="eq:full-self-energy"}, the external resolvent can be non-normal, spectral-parameter dependent, and high dimensional. Its norm can be much larger than inverse spectral distance [@TrefethenEmbree2005]. The scalar nonresonance result cannot be transferred to it without a resolvent estimate.

# A falsifiable next-stage roadmap {#sec:roadmap}

The nested identity turns the next stage into a sequence of concrete tests.

1.  **Fix the physical bright packet.** Use the canonical Perron/parity-complement pair from RH-21, so the entrance and exit maps are not changed while the complement is enlarged.

2.  **Define the external block before solving.** Split the complement into the local dark profile and an external packet/ bulk space. Record $B,C,R,S,E$ in [\[eq:three-block-matrix\]](#eq:three-block-matrix){reference-type="eqref" reference="eq:three-block-matrix"}; do not infer them from a fitted root.

3.  **Evaluate shifted actions.** At $\zeta=\tau_\sigma$ and on a small contour around it, compute $G_E(\zeta)C$ and $G_E(\zeta)S$ by sparse shifted solves or a rational Krylov method. Materializing $G_E$ is unnecessary.

4.  **Audit the four dressed entries.** Separate the direct excursion $B G_E C$ from the dressed dark term in [\[eq:full-self-energy\]](#eq:full-self-energy){reference-type="eqref" reference="eq:full-self-energy"}. Compare the total self-energy with the exact required shift $\tau-a$, including sign and phase.

5.  **Test stability before asymptotics.** Repeat in grid density, packet-window width, and external-space dimension. If the correction is unstable or remains too small, the packet-complement mechanism is falsified at this level.

6.  **Only then seek contour control.** If the full correction has the right scale, establish resolvent and determinant bounds on a contour and use Rouché/Fredholm arguments to compare root counts. A value match at one $\zeta$ is not enough.

This roadmap has a meaningful stopping criterion. The next calculation must produce an order-$|\tau-a|$ correction with the correct sign and stable contour behavior. If it does not, the current spectral-packet route should not be promoted by adding another fitted phase. If it does, the nested identity identifies the exact terms for a theorem.

# Conclusion {#sec:conclusion}

The spectral-parameter dark-channel test can be settled completely at the local two-profile level. The exact Schur function is $$\label{eq:conclusion-schur}
 F_b(\zeta)=\zeta-a-\frac{bc}{\zeta-d},$$ and the required target product is $$\label{eq:conclusion-target}
 p_{\rm req}=(\tau-a)(\tau-d).$$ These identities expose sign, magnitude, pole-distance, root-motion, and companion-root obstructions without a fitted parameter.

For the archived seven-scale family, the local antisymmetric profile does not close the physical bulk gap. Six products have the wrong sign; the one with the correct sign is smaller than required by a factor about $1.79
\times10^4$. The result survives peripheral/biorthogonal variants and the reported resolution audit. This is a useful negative result because it prevents a coordinate or scalar-resonance effect from being mistaken for a physical completion.

The route is nevertheless sharper, not closed. The exact nested Schur identity shows that a larger complement contributes a direct external self-energy and dresses the local dark entrance, exit, and pole. Measuring those terms is the next well-posed step. It will either produce the missing attenuation with contour-stable control or provide a stronger and genuinely global no-go result.

# Data and code availability {#data-and-code-availability .unnumbered}

Source code, unit tests, input hashes, generated CSV tables, JSON metadata, and vector/raster figures are available in the accompanying repository [@WangDarkSchurCode2026]. The default script reuses committed RH-20 and RH-21 data; the optional flag rebuilds the six sparse resolution checks.

# Acknowledgment of numerical scope {#acknowledgment-of-numerical-scope .unnumbered}

All reported matrix entries and spectral radii are ordinary double-precision floating-point values. Exact statements in [\[sec:scalar-schur,sec:bounds,sec:nested-schur\]](#sec:scalar-schur,sec:bounds,sec:nested-schur){reference-type="ref" reference="sec:scalar-schur,sec:bounds,sec:nested-schur"} are algebraic theorems. Applications of those statements to the archived Gaussian matrices are numerical diagnostics. No interval enclosure, uniform small-noise resolvent bound, or proof of a limiting spectral law is claimed.
