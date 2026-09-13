---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-326-parity-renormalized-first-alias-packet-identity"
canonical_tex: "zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity/main.pdf"
source_sha256: "73dbc3f0c2b1e11e57d25392ea72e65437838ad51de2f93ee9ed8c17e0829faa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parity-Renormalized First-Alias Packets: Exact Signs, Clock Phase, and the Neighboring-Shell Interface

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-326-parity-renormalized-first-alias-packet-identity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The first counterloop alias and the square-root parity leakage occur at the same weighted order, so their signs and normalization cannot be suppressed. We restore the Hardy scaling hidden in the earlier first-alias ledger and split the coefficient defect exactly into a raw-trace packet, a signed parity packet, a finite-radius radial correction, and the roots-of-unity alias impulse. At the even first alias the parity correction is positive, whereas the counterloop defect is subtracted from the total residual. The parity packet has a uniform moving-order expansion with an explicit quadratic remainder. On a fixed clock phase $\eta$, its leading ratio to the alias defect is $C_*C_M\lambda^\eta$, so the unique symbolic balance phase is $-\log(C_*C_M)/\log\lambda$. If $C_*C_M\lambda<1$, this gives a strict scalar-only obstruction throughout the usual floor/ceil/nearest phase window $|\eta|\le1$. The archived decimal evaluation supports that hypothesis but is not an interval certificate. This conditional negative result does not exclude cancellation by the raw physical boundary packet and neighboring shell. We finish with a phase- and coordinate-preserving interface for that calculation. No joint full-trace replacement is proved.
author:
- Bin Wang
date: July 2026
title: |
  Parity-Renormalized First-Alias Packets:\
  Exact Signs, Clock Phase, and the Neighboring-Shell Interface
```

## Markdown 正文

# Normalization and four packet types

Put $$\lambda=1.678573510428322\ldots,
 \qquad r_H=0.85,
 \qquad R=1.4,
 \qquad \beta=(r_H\sqrt\lambda)^{-1}.
 \label{eq:constants}$$ The number $r_H$ is the chosen Hardy scaling radius, not a dynamical invariant. Let $P_n$ be the deterministic physical flat trace and let $K_\sigma$ be the row-normalized noisy Markov operator. The peripheral parity eigenvalue is written $$\lambda_-(\sigma)=-(1-\delta_\sigma),
 \qquad
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma),
 \qquad
 C_*=0.105258535936908\ldots .
 \label{eq:parity-gap}$$ The decimal evaluates an archived positive integral; positivity and the square-root law, rather than the rounded decimal, are the analytic inputs.

We use explicit Hardy superscripts to avoid mixing two archived conventions: $$\begin{aligned}
 c^H_{\sigma,n}
 &=r_H^{-n}\{\operatorname{Tr}K_\sigma^n-1-\lambda_-(\sigma)^n\},
 \label{eq:noisy-hardy}\\
 c^H_n
 &=r_H^{-n}\{P_n-1-(-1)^n\}.
 \label{eq:det-hardy}\end{aligned}$$ Define the raw-trace and parity packets $$\begin{aligned}
 \mathcal T_{\sigma,n}
 &=r_H^{-n}\{\operatorname{Tr}K_\sigma^n-P_n\},
 \label{eq:raw-packet}\\
 \mathcal P_{\sigma,n}
 &=r_H^{-n}\{(-1)^n-\lambda_-(\sigma)^n\}
 =(-1)^nr_H^{-n}\{1-(1-\delta_\sigma)^n\}.
 \label{eq:parity-packet}\end{aligned}$$ Then, identically, $$c^H_{\sigma,n}-c^H_n=\mathcal T_{\sigma,n}+\mathcal P_{\sigma,n}.
 \label{eq:bulk-split}$$

For $k\ge2$, let $M_k$ be the archived boundary-cycle multiplier and put $$\rho_k=|M_k|^{-1/k},
 \qquad
 \beta_k=\frac{\sqrt{\rho_k}}{r_H}
 =\frac{|M_k|^{-1/(2k)}}{r_H}.
 \label{eq:beta-type}$$ The Hardy-scaled finite counterloop is $$s_{k,n}=\beta_k^n
 \bigl(2k\mathbf 1_{2k\mid n}-1-(-1)^n\bigr),
 \qquad \beta_k\longrightarrow\beta.
 \label{eq:counterloop}$$ Rename the limiting pole moment and numerator anchor to avoid collisions with older uses of $p_n$ and $a_n$: $$p_n^{\rm pole}=-2\mathbf 1_{2\mid n}\beta^n,
 \qquad
 a_n^{\rm num}=c^H_n-p_n^{\rm pole}.
 \label{eq:pole-anchor}$$

# Exact alias and parity algebra

[\[thm:counterloop-split\]]{#thm:counterloop-split label="thm:counterloop-split"} For every $k\ge2$ and $n\ge1$, the counterloop defect is exactly $$\boxed{
 \mathcal A_{k,n}:=s_{k,n}-p_n^{\rm pole}
 =2\mathbf 1_{2\mid n}(\beta^n-\beta_k^n)
 +2k\beta_k^n\mathbf 1_{2k\mid n}.}
 \label{eq:counterloop-split}$$ The first term is finite-radius radial drift and the second is the exact roots-of-unity alias impulse. In particular, $\mathcal A_{k,n}=0$ for every odd $n$, while $$\mathcal A_{k,2k}=(2k-2)\beta_k^{2k}+2\beta^{2k}>0.
 \label{eq:first-alias-defect}$$

Substitute [\[eq:counterloop\]](#eq:counterloop){reference-type="eqref" reference="eq:counterloop"} and [\[eq:pole-anchor\]](#eq:pole-anchor){reference-type="eqref" reference="eq:pole-anchor"}. If $n$ is odd, both $1+(-1)^n$ and the two divisibility indicators vanish. If $n$ is even, the non-alias part is $-2\beta_k^n+2\beta^n$, and an order divisible by $2k$ receives the additional impulse $2k\beta_k^n$. Setting $n=2k$ gives [\[eq:first-alias-defect\]](#eq:first-alias-defect){reference-type="eqref" reference="eq:first-alias-defect"}.

The sign ledger is now unambiguous:

  order                 parity packet $\mathcal P_{\sigma,n}$   counterloop defect $\mathcal A_{k,n}$    signs in the residual
  -------------------- --------------------------------------- --------------------------------------- --------------------------
  odd                                 negative                                   $0$                         $+\mathcal P$
  even, $2k\nmid n$                   positive                         $2(\beta^n-\beta_k^n)$           $+\mathcal P-\mathcal A$
  first alias $n=2k$                  positive                    $(2k-2)\beta_k^{2k}+2\beta^{2k}$      $+\mathcal P-\mathcal A$

Only the parity sign is asserted in the middle row; the radial difference need not be assigned a sign without a finite-$k$ radius inequality.

[\[thm:main-identity\]]{#thm:main-identity label="thm:main-identity"} Let $$e_{\sigma,k,n}=c^H_{\sigma,n}-s_{k,n}-a_n^{\rm num}.
 \label{eq:error}$$ Then at the first alias, $$\begin{aligned}
 e_{\sigma,k,2k}
 &=\mathcal T_{\sigma,2k}+\mathcal P_{\sigma,2k}-\mathcal A_{k,2k}
 \label{eq:packet-form}\\
 &=r_H^{-2k}\{\operatorname{Tr}K_\sigma^{2k}-P_{2k}
     +1-\lambda_-(\sigma)^{2k}\}
 \notag\\[-0.2em]
 &\hspace{5em}
 -\{(2k-2)\beta_k^{2k}+2\beta^{2k}\}.
 \label{eq:expanded-form}\end{aligned}$$ In particular, the scalar parity contribution in [\[eq:expanded-form\]](#eq:expanded-form){reference-type="eqref" reference="eq:expanded-form"} is $$r_H^{-2k}\{1-\lambda_-(\sigma)^{2k}\}
 =r_H^{-2k}\{1-(1-\delta_\sigma)^{2k}\}>0.
 \label{eq:positive-even-parity}$$

Using $a_n^{\rm num}=c^H_n-p_n^{\rm pole}$ in [\[eq:error\]](#eq:error){reference-type="eqref" reference="eq:error"} gives $$e_{\sigma,k,n}=(c^H_{\sigma,n}-c^H_n)
 -(s_{k,n}-p_n^{\rm pole}).$$ Apply [\[eq:bulk-split\]](#eq:bulk-split){reference-type="eqref" reference="eq:bulk-split"}, [\[thm:counterloop-split\]](#thm:counterloop-split){reference-type="ref" reference="thm:counterloop-split"}, and set $n=2k$. Equation [\[eq:positive-even-parity\]](#eq:positive-even-parity){reference-type="eqref" reference="eq:positive-even-parity"} follows because $0<1-\delta_\sigma<1$ for sufficiently small noise.

This theorem is an exact coefficient identity. It does not approximate $\mathcal T_{\sigma,2k}$ by a local Gaussian law and therefore does not assume the missing trace-observation theorem.

# Uniform parity packet on the first-alias clock

[\[thm:parity-expansion\]]{#thm:parity-expansion label="thm:parity-expansion"} For $0\le\delta<1$ and every $n\ge1$, $$\left|
 \mathcal P_{\sigma,n}-(-1)^n n\delta r_H^{-n}
 \right|
 \le \frac{n(n-1)}2\delta^2r_H^{-n},
 \label{eq:uniform-remainder}$$ where the left side uses [\[eq:parity-packet\]](#eq:parity-packet){reference-type="eqref" reference="eq:parity-packet"} with $\delta_\sigma=\delta$. Consequently, if $$k_\sigma=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \label{eq:natural-clock}$$ then $$\mathcal P_{\sigma,2k_\sigma}
 =2k_\sigma C_*\sqrt\sigma\,r_H^{-2k_\sigma}
 \{1+o(1)\}.
 \label{eq:moving-parity}$$ Its weighted size and the weighted first-alias defect share the growth exponent $$\chi=\frac{\log(\beta R)}{\log\lambda}
 =0.463406944517002\ldots .
 \label{eq:common-exponent}$$

Taylor's theorem for $f(\delta)=1-(1-\delta)^n$ gives $$f(\delta)=n\delta-\frac{n(n-1)}2(1-\xi)^{n-2}\delta^2$$ for some $0\le\xi\le\delta$, proving [\[eq:uniform-remainder\]](#eq:uniform-remainder){reference-type="eqref" reference="eq:uniform-remainder"}. On [\[eq:natural-clock\]](#eq:natural-clock){reference-type="eqref" reference="eq:natural-clock"}, $k_\sigma\delta_\sigma\to0$, so the remainder is $o(k_\sigma\delta_\sigma r_H^{-2k_\sigma})$ and [\[eq:moving-parity\]](#eq:moving-parity){reference-type="eqref" reference="eq:moving-parity"} follows.

The archived multiplier law is $$\beta_k=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right],
 \qquad C_M=1.946342905200968\ldots .
 \label{eq:beta-k}$$ Hence $$\frac{\mathcal A_{k,2k}}{2k}
 =\frac{\beta^{2k}}{C_M}\{1+o(1)\}.
 \label{eq:alias-asymptotic}$$ After multiplication by $R^{2k}$, this is a constant multiple of $(\beta R)^{2k}$. The weighted parity packet divided by $2k$ is $C_*\sqrt\sigma(R/r_H)^{2k}\{1+o(1)\}$. Using $2k=\log(1/\sigma)/\log\lambda+O(1)$ gives the same exponent [\[eq:common-exponent\]](#eq:common-exponent){reference-type="eqref" reference="eq:common-exponent"}.

# Clock phase and a scalar-only obstruction

The bounded integer phase must be retained: $$\eta_\sigma
 =k_\sigma-\frac{\log(1/\sigma)}{2\log\lambda}.
 \label{eq:phase}$$

[\[thm:phase-law\]]{#thm:phase-law label="thm:phase-law"} Along every natural-clock sequence with bounded $\eta_\sigma$, $$\boxed{
 \frac{\mathcal P_{\sigma,2k_\sigma}}{\mathcal A_{k_\sigma,2k_\sigma}}
 =C_*C_M\lambda^{\eta_\sigma}\{1+o(1)\}.}
 \label{eq:ratio-law}$$ Consequently, along a subsequence with $\eta_\sigma\to\eta$, the ratio tends to $C_*C_M\lambda^\eta$. The leading scalar packets balance at the unique symbolic phase $$\eta_*=-\frac{\log(C_*C_M)}{\log\lambda}.
 \label{eq:balance-phase}$$

Divide [\[eq:moving-parity\]](#eq:moving-parity){reference-type="eqref" reference="eq:moving-parity"} by [\[eq:alias-asymptotic\]](#eq:alias-asymptotic){reference-type="eqref" reference="eq:alias-asymptotic"} and use $\beta^{2k}=r_H^{-2k}\lambda^{-k}$: $$\frac{\mathcal P_{\sigma,2k}}{\mathcal A_{k,2k}}
 =C_*C_M\sqrt\sigma\,\lambda^k\{1+o(1)\}.$$ Equation [\[eq:phase\]](#eq:phase){reference-type="eqref" reference="eq:phase"} makes $\sqrt\sigma\lambda^k=\lambda^{\eta_\sigma}$, proving [\[eq:ratio-law\]](#eq:ratio-law){reference-type="eqref" reference="eq:ratio-law"}. Positivity of $C_*,C_M$, and $\lambda>1$ makes the right side strictly increasing in $\eta$, so its value one has the unique solution [\[eq:balance-phase\]](#eq:balance-phase){reference-type="eqref" reference="eq:balance-phase"}.

[\[cor:conditional-obstruction\]]{#cor:conditional-obstruction label="cor:conditional-obstruction"} Put $$q_+=C_*C_M\lambda.
 \label{eq:q-plus}$$ Assume $q_+<1$, let $|\eta_\sigma|\le1$, and suppose $\mathcal T_{\sigma,2k}=o(\mathcal A_{k,2k})$. Then $$|e_{\sigma,k,2k}|
 \ge\{1-q_++o(1)\}\mathcal A_{k,2k},
 \label{eq:scalar-obstruction}$$ and this is not $o(kR^{-2k})$.

Equation [\[eq:ratio-law\]](#eq:ratio-law){reference-type="eqref" reference="eq:ratio-law"} and $|\eta_\sigma|\le1$ give $\mathcal P_{\sigma,2k}/\mathcal A_{k,2k}\le q_++o(1)$. Substitute into [\[eq:packet-form\]](#eq:packet-form){reference-type="eqref" reference="eq:packet-form"}. Finally, $$\frac{\mathcal A_{k,2k}}{kR^{-2k}}
 =\frac{2}{C_M}(\beta R)^{2k}\{1+o(1)\}\longrightarrow\infty$$ because $\beta R>1$.

This is deliberately a conditional scalar-only negative result. The repository proves the symbolic corollary but does not contain a directed interval enclosure certifying $q_+<1$. The archived decimal values make the hypothesis numerically plausible; they are not used as a rigorous inequality. Even under that hypothesis, the result does not bound the actual raw trace packet and does not prove divergence of the combined physical residual.

The same phase controls the local clearance. If the archived boundary-cycle clearance is $$\Delta_k^{\rm clr}=C_{\rm b}\lambda^{-2k}\{1+o(1)\},
 \qquad C_{\rm b}>0,
 \label{eq:clearance}$$ then $$d_{\sigma,k}:=\frac{\Delta_k^{\rm clr}}\sigma
 =C_{\rm b}\lambda^{-2\eta_\sigma}\{1+o(1)\}.
 \label{eq:clearance-phase}$$ At scalar balance, $$d_*=C_{\rm b}(C_*C_M)^2.
 \label{eq:balance-clearance}$$ Thus suppressing the clock phase would discard both the symbolic scalar balance ratio and the RH-322 entrance profile. The decimal evaluations of $C_{\rm b}$ and $d_*$ are numerical diagnostics only.

# Typed interface for the neighboring shell

RH-322--RH-324 retain the entrance clearance and the oriented affine frame $$V\sim g_d,
 \qquad U=-\alpha V-Z_1,
 \qquad W=-\lambda U+Z_2,
 \qquad (V,U,W)\text{ has orientation }(+,-,+),
 \label{eq:local-frame}$$ where $\alpha=2u_c$ and the output is compared after the center shift $\kappa_{\rm aff}d=2u_c\lambda d$. Their objects are forward probability laws of mass one. They do not yet define a signed trace observation, and RH-19 shows that the neighboring critical sibling cannot be hidden in a far Gaussian tail.

The exact handoff is therefore conditional but typed. A later theorem must construct, on the same clock, phase, coordinate frame, and Hardy normalization, a decomposition $$\mathcal T_{\sigma,2k}
 =\mathcal B_{\sigma,k}(d,\eta;V,U,W,\mathfrak t)
 +\mathcal S_{\sigma,k}(d,\eta;\mathfrak t)
 +\mathcal R_{\sigma,k}.
 \label{eq:future-decomposition}$$ Here $\mathfrak t$ is the still-missing trace observation, $\mathcal B$ is the physical boundary packet, $\mathcal S$ is the neighboring-shell packet, and $\mathcal R$ contains the second-leg, all-leg transport, and observation remainders. Combining [\[eq:future-decomposition\]](#eq:future-decomposition){reference-type="eqref" reference="eq:future-decomposition"} with [\[thm:main-identity\]](#thm:main-identity){reference-type="ref" reference="thm:main-identity"} gives the exact join $$e_{\sigma,k,2k}
 =\mathcal B_{\sigma,k}+\mathcal S_{\sigma,k}+\mathcal R_{\sigma,k}
 +\mathcal P_{\sigma,2k}-\mathcal A_{k,2k}.
 \label{eq:typed-join}$$ Consequently, if $\mathcal R_{\sigma,k}=o(kR^{-2k})$, the desired matching is equivalent to the signed condition $$\boxed{
 \mathcal B_{\sigma,k}+\mathcal S_{\sigma,k}
 =\mathcal A_{k,2k}-\mathcal P_{\sigma,2k}+o(kR^{-2k}).}
 \label{eq:shell-target}$$ Equation [\[eq:shell-target\]](#eq:shell-target){reference-type="eqref" reference="eq:shell-target"} is an interface, not a theorem that the packets on its left have been constructed.

# Reproduction and claim boundary

The reproduction code checks the exact moment split, the parity signs, the uniform Taylor bound, the clock/clearance dictionary, and the scalar balance law. Ordinary floating-point substitution of the archived decimal constants gives the following diagnostic ledger:

           $\eta$   $C_*C_M\lambda^\eta$   $C_{\rm b}\lambda^{-2\eta}$
  --------------- ---------------------- -----------------------------
             $-1$          $0.122049588$                 $1.298368749$
              $0$          $0.204869205$                 $0.460805149$
              $1$          $0.343888020$                 $0.163544745$
    $3.060914914$          $1.000000000$                 $0.019340633$

These are evaluations of proved symbolic formulas, not fitted noisy traces or directed-rounding enclosures. In particular, the table does not certify $q_+<1$, $\eta_*>1$, or the displayed clearance interval.

The exact identity combines only known algebraic packets. The phase law is symbolic, while the canonical-window obstruction is conditional on $q_+<1$ because the archived decimals are not interval certified. The paper does not identify the RH-322--RH-324 probability law with $\mathcal T_{\sigma,2k}$, control the second physical critical leg, prove all-leg phase transport, bound the weighted trace observation, include the neighboring shell, or establish [\[eq:future-decomposition\]](#eq:future-decomposition){reference-type="eqref" reference="eq:future-decomposition"}. Hence no joint first-alias trace law, full-trace replacement, or actual divergence theorem is obtained. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace formula or zeta-divisor equality, and does not imply RH.

RH-327 should now compute the neighboring-shell coupling in the typed frame of [\[eq:future-decomposition\]](#eq:future-decomposition){reference-type="eqref" reference="eq:future-decomposition"}; RH-328 may formulate the joint matching equation only after that shell and the trace observation are defined.
