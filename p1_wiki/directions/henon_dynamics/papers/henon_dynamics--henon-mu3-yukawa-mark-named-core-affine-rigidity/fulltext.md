---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-named-core-affine-rigidity"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/paper/main.pdf"
source_sha256: "c8247bb8594d831a7f067707ee38f583d57aabcb78e4d9c0f497b57d368bc561"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Affine Rigidity of a Named Complement Core

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_named_core_affine_rigidity/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The preceding complement atlas realizes its universal core as $Q\cong\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2$ with sixteen named coordinate occurrences. The preceding deletion paper found an abstract generation-hypergraph automorphism group of order $345600$, while leaving its relation to the actual core open. We enumerate the finite affine group of the frozen realization: $|\operatorname{Aut}(Q)|=108$ and $|\operatorname{Aff}(Q)|=5832$. The sixteen-occurrence multiset and its ten-point underlying set each have trivial affine stabilizer. We give complete occurrence- and point-overlap censuses; the nearest nonidentity affine maps overlap fourteen of sixteen occurrences. This is a rigidity statement about one named presentation, not a claim that the combinatorial hypergraph is a core-group symmetry.
author:
- Anonymous
title: Affine Rigidity of a Named Complement Core
```

## Markdown 正文

# Frozen named realization

Let $M$ be the multiset of the sixteen C72 coordinates in

$$Q=\mathbb Z/9\oplus\mathbb Z/3\oplus\mathbb Z/2,$$

and let $X=\operatorname{supp}(M)$. Thus $|M|=16$, $|X|=10$, and the multiplicity profile of $M$ is

$$5,2,2,1,1,1,1,1,1,1.$$

The two repeated nonzero points are $(0,1,0)$ and $(3,1,0)$; the point $(0,0,0)$ has multiplicity five. We retain the named presentation rather than choosing a new basis. The scope firewall is $$\texttt{NO\_BAD\_EULER\_OR\_ROOT\_NUMBER}.$$ No full Burnside ring, arithmetic or local construction, Euler factor, root number, automorphy, or Hilbert--Polya operator is claimed.

# The finite affine group

Put $P=\mathbb Z/9\oplus\mathbb Z/3$. Every endomorphism of $P$ has the form $$\label{eq:matrix}
 (x,y)\longmapsto (ax+3by\bmod 9,\;cx+dy\bmod 3),$$ where $a\in\mathbb Z/9$ and $b,c,d\in\mathbb Z/3$. The dyadic factor has only the identity automorphism.

[\[thm:order\]]{#thm:order label="thm:order"} There are $243$ endomorphism matrices of $P$ in [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"}; adjoining the two endomorphisms of the $\mathbb Z/2$ factor gives $486$ endomorphisms of $Q$. A full endomorphism is an automorphism exactly when its dyadic component is the identity and $a$ and $d$ are nonzero modulo $3$. Consequently $$|\operatorname{Aut}(Q)|=6\cdot3\cdot3\cdot2=108,
 \qquad |\operatorname{Aff}(Q)|=54\cdot108=5832.$$

Modulo $3P$, the induced matrix is triangular with diagonal entries $\bar a,d$. This proves the criterion; direct enumeration on all $54$ group points gives the same bijective list. The affine group is the semidirect product of translations by $Q$ with the automorphism group.

# Rigidity of points and occurrences

For an affine map $\varphi$, define the occurrence overlap by $$\label{eq:overlap}
 O(\varphi)=\sum_{q\in Q}\min\bigl(m_M(q),m_{\varphi(M)}(q)\bigr).$$ This counts duplicate occurrences. It is distinct from a pointwise fixed-label count and from $|X\cap\varphi(X)|$.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} $$\operatorname{Stab}_{\operatorname{Aff}(Q)}(M)=1,
 \qquad
 \operatorname{Stab}_{\operatorname{Aff}(Q)}(X)=1.$$ The corresponding linear stabilizers are also trivial. The linear and affine orbit sizes of either named object are therefore $108$ and $5832$.

For $M$, the unique multiplicity-five point is zero, so a stabilizing translation vanishes. The unique nonzero point of $M\cap3P$ is $(6,0,0)$, which gives $a\equiv1\pmod3$. The multiplicity-two pair $u=(0,1,0)$, $v=(3,1,0)$ is preserved setwise. Equation [\[eq:matrix\]](#eq:matrix){reference-type="eqref" reference="eq:matrix"} first gives $d=1$ and $b\in\{0,1\}$; if $b=1$, the image of $v$ has first coordinate $6$, outside the pair, so $b=0$. The image of $(1,0,0)$ can only be the named order-nine point $(1,0,0)$ or $(4,2,0)$; the latter would map $(4,2,0)$ to the absent point $(7,1,0)$. Hence $a=1,c=0$.

For $X$, its unique point with dyadic coordinate one first forces the dyadic translation to vanish. Write the affine map as $\varphi(q)=Aq+t$. The sum of the ten distinct points is $(0,0,1)$; every automorphism fixes the unique order-two element, and preservation of the set therefore gives the explicit affine sum identity $$(0,0,1)=\sum_{q\in X}\varphi(q)
 =A\!\left(\sum_{q\in X}q\right)+10t
 =A(0,0,1)+10t=(0,0,1)+10t.$$ Thus $10t=0$ in the odd factors (the dyadic component was already shown to vanish). Since $10\equiv1$ modulo both $9$ and $3$, the odd translation also vanishes. Reducing the order-nine points modulo three gives $T=\{(1,0),(1,2),(2,1),(2,2)\}$; checking the six possible induced $(c,d)$ pairs forces $c=0,d=1$, and the remaining representatives force $a=1,b=0$. Thus both stabilizers are trivial.

# Exact overlap census

The complete occurrence-overlap histogram is

::: {#tab:multiset}
      $O$      0      1      2     3     4     5     6    7
  ------- ------ ------ ------ ----- ----- ----- ----- ----
    count   1435   1339   1068   771   621   265   134   87
      $O$      8      9     10    11    12    13    14   16
    count     26     29     35     7    10     2     2    1

  : Occurrence overlap over all $5832$ affine maps.
:::

The distinct-point intersection histogram, in contrast, is $$\begin{array}{c|rrrrrrrrrr}
|X\cap\varphi(X)|&0&1&2&3&4&5&6&7&8&10\\\hline
\text{count}&1435&1346&1139&929&628&275&63&14&2&1.
\end{array}$$ The identity is the unique occurrence overlap $16$. The largest nonidentity value is $14$, attained exactly by $$(x,y,z)\mapsto(4x,2x+y,z),
 \qquad (x,y,z)\mapsto(7x,x+y,z),$$ whose distinct-point overlap is $8$.

# Symmetry boundary and conclusion

C73's minimal-generation hypergraph on sixteen labels has abstract automorphism order $$6!\,2!\,2!\,5!=345600.$$ C74 proves that no nonidentity affine map of the actual named core permutes the named point set. These are different structures: the first permutes combinatorial labels while the second acts on points of a fixed finite abelian group. After the point map is fixed, duplicate labels admit the bookkeeping fiber $5!\,2!\,2!=480$; this is not an affine stabilizer.

The producer, independent 54-point checker, alternate matrix/image cross-check, clean replay, and hostile mutations certify the census. All claims remain confined to the frozen named presentation.
