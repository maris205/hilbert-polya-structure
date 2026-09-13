---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-328-joint-alias-parity-shell-matching-equation"
canonical_tex: "zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation/main.pdf"
source_sha256: "44c242c08e18eb3c0dc3d72e9a41aa5ef3343d03987f81993d6036cd7c9e426b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Joint Alias--Parity--Shell Matching: Fixed-Reference Certificates and Exponential Contrast Precision

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-328-joint-alias-parity-shell-matching-equation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The first-alias ledger now has actual localized boundary, neighboring-shell, and far-remainder slots, but the shell is not identified with the earlier forward Gaussian laws. We formulate the exact fixed-reference matching equation without making that identification. If a typed shell representation has scale $L$, physical contrast $c_{\rm phys}$, fixed deterministic contrast $c_0$, and observation error $\mathcal E_{\rm obs}$, then the full signed packet is exactly $$e=L(c_{\rm phys}^{2k}-y)+\mathcal E_{\rm obs}+\mathcal R,
   \qquad
   y=c_0^{2k}+\frac{\mathcal A-\mathcal P-\mathcal B}{L}.$$ In alias-normalized variables this gives $y=z_0+(1-q-b)/\ell$. On a fixed phase, the parity ratio and endpoint clearance remain synchronized. If $L$ is comparable to the alias scale, $y$ stays away from zero, and the observation error plus far remainder is $o(kR^{-2k})$, target closure forces contrast-radius precision $o((\beta R)^{-2k}/k)$. We also prove a sharp interval certificate retaining every trace-observation Duhamel weight, and an explicit scoped counterexample: the best-case reachability distance may vanish while the physical mismatch is order $L$ and diverges relative to $kR^{-2k}$. The shell representation, contrast, observation bound, and far remainder remain unproved for the actual operator; no full-trace replacement or Riemann-hypothesis conclusion follows.
author:
- Bin Wang
date: July 2026
title: |
  Joint Alias--Parity--Shell Matching:\
  Fixed-Reference Certificates and Exponential Contrast Precision
```

## Markdown 正文

# The actual packet and retained interface

Let $u_c\in(1,2)$ solve $u^3-2u^2+2u-2=0$, put $$f(x)=1-u_cx^2,
 \qquad
 \lambda=2u_c(u_c-1),
 \qquad
 r_H=0.85,
 \qquad
 R=1.4,
 \label{eq:route-constants}$$ and let $K_\sigma$ be the row-normalized folded noisy Markov operator on $[0,1]$. For a measurable $J\subset[0,1]$, let $M_J$ be multiplication by its indicator and define the localized noisy and deterministic cyclic observations $$\begin{aligned}
 L_{\sigma,n}(J)&=\operatorname{Tr}(M_JK_\sigma^n),
 \label{eq:localized-noisy}\\
 P_n(J)&=\sum_{\substack{f^n(x)=x\\x\in J}}
 \frac{1}{|1-(f^n)'(x)|}.
 \label{eq:localized-flat}\end{aligned}$$

We retain the RH-327 physical basepoint partition. If $p_{2k}$ is the distinguished boundary periodic point, write $$\begin{aligned}
 \Delta_k^{\rm clr}
 &=1-p_{2k}=C_{\rm b}\lambda^{-2k}\{1+o(1)\},
 & C_{\rm b}&>0,
 \label{eq:clearance}\\
 h(x)&=\sqrt{\frac{1-\sqrt{(1-x)/u_c}}{u_c}},
 &s_{\sigma,k}&=h(p_{2k}),
 \label{eq:source}\end{aligned}$$ and set $$b_*=u_c^{-1/2},
 \qquad
 q_{{\rm b},\sigma,k}=\frac{b_*-s_{\sigma,k}}{\sqrt\sigma},
 \qquad
 q_{\sigma,k}(x)=\frac{x-s_{\sigma,k}}{\sqrt\sigma}.
 \label{eq:partition-coordinate}$$ For a fixed radius $A>0$, the two half-open windows are $$\begin{aligned}
 J^-_{\sigma,k,A}
 &=\{x\in[0,1]:q_{{\rm b},\sigma,k}-A
       \le q_{\sigma,k}(x)<q_{{\rm b},\sigma,k}\},
 \label{eq:left-window}\\
 J^+_{\sigma,k,A}
 &=\{x\in[0,1]:q_{{\rm b},\sigma,k}
       \le q_{\sigma,k}(x)\le q_{{\rm b},\sigma,k}+A\},
 \label{eq:right-window}\end{aligned}$$ and $F_{\sigma,k,A}$ is their complement. The actual Hardy-scaled slots at order $2k$ are $$\begin{aligned}
 \mathcal B_{\sigma,k}
 &=r_H^{-2k}\{L_{\sigma,2k}(J^-_{\sigma,k,A})
                  -P_{2k}(J^-_{\sigma,k,A})\},
 \label{eq:boundary-slot}\\
 \mathcal S_{\sigma,k}
 &=r_H^{-2k}\{L_{\sigma,2k}(J^+_{\sigma,k,A})
                  -P_{2k}(J^+_{\sigma,k,A})\},
 \label{eq:shell-slot}\\
 \mathcal R_{\sigma,k}
 &=r_H^{-2k}\{L_{\sigma,2k}(F_{\sigma,k,A})
                  -P_{2k}(F_{\sigma,k,A})\}.
 \label{eq:far-slot}\end{aligned}$$ With $$\mathcal T_{\sigma,2k}
 :=r_H^{-2k}\{\operatorname{Tr}K_\sigma^{2k}-P_{2k}([0,1])\},
 \label{eq:raw-packet}$$ they satisfy the exact actual partition $\mathcal T_{\sigma,2k}=\mathcal B_{\sigma,k}+\mathcal S_{\sigma,k}+\mathcal R_{\sigma,k}$.

The parity and first-counterloop packets are typed by $$\begin{aligned}
 \lambda_-(\sigma)&=-(1-\delta_\sigma),
 &\delta_\sigma&=C_*\sqrt\sigma+o(\sqrt\sigma),
 \label{eq:parity-type}\\
 \beta&=(r_H\sqrt\lambda)^{-1},
 &\beta_k&=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right],
 \label{eq:alias-type}\end{aligned}$$ where $C_*,C_M>0$, and $$\begin{aligned}
 \mathcal P_{\sigma,2k}
 &=r_H^{-2k}\{1-\lambda_-(\sigma)^{2k}\}>0,
 \label{eq:parity-packet}\\
 \mathcal A_{k,2k}
 &=(2k-2)\beta_k^{2k}+2\beta^{2k}>0.
 \label{eq:alias-packet}\end{aligned}$$ The exact signed coefficient ledger inherited from RH-326 and RH-327 is $$\boxed{
 e_{\sigma,k}
 =\mathcal B_{\sigma,k}+\mathcal S_{\sigma,k}+\mathcal R_{\sigma,k}
  +\mathcal P_{\sigma,2k}-\mathcal A_{k,2k}.}
 \label{eq:exact-ledger}$$ The target is $$H_k=kR^{-2k}.
 \label{eq:target}$$

All moving-order limits use $$k=k_\sigma
 =\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad
 \eta_\sigma=k_\sigma-
 \frac{\log(1/\sigma)}{2\log\lambda},
 \qquad
 \eta_\sigma\longrightarrow\eta
 \label{eq:clock}$$ along a fixed-phase subsequence. Thus $$d_{\sigma,k}:=\frac{\Delta_k^{\rm clr}}{\sigma}
 \longrightarrow C_{\rm b}\lambda^{-2\eta}.
 \label{eq:clearance-phase}$$ For $d\ge0$, let $$\phi(t)=(2\pi)^{-1/2}e^{-t^2/2},
 \qquad
 \Phi(d)=\int_{-\infty}^d\phi(t)\,dt,
 \qquad
 g_d(v)=\frac{\phi(v-d)}{\Phi(d)}\mathbf1_{v\ge0}.
 \label{eq:entrance-density}$$ With standard normals $Z_1,Z_2$ independent of $V$ and of each other, the retained local frame is $$V\sim g_d,
 \qquad U=-2u_cV-Z_1,
 \qquad W=-\lambda U+Z_2,
 \qquad (V,U,W)\text{ has orientation }(+,-,+),
 \label{eq:frame}$$ with output shift $\kappa_{\rm aff}d=2u_c\lambda d$. These coordinates remain interface data; they do not identify the cyclic observation in [\[eq:shell-slot\]](#eq:shell-slot){reference-type="eqref" reference="eq:shell-slot"}.

# The exact fixed-reference matching equation

Fix $L=L_{\sigma,k}>0$ and a deterministic reference contrast $c_0=c_{0,k}\in[-1,1]$. For a proposed physical contrast $c_{\rm phys}=c_{\sigma,k}^{\rm phys}\in[-1,1]$, put $$X_{k,L}(c_{\rm phys};c_0)
 =L\{c_{\rm phys}^{2k}-c_0^{2k}\}.
 \label{eq:exchange-shell}$$ The actual shell slot has a representation error $$\mathcal E_{\sigma,k}^{\rm obs}
 :=\mathcal S_{\sigma,k}-X_{k,L}(c_{\rm phys};c_0).
 \label{eq:observation-error}$$ This is a definition once $L,c_0,c_{\rm phys}$ are supplied. No smallness or physical identification is assumed.

Define the signed demand and required even power by $$\begin{aligned}
 D_{\sigma,k}
 &=\mathcal A_{k,2k}-\mathcal P_{\sigma,2k}-\mathcal B_{\sigma,k},
 \label{eq:demand}\\
 y_{\sigma,k}
 &=c_0^{2k}+\frac{D_{\sigma,k}}{L}.
 \label{eq:required-power}\end{aligned}$$

[\[thm:joint-equation\]]{#thm:joint-equation label="thm:joint-equation"} For every typed choice above, $$\boxed{
 e_{\sigma,k}
 =L\{c_{\rm phys}^{2k}-y_{\sigma,k}\}
  +\mathcal E_{\sigma,k}^{\rm obs}+\mathcal R_{\sigma,k}.}
 \label{eq:joint-equation}$$ Moreover, the image of [\[eq:exchange-shell\]](#eq:exchange-shell){reference-type="eqref" reference="eq:exchange-shell"} over $|c_{\rm phys}|\le1$ is $$I_{k,L,c_0}
 =[-L|c_0|^{2k},\,L(1-|c_0|^{2k})],
 \label{eq:interval}$$ and the RH-327 best-case screen has the exact normalized form $$\operatorname{dist}(D_{\sigma,k},I_{k,L,c_0})
 =L\,\operatorname{dist}(y_{\sigma,k},[0,1]).
 \label{eq:distance-identity}$$

Substitute $\mathcal S=X_{k,L}+\mathcal E^{\rm obs}$ into [\[eq:exact-ledger\]](#eq:exact-ledger){reference-type="eqref" reference="eq:exact-ledger"} and use $D=\mathcal A-\mathcal P-\mathcal B$: $$e=X_{k,L}-D+\mathcal E^{\rm obs}+\mathcal R
  =L(c_{\rm phys}^{2k}-y)+\mathcal E^{\rm obs}+\mathcal R.$$ Since $c_{\rm phys}^{2k}$ ranges exactly over $[0,1]$, translation by $-Lc_0^{2k}$ proves [\[eq:interval\]](#eq:interval){reference-type="eqref" reference="eq:interval"}. The affine change $D=L(y-c_0^{2k})$ then gives [\[eq:distance-identity\]](#eq:distance-identity){reference-type="eqref" reference="eq:distance-identity"}.

[\[cor:closure\]]{#cor:closure label="cor:closure"} For an identified physical representation, target closure is equivalent to the signed condition $$L(c_{\rm phys}^{2k}-y_{\sigma,k})
 +\mathcal E_{\sigma,k}^{\rm obs}+\mathcal R_{\sigma,k}=o(H_k).
 \label{eq:signed-closure}$$ If additionally $\mathcal E_{\sigma,k}^{\rm obs}+\mathcal R_{\sigma,k}=o(H_k)$, then it is equivalent to $$c_{\rm phys}^{2k}-y_{\sigma,k}=o(H_k/L).
 \label{eq:power-precision}$$

This corollary is conditional on the physical fields. The repository does not identify $L,c_0,c_{\rm phys}$, prove [\[eq:observation-error\]](#eq:observation-error){reference-type="eqref" reference="eq:observation-error"} small, or control $\mathcal R$.

# Phase law and contrast conditioning

Normalize by the positive alias packet: $$q_{\sigma,k}=\frac{\mathcal P_{\sigma,2k}}{\mathcal A_{k,2k}},
 \qquad
 b_{\sigma,k}=\frac{\mathcal B_{\sigma,k}}{\mathcal A_{k,2k}},
 \qquad
 \ell_{\sigma,k}=\frac{L}{\mathcal A_{k,2k}},
 \qquad
 z_{0,k}=c_0^{2k}.
 \label{eq:normalized-data}$$

[\[prop:phase-power\]]{#prop:phase-power label="prop:phase-power"} The required power is exactly $$\boxed{
 y_{\sigma,k}
 =z_{0,k}+\frac{1-q_{\sigma,k}-b_{\sigma,k}}
                    {\ell_{\sigma,k}}.}
 \label{eq:normalized-power}$$ On a fixed phase, RH-326 gives $$q_{\sigma,k}=C_*C_M\lambda^\eta+o(1).
 \label{eq:phase-ratio}$$ If also $b_{\sigma,k}\to b_\eta$, $\ell_{\sigma,k}\to\ell_\eta\in(0,\infty)$, and $z_{0,k}\to z_{0,\eta}$, then $$y_{\sigma,k}\longrightarrow
 y_\eta:=z_{0,\eta}
 +\frac{1-C_*C_M\lambda^\eta-b_\eta}{\ell_\eta}.
 \label{eq:phase-limit}$$ When $y_\eta\in(0,1)$, the unique required contrast magnitude satisfies $$r_k:=y_{\sigma,k}^{1/(2k)}
 =1+\frac{\log y_\eta}{2k}+o(k^{-1}).
 \label{eq:unit-edge-law}$$

Divide [\[eq:required-power\]](#eq:required-power){reference-type="eqref" reference="eq:required-power"} by the definitions in [\[eq:normalized-data\]](#eq:normalized-data){reference-type="eqref" reference="eq:normalized-data"} to obtain [\[eq:normalized-power\]](#eq:normalized-power){reference-type="eqref" reference="eq:normalized-power"}. The fixed phase law yields [\[eq:phase-limit\]](#eq:phase-limit){reference-type="eqref" reference="eq:phase-limit"}. Finally, $r_k=\exp\{(\log y_{\sigma,k})/(2k)\}$ and $\log y_{\sigma,k}\to\log y_\eta$.

The limits of $b_{\sigma,k}$ and $\ell_{\sigma,k}$ are assumptions, not archived physical theorems. The same phase simultaneously fixes the clearance in [\[eq:clearance-phase\]](#eq:clearance-phase){reference-type="eqref" reference="eq:clearance-phase"}; it cannot be optimized independently after inspecting [\[eq:normalized-power\]](#eq:normalized-power){reference-type="eqref" reference="eq:normalized-power"}.

[\[thm:radius-precision\]]{#thm:radius-precision label="thm:radius-precision"} Let $y_k\in[a,1]$ for some fixed $a>0$, let $\rho_k=|c_{\rm phys}|\in[0,1]$, put $r_k=y_k^{1/(2k)}$, and suppose $\varepsilon_k:=H_k/L\to0$. Then $$\rho_k^{2k}-y_k=o(\varepsilon_k)
 \quad\Longleftrightarrow\quad
 \rho_k-r_k=o(\varepsilon_k/k).
 \label{eq:precision-equivalence}$$ If in addition $$\mathcal A_{k,2k}=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},
 \qquad
 \frac{L}{\mathcal A_{k,2k}}\longrightarrow\ell\in(0,\infty),
 \label{eq:same-order-scale}$$ then $$\begin{aligned}
 \frac{H_k}{L}
 &=\frac{C_M}{2\ell}(\beta R)^{-2k}\{1+o(1)\},
 \label{eq:power-scale}\\
 |\rho_k-r_k|
 &=o\left(\frac{(\beta R)^{-2k}}{k}\right)
 \label{eq:radius-scale}\end{aligned}$$ is the contrast-radius demand corresponding to [\[eq:power-precision\]](#eq:power-precision){reference-type="eqref" reference="eq:power-precision"}.

Assume first that the power mismatch is $o(\varepsilon_k)$. For large $k$ it is at most $a/2$, so both $y_k$ and $\rho_k^{2k}$ are at least $a/2$. The mean-value theorem gives $$2k\min(\rho_k,r_k)^{2k-1}|\rho_k-r_k|
 \le |\rho_k^{2k}-r_k^{2k}|
 \le 2k|\rho_k-r_k|.
 \label{eq:mvt-bounds}$$ Because $0\le\min(\rho_k,r_k)\le1$ and its $2k$th power is at least $a/2$, the left coefficient is at least $ka$. This proves the forward implication. The upper bound in [\[eq:mvt-bounds\]](#eq:mvt-bounds){reference-type="eqref" reference="eq:mvt-bounds"} proves the converse. Finally, divide $H_k=kR^{-2k}$ by [\[eq:same-order-scale\]](#eq:same-order-scale){reference-type="eqref" reference="eq:same-order-scale"} to obtain [\[eq:power-scale\]](#eq:power-scale){reference-type="eqref" reference="eq:power-scale"}; substitute into [\[eq:precision-equivalence\]](#eq:precision-equivalence){reference-type="eqref" reference="eq:precision-equivalence"}.

At even order the signs $c_{\rm phys}$ and $-c_{\rm phys}$ are identical in every formula above. Thus even perfect matching identifies at most a contrast magnitude.

# Sharp uncertainty certificate and a false-positive theorem

Retain the RH-325 trace-observation Duhamel ledger. Let $A_j,G_j:B_{j-1}\to B_j$, $B_m=B_0$, and suppose $|\mathfrak t(H)|\le T\lVert H\rVert$. Then $$|\mathfrak t(A_m\cdots A_1-G_m\cdots G_1)|
 \le \mathcal U_{\sigma,k}:=\sum_{j=1}^mW_j\delta_j,
 \label{eq:duhamel-bound}$$ where $$\delta_j=\lVert A_j-G_j\rVert,
 \qquad
 W_j=T\prod_{\ell=j+1}^m\lVert A_\ell\rVert
       \prod_{\ell=1}^{j-1}\lVert G_\ell\rVert.
 \label{eq:duhamel-weights}$$ No Markov $L^1$ contraction may replace the observation norm or these prefix/suffix factors. Applying [\[eq:duhamel-bound\]](#eq:duhamel-bound){reference-type="eqref" reference="eq:duhamel-bound"} to $\mathcal E^{\rm obs}$ additionally requires an identified operator-product realization of the shell observation; no such realization is proved here.

[\[thm:uncertainty\]]{#thm:uncertainty label="thm:uncertainty"} Put $$m_{\sigma,k}=L(c_{\rm phys}^{2k}-y_{\sigma,k}).
 \label{eq:model-mismatch}$$ If $|\mathcal E_{\sigma,k}^{\rm obs}|\le\mathcal U_{\sigma,k}$ and $|\mathcal R_{\sigma,k}|\le V_{\sigma,k}$, then the set of residuals compatible with only these symmetric bounds is exactly $$.
 \label{eq:uncertainty-interval}$$ Its best possible and worst possible absolute residuals are $$\begin{aligned}
 E_{\rm best}
 &=\max\{|m_{\sigma,k}|-\mathcal U_{\sigma,k}-V_{\sigma,k},0\},
 \label{eq:best-residual}\\
 E_{\rm worst}
 &=|m_{\sigma,k}|+\mathcal U_{\sigma,k}+V_{\sigma,k}.
 \label{eq:worst-residual}\end{aligned}$$ Consequently every error pair allowed by the bounds gives $o(H_k)$ if and only if $E_{\rm worst}=o(H_k)$.

Equation [\[eq:joint-equation\]](#eq:joint-equation){reference-type="eqref" reference="eq:joint-equation"} is $e=m+\mathcal E^{\rm obs}+\mathcal R$. The Minkowski sum of the two symmetric error intervals is $[-\mathcal U-V,\mathcal U+V]$, proving [\[eq:uncertainty-interval\]](#eq:uncertainty-interval){reference-type="eqref" reference="eq:uncertainty-interval"}. Distance from zero to this interval gives [\[eq:best-residual\]](#eq:best-residual){reference-type="eqref" reference="eq:best-residual"}; its farthest endpoint gives [\[eq:worst-residual\]](#eq:worst-residual){reference-type="eqref" reference="eq:worst-residual"}.

The best case is an existential statement over an uncertainty class. It does not show that the actual observation error and remainder choose the cancelling values.

[\[prop:false-positive\]]{#prop:false-positive label="prop:false-positive"} Fix $0<\theta<1$, take $c_0=0$, and set $D_{\sigma,k}=\theta L$. Then $$\operatorname{dist}(D_{\sigma,k},I_{k,L,0})=0,
 \qquad
 y_{\sigma,k}=\theta.
 \label{eq:screen-passes}$$ Nevertheless the admissible designated contrast $c_{\rm phys}=0$ with $\mathcal E^{\rm obs}=\mathcal R=0$ gives $$e_{\sigma,k}=-\theta L.
 \label{eq:false-positive-residual}$$ Hence if $L/H_k\to\infty$, the best-case screen vanishes identically while $|e_{\sigma,k}|/H_k\to\infty$.

For $c_0=0$, [\[eq:interval\]](#eq:interval){reference-type="eqref" reference="eq:interval"} is $[0,L]$, which contains $\theta L$. Equation [\[eq:required-power\]](#eq:required-power){reference-type="eqref" reference="eq:required-power"} gives $y=\theta$. Substitution of $c_{\rm phys}=0$ into [\[eq:joint-equation\]](#eq:joint-equation){reference-type="eqref" reference="eq:joint-equation"} proves the residual formula.

This is a scalar information-class counterexample. It is not evidence that the actual noisy operator selects $c_{\rm phys}=0$ or that its full trace diverges.

# Reproducible formula diagnostics

The code evaluates only proved formulas. For a visible phase diagnostic, take $k=16$, $b_{\sigma,k}=0.2$, $\ell_{\sigma,k}=1$, and $c_0=0.8$. Using the archived ordinary floating-point constants gives

    $\eta$   $C_*C_M\lambda^\eta$   $C_{\rm b}\lambda^{-2\eta}$          $y$   $y^{1/(2k)}$
  -------- ---------------------- ----------------------------- ------------ --------------
      $-1$             $0.122050$                    $1.298369$   $0.678743$     $0.987963$
    $-0.5$             $0.158127$                    $0.773495$   $0.642665$     $0.986278$
       $0$             $0.204869$                    $0.460805$   $0.595923$     $0.983954$
     $0.5$             $0.265428$                    $0.274522$   $0.535364$     $0.980664$
       $1$             $0.343888$                    $0.163545$   $0.456904$     $0.975820$

The boundary and shell ratios in this table are synthetic. They are not fitted or measured physical trace ratios.

With the leading alias scale $L=(2k/C_M)\beta^{2k}$ at phase zero, the matching and false-positive scales are

     $k$                  $H_k/L$               $H_k/(kL)$   false-positive $|e|/H_k$ at $\theta=1/4$
  ------ ------------------------ ------------------------ ------------------------------------------
     $8$    $2.0911\times10^{-2}$    $2.6138\times10^{-3}$                       $1.1956\times10^{1}$
    $16$    $4.4931\times10^{-4}$    $2.8082\times10^{-5}$                       $5.5641\times10^{2}$
    $32$    $2.0744\times10^{-7}$    $6.4826\times10^{-9}$                       $1.2052\times10^{6}$
    $64$   $4.4219\times10^{-14}$   $6.9092\times10^{-16}$                      $5.6537\times10^{12}$

These are formula evaluations, not interval-certified constants or physical shell data. Finite rows are reproduction checks only and are not promoted to all-order noisy asymptotics.

# Claim boundary and RH-329 handoff

The paper proves the exact conditional matching equation, its normalized phase law, the contrast-conditioning theorem, the sharp uncertainty interval, and a scoped reachability false positive. It does not prove that the actual shell has the exchange representation, identify its scale or contrast, control the RH-325 observation norm and every Duhamel weight, bound the second physical critical leg, prove $\mathcal E^{\rm obs}=o(H_k)$ or $\mathcal R=o(H_k)$, or establish actual joint matching.

RH-329 should audit one fully fixed isolated model. It must freeze the reference before seeing the demand, measure rather than optimize the physical contrast, retain every observation weight, and report both [\[eq:best-residual\]](#eq:best-residual){reference-type="eqref" reference="eq:best-residual"} and [\[eq:worst-residual\]](#eq:worst-residual){reference-type="eqref" reference="eq:worst-residual"} in units of $H_k$. A failure should be published as a scoped isolated-model negative result. A finite pass would still not identify the actual noisy operator or prove the RH-330 full-trace transfer criterion.

Gates A--E remain false/open. This work constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or completed-zeta divisor equality, and does not imply the Riemann Hypothesis.
