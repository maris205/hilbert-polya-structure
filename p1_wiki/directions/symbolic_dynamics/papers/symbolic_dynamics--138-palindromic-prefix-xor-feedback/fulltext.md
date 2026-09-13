---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--138-palindromic-prefix-xor-feedback"
canonical_tex: "symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback/main.pdf"
source_sha256: "e988fca92663c88d1d1f69498cfb54c57dbf4191a19f0c463d3e4558e706787b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Palindromic-Prefix XOR Feedback: One Two-Cycle, a Sharp Linear Clock, and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/138-palindromic-prefix-xor-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a binary word, form the complete indicator vector of its palindromic prefixes and XOR that vector with the word. We iterate this synchronous self-map. Global complement removes a phase bit and produces a normalized system in which one update zeros the first three coordinates and every later update extends a leading zero prefix. We prove that the original system has the single strict two-cycle $0^n\leftrightarrow1^n$ and that its maximum transient depth is $0$ at length one, $1$ at length two, and sharply $n-2$ thereafter. A periodic source whose ones occur at positions congruent to $3$ modulo $4$ attains the bound. We also give a complete left-to-right decoder for every one-step fibre; it is simultaneously an exact image test. Palindrome recognition and static palindrome data structures are credited background. Computation is used only for exact finite checks. External release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Palindromic-Prefix XOR Feedback: One Two-Cycle, a Sharp Linear Clock, and Exact Fibres'
```

## Markdown 正文

# The feedback map and the subtraction boundary

For a word $x=x_1\cdots x_n\in\{0,1\}^n$, put $$p_i(x)=\mathbf 1\{x_1\cdots x_i=x_i\cdots x_1\},\qquad 1\le i\le n.$$ All arithmetic on bits is in $\mathbb F_2$, written $\oplus$. We study the self-map $$\label{eq:T}
 T_n(x)_i=x_i\oplus p_i(x).$$ The entire prefix-indicator vector is recomputed after every update.

Initial-palindrome recognition has real-time algorithms [@Galil1978]; palindromic trees support access to all palindromic factors [@RubinchikShur2018], and recent work compresses families of palindromic prefixes [@BathieEllertStarikovskaya2025]. Static palindromic generation of binary words has a separate structural theory [@HarjuHuovaZamboni2015]. These results, ordinary border algorithms, and generic XOR-network terminology are background here. Our object is only the repeated full-vector feedback in [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}, its temporal dynamics, and its inverse fibres.

A state is *recurrent* if it belongs to a directed cycle. Its depth is the least number of updates needed to reach a recurrent state. Write $\bar x=x\oplus1^n$ for global complement and normalize a word by $$\label{eq:normalize}
 N(x)_i=x_i\oplus x_1.$$ Thus $N(x)_1=0$, and the two words in a complement pair have the same normalization.

# Complement quotient and the recurrent class

[\[prop:quotient\]]{#prop:quotient label="prop:quotient"} For every $x\in\{0,1\}^n$, $$T_n(\bar x)=\overline{T_n(x)}.$$ On the normalized carrier $\mathcal Q_n=\{y\in\{0,1\}^n:y_1=0\}$, the induced map is $$\label{eq:Q}
 Q_n(y)_i=y_i\oplus1\oplus p_i(y),$$ and $N(T_n(x))=Q_n(N(x))$.

Complementing every letter preserves every equality between two positions, so $p_i(\bar x)=p_i(x)$. Equation [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} then gives the first identity. Normalization also preserves all equality tests, hence $p_i(N(x))=p_i(x)$. Since $p_1(x)=1$, $$N(T_n(x))_i
 =(x_i\oplus p_i(x))\oplus(x_1\oplus1)
 =N(x)_i\oplus1\oplus p_i(N(x)),$$ which is [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}. At $i=1$ its value is zero, so $Q_n$ is closed on $\mathcal Q_n$.

For $y\in\mathcal Q_n$, let $\ell(y)$ be the length of its leading zero run.

[\[lem:amplifier\]]{#lem:amplifier label="lem:amplifier"} For every $y\in\mathcal Q_n$, the first $\min(3,n)$ coordinates of $Q_n(y)$ are zero. More generally, if $y$ begins with $0^k$ and $1\le k<n$, then $Q_n(y)$ begins with $0^{k+1}$.

The first coordinate is zero by [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}. Write the first three source bits as $0ab$ when they exist. The length-two prefix is palindromic exactly when $a=0$, and the length-three prefix is palindromic exactly when $b=0$. Thus at each of coordinates two and three, the last two terms in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} cancel the source bit.

Now suppose that $y_1\cdots y_k=0^k$. Every prefix ending at or before $k$ is palindromic, so its image bit is zero. If $y_{k+1}=0$, the next prefix is also all zero. If $y_{k+1}=1$, its first and last bits differ, so it is not palindromic. In either case [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} gives $Q_n(y)_{k+1}=0$.

[\[thm:recurrence\]]{#thm:recurrence label="thm:recurrence"} The only recurrent class of $T_n$ is the strict two-cycle $$0^n\longleftrightarrow1^n.$$ The maximum depth is at most $0$ for $n=1$, at most $1$ for $n=2$, and at most $n-2$ for $n\ge3$.

The normalized word $0^n$ is fixed by $Q_n$. If a normalized word is not zero, then after one update it has at least $\min(3,n)$ leading zeros by [\[lem:amplifier\]](#lem:amplifier){reference-type="ref" reference="lem:amplifier"}; every subsequent nonzero state has a strictly longer leading zero prefix. Hence $0^n$ is the only recurrent quotient state. The number of required updates is zero at $n=1$, at most one at $n=2$, and at most $1+(n-3)=n-2$ for $n\ge3$.

In the original system the first bit flips at every update because $p_1(x)=1$. Once the normalization is zero, the word is constant, and every prefix of a constant word is palindromic. Therefore $T_n(0^n)=1^n$ and $T_n(1^n)=0^n$. Each recurrent original state must project to the unique recurrent quotient state, and the phase flip then forces exactly this strict two-cycle.

# A sharp periodic source

For $n\ge3$, define $u^{(n)}\in\mathcal Q_n$ by $$\label{eq:witness}
 u^{(n)}_i=1\quad\Longleftrightarrow\quad i\equiv3\pmod4.$$ For $3\le k\le n$, let $v^{(n)}_k$ be the length-$n$ prefix of $0^k1010\cdots$; in particular $v^{(n)}_n=0^n$.

[\[lem:sharp\]]{#lem:sharp label="lem:sharp"} For $n\ge3$, $$Q_n(u^{(n)})=v^{(n)}_3,
 \qquad
 Q_n(v^{(n)}_k)=v^{(n)}_{k+1}\quad(3\le k<n).$$ Consequently $u^{(n)}$ reaches $0^n$ for the first time after $n-2$ updates.

The palindromic prefixes of $u^{(n)}$ have lengths $1$, $2$, and the lengths $i\ge5$ satisfying $i\equiv1\pmod4$. To verify this, for $i\ge3$ note that the one-positions in the prefix are $3,7,\ldots$. Reflection in a word of length $i$ sends position $3+4j$ to $i-2-4j$. This preserves that set exactly when $i\equiv1\pmod4$; in every other residue class the reflection of position $3$ is not a one-position. Substitution in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}, one residue class at a time, gives zeros at positions one through three and thereafter a one exactly at each even position. This is $v^{(n)}_3$.

Fix $k\ge3$. The prefixes of $v^{(n)}_k$ of length at most $k$ are all zero and hence palindromic. No longer prefix is palindromic. Indeed, such a palindrome would have to end in $0^k$. If its length is less than $2k$, its last $k$ positions include position $k+1$, whose bit is one. If its length is at least $2k$, its last $k$ positions lie in an alternating tail and again contain a one. Thus beyond position $k$ the palindrome indicator vanishes, and [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} complements the alternating tail. Its first one is thereby absorbed into the zero prefix, giving exactly $v^{(n)}_{k+1}$.

The displayed chain contains $n-2$ arrows from $u^{(n)}$ to $v^{(n)}_n$. Every preceding member is nonzero, so this is the first hitting time.

[\[cor:clock\]]{#cor:clock label="cor:clock"} The maximum depth of $T_n$ is $$\begin{array}{c|ccc}
n&1&2&n\ge3\\ \midrule
\max\operatorname{depth}&0&1&n-2.
\end{array}$$

The upper bounds are [\[thm:recurrence\]](#thm:recurrence){reference-type="ref" reference="thm:recurrence"}. At length two either nonconstant word has nonzero normalization and reaches the recurrent class in one step. For $n\ge3$, choose either original phase above the normalized word $u^{(n)}$; [\[lem:sharp\]](#lem:sharp){reference-type="ref" reference="lem:sharp"} gives depth $n-2$.

# The complete one-step fibre decoder

We now count the fibre of an arbitrary original target $t\in\{0,1\}^n$. Put $z=N(t)$. Define sets $\mathcal D_i(z)$ of normalized source prefixes recursively. Start with $\mathcal D_1(z)=\{0\}$. Given $y_1\cdots y_{i-1}\in\mathcal D_{i-1}(z)$, let $m=y_2\cdots y_{i-1}$, where the empty word is palindromic. Extend by the following rule: $$\label{eq:decoder}
\begin{array}{c|c|c}
m&z_i&\text{allowed }y_i\\ \midrule
\text{nonpalindromic}&0\text{ or }1&1\oplus z_i\\
\text{palindromic}&0&0,1\\
\text{palindromic}&1&\text{none}.
\end{array}$$

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} For every $t\in\{0,1\}^n$, $$|T_n^{-1}(t)|=|\mathcal D_n(N(t))|.$$ In particular, $t$ belongs to the image exactly when the decoder leaves at least one branch. The original complement phase contributes no additional multiplicity.

Consider a normalized source prefix $y_1\cdots y_i$, with $y_1=0$. Its full length-$i$ prefix is palindromic exactly when $y_i=0$ and the middle word $m=y_2\cdots y_{i-1}$ is palindromic. If $m$ is nonpalindromic, the indicator in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} is zero for either $y_i$, so the target equation $Q_n(y)_i=z_i$ forces $y_i=1\oplus z_i$. If $m$ is palindromic, then $y_i=0$ turns the indicator on and $y_i=1$ turns it off; both choices give target bit zero, and neither gives target bit one. These are precisely the three cases in [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"}.

The $i$th quotient output depends only on the first $i$ source bits. Induction on $i$ therefore shows that $\mathcal D_i(z)$ is exactly the set of normalized length-$i$ prefixes whose quotient image agrees with $z$ through position $i$. At $i=n$ it is the complete normalized fibre.

Finally, if $x$ is an original source of $t$, then its first bit is forced by $t_1=x_1\oplus1$, namely $x_1=1\oplus t_1$. Every normalized branch $y$ therefore lifts to the unique source $x_i=y_i\oplus(1\oplus t_1)$, and [\[prop:quotient\]](#prop:quotient){reference-type="ref" reference="prop:quotient"} shows that this source maps to $t$. Hence there is no factor of two.

The decoder is target-wise, including targets outside the image. It is not merely a recurrence for the largest fibre: it returns the exact cardinality of every fibre using only palindrome tests on prefixes already constructed.

# Exact control and limitations

The dependency-free paper-local verifier constructs every functional graph for $1\le n\le18$, totaling $524{,}286$ states. It checks complement equivariance, the literal quotient, all cycles and depths, and both amplifier statements. For every target through $n=15$, it independently compares [\[eq:decoder\]](#eq:decoder){reference-type="eqref" reference="eq:decoder"} with the literal fibre. It also checks the closed sharp family through $n=64$. The canonical run executes $3{,}870{,}590$ exact assertions.

These finite checks are counterexample pressure and do not prove statements at untested lengths. Conversely, no observed image or maximum-fibre sequence is promoted to an all-length claim. The owner search is bounded, and a non-hit is not a novelty or priority certificate. This anonymous artifact is therefore marked `HOLD_EXTERNAL`: posting, submission, and release are outside the present result.
