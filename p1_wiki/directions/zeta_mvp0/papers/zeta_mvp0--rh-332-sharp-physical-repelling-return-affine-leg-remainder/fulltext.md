---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-332-sharp-physical-repelling-return-affine-leg-remainder"
canonical_tex: "zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder/main.pdf"
source_sha256: "99ce48d3592a834ece5ea3c1cc100f9b7bd801277ffa1d44fccafc22511d0496"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Physical Repelling-Return Affine-Leg Remainder

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-332-sharp-physical-repelling-return-affine-leg-remainder/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The first physical endpoint leg of RH-324 produces an actual finite-noise prefix near the repelling point. We pass that same prefix through the second physical row and compare only this row with the RH-323 repelling tangent row, retaining the incoming coordinate. After including the Jacobian, the scaled physical row has an exact two-lobe formula. Its $L^1$ distance to the full Gaussian at the curved image is exactly two state-boundary tails, while removal of the quadratic displacement costs $4\Phi(u_c\sigma u^2/2)-2$. We prove a uniform fourth moment for the actual first-leg marginal; this is the missing uniform-integrability input that ordinary $L^1$ convergence does not provide. For either repelling orientation, $$\frac{D_{\sigma,a_\sigma}^{\pm}}{\sigma}
   \longrightarrow
   \sqrt{\frac2\pi}\,u_c
   \int_{\{\pm u>0\}}u^2p_d(u)\,du>0,
   \qquad a_\sigma\longrightarrow d.$$ The sum has a closed coefficient. Thus exponential, or even $o(\sigma)$, accuracy is false for this exact second hybrid Duhamel row term. The coefficient vanishes at the single row $u=0$, and a source moving to the critical partition disproves a global uniform $O(\sigma)$ row estimate. No fully physical-to-fully affine two-leg equality, all-cycle transport, cyclic trace estimate, or Gate A--E promotion is asserted.
author:
- Bin Wang
date: August 2026
title: 'Sharp Physical Repelling-Return Affine-Leg Remainder'
```

## Markdown 正文

# Physical row and repelling coordinates

Let $u_c$ be the root in $(1,2)$ of $$u^3-2u^2+2u-2=0,$$ and put $$\label{eq:constants}
 f(x)=1-u_cx^2,
 \qquad r=u_c-1,
 \qquad \lambda=2u_cr,
 \qquad \alpha=2u_c,
 \qquad b=u_c^{-1/2}.$$ Numerically, $$\begin{aligned}
 u_c&=1.543689012692076\ldots,
 &r&=0.543689012692076\ldots,\\
 \lambda&=1.678573510428322\ldots,
 &b&=0.804859535112210\ldots .\end{aligned}$$ Write $\phi$, $\Phi$, and $\overline\Phi=1-\Phi$ for the standard normal density, distribution, and survival functions. The archived row-normalized folded kernel on $[0,1]$ is $$\label{eq:physical-kernel}
 P_\sigma(x,y)=
 \frac{\phi_\sigma(y-f(x))+\phi_\sigma(y+f(x))}{Z_\sigma(x)},
 \qquad
 \phi_\sigma(t)=\sigma^{-1}\phi(t/\sigma),$$ where $$\label{eq:normalizer}
 Z_\sigma(x)=
 1-\overline\Phi\!\left(\frac{1-f(x)}\sigma\right)
  -\overline\Phi\!\left(\frac{1+f(x)}\sigma\right).$$ This is the probability that the folded Gaussian lies in the physical state interval; in particular $0<Z_\sigma(x)\le1$.

Use repelling coordinates $$\label{eq:repelling-coordinates}
 x=r+\sigma u,
 \qquad y=r+\sigma w,
 \qquad
 I_\sigma=\left[-\frac r\sigma,\frac{1-r}\sigma\right].$$ The quadratic map gives the exact, rather than asymptotic, expansion $$\label{eq:repelling-expansion}
 f(r+\sigma u)=r-\lambda\sigma u-u_c\sigma^2u^2
 =r-\sigma d_\sigma(u),
 \qquad
 d_\sigma(u)=\lambda u+u_c\sigma u^2.$$ The Jacobian in the next definition is essential.

For $u\in I_\sigma$, define the scaled physical row $$\begin{aligned}
 L_\sigma(u,w)
 &:=\sigma P_\sigma(r+\sigma u,r+\sigma w)\nonumber\\
 &=\frac{
 \phi(w+d_\sigma(u))
 +\phi\!\left(w+\frac{2r}\sigma-d_\sigma(u)\right)}
 {Z_\sigma(r+\sigma u)}\mathbf 1_{I_\sigma}(w),
 \label{eq:physical-second-row}\end{aligned}$$ and, on the full line, $$\label{eq:curved-tangent-rows}
 C_{\sigma,u}(w)=\phi(w+d_\sigma(u)),
 \qquad
 A_u(w)=\phi(w+\lambda u).$$ All three rows have mass one.

The first lobe in [\[eq:physical-second-row\]](#eq:physical-second-row){reference-type="eqref" reference="eq:physical-second-row"} is centered at the signed exact image; that image is positive in the fixed local repelling chart near $r$. The other lobe is the folded companion. No symmetry with the endpoint expansion of RH-324 has been assumed.

# Exact row identities and their sharp local limit

[\[thm:row-identities\]]{#thm:row-identities label="thm:row-identities"} For every $\sigma>0$ and every physical source $u\in I_\sigma$, $$\label{eq:boundary-identity}
 \boxed{
 \|L_\sigma(u,\cdot)-C_{\sigma,u}\|_1
 =2\left[
 \overline\Phi\!\left(\frac r\sigma-d_\sigma(u)\right)
 +\overline\Phi\!\left(\frac{1-r}\sigma+d_\sigma(u)\right)
 \right].}$$ Moreover, $$\label{eq:shift-identity}
 \boxed{
 \|C_{\sigma,u}-A_u\|_1
 =4\Phi\!\left(\frac{u_c\sigma u^2}{2}\right)-2.}$$ Consequently, if $B_\sigma(u)$ and $S_\sigma(u)$ denote the right sides of [\[eq:boundary-identity\]](#eq:boundary-identity){reference-type="eqref" reference="eq:boundary-identity"} and [\[eq:shift-identity\]](#eq:shift-identity){reference-type="eqref" reference="eq:shift-identity"}, then $$\label{eq:triangle-sandwich}
 \max\{0,S_\sigma(u)-B_\sigma(u)\}
 \le \|L_\sigma(u,\cdot)-A_u\|_1
 \le S_\sigma(u)+B_\sigma(u).$$

The two unnormalized lobes in [\[eq:physical-kernel\]](#eq:physical-kernel){reference-type="eqref" reference="eq:physical-kernel"} have total mass one on $[0,\infty)$, so restriction to $[0,1]$ gives $Z_\sigma\le1$. On $I_\sigma$, the numerator of $L_\sigma$ contains $C_{\sigma,u}$ and division by $Z_\sigma\le1$ only increases it. Hence $L_\sigma\ge C_{\sigma,u}$ on $I_\sigma$, while $L_\sigma=0$ off that interval. Since both are probability densities, the positive and negative parts of their difference have equal mass. Each mass is the amount of $C_{\sigma,u}$ outside $I_\sigma$, namely $$\overline\Phi(r/\sigma-d_\sigma(u))
 +\overline\Phi((1-r)/\sigma+d_\sigma(u)).$$ This proves [\[eq:boundary-identity\]](#eq:boundary-identity){reference-type="eqref" reference="eq:boundary-identity"}; in particular the companion lobe, state restriction, and exact normalizer have already been combined.

The centers in [\[eq:curved-tangent-rows\]](#eq:curved-tangent-rows){reference-type="eqref" reference="eq:curved-tangent-rows"} differ by $u_c\sigma u^2$. Unit Gaussians separated by $t$ have unhalved $L^1$ distance $4\Phi(|t|/2)-2$, which proves [\[eq:shift-identity\]](#eq:shift-identity){reference-type="eqref" reference="eq:shift-identity"}. The ordinary and reverse triangle inequalities give [\[eq:triangle-sandwich\]](#eq:triangle-sandwich){reference-type="eqref" reference="eq:triangle-sandwich"}.

[\[cor:fixed-row\]]{#cor:fixed-row label="cor:fixed-row"} For each fixed $u\in\mathbb R$, $$\label{eq:fixed-row-limit}
 \boxed{
 \lim_{\sigma\downarrow0}
 \frac{\|L_\sigma(u,\cdot)-A_u\|_1}{\sigma}
 =\sqrt{\frac2\pi}\,u_cu^2.}$$ At $u=0$ the coefficient is zero; for every fixed $u\ne0$ it is positive.

For fixed $u$, both arguments of the survival functions in [\[eq:boundary-identity\]](#eq:boundary-identity){reference-type="eqref" reference="eq:boundary-identity"} are a positive constant times $\sigma^{-1}$ up to $O(1)$. Thus $B_\sigma(u)=o(\sigma)$. Taylor expansion at zero gives $$\frac{S_\sigma(u)}\sigma
 \longrightarrow 2\phi(0)u_cu^2
 =\sqrt{2/\pi}\,u_cu^2.$$ Now use [\[eq:triangle-sandwich\]](#eq:triangle-sandwich){reference-type="eqref" reference="eq:triangle-sandwich"}.

The fixed-source quantifier cannot be made global.

[\[prop:global-obstruction\]]{#prop:global-obstruction label="prop:global-obstruction"} Let $$u_\sigma=\frac{b-r}{\sigma},$$ so that the physical source $r+\sigma u_\sigma$ equals the critical partition $b$. Then $$\label{eq:global-obstruction}
 \liminf_{\sigma\downarrow0}
 \|L_\sigma(u_\sigma,\cdot)-A_{u_\sigma}\|_1\ge1.$$ In particular, $\sup_{u\in I_\sigma}\|L_\sigma(u,\cdot)-A_u\|_1$ is not $O(\sigma)$.

Since $f(b)=0$, [\[eq:repelling-expansion\]](#eq:repelling-expansion){reference-type="eqref" reference="eq:repelling-expansion"} gives $d_\sigma(u_\sigma)=r/\sigma$. Therefore $B_\sigma(u_\sigma)\to1$: the curved Gaussian has half its mass beyond the state boundary, while the other boundary tail vanishes. On the other hand, the curved-to-tangent displacement is $$u_c\sigma u_\sigma^2=\frac{u_c(b-r)^2}{\sigma}\longrightarrow\infty,$$ so $S_\sigma(u_\sigma)\to2$. The lower bound in [\[eq:triangle-sandwich\]](#eq:triangle-sandwich){reference-type="eqref" reference="eq:triangle-sandwich"} yields [\[eq:global-obstruction\]](#eq:global-obstruction){reference-type="eqref" reference="eq:global-obstruction"}.

# The actual physical first-leg prefix

We now specify the incoming law rather than reusing a local seed. Put $L=\sigma^{-1}$ and, for $0\le a\le L$, let the exact RH-322 entrance density be $$\label{eq:finite-seed}
 \widetilde h_{\sigma,a}(v)=
 \frac{\phi(v-a)+\phi(2L-v-a)}
 {\Phi(a)-\overline\Phi(2L-a)}\mathbf 1_{[0,L]}(v).$$ For $c_\sigma(v)=\alpha v-u_c\sigma v^2$, the exact RH-324 first physical row is $$\label{eq:first-row}
 K_\sigma(v,u)=
 \frac{
 \phi(u+2r/\sigma-c_\sigma(v))+\phi(u+c_\sigma(v))}
 {Z_\sigma(1-\sigma v)}\mathbf 1_{I_\sigma}(u).$$ Define its actual $U$-marginal by $$\label{eq:actual-prefix}
 \mu_{\sigma,a}(du)=
 \left\{\int_0^L\widetilde h_{\sigma,a}(v)
 K_\sigma(v,u)\,dv\right\}du.$$ This is an exact physical prefix, not the affine $U$-law.

For $d\ge0$, the RH-323 affine entrance and intermediate densities are $$\begin{aligned}
 g_d(v)&=\frac{\phi(v-d)}{\Phi(d)}\mathbf 1_{[0,\infty)}(v),
 \label{eq:gd}\\
 p_d(u)&=\frac1{s_1\Phi(d)}
 \phi\!\left(\frac{u+\alpha d}{s_1}\right)
 \Phi\!\left(\frac{d-\alpha u}{s_1}\right),
 \qquad s_1=\sqrt{1+\alpha^2}.
 \label{eq:pd}\end{aligned}$$ Equivalently, $p_d$ is the law of $$\label{eq:affine-U}
 U=-\alpha V-Z_1,
 \qquad V\sim g_d,
 \qquad Z_1\sim N(0,1),$$ with $V$ and $Z_1$ independent. RH-324 proves, for fixed $0<\rho<1-b$ and $$m_\rho=u_c(1-\rho)^2-1>0,
 \qquad
 M_2(a)=a^2+1+a\frac{\phi(a)}{\Phi(a)},$$ the explicit marginal consequence $$\begin{aligned}
 \|\mu_{\sigma,a}-p_d\|_1
 \le{}&|a-d|+
 \frac{2\overline\Phi(L-a)}{\Phi(a)}
 +\sqrt{\frac2\pi}u_c\sigma M_2(a)\nonumber\\
 &+2\{\overline\Phi(m_\rho/\sigma)
       +\overline\Phi((1-r)/\sigma)\}
 +\frac{2\overline\Phi(\rho/\sigma-a)}{\Phi(a)}.
 \label{eq:rh324-prefix-bound}\end{aligned}$$ Thus $a_\sigma\to d$ implies ordinary $L^1$ convergence. The next lemma supplies the weighted convergence that [\[eq:rh324-prefix-bound\]](#eq:rh324-prefix-bound){reference-type="eqref" reference="eq:rh324-prefix-bound"} alone does not imply.

[\[lem:fourth-moment\]]{#lem:fourth-moment label="lem:fourth-moment"} For every compact $\mathcal K\subset[0,\infty)$ there are $\sigma_0,C_{\mathcal K}>0$ such that $$\label{eq:uniform-fourth}
 \sup_{0<\sigma<\sigma_0}\ \sup_{a\in\mathcal K}
 \int_{I_\sigma}|u|^4\,\mu_{\sigma,a}(du)
 \le C_{\mathcal K}.$$ Consequently, whenever $a_\sigma\to d$, $$\label{eq:sector-moment-convergence}
 \int_{\{\pm u>0\}}u^2\,\mu_{\sigma,a_\sigma}(du)
 \longrightarrow
 \int_{\{\pm u>0\}}u^2p_d(u)\,du.$$

Fix $0<\rho<1-b$ and put $$q_0=\max\{r,1-r\},
 \qquad z_0=\Phi(1)-\tfrac12>0.$$ The explicit density [\[eq:finite-seed\]](#eq:finite-seed){reference-type="eqref" reference="eq:finite-seed"} gives, uniformly for $a\in\mathcal K$ and small $\sigma$, $$\label{eq:V8}
 \mathbb E_{\widetilde h_{\sigma,a}}V^8\le C_{\mathcal K}.$$ Indeed, its denominator is bounded below, the first numerator term is a Gaussian with bounded center, and the reflected term begins at $L-\sup\mathcal K$ after reflection and is Gaussian-tail small.

For every $x\in[0,1]$ and small $\sigma$, the folded normalizer is at least $z_0$: the corresponding standard-normal interval has length at least two and contains zero. On $v\le\rho/\sigma$, the source $1-\sigma v$ remains in the negative endpoint branch and its image has modulus at least $m_\rho$. Integrating the two numerator lobes in [\[eq:first-row\]](#eq:first-row){reference-type="eqref" reference="eq:first-row"} therefore gives $$\begin{aligned}
 \mathbb E(|U|^4\mid V=v)
 &\le z_0^{-1}\bigl\{c_\sigma(v)^4+6c_\sigma(v)^2+3\nonumber\\
 &\hspace{5.7em}{}+q_0^4\sigma^{-4}
 \overline\Phi(m_\rho/\sigma)\bigr\}.
 \label{eq:conditional-fourth}\end{aligned}$$ Here the first three terms are the fourth moment of the full main Gaussian; the last term bounds the remote folded lobe on the physical support. Moreover, $$\label{eq:c-fourth}
 |c_\sigma(v)|^4
 \le8\alpha^4v^4+8u_c^4\sigma^4v^8.$$ Equations [\[eq:V8\]](#eq:V8){reference-type="eqref" reference="eq:V8"}--[\[eq:c-fourth\]](#eq:c-fourth){reference-type="eqref" reference="eq:c-fourth"} make the contribution of $v\le\rho/\sigma$ uniformly bounded.

On the complementary entrance tail, $|U|\le q_0/\sigma$ and Markov's inequality applied to [\[eq:V8\]](#eq:V8){reference-type="eqref" reference="eq:V8"} gives $$\Pr\{V>\rho/\sigma\}
 \le \rho^{-8}\sigma^8\mathbb EV^8.$$ Its contribution to $\mathbb E|U|^4$ is therefore $O(\sigma^4)$. This proves [\[eq:uniform-fourth\]](#eq:uniform-fourth){reference-type="eqref" reference="eq:uniform-fourth"}.

For the second assertion, truncate $u^2\mathbf 1_{\{\pm u>0\}}$ at $|u|\le M$. The error between the truncated $\mu_{\sigma,a_\sigma}$ and $p_d$ integrals is at most $M^2\|\mu_{\sigma,a_\sigma}-p_d\|_1$. The two omitted tails are at most $M^{-2}$ times their fourth moments; $p_d$ has all moments by [\[eq:affine-U\]](#eq:affine-U){reference-type="eqref" reference="eq:affine-U"}. First let $\sigma\downarrow0$ using [\[eq:rh324-prefix-bound\]](#eq:rh324-prefix-bound){reference-type="eqref" reference="eq:rh324-prefix-bound"}, then let $M\to\infty$. This proves [\[eq:sector-moment-convergence\]](#eq:sector-moment-convergence){reference-type="eqref" reference="eq:sector-moment-convergence"} separately for both signs.

# Sharp transported second-hybrid row term

The data type of the main result is fixed before measuring its error. The two retained $(u,w)$ path laws $$\label{eq:hybrid-laws}
 \mathsf H^{\rm phys}_{\sigma,a}(du,dw)
 =\mu_{\sigma,a}(du)L_\sigma(u,w)\,dw,
 \qquad
 \mathsf H^{\rm tan}_{\sigma,a}(du,dw)
 =\mu_{\sigma,a}(du)A_u(w)\,dw$$ have the *same actual physical first-leg prefix*. Only the second row changes. This is precisely the second hybrid row term in the retained-path Duhamel telescope of RH-325.

For the two repelling orientations define $$\label{eq:D-sector}
 D^{\pm}_{\sigma,a}
 =\int_{\{\pm u>0\}}
 \|L_\sigma(u,\cdot)-A_u\|_1\,\mu_{\sigma,a}(du),
 \qquad
 D_{\sigma,a}=D^+_{\sigma,a}+D^-_{\sigma,a}.$$ Because $u$ is retained, $D^{\pm}_{\sigma,a}$ is exactly the unhalved $L^1$ norm of the difference in [\[eq:hybrid-laws\]](#eq:hybrid-laws){reference-type="eqref" reference="eq:hybrid-laws"} restricted to the corresponding sector.

[\[lem:averaged-boundary\]]{#lem:averaged-boundary label="lem:averaged-boundary"} Uniformly for $a$ in a fixed compact subset of $[0,\infty)$, $$\label{eq:averaged-boundary}
 \int B_\sigma(u)\,\mu_{\sigma,a}(du)=o(\sigma).$$

Choose $0<\varepsilon<\min\{r,b-r\}$ and set $$m_\varepsilon
 =\min\{f(r+\varepsilon),1-f(r-\varepsilon)\}>0.$$ When $|u|\le\varepsilon/\sigma$, the two survival-function arguments in [\[eq:boundary-identity\]](#eq:boundary-identity){reference-type="eqref" reference="eq:boundary-identity"} are exactly $f(r+\sigma u)/\sigma$ and $(1-f(r+\sigma u))/\sigma$. Hence $B_\sigma(u)\le4\overline\Phi(m_\varepsilon/\sigma)$ there. Off this local chart, $B_\sigma\le2$, while [\[lem:fourth-moment\]](#lem:fourth-moment){reference-type="ref" reference="lem:fourth-moment"} gives $$\mu_{\sigma,a}\{|u|>\varepsilon/\sigma\}
 \le C_{\mathcal K}\sigma^4/\varepsilon^4.$$ Thus the integral is at most $4\overline\Phi(m_\varepsilon/\sigma)
 +2C_{\mathcal K}\sigma^4/\varepsilon^4=o(\sigma)$.

[\[thm:transported-sharp\]]{#thm:transported-sharp label="thm:transported-sharp"} Let $\sigma\downarrow0$ and let $a_\sigma\ge0$ satisfy $a_\sigma\to d\ge0$. Then, for each sign, $$\label{eq:sector-sharp}
 \boxed{
 \frac{D^{\pm}_{\sigma,a_\sigma}}{\sigma}
 \longrightarrow
 \sqrt{\frac2\pi}\,u_c
 \int_{\{\pm u>0\}}u^2p_d(u)\,du>0.}$$ Summing the orientations gives the closed formula $$\label{eq:total-sharp}
 \boxed{
 \frac{D_{\sigma,a_\sigma}}\sigma
 \longrightarrow
 \sqrt{\frac2\pi}\,u_c
 \left[
 1+\alpha^2\left(
 d^2+1+d\frac{\phi(d)}{\Phi(d)}
 \right)
 \right]>0.}$$

Let $E_\sigma(u)=\|L_\sigma(u,\cdot)-A_u\|_1$ and let $S_\sigma(u)$ be [\[eq:shift-identity\]](#eq:shift-identity){reference-type="eqref" reference="eq:shift-identity"}. The reverse and ordinary triangle inequalities give $|E_\sigma(u)-S_\sigma(u)|\le B_\sigma(u)$. Therefore [\[lem:averaged-boundary\]](#lem:averaged-boundary){reference-type="ref" reference="lem:averaged-boundary"} shows, in either sector, $$\label{eq:E-to-S}
 \left|\int_{\{\pm u>0\}}(E_\sigma-S_\sigma)
 \,d\mu_{\sigma,a_\sigma}\right|=o(\sigma).$$

The elementary Gaussian-shift inequality $$0\le4\Phi(t/2)-2\le\sqrt{\frac2\pi}\,t,
 \qquad t\ge0,$$ implies $$\label{eq:curvature-domination}
 0\le\frac{S_\sigma(u)}\sigma
 \le\sqrt{\frac2\pi}u_cu^2,
 \qquad
 \frac{S_\sigma(u)}\sigma
 \longrightarrow\sqrt{\frac2\pi}u_cu^2.$$ The convergence is uniform on each fixed bounded $u$-interval. On such an interval, [\[eq:rh324-prefix-bound\]](#eq:rh324-prefix-bound){reference-type="eqref" reference="eq:rh324-prefix-bound"} transfers the integral from $\mu_{\sigma,a_\sigma}$ to $p_d$. Outside it, [\[eq:curvature-domination\]](#eq:curvature-domination){reference-type="eqref" reference="eq:curvature-domination"} and the uniform fourth moment make the second-moment tails uniformly small. Thus $$\int_{\{\pm u>0\}}\frac{S_\sigma(u)}\sigma
 \,\mu_{\sigma,a_\sigma}(du)
 \longrightarrow
 \sqrt{\frac2\pi}u_c
 \int_{\{\pm u>0\}}u^2p_d(u)\,du.$$ Together with [\[eq:E-to-S\]](#eq:E-to-S){reference-type="eqref" reference="eq:E-to-S"}, this proves [\[eq:sector-sharp\]](#eq:sector-sharp){reference-type="eqref" reference="eq:sector-sharp"}. The density [\[eq:pd\]](#eq:pd){reference-type="eqref" reference="eq:pd"} is strictly positive on $\mathbb R$, so both sector coefficients are strictly positive.

Finally [\[eq:affine-U\]](#eq:affine-U){reference-type="eqref" reference="eq:affine-U"} gives $$\mathbb EU^2=1+\alpha^2\mathbb EV^2,
 \qquad
 \mathbb EV^2=d^2+1+d\frac{\phi(d)}{\Phi(d)}.$$ Adding the two sector moments proves [\[eq:total-sharp\]](#eq:total-sharp){reference-type="eqref" reference="eq:total-sharp"}.

[\[cor:negative-phase\]]{#cor:negative-phase label="cor:negative-phase"} For every $d\ge0$ and along every sequence $a_\sigma\to d$, the exact second hybrid row error in [\[eq:D-sector\]](#eq:D-sector){reference-type="eqref" reference="eq:D-sector"} is neither exponentially small nor $o(\sigma)$. If the inherited first-alias clearance satisfies $$\delta_k=C_{\rm b}\lambda^{-2k}\{1+o(1)\},
 \qquad C_{\rm b}>0,$$ and $$a_\sigma=\frac{\delta_k}{\sigma},
 \qquad
 \eta_\sigma:=k-\frac{\log(1/\sigma)}{2\log\lambda}
 \longrightarrow\eta,$$ then $a_\sigma\to d=C_{\rm b}\lambda^{-2\eta}$ and [\[eq:sector-sharp\]](#eq:sector-sharp){reference-type="eqref" reference="eq:sector-sharp"}--[\[eq:total-sharp\]](#eq:total-sharp){reference-type="eqref" reference="eq:total-sharp"} hold with this phase-matched $d$.

The comparison $\sigma=o(R^{-2k})$ for $R=1.4$ and $k=\log(1/\sigma)/(2\log\lambda)+O(1)$ remains valid because $\log R/\log\lambda=0.6496301165\ldots<1$. This is only local scale compatibility. The positive coefficient is an obstruction to improving the hybrid term below order $\sigma$, not an obstruction at the larger first-alias target scale.

# Deterministic reproduction and claim boundary

The implementation evaluates the exact normalizer, both row identities, triangle bounds, the density $p_d$, and its two sector moments using standard-library composite Simpson quadrature. The displayed sector integrals use the finite numerical window $|u|\le32$; the exact total uses the closed formula in [\[eq:total-sharp\]](#eq:total-sharp){reference-type="eqref" reference="eq:total-sharp"}. Selected coefficients are

    $d$     $u<0$ coefficient   $u>0$ coefficient     exact total
  ------- ------------------- ------------------- ---------------
    $0$         $12.88903630$        $0.08295737$   $12.97199367$
   $0.5$        $18.83879635$        $0.05712449$   $18.89592085$
    $1$         $28.05382711$        $0.03498685$   $28.08881396$

The sector sums agree with the closed total to the displayed digits. Finite curvature-proxy rows approach these values and exact row quadrature lies inside [\[eq:triangle-sandwich\]](#eq:triangle-sandwich){reference-type="eqref" reference="eq:triangle-sandwich"}. These rows check formulas; no exponent is fitted and no finite table is used to prove an asymptotic statement.

The signs $U<0$ and $U>0$ label the two orientations on either side of the repelling coordinate $r$. They are *not* the two RH-19 critical siblings, which live in $\sqrt\sigma$-scale windows around the distinct partition point $b$. The folded companion lobe in [\[eq:physical-second-row\]](#eq:physical-second-row){reference-type="eqref" reference="eq:physical-second-row"} is already included in the exact boundary identity and is not assigned a parity weight.

[\[rem:firewall\]]{#rem:firewall label="rem:firewall"} The equality represented by $D_{\sigma,a}^{\pm}$ belongs only to the second hybrid Duhamel row term with the same actual first-leg prefix and retained $u$. Marginalizing $u$ gives only the contraction bound $$\|\mathsf H^{\rm phys}_{\sigma,a,W}
   -\mathsf H^{\rm tan}_{\sigma,a,W}\|_1
 \le D_{\sigma,a}.$$ Replacing the first physical leg as well creates a separate hybrid term; there is no asserted equality between the fully physical two-leg law and the fully affine two-leg law. Nor does the theorem supply a global uniform row bound, an all-cycle $O(k\sigma)$ estimate, phase transport through $2k$ legs, cyclic trace control, parity/shell cancellation, full-trace replacement, or determinant gluing.

Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or completed-zeta divisor equality, and does not imply the Riemann Hypothesis. The next legitimate interface, RH-333, is to transport the common clearance phase and incoming moments through the full boundary cycle and either prove the retained-path $O(k\sigma)$ estimate on that one clock or isolate a genuine phase/stability obstruction. Its first admissible test is the possible escape gap in the raw mass-one forward all-affine chain. That test must be kept distinct from any cyclic bridge, Doob transform, or branch-complete non-Gaussian reference, which is not yet defined in the required physical data type.
