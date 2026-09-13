---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction/main.pdf"
source_sha256: "143e682c7a5e098642d0f8dd76a3be58ec2bfce7c584e3631f7ff5f312a1aa33"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Boundary-Orbit Far Atom and a Signed Diffuse-Compensation Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-338-boundary-orbit-far-atom-and-signed-diffuse-compensation-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The corrected RH-334 observation map defines an actual physical signed far slot at the first alias. We isolate within that slot a real deterministic boundary-orbit atom. For the primitive period-$2k$ boundary cycle, all but one of its folded marked points lie in the frozen far set for every fixed window parameter and all sufficiently small noise. The resulting set has $2k-1$ points. Its noisy localized trace is exactly zero because a finite set has zero multiplication operator on $L^2$, whereas its corrected deterministic mass is $$D_k^{\rm orb}=r_H^{-2k}\frac{2k-1}{1+|M_k|}.$$ Thus its signed far subledger is $-D_k^{\rm orb}$. The physical multiplier law gives $D_k^{\rm orb}/\mathcal A_{k,2k}\to1$ and $D_k^{\rm orb}/H_k\to+\infty$. This is an alias-sized physical obstruction to proving the far estimate by taking separate absolute values after the orbit/rest split. It is not an aggregate far nonvanishing theorem. If the full far slot is $o(H_k)$, the complementary diffuse ledger must compensate the orbit atom as $D_k^{\rm orb}+o(H_k)$, requiring relative precision $o((\beta R)^{-2k})$. No moving-order estimate for that diffuse term is available, so aggregate far closure and aggregate nonvanishing both remain not testable. No determinant or Riemann-hypothesis conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Boundary-Orbit Far Atom and a Signed\
  Diffuse-Compensation Obstruction
```

## Markdown 正文

# Frozen far observation and boundary orbit

Let $u_c\in(1,2)$ solve $$\label{eq:u-cubic}
 u_c^3-2u_c^2+2u_c-2=0$$ and put $$\label{eq:physical-constants}
 f(x)=1-u_cx^2,
 \qquad r=u_c-1,
 \qquad \lambda=2u_cr>1,
 \qquad b=u_c^{-1/2}.$$ Then $f(r)=r$, $f(1)=-r$, and the two-step component map is $S=f^2$. The inverse branch used by the primitive boundary word is $$\label{eq:h}
 h(x)=\sqrt{\frac{1-\sqrt{(1-x)/u_c}}{u_c}},
 \qquad h(1)=b,$$ with $h$ increasing and $h(x)<x$ on $(r,1)$ [@WangBoundaryMonodromy2026].

Fix $A>0$. RH-334 freezes the boundary-owned windows before evaluating any trace: $$\begin{aligned}
 J^-_{\sigma,k,A}&=[0,1]\cap[b-A\sqrt\sigma,b),\label{eq:Jminus}\\
 J^+_{\sigma,k,A}&=[0,1]\cap[b,b+A\sqrt\sigma],\label{eq:Jplus}\\
 F_{\sigma,k,A}&=[0,1]\setminus(J^-_{\sigma,k,A}\cup J^+_{\sigma,k,A}).
 \label{eq:F}\end{aligned}$$ For measurable $J\subset[0,1]$ and $n\ge2$, let $$\begin{aligned}
 L_{\sigma,n}(J)&=\operatorname{Tr}(M_JK_\sigma^n),\label{eq:L}\\
 P_n^{\rm abs}(J)&=
 \sum_{\substack{f^n(x)=x\\ |x|\in J}}
 \frac1{|1-(f^n)'(x)|}.
 \label{eq:Pabs}\end{aligned}$$ Here $K_\sigma$ is the RH-334 folded backward-observable noisy operator; the multiplication operator marks the cyclic basepoint rather than a forward probability event. The corrected actual far slot is $$\label{eq:R-full}
 \mathcal R_k:=r_H^{-2k}
 \{L_{\sigma,2k}(F_{\sigma,k,A})
       -P_{2k}^{\rm abs}(F_{\sigma,k,A})\},
 \qquad r_H=\frac{17}{20}.$$ Absolute-value folding is a multiplier-preserving bijection between the signed and folded fixed points, including marked-point multiplicity and minimal period [@WangObservation2026].

Let $p_k=p_{2k}$ be the primitive boundary point coded by $CA(CB)^{k-1}$. RH-17 proves that its $S$-orbit is the exact ordered chain $$\label{eq:S-chain}
 p_k, h^{k-1}(p_k), h^{k-2}(p_k),\ldots,h(p_k),$$ and that $$\label{eq:multiplier-law}
 M_k:=(f^{2k})'(p_k)=(S^k)'(p_k)
 =-C_M\lambda^k\{1+o(1)\},
 \qquad C_M>0.$$ The word is primitive, so all $2k$ signed and folded marked points are distinct [@WangLongCycle2026; @WangBoundaryMonodromy2026].

We work on the exact physical natural clock $$\label{eq:natural-clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad \sigma\to0,$$ though the containment argument below needs only $k\to\infty$ and $\sigma\to0$.

# The physical far-orbit atom

For the signed orbit $x_j=f^j(p_k)$, define the folded marked set with one point deleted: $$\label{eq:Omega}
 \Omega_k=
 \{|x_j|:0\le j<2k,\ j\ne2k-2\}.$$ The deleted point is the final even component point $|x_{2k-2}|=h(p_k)$. Its distance from $b$ is itself on the critical $\lambda^{-k}$ scale, so no fixed-$A$ membership is asserted for it.

[\[thm:containment\]]{#thm:containment label="thm:containment"} For every fixed $A>0$, along [\[eq:natural-clock\]](#eq:natural-clock){reference-type="eqref" reference="eq:natural-clock"} and all sufficiently large $k$, $$\label{eq:Omega-in-F}
 \Omega_k\subset F_{\sigma,k,A},
 \qquad |\Omega_k|=2k-1.$$

RH-17 proves that $p_k$ increases with $k$ and $$\label{eq:right-gap}
 p_k\ge p_1>b.$$ Thus the endpoint $p_k$ lies to the right of the shrinking windows by the fixed gap $p_1-b>0$.

The even marked points are the $S$-chain [\[eq:S-chain\]](#eq:S-chain){reference-type="eqref" reference="eq:S-chain"}. Except for $h(p_k)$, every internal even point has the form $h^m(p_k)$ with $m\ge2$. Monotonicity and $p_k<1$ give $$\label{eq:even-left-gap}
 h^m(p_k)\le h^2(1)=h(b)<b.$$ Hence these points lie to the left by the fixed gap $b-h(b)>0$.

Every point in the positive $S$-chain lies in $[r,1]$. Since $f$ decreases from $f(r)=r$ to $f(1)=-r$ on this interval, every odd folded point satisfies $$\label{eq:odd-left-gap}
 |f(S^j(p_k))|\le r<b,$$ with fixed gap $b-r>0$. Choose $k$ large enough that $$A\sqrt\sigma<min\{p_1-b,\ b-h(b),\ b-r\}.$$ Equations [\[eq:right-gap\]](#eq:right-gap){reference-type="eqref" reference="eq:right-gap"}--[\[eq:odd-left-gap\]](#eq:odd-left-gap){reference-type="eqref" reference="eq:odd-left-gap"} then place every marked point except $h(p_k)$ in $F_{\sigma,k,A}$. Primitivity and the folding bijection give distinctness, so deleting one of $2k$ points leaves cardinality $2k-1$.

[\[thm:far-atom\]]{#thm:far-atom label="thm:far-atom"} For all $k$ in the range of [\[thm:containment\]](#thm:containment){reference-type="ref" reference="thm:containment"}, define $$\label{eq:D-orb}
 D_k^{\rm orb}
 =r_H^{-2k}\frac{2k-1}{1+|M_k|}>0.$$ Then $$\label{eq:R-orb}
 \boxed{
 \mathcal R_k^{\rm orb}:=r_H^{-2k}
 \{L_{\sigma,2k}(\Omega_k)-P_{2k}^{\rm abs}(\Omega_k)\}
 =-D_k^{\rm orb}.}$$ Moreover the full actual far slot has the exact decomposition $$\label{eq:atom-rest}
 \mathcal R_k=\mathcal R_k^{\rm orb}+\mathcal R_k^{\rm rest},$$ where $\mathcal R_k^{\rm rest}$ is the same localized ledger on $F_{\sigma,k,A}\setminus\Omega_k$.

A finite set has indicator zero almost everywhere, so $M_{\Omega_k}=0$ as an operator on $L^2[0,1]$. Therefore $L_{\sigma,2k}(\Omega_k)=0$ exactly. The derivative of $f^{2k}$ is the same cyclic product at every marked point of one orbit. By [\[eq:multiplier-law\]](#eq:multiplier-law){reference-type="eqref" reference="eq:multiplier-law"} it is negative for large $k$, and the RH-334 folding theorem preserves it. Each of the $2k-1$ folded marked points therefore has deterministic weight $$\frac1{|1-M_k|}=\frac1{1+|M_k|}.$$ This proves [\[eq:R-orb\]](#eq:R-orb){reference-type="eqref" reference="eq:R-orb"}. Additivity of the localized noisy trace and of the deterministic fixed-point sum across the disjoint partition $F=\Omega_k\sqcup(F\setminus\Omega_k)$ proves [\[eq:atom-rest\]](#eq:atom-rest){reference-type="eqref" reference="eq:atom-rest"}.

$\Omega_k$ is an analytic subpartition of the already-frozen far set; it is not promoted to a new canonical physical window or a fitted observation coefficient. Its dependence on the known deterministic orbit is used only to expose one exact signed constituent of $\mathcal R_k$. The aggregate far slot and all claims about it retain the original RH-334 windows.

# Alias scale and signed compensation

Retain $$\label{eq:beta-H}
 \beta=\frac1{r_H\sqrt\lambda},
 \qquad H_k=kR^{-2k},
 \qquad R=\frac75.$$ The physical first-alias packet of RH-326 [@WangFirstAlias2026] is $$\label{eq:alias}
 \mathcal A_{k,2k}=(2k-2)\beta_k^{2k}+2\beta^{2k},
 \qquad
 \beta_k^{2k}=\frac{r_H^{-2k}}{|M_k|}.$$

[\[thm:scales\]]{#thm:scales label="thm:scales"} As $k\to\infty$, $$\begin{aligned}
 D_k^{\rm orb}
 &=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},
 \label{eq:D-asymptotic}\\
 \frac{D_k^{\rm orb}}{\mathcal A_{k,2k}}
 &\longrightarrow1,
 \label{eq:D-over-A}\\
 \frac{D_k^{\rm orb}}{H_k}
 &=\frac{2}{C_M}(\beta R)^{2k}\{1+o(1)\}
 \longrightarrow+\infty.
 \label{eq:D-over-H}\end{aligned}$$

Insert [\[eq:multiplier-law\]](#eq:multiplier-law){reference-type="eqref" reference="eq:multiplier-law"} into [\[eq:D-orb\]](#eq:D-orb){reference-type="eqref" reference="eq:D-orb"} and use $\beta^{2k}=r_H^{-2k}\lambda^{-k}$ to obtain [\[eq:D-asymptotic\]](#eq:D-asymptotic){reference-type="eqref" reference="eq:D-asymptotic"}. The same multiplier law in [\[eq:alias\]](#eq:alias){reference-type="eqref" reference="eq:alias"} gives $$\mathcal A_{k,2k}=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},$$ which proves [\[eq:D-over-A\]](#eq:D-over-A){reference-type="eqref" reference="eq:D-over-A"}. Division by $H_k$ gives the first identity in [\[eq:D-over-H\]](#eq:D-over-H){reference-type="eqref" reference="eq:D-over-H"}. RH-336 certifies $\beta R>1$ exactly, without relying on a rounded decimal [@WangProjectorMass2026]; hence the limit is infinite.

[\[cor:compensation\]]{#cor:compensation label="cor:compensation"} The aggregate far estimate $\mathcal R_k=o(H_k)$ holds if and only if $$\label{eq:compensation}
 \mathcal R_k^{\rm rest}=D_k^{\rm orb}+o(H_k).$$ Relative to the orbit mass, the required precision is $$\label{eq:relative-precision}
 o\!\left(\frac{H_k}{D_k^{\rm orb}}\right)
 =o\!\left((\beta R)^{-2k}\right).$$ In particular, taking separate absolute values after the atom/rest split cannot prove $\mathcal R_k=o(H_k)$, because $$\label{eq:absolute-obstruction}
 \frac{|\mathcal R_k^{\rm orb}|+|\mathcal R_k^{\rm rest}|}{H_k}
 \ge\frac{D_k^{\rm orb}}{H_k}\longrightarrow+\infty.$$

Substitute $\mathcal R_k^{\rm orb}=-D_k^{\rm orb}$ into [\[eq:atom-rest\]](#eq:atom-rest){reference-type="eqref" reference="eq:atom-rest"}. This proves the equivalence. The reciprocal of [\[eq:D-over-H\]](#eq:D-over-H){reference-type="eqref" reference="eq:D-over-H"} gives [\[eq:relative-precision\]](#eq:relative-precision){reference-type="eqref" reference="eq:relative-precision"}, up to a harmless positive constant. Inequality [\[eq:absolute-obstruction\]](#eq:absolute-obstruction){reference-type="eqref" reference="eq:absolute-obstruction"} is immediate.

This corollary does not say that signed compensation is absent. It says precisely what an aggregate positive theorem must prove. RH-19's local tail analysis explicitly leaves genuine bulk excursions to a missing resolvent or moving-order theorem [@WangBoundaryTail2026]; the repository contains no estimate of $\mathcal R_k^{\rm rest}$ at the scale in [\[eq:relative-precision\]](#eq:relative-precision){reference-type="eqref" reference="eq:relative-precision"}. Accordingly both $\mathcal R_k=o(H_k)$ and aggregate nonvanishing remain `NOT_TESTABLE`. After the clock obstruction of RH-337 there is also no valid hatted actual/model pair typing a physical $\Delta\mathcal R_k$ [@WangClockDrift2026]. The result here concerns the actual physical far slot itself, not RH-330 transfer [@WangTransfer2026].

# Reproduction and claim boundary

The artifact solves the physical algebraic constants and boundary inverse word at high Decimal precision. For $k=2,4,8,16,32$ and the diagnostic choice $A=1/4$, it checks the counts $3,7,15,31,63$, orbit closure, multiplier sign, approach of $D_k^{\rm orb}/\mathcal A_{k,2k}$ to one, and growth of $D_k^{\rm orb}/H_k$. These rows reproduce the analytic formulas; they are not interval certificates and do not prove the moving theorem.

The maximum rigorous conclusion is the exact physical orbit subledger, its alias-scale asymptotic, and the necessary signed compensation law. The paper does not bound the diffuse rest, prove aggregate far vanishing or nonvanishing, close the parity--alias or off-alias packets, transport the noisy head, glue a determinant, or prove full-trace divergence. No Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace, completed-zeta divisor equality, or Riemann-hypothesis proof is obtained. Gates A--E remain false/open.
