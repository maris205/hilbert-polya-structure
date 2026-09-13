---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction/main.pdf"
source_sha256: "195212d26929aadfb9606c2eed932a7e25486bbb853f0a61c85ae022a63d2100"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Synchronized Determinant Prefixes and a Two-Order Orbit--Head Compensation Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-340-synchronized-determinant-prefix-and-two-order-orbit-head-compensation-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We put the weighted prefix--tail determinant criterion of RH-288 [@WangGluing2026] on the physical first-alias clock. If $L=\log(1/\sigma)$ and $k=L/(2\log\lambda)+O(1)$, the integer cut $u=4k$ is still inside the one-alias window. Reapplying the RH-282 mass-and-cap estimate at this cut, rather than identifying it with RH-282's displayed $\lceil4L\rceil$ cut, proves that both the noisy modulus-complement tail and the deterministic target tail vanish on the disk $|z|\le R$, $R=7/5$.

  On one common Hardy normalization define the direct complement prefix $P_u$, the full-trace prefix $E_u$, and the head/counterloop prefix $D_u$. The exact identity $p_n=q_n-d_n$ gives the sharp finite-sum inequality $|P_u-E_u|\le D_u$. Thus, if the head budget vanishes on the same clock, direct complement closure is equivalent to full-trace closure; the RH-330 critical extraction then reduces the remaining condition to the same-clock triple $(D_u,E_{\rm off},q_{2k}/H_k)$.

  The critical orbit atom of RH-338 and the mandatory lower sideband atom of RH-339 force two signed compensation equations at orders $2k$ and $2k-2$. Any proof that takes separate absolute values of the orbit, diffuse, and head pieces has a divergent two-atom majorant. This is a strict synchronization theorem and a scoped obstruction to a cancellation-blind route. It is not a lower bound for the fully signed prefix: the aggregate signed complements, the head budget, and $E_{\rm off}$ remain `NOT_TESTABLE`. RH-288 is not activated, Gates A--E remain false/open, and no Hilbert--Polya or Riemann-hypothesis conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Synchronized Determinant Prefixes and a\
  Two-Order Orbit--Head Compensation Obstruction
```

## Markdown 正文

# The physical cut and its two tails

Let the physical first-alias clock be the RH-337 clock [@WangClock2026]: $$\label{eq:clock}
 L=\log(1/\sigma),\qquad
 k=k_\sigma\in\mathbb N,\quad k\ge2,\qquad
 k=\frac{L}{2\log\lambda}+O(1),
 \qquad R=\frac75.$$ The common determinant cut is $$\label{eq:cut}
 u=4k,
 \qquad 2k<u\le4k.$$ The physical constants use $r_H=17/20$, $q=1/2$, and $$\label{eq:constants}
 q_*=(r_H\lambda)^{-1},\qquad
 qR=\frac7{10},\qquad
 q_*R=\frac{28}{17\lambda}<1.$$ The last strict inequality is the exact RH-262 boundary certificate [@WangBoundaryBudget2026]; RH-336 supplies the certified bound $\lambda<17/10$[@WangProjectorMass2026].

Write $\tau_{\sigma,n}$ for the modulus-complement trace in the RH-288 normalization and $a_n=a_n^{\rm num}$ for the deterministic numerator anchor. The direct complement tail and target tail at the cut are $$\begin{aligned}
 S_{\sigma,u}(R)&=\sum_{n\ge u}\frac{|\tau_{\sigma,n}|R^n}{n},
 &T_u(R)&=\sum_{n\ge u}\frac{|a_n|R^n}{n}.
 \label{eq:tails}\end{aligned}$$

[\[thm:tails\]]{#thm:tails label="thm:tails"} Under the RH-282 mass-and-cap estimate [@WangSpectralTail2026] and the RH-267/RH-268 deterministic all-order envelope [@WangUnifiedEnvelope2026; @WangSharpRadius2026], $$S_{\sigma,4k}(R)\longrightarrow0,
 \qquad T_{4k}(R)\longrightarrow0
 \quad (\sigma\downarrow0).
 \label{eq:tail-vanish}$$

RH-282 gives, for the modulus-complement sequence and every integer $n\ge2$, $$|\tau_{\sigma,n}|\le C\,\sigma^{-1}q^{n-2}
 \label{eq:mass-cap}$$ with a fixed harmless constant $C$. Hence $$S_{\sigma,4k}(R)
 \le \frac{Cq^{-2}}{1-qR}
 \frac{\sigma^{-1}(qR)^{4k}}{4k}.
 \label{eq:noisy-bound}$$ Since $k=L/(2\log\lambda)+O(1)$, $$\sigma^{-1}(qR)^{4k}
 =O\!\left(\sigma^{\delta_N}\right),
 \qquad
 \delta_N=\frac{2\log(10/7)}{\log\lambda}-1>0.
 \label{eq:noisy-exponent}$$ The strict sign follows from $\lambda<17/10<(10/7)^2$. This proves the first limit.

RH-267 gives $|a_n|<48q_*^n$ for every $n\ge2$. Therefore $$T_{4k}(R)
 \le \frac{48(q_*R)^{4k}}{4k(1-q_*R)},
 \label{eq:target-bound}$$ which tends to zero by [\[eq:constants\]](#eq:constants){reference-type="eqref" reference="eq:constants"}. The argument is a direct reapplication of the exact RH-282 mass bound at $4k$; it does not claim that the displayed RH-282 choice $\lceil4L\rceil$ is equal to $4k$.

The tail theorem closes only the two analytic tail leaves. It does not identify a physical head, a counterloop, or a signed prefix, and therefore it does not activate RH-288.

# A sharp same-clock prefix identity

Let $q_{\sigma,k,n}$ be the Hardy full-trace constituent of RH-334 [@WangObservation2026] and let $d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}$ be its noisy-head/counterloop defect. RH-334 gives the exact identity, for every finite order in the common data type, $$\label{eq:typed-identity}
 p_{\sigma,k,n}:=\tau_{\sigma,n}-a_n
 =q_{\sigma,k,n}-d_{\sigma,k,n}.$$ Define the three nonnegative finite budgets $$\begin{aligned}
 P_u(R)&=\sum_{2\le n<u}\frac{|p_{\sigma,k,n}|R^n}{n},
 &E_u(R)&=\sum_{2\le n<u}\frac{|q_{\sigma,k,n}|R^n}{n},
 &D_u(R)&=\sum_{2\le n<u}\frac{|d_{\sigma,k,n}|R^n}{n}.
 \label{eq:budgets}\end{aligned}$$

[\[thm:synchronization\]]{#thm:synchronization label="thm:synchronization"} For every finite common cut $u$ and radius $R$, $$\label{eq:sharp-triangle}
 \bigl|P_u(R)-E_u(R)\bigr|\le D_u(R).$$ Consequently, on any common moving clock, $$\label{eq:equiv}
 D_u(R)\to0
 \quad\Longrightarrow\quad
 \left(P_u(R)\to0\ \Longleftrightarrow\ E_u(R)\to0\right).$$

For each order, [\[eq:typed-identity\]](#eq:typed-identity){reference-type="eqref" reference="eq:typed-identity"} and the reverse triangle inequality give $$\bigl||p_{\sigma,k,n}|-|q_{\sigma,k,n}|\bigr|
 \le |d_{\sigma,k,n}|.$$ Multiply by $R^n/n$ and sum over the finite set $2\le n<u$. This is [\[eq:sharp-triangle\]](#eq:sharp-triangle){reference-type="eqref" reference="eq:sharp-triangle"}. If $D_u\to0$, the difference of the two nonnegative budgets tends to zero, proving [\[eq:equiv\]](#eq:equiv){reference-type="eqref" reference="eq:equiv"}.

For the one-alias cut [\[eq:cut\]](#eq:cut){reference-type="eqref" reference="eq:cut"}, RH-330 isolates the critical order [@WangTransfer2026]: $$\label{eq:eoff}
 E_u(R)=E_{{\rm off},u}(R)
 +\frac{|q_{\sigma,k,2k}|}{2H_k},
 \qquad H_k=kR^{-2k},
 \quad u=4k.$$ Combining [\[eq:equiv\]](#eq:equiv){reference-type="eqref" reference="eq:equiv"} and [\[eq:eoff\]](#eq:eoff){reference-type="eqref" reference="eq:eoff"} gives the exact conditional three-budget criterion $$\label{eq:three-budget}
 D_u\to0\ \text{and}\ P_u\to0
 \quad\Longleftrightarrow\quad
 D_u\to0,\quad E_{{\rm off},u}\to0,\quad
 q_{\sigma,k,2k}=o(H_k).$$ This is a same-clock statement; it permits no splice of a head estimate, critical estimate, and off-alias estimate taken on different clocks.

[\[cor:det-reduction\]]{#cor:det-reduction label="cor:det-reduction"} At $u=4k$, the two tails in Theorem [\[thm:tails\]](#thm:tails){reference-type="ref" reference="thm:tails"} vanish. Hence the RH-288 determinant quotient would converge uniformly on $|z|\le R$ if the left-hand side of [\[eq:three-budget\]](#eq:three-budget){reference-type="eqref" reference="eq:three-budget"} were proved. The repository does not prove those prefix budgets, so RH-288 remains inactive.

# Two mandatory orbit atoms

The critical boundary orbit of RH-338 gives a signed far subledger [@WangFarAtom2026] $$\label{eq:critical-scale}
 \mathcal R_{k,\rm orb}=-D_k^{\rm orb},
 \qquad
 \frac{D_k^{\rm orb}}{H_k}\to+\infty,
 \qquad
 D_k^{\rm orb}/H_k
 =\frac2{C_M}(\beta R)^{2k}(1+o(1)),$$ where $\beta R>1$ is the exact RH-336 certificate [@WangFarAtom2026; @WangProjectorMass2026]. Put $$C_k^0:=q_{\sigma,k,2k}+D_k^{\rm orb}.
 \label{eq:C0}$$

The mandatory lower sideband of RH-339 has $m=k-1$ [@WangSidebandAtom2026] and $$\label{eq:lower-atom}
 \mathcal R_{k,-,\rm orb}=-D_m^{\rm orb},
 \qquad
 \frac{D_m^{\rm orb}}{H_m}
 =\frac2{C_M}(\beta R)^{2m}(1+o(1))\to+\infty,
 \qquad H_m=mR^{-2m}.$$ Put $$C_k^-:=q_{\sigma,k,2m}+D_m^{\rm orb}.
 \label{eq:Cminus}$$ Both $2k$ and $2m=2k-2$ occur in the prefix $2\le n<u$.

[\[thm:two-order\]]{#thm:two-order label="thm:two-order"} If the direct complement prefix satisfies $P_{4k}(R)\to0$, then $$\begin{aligned}
 C_k^0-d_{\sigma,k,2k}
 &=D_k^{\rm orb}+o(H_k),
 \label{eq:critical-compensation}\\
 C_k^- -d_{\sigma,k,2m}
 &=D_m^{\rm orb}+o(H_m).
 \label{eq:lower-compensation}\end{aligned}$$ The required relative precisions are respectively $$\label{eq:relative-precision}
 o\!\left((\beta R)^{-2k}\right),
 \qquad
 o\!\left((\beta R)^{-2(k-1)}\right).$$ If in addition $D_{4k}(R)\to0$, the head terms in [\[eq:critical-compensation\]](#eq:critical-compensation){reference-type="eqref" reference="eq:critical-compensation"}--[\[eq:lower-compensation\]](#eq:lower-compensation){reference-type="eqref" reference="eq:lower-compensation"} are themselves $o(H_k)$ and $o(H_m)$, so both diffuse complements must pay their orbit atoms internally.

By [\[eq:typed-identity\]](#eq:typed-identity){reference-type="eqref" reference="eq:typed-identity"}, [\[eq:C0\]](#eq:C0){reference-type="eqref" reference="eq:C0"}, and [\[eq:Cminus\]](#eq:Cminus){reference-type="eqref" reference="eq:Cminus"}, $$\begin{aligned}
 p_{\sigma,k,2k}&=-D_k^{\rm orb}+C_k^0-d_{\sigma,k,2k},\\
 p_{\sigma,k,2m}&=-D_m^{\rm orb}+C_k^- -d_{\sigma,k,2m}.\end{aligned}$$ Since both orders occur in the nonnegative prefix, $$\label{eq:two-term-lower}
 P_{4k}(R)\ge
 \frac{|p_{\sigma,k,2k}|}{2H_k}
 +\frac{|p_{\sigma,k,2m}|}{2H_m}.$$ If the left side tends to zero, each numerator is respectively $o(H_k)$ and $o(H_m)$, which gives [\[eq:critical-compensation\]](#eq:critical-compensation){reference-type="eqref" reference="eq:critical-compensation"} and [\[eq:lower-compensation\]](#eq:lower-compensation){reference-type="eqref" reference="eq:lower-compensation"}. Division by the asymptotics in [\[eq:critical-scale\]](#eq:critical-scale){reference-type="eqref" reference="eq:critical-scale"} and [\[eq:lower-atom\]](#eq:lower-atom){reference-type="eqref" reference="eq:lower-atom"} gives [\[eq:relative-precision\]](#eq:relative-precision){reference-type="eqref" reference="eq:relative-precision"}. Finally, $D_{4k}\to0$ implies each displayed head summand is $o(H_k)$ or $o(H_m)$ by nonnegativity of $D_{4k}$.

[\[prop:absolute\]]{#prop:absolute label="prop:absolute"} Any proof that takes separate absolute values of the two orbit atoms before their signed diffuse/head complements contains the atom submajorant $$\label{eq:majorant}
 \frac{D_k^{\rm orb}}{2H_k}+\frac{D_m^{\rm orb}}{2H_m}
 =\frac1{C_M}\left((\beta R)^{2k}+(\beta R)^{2k-2}\right)(1+o(1))
 \longrightarrow+\infty.$$ This proposition does not lower-bound $P_{4k}$ or $E_{{\rm off},4k}$: a fully signed complement may still cancel both atoms.

Insert [\[eq:critical-scale\]](#eq:critical-scale){reference-type="eqref" reference="eq:critical-scale"} and [\[eq:lower-atom\]](#eq:lower-atom){reference-type="eqref" reference="eq:lower-atom"} into the two weighted atom terms. Since $\beta R>1$, the sum diverges. The final scope statement follows because the complements in [\[eq:C0\]](#eq:C0){reference-type="eqref" reference="eq:C0"} and [\[eq:Cminus\]](#eq:Cminus){reference-type="eqref" reference="eq:Cminus"} retain their signs.

# Executable audit and claim boundary

The artifact evaluates the exact cut indices and the two positive tail exponents at $k=3,5,9,17,33$. It also reports the diagnostic two-atom majorant using the printed $C_M$ value; that decimal is not an interval certificate and is not used for a theorem sign. The tests lock the one-alias window, the $2k$ and $2k-2$ orders, the deterministic result, and the claim firewall.

The maximum justified conclusion is therefore:

-   the analytic tails can be synchronized at $u=4k$ by direct corollaries of existing bounds;

-   same-clock head closure makes direct and full-trace prefix closure equivalent, with the exact critical/off-alias extraction;

-   the two physical orbit atoms impose the necessary signed laws above, and cancellation-blind absolute splitting is impossible;

-   no moving-order signed complement or head estimate is available, so aggregate prefix closure and nonclosure are both `NOT_TESTABLE`.

No physical determinant gluing is activated. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt trace or completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
