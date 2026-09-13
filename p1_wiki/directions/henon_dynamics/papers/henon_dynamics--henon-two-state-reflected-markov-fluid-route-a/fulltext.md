---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-two-state-reflected-markov-fluid-route-a"
canonical_tex: "henon_dynamics/henon_two_state_reflected_markov_fluid_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_two_state_reflected_markov_fluid_route_a/paper/main.pdf"
source_sha256: "4226269a6b7eceaefc8753e9fc304dca79320aa0ad4beb629a0718693a2eb7f0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Closed Recurrence and Stationary Atlas for a Two-State Reflected Markov Fluid

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_two_state_reflected_markov_fluid_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_two_state_reflected_markov_fluid_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_two_state_reflected_markov_fluid_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_two_state_reflected_markov_fluid_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify a two-state Markov-modulated fluid reflected at zero. The sign of one stationary drift separates positive recurrence, null recurrence, and linear escape. In the stable chamber we reconstruct the unique invariant law, including its boundary atom, two interior densities, every workload moment, and the regulator rate. Vanishing switching and drift rates are classified by closed environmental classes. This round is the **drift-trichotomy owner**.
author:
- 'HCS-C367 / HEN-O351'
date: 4 September 2026
title: 'A Closed Recurrence and Stationary Atlas for a Two-State Reflected Markov Fluid'
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3672026090400000000000000000000\>\<C3672026090400000000000000000000\>\]

# Model and sharp trichotomy

Let $J$ jump $0\to1$ at rate $a$ and $1\to0$ at rate $b$. The fluid slopes are $r_0=-d$ and $r_1=c$. For now $a,b,c,d>0$, and $$\label{eq:sk}
 Y_t=X_0+\int_0^t r_{J_s}\,ds,\qquad
 L_t=\sup_{0\le s\le t}(-Y_s)^+ ,\qquad X_t=Y_t+L_t.$$ Thus $L$ is the minimal right-continuous regulator and can increase only at $(X,J)=(0,0)$. Put $$\label{eq:drift}
 \bar r=\frac{ac-bd}{a+b}.$$

[\[thm:core\]]{#thm:core label="thm:core"} The formula [\[eq:sk\]](#eq:sk){reference-type="eqref" reference="eq:sk"} defines the unique global reflected PDMP. If $ac<bd$, it is positive recurrent with one invariant probability. If $ac=bd$, it is null recurrent and has no invariant probability. If $ac>bd$, it is transient and $X_t/t\to\bar r>0$ almost surely.

In the stable chamber let $$\kappa=\frac{bd-ac}{cd},\qquad
 p_*=\frac{bd-ac}{(a+b)d}.$$ The only boundary atom is $p_*$ at $(0,0)$, and on $x>0$ the state densities are $$\label{eq:density}
 f_0(x)=\frac{ac\kappa}{(a+b)d}e^{-\kappa x},\qquad
 f_1(x)=\frac{a\kappa}{a+b}e^{-\kappa x}.$$

The Skorokhod map on the half-line proves existence, uniqueness, and nonnegativity. The environment has stationary law $\pi=(b,a)/(a+b)$, so its ergodic theorem gives $Y_t/t\to\bar r$.

Observe $X$ at successive starts of state $1$. If $I_n\sim\mathrm{Exp}(b)$ and $O_n\sim\mathrm{Exp}(a)$ are the following on- and off-times, then $$\label{eq:lindley}
 W_{n+1}=\max\{0,W_n+cI_n-dO_n\},\qquad
 \mathbb E(cI_n-dO_n)=\frac cb-\frac da.$$ The increments are continuous, nondegenerate, and have finite variance. The negative-mean Lindley chain is positive recurrent; at zero mean it is recurrent but has only an infinite invariant measure; at positive mean it escapes linearly. Renewal normalization by $\mathbb E(I_n+O_n)=1/b+1/a$ yields [\[eq:drift\]](#eq:drift){reference-type="eqref" reference="eq:drift"}, including the asserted continuous-time speed.

For $ac<bd$, the stationary forward equations on $x>0$ are $$\label{eq:forward}
 0=d f_0'-a f_0+b f_1,\qquad
 0=-c f_1'+a f_0-b f_1.$$ Their sum and integrability give $d f_0=c f_1$. Substitution gives the decay rate $\kappa$. Boundary flux $ap_*=df_0(0)$ and normalization give [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"}. Irreducibility and positive recurrence give uniqueness.

\>0

# Mass, moments, and regulator

This revision is the **stationary-reconstruction owner**. Direct integration of [\[eq:density\]](#eq:density){reference-type="eqref" reference="eq:density"} gives $$\label{eq:marg}
 p_*+\int_0^\infty f_0(x)\,dx=\frac b{a+b},\qquad
 \int_0^\infty f_1(x)\,dx=\frac a{a+b}.$$ Moreover, $$\label{eq:positive}
 p_+:=\mathbb P\{X>0\}=\frac{a(c+d)}{(a+b)d}.$$ Hence $X\mid\{X>0\}$ is exponential with rate $\kappa$, and for every integer $n\ge1$, $$\label{eq:moments}
 \mathbb EX^n=p_+\frac{n!}{\kappa^n}.$$ The state-resolved moments are obtained by integrating each density.

Dividing [\[eq:sk\]](#eq:sk){reference-type="eqref" reference="eq:sk"} by $t$ in stationarity gives $$\label{eq:reg}
 \frac{L_t}{t}\longrightarrow-\bar r
 =\frac{bd-ac}{a+b}=d p_*$$ almost surely and in mean. The last equality is also the direct rate at which reflection cancels slope $-d$ on the boundary atom. Thus atom, densities, marginals, moments, and regulator use one consistent normalization.

\>1

# Every zero-rate face

This revision is the **closed-class boundary owner**. Degenerate cases must be stated per closed environmental class.

[\[prop:faces\]]{#prop:faces label="prop:faces"} Allow $a,b,c,d\ge0$.

1.  If $a,b>0$, Theorem [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"} applies for $c,d>0$. For $c=0<d$ the unique law is $\delta_0\otimes\pi$; for $d=0<c$ the speed is $ac/(a+b)>0$; for $c=d=0$ the workload is frozen and every $\nu\otimes\pi$ is invariant.

2.  If $a=0<b$, state $0$ is the unique closed class. For $d>0$ the unique invariant law is $\delta_{(0,0)}$; for $d=0$ every $\nu\otimes\delta_0$ is invariant. The value of $c$ affects only the finite pre-absorption excursion.

3.  If $b=0<a$, state $1$ is the unique closed class. For $c>0$ its paths escape at speed $c$ and it supports no invariant probability; for $c=0$ every $\nu\otimes\delta_1$ is invariant. The value of $d$ affects only the finite pre-absorption excursion.

4.  If $a=b=0$, both singleton classes are closed. Class $0$ has only $\delta_{(0,0)}$ when $d>0$ and arbitrary workload laws when $d=0$; class $1$ has no invariant law when $c>0$ and arbitrary workload laws when $c=0$. All global invariant probabilities are exactly convex mixtures of available class-supported laws. No reducible-face uniqueness is asserted.

The proof follows directly from deterministic motion inside each closed class and almost-sure absorption when precisely one transition rate vanishes.

# Evidence, sources, and route boundary

Exact rational panels audit [\[eq:drift\]](#eq:drift){reference-type="eqref" reference="eq:drift"}--[\[eq:reg\]](#eq:reg){reference-type="eqref" reference="eq:reg"}; a separate closed-class table audits Proposition [\[prop:faces\]](#prop:faces){reference-type="ref" reference="prop:faces"}. These are regression receipts only. The analytic argument owns the continuum classification.

Anick, Mitra, and Sondhi introduced a foundational Markov-fluid queueing model [@AMS]; Asmussen developed general stationary fluid-flow methods [@Asm]. We claim no priority. C351 owns discrete Jackson queues, C346 a deterministic two-dimensional oblique Skorokhod map, and C332 scalar play; none owns this stochastic Markov-additive reflected fluid.

There is no rational-prime carrier, primitive arithmetic orbit ledger, dynamical zeta, target analytic bridge, or natural same-clock unitary lift. Route A is rejected as $(A0_{\rm FAIL},A1_{\rm FAIL},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FAIL})$. Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`; no target zero match or Hilbert--Pólya operator is claimed.

9 D. Anick, D. Mitra, and M. M. Sondhi, *Stochastic theory of a data-handling system with multiple sources*, Bell System Technical Journal 61 (1982), 1871--1894. <https://doi.org/10.1002/j.1538-7305.1982.tb03089.x>. S. Asmussen, *Stationary distributions for fluid flow models with or without Brownian noise*, Stochastic Models 11 (1995), 21--49. <https://doi.org/10.1080/15326349508807330>.
