---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--139-lyndon-factor-start-feedback"
canonical_tex: "symbolic_dynamics/papers/139-lyndon-factor-start-feedback/main.tex"
canonical_pdf: "symbolic_dynamics/papers/139-lyndon-factor-start-feedback/main.pdf"
source_sha256: "97299a0a7b211a8434e3bf96612969d4cad8013796820181b2c723d3130e0af3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Iterating Lyndon-Factor Starts on Binary Words

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/139-lyndon-factor-start-feedback>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/139-lyndon-factor-start-feedback/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/139-lyndon-factor-start-feedback/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/139-lyndon-factor-start-feedback/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/139-lyndon-factor-start-feedback/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $0<1$ and replace a binary word by the mask of the starting positions in its nonincreasing Chen--Fox--Lyndon factorization, and iterate this mask map. The classical suffix-array characterization of factor starts is imported as owned static input and receives no contribution credit. In the resulting dynamics, every leading $1$ is a singleton Lyndon factor, so the leading-one prefix grows under every nonfixed update. We prove that $1^n$ is the unique recurrent state and that every orbit reaches it within $n$ steps. The bound is sharp at a unique state, the alternating word $0101\cdots$. For every target mask, we also identify the complete fibre with the nonincreasing chains of binary Lyndon words having prescribed lengths and express its size as a product of rectangular comparison matrices. The one-factor and all-singleton targets give the classical binary Lyndon census and $n+1$. All static factorization, suffix-record, and enumeration results are credited background. External release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Iterating Lyndon-Factor Starts on Binary Words'
```

## Markdown 正文

# Factor-start feedback and the credit boundary

Words are ordered lexicographically over $0<1$, with a proper prefix smaller than the longer word. A nonempty word $u$ is *Lyndon* if it is strictly smaller than each of its nontrivial rotations. The classical Chen--Fox--Lyndon theorem [@ChenFoxLyndon1958] gives every nonempty word a unique factorization $$\label{eq:CFL}
 w=u_1u_2\cdots u_k,\qquad u_1\ge u_2\ge\cdots\ge u_k,$$ into Lyndon words; repeated factors are written separately.

Let $1=s_1<s_2<\cdots<s_k\le n$ be the factor starts in [\[eq:CFL\]](#eq:CFL){reference-type="eqref" reference="eq:CFL"}. Define the binary self-map $L_n:\{0,1\}^n\to\{0,1\}^n$ by $$\label{eq:map}
 L_n(w)_i=1\quad\Longleftrightarrow\quad i\in\{s_1,\ldots,s_k\}.$$ The factorization is recomputed from the mask after every update.

Duval computes [\[eq:CFL\]](#eq:CFL){reference-type="eqref" reference="eq:CFL"}, the least suffix, and the least circular shift in linear time [@Duval1983]. Lyndon arrays and forests have their own algorithmic theory [@FranekIslamRahmanSmyth2016; @BadkobehCrochemore2022]. Mantaci, Restivo, Rosone, and Sciortino prove that the CFL factor starts are exactly the left-to-right minima of the suffix-rank permutation [@MantaciRestivoRosoneSciortino2014 Theorem 2.2]. The equivalent strict suffix-record formulation and the ordered-tail comparison used to recover it are therefore owned static inputs. We restate them in [2](#sec:owned){reference-type="ref" reference="sec:owned"} only to fix conventions; they receive zero contribution credit.

The CFL theorem, all suffix-array and factor-start characterizations, the algorithms above, the binary Lyndon census, necklace Möbius inversion, and matrix multiplication are likewise zero-credit background. After this subtraction, the residual package consists only of the recurrent dynamics of the repeated map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, its sharp unique depth-$n$ state, and its target-wise ordered-Lyndon fibre atlas.

A state is recurrent if it lies on a directed cycle. Its depth is the first time its orbit reaches a recurrent state.

# Owned static interface: suffix records {#sec:owned}

The suffix-record equivalence in this section is exactly the static result of @MantaciRestivoRosoneSciortino2014 [Theorem 2.2], written in suffix notation rather than inverse-suffix-array notation. We reproduce a proof so that the orientation and strictness convention are auditable, but neither the statement nor the proof is a residual contribution.

The proof uses two classical consequences of the Lyndon definition. A Lyndon word is unbordered and is strictly smaller than each of its nonempty proper suffixes. It also uses the ordered-tail comparison underlying the CFL theorem: if $u_1\ge\cdots\ge u_k$ are Lyndon and $S_h=u_h\cdots u_k$, then $$\label{eq:taildescent}
 S_1>S_2>\cdots>S_k.$$ Here is the short reduction, including equal factors. It is enough to compare adjacent tails. Fix $h$, put $u=u_h$, and remove from both tails the common initial copies of $u$ occurring in $S_{h+1}$. If no word remains on the right, that right-hand word is a proper prefix. Otherwise it begins with a Lyndon factor $v<u$; the classical Lyndon concatenation comparison says $uz>z$ whenever the CFL factors of $z$ begin with $v<u$ and thereafter do not increase. Thus $S_h>S_{h+1}$ in both cases. This is a static comparison lemma, not a dynamical contribution; it is also the comparison step in the standard proof of the CFL factorization [@ChenFoxLyndon1958; @Duval1983]. This ordered-tail comparison is owned static machinery and receives zero contribution credit as well.

[\[prop:records\]]{#prop:records label="prop:records"} For $w=w_1\cdots w_n$, position $i$ starts a factor in [\[eq:CFL\]](#eq:CFL){reference-type="eqref" reference="eq:CFL"} if and only if its suffix is a strict new minimum among the suffixes seen from the left: $$\label{eq:record}
 L_n(w)_i=1
 \quad\Longleftrightarrow\quad
 w_i\cdots w_n<w_j\cdots w_n\quad\text{for every }j<i.$$

Write $S_h=u_hu_{h+1}\cdots u_k$ for the suffix beginning at factor $u_h$. By [\[eq:taildescent\]](#eq:taildescent){reference-type="eqref" reference="eq:taildescent"}, each later factor-start suffix is strictly smaller than every earlier factor-start suffix; repeated equal factors are included in the proper-prefix case of the reduction above.

Now take a position $q$ strictly inside $u_h$, and write $v$ for the proper suffix of $u_h$ beginning there. Since $u_h$ is Lyndon, $u_h<v$. The two words are not in a prefix relation: $v$ is shorter, while $v$ cannot be a prefix of $u_h$ because that would make it a border. Appending the same later factor tail therefore preserves the strict comparison, so $S_h$ is smaller than the suffix beginning at $q$.

If $i=s_j$ is a factor start, every earlier position is either an earlier factor start, whose suffix is larger by the first paragraph, or lies inside an earlier factor, whose suffix is larger than that factor-start suffix by the second paragraph. Hence [\[eq:record\]](#eq:record){reference-type="eqref" reference="eq:record"} holds. Conversely, if $i$ lies inside $u_h$, the earlier position $s_h$ has a strictly smaller suffix, so $i$ is not a new minimum. This proves both directions.

Strictness matters when consecutive factors are equal. For example, the CFL factorization of $00$ is $0\,0$, and the second suffix $0$ is strictly smaller than the first suffix $00$ because it is a proper prefix.

Thus [\[prop:records\]](#prop:records){reference-type="ref" reference="prop:records"} supplies an intrinsic implementation check for the map, but it is not counted among the paper's residual theorems.

# The leading-one amplifier

[\[lem:prefix\]]{#lem:prefix label="lem:prefix"} If $w=1^r0s$ with $0\le r<n$, then $$\label{eq:prefix}
 L_n(w)=1^r L_{n-r}(0s).$$ More generally, $L_{m+1}(1v)=1L_m(v)$ for every $v\in\{0,1\}^m$.

A binary Lyndon word of length greater than one begins with zero: a word beginning in one and containing a zero has a smaller rotation beginning at that zero, while $1^d$ is not primitive for $d>1$. Hence every leading one in $w$ is a singleton Lyndon factor. The first factor of the nonempty remainder $0s$ begins in zero and is therefore smaller than the singleton $1$. Uniqueness of [\[eq:CFL\]](#eq:CFL){reference-type="eqref" reference="eq:CFL"} shows that the full factorization is the $r$ singleton factors followed by the CFL factorization of $0s$, proving [\[eq:prefix\]](#eq:prefix){reference-type="eqref" reference="eq:prefix"}.

For arbitrary $v$, either $v=1^m$, when the last statement is immediate, or $v=1^q0s$ and [\[eq:prefix\]](#eq:prefix){reference-type="eqref" reference="eq:prefix"} applied with $r=q$ and $r=q+1$ gives the identity.

Let $\lambda(w)$ be the number of leading ones in $w$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} The word $1^n$ is the unique fixed point and the unique recurrent state of $L_n$. Every orbit reaches it in at most $n$ updates.

The CFL factorization of $1^n$ consists of $n$ singleton factors, so $1^n$ is fixed. If $w\ne1^n$, write $w=1^r0s$. Equation [\[eq:prefix\]](#eq:prefix){reference-type="eqref" reference="eq:prefix"} shows that the first $r$ output bits are one, and the first bit of $L_{n-r}(0s)$ is also one because every nonempty factorization has a first factor. Thus $\lambda(L_n(w))\ge r+1$. The integer $\lambda$ strictly increases at every nonfixed update and is bounded by $n$. No other recurrent state can exist, and at most $n$ updates are required.

# The sharp and unique deepest word

Let $a_n=0101\cdots$ be the length-$n$ alternating word beginning in zero.

[\[lem:alternating\]]{#lem:alternating label="lem:alternating"} For every $n\ge1$, $$\label{eq:alternating}
 L_n(a_n)=1a_{n-1},$$ where $a_0$ is empty.

The word $01$ is Lyndon. If $n=2m$, the CFL factorization of $a_n$ is $(01)^m$, written as $m$ equal factors. If $n=2m+1$, it is $(01)^m0$; this is nonincreasing because $01>0$. The starts are exactly the odd positions, which is the mask $1a_{n-1}$. At $n=1$, the factorization is the singleton $0$ and the same identity holds.

[\[thm:unique\]]{#thm:unique label="thm:unique"} The maximum depth of $L_n$ is $n$. Its unique depth-$n$ state is $a_n$.

By [\[lem:prefix\]](#lem:prefix){reference-type="ref" reference="lem:prefix"}, prefixing a word by one does not change its depth: the identity $L_{m+1}(1v)=1L_m(v)$ persists under iteration, including when $v$ becomes all ones. Therefore [\[eq:alternating\]](#eq:alternating){reference-type="eqref" reference="eq:alternating"} and induction give $$\operatorname{depth}(a_n)=1+\operatorname{depth}(a_{n-1})=n,$$ with $a_1=0\mapsto1$. This attains the upper bound in [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}.

We prove uniqueness by induction. At $n=1$, the word $0$ is the only state of depth one. Let $n\ge2$ and suppose $w$ has depth $n$. Its image has depth $n-1$ and begins in one. Write $L_n(w)=1v$. Prefix invariance of depth and the induction hypothesis force $v=a_{n-1}$, so $$\label{eq:forcedmask}
 L_n(w)=1a_{n-1}.$$ The one-positions in this mask prescribe CFL factor lengths $(2,2,\ldots,2)$ when $n$ is even and $(2,2,\ldots,2,1)$ when $n$ is odd. The only binary Lyndon word of length two is $01$. In the odd case, the last singleton cannot be $1$, because the required nonincrease would read $01\ge1$, which is false; it must be $0$. Hence $w=(01)^{n/2}$ for even $n$, and $w=(01)^{(n-1)/2}0$ for odd $n$. In both cases $w=a_n$.

# Every target fibre as an ordered Lyndon chain

For $d\ge1$, let $\mathcal L_d$ be the lexicographically ordered set of binary Lyndon words of length $d$. If a target $y\in\{0,1\}^n$ begins in one, its one-positions determine a composition $\ell(y)=(\ell_1,\ldots,\ell_k)$ of $n$: these are the successive gaps between factor starts, with the last gap ending at $n+1$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} If $y_1=0$, then $L_n^{-1}(y)$ is empty. If $y_1=1$ and $\ell(y)=(\ell_1,\ldots,\ell_k)$, then $$\label{eq:fibre}
 |L_n^{-1}(y)|
 =\#\{(u_1,\ldots,u_k):u_i\in\mathcal L_{\ell_i},\
                         u_1\ge\cdots\ge u_k\}.$$ Thus positivity of the right-hand side is the complete image criterion.

Every factor-start mask begins with one, giving the first assertion. For a target beginning in one, any preimage has factors starting at exactly its one-positions, so their lengths are $\ell_1,\ldots,\ell_k$. By the CFL theorem, those factors are Lyndon and nonincreasing, which maps the fibre into the set on the right of [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Conversely, concatenate any tuple on the right. It is already a nonincreasing factorization into Lyndon words; uniqueness of [\[eq:CFL\]](#eq:CFL){reference-type="eqref" reference="eq:CFL"} makes it the CFL factorization of the concatenation, whose start mask is $y$. The two constructions are inverse.

The count has a finite matrix form. For positive $a,b$, let $M_{a,b}$ be the $|\mathcal L_a|\times|\mathcal L_b|$ zero-one matrix $$\label{eq:matrix}
 M_{a,b}(u,v)=\mathbf 1\{u\ge v\},\qquad u\in\mathcal L_a, v\in\mathcal L_b,$$ and let $\mathbf 1_d$ be the all-one column indexed by $\mathcal L_d$.

[\[cor:special\]]{#cor:special label="cor:special"} For $k\ge2$, the fibre in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} equals $$\label{eq:product}
 \mathbf 1_{\ell_1}^{\mathsf T}
 M_{\ell_1,\ell_2}\cdots
 M_{\ell_{k-1},\ell_k}\mathbf 1_{\ell_k};$$ for $k=1$ it equals $|\mathcal L_{\ell_1}|$. Moreover, $$\begin{aligned}
 |L_n^{-1}(10^{n-1})|
   &=\frac1n\sum_{d\mid n}\mu(d)2^{n/d},\label{eq:onefactor}\\
 |L_n^{-1}(1^n)|&=n+1.\label{eq:allstarts}\end{aligned}$$

Expanding [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} sums one for each tuple satisfying all adjacent inequalities, exactly as in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. The target $10^{n-1}$ prescribes the one-part composition $(n)$, so its fibre is $\mathcal L_n$. The classical primitive-necklace Möbius formula gives [\[eq:onefactor\]](#eq:onefactor){reference-type="eqref" reference="eq:onefactor"}. For $1^n$, every factor has length one. The two one-letter Lyndon words are $0$ and $1$, and a nonincreasing sequence is uniquely $1^j0^{n-j}$ for some $0\le j\le n$, proving [\[eq:allstarts\]](#eq:allstarts){reference-type="eqref" reference="eq:allstarts"}.

# Exact control and limitations

The paper-local verifier independently computes the Duval mask and the strict suffix-record mask for every binary word through $n=18$. Their comparison is an integration check for the imported theorem of Mantaci et al., not evidence for a residual claim. The verifier also constructs every functional graph in that range, totaling $524{,}286$ states, and checks the fixed atlas, clock, and unique deepest word. A separate Lyndon-word generator and rectangular-matrix evaluator agrees with every literal target fibre through $n=14$; the two special fibres are checked through $n=18$. The canonical run executes $2{,}654{,}300$ exact assertions.

Finite enumeration is only counterexample pressure. The observed image and largest-fibre sequences are not promoted to unproved all-length statements. The suffix-record theorem and ordered-tail comparison are explicitly owner-subtracted; the residual is limited to the iterated start-mask dynamics, the sharp unique depth-$n$ orbit, and the ordered-Lyndon fibre atlas. The owner search for that residual is bounded, so a non-hit is not a novelty or priority certificate. This anonymous artifact remains `HOLD_EXTERNAL`; public posting, submission, and release are not authorized.
