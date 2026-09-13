---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--93-random-push-pop-stack-cocycles"
canonical_tex: "symbolic_dynamics/papers/93-random-push-pop-stack-cocycles/main.tex"
canonical_pdf: "symbolic_dynamics/papers/93-random-push-pop-stack-cocycles/main.pdf"
source_sha256: "2bb37524d9a4d7a826d0306364245c96b4ff4ba697213c25bcc67b172fe480a8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Running-Maximum Normal Forms for Random Push--Pop Stack Cocycles: Image Contraction, Fibre Growth, and Two Exact Thresholds

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/93-random-push-pop-stack-cocycles>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/93-random-push-pop-stack-cocycles/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/93-random-push-pop-stack-cocycles/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/93-random-push-pop-stack-cocycles/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/93-random-push-pop-stack-cocycles/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $X=\mathcal A^{\mathbb N_0}$, where $|\mathcal A|=b\geq2$. At each time, independently apply the left shift $D$ with probability $p$, or prefix a uniformly chosen letter with probability $1-p$. If $S_n$ counts shifts minus prefixes and $M_n=\max_{0\leq k\leq n}S_k$, every length-$n$ cocycle has the exact normal form $$\Phi_n=C_{u_n}D^{J_n},\qquad J_n=M_n,\qquad |u_n|=I_n=M_n-S_n.$$ Consequently, $\Phi_n(X)$ is one cylinder of diameter $b^{-I_n}$ and every point in that cylinder has exactly $b^{J_n}$ preimages. We prove the almost-sure rates $(1-2p)_+\log b$ for image contraction and $(2p-1)_+\log b$ for fibre growth. For $A_n=\mathbb Eb^{J_n}$ and $\lambda=bp+(1-p)/b$, a first-passage expansion and an exponential change of measure give the full trichotomy: $A_n$ converges if $p<1/(b+1)$, grows linearly at $p=1/(b+1)$, and is asymptotic to an explicit constant times $\lambda^n$ above that threshold. Thus the annealed exponent turns on at $1/(b+1)$, while synchronization and quenched fibre growth change at $1/2$. At $p=1/2$, the typical logarithmic scales are of order $\sqrt n$, although the annealed fibre moment is exponential. The general monoid-walk, reflected-walk, and random-cocycle frameworks are classical; this internal note makes no absolute novelty or priority claim.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: |
  Running-Maximum Normal Forms for Random Push--Pop Stack Cocycles:\
  Image Contraction, Fibre Growth, and Two Exact Thresholds
```

## Markdown 正文

# Introduction

A one-sided shift forgets one symbol, while a prefix map inserts one. Their composition is elementary, but a random sequence of the two operations has two different records of information loss: unmatched shifts create preimages, and unmatched prefixes shrink the image to a cylinder. The two records are not independent. They are the running maximum and the drawdown of the same nearest-neighbour walk.

This note turns that observation into an exact random dynamical calculation. One-sided full shifts and their cylinder geometry are standard symbolic systems [@LindMarcus1995]; random cocycles belong to the general framework developed in, for example, Arnold's monograph [@Arnold1998]. The algebra also has a clear prior owner boundary. If one fixes a single prefix letter, the shift and prefix maps realize the bicyclic relation $DC=\operatorname{Id}$. Normal forms, drift, entropy, and harmonic measures for random walks on suitable groups and monoids have an established theory, including Mairesse's treatment of zero-automatic monoids and the bicyclic example [@Mairesse2005]. Ballot identities, first-passage laws, and reflected random walks are classical probability [@Feller1968; @Asmussen2003].

The residual purpose here is narrower: we couple that normal form to exact symbolic image and fibre observables, then compute the exponential moment of the fibre degree with its reflection correction intact. Four conclusions result.

1.  Every finite cocycle is one prefix followed by a power of the shift; the two exponents are exactly $I_n=M_n-S_n$ and $J_n=M_n$.

2.  The pathwise image contraction and fibre-growth rates have the sharp drift threshold $p=1/2$, and uniform synchronization occurs exactly for $p<1/2$.

3.  The annealed fibre degree has a different threshold, $p=1/(b+1)$. We give its finite ballot sum, its subcritical limit, its critical linear coefficient, and its supercritical exponential prefactor.

4.  At $p=1/2$, each of $I_n/\sqrt n$ and $J_n/\sqrt n$, marginally, converges in law to a half-normal variable, whereas $\mathbb Eb^{J_n}$ grows exponentially. No joint-limit claim is made.

All logarithms are natural. External release is **HOLD**: the displayed conjunction is supported by complete proofs and exact controls, but the note does not claim that no equivalent specialization appears in the monoid, queueing, or random-dynamical-systems literature.

# The cocycle and its finite normal form {#sec:model}

Fix a finite alphabet $\mathcal A$ with cardinality $b\geq2$, and put $X=\mathcal A^{\mathbb N_0}$. For distinct $x,y\in X$, let $$\kappa(x,y)=\min\{k\geq0:x_k\neq y_k\},
 \qquad d_b(x,y)=b^{-\kappa(x,y)},$$ with $d_b(x,x)=0$. If $u=u_0\cdots u_{r-1}\in\mathcal A^r$, write $$[u]=\{x\in X:x_0\cdots x_{r-1}=u\},
 \qquad C_u(x)=ux.$$ The restriction $b\geq2$ is essential for this formulation. If $b=1$, $X$ is a singleton, every generator is the identity map, the stated normal form is nonunique, and every image has diameter zero rather than the formal quantity $b^{-I}=1$. The empty word $\epsilon$ satisfies $C_\epsilon=\operatorname{Id}$. For a letter $a\in\mathcal A$, write $C_a$ for the corresponding one-letter prefix map, and let $$D(x_0x_1x_2\ldots)=x_1x_2\ldots .$$ The defining cancellation is $$\label{eq:cancellation}
 DC_a=\operatorname{Id}\qquad(a\in\mathcal A).$$

Let $(\omega_t)_{t\geq1}$ be iid with $$\label{eq:environment-law}
 \mathbb P(\omega_t=D)=p,
 \qquad
 \mathbb P(\omega_t=C_a)=\frac{q}{b},
 \qquad q=1-p,$$ and define the forward cocycle $$\label{eq:cocycle}
 \Phi_0=\operatorname{Id},
 \qquad
 \Phi_n=\omega_n\circ\cdots\circ\omega_1.$$ The uniform law on prefix letters is convenient but inessential for all length, image-diameter, and fibre-degree statements below.

Set $$\label{eq:walk}
 \xi_t=\begin{cases}+1,&\omega_t=D,\\-1,&\omega_t=C_a\text{ for some }a,
 \end{cases}
 \qquad
 S_n=\sum_{t=1}^n\xi_t,
 \qquad
 M_n=\max_{0\leq k\leq n}S_k.$$ Thus $\mathbb E\xi_t=2p-1$.

[\[thm:normal-form\]]{#thm:normal-form label="thm:normal-form"} For every finite environment word, there is a unique word $u_n\in\mathcal A^*$ and a unique integer $J_n\geq0$ such that $$\label{eq:normal-form}
 \Phi_n=C_{u_n}D^{J_n}.$$ Their lengths are $$\label{eq:IJ}
 \boxed{\quad J_n=M_n,\qquad I_n:=|u_n|=M_n-S_n.\quad}$$ Moreover, $$\label{eq:image-fibre}
 \Phi_n(X)=[u_n],
 \qquad
 \operatorname{diam}\Phi_n(X)=b^{-I_n},
 \qquad
 \#\Phi_n^{-1}(y)=b^{J_n}\quad(y\in[u_n]).$$

We induct on $n$. The empty product has $u_0=\epsilon$ and $J_0=0$. Suppose $\Phi_n=C_uD^J$.

If $\omega_{n+1}=C_a$, then $\Phi_{n+1}=C_{au}D^J$. The walk decreases by one and its running maximum does not change, so $J=M_n=M_{n+1}$ and $|au|=M_{n+1}-S_{n+1}$.

Suppose next that $\omega_{n+1}=D$. If $u=av$ is nonempty, then [\[eq:cancellation\]](#eq:cancellation){reference-type="eqref" reference="eq:cancellation"} gives $\Phi_{n+1}=C_vD^J$. Here $I_n=M_n-S_n>0$, so $S_n+1\leq M_n$. The maximum and $J$ stay fixed, while the prefix length decreases by one. If $u=\epsilon$, then $S_n=M_n$ and $$\Phi_{n+1}=D^{J+1},\qquad
 S_{n+1}=M_{n+1}=M_n+1.$$ This proves existence and [\[eq:IJ\]](#eq:IJ){reference-type="eqref" reference="eq:IJ"}.

The map $D^J$ is onto and every point of $X$ has exactly $b^J$ preimages under it. The map $C_u$ is injective with image $[u]$. Hence [\[eq:image-fibre\]](#eq:image-fibre){reference-type="eqref" reference="eq:image-fibre"} follows, including the exact cylinder diameter in the metric $d_b$. Finally, the image determines $u$ and $|u|$, while the constant fibre cardinality determines $J$. The normal form is unique.

For later use, write $\operatorname{deg}(\Phi_n)=b^{J_n}$ for this common fibre cardinality on $\Phi_n(X)$.

[\[rem:bicyclic\]]{#rem:bicyclic label="rem:bicyclic"} For a fixed prefix letter, [\[eq:cancellation\]](#eq:cancellation){reference-type="eqref" reference="eq:cancellation"} is the bicyclic relation. The theorem does not claim ownership of that algebraic normal form. Its role here is to identify the two symbolic observables in [\[eq:image-fibre\]](#eq:image-fibre){reference-type="eqref" reference="eq:image-fibre"} with $M_n$ and $M_n-S_n$ without a subadditive error.

# Quenched geometry and the drift threshold {#sec:quenched}

Define the quenched fibre-growth and image-contraction rates by $$\label{eq:quenched-rates}
 g_{\mathrm q}(p)=\lim_{n\to\infty}\frac1n\log b^{J_n},
 \qquad
 c_{\mathrm q}(p)=\lim_{n\to\infty}
   -\frac1n\log\operatorname{diam}\Phi_n(X),$$ whenever the limits exist.

[\[thm:quenched\]]{#thm:quenched label="thm:quenched"} For every $0\leq p\leq1$, both limits in [\[eq:quenched-rates\]](#eq:quenched-rates){reference-type="eqref" reference="eq:quenched-rates"} exist almost surely and $$\label{eq:quenched-formulas}
 \boxed{
 g_{\mathrm q}(p)=(2p-1)_+\log b,
 \qquad
 c_{\mathrm q}(p)=(1-2p)_+\log b.}$$ The random cocycle synchronizes uniformly, $$\label{eq:synchronization}
 \sup_{x,y\in X}d_b(\Phi_nx,\Phi_ny)\longrightarrow0,$$ if and only if $p<1/2$.

The strong law gives $S_n/n\to\delta:=2p-1$ almost surely. We first show $$\label{eq:max-rate}
 \frac{M_n}{n}\longrightarrow\delta_+.$$ If $\delta<0$, then $S_n\to-\infty$, so the all-time maximum is finite and $M_n/n\to0$. If $\delta=0$, the strong law implies that, for every $\varepsilon>0$, all sufficiently large $k$ satisfy $|S_k|\leq\varepsilon k$. After dividing by $n$, the maximum over the finitely many earlier $k$ vanishes, and the later maximum is at most $\varepsilon$. If $\delta>0$, the same uniform tail estimate gives $M_n\leq(\delta+\varepsilon)n+o(n)$, while $M_n\geq S_n$ gives the matching lower bound. This proves [\[eq:max-rate\]](#eq:max-rate){reference-type="eqref" reference="eq:max-rate"}.

Now use $J_n=M_n$, $I_n=M_n-S_n$, and [\[eq:image-fibre\]](#eq:image-fibre){reference-type="eqref" reference="eq:image-fibre"} to obtain [\[eq:quenched-formulas\]](#eq:quenched-formulas){reference-type="eqref" reference="eq:quenched-formulas"}. If $p<1/2$, then $I_n/n\to1-2p>0$, so the diameter in [\[eq:image-fibre\]](#eq:image-fibre){reference-type="eqref" reference="eq:image-fibre"} tends to zero and [\[eq:synchronization\]](#eq:synchronization){reference-type="eqref" reference="eq:synchronization"} holds. If $p>1/2$, then $S_n\to+\infty$ and there are infinitely many strict record times; at each record time $S_n=M_n$, hence $I_n=0$ and the image diameter is one. At $p=1/2$, the simple symmetric walk hits every positive integer almost surely, so the same record-time argument applies. Uniform synchronization therefore fails for every $p\geq1/2$.

At the drift boundary the quenched exponential rates vanish, but the normal-form exponents still have a precise diffusive scale.

[\[prop:critical-scale\]]{#prop:critical-scale label="prop:critical-scale"} If $p=1/2$ and $Z$ is standard normal, then $$\label{eq:critical-law}
 \frac{J_n}{\sqrt n}\xrightarrow{\mathrm d}|Z|,
 \qquad
 \frac{I_n}{\sqrt n}\xrightarrow{\mathrm d}|Z|,$$ and $$\label{eq:critical-means}
 \mathbb EJ_n\sim\mathbb EI_n\sim\sqrt{\frac{2n}{\pi}}.$$

Donsker's invariance principle and the continuous-mapping theorem [@Billingsley1999] give $M_n/\sqrt n\Rightarrow\sup_{0\leq t\leq1}B_t$. The reflection principle identifies the last variable with $|Z|$. Time reversal and sign reversal of the symmetric increments show, for each fixed $n$, that $$I_n=M_n-S_n
 =\max_{0\leq k\leq n}(S_k-S_n)
 \quad\text{has the same law as }M_n.$$ This proves [\[eq:critical-law\]](#eq:critical-law){reference-type="eqref" reference="eq:critical-law"}. Doob's $L^2$ maximal inequality gives $\mathbb E[M_n^2]\leq\mathbb E[\max_{k\leq n}|S_k|^2]\leq4n$. Thus $M_n/\sqrt n$ is uniformly integrable. Taking expectations in the weak limit yields $\mathbb EM_n/\sqrt n\to\mathbb E|Z|=\sqrt{2/\pi}$, and the equality in law transfers the result to $I_n$.

# Annealed fibre degree and the rare-event threshold {#sec:annealed}

Put $$\label{eq:annealed-def}
 A_n(p)=\mathbb E\bigl[b^{J_n}\bigr],
 \qquad
 \lambda=bp+\frac qb.$$ The number $\lambda$ is the moment-generating factor $\mathbb E[b^{\xi_1}]$. Reflection changes finite-time constants and even creates a bounded phase, so $A_n$ is not simply $\lambda^n$.

For $k\geq1$, let $T_k=\inf\{n\geq0:S_n=k\}$. Since $$b^m=1+(b-1)\sum_{k=1}^m b^{k-1}\qquad(m\in\mathbb N_0),$$ we have $$\label{eq:first-passage-decomposition}
 A_n(p)=1+(b-1)\sum_{k=1}^n b^{k-1}\mathbb P(T_k\leq n).$$ For $0<p<1$, the ballot theorem gives, for $m\geq k$ with $m\equiv k\pmod2$, $$\label{eq:ballot}
 \mathbb P(T_k=m)=\frac{k}{m}
 \binom{m}{(m+k)/2}
 p^{(m+k)/2}q^{(m-k)/2}.$$ Equations [\[eq:first-passage-decomposition\]](#eq:first-passage-decomposition){reference-type="eqref" reference="eq:first-passage-decomposition"}--[\[eq:ballot\]](#eq:ballot){reference-type="eqref" reference="eq:ballot"} are an exact finite-$n$ formula for $A_n$.

[\[thm:annealed\]]{#thm:annealed label="thm:annealed"} Assume $0<p<1$, and let $A_n$ and $\lambda$ be as in [\[eq:annealed-def\]](#eq:annealed-def){reference-type="eqref" reference="eq:annealed-def"}.

1.  If $p<1/(b+1)$, put $r=p/q$. Then $$\label{eq:subcritical}
     A_n\longrightarrow\frac{1-r}{1-br}.$$

2.  If $p=1/(b+1)$, then $$\label{eq:critical-linear}
     A_n=\frac{(b-1)^2}{b(b+1)}n+O(1).$$ More exactly, if $\widehat M_n$ is the maximum of a walk whose $+1$ probability is $b/(b+1)$, then $$\label{eq:critical-exact}
     A_n=1+\frac{b-1}{b}\,\widehat\mathbb E\widehat M_n.$$

3.  If $p>1/(b+1)$, put $$\label{eq:rho}
     \rho=\frac{q}{pb^2}<\frac1b.$$ Then $$\label{eq:supercritical}
     \frac{A_n}{\lambda^n}\longrightarrow
     \frac{1-\rho}{1-b\rho}.$$

At the endpoints, $A_n(0)=1$ and $A_n(1)=b^n$. Consequently the annealed fibre-degree exponent is $$\label{eq:annealed-exponent}
 \boxed{
 g_{\mathrm a}(p):=\lim_{n\to\infty}\frac1n\log A_n(p)
 =\log\max\left\{1,bp+\frac{1-p}{b}\right\}.}$$

The equivalence $$\label{eq:threshold-equivalence}
 \lambda-1=(b-1)\left(p-\frac qb\right)$$ places the threshold at $p=q/b=1/(b+1)$.

Suppose first that $p<1/(b+1)$. Then $p<q$, and the negatively drifting walk has a finite all-time maximum $M_\infty$. The classical gambler's-ruin calculation gives $$\mathbb P(M_\infty\geq k)=\mathbb P(T_k<\infty)=\left(\frac pq\right)^k=r^k.$$ Thus $M_\infty$ is geometric on $\mathbb N_0$ with mass $(1-r)r^m$. Since $br<1$, monotone convergence yields $$A_n\uparrow\mathbb Eb^{M_\infty}
 =(1-r)\sum_{m\geq0}(br)^m=\frac{1-r}{1-br}.$$

Now let $p=1/(b+1)$. Tilt each first-hit path by $b^{S_m}$. Because $\lambda=1$, the tilted walk has $+1$ probability $bp=q=b/(b+1)$ and $-1$ probability $q/b=p=1/(b+1)$. Every path stopped upon first hitting $k$ acquires the same likelihood factor $b^k$, hence $$\label{eq:critical-hit-tilt}
 \mathbb P(T_k\leq n)=b^{-k}\widehat\mathbb P(T_k\leq n).$$ Substitution into [\[eq:first-passage-decomposition\]](#eq:first-passage-decomposition){reference-type="eqref" reference="eq:first-passage-decomposition"} gives $$A_n=1+\frac{b-1}{b}\sum_{k\geq1}
 \widehat\mathbb P(\widehat M_n\geq k)
 =1+\frac{b-1}{b}\widehat\mathbb E\widehat M_n,$$ which is [\[eq:critical-exact\]](#eq:critical-exact){reference-type="eqref" reference="eq:critical-exact"}. Under the tilted law the drift is $\widehat\delta=(b-1)/(b+1)$. Set $\widehat Y_n=\widehat M_n-\widehat S_n$. This reflected birth--death chain moves toward zero with probability $b/(b+1)$ and away from zero with probability $1/(b+1)$; at zero those moves lead respectively to zero and one. Its stationary law is $$\widehat\pi(y)=(1-b^{-1})b^{-y}\qquad(y\in\mathbb N_0).$$ The monotone common-increment coupling of the chain started at zero with a stationary copy gives $$0\leq\widehat\mathbb E\widehat Y_n
 \leq\sum_{y\geq0}y\widehat\pi(y)=\frac1{b-1}.$$ Since $\widehat M_n=\widehat S_n+\widehat Y_n$ and $\widehat\mathbb E\widehat S_n=\widehat\delta n$, it follows that $$\widehat\mathbb E\widehat M_n
 =\widehat\delta n+O(1),$$ and [\[eq:critical-linear\]](#eq:critical-linear){reference-type="eqref" reference="eq:critical-linear"} follows.

Finally suppose $p>1/(b+1)$. On paths through time $n$, define the tilted law $\mathbb P_*$ by $$\label{eq:exponential-tilt}
 \frac{d\mathbb P_*}{d\mathbb P}\bigg|_{\sigma(\xi_1,\ldots,\xi_n)}
 =\frac{b^{S_n}}{\lambda^n}.$$ Indeed, $$\frac{b^{S_n}}{\lambda^n}
 =\prod_{t=1}^n\frac{b^{\xi_t}}{\lambda}$$ is a mean-one product martingale. Hence the finite-dimensional tilted laws are consistent and define iid increments on the infinite path space. Under $\mathbb P_*$, the $+1$ and $-1$ probabilities are $$\label{eq:tilted-probabilities}
 \alpha=\frac{bp}{\lambda},
 \qquad
 \beta=\frac{q}{b\lambda},
 \qquad \alpha>\beta.$$ Writing $Y_n=M_n-S_n$, the change of measure gives the exact identity $$\label{eq:tilted-moment}
 A_n=\lambda^n\mathbb E_*[b^{Y_n}].$$ The process $Y_n$ moves from $y\geq1$ to $y-1$ with probability $\alpha$ and to $y+1$ with probability $\beta$; at zero, $P_*(0,0)=\alpha$ and $P_*(0,1)=\beta$. It is an irreducible aperiodic reflected birth--death chain with stationary law $$\label{eq:stationary-drawdown}
 \pi(y)=(1-\rho)\rho^y,
 \qquad
 \rho=\frac\beta\alpha=\frac{q}{pb^2}.$$ Starting from zero, the monotone common-increment coupling bounds $Y_n$ by a stationary copy. Because $b\rho<1$, this domination makes $(b^{Y_n})_n$ uniformly integrable. Ergodic convergence of the chain and [\[eq:stationary-drawdown\]](#eq:stationary-drawdown){reference-type="eqref" reference="eq:stationary-drawdown"} now give $$\mathbb E_*b^{Y_n}\longrightarrow
 \sum_{y\geq0}(1-\rho)(b\rho)^y
 =\frac{1-\rho}{1-b\rho}.$$ Together with [\[eq:tilted-moment\]](#eq:tilted-moment){reference-type="eqref" reference="eq:tilted-moment"}, this proves [\[eq:supercritical\]](#eq:supercritical){reference-type="eqref" reference="eq:supercritical"}. The endpoint identities follow directly from $M_n=0$ at $p=0$ and $M_n=n$ at $p=1$. The three cases then imply [\[eq:annealed-exponent\]](#eq:annealed-exponent){reference-type="eqref" reference="eq:annealed-exponent"}.

The trichotomy exposes a rare-event regime that an almost-sure drift calculation cannot see.

[\[cor:two-thresholds\]]{#cor:two-thresholds label="cor:two-thresholds"} For $1/(b+1)<p<1$, $$\label{eq:strict-gap}
 g_{\mathrm a}(p)>g_{\mathrm q}(p).$$ For $0\leq p\leq1/(b+1)$ and for $p=1$, equality holds. In particular, when $$\label{eq:intermediate-window}
 \frac1{b+1}<p<\frac12,$$ the fibre degree $b^{J_n}$ is eventually constant almost surely, but its expectation grows exponentially.

If $1/(b+1)<p\leq1/2$, then $g_{\mathrm a}>0=g_{\mathrm q}$. If $1/2<p<1$, strict Jensen applied to the nonconstant variable $b^{\xi_1}$ gives $$g_{\mathrm a}=\log\mathbb Eb^{\xi_1}
 >\mathbb E\log b^{\xi_1}=(2p-1)\log b=g_{\mathrm q}.$$ The equality cases follow from [\[eq:quenched-formulas\]](#eq:quenched-formulas){reference-type="eqref" reference="eq:quenched-formulas"} and [\[eq:annealed-exponent\]](#eq:annealed-exponent){reference-type="eqref" reference="eq:annealed-exponent"}. In the window [\[eq:intermediate-window\]](#eq:intermediate-window){reference-type="eqref" reference="eq:intermediate-window"}, the walk has negative drift, so $J_n=M_n$ increases to the finite all-time maximum almost surely, while $\lambda>1$ gives exponential annealed growth.

At the second threshold, [\[prop:critical-scale,thm:annealed\]](#prop:critical-scale,thm:annealed){reference-type="ref" reference="prop:critical-scale,thm:annealed"} combine to give a particularly sharp separation.

[\[cor:symmetric-annealed\]]{#cor:symmetric-annealed label="cor:symmetric-annealed"} At $p=1/2$, $$\label{eq:symmetric-degree-law}
 \frac{\log\operatorname{deg}(\Phi_n)}{\sqrt n}
 \xrightarrow{\mathrm d}(\log b)|Z|,
 \qquad
 \frac{-\log\operatorname{diam}\Phi_n(X)}{\sqrt n}
 \xrightarrow{\mathrm d}(\log b)|Z|,$$ whereas $$\label{eq:symmetric-annealed-asymptotic}
 \mathbb E\operatorname{deg}(\Phi_n)
 \sim\frac{b+1}{b}
 \left(\frac{b+b^{-1}}2\right)^n.$$

Equation [\[eq:symmetric-degree-law\]](#eq:symmetric-degree-law){reference-type="eqref" reference="eq:symmetric-degree-law"} is [\[prop:critical-scale\]](#prop:critical-scale){reference-type="ref" reference="prop:critical-scale"} combined with [\[eq:image-fibre\]](#eq:image-fibre){reference-type="eqref" reference="eq:image-fibre"}. In [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"}, $p=q=1/2$ gives $\rho=b^{-2}$, so the prefactor in [\[eq:supercritical\]](#eq:supercritical){reference-type="eqref" reference="eq:supercritical"} is $(1-b^{-2})/(1-b^{-1})=(b+1)/b$. The base is $\lambda=(b+b^{-1})/2$, proving [\[eq:symmetric-annealed-asymptotic\]](#eq:symmetric-annealed-asymptotic){reference-type="eqref" reference="eq:symmetric-annealed-asymptotic"}.

# Exact controls and ownership boundary {#sec:controls}

The accompanying standard-library program separates exact regression checks from floating diagnostics. Its integer and rational layer performs 265,861 assertions:

-   all $65{,}535$ direction words through time $15$ satisfy $J=M$ and $I=M-S$, with three identities checked per word;

-   all $29{,}524$ labelled words over $\{D,C_0,C_1\}$ through time $9$ agree with definition-level composition on symbolic tails;

-   exhaustive finite-input maps verify the exact image cylinders and constant fibre degrees through $(b,n)=(2,10)$ and $(3,7)$;

-   the ballot sum [\[eq:first-passage-decomposition\]](#eq:first-passage-decomposition){reference-type="eqref" reference="eq:first-passage-decomposition"}--[\[eq:ballot\]](#eq:ballot){reference-type="eqref" reference="eq:ballot"} agrees with direct rational walk propagation for $b=2,3,5$, five interior rational probabilities through $n=18$, and separately at $p=0,1$ through $n=20$;

-   the critical identity [\[eq:critical-exact\]](#eq:critical-exact){reference-type="eqref" reference="eq:critical-exact"}, the supercritical tilt [\[eq:tilted-moment\]](#eq:tilted-moment){reference-type="eqref" reference="eq:tilted-moment"}, the stationary prefactor, and the symmetric equality in law of $I_n$ and $J_n$ are checked independently.

Five rescaled floating values illustrate convergence but do not certify an identity, almost-sure limit, or weak limit.

The scope boundary is equally explicit. Arnold provides the cited broad random cocycle framework [@Arnold1998]. Mairesse provides the cited general normal-form, drift, entropy, and harmonic-measure results for the relevant monoid-walk setting [@Mairesse2005]. Feller and Asmussen represent the classical ballot, first-passage, exponential-tilting, and reflected-walk tools [@Feller1968; @Asmussen2003]. The note does not claim any of those ingredients. Its residual theorem package is the exact coupling $$\text{prefix--shift cocycle}
 \longleftrightarrow
 (\text{image cylinder},\text{fibre degree})
 \longleftrightarrow
 (M_n-S_n,M_n),$$ together with the alphabet-dependent annealed trichotomy and its comparison with pathwise synchronization.

This system is not a random subshift of finite type: there is no random adjacency constraint, forbidden language, or path-count matrix. It is also not a rank-one reset or a renewal-reward model. A shift can cancel any currently unmatched prefix, and the surviving normal form depends on the running maximum of the entire direction walk rather than on iid reset gaps. Nor is it a hidden-output process: the assertions concern images and fibres of actual random maps on the full shift. These distinctions are an internal collision firewall, not a novelty claim. Public posting, submission, and priority language remain unauthorized pending a specialist literature review.
