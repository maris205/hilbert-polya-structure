---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-327-neighboring-shell-coupling-cancellation-budget"
canonical_tex: "zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget/main.pdf"
source_sha256: "6ed25e7467d7cfaf0dbbd8409a061680bb5caf746cae19b0c5d80c15f34deb3a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Neighboring-Shell Coupling and Cancellation Budgets: Exact Localized Trace Slots and Exchange-Channel Nonidentifiability

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-327-neighboring-shell-coupling-cancellation-budget/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The critical sibling cannot be discarded as a Gaussian tail, but its equal forward mass does not determine a signed trace contribution. We first define the missing object directly at the cyclic-trace level. A basepoint partition into the boundary window, its neighboring critical sibling, and the far complement gives an exact Hardy-scaled decomposition of the actual raw trace packet into boundary, shell, and remainder slots. No smallness of the remainder or sign of the shell is inferred. We then construct an exchange-symmetric two-channel Markov completion retaining the clearance parameter and the oriented affine payload of RH-323. Every branch-blind power compression is independent of the exchange contrast, whereas the trace power equals $1+c^m$. Thus the archived local probability data do not identify the shell trace. For a fixed reference contrast $c_0$, the even-order signed defect has the exact interval $[-L|c_0|^{2k},L(1-|c_0|^{2k})]$, yielding a sharp cancellation-distance formula. A fixed nonzero fraction of the scale forces at least one contrast to approach unit modulus at rate $1-O(k^{-1})$. These are exact localized and synthetic-model theorems, not an identification of the physical shell, a joint first-alias matching theorem, or a full-trace replacement.
author:
- Bin Wang
date: July 2026
title: |
  Neighboring-Shell Coupling and Cancellation Budgets:\
  Exact Localized Trace Slots and Exchange-Channel Nonidentifiability
```

## Markdown 正文

# Actual localized trace slots

Let $u_c\in(1,2)$ be the root of $u^3-2u^2+2u-2=0$, put $f(x)=1-u_cx^2$, and let $K_\sigma$ be the row-normalized noisy Markov operator with smooth kernel $p_\sigma(x,y)$ on $[0,1]$. Define the deterministic flat trace by $$P_n=\sum_{f^n(x)=x}\frac1{|1-(f^n)'(x)|}
 \label{eq:flat-trace}$$ Put $r_H=0.85$. The raw Hardy packet is $$\mathcal T_{\sigma,n}=r_H^{-n}\{\operatorname{Tr}K_\sigma^n-P_n\}.
 \label{eq:raw-packet}$$

Put $$\lambda=2u_c(u_c-1),
 \qquad
 \beta=(r_H\sqrt\lambda)^{-1},
 \qquad
 R=1.4.
 \label{eq:route-constants}$$ All first-alias asymptotics below are taken as $\sigma\to0$ along $$k=k_\sigma
 =\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad
 \eta_\sigma=k_\sigma-\frac{\log(1/\sigma)}{2\log\lambda},
 \label{eq:natural-clock}$$ with bounded $\eta_\sigma$. Passing to a fixed-phase subsequence when needed, we write $\eta_\sigma\to\eta$.

We retain the first-alias clearance rather than suppressing its integer phase. Let $p_{2k}$ be the distinguished deterministic boundary periodic point, set $$\begin{aligned}
 \Delta_k^{\rm clr}
 &=1-p_{2k}=C_{\rm b}\lambda^{-2k}\{1+o(1)\},
 & C_{\rm b}&>0,
 \label{eq:clearance-source}
 \\
 h(x)&=\sqrt{\frac{1-\sqrt{(1-x)/u_c}}{u_c}},
 & s_{\sigma,k}&=h(p_{2k})\end{aligned}$$ and write $$d_{\sigma,k}=\frac{\Delta_k^{\rm clr}}\sigma,
 \qquad
 b=u_c^{-1/2},
 \qquad
 q_{{\rm b},\sigma,k}=\frac{b-s_{\sigma,k}}{\sqrt\sigma},
 \qquad
 q_{\sigma,k}(x)=\frac{x-s_{\sigma,k}}{\sqrt\sigma},
 \label{eq:sibling-coordinates}$$ where $s_{\sigma,k}$ is the final source point. The archived inverse-branch expansion gives $$q_{{\rm b},\sigma,k}
 =\frac{\sqrt{d_{\sigma,k}}}{2u_c}
  +O(\sqrt\sigma\,d_{\sigma,k}).
 \label{eq:partition-asymptotic}$$ Moreover, the natural clock gives $$d_{\sigma,k}=C_{\rm b}\lambda^{-2\eta_\sigma}\{1+o(1)\}
 \longrightarrow C_{\rm b}\lambda^{-2\eta}
 \label{eq:clearance-phase}$$ along a fixed-phase subsequence. For a fixed window radius $A>0$, choose the half-open physical sibling windows $$\begin{aligned}
 J^-_{\sigma,k,A}
 &=\{x\in[0,1]:q_{{\rm b},\sigma,k}-A
     \le q_{\sigma,k}(x)<q_{{\rm b},\sigma,k}\},
 \label{eq:left-window}\\
 J^+_{\sigma,k,A}
 &=\{x\in[0,1]:q_{{\rm b},\sigma,k}
     \le q_{\sigma,k}(x)\le q_{{\rm b},\sigma,k}+A\},
 \label{eq:right-window}\end{aligned}$$ and let $F_{\sigma,k,A}$ be their complement. The labels $-$ and $+$ here refer to the two RH-19 physical branches. They are not the signs in the RH-323 coordinate orientation $(+,-,+)$.

For a measurable set $J\subset[0,1]$, let $M_J$ be multiplication by its indicator and define $$\begin{aligned}
 L_{\sigma,n}(J)&=\operatorname{Tr}(M_JK_\sigma^n),
 \label{eq:localized-noisy}\\
 P_n(J)&=\sum_{\substack{f^n(x)=x\\x\in J}}
       \frac1{|1-(f^n)'(x)|}.
 \label{eq:localized-flat}\end{aligned}$$

[\[thm:localized-partition\]]{#thm:localized-partition label="thm:localized-partition"} For every $n\ge2$ for which $K_\sigma^n$ is trace class, $$L_{\sigma,n}(J)
 =\int_{x_0\in J}\int_{[0,1]^{n-1}}
   \prod_{j=0}^{n-1}p_\sigma(x_j,x_{j+1})
   \,dx_1\cdots dx_{n-1}\,dx_0,
 \qquad x_n=x_0.
 \label{eq:closed-loop-observation}$$ With the partition in [\[eq:left-window\]](#eq:left-window){reference-type="eqref" reference="eq:left-window"}--[\[eq:right-window\]](#eq:right-window){reference-type="eqref" reference="eq:right-window"}, define $$\begin{aligned}
 \mathcal B_{\sigma,k,n}
 &=r_H^{-n}\{L_{\sigma,n}(J^-_{\sigma,k,A})
                   -P_n(J^-_{\sigma,k,A})\},
 \label{eq:boundary-slot}\\
 \mathcal S_{\sigma,k,n}
 &=r_H^{-n}\{L_{\sigma,n}(J^+_{\sigma,k,A})
                   -P_n(J^+_{\sigma,k,A})\},
 \label{eq:shell-slot}\\
 \mathcal R_{\sigma,k,n}
 &=r_H^{-n}\{L_{\sigma,n}(F_{\sigma,k,A})
                   -P_n(F_{\sigma,k,A})\}.
 \label{eq:far-slot}\end{aligned}$$ Then the actual raw trace packet has the exact signed decomposition $$\boxed{\mathcal T_{\sigma,n}
 =\mathcal B_{\sigma,k,n}+\mathcal S_{\sigma,k,n}+\mathcal R_{\sigma,k,n}.}
 \label{eq:raw-decomposition}$$

Equation [\[eq:closed-loop-observation\]](#eq:closed-loop-observation){reference-type="eqref" reference="eq:closed-loop-observation"} is the diagonal-kernel trace of $M_JK_\sigma^n$. The three indicators sum to one, so linearity of the trace splits $\operatorname{Tr}K_\sigma^n$. The fixed points in [\[eq:flat-trace\]](#eq:flat-trace){reference-type="eqref" reference="eq:flat-trace"} are partitioned by the same three sets. Subtract and multiply by $r_H^{-n}$.

This theorem constructs an actual cyclic observation and an actual signed shell slot. It does not identify [\[eq:shell-slot\]](#eq:shell-slot){reference-type="eqref" reference="eq:shell-slot"} with the RH-19 one-pullback $L^2$ mass or with the RH-322--RH-324 forward probability laws. The localization marks a closed-loop basepoint; the older branch-return operators mark a prescribed time-labeled path. No estimate here proves that $\mathcal R_{\sigma,k,2k}$ is small.

# The exact first-alias budget

Write the peripheral parity eigenvalue as $$\lambda_-(\sigma)=-(1-\delta_\sigma),
 \qquad
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma),
 \qquad C_*>0,
 \label{eq:parity-type}$$ and, for the archived boundary-cycle multiplier $M_k$, type the finite counterloop radius by $$\beta_k=\frac{|M_k|^{-1/(2k)}}{r_H}
 =\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right],
 \qquad C_M>0.
 \label{eq:counterloop-type}$$ The even parity packet and first-alias counterloop defect are $$\begin{aligned}
 \mathcal P_{\sigma,2k}
 &=r_H^{-2k}\{1-\lambda_-(\sigma)^{2k}\}>0,
 \label{eq:parity-packet}\\
 \mathcal A_{k,2k}
 &=(2k-2)\beta_k^{2k}+2\beta^{2k}>0.
 \label{eq:alias-defect}\end{aligned}$$ Define the RH-326 coefficient residual at $n=2k$ by the exact ledger $$e_{\sigma,k,2k}
 =\mathcal B_{\sigma,k,2k}+\mathcal S_{\sigma,k,2k}
  +\mathcal R_{\sigma,k,2k}+\mathcal P_{\sigma,2k}-\mathcal A_{k,2k},
 \label{eq:joint-ledger}$$ Thus the positive packets occur with signs $+\mathcal P-\mathcal A$. No rounded decimal inequality for $C_*$ or $C_M$ is used. Let $$H_k=kR^{-2k}.
 \label{eq:target}$$

[\[prop:necessary-budget\]]{#prop:necessary-budget label="prop:necessary-budget"} If $e_{\sigma,k,2k}=o(H_k)$ and $\mathcal R_{\sigma,k,2k}=o(H_k)$, then necessarily $$\mathcal B_{\sigma,k,2k}+\mathcal S_{\sigma,k,2k}
 =\mathcal A_{k,2k}-\mathcal P_{\sigma,2k}+o(H_k).
 \label{eq:necessary-match}$$ The archived counterloop asymptotic gives $$\mathcal A_{k,2k}=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},
 \qquad
 \frac{H_k}{\mathcal A_{k,2k}}
 =\frac{C_M}{2}(\beta R)^{-2k}\{1+o(1)\}.
 \label{eq:relative-target}$$ Hence [\[eq:necessary-match\]](#eq:necessary-match){reference-type="eqref" reference="eq:necessary-match"} is equivalently the exact-centered demand $$\frac{\mathcal B+\mathcal S}{\mathcal A}
 -\left(1-\frac{\mathcal P}{\mathcal A}\right)
 =o\bigl((\beta R)^{-2k}\bigr).
 \label{eq:relative-demand}$$ Along a fixed phase subsequence, $\mathcal P/\mathcal A=C_*C_M\lambda^\eta+o(1)$, but that leading phase law alone does not supply the much finer error in [\[eq:relative-demand\]](#eq:relative-demand){reference-type="eqref" reference="eq:relative-demand"}.

Rearrange [\[eq:joint-ledger\]](#eq:joint-ledger){reference-type="eqref" reference="eq:joint-ledger"}. Equation [\[eq:relative-target\]](#eq:relative-target){reference-type="eqref" reference="eq:relative-target"} is the RH-326 multiplier asymptotic divided into [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"}. Division of [\[eq:necessary-match\]](#eq:necessary-match){reference-type="eqref" reference="eq:necessary-match"} by $\mathcal A$ proves [\[eq:relative-demand\]](#eq:relative-demand){reference-type="eqref" reference="eq:relative-demand"}.

No sign is assigned to the required quantity in [\[eq:necessary-match\]](#eq:necessary-match){reference-type="eqref" reference="eq:necessary-match"}. In particular, the repository does not contain an interval certificate for $C_*C_M\lambda<1$.

# A branch-blind exchange completion

The localized trace slots are exact, but their asymptotics remain unknown. We now isolate the missing information with a synthetic two-channel model. Let $$\Pi_{\rm s}=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
 \qquad
 \Pi_{\rm a}=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \qquad
 \mathbf K_c=\Pi_{\rm s}+c\Pi_{\rm a},\quad |c|\le1.
 \label{eq:exchange-matrix}$$ Write $E_-=\operatorname{diag}(1,0)$ and $E_+=\operatorname{diag}(0,1)$ for the two branch-coordinate projectors. This is a nonnegative symmetric Markov matrix. Its branch labels are the physical sibling coordinate; the sign of $c$ is neither a parity sign nor a sign of an individual branch mass.

To retain the RH-323 payload, define $$\phi(t)=\frac{e^{-t^2/2}}{\sqrt{2\pi}},
 \qquad
 \Phi(t)=\int_{-\infty}^t\phi(s)\,ds,
 \qquad
 g_d(v)=\frac{\phi(v-d)}{\Phi(d)}\mathbf1_{[0,\infty)}(v),
 \quad d\ge0,
 \label{eq:affine-ingredients}$$ and let $J_d$ be the probability law $$dJ_d(v,u,w)
 =g_d(v)\phi(u+\alpha v)\phi(w+\lambda u)\,dv\,du\,dw,
 \label{eq:affine-law}$$ where $\alpha=2u_c$ and $\kappa_{\rm aff}=\alpha\lambda$. It has orientation $(V,U,W)=(+,-,+)$ and its output is compared after the shift $W-\kappa_{\rm aff}d$. On $L^2(J_d)$ define the rank-one Markov reset $$G_df=\left(\int f\,dJ_d\right)\mathbf1,
 \label{eq:reset}$$ so $G_d$ is a rank-one trace-class projection with $\operatorname{Tr}G_d=1$. Put $Q_{d,c}=G_d\otimes\mathbf K_c$. This is an explicit synthetic completion, not the physical noisy kernel.

[\[thm:nonidentifiability\]]{#thm:nonidentifiability label="thm:nonidentifiability"} Let $e_{\rm s}=2^{-1/2}(1,1)^T$ and let $I_{\rm s}h=h\otimes e_{\rm s}$. For every $m\ge1$, $$\begin{aligned}
 \mathbf K_c^m&=\Pi_{\rm s}+c^m\Pi_{\rm a},
 \label{eq:power-law}\\
 I_{\rm s}^*Q_{d,c}^mI_{\rm s}&=G_d,
 \label{eq:blind-compression}\\
 \operatorname{Tr}Q_{d,c}^m&=1+c^m.
 \label{eq:trace-contrast}\end{aligned}$$ Moreover, the two branch-localized traces are exactly equal: $$\operatorname{Tr}\{(I\otimes E_\pm)Q_{d,c}^m\}
 =\frac{1+c^m}{2}.
 \label{eq:equal-localized-traces}$$ Thus the clearance, affine law, orientation, output shift, and every symmetric power compression are identical for all $c$, while the trace power varies with $c$.

The two projectors in [\[eq:exchange-matrix\]](#eq:exchange-matrix){reference-type="eqref" reference="eq:exchange-matrix"} are complementary and orthogonal, proving [\[eq:power-law\]](#eq:power-law){reference-type="eqref" reference="eq:power-law"}. Since $G_d^m=G_d$ and $\Pi_{\rm s}e_{\rm s}=e_{\rm s}$ while $\Pi_{\rm a}e_{\rm s}=0$, tensor compression gives [\[eq:blind-compression\]](#eq:blind-compression){reference-type="eqref" reference="eq:blind-compression"}. Both $G_d$ and $\Pi_{\rm s}$ have trace one, and $\Pi_{\rm a}$ has trace one, proving [\[eq:trace-contrast\]](#eq:trace-contrast){reference-type="eqref" reference="eq:trace-contrast"}. The diagonal entries of [\[eq:power-law\]](#eq:power-law){reference-type="eqref" reference="eq:power-law"} are equal to $(1+c^m)/2$, proving [\[eq:equal-localized-traces\]](#eq:equal-localized-traces){reference-type="eqref" reference="eq:equal-localized-traces"}.

The theorem is a closure-observation no-go: branch-blind probability data do not identify the antisymmetric loop contrast. It does not say that the actual Gaussian shell is small, large, or represented by any $Q_{d,c}$.

# Fixed-reference shell interval and sharp residual

Let $L>0$ be a typed shell scale and let $c_0\in[-1,1]$ be a fixed deterministic reference contrast. At the even first alias define the signed exchange defect $$X_{k,L}(c;c_0)=L\{c^{2k}-c_0^{2k}\}.
 \label{eq:exchange-defect}$$ Its sign comes only from noisy-minus-reference subtraction. A single positive Markov completion has no signed shell defect by itself.

[\[thm:fixed-budget\]]{#thm:fixed-budget label="thm:fixed-budget"} For fixed $c_0$, the exact image of [\[eq:exchange-defect\]](#eq:exchange-defect){reference-type="eqref" reference="eq:exchange-defect"} is $$\boxed{
 I_{k,L,c_0}
 =[-L|c_0|^{2k},\,L(1-|c_0|^{2k})].}
 \label{eq:fixed-interval}$$ For any demanded shell value $D\in\mathbb R$, $$\inf_{|c|\le1}|X_{k,L}(c;c_0)-D|
 =\operatorname{dist}(D,I_{k,L,c_0}).
 \label{eq:sharp-distance}$$ If $D$ lies in the interval, a realizing nonnegative contrast is $$c=\left(\frac DL+|c_0|^{2k}\right)^{1/(2k)}.
 \label{eq:realizing-contrast}$$

As $|c|\le1$, the even power $c^{2k}$ fills $[0,1]$. Translation by $-|c_0|^{2k}$ and multiplication by $L$ gives [\[eq:fixed-interval\]](#eq:fixed-interval){reference-type="eqref" reference="eq:fixed-interval"}. The closest attainable scalar is the projection of $D$ onto this closed interval, proving [\[eq:sharp-distance\]](#eq:sharp-distance){reference-type="eqref" reference="eq:sharp-distance"}. Solving [\[eq:exchange-defect\]](#eq:exchange-defect){reference-type="eqref" reference="eq:exchange-defect"} for $c$ gives [\[eq:realizing-contrast\]](#eq:realizing-contrast){reference-type="eqref" reference="eq:realizing-contrast"}.

[\[cor:free-budget\]]{#cor:free-budget label="cor:free-budget"} If both $c$ and $c_0$ are allowed to vary over the unidentified completion class, the union of defect values is $[-L,L]$ and the sharp residual is $$(|D|-L)_+.
 \label{eq:free-distance}$$ This is an information-class result. It is not permissible to optimize the physical deterministic reference when testing an actual matching equation.

[\[prop:edge-law\]]{#prop:edge-law label="prop:edge-law"} If $|X_{k,L}(c;c_0)|\ge\delta L$ for a fixed $0<\delta\le1$, then $$\max\{|c|,|c_0|\}\ge\delta^{1/(2k)}.
 \label{eq:edge-necessity}$$ Consequently at least one contrast obeys $$1-|c_*|\le\frac{\log(1/\delta)}{2k}+O(k^{-2}).
 \label{eq:edge-gap}$$ If both contrasts are bounded by $1-\varepsilon$, then $|X_{k,L}|/L\le(1-\varepsilon)^{2k}$ and the exchange defect is not a fixed nonzero fraction of $L$.

Put $r=\max\{|c|,|c_0|\}$. Both even powers lie in $[0,r^{2k}]$, so their difference has modulus at most $r^{2k}$. This proves [\[eq:edge-necessity\]](#eq:edge-necessity){reference-type="eqref" reference="eq:edge-necessity"}. Expanding $\delta^{1/(2k)}=\exp\{\log\delta/(2k)\}$ gives [\[eq:edge-gap\]](#eq:edge-gap){reference-type="eqref" reference="eq:edge-gap"}. The uniform-gap statement is immediate.

For example, with $2k=8$ and $c_0=0.8$, the unit-scale interval is $$.
 \label{eq:numeric-interval}$$ Demands $-0.25$ and $0.9$ therefore leave exact residual fractions $0.08222784$ and $0.06777216$, respectively. These are ordinary evaluations of exact formulas for a synthetic model, not physical shell measurements.

# RH-328 interface and claim boundary

For the actual first-alias ledger, put $$D_{\sigma,k}=\mathcal A_{k,2k}-\mathcal P_{\sigma,2k}
               -\mathcal B_{\sigma,k,2k}.
 \label{eq:actual-demand}$$ If an RH-328 model proposes to replace the actual localized shell by $X_{k,L}(c;c_0)$, then its best leading residual before $\mathcal R$ is exactly $$\operatorname{dist}(D_{\sigma,k},I_{k,L,c_0}).
 \label{eq:handoff-distance}$$ This distance optimizes over every noisy contrast in the synthetic class. It is only a best-case reachability obstruction and does not show that the physical contrast attains the closest point. A necessary pre-screen is $$\operatorname{dist}(D_{\sigma,k},I_{k,L,c_0})=o(kR^{-2k}).
 \label{eq:reachability-screen}$$ Actual closure through this model requires an identified contrast $c_{\sigma,k}^{\rm phys}$ satisfying $$|X_{k,L}(c_{\sigma,k}^{\rm phys};c_0)-D_{\sigma,k}|
 =o(kR^{-2k}),
 \qquad
 \mathcal R_{\sigma,k,2k}=o(kR^{-2k}),
 \label{eq:handoff-requirements}$$ together with a theorem identifying the physical trace observation, shell scale $L$, noisy contrast $c$, and fixed reference $c_0$. None of those identifications is supplied by the reset completion.

The typed handoff retains $\sigma$, $k$, period $2k$, phase $\eta$, clearance $d$, the coordinates $(V,U,W)$ with orientation $(+,-,+)$, the shift $\kappa_{\rm aff}d$, Hardy normalization $r_H^{-2k}$, and the exact sign ledger $$e=\mathcal B+\mathcal S+\mathcal R+\mathcal P-\mathcal A.
 \label{eq:typed-ledger}$$ RH-325's operator Duhamel weights must still include the trace-observation norm and every prefix/suffix product norm. Markov $L^1$ contraction does not prove either requirement in [\[eq:handoff-requirements\]](#eq:handoff-requirements){reference-type="eqref" reference="eq:handoff-requirements"}.

The paper proves an actual basepoint-localized raw-trace partition and exact theorems for a synthetic exchange completion. It does not control the magnitude or sign of the actual shell slot, identify the RH-323 probability law with the localized cyclic trace, prove a physical exchange parameter, bound the far trace remainder, control the second physical leg, or establish the joint alias/parity/shell matching equation. No full-trace replacement or actual divergence theorem follows. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or completed-zeta divisor equality, and does not imply RH.

RH-328 may now test a fixed-reference joint matching equation only after it supplies the physical localized observation estimates and the shell parameters required in [\[eq:reachability-screen\]](#eq:reachability-screen){reference-type="eqref" reference="eq:reachability-screen"}--[\[eq:handoff-requirements\]](#eq:handoff-requirements){reference-type="eqref" reference="eq:handoff-requirements"}.
