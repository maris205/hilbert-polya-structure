---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-350-growing-depth-lower-sideband-phase-incompatibility"
canonical_tex: "zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility/main.pdf"
source_sha256: "978fcde7a1532c84a8aa11c3c6d290fe34679fa9d0823459f57d97ea84671e8c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Growing-Depth Lower-Sideband Phase Incompatibility

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-350-growing-depth-lower-sideband-phase-incompatibility/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We extend the two-coordinate phase obstruction of RH-349 to a triangular lower-even ladder. Let $J_k\to\infty$, $J_k=o(k)$, and $m_{k,j}=k-j$ for $2\le j\le J_k$. The exact direct coefficient is $$p_{k,j}=Y_{k,j}+\mathcal P_{k,j}-S_{k,j}.$$ Writing $H_m=mR^{-2m}$, $x=(\beta R)^2>1$, and $a_k=C_*C_M\lambda^{\eta_k-2}$, we prove the uniform deterministic laws $$\sup_{2\le j\le J_k}
   \left|\frac{C_MS_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}-1\right|\to0,$$ $$\sup_{2\le j\le J_k}
   \left|\frac{C_M\mathcal P_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}
         -a_k\lambda^{2-j}\right|\to0.$$ For a fixed depth $J\ge3$, the relative phase mismatch has exact minimax value $$\inf_{a>0}\max_{2\le j\le J}|a\lambda^{2-j}-1|
   =\frac{\lambda^{J-2}-1}{\lambda^{J-2}+1}.$$ For the physical prefix weighting, put $F_N(a)=\sum_{r=0}^{N}x^{-r}|a\lambda^{-r}-1|$. Since $x\lambda=(28/17)^2>2$, its unique minimizer is $a=1$ and $$\inf_{a>0}F_N(a)
   =\frac{1-x^{-N}}{x-1}
    -\frac{1-(x\lambda)^{-N}}{x\lambda-1}.$$ Under the explicit, presently unproved actual aggregate hypothesis $$x^{-(k-2)}\sum_{j=2}^{J_k}
   \frac{|Y_{k,j}|}{2H_{m_{k,j}}}\to0,$$ the selected direct subprefix therefore has a strictly positive normalized liminf and diverges exponentially. This is a conditional growing-depth theorem, not unconditional physical nonclosure. Odd orders, upper-alias orders, the full off-alias aggregate, determinant gluing, and Gates A--E remain open. No Riemann-hypothesis conclusion is made.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'Growing-Depth Lower-Sideband Phase Incompatibility'
```

## Markdown 正文

# The triangular lower-even ledger

Use the physical clock and bounded phase $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad
 \eta_k=k-\frac{\log(1/\sigma)}{2\log\lambda}.$$ Let $J_k$ be integer-valued with $$\label{eq:depth}
 J_k\longrightarrow\infty,\qquad J_k=o(k),\qquad J_k\ge3,$$ and set, for $2\le j\le J_k$, $$\label{eq:indices}
 m_{k,j}=k-j,\qquad n_{k,j}=2m_{k,j},\qquad
 H_m=mR^{-2m},\qquad x=(\beta R)^2.$$ Because $k-J_k\to\infty$, every selected $m_{k,j}$ eventually belongs to the RH-348 ladder $I_k$ [@WangLowerLadder2026].

Abbreviate $$p_{k,j}=p_{\sigma,k,2m_{k,j}},\qquad
 \mathcal P_{k,j}=\mathcal P_{\sigma,2m_{k,j}}.$$ The simultaneous complete-orbit extraction gives, exactly, $$\label{eq:coefficient}
 \boxed{
 p_{k,j}=Y_{k,j}+\mathcal P_{k,j}-S_{k,j},}$$ where $$\label{eq:YS}
 Y_{k,j}=\mathcal T_{k,m_{k,j}}^{\rm rest}
          -d_{\sigma,k,2m_{k,j}},\qquad
 S_{k,j}=F_{m_{k,j}}^{\rm orb}+\mathcal A_{k,2m_{k,j}}.$$ Here $$\begin{aligned}
 F_m^{\rm orb}&=2mG_m,
 &G_m&=\frac{r_H^{-2m}}{1+|M_m|},\label{eq:orbit}\\
 \mathcal A_{k,2m}&=2(\beta^{2m}-\beta_k^{2m}),
 &\beta_k&=\frac{|M_k|^{-1/(2k)}}{r_H},
 \qquad \beta=\frac1{r_H\sqrt\lambda}.\label{eq:radial}\end{aligned}$$ The coefficient $p$ is direct. The actual signed term $Y_{k,j}$ retains both the orbit-free trace remainder and the noisy-head/counterloop defect; no full-trace/direct substitution is made [@WangObservation2026; @WangTwoSidebands2026].

# Uniform deterministic and parity laws

[\[thm:uniformity\]]{#thm:uniformity label="thm:uniformity"} Under [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}--[\[eq:depth\]](#eq:depth){reference-type="eqref" reference="eq:depth"}, put $$\label{eq:a-k}
 a_k=C_*C_M\lambda^{\eta_k-2}.$$ Then $$\label{eq:demand-uniform}
 \boxed{
 \sup_{2\le j\le J_k}
 \left|
 \frac{C_MS_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}-1
 \right|\longrightarrow0,}$$ and $$\label{eq:parity-uniform}
 \boxed{
 \sup_{2\le j\le J_k}
 \left|
 \frac{C_M\mathcal P_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}
 -a_k\lambda^{2-j}
 \right|\longrightarrow0.}$$ These are uniform deterministic/scalar packet laws. They contain no estimate for the actual signed $Y_{k,j}$.

Write $$|M_m|=C_M\lambda^m\{1+\varepsilon_m\},\qquad
 \varepsilon_m\to0.$$ Since $m_{k,j}\ge k-J_k\to\infty$, $\sup_{2\le j\le J_k}|\varepsilon_{m_{k,j}}|\to0$. Thus, uniformly on the selected window, $$\label{eq:orbit-uniform}
 F_{m_{k,j}}^{\rm orb}
 =\frac{2m_{k,j}}{C_M}\beta^{2m_{k,j}}\{1+o(1)\}.$$ The finite-radius law $$\beta_k=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right]$$ and the RH-348 exponential bound give, uniformly for $m\le k$, $$|\mathcal A_{k,2m}|\le C\frac{m}{k}\beta^{2m}.$$ After division by [\[eq:orbit-uniform\]](#eq:orbit-uniform){reference-type="eqref" reference="eq:orbit-uniform"}, the radial term is $O(k^{-1})$ uniformly. Hence $S_{k,j}$ has the same uniform leading law as the orbit term. Since $2H_mx^m=2m\beta^{2m}$, this proves [\[eq:demand-uniform\]](#eq:demand-uniform){reference-type="eqref" reference="eq:demand-uniform"} [@WangBoundaryMonodromy2026; @WangLowerLadder2026].

For every even order, the exact parity formula is $$\mathcal P_{\sigma,2m}
 =r_H^{-2m}\{1-(1-\delta_\sigma)^{2m}\},\qquad
 \delta_\sigma=C_*\sqrt\sigma\{1+o(1)\}.$$ The all-order Taylor remainder in RH-326 yields $$\mathcal P_{\sigma,2m}
 =2mC_*\sqrt\sigma\,r_H^{-2m}\{1+o(1)\}$$ uniformly for $m\le k$, because $k\delta_\sigma\to0$. Therefore $$\frac{C_M\mathcal P_{k,j}}{2H_{m_{k,j}}x^{m_{k,j}}}
 =C_*C_M\sqrt\sigma\,\lambda^{m_{k,j}}+o(1)
 =a_k\lambda^{2-j}+o(1)$$ uniformly in $j$. Boundedness of [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} makes $a_k$ bounded and justifies the final uniform absolute error [@WangParityBoundary2026; @WangFirstAlias2026].

The growing-depth conclusion is not inferred from finitely many fixed-$j$ limits. It follows from a tail-uniform multiplier asymptotic, an all-order parity remainder, and the explicit radial bound on one common window.

# Finite-depth relative minimax

[\[prop:relative\]]{#prop:relative label="prop:relative"} For every integer $J\ge3$ and $\lambda>1$, $$\label{eq:relative}
 \boxed{
 \inf_{a>0}\max_{2\le j\le J}
 |a\lambda^{2-j}-1|
 =\frac{\lambda^{J-2}-1}{\lambda^{J-2}+1}.}$$ The unique minimizer is $$\label{eq:relative-optimizer}
 a_J^{\rm rel}=\frac{2\lambda^{J-2}}{\lambda^{J-2}+1}.$$ In particular, the optimal largest relative mismatch tends to one as $J\to\infty$.

The values $a\lambda^{2-j}$ decrease with $j$. Convexity of $t\mapsto|t-1|$ implies that the largest mismatch occurs at one of the two endpoints $j=2$ and $j=J$. Hence the problem is $$\inf_{a>0}\max\{|a-1|,|a\lambda^{2-J}-1|\}.$$ At the minimizer the two endpoint errors are equal with opposite signs: $$a-1=1-a\lambda^{2-J}.$$ Solving gives [\[eq:relative-optimizer\]](#eq:relative-optimizer){reference-type="eqref" reference="eq:relative-optimizer"} and substitution gives [\[eq:relative\]](#eq:relative){reference-type="eqref" reference="eq:relative"}. The endpoint regimes are monotone, so the minimizer is unique.

# Exact physical weighted minimax

For $N\ge1$, define $$\label{eq:F-N}
 F_N(a)=\sum_{r=0}^{N}x^{-r}|a\lambda^{-r}-1|,
 \qquad a>0.$$ The physical constants satisfy the exact identity $$\label{eq:xlambda}
 x\lambda=\left(\frac{R}{r_H}\right)^2
 =\left(\frac{28}{17}\right)^2>2.$$ This rational dominance is the exact form of the superunit certificate used in the physical Hardy normalization [@WangProjectorMass2026].

[\[thm:weighted\]]{#thm:weighted label="thm:weighted"} For every $N\ge1$, the unique minimizer of $F_N$ is $a=1$, and $$\label{eq:A-N}
 \boxed{
 \inf_{a>0}F_N(a)=A_N
 :=\frac{1-x^{-N}}{x-1}
   -\frac{1-(x\lambda)^{-N}}{x\lambda-1}.}$$ Moreover, $$\label{eq:A-infinity}
 A_N\nearrow A_\infty
 :=\frac1{x-1}-\frac1{x\lambda-1}>0.$$

Rewrite each summand as $$x^{-r}|a\lambda^{-r}-1|
 =(x\lambda)^{-r}|a-\lambda^r|.$$ Thus $F_N$ is a weighted absolute-deviation functional with knots $1,\lambda,\ldots,\lambda^N$ and weights $1,(x\lambda)^{-1},\ldots,(x\lambda)^{-N}$. By [\[eq:xlambda\]](#eq:xlambda){reference-type="eqref" reference="eq:xlambda"}, $$\sum_{r=1}^{N}(x\lambda)^{-r}
 <\sum_{r=1}^{\infty}(x\lambda)^{-r}<1.$$ The first knot therefore carries more weight than all later knots combined, so the unique weighted median is $a=1$. Evaluation gives $$F_N(1)=\sum_{r=1}^{N}x^{-r}(1-\lambda^{-r}),$$ and the two geometric sums yield [\[eq:A-N\]](#eq:A-N){reference-type="eqref" reference="eq:A-N"}. Every added summand is positive, and passage to the two infinite geometric series proves [\[eq:A-infinity\]](#eq:A-infinity){reference-type="eqref" reference="eq:A-infinity"}.

With the alternative bottom-sideband normalization, [\[thm:weighted\]](#thm:weighted){reference-type="ref" reference="thm:weighted"} is equivalently $$\inf_{a>0}\sum_{j=2}^{J}x^{J-j}|a\lambda^{2-j}-1|
 =\frac{x^{J-2}-1}{x-1}
  -\frac{x^{J-2}-\lambda^{2-J}}{x\lambda-1}.$$ At $J=3$ this reduces to the RH-349 constant $1-\lambda^{-1}$ [@WangTwoSidebands2026].

# Conditional growing-depth direct-prefix obstruction

Put $$\label{eq:W}
 W_{k,j}=\frac{|p_{k,j}|}{2H_{m_{k,j}}}
 =\frac{|p_{k,j}|R^{2m_{k,j}}}{2m_{k,j}}.$$ The actual aggregate remainder scale on the selected triangular window is $$\label{eq:Y-aggregate}
 \mathcal Y_k
 :=\frac1{x^{k-2}}
 \sum_{j=2}^{J_k}\frac{|Y_{k,j}|}{2H_{m_{k,j}}}.$$

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Suppose the actual physical coefficients satisfy the explicit hypothesis $$\label{eq:Y-hypothesis}
 \boxed{\mathcal Y_k\longrightarrow0.}$$ Then, with $N_k=J_k-2$, $$\label{eq:conditional-asymptotic}
 \boxed{
 \frac1{x^{k-2}}\sum_{j=2}^{J_k}W_{k,j}
 =\frac{F_{N_k}(a_k)}{C_M}+o(1).}$$ Consequently, $$\label{eq:liminf}
 \boxed{
 \liminf_{k\to\infty}
 \frac1{x^{k-2}}\sum_{j=2}^{J_k}W_{k,j}
 \ge\frac1{C_M}
 \left(\frac1{x-1}-\frac1{x\lambda-1}\right)>0.}$$ The selected lower-even direct subprefix therefore diverges exponentially.

For each $j$, the elementary inequality $$\bigl||\mathcal P_{k,j}-S_{k,j}+Y_{k,j}|
       -|\mathcal P_{k,j}-S_{k,j}|\bigr|
 \le |Y_{k,j}|$$ shows that hypothesis [\[eq:Y-hypothesis\]](#eq:Y-hypothesis){reference-type="eqref" reference="eq:Y-hypothesis"} permits deletion of the actual $Y$ aggregate at the normalization in [\[eq:conditional-asymptotic\]](#eq:conditional-asymptotic){reference-type="eqref" reference="eq:conditional-asymptotic"}. By [\[thm:uniformity\]](#thm:uniformity){reference-type="ref" reference="thm:uniformity"}, uniformly in $j$, $$\frac{|\mathcal P_{k,j}-S_{k,j}|}{2H_{m_{k,j}}x^{m_{k,j}}}
 =\frac{|a_k\lambda^{2-j}-1|}{C_M}+o(1).$$ Since $x^{m_{k,j}}/x^{k-2}=x^{2-j}$ and $\sum_{j=2}^{\infty}x^{2-j}<\infty$, summing the uniform error gives $o(1)$. Reindexing by $r=j-2$ proves [\[eq:conditional-asymptotic\]](#eq:conditional-asymptotic){reference-type="eqref" reference="eq:conditional-asymptotic"}. Apply [\[thm:weighted\]](#thm:weighted){reference-type="ref" reference="thm:weighted"} with $N=N_k\to\infty$ to obtain [\[eq:liminf\]](#eq:liminf){reference-type="eqref" reference="eq:liminf"}.

If $$\label{eq:Y-uniform}
 \max_{2\le j\le J_k}
 \frac{|Y_{k,j}|}{H_{m_{k,j}}}\longrightarrow0,$$ then [\[eq:Y-hypothesis\]](#eq:Y-hypothesis){reference-type="eqref" reference="eq:Y-hypothesis"} holds and hence so do [\[eq:conditional-asymptotic\]](#eq:conditional-asymptotic){reference-type="eqref" reference="eq:conditional-asymptotic"}--[\[eq:liminf\]](#eq:liminf){reference-type="eqref" reference="eq:liminf"}.

The left side of [\[eq:Y-aggregate\]](#eq:Y-aggregate){reference-type="eqref" reference="eq:Y-aggregate"} is at most $$\frac{J_k}{2x^{k-2}}
 \max_{2\le j\le J_k}\frac{|Y_{k,j}|}{H_{m_{k,j}}},$$ which tends to zero because $J_k=o(k)$ while $x>1$.

Neither [\[eq:Y-hypothesis\]](#eq:Y-hypothesis){reference-type="eqref" reference="eq:Y-hypothesis"} nor [\[eq:Y-uniform\]](#eq:Y-uniform){reference-type="eqref" reference="eq:Y-uniform"} is proved in the repository. They concern the actual signed orbit-free trace remainder and noisy-head/counterloop defect. The theorem is therefore conditional and does not establish unconditional full-prefix or $E_{\rm off}$ nonclosure.

# Executable protocol and route boundary

The artifact evaluates the exact finite multiplier, orbit, radial, and leading-law parity formulas for several pairs $(k,J)$ with $J=\lfloor\sqrt{k}\rfloor$. It uses the scalar fixture $a_k=1$ and $Y_{k,j}=0$ solely to reproduce the deterministic formulas. It also checks the exact relative minimax, the weighted-median identity, monotone convergence of $A_N$, and the identity $x\lambda=(28/17)^2$. The rows are not interval certificates, asymptotic evidence, or observations of the actual $Y$ aggregate.

RH-350 proves a genuinely growing-depth deterministic uniformity theorem, an exact family of finite-depth minimax laws, and a conditional selected direct-subprefix obstruction. It does not estimate the actual signed remainder, control odd or upper-alias orders, decide the full $E_{\rm off}$ aggregate, or activate RH-288. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
