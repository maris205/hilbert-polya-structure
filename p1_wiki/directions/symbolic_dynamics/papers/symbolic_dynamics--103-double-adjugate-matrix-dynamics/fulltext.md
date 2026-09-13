---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--103-double-adjugate-matrix-dynamics"
canonical_tex: "symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics/main.pdf"
source_sha256: "f15eb1c90a760cc4e157a2380e8fc44f1f052ad953717a90b25ed9f22e2a2956"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Double-Adjugate Dynamics over Finite Fields: Singular Collapse and Projective Image Staircases

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/103-double-adjugate-matrix-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $d\ge3$ and a finite field $\mathbb F_q$, we study the self-map of the full matrix space $$\Psi(A)=\operatorname{adj}(\operatorname{adj}A),\qquad A\in M_d(\mathbb F_q).$$ Jacobi's classical identity gives $\Psi(A)=\det(A)^{d-2}A$; we assign that identity zero novelty credit and determine its finite temporal consequences. Every singular matrix enters zero in one step. With $\alpha=(d-1)^2$ and $E_k=(\alpha^k-1)/d$, every invertible matrix satisfies $$\Psi^k(A)=\det(A)^{E_k}A.$$ Consequently $$|\operatorname{Fix}(\Psi^k)|=1+|\operatorname{SL}_d(q)|\gcd(E_k,q-1),
   \qquad
   |\operatorname{im}(\Psi^k)|=1+\frac{|\operatorname{GL}_d(q)|}{\gcd(\alpha^k,q-1)}.$$ The second formula yields the recurrent-core size and a sharp prime-valuation stabilization time. The first gives every cycle count and the Artin--Mazur zeta function by Möbius inversion, including alternating and third-period fixed-count anomalies. A second route computes two adjugates literally from minors and exhausts small matrix spaces. The note is owner-subtracted against Jacobi identities, projective adjugate/Cremona maps, and scalar power-map functional graphs; external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Double-Adjugate Dynamics over Finite Fields: Singular Collapse and Projective Image Staircases'
```

## Markdown 正文

# Introduction

The adjugate is simultaneously a polynomial matrix operation and, on invertible matrices, determinant times inversion. Its projectivization is a classical Cremona transformation [@Dolgachev2012]. Jacobi's complementary-minor identity and its hyperadjugate extensions are established material [@Lawrence1964]; standard finite-field facts used below can be found in [@LidlNiederreiter1997]. Functional graphs of power maps on finite groups likewise have a direct modern literature [@QureshiReis2023]. None of those ingredients is claimed here.

We instead ask what happens when the adjugate is applied twice at every time step on the *entire* finite matrix space. Two regimes coexist. All singular ranks collapse immediately to zero, whereas every invertible projective scalar line is invariant and carries an affine power map on its nonzero scalars. This separation makes both the fixed sequence and the shrinking image sequence exact. Their arithmetic is different: fixed counts see $(\alpha^k-1)/d$, while image sizes see $\alpha^k$ itself.

The residual contribution is the conjunction of the iterate normal form, singular basin, fixed and image formulas, valuation stabilization, and full cycle/zeta census over finite fields. A bounded source search did not find this temporal package, but it is not an absolute novelty certificate. External submission, public release, and priority language remain **HOLD**.

# Normal form and singular collapse

Fix a prime power $q$ and an integer $d\ge3$. Put $$X_{q,d}=M_d(\mathbb F_q),\qquad \Psi(A)=\operatorname{adj}(\operatorname{adj}A).$$ The restriction $d\ge3$ is structural: for $d=2$, adjugation is already a linear involution and its square is the identity.

[\[lem:jacobi\]]{#lem:jacobi label="lem:jacobi"} For every $A\in M_d(\mathbb F_q)$, $$\label{eq:double-adj}
 \Psi(A)=\det(A)^{d-2}A.$$ In particular, every singular matrix maps to zero, and zero is fixed.

For invertible $A$, the identities $\operatorname{adj}(A)=\det(A)A^{-1}$ and $\det(\operatorname{adj}A)=\det(A)^{d-1}$ give [\[eq:double-adj\]](#eq:double-adj){reference-type="eqref" reference="eq:double-adj"} immediately. Both sides of [\[eq:double-adj\]](#eq:double-adj){reference-type="eqref" reference="eq:double-adj"} are polynomial in the matrix entries, and Jacobi's identity extends the equality to all matrices [@Lawrence1964]. Alternatively, the rank-$d-1$ case has $\operatorname{rank}(\operatorname{adj}A)=1$, whose adjugate vanishes for $d\ge3$; lower ranks already have $\operatorname{adj}A=0$. If $\det A=0$, the right side of [\[eq:double-adj\]](#eq:double-adj){reference-type="eqref" reference="eq:double-adj"} is zero.

Define $$\label{eq:alpha-E}
 \alpha=(d-1)^2,\qquad E_k=\frac{\alpha^k-1}{d}\quad(k\ge1).$$ The quotient is integral because $\alpha\equiv1\pmod d$.

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} If $A\in\operatorname{GL}_d(q)$ and $\delta=\det A$, then for every $k\ge1$, $$\label{eq:iterate}
 \boxed{\Psi^k(A)=\delta^{E_k}A},
 \qquad
 \det(\Psi^k(A))=\delta^{\alpha^k}.$$ Every nonzero singular matrix has transient depth one and then stays at zero.

By [\[lem:jacobi\]](#lem:jacobi){reference-type="ref" reference="lem:jacobi"}, if $B$ is invertible with determinant $\eta$, then $\Psi(B)=\eta^{d-2}B$ and $$\det\Psi(B)=\eta^{d(d-2)+1}=\eta^{(d-1)^2}=\eta^\alpha.$$ Thus the scalar exponent in the $k$th iterate obeys $E_{k+1}=E_k+(d-2)\alpha^k$, with $E_1=d-2$. Since $\alpha-1=d(d-2)$, summing the geometric progression gives $E_k=(\alpha^k-1)/d$. The singular assertion follows from [\[lem:jacobi\]](#lem:jacobi){reference-type="ref" reference="lem:jacobi"}.

# Fixed sequence and cycle census

Write $$\label{eq:group-sizes}
 |\operatorname{GL}_d(q)|=\prod_{j=0}^{d-1}(q^d-q^j),
 \qquad |\operatorname{SL}_d(q)|=\frac{|\operatorname{GL}_d(q)|}{q-1}.$$

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} For every $k\ge1$, $$\label{eq:fixed}
 \boxed{\displaystyle
 |\operatorname{Fix}(\Psi^k)|
 =1+|\operatorname{SL}_d(q)|\gcd(E_k,q-1).}$$ Consequently, the number $C_r$ of cycles of exact length $r$ is $$\label{eq:cycles}
 C_r=\frac1r\sum_{e\mid r}\mu(r/e)
 \left(1+|\operatorname{SL}_d(q)|\gcd(E_e,q-1)\right),$$ and $$\label{eq:zeta}
 \zeta_\Psi(z)=\prod_{r\ge1}(1-z^r)^{-C_r}
 =\exp\left(\sum_{k\ge1}
 \frac{1+|\operatorname{SL}_d(q)|\gcd(E_k,q-1)}{k}z^k\right).$$

A singular matrix fixed by a positive iterate must equal zero. For $A\in\operatorname{GL}_d(q)$, [\[thm:iterate\]](#thm:iterate){reference-type="ref" reference="thm:iterate"} gives $\Psi^k(A)=A$ exactly when $(\det A)^{E_k}=1$. The cyclic group $\mathbb F_q^\times$ has $\gcd(E_k,q-1)$ such determinants, and every determinant fiber in $\operatorname{GL}_d(q)$ has cardinality $|\operatorname{SL}_d(q)|$. This proves [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}. Möbius inversion of iterate-fixed counts gives [\[eq:cycles\]](#eq:cycles){reference-type="eqref" reference="eq:cycles"}, and the standard finite-map cycle factorization gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The formula can show large low-period jumps even though projective matrix classes never move. Two registered examples are $$\begin{aligned}
 (q,d)=(5,4):&\quad
 |\operatorname{Fix}(\Psi^k)|=58\,032\,000\,001,
 116\,064\,000\,001,\ldots,\\
 (q,d)=(7,3):&\quad
 |\operatorname{Fix}(\Psi^k)|=5\,630\,689,5\,630\,689,
 16\,892\,065,\ldots.\end{aligned}$$ The first sequence alternates; the second has a jump precisely at multiples of three. These are direct gcd effects in [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}, not numerical experiments.

# Projective image staircase and recurrent core

Let $[A]=\{cA:c\in\mathbb F_q^\times\}$ be the projective scalar line through an invertible matrix. Every such line has $q-1$ points, and distinct lines are disjoint.

[\[thm:image\]]{#thm:image label="thm:image"} For every $k\ge1$, $$\label{eq:image}
 \boxed{\displaystyle
 |\operatorname{im}(\Psi^k)|
 =1+\frac{|\operatorname{GL}_d(q)|}{\gcd(\alpha^k,q-1)}.}$$ Let $$\label{eq:b}
 b=\prod_{\ell\mid\alpha}\ell^{v_\ell(q-1)},$$ where the product is over primes dividing $\alpha$. Then $$\label{eq:recurrent}
 |\operatorname{Rec}(\Psi)|=1+\frac{|\operatorname{GL}_d(q)|}{b}.$$ With the empty maximum interpreted as zero, put $$\label{eq:tstar}
 t_*=\max_{\ell\mid\gcd(\alpha,q-1)}
 \left\lceil\frac{v_\ell(q-1)}{v_\ell(\alpha)}\right\rceil.$$ For $k\geq0$, write $I_k=\Psi^k(\operatorname{GL}_d(q))$, so that $I_0=\operatorname{GL}_d(q)$. The nested invertible image chain $I_0\supseteq I_1\supseteq\cdots$ stabilizes for the first time at $t_*$, and the maximum transient depth on all of $M_d(\mathbb F_q)$ is $$\label{eq:max-depth}
 \boxed{\max\{1,t_*\}.}$$

Fix $A\in\operatorname{GL}_d(q)$ with determinant $\delta$. For $c\in\mathbb F_q^\times$, [\[thm:iterate\]](#thm:iterate){reference-type="ref" reference="thm:iterate"} gives $$\label{eq:line-action}
 \Psi^k(cA)=\delta^{E_k}c^{dE_k+1}A
 =\delta^{E_k}c^{\alpha^k}A.$$ Thus the image on each projective line is a coset of the subgroup of $\alpha^k$th powers. It has $(q-1)/\gcd(\alpha^k,q-1)$ points. There are $|\operatorname{GL}_d(q)|/(q-1)$ invertible projective lines, and every singular matrix contributes only the common image zero. This proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

For each prime $\ell$, the exponent of $\ell$ in $\gcd(\alpha^k,q-1)$ is $\min\{k v_\ell(\alpha),v_\ell(q-1)\}$. Hence these gcds stabilize at $b$, first at the time [\[eq:tstar\]](#eq:tstar){reference-type="eqref" reference="eq:tstar"}. In a finite functional graph the stable image is exactly the recurrent set, proving [\[eq:recurrent\]](#eq:recurrent){reference-type="eqref" reference="eq:recurrent"}. Because images of a finite self-map are nested, strict image loss through time $t_*-1$ and equality from time $t_*$ imply that the maximum invertible tail depth is exactly $t_*$. This includes $t_*=0$, when the restriction to the invertible set is a permutation. Singular points contribute depth one, proving [\[eq:max-depth\]](#eq:max-depth){reference-type="eqref" reference="eq:max-depth"}.

In discrete-log coordinates on a projective line, [\[eq:line-action\]](#eq:line-action){reference-type="eqref" reference="eq:line-action"} is an affine power map $x\mapsto\alpha x+h$ modulo $q-1$. This is the second proof route for the valuation staircase: an affine translation changes cycle placement but not the image index of multiplication by $\alpha^k$.

# Exact controls and owner boundary

The accompanying program computes determinants by modular elimination and adjugates literally from signed minors. It exhausts $M_3(\mathbb F_2)$, $M_3(\mathbb F_3)$, and $M_4(\mathbb F_2)$, comparing two literal adjugations with [\[eq:double-adj\]](#eq:double-adj){reference-type="eqref" reference="eq:double-adj"}. It then checks singular collapse, six fixed counts, and six image sizes. Separate determinant-representative lanes test twelve iterates for $(q,d)=(5,4),(7,3),(11,4),(13,5)$. Independent scalar-line lanes at $(q,d)=(5,4),(7,3),(17,3),(257,3),(19,4)$ exercise image stabilization times $t_*=0,1,2,4,1$, respectively, including literal strict losses and the first stable image. All arithmetic is exact. The computations are finite falsifiers, not a replacement for the proofs.

Jacobi's identity, the projective adjugate map, cyclicity of $\mathbb F_q^\times$, and general power-map functional graphs are established background. We claim none of them separately. The residual claim is the full-matrix temporal package [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}--[\[eq:max-depth\]](#eq:max-depth){reference-type="eqref" reference="eq:max-depth"}, under a bounded collision search and an external-release hold.

Two internal boundaries are explicit. P99 obtains valuation staircases from a unipotent permutation of fixed-index sublattices; it has no singular basin, adjugate identity, or shrinking projective lines. P97 studies sumset squaring on subsets of a prime cyclic group; here the power map occurs only on scalar coordinates inside an invariant matrix line. Neither paper owns the full-matrix fixed/image pair proved here, while the shared valuation and power-map primitives receive no separate credit.

# Conclusion

Double adjugation separates the finite matrix space into a singular basin that dies immediately and invertible projective lines carrying affine power maps. This yields two complementary exact time series: the fixed sequence detects $E_k=(\alpha^k-1)/d$, while the image staircase detects the prime valuations of $\alpha^k$ against $q-1$. Together they determine every cycle count, the zeta function, the recurrent core, and the sharp transient depth.
