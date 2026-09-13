---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--117-odd-run-reversal-cyclic-words"
canonical_tex: "symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/main.tex"
canonical_pdf: "symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/main.pdf"
source_sha256: "61e9d0ee7af6491a93e713dfa57707ec739609438ec8029d8115eb9e7a064053"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Odd-Run Reversal on Cyclic Binary Words: Exact Recurrence and Sharp Parity-Dependent Transients

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/117-odd-run-reversal-cyclic-words/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On labelled cyclic binary words of length $n$, consider the parallel rule that flips every bit belonging to a maximal run of odd length. A boundary survives one round exactly when its two incident run lengths have the same parity; no new boundary is created. We prove that a word is recurrent exactly when all its cyclic run lengths have one parity. All eventual periods are therefore at most two. For odd $n$, the two constant words form the only recurrent orbit. For $n=2m$, the fixed-state count is $2^{m+1}-2$, while the number of period-two states is $$p_{2m}=\sum_{\substack{2\le r\le2m\\r\ {\rm even}}}
   \frac{4m}{r}\binom{m+r/2-1}{r-1}.$$ The main temporal result is the sharp maximum preperiod $$\max\operatorname{depth}=
   \begin{cases}
   (n-1)/2,&n\ \text{odd},\\
   \lfloor(n-2)/4\rfloor,&n\ \text{even}.
   \end{cases}$$ The odd case follows from run coalescence. The even case needs a different coordinate: label surviving boundaries by their site parity, delete a label when its two neighbours differ, and use a realization cost that drops by at least four at every mixed step. Binary-run enumeration, shrinking-cell models, cyclic compositions, and zeta bookkeeping receive zero contribution credit. The residual scope is only this rule-specific conjunction. Ownership, priority, and external circulation remain on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Odd-Run Reversal on Cyclic Binary Words: Exact Recurrence and Sharp Parity-Dependent Transients'
```

## Markdown 正文

# Introduction

A local update stated in terms of maximal runs is not a fixed-radius cellular automaton: a decision can depend on the distance to the next change of bit. It nevertheless has a simple lower-dimensional trace. The rule studied here flips every odd run simultaneously. Instead of tracking the bits, we track the boundaries between runs. They can disappear but never appear.

This places the mechanism near shrinking cellular automata, where deleted cells make their surviving neighbours adjacent [@RosenfeldWuDubitzki1983; @ModaneseWorsch2016; @KutribMalcherWendlandt2017]. Those models and their language-recognition theory are background, not claims of this paper. Static enumeration of binary runs and its connection with compositions are also mature; a current systematic account is [@BaladoSilvestre2026]. We give all such run and composition machinery zero contribution credit.

After that subtraction, four exact statements remain for one specified finite self-map. First, boundary survival is governed only by the parities of the two incident run lengths. Second, this gives a complete recurrent classification and labelled census. Third, elementary coalescence proves a sharp clock at odd circumference. Fourth, even circumference carries an intrinsic parity label on each boundary; its induced eroder and a cost-drop lemma prove a different sharp clock.

The parity distinction is essential. Counting boundaries gives the exact odd bound but loses a factor of two in the even case. Conversely, boundary site parity is globally well defined only when the circumference is even. The two proof routes therefore meet at the survival lemma and then separate.

We count labelled words, not rotation classes. We do not determine every basin layer or claim that the update is identical to a named shrinking automaton. A bounded owner search did not expose the same temporal conjunction, but a search miss is neither novelty evidence nor a priority certificate. External dissemination remains **HOLD**.

# The update and its boundary trace

Let $\mathbb Z_n=\mathbb Z/n\mathbb Z$, with $n\ge1$, and let $\mathcal W_n=\{0,1\}^{\mathbb Z_n}$. A *cyclic run* is a maximal cyclic interval on which a word is constant. A constant word has one run, of length $n$.

[\[def:update\]]{#def:update label="def:update"} For $w\in\mathcal W_n$, the word $\mathcal F_n(w)$ is obtained by flipping every bit in every odd-length cyclic run of $w$, simultaneously, and retaining every bit in an even-length run.

For a nonconstant word, let $\mathcal B(w)\subseteq\mathbb Z_n$ be its set of run starts: $i\in\mathcal B(w)$ when $w(i-1)\ne w(i)$. In cyclic order write the run lengths as $\ell_0,\ldots,\ell_{r-1}$. Here $r=|\mathcal B(w)|$ is even.

[\[lem:survival\]]{#lem:survival label="lem:survival"} No new run boundary is created. The boundary between consecutive runs of lengths $\ell_{i-1}$ and $\ell_i$ survives one update if and only if $$\ell_{i-1}\equiv\ell_i\pmod2.$$

Every bit of one old run receives the same flip decision, so no boundary can appear inside it. Let the bit on the left of an old boundary be $a$, and the bit on the right be $1-a$. Put $\epsilon=\ell_{i-1}\bmod2$ and $\eta=\ell_i\bmod2$. The two new endpoint bits are $$a+\epsilon,\qquad 1-a+\eta
                  \quad\text{in }\mathbb F_2.$$ They remain different exactly when $\epsilon=\eta$.

[\[thm:recurrence\]]{#thm:recurrence label="thm:recurrence"} A word is recurrent under $\mathcal F_n$ if and only if all of its cyclic run lengths have the same parity. In that case it is fixed when all run lengths are even and has exact period two when all run lengths are odd. Every orbit has eventual period at most two.

By [\[lem:survival\]](#lem:survival){reference-type="ref" reference="lem:survival"}, boundary sets decrease under inclusion. If an orbit returns to a previous word, its boundary set cannot have decreased anywhere along the intervening segment. Every boundary therefore survives the first round of that segment. Equality of the two incident parities at every boundary propagates around the cyclic run list, so all run lengths have one parity.

Conversely, if all runs are even, no bit flips and the word is fixed. If all runs are odd, every bit flips. The resulting complement has the same run decomposition, so the next update returns to the original word. A binary word never equals its bitwise complement, hence this period is exactly two. Every finite orbit eventually becomes recurrent, which proves the last claim.

# Exact recurrent census

Let $f_n$ and $p_n$ denote the numbers of fixed and exact-period-two states, respectively.

[\[thm:census\]]{#thm:census label="thm:census"} For odd $n$, $$f_n=0,\qquad p_n=2.$$ For $n=2m$, $$\begin{aligned}
 f_{2m}&=2^{m+1}-2,                                      \label{eq:fixed}\\
 p_{2m}&=\sum_{\substack{2\le r\le2m\\r\ {\rm even}}}
 \frac{4m}{r}\binom{m+r/2-1}{r-1}.                       \label{eq:two}\end{aligned}$$

A nonconstant binary cyclic word has an even number of runs. If $n$ is odd, neither a sum of even run lengths nor a sum of an even number of odd run lengths can equal $n$. Thus only the two constant words recur. Their single run has odd length, so they form a two-cycle.

Now let $n=2m$. For a nonconstant fixed word, all boundary gaps are even. Equivalently, its nonempty boundary set is an even-cardinality subset of one of the two parity classes in $\mathbb Z_{2m}$. Each parity class has $m$ sites and $2^{m-1}-1$ nonempty even subsets. Each boundary set supports two complementary words. Adding the two constant words gives $$2\cdot2(2^{m-1}-1)+2=2^{m+1}-2.$$

For an exact-period-two word with $r$ runs, every run length is positive and odd. Writing $\ell_i=2x_i+1$, stars and bars gives $$\#\{(\ell_0,\ldots,\ell_{r-1}):\ell_i\text{ odd},
       \ \sum_i\ell_i=2m\}
 =\binom{m+r/2-1}{r-1}.$$ Choose a labelled distinguished boundary in $2m$ ways and the bit after it in two ways, then divide by the $r$ possible distinguished boundaries of the same word. Summing over even $r$ proves [\[eq:two\]](#eq:two){reference-type="eqref" reference="eq:two"}.

For a finite map $F$, write $$\zeta_F(z)=\exp\!\left(\sum_{j\ge1}
          \frac{|\operatorname{Fix}(F^j)|}{j}z^j\right).$$ This periodic-point construction is standard [@ArtinMazur1965].

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} $$\zeta_{\mathcal F_n}(z)=(1-z)^{-f_n}(1-z^2)^{-p_n/2},$$ with $f_n,p_n$ from [\[thm:census\]](#thm:census){reference-type="ref" reference="thm:census"}.

leaves only fixed orbits and two-cycles. The formula is the routine product of one factor for every primitive cycle.

::: {#tab:census}
    $n$   fixed states   period-two states   two-cycles   max preperiod
  ----- -------------- ------------------- ------------ ---------------
      1              0                   2            1               0
      2              2                   2            1               0
      3              0                   2            1               1
      4              6                  10            5               0
      5              0                   2            1               2
      6             14                  32           16               1
      7              0                   2            1               3
      8             30                  90           45               1
      9              0                   2            1               4
     10             62                 242          121               2

  : Exact recurrent census and sharp maximum preperiod for small orders. The table is illustrative; the formulas hold for every $n$.
:::

# The sharp odd clock

Define the preperiod $$\operatorname{depth}(w)=\min\{t\ge0:\mathcal F_n^t(w)\text{ is recurrent}\}.$$

[\[thm:odd-depth\]]{#thm:odd-depth label="thm:odd-depth"} If $n$ is odd, then $$\max_{w\in\mathcal W_n}\operatorname{depth}(w)=\frac{n-1}{2}.$$

At a nonrecurrent state, some adjacent run parities differ. The number of deleted cyclic boundaries is even and positive, so at least two boundaries disappear. An odd cyclic word has at most $n-1$ boundaries: a boundary at every site would be an alternating cycle, which exists only at even circumference. Monotone boundary loss therefore gives $\operatorname{depth}(w)\le(n-1)/2$.

For sharpness, write $n=2t+1$. Use the cyclic run composition consisting of one part of length two and $2t-1$ parts of length one. The unique even run has an odd run on each side. At the next update both incident boundaries disappear, and these three runs coalesce into one even run. Every other boundary, lying between two odd runs, survives. The same description repeats for the first $t-1$ rounds, with two fewer odd singleton runs each time. The remaining run composition is then $(2t,1)$; its last two boundaries disappear together, leaving the odd constant run of length $2t+1$. Thus the first recurrent state occurs after exactly $t$ rounds. (For $t=1$, this last two-run collapse is the only round.) For $n=1$, the constant word is already recurrent and the same formula gives zero.

# The parity eroder and the sharp even clock

Assume throughout this section that $n$ is even. If a nonconstant word has surviving boundaries $$b_0,b_1,\ldots,b_{r-1}\in\mathbb Z_n$$ in cyclic order, define its *boundary-parity word* $$q_i=b_i\bmod2.$$ This label is intrinsic because reduction modulo two is well defined on $\mathbb Z_n$ exactly when $n$ is even. The run between $b_i$ and $b_{i+1}$ has parity $q_i+q_{i+1}$ in $\mathbb F_2$. Applying [\[lem:survival\]](#lem:survival){reference-type="ref" reference="lem:survival"} at $b_i$ yields the following autonomous rule.

[\[def:eroder\]]{#def:eroder label="def:eroder"} For a cyclic binary word $q$, let $Dq$ be the subsequence that retains position $i$ precisely when $$q_{i-1}=q_{i+1}.$$ The cyclic order of retained positions is unchanged.

Thus the boundary-parity word after one $\mathcal F_n$-update is exactly $Dq$. The recurrent parity words are constant and alternating: they correspond, respectively, to all-even and all-odd original run lengths.

For a nonempty cyclic word $q$, let $$e(q)=|\{i:q_i=q_{i+1}\}|,\qquad C(q)=|q|+e(q).$$ Put $C(\varnothing)=0$.

[\[lem:cost\]]{#lem:cost label="lem:cost"} If $q$ is the boundary-parity word of a cyclic word of circumference $n$, then $q$ has even length and $n\ge C(q)$. Conversely, every nonempty cyclic binary word $q$ of even length is realizable as a boundary-parity word at circumference $C(q)$, and at every circumference $C(q)+2j$, $j\ge0$. The empty word is realized by either constant word.

The positive gap from $b_i$ to $b_{i+1}$ is even when $q_i=q_{i+1}$, so it costs at least two, and is odd otherwise, so it costs at least one. Summing the gap minima gives $$2e(q)+(|q|-e(q))=C(q).$$ Taking every gap at its minimum realizes equality. Adding two to any one gap preserves every boundary parity and realizes all larger circumferences of the same parity. Since a binary cyclic word has an even number of boundaries, alternating bit values can be assigned consistently between the chosen positions.

[\[lem:drop\]]{#lem:drop label="lem:drop"} If $q$ is neither constant nor alternating and has even length, then $$C(Dq)\le C(q)-4.$$

Decompose $q$ into cyclic constant runs. A singleton run survives. A run of length two disappears. A run of length at least three loses its two endpoints and retains its interior.

Let $a$ be the number of nonsingleton runs and $h\le a$ the number of length-two runs. If $s$ is the number of transitions of $q$, then $e(q)=|q|-s$, so $C(q)=2|q|-s$. The update deletes exactly $2a$ symbols. Only a disappearing length-two run can merge its two neighbouring surviving runs; deleting one such run lowers the transition count by at most two. Thus, with $s'$ the transition count after deletion (and with the transition count of the empty word defined to be zero), $$|Dq|=|q|-2a,\qquad s'\ge s-2h.$$ Consequently $$C(q)-C(Dq)=4a+s'-s\ge4a-2h.$$ If $a\ge2$, the right side is at least $2a\ge4$.

It remains to consider $a=1$. All other constant runs are singletons. Both the total length and the number of cyclic runs are even, so the unique nonsingleton run has odd length, necessarily at least three. It remains nonempty, no run disappears, and $s'=s$. The cost drop is then exactly four.

[\[thm:even-depth\]]{#thm:even-depth label="thm:even-depth"} If $n$ is even, then $$\max_{w\in\mathcal W_n}\operatorname{depth}(w)
        =\left\lfloor\frac{n-2}{4}\right\rfloor.$$

A mixed even-length parity word has at least four symbols. Its number of equal adjacencies is positive and even, hence at least two. Therefore its cost is at least six. If an original word has preperiod $t\ge1$, its parity words before rounds $0,\ldots,t-1$ are mixed. Applying [\[lem:drop\]](#lem:drop){reference-type="ref" reference="lem:drop"} for the first $t-1$ transitions and then [\[lem:cost\]](#lem:cost){reference-type="ref" reference="lem:cost"} gives $$n\ge6+4(t-1)=4t+2.$$ Thus $t\le\lfloor(n-2)/4\rfloor$.

For sharpness, fix $t\ge1$ and take $$q=0^{\,2t+1}1.$$ Its cost is $4t+2$. Each eroder round removes the two endpoints of the long zero run. After exactly $t$ rounds it becomes the alternating word $01$, and no earlier state is recurrent. By [\[lem:cost\]](#lem:cost){reference-type="ref" reference="lem:cost"}, this boundary word is realized by an original cyclic word at circumference $4t+2$; adding two to one gap realizes circumference $4t+4$ with the same parity dynamics. These are exactly the two even circumferences for which $\lfloor(n-2)/4\rfloor=t$. At $n=2,4$, the claimed maximum is zero and the recurrent classification verifies it directly.

# Exact controls, scope, and conclusion

The accompanying deterministic verifier exhausts all $2^n$ labelled words for $1\le n\le16$. It directly checks one-step boundary survival and the induced parity eroder, as well as recurrence, the exact census, both sharp depth formulas, and extremal witnesses. A second exact lane enumerates all $349{,}524$ even-length parity words through length eighteen, constructs their minimum-cost realizations, and checks the four-unit drop on all $349{,}488$ mixed cases. A fresh run executes $1{,}529{,}158$ exact assertions. This finite calculation is falsification and regression evidence; none of the all-$n$ statements depends on it.

The result is deliberately narrow. It gives no complete transient-layer distribution and no orbit census modulo rotation. Shrinking automata, binary-run enumeration, cyclic compositions, and periodic-point zeta bookkeeping are prior tools and receive zero credit. The labelled census is a routine enumerative corollary once the temporal classification is known. What remains is the exact map-specific conjunction for odd-run reversal: the boundary survival law, complete recurrence, and the two parity-sensitive sharp clocks. Owner clearance, priority, and external release remain on hold.
