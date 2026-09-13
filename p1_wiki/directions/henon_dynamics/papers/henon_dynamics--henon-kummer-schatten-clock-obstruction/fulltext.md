---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kummer-schatten-clock-obstruction"
canonical_tex: "henon_dynamics/henon_kummer_schatten_clock_obstruction/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_kummer_schatten_clock_obstruction/paper/paper.pdf"
source_sha256: "699d8555cdb4e402c2205bcb17bf356858874b61d7c3a420c6206d7c9396a8ba"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Sharp Schatten Diagram for Cubic Kummer Prime Blocks and the Obstruction of an External Second Clock

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kummer_schatten_clock_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kummer_schatten_clock_obstruction/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kummer_schatten_clock_obstruction/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kummer_schatten_clock_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_kummer_schatten_clock_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The raw three-channel Kummer prime product has an interior divisor accumulation. We study its minimal convergence repair. On the prime-block Hilbert space $\bigoplus_p\mathbb C^3$, let $T_\sigma=\bigoplus_p p^{-\sigma}U_p$, where every $U_p$ is unitary. We prove the sharp phase diagram $T_\sigma\in\mathcal S_q$ if and only if $\sigma q>1$. In particular, the operator is compact exactly for $\sigma>0$, Hilbert--Schmidt exactly for $\sigma>1/2$, and trace class exactly for $\sigma>1$. The latter region gives a valid ordinary Fredholm determinant. However, the three-channel Kummer representation is unramified at every good prime and has Artin conductor exponent zero there. It cannot supply the damping $p^{-\sigma}$; that factor is an external second clock. Exact threshold tests and prime-sum diagnostics accompany the proof. The result separates a positive operator theorem from a negative canonicality theorem and points to geometric cubic cohomology as the next intrinsic normalization.
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
  A Sharp Schatten Diagram for Cubic Kummer Prime Blocks\
  and the Obstruction of an External Second Clock
```

## Markdown 正文

# Introduction

Finite Kummer channel permutations are the smallest nonscalar structures not removed by the homogeneous Hénon gauge. Without size decay, their local zeros and poles accumulate at the critical interior point. The most direct repair is to damp the prime block by $p^{-\sigma}$. This paper asks two separate questions: exactly when does that repair define a standard operator determinant, and does the Hénon/Kummer source produce the needed exponent?

The first answer is completely positive. A fixed-rank block sum has a sharp Schatten threshold governed by the prime Dirichlet series. The second answer is negative. The Kummer channel is unramified away from a fixed bad-prime set, so its Artin conductor has no growing good-prime exponent [@Serre1979]. The new $\sigma\log p$ scale is inserted, not derived.

This distinction matters for Hilbert--Pólya exploration. A well-defined determinant is meaningful analytic structure, but an external convergence clock cannot be credited as Hénon dynamics. The paper therefore records both the exact determinant theorem and the exact provenance obstruction.

# Prime-block operator

Let $U_p\in U(3)$ be any unitary three-channel Kummer block and set $$\mathcal H=\bigoplus_p\mathbb C^3,
 \qquad T_\sigma=\bigoplus_p p^{-\sigma}U_p.$$ Each block has three singular values equal to $p^{-\sigma}$. Hence, for $0<q<\infty$, $$\label{eq:norm}
 \|T_\sigma\|_{\mathcal S_q}^q
 =3\sum_p p^{-\sigma q}.$$ The phases of the channel permutation play no role in this norm identity.

[\[thm:phase\]]{#thm:phase label="thm:phase"} For $0<q<\infty$, $$T_\sigma\in\mathcal S_q
 \quad\Longleftrightarrow\quad \sigma q>1.$$ Moreover, $T_\sigma$ is compact if and only if $\sigma>0$.

Equation [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"} reduces membership to convergence of $\sum_p p^{-u}$, which holds exactly for $u>1$. At $u=1$, Euler's prime-harmonic divergence applies; for $u<1$, comparison is stronger. See [@Apostol1976]. Compactness of a block-diagonal operator is equivalent to its block norms tending to zero, which occurs exactly when $p^{-\sigma}\to0$.

The operator is Hilbert--Schmidt exactly for $\sigma>1/2$ and trace class exactly for $\sigma>1$. In the trace-class region, $$\det(I-zT_\sigma)=\prod_p\det(I-zp^{-\sigma}U_p)$$ is an ordinary Fredholm determinant, locally uniformly in $z$.

Take $q=2$ and $q=1$ in Theorem [\[thm:phase\]](#thm:phase){reference-type="ref" reference="thm:phase"}. The determinant claim is the standard trace-ideal theorem [@Simon2005].

The theorem is robust under any fixed block rank $d$: the factor three in [\[eq:norm\]](#eq:norm){reference-type="eqref" reference="eq:norm"} becomes $d$, while the threshold is unchanged.

# Why the damping is not intrinsic

For a finite-dimensional representation of a local Galois or inertia group, the Artin conductor records ramification. The frozen cubic permutation channel is unramified for every good prime $p\ne3$. Its conductor exponent there is therefore $$a_p=0.$$ Only the fixed bad-prime set can contribute. No source-native conductor function produces a positive constant $\sigma$ at all primes, much less a weight $p^{-\sigma}$.

Within the unramified three-channel Kummer model, the damping in $T_\sigma$ is not determined by local conductor data. For every $\sigma>0$, it adds the independent clock $\sigma\log p$.

The local conductor exponent is zero at all good primes, while $-\log(p^{-\sigma})=\sigma\log p>0$. The two functions disagree on every good prime. Thus the damping cannot be recovered from that conductor.

This is a provenance theorem, not a claim that weighted determinants are illegitimate. They are legitimate analytic objects. They simply do not show that the homogeneous Hénon phase generated the required convergence.

# Finite diagnostics

The release checker evaluates exact rational threshold sentinels on both sides of $\sigma q=1$. It also reports the positive partial sums $$3\sum_{p\le X}p^{-u},\qquad u\in\{0.8,1.0,1.2\},$$ for four cutoffs through $10^6$. Those values are diagnostics only: slow growth at $u=1$ and apparent stabilization at $u=1.2$ are not used to prove either statement.

   $\sigma$   $q$          Verdict
  ---------- ----- -----------------------
    $1/3$      2    not in $\mathcal S_2$
    $1/2$      2     boundary divergence
    $2/3$      2      in $\mathcal S_2$
      1        1     boundary divergence
    $6/5$      1         trace class

  : Exact membership sentinels.

# Route evaluation

A1 remains weak because the prime labels are inherited and the damping is a second clock. A2 receives the exact label `A2_ANALYTIC_DETERMINANT` for $\sigma>1$. A3 fails because this determinant has no derived functional equation, gamma factor, or Riemann divisor. A4 is a formal operator hint, not a Hilbert--Pólya operator. The tuple is $$(A1_{\rm WEAK},A2_{\rm ANALYTIC\ DET},A3_{\rm FAIL},A4_{\rm FORMAL\ HINT}).$$ Route B is not authorized.

# Conclusion

Prime damping repairs the C39 analytic failure exactly, and the repair has a sharp universal threshold. It does not repair provenance. The positive Fredholm determinant depends on an external exponent that the unramified Kummer channel cannot supply. The most natural next step is therefore not to tune $\sigma$, but to replace the finite channel by a geometric cubic object whose Frobenius eigenvalues carry intrinsic square-root size. The minimal such object is the $j=0$ elliptic curve $y^2=x^3+1$.
