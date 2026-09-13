---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-monod-chemostat-threshold-route-a"
canonical_tex: "henon_dynamics/henon_monod_chemostat_threshold_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_monod_chemostat_threshold_route_a/paper/main.pdf"
source_sha256: "af4acf2d537e491e1c39c28edb939ba7258edca9fc3a309ddc95627839b9e7ec"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Threshold and Transient Atlas for the Monod Chemostat

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_monod_chemostat_threshold_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_monod_chemostat_threshold_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_monod_chemostat_threshold_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_monod_chemostat_threshold_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the one-species constant-yield Monod chemostat we expose an exact total- nutrient coordinate and use it to classify washout, equality and survival for all positive parameters. We also derive a separated transient on the invariant nutrient leaf and prove that every recurrent state is an equilibrium. This is an idealized source ODE, not biological calibration or an arithmetic determinant.
author:
- 'Route-A source-local certificate HCS-C254'
date: 31 August 2026
title: An Exact Threshold and Transient Atlas for the Monod Chemostat
```

## Markdown 正文

trailerid \[\<C2542026083100000000000000000000\>\<C2542026083100000000000000000000\>\]

# Frozen model and exact reduction

Let $D,S_{\rm in},\mu_m,K,Y>0$ and $$\dot S=D(S_{\rm in}-S)-\frac{\mu(S)X}{Y},\qquad
 \dot X=(\mu(S)-D)X,\qquad \mu(S)=\frac{\mu_mS}{K+S}. \tag{1}$$ The nonnegative quadrant is invariant. With $x=X/Y$ and $Q=S+x$, $$\dot Q=D(S_{\rm in}-Q),\qquad
 Q(t)=S_{\rm in}+(Q_0-S_{\rm in})e^{-Dt}. \tag{2}$$ Thus every solution is global and bounded.

# Threshold theorem

Put $\Delta=\mu(S_{\rm in})-D$.

If $\Delta<0$, every state converges to $E_0=(S_{\rm in},0)$. The same holds at $\Delta=0$, with a nonhyperbolic biomass direction. If $\Delta>0$, then $$S_*=\frac{DK}{\mu_m-D}<S_{\rm in},\qquad
 X_*=Y(S_{\rm in}-S_*), \tag{3}$$ and every state with $X_0>0$ converges to $E_+=(S_*,X_*)$; the invariant face $X_0=0$ converges to $E_0$.

Equation (2) gives $Q\to S_{\rm in}$. Substitution $S=Q-x$ gives $\dot x=[\mu(Q-x)-D]x$. Strict monotonicity of $\mu$, together with scalar comparison at $S_{\rm in}\pm\varepsilon$, leaves zero as the limiting root when $\Delta\le0$ and the unique root $S_{\rm in}-S_*$ when $\Delta>0$. The face $x=0$ is invariant and must be separated.

For completeness, after any fixed $\varepsilon>0$ one has $S_{\rm in}-\varepsilon<Q(t)<S_{\rm in}+\varepsilon$. Monotonicity of $\mu$ brackets $x$ between the two scalar logistic-type equations obtained by replacing $Q(t)$ with these endpoints. Their nonnegative equilibria converge to the roots stated above as $\varepsilon\downarrow0$; this closes both $\liminf x$ and $\limsup x$ and does not assume local stability. At washout the eigenvalues are $-D,\Delta$. At survival, the $(Q,x)$ eigenvalues are $$-D,\qquad -(S_{\rm in}-S_*)\mu'(S_*). \tag{4}$$ The equality face is the transcritical exchange.

# Exact attracting-leaf transient

On $Q=S_{\rm in}$ let $A=\mu_m-D$ and $x_*=S_{\rm in}-S_*$. Then $$\dot x=\frac{A x(x_*-x)}{K+S_{\rm in}-x}. \tag{5}$$ For $x_*\ne0$, partial fractions give $$\frac{K+S_{\rm in}}{x_*}\log x-
 \frac{K+S_*}{x_*}\log|x_*-x|=At+C. \tag{6}$$ At equality $x_*=0$ this is replaced by $$\frac{K+S_{\rm in}}{x}+\log x=At+C,
 \qquad x(t)\sim \frac{1}{\mu'(S_{\rm in})t}. \tag{7}$$

# Recurrence obstruction

Every recurrent state of (1) is an equilibrium; in particular, the positive chemostat has no nonconstant periodic orbit.

If a trajectory were periodic, (2) would make its $Q$ coordinate periodic. The only periodic solution of the scalar relaxation equation is $Q=S_{\rm in}$. Equation (5) then governs the entire trajectory, and a one-dimensional autonomous flow has no nonconstant periodic solution.

# Boundaries and evidence

If $X_0=0$, biomass stays zero. At $D=0$, $Q$ is conserved; for positive biomass substrate tends to zero. With $\mu_m=0$ the system is linear, and $S_{\rm in}=0$ forces $Q\to0$. The faces $K=0$ and $Y=0$ change the model and are not reached by division.

  face             exact reduced law           status
  ---------------- --------------------------- ----------------------------
  $X_0=0$          $X(t)=0$                    invariant washout boundary
  $D=0$            $Q(t)=Q_0$                  closed batch limit
  $\mu_m=0$        linear exponential system   no-growth boundary
  $S_{\rm in}=0$   $Q(t)=Q_0e^{-Dt}$           origin attracting

The executable certificate contains eighteen exact rational rows and five boundary contracts. An independent checker closes 244 assertions; fresh SymPy closes 14 identities; replay is byte-exact and 28/28 hostile semantic mutations are rehashed before testing. These finite receipts test algebra and conventions, not the continuous-parameter convergence proof. Monod supplies the named response convention; the 1977 SIAM paper supplies continuous-culture context; and the Smith--Waltman monograph supplies an authoritative model reference. No literature-priority claim is made.

# Route-A boundary

The arithmetic origin is `none`. The strict tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the verdict is `ROUTE_A_REJECTED`, with `route_b_invocation_allowed: false`, under `NO_BAD_EULER_OR_ROOT_NUMBER`. No target divisor, functional equation, Euler factor, root number, automorphy or Hilbert--Pólya operator is claimed.

9 J. Monod, "The Growth of Bacterial Cultures," *Annu. Rev. Microbiol.* 3 (1949), 371--394. S. B. Hsu, S. Hubbell and P. Waltman, "A Mathematical Theory for Single-Nutrient Competition in Continuous Cultures of Micro-Organisms," *SIAM J. Appl. Math.* 32 (1977), 366--383. H. L. Smith and P. Waltman, *The Theory of the Chemostat*, Cambridge University Press, 1995.
