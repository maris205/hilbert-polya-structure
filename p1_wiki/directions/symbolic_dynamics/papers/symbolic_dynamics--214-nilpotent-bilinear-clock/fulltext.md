---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--214-nilpotent-bilinear-clock"
canonical_tex: "symbolic_dynamics/papers/214-nilpotent-bilinear-clock/main.tex"
canonical_pdf: "symbolic_dynamics/papers/214-nilpotent-bilinear-clock/main.pdf"
source_sha256: "fd308d1a7ef1b583df524b1ab3d161900af2f02895801eff112465a180a71ada"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A cancellation-safe clock for nilpotent bilinear dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the exact time to zero for the polynomial map $F(x,y)=(y,x(t+y))$ on $I^2$, where $I=t\mathbb F_q[t]/(t^m)$, $q$ is any prime power and $m\geq2$. With the truncated valuation normalized by $v(0)=m$, this time is $\max\{2(m-v(y)),2(m-v(x))-1\}$. The nonlinear term can cancel the leading term of one register, so a coordinatewise linear-clock argument does not suffice. After separating the two parity chains, the other register gives the sharp deadline even in the cancellation case. Consequently zero is the unique recurrent state, the maximum depth is $2m-2$, and exactly $q^h$ states have depth at most $h$ for $0\leq h\leq2m-2$. We also evaluate every one-step fibre by an elementary ideal calculation. This inverse mechanism is multiplication under separate input and output translations, not a new inversion method. The clock and depth distribution agree with a linear control, but for $m\geq3$ unequal nonempty fibre sizes exclude conjugacy to any finite-group endomorphism. The case $m=2$ is precisely the linear boundary.
author:
- Anonymous Authors
bibliography:
- references.bib
title: 'A cancellation-safe clock for nilpotent bilinear dynamics'
```

## Markdown 正文

# The map and the question {#sec:setup}

Nilpotence forces many finite algebraic systems to lose information, but it does not determine when both registers of a coupled recurrence vanish. For the map studied here, a leading-term cancellation can erase one register earlier than a linear model predicts. The exact full-state deadline nevertheless agrees with that model. Our purpose is to prove this agreement on the full carrier, including the cancellation locus, and to distinguish it from a linearization of the dynamics.

Throughout, $q$ is a prime power, $m\geq2$, and $$R=\mathbb F_q[t]/(t^m),\qquad I=tR,\qquad
 F:I^2\longrightarrow I^2,\quad F(x,y)=(y,x(t+y)).
 \label{eq:map}$$ The symbol $t$ denotes its residue class in $R$. For a nonzero element $z$, let $v(z)$ be the least degree of its nonzero coefficients, and put $v(0)=m$. Coefficient multiplication and counting give $$v(zw)=\min\{m,v(z)+v(w)\},\qquad
 |t^rR|=q^{m-r}\quad(0\leq r\leq m).
 \label{eq:ideals}$$ An element with nonzero constant coefficient is a unit: factoring out that coefficient reduces its inverse to a finite geometric series. In particular, $v(t+z)=1$ whenever $z\in t^2R$.

For $s\in I^2$, define its depth by $\tau(s)=\min\{n\in\mathbb Z_{\geq 0}:F^n(s)=(0,0)\}$, initially allowing infinity. A state is recurrent if some positive iterate returns to it. We prove that all depths are finite and that $$\tau(x,y)=\max\{2(m-v(y)),\,2(m-v(x))-1\}.
 \label{eq:preview}$$ The associated depth count and the full target-fibre count follow from different calculations: the first uses parity chains, the second uses the image and kernel of multiplication on $I$.

Endomorphism dynamics provide a useful comparison class: their finite state graphs have structural restrictions coming from the group operation [@Bors2017]. The present map is not assumed to be an endomorphism. Multiplicative feedback also occurs in the complex Fibonacci maps $(x,y)\mapsto(xy+c,x)$ [@ElAbdalaouiEtAl2016]. At $c=0$, interchanging coordinates gives the polynomial $(x,y)\mapsto(y,xy)$. This is background for the one-step multiplication relation, not a transfer of complex dynamics to the nilpotent ideal in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}.

The contribution is the cancellation-safe temporal theorem for this explicit nonlinear map. Neither the resulting numerical clock shape nor the general valuation-contraction method is asserted to be new. We evaluate the one-step inverse completely while explicitly deducting its multiplication mechanism in Section [4](#sec:controls){reference-type="ref" reference="sec:controls"}. Equal depth distributions will not be confused with conjugate state graphs.

# The exact clock {#sec:clock}

The recurrence representation isolates the only multiplier at which leading-term cancellation matters.

[\[lem:recurrence\]]{#lem:recurrence label="lem:recurrence"} Set $x_0=x$, $x_1=y$ and $$x_{n+2}=x_n(t+x_{n+1})\quad(n\geq0).
 \label{eq:recurrence}$$ Then $F^n(x,y)=(x_n,x_{n+1})$. Every $x_n$ belongs to $I$, and $x_n\in t^2R$ for $n\geq2$. Thus $v(t+x_n)=1$ for $n\geq2$.

The iterate identity follows by induction from [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. If two consecutive terms belong to $I$, both factors on the right of [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} belong to $I$, so their product belongs to $t^2R
\subseteq I$. Starting with $x,y\in I$ proves both inclusions. The last claim follows from the coefficient of $t$ in $t+x_n$.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every $(x,y)\in I^2$, formula [\[eq:preview\]](#eq:preview){reference-type="eqref" reference="eq:preview"} holds. Zero is the unique recurrent state. The maximum depth is $2m-2$, attained exactly at the states with $v(y)=1$.

Write $a=v(x)$ and $b=v(y)$. First suppose $b\geq2$. The initial multiplier $t+y$ and every later multiplier in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} have valuation one. Induction therefore gives, for $k\geq0$, $$v(x_{2k})=\min\{m,a+k\},\qquad
 v(x_{2k+1})=\min\{m,b+k\}.
 \label{eq:exactchains}$$ If $a<m$, the last nonzero even-indexed term has index $2(m-a-1)$; if $b<m$, the last nonzero odd-indexed term has index $2(m-b-1)+1$. The first zero state occurs one index after the last nonzero term, giving the maximum in [\[eq:preview\]](#eq:preview){reference-type="eqref" reference="eq:preview"}. If $a=m$, the even chain is absent and its displayed contribution is $-1$, which cannot dominate the nonnegative odd-chain contribution. If $b=m$, the odd chain is absent and contributes zero. In particular $a=b=m$ gives depth zero.

Now suppose $b=1$. Cancellation in $t+y$ can only accelerate the even chain. Lemma [\[lem:recurrence\]](#lem:recurrence){reference-type="ref" reference="lem:recurrence"} and [\[eq:ideals\]](#eq:ideals){reference-type="eqref" reference="eq:ideals"} imply $$v(x_{2k})\geq\min\{m,a+k\}\quad(k\geq1),\qquad
 v(x_{2k+1})=\min\{m,1+k\}\quad(k\geq0).
 \label{eq:cancellationchains}$$ For the second equality, the first update of the odd chain uses $t+x_2$; all such adjacent even terms lie in $t^2R$. Hence $x_{2m-3}\ne0$ but $x_{2m-2}=x_{2m-1}=0$, proving $\tau=2m-2$. Since $a\geq1$, this is exactly [\[eq:preview\]](#eq:preview){reference-type="eqref" reference="eq:preview"}. The argument includes $m=2$.

Every state reaches the fixed state zero, so no other state is recurrent. When $b\geq2$, both contributions to [\[eq:preview\]](#eq:preview){reference-type="eqref" reference="eq:preview"} are at most $2m-3$; when $b=1$, the depth is $2m-2$. This proves sharpness and its equality condition.

For example, $(t,-t)$ has $x_2=0$, whereas for $k\geq1$ its iterates are $$F^{2k}(t,-t)=(0,-t^{k+1}),\qquad
 F^{2k+1}(t,-t)=(-t^{k+1},0).
 \label{eq:example}$$ Powers are taken modulo $t^m$. The first zero state is still $2m-2$; an exact valuation increment for both chains would have been false.

[\[cor:depth\]]{#cor:depth label="cor:depth"} For every integer $0\leq h\leq2m-2$, exactly $q^h$ states have depth at most $h$. Depth zero has one state, and each depth $1\leq h\leq2m-2$ has $(q-1)q^{h-1}$ states.

The two inequalities in [\[eq:preview\]](#eq:preview){reference-type="eqref" reference="eq:preview"} give $$\tau(x,y)\leq h\quad\Longleftrightarrow\quad
 v(x)\geq m-\lceil h/2\rceil,\quad
 v(y)\geq m-\lfloor h/2\rfloor.$$ Both thresholds lie between $1$ and $m$. Formula [\[eq:ideals\]](#eq:ideals){reference-type="eqref" reference="eq:ideals"} therefore gives $$q^{\lceil h/2\rceil}q^{\lfloor h/2\rfloor}=q^h$$ states. Subtract the count at $h-1$ for the exact positive-depth count.

# Complete one-step fibres {#sec:fibres}

The inverse fixes one register and leaves a multiplication equation in $I$. The final valuation stratum requires the kernel inside $I$, rather than the annihilator in all of $R$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Fix $(u,w)\in I^2$ and set $d=\min\{v(t+u),m-1\}$. The target is reachable if and only if $w\in t^{d+1}R$. If it is reachable and $x_0$ is one solution of $(t+u)x_0=w$ in $I$, its full predecessor set is $$F^{-1}(\{(u,w)\})=
 \{(x_0+k,u):k\in t^{m-d}R\},
 \label{eq:fibre}$$ and has cardinality $q^d$.

The first target coordinate forces $y=u$, so the remaining equation is $(t+u)x=w$ with $x\in I$. If $d\leq m-2$, write $t+u=t^d e$ for a unit $e$. Multiplication by $e$ permutes every ideal $t^rR$. Consequently multiplication by $t+u$ maps $I$ onto $t^{d+1}R$ and has kernel $t^{m-d}R$. For $w=t^{d+1}w_0$, a concrete solution is $x_0=te^{-1}w_0$; choosing another lift of $w_0$ changes this solution only by the kernel. Two solutions differ by a kernel element, and adding any kernel element preserves the equation. This proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} in this case.

If $d=m-1$, then $t+u\in t^{m-1}R$ and $(t+u)I=0$, including the case $t+u=0$. The only reachable second coordinate is $w=0$, and every $x\in I$ is then a solution. Here $t^{d+1}R=0$ and $t^{m-d}R=I$, so the same formula applies. The ideal cardinality in [\[eq:ideals\]](#eq:ideals){reference-type="eqref" reference="eq:ideals"} gives $q^d$.

[\[cor:fibrecensus\]]{#cor:fibrecensus label="cor:fibrecensus"} For $1\leq d\leq m-2$, exactly $$(q-1)q^{2(m-d-1)}
 \label{eq:ordinarycount}$$ targets have $q^d$ predecessors. Exactly $q$ targets have the largest fibre size $q^{m-1}$; they are $$(-t+c t^{m-1},0),\qquad c\in\mathbb F_q.
 \label{eq:maximizers}$$ The image size is $$|\mathop{\mathrm{im}}F|=q+(q-1)\sum_{j=1}^{m-2}q^{2j}.
 \label{eq:image}$$ All remaining targets have empty fibres. An empty sum is zero.

Translation $u\mapsto t+u$ permutes $I$. For each ordinary stratum $1\leq d\leq m-2$, exactly $(q-1)q^{m-d-1}$ values of $u$ give valuation $d$. For each such $u$, there are $q^{m-d-1}$ admissible values of $w$. Their product is [\[eq:ordinarycount\]](#eq:ordinarycount){reference-type="eqref" reference="eq:ordinarycount"}. The saturated condition $t+u\in t^{m-1}R$ instead has the $q$ solutions in [\[eq:maximizers\]](#eq:maximizers){reference-type="eqref" reference="eq:maximizers"}, each permitting only $w=0$. These fibres are larger than all ordinary ones. Summing their counts gives [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. At $m=2$ there is no ordinary stratum: all $q$ reachable targets have $q$ predecessors.

# Multiplication and linear controls {#sec:controls}

The fibre theorem is an evaluated multiplication relation. On the same carrier $I^2$, define $$M(a,b)=(b,ab),\qquad P(x,y)=(x,y+t),\qquad Q(u,w)=(u-t,w).$$ Both $P$ and $Q$ are bijections, and direct substitution gives $$F=Q\circ M\circ P.
 \label{eq:adapter}$$ Thus every one-step fibre and image count transfers from multiplication. No new inverse mechanism is claimed. Since $Q\ne P^{-1}$, this two-sided identity is not an iterate conjugacy and does not supply the temporal proof.

[\[prop:linear\]]{#prop:linear label="prop:linear"} The linear map $L:I^2\to I^2$, $L(x,y)=(y,tx)$, has the same pointwise clock and depth census as $F$. If $m=2$, then $F=L$. If $m\geq3$, $F$ is not bijectively conjugate to any endomorphism of a finite group.

For $k\geq0$, $$L^{2k}(x,y)=(t^kx,t^ky),\qquad
 L^{2k+1}(x,y)=(t^ky,t^{k+1}x).$$ These formulas give [\[eq:preview\]](#eq:preview){reference-type="eqref" reference="eq:preview"} and hence Corollary [\[cor:depth\]](#cor:depth){reference-type="ref" reference="cor:depth"}. When $m=2$, every product $xy$ with $x,y\in I$ vanishes, so $F=L$.

For $m\geq3$, Corollary [\[cor:fibrecensus\]](#cor:fibrecensus){reference-type="ref" reference="cor:fibrecensus"} supplies nonempty fibres of distinct sizes $q$ and $q^{m-1}$. If $\phi:G\to G$ is a finite-group endomorphism and $\phi(g)=h$, then $\phi^{-1}(\{h\})=g\mathop{\mathrm{ker}}\phi$: applying $\phi$ to $g^{-1}z$ proves both inclusions. All its nonempty fibres therefore have the same size. A bijective conjugacy preserves fibre cardinalities, giving the contradiction.

The obstruction concerns endomorphisms, not arbitrary nonlinear factors. Equal clocks and equal depth distributions are therefore weaker than a conjugacy in this family; their common numerical shape is not itself the advance of Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}.

# Verification scope and limitations {#sec:scope}

The proofs above hold for every prime power $q$ and every $m\geq2$. The accompanying author verifier was run for $q\in\{2,3,4\}$ and $m\in\{2,3,4\}$. It exhaustively checked every state, its literal transition and orbit-derived depth, and the full predecessor set of every target against the displayed formulas. For $q=4$ the coefficient field is $\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)$, not arithmetic modulo four. The nine carriers contain 5,271 states, and the complete output contains 10,646 records. Two further strict runs reproduced the canonical output byte for byte. These finite checks do not establish the all-parameter statements.

The result is specific to [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} on the full ideal square $I^2$. It establishes neither an arbitrary-chain-ring extension nor all-time fibre formulas or a classification of functional-graph isomorphisms. The temporal conclusion is narrower: leading-term cancellation changes one register's history without changing the exact deadline of the full nonlinear state.
