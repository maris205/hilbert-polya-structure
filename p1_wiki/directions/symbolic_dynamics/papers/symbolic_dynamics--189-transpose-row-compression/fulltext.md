---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--189-transpose-row-compression"
canonical_tex: "symbolic_dynamics/papers/189-transpose-row-compression/main.tex"
canonical_pdf: "symbolic_dynamics/papers/189-transpose-row-compression/main.pdf"
source_sha256: "c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Four-Iterate Collapse and Exact Fibres for Transpose--Row-Compression Dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/189-transpose-row-compression>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/189-transpose-row-compression/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/189-transpose-row-compression/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/189-transpose-row-compression/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/189-transpose-row-compression/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Left-compress every row of a labelled binary square matrix and transpose the result, then feed the output back into the same rule. We determine the complete functional graph. If $r$ is the labelled row-sum vector, successive column-height vectors are $r$, its threshold conjugate $r^*$, and its decreasing rearrangement $r^\downarrow$; hence $F^4=F^2$. The recurrent states are exactly the Ferrers matrices, where $F$ acts by partition conjugation. There are $\binom{2n}{n}$ recurrent states, $2^n$ fixed states, and $(\binom{2n}{n}-2^n)/2$ strict two-cycles. We give the exact three depth populations, including a weighted-partition formula for depth at most one. Independently, we determine every time-one and time-two target fibre, with zero-fibre criteria, and obtain image sizes $(n+1)^n$ and $\binom{2n}{n}$. The one-dimensional boundary is entirely fixed. Ferrers diagrams, conjugation, and line-sum theory receive no contribution credit; the retained iterative conjunction is [owner\_amber / hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Four-Iterate Collapse and Exact Fibres for\
  Transpose--Row-Compression Dynamics
```

## Markdown 正文

# The literal map and the subtraction boundary

Fix $n\geq1$, write $[n]=\{1,\ldots,n\}$, and let $\mathcal X_n=\{0,1\}^{n\times n}$. Rows and columns retain their displayed labels. For $A\in\mathcal X_n$, put $$r_j(A)=\sum_{k=1}^n A_{jk},\qquad
 r(A)=(r_1(A),\ldots,r_n(A)).$$ The transpose--row-compression map is $$\label{eq:map}
 F(A)_{ij}=\mathbf1\{i\leq r_j(A)\},\qquad i,j\in[n].$$ Thus one first moves every $1$ in source row $j$ to the left without changing that row's sum, and then transposes. Equivalently, source row $j$ becomes an initial column of height $r_j(A)$. The rule is synchronous, deterministic, and total on the labelled carrier.

Binary matrices with prescribed line sums and generalized conjugate sequences are classical [@Miller2013; @KouteckyOnn2020]; Ferrers matrices and bigraphs are established objects [@DasDasSen2016]; and partition conjugation and diagonal hooks are standard [@Andrews1998]. We assign all of that material, as well as generic finite-map bookkeeping, zero contribution credit. The scoped object here is only the repeated literal map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} and the conjunction of its exact clock and target-local inverse laws. A bounded owner search did not locate that conjunction. This non-hit is not novelty or priority evidence, and external circulation remains on hold.

For a height vector $h=(h_1,\ldots,h_n)\in\{0,\ldots,n\}^n$, define $$\label{eq:diagram-star}
 D(h)_{ij}=\mathbf1\{i\leq h_j\},\qquad
 h_i^*=\#\{j:h_j\geq i\}\quad(i\in[n]).$$ Write $h^\downarrow$ for the decreasing rearrangement of $h$. The transform $h^*$ is always a partition in the $n\times n$ square, padded with zeros. Let $\mathcal P_n$ be the set of all such partitions.

# The four-iterate normal form

The distinction between the labelled vector $h$ and its rearrangement is essential at the first epoch.

[\[lem:height\]]{#lem:height label="lem:height"} The map $D$ is injective and $$\label{eq:height-calculus}
 r(D(h))=h^*,\qquad (h^*)^*=h^\downarrow.$$ For $\lambda\in\mathcal P_n$, the operation $\lambda\mapsto\lambda^*$ is ordinary Ferrers conjugation and is an involution.

The initial run of ones in column $j$ recovers $h_j$, proving injectivity. Row $i$ of $D(h)$ has a one precisely in the columns with $h_j\geq i$, which proves the first identity. Threshold counts do not depend on coordinate order, so $h^*=(h^\downarrow)^*$. Reflecting the Ferrers diagram of the partition $h^\downarrow$ across its diagonal proves the second identity and the final assertion.

[\[thm:normal\]]{#thm:normal label="thm:normal"} For $A\in\mathcal X_n$, let $r=r(A)$. Then $$\begin{aligned}
 F(A)&=D(r),& F^2(A)&=D(r^*),\label{eq:first-second}\\
 F^3(A)&=D(r^\downarrow),& F^4(A)&=D(r^*)=F^2(A).\label{eq:third-fourth}\end{aligned}$$ Consequently, for every $q\geq1$, $$F^{2q}(A)=D(r^*),\qquad F^{2q+1}(A)=D(r^\downarrow).$$

Equation [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is $F(A)=D(r(A))$. Apply Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} successively: $$F^2(A)=D(r^*),\qquad
 F^3(A)=D((r^*)^*)=D(r^\downarrow).$$ Since threshold counts ignore rearrangement, $(r^\downarrow)^*=r^*$, giving $F^4(A)=D(r^*)$. Reapplying $F$ alternates the last two matrices.

For example, every matrix with row-sum vector $(1,3,0)$ follows the height trajectory $$A\longmapsto D(1,3,0)\longmapsto D(2,1,1)
 \longleftrightarrow D(3,1,0).$$ Thus neither $F^2=F$ nor $F^3=F$ holds in general, despite the shallow universal bound.

# Recurrent states and exact depth layers

Depth means distance to the recurrent set; a strict two-cycle is an orbit of two distinct states. Put $$\label{eq:weighted-partitions}
 W_n=\sum_{\lambda\in\mathcal P_n}\prod_{i=1}^n\binom n{\lambda_i}
 =[z^n]\prod_{k=0}^n\frac{1}{1-\binom nk z}.$$ The coefficient identity records the multiplicities of the $n+1$ possible parts.

[\[thm:functional\]]{#thm:functional label="thm:functional"} The recurrent states are exactly $D(\lambda)$ for $\lambda\in\mathcal P_n$, and $$\label{eq:recurrent-action}
                 F(D(\lambda))=D(\lambda^*).$$ Hence the recurrent, fixed, and strict-two-cycle counts are $$\label{eq:cycle-counts}
 \binom{2n}{n},\qquad 2^n,\qquad
 \frac12\left(\binom{2n}{n}-2^n\right).$$ The exact depth sets are $$\begin{aligned}
 L_0&=\{D(\lambda):\lambda\in\mathcal P_n\},\\
 L_1&=\{A:r_1(A)\geq\cdots\geq r_n(A)\}\setminus L_0,\\
 L_2&=\{A:r_i(A)<r_{i+1}(A)\text{ for some }i<n\},\end{aligned}$$ with populations $$\label{eq:depth-counts}
 |L_0|=\binom{2n}{n},\quad
 |L_1|=W_n-\binom{2n}{n},\quad
 |L_2|=2^{n^2}-W_n.$$ For $n\geq2$ the height is exactly two. For $n=1$, both states are fixed, so the height is zero and the populations are $(2,0,0)$.

Theorem [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"} implies that every $F^2(A)$ is fixed by $F^2$. Conversely, if $A$ lies on a cycle, $F$ is invertible on that cycle, so cancelling $F^2$ from $F^4(A)=F^2(A)$ gives $F^2(A)=A$. The recurrent set is therefore $\operatorname{Fix}(F^2)$. Every second image is $D(\lambda)$ for the partition $\lambda=r(A)^*$. Conversely, Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} gives $F^2(D(\lambda))=D(\lambda)$, proving the characterization and [\[eq:recurrent-action\]](#eq:recurrent-action){reference-type="eqref" reference="eq:recurrent-action"}.

Partitions in the square are in bijection with monotone boundary paths having $n$ horizontal and $n$ vertical steps, hence there are $\binom{2n}{n}$. A recurrent matrix is fixed precisely when $\lambda=\lambda^*$. The diagonal hook lengths of a self-conjugate shape form an arbitrary subset of $\{1,3,\ldots,2n-1\}$, and this construction is reversible inside the square. Thus there are $2^n$ fixed states. Conjugation pairs all remaining shapes, which proves [\[eq:cycle-counts\]](#eq:cycle-counts){reference-type="eqref" reference="eq:cycle-counts"}.

It remains to distinguish depths one and two. The first image $D(r(A))$ is recurrent exactly when the *labelled* row-sum vector is decreasing. For a fixed decreasing vector $\lambda$, the supports of its rows can be chosen in $\prod_i\binom n{\lambda_i}$ ways. Summing proves that $W_n$ is the depth-at-most-one population and gives [\[eq:depth-counts\]](#eq:depth-counts){reference-type="eqref" reference="eq:depth-counts"}. A matrix with only $A_{1n}=1$ has depth one when $n\geq2$, whereas a matrix with only $A_{21}=1$ has depth two. This proves sharpness and all boundary claims.

# Every-target fibres at times one and two

The inverse laws retain labelled row assignment, which disappears from the forward partition quotient. For $\lambda\in\mathcal P_n$, let $m_k(\lambda)$ be the multiplicity of part $k$, including $k=0$.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} For an arbitrary target $B\in\mathcal X_n$, $$\label{eq:fibre-one}
 |F^{-1}(B)|=
 \begin{cases}
  \displaystyle\prod_{j=1}^n\binom n{h_j},&B=D(h),\\[3pt]
  0,&B\notin D(\{0,\ldots,n\}^n).
 \end{cases}$$ Consequently $|\operatorname{im}F|=(n+1)^n$.

At time two, let $\mu\in\mathcal P_n$, put $\lambda=\mu^*$, and use zero for every non-Ferrers target. Then $$\label{eq:fibre-two}
 |(F^2)^{-1}(D(\mu))|
 =\frac{n!}{\prod_{k=0}^n m_k(\lambda)!}
   \prod_{k=0}^n\binom nk^{m_k(\lambda)}.$$ Thus $|\operatorname{im}F^2|=\binom{2n}{n}$. Both formulas include the all-zero and all-one height boundaries and remain valid for $n=1$.

The equation $F(A)=B$ is possible precisely when every column of $B$ is an initial segment. In that case injectivity of $D$ gives $B=D(h)$ uniquely and forces source row $j$ to have sum $h_j$. Its support has $\binom n{h_j}$ choices, independently across labelled rows. This proves [\[eq:fibre-one\]](#eq:fibre-one){reference-type="eqref" reference="eq:fibre-one"}; arbitrary $h$ gives the first image count.

By [\[eq:first-second\]](#eq:first-second){reference-type="eqref" reference="eq:first-second"}, $F^2(A)=D(\mu)$ is equivalent to $r(A)^*=\mu$. Lemma [\[lem:height\]](#lem:height){reference-type="ref" reference="lem:height"} says equivalently that the decreasing rearrangement of $r(A)$ is $\lambda=\mu^*$. Assigning this multiset of parts to the labelled rows gives $n!/\prod_km_k(\lambda)!$ distinct row-sum vectors. For each assignment, independent row supports contribute $\prod_k\binom nk^{m_k(\lambda)}$. This proves [\[eq:fibre-two\]](#eq:fibre-two){reference-type="eqref" reference="eq:fibre-two"}. Finally, every partition $\mu$ occurs, and no other second target occurs, so the boundary-path count gives $|\operatorname{im}F^2|=\binom{2n}{n}$.

Summing either fibre law over its admissible targets recovers $2^{n^2}$. This mass identity is a check, not a derivation of the target-local formulas.

# Exact control, limitations, and declarations

The paper-local standard-library verifier is independent of the scouting implementation. It exhausts all $2^{n^2}$ matrices for $1\leq n\leq4$, constructs literal transitions entry by entry, and compares every target fibre with [\[eq:fibre-one\]](#eq:fibre-one){reference-type="eqref" reference="eq:fibre-one"}--[\[eq:fibre-two\]](#eq:fibre-two){reference-type="eqref" reference="eq:fibre-two"}. Separate partition-level controls reach $n=12$. Its complete boxes are:

    $n$   states   $|\operatorname{im}F|$   $|\operatorname{im}F^2|$   fixed   strict $2$-cycles   $|L_1|$   $|L_2|$
  ----- -------- ------------------------ -------------------------- ------- ------------------- --------- ---------
      1        2                        2                          2       2                   0         0         0
      2       16                        9                          6       4                   1         5         5
      3      512                       64                         20       8                   6       164       328
      4   65,536                      625                         70      16                  27    10,051    55,415

The audit also searches explicitly for and finds counterexamples to the false strengthenings $F^2=F$ and $F^3=F$, distinguishes labelled row order from its multiset, attacks columns with holes, and checks the $n=1$ boundary. It makes $5{,}336{,}613$ exact assertions. Finite computation is falsification pressure, not proof or ownership evidence.

The theorem depends on a square carrier, fixed labels, synchronous updating, and transposition after compression. Rectangular variants, sorting inside the literal update, asynchronous schedules, random kernels, and unlabelled quotients are outside scope. The bounded owner search leaves live ownership risk; status is [owner\_amber / hold\_external]{.smallcaps}, and no novelty, priority, or circulation claim is authorized.

#### Data availability.

No external data were used. The exact verifier and canonical transcript accompany the source.

#### Ethics statement.

The work uses no human participants, animals, personal data, or experiments requiring ethics approval.

#### CRediT author statement.

The anonymous author performed conceptualization, formal analysis, software, validation, and writing.

#### Competing interests.

The author declares no competing interests.

#### Funding.

No external funding is declared.

#### AI-use statement.

Generative AI assisted drafting and code generation. All mathematical, bibliographic, and artifact claims require human verification before external use.
