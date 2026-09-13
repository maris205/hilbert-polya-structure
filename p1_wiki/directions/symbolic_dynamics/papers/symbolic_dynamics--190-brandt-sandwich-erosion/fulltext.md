---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--190-brandt-sandwich-erosion"
canonical_tex: "symbolic_dynamics/papers/190-brandt-sandwich-erosion/main.tex"
canonical_pdf: "symbolic_dynamics/papers/190-brandt-sandwich-erosion/main.pdf"
source_sha256: "73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Run Erosion and Exact Fibres for a Brandt Sandwich Map on Cyclic Words

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/190-brandt-sandwich-erosion>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/190-brandt-sandwich-erosion/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/190-brandt-sandwich-erosion/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/190-brandt-sandwich-erosion/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/190-brandt-sandwich-erosion/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $B_n=\{0\}\cup[n]^2$ be the aperiodic Brandt semigroup of matrix units. On cyclic words of length $m$, we study the parallel local map $T(x)_i=x_i x_{i+1}x_i$. A nonzero letter survives one step exactly when its successor is its inverse. We lift this local filter to an all-time normal form: a coordinate survives time $t$ precisely along a forward run of $t$ inverse-compatible edges. It follows that every orbit is eventually fixed, with $1+n$ fixed words for odd $m$ and $1+n^2$ for even $m$. Every pointwise tail is one plus a longest cyclic compatible run; for $n\geq2$ the sharp maximum is $m$ in odd length and $m-1$ in even length, while $n=1$ has maximum $\max\{0,m-1\}$. Independently, we determine every labelled one-step fibre as a cyclic transfer-matrix trace. Nonzero target letters pin adjacent source letters, reducing the trace to an explicit product of powers of one zero-output matrix across target gaps. We diagonalize that matrix, obtain a closed recurrence for the all-zero fibre, characterize the complete image, and verify total fibre mass. Exact enumeration in 26 finite boxes supplies 1,555,420 author-side regression assertions, not proof or novelty evidence. External ownership remains unresolved, so the manuscript is `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: Run Erosion and Exact Fibres for a Brandt Sandwich Map on Cyclic Words
```

## Markdown 正文

# The map and its subtraction boundary

For $n\geq1$, the aperiodic Brandt semigroup is $$\label{eq:brandt}
 B_n=\{0\}\cup\{(a,b):a,b\in[n]\},\qquad
 (a,b)(c,d)=\begin{cases}(a,d),&b=c,\\0,&b\ne c,\end{cases}$$ with zero absorbing. Put $(a,b)^*=(b,a)$ and $0^*=0$. Brandt semigroups and their identities are established algebraic objects [@Volkov2019]. The word "sandwich" also has an established use for a fixed-element variant $x*_a y=xay$ [@DesiaterykGanyushkin2024]; our outer letter varies with the site and is repeated on both sides.

Fix a cyclic length $m\geq1$, with indices in $\mathbb Z/m\mathbb Z$. The literal deterministic map on $B_n^m$ is $$\label{eq:update}
 (Tx)_i=x_i x_{i+1}x_i.$$ This is a right-sided nearest-neighbour cellular map on a finite cyclic carrier. Finite cyclic cellular-automaton transformation semigroups are standard background [@CastilloRamirezGadouleau2016]. Explicit iterates for local rules furnished by small associative semigroups are also known [@Fuks2025]. Here the binary local operation $(u,v)\mapsto uvu$ is not asserted to be a semigroup multiplication.

De Bruijn and path automata are standard tools for cellular images and preimages [@Salo2023]. We assign that machinery, Brandt identities, sandwich terminology, and generic support erosion zero contribution credit. The retained result is the conjunction of a parity-sensitive temporal classification and an explicit every-target inverse factorization for [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. Our owner search is bounded. A search non-hit is not a novelty or priority certificate, and a later literal or equivalent owner requires withdrawal or repositioning.

# All-time dynamics

For $x\in B_n^m$, define its cyclic compatibility indicators by $$\label{eq:good}
 g_i(x)=\boldsymbol{1}\{x_i\ne0\ \text{and}\ x_{i+1}=x_i^*\}.$$

[\[lem:filter\]]{#lem:filter label="lem:filter"} For $u,v\in B_n$, $$\label{eq:filter}
 uvu=\begin{cases}u,&u\ne0\text{ and }v=u^*,\\0,&\text{otherwise}.
 \end{cases}$$

The assertion holds when $u=0$. Let $u=(a,b)$ and $v=(c,d)$. The first product is nonzero exactly when $b=c$; the second multiplication is then nonzero exactly when $d=a$. Together these conditions give $v=(b,a)=u^*$, and the surviving product is $(a,b)=u$.

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} For every $t\geq0$, every $x\in B_n^m$, and every site $i$, $$\label{eq:iterate}
 (T^t x)_i=\begin{cases}
 x_i,&\displaystyle\prod_{j=0}^{t-1}g_{i+j}(x)=1,\\
 0,&\text{otherwise}.
 \end{cases}$$ The product is empty when $t=0$.

At $t=0$, equation [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} is the identity. Suppose it holds at time $t$. Lemma [\[lem:filter\]](#lem:filter){reference-type="ref" reference="lem:filter"} says that site $i$ survives the next update only if the time-$t$ letters at $i$ and $i+1$ both survive and are inverses. The induction hypothesis requires the edge blocks $i,\ldots,i+t-1$ and $i+1,\ldots,i+t$ to be good. Their union is $i,\ldots,i+t$, and its first edge supplies the inverse relation. When this condition holds, the output remains the original letter $x_i$; otherwise it is zero. This proves the claim at $t+1$.

[\[cor:fixed\]]{#cor:fixed label="cor:fixed"} Every recurrent state is fixed, and $$\label{eq:fixed}
 |\operatorname{Fix}(T)|=\begin{cases}1+n,&m\text{ odd},\\1+n^2,&m\text{ even}.
 \end{cases}$$

Theorem [\[thm:iterate\]](#thm:iterate){reference-type="ref" reference="thm:iterate"} makes the nonzero support nonincreasing and sends every non-all-good word to zero after at most $m$ steps, so a recurrent word is fixed. A fixed word with one nonzero letter must have every successor equal to the inverse of its predecessor; hence all letters are nonzero and alternate under $*$. Odd length forces the starting unit to be diagonal, giving $n$ choices, whereas even length permits all $n^2$ units. The all-zero word supplies the additional fixed point.

For a non-all-good cyclic binary word, let $L(x)$ denote the length of its longest cyclic run of good edges. Define the tail $\mu(x)$ as the least $t\geq0$ for which $T^t x$ is fixed.

[\[thm:tails\]]{#thm:tails label="thm:tails"} The all-zero and all-good words have tail zero. Every other word satisfies $$\label{eq:point-tail}
 \mu(x)=L(x)+1.$$ For $n\geq2$, $$\label{eq:max-tail}
 \max_x\mu(x)=\begin{cases}m,&m\text{ odd},\\m-1,&m\text{ even}.
 \end{cases}$$ For $n=1$, the maximum is $\max\{0,m-1\}$.

By Theorem [\[thm:iterate\]](#thm:iterate){reference-type="ref" reference="thm:iterate"}, some nonzero coordinate remains at time $L(x)$, while no coordinate remains at time $L(x)+1$. This proves [\[eq:point-tail\]](#eq:point-tail){reference-type="eqref" reference="eq:point-tail"}.

Assume $n\geq2$ and choose an off-diagonal unit $u$. When $m$ is odd, alternate $u,u^*$ along $m-1$ successive edges. The closing edge is the unique bad edge, so $L=m-1$. When $m$ is even, a word cannot have exactly one bad edge: traversing the other $m-1$ inverse relations forces the omitted relation as well. Thus $L\leq m-2$. Alternating along $m-2$ edges and then repeating $u$ produces two adjacent bad edges and attains this bound.

If $n=1$, write $e$ for the unique nonzero unit. The good edges are exactly the occurrences of $ee$. A mixed word has $L\leq m-2$, with equality for one zero followed cyclically by $m-1$ copies of $e$ when $m\geq2$. For $m=1$, both words are fixed.

[\[rem:boundaries\]]{#rem:boundaries label="rem:boundaries"} For $m=1$, the fixed states are $0$ and the $n$ diagonal units. The maximum tail is one for $n\geq2$ and zero for $n=1$. For $m=2$, the nonzero fixed words are $(u,u^*)$, one for each nonzero unit; every other word maps to $(0,0)$ in one step. These cases agree with Corollary [\[cor:fixed\]](#cor:fixed){reference-type="ref" reference="cor:fixed"} and Theorem [\[thm:tails\]](#thm:tails){reference-type="ref" reference="thm:tails"}.

# Every-target fibres and the image

Put $Q=B_n$, $q=n^2+1$, and for each output letter $y\in Q$ define the $q\times q$ zero-one matrix $$\label{eq:matrix}
 M_y(u,v)=\boldsymbol{1}\{uvu=y\}\qquad(u,v\in Q).$$ Rows represent the current source letter and columns the next source letter.

[\[thm:trace\]]{#thm:trace label="thm:trace"} For every target $y=(y_0,\ldots,y_{m-1})\in Q^m$, $$\label{eq:trace}
 |T^{-1}(y)|=\operatorname{tr}\bigl(M_{y_0}M_{y_1}\cdots M_{y_{m-1}}\bigr).$$

Expanding the trace gives a sum over cyclic source-letter paths $u_0,\ldots,u_{m-1}$ of $\prod_i M_{y_i}(u_i,u_{i+1})$. A product equals one exactly when $u_i u_{i+1}u_i=y_i$ at every site. These paths are precisely the source words in the labelled fibre.

Let $A=M_0$. Suppose a target has nonzero sites $i_1,\ldots,i_s$ in cyclic order. Let $h_j$ be the number of zero target sites strictly between $i_j$ and $i_{j+1}$, with $i_{s+1}=i_1$ cyclically.

[\[thm:gaps\]]{#thm:gaps label="thm:gaps"} If $s\geq1$, then $$\label{eq:gaps}
 |T^{-1}(y)|=\prod_{j=1}^s
 (A^{h_j})_{y_{i_j}^*,\,y_{i_{j+1}}}.$$ For $y=0^m$, the fibre is $\operatorname{tr}(A^m)$.

By Lemma [\[lem:filter\]](#lem:filter){reference-type="ref" reference="lem:filter"}, a nonzero output $y_i$ pins the adjacent source pair to $(y_i,y_i^*)$. Between two pinned pairs, every zero output inserts one transition of $A$. Multiplying the path counts across all cyclic gaps gives [\[eq:gaps\]](#eq:gaps){reference-type="eqref" reference="eq:gaps"}. With no pinned site, the cyclic path expansion is exactly $\operatorname{tr}(A^m)$.

The zero-output trace admits a closed form. Put $r=n^2$, and define $$\label{eq:recurrence}
 s_0=2,\qquad s_1=r,\qquad s_k=r s_{k-1}+s_{k-2}\quad(k\geq2).$$

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For every $m\geq1$, $$\label{eq:zero-fibre}
 |T^{-1}(0^m)|=s_m+(-1)^m\left(\frac{r+n}{2}-1\right)
 +\frac{r-n}{2}.$$ The spectrum of $A$ consists of the two roots of $z^2-rz-1$, together with $-1$ of multiplicity $(r+n)/2-1$ and $+1$ of multiplicity $(r-n)/2$.

The zero row of $A$ is all ones. A nonzero row indexed by $u$ is all ones except for a zero in column $u^*$. Let $P$ be inversion on the $r$ unit coordinates. On the unit-coordinate subspace whose coefficients sum to zero, $A=-P$. Inversion has $n$ fixed diagonal units and $(r-n)/2$ two-element orbits. Its positive and negative eigenspaces therefore have dimensions $(r+n)/2$ and $(r-n)/2$. Removing the all-unit vector from the positive eigenspace gives the asserted multiplicities for $A$.

Let $e_0$ be the zero-coordinate vector and $w$ the sum of all unit-coordinate vectors. Then $$A e_0=e_0+w,\qquad A w=r e_0+(r-1)w.$$ The matrix on $\operatorname{span}\{e_0,w\}$ has trace $r$ and determinant $-1$, hence characteristic polynomial $z^2-rz-1$. The sum of the $m$th powers of its roots obeys [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. Adding the powers of the remaining eigenvalues proves [\[eq:zero-fibre\]](#eq:zero-fibre){reference-type="eqref" reference="eq:zero-fibre"}.

[\[cor:image\]]{#cor:image label="cor:image"} The all-zero target lies in $\operatorname{im}T$. A target with nonzero anchors lies in $\operatorname{im}T$ if and only if every consecutive cyclic anchor pair satisfies $$\label{eq:image}
 \begin{cases}
 y_{i_{j+1}}=y_{i_j}^*,&h_j=0,\\
 y_{i_{j+1}}\ne y_{i_j},&h_j=1,
 \end{cases}$$ with no restriction when $h_j\geq2$.

In [\[eq:gaps\]](#eq:gaps){reference-type="eqref" reference="eq:gaps"}, $A^0$ is the identity. For $h=1$, the entry from $y^*$ to $z$ vanishes exactly when $z=y$. For $h\geq2$, a path can move from any letter to zero, remain there for $h-2$ steps, and then move to any letter, so every entry of $A^h$ is positive. The all-zero source maps to the all-zero target.

[\[cor:mass\]]{#cor:mass label="cor:mass"} The complete labelled fibres satisfy $$\label{eq:mass}
 \sum_{y\in Q^m}|T^{-1}(y)|=q^m.$$

Every ordered pair $(u,v)$ has one local output, so $\sum_{y\in Q}M_y=J_q$, the all-ones matrix. Summing [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"} over all targets gives $\operatorname{tr}(J_q^m)=q^m$.

The short-cycle fibres are now explicit. At $m=1$, the zero fibre has $n^2-n+1$ sources, each diagonal target has one source, and each off-diagonal target is empty. At $m=2$, the zero fibre has $(n^2+1)^2-n^2$ sources, while every nonzero alternating target $(u,u^*)$ has its unique source and all other targets are empty.

# Exact pressure, limitations, and conclusion

The paper-local standard-library verifier enumerates every source and target in 26 boxes, including $n=1$ through length ten, $n=2$ through length seven, and $n=3,4,5$ at shorter lengths. It compares literal iterates with Theorem [\[thm:iterate\]](#thm:iterate){reference-type="ref" reference="thm:iterate"}, reconstructs every target by a cyclic path dynamic program, attacks matrix direction by dense products, and checks integer eigenspace bases. Selected results appear in Table [1](#tab:control){reference-type="ref" reference="tab:control"}.

::: {#tab:control}
    $n$   $m$   states   image   fixed   zero fibre
  ----- ----- -------- ------- ------- ------------
      1    10     1024     277       2          123
      2     5     3125     183       3         1363
      2     7    78125    1459       3        24475
      3     4    10000     226      10         6895
      4     3     4913      89       5         4141

  : Selected exhaustive author controls. Enumeration is regression pressure; the proofs cover every $n,m\geq1$.
:::

The paper treats the aperiodic Brandt semigroup and a cyclic one-sided neighbourhood only. It gives no theorem for Brandt semigroups over nontrivial groups, other boundary conditions, asynchronous schedules, or time-$t$ inverse fibres. The finite controls are not experiments, proofs, or owner evidence. The exact contribution is the closed temporal and one-step inverse package for [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}; generic erosion and transfer-matrix vocabulary remain background. External circulation is blocked while ownership remains amber.

# Declarations {#declarations .unnumbered}

#### Data availability.

No external data were used. Exact source code and its canonical stdout accompany the manuscript.

#### Ethics.

The work studies finite algebraic maps and raises no human-subject, personal-data, or deployment issue.

#### CRediT

Anonymous author(s) performed conceptualization, formal analysis, software, validation, original drafting, and review and editing.

#### Competing interests.

No competing interests are declared.

#### Funding.

No external funding is declared for this manuscript.

#### AI-use statement.

Generative AI tools assisted with ideation, drafting, and code scaffolding. The author-side verifier checks finite cases; responsibility for every definition, proof, citation, and disclosure remains with the human author(s).

#### Release status.

External circulation, posting, and submission are not authorized while `HOLD_EXTERNAL` remains active.
