---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-barenblatt-full-exponent-similarity-route-a"
canonical_tex: "henon_dynamics/henon_barenblatt_full_exponent_similarity_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_barenblatt_full_exponent_similarity_route_a/paper/main.pdf"
source_sha256: "4883e8dd2c4830f4cfc3a0dd8e40420e663572077da8b191e70e0204bf904ea2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Barenblatt Similarity Profiles for Every Positive Exponent: Exact Mass, Moment, Free-Boundary, and Dissipation Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_barenblatt_full_exponent_similarity_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_barenblatt_full_exponent_similarity_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_barenblatt_full_exponent_similarity_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_barenblatt_full_exponent_similarity_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the one-dimensional equation $u_t=(u^m)_{xx}$, every $m>0$ and mass $M>0$, we classify the centered nonnegative integrable zero-flux first-kind similarity profiles. One derivation yields compact support for $m>1$, the Gaussian at $m=1$, and algebraic tails for $0<m<1$. Exact Beta integrals normalize mass and give every absolute moment, including the sharp threshold $r<(1+m)/(1-m)$ and the logarithmic second-moment boundary $m=1/3$. We also give porous pressure/free-boundary data and a conditional rescaled dissipation identity. The statement does not classify arbitrary Cauchy solutions. Exact finite cells audit conventions but do not prove the continuous theorem. Every Route-A gate fails.
author:
- 'Route-A structural certificate C207'
title: |
  Barenblatt Similarity Profiles for Every Positive Exponent:\
  Exact Mass, Moment, Free-Boundary, and Dissipation Atlas
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** porous-medium equation; fast diffusion; Barenblatt profile; similarity solution; moment threshold.

chinese-simplified

中文摘要

本文对一维方程$u_t=(u^m)_{xx}$的全部$m>0$和给定质量，分类中心化、非负、可积、零通量的第一类自相似剖面。统一推导覆盖紧支撑、高斯与代数尾三种区域，并给出精确质量、全阶绝对矩、$m=1/3$二阶矩边界、压力自由边界及限定适用范围的重标度耗散。结论不扩张为任意初值问题解的分类；路线[A]{lang="en"}全部门失败。

# Frozen class and profile equation

Let $m>0$, $M>0$, and consider $$\label{eq:pde}
 u_t=(u^m)_{xx},\qquad x\in\mathbb R,\quad t>0.$$ We classify only centered, nonnegative, integrable first-kind profiles of mass $M$ such that $F^m\in W^{1,1}_{\mathrm{loc}}(\mathbb R)$ and the integrated zero-flux law below holds almost everywhere. Uniqueness is up to almost-everywhere equality (equivalently, for the continuous representative determined by $F^m$). Translates, signed profiles, higher dimensions, and arbitrary Cauchy solutions are outside the claim. Source-type ownership and the surrounding theory are classical [@Barenblatt; @Vazquez]; no formula priority is claimed.

Mass-preserving scaling has $$u(x,t)=t^{-\alpha}F(\xi),\qquad \xi=xt^{-\alpha},\qquad
 \alpha=\frac1{m+1}.$$ Indeed exponent matching gives $\alpha+1=m\alpha+2\alpha$. The profile equation (in distributions) and its zero-flux integral (almost everywhere) are $$\label{eq:profile}
 -\alpha(F+\xi F')=(F^m)'',\qquad
 (F^m)'+\alpha\xi F=0.$$

# All positive exponents and exact mass

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} In the frozen class there is exactly one mass-$M$ profile. For $m>1$, set $$p=\frac1{m-1},\qquad k=\frac{m-1}{2m(m+1)}.$$ Then $$\label{eq:porous}
 F(\xi)=(C-k\xi^2)_+^p,\qquad
 M=C^{p+1/2}k^{-1/2}\mathrm B\!\left(\frac12,p+1\right).$$ For $m=1$, $$\label{eq:heat}
 F(\xi)=\frac{M}{2\sqrt\pi}\mathrm e^{-\xi^2/4}.$$ For $0<m<1$, set $$q=\frac1{1-m},\qquad b=\frac{1-m}{2m(m+1)}.$$ Then $$\label{eq:fast}
 F(\xi)=(C+b\xi^2)^{-q},\qquad
 M=C^{1/2-q}b^{-1/2}\mathrm B\!\left(\frac12,q-\frac12\right).$$ In each nonlinear regime the displayed equation uniquely fixes $C>0$.

Where $F>0$, equation [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"} gives $$(F^{m-1})'=-\frac{\alpha(m-1)}m\xi \quad(m\ne1),
 \qquad (\log F)'=-\alpha\xi \quad(m=1).$$ Integration on each positivity component gives [\[eq:porous\]](#eq:porous){reference-type="eqref" reference="eq:porous"}--[\[eq:fast\]](#eq:fast){reference-type="eqref" reference="eq:fast"}. Local absolute continuity makes $F$ continuous. In the porous case a finite endpoint forces $F^{m-1}=C-k\xi^2=0$; the two endpoints therefore have equal modulus, so the only nonempty component is $(-\sqrt{C/k},\sqrt{C/k})$. In the fast and heat cases the displayed finite expressions cannot approach zero at a finite component endpoint, while integrability excludes a missing infinite end; their positivity set is all of $\mathbb R$. Thus no extra positivity component or zero interval is possible. Substituting $z=k\xi^2/C$ or $z=b\xi^2/C$ evaluates the two mass integrals by Euler's Beta integral; Gaussian integration gives [\[eq:heat\]](#eq:heat){reference-type="eqref" reference="eq:heat"}. The porous mass is strictly increasing in $C$, while the fast mass is strictly decreasing because $q>1$. Thus mass fixes $C$. Conversely the formulas satisfy [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"}, have mass $M$, and are centered. This proves existence and uniqueness inside the frozen profile class.

\>0

# All absolute moments and the sharp tail boundary

[\[prop:moments\]]{#prop:moments label="prop:moments"} For every $r>-1$, the porous and Gaussian absolute moments are respectively $$\label{eq:pmoment}
 \int_\mathbb R|\xi|^rF_{\mathrm{por}}(\xi)\,d\xi
 =C^{p+(r+1)/2}k^{-(r+1)/2}
 \mathrm B\!\left(\frac{r+1}{2},p+1\right).$$ For the Gaussian, $$\label{eq:gmoment}
 \int_\mathbb R|\xi|^rF_{\mathrm{G}}(\xi)\,d\xi
 =M\,2^r\frac{\Gamma((r+1)/2)}{\sqrt\pi}.$$ Both are finite. In fast diffusion the moment is finite exactly when $$\label{eq:threshold}
 r<2q-1=\frac{1+m}{1-m},$$ and then equals $$\label{eq:fmoment}
 \int_\mathbb R|\xi|^rF_{\mathrm{fast}}(\xi)\,d\xi
 =C^{-q+(r+1)/2}b^{-(r+1)/2}
 \mathrm B\!\left(\frac{r+1}{2},q-\frac{r+1}{2}\right).$$ At equality divergence is logarithmic; above it divergence is a power. Hence the fast second moment is finite exactly for $m>1/3$, logarithmically divergent at $m=1/3$.

Evenness and the substitutions used for mass give [\[eq:pmoment\]](#eq:pmoment){reference-type="eqref" reference="eq:pmoment"}--[\[eq:fmoment\]](#eq:fmoment){reference-type="eqref" reference="eq:fmoment"}. Alternatively, $F(\xi)\asymp |\xi|^{-2q}$ in the fast regime, so the tail integral has power $r-2q$ and converges exactly when $r-2q<-1$. Equality yields $\int^R d\xi/\xi$; the second-moment statement follows by solving $2<(1+m)/(1-m)$.

# Pressure, free boundary, and rescaled dissipation

For $m>1$, the pressure $$P=\frac{m}{m-1}u^{m-1}$$ is quadratic on the positivity set. If $R_M=\sqrt{C/k}$, then $\operatorname{supp}u(\cdot,t)=[-R_Mt^\alpha,R_Mt^\alpha]$ and the two interfaces $X_\pm(t)=\pm R_Mt^\alpha$ obey the exact one-sided pressure law $$X_\pm'(t)=\frac{\alpha X_\pm(t)}t
 =-\lim_{x\to X_\pm(t),\,u(x,t)>0}P_x(x,t).$$

Put $\tau=\log t$, $\xi=xt^{-\alpha}$, and $v=t^\alpha u$. Then $$\label{eq:rescaled}
 v_\tau=(v^m)_{\xi\xi}+\alpha(\xi v)_\xi
 =\partial_\xi(v\partial_\xi\mu),$$ where $$\mu=\frac{m}{m-1}v^{m-1}+\frac\alpha2\xi^2\ (m\ne1),
 \qquad \mu=\log v+\frac\alpha2\xi^2\ (m=1).$$ This is the first variation of the explicitly branched free energy $$\label{eq:energy}
 \mathcal F_m[v]=
 \begin{cases}
 \displaystyle\int_\mathbb R\left(\frac{v^m}{m-1}
       +\frac\alpha2\xi^2v\right)d\xi,&m\ne1,\\[5pt]
 \displaystyle\int_\mathbb R\left(v\log v-v
       +\frac14\xi^2v\right)d\xi,&m=1.
 \end{cases}$$ Every profile in Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"} is stationary. For sufficiently regular positive rescaled solutions for which the displayed terms in [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"} are finite (so no $\infty-\infty$ is used) and whose decay justifies integration by parts, $$\label{eq:dissipation}
 \frac{d\mathcal F_m}{d\tau}
 =\int_\mathbb R\mu\,\partial_\xi(v\partial_\xi\mu)\,d\xi
 =-\int_\mathbb Rv|\partial_\xi\mu|^2\,d\xi.$$ This identity is not asserted outside that class. For the fast Barenblatt profiles, the finite-second-moment/free-energy setting used here starts at $m>1/3$. At $m\le1/3$ that functional is not finite on the Barenblatt profile, so equation [\[eq:dissipation\]](#eq:dissipation){reference-type="eqref" reference="eq:dissipation"} is not applied to it.

\>1

# Executable closure and strict Route-A stop

The canonical ledger has 18 profiles, 90 sample cells, and 108 moment cells, computed with 100 working decimal digits and serialized at 82 significant digits. A checker importing no producer validates the recursively frozen schema and every grid and formula in 3,462 assertions. A separate SymPy path closes 56 generic and row-level checks, including the transformed Beta integrals; replay is byte exact; 33 repaired-hash semantic/schema attacks and one stale-hash attack are rejected. These cells are convention sentinels; the proof above carries every continuous quantifier.

There is no arithmetic origin, rational-prime primitive owner, isolated periodic ledger, target determinant, target analytic structure, Weil compression, or same-clock unitary lift. Therefore $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FAIL}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Claim firewall.

We claim no classification of arbitrary Cauchy solutions, signed or noncentered profiles, higher dimensions, long-time convergence, free-energy identity without its hypotheses, arithmetic local data, Euler factor, root number, automorphy, target divisor or functional equation, Hilbert--Pólya operator, finite-regression proof, exhaustive priority, external review, or acceptance score.

#### Revision focus.

Round 0 freezes the profile class and proves the complete three-regime mass-normalized classification.

#### Revision focus.

Round 1 adds every absolute moment, the sharp tail and $m=1/3$ boundaries, pressure/free-boundary data, and conditional rescaled dissipation from the explicitly branched free energy.

#### Revision focus.

Round 2 adds independent executable closure, source ownership, Route-A evaluation, disclosures, and the claim firewall.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local exact synthetic evidence and deterministic code accompany the paper; no observational data are used.

#### Ethics.

No human, animal, personal, or sensitive data are used.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported derivation, drafting, and exact-code development; it was not an external reviewer or an independent peer-review process.

2 G. I. Barenblatt, "On some unsteady motions of a liquid and gas in a porous medium," *Prikl. Mat. Mekh.* 16 (1952), 67--78. J. L. Vázquez, *The Porous Medium Equation: Mathematical Theory*, Oxford University Press, 2007. DOI: [10.1093/acprof:oso/9780198569039.001.0001](https://doi.org/10.1093/acprof:oso/9780198569039.001.0001).
