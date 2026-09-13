---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-345-double-alias-parity-phase-compensation-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction/main.pdf"
source_sha256: "aecf73084c9782839edcc56e3948d214f323d4567e0d7dd488fa339799526cd7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Double-Alias Parity-Phase Obstruction at the Critical Order

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-345-double-alias-parity-phase-compensation-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-344 completes the physical boundary-orbit extraction at the first alias and gives $$p_{\sigma,k,2k}=Y_k+\mathcal P_{\sigma,2k}-S_k,
   \qquad
   Y_k=\mathcal T_k^{\rm rest}-d_{\sigma,k,2k},
   \qquad
   S_k=\mathcal A_{k,2k}+F_k^{\rm orb}.$$ Here $S_k/\mathcal A_{k,2k}\to2$ and $\mathcal A_{k,2k}/H_k\to\infty$. Combining this with the actual RH-326 phase law $$\frac{\mathcal P_{\sigma,2k}}{\mathcal A_{k,2k}}
   =C_*C_M\lambda^{\eta_\sigma}\{1+o(1)\}$$ shifts the scalar balance from one alias packet to two. The unique symbolic phase is $$\eta_2=\frac{\log(2/(C_*C_M))}{\log\lambda}.$$ If the actual orbit-free remainder satisfies $Y_k=o(H_k)$, then every fixed phase other than $\eta_2$ has a divergent critical weighted contribution. This is a conditional physical obstruction, not aggregate nonclosure.

  At $\eta_2$, the proved relative $o(1)$ phase law remains exponentially too weak for the necessary relative precision $o((\beta R)^{-2k})$. We prove an exact scalar information-class theorem. Two parity eigenvalue sequences of the form $\lambda_{-,k}=-(1-\delta_k)$ both satisfy $\delta_k=C_*\sqrt{\sigma_k}\{1+o(1)\}$ and the exact even parity-packet formula. One makes the critical scalar residual zero; the other leaves $\mathcal A_{k,2k}/k$, whose weighted contribution diverges. These scalar sequences are not two noisy operators. Actual signed compensation, the strict prefix, determinant gluing, and Gates A--E remain open. No Riemann-hypothesis conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'A Double-Alias Parity-Phase Obstruction at the Critical Order'
```

## Markdown 正文

# The complete critical scalar ledger

Use the physical natural clock and target $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad
 \eta_\sigma=k-\frac{\log(1/\sigma)}{2\log\lambda},\qquad
 H_k=kR^{-2k},\quad R=\frac75.$$ RH-344 gives the exact direct critical coefficient $$\label{eq:critical}
 p_{\sigma,k,2k}=Y_k+\mathcal P_{\sigma,2k}-S_k,
 \qquad
 Y_k=\mathcal T_k^{\rm rest}-d_{\sigma,k,2k},
 \qquad
 S_k=\mathcal A_{k,2k}+F_k^{\rm orb}.$$ The two positive deterministic packets obey $$\begin{aligned}
 \mathcal A_{k,2k}
 &=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},
 \label{eq:A-scale}\\
 F_k^{\rm orb}
 &=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},
 \label{eq:F-scale}\end{aligned}$$ where $\beta=(r_H\sqrt\lambda)^{-1}$ and $\beta R>1$. Therefore $$\begin{aligned}
 \frac{S_k}{\mathcal A_{k,2k}}&\longrightarrow2,
 \label{eq:S-over-A}\\
 S_k&=\frac{4k}{C_M}\beta^{2k}\{1+o(1)\},
 \qquad
 \frac{S_k}{H_k}=\frac4{C_M}(\beta R)^{2k}\{1+o(1)\}
 \longrightarrow\infty.
 \label{eq:S-scale}\end{aligned}$$ These are exact physical deterministic constituents. No assumption has yet been made about the signed orbit-free remainder $Y_k$ [@WangCompleteOrbit2026].

The actual parity eigenvalue satisfies the square-root boundary-layer law $$\label{eq:delta}
 \lambda_-(\sigma)=-(1-\delta_\sigma),\qquad
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma),\qquad C_*>0,$$ and its even packet is $$\label{eq:P}
 \mathcal P_{\sigma,2k}=r_H^{-2k}\{1-(1-\delta_\sigma)^{2k}\}.$$ RH-326 proves, for bounded physical phase, $$\label{eq:phase-law}
 \frac{\mathcal P_{\sigma,2k}}{\mathcal A_{k,2k}}
 =C_*C_M\lambda^{\eta_\sigma}\{1+o(1)\}$$ [@WangParityBoundary2026; @WangFirstAlias2026].

# Off-balance scalar obstruction

Put $$\label{eq:gamma}
 \gamma(\eta)=C_*C_M\lambda^\eta.$$ Since $\lambda>1$, $\gamma$ is strictly increasing. The complete scalar demand has the unique leading balance phase $$\label{eq:eta-two}
 \boxed{\eta_2=\frac{\log(2/(C_*C_M))}{\log\lambda}},
 \qquad \gamma(\eta_2)=2.$$ This differs from the single-alias equation $\gamma=1$ because the complete raw orbit contributes the second alias-sized packet.

[\[thm:off-balance\]]{#thm:off-balance label="thm:off-balance"} Consider an actual physical sequence with bounded phase $\eta_\sigma\to\eta$. If $$\label{eq:Y-small}
 Y_k=o(H_k)$$ and $\eta\ne\eta_2$, then $$\label{eq:divergence}
 \frac{|p_{\sigma,k,2k}|}{2H_k}\longrightarrow\infty.$$ More precisely, $$\label{eq:divergence-rate}
 \frac{|p_{\sigma,k,2k}|}{2H_k}
 =\frac{|\gamma(\eta)-2|}{C_M}
 (\beta R)^{2k}\{1+o(1)\}.$$

By [\[eq:A-scale\]](#eq:A-scale){reference-type="eqref" reference="eq:A-scale"}, $H_k/\mathcal A_{k,2k}\to0$, so [\[eq:Y-small\]](#eq:Y-small){reference-type="eqref" reference="eq:Y-small"} gives $Y_k/\mathcal A_{k,2k}\to0$. Divide [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} by $\mathcal A_{k,2k}$ and use [\[eq:S-over-A\]](#eq:S-over-A){reference-type="eqref" reference="eq:S-over-A"} and [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"}: $$\frac{p_{\sigma,k,2k}}{\mathcal A_{k,2k}}
 \longrightarrow\gamma(\eta)-2\ne0.$$ Finally [\[eq:A-scale\]](#eq:A-scale){reference-type="eqref" reference="eq:A-scale"} divided by $2H_k$ gives $\mathcal A_{k,2k}/(2H_k)=C_M^{-1}(\beta R)^{2k}\{1+o(1)\}$. This proves both claims.

The hypothesis [\[eq:Y-small\]](#eq:Y-small){reference-type="eqref" reference="eq:Y-small"} is a statement about the actual signed orbit-free raw remainder and head defect. No repository theorem proves it. The theorem stops parity as a scalar-only compensation mechanism off balance; it does not stop cancellation by $Y_k$.

# The balance phase still misses target precision

At $\eta=\eta_2$, the leading ratio in [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"} equals two, but critical closure requires much more.

[\[prop:precision\]]{#prop:precision label="prop:precision"} Under $Y_k=o(H_k)$, critical closure is equivalent to $$\label{eq:scalar-match}
 \mathcal P_{\sigma,2k}=S_k+o(H_k).$$ Relative to $S_k$, the required precision is $$\label{eq:relative-precision}
 o\!\left(\frac{H_k}{S_k}\right)
 =o\!\left((\beta R)^{-2k}\right).$$ The source law [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"} supplies only relative $o(1)$ and hence does not decide [\[eq:scalar-match\]](#eq:scalar-match){reference-type="eqref" reference="eq:scalar-match"}, even at $\eta_2$.

Rearrange [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} and use $Y_k=o(H_k)$. Equation [\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"} gives [\[eq:relative-precision\]](#eq:relative-precision){reference-type="eqref" reference="eq:relative-precision"}. The final statement is the strict distinction between an unspecified vanishing relative error and the exponentially smaller target-relative error.

This proposition is not merely a warning about rates. The next theorem gives two exact scalar sequences with the same source asymptotic and opposite target behavior.

# Exact scalar underdetermination at balance

Freeze the balance-phase clock $$\label{eq:sigma-balance}
 \sigma_k=\lambda^{-2(k-\eta_2)},
 \qquad
 C_*\sqrt{\sigma_k}=\frac2{C_M}\lambda^{-k}.$$ For any desired scalar packet $0<X_k<r_H^{-2k}$, define $$\label{eq:inverse-parity}
 \delta_k(X)=1-\{1-r_H^{2k}X_k\}^{1/(2k)},
 \qquad
 \lambda_{-,k}(X)=-(1-\delta_k(X)).$$ Then $\lambda_{-,k}(X)\in(-1,0)$ and its exact even parity packet is $X_k$.

[\[thm:scalar-completions\]]{#thm:scalar-completions label="thm:scalar-completions"} For all sufficiently large $k$, let $$\label{eq:two-packets}
 X_k^{\rm close}=S_k,
 \qquad
 X_k^{\rm far}=S_k+\frac{\mathcal A_{k,2k}}k.$$ The two sequences [\[eq:inverse-parity\]](#eq:inverse-parity){reference-type="eqref" reference="eq:inverse-parity"} satisfy the same square-root law $$\label{eq:common-delta}
 \delta_k(X^{\rm close})
 =C_*\sqrt{\sigma_k}\{1+o(1)\},
 \qquad
 \delta_k(X^{\rm far})
 =C_*\sqrt{\sigma_k}\{1+o(1)\}.$$ In the scalar information class with $Y_k=0$, the close sequence has $p_{\sigma,k,2k}=0$, while the far sequence has $$\label{eq:far-residual}
 p_{\sigma,k,2k}=\frac{\mathcal A_{k,2k}}k,
 \qquad
 \frac{|p_{\sigma,k,2k}|}{2H_k}
 =\frac1{C_Mk}(\beta R)^{2k}\{1+o(1)\}
 \longrightarrow\infty.$$

By [\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"}, $r_H^{2k}X_k^{\rm close}=O(k\lambda^{-k})\to0$; the far correction is smaller by a factor $O(k^{-1})$. Hence both desired packets lie in the domain of [\[eq:inverse-parity\]](#eq:inverse-parity){reference-type="eqref" reference="eq:inverse-parity"} eventually. For $x_k=r_H^{2k}X_k\to0$, $$\label{eq:root-expansion}
 1-(1-x_k)^{1/(2k)}=\frac{x_k}{2k}\{1+o(1)\}.$$ Equations [\[eq:A-scale\]](#eq:A-scale){reference-type="eqref" reference="eq:A-scale"}--[\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"} give, for both choices, $$\frac{r_H^{2k}X_k}{2k}
 =\frac2{C_M}\lambda^{-k}\{1+o(1)\}
 =C_*\sqrt{\sigma_k}\{1+o(1)\},$$ which proves [\[eq:common-delta\]](#eq:common-delta){reference-type="eqref" reference="eq:common-delta"}. Substituting the two exact packets into [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} with $Y_k=0$ gives zero and $\mathcal A_{k,2k}/k$. Divide the latter by $2H_k$ and use [\[eq:A-scale\]](#eq:A-scale){reference-type="eqref" reference="eq:A-scale"}.

Equation [\[eq:inverse-parity\]](#eq:inverse-parity){reference-type="eqref" reference="eq:inverse-parity"} constructs scalar eigenvalue sequences, not noisy transfer operators. It proves that the exact parity-packet form and the leading physical square-root law do not determine target closure at the balance phase. It does not replace the actual $\lambda_-(\sigma)$ or construct two physical orbit-free remainders.

# Protocol, verdict, and next physical route

The executable artifact evaluates the exact inverse parity map at $k=8,16,24,32$, verifies both packet recoveries, checks the common leading square-root ratio, and records the growing far weighted residual. Archived decimals for $C_*$ and $C_M$ are reproduction inputs only, not interval certificates or theorem evidence.

The scalar-only critical route is therefore `STOP_SCOPED`: off the unique double-alias phase it fails under a target-negligible actual remainder, and at the balance phase the source scalar information admits opposite exact target behaviors. Actual signed critical compensation remains `NOT_TESTABLE`/open because $Y_k$ is not estimated.

The next physical layer is the order-$2k-2$ lower-sideband decomposition. It must retain the same noise clock, freeze the actual cells before evaluation, and extract the complete period-$2(k-1)$ boundary orbit before testing any scalar mechanism. Closing one selected order would still not close the remaining off-alias prefix [@WangSynchronizedPrefix2026].

RH-288 remains inactive and the RH-341 frontier is not promoted [@WangActualFrontier2026]. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
