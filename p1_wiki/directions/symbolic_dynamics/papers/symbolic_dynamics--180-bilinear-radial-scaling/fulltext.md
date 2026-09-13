---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--180-bilinear-radial-scaling"
canonical_tex: "symbolic_dynamics/papers/180-bilinear-radial-scaling/main.tex"
canonical_pdf: "symbolic_dynamics/papers/180-bilinear-radial-scaling/main.pdf"
source_sha256: "529bd4c0c091d3932c35de0b1ac8a6d347b3c65a838738bccfc1167207929991"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Bilinear Radial Scaling over Finite Fields

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/180-bilinear-radial-scaling>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/180-bilinear-radial-scaling/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/180-bilinear-radial-scaling/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/180-bilinear-radial-scaling/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/180-bilinear-radial-scaling/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $B$ be a nondegenerate bilinear form on $V=\mathbb F_q^m$. We determine the finite polynomial map $\Phi(u,v)=(B(u,v)u,B(u,v)v)$. Its $t$th iterate is radial with exponent $(3^t-1)/2$, while its bilinear value follows the scalar cube map. This gives every tail and eventual period from the decomposition of the initial value's order into its $3$-part and prime-to-$3$ part. We lift the scalar description back to all pair targets: every-time fibres are power-map root counts, except for a null cone collapsing to zero. We also give every tail population, the recurrent census, image size, and complete one-step fibre distribution; zero is the unique maximum-fibre target. Power maps, bilinear level counts, and generic polynomial functional graphs receive zero contribution credit. Status is `OWNER_AMBER / HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: Bilinear Radial Scaling over Finite Fields
```

## Markdown 正文

# Literal map and subtraction boundary

Let $q$ be a prime power and $m\ge1$. Fix a nondegenerate bilinear form $B:V\times V\to\mathbb F_q$ and define $$\label{eq:map}
 \Phi(u,v)=\bigl(cu,cv\bigr),\qquad c=B(u,v).$$ The form need not be symmetric. A state means the ordered pair $(u,v)$; write $0=(0,0)$.

Monomial dynamics over finite fields is established background [@ColonReyesEtAl2006], as are polynomial functional graphs [@KonyaginEtAl2016] and, most directly, the structure of power-map functional graphs over finite groups [@QureshiReis2023]. We therefore assign finite-field cyclicity, scalar power-map tails and roots, and static level counts of $B$ zero contribution credit. The retained conjunction is the literal pair map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, its radial iterate, the lift of every scalar time/fibre statement to every pair target, the exceptional null cone, and the complete population atlas. A literal or conjugate owner triggers withdrawal. The bounded source non-hit used for internal drafting is not a novelty certificate.

Internally, P102 and P103 contain scalar power-map reductions inside, respectively, an involutive group-algebra norm map and double-adjugate matrix dynamics; P125 is a formed-space pair map with a different shear update. P171 is a Gram-type warning, but it lives over the Boolean semiring rather than a finite-field bilinear radial map. None supplies the present source-to-pair lift, null-cone collapse, or bilinear population atlas, and all shared scalar-power and formed-space vocabulary receives zero credit.

For later counts put $$\label{eq:QZ}
 Q=q^{m-1}(q^m-1),\qquad
 Z=q^{2m-1}+q^m-q^{m-1}.$$

[\[lem:levels\]]{#lem:levels label="lem:levels"} For each $d\in\mathbb F_q^*$, exactly $Q$ states satisfy $B(u,v)=d$, while exactly $Z$ states lie on the null cone $B(u,v)=0$.

For each $u\ne0$, nondegeneracy makes $v\mapsto B(u,v)$ a nonzero linear functional, so every value has $q^{m-1}$ preimages. Thus a nonzero level has $(q^m-1)q^{m-1}=Q$ points. Subtracting the $q-1$ nonzero levels from $q^{2m}$ gives $Z$.

# Iterates, tails, and periods

Set $a_t=(3^t-1)/2$, an ordinary integer exponent (also in characteristic two).

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} For every $t\ge0$, $$\label{eq:iterate}
 \Phi^t(u,v)=\bigl(c^{a_t}u,c^{a_t}v\bigr),
 \qquad B(\Phi^t(u,v))=c^{3^t},$$ with the evident exponent-zero convention at $t=0$.

If a pair is scaled by $\lambda$, bilinearity scales its $B$-value by $\lambda^2$. Hence one step sends $c$ to $c^3$. If the accumulated radial exponent is $a_t$, the next is $a_t+3^t=a_{t+1}$. Induction proves both identities, including $c=0$.

For $c\ne0$, let $r=\operatorname{ord}_{\mathbb F_q^*}(c)$ and factor $r=3^a s$ with $(s,3)=1$. Write $\operatorname{ord}_{2s}(3)$ for the multiplicative order of $3$ modulo the ordinary integer $2s$; in particular $\operatorname{ord}_2(3)=1$. Thus no division by two in $\mathbb F_q$ is intended.

[\[thm:orbit\]]{#thm:orbit label="thm:orbit"} The zero state is fixed. Every other state on the null cone has exact tail one and eventual period one. A state with $c\ne0$ has exact tail $a$ and eventual period $$\label{eq:period}
 \operatorname{ord}_{2s}(3).$$

A null state maps to zero, proving the first claims. For $c\ne0$, the pair itself has a nonzero coordinate, so two radial multiples are equal exactly when their scalars are equal. By [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}, equality at epochs $t$ and $t+\ell$ is equivalent to $$\label{eq:divisibility}
 3^a s\mid 3^t\frac{3^\ell-1}{2}.$$ Because $3\nmid 3^\ell-1$, a cycle can first be reached exactly at $t=a$. After cancelling $3^a$, the least positive $\ell$ satisfies $2s\mid3^\ell-1$, which is [\[eq:period\]](#eq:period){reference-type="eqref" reference="eq:period"}.

# Every-time fibres

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} At $t=0$, every target has exactly one predecessor under $\Phi^0$. For $t\ge1$, put $g_t=\gcd(3^t,q-1)$, and let $(x,y)$ be a target with $d=B(x,y)$. Then $$\label{eq:fibres}
 \#(\Phi^t)^{-1}(x,y)=
 \begin{cases}
 Z,&(x,y)=0,\\
 0,&(x,y)\ne0\text{ and }d=0,\\
 g_t,&d\ne0\text{ and }d^{(q-1)/g_t}=1,\\
 0,&d\ne0\text{ and }d^{(q-1)/g_t}\ne1.
 \end{cases}$$

The time-zero statement is the identity-map boundary. Suppose henceforth that $t\ge1$. The null cone is precisely the fibre of zero: its points collapse in one step, while a nonzero bilinear value gives a nonzero radial scalar. Now let the target be nonzero. A predecessor with initial value $c\ne0$ is forced by [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} to be $c^{-a_t}(x,y)$. Its bilinear value equals $c$ exactly when $d=c^{2a_t+1}=c^{3^t}$. Thus predecessors are in bijection with $3^t$th roots of $d$ in the cyclic group $\mathbb F_q^*$. The standard cyclic-group root criterion gives the final two cases.

This proof supplies an explicit predecessor, not just its number: each root $c$ gives $c^{-a_t}(x,y)$.

# Population and image atlases

Write $q-1=3^A h$ with $(h,3)=1$.

[\[thm:census\]]{#thm:census label="thm:census"} Among states with nonzero $B$-value, exactly $hQ$ are recurrent, and for $1\le a\le A$ exactly $$\label{eq:tails}
 2\cdot3^{a-1}hQ$$ have tail $a$. Including the null cone, the total tail-zero population is $1+hQ$; the tail-one population is $Z-1+\mathbf 1_{A\ge1}\,2hQ$; and for $2\le a\le A$ it is [\[eq:tails\]](#eq:tails){reference-type="eqref" reference="eq:tails"}. The sharp maximum tail is $\max\{1,A\}$.

The cyclic group $\mathbb F_q^*$ is the product of cyclic factors of orders $3^A$ and $h$. Exactly $h$ elements have order prime to $3$. For $a\ge1$, exactly $\varphi(3^a)h=2\cdot3^{a-1}h$ elements have order with exact $3$-primary part $3^a$. Multiply these scalar counts by the common level size $Q$ from Lemma [\[lem:levels\]](#lem:levels){reference-type="ref" reference="lem:levels"}, then add zero and the $Z-1$ nonzero null states. Such null states ensure tail one exists for every $q,m$.

[\[thm:image\]]{#thm:image label="thm:image"} Let $g=\gcd(3,q-1)$. Then $$\label{eq:image}
 |\operatorname{im}\Phi|=1+\frac{(q-1)Q}{g}.$$ Every nonzero image target has exactly $g$ predecessors. Zero has $Z$ predecessors and is the unique maximum-fibre target.

Apply Theorem [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"} at $t=1$. The cube subgroup has $(q-1)/g$ values, each supporting $Q$ pair targets, plus zero. This proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} and uniformity. Finally $Z=q^{m-1}(q^m+q-1)>q-1\ge g$, so zero is uniquely maximal.

All statements are deductive for arbitrary prime powers and nondegenerate bilinear forms. The accompanying prime-field enumeration is only finite counterexample pressure; it is neither experimental nor novelty evidence.
