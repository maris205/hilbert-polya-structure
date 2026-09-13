---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--131-euclidean-quotient-queues"
canonical_tex: "symbolic_dynamics/papers/131-euclidean-quotient-queues/main.tex"
canonical_pdf: "symbolic_dynamics/papers/131-euclidean-quotient-queues/main.pdf"
source_sha256: "698301de313a91d70a44f9c3daf9fe02a25cf5233c9cd40f878c6e9cd278dc0c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cyclic Euclidean-Quotient Queues: Terminal Cores, Depth Layers, and Small Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/131-euclidean-quotient-queues>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/131-euclidean-quotient-queues/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/131-euclidean-quotient-queues/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/131-euclidean-quotient-queues/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/131-euclidean-quotient-queues/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix the sum $N$ of the canonical continued-fraction digits of a rational in $(0,1)$. We move its first Euclidean quotient to the back of the queue and, when necessary, apply the terminal-one identity that restores the unique finite expansion. The entrance time is exactly the position of the last quotient equal to one, with sharp maximum $N-2$. We give a cyclic run-absorption decoder for the terminal core and identify the eventual period with its primitive rotation period. Formal generating functions enumerate every exact-depth layer. Two explicit inverse branches give every one-step fibre, the image, and all Garden states; fibres have size at most two. A second derivation uses the alternating run blocks of the subtractive Euclidean path. Restricted compositions, Stern--Brocot coding, continuants, and necklace enumeration are treated as background. The owner search is bounded; no novelty, priority, or external-release claim is made.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Cyclic Euclidean-Quotient Queues:\
  Terminal Cores, Depth Layers, and Small Fibres
```

## Markdown 正文

# An honest rational level and the queue map

Every rational $q\in(0,1)$ has a unique canonical finite regular continued fraction $$q=[0;a_1,\ldots,a_k],\qquad a_i\ge1,\quad a_k\ge2.$$ For $N\ge2$, define $$\mathcal R_N=\{q\in\mathbb Q:0<q<1,\ \textstyle\sum_i a_i=N\}.$$ The levels $N=0,1$ are empty. Subtracting one from the final digit identifies the digit words in $\mathcal R_N$ with the positive compositions of $N-1$, so $$|\mathcal R_N|=2^{N-2}.                \label{eq:size}$$

To fix the Euclidean convention, write $q=u/v$ in lowest terms. Repeatedly subtract the smaller positive coordinate from the larger, recording $L$ for $v\leftarrow v-u$ and $R$ for $u\leftarrow u-v$. At equality, repeat the preceding letter: if it was $L$, record $L$ and perform $v\leftarrow v-u=0$; if it was $R$, record $R$ and perform $u\leftarrow u-v=0$. A preceding letter always exists because initially $0<u<v$. The run word is $$E(q)=L^{a_1}R^{a_2}L^{a_3}\cdots,                     \label{eq:path}$$ with alternating letters, and its length is $N$. This follows by grouping successive subtractions between exchanges of the smaller coordinate; the last equality step belongs to the final quotient, explaining $a_k\ge2$. Thus $N$ is the step count for this explicitly stated subtractive algorithm. Euclidean cost statistics are established territory [@MinelliSourmelidisTechnau2023], and the Stern--Brocot/run-word relation is classical [@Reutenauer2019]; both receive zero contribution credit.

On digit words put $$\Phi(a_1,\ldots,a_k)=
 \begin{cases}
 (a_1),&k=1,\\
 (a_2,\ldots,a_k,a_1),&k>1,\ a_1>1,\\
 (a_2,\ldots,a_{k-1},a_k+1),&k>1,\ a_1=1.
 \end{cases}                                           \label{eq:update}$$ The final branch is rotation followed by the canonical identity $[\ldots,b,1]=[\ldots,b+1]$. It is part of the definition, not an optional postprocessing step. Digit sum and the terminal condition are preserved, so $\Phi$ is a self-map of every $\mathcal R_N$.

Finite words, continuants, prefixes, endings, and cyclic permutations are well-developed interfaces [@Kan2026; @Jones2026]. Cyclic and restricted-part compositions likewise have direct enumerative owners [@GibsonJustWang2018; @Hadjicostas2016]. All uniqueness, continuant, composition, regular-language, Burnside, and divisor-counting machinery is zero credit. Internally, P117 already owns cyclic run reduction and recurrent classification language, while P122 owns the sharp-linear-clock plus target-fibre/image/Garden presentation silhouette; both receive zero credit. P126 is the hard collision: after $a_k\mapsto a_k-1$, the carrier is literally the compositions of $N-1$. It already has depth layers, pointwise fibres, and image enumeration for synchronous balanced refinement, with logarithmic absorption, an all-iterate kernel, and one attractor. Here a one-place Euclidean-path queue has linear marker depth, fibres at most two, and many cycles. Thus levelwise nonconjugacy holds for $N\ge4$ (the $N=2,3$ graphs are isomorphic), proving graded-family separation but no priority. Generic composition dynamics receive no credit. The residual is the exact temporal conjunction for [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, including the raw $L/R$-path engine below.

A state is *recurrent* if it lies on a directed cycle of this finite map. Its depth is $$\operatorname{depth}(w)=\min\{t\ge0:\Phi^t(w)\text{ is recurrent}\}.$$

# The marker clock and terminal core

For a digit word $w=(a_1,\ldots,a_k)$, set $$\delta(w)=\max\{i:a_i=1\},$$ with $\delta(w)=0$ when no digit equals one. View the indices cyclically. For every maximal run of ones, add its length to the non-one digit immediately preceding it and delete the run. If $j$ is the last original position equal to one, mark the gap between $a_j$ and the first original non-one following it cyclically. (Such a non-one exists because $a_k\ge2$.) Transport this gap through the contractions and cut so that this surviving non-one is first; call the ordered word $\kappa(w)$. If there was no one, put $\kappa(w)=w$.

[\[thm:core\]]{#thm:core label="thm:core"} For every $w\in\mathcal R_N$, $$\operatorname{depth}(w)=\delta(w),\qquad
 \Phi^{\delta(w)}(w)=\kappa(w).                         \label{eq:core}$$ The recurrent set is exactly the words whose digits are all at least two. On it $\Phi$ is left rotation. Hence the eventual period of $w$ is the primitive rotation period of $\kappa(w)$. The maximum depth on $\mathcal R_N$ is $N-2$, attained by $(1^{N-2},2)$.

If the leading digit exceeds one, [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} moves it behind every one; if it equals one, the update deletes it and increments the current last digit, which is at least two. No step creates a one. Therefore the largest index occupied by a one decreases by exactly one at each step until it vanishes, proving the first formula.

Track a maximal cyclic run of $s$ ones. When its leading member reaches the front, deletion contributes one to the digit preceding that run in cyclic order; repeating this $s$ times adds $s$ there. Runs do not interfere because no new one is created. After the last original one is deleted, the next original non-one digit is at the front, which is exactly the prescribed cut. This proves [\[eq:core\]](#eq:core){reference-type="eqref" reference="eq:core"}. A word with no one is merely rotated, so it is recurrent and has the stated primitive period; every other word has positive depth. Finally, a word of weight $N$ ending at least two has at most $N-2$ digits before its end, and the displayed witness realizes that bound.

For example, $$(2,1,3)\longmapsto(1,3,2)\longmapsto(3,3).$$ The marked gap follows the original one, so the surviving original $3$ is first in the core; the preceding $2$ has absorbed that one and becomes the second $3$.

## Independent raw Euclidean-path route

Let $\mathcal E_N$ be the strings in $\{L,R\}^N$ that begin with $L$ and whose terminal constant block has length at least two. The map $E$ in [\[eq:path\]](#eq:path){reference-type="eqref" reference="eq:path"} is a bijection $\mathcal R_N\to\mathcal E_N$: its inverse takes the successive run lengths as canonical quotients.

We now define a self-map $\Psi$ on the *strings*, before taking any run lengths. Exchange $L$ and $R$ symbolwise with an overline. A string with more than one block has a unique factorisation $W=L^aY$, where $Y$ begins with $R$. Put $\epsilon=\operatorname{last}(\overline Y)$ and let $\overline\epsilon$ be the opposite letter. Define $$\Psi(W)=
 \begin{cases}
 W,&Y=\varnothing,\\
 \overline Y\,\epsilon,&a=1,\\
 \overline Y\,\overline\epsilon^{\,a},&a>1.
 \end{cases}                                           \label{eq:path-map}$$ The second branch extends the final block by one symbol; the third appends a new block of length $a$. Thus every output again begins with $L$ and has a terminal block of length at least two.

[\[prop:path\]]{#prop:path label="prop:path"} For every $q\in\mathcal R_N$, $$E(\Phi(q))=\Psi(E(q)).         \label{eq:conjugacy}$$ In path language alone, the last singleton-block index is the depth, cyclic runs of singleton blocks contract into their preceding nonsingleton block, and every target path has exactly the two inverse alternatives described below when their stated conditions hold.

Suppose the successive blocks of $W$ have lengths $(a_1,\ldots,a_k)$. If $k=1$, both maps fix the state. Otherwise $a=a_1$, and symbolwise complementation makes $Y$ a normalized string with block lengths $(a_2,\ldots,a_k)$. When $a>1$, the last branch of [\[eq:path-map\]](#eq:path-map){reference-type="eqref" reference="eq:path-map"} appends a distinct block of length $a$, giving $(a_2,\ldots,a_k,a_1)$. When $a=1$, it repeats the current final symbol, giving $(a_2,\ldots,a_{k-1},a_k+1)$. These are exactly the three branches of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}, proving [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"} for every size without compressing the output string first.

Now mark the maximal constant blocks of length one directly in $W$. A nonsingleton first block is transported to the end, whereas a singleton first block is deleted and contributes one symbol to the last block. Hence the last marked-block index decreases by exactly one, and no new singleton is created. Successive deletions absorb every cyclic run of marked singletons into its preceding nonsingleton block; after the last deletion, the marked gap specifies the first surviving block. This proves the path versions of the clock and core independently of the digit recurrence.

Finally let $V$ be a target path and let $Z$ be its terminal block. If $V$ has one block, its rotation predecessor is $V$ itself. Otherwise write $V=UZ$. A rotation predecessor exists exactly when the terminal block of $U$ has length at least two, and it is $$L^{|Z|}\overline U.            \label{eq:path-rho}$$ The other possibility exists exactly when $|Z|\ge3$: delete the final symbol of $V$ to obtain $V^-$ and take $$L\,\overline{V^-}.             \label{eq:path-eta}$$ Direct substitution in [\[eq:path-map\]](#eq:path-map){reference-type="eqref" reference="eq:path-map"} returns $V$ in both cases. Conversely, its $a>1$ and $a=1$ branches force [\[eq:path-rho\]](#eq:path-rho){reference-type="eqref" reference="eq:path-rho"} and [\[eq:path-eta\]](#eq:path-eta){reference-type="eqref" reference="eq:path-eta"}, respectively, so there is no third source. The alternatives have different block counts and cannot collide. This is a path-string proof of the complete predecessor split.

# Every exact-depth layer

Let $D_t(x)$ be the formal ordinary generating function in digit sum for states of exact depth $t$. A recurrent word is a nonempty sequence of parts at least two. If $t\ge1$, its first $t-1$ parts are arbitrary positive parts, part $t$ equals one, and its nonempty suffix has all parts at least two. Consequently $$D_0(x)=\frac{x^2}{1-x-x^2},\qquad
 D_t(x)=\frac{x^{t+2}}{(1-x)^{t-1}(1-x-x^2)}\quad(t\ge1). \label{eq:layers}$$ With $F_0=0,F_1=1$, this says $$[x^N]D_0=F_{N-1},\qquad [x^N]D_1=F_{N-2},$$ and, for $t\ge2$ and $M=N-t-2\ge0$, $$D_t=\sum_{j=0}^{M}
 \binom{j+t-2}{t-2}F_{M-j+1};                          \label{eq:coeff}$$ the coefficient is zero when $N<t+2$. As a boundary check, $$\sum_{t\ge0}D_t(x)=\frac{x^2}{1-2x},                 \label{eq:layer-sum}$$ whose weight-$N$ coefficient is [\[eq:size\]](#eq:size){reference-type="eqref" reference="eq:size"}.

The atomic series for a positive part is $x/(1-x)$ and for a part at least two is $x^2/(1-x)$. The two sequence decompositions above give [\[eq:layers\]](#eq:layers){reference-type="eqref" reference="eq:layers"}. Expanding $(1-x)^{-(t-1)}$ and $(1-x-x^2)^{-1}=\sum_{m\ge0}F_{m+1}x^m$ gives [\[eq:coeff\]](#eq:coeff){reference-type="eqref" reference="eq:coeff"}. Summing the geometric series over $t$ yields [\[eq:layer-sum\]](#eq:layer-sum){reference-type="eqref" reference="eq:layer-sum"}.

# Every one-step fibre

For a target $y=(b_1,\ldots,b_\ell)$, define the possible rotation inverse $$\rho(y)=
 \begin{cases}
 y,&\ell=1,\\
 (b_\ell,b_1,\ldots,b_{\ell-1}),&\ell>1, b_{\ell-1}\ge2,
 \end{cases}$$ when the displayed branch applies, and the possible deletion inverse $$\eta(y)=
 \begin{cases}
  (1,b_1-1),&\ell=1,\ b_1\ge3,\\
  (1,b_1,\ldots,b_{\ell-1},b_\ell-1),
      &\ell>1,\ b_\ell\ge3.
 \end{cases}$$

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} The fibre of $y$ consists exactly of the applicable, distinct words $\rho(y)$ and $\eta(y)$. Hence every fibre has size $0,1$, or $2$. Moreover $$|\operatorname{im}\Phi|=
 \begin{cases}
 1,&N=2,3,\\
 3\cdot2^{N-4},&N\ge4,
 \end{cases}                                           \label{eq:image}$$ and the number of Garden states is $0$ for $N=2$, $1$ for $N=3$, and $2^{N-4}$ for $N\ge4$.

The first two branches of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} invert only by moving the last digit to the front; for length greater than one the resulting last digit is $b_{\ell-1}$, so canonicality is exactly the displayed condition. The last branch can invert only by inserting a leading one and removing one from the last digit, which is legal exactly when $b_\ell\ge3$. These sources have different lengths and direct substitution verifies them, so there are no others and no collision.

A target has no inverse precisely when it has length at least two and ends in $(1,2)$. For $N=3$ this is the sole word $(1,2)$. For $N\ge4$, deleting that suffix leaves an arbitrary positive composition of $N-3$, giving $2^{N-4}$ Garden states. Subtracting from [\[eq:size\]](#eq:size){reference-type="eqref" reference="eq:size"} proves [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}; $N=2$ is immediate.

# Recurrent necklaces

For recurrent words of weight $N$ and length $k$, Burnside's lemma gives the number of rotation orbits $$\mathcal C_{N,k}=\frac1k\sum_{d\mid\gcd(N,k)}\varphi(d)
 \binom{N/d-k/d-1}{k/d-1},
 \quad1\le k\le\lfloor N/2\rfloor.                    \label{eq:burnside}$$ Indeed a word fixed by a rotation with repetition factor $d$ reduces to a length-$k/d$ composition of $N/d$ with parts at least two. The binomial is well-defined because $N\ge2k$. Formula [\[eq:burnside\]](#eq:burnside){reference-type="eqref" reference="eq:burnside"} counts cycles by word length, not by primitive dynamical period; no zeta formula is inferred. Fixed points are the constant digit words, so $$|\operatorname{Fix}\Phi|=d(N)-1,             \label{eq:fixed}$$ where $d(N)$ is the number of positive divisors. Both formulas are classical necklace consequences and receive zero contribution credit; their role is only to complete the recurrent picture produced by [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"}.

# Exact control and limitations

The deterministic verifier constructs the rational numerator/denominator by continuants, independently reconstructs its subtractive $L/R$ path, and exhausts every state for $2\le N\le18$. It checks the path blocks, terminal core, exact depth, primitive period, every target fibre, all layer counts, image and Garden counts, Burnside orbits, and fixed points. These finite checks are falsification evidence, not proofs.

The map is specific to canonical finite expansions in $(0,1)$ and to the stated terminal convention. It is not a map on all positive rationals, not a Gauss/Farey shift, and not an assertion about general continued fractions or continuants. The owner screen was bounded and cannot certify absence. Novelty, priority, authorship, posting, submission, and every external-release decision remain on hold.
