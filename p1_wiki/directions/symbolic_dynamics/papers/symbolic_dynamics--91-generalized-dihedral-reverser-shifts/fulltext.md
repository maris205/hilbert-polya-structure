---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--91-generalized-dihedral-reverser-shifts"
canonical_tex: "symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts/main.pdf"
source_sha256: "3e90a8652933a1739557153c700e0f9c01e1d2c14a969ac8856e6ed7ed6ce69d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Reverser Shifts on Generalized Dihedral Groups: Cubic Zeta Compression and Two-Period Rigidity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/91-generalized-dihedral-reverser-shifts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $A$ be a finite abelian group and $G=\operatorname{Dih}(A)=A\rtimes\{\pm1\}$. We form a one-step shift on alphabet $G$ by declaring $g\to h$ when $hgh^{-1}=g^{-1}$. Write $N=|A|$, $t=|A[2]|$, and $c=N/t$. We prove that the shift is mixing and that its entire $2N$-state adjacency spectrum depends only on $(N,t)$. When $N>t$, the characteristic polynomial is $$\lambda^{2N-c-2}(\lambda-t)^{c-1}
   \bigl(\lambda^3-2t\lambda^2+t(t-N)\lambda-Nt(N-t)\bigr).$$ Thus its zeta function is controlled by one repeated linear factor and a cubic. In particular, $$\#\operatorname{Fix}(\sigma)=N+t,\qquad
   \#\operatorname{Fix}(\sigma^2)=t(3N+t).$$ These first two counts recover $(N,t)$. Conversely, an explicit cosetwise graph model shows that equal parameter pairs give isomorphic relation graphs. Hence two shifts in the family are conjugate exactly when their pairs $(|A|,|A[2]|)$ agree. Nonisomorphic groups, for example $\mathbb Z/9\mathbb Z$ and $(\mathbb Z/3\mathbb Z)^2$, therefore produce the same symbolic system. Exact group-law enumeration checks the quotient, spectrum, periods, and collapse on the registered finite families.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: 'Reverser Shifts on Generalized Dihedral Groups: Cubic Zeta Compression and Two-Period Rigidity'
```

## Markdown 正文

# Introduction

An element $h$ reverses $g$ when conjugation by $h$ sends $g$ to $g^{-1}$. Reversing symmetries are standard in group-theoretic approaches to dynamics; their structural setting is developed, for example, by Baake and Roberts [@BaakeRoberts2006]. Generalized dihedral groups are a basic source of such involutory behavior. Their commuting graphs have also been studied directly [@KakkarRawat2018].

This note asks a different symbolic question. Instead of forming an undirected commuting graph, we use the directed local relation $hgh^{-1}=g^{-1}$ as the adjacency rule of a one-dimensional shift of finite type. A small-group calculation gives two immediate anomalies: the adjacency matrix has very low rank, and nonisomorphic abelian groups with the same order and the same size of their two-torsion subgroup give identical graphs.

We close these observations for every finite abelian $A$. The contributions are:

1.  a canonical row-and-coset model depending only on $(N,t)=(|A|,|A[2]|)$;

2.  mixing and unique maximal entropy measure for every member;

3.  a complete characteristic polynomial, periodic-point formula, and rational zeta function compressed to a cubic factor;

4.  family rigidity from only the first two periodic counts.

The concepts of reversing elements, generalized dihedral groups, equitable spectral compression, and finite-type zeta functions are prior tools [@BaakeRoberts2006; @GodsilRoyle2001; @LindMarcus1995]. The residual object is the particular directed reverser relation and its exact symbolic package. A bounded search through 28 August 2026 found no exact-system collision under the relation and parameter keywords recorded in the package audit. That is not an exhaustive priority search, and no absolute priority claim is made.

# The relation shift

Write $A$ additively and let $$G=\operatorname{Dih}(A)=A\rtimes\{0,1\},\qquad
 (a,\epsilon)(b,\eta)
 =\bigl(a+(-1)^\epsilon b,\epsilon+\eta\bmod2\bigr).$$ Elements $(a,0)$ are rotations and $(a,1)$ are reflections. Put $$T=A[2]=\{a\in A:2a=0\},\qquad N=|A|,\quad t=|T|,\quad c=N/t.$$ Since $T$ is a subgroup, $t$ divides $N$ and $c$ is a positive integer.

Let $M_A$ be the zero--one matrix indexed by $G$ with $$M_A(g,h)=1\quad\Longleftrightarrow\quad hgh^{-1}=g^{-1}.$$ The reverser shift is $$X_A=\{x\in G^{\mathbb Z}:M_A(x_i,x_{i+1})=1\text{ for every }i\},$$ with left shift $\sigma$.

The local relation is directed: the role of the state being reversed and the role of its reverser are not interchangeable in the definition.

[\[lem:rows\]]{#lem:rows label="lem:rows"} The outgoing neighbors have the following form.

1.  If $g=(a,0)$ with $a\in T$, every element of $G$ follows $g$.

2.  If $g=(a,0)$ with $a\notin T$, precisely the $N$ reflections follow $g$.

3.  If $g=(a,1)$, its successors are the $t$ rotations $(y,0)$ with $y\in T$ and the $t$ reflections $(y,1)$ with $y\in a+T$.

Conjugation by a rotation fixes every rotation, while conjugation by a reflection inverts every rotation. This gives the first two statements. For a reflection, direct multiplication gives $$(y,0)(a,1)(y,0)^{-1}=(a+2y,1),$$ and $$(y,1)(a,1)(y,1)^{-1}=(2y-a,1).$$ Every reflection is an involution, so equality with $(a,1)^{-1}=(a,1)$ requires $2y=0$ in the first display and $2(y-a)=0$ in the second.

[\[prop:mixing\]]{#prop:mixing label="prop:mixing"} Every $X_A$ is a mixing shift of finite type. It therefore has a unique measure of maximal entropy.

Every reflection has the identity rotation among its successors. Every non-two-torsion rotation reaches a reflection and then the identity, while a two-torsion rotation already lies in that class. Conversely, the identity rotation has every group element as a successor. The graph is strongly connected. The identity rotation also has a loop, so the graph period is one and its adjacency matrix is primitive. The maximal-measure conclusion is the standard Parry theorem [@Parry1964].

# Canonical collapse and spectrum

Partition the vertices into the $t$ two-torsion rotations $R_T$, the $N-t$ remaining rotations $R_U$, and the reflections. Further partition the reflections into the $c$ cosets of $T$ in $A$. By [\[lem:rows\]](#lem:rows){reference-type="ref" reference="lem:rows"}, the graph is canonically described as follows:

-   every vertex of $R_T$ points to all $2N$ vertices;

-   every vertex of $R_U$ points to all reflections;

-   every reflection in coset $C$ points to all of $R_T$ and all reflections in $C$.

In particular, the graph depends only on $(N,t)$.

We use the row action on column functions, $(M_Af)(g)=\sum_hM_A(g,h)f(h)$. On functions constant on the three coarse classes, the adjacency action is represented by $$\label{eq:Q}
 Q_{N,t}=
 \begin{pmatrix}
  t&N-t&N\\
  0&0&N\\
  t&0&t
 \end{pmatrix}.$$

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} If $N>t$, then $$\label{eq:charpoly}
 \det(\lambda I-M_A)
 =\lambda^{2N-c-2}(\lambda-t)^{c-1}
 \bigl(\lambda^3-2t\lambda^2+t(t-N)\lambda-Nt(N-t)\bigr).$$ In particular, $\operatorname{rank}M_A=c+2$. If $N=t$, then $M_A$ is the $2N$ by $2N$ all-ones matrix, so its characteristic polynomial is $\lambda^{2N-1}(\lambda-2N)$.

Assume $N>t$. Vectors whose coordinate sum is zero within $R_T$, within $R_U$, or within any single reflection coset are killed by $M_A$. Their direct sum, denoted $V_0$, has dimension $$(t-1)+(N-t-1)+c(t-1)=2N-c-2.$$ Next take the space $V_t$ of functions that vanish on all rotations and are constant with value $\alpha_i$ on the $i$th reflection coset, where $\sum_i\alpha_i=0$. [\[lem:rows\]](#lem:rows){reference-type="ref" reference="lem:rows"} shows that $M_A$ multiplies this $(c-1)$-dimensional space by $t$. Finally, let $V_Q$ be the three-dimensional space of functions constant on $R_T$, on $R_U$, and on the union of all reflections. These three invariant spaces are mutually disjoint and their dimensions sum to $$(2N-c-2)+(c-1)+3=2N.$$ Thus $\mathbb C^G=V_0\oplus V_t\oplus V_Q$, and the action on $V_Q$ is $Q_{N,t}$. Direct expansion gives $$\det(\lambda I-Q_{N,t})
 =\lambda^3-2t\lambda^2+t(t-N)\lambda-Nt(N-t).$$ The cubic has nonzero constant term because $N>t$, so $Q_{N,t}$ has rank three. Since $t>0$, the action on $V_t$ is invertible. The zero action on $V_0$ therefore gives rank $(c-1)+3=c+2$, as well as the factorization. If $N=t$, every element of $A$ has order at most two, $G$ is abelian of exponent two, and every pair satisfies the relation; hence $M_A$ is all ones.

For $N>t$, the entropy is $\log\rho_{N,t}$, where $\rho_{N,t}$ is the Perron root of the cubic factor in [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}. The full-shift endpoint has entropy $\log(2N)$.

# Periodic points, zeta, and two-count rigidity

Let $F_k(A)=\#\operatorname{Fix}(\sigma^k)=\operatorname{tr}(M_A^k)$. The spectral decomposition gives, for $N>t$, $$\label{eq:allfix}
 F_k(A)=(c-1)t^k+\operatorname{tr}(Q_{N,t}^k).$$

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} For $N>t$, the Artin--Mazur zeta function of the shift is $$\label{eq:zeta}
 \zeta_{X_A}(z)
 =\frac{1}{(1-tz)^{c-1}
 \left[1-2tz+t(t-N)z^2-Nt(N-t)z^3\right]}.$$ At the full-shift endpoint $N=t$, $$\label{eq:zeta-endpoint}
 \zeta_{X_A}(z)=\frac1{1-2Nz}.$$ Moreover, for every $N,t$, including $N=t$, $$\label{eq:firsttwo}
 F_1=N+t,\qquad F_2=t(3N+t).$$

For an SFT, $\zeta(z)=\det(I-zM_A)^{-1}$ [@LindMarcus1995]. Substitution of [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}, or direct evaluation of the determinant on the invariant decomposition, gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. If $N=t$, the all-ones matrix has one eigenvalue $2N$ and all others zero, proving [\[eq:zeta-endpoint\]](#eq:zeta-endpoint){reference-type="eqref" reference="eq:zeta-endpoint"}.

For $N>t$, $\operatorname{tr}Q_{N,t}=2t$ and $\operatorname{tr}(Q_{N,t}^2)=2t(N+t)$. Adding the $(c-1)$ copies of the eigenvalue $t$ gives $$F_1=(c-1)t+2t=N+t,
 \qquad
 F_2=(c-1)t^2+2t(N+t)=t(3N+t).$$ The same formulas reduce to $(2N)$ and $(2N)^2$ when $N=t$.

[\[thm:rigidity\]]{#thm:rigidity label="thm:rigidity"} For finite abelian groups $A$ and $B$, $$X_A\cong X_B
 \quad\Longleftrightarrow\quad
 (|A|,|A[2]|)=(|B|,|B[2]|).$$ The reverse implication is realized by a one-block conjugacy induced by a relation-graph isomorphism.

A conjugacy preserves every periodic count. Put $S=F_1=N+t$. By [\[eq:firsttwo\]](#eq:firsttwo){reference-type="eqref" reference="eq:firsttwo"}, $t$ solves $$\label{eq:quadratic}
 2x^2-3Sx+F_2=0.$$ The genuine root is a positive integer and satisfies $t\leq N$, hence $t\leq S/2$. The other root is $3S/2-t\geq S$, so it cannot satisfy the same bound. Thus $t$ is recovered uniquely and $N=S-t$. Conjugate shifts therefore have the same $(N,t)$.

Conversely, the canonical description preceding [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} uses only the sizes $t$, $N-t$, and $c$ reflection fibers of size $t$. Choose bijections between the two $R_T$ classes and the two $R_U$ classes, choose a bijection between their sets of reflection cosets, and then choose a bijection inside each paired coset. The three adjacency bullets show entry by entry that the result is a directed graph isomorphism, hence a one-block conjugacy.

For example, $A=\mathbb Z/9\mathbb Z$ and $B=(\mathbb Z/3\mathbb Z)^2$ are nonisomorphic, but both have $(N,t)=(9,1)$, so their reverser shifts are conjugate. The symbolic system forgets the abelian group structure beyond order and two-torsion size.

# Exact controls and scope

The accompanying Python program independently implements the semidirect product, inverse, conjugation, and relation graph for 20 product-of-cyclic presentations. It compares every canonical adjacency entry, explicitly checks the zero, $t$, and quotient invariant spaces, checks rank and strong connectivity, verifies traces through period ten, computes small characteristic and zeta polynomials, reconstructs $(N,t)$ from $(F_1,F_2)$, and tests nonisomorphic same-parameter collapses both at $(N,t)=(9,1)$ and $(16,4)$.

These finite computations guard the group-law convention and all endpoint formulas; they are not evidence for claims beyond the proofs. The classification is only inside this reverser-shift family. It does not classify generalized dihedral groups, reversing symmetry groups, commuting graphs, or arbitrary group-relation SFTs. External release and priority claims remain on hold.
