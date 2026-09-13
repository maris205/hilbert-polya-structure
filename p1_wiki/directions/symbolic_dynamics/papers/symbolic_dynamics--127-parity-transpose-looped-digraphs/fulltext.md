---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--127-parity-transpose-looped-digraphs"
canonical_tex: "symbolic_dynamics/papers/127-parity-transpose-looped-digraphs/main.tex"
canonical_pdf: "symbolic_dynamics/papers/127-parity-transpose-looped-digraphs/main.pdf"
source_sha256: "ede8031b5c8fb5bf4e91de83977ccb41690df236c5f700d89469c2e293e971ea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Odd-Outdegree Transpose Dynamics on Looped Digraphs: Parity Collapse, Fibres, and Components

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/127-parity-transpose-looped-digraphs>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/127-parity-transpose-looped-digraphs/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/127-parity-transpose-looped-digraphs/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/127-parity-transpose-looped-digraphs/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/127-parity-transpose-looped-digraphs/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On a labelled looped digraph, reverse every arc and then toggle every ordered pair, loops included, inside the set of vertices of odd current outdegree. Equivalently, on $M_n(\mathbb F_2)$ we iterate $\Phi(A)=A^{\mathsf T}+(A\mathbf1)(A\mathbf1)^{\mathsf T}$. We prove that one step maps onto the even-total-parity hyperplane, which is the complete recurrent set, and that all recurrent periods divide four. Every codomain fibre has size $0$, $1$, or $2^{n-1}+1$, according to an explicit column-parity test. We then give exact formulas for fixed points, two- and four-cycles, depth-one states, and the finite dynamical zeta function. A second factorisation views the state-dependent left factor as the identity or an involutory transvection, versus a singular projection, and independently recovers the second and fourth iterates. Static graph complementation, binary-margin counting, and finite-map zeta bookkeeping are treated as background. The owner search is bounded; no novelty, priority, or external-release claim is made.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Odd-Outdegree Transpose Dynamics on Looped Digraphs:\
  Parity Collapse, Fibres, and Components
```

## Markdown 正文

# The update and its subtraction boundary

Fix $n\geq1$, work over $\mathbb F_2$, and let $\mathbf 1$ be the all-one column. A matrix $A\in M_n(\mathbb F_2)$ is the adjacency matrix of a labelled directed graph in which loops are allowed. Put $$r=A\mathbf 1,\qquad c=A^{\mathsf T}\mathbf 1,\qquad
 \tau=\mathbf 1^{\mathsf T}A\mathbf 1.$$ Thus $r$ and $c$ are the out- and indegree parity vectors and $\tau=\mathbf 1^{\mathsf T}r=\mathbf 1^{\mathsf T}c$ is total arc parity. Define $$\Phi(A)=A^{\mathsf T}+rr^{\mathsf T}.                 \label{eq:update}$$ The second summand toggles the complete looped subdigraph on the current odd-outdegree vertices. It is a rank-*at-most*-one correction and is recomputed after every step.

Local complementation and its binary-matrix formulation are classical [@Bouchet1993; @Traldi2012]; pivot and loop complementation have an established algebraic calculus [@BrijderHoogeboom2011]. Static subgraph complementation, including its rank and algorithmic interfaces, is also a separate mature operation [@BuchananEtAl2022; @KochPardalSantos2025]; see also [arXiv:2502.15675](https://arxiv.org/abs/2502.15675). Modular invariant rings for transpose group actions on full $2\times2$ matrix spaces form another neighboring, but static, interface [@ChenRen2026]. All such static operations and invariant rings, transpose, outer products, transvections, binary margin enumeration, and generic functional-graph bookkeeping receive zero contribution credit here. The residual question is only the exact temporal structure of the state-dependent update [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}.

The internal subtraction is equally strict. P102's involution-norm dynamics and P103's double-adjugation dynamics receive zero credit. P125 acts on pairs in a nonsingular quadratic space, has a quadratic/polar three-bit quotient, and permits tail two and period three. In contrast, the present carrier is all of $M_n(\mathbb F_2)$, its feasible row/column-margin quotient has dimension $2n-1$, its tail is at most one, and its recurrent periods are only $1,2,4$. Thus the literal systems are not conjugate; generic quotient, matrix, quadratic-map, cycle, fibre, component, and zeta packaging still receive zero credit. A bounded formula-and-owner search found no literal-map match; a bounded non-hit is not a novelty certificate.

# The parity quotient and all orbits

For $B=\Phi(A)$, write its margins as $r(B),c(B),\tau(B)$.

[\[lem:quotient\]]{#lem:quotient label="lem:quotient"} For every $A$, $$r(B)=c+\tau r,\qquad c(B)=(1+\tau)r,\qquad \tau(B)=0.   \label{eq:quotient}$$ Consequently the even-total hyperplane $\mathcal H_n=\{A:\tau(A)=0\}$ is invariant; on it the margin pair is swapped.

Multiplying [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} on the right by $\mathbf 1$ gives $r(B)=c+r(r^{\mathsf T}\mathbf 1)=c+\tau r$. Transposing first gives $c(B)=r+r(r^{\mathsf T}\mathbf 1)=(1+\tau)r$. Finally, $\tau(B)=\mathbf 1^{\mathsf T}(c+\tau r)=\tau+\tau^2=0$ in $\mathbb F_2$.

[\[thm:orbits\]]{#thm:orbits label="thm:orbits"} The image and complete recurrent set are both $\mathcal H_n$. Every state outside $\mathcal H_n$ has exact depth one. On $\mathcal H_n$, $$\Phi^2(A)=A+rr^{\mathsf T}+cc^{\mathsf T},
 \qquad \Phi^4(A)=A.                                  \label{eq:four}$$ If $r\ne c$, then $A$ has exact period four. If $r=c$, its period is one or two.

The last identity in [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"} shows that $\operatorname{im}\Phi\subseteq
\mathcal H_n$. The reverse inclusion follows from the explicit preimage in [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"}. On $\mathcal H_n$ the margins swap, so a second use of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} yields the first identity in [\[eq:four\]](#eq:four){reference-type="eqref" reference="eq:four"}; this added matrix has zero row and column margins. Repeating the same two steps cancels it in characteristic two, proving the second identity. Thus every point of $\mathcal H_n$ is recurrent. Every odd-total point reaches it after one step and cannot already be recurrent, proving exact depth one.

If $r\ne c$, then $rr^{\mathsf T}\ne cc^{\mathsf T}$ because the diagonal of $vv^{\mathsf T}$ is $v$; hence $\Phi^2(A)\ne A$, and the period is exactly four. If $r=c$, [\[eq:four\]](#eq:four){reference-type="eqref" reference="eq:four"} gives $\Phi^2(A)=A$.

Here depth means the least entrance time into the recurrent set. On a finite map this equals the distance to the first periodic point. The unique matrix in $M_0(\mathbb F_2)$ may separately be declared fixed; all remaining formulas assume $n\ge1$.

# Every one-step fibre and a second route

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} For every $B\in M_n(\mathbb F_2)$, $$|\Phi^{-1}(B)|=
 \begin{cases}
 0,&\tau(B)=1,\\
 1,&\tau(B)=0\text{ and }c(B)\ne0,\\
 2^{n-1}+1,&\tau(B)=0\text{ and }c(B)=0.
 \end{cases}                                           \label{eq:fibres}$$ In particular, $|\operatorname{im}\Phi|=2^{n^2-1}$, and precisely $2^{n(n-1)}$ image targets have the large fibre.

If a preimage has row margin $r$, solving [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} for it gives $A=B^{\mathsf T}+rr^{\mathsf T}$. Requiring $A\mathbf 1=r$ is equivalent to $$r=c(B)+(\mathbf 1^{\mathsf T}r)r.                           \label{eq:solve}$$ For even-weight $r$, this forces $r=c(B)$ and exists exactly when $\tau(B)=0$; it then supplies one preimage. For odd-weight $r$, [\[eq:solve\]](#eq:solve){reference-type="eqref" reference="eq:solve"} is equivalent to $c(B)=0$. In that case all $2^{n-1}$ odd vectors work, in addition to the even solution $r=0$. This proves [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"} and also $\operatorname{im}\Phi=\mathcal H_n$.

There are $2^{n-1}$ choices for each even-parity column, independently over $n$ columns, so exactly $2^{n(n-1)}$ matrices have $c(B)=0$.

The odd-total zero case in [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"} is essential. For example, when $n=1$, the target $[1]$ has nonzero column margin but no preimage.

[\[prop:factor\]]{#prop:factor label="prop:factor"} The update has the factorisation $$\Phi(A)=(I+r\mathbf 1^{\mathsf T})A^{\mathsf T}.            \label{eq:factor}$$ If $\tau=0$, the left factor is the identity when $r=0$ and an involutory transvection otherwise. If $\tau=1$, it is an idempotent rank-$n-1$ projection with kernel $\langle r\rangle$ and image $\mathbf 1^\perp$. Moreover, for $\tau=0$ the factor product independently gives $$\Phi^2(A)=(I+c\mathbf 1^{\mathsf T})A
              (I+\mathbf 1r^{\mathsf T})
           =A+cc^{\mathsf T}+rr^{\mathsf T},           \label{eq:factor-two}$$ and hence $\Phi^4(A)=A$.

Since $\mathbf 1^{\mathsf T}A^{\mathsf T}=r^{\mathsf T}$, [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} is [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. Put $L_r=I+r\mathbf 1^{\mathsf T}$. Direct multiplication gives $L_r^2=I+\tau r\mathbf 1^{\mathsf T}$, while $$\mathbf 1^{\mathsf T}L_r=(1+\tau)\mathbf 1^{\mathsf T},
 \qquad \det L_r=1+\tau.                              \label{eq:factor-rank}$$ Thus $L_r^2=I$ when $\tau=0$, with the stated identity/transvection distinction. When $\tau=1$, $L_r^2=L_r$ and $$L_rx=0\quad\Longleftrightarrow\quad
 x=r(\mathbf 1^{\mathsf T}x).$$ Here $r\ne0$, and $L_rr=0$, so $\ker L_r=\langle r\rangle$. Rank--nullity gives rank $n-1$; [\[eq:factor-rank\]](#eq:factor-rank){reference-type="eqref" reference="eq:factor-rank"} places the image in the $(n-1)$-dimensional space $\mathbf 1^\perp$, hence the two are equal.

It remains to obtain the temporal identity from the factors. Suppose $\tau=0$ and put $B=L_rA^{\mathsf T}$. Direct multiplication of this product by $\mathbf 1$ and of its transpose by $\mathbf 1$ gives row and column margins $c$ and $r$, respectively. Therefore $$\Phi^2(A)=L_cB^{\mathsf T}=L_cAL_r^{\mathsf T}.$$ Expanding the two factors gives [\[eq:factor-two\]](#eq:factor-two){reference-type="eqref" reference="eq:factor-two"}; its mixed term is $c(\mathbf 1^{\mathsf T}A\mathbf 1)r^{\mathsf T}=0$. Because $r$ and $c$ have even weight, the correction $cc^{\mathsf T}+rr^{\mathsf T}$ has zero row and column margins. The same factor-product calculation on $\Phi^2(A)$ adds that correction once more, proving $\Phi^4(A)=A$ in characteristic two.

Thus the factor route both identifies the singular odd-coset projection and recovers the even-coset temporal identities; the direct margin equation in [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"} is still needed to distinguish individual target fibres.

# Components and zeta function

[\[lem:margins\]]{#lem:margins label="lem:margins"} For $u,v\in\mathbb F_2^n$, there is a matrix with row margin $u$ and column margin $v$ exactly when $\mathbf 1^{\mathsf T}u=\mathbf 1^{\mathsf T}v$. In that case there are $2^{(n-1)^2}$ such matrices.

Choose the upper-left $(n-1)\times(n-1)$ entries freely. The prescribed row sums force the last entry of each of the first $n-1$ rows, and the prescribed column sums force the last entry of each of the first $n-1$ columns. The two requirements on the bottom-right corner agree precisely when the total parities agree.

Put $$F_n=2^{n(n-1)/2},\qquad
 C_{2,n}=\frac{2^{n(n-1)}-F_n}{2},\qquad
 C_{4,n}=\frac{2^{n^2-1}-2^{n(n-1)}}{4}.$$

[\[thm:census\]]{#thm:census label="thm:census"} The map has $F_n$ fixed points, $C_{2,n}$ two-cycles, and $C_{4,n}$ four-cycles. It has $2^{n^2-1}$ depth-one states. With the usual finite-map convention [@ArtinMazur1965], $$\zeta_{\Phi_n}(z)=
 (1-z)^{-F_n}(1-z^2)^{-C_{2,n}}(1-z^4)^{-C_{4,n}}.       \label{eq:zeta}$$

A fixed point satisfies $A+A^{\mathsf T}=rr^{\mathsf T}$. Comparing diagonals forces $r=0$; then $A$ is symmetric with zero row sums. Its off-diagonal entries are arbitrary and its diagonal is forced by the row sums, giving dimension $n(n-1)/2$ and hence $F_n$ fixed points.

By [\[lem:margins\]](#lem:margins){reference-type="ref" reference="lem:margins"}, for each of the $2^{n-1}$ even vectors $r$, there are $2^{(n-1)^2}$ recurrent matrices with margins $(r,r)$. Thus $2^{n(n-1)}$ recurrent points have period dividing two. Removing fixed points and dividing by two gives $C_{2,n}$. All remaining recurrent points have exact period four by [\[thm:orbits\]](#thm:orbits){reference-type="ref" reference="thm:orbits"}, giving $C_{4,n}$. The odd coset has size $2^{n^2-1}$ and consists exactly of the depth-one points. Finally, the standard product of one factor $(1-z^k)^{-1}$ per $k$-cycle gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

# Exact control and limitations

The accompanying deterministic verifier exhausts every one of the $2^{n^2}$ matrices for $1\le n\le4$. It checks both forms of the update, the quotient and fourth-iterate identities, exact depths and periods, all codomain fibres including zero fibres, the affine margin count, and every component formula. These bounded computations are counterexample searches, not proofs of the all-$n$ statements above.

The result is specific to the binary field, square matrices, transpose, and the recomputed row-margin selector. Rectangular carriers, other fields, other bilinear forms, and static graph complementation require new proofs and owner gates. Literature screening was bounded and can establish a hit but not an absence. Accordingly we make no claim of novelty, priority, authorship, posting readiness, or external release.
