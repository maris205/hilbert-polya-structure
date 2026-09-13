---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-cubic-cm-frobenius-bridge"
canonical_tex: "henon_dynamics/henon_cubic_cm_frobenius_bridge/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_cubic_cm_frobenius_bridge/paper/paper.pdf"
source_sha256: "3a13186a2797936dc79071523a53cb78861bb3a806e1eda97368c954aefb5bc2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# From a Cubic Hénon Channel to CM Frobenius Data: An Exact Arithmetic Bridge and Its Scope Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_cubic_cm_frobenius_bridge>)
- [规范 TeX](<../../../../../henon_dynamics/henon_cubic_cm_frobenius_bridge/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_cubic_cm_frobenius_bridge/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_cubic_cm_frobenius_bridge/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_cubic_cm_frobenius_bridge/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Artificial prime damping makes a three-channel Hénon--Kummer block determinant trace class but adds an external clock. We replace that damping by the minimal geometric carrier of cubic symmetry, the elliptic curve $E:y^2=x^3+1$. Its order-three automorphism gives complex multiplication by $\mathbb Z[\zeta_3]$, and its local polynomial is $1-a_pT+pT^2$. We prove directly that $a_p=0$ for every good prime $p\equiv2\pmod3$, because the cube map is bijective in that residue class. An exact certificate counts all good primes below 2,000, verifies every Hasse bound, and independently enumerates $E(\mathbb F_{p^2})$ at four primes. This supplies a genuine arithmetic connection and intrinsic square-root normalization. It does not supply a Hénon periodic-orbit determinant: the resulting object is the CM elliptic $L$-function, with different local and global analytic data from the Riemann $\xi$-function.
author:
- |
  Liang Wang$^{*1}$\
  $^{1}$School of Artificial Intelligence and Automation, Huazhong University of Science and Technology\
  Wuhan 430074, P.R. China\
  $^*$Corresponding author
bibliography:
- references.bib
date: 'Preprint, August 2026'
title: |
  From a Cubic Hénon Channel to CM Frobenius Data:\
  An Exact Arithmetic Bridge and Its Scope Boundary
```

## Markdown 正文

# Introduction

The homogeneous area-preserving Hénon route naturally produces a cubic phase. A direct three-channel Kummer representation is gauge trivial; a nonfunctorial permutation survives locally but its raw prime divisor accumulates; and scalar damping repairs convergence only by inserting a new clock. These failures suggest a change in mathematical object rather than another weight adjustment.

The curve $$\label{eq:E}
 E:\quad y^2=x^3+1$$ is the smallest smooth projective arithmetic object carrying the same cubic symmetry. Over a field containing $\zeta_3$, the map $(x,y)\mapsto(\zeta_3x,y)$ is an order-three endomorphism. The curve has $j=0$ and complex multiplication by $\mathbb Z[\zeta_3]$; see [@Milne2026; @Silverman2009]. This paper asks what exact arithmetic data the cubic channel obtains from this completion and where the Hénon claim must stop.

We obtain a positive local theorem, a two-implementation numerical certificate, and a negative provenance conclusion. The positive theorem is intrinsic arithmetic. The negative conclusion prevents an elliptic $L$-function from being promoted coordinatewise to a Riemann or Hénon determinant.

# Local Frobenius factors

For a prime $p>3$, let $$N_p=\#E(\mathbb F_p),\qquad a_p=p+1-N_p.$$ The local zeta numerator is $$\label{eq:local}
 L_p(T)=1-a_pT+pT^2.$$ Its roots have absolute value $\sqrt p$ by the elliptic-curve Riemann hypothesis, equivalently $|a_p|\le2\sqrt p$. This is intrinsic square-root normalization, not a fitted factor.

[\[thm:inert\]]{#thm:inert label="thm:inert"} If $p>3$ and $p\equiv2\pmod3$, then $a_p=0$ and $L_p(T)=1+pT^2$.

Let $\chi$ be the quadratic character of $\mathbb F_p$, extended by $\chi(0)=0$. Point counting gives $$N_p=p+1+\sum_{x\in\mathbb F_p}\chi(x^3+1),
 \quad
 a_p=-\sum_x\chi(x^3+1).$$ Because $\gcd(3,p-1)=1$, the map $x\mapsto x^3$ is a bijection of $\mathbb F_p$. Therefore $$\sum_x\chi(x^3+1)=\sum_u\chi(u+1)=0,$$ and the claim follows.

For split primes $p\equiv1\pmod3$, the trace need not vanish. Direct counts give $$a_7=-4,\qquad a_{13}=2,\qquad a_{19}=8.$$ Thus the cubic channel distinguishes the inert and split prime classes without a fitted classifier.

# Quadratic-extension independent check

Let $\alpha_p,\beta_p$ be the roots of [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"}. Then $\alpha_p+\beta_p=a_p$, $\alpha_p\beta_p=p$, and $$\alpha_p^2+\beta_p^2=a_p^2-2p.$$ Hence $$\label{eq:p2}
 \#E(\mathbb F_{p^2})=p^2+1-(a_p^2-2p).$$

The release code verifies [\[eq:p2\]](#eq:p2){reference-type="eqref" reference="eq:p2"} independently. For each of $p=5,7,11,13$, it chooses a quadratic nonsquare $d$, represents $\mathbb F_{p^2}$ as pairs in $\mathbb F_p[u]/(u^2-d)$, and tests square status for every $x$ in the extension. This computation does not reuse the prime-field point list.

    $p$   $p\bmod3$   $a_p$       $L_p(T)$
  ----- ----------- ------- --------------
      5           2       0       $1+5T^2$
      7           1      -4    $1+4T+7T^2$
     11           2       0      $1+11T^2$
     13           1       2   $1-2T+13T^2$
     19           1       8   $1-8T+19T^2$

  : Frozen local sentinels.

# What the bridge proves

The construction solves the provenance defect of C40 at one level. The factor $p$ in [\[eq:local\]](#eq:local){reference-type="eqref" reference="eq:local"} and the size $\sqrt p$ of Frobenius are forced by geometry. The local traces are reproducible, and repetitions are controlled by the recurrence $a_{p,r}=a_pa_{p,r-1}-pa_{p,r-2}$.

It does not solve the Hénon identification. The curve [\[eq:E\]](#eq:E){reference-type="eqref" reference="eq:E"} is selected because it carries cubic symmetry, but no theorem maps primitive Hénon unstable orbits to its Frobenius classes. Its Euler product is the elliptic $L$-function of $E$, not the Riemann zeta function. Its degree, bad factors, gamma factor, and nontrivial zeros are correspondingly different. This is a new arithmetic connection, not a Hilbert--Pólya realization.

# Evaluator audit

Route A credits reproducible Frobenius data at A1, but only weakly because Hénon chronology is missing. The classical elliptic Euler product earns an analytic determinant label at A2. CM and square-root normalization give partial A3. Cohomology is only an A4 formal hint relative to the Hénon map. The strict tuple is $$(A1_{\rm WEAK},A2_{\rm ANALYTIC\ DET},
A3_{\rm PARTIAL\ ANALYTIC},A4_{\rm FORMAL\ HINT}).$$

A limited Route-B audit stops at B1. No Hénon-derived Hilbert space, densely defined operator, domain, or spectral parameter map has been given. An arithmetic Euler product cannot substitute for those data.

# Conclusion

The cubic Hénon channel has a natural arithmetic completion, and that completion is nontrivial: the $j=0$ CM curve supplies exact inert/split Frobenius behavior and intrinsic square-root normalization. It also changes the target. The next decisive question is finite and local: can any virtual combination of this $H^1$ factor and Tate factors equal the Riemann local factor without inserting an exact negative copy? A three-prime comparison will answer that question before any global operator is attempted.
