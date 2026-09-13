---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--122-even-record-block-reversal"
canonical_tex: "symbolic_dynamics/papers/122-even-record-block-reversal/main.tex"
canonical_pdf: "symbolic_dynamics/papers/122-even-record-block-reversal/main.pdf"
source_sha256: "e443cc734b226a5c4d9a598369fc0f8fc42dc6b17ec5973815b9163c0896c576"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Even Record-Block Reversal: Sharp Descent, Exact Fibres, and a Finite-State Image Census

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/122-even-record-block-reversal>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/122-even-record-block-reversal/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/122-even-record-block-reversal/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/122-even-record-block-reversal/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/122-even-record-block-reversal/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Cut a permutation immediately before every left-to-right maximum, reverse all even-length record blocks simultaneously, and leave the odd blocks unchanged. We prove that every changed permutation decreases lexicographically and that the maximum transient depth on $\mathfrak S_n$ is exactly $n-1$. The fixed-point enumeration transfers, classically, to permutations with odd cycles and receives no contribution credit. The main results instead describe every one-step fibre by admissible target cuts and an explicit quadratic-arithmetic dynamic program, and compress all targets to a five-bit weighted automaton giving the image and Garden-of-Eden counts for every $n$. Exact enumeration through $n=9$ and the transfer through $n=30$ provide falsification controls. Record--cycle correspondence, record-indicator weights, and nearby left-to-right-maximum fibre methods are explicitly subtracted. The owner search is bounded; novelty and priority remain unresolved, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Even Record-Block Reversal:\
  Sharp Descent, Exact Fibres, and a Finite-State Image Census
```

## Markdown 正文

# The map and the residual claim

Let $\pi=\pi_1\cdots\pi_n\in\mathfrak S_n$. Insert a cut before every left-to-right maximum. The resulting unique factorization $$\pi=B_1B_2\cdots B_k                 \tag{1.1}$$ has two useful properties: every $B_i$ begins with its largest entry, and these leading entries increase with $i$. Define $\Phi(\pi)$ by reversing every even-length $B_i$, retaining every odd-length $B_i$, and concatenating the outputs synchronously. The empty permutation is fixed.

The record/cycle interface is classical. The precise maximum-first version of Foata's first fundamental transformation lists cycles by increasing maximum, writes each maximum first, and erases parentheses; it is stated explicitly by @RemmelWachs2004 [p. 40], with related fundamental- transformation background in @FoataHan2007. Thus its output cuts at left-to-right maxima are exactly the source cycles. Weighted cycle enumeration is also established [@Lugo2009]. These facts, the resulting fixed-point count, and generic lexicographic termination receive zero contribution credit.

Pointwise preimages of permutation operators described by left-to-right maxima are an active neighboring subject. @BouvelCioniFerrari2022 treat bubblesort preimages and functional trees, while @CioniFerrari2021 give recursive queuesort preimages, including a special left-to-right-maximum class. These own nearby permutation-operator fibre methods. @Huang2026 instead refine a greedy record statistic by record sets and endpoint paths in an order-polynomial setting; this is a record-set fibre neighbor, not a permutation self-map. None of these inspected sources states the literal map above, the endpoint-parity cut bijection below, or its image automaton. This is only a bounded non-hit.

There is also a strict internal firewall. P105 already occupies the broad silhouette "permutations, depth $n-1$, fibres, and Garden states" via cycle-minimum pruning and an iterate normal form. P117 uses parity-selected run reversal on cyclic binary words, and P120 uses parity-selected fringe mirroring on a fixed plane tree. Here record cuts are recomputed, rank is preserved, and the residual is specifically the target-cut bijection plus the weighted record-word automaton. The shared carrier, depth scale, or reversal vocabulary earns no contribution credit.

After those deductions, the residual package is:

1.  a sharp transient clock for the literal synchronous map;

2.  a bijection between every target fibre and its admissible cuts; and

3.  an all-size finite-state recurrence for the image and Garden-of-Eden counts.

Items (ii) and (iii) are distinct: the fibre theorem is target-local and retains multiplicity, whereas the image recurrence sums nonempty-fibre membership over all record sets without enumerating permutations.

# Strict descent and a sharp clock

The construction depends only on relative order. Thus standardization of a word on any finite totally ordered alphabet commutes with its record cuts, block reversals, and $\Phi$. We use this equivariance when reducing to a prefix.

[\[thm:clock\]]{#thm:clock label="thm:clock"} If $\Phi(\pi)\ne\pi$, then $$\Phi(\pi)<_{\rm lex}\pi.             \tag{2.1}\label{eq:lex}$$ Consequently $\Phi$ has no nontrivial cycles. Every orbit in $\mathfrak S_n$ reaches a fixed point in at most $n-1$ steps, and this bound is attained by $$\omega_n=(2,3,\ldots,n,1).             \tag{2.2}$$

Let $B$ be the first even record block. All earlier blocks are odd and unchanged. The first entry of $B$ is its strict maximum, whereas reversal puts its strictly smaller last entry at the first changed position. This proves [\[eq:lex\]](#eq:lex){reference-type="eqref" reference="eq:lex"}; finiteness then excludes nontrivial cycles.

Write uniquely $\pi=\alpha n\beta$. The final record block is $n\beta$. If $|\beta|$ is even, this block has odd length and remains inert at every later step, so the orbit is exactly the orbit of $\alpha$ with the fixed suffix $n\beta$. If $|\beta|$ is odd, then $$\Phi(\pi)=\Phi(\alpha)\operatorname{rev}(\beta)n.          \tag{2.3}$$ The final $n$ is thereafter a permanent singleton record block. After one step, standardize the preceding $n-1$ letters and apply induction. The empty prefix and $n=0,1$ supply the bases, giving depth at most $n-1$.

For $\omega_n$, the sole even block is $(n,1)$. One update gives $\omega_{n-1}n$, and the last entry remains a singleton. Hence its depth is $1+\operatorname{depth}(\omega_{n-1})=n-1$.

A permutation is fixed exactly when every record block has odd length. Foata's correspondence therefore makes the fixed points equinumerous with permutations all of whose cycles are odd. If $f_0=1$, then $$\sum_{n\ge0}f_n\frac{x^n}{n!}=\sqrt{\frac{1+x}{1-x}},\qquad
 f_{2m}=((2m-1)!!)^2,\qquad
 f_{2m+1}=(2m+1)!!(2m-1)!!.                              \tag{2.4}\label{eq:fixed}$$ For $m=0$, the last formula is read separately as $f_1=1$. Equation [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} is an owned control, not residual contribution mass.

# Every one-step fibre

Fix $\sigma=\sigma_1\cdots\sigma_n$, and put $M_j=\max(\sigma_1,\ldots,\sigma_j)$. A cut sequence $$0=i_0<i_1<\cdots<i_k=n              \tag{3.1}\label{eq:cuts}$$ is *admissible* if every segment $(i_{r-1},i_r]$ satisfies $$\begin{cases}
 \sigma_{i_{r-1}+1}=M_{i_r},&i_r-i_{r-1}\text{ odd},\\
 \sigma_{i_r}=M_{i_r},&i_r-i_{r-1}\text{ even}.
\end{cases}                                                \tag{3.2}\label{eq:admissible}$$

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} The preimages of $\sigma$ under $\Phi$ are in bijection with the admissible cut sequences [\[eq:cuts\]](#eq:cuts){reference-type="eqref" reference="eq:cuts"}. Given such cuts, retain every odd segment, reverse every even segment, and concatenate; this is the unique associated preimage.

Take a literal preimage and its unique record blocks. An unchanged odd block has its maximum at the first image endpoint; a reversed even block has its maximum at the last. Since the source block maxima increase, either endpoint is the maximum of the complete image prefix ending there. Thus its image cuts satisfy [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"}.

Conversely, reconstruct the segments as stated. Condition [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"} puts $M_{i_r}$ at the first position of the reconstructed segment, directly in the odd case and after reversal in the even case. In either parity case, the designated endpoint carrying $M_{i_r}$ lies in the reconstructed source segment. It therefore cannot be the earlier prefix maximum, whose entry lies before that segment; hence the successive values $M_{i_r}$ increase strictly. Every other entry of a segment is smaller than its first, so there is no extra record cut inside it. Hence the selected cuts are exactly the reconstructed word's record cuts. Applying $\Phi$ restores the target segments.

The constructions are inverse. In particular, two cut sequences cannot give the same preimage, since a permutation has a unique record-block decomposition.

The theorem immediately gives a target-local dynamic program. Set $h_0=1$, and for $1\le j\le n$ put $$h_j=\sum_{i=0}^{j-1}h_i\,
\mathbf 1\!\left[
 \begin{array}{l}
 j-i\text{ odd and }\sigma_{i+1}=M_j,\quad\text{or}\\
 j-i\text{ even and }\sigma_j=M_j.
 \end{array}\right] .                                     \tag{3.3}\label{eq:fibredp}$$

[\[cor:dp\]]{#cor:dp label="cor:dp"} For every target $\sigma$, $$|\Phi^{-1}(\sigma)|=h_n.           \tag{3.4}\label{eq:fibresize}$$ Thus $\sigma$ lies in the one-step image exactly when $h_n>0$. After prefix maxima are known, [\[eq:fibredp\]](#eq:fibredp){reference-type="eqref" reference="eq:fibredp"} uses $O(n^2)$ integer additions and indicator tests; no unit-cost bit-runtime claim is made.

Partition admissible cuts by the preceding cut $i$ of their final segment. The prefix has $h_i$ choices, and [\[eq:admissible\]](#eq:admissible){reference-type="eqref" reference="eq:admissible"} is exactly the displayed indicator. These classes are disjoint, proving [\[eq:fibredp\]](#eq:fibredp){reference-type="eqref" reference="eq:fibredp"}--[\[eq:fibresize\]](#eq:fibresize){reference-type="eqref" reference="eq:fibresize"}.

[\[rem:example\]]{#rem:example label="rem:example"} For $\sigma=12435$, the prefix maxima are $1,2,4,4,5$. Its four admissible endpoint sequences and reconstructed sources are $$\begin{array}{c@{\quad\longleftrightarrow\quad}c}
(1,2,3,5)&12453\\
(1,3,5)&14253\\
(1,5)&15342\\
(2,3,5)&21453.
\end{array}$$ Direct block reversal sends each source to $12435$, and the DP vector is $(h_0,\ldots,h_5)=(1,1,2,3,0,4)$. Thus the bijection, not only the final count, is visible in this example.

# A five-bit image automaton

The fibre DP depends on a target only through its record positions. We now turn this reduction into an all-size aggregate recurrence.

Let $r_j$ mark whether position $j$ is a record. Set $d_0=1$, and let $d_j$ mark whether the prefix of length $j$ admits cuts. After position $j$, retain the state $$s_j=(E_j,O_j,Q_j,L_j,D_j)\in\{0,1\}^5, \tag{4.1}$$ where, with OR over the displayed finite ranges, $$E_j=\bigvee_{\substack{0\le i\le j\\i\ {m even}}}d_i,
 \qquad
 O_j=\bigvee_{\substack{0\le i\le j\\i\ {m odd}}}d_i.$$ Also, $\ell_j$ is the most recent record position, $L_j=\ell_j\bmod2$, $Q_j=d_{\ell_j-1}$, and $D_j=d_j$.

After the forced record at position one, start at $$s_1=(1,1,1,1,1).                  \tag{4.2}\label{eq:start}$$ At a record position $j$, set $$\begin{split}
 L_j&=j\bmod2,\qquad Q_j=D_{j-1},\\
 D_j&=D_{j-1}\vee
 \begin{cases}E_{j-1},&j\text{ even},\\O_{j-1},&j\text{ odd};\end{cases}
\end{split}                                                \tag{4.3}\label{eq:recordtransition}$$ at a nonrecord position, set $$L_j=L_{j-1},\qquad Q_j=Q_{j-1},\qquad
 D_j=Q_{j-1}\wedge[j\equiv L_{j-1}\pmod2].                \tag{4.4}\label{eq:nonrecordtransition}$$ In either case, OR $D_j$ into the accumulator of parity $j$.

[\[lem:state\]]{#lem:state label="lem:state"} Equations [\[eq:start\]](#eq:start){reference-type="eqref" reference="eq:start"}--[\[eq:nonrecordtransition\]](#eq:nonrecordtransition){reference-type="eqref" reference="eq:nonrecordtransition"} compute the admissibility bit of [\[eq:fibredp\]](#eq:fibredp){reference-type="eqref" reference="eq:fibredp"}; in particular, five bits are sufficient.

At $j=1$, both the empty cut and the singleton prefix are reachable, so $d_0=d_1=1$, giving $(E_1,O_1,Q_1,L_1,D_1)=(1,1,1,1,1)$. Assume all five displayed invariants after position $j-1$.

If $j$ is a record, an odd final segment of length one is available exactly when $D_{j-1}=1$. An even final segment exists exactly when a reachable cut has the same parity as $j$, tested by $E_{j-1}$ or $O_{j-1}$. The new most recent record is $j$, so $L_j=j\bmod2$ and $Q_j=D_{j-1}$. This is precisely [\[eq:recordtransition\]](#eq:recordtransition){reference-type="eqref" reference="eq:recordtransition"}.

If $j$ is not a record, an even final segment is impossible. An odd one must begin at the most recent record $\ell_j=\ell_{j-1}$; it exists exactly when its preceding cut is reachable, $Q_{j-1}=d_{\ell_j-1}=1$, and its length is odd, $j\equiv L_{j-1}\pmod2$. This is [\[eq:nonrecordtransition\]](#eq:nonrecordtransition){reference-type="eqref" reference="eq:nonrecordtransition"}, while $Q,L$ persist. Finally, ORing the new $D_j=d_j$ into the parity-$j$ accumulator preserves the definitions of $E_j,O_j$. Induction proves all five invariants. Minimality of five bits is not claimed.

For the target in [\[rem:example\]](#rem:example){reference-type="ref" reference="rem:example"}, the record word is $R,R,R,N,R$. The complete bit trace is $$\begin{array}{c@{\quad}c@{\quad}ccccc}
j&r_j&E_j&O_j&Q_j&L_j&D_j\\ \midrule
1&R&1&1&1&1&1\\
2&R&1&1&1&0&1\\
3&R&1&1&1&1&1\\
4&N&1&1&1&1&0\\
5&R&1&1&0&1&1.
\end{array}$$

Let $R_j,N_j$ be the deterministic $0$-$1$ transition matrices on the 32 states for a record and nonrecord at position $j$, acting on columns. Let $v_1$ be the unit vector at [\[eq:start\]](#eq:start){reference-type="eqref" reference="eq:start"}. Define $$v_n=\bigl(R_n+(n-1)N_n\bigr)\cdots
       \bigl(R_2+N_2\bigr)v_1.                             \tag{4.5}\label{eq:transfer}$$

[\[thm:image\]]{#thm:image label="thm:image"} For $n\ge1$, the one-step image size is $$I_n=\sum_{s:D(s)=1}v_n(s),         \tag{4.6}\label{eq:image}$$ with $I_0=1$. Consequently the number of Garden-of-Eden permutations is $n!-I_n$ for every $n$.

Encode a permutation by the relative rank of its $j$th entry among its first $j$ entries. This is a bijection $\mathfrak S_n\to[1]\times[2]\times\cdots\times[n]$, and position $j$ is a record exactly when its rank is $j$. Hence a fixed record-position set $S\ni1$ has $$\prod_{j\notin S}(j-1)                   \tag{4.7}\label{eq:recordweight}$$ permutations. Thus the record transition has weight one and the nonrecord transition weight $j-1$, exactly as in [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}. Summing all terminal states gives $n!$; by [\[lem:state\]](#lem:state){reference-type="ref" reference="lem:state"}, restricting to $D=1$ gives precisely the targets with nonempty fibre.

The resulting image counts begin $$1,1,1,4,12,60,320,2160,15960,138880,\ldots   \tag{4.8}$$ for $0\le n\le9$. Formula [\[eq:recordweight\]](#eq:recordweight){reference-type="eqref" reference="eq:recordweight"} and record-indicator independence are classical and receive zero credit; the residual is their composition with the new admissibility state.

# Exact controls and claim boundary

Two standard-library implementations are included. The target-local verifier exhausts every source and target through $n=9$, reconstructs all admissible cuts, compares them with literal preimages and [\[eq:fibredp\]](#eq:fibredp){reference-type="eqref" reference="eq:fibredp"}, and checks fixed counts and fibre mass. The aggregate verifier independently implements [\[eq:start\]](#eq:start){reference-type="eqref" reference="eq:start"}--[\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}, checks literal image counts through $n=9$, record-set weights, total factorial mass, and continues the transfer through $n=30$. Together they make $1{,}637{,}027$ exact assertions.

The computation proves neither the all-size theorems nor ownership. No formula for maximum indegree, all depth layers, or iterated fibres is claimed. The manuscript likewise makes no claim of first occurrence, novelty, or priority. External circulation remains on hold pending a specialist search of the record-transformation and permutation-operator literatures.
