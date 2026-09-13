---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--202-ternary-ordered-reset"
canonical_tex: "symbolic_dynamics/papers/202-ternary-ordered-reset/main.tex"
canonical_pdf: "symbolic_dynamics/papers/202-ternary-ordered-reset/main.pdf"
source_sha256: "bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two Recurrent Languages and Sharp Tails for a Ternary Reset Rule

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/202-ternary-ordered-reset>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/202-ternary-ordered-reset/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/202-ternary-ordered-reset/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/202-ternary-ordered-reset/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/202-ternary-ordered-reset/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On cyclic ternary words, increment a letter modulo three when it is at most its right neighbor, and otherwise reset it to zero. We determine the full recurrent set of this synchronous map. One recurrent language evolves by global colour advance, while another evolves by spatial rotation. Their union is exhaustive, and the maximum tail is $3\lfloor n/3\rfloor+1$ for every length $n\ge3$, with explicit separate values at lengths one and two. After two steps, run surpluses follow a standard finite parking process; its first clearance time is exactly the remaining entrance time in the original word system. Independently, the image consists of the words avoiding cyclic $21$. Each target has one binary source choice at every occurrence of $01$, giving all fibres and every maximizing target. Finite adjacency matrices yield the image and periodic-point counts. The parking mechanism, oscillator background and trace methods are prior tools, not claims of a new general mechanism. Exact full graphs and source sets through length twelve support the all-length proofs.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Two Recurrent Languages and Sharp Tails\
  for a Ternary Reset Rule
```

## Markdown 正文

# The map and its source boundary

For $n\ge1$, let $X_n=\{0,1,2\}^{\mathbb Z/n\mathbb Z}$, with the order $0<1<2$. All coordinates are updated simultaneously by $$\label{eq:rule}
 F(x)_i=\begin{cases}(x_i+1)\bmod3,&x_i\le x_{i+1},\\
 0,&x_i>x_{i+1}.
 \end{cases}$$ Thus $0$ always becomes $1$, $2$ always becomes $0$, and $1$ becomes $0$ precisely before $0$, otherwise $2$. Write $C$ for global addition by one modulo three and $R$ for left rotation, $(Rx)_i=x_{i+1}$. A recurrent point means a periodic point. Its entrance time is $h(x)=\min\{t\ge0:F^t(x)\in\operatorname{Rec}(F)\}$, and $H(n)=\max_{x\in X_n}h(x)$.

Finite-state pulse-coupled oscillators and moving colour frames are established models [@Lyu2015]; annihilating particle descriptions also occur in cyclic, Greenberg--Hastings and firefly automata [@LyuSivakoff2019]. Here $F(x)_i=x_i+1+\mathbf 1_{\{x_ix_{i+1}=10\}}\pmod3$. The extra advance differs from the inhibited update of the firefly rule. Subtracting time from the colours rotates the exceptional pair with time; it does not by itself give an autonomous cyclic-automaton conjugacy.

The run factor below is a specialization of particle parking, where a particle stays at an available unit slot and later particles pass it [@DamronEtAl2019; @CabezasRollaSidoravicius2014]. We claim no new parking mechanism, moving-frame method, or transfer-matrix technique [@LindMarcus1995]. The result concerns the joint temporal and inverse description of the particular map [\[eq:rule\]](#eq:rule){reference-type="eqref" reference="eq:rule"}. No external priority claim is made; the source boundary remains `HOLD_EXTERNAL`.

# Every target and all largest fibres

Let $e_{01}(y)$ count cyclic adjacent occurrences of $01$ in $y$.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} A target $y\in X_n$ lies in $\operatorname{im}F$ exactly when it avoids cyclic $21$. For such a target, start with $x_i=y_i-1\pmod3$. Independently at each edge $y_i y_{i+1}=01$, either keep $x_i=2$ or replace it by $1$. These are exactly all sources, without repetition. In particular, $$\label{eq:fibre}
 |F^{-1}(y)|=\begin{cases}2^{e_{01}(y)},&y\text{ avoids }21,\\
 0,&\text{otherwise}.
 \end{cases}$$ The maximum is $2^{\lfloor n/2\rfloor}$. At even $n\ge2$, its targets are exactly the two alternating words. At odd $n=2m+1\ge3$, they are exactly the $n$ rotations of each word $$\label{eq:oddmax}
 001(01)^{m-1},\qquad011(01)^{m-1},\qquad012(01)^{m-1}.$$ At $n=1$ all three targets have fibre one.

An output $2$ requires source $1$ with a nonzero right neighbor; an output $1$ at that neighbor would instead require source $0$ there. Hence $21$ is impossible. If $y$ avoids $21$, the proposed initial source works: a target $2$ is followed by $0$ or $2$, so its source $1$ sees $2$ or $1$; target $1$ forces source $0$; target $0$ permits source $2$. The only alternative producing target $0$ is source $1$ followed by $0$. The latter neighbor forces target $1$, giving exactly the stated choices. Distinct $01$ edges share no vertex, so the choices do not interfere. Each chosen source is recoverable from the target and its selected edges.

The $e_{01}$ disjoint edges use $2e_{01}$ vertices. Equality in $e_{01}\le\lfloor n/2\rfloor$ at even length forces alternation. At odd length the disjoint pairs leave one vertex. Cutting at that vertex gives [\[eq:oddmax\]](#eq:oddmax){reference-type="eqref" reference="eq:oddmax"}, according to its letter $0$, $1$ or $2$. All these words avoid $21$. Their unique doubled-zero, doubled-one or sole-two feature makes their rotation orbits primitive and mutually disjoint, giving exactly $3n$ targets. At length one the map is the three-cycle $0\mapsto1\mapsto2\mapsto0$.

# Run coordinates and finite parking

A nonconstant image word contains a zero: otherwise a nonconstant cyclic word in $\{1,2\}$ would contain $21$. Cutting at the starts of its zero runs gives, in cyclic order, $$\label{eq:runs}
 0^{c_i}1^{a_i}2^{b_i},\qquad
 c_i\ge1,\quad a_i,b_i\ge0,\quad a_i+b_i\ge1,
 \qquad i\in\mathbb Z/k\mathbb Z.$$ This decomposition is unique up to the first block. Constants have unique constant predecessors by Theorem [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"}, so nonconstant orbits never become constant.

[\[lem:runs\]]{#lem:runs label="lem:runs"} With the cyclic block order tracked, one update gives $$\label{eq:runupdate}
 c_i'=\max\{b_{i-1},1\},\qquad a_i'=c_i,\qquad
 b_i'=a_i-\mathbf 1_{\{b_i=0\}}.$$ The number $k$ of blocks is preserved. After two original updates, $c_i,a_i\ge1$ and $b_i\ge0$.

The old zero run becomes a positive one run of length $c_i$. If $b_i>0$, all $a_i$ ones become twos and all $b_i$ twos become zeros. If $b_i=0$, the final old one resets to zero and the other $a_i-1$ ones become twos. The new zero run before the new one run comes from the previous block. Every new one run is positive, so no further block merger occurs. These facts give [\[eq:runupdate\]](#eq:runupdate){reference-type="eqref" reference="eq:runupdate"}, including $a_i=0$ when $b_i>0$.

In the twice-image domain put $z_{c_i}=c_i-1$, $z_{a_i}=a_i-1$ and $z_{b_i}=b_i$. Write $u_+=\max\{u,0\}$. Their total is $M=n-2k$, and [\[eq:runupdate\]](#eq:runupdate){reference-type="eqref" reference="eq:runupdate"} becomes $$\label{eq:parking}
 z_{c_i}'=(z_{b_{i-1}}-1)_+,\qquad
 z_{a_i}'=z_{c_i},\qquad
 z_{b_i}'=z_{a_i}+\min\{z_{b_i},1\}.$$ This is a ring of $3k$ bins in the order $c_i,a_i,b_i,c_{i+1}$. Each $b$ bin retains one particle permanently once occupied; all other particles move one bin per step. Simultaneous arrivals to an empty slot can be distinguished arbitrarily: which particle parks does not change the bin counts. Run coordinates retain cyclic block order but not an absolute spatial origin; no full labelled-word conjugacy is asserted.

[\[lem:clearance\]]{#lem:clearance label="lem:clearance"} For $k\ge1$ slots every third bin and $M\ge0$ particles, the first time when all particles are parked or all slots are occupied is at most $$\label{eq:clearbound}
 \tau(k,M)=\begin{cases}0,&M=0,\\3\min\{k,M\}-1,&M>0.
 \end{cases}$$ The bound is attained for every $k,M$.

Give the particles distinct labels. For $1\le M\le k$, a mobile particle cannot complete a circuit before parking: passing all slots occupied by other particles would require at least $k+1$ particles. Thus its passed slots are distinct, and each holds another particle. From a transit bin the first slot is at distance at most two, giving parking time at most $2+3(M-1)$. If it starts in an occupied slot, that slot already uses another particle, and the bound is $3+3(M-2)$ whenever this case occurs.

For $M\ge k$, suppose a slot is still empty after $3k-1$ steps. Fewer than $k$ particles are parked, so one is still mobile. It has moved at every step, since parked particles never restart. Its destinations visit every bin except possibly its starting bin. It therefore encountered the proposed empty slot, unless it started there; in the latter case it would have parked initially. Both alternatives are impossible.

Placing all particles in one $c$ bin fills successive slots at times $2,5,8,\ldots$. The last necessary slot is filled at $3\min\{k,M\}-1$. Zero mass has clearance zero.

# Recurrent languages and sharp tails

Define two rotation-invariant languages by $$\begin{aligned}
 \mathcal A_n&=\{x:x_{i+1}-x_i\pmod3\in\{0,1\}\text{ for every }i\},
 \label{eq:A}\\
 \mathcal B_n&=\{x:x_i x_{i+1}\in\{01,10,12,20\}\text{ for every }i\}.
 \label{eq:B}\end{aligned}$$ The second language consists of circular concatenations of $01$ and $012$.

[\[thm:time\]]{#thm:time label="thm:time"} For every $n\ge1$, $\operatorname{Rec}(F)=\mathcal A_n\cup\mathcal B_n$. On $\mathcal A_n$ one has $F=C$, and every point has exact period three. On $\mathcal B_n$ one has $F=R$, and the exact period is the least spatial rotation period. The intersection has the three rotations of $(012)^{n/3}$ if $3\mid n$, and is empty otherwise. In the twice-image run domain, $h(x)$ is exactly the first clearance time of [\[eq:parking\]](#eq:parking){reference-type="eqref" reference="eq:parking"}. Moreover, $$\label{eq:H}
 H(1)=0,\qquad H(2)=2,\qquad
 H(n)=3\lfloor n/3\rfloor+1\quad(n\ge3).$$

On the six allowed edges of $\mathcal A_n$, the output is the current letter plus one. Global colour advance preserves its edge differences, so this action persists and has exact period three. On each of the four edges of $\mathcal B_n$, the output is the right letter. Rotation preserves this language. Intersecting the edge lists leaves $01,12,20$, which proves the overlap.

For a nonconstant twice-image, all slots occupied means $b_i\ge1$ in every block, exactly the condition for $\mathcal A_n$ in its run domain. All particles parked means $c_i=a_i=1$ and $b_i\in\{0,1\}$, exactly $\mathcal B_n$. Lemma [\[lem:clearance\]](#lem:clearance){reference-type="ref" reference="lem:clearance"} therefore sends every such state into the union. Constants already belong to $\mathcal A_n$. Both languages have explicit periodic actions, so they exhaust the recurrent set. Before clearance there are both a mobile particle and an empty slot, excluding both conditions. This also proves the exact pointwise entrance criterion. The actions were checked on original coordinates; quotient phases have not been used to infer the periods.

For the upper bound, a nonconstant twice-image has $k\ge1$ and $M=n-2k\ge0$. If $M>0$, the original entrance time is at most $2+3\min\{k,n-2k\}-1\le3\lfloor n/3\rfloor+1$. If $M=0$, or the twice-image is constant, the time is at most two. At length one every state is recurrent. At length two the upper bound is two and $12\mapsto20\mapsto01$ attains it.

For sharpness at $n=3k+r\ge3$, where $0\le r\le2$, use $$\begin{aligned}
 x&=1^{k+r+1}2(12)^{k-1},\\
 F(x)&=2^{k+r+1}0(20)^{k-1},\\
 F^2(x)&=0^{k+r+1}1(01)^{k-1}.\end{aligned}$$ The last word has $k$ blocks, all $M=k+r$ particles in one $c$ bin, and every slot empty. Its remaining entrance time is exactly $3k-1$ by the equality example in Lemma [\[lem:clearance\]](#lem:clearance){reference-type="ref" reference="lem:clearance"}. No earlier point on the orbit can be recurrent, since the recurrent set is forward invariant. Thus $h(x)=3k+1$, completing [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"}.

# Census and exact controls

Let $P_3$ be the three-colour permutation matrix, with entries one at $01,12,20$. Set $a_n=\operatorname{tr}(I+P_3)^n$ and $b_n=\operatorname{tr}Q^n$, where $$\label{eq:matrices}
 Q=\begin{pmatrix}0&1&0\\1&0&1\\1&0&0\end{pmatrix},
 \qquad V(u)=\begin{pmatrix}1&u&1\\1&1&1\\1&0&1\end{pmatrix}.$$

[\[cor:counts\]]{#cor:counts label="cor:counts"} For $n\ge1$, with Lucas numbers $L_0=2,L_1=1$ and $L_j=L_{j-1}+L_{j-2}$, $$\begin{aligned}
 |\operatorname{im}F|&=L_{2n},&
 \sum_{y\in\operatorname{im}F}u^{e_{01}(y)}&=\operatorname{tr}V(u)^n,\label{eq:imagecount}\\
 |\operatorname{Rec}(F)|&=a_n+b_n-3\mathbf 1_{\{3\mid n\}}.\label{eq:reccount}\end{aligned}$$ Here $a_n=2^n+\epsilon_n$, where $\epsilon_n$ is periodic modulo six with values $(2,1,-1,-2,-1,1)$ at residues $0,\ldots,5$; also $b_0=3,b_1=0,b_2=2$ and $b_n=b_{n-2}+b_{n-3}$ for $n\ge3$. For $t\ge1$ and $d=\gcd(n,t)$, $$\label{eq:fixt}
 |\operatorname{Fix}(F^t)|=\mathbf 1_{\{3\mid t\}}a_n+b_d-3\mathbf 1_{\{3\mid d\}}.$$

A cyclic word is a closed adjacency walk with labelled initial position, so the finite trace counts words, not rotation classes. The matrix $V(1)$ encodes precisely avoidance of $21$. Its characteristic polynomial is $\lambda(\lambda^2-3\lambda+1)$: the trace is three, the principal two-minors sum to one, and two rows agree. Its nonzero eigenvalues are the squares of the roots of $z^2-z-1$, proving the Lucas formula. The weight on edge $01$ gives the second part of [\[eq:imagecount\]](#eq:imagecount){reference-type="eqref" reference="eq:imagecount"}.

The matrices $I+P_3$ and $Q$ encode $\mathcal A_n$ and $\mathcal B_n$. The eigenvalues of $I+P_3$ are $2,1+\omega,1+\omega^2$ for $\omega^3=1$, $\omega\ne1$; their powers give $\epsilon_n$. The characteristic polynomial of $Q$ is $\lambda^3-\lambda-1$, giving the recurrence and the three direct initial traces. The value $b_0$ is a matrix convention, not an empty-word carrier. Theorem [\[thm:time\]](#thm:time){reference-type="ref" reference="thm:time"} and its overlap prove [\[eq:reccount\]](#eq:reccount){reference-type="eqref" reference="eq:reccount"}. For [\[eq:fixt\]](#eq:fixt){reference-type="eqref" reference="eq:fixt"}, the colour branch contributes exactly when $3\mid t$; rotation-fixed words in the other branch repeat a closed word of length $d$, contributing $b_d$. The overlap is counted twice precisely when $3\mid d$ and then has three words.

The standalone exact verifier builds complete functional graphs and every target's full source set for $1\le n\le12$, totaling $797{,}160$ states. Bitplane updates, orbit-path cycle discovery and source-edge walks check the literal map independently of the closed formulae. Labelled-particle controls cover $7{,}280$ complete finite parking configurations and the sharp witnesses for every $3\le n\le150$. Two fresh author runs have identical transcripts. These finite tests are falsifiers, not proofs of the all-length statements. The code is adapted from an earlier checker by the same writer and is not counted as a new independent paper review.

The results cover only the printed ternary synchronous ring map. They do not classify all maximum-tail sources, extend to larger alphabets, or exclude every possible block-code or time-rescaled identification with previous systems. Generic parking, trace enumeration and local decoding methods receive no novelty credit. External status remains `OWNER_AMBER / HOLD_EXTERNAL`.
