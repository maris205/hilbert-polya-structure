---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--99-unipotent-shear-sublattice-dynamics"
canonical_tex: "symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics/main.pdf"
source_sha256: "af020b21858eeeb4a1856edb22813197ba5d30f4b3ef6cce6fc7b34939dc9258"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Unipotent Shear on Fixed-Index Sublattices: Complete Cycle Data and Valuation Staircases

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/99-unipotent-shear-sublattice-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a positive integer $N$, let $\mathcal L_N$ be the finite set of index-$N$ sublattices of $\mathbb Z^2$. We determine the complete finite dynamics on $\mathcal L_N$ induced by the unipotent shear $U=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$. Unique column Hermite coordinates turn the action into a disjoint union of translations $b\mapsto b+N/a$ on $\mathbb Z/a\mathbb Z$, one for every divisor $a$ of $N$. This gives every cycle, every fixed-point count, and the finite Artin--Mazur zeta function in closed form. For $N=p^r$, the fixed counts form a parity-sensitive valuation staircase and the zeta function has an explicit sparse prime-power product. Finally, the maximal cycle is unique and has length $N$, so the full temporal data recover the index. Exact integer controls enumerate every canonical phase and trace its orbit for $1\leq N\leq120$, with separate prime-power tests.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Unipotent Shear on Fixed-Index Sublattices: Complete Cycle Data and Valuation Staircases'
```

## Markdown 正文

# Introduction

Fix $N\geq1$ and write $$\mathcal L_N=\{L\leq\mathbb Z^2:[\mathbb Z^2:L]=N\}.$$ The integral matrix $$U=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$ lies in $\operatorname{SL}_2(\mathbb Z)$ and therefore acts by the permutation $T_N(L)=UL$ of $\mathcal L_N$. Although $U$ has infinite order on $\mathbb Z^2$, every $T_N$ is a finite permutation. The purpose of this note is to give its complete temporal census.

The calculation has two ingredients. First, column Hermite normal form provides a canonical divisor-layer coordinate system; see, for example, @Cohen1993 [Chapter 2]. Second, on each layer the shear is a cyclic translation. The resulting formulas simultaneously describe cycle lengths, fixed points, and the Artin--Mazur zeta function [@ArtinMazur1965]. The prime-power specialization exposes a sharp valuation staircase that is less visible in the undigested divisor sum.

Classical ownership includes Hermite normal form, the enumeration $|\mathcal L_N|=\sigma_1(N)$, and finite-index subgroup and subgroup-zeta theory [@GrunewaldSegalSmith1988]. Our bounded contribution is the temporal package for this one fixed-index shear and its recovery consequence. No priority is claimed for Hermite normal form, subgroup enumeration, subgroup-zeta theory, or Hecke correspondences. The external literature status of the exact package remains on hold.

# Hermite coordinates and the shear action

For positive integers $a,c$ and $0\leq b<a$, put $$H(a,b,c)=\begin{pmatrix}a&b\\0&c\end{pmatrix},
 \qquad
 L(a,b,c)=H(a,b,c)\mathbb Z^2=\mathbb Z(a,0)+\mathbb Z(b,c).$$

[\[prop:hnf\]]{#prop:hnf label="prop:hnf"} Every $L\in\mathcal L_N$ has a unique expression $$L=L(a,b,c),\qquad ac=N,\quad 0\leq b<a.$$ In these coordinates, $$\label{eq:action}
 T_N\bigl(L(a,b,c)\bigr)=L(a,b+c\bmod a,c).$$ Consequently $|\mathcal L_N|=\sum_{a\mid N}a=\sigma_1(N)$.

Let the image of $L$ under projection onto the second coordinate be $c\mathbb Z$, and let $L\cap(\mathbb Z\times\{0\})=a\mathbb Z\times\{0\}$. Choose $(b,c)\in L$ and reduce $b$ modulo $a$ into $0\leq b<a$. If $(x,y)\in L$, then $y=kc$ for some $k\in\mathbb Z$, and $(x,y)-k(b,c)\in L\cap(\mathbb Z\times\{0\})$. Thus $(a,0)$ and $(b,c)$ generate $L$. Projection, intersection, and the residue class of $b$ show uniqueness. The determinant of this basis is $ac$, hence $ac=N$.

Left multiplication acts on the displayed column basis as $$U H(a,b,c)=
 \begin{pmatrix}1&1\\0&1\end{pmatrix}
 \begin{pmatrix}a&b\\0&c\end{pmatrix}
 =\begin{pmatrix}a&b+c\\0&c\end{pmatrix}.$$ Reducing the first coordinate of the second generator modulo $a$ proves [\[eq:action\]](#eq:action){reference-type="eqref" reference="eq:action"}. For each $a\mid N$ there are exactly $a$ permitted values of $b$, giving the final assertion.

Thus the divisor $a$ labels an invariant layer, with $c=N/a$ and phase $b\in\mathbb Z/a\mathbb Z$. Define $$\label{eq:gh}
 g_a=\gcd(a,N/a),\qquad h_a=\frac{a}{g_a}.$$

# Complete temporal census

Let $C_N(m)$ denote the number of cycles of exact length $m$, and let $F_N(n)=\#\operatorname{Fix}(T_N^n)$.

[\[thm:census\]]{#thm:census label="thm:census"} For every $N,n,m\geq1$, $$\begin{aligned}
 C_N(m)
   &=\sum_{\substack{a\mid N\\h_a=m}}g_a,                                      \label{eq:cycles}\\
 F_N(n)
   &=\sum_{\substack{a\mid N\\a\mid n(N/a)}}a
     =\sum_{\substack{a\mid N\\h_a\mid n}}a.                                \label{eq:fixed}\end{aligned}$$ In particular, $$\label{eq:mobius}
 C_N(m)=\frac1m\sum_{d\mid m}\mu(m/d)F_N(d),$$ and the finite Artin--Mazur zeta function is the rational function $$\label{eq:zeta}
 \zeta_N(z)
 :=\exp\left(\sum_{n\geq1}\frac{F_N(n)}{n}z^n\right)
 =\prod_{a\mid N}(1-z^{h_a})^{-g_a}
 =\prod_{m\geq1}(1-z^m)^{-C_N(m)}.$$ The products are finite, and $$\label{eq:accounting}
 \sum_{m\geq1}mC_N(m)=\sigma_1(N).$$

On the $a$-layer, [\[eq:action\]](#eq:action){reference-type="ref" reference="eq:action"} is translation by $c=N/a$ on $\mathbb Z/a\mathbb Z$. Such a translation has $g_a=\gcd(a,c)$ orbits, each of length $h_a=a/g_a$. Summing these layer inventories proves [\[eq:cycles\]](#eq:cycles){reference-type="eqref" reference="eq:cycles"} and [\[eq:accounting\]](#eq:accounting){reference-type="eqref" reference="eq:accounting"}.

The $n$th iterate translates by $nc$. It fixes a phase if and only if $a\mid nc$; when this happens, it fixes all $a$ phases in the layer. Writing $a=g_aa'$ and $c=g_ac'$ with $\gcd(a',c')=1$ shows that $a\mid nc$ is equivalent to $h_a=a'\mid n$, proving [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}.

Every finite permutation satisfies $F_N(n)=\sum_{m\mid n}mC_N(m)$. Möbius inversion gives [\[eq:mobius\]](#eq:mobius){reference-type="eqref" reference="eq:mobius"}. Finally, one cycle of length $m$ contributes $$\exp\left(\sum_{k\geq1}\frac{z^{km}}{k}\right)=(1-z^m)^{-1}$$ to the zeta function. Multiplication over the cycles proves [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The formulas retain the layer decomposition rather than merely the characteristic polynomial of a permutation matrix. For example, [1](#tab:examples){reference-type="ref" reference="tab:examples"} records three complete inventories.

::: {#tab:examples}
   $N$    $|\mathcal L_N|$  nonzero cycle inventory    $\zeta_N(z)$
  ------ ------------------ -------------------------- -----------------------------------------------------
   $8$          $15$        $1^3,\ 2^2,\ 8^1$          $(1-z)^{-3}(1-z^2)^{-2}(1-z^8)^{-1}$
   $12$         $28$        $1^3,\ 3^3,\ 4^1,\ 12^1$   $(1-z)^{-3}(1-z^3)^{-3}(1-z^4)^{-1}(1-z^{12})^{-1}$
   $16$         $31$        $1^7,\ 4^2,\ 16^1$         $(1-z)^{-7}(1-z^4)^{-2}(1-z^{16})^{-1}$

  : Exact cycle data for selected indices. An entry $m^{C_N(m)}$ means $C_N(m)$ cycles of length $m$.
:::

# Prime powers and the valuation staircase

The divisor layers become particularly sparse when $N=p^r$. Let $v_p(n)$ be the $p$-adic valuation of $n$.

[\[thm:primepower\]]{#thm:primepower label="thm:primepower"} Let $p$ be prime and $r\geq1$. For the layer $a=p^j$, $c=p^{r-j}$, $0\leq j\leq r$, one has $$\label{eq:prime-layer}
 g_j=p^{\min(j,r-j)},\qquad
 h_j=
 \begin{cases}
  1,&2j\leq r,\\
  p^{2j-r},&2j>r.
 \end{cases}$$ Hence, with $$A_{p,r}=\sum_{j=0}^{\lfloor r/2\rfloor}p^j
 =\frac{p^{\lfloor r/2\rfloor+1}-1}{p-1},$$ the complete cycle inventory consists of $A_{p,r}$ fixed cycles and, for each $j>r/2$, exactly $p^{r-j}$ cycles of length $p^{2j-r}$. Equivalently, $$\label{eq:prime-zeta}
 \zeta_{p^r}(z)
 =(1-z)^{-A_{p,r}}
 \prod_{j=\lfloor r/2\rfloor+1}^{r}
       (1-z^{p^{2j-r}})^{-p^{r-j}}.$$ For every $n\geq1$, put $s=v_p(n)$ and $$J=\min\left\{r,\left\lfloor\frac{r+s}{2}\right\rfloor\right\}.$$ Then $$\label{eq:staircase}
 F_{p^r}(n)=\sum_{j=0}^{J}p^j=\frac{p^{J+1}-1}{p-1}.$$ Thus the fixed count changes only when the valuation crosses a threshold of the same parity as $r$ and saturates at $\sigma_1(p^r)$ when $s\geq r$.

Substitution of $a=p^j$ and $c=p^{r-j}$ into [\[eq:gh\]](#eq:gh){reference-type="ref" reference="eq:gh"} gives $g_j=p^{\min(j,r-j)}$ and then [\[eq:prime-layer\]](#eq:prime-layer){reference-type="eqref" reference="eq:prime-layer"}. The layers with $2j\leq r$ consist entirely of fixed cycles, whose total number is $A_{p,r}$. In every remaining layer, $g_j=p^{r-j}$ and $h_j=p^{2j-r}$, proving the inventory and [\[eq:prime-zeta\]](#eq:prime-zeta){reference-type="eqref" reference="eq:prime-zeta"}.

By [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}, the $j$th layer contributes its $p^j$ states precisely when $p^j\mid n p^{r-j}$, or equivalently $2j\leq r+s$. Therefore the contributing layers are exactly $0\leq j\leq J$, which gives [\[eq:staircase\]](#eq:staircase){reference-type="eqref" reference="eq:staircase"}. If $s\geq r$, then $J=r$.

The parity effect is exact: both the nontrivial period exponents in base $p$ and the fixed-count jump valuations $s=v_p(n)$ are $1,3,\ldots,r$ for odd $r$ and $2,4,\ldots,r$ for even $r$.

# Temporal recovery

The cycle census contains a rigid marker that is present for every index, not only at prime powers.

[\[thm:recovery\]]{#thm:recovery label="thm:recovery"} For every $N\geq1$, the maximal cycle length of $T_N$ is $N$, and there is exactly one cycle of that length. Consequently each of the following data determines $N$:

1.  the complete cycle inventory $\{C_N(m)\}_{m\geq1}$;

2.  the complete fixed sequence $\{F_N(n)\}_{n\geq1}$;

3.  the formal zeta series $\zeta_N(z)$.

For $N=p^r$, the recovered integer then determines both $p$ and $r$ by unique factorization.

The layer $a=N$, $c=1$ has $g_N=1$ and $h_N=N$, so it is one $N$-cycle. For every divisor layer, $h_a=a/g_a\leq a\leq N$. Equality $h_a=N$ forces $a=N$ and $g_a=1$, so the displayed cycle is the unique maximal one. Thus $$N=\max\{m:C_N(m)>0\}.$$ The fixed sequence determines the cycle inventory through [\[eq:mobius\]](#eq:mobius){reference-type="ref" reference="eq:mobius"}. The formal identity $$z\frac{d}{dz}\log\zeta_N(z)=\sum_{n\geq1}F_N(n)z^n$$ shows coefficient by coefficient that the zeta series determines every $F_N(n)$; hence it also determines the inventory and $N$. The case $N=1$ is included: there is one fixed lattice and the maximal period is $1$.

The conclusion deliberately uses temporal data. Although $|\mathcal L_N|=\sigma_1(N)$ is a useful accounting identity, no injectivity claim for the divisor-sum function is needed or made.

# Exact controls and scope

The accompanying standard-library script constructs all HNF states, applies $U$ to the two raw basis columns, reduces the off-diagonal residue, verifies mutual lattice containment, enumerates the permutation cycles, and compares the result with [\[eq:cycles\]](#eq:cycles){reference-type="ref" reference="eq:cycles"}. For every $1\leq N\leq120$ it also checks every fixed count through time $2N$, Möbius reconstruction through period $N$, state accounting, and maximal cycle recovery. Separate symbolic lanes test [\[thm:primepower\]](#thm:primepower){reference-type="ref" reference="thm:primepower"} for $p\in\{2,3,5,7\}$ and $1\leq r\leq10$. All calculations use exact integers; no floating-point spectral inference enters a theorem.

The result is intentionally finite and rank two. It does not address higher-rank unipotent actions, random walks on sublattices, orbit statistics as $N\to\infty$, or the Hecke-algebraic organization of related correspondences. Those would require distinct ownership audits and proof engines.

# Conclusion

The fixed-index sublattice action of a unipotent shear reduces exactly to divisor-indexed cyclic translations. This reduction gives a full temporal census, turns prime powers into explicit valuation staircases, and exposes the unique maximal orbit that recovers the index. The formulas are closed at finite $N$ and are independently checkable by exhaustive integer enumeration in the accompanying artifact.
