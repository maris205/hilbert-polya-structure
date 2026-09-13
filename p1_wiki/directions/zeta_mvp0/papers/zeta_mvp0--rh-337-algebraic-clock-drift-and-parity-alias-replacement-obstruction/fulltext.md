---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction/main.pdf"
source_sha256: "225554606ade153067a18913a81907f413e5d1e4bc37c3be5dcd90d5fd53b425"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Algebraic Clock Drift and a Parity--Alias Replacement Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-337-algebraic-clock-drift-and-parity-alias-replacement-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The exact-rational comparator of RH-329 freezes the exponential clock $\sigma_k=\widehat\Lambda^{-2k}$, where $\widehat\Lambda=2098216888035403/1250000000000000$. We prove that this clock is not the physical fixed-phase clock. The physical expansion rate is the unique positive root of $p(x)=x^3+4x^2-16$, and exact rational arithmetic gives $p(\widehat\Lambda)>0$; hence $\widehat\Lambda>\lambda$ and the physical phase tends to $-\infty$. Directly from the uniform parity remainder and the physical multiplier law, we derive an off-phase trichotomy valid for every clock $\sigma_k=\Lambda_c^{-2k}$ with $\Lambda_c>1$. On the RH-329 clock the physical alias packet dominates both the physical parity packet and the two hatted model packets exponentially. The resulting scalar parity--alias comparator defect divided by the physical alias packet tends to $-1$, and divided by the target $H_k=kR^{-2k}$ tends to $-\infty$. This rejects RH-329 only as a physical bounded-phase parity--alias comparator. It is not an actual full-trace divergence theorem and does not activate the fixed-phase transfer theorem of RH-330. Replacing the clock by the exact physical $\lambda$ leaves target-scale replacement not testable: the archived relative $o(1)$ laws do not supply the exponentially sharper remainder $o((\beta R)^{-2k})$. No determinant gate or Riemann-hypothesis conclusion is obtained.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Algebraic Clock Drift and a Parity--Alias\
  Replacement Obstruction
```

## Markdown 正文

# Physical and hatted clocks

Let $u_c\in(1,2)$ be the physical parameter and put $$\label{eq:lambda-from-u}
 \lambda=2u_c(u_c-1)>1.$$ The algebraic identities of the gauge-fixed physical observation source give $$\label{eq:physical-polynomial}
 p(\lambda)=0,
 \qquad p(x)=x^3+4x^2-16$$ [@WangObservation2026]. The RH-329 model instead defines the exact rational constant $$\label{eq:Lambda-hat}
 \widehat\Lambda=\frac{2098216888035403}{1250000000000000}$$ and freezes $\sigma_k=\widehat\Lambda^{-2k}$ for integers $k\ge2$ [@WangIsolatedAudit2026]. The hat is part of the model type. It is not an interval enclosure for the physical root.

For an arbitrary clock base $\Lambda_c>1$, define $$\label{eq:clock-and-phase}
 \sigma_k=\Lambda_c^{-2k},
 \qquad
 \eta_k=k-\frac{\log(1/\sigma_k)}{2\log\lambda}
 =k\left(1-\frac{\log\Lambda_c}{\log\lambda}\right).$$ Only $\Lambda_c=\lambda$ has bounded phase. This observation must be proved exactly for a proposed algebraic comparator; closeness of printed decimals is irrelevant.

[\[thm:clock-mismatch\]]{#thm:clock-mismatch label="thm:clock-mismatch"} The polynomial $p$ has one positive root $\lambda\in(1,2)$ and $$\label{eq:exact-residual}
 p(\widehat\Lambda)=
 \frac{5765081705833725291502719395827}
 {1953125000000000000000000000000000000000000000}>0.$$ Consequently $\widehat\Lambda>\lambda$, and on the RH-329 clock $$\label{eq:eta-minus-infinity}
 \eta_k=k\left(1-\frac{\log\widehat\Lambda}{\log\lambda}\right)
 \longrightarrow-\infty.$$

We have $p(1)=-11$, $p(2)=8$, and $$p'(x)=3x^2+8x=x(3x+8)>0\qquad(x>0).$$ Thus $p$ has a unique positive root in $(1,2)$. Direct rational evaluation at [\[eq:Lambda-hat\]](#eq:Lambda-hat){reference-type="eqref" reference="eq:Lambda-hat"} gives [\[eq:exact-residual\]](#eq:exact-residual){reference-type="eqref" reference="eq:exact-residual"}. Since $1<\widehat\Lambda<2$ and $p$ is strictly increasing there, $\widehat\Lambda>\lambda$. The coefficient of $k$ in [\[eq:eta-minus-infinity\]](#eq:eta-minus-infinity){reference-type="eqref" reference="eq:eta-minus-infinity"} is therefore strictly negative.

High-precision substitution gives the diagnostic values $$\begin{aligned}
 \lambda&=1.6785735104283222651037051293\ldots,\nonumber\\
 \widehat\Lambda-\lambda&=1.3489629487069342\ldots\times10^{-16},\nonumber\\
 1-\frac{\log\widehat\Lambda}{\log\lambda}
 &=-1.5515885691166900\ldots\times10^{-16}.
 \label{eq:diagnostics}\end{aligned}$$ These decimals reproduce the size of the drift; only [\[eq:exact-residual\]](#eq:exact-residual){reference-type="eqref" reference="eq:exact-residual"} certifies its sign.

# Off-phase parity--alias trichotomy

Retain the physical constants and packet laws of RH-326--RH-328 [@WangFirstAlias2026; @WangMatching2026]. Namely, $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad R=\frac75,\qquad
 \beta=\frac1{r_H\sqrt\lambda},$$ $$\label{eq:physical-laws}
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma),
 \qquad
 \beta_k=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right],
 \qquad C_*,C_M>0.$$ At even order $2k$, the positive parity and alias packets are $$\begin{aligned}
 \mathcal P_k^{\rm route}
 &=r_H^{-2k}\{1-(1-\delta_{\sigma_k})^{2k}\},
 \label{eq:route-parity}\\
 \mathcal A_k^{\rm route}
 &=(2k-2)\beta_k^{2k}+2\beta^{2k}.
 \label{eq:route-alias}\end{aligned}$$ Their signs in the five-slot coefficient are $+\mathcal P-\mathcal A$. The target scale is $$\label{eq:target}
 H_k=kR^{-2k}.$$

The bounded-phase ratio theorem of RH-326 cannot be cited when $|\eta_k|\to\infty$. The next result instead starts from its uniform binomial inequality, valid for every $k$ and $0\le\delta<1$.

[\[thm:trichotomy\]]{#thm:trichotomy label="thm:trichotomy"} For every fixed $\Lambda_c>1$ and the clock $\sigma_k=\Lambda_c^{-2k}$, $$\begin{aligned}
 \mathcal P_k^{\rm route}
 &=2kC_*r_H^{-2k}\Lambda_c^{-k}\{1+o(1)\},
 \label{eq:P-asymptotic}\\
 \mathcal A_k^{\rm route}
 &=\frac{2k}{C_M}r_H^{-2k}\lambda^{-k}\{1+o(1)\},
 \label{eq:A-asymptotic}\\
 \frac{\mathcal P_k^{\rm route}}{\mathcal A_k^{\rm route}}
 &=C_*C_M\left(\frac{\lambda}{\Lambda_c}\right)^k
 \{1+o(1)\}.
 \label{eq:ratio-trichotomy}\end{aligned}$$ Hence the alias packet dominates exponentially if $\Lambda_c>\lambda$, a finite nonzero leading balance is possible if $\Lambda_c=\lambda$, and the parity packet dominates exponentially if $1<\Lambda_c<\lambda$.

On the stated clock, $$\delta_{\sigma_k}=C_*\Lambda_c^{-k}\{1+o(1)\},
 \qquad k\delta_{\sigma_k}\longrightarrow0.$$ The uniform parity remainder from RH-326 is $$\left|1-(1-\delta)^{2k}-2k\delta\right|
 \le k(2k-1)\delta^2.$$ After division by $2k\delta$, its right side is $O(k\delta)=o(1)$, proving [\[eq:P-asymptotic\]](#eq:P-asymptotic){reference-type="eqref" reference="eq:P-asymptotic"}. The multiplier law gives $$\beta_k^{2k}=\frac{\beta^{2k}}{C_M}\{1+o(1)\}.$$ Since $\beta^{2k}=r_H^{-2k}\lambda^{-k}$, the $2\beta^{2k}$ endpoint term is lower by a factor $O(k^{-1})$, and [\[eq:A-asymptotic\]](#eq:A-asymptotic){reference-type="eqref" reference="eq:A-asymptotic"} follows. Division proves [\[eq:ratio-trichotomy\]](#eq:ratio-trichotomy){reference-type="eqref" reference="eq:ratio-trichotomy"}; the three cases follow from the strict ordering of positive clock bases.

# Failure of the hatted fixed-phase comparator

The RH-329 comparator defines the exact model constants $$\label{eq:hatted-constants}
 \widehat C_M=\frac{9731714526004839}{5000000000000000},
 \qquad
 \widehat C_* =\frac{26314633984227}{250000000000000}$$ and $$\label{eq:hatted-packets}
 \widehat\beta^2=\frac1{r_H^2\widehat\Lambda},
 \quad
 \widehat\mathcal A_k=\left(\frac{2k-2}{\widehat C_M}+2\right)\widehat\beta^{2k},
 \quad
 \widehat\mathcal P_k=r_H^{-2k}
 \left\{1-(1-\widehat C_*\widehat\Lambda^{-k})^{2k}\right\}.$$ Again, these are model definitions, not physical interval data. Compare only the parity--alias scalar, with the RH-330 actual-minus-model sign convention: $$\label{eq:D-def}
 D_k=(\mathcal P_k^{\rm route}-\widehat\mathcal P_k)
 -(\mathcal A_k^{\rm route}-\widehat\mathcal A_k),
 \qquad \sigma_k=\widehat\Lambda^{-2k}.$$

[\[thm:comparator-obstruction\]]{#thm:comparator-obstruction label="thm:comparator-obstruction"} On the RH-329 clock, $$\label{eq:D-over-A}
 \frac{D_k}{\mathcal A_k^{\rm route}}\longrightarrow-1.$$ Moreover, $$\label{eq:A-and-D-over-H}
 \frac{\mathcal A_k^{\rm route}}{H_k}\longrightarrow+\infty,
 \qquad
 \frac{D_k}{H_k}\longrightarrow-\infty.$$ Thus RH-329 is not a physical bounded-phase parity--alias comparator.

By [\[thm:trichotomy\]](#thm:trichotomy){reference-type="ref" reference="thm:trichotomy"} and $\widehat\Lambda>\lambda$, $$\mathcal P_k^{\rm route}
 =O\!\left(k r_H^{-2k}\widehat\Lambda^{-k}\right)
 =o(\mathcal A_k^{\rm route}).$$ The same uniform binomial upper bound and the exact formulas [\[eq:hatted-packets\]](#eq:hatted-packets){reference-type="eqref" reference="eq:hatted-packets"} give $$\widehat\mathcal P_k+\widehat\mathcal A_k
 =O\!\left(k r_H^{-2k}\widehat\Lambda^{-k}\right)
 =o(\mathcal A_k^{\rm route}).$$ Expanding [\[eq:D-def\]](#eq:D-def){reference-type="eqref" reference="eq:D-def"} therefore leaves $D_k=-\mathcal A_k^{\rm route}\{1+o(1)\}$, proving [\[eq:D-over-A\]](#eq:D-over-A){reference-type="eqref" reference="eq:D-over-A"}.

Next, [\[eq:A-asymptotic\]](#eq:A-asymptotic){reference-type="eqref" reference="eq:A-asymptotic"} and [\[eq:target\]](#eq:target){reference-type="eqref" reference="eq:target"} give $$\label{eq:A-over-H-proof}
 \frac{\mathcal A_k^{\rm route}}{H_k}
 =\frac{2}{C_M}\left(\frac{R^2}{r_H^2\lambda}\right)^k
 \{1+o(1)\}
 =\frac{2}{C_M}(\beta R)^{2k}\{1+o(1)\}.$$ The exact certificate $\beta R>1$ is established in RH-336 [@WangProjectorMass2026], so the first limit in [\[eq:A-and-D-over-H\]](#eq:A-and-D-over-H){reference-type="eqref" reference="eq:A-and-D-over-H"} follows. Multiplying it by [\[eq:D-over-A\]](#eq:D-over-A){reference-type="eqref" reference="eq:D-over-A"} proves the second.

$D_k$ contains only the parity and alias replacement defects. It is not the complete signed replacement aggregate $\Delta\mathcal B+\Delta\mathcal S+\Delta\mathcal R+
\Delta\mathcal P-\Delta\mathcal A$, not the actual five-slot coefficient, and not a full-trace residual. The boundary, shell, and far slots could still contribute at the same or larger scale. In addition, the sharp transfer theorem of RH-330 assumes one common bounded-phase clock [@WangTransfer2026]; [\[thm:clock-mismatch\]](#thm:clock-mismatch){reference-type="ref" reference="thm:clock-mismatch"} proves that hypothesis false for the RH-329 clock. We therefore do not use that theorem to promote [\[eq:A-and-D-over-H\]](#eq:A-and-D-over-H){reference-type="eqref" reference="eq:A-and-D-over-H"}.

# Correct-clock target-resolution barrier

It is natural to replace $\widehat\Lambda$ by the exact physical $\lambda$. On that corrected clock, [\[thm:trichotomy\]](#thm:trichotomy){reference-type="ref" reference="thm:trichotomy"} removes the exponential parity--alias mismatch, but it does not prove target-scale replacement.

[\[prop:not-testable\]]{#prop:not-testable label="prop:not-testable"} On the correct clock $\sigma_k=\lambda^{-2k}$, $$\label{eq:H-over-A}
 \frac{H_k}{\mathcal A_k^{\rm route}}
 =\frac{C_M}{2}(\beta R)^{-2k}\{1+o(1)\}.$$ Consequently a relative parity--alias replacement estimate sufficient for an $o(H_k)$ scalar defect must be $$\label{eq:required-precision}
 o\!\left(\frac{H_k}{\mathcal A_k^{\rm route}}\right)
 =o\!\left((\beta R)^{-2k}\right).$$ The archived laws [\[eq:physical-laws\]](#eq:physical-laws){reference-type="eqref" reference="eq:physical-laws"} provide only relative $o(1)$ remainders. They neither imply nor refute [\[eq:required-precision\]](#eq:required-precision){reference-type="eqref" reference="eq:required-precision"}; the correct-clock physical replacement is therefore `NOT_TESTABLE` from the present inputs.

Equation [\[eq:H-over-A\]](#eq:H-over-A){reference-type="eqref" reference="eq:H-over-A"} is the reciprocal of [\[eq:A-over-H-proof\]](#eq:A-over-H-proof){reference-type="eqref" reference="eq:A-over-H-proof"}. Since $\beta R>1$, the right side tends to zero exponentially. A bare relative $o(1)$ remainder has no specified rate and does not imply an exponentially weighted little-oh estimate. No lower bound in the archived source proves that such an estimate is impossible, so only the stated insufficiency verdict is justified.

This barrier is the same target-resolution issue isolated for the physical shell in RH-327 and the matching equation in RH-328 [@WangShellBudget2026; @WangMatching2026]. It must not be replaced by a finite fit of $C_*$, $C_M$, or $\lambda$.

# Reproduction protocol and claim boundary

The executable artifact evaluates the polynomial residual, hatted constants, finite model packets, and binomial enclosures with exact rational arithmetic. It separately prints high-precision clock diagnostics. The finite rows $k\in\{2,3,4,6\}$ reproduce exact formulas only; they do not certify any moving-order physical asymptotic. The tests lock the exact root ordering, model types, packet bounds, sign convention, target barrier, and the complete claim firewall.

The maximum conclusion is scoped: the RH-329 hatted clock is off the physical bounded-phase route, and its scalar parity--alias comparison has the limits in [\[thm:comparator-obstruction\]](#thm:comparator-obstruction){reference-type="ref" reference="thm:comparator-obstruction"}. No result here estimates the physical boundary/shell aggregate or signed far remainder, proves off-alias convergence, transports the noisy head, glues a determinant, or proves actual full-trace divergence. No Hilbert--Polya operator is constructed, no Riemann zero or von Mangoldt trace is identified, no completed-zeta divisor equality is proved, and no implication for the Riemann hypothesis is asserted. Gates A--E remain false/open.
