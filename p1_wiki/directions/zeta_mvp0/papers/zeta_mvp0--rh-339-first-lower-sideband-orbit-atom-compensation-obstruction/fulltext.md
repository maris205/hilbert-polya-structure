---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-339-first-lower-sideband-orbit-atom-compensation-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction/main.pdf"
source_sha256: "2e9e3758e5427c10ccc513c5b02619f35477623b1f91a841f22a73234048699f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A First-Lower-Sideband Orbit Atom and a Mandatory Compensation Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-339-first-lower-sideband-orbit-atom-compensation-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The one-alias off-background of RH-330 contains every coefficient below the critical order $2k$ except the critical coefficient itself. We prove that the first lower even sideband $n_-=2k-2$ already contains an alias-scale physical boundary-orbit atom. The primitive period-$2(k-1)$ boundary orbit has a folded subset of $2k-3$ marked points in the frozen RH-334 far set. Its noisy localized trace is exactly zero, while its deterministic mass $D_{k-1}^{\rm orb}$ satisfies $$D_{k-1}^{\rm orb}/H_{k-1}\longrightarrow+\infty,
   \qquad H_{k-1}=(k-1)R^{-2(k-1)}.$$ Writing the actual typed sideband coefficient as $q_-= -D_{k-1}^{\rm orb}+C_-$, vanishing of the off-alias weighted prefix necessarily forces $C_-=D_{k-1}^{\rm orb}+o(H_{k-1})$, at relative precision $o((\beta R)^{-2(k-1)})$. Thus any proof that takes separate absolute values after the orbit/complement split fails at this mandatory sideband. This is not a positive lower bound for the fully signed coefficient: the complement may cancel the atom. The repository provides no moving-order estimate for that complement, so both off-alias vanishing and off-alias nonvanishing remain not testable. The physical counterloop radial sideband is retained without a sign claim because the printed value $C_M>1$ lacks an interval certificate. No determinant or Riemann-hypothesis conclusion is obtained.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A First-Lower-Sideband Orbit Atom and a\
  Mandatory Compensation Obstruction
```

## Markdown 正文

# Typed off-alias coefficient

Work on the physical natural clock $$\label{eq:clock}
 k=k_\sigma\in\mathbb N,\qquad k\ge2,\qquad
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad \sigma\to0,
 \qquad H_k=kR^{-2k},
 \qquad R=\frac75.$$ Choose any integer cut $$\label{eq:cut}
 2k<h_\sigma\le4k.$$ For the actual Hardy full-trace constituent $q_{\sigma,k,n}$, RH-330 defines the nonnegative off-alias prefix $$\label{eq:E-off}
 \mathcal E_{\sigma,\rm off}^{(h)}(R)
 =\sum_{\substack{2\le n<h_\sigma\\ n\ne2k}}
 \frac{|q_{\sigma,k,n}|R^n}{n}$$ [@WangTransfer2026].

We retain the corrected RH-334 folded backward-observable operator $K_\sigma$, the frozen basepoint partition $[0,1]=J^-\sqcup J^+\sqcup F$, and the localized raw slots $\mathcal B_{\sigma,k,n},\mathcal S_{\sigma,k,n},\mathcal R_{\sigma,k,n}$ [@WangObservation2026]. For every $n\ge2$, define $$\begin{aligned}
 q_{\sigma,k,n}
 &=c^H_{\sigma,n}-s_{k,n}-a_n^{\rm num},
 \label{eq:q-definition}\\
 \mathcal P_{\sigma,n}
 &=r_H^{-n}\{(-1)^n-\lambda_-(\sigma)^n\},
 \qquad r_H=\frac{17}{20},
 \label{eq:parity}\\
 \mathcal A_{k,n}&=s_{k,n}-p_n^{\rm pole}.
 \label{eq:counterloop-defect}\end{aligned}$$

[\[prop:five-slot\]]{#prop:five-slot label="prop:five-slot"} For every $n\ge2$, $$\label{eq:five-slot}
 \boxed{
 q_{\sigma,k,n}
 =\mathcal B_{\sigma,k,n}+\mathcal S_{\sigma,k,n}+\mathcal R_{\sigma,k,n}
  +\mathcal P_{\sigma,n}-\mathcal A_{k,n}.}$$ The coefficient type is the Hardy full-trace constituent, not automatically the modulus-complement coefficient.

The deterministic numerator anchor is $a_n^{\rm num}=c^H_n-p_n^{\rm pole}$. Hence $$q_{\sigma,k,n}
 =(c^H_{\sigma,n}-c^H_n)-(s_{k,n}-p_n^{\rm pole}).$$ The exact bulk split gives $$c^H_{\sigma,n}-c^H_n
 =r_H^{-n}\{\operatorname{Tr}K_\sigma^n-P_n\}+\mathcal P_{\sigma,n}.$$ RH-334 partitions the raw trace into $\mathcal B+\mathcal S+\mathcal R$ for every $n\ge2$. Substitution proves [\[eq:five-slot\]](#eq:five-slot){reference-type="eqref" reference="eq:five-slot"}. Identifying this constituent with the modulus complement would additionally require the noisy-head defect to vanish, which is not assumed here.

Set $$\label{eq:n-minus}
 n_-=2k-2=2m,
 \qquad m=k-1,
 \qquad H_m=mR^{-2m}.$$ For every admissible cut [\[eq:cut\]](#eq:cut){reference-type="eqref" reference="eq:cut"}, $2\le n_-<h_\sigma$ and $n_-\ne2k$. Therefore the corresponding summand is always present in [\[eq:E-off\]](#eq:E-off){reference-type="eqref" reference="eq:E-off"}.

At this sideband the exact RH-326 counterloop identity is $$\label{eq:radial-sideband}
 \mathcal A_{k,n_-}=2(\beta^{n_-}-\beta_k^{n_-}),
 \qquad
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},
 \qquad
 \beta=\frac1{r_H\sqrt\lambda}$$ [@WangFirstAlias2026]. RH-17 proves only $C_M>0$ analytically in $|M_k|=C_M\lambda^k(1+o(1))$. Its printed value $1.9463429052\ldots$ is not an interval certificate, so no eventual sign of [\[eq:radial-sideband\]](#eq:radial-sideband){reference-type="eqref" reference="eq:radial-sideband"} is used. Here "alias-scale" refers only to the size of the orbit atom. The lower sideband is not an alias impulse of the current period-$2k$ counterloop; [\[eq:radial-sideband\]](#eq:radial-sideband){reference-type="eqref" reference="eq:radial-sideband"} is its radial counterloop contribution.

# A physical orbit atom at $n_-=2k-2$

Let $p_{2m}$ be the primitive boundary point of physical period $2m$ and write $x_j=f^j(p_{2m})$. RH-17 supplies the ordered component chain, fixed gaps from the fold cusp $b$, and the multiplier law $$\label{eq:M-m}
 M_m=(f^{2m})'(p_{2m})=-C_M\lambda^m\{1+o(1)\}$$ [@WangBoundaryMonodromy2026]. Define $$\label{eq:Omega-m}
 \Omega_m=\{|x_j|:0\le j<2m,\ j\ne2m-2\}.$$

[\[thm:sideband-atom\]]{#thm:sideband-atom label="thm:sideband-atom"} For every fixed RH-334 window parameter $A>0$ and all sufficiently large $k$, $$\label{eq:Omega-sideband-F}
 \Omega_m\subset F_{\sigma,k,A},
 \qquad |\Omega_m|=2m-1=2k-3.$$ Define $$\label{eq:D-m}
 D_m^{\rm orb}
 =r_H^{-2m}\frac{2m-1}{1+|M_m|}>0.$$ Then the localized sideband far subledger is exactly $$\label{eq:R-orb-minus}
 \mathcal R_{k,-}^{\rm orb}
 :=r_H^{-2m}\{L_{\sigma,2m}(\Omega_m)
              -P_{2m}^{\rm abs}(\Omega_m)\}
 =-D_m^{\rm orb},$$ and $$\label{eq:D-Hm}
 \frac{D_m^{\rm orb}}{H_m}
 =\frac{2}{C_M}(\beta R)^{2m}\{1+o(1)\}
 \longrightarrow+\infty.$$

The fixed-gap proof of RH-338 applies to the period-$2m$ orbit even though the windows are evaluated on the narrower $k$-clock [@WangFarAtom2026]. The endpoint lies to the right of $b$ by a fixed gap; all retained internal even points are at most $h(b)<b$; and all odd folded points are at most $r<b$. Since $A\sqrt\sigma\to0$, deleting only $h(p_{2m})$ leaves $2m-1$ distinct points in $F_{\sigma,k,A}$.

The finite set $\Omega_m$ has zero multiplication operator on $L^2$, so its noisy localized trace is zero. Folding preserves the multiplier and marked multiplicity. Since $M_m<0$ for large $m$, each deterministic weight is $1/(1+|M_m|)$, proving [\[eq:R-orb-minus\]](#eq:R-orb-minus){reference-type="eqref" reference="eq:R-orb-minus"}. Finally [\[eq:M-m\]](#eq:M-m){reference-type="eqref" reference="eq:M-m"} and $\beta^{2m}=r_H^{-2m}\lambda^{-m}$ give $$D_m^{\rm orb}=\frac{2m}{C_M}\beta^{2m}\{1+o(1)\}.$$ Division by $H_m$ gives [\[eq:D-Hm\]](#eq:D-Hm){reference-type="eqref" reference="eq:D-Hm"}; RH-336 proves $\beta R>1$ exactly [@WangProjectorMass2026].

As in RH-338, $\Omega_m$ is only an analytic subpartition of the already frozen far set. It is not a new canonical physical observation window.

# Off-alias compensation obstruction

Collect every other signed contribution at $n_-$ into the exact complement $$\label{eq:C-minus}
 C_k^-:=q_{\sigma,k,n_-}+D_m^{\rm orb}.$$ Thus $$\label{eq:q-minus-split}
 q_{\sigma,k,n_-}=-D_m^{\rm orb}+C_k^-.$$ $C_k^-$ includes the rest of the raw far slot, the boundary and sibling slots, the parity packet, and the radial counterloop term [\[eq:radial-sideband\]](#eq:radial-sideband){reference-type="eqref" reference="eq:radial-sideband"}, with their actual signs retained.

[\[thm:necessary-compensation\]]{#thm:necessary-compensation label="thm:necessary-compensation"} For every admissible cut [\[eq:cut\]](#eq:cut){reference-type="eqref" reference="eq:cut"}, $$\label{eq:E-lower-coeff}
 \mathcal E_{\sigma,\rm off}^{(h)}(R)
 \ge\frac{|q_{\sigma,k,n_-}|R^{2m}}{2m}
 =\frac{|q_{\sigma,k,n_-}|}{2H_m}.$$ Consequently, $$\label{eq:E-implies-compensation}
 \mathcal E_{\sigma,\rm off}^{(h)}(R)\longrightarrow0
 \quad\Longrightarrow\quad
 C_k^-=D_m^{\rm orb}+o(H_m).$$ The required relative precision is $$\label{eq:relative-sideband}
 o\!\left(\frac{H_m}{D_m^{\rm orb}}\right)
 =o\!\left((\beta R)^{-2m}\right).$$ Moreover, an atom/complement proof that takes separate absolute values before their signed sum cannot close, because the orbit atom alone contributes $$\label{eq:absolute-sideband}
 \frac{D_m^{\rm orb}R^{2m}}{2m}
 =\frac{D_m^{\rm orb}}{2H_m}
 \longrightarrow+\infty.$$

The $n_-$ summand is present in [\[eq:E-off\]](#eq:E-off){reference-type="eqref" reference="eq:E-off"}, proving [\[eq:E-lower-coeff\]](#eq:E-lower-coeff){reference-type="eqref" reference="eq:E-lower-coeff"}. If the nonnegative prefix tends to zero, that summand tends to zero and hence $q_{\sigma,k,n_-}=o(H_m)$. Substitute [\[eq:q-minus-split\]](#eq:q-minus-split){reference-type="eqref" reference="eq:q-minus-split"} to obtain [\[eq:E-implies-compensation\]](#eq:E-implies-compensation){reference-type="eqref" reference="eq:E-implies-compensation"}. The reciprocal of [\[eq:D-Hm\]](#eq:D-Hm){reference-type="eqref" reference="eq:D-Hm"} gives [\[eq:relative-sideband\]](#eq:relative-sideband){reference-type="eqref" reference="eq:relative-sideband"}; [\[eq:absolute-sideband\]](#eq:absolute-sideband){reference-type="eqref" reference="eq:absolute-sideband"} is the same identity without the signed complement.

This theorem is one-way. It does not lower-bound the fully signed $|q_{\sigma,k,n_-}|$, because $C_k^-$ may compensate the orbit atom. RH-19 leaves the requisite bulk moving-order control open [@WangComplement2026]. Therefore neither $\mathcal E_{\sigma,\rm off}^{(h)}(R)\to0$ nor its failure follows from the current repository. The exact verdict is a scoped obstruction to the separate-absolute sideband route and `NOT_TESTABLE` for the aggregate off-alias background.

# Reproduction and claim boundary

The artifact evaluates the physical algebraic constants and period-$2m$ boundary orbits at high Decimal precision for $k=3,5,9,17,33$ and $A=1/4$. It reproduces the mandatory sideband orders, far counts $3,7,15,31,63$, orbit closure, the identity $R^{2m}/(2m)=1/(2H_m)$, and the super-target orbit mass. These finite rows are diagnostic formula checks, not interval certificates or moving-order evidence.

The paper proves only the actual typed lower-sideband atom and the necessary signed compensation condition. It proves neither off-alias vanishing nor a positive lower bound for the fully signed sideband coefficient. It does not close the critical packet, noisy head, counterloop synchronization, determinant gluing, full-trace replacement, or full-trace divergence. No Hilbert--Polya operator, Riemann-zero identification, von Mangoldt trace, completed-zeta divisor equality, or Riemann-hypothesis proof is obtained. Gates A--E remain false/open.
