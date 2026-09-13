---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quadratic-polubarinova-galin-route-a"
canonical_tex: "henon_dynamics/henon_quadratic_polubarinova_galin_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quadratic_polubarinova_galin_route_a/paper/main.pdf"
source_sha256: "90686caffa9379f7e200b60b7906d6dcddff671633d96ef1ba40aefa60590a1d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Complete Injection--Suction and First-Cusp Atlas for Quadratic Polubarinova--Galin Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quadratic_polubarinova_galin_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quadratic_polubarinova_galin_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quadratic_polubarinova_galin_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quadratic_polubarinova_galin_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the normalized quadratic map $f(\zeta,t)=a(t)\zeta+b(t)\zeta^2$ we solve the constant-rate Polubarinova--Galin equation on its entire smooth univalent branch. The complex coefficient $a^2b$ is conserved, normalized area is affine in physical time, injection is global and asymptotically circular, while noncircular suction ends at an explicitly timed ordinary semicubical cusp. Circular collapse and nonsmooth or invalid initial faces are separated. This round is the **coefficient-reduction owner**.
author:
- 'HCS-C368 / HEN-O352'
date: 4 September 2026
title: |
  The Complete Injection--Suction and First-Cusp Atlas\
  for Quadratic Polubarinova--Galin Flow
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3682026090400000000000000000000\>\<C3682026090400000000000000000000\>\]

# Normalized flow and exact reduction

Let $a(t)>0$, $b(t)\in\mathbb C$, and $$\label{eq:model}
 f(\zeta,t)=a(t)\zeta+b(t)\zeta^2,
 \qquad
 \operatorname{Re}\!\left[f_t\,\overline{\zeta f_\zeta}\right]=q
 \quad (|\zeta|=1),$$ where $q\in\mathbb R$ is constant. The normalization $f(0,t)=0$ and $f_\zeta(0,t)=a(t)>0$ fixes translation and rotation. A *smooth univalent solution* means $a>2|b|$; then $f$ is conformal on a neighborhood of $\overline{\mathbb D}$ and parametrizes a smooth Jordan boundary.

[\[thm:main\]]{#thm:main label="thm:main"} For smooth univalent initial data, equation [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} is equivalent to $$\label{eq:ode}
 \dot a=\frac{aq}{a^2-4|b|^2},\qquad
 \dot b=-\frac{2qb}{a^2-4|b|^2}.$$ On its unique maximal smooth interval, $$\label{eq:invariants}
 \kappa:=a^2b\quad\hbox{is constant},\qquad
 M_0:=a^2+2|b|^2=\frac{\operatorname{Area}(f(\mathbb D))}{\pi},\qquad
 \dot M_0=2q.$$ Put $u=a^2$ and $u_c=(4|\kappa|^2)^{1/3}$, taking $u_c=0$ when $\kappa=0$. Then $$\label{eq:F}
 M_0=F(u):=u+\frac{2|\kappa|^2}{u^2},\qquad
 F'(u)=1-\frac{4|\kappa|^2}{u^3},$$ and smooth univalence is exactly $u>u_c$.

If $q>0$, the solution is smooth for every $t\ge0$, $u$ increases to infinity, and $2|b|/a\to0$. If $q=0$, the map is stationary.

On $|\zeta|=1$, expanding the left side of [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} and equating its constant and first Fourier modes gives $$\label{eq:fourier}
 a\dot a+2\operatorname{Re}(\dot b\,\overline b)=q,
 \qquad a\dot b+2\dot a b=0.$$ The determinant is $a^2-4|b|^2$, so [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"} follows. The second identity gives $(a^2b)^{\boldsymbol\cdot}=0$, and both identities give $\dot M_0=2q$. The area formula follows either from the coefficient area theorem or from $\tfrac12\int_0^{2\pi}\!\operatorname{Im}(\overline f f_\theta)d\theta$. Substituting $b=\kappa/u$ proves [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}.

Indeed, $$f(z_1)-f(z_2)=(z_1-z_2)\{a+b(z_1+z_2)\},\qquad
 f'(\zeta)=a+2b\zeta.$$ Thus $a>2|b|$ gives injectivity and nonvanishing derivative on $\overline\mathbb D$; equality puts the sole critical point on its boundary, and $a<2|b|$ puts it inside. Since $F$ is strictly increasing on $(u_c,\infty)$, $M_0(t)=M_0(0)+2qt$ uniquely determines that branch. For $q>0$ it exists globally with $u\to\infty$ and $2|b|/a=2|\kappa|/u^{3/2}\to0$. For $q=0$, [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"} vanishes.

\>0

# Sharp suction endpoint and cusp normal form

This revision is the **first-cusp owner**.

[\[thm:cusp\]]{#thm:cusp label="thm:cusp"} Assume $q<0$ and smooth univalent initial data. If $\kappa\ne0$, the maximal smooth time is $$\label{eq:T}
 T=\frac{M_0(0)-M_c}{-2q},\qquad
 M_c=F(u_c)=\frac32u_c.$$ As $t\uparrow T$, $u\downarrow u_c$, $a\downarrow\sqrt{u_c}$, and $|b|\uparrow\sqrt{u_c}/2$. No self-intersection on $\overline\mathbb D$ and no critical point in $\overline\mathbb D$ occurs earlier. At $T$ the limiting boundary has exactly one ordinary semicubical cusp at $$\label{eq:location}
 \zeta_c=-\frac{a_c}{2b_c},\qquad
 z_c=f(\zeta_c,T)=-\overline{b_c}.$$

On the upper branch $u>u_c$, equation [\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"} is strictly increasing and its infimum is $F(u_c)=3u_c/2$. The affine area clock therefore reaches that value at exactly [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}; before then the strict quadratic criterion in the preceding proof excludes both critical points and self-intersections. At the endpoint write $b_c=Be^{i\phi}$, so $a_c=2B$, and set $\zeta=-e^{-i\phi}e^{is}$. Then $$\begin{aligned}
\label{eq:cusp}
 e^{i\phi}\{f(\zeta,T)-z_c\}
 &=B\{-2e^{is}+e^{2is}+1\}\\
 &=-Bs^2-iBs^3+\frac7{12}Bs^4+O(s^5).\notag\end{aligned}$$ With $X=-\operatorname{Re}(e^{i\phi}(z-z_c))$ and $Y=-\operatorname{Im}(e^{i\phi}(z-z_c))$, one has $X=Bs^2+O(s^4)$, $Y=Bs^3+O(s^5)$, and $$\label{eq:semi}
 \lim_{s\to0}\frac{Y^2}{X^3}=\frac1B.$$ This is the ordinary semicubical normal form and proves uniqueness of the boundary cusp.

\>1

# Circular and excluded faces

This revision is the **boundary-and-route owner**.

[\[prop:boundary\]]{#prop:boundary label="prop:boundary"} If $\kappa=0$, then $b=0$ throughout and $a(t)^2=a(0)^2+2qt$. Injection expands circles globally, $q=0$ fixes the circle, and suction collapses it at $T=a(0)^2/(-2q)$ without a pre-collapse cusp.

If $a(0)=2|b(0)|$ with $b(0)\ne0$, the datum already has the cusp [\[eq:cusp\]](#eq:cusp){reference-type="eqref" reference="eq:cusp"} and its smooth lifespan is zero. If $0<a(0)<2|b(0)|$, then $f'$ vanishes inside $\mathbb D$ and no conformal Laplacian-growth domain is asserted. No surface-tension regularization, weak post-cusp continuation, higher-degree classification, or multiply connected extension is included.

# Source boundary, evidence, and route decision

Richardson's injected Hele--Shaw analysis supplies classical moment-method lineage [@Richardson]. Gustafsson formulates the polynomial string and Polubarinova--Galin setting [@Gustafsson]; Gustafsson and Lin analyze root and pole dynamics for such solutions [@GL]. We claim no priority. The contribution here is the self-contained degree-two branch theorem and its explicit first-cusp clock.

Exact rational panels verify [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"}--[\[eq:F\]](#eq:F){reference-type="eqref" reference="eq:F"}; separately chosen rationalized endpoint families verify [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}--[\[eq:semi\]](#eq:semi){reference-type="eqref" reference="eq:semi"}. They are regression receipts only. The proofs own the continuum theorem.

There is no rational-prime carrier, isolated primitive-orbit ledger, dynamical zeta, target analytic bridge, or natural same-clock unitary lift. Route A is rejected as $(A0_{\rm FAIL},A1_{\rm FAIL},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FAIL})$. Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`; no target zero match or Hilbert--Pólya operator is claimed.

9 S. Richardson, *Hele Shaw flows with a free boundary produced by the injection of fluid into a narrow channel*, Journal of Fluid Mechanics 56 (1972), 609--618. <https://doi.org/10.1017/S0022112072002551>. B. Gustafsson, *The string equation for polynomials*, Analysis and Mathematical Physics 8 (2018), 637--653. <https://doi.org/10.1007/s13324-018-0239-3>. B. Gustafsson and Y.-L. Lin, *On the dynamics of roots and poles for solutions of the Polubarinova--Galin equation*, Annales Academiae Scientiarum Fennicae Mathematica 38 (2013), 259--286. <https://doi.org/10.5186/aasfm.2013.3802>.
