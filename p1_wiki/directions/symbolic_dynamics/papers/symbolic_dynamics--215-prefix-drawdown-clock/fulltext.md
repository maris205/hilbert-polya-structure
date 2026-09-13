---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--215-prefix-drawdown-clock"
canonical_tex: "symbolic_dynamics/papers/215-prefix-drawdown-clock/main.tex"
canonical_pdf: "symbolic_dynamics/papers/215-prefix-drawdown-clock/main.pdf"
source_sha256: "ab581ad942de1785cbfdb49c5f930597f1439c41dec4daca4e499c4a52f04e1b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Clocks and Inverse Fibres for Iterated Prefix Drawdown

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/215-prefix-drawdown-clock>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a bounded nonnegative integer word, replace each coordinate by its running prefix maximum minus its current value, and iterate the entire word. We prove that the exact time to reach zero is the number of sign runs in its successive differences after an initial zero is adjoined and zero differences are discarded. The key identity removes the first positive sign run and reverses each remaining sign, including when the drawdown saturates at zero. Hence zero is uniquely recurrent, and the sharp height on length-$n$ words over $\{0,\ldots,q\}$ is $n$ for $n,q>0$. Independently, every predecessor of a target is reconstructed from nondecreasing record heights at its zero positions. This gives an explicit binomial recurrence for every fibre and a unique largest fibre of size $\binom{q+n}{n}$. The drawdown statistic and the resulting classical barrier-counting problem are background, not new general methods; the scope is this autonomous clock and its inverse reconstruction.
author:
- Anonymous
bibliography:
- references.bib
title: Exact Clocks and Inverse Fibres for Iterated Prefix Drawdown
```

## Markdown 正文

# The map and the contribution boundary

Let $n,q$ be nonnegative integers and let $\mathcal X_{n,q}=\{0,\ldots,q\}^n$. Coordinates are labelled and ordered. For $n>0$, define $$\label{eq:map}
 F(x)_i=M_i(x)-x_i,\qquad
 M_i(x)=\max_{1\le j\le i}x_j\quad(1\le i\le n).$$ The empty word is fixed. Since $0\le F(x)_i\le q$, this is a finite autonomous self-map. No sorting, wraparound, external input or additional normalization is performed between updates.

The one-step statistic is classical drawdown: Goldberg and Mahmoud [@goldberg2017drawdown] define the drawdown path as the running maximum minus the current path value. Restricting that operation to finite integer words does not make the statistic new. Our question is what happens when its whole output is repeatedly fed back into the same operation. Stochastic first-passage or risk statements about one drawdown path do not, by themselves, give this autonomous iteration clock.

For $x\in\mathcal X_{n,q}$ adjoin $x_0=0$ and form $d_i=x_i-x_{i-1}$. Delete zero differences and compress every consecutive run of equal signs to one sign. Write $R(x)$ for the resulting number of signs. Thus $R(x)=0$ exactly when $x=\boldsymbol 0$, and every nonempty sign word starts with $+$. A state is recurrent if it lies on a directed cycle; its depth $h(x)$ is the first time it reaches a recurrent state.

The main result identifies $h(x)=R(x)$, not merely the triangular bound $h(x)\le n$. For example, every nonzero nondecreasing word reaches zero in one step, while an alternating word $(q,0,q,0,\ldots)$ takes $n$ steps when $q>0$. The inverse problem uses different data: a target's zero positions identify its possible record heights. Those heights form nondecreasing integer sequences with barriers, a classical enumeration problem studied by Pemantle and Wilf [@pemantle2009barrier]. We give a direct evaluated recurrence for completeness, without claiming a new barrier-enumeration method. The contribution is limited to the exact clock and the full record-height reconstruction for [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}.

# An exact sign-run clock {#sec:clock}

[\[lem:run\]]{#lem:run label="lem:run"} For $x\ne\boldsymbol 0$, one has $R(Fx)=R(x)-1$.

Put $y=Fx$, extend $M_0(x)=0$, and set $y_0=0$. The maximum recurrence $M_i(x)=\max(M_{i-1}(x),x_i)$ gives $$\label{eq:reflection}
 y_i=\max\{y_{i-1}-d_i,0\},\qquad d_i=x_i-x_{i-1}.$$ When $d_i=0$, the output does not change, so deleting those input differences does not affect the output sign analysis. A negative input difference makes $y$ strictly increase. A positive input difference makes $y$ decrease strictly if its previous value is positive, or stay zero if that value is zero.

In the first positive input run, the output starts at zero and stays zero. Each negative input run then gives a nonempty positive output run. Every later positive input run follows a negative run, so it starts with positive output and gives at least one strict decrease. It continues decreasing until zero, if zero is reached, and then remains zero for the rest of that run. Its nonzero output differences therefore form exactly one negative run.

These output runs cannot merge: between two positive output runs there is the nonempty negative run supplied by the intervening positive input run, and between two negative output runs there is a nonempty positive one. Input plateaus add only output plateaus. Thus the compressed sign word loses its first $+$, and each remaining sign is reversed. Its length decreases by exactly one.

[\[thm:clock\]]{#thm:clock label="thm:clock"} Zero is the unique recurrent state of $F$, and $$\label{eq:clock}
 h(x)=R(x)\qquad(x\in\mathcal X_{n,q}).$$ If $n,q>0$, the maximum depth is $n$. A word has depth $n$ if and only if all $n$ differences of $(0,x_1,\ldots,x_n)$ are nonzero and their signs alternate. If $n=0$ or $q=0$, the maximum depth is zero.

The equality $R(x)=0$ forces every difference from initial zero to vanish, so it detects exactly the zero word. Lemma [\[lem:run\]](#lem:run){reference-type="ref" reference="lem:run"} therefore makes each orbit reach zero after exactly $R(x)$ updates. Zero is fixed; since every orbit reaches it, there is no other recurrent state.

There are $n$ initial differences, so $R(x)\le n$. Equality holds exactly when none is zero and none is compressed with a neighbouring difference, which is the stated alternating-sign condition. The word $(q,0,q,0,\ldots)$ satisfies that condition for $q>0$. The cases $n=0$ and $q=0$ have singleton carriers.

For a concrete identity independent of any computation, $$(2,0,1)\longmapsto(0,2,1)\longmapsto(0,0,1)
       \longmapsto(0,0,0).$$ The three signs of its initial-zero differences are $+,-,+$. Saturation can flatten part of a later positive input run, but the proof shows why it cannot erase that whole run's contribution to the clock.

# Every inverse fibre {#sec:inverse}

For $n>0$, a target $y$ can have predecessors only if $y_1=0$. Assume this condition and list its zero positions as $$1=z_1<\cdots<z_k,\qquad z_{k+1}=n+1.$$ For $1\le j\le k$, define $$\label{eq:barriers}
 b_j=\max_{z_j\le i<z_{j+1}}y_i,
 \qquad B_j=\max_{1\le r\le j}b_r.$$

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} The predecessors of $y$ are in bijection with the integer sequences $$\label{eq:heights}
 0\le L_1\le\cdots\le L_k\le q,\qquad L_j\ge B_j.$$ The source corresponding to such a sequence is $$\label{eq:reconstruct}
 x_i=L_j-y_i\qquad(z_j\le i<z_{j+1}).$$ Every target with $y_1=0$ has a predecessor.

Suppose $Fx=y$. A strict increase of the running maximum requires $x_i=M_i(x)$ and therefore $y_i=0$. The running maximum is consequently constant on each displayed block; call its value $L_j$. These values are nondecreasing and at most $q$. Nonnegativity of each source coordinate forces $L_j\ge b_j$, and [\[eq:reconstruct\]](#eq:reconstruct){reference-type="eqref" reference="eq:reconstruct"} is necessary. For a nondecreasing sequence, the conditions $L_j\ge b_j$ are equivalent to $L_j\ge B_j$.

Conversely, construct $x$ by [\[eq:reconstruct\]](#eq:reconstruct){reference-type="eqref" reference="eq:reconstruct"} from admissible heights. All entries lie between zero and $q$. At $z_j$ the source value is $L_j$, while all earlier entries are at most $L_j$. The other entries of the block are less than $L_j$ because their target entries are positive. Hence the actual running maximum throughout that block is $L_j$, proving $Fx=y$. The source's running maxima recover the heights, which proves uniqueness. Finally, $L_j=q$ for all $j$ is admissible.

To evaluate the fibre, put $$\label{eq:upper}
 c_i=q-B_{k+1-i}\quad(1\le i\le k).$$ These are nonnegative and nondecreasing. Reversing and complementing the heights, $a_i=q-L_{k+1-i}$, gives precisely the sequences $0\le a_1\le\cdots\le a_k$ with $a_i\le c_i$. This is the classical upper-barrier problem. The following evaluation is included with its first-violation proof so that no enumeration oracle is needed. We use $\binom{u}{v}=0$ for integers $v>u\ge0$.

[\[thm:count\]]{#thm:count label="thm:count"} Set $A_0=1$ and, for $1\le m\le k$, compute $$\label{eq:count}
 A_m=\binom{c_m+m}{m}
       -\sum_{i=1}^{m-1}A_{i-1}
                   \binom{c_m-c_i+m-i}{m-i+1}.$$ Then $|F^{-1}(y)|=A_k$.

There are $\binom{c_m+m}{m}$ nondecreasing length-$m$ sequences between zero and $c_m$. An invalid one has a unique first index $i$ at which $a_i>c_i$, and $i<m$. Its prefix of length $i-1$ is one of the $A_{i-1}$ valid prefixes. Its remaining $m-i+1$ entries form an arbitrary nondecreasing sequence in $\{c_i+1,\ldots,c_m\}$, counted by the binomial coefficient in the summand.

For $i>1$, the prefix is bounded above by $c_{i-1}\le c_i$; for $i=1$ it is empty. Thus every such prefix and suffix concatenate nondecreasingly and have first violation exactly $i$. Subtracting these disjoint invalid classes proves [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"} by induction on $m$. Theorem [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"} then identifies $A_k$ with the desired fibre.

[\[cor:extreme\]]{#cor:extreme label="cor:extreme"} For $n>0$, the image is $\{y\in\mathcal X_{n,q}:y_1=0\}$ and has size $(q+1)^{n-1}$. If $n,q>0$, the unique largest fibre is at $\boldsymbol 0$, with size $\binom{q+n}{n}$. If $n=0$ or $q=0$, the unique fibre has size one.

The image statement follows from Theorem [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"}. At zero there are $n$ zero positions and all barriers vanish. Its predecessors are all nondecreasing height sequences in $\{0,\ldots,q\}$, giving $\binom{q+n}{n}$ choices. A nonzero image target has $k<n$ zero positions, so it has at most $\binom{q+k}{k}$ predecessors. For $q>0$ this is strictly smaller than $\binom{q+n}{n}$, since increasing $k$ by one multiplies that quantity by $(q+k+1)/(k+1)>1$. Targets outside the image have no predecessors. The remaining cases have singleton carriers.

# Scope and finite-verification protocol

The temporal proof concerns repeated full-vector feedback on a finite ordered word. It does not assert a new drawdown statistic, a stochastic stopping-time theorem, or an extension to arbitrary posets. The inverse reconstruction identifies the exact barriers for each target; the subsequent static enumeration and multiset counting are established primitives. No all-time inverse formula or global priority claim is made. The bounded source and collision checks supporting this scope cannot exclude every possible prior encoding or factor.

All statements above have deductive proofs. The accompanying author verifier source specifies the fixed boxes $0\le n\le5$, $0\le q\le3$. These are 24 parameter cases and a total of 1798 states by summing $\sum_{n=0}^{5}\sum_{q=0}^{3}(q+1)^n$. The accepted finite DATA contains all 24 cases and all 1798 states. Empty-word and zero-alphabet cases remain separate boxes. The comparison walks literal orbits until a state repeats, without using the sign-run clock as a stopping condition. Complete transition-derived predecessor buckets are compared with the record-height reconstruction and the recurrence. Every state and target, including empty fibres and singleton boundaries, is retained in the deterministic output.

The complete initial DATA, actual canonical copy and two strict author replays have been accepted. They agree byte for byte and cover 24 boxes, 1798 states, 1798 targets and 20044 producer comparisons with zero finite failures. These finite checks test implementation and pressure the proofs; they do not establish the all-parameter conclusions.
