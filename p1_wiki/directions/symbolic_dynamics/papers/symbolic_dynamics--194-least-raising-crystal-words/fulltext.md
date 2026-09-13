---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--194-least-raising-crystal-words"
canonical_tex: "symbolic_dynamics/papers/194-least-raising-crystal-words/main.tex"
canonical_pdf: "symbolic_dynamics/papers/194-least-raising-crystal-words/main.pdf"
source_sha256: "d4c81d389dba055a3a232077e79058c09cae1be40b8822d49f976c4242d97ce9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Least-Colour Raising Dynamics on Finite Type-A Crystal Words

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/194-least-raising-crystal-words>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/194-least-raising-crystal-words/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/194-least-raising-crystal-words/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/194-least-raising-crystal-words/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/194-least-raising-crystal-words/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix an alphabet $[k]$ and a word length $n$. At each epoch, apply the Kashiwara raising operator $e_i$ of the least colour for which it is defined; if none is defined, hold. This deterministic choice orients every type-A word-crystal component toward its unique highest word. We give the exact entrance time of every word, prove the sharp global depth $n(k-1)$ with unique extremizer $k^n$, and enumerate every depth layer by a normalized principal specialization of a Schur polynomial. Components of shape $\lambda$ occur with multiplicity $f^\lambda$, so the fixed words are counted by involutions whose Robinson--Schensted shape has at most $k$ rows. Independently, we solve the inverse problem for every labelled target: its predecessors are precisely the admissible one-step lowerings $f_i$, together with a self-predecessor at a highest word. Every fibre has size at most $k$, and this bound is attained exactly in the stable range $n\geq\binom{k}{2}$; a staircase highest word gives an explicit witness. Classical crystal, tableau, RSK, Schur, and hook formulas, as well as existing crystal pop-stack sorting, receive zero contribution credit. The retained object is only the least-colour scheduler and its targetwise fibre atlas. A bounded owner search leaves the manuscript `OWNER_AMBER / HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'Least-Colour Raising Dynamics on Finite Type-A Crystal Words'
```

## Markdown 正文

# The literal scheduler and its subtraction boundary

Let $n,k\geq1$ and $\mathcal W_{n,k}=[k]^n$. We first fix the signature convention, since reversing a word or reversing the tensor convention changes which occurrence an operator edits. For $1\leq i<k$ and $w=w_1\cdots w_n$, ignore letters outside $\{i,i+1\}$, write a plus sign for each $i$ and a minus sign for each $i+1$, and repeatedly delete matched pairs $+-$, with ignored letters allowed between the signs. The remaining signs are a string of minuses followed by a string of pluses. If a minus remains, $e_i(w)$ changes the position of the *rightmost* unpaired $i+1$ into $i$; otherwise $e_i(w)$ is undefined. If a plus remains, $f_i(w)$ changes the position of the *leftmost* unpaired $i$ into $i+1$; otherwise $f_i(w)$ is undefined. These partial maps are mutual inverses along every $i$-string.

Define $F=F_{n,k}:\mathcal W_{n,k}\to\mathcal W_{n,k}$ by $$\label{eq:update}
 F(w)=
 \begin{cases}
 e_{m(w)}(w),&m(w)=\min\{i:e_i(w)\text{ is defined}\}\text{ exists},\\
 w,&\text{all }e_i(w)\text{ are undefined}.
 \end{cases}$$ Thus the state is re-examined after every individual crystal edge. For example, when $k=3$, $$\label{eq:example}
333\xrightarrow{2}332\xrightarrow{1}331\xrightarrow{2}321
\xrightarrow{1}311\xrightarrow{2}211\xrightarrow{1}111,$$ where the superscript is the selected colour.

Crystal bases, Kashiwara operators, tensor-product signatures, and unique highest vertices are established theory [@Kashiwara1991; @BumpSchilling2017]. RSK, tableaux, Schur functions, principal specialization, and hook formulas are likewise classical [@Fulton1997; @Stanley2023; @Sagan2001]. We use all of that material as background and claim no contribution for it. In particular, neither the crystal edges nor the decomposition of $[k]^n$ is new here. The only retained conjunction is the autonomous least-colour choice in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, its exact clock, and its complete labelled inverse atlas. A bounded source non-hit is not evidence of novelty, priority, completeness, or freedom to operate; external circulation remains on hold.

Defant and Williams' crystal pop-stack operator sends a vertex in a poppable crystal to the unique source of its connected component after restricting to all descent colours of the starting vertex [@DefantWilliams2022]. It is a noninvertible deterministic crystal map whose forward orbits reach the highest-weight vertex, with a sharp maximum orbit-size theorem. This is the nearest located dynamical surface and receives zero contribution credit. It is not [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}: one pop-stack macrostep resolves a whole descent-colour component using the starting descent set, whereas $F$ takes one edge of the least currently available colour and recomputes after every edge. That work does not supply the letter-sum clock, Schur depth layers, or the targetwise $f_i$ predecessor atlas proved below. These distinctions bound the literal object; they do not assert novelty.

# Components, recurrent states, and the exact clock

Write $$\label{eq:energy}
 E(w)=\sum_{a=1}^n w_a.$$ With our signature convention, the convenient RSK shape is $$\label{eq:reverse-rsk}
 \operatorname{sh}(w)=\operatorname{shape}\bigl(\operatorname{RSK}(w_n\cdots w_1)\bigr).$$ This reversal is part of the convention, not a dynamical operation. If $\lambda=(\lambda_1,\ldots,\lambda_k)$ is a partition padded by zero parts, put $$\label{eq:baseline}
 b(\lambda)=\sum_{i=1}^k i\lambda_i.$$

[\[prop:highest\]]{#prop:highest label="prop:highest"} The following are equivalent for $h\in\mathcal W_{n,k}$:

(i) $F(h)=h$;

(ii) every $e_i(h)$ is undefined;

(iii) for every prefix $u$ of $h$ and every $1\leq i<k$, the number of letters $i$ in $u$ is at least the number of letters $i+1$ in $u$.

Thus the fixed states are exactly the ballot, or Yamanouchi, words. Every crystal component contains exactly one of them. If its shape is $\lambda$, that word has content $\lambda$ and energy $b(\lambda)$.

The first equivalence is the holding clause in [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. Under the matching rule, an unpaired minus in the $i$-signature exists exactly when some prefix has seen more letters $i+1$ than letters $i$. This proves the second equivalence. The remaining assertions are the highest-weight description of a finite type-A word crystal; with [\[eq:reverse-rsk\]](#eq:reverse-rsk){reference-type="eqref" reference="eq:reverse-rsk"}, its highest weight is its RSK shape.

Let $\tau(w)$ be the least $t\geq0$ for which $F^t(w)$ is recurrent.

[\[thm:clock\]]{#thm:clock label="thm:clock"} Every recurrent state is fixed. A word $w$ remains in its crystal component and converges to that component's unique highest word $h(w)$. If $\lambda=\operatorname{sh}(w)$, then $$\label{eq:clock}
 \tau(w)=E(w)-b(\lambda).$$ Consequently, $$\label{eq:sharp-depth}
 \max_{w\in\mathcal W_{n,k}}\tau(w)=n(k-1),$$ and $k^n$ is the unique word attaining this maximum.

Whenever [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} moves, one letter $i+1$ becomes $i$, so $E$ drops by exactly one. The move is a crystal edge and hence preserves the component. Strict decrease excludes every nontrivial directed cycle, while finiteness and Proposition [\[prop:highest\]](#prop:highest){reference-type="ref" reference="prop:highest"} force the orbit to stop at the unique highest word of its component. Its energy is $b(\lambda)$, proving [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}.

Since $E(w)\leq nk$ and $b(\lambda)\geq n$, equation [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} gives $\tau(w)\leq n(k-1)$. Equality requires every letter of $w$ to be $k$ and $b(\lambda)=n$. The first condition already forces $w=k^n$; its reverse-RSK shape is $(n)$ and its endpoint is $1^n$, so equality does hold.

The colour schedule affects the route but not the length: any sequence of raising edges ending at the component's highest word has the energy difference in [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}. What is special to [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} begins with the actual chosen route and, decisively, with its inverse problem.

# Exact component and global layer polynomials

For a cell $x=(r,c)$ of a Young diagram, with rows and columns numbered from one, let $\operatorname{ct}(x)=c-r$ and let $h(x)$ be its hook length. Write $f^\lambda=|\operatorname{SYT}(\lambda)|=n!/\prod_{x\in\lambda}h(x)$.

[\[thm:layers\]]{#thm:layers label="thm:layers"} Every shape-$\lambda$ crystal component has depth polynomial $$\begin{aligned}
 D_{\lambda,k}(q)
  &=\sum_{w\text{ in one component}}q^{\tau(w)}\label{eq:component-poly}\\
  &=q^{-b(\lambda)}s_\lambda(q,q^2,\ldots,q^k)\notag\\
  &=q^{-\sum_{r\geq1}(r-1)\lambda_r}
       s_\lambda(1,q,\ldots,q^{k-1})\notag\\
  &=\prod_{x\in\lambda}
       \frac{1-q^{k+\operatorname{ct}(x)}}{1-q^{h(x)}}.\notag\end{aligned}$$ There are exactly $f^\lambda$ such components. Hence the global depth polynomial is $$\label{eq:global-poly}
 D_{n,k}(q)=\sum_{\substack{\lambda\vdash n\\\ell(\lambda)\leq k}}
 f^\lambda D_{\lambda,k}(q),$$ and $[q^d]D_{n,k}(q)$ is the exact number of words at depth $d$.

Reverse-word RSK identifies words with pairs $(P,Q)$ of common shape $\lambda$, where $P$ is semistandard with entries in $[k]$ and $Q$ is standard. With the convention of Section 1, crystal operators change $P$ and preserve $Q$. Thus $Q$ indexes a component, giving $f^\lambda$ components, and the energy is the sum of the entries of $P$. The unique highest tableau has every cell in row $r$ filled by $r$, of weight $b(\lambda)$. Summing [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} over all $P$ gives the first Schur specialization in [\[eq:component-poly\]](#eq:component-poly){reference-type="eqref" reference="eq:component-poly"}. Homogeneity removes a factor $q^n$, and the principal-specialization hook-content identity gives the product. Summing over the recording tableaux proves [\[eq:global-poly\]](#eq:global-poly){reference-type="eqref" reference="eq:global-poly"}.

At $q=1$, the component size is the hook-content value $$\label{eq:hook-content}
 D_{\lambda,k}(1)=s_\lambda(1^k)
 =\prod_{x\in\lambda}\frac{k+\operatorname{ct}(x)}{h(x)},$$ and [\[eq:global-poly\]](#eq:global-poly){reference-type="eqref" reference="eq:global-poly"} specializes to $k^n$.

[\[cor:fixed\]]{#cor:fixed label="cor:fixed"} The recurrent and fixed census is $$\label{eq:fixed-count}
 |\operatorname{Fix}(F_{n,k})|
 =\sum_{\substack{\lambda\vdash n\\\ell(\lambda)\leq k}}f^\lambda.$$ It also counts involutions in $S_n$ whose RSK shape has at most $k$ rows, equivalently whose longest decreasing subsequence has length at most $k$. For $k\geq n$ this is the ordinary involution number $I_n$, with $$\label{eq:telephone}
 \sum_{n\geq0}I_n\frac{z^n}{n!}=\exp(z+z^2/2).$$

Each component contributes its unique highest word. Under RSK, involutions are the pairs $(Q,Q)$, one for each standard tableau $Q$; Schensted's theorem identifies the number of rows with longest decreasing subsequence length. The unrestricted recurrence $I_n=I_{n-1}+(n-1)I_{n-2}$ gives [\[eq:telephone\]](#eq:telephone){reference-type="eqref" reference="eq:telephone"}.

Equations [\[eq:component-poly\]](#eq:component-poly){reference-type="eqref" reference="eq:component-poly"}--[\[eq:telephone\]](#eq:telephone){reference-type="eqref" reference="eq:telephone"} are classical crystal/RSK enumerations applied to the clock. They provide exact layers but do not by themselves supply an originality claim.

# Every-target inverse atlas

For an assertion such as "$e_j(x)$ is absent", we mean that the partial operator is undefined on that specific labelled word $x$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For every target $y\in\mathcal W_{n,k}$, $$\label{eq:fibre-set}
 F^{-1}(y)=
 \bigl(\{y\}\ \text{if $y$ is highest, else }\varnothing\bigr)
 \ \cup\!!
 \bigcup_{i=1}^{k-1}
 \left\{
 f_i(y):
 \begin{array}{l}
 f_i(y)\text{ is defined},\\[-1mm]
 e_j(f_i(y))\text{ is undefined for every }j<i
 \end{array}
 \right\}.$$ Each displayed lowering contributes at most one distinct source. In particular, $$\label{eq:fibre-bound}
 |F^{-1}(y)|\leq k$$ for every target, and the fibres sum to $k^n$.

Suppose first that $x\neq F(x)=y$, and let $i$ be the colour selected at $x$. Then $y=e_i(x)$ and the crystal-string inverse property gives $x=f_i(y)$. The scheduler selected $i$ exactly because every $e_j(x)$ with $j<i$ was absent. Thus $x$ appears on the right of [\[eq:fibre-set\]](#eq:fibre-set){reference-type="eqref" reference="eq:fibre-set"}. The only possible self-predecessors are the holding, hence highest, states.

Conversely, let $x=f_i(y)$ satisfy the displayed absence conditions. Then $e_i(x)=y$, and no lower colour is available at $x$, so [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} selects $i$ and sends $x$ to $y$. A candidate $f_i(y)$ changes the content by the simple root of colour $i$, so candidates from different colours are distinct. There are at most $k-1$ of them and at most one self-source, proving [\[eq:fibre-bound\]](#eq:fibre-bound){reference-type="eqref" reference="eq:fibre-bound"}. Summing fibres over a finite self-map counts each source once.

The bound has an exact stability threshold.

[\[cor:stable\]]{#cor:stable label="cor:stable"} Assume $k\geq2$. Some target has fibre size $k$ if and only if $$\label{eq:stable-threshold}
 n\geq\binom{k}{2}.$$ For $s=n-\binom{k}{2}\geq0$, an explicit target attaining the bound is the highest word $$\label{eq:staircase}
 h_{n,k}=1^{k-1+s}2^{k-2}3^{k-3}\cdots(k-1).$$ For example, $F^{-1}(112)=\{112,212,113\}$ when $(n,k)=(3,3)$. For $k=1$, the sole fibre has size one.

A fibre of size $k$ must use all $k-1$ lowering candidates and the self candidate, so its target is highest. If its padded highest weight is $\lambda=(\lambda_1,\ldots,\lambda_k)$, then $f_i$ is defined exactly when $\lambda_i>\lambda_{i+1}$. Strict inequalities for every $i$ force $$n=\sum_i\lambda_i\geq(k-1)+(k-2)+\cdots+1=\binom{k}{2}.$$

Conversely, the word in [\[eq:staircase\]](#eq:staircase){reference-type="eqref" reference="eq:staircase"} is ballot and has padded content $(k-1+s,k-2,\ldots,1,0)$, so every $f_i(h_{n,k})$ exists. For $j<i-1$, applying $f_i$ does not change the $j$-signature; in the $(i-1)$-signature it removes one minus and therefore cannot create an unpaired minus. Since the target is highest, every lower $e_j$ remains absent. All $k-1$ candidates are therefore admitted by [\[eq:fibre-set\]](#eq:fibre-set){reference-type="eqref" reference="eq:fibre-set"}, along with the self-source.

Unlike the Schur layer formula, Theorem [\[thm:fibre\]](#thm:fibre){reference-type="ref" reference="thm:fibre"} depends on the least-colour scheduler: another order on the same crystal edges changes its admissibility conditions and its labelled fibres.

# Finite control and evidence boundary

The paper-local verifier constructs the literal signatures and the whole functional graph independently of its tableau routines. On all words for $1\leq k\leq4$ and $1\leq n\leq7$, it checks the pointwise clock, unique highest endpoint, ballot criterion, reverse-RSK shape invariance, sharp and unique deepest word, and every target's exact predecessor set. It separately enumerates semistandard tableaux and compares their depth polynomials with the hook-content principal specialization, builds crystal components and checks the multiplicity $f^\lambda$, verifies the hook-length formula by a corner-removal recurrence, and checks the bounded-height involution census through $S_8$. Staircase fibres are tested directly through $k=9$ without enumerating their exponentially larger ambient word spaces.

The canonical run makes $618{,}419$ exact assertions over $25{,}384$ source transitions. Its final status is `PASS`. This is regression and counterexample pressure only, not a proof, a process-separated review, an exhaustive owner search, or evidence of novelty. In particular, all classical representation-theoretic identities used in Sections 2--3 remain fully subtracted, as does the crystal pop-stack dynamical surface. The claim ceiling is the finite dynamical conjunction of the literal scheduler [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, the clock [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, and the targetwise inverse rule [\[eq:fibre-set\]](#eq:fibre-set){reference-type="eqref" reference="eq:fibre-set"}. The package remains `OWNER_AMBER / HOLD_EXTERNAL`.
