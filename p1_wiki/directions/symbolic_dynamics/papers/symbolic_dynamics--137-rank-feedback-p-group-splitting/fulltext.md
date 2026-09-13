---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--137-rank-feedback-p-group-splitting"
canonical_tex: "symbolic_dynamics/papers/137-rank-feedback-p-group-splitting/main.tex"
canonical_pdf: "symbolic_dynamics/papers/137-rank-feedback-p-group-splitting/main.pdf"
source_sha256: "ee654e1de7900435356ec258761c58603aa8b028eccad1c3d9020a907c5a89a9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rank-Feedback Splitting of Finite Abelian $p$-Groups: A Sharp Triangular Clock and Exact Target Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/137-rank-feedback-p-group-splitting>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/137-rank-feedback-p-group-splitting/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/137-rank-feedback-p-group-splitting/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/137-rank-feedback-p-group-splitting/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/137-rank-feedback-p-group-splitting/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a finite abelian $p$-group $G$, let $d(G)$ be its minimum number of generators and iterate $$\mathsf F(G)=p^{d(G)}G\oplus G[p^{d(G)}].$$ If $G$ has partition type $\lambda=(a_1,\ldots,a_r)$, the induced rule keeps each $a_i\leq r$ and splits each $a_i>r$ into $(r,a_i-r)$. We prove that the recurrent types are exactly the fixed types $a_1\leq r$ and give their ordinary generating function. More sharply, for every type of order $p^n$ and initial rank $r_0$, a transient of length $d$ satisfies $n\geq r_0(d+1)+\binom d2$. Consequently the maximum transient length is $$\left\lceil\frac{\sqrt{8n+1}-3}{2}\right\rceil,$$ and the unique type attaining it is the cyclic type $(n)$, whose whole orbit is explicit. Finally, a bounded-coefficient formula counts the one-step fibre over every target partition and yields a necessary and sufficient image criterion. The classification of finite abelian groups, cyclic kernel/image formulas, torsion terminology, and Gaussian-binomial partition enumeration are assigned zero contribution credit. Exact enumeration is used only for falsification, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Rank-Feedback Splitting of Finite Abelian $p$-Groups: A Sharp Triangular Clock and Exact Target Fibres'
```

## Markdown 正文

# The literal operator and complete statement

Fix a prime $p$. Let $\mathcal A_{p,n}$ be the set of isomorphism classes of finite abelian groups of order $p^n$. For $G\in\mathcal A_{p,n}$ put $$d(G)=\dim_{\mathbb F_p}(G/pG),\qquad
 G[p^s]=\{g\in G:p^sg=0\},$$ and define $$\label{eq:group-map}
                      \mathsf F(G)=p^{d(G)}G\oplus G[p^{d(G)}].$$ The direct sum in [\[eq:group-map\]](#eq:group-map){reference-type="eqref" reference="eq:group-map"} is external. The zero group is fixed by convention.

Write $\mathcal P_n$ for the integer partitions of $n$. Parts are decreasing, $\ell(\lambda)$ is their number, and $m_j(\lambda)$ is the multiplicity of $j$. Put $\operatorname T_t=t(t+1)/2$. The *entry time* $\tau(\lambda)$ is the least $t\geq0$ for which the $t$th iterate is recurrent.

For later use, fix a target $\mu\in\mathcal P_n$ of length $L$ and write $m_j=m_j(\mu)$. For $$\left\lceil\frac L2\right\rceil\leq r\leq L,
             \qquad c_r=L-r,$$ if $m_r\geq c_r$, define $$\label{eq:q-and-h}
 q_j^{(r)}=m_j-c_r\mathbf 1_{\{j=r\}},\qquad
 h_r=\sum_{j>r}q_j^{(r)},$$ and set $$\label{eq:Ar}
 A_r(\mu)=
 \begin{cases}
 [u^{c_r-h_r}]\displaystyle\prod_{j=1}^{r}
       (1+u+\cdots+u^{q_j^{(r)}}),&m_r\geq c_r,\ h_r\leq c_r,\\
 0,&\text{otherwise}.
 \end{cases}$$

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq1$, the following statements hold.

1.  Under the usual type bijection $$\lambda=(a_1,\ldots,a_r)\longleftrightarrow
     G_\lambda=\bigoplus_{i=1}^{r}C_{p^{a_i}},$$ the group operator [\[eq:group-map\]](#eq:group-map){reference-type="eqref" reference="eq:group-map"} is the weight-preserving partition map $$\label{eq:type-map}
     \mathsf F(\lambda)=\operatorname{sort}
     \left(\biguplus_{a_i\leq r}\{a_i\}
           \uplus\biguplus_{a_i>r}\{r,a_i-r\}\right).$$ In particular, its type dynamics is independent of $p$.

2.  A type $\lambda=(a_1,\ldots,a_r)$ is recurrent if and only if it is fixed, if and only if $a_1\leq r$. If $f_n$ counts fixed types and $f_0=1$, then, as a formal power series, $$\label{eq:fixed-ogf}
     \sum_{n\geq0}f_nz^n
       =1+\sum_{r\geq1}z^r
           \genfrac{[}{]}{0pt}{}{2r-1}{r}_{\!z}.$$

3.  If $\lambda\vdash n$ has initial length $r_0$ and entry time $d$, then $$\label{eq:pointwise-clock}
                             n\geq r_0(d+1)+\binom d2.$$ The exact maximum and its unique maximizer are $$\label{eq:sharp-clock}
     \max_{\lambda\vdash n}\tau(\lambda)
      =D(n):=\left\lceil\frac{\sqrt{8n+1}-3}{2}\right\rceil,
     \qquad \tau(\lambda)=D(n)\Longleftrightarrow\lambda=(n).$$ Moreover, for $0\leq t\leq D(n)$, $$\label{eq:deep-orbit}
     \mathsf F^t((n))=\operatorname{sort}(n-\operatorname T_t,t,t-1,\ldots,1),$$ where the list after $n-\operatorname T_t$ is empty when $t=0$.

4.  The fibre over every target, including a target outside the image, is $$\label{eq:fibre-formula}
     |\mathsf F^{-1}(\mu)|=
     \sum_{r=\lceil L/2\rceil}^{L}A_r(\mu).$$ The corresponding exact image criterion is $$\label{eq:image-criterion}
     \mu\in\operatorname{im}\mathsf F
     \quad\Longleftrightarrow\quad
     \text{some }r\in[\lceil L/2\rceil,L]\text{ satisfies }
     m_r\geq L-r\text{ and }\sum_{j>r}m_j\leq L-r.$$

# From groups to a feedback split

The classification and cyclic decomposition of finite abelian groups are standard; see, for example, Fuchs [@Fuchs2015]. We nevertheless include the short calculation that fixes the literal map and all conventions.

[\[prop:type\]]{#prop:type label="prop:type"} The operator [\[eq:group-map\]](#eq:group-map){reference-type="eqref" reference="eq:group-map"} preserves group order and induces [\[eq:type-map\]](#eq:type-map){reference-type="eqref" reference="eq:type-map"}.

For $G_\lambda=\bigoplus_{i=1}^rC_{p^{a_i}}$ one has $G_\lambda/pG_\lambda\cong\mathbb F_p^r$, and $r$ generators visibly suffice. Hence $d(G_\lambda)=r$. On one cyclic factor, $$\begin{aligned}
\label{eq:cyclic-pieces}
 p^rC_{p^a}&\cong C_{p^{\max(a-r,0)}},&
 C_{p^a}[p^r]&\cong C_{p^{\min(a,r)}},\end{aligned}$$ with an exponent zero denoting the trivial factor. Thus $a\leq r$ yields one exponent $a$, while $a>r$ yields exponents $r$ and $a-r$. Direct sums commute with both constructions, proving [\[eq:type-map\]](#eq:type-map){reference-type="eqref" reference="eq:type-map"}.

Multiplication by $p^r$ also gives an exact sequence $$0\longrightarrow G[p^r]\longrightarrow G
   \longrightarrow p^rG\longrightarrow0.$$ Therefore $|p^rG|\,|G[p^r]|=|G|$, so [\[eq:group-map\]](#eq:group-map){reference-type="eqref" reference="eq:group-map"} indeed remains in $\mathcal A_{p,n}$.

Both [\[eq:cyclic-pieces\]](#eq:cyclic-pieces){reference-type="eqref" reference="eq:cyclic-pieces"} and the order identity are classical inputs, not contribution claims. The dynamics begins only when their exponent $r$ is fed back from the current state.

# Fixed and recurrent types

For a type $\lambda$ of length $r$, set $$\label{eq:split-count}
                         c(\lambda)=|\{i:a_i>r\}|.$$ Every such part splits into two and every other part remains one part, so $$\label{eq:rank-rise}
                  \ell(\mathsf F(\lambda))=r+c(\lambda).$$

[\[prop:recurrent\]]{#prop:recurrent label="prop:recurrent"} A partition is recurrent precisely when $c(\lambda)=0$, equivalently when $a_1\leq\ell(\lambda)$, and all recurrent types are fixed.

If $c(\lambda)=0$, [\[eq:type-map\]](#eq:type-map){reference-type="eqref" reference="eq:type-map"} leaves every part unchanged. If $c(\lambda)>0$, [\[eq:rank-rise\]](#eq:rank-rise){reference-type="eqref" reference="eq:rank-rise"} strictly increases the length. A partition of $n$ has length at most $n$, so every orbit eventually reaches a fixed type. Strict length increase also prevents a nonfixed state from lying on a directed cycle.

Fix the length $r$. A fixed type has exactly $r$ positive parts, all at most $r$. Subtracting one from every part produces a Ferrers diagram in an $r$-by-$(r-1)$ rectangle, with zero rows allowed. Its size enumerator is the Gaussian polynomial $\genfrac{[}{]}{0pt}{}{2r-1}{r}_{z}$. Restoring the removed column shifts the weight by $r$ and gives the $r$th summand of [\[eq:fixed-ogf\]](#eq:fixed-ogf){reference-type="eqref" reference="eq:fixed-ogf"}. The initial $1$ is the empty type. Rectangle enumeration by Gaussian polynomials is standard partition theory [@Andrews1984] and receives zero credit here.

# Frozen markers and the unique sharp clock

Let $$\lambda^{(0)}\longmapsto\lambda^{(1)}\longmapsto\cdots
 \longmapsto\lambda^{(d)}$$ be an orbit segment in which the first $d$ states are nonfixed and the last is fixed. Write $r_t=\ell(\lambda^{(t)})$ and $c_t=c(\lambda^{(t)})$ for $0\leq t<d$.

[\[lem:budget\]]{#lem:budget label="lem:budget"} For every such segment, $$\label{eq:marker-budget}
 n\geq r_0+\sum_{t=0}^{d-1}c_tr_t
   \geq r_0(d+1)+\binom d2.$$

Temporarily tag the $r_0$ initial parts. Within each tag, distinguish one positive *residual*. When a residual part $a>r_t$ splits, designate the new part $r_t$ as a marker and retain $a-r_t>0$ as that tag's residual. Unsplit parts remain residuals. The map never merges parts.

Equation [\[eq:rank-rise\]](#eq:rank-rise){reference-type="eqref" reference="eq:rank-rise"} gives $r_{t+1}=r_t+c_t>r_t$. Hence a marker of size $r_t$ is at most every later rank and can never split later. At time $d$ there are consequently $c_t$ disjoint permanent markers of weight $r_t$ from each transition $t$, plus one positive residual for every initial tag. Their weights give the first inequality in [\[eq:marker-budget\]](#eq:marker-budget){reference-type="eqref" reference="eq:marker-budget"}.

Since every $c_t\geq1$, the rank recurrence implies $r_t\geq r_0+t$. Therefore $$r_0+\sum_{t=0}^{d-1}c_tr_t
 \geq r_0+\sum_{t=0}^{d-1}(r_0+t)
 =r_0(d+1)+\binom d2,$$ which proves the second inequality.

[\[thm:clock\]]{#thm:clock label="thm:clock"} Equations [\[eq:pointwise-clock\]](#eq:pointwise-clock){reference-type="eqref" reference="eq:pointwise-clock"}--[\[eq:deep-orbit\]](#eq:deep-orbit){reference-type="eqref" reference="eq:deep-orbit"} hold.

Taking $r_0\geq1$ in Lemma [\[lem:budget\]](#lem:budget){reference-type="ref" reference="lem:budget"} gives $$n\geq\operatorname T_d+1,$$ so $\operatorname T_d<n$. The largest integer with that strict inequality is $D(n)$ in [\[eq:sharp-clock\]](#eq:sharp-clock){reference-type="eqref" reference="eq:sharp-clock"}; equivalently $\operatorname T_{D(n)}<n\leq\operatorname T_{D(n)+1}$. This proves the universal upper bound and the displayed radical form.

Starting from $(n)$, suppose $0\leq t<D(n)$ and [\[eq:deep-orbit\]](#eq:deep-orbit){reference-type="eqref" reference="eq:deep-orbit"} holds. Its length is $t+1$, its parts $t,t-1,\ldots,1$ are already at most that length, and $$n-\operatorname T_t>t+1$$ because $\operatorname T_{t+1}<n$. Thus only $n-\operatorname T_t$ splits, into $(t+1,n-\operatorname T_{t+1})$, proving the next instance of [\[eq:deep-orbit\]](#eq:deep-orbit){reference-type="eqref" reference="eq:deep-orbit"}. At $t=D(n)$, the reverse inequality $n\leq\operatorname T_{D(n)+1}$ says that $n-\operatorname T_{D(n)}\leq D(n)+1$; all parts are then at most the rank, so this state is fixed. Hence $(n)$ attains the bound.

Finally, suppose a type of length $r_0\geq2$ had entry time $D=D(n)$. The pointwise bound would give $$n\geq2(D+1)+\binom D2=\operatorname T_{D+1}+1,$$ contrary to $n\leq\operatorname T_{D+1}$. Thus every maximizer has $r_0=1$, and the only partition of $n$ with one part is $(n)$. This also covers $n=1$, for which $D(n)=0$.

# Every-target fibres and the image

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} The fibre formula [\[eq:fibre-formula\]](#eq:fibre-formula){reference-type="eqref" reference="eq:fibre-formula"} and image criterion [\[eq:image-criterion\]](#eq:image-criterion){reference-type="eqref" reference="eq:image-criterion"} hold for every $\mu\vdash n$.

Fix a source rank $r$, and let $c$ of its $r$ parts exceed $r$. Each of those $c$ parts contributes a marker $r$ and one positive remainder; every other source part is unchanged. Hence the target length is $L=r+c$. Since $0\leq c\leq r$, the possible source ranks are exactly in $[\lceil L/2\rceil,L]$, with $c=c_r=L-r$.

For one such $r$, the target must contain at least $c_r$ copies of $r$. Remove those marker copies. The residual multiset has counts $q_j^{(r)}$ and exactly $r$ parts. Every residual part greater than $r$ must have come from a split source part, so all $h_r$ such copies are forced remainders. Among the copies of sizes $1,\ldots,r$, choose another $c_r-h_r$ remainders. If $s_j$ copies of size $j$ are chosen, then $$0\leq s_j\leq q_j^{(r)},\qquad
 \sum_{j=1}^{r}s_j=c_r-h_r.$$ The number of such multiplicity vectors is exactly the coefficient in [\[eq:Ar\]](#eq:Ar){reference-type="eqref" reference="eq:Ar"}.

The reconstruction is explicit: combine every selected remainder $j$ with one removed marker to make the source part $r+j>r$, and retain each unselected residual part as an unsplit source part. It produces $c_r$ large and $r-c_r$ small source parts, hence a source of rank $r$. The construction and marker removal are inverse, and different source ranks are disjoint. Summing over $r$ proves [\[eq:fibre-formula\]](#eq:fibre-formula){reference-type="eqref" reference="eq:fibre-formula"}.

It remains to read positivity. If $m_r\geq c_r$ and $h_r\leq c_r$, then there are $r-h_r$ residual copies of size at most $r$, and $$0\leq c_r-h_r\leq r-h_r$$ because $c_r\leq r$. Thus a choice exists, so $A_r(\mu)>0$. Conversely, a preimage necessarily supplies both the $c_r$ markers and at most $c_r$ large residuals. Since $h_r=\sum_{j>r}m_j$, these are precisely the two conditions in [\[eq:image-criterion\]](#eq:image-criterion){reference-type="eqref" reference="eq:image-criterion"}.

# Ownership boundary and exact controls

All classical structure is subtracted. The finite abelian $p$-group classification, $d(G)=\dim_{\mathbb F_p}G/pG$, and the cyclic formulas [\[eq:cyclic-pieces\]](#eq:cyclic-pieces){reference-type="eqref" reference="eq:cyclic-pieces"} are standard group theory [@Fuchs2015]. Delaunay and Jouhet use partition-indexed finite abelian groups and $p^\ell$-torsion statistics in a different probabilistic and combinatorial setting [@DelaunayJouhet2014]; that torsion machinery is prior art, not part of the residual claim. Ferrers diagrams, Gaussian polynomials, and formal coefficient extraction are likewise standard [@Andrews1984]. Existing iterated maps on partitions include multiplicity-description and continued-fraction-type systems [@EliahouErickson2013; @BaalbakiEtAl2024]. They do not supply ownership clearance for the present map, and their general partition-dynamics language receives zero credit.

The residual package is limited to the conjunction for the literal state-dependent operator [\[eq:group-map\]](#eq:group-map){reference-type="eqref" reference="eq:group-map"}: the monotone feedback split, pointwise marker budget, unique sharp triangular clock, and all-target one-step inverse decoder. Internally, this is not P126's synchronous balanced refinement of ordered compositions: there the threshold is fixed, the split is nearly halving, and the main result concerns complete iterate kernels. It is not P135's derived-centralizer multiplicity rule, which has mergers and genuine two-cycles, and it is not P115's linear Cartier/Frobenius coefficient dynamics. Merely sharing splitting, partition, or finite algebraic vocabulary transfers no theorem.

The paper-local exact audit constructs literal cyclic kernels and images, enumerates every partition through weight $50$, compares the fixed counts with an independent Gaussian recurrence, and checks [\[eq:fibre-formula\]](#eq:fibre-formula){reference-type="eqref" reference="eq:fibre-formula"} and [\[eq:image-criterion\]](#eq:image-criterion){reference-type="eqref" reference="eq:image-criterion"} over every target through weight $35$. A bounded source audit did not locate the exact literal operator or theorem conjunction. This non-hit is not novelty, priority, or authorship evidence; external status is `HOLD_EXTERNAL`.

::: {#tab:controls}
  control                                   exact count
  -------------------------------------- --------------
  partition states, all $n\leq50$             1,295,970
  target fibre cells, all $n\leq35$              81,155
  zero-fibre targets among those cells           30,923
  literal cyclic cells / base elements     176 / 10,350
  fixed-OGF coefficients                             51
  exact assertions                           18,504,770

  : Dependency-free exact controls. Enumeration is falsification evidence only, not an all-weight proof or an ownership certificate.
:::
