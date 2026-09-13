---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--175-diagonal-feedback-commutator"
canonical_tex: "symbolic_dynamics/papers/175-diagonal-feedback-commutator/main.tex"
canonical_pdf: "symbolic_dynamics/papers/175-diagonal-feedback-commutator/main.pdf"
source_sha256: "d660c01649ba648ab2cd915ab6bceacfef695789eb7856c1c7823dbce95cceb5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Diagonal-Feedback Commutators and Support-Colouring Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/175-diagonal-feedback-commutator>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/175-diagonal-feedback-commutator/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/175-diagonal-feedback-commutator/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/175-diagonal-feedback-commutator/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/175-diagonal-feedback-commutator/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $K=\mathbb F_q$ and iterate the state-feedback commutator $\Phi(A)=[\operatorname{Diag}(a_{11},\ldots,a_{nn}),A]$ on $\mathrm M_n(K)$, with the standard ordered basis fixed. The map satisfies $\Phi^2=0$, but its one-step inverse problem is nonuniform. We prove that a matrix $B$ is reachable precisely when its diagonal is zero and the undirected support graph of its off-diagonal entries is $q$-colourable. More strongly, every target fibre is an occupation-weighted proper-colouring sum. This gives closed graph sums for the image, a weak-composition formula for the kernel, and the complete functional graph: one fixed root, explicit depth-one leaves and branch vertices, and support-indexed depth-two leaves. The zero matrix uniquely maximizes the one-step fibre, and all later fibres and image sets are immediate. Classical matrix and group commutator theory and Potts--chromatic partition functions are treated as prior owner regions; the residual claim concerns only their exact conjunction for this literal self-map. External circulation remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Diagonal-Feedback Commutators and Support-Colouring Fibres'
```

## Markdown 正文

# Diagonal feedback and scope

Fix a prime power $q$, put $K=\mathbb F_q$, and let $$\label{eq:map}
 \Delta(A)=\operatorname{Diag}(a_{11},\ldots,a_{nn}),\qquad
 \Phi:\mathrm M_n(K)\longrightarrow\mathrm M_n(K),\qquad
 \Phi(A)=[\Delta(A),A].$$ The ordered basis is part of the definition: neither $\Delta$ nor $\Phi$ is similarity invariant. Entrywise, $$\label{eq:entry}
 \Phi(A)_{ij}=(a_{ii}-a_{jj})a_{ij}.$$ Thus the diagonal is erased after one step. The temporal clock is therefore short, yet [\[eq:entry\]](#eq:entry){reference-type="eqref" reference="eq:entry"} leaves a nonconstant inverse multiplicity which records how the input diagonal partitions the coordinate set.

This note makes a deliberately narrow claim. Additive commutators with prescribed diagonal behaviour belong to established matrix-commutator theory [@Young2021; @KadyrsizovaYerlanov2022]; images and fibres of classical commutator word maps have their own literature [@Baddeley1994; @LarsenLu2021]. Fixed-element triangular Engel equations are treated by Bier [@Bier2013]. In particular, the fixed-regular unitriangular commutator system catalogued as P119 in the accompanying programme---including its centralizer-coset fibres and filtration tree---is assigned no contribution credit here. Likewise, proper colourings and Potts/Tutte partition functions are prior combinatorial mechanisms [@Sokal2005], and their labelled occupation enumerator is controlled by Stanley's chromatic symmetric function [@Stanley1995]. What remains is the matrix-to-support reduction for every target of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} and the rooted functional graph forced by it; no novelty or priority conclusion is drawn from the bounded literature audit.

For a zero-diagonal $B\in\mathrm M_n(K)$, let $G_B$ be the simple graph on $[n]=\{1,\ldots,n\}$ in which $$\label{eq:support}
 \{i,j\}\in E(G_B)
 \quad\Longleftrightarrow\quad
 b_{ij}\ne0\ \text{ or }\ b_{ji}\ne0.$$ For a colouring $c:[n]\to K$, write $$n_\alpha(c)=|c^{-1}(\alpha)|,
 \qquad
 m(c)=\sum_{\alpha\in K}n_\alpha(c)\bigl(n_\alpha(c)-1\bigr).$$ Here $m(c)$ counts ordered pairs of distinct vertices of equal colour. For a simple graph $G$ define the occupation-marked proper-colouring sum $$\label{eq:partition}
 \mathcal P_{G,q}(X;\boldsymbol z)
 =\sum_{c\in\operatorname{Col}_q(G)}
 X^{m(c)}\prod_{\alpha\in K}z_\alpha^{n_\alpha(c)},$$ where $\operatorname{Col}_q(G)$ is the set of proper $K$-colourings of $G$. This polynomial is not proposed as a new graph invariant. In the standard $q$-state spin form of the multivariate Potts partition function on $K_n$, put $$v_{ij}=\begin{cases}
 -1,&\{i,j\}\in E(G),\\
 X^2-1,&\{i,j\}\notin E(G).
 \end{cases}$$ Then $$\label{eq:potts-owner}
 Z^{\rm Potts}_{K_n}\!\left(q,\{v_{ij}\}\right)
 =\sum_{c:[n]\to K}\prod_{i<j}
   \left(1+v_{ij}\mathbf1_{\{c_i=c_j\}}\right)
 =\mathcal P_{G,q}(X;\boldsymbol1).$$ A monochromatic edge of $G$ has factor zero, while each monochromatic nonedge has factor $X^2$; under properness there are $m(c)/2$ such unordered pairs. Also, $$X_G(z_1,\ldots,z_q,0,\ldots)
 =\sum_{c\in\operatorname{Col}_q(G)}\prod_{i=1}^n z_{c_i}$$ is the $q$-variable truncation of Stanley's chromatic symmetric function. The marked polynomial [\[eq:partition\]](#eq:partition){reference-type="eqref" reference="eq:partition"} is its deterministic coefficientwise transform multiplying occupation $\boldsymbol r$ by $X^{\sum_\alpha r_\alpha(r_\alpha-1)}$. Both graph-polynomial identities and their specializations receive zero contribution credit.

# Support colourings and every-target fibres

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For every $B\in\mathrm M_n(K)$, $$\label{eq:fibre}
 |\Phi^{-1}(B)|=
 \begin{cases}
  \mathcal P_{G_B,q}(q;\boldsymbol 1),&\operatorname{diag}(B)=0,\\
  0,&\operatorname{diag}(B)\ne0.
 \end{cases}$$ More precisely, for every occupation vector $\boldsymbol r=(r_\alpha)_{\alpha\in K}$, the number of sources in the fibre with $|\{i:a_{ii}=\alpha\}|=r_\alpha$ is the coefficient of $\boldsymbol z^{\boldsymbol r}$ in $\mathcal P_{G_B,q}(q;\boldsymbol z)$. Consequently, $$\label{eq:imagecriterion}
 B\in\operatorname{im}\Phi
 \quad\Longleftrightarrow\quad
 \operatorname{diag}(B)=0\ \text{ and }\ \chi(G_B)\le q,$$ and the fibre cardinality depends only on the undirected support $G_B$.

Every output has zero diagonal by [\[eq:entry\]](#eq:entry){reference-type="eqref" reference="eq:entry"}, proving the second line of [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Suppose now that $B$ has zero diagonal and freeze the prospective input diagonal as $c_i=a_{ii}$. For each ordered pair $i\ne j$ we must solve $$\label{eq:scalar}
 (c_i-c_j)a_{ij}=b_{ij}.$$ If $c_i\ne c_j$, there is exactly one solution. If $c_i=c_j$, there are $q$ solutions when $b_{ij}=0$ and none when $b_{ij}\ne0$. Hence the diagonal $c$ is admissible exactly when it is a proper colouring of $G_B$. For such a colouring, precisely $m(c)$ ordered off-diagonal entries are free, so it contributes $q^{m(c)}$ sources. Summing over $c$ proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}; retaining the monomial in [\[eq:partition\]](#eq:partition){reference-type="eqref" reference="eq:partition"} proves the marked assertion. Positivity of every summand then gives [\[eq:imagecriterion\]](#eq:imagecriterion){reference-type="eqref" reference="eq:imagecriterion"} and support-only dependence.

Write $\kappa_{n,q}=|\Phi^{-1}(0)|$ and $I_{n,q}=|\operatorname{im}\Phi|$.

[\[cor:counts\]]{#cor:counts label="cor:counts"} The zero matrix uniquely maximizes $|\Phi^{-1}(B)|$. Moreover, $$\begin{aligned}
 \kappa_{n,q}
 &=\sum_{\substack{(r_\alpha)_{\alpha\in K}\ge0\\
                    \sum_\alpha r_\alpha=n}}
   \binom{n}{(r_\alpha)_{\alpha\in K}}
   q^{\sum_\alpha r_\alpha(r_\alpha-1)},
   \label{eq:kappa}\\
 I_{n,q}
 &=\sum_{\substack{G\subseteq K_n\\\chi(G)\le q}}
   (q^2-1)^{|E(G)|}.
   \label{eq:image}\end{aligned}$$ The graphs in [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} are simple and labelled on $[n]$.

For $B=0$, the support graph is empty, so every colouring contributes; group these colourings by their labelled occupation vector to obtain [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"}. If $B\ne0$ has zero diagonal, then $G_B$ contains an edge. Its proper colourings form a strict subset of all colourings, while all weights $q^{m(c)}$ are positive. If $B$ has nonzero diagonal, its fibre is empty. Thus zero is the unique maximum.

For [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}, first choose the support $G$. It occurs precisely when $G$ is $q$-colourable. On every edge $\{i,j\}$, the ordered pair $(b_{ij},b_{ji})$ may be any nonzero vector in $K^2$, giving $q^2-1$ choices, independently across edges. Nonedges force both entries to zero.

At $X=q$, [\[eq:potts-owner\]](#eq:potts-owner){reference-type="eqref" reference="eq:potts-owner"} is exactly the unmarked target fibre in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, not merely a Potts analogy. The retained step is instead that the state-extracted diagonal turns every matrix inverse equation into this standard support-colouring evaluation, simultaneously for every target, and hence determines the functional graph below.

# The complete functional graph

[\[thm:graph\]]{#thm:graph label="thm:graph"} The map satisfies $\Phi^2=0$. Its functional graph is one rooted component with the zero matrix as its only periodic point and with a loop at the root. Its sharp height is $1$ for $n=1$ and $2$ for $n\ge2$. The depth layers have cardinalities $$\label{eq:depths}
 D_0=1,\qquad D_1=\kappa_{n,q}-1,\qquad
 D_2=q^{n^2}-\kappa_{n,q},$$ where $D_2=0$ when $n=1$.

Among the depth-one vertices, $I_{n,q}-1$ are branch vertices and $\kappa_{n,q}-I_{n,q}$ are leaves. For every nonempty $q$-colourable labelled graph $G$, there are $(q^2-1)^{|E(G)|}$ branch vertices with support $G$, and each has $\mathcal P_{G,q}(q;\boldsymbol1)$ depth-two leaf preimages. Equivalently, $$\label{eq:mass}
 \sum_{\substack{\varnothing\ne G\subseteq K_n\\\chi(G)\le q}}
 (q^2-1)^{|E(G)|}\mathcal P_{G,q}(q;\boldsymbol1)
 =q^{n^2}-\kappa_{n,q}.$$ For $t\ge0$ and any target $B$, $$\label{eq:alltime}
 |(\Phi^t)^{-1}(B)|=
 \begin{cases}
 1,&t=0,\\
 |\Phi^{-1}(B)|,&t=1,\\
 q^{n^2},&t\ge2\ \text{and }B=0,\\
 0,&t\ge2\ \text{and }B\ne0.
 \end{cases}$$ In particular, $\operatorname{im}\Phi^0=\mathrm M_n(K)$, $|\operatorname{im}\Phi|=I_{n,q}$, and $\operatorname{im}\Phi^t=\{0\}$ for $t\ge2$.

Every $C=\Phi(A)$ has zero diagonal. Therefore $\Delta(C)=0$ and $\Phi(C)=[0,C]=0$, proving $\Phi^2=0$. It follows that every orbit enters zero within two steps and that $\operatorname{im}\Phi\subseteq\ker\Phi$. A fixed point $A$ obeys $A=\Phi(A)=\Phi^2(A)=0$; the same collapse excludes every other periodic orbit.

The zero fibre is the kernel of the set map, of size $\kappa_{n,q}$, so it consists of the root and $\kappa_{n,q}-1$ nonzero depth-one vertices. All remaining $q^{n^2}-\kappa_{n,q}$ states have nonzero image and hence depth two, proving [\[eq:depths\]](#eq:depths){reference-type="eqref" reference="eq:depths"}. For $n=1$, every output is zero. If $n\ge2$, choose two diagonal entries of different colours and one off-diagonal entry nonzero; its image is nonzero, so height two occurs.

A nonzero depth-one vertex has predecessors exactly when it lies in the image. Thus the $I_{n,q}-1$ nonzero image points are precisely the branch vertices, leaving $\kappa_{n,q}-I_{n,q}$ leaves. The support census from Corollary [\[cor:counts\]](#cor:counts){reference-type="ref" reference="cor:counts"}, followed by Theorem [\[thm:fibre\]](#thm:fibre){reference-type="ref" reference="thm:fibre"}, gives the branching statement. Every predecessor of a nonzero image point has depth two and cannot itself lie in the image, so these predecessors are leaves. Summing them proves [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}. Finally $\Phi^2$ is the constant-zero map, which gives [\[eq:alltime\]](#eq:alltime){reference-type="eqref" reference="eq:alltime"} and the image tower.

Because every iterate has exactly one fixed point, the Artin--Mazur bookkeeping [@ArtinMazur1965] gives $$\label{eq:zeta}
 \zeta_\Phi(z)=\exp\!\left(\sum_{r\ge1}
 \frac{|\operatorname{Fix}(\Phi^r)|}{r}z^r\right)=\frac1{1-z}.$$

# Exact controls and limitations

An independent standard-library verifier enumerates every literal arrow and every codomain target in eleven boxes. It evaluates the marked fibre sum, tests support-only dependence and image membership, independently enumerates support graphs for [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}, evaluates [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"}, and checks the depth layers. The field implementation includes $\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)$, so the controls are not confined to prime fields. Representative boxes are shown below; $S=q^{n^2}$.

    $n$   $q$      $S$   $I_{n,q}$   $\kappa_{n,q}$   height
  ----- ----- -------- ----------- ---------------- --------
      1     4        4           1                4        1
      2     4      256          16               76        2
      3     2      512          37              152        2
      3     4   262144        4096            16984        2
      4     2    65536         829             8800        2

The settled transcript records $2{,}111{,}465$ assertions and a deterministic literal-edge digest. These finite calculations are falsification controls, not a substitute for the uniform proofs. The dynamics has a deliberately shallow clock, while its inverse axis lies in an owner-dense colouring region. The Potts specialization and chromatic-symmetric occupation inventory earn no standalone credit; only the literal matrix-to-support reduction and consequent rooted tree remain under evaluation. External circulation, novelty, priority, and submission therefore remain `HOLD_EXTERNAL`.
