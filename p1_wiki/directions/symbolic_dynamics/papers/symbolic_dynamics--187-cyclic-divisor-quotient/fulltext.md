---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--187-cyclic-divisor-quotient"
canonical_tex: "symbolic_dynamics/papers/187-cyclic-divisor-quotient/main.tex"
canonical_pdf: "symbolic_dynamics/papers/187-cyclic-divisor-quotient/main.pdf"
source_sha256: "e4dd2c5afb6381563476c6b6735f94c932403492165b8f21adeee6a448f7b83d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cyclic Divisor-Quotient Dynamics: Sharp Height Clocks and Exact Target Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/187-cyclic-divisor-quotient>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/187-cyclic-divisor-quotient/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/187-cyclic-divisor-quotient/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/187-cyclic-divisor-quotient/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/187-cyclic-divisor-quotient/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a positive integer $N$ and a cyclic word of divisors of $N$, divide each letter synchronously by its gcd with the next letter. Prime valuations turn this nonlinear arithmetic rule into the truncated difference $(e_i-e_{i+1})_+$. We prove that every orbit becomes fixed, with sharp global height equal to the largest prime exponent of $N$ for cycles of length at least three; when $N>1$, lengths one and two have sharp height one. Fixed words are counted by weighted cyclic independence polynomials, prime by prime. We also solve the labelled one-step inverse problem: every target fibre is a product of traces of explicit local zero--one matrices, including empty fibres and all boundary parameters. Summing these traces recovers the full state-space mass. Exact enumeration supplies author-side counterexample pressure but is not proof or novelty evidence. Standard difference dynamics, divisor valuations, and transfer matrices receive no contribution credit, and the manuscript remains `HOLD_EXTERNAL` under an open owner audit.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Cyclic Divisor-Quotient Dynamics:\
  Sharp Height Clocks and Exact Target Fibres
```

## Markdown 正文

# The literal map and its boundary

Let $N\geq1$, let $\operatorname{Div}(N)$ be its positive divisors, and let $m\geq1$. On $\operatorname{Div}(N)^m$, with indices in $\mathbb Z/m\mathbb Z$, define $$\label{eq:Q}
 (Q_Nx)_i=\frac{x_i}{\gcd(x_i,x_{i+1})}.$$ This is a deterministic synchronous finite system in the sense of the broad parallel-dynamics framework surveyed in [@AledoMartinezValverde2015]. Cyclic difference systems such as Ducci maps are established objects [@LewisTefft2025]; their additive modular rule is not [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}. We assign this general vocabulary, prime factorization, and generic transfer-matrix counting zero contribution credit. The scoped result is the joint clock, fixed-locus, and every-labelled-target theorem for [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"}. A bounded formula search found no literal owner, but that non-hit establishes neither novelty nor priority.

Write $N=\prod_{p\mid N}p^{a_p}$. For $a\geq0$ define $$\label{eq:D}
 D_a(e)_i=(e_i-e_{i+1})_+,
 \qquad e\in\{0,\ldots,a\}^m.$$ Taking $p$-adic valuations in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} gives $$\label{eq:conjugacy}
 \nu_p((Q_Nx)_i)=D_{a_p}(\nu_p(x_0),\ldots,\nu_p(x_{m-1}))_i.$$ Thus the arithmetic system is the direct product of the maps [\[eq:D\]](#eq:D){reference-type="eqref" reference="eq:D"}.

For a finite map, the tail of a state is its least entrance time into a cycle. All cycles below will be fixed points.

# The truncated-difference clock

[\[lem:peaks\]]{#lem:peaks label="lem:peaks"} Let $e\in\{0,\ldots,a\}^m$ have maximum $h>0$ and put $z=D_a(e)$. Every coordinate of $z$ equal to $h$ is bordered by zeros and remains an isolated value $h$ under all later iterates. All other coordinates of $z$ are at most $h-1$.

The equality $z_i=h$ forces $e_i=h$ and $e_{i+1}=0$. Maximality of $h$ then gives $z_{i-1}=0$, while $z_{i+1}=0$ follows directly. Let $S$ be the set of these top-peak positions, put $f_i=h\mathbf1\{i\in S\}$, and write $z=f+w$. The vector $w$ vanishes on $S$ and on both neighboring sites of every member of $S$. A coordinate check gives $$\label{eq:split}
 D_a(f+w)=f+D_a(w).$$ The required zeros persist under $D_a$, so [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"} may be iterated. Thus the top peaks remain frozen and the independent residual vector has maximum at most $h-1$.

[\[thm:clock\]]{#thm:clock label="thm:clock"} Every orbit of $Q_N$ reaches a fixed point. If $N=1$, the unique state is fixed. If $N>1$, the sharp maximum tail is $$\label{eq:height}
 H(N,m)=
 \begin{cases}
 1,&m=1\text{ or }m=2,\\
 \max_{p\mid N}a_p,&m\geq3.
 \end{cases}$$ In particular, there are no nontrivial recurrent cycles.

Induct on the largest exponent $h$ in a word for $D_a$. After one step, Lemma [\[lem:peaks\]](#lem:peaks){reference-type="ref" reference="lem:peaks"} separates permanent top peaks from subsystems of height at most $h-1$, with zero boundary letters. The induction hypothesis fixes the latter within $h-1$ more steps. Hence $D_a^h(e)$ is fixed. For $m\geq3$ the word $$(0,\ldots,0,h,1)$$ has exact tail $h$: each step decreases the penultimate positive entry by one, and the final $1$ then becomes isolated. For $m=1$, $D_a(e)=0$. For $m=2$, $D_a(u,v)$ is either $(u-v,0)$ or $(0,v-u)$ and is fixed. Nonfixed examples exist in both cases when $a>0$.

Equation [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"} makes the tail of a divisor word the maximum of its primewise tails. Choosing only a prime with largest exponent proves sharpness in [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}. Since every orbit reaches a fixed point, recurrence equals fixedness.

# Fixed words

Define the cyclic support polynomial $$\label{eq:Im}
 I_m(z)=\sum_{\substack{s\in\{0,1\}^m\\s_is_{i+1}=0\ \forall i}}
 z^{\sum_i s_i}
 =\operatorname{tr}\left(\begin{bmatrix}1&z\\1&0\end{bmatrix}^{m}\right).$$ This convention includes the self-neighboring $m=1$ cycle, so $I_1(z)=1$; $I_2(z)=1+2z$. For $m\geq2$ one may also write $$\label{eq:Iclosed}
 I_m(z)=\sum_{k=0}^{\lfloor m/2\rfloor}
 \frac{m}{m-k}\binom{m-k}{k}z^k.$$

[\[thm:fixed\]]{#thm:fixed label="thm:fixed"} A divisor word is fixed by $Q_N$ exactly when $$\label{eq:coprime}
 \gcd(x_i,x_{i+1})=1\qquad\text{for every }i.$$ Consequently $$\label{eq:fixedcount}
 |\operatorname{Fix}(Q_N)|=\prod_{p\mid N} I_m(a_p),$$ where the empty product for $N=1$ is one.

The equality $D_a(e)=e$ holds precisely when $e_i>0$ implies $e_{i+1}=0$. Thus the positive support is a cyclic zero--one word with no adjacent ones. Once its support has size $k$, its positive heights have $a^k$ choices. This gives $I_m(a)$ for one prime. Prime valuations are independent, proving both [\[eq:coprime\]](#eq:coprime){reference-type="eqref" reference="eq:coprime"} and the product [\[eq:fixedcount\]](#eq:fixedcount){reference-type="eqref" reference="eq:fixedcount"}. The two-state transfer matrix in [\[eq:Im\]](#eq:Im){reference-type="eqref" reference="eq:Im"} records whether the preceding support site was occupied; expansion by the support size gives [\[eq:Iclosed\]](#eq:Iclosed){reference-type="eqref" reference="eq:Iclosed"}.

The same two-state matrix also gives a compact recurrence that avoids any ambiguity about the short cyclic supports.

[\[cor:fixed-recurrence\]]{#cor:fixed-recurrence label="cor:fixed-recurrence"} Put $I_1(z)=1$ and $I_2(z)=1+2z$. For $m\geq3$, $$\label{eq:Irecurrence}
 I_m(z)=I_{m-1}(z)+zI_{m-2}(z).$$ Equivalently, if $\lambda_\pm=(1\pm\sqrt{1+4z})/2$, then $I_m(z)=\lambda_+^m+\lambda_-^m$.

The matrix in [\[eq:Im\]](#eq:Im){reference-type="eqref" reference="eq:Im"} satisfies $M^2=M+zI$. Multiply by $M^{m-2}$ and take traces. Its two eigenvalues are $\lambda_\pm$.

# Every-target fibres

For $a\geq0$ and $b\in\{0,\ldots,a\}$, let $L_b^{(a)}$ be the $(a+1)\times(a+1)$ zero--one matrix $$\label{eq:localmatrix}
 L_b^{(a)}(u,v)=\mathbf1\{(u-v)_+=b\},
 \qquad 0\leq u,v\leq a.$$

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Let $y\in\operatorname{Div}(N)^m$ and put $b_{p,i}=\nu_p(y_i)$. Then $$\label{eq:fibre}
 |Q_N^{-1}(y)|=
 \prod_{p\mid N}\operatorname{tr}\left(
   L_{b_{p,0}}^{(a_p)}L_{b_{p,1}}^{(a_p)}\cdots
   L_{b_{p,m-1}}^{(a_p)}\right).$$ The formula is valid for $N=1$, $m=1$, $m=2$, zero exponents, and empty fibres. Moreover, $$\label{eq:mass}
 \sum_{y\in\operatorname{Div}(N)^m}|Q_N^{-1}(y)|=|\operatorname{Div}(N)|^m.$$

For a fixed prime, a source exponent word $u_0,\ldots,u_{m-1}$ contributes one to the matrix-product trace exactly when every cyclic local constraint $(u_i-u_{i+1})_+=b_{p,i}$ holds. This counts precisely the primewise predecessors. Unique factorization makes the choices for distinct primes independent, yielding [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

For each ordered pair $(u,v)$ there is exactly one output exponent $b=(u-v)_+$. Hence $\sum_{b=0}^aL_b^{(a)}=J_{a+1}$, the all-ones matrix. Summing the trace over all primewise targets gives $\operatorname{tr}(J_{a+1}^m)=(a+1)^m$. Multiplying these identities over the primes gives [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}.

The local matrices are particularly concrete. The zero-output matrix is the upper-triangular all-ones matrix $$\label{eq:U}
 L_0^{(a)}(u,v)=\mathbf1\{u\leq v\},$$ whereas for $b>0$, $L_b^{(a)}$ has one on the offset diagonal $u=v+b$ and zero elsewhere. Thus [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is an effective exact formula, not an existence statement about an unspecified automaton.

Let $\mathbf1=(1,\ldots,1)$. Then $$\label{eq:onefibre}
 |Q_N^{-1}(\mathbf1)|=|\operatorname{Div}(N)|.$$ Its predecessors are exactly the constant divisor words. More generally, if one prime divides every coordinate of a target word, that target has no predecessor.

For one prime, zero output at every site requires $u_0\leq u_1\leq\cdots\leq u_{m-1}\leq u_0$, so every exponent is constant; there are $a+1$ choices. Multiplication over primes proves [\[eq:onefibre\]](#eq:onefibre){reference-type="eqref" reference="eq:onefibre"}. If every target exponent for one prime is positive, then a predecessor would require the strict cyclic chain $u_0>u_1>\cdots>u_{m-1}>u_0$, which is impossible.

The matrix formula specializes to elementary boundary laws that are useful for checking the cyclic convention.

[\[cor:short-fibres\]]{#cor:short-fibres label="cor:short-fibres"} For $m=1$, the image is the single word $(1)$ and its fibre has size $|\operatorname{Div}(N)|$. For $m=2$, write the target as $(y_0,y_1)$ and put $b_{p,j}=\nu_p(y_j)$. Its fibre is empty unless $\gcd(y_0,y_1)=1$. When this condition holds, its size is $$\label{eq:short-fibre}
 \prod_{p^{a_p}\parallel N}
 \begin{cases}
  a_p+1,&b_{p,0}=b_{p,1}=0,\\
  a_p-b_{p,0}+1,&b_{p,0}>0,\\
  a_p-b_{p,1}+1,&b_{p,1}>0.
 \end{cases}$$ Every image word at length two is already fixed.

At length one, $(u-u)_+=0$. At length two, a primewise source pair $(u,v)$ maps to $((u-v)_+,(v-u)_+)$, so the two target exponents cannot both be positive. The zero--zero target has the $a_p+1$ sources $u=v$; a target $(b,0)$ with $b>0$ has $a_p-b+1$ sources $(v+b,v)$, and the reverse case is symmetric. Multiplication over primes proves [\[eq:short-fibre\]](#eq:short-fibre){reference-type="eqref" reference="eq:short-fibre"}.

Take $N=12=2^2\cdot3$ and $m=3$. The sharp height is two, witnessed by the word $(1,4,2)$: $$(1,4,2)\longmapsto(1,2,2)\longmapsto(1,1,2),$$ and the last word is fixed. Since $I_3(z)=1+3z$, the fixed-state count is $I_3(2)I_3(1)=7\cdot4=28$. This example also shows why the largest prime exponent, rather than the number or size of the prime divisors, controls the global tail.

The temporal proof and the inverse proof are logically separate: frozen-peak induction never uses a transfer matrix, and the trace count does not use eventual stabilization. The exact computation shipped with the manuscript checks finite boxes only. Direct-owner review remains open, so the result is not cleared for external circulation.
