---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--185-prefix-diversity-delay"
canonical_tex: "symbolic_dynamics/papers/185-prefix-diversity-delay/main.tex"
canonical_pdf: "symbolic_dynamics/papers/185-prefix-diversity-delay/main.pdf"
source_sha256: "e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Pointwise Clocks and All-Time Fibres for Prefix-Diversity Delay

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/185-prefix-diversity-delay>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/185-prefix-diversity-delay/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/185-prefix-diversity-delay/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/185-prefix-diversity-delay/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/185-prefix-diversity-delay/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Replace every coordinate of a length-$n$ word over an $n$-letter alphabet by the number of distinct letters in its strict prefix, and feed the entire output word back into the same rule. We prove a pointwise iterate formula: after the first epoch, each further epoch inserts one forced identity coordinate and shifts the original prefix-diversity path. It follows that the identity word is the unique recurrent point and that a word's exact entrance time is determined by its longest all-distinct prefix. For $1\le t\le n-1$, the image consists of $2^{n-t-1}$ binary-rise paths with an identity prefix, and the depth CDF is $(n)_{n-t}n^t$. Every transient target fibre is a local product of fresh-letter and old-letter choices, with the identity and stabilized cases stated separately. For $n\ge3$ the global height is $n-1$, with exactly $n^{n-1}$ deepest words; the two-letter boundary is explicit. Restricted-growth encodings and prefix statistics receive no contribution credit. The retained iterative conjunction is [owner\_amber]{.smallcaps}; circulation remains [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Pointwise Clocks and All-Time Fibres for\
  Prefix-Diversity Delay
```

## Markdown 正文

# Literal rule and contribution boundary

Write $[n]_0=\{0,\ldots,n-1\}$ and $\mathcal W_n=[n]_0^n$ for $n\ge1$. Define the prefix-diversity self-map $P_n:\mathcal W_n\to\mathcal W_n$ by $$\label{eq:map}
 (P_nw)_i=|\{w_0,\ldots,w_{i-1}\}|,
 \qquad 0\le i<n,$$ where the empty prefix has size zero. Since $(P_nw)_i\le i<n$, no totalisation is needed.

Restricted-growth functions and their set-partition encodings are classical [@Wachs1994]. More closely, Mansour and Vajnovszki define restricted growth words through general prefix statistics and give efficient Gray-code generation [@MansourVajnovszki2013]. We therefore assign restricted-growth vocabulary, first-occurrence patterns, prefix-statistic evaluation, falling factorials, and generic finite-map bookkeeping no contribution credit. The scoped residual is only the autonomous iteration of the literal vector [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, its pointwise delay law, and the joint all-time clock/image/every-target inverse atlas. A bounded search found no source stating that conjunction. This non-hit is neither novelty nor priority evidence.

Internally, P132 thresholds binary prefix sums; P134 recomputes border arrays; P138 and P139 use palindromic and Lyndon prefix structure; P164 passes a cyclic equality mask into a linear cellular automaton; and P176 rotates by a first-symbol frequency. None yields [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} or the delay identity below, but all generic prefix and word-feedback language is subtracted.

For a word $w$, put $d=P_nw$. Its increments record novelty: $$\label{eq:novelty}
 d_0=0,\qquad d_i-d_{i-1}=\mathbf1\{w_{i-1}\notin
 \{w_0,\ldots,w_{i-2}\}\}\quad(1\le i<n).$$ In particular $d_1=1$ when $n\ge2$.

# The delay normal form

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} Let $w\in\mathcal W_n$, $d=P_nw$, and $t\ge1$. With $r=t-1$, $$\label{eq:iterate}
 (P_n^tw)_i=
 \begin{cases}
 i,&i<r,\\
 r+d_{i-r},&i\ge r.
 \end{cases}$$ For $r\ge n$, the first branch applies at every coordinate.

Every prefix-diversity word $d$ starts at zero and rises at each step by zero or one. Hence its prefix $d_0,\ldots,d_{i-1}$ contains every integer from zero through $d_{i-1}$. Applying [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} to such a path gives $$\label{eq:shift}
 (P_nd)_0=0,\qquad (P_nd)_i=d_{i-1}+1\quad(i\ge1).$$ The right-hand side is again a zero-one-rise path. Iterating [\[eq:shift\]](#eq:shift){reference-type="eqref" reference="eq:shift"} inserts one more forced identity coordinate on the left and shifts the old path one place right. Starting from $P_nw=d$ proves [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} by induction.

Thus the entire future of $w$ is already coded by the novelty decisions in its first image; no orbit search is needed.

# Images, recurrence, and pointwise clocks

Let $e=(0,1,\ldots,n-1)$. For $w\in\mathcal W_n$, let $\rho(w)$ be the length of its longest all-distinct prefix.

[\[thm:forward\]]{#thm:forward label="thm:forward"} For $1\le t\le n-1$, the time-$t$ image is exactly the set of words $y$ with $$\label{eq:image}
 y_i=i\ (0\le i\le t),\qquad
 y_i-y_{i-1}\in\{0,1\}\ (t<i<n).$$ Consequently, $$\label{eq:image-size}
                 |\operatorname{im}P_n^t|=2^{n-t-1}.$$ The word $e$ is the unique fixed and recurrent state, and $P_n^{n-1}$ is constant with value $e$. The exact entrance time $\tau(w)$ is $$\label{eq:clock}
 \tau(w)=
 \begin{cases}
 0,&w=e,\\
 \max\{1,n-\rho(w)\},&w\ne e.
 \end{cases}$$ For $n\ge3$, the sharp height is $n-1$; its complete deepest set is $\{w:w_0=w_1\}$ and has size $n^{n-1}$. At $n=2$, the height is one and all three nonidentity words are deepest. At $n=1$, the height is zero.

Formula [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} forces [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. Conversely, a target of that form recovers the prefix $$\label{eq:recover-d}
 d_j=y_{j+t-1}-(t-1),\qquad 0\le j\le n-t.$$ It begins $0,1$ and has zero-one rises, so choose a fresh source letter at each rise and a previously seen letter at each flat. There are always enough letters, and the last $t$ source coordinates are arbitrary. Thus every target in [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} occurs. Its final $n-t-1$ increments are free bits, proving [\[eq:image-size\]](#eq:image-size){reference-type="eqref" reference="eq:image-size"}.

For $n=1$ the claim is immediate. For $n\ge2$, taking $t=n-1$ gives the constant image $e$. If $P_nw=w$, then $w_0=0,w_1=1$ and induction in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} forces $w_i=i$; hence $e$ is the only fixed point and, because every orbit reaches it, the only recurrent point.

For $t\ge1$, [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} equals $e$ exactly when $d_j=j$ through $j=n-t$, equivalently when the first $n-t$ letters of $w$ are distinct. Taking the least such positive $t$ and separating the already fixed word proves [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}. For $n\ge3$, depth $n-1\ge2$ means $\rho(w)=1$, which is exactly $w_0=w_1$; choose this repeated letter in $n$ ways and the remaining $n-2$ coordinates arbitrarily. Directly, $\mathcal W_2$ consists of the fixed word $01$ and three depth-one words, while $\mathcal W_1=\{0\}$.

[\[cor:depth\]]{#cor:depth label="cor:depth"} For $1\le t\le n-1$, $$\label{eq:depth-cdf}
 |\{w:\tau(w)\le t\}|=(n)_{n-t}n^t,$$ where $(n)_k=n(n-1)\cdots(n-k+1)$. Thus every positive depth population is the difference of consecutive values in [\[eq:depth-cdf\]](#eq:depth-cdf){reference-type="eqref" reference="eq:depth-cdf"}, with the depth-zero value equal to one.

The proof of Theorem [\[thm:forward\]](#thm:forward){reference-type="ref" reference="thm:forward"} says that $\tau(w)\le t$ precisely when the first $n-t$ letters are distinct. There are $(n)_{n-t}$ choices for that prefix and $n^t$ choices for the invisible suffix.

# All-time every-target fibres

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Let $1\le t\le n-1$ and let $y$ satisfy [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. Recover $d_0,\ldots,d_{n-t}$ by [\[eq:recover-d\]](#eq:recover-d){reference-type="eqref" reference="eq:recover-d"}. Then $$\label{eq:fibre}
 |(P_n^t)^{-1}(y)|=
 n^{t+1}\prod_{q=1}^{n-t-1}
 \begin{cases}
 n-d_q,&d_{q+1}-d_q=1,\\
 d_q,&d_{q+1}-d_q=0.
 \end{cases}$$ Targets outside [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"} have fibre zero. In particular, the fibre of $e$ is $(n)_{n-t}n^t$, exactly the depth CDF. The product in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is empty when $t=n-1$. At time $t=0$, $P_n^0$ is the identity, so every target has fibre one. For every $t\ge n-1$, the image is the singleton $\{e\}$, the fibre of $e$ has size $n^n$, and every other fibre is zero.

The target exposes whether source position $q$ is a new letter for every $1\le q\le n-t-1$. Before that position, exactly $d_q$ letters have appeared. A rise therefore has $n-d_q$ choices and a flat has $d_q$ choices. The first source letter has $n$ choices, while the last $t$ source letters are invisible and contribute $n^t$. These choices are independent conditional on the displayed novelty path, proving [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} and also proving fibre-mass conservation without division by the image size. For $y=e$, every visible decision is a rise, yielding the falling factorial in [\[eq:depth-cdf\]](#eq:depth-cdf){reference-type="eqref" reference="eq:depth-cdf"}.

For orientation, at $n=4$ the word $0013$ follows $$0013\longmapsto0112\longmapsto0122\longmapsto0123=e,$$ and its initial repetition witnesses the sharp depth three. At $n=7$, the exact depth histogram is $$1,\ 35279,\ 88200,\ 164640,\ 216090,\ 201684,\ 117649.$$

# Exact control, limitations, and declarations

The paper-local standard-library verifier exhausts all $n^n$ words through $n=7$. For every source and all relevant times it compares literal iteration with [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}; it rebuilds the image language and every target fibre, checks the least pointwise clock and every depth CDF, and verifies the complete deepest population. Finite computation is falsification pressure, not proof.

The alphabet size is tied to the word length, and the update retains counts rather than the equality partition alone. We do not classify rectangular alphabet/length variants, random updates, or asymptotic laws. The closest restricted-growth literature is structurally adjacent, and the bounded owner search leaves a live terminology risk. The status is therefore [owner\_amber / hold\_external]{.smallcaps}; no circulation or priority claim is authorized.

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

Generative AI assisted drafting and code generation. All mathematical, bibliographic, and artifact claims require human verification before any external use.
