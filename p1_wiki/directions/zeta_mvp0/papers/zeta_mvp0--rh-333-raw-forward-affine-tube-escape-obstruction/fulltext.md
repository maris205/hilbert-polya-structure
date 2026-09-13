---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-333-raw-forward-affine-tube-escape-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction/main.pdf"
source_sha256: "e65f5ed8b22b449eac006e03d1846e29c41efff403cd4055c5b9c5a8c07ecdeb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Raw Forward Affine-Tube Escape Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-333-raw-forward-affine-tube-escape-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The RH-332 roadmap asks whether the raw mass-one forward affine tube can be transported through the full boundary cycle with retained-path error $O(k\sigma)$. We give a scoped negative answer before the final critical closing component row. Along the RH-17 component cycle, keep the signed forward slopes $a_{k,j}=S'(x_{k,j})$ and let $Q_{j+1}=a_{k,j}Q_j+\beta_{k,j}Z_j$ for $0\le j\le k-2$. The first innovation reaches the preclosing coordinate with standard deviation $$s_k=\beta_{k,0}\prod_{j=1}^{k-2}|a_{k,j}|
   =\frac{\beta_{k,0}|M_k|}{m_{k,0}m_{k,k-1}}
   =C_s\lambda^{2k}\{1+o(1)\},$$ where $C_s=C_M\sqrt{1+\lambda^2}/(8u_c^2\lambda\sqrt{C_{\rm b}})>0$. Every physical folded and normalized preclosing marginal is supported in an interval of length $1/\sigma$. A uniform Gaussian maximum-interval-mass lemma therefore gives the finite, unhalved bound $$\|\mu_{\rm phys}-\mu_{\rm aff}\|_1
   \ge4\overline\Phi\!\left(\frac1{2\sigma s_k}\right).$$ At fixed first-alias phase $\eta$ this has the strictly positive limit lower bound $4\overline\Phi(1/(2C_s\lambda^{2\eta}))$. Marginal contraction lifts the bound to every retained path and every extension retaining the preclosing coordinate. Thus, on fixed or compact first-alias phase families, $O(k\sigma)$ and $o(kR^{-2k})$ are false for this raw full-line affine reference. The result does not give a final endpoint marginal lower bound after the omitted closing row and does not test cyclic, conditioned, truncated, folded, adapted, or nonlinear closing references. It is a probability-path obstruction, not a cyclic-trace theorem.
author:
- Bin Wang
date: August 2026
title: 'Raw Forward Affine-Tube Escape Obstruction'
```

## Markdown 正文

# Boundary cycle and data type

Let $u_c\in(1,2)$ be the root of $$\label{eq:cubic}
 u^3-2u^2+2u-2=0,$$ and define $$\label{eq:map-constants}
 f(x)=1-u_cx^2,
 \qquad S=f^2,
 \qquad r=u_c-1,
 \qquad \lambda=2u_cr.$$ For this preclosing-prefix problem, fix $k\ge2$ and $\sigma>0$. The RH-17 same-cycle component order is $$\label{eq:cycle-order}
 x_{k,0}=p_k,
 \qquad x_{k,j}=h^{k-j}(p_k)\quad(1\le j\le k-1),
 \qquad S(x_{k,j})=x_{k,j+1\bmod k}.$$ Thus $k$ is the component period for $S=f^2$, while the physical one-step period for $f$ is $2k$. This clock distinction will be retained throughout.

Put $$\label{eq:slopes-noise}
 a_{k,j}:=S'(x_{k,j}),
 \qquad m_{k,j}:=|a_{k,j}|,
 \qquad
 \beta_{k,j}^2:=1+f'(f(x_{k,j}))^2,
 \qquad
 M_k:=\prod_{j=0}^{k-1}a_{k,j}.$$ The sign of $a_{k,j}$ is part of the forward mean. Indeed, $$\label{eq:signed-slope-formula}
 S'(x)=4u_c^2x f(x),$$ so $a_{k,0}<0$ for all large $k$, whereas the following slopes in the positive component chain are positive. Replacing $a_{k,j}$ by $m_{k,j}$ is legitimate for a centered even backward observable, but not for a signed forward conditional mean.

[\[def:raw-prefix\]]{#def:raw-prefix label="def:raw-prefix"} Fix $k\ge2$. The variable $Q_j$ is the $\sigma$-scaled tangent coordinate about $x_{k,j}$. To see the canonical component coarsening, take two independent one-step standard-normal innovations $\xi_1,\xi_2$. Linearizing two noisy applications of $f$ gives the signed mean slope $f'(f(x_{k,j}))f'(x_{k,j})=S'(x_{k,j})$ and combined innovation $f'(f(x_{k,j}))\xi_1+\xi_2$, whose variance is $1+f'(f(x_{k,j}))^2=\beta_{k,j}^2$. For $0\le j\le k-2$, let $$\label{eq:raw-kernel}
 \mathsf Q_{k,j}(q,dq')
 =\mathcal N(a_{k,j}q,\beta_{k,j}^2)(dq')$$ be a mass-one kernel on the full line. Equivalently, for independent standard normals $Z_0,\ldots,Z_{k-2}$ and an arbitrary entrance variable $Q_0$ independent of those innovations, $$\label{eq:forward-recurrence}
 Q_{j+1}=a_{k,j}Q_j+\beta_{k,j}Z_j,
 \qquad 0\le j\le k-2.$$ The law at $Q_{k-1}$ is the raw affine preclosing marginal. No cyclic conditioning or final closing row is included in this definition.

The physical comparison uses the same coordinate location but a different state space. A row-normalized folded physical chain always lies in $[0,1]$. Hence its coordinate about the preclosing cycle point, $$\label{eq:physical-coordinate}
 q=\frac{x-x_{k,k-1}}\sigma,$$ is supported in the exact interval $$\label{eq:physical-interval}
 I_{\sigma,k}
 =\left[-\frac{x_{k,k-1}}\sigma,
         \frac{1-x_{k,k-1}}\sigma\right],
 \qquad |I_{\sigma,k}|=\frac1\sigma.$$ The physical law below may have any entrance and any exact folded/normalized prefix consistent with that support. The affine entrance may also be arbitrary; only its independence from the innovations is used. Write $\mathsf P^{\rm phys}_{\sigma,k}$ for the retained physical prefix path law and $\mathsf Q^{\rm raw}_{\sigma,k}$ for the retained raw affine prefix path law.

All distances are unhalved. For probability measures $\mu,\nu$ on a common measurable space $(E,\mathcal E)$, define $$\label{eq:unhalved}
 \|\mu-\nu\|_1:=|\mu-\nu|(E)
 =2\sup_{A\in\mathcal E}|\mu(A)-\nu(A)|.$$ For densities this is the usual $L^1$ distance. The scalar marginals use $E=\mathbb R$; retained paths use their corresponding product space.

# Exact forward expansion and the escaping innovation

[\[prop:expansion\]]{#prop:expansion label="prop:expansion"} The raw forward prefix satisfies $$\begin{aligned}
 Q_{k-1}
 ={}&\left(\prod_{j=0}^{k-2}a_{k,j}\right)Q_0 \nonumber\\
 &+\sum_{\ell=0}^{k-2}
 \beta_{k,\ell}
 \left(\prod_{j=\ell+1}^{k-2}a_{k,j}\right)Z_{\ell},
 \label{eq:exact-expansion}\end{aligned}$$ where an empty product equals one. In particular, the first innovation has propagated standard deviation $$\label{eq:sk-product}
 \boxed{
 s_k=\beta_{k,0}\prod_{j=1}^{k-2}m_{k,j}
 =\frac{\beta_{k,0}|M_k|}{m_{k,0}m_{k,k-1}}.}$$

Iterate [\[eq:forward-recurrence\]](#eq:forward-recurrence){reference-type="eqref" reference="eq:forward-recurrence"}; each later row multiplies every already-present term by its signed slope and adds one new innovation. This gives [\[eq:exact-expansion\]](#eq:exact-expansion){reference-type="eqref" reference="eq:exact-expansion"}. Taking the absolute value of the $Z_0$ coefficient gives the first expression in [\[eq:sk-product\]](#eq:sk-product){reference-type="eqref" reference="eq:sk-product"}. Since $|M_k|=\prod_{j=0}^{k-1}m_{k,j}$, cancellation of the first and last factors gives the second expression exactly.

The expansion also fixes the direction of variance propagation.

[\[lem:forward-variance\]]{#lem:forward-variance label="lem:forward-variance"} If $Q_j$ has finite variance and is independent of $Z_j$, then $$\label{eq:forward-variance}
 \boxed{
 \operatorname{Var}(Q_{j+1})
 =a_{k,j}^2\operatorname{Var}(Q_j)+\beta_{k,j}^2.}$$ Consequently the variance obtained by iterating [\[eq:forward-variance\]](#eq:forward-variance){reference-type="eqref" reference="eq:forward-variance"} equals the sum of the squared coefficients in [\[eq:exact-expansion\]](#eq:exact-expansion){reference-type="eqref" reference="eq:exact-expansion"}, including the squared entrance coefficient.

Independence kills the covariance in [\[eq:forward-recurrence\]](#eq:forward-recurrence){reference-type="eqref" reference="eq:forward-recurrence"}; the innovation variance is one. Iteration gives the coefficient-square formula.

RH-18 applies a backward affine operator to peak-normalized even Gaussian observables. Its periodic packet parameters satisfy $$\label{eq:backward-width}
 m_{k,j}^2v_{k,j}=v_{k,j+1}+\beta_{k,j}^2$$ so that Gaussian integration preserves the packet shape up to a peak amplitude. Equation [\[eq:backward-width\]](#eq:backward-width){reference-type="eqref" reference="eq:backward-width"} is neither [\[eq:forward-variance\]](#eq:forward-variance){reference-type="eqref" reference="eq:forward-variance"} nor an upper bound for it. The sign disappears there only because the observable is centered and even. Here the kernel is a mass-one forward probability kernel, the mean slope is signed, and every new noise variance enters with the plus sign in [\[eq:forward-variance\]](#eq:forward-variance){reference-type="eqref" reference="eq:forward-variance"}.

The analytic inputs are now symbolic. The archived boundary-cycle theorems give $$\begin{aligned}
 |M_k|&=C_M\lambda^k\{1+o(1)\},
 &m_{k,0}&\longrightarrow2u_c\lambda,
 \label{eq:input-one}\\
 \beta_{k,0}&\longrightarrow\sqrt{1+\lambda^2},
 &m_{k,k-1}
 &=4u_c\sqrt{C_{\rm b}}\,\lambda^{-k}\{1+o(1)\},
 \label{eq:input-two}\end{aligned}$$ with analytic constants $C_{\rm b},C_M>0$. The last law is the tiny critical closing slope. It is excluded from the raw prefix rows, but it appears in the exact multiplier quotient [\[eq:sk-product\]](#eq:sk-product){reference-type="eqref" reference="eq:sk-product"}.

[\[thm:propagated-scale\]]{#thm:propagated-scale label="thm:propagated-scale"} The standard deviation in [\[eq:sk-product\]](#eq:sk-product){reference-type="eqref" reference="eq:sk-product"} obeys $$\label{eq:sk-asymptotic}
 \boxed{
 s_k=C_s\lambda^{2k}\{1+o(1)\},
 \qquad
 C_s=
 \frac{C_M\sqrt{1+\lambda^2}}
 {8u_c^2\lambda\sqrt{C_{\rm b}}}>0.}$$

Substitute [\[eq:input-one\]](#eq:input-one){reference-type="eqref" reference="eq:input-one"}--[\[eq:input-two\]](#eq:input-two){reference-type="eqref" reference="eq:input-two"} into the quotient in [\[eq:sk-product\]](#eq:sk-product){reference-type="eqref" reference="eq:sk-product"}. Its denominator is $$(2u_c\lambda)\,
 (4u_c\sqrt{C_{\rm b}}\lambda^{-k})\{1+o(1)\},$$ while the numerator is $C_M\sqrt{1+\lambda^2}\lambda^k\{1+o(1)\}$. Their quotient is [\[eq:sk-asymptotic\]](#eq:sk-asymptotic){reference-type="eqref" reference="eq:sk-asymptotic"}.

No decimal evaluation of $C_{\rm b}$ or $C_M$ is used in this theorem.

# Maximum interval mass and the finite escape gap

Write $\Phi$ and $\overline\Phi=1-\Phi$ for the standard normal distribution and survival functions.

[\[lem:max-interval\]]{#lem:max-interval label="lem:max-interval"} For every $L>0$, $s>0$, mean $y\in\mathbb R$, and interval $J\subset\mathbb R$ of length $L$, $$\label{eq:max-interval}
 \Pr\{\mathcal N(y,s^2)\in J\}
 \le2\Phi\!\left(\frac{L}{2s}\right)-1.$$ The bound is uniform in the mean and interval location and is attained when $J$ is centered at $y$. The same upper bound holds for a mixture whose conditional law, given an arbitrary random mean, is $\mathcal N(y,s^2)$.

By translation and scaling, an interval starting at $t$ has mass $F(t)=\Phi(t+L/s)-\Phi(t)$ for a standard normal. Its derivative is $F'(t)=\phi(t+L/s)-\phi(t)$, which is positive before $t=-L/(2s)$ and negative after it. The unique maximum is the centered interval, with value [\[eq:max-interval\]](#eq:max-interval){reference-type="eqref" reference="eq:max-interval"}. Conditioning on the random mean and averaging preserves the same uniform bound.

[\[thm:finite-obstruction\]]{#thm:finite-obstruction label="thm:finite-obstruction"}

Fix $k\ge2$ and $\sigma>0$. Let $\mu^{\rm phys}_{\sigma,k}$ be any physical folded/normalized preclosing marginal in the coordinate [\[eq:physical-coordinate\]](#eq:physical-coordinate){reference-type="eqref" reference="eq:physical-coordinate"}. Let $\mu^{\rm aff}_{\sigma,k}$ be the $Q_{k-1}$ marginal of [\[def:raw-prefix\]](#def:raw-prefix){reference-type="ref" reference="def:raw-prefix"}, with an arbitrary entrance law independent of the innovations. Then $$\label{eq:finite-lower}
 \boxed{
 \|\mu^{\rm phys}_{\sigma,k}
     -\mu^{\rm aff}_{\sigma,k}\|_1
 \ge4\overline\Phi\!\left(\frac1{2\sigma s_k}\right).}$$ The same lower bound holds for the two retained component-prefix path laws. It also holds for any full retained extensions of those laws that still include the preclosing coordinate $Q_{k-1}$.

In [\[eq:exact-expansion\]](#eq:exact-expansion){reference-type="eqref" reference="eq:exact-expansion"}, isolate the first innovation and write $$\label{eq:Y-plus-noise}
 Q_{k-1}=Y+\varepsilon_kZ_0,
 \qquad |\varepsilon_k|=s_k.$$ Here $Y$ consists of the entrance term and innovations $Z_1,\ldots,Z_{k-2}$, so it is independent of $Z_0$. Conditional on $Y$, the affine preclosing law is Gaussian with standard deviation $s_k$. Since $|I_{\sigma,k}|=1/\sigma$, [\[lem:max-interval\]](#lem:max-interval){reference-type="ref" reference="lem:max-interval"} gives $$\label{eq:affine-escape}
 \mu^{\rm aff}_{\sigma,k}(I_{\sigma,k}^{\mathsf c})
 \ge2\overline\Phi\!\left(\frac1{2\sigma s_k}\right).$$ The physical law gives the complement zero mass. By the unhalved convention [\[eq:unhalved\]](#eq:unhalved){reference-type="eqref" reference="eq:unhalved"}, its distance from the affine law is at least twice the right side of [\[eq:affine-escape\]](#eq:affine-escape){reference-type="eqref" reference="eq:affine-escape"}, proving the factor four in [\[eq:finite-lower\]](#eq:finite-lower){reference-type="eqref" reference="eq:finite-lower"}.

Projection from a retained joint path to its preclosing coordinate is an $L^1$ contraction. Hence the joint distance is at least the marginal distance. The same projection argument applies after adding any further coordinates, provided the preclosing coordinate remains retained.

The bound needs no moment assumption on either entrance law. It uses only mass-one forward normalization, independence of the raw innovations, and the physical support interval.

# First-alias phase and the failed target scales

Let $\sigma\downarrow0$, let $k=k_\sigma\to\infty$, and define $$\label{eq:phase-clock}
 \eta_\sigma
 :=k-\frac{\log(1/\sigma)}{2\log\lambda}.$$ Then the identity $$\label{eq:clock-identity}
 \sigma\lambda^{2k}=\lambda^{2\eta_\sigma}$$ is exact.

[\[thm:phase-obstruction\]]{#thm:phase-obstruction label="thm:phase-obstruction"} If $\eta_\sigma\to\eta\in\mathbb R$, then every family in [\[thm:finite-obstruction\]](#thm:finite-obstruction){reference-type="ref" reference="thm:finite-obstruction"} satisfies $$\label{eq:fixed-phase-lower}
 \boxed{
 \liminf_{\sigma\downarrow0}
 \|\mu^{\rm phys}_{\sigma,k}
     -\mu^{\rm aff}_{\sigma,k}\|_1
 \ge
 4\overline\Phi\!\left(\frac1{2c_\eta}\right)>0,
 \qquad c_\eta=C_s\lambda^{2\eta}.}$$ The identical lower bound holds for the retained paths and full retained extensions described there.

More generally, if $\eta_\sigma\in[\eta_-,\eta_+]$ for all sufficiently small $\sigma$, then $$\label{eq:compact-phase-lower}
 \liminf_{\sigma\downarrow0}
 \|\mu^{\rm phys}_{\sigma,k}
     -\mu^{\rm aff}_{\sigma,k}\|_1
 \ge
 4\overline\Phi\!\left(
   \frac1{2C_s\lambda^{2\eta_-}}
 \right)>0.$$ Thus the obstruction is uniform on every compact phase interval.

Equations [\[eq:sk-asymptotic\]](#eq:sk-asymptotic){reference-type="eqref" reference="eq:sk-asymptotic"} and [\[eq:clock-identity\]](#eq:clock-identity){reference-type="eqref" reference="eq:clock-identity"} give $$\label{eq:sigma-sk}
 \sigma s_k=C_s\lambda^{2\eta_\sigma}\{1+o(1)\}.$$ The function $c\mapsto4\overline\Phi(1/(2c))$ is continuous and strictly increasing for $c>0$. Taking the limit in [\[eq:finite-lower\]](#eq:finite-lower){reference-type="eqref" reference="eq:finite-lower"} proves [\[eq:fixed-phase-lower\]](#eq:fixed-phase-lower){reference-type="eqref" reference="eq:fixed-phase-lower"}. When the phase remains in a compact interval, the $o(1)$ in [\[eq:sigma-sk\]](#eq:sigma-sk){reference-type="eqref" reference="eq:sigma-sk"} is independent of the phase because it is the one-variable sequence $s_k/(C_s\lambda^{2k})-1$. The smallest limiting scale on the interval is $C_s\lambda^{2\eta_-}$, proving [\[eq:compact-phase-lower\]](#eq:compact-phase-lower){reference-type="eqref" reference="eq:compact-phase-lower"}.

The RH-332 clearance phase is $$\label{eq:clearance-relation}
 d=C_{\rm b}\lambda^{-2\eta}>0.$$ It is related to the present scale only by $$\label{eq:c-d-relation}
 c_\eta=C_s\lambda^{2\eta}
 =\frac{C_sC_{\rm b}}d.$$ This relation matches clocks; it does not identify the raw affine tube with a physical closing profile.

[\[cor:rate-failure\]]{#cor:rate-failure label="cor:rate-failure"} On every sequence for which $\eta_\sigma$ stays in one fixed compact interval (in particular, on every fixed-phase sequence), neither $$\label{eq:false-rates}
 \|\mathsf P^{\rm phys}_{\sigma,k}-\mathsf Q^{\rm raw}_{\sigma,k}\|_1
 =O(k\sigma)
 \qquad\text{nor}\qquad
 \|\mathsf P^{\rm phys}_{\sigma,k}-\mathsf Q^{\rm raw}_{\sigma,k}\|_1
 =o(H_k),
 \quad H_k=kR^{-2k},\ R=1.4,$$ can hold for the retained paths in [\[thm:finite-obstruction\]](#thm:finite-obstruction){reference-type="ref" reference="thm:finite-obstruction"}.

The left sides have a uniformly positive liminf by the compact-phase part of [\[thm:phase-obstruction\]](#thm:phase-obstruction){reference-type="ref" reference="thm:phase-obstruction"}. Meanwhile boundedness of $\eta_\sigma$ and $\sigma=\lambda^{-2(k-\eta_\sigma)}$ give $k\sigma\to0$, and $H_k=kR^{-2k}\to0$. Both proposed upper scales therefore contradict the positive lower bound.

# Deterministic reproduction

The implementation reconstructs the RH-17 orbit by inverse contraction at 110 decimal working digits and evaluates both sides of [\[eq:sk-product\]](#eq:sk-product){reference-type="eqref" reference="eq:sk-product"} before converting the result rows to binary64 JSON. Selected rows are

    $k$   $2k$       $a_{k,0}$   $|M_k|/\lambda^k$   $s_k/\lambda^{2k}$
  ----- ------ --------------- ------------------- --------------------
      4      8   $-4.95945990$        $1.84255673$         $0.18488292$
      8     16   $-5.17844066$        $1.93725622$         $0.17646891$
     12     24   $-5.18232740$        $1.94527476$         $0.17524766$
     16     32   $-5.18238996$        $1.94620960$         $0.17509057$
     20     40   $-5.18239095$        $1.94632613$         $0.17507073$
     24     48   $-5.18239097$        $1.94634079$         $0.17506823$

The product and quotient evaluations of $s_k$ agree to the 110-digit working precision before conversion to the displayed decimals.

For orientation only, the phase table inserts the repository evaluations $$C_{\rm b}=0.4608051492217\ldots,
 \qquad C_M=1.946342905200967\ldots$$ into [\[eq:sk-asymptotic\]](#eq:sk-asymptotic){reference-type="eqref" reference="eq:sk-asymptotic"} and evaluates the normal survival function with binary64 arithmetic. This gives $C_s=0.175067867214394\ldots$ and the following phase rows.

    $\eta$   $d=C_{\rm b}\lambda^{-2\eta}$   $c_\eta=C_s\lambda^{2\eta}$   $4\overline\Phi(1/(2c_\eta))$
  -------- ------------------------------- ----------------------------- -------------------------------
    $-1/2$                    $0.77349532$                  $0.10429562$                    $0.00000327$
       $0$                    $0.46080515$                  $0.17506787$                    $0.00857935$
     $1/2$                    $0.27452188$                  $0.29386428$                    $0.17771115$

Both protocols produce ordinary numerical reproduction values, not directed-rounding interval certificates: the orbit identities use the stated high working precision, while the phase and $C_s$ table uses binary64 arithmetic. The finite rows verify identities and illustrate convergence; they do not prove [\[eq:sk-asymptotic\]](#eq:sk-asymptotic){reference-type="eqref" reference="eq:sk-asymptotic"} or [\[eq:fixed-phase-lower\]](#eq:fixed-phase-lower){reference-type="eqref" reference="eq:fixed-phase-lower"}.

# Claim boundary and next interface

The proved negative statement has four simultaneous qualifiers:

1.  the comparison object is the canonical raw, mass-one, full-line forward affine reference [\[eq:raw-kernel\]](#eq:raw-kernel){reference-type="eqref" reference="eq:raw-kernel"};

2.  the theorem concerns the prefix of $k-1$ component rows before the tiny closing component row, equivalently a retained preclosing coordinate inside the full $2k$ one-step path;

3.  the lower bound survives in a full retained path only because that preclosing coordinate remains present; and

4.  the statement belongs to probability path laws, not cyclic trace observations.

The tiny closing row may strongly contract its input. After marginalizing away the preclosing coordinate, [\[thm:finite-obstruction\]](#thm:finite-obstruction){reference-type="ref" reference="thm:finite-obstruction"} supplies no lower bound for the final endpoint marginal. It therefore does not prove endpoint failure after closure.

Nor does the theorem refute a cyclic bridge, a Doob transform, a physical truncated or folded affine kernel, an adapted reference, or a branch-complete nonlinear closing profile. None of those alternatives is currently defined with the required common entrance, normalization, path coordinates, and physical comparison map, so their status here is `NOT_TESTABLE`. A future positive transport route must first define one such reference and then handle the closing row in that exact data type.

No probability-to-trace observation is proved. There is no cyclic trace control, signed shell or parity cancellation, full-trace replacement, or determinant gluing. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt-weighted prime-power trace or completed-zeta divisor equality, and does not imply the Riemann Hypothesis.
