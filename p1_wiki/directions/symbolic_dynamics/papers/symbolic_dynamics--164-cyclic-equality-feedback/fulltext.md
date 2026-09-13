---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--164-cyclic-equality-feedback"
canonical_tex: "symbolic_dynamics/papers/164-cyclic-equality-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/164-cyclic-equality-feedback/main.pdf"
source_sha256: "6a589c778137cb6e039f7a01710e7264686c6952321f0494ee3c992bfcda4218"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cyclic Equality-Feedback Dynamics at Dyadic Lengths

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/164-cyclic-equality-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/164-cyclic-equality-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/164-cyclic-equality-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/164-cyclic-equality-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/164-cyclic-equality-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $q\geq3$ and a dyadic length $n\geq4$. We iterate on $q$-ary cyclic words the local rule which records whether adjacent letters are equal. The first step is nonlinear and $q$-ary, whereas the tail is the affine complement of periodic Rule 102. After assigning zero contribution credit to the additive cellular automaton, repeated-root code weights, and the cycle chromatic polynomial, we determine the remaining finite atlas. It contains a sharp height $n+1$, all depth shells, the complete image staircase, and every target fibre as a $q$-weighted affine-code enumerator. Two slices of that inverse atlas are evaluated completely: time two is classified by the smaller weight in a complementary solution pair, and time $n/2+1$ by a half-word weight. Their parameter-class multiplicities are explicit, including possible collisions of numerical fibre values. An exact audit checks all words and targets in six boxes and the two special spectra through length $16$.
author:
- Anonymous
bibliography:
- references.bib
title: 'Cyclic Equality-Feedback Dynamics at Dyadic Lengths'
```

## Markdown 正文

# Object, prior boundary, and theorem

Let $\mathcal A_q=\{0,\ldots,q-1\}$ and index coordinates by $\mathbb Z/n\mathbb Z$. Define $$\label{eq:T}
 T_q(w)_i=\mathbf 1\{w_i=w_{i+1}\},\qquad w\in\mathcal A_q^n.$$ Thus $T_q(w)$ is binary after one step. Let $S$ denote cyclic shift on $\mathbb F_2^n$ and put $D=I+S$.

The linear tail is classical. Periodic additive cellular automata and their matrix powers are treated in [@MartinOdlyzkoWolfram1984; @Kim2011]; in particular, the Rule--102 power-of-two vanishing mechanism is not claimed here. Repeated-root cyclic-code weight distributions are also available in substantially greater generality [@ZhaoEtAl2025]. Equality-pattern cellular automata occur in other carriers [@BolognesiCiancia2017]. We therefore give no contribution credit to $D$, its kernels and images, homogeneous code enumerators, finite Fourier inversion, or the chromatic polynomial of a cycle. The scoped object is the interface between the literal $q$-ary rule [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} and that zero-credit tail.

For $w\in\mathcal A_q^n$, define its change mask $$c(w)_i=\mathbf 1\{w_i\ne w_{i+1}\}.$$ For $0\leq j\leq n$ and $d\in\mathbb F_2^n$, write $$\begin{aligned}
 W_{j,d}(a)&=\sum_{\substack{c\in\mathbb F_2^n\\D^jc=d}}a^{\operatorname{wt}(c)},
 \label{eq:affine-enum}\\
 C_{n,j}(q)&=W_{j,0}(q-1)+(q-1)W_{j,0}(-1).
 \label{eq:Cnj}\end{aligned}$$

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} Let $q\geq3$ and $n=2^m\geq4$.

(A) The all-one word is the unique recurrent point. Every nonconstant $w$ has depth $$\label{eq:depth}
     1+\min\{j\geq0:D^jc(w)=0\},$$ while the other $q-1$ constant words have depth one. The height is exactly $n+1$. The depth-zero and depth-one shells have sizes $1$ and $q-1$; for $1\leq j\leq n$, the depth-$(j+1)$ shell has size $$\label{eq:shell}
     C_{n,j}(q)-C_{n,j-1}(q).$$ At every dyadic $j<n$, $$\label{eq:checkpoint}
     C_{n,j}(q)=\bigl(1+(q-1)^{n/j}\bigr)^j+(q-1)2^j,$$ and the last shell has size $$\label{eq:last}
     \frac{q^n-(q-2)^n}{2}-(q-1)2^{n-1}>0.$$

(B) The first image has size $2^n-n$. For $t\geq2$, put $j=\min(t-1,n)$. Then $$\label{eq:image}
     \operatorname{im}T_q^t=\boldsymbol 1+\operatorname{im}D^j,\qquad |\operatorname{im}T_q^t|=2^{n-j}.$$ For a binary target $y$, with $d=y+\boldsymbol 1$, $$\label{eq:fibre}
     |(T_q^t)^{-1}(y)|=W_{j,d}(q-1)+(q-1)W_{j,d}(-1),
     \qquad j=\min(t-1,n),$$ and every nonbinary target has fibre zero at positive time.

(C) At time two, a target occurs exactly when $d=y+\boldsymbol 1$ has even weight. If $Dc=d$ and $\rho(d)=\min\{\operatorname{wt}(c),n-\operatorname{wt}(c)\}$, then $$\label{eq:t2}
     |(T_q^2)^{-1}(y)|=(q-1)^{\rho(d)}+(q-1)^{n-\rho(d)}
           +2(q-1)(-1)^{\rho(d)}.$$ For $r<n/2$, precisely $\binom nr$ supported targets have parameter $r$; for $r=n/2$, precisely $\frac12\binom n{n/2}$ do.

(D) At time $n/2+1$, a target occurs exactly when $d=y+\boldsymbol 1=(u,u)$. If $h=\operatorname{wt}(u)$, then $$\label{eq:mid}
    \begin{split}
     |(T_q^{n/2+1})^{-1}(\boldsymbol 1+d)|={}&
     \bigl(1+(q-1)^2\bigr)^{n/2-h}\bigl(2(q-1)\bigr)^h\\
     &+(q-1)2^{n/2}(-1)^h.
    \end{split}$$ Exactly $\binom{n/2}{h}$ supported targets have parameter $h$.

The multiplicities in parts (C) and (D) are parameter-class multiplicities. Equal numerical fibre values from different parameters must be merged. For example, at $n=4,q=4$, the $r=1,2$ values in [\[eq:t2\]](#eq:t2){reference-type="eqref" reference="eq:t2"} coincide.

# The nonlinear interface and temporal clock

[\[lem:chi\]]{#lem:chi label="lem:chi"} For $c\in\mathbb F_2^n$ of weight $r$, the number of $q$-ary cyclic words with change mask $c$ is $$\label{eq:chi}
 \chi_q(c)=(q-1)^r+(-1)^r(q-1).$$ It vanishes exactly at $r=1$.

Contract every equality edge of the cyclic word. If $r>0$, the remaining quotient is a cycle with $r$ edges, whose proper $q$-colourings are counted by the right-hand side of [\[eq:chi\]](#eq:chi){reference-type="eqref" reference="eq:chi"}. If $r=0$, all letters are equal and both sides equal $q$. For $q\geq3$, the asserted zero set follows immediately.

[\[lem:tail\]]{#lem:tail label="lem:tail"} For every $t\geq1$, $$\label{eq:iterate}
 T_q^t(w)=\boldsymbol 1+D^{t-1}c(w).$$ Moreover $D^n=0$, $\dim\ker D^j=j$, and $\operatorname{im}D^j=\ker D^{n-j}$ for $0\leq j\leq n$.

The first identity at $t=1$ is the definition. For a binary word $b$, equality is the complement of XOR, so $T_q(b)=\boldsymbol 1+Db$. Since $D\boldsymbol 1=0$, induction proves [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}. Identifying cyclic words with $\mathbb F_2[x]/(x^n-1)$ identifies $D$ with multiplication by $1+x$. Dyadicity gives $x^n-1=(x+1)^n$, so multiplication by $x+1$ is one nilpotent Jordan block. The remaining assertions follow.

Lemma [\[lem:tail\]](#lem:tail){reference-type="ref" reference="lem:tail"} gives the pointwise depth formula and absorption by time $n+1$. Summing Lemma [\[lem:chi\]](#lem:chi){reference-type="ref" reference="lem:chi"} over $\ker D^j$ gives [\[eq:Cnj\]](#eq:Cnj){reference-type="eqref" reference="eq:Cnj"}; consecutive kernel differences give [\[eq:shell\]](#eq:shell){reference-type="eqref" reference="eq:shell"}. When $j$ is dyadic, $D^j=I+S^j$ and the kernel consists of $j$ freely chosen bits repeated $n/j$ times. Its weight enumerator is $(1+a^{n/j})^j$, which yields [\[eq:checkpoint\]](#eq:checkpoint){reference-type="eqref" reference="eq:checkpoint"}.

Finally $\ker D^{n-1}$ is the even-weight hyperplane, whereas $\ker D^n=\mathbb F_2^n$. The $q$-weighted mass of the complementary odd-weight class is $$\frac{q^n-(q-2)^n}{2}-(q-1)2^{n-1},$$ where the second term is the signed correction from [\[eq:chi\]](#eq:chi){reference-type="eqref" reference="eq:chi"}. It is positive for $q\geq3,n\geq4$: writing $x=q-1\geq2$ and expanding the odd part gives $$\frac{(x+1)^n-(x-1)^n}{2}-x2^{n-1}
 \geq x\bigl(nx^{n-2}-2^{n-1}\bigr)
 \geq x2^{n-2}(n-2)>0.$$ This proves sharpness. Since every state is absorbed and $\boldsymbol 1$ is fixed, it is the sole recurrent point.

# Images and arbitrary target fibres

At time one, Lemma [\[lem:chi\]](#lem:chi){reference-type="ref" reference="lem:chi"} says that exactly the complements of the $n$ unit masks are absent, giving $2^n-n$. For $t\geq2$, every affine class of $\ker D^j$ contains a feasible change mask: the only forbidden masks are units. Here $1\leq j\leq n$ and $D\boldsymbol 1=0$, hence $\boldsymbol 1\in\ker D^j$, including when $j=n$. If a chosen representative is a unit $e_i$, then $e_i+\boldsymbol 1$ has the same $D^j$-image and weight $n-1\geq3$; Lemma [\[lem:chi\]](#lem:chi){reference-type="ref" reference="lem:chi"} therefore makes it a feasible change mask. Every affine class consequently contains a feasible representative, proving [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}.

For a fixed change mask $c$, Lemma [\[lem:chi\]](#lem:chi){reference-type="ref" reference="lem:chi"} is its exact source multiplicity. Summing it over $D^jc=d$ gives [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. For completeness, character orthogonality also gives the computable expression $$\label{eq:fourier}
 W_{j,d}(a)=2^{-n}\sum_{\lambda\in\mathbb F_2^n}(-1)^{\lambda\cdot d}
 (1+a)^{n-\operatorname{wt}((D^j)^T\lambda)}
 (1-a)^{\operatorname{wt}((D^j)^T\lambda)}.$$ Equation [\[eq:fourier\]](#eq:fourier){reference-type="eqref" reference="eq:fourier"} is a verification device, not a separate contribution claim.

The arbitrary-target formula is exact but does not by itself classify the dependence on $d$. The next section evaluates two slices rather than hiding that dependence inside a transform.

# Two evaluated fibre spectra

The image of $D$ is the even-weight hyperplane and its kernel is $\{0,\boldsymbol 1\}$. Thus a feasible equation $Dc=d$ has the complementary pair $\{c,c+\boldsymbol 1\}$. Substituting their two weights into [\[eq:chi\]](#eq:chi){reference-type="eqref" reference="eq:chi"} gives [\[eq:t2\]](#eq:t2){reference-type="eqref" reference="eq:t2"}; the parity of $\rho(d)$ agrees with both complementary weights because $n$ is even. Complementary pairs of smaller weight $r<n/2$ are indexed by all weight-$r$ masks. At $r=n/2$ each pair is indexed twice. This proves the two class counts. Their sum is $2^{n-1}$, and the class-weighted fibre mass is $q^n$.

In characteristic two, $D^{n/2}=(I+S)^{n/2}=I+S^{n/2}$. Hence its image consists exactly of duplicated half-words $d=(u,u)$. For a coordinate pair $(i,i+n/2)$, a zero bit of $u$ requires equal mask bits and contributes $1+a^2$ to $W_{n/2,d}(a)$; a one bit requires unequal mask bits and contributes $2a$. Therefore $$W_{n/2,d}(a)=(1+a^2)^{n/2-h}(2a)^h.$$ Evaluation at $a=q-1$ and $a=-1$ in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} gives [\[eq:mid\]](#eq:mid){reference-type="eqref" reference="eq:mid"}. Choosing the $h$ nonzero coordinates of $u$ gives the class multiplicity, whose sum is $2^{n/2}$; weighted fibre mass again sums to $q^n$.

# Exact controls and limitations

The paper-local audit begins with the literal rule [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}, not the linearized formulas. It exhausts the six boxes $$(n,q)=(4,3),(4,4),(4,5),(4,6),(8,3),(8,4),$$ comprising $74{,}355$ words, and checks every orbit, depth shell, image, and binary target fibre. It separately checks both parameter-class spectra for $n\in\{4,8,16\}$ and $q\in\{3,4,5,7\}$, including numerical-collision aggregation, mass conservation, and the excluded boundaries $q=2$, $n=2$, and nondyadic $n=6$.

The restrictions matter. At $q=2$, the feasible change masks differ; at $n=2$, the support repair by complementary masks fails; at nondyadic length, $D$ need not be nilpotent. Nothing here claims a classification for those regimes, a new theorem about Rule 102, a new repeated-root code enumerator, or absolute novelty. The result is an internally verified, owner-thin finite atlas. External posting, circulation, or submission remains `HOLD_EXTERNAL`.

## Data and code statement {#data-and-code-statement .unnumbered}

No external dataset or training data are used. The exact verifier and its deterministic transcript accompany the paper.

## Conflict-of-interest statement {#conflict-of-interest-statement .unnumbered}

The anonymous author declares no conflict of interest.
