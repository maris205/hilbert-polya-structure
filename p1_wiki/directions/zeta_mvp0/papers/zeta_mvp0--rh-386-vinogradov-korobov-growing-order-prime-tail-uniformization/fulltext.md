---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-386-vinogradov-korobov-growing-order-prime-tail-uniformization"
canonical_tex: "zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization/main.pdf"
source_sha256: "d4dcd69877b04c382ba5cdc27918f841a40709c8064908c5063fecd222552269"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Vinogradov--Korobov Growing-Order Prime-Tail Uniformization

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-386-vinogradov-korobov-growing-order-prime-tail-uniformization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $3=p_1<p_2<\cdots$ be the odd primes, put $x=p_y$ and $L=\log x$, and define the strict tails $$P_r(y)=\sum_{p>x}(p^2-1)^{-r}\qquad(r\ge1).$$ Using the explicit Vinogradov--Korobov estimate of Johnston and Yang, we prove a quantitative comparison of $P_r$ with three successive kernels. With $$V=L^{3/5}(\log L)^{-1/5},\qquad
   \varepsilon_x=0.027L^{1.801}e^{-0.1853V},$$ the exact Stieltjes kernel $J_r$, power kernel $I_{2r}$, and leading term $K_r=x^{1-2r}/((2r-1)L)$ satisfy $$\left|\log\frac{P_r}{J_r}\right|\le14r\varepsilon_x,
   \quad
   0\le\log\frac{J_r}{I_{2r}}\le\frac{r}{x^2-1},
   \quad
   \left|\log\frac{I_{2r}}{K_r}\right|
   \le\frac{1}{(2r-1)L},$$ whenever $L\ge512$ and $7r\varepsilon_x\le1/2$. For a partition $\lambda=1^{k_1}2^{k_2}\cdots$, set $d=\sum rk_r$, $H=\sum k_r/(2r-1)$, and $H_2=\sum k_r/(2r-1)^2$. The corresponding product has the refined uniform expansion $$\log\frac{\mathcal P_\lambda}{\mathcal M_\lambda}
   =-\frac{H}{L}
   +O\!\left(d\varepsilon_x+\frac{d}{x^2-1}+\frac{H_2}{L^2}\right),$$ with explicit constants $14,1,2$. Thus $d\varepsilon_x+d/x^2\to0$ is a robust source-and-power condition, while the leading equivalent holds precisely when $H/L\to0$. In particular $\log d=o(V)$ and $H=o(L)$ suffice. For a single order the range $\log R=o(V)$ is uniform, and one may sharpen it to $R\le e^{(0.1853-\delta)V}$ for fixed $0<\delta<0.1853$. The family $\lambda=1^{\lfloor cL\rfloor}$ has leading ratio tending to $e^{-c}$, proving the $H/L$ obstruction is real. An exact 96-row artifact reproduces the algebraic interfaces but is not an analytic proof.
author:
- RH research program
bibliography:
- references.bib
date: 'August 8, 2026'
title: |
  Vinogradov--Korobov Growing-Order\
  Prime-Tail Uniformization
```

## Markdown 正文

**Keywords:** explicit prime number theorem; Vinogradov--Korobov estimate; strict Stieltjes boundary; prime-square tail; growing integer partitions; uniform asymptotics.

# Scope and notation

The fixed-order asymptotic $$P_r(y)\sim\frac{x^{1-2r}}{(2r-1)\log x}$$ follows from the prime number theorem when $r$ is fixed. That statement does not by itself permit $r$, the degree of a partition, or the number of factors to grow with $y$. The purpose of this paper is to pay for those three kinds of growth explicitly. The new input is the global explicit Vinogradov--Korobov estimate of Johnston and Yang [@JohnstonYang2023 Theorem 1.4, equation (1.8)]; the prior fixed-order prime-tail calculation in RH-384 is used only as a finite regression target for the accompanying artifact [@RH384].

Throughout, $$3=p_1<p_2<\cdots,\qquad x=p_y,\qquad L=\log x,$$ and $r$ is a positive integer. Write $$\vartheta(t)=\sum_{p\le t}\log p,
 \qquad E(t)=\vartheta(t)-t.$$ The strict prime tail and its three comparison kernels are $$\begin{aligned}
 P_r(y)&=\sum_{p>x}\frac{1}{(p^2-1)^r},
 \label{eq:Pr}\\
 h_r(t)&=\frac{(t^2-1)^{-r}}{\log t},
 &J_r(x)&=\int_x^\infty h_r(t)\,dt,
 \label{eq:Jr}\\
 I_{2r}(x)&=\int_x^\infty\frac{t^{-2r}}{\log t}\,dt,
 &K_r(x)&=\frac{x^{1-2r}}{(2r-1)L}.
 \label{eq:IK}\end{aligned}$$ The endpoint in [\[eq:Pr\]](#eq:Pr){reference-type="eqref" reference="eq:Pr"} is always strict. In particular, $$P_r(y)=\frac{1}{(p_{y+1}^2-1)^r}+P_r(y+1).
 \label{eq:successor}$$ This exact successor identity distinguishes $p>x$ from $p\ge x$ even though their leading asymptotics agree.

Set $$V(L)=L^{3/5}(\log L)^{-1/5},\qquad
 \varepsilon_x=\frac{27}{1000}L^{1801/1000}
 \exp\!\left(-\frac{1853}{10000}V(L)\right).
 \label{eq:epsilon}$$ Johnston and Yang prove that, for every $t\ge23$, $$|E(t)|\le t\varepsilon_t.
 \label{eq:JY}$$ Their Corollary 1.2, equation (1.5), and the $X=\log2$ row of their Table 1 are retained in the external source lock as provenance locators, but the derived square-root-exponential fallback is not used or asserted as a result here. Only [\[eq:JY\]](#eq:JY){reference-type="eqref" reference="eq:JY"} enters the proof.

[\[prop:eta-monotone\]]{#prop:eta-monotone label="prop:eta-monotone"} The function of $L$ on the right of [\[eq:epsilon\]](#eq:epsilon){reference-type="eqref" reference="eq:epsilon"} is strictly decreasing for $L\ge512$.

Logarithmic differentiation gives $$\frac{d}{dL}\log\varepsilon
 =\frac1L\left[
 \frac{1801}{1000}
 -\frac{1853}{10000}V(L)
 \left(\frac35-\frac{1}{5\log L}\right)
 \right].$$ For $L\ge512$, one has $\log L>6$, $\sqrt L>22$, and $V(L)\ge\sqrt L$. The last inequality is equivalent to $\sqrt L\ge\log L$, which holds on this range. Hence the factor in parentheses is at least $17/30$, and $$\frac{1853}{10000}\,22\,\frac{17}{30}
 -\frac{1801}{1000}>0.$$ The displayed derivative is therefore negative.

# The strict Stieltjes transfer

The endpoint and the boundary term must be kept exact before applying the source estimate.

[\[lem:stieltjes\]]{#lem:stieltjes label="lem:stieltjes"} For $x=p_y$ and $r\ge1$, $$P_r(y)=\int_{(x,\infty)}h_r(t)\,d\vartheta(t)
 =-\vartheta(x)h_r(x)-\int_x^\infty\vartheta(t)h_r'(t)\,dt.
 \label{eq:stieltjes}$$ Consequently, $$P_r(y)-J_r(x)
 =-E(x)h_r(x)-\int_x^\infty E(t)h_r'(t)\,dt.
 \label{eq:error-identity}$$

At a prime $p$, the jump of $\vartheta$ is $\log p$, so the first integral equals [\[eq:Pr\]](#eq:Pr){reference-type="eqref" reference="eq:Pr"}. Stieltjes integration by parts on $(x,R]$ gives the second expression with the lower boundary $-\vartheta(x)h_r(x)$. The upper boundary tends to zero; for example $\vartheta(R)\le R\log R$ and $h_r(R)=O(R^{-2r}/\log R)$. Substitute $\vartheta(t)=t+E(t)$ and use $$-xh_r(x)-\int_x^\infty t h_r'(t)\,dt
 =\int_x^\infty h_r(t)\,dt=J_r(x)$$ to obtain [\[eq:error-identity\]](#eq:error-identity){reference-type="eqref" reference="eq:error-identity"}.

[\[lem:hazard\]]{#lem:hazard label="lem:hazard"} The logarithmic hazard $$q_r(t)=-\frac{h_r'(t)}{h_r(t)}
 =\frac{2rt}{t^2-1}+\frac{1}{t\log t}
 \label{eq:hazard}$$ is positive and strictly decreasing for $t>1$. Moreover, $$J_r(x)\ge\frac{h_r(x)}{q_r(x)},\qquad
 xq_r(x)\le3r\quad(x\ge23).
 \label{eq:hazard-bounds}$$

Both summands in [\[eq:hazard\]](#eq:hazard){reference-type="eqref" reference="eq:hazard"} are positive and strictly decreasing: their derivatives have numerators $-2r(t^2+1)$ and $-(\log t+1)$, respectively, after multiplication by positive denominators. Hence $$h_r(x)=\int_x^\infty q_r(t)h_r(t)\,dt
 \le q_r(x)J_r(x).$$ Finally $$xq_r(x)=\frac{2rx^2}{x^2-1}+\frac1{\log x}
 \le r\left(2+\frac{2}{528}+\frac13\right)<3r$$ for $x\ge23$.

[\[prop:source-transfer\]]{#prop:source-transfer label="prop:source-transfer"} Assume $L\ge512$. Then $$\left|\frac{P_r(y)}{J_r(x)}-1\right|\le7r\varepsilon_x.
 \label{eq:relative-source}$$ If in addition $7r\varepsilon_x\le1/2$, then $$\boxed{\left|\log\frac{P_r(y)}{J_r(x)}\right|
 \le14r\varepsilon_x.}
 \label{eq:log-source}$$

Since $h_r'<0$, Proposition [\[prop:eta-monotone\]](#prop:eta-monotone){reference-type="ref" reference="prop:eta-monotone"}, [\[eq:JY\]](#eq:JY){reference-type="eqref" reference="eq:JY"}, and [\[eq:error-identity\]](#eq:error-identity){reference-type="eqref" reference="eq:error-identity"} imply $$\begin{aligned}
 |P_r-J_r|
 &\le\varepsilon_x\left(xh_r(x)+
       \int_x^\infty t(-h_r'(t))\,dt\right)\\
 &=\varepsilon_x\bigl(2xh_r(x)+J_r(x)\bigr).\end{aligned}$$ Lemma [\[lem:hazard\]](#lem:hazard){reference-type="ref" reference="lem:hazard"} gives $xh_r(x)/J_r(x)\le3r$, so the relative error is at most $(6r+1)\varepsilon_x\le7r\varepsilon_x$. If this is at most $1/2$, then $|\log(1+u)|\le2|u|$ for $|u|\le1/2$, proving [\[eq:log-source\]](#eq:log-source){reference-type="eqref" reference="eq:log-source"}.

The two copies of $xh_r(x)$ in the proof have different origins: one is the strict Stieltjes boundary and one comes from $\int t(-h_r')=xh_r+J_r$. Deleting the boundary changes the transfer algebra. Conversely, the leading asymptotic alone cannot detect an inclusive-endpoint mutation, which is why [\[eq:successor\]](#eq:successor){reference-type="eqref" reference="eq:successor"} is also retained.

# Two kernel comparisons

[\[lem:J-I\]]{#lem:J-I label="lem:J-I"} For every $x>1$ and $r\ge1$, $$0\le\log\frac{J_r(x)}{I_{2r}(x)}
 \le-r\log(1-x^{-2})
 \le\frac{r}{x^2-1}.
 \label{eq:J-I}$$ No smallness assumption on $r/x^2$ is required.

The quotient $J_r/I_{2r}$ is the weighted average, with positive weight $t^{-2r}/\log t$, of $(1-t^{-2})^{-r}$. That factor decreases from $(1-x^{-2})^{-r}$ to $1$. This gives the first two inequalities. The last follows from $-\log(1-u)\le u/(1-u)$ with $u=x^{-2}$.

The optional coarser estimate $\log(J_r/I_{2r})\le4r/x^2$ used in an earlier finite interface follows immediately on the present range (and in particular under the formerly declared condition $r/x^2\le3/8$). It is not used in the canonical ledger.

[\[lem:I-K\]]{#lem:I-K label="lem:I-K"} Put $$a_r=\frac{1}{(2r-1)L},\qquad
 G(a)=\int_0^\infty\frac{e^{-v}}{1+av}\,dv.$$ Then $$\frac{I_{2r}(x)}{K_r(x)}=G(a_r),\qquad
 \frac1{1+a}\le G(a)\le1,
 \label{eq:G-bounds}$$ and therefore $$\left|\log\frac{I_{2r}(x)}{K_r(x)}\right|
 \le a_r=\frac{1}{(2r-1)L}.
 \label{eq:I-K}$$ For $0\le a\le1/4$ one also has $$0\le\log G(a)+a\le2a^2.
 \label{eq:G-refined}$$

Set $t=xe^{v/(2r-1)}$ in $I_{2r}$. This gives the identity in [\[eq:G-bounds\]](#eq:G-bounds){reference-type="eqref" reference="eq:G-bounds"}. If $V_0$ is exponentially distributed with mean one, then $G(a)=\mathbb E(1+aV_0)^{-1}$. Jensen's inequality and the trivial upper bound give $1/(1+a)\le G(a)\le1$, hence $|\log G(a)|\le\log(1+a)\le a$.

For the refinement, $1/(1+a)\ge e^{-a}$ implies $\log G(a)+a\ge0$. The pointwise inequality $(1+z)^{-1}\le1-z+z^2$ and the exponential moments $\mathbb EV_0=1$, $\mathbb EV_0^2=2$ yield $G(a)\le1-a+2a^2$. Since $\log u\le u-1$, $\log G(a)+a\le2a^2$.

# Growing partitions and the uniform theorem

Let $\lambda=1^{k_1}2^{k_2}\cdots$ be a nonempty integer partition, with only finitely many nonzero $k_r$. Define $$\ell=\sum_rk_r,\qquad d=\sum_rrk_r,\qquad
 R=\max\{r:k_r>0\},
 \label{eq:degree-order}$$ and $$H=\sum_r\frac{k_r}{2r-1},\qquad
 H_2=\sum_r\frac{k_r}{(2r-1)^2}.
 \label{eq:H}$$ Thus $0<H_2\le H\le d$ and $R\le d$. For $A_r\in\{P_r,J_r,I_{2r},K_r\}$ write $$\mathcal A_\lambda=\prod_r A_r^{k_r},$$ using the corresponding calligraphic letter. In particular, $$\mathcal M_\lambda(x)
 =x^{-(2d-\ell)}L^{-\ell}
  \prod_r(2r-1)^{-k_r}.
 \label{eq:Mlambda}$$

[\[thm:master\]]{#thm:master label="thm:master"} Let $x=p_y$, $L\ge512$, and let $\lambda$ be a nonempty partition such that $7R\varepsilon_x\le1/2$. Then $$\begin{aligned}
 \left|\log\frac{\mathcal P_\lambda}{\mathcal J_\lambda}\right|
 &\le14d\varepsilon_x,
 \label{eq:ledger-J}\\
 \left|\log\frac{\mathcal P_\lambda}{\mathcal I_\lambda}\right|
 &\le14d\varepsilon_x+\frac{d}{x^2-1},
 \label{eq:ledger-I}\\
 \left|\log\frac{\mathcal P_\lambda}{\mathcal M_\lambda}\right|
 &\le14d\varepsilon_x+\frac{d}{x^2-1}+\frac{H}{L}.
 \label{eq:ledger-M}\end{aligned}$$ More precisely, $$\boxed{
 \left|\log\frac{\mathcal P_\lambda}{\mathcal M_\lambda}+\frac{H}{L}\right|
 \le14d\varepsilon_x+\frac{d}{x^2-1}+\frac{2H_2}{L^2}.}
 \label{eq:refined-master}$$

Sum Proposition [\[prop:source-transfer\]](#prop:source-transfer){reference-type="ref" reference="prop:source-transfer"} with multiplicities $k_r$; the result is $14\varepsilon_x\sum_r r k_r=14d\varepsilon_x$. Sum Lemma [\[lem:J-I\]](#lem:J-I){reference-type="ref" reference="lem:J-I"} to obtain $d/(x^2-1)$, and sum [\[eq:I-K\]](#eq:I-K){reference-type="eqref" reference="eq:I-K"} to obtain $H/L$. Finally $a_r\le1/L\le1/4$, so summing [\[eq:G-refined\]](#eq:G-refined){reference-type="eqref" reference="eq:G-refined"} gives $$0\le\log\frac{\mathcal I_\lambda}{\mathcal M_\lambda}+\frac HL
 \le\frac{2H_2}{L^2}.$$ The triangle inequality proves [\[eq:refined-master\]](#eq:refined-master){reference-type="eqref" reference="eq:refined-master"}.

[\[cor:criterion\]]{#cor:criterion label="cor:criterion"} Let $\lambda_y$ be any sequence of nonempty partitions. If $$d_y\varepsilon_{p_y}+\frac{d_y}{p_y^2}\longrightarrow0,
 \label{eq:source-power-condition}$$ then $\mathcal P_{\lambda_y}/\mathcal J_{\lambda_y}\to1$ and $\mathcal P_{\lambda_y}/\mathcal I_{\lambda_y}\to1$. Under [\[eq:source-power-condition\]](#eq:source-power-condition){reference-type="eqref" reference="eq:source-power-condition"}, $$\frac{\mathcal P_{\lambda_y}}{\mathcal M_{\lambda_y}}\longrightarrow1
 \quad\Longleftrightarrow\quad
 \frac{H_y}{L_y}\longrightarrow0.
 \label{eq:iff-H}$$ Still under [\[eq:source-power-condition\]](#eq:source-power-condition){reference-type="eqref" reference="eq:source-power-condition"}, the explicit expansion is $$\log\frac{\mathcal P_{\lambda_y}}{\mathcal M_{\lambda_y}}
 =-\frac{H_y}{L_y}
 +O\!\left(d_y\varepsilon_{p_y}+\frac{d_y}{p_y^2-1}
              +\frac{H_{2,y}}{L_y^2}\right).
 \label{eq:partition-expansion}$$

Condition [\[eq:source-power-condition\]](#eq:source-power-condition){reference-type="eqref" reference="eq:source-power-condition"} implies $7R_y\varepsilon_{p_y}\le7d_y\varepsilon_{p_y}\le1/2$ eventually, so Theorem [\[thm:master\]](#thm:master){reference-type="ref" reference="thm:master"} applies. The first two conclusions follow from [\[eq:ledger-J\]](#eq:ledger-J){reference-type="eqref" reference="eq:ledger-J"}--[\[eq:ledger-I\]](#eq:ledger-I){reference-type="eqref" reference="eq:ledger-I"}. The refined estimate gives [\[eq:partition-expansion\]](#eq:partition-expansion){reference-type="eqref" reference="eq:partition-expansion"}. Since $H_2\le H$, $$\frac{2H_2}{L^2}\le\frac2L\frac HL.$$ Thus $H/L\to0$ is sufficient. Conversely, with $A_y=14d_y\varepsilon_{p_y}+d_y/(p_y^2-1)$, the refined estimate gives the explicit lower bound $$\left|\log\frac{\mathcal P_{\lambda_y}}{\mathcal M_{\lambda_y}}\right|
 \ge\left(1-\frac2{L_y}\right)\frac{H_y}{L_y}-A_y.$$ Here $A_y\to0$, so convergence of the ratio to one forces $H_y/L_y\to0$.

[\[cor:uniform-families\]]{#cor:uniform-families label="cor:uniform-families"} For each $y$, let $\mathfrak F_y$ be a nonempty family of finite nonempty partitions, and suppose $$D_y=\sup_{\lambda\in\mathfrak F_y}d(\lambda)<\infty,
 \qquad
 H_y^*=\sup_{\lambda\in\mathfrak F_y}H(\lambda)<\infty.$$ If $$D_y\varepsilon_{p_y}+\frac{D_y}{p_y^2}\longrightarrow0,
 \label{eq:uniform-source-power}$$ then $$\begin{aligned}
 \sup_{\lambda\in\mathfrak F_y}
 \left|\log\frac{\mathcal P_\lambda}{\mathcal J_\lambda}\right|&\longrightarrow0,\\
 \sup_{\lambda\in\mathfrak F_y}
 \left|\log\frac{\mathcal P_\lambda}{\mathcal I_\lambda}\right|&\longrightarrow0.\end{aligned}$$ Moreover, $$\sup_{\lambda\in\mathfrak F_y}
 \left|\frac{\mathcal P_\lambda}{\mathcal M_\lambda}-1\right|\longrightarrow0
 \quad\Longleftrightarrow\quad
 \frac{H_y^*}{L_y}\longrightarrow0.
 \label{eq:uniform-iff}$$

Since $R(\lambda)\le d(\lambda)\le D_y$, condition [\[eq:uniform-source-power\]](#eq:uniform-source-power){reference-type="eqref" reference="eq:uniform-source-power"} makes the source smallness hypothesis uniformly valid. Equations [\[eq:ledger-J\]](#eq:ledger-J){reference-type="eqref" reference="eq:ledger-J"} and [\[eq:ledger-I\]](#eq:ledger-I){reference-type="eqref" reference="eq:ledger-I"} give the first two assertions. Put $$A_y^*=14D_y\varepsilon_{p_y}+\frac{D_y}{p_y^2-1}.$$ For every $\lambda\in\mathfrak F_y$, [\[eq:refined-master\]](#eq:refined-master){reference-type="eqref" reference="eq:refined-master"} and $H_2(\lambda)\le H(\lambda)$ give $$\left|\log\frac{\mathcal P_\lambda}{\mathcal M_\lambda}+\frac{H(\lambda)}{L_y}\right|
 \le A_y^*+\frac2{L_y}\frac{H(\lambda)}{L_y}.$$ The upper bound proves sufficiency. Taking suprema in the corresponding reverse-triangle lower bound gives $$\sup_{\lambda\in\mathfrak F_y}
 \left|\log\frac{\mathcal P_\lambda}{\mathcal M_\lambda}\right|
 \ge\left(1-\frac2{L_y}\right)\frac{H_y^*}{L_y}-A_y^*.$$ Uniform convergence of the positive ratios to one is equivalent to uniform convergence of their logarithms to zero, and necessity follows.

The quantity $d\varepsilon_x$ is a robust sufficient payment obtained from the available source upper bound. It is not asserted to be logically necessary for the actual, unknown signed prime error.

[\[cor:sufficient\]]{#cor:sufficient label="cor:sufficient"} If $$\log d_y=o(V(L_y)),\qquad H_y=o(L_y),
 \label{eq:sufficient}$$ then $\mathcal P_{\lambda_y}/\mathcal M_{\lambda_y}\to1$.

Because $\log L=o(V(L))$, equation [\[eq:epsilon\]](#eq:epsilon){reference-type="eqref" reference="eq:epsilon"} and $\log d=o(V)$ give $d\varepsilon_x\to0$. Also $V(L)=o(L)$, so $d/x^2\to0$. Apply Corollary [\[cor:criterion\]](#cor:criterion){reference-type="ref" reference="cor:criterion"} and $H=o(L)$.

[\[cor:single-r\]]{#cor:single-r label="cor:single-r"} Let $R_y\ge1$ be integers. If $\log R_y=o(V(L_y))$, then $$\max_{1\le r\le R_y}
 \left|\log\frac{P_r(y)}{K_r(p_y)}\right|\longrightarrow0.
 \label{eq:single-uniform}$$ More sharply, [\[eq:single-uniform\]](#eq:single-uniform){reference-type="eqref" reference="eq:single-uniform"} holds whenever, for some fixed $0<\delta<0.1853$, $$R_y\le\exp\bigl((0.1853-\delta)V(L_y)\bigr)
 \label{eq:delta-range}$$ for all sufficiently large $y$.

For $r\le R_y$, the three one-factor errors are bounded by $$14R_y\varepsilon_x+\frac{R_y}{x^2-1}+\frac1L.$$ The first growth hypothesis makes the first two terms vanish. Under [\[eq:delta-range\]](#eq:delta-range){reference-type="eqref" reference="eq:delta-range"}, $$R_y\varepsilon_x\le0.027L^{1.801}e^{-\delta V(L)}\longrightarrow0,$$ and $R_y/x^2\to0$ because $V(L)=o(L)$. The source smallness condition is therefore automatic eventually.

# Sharpness of the leading-kernel condition

[\[prop:sharpness\]]{#prop:sharpness label="prop:sharpness"} Fix $c>0$ and let $$\lambda_y=1^{k_y},\qquad k_y=\lfloor cL_y\rfloor.$$ Then $$\frac{\mathcal P_{\lambda_y}}{\mathcal M_{\lambda_y}}\longrightarrow e^{-c}.
 \label{eq:sharpness}$$

Here $d_y=H_y=H_{2,y}=k_y$. The source and power errors satisfy $k_y\varepsilon_{p_y}+k_y/p_y^2\to0$, while $k_y/L_y\to c$ and $k_y/L_y^2\to0$. Equation [\[eq:refined-master\]](#eq:refined-master){reference-type="eqref" reference="eq:refined-master"} therefore gives $\log(\mathcal P_{\lambda_y}/\mathcal M_{\lambda_y})\to-c$.

Thus a degree condition alone cannot guarantee the leading equivalent. The statistic $H$ is not an artifact of the proof: even the simplest growing partition detects the accumulated first correction of the logarithmic integral kernel.

# Exact artifact, provenance, and claim boundary {#sec:artifact}

The companion artifact has epistemic role `reproduction_not_analytic_proof`. It compiles exactly 96 structured oracle rows:

  interface                                                  rows
  -------------------------------------------------------- ------
  source constants, endpoint, hazard, and kernel algebra       16
  fixed orders $r\in\{1,2,3,4,8,16,32,64\}$                     8
  integer partitions of degrees at most $8$                    66
  growth envelopes and sharpness                                6
  total                                                        96

Every scalar field is checked by an independent exact-type semantic verifier. Twenty-four theorem-interface mutations---including an inclusive endpoint, a missing Stieltjes boundary, a reversed hazard or Jensen inequality, wrong $2r-1$ factors, deletion of $H/L$, and a degree-only leading claim---are rejected. Seven separate source-metadata and strict-JSON attacks are also rejected. The canonical certificate has 29,717 bytes and SHA-256

`64761d3a85afdee4682982ad545d20a66d2ed69926764bcc9580e0dc8c5f8710`.

The immutable Git closure contains 59 exact release blobs: the 51-row RH-384 inherited closure and its eight standard release files. The new Johnston--Yang input is one logical external lock, giving 60 logical source objects. The author-manuscript PDF is not redistributed. Its lock records the versioned URL, DOI, MIME type, 278,380-byte length, 22-page count, and SHA-256, as well as the versioned source-tar and source- `main.tex` hashes. Network verification is disabled by default and requires the explicit `–network` flag. The publication archive contains the lock record and verifier, but excludes the external PDF and source tar.

The finite regression inherited from RH-384 checks only the degree-eight partition bookkeeping. It neither establishes the Johnston--Yang estimate nor proves any limiting statement. Conversely, the analytic proof above does not depend on a finite numerical fit.

In the surrounding prime-dynamics program, all clocks remain fixed and finite before any prefix limit, and only the universally safe phasewise class with $c_{11}=0$ is in scope. Nothing in this paper gives a growing clock, an active-$c_{11}$ cancellation theorem, a projectively compatible selector, an effective threshold, an operator or trace formula, a zeta-zero identification, or a proof of the Riemann hypothesis. Gates A--E remain false.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

The analytic proof, exact certificate compiler, tests, official closed Draft 2020--12 schema, source-lock records, opt-in verifier, and archive replay tools accompany the paper. The Johnston--Yang PDF and source tar are not redistributed; their exact remote identifiers are recorded in the external lock.

#### Author contributions.

The author is responsible for the conceptualization, proof, software, validation, writing, and release audit.

#### Funding.

No external funding was received.

#### Competing interests.

The author declares no competing interests.

#### Ethics.

No human participants, animals, personal data, or clinical interventions are involved.

#### AI assistance.

AI-assisted tools were used for proof-interface enumeration, adversarial testing, manuscript drafting, and release auditing. All mathematical claims, citations, source locks, and final text were reviewed under author responsibility.
