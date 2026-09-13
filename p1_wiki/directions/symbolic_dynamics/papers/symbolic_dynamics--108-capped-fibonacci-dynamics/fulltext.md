---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--108-capped-fibonacci-dynamics"
canonical_tex: "symbolic_dynamics/papers/108-capped-fibonacci-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/108-capped-fibonacci-dynamics/main.pdf"
source_sha256: "fbb093a9d89d646069e351554fb21031cff4965f56db487ab84dcc5860361066"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Capped Fibonacci Dynamics on a Finite Square: Exact Iterates, Lattice-Point Transients, and Sharp Depth

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/108-capped-fibonacci-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/108-capped-fibonacci-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/108-capped-fibonacci-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/108-capped-fibonacci-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/108-capped-fibonacci-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For an integer cap $a\geq1$, consider the finite dynamical system $$T_a(x,y)=(y,\min\{a,x+y\})
   \quad\text{on}\quad\{0,1,\ldots,a\}^2.$$ Saturation commutes with nonnegative addition strongly enough to preserve an exact Fibonacci normal form: $$T_a^t(x,y)=
   \bigl(\min\{a,F_{t-1}x+F_ty\},
         \min\{a,F_tx+F_{t+1}y\}\bigr),\qquad t\geq1.$$ There are exactly two recurrent states, both fixed. Every nonzero state hits $(a,a)$, and its exact depth is the first Fibonacci-weighted half-plane crossing. This yields a closed lattice-point cumulative distribution and the sharp maximum depth $1+\min\{k:F_k\geq a\}$. We also determine the one-step image, every fibre size, and all Garden-of-Eden states. Exhaustive integer iteration supplies an independent convention-sensitive control.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Capped Fibonacci Dynamics on a Finite Square: Exact Iterates, Lattice-Point Transients, and Sharp Depth'
```

## Markdown 正文

# Introduction and ownership boundary

Let $Q_a=\{0,1,\ldots,a\}^2$ and define $$\label{eq:map}
 T_a(x,y)=(y,x\oplus_a y),
 \qquad u\oplus_a v:=\min\{a,u+v\}.$$ The ordinary Fibonacci recurrence and its matrix identities are classical; we use the convention $F_0=0$, $F_1=1$, and $F_{t+1}=F_t+F_{t-1}$ [@Koshy2001; @Miles1960]. Saturated arithmetic and bounded recurrences occur broadly in digital and control systems [@HmamedEtAl2010]. These backgrounds receive no novelty credit. Our bounded object is the complete finite phase portrait of the particular map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}: the exact capped iterate, the half-plane transient law, the Fibonacci threshold for worst-case depth, and the inverse-fibre geometry. A targeted search on 29 August 2026 found uses of capped Fibonacci block sizes but not this self-map and theorem package. That bounded absence is not a priority claim; external circulation remains on **HOLD**.

Two proof lanes are kept separate. The forward lane uses the clipping identity for nonnegative integers and lifts the standard Fibonacci matrix induction. The inverse lane solves the two coordinate equations of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} directly and recovers the image and fibre sizes without using the iterate formula. The exact program implements literal integer updates and compares both predictions.

The internal collision boundary is also at the update-rule level. This is not a Catalan renewal shift, a Bernoulli reset of a golden-mean adjacency matrix, or a random cap--floor composition on an interval. Those nearby systems have different phases, randomness, and observables; the present map is one deterministic saturated second-order recurrence on an integer square. Within the present batch, P107 acts on ideals by an annihilator--power rule, P109 sends subspaces through a nilpotent linear operator, P110 joins translated set partitions, and P111 is an iid positive Heisenberg product. None has the phase space, update, or Fibonacci half-plane clock of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}.

# The Fibonacci normal form

The elementary saturation identity $$\label{eq:sat}
 \min\{a,\min\{a,u\}+\min\{a,v\}\}=\min\{a,u+v\}
 \qquad(u,v\geq0)$$ is the mechanism that prevents intermediate clipping from losing the final closed form.

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} For every $(x,y)\in Q_a$ and every $t\geq1$, $$\label{eq:iterate}
 T_a^t(x,y)=
 \left(
 \min\{a,F_{t-1}x+F_ty\},
 \min\{a,F_tx+F_{t+1}y\}
 \right).$$

For $t=1$, [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} is exactly [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. Assume it at time $t$ and abbreviate the uncapped linear forms by $U$ and $V$. One further step produces $$\bigl(\min\{a,V\},
 \min\{a,\min\{a,U\}+\min\{a,V\}\}\bigr).$$ Apply [\[eq:sat\]](#eq:sat){reference-type="eqref" reference="eq:sat"} to the second coordinate and use $F_{t-1}+F_t=F_{t+1}$ coefficientwise. The result is the formula with $t$ replaced by $t+1$.

This is stronger than merely saying that the uncapped recurrence eventually exceeds the cap: it identifies every finite-time state, including partially saturated trajectories.

# Attractors and exact transient census

[\[prop:recurrence\]]{#prop:recurrence label="prop:recurrence"} The only recurrent states are the two fixed points $(0,0)$ and $(a,a)$. Every nonzero state reaches $(a,a)$. Consequently, for every $k\geq1$, $$\label{eq:fixed}
 \#\operatorname{Fix}(T_a^k)=2,
 \qquad \zeta_{T_a}(z)=(1-z)^{-2}.$$

A fixed point has $x=y$ and $y=\min\{a,2y\}$, giving only $y=0$ or $a$. If $(x,y)\neq(0,0)$, then for large $t$ both nonnegative linear forms in [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} are at least $a$, so the orbit reaches $(a,a)$. Thus no other periodic point exists. The zeta identity follows from the constant iterate-fixed count and the definition of Artin--Mazur zeta [@ArtinMazur1965].

Define $\operatorname{depth}(x,y)$ as the first time the orbit is recurrent. For $t\geq1$ put $u_t=F_{t-1}$ and $v_t=F_t$.

[\[thm:cdf\]]{#thm:cdf label="thm:cdf"} The two fixed points have depth zero. Every other state satisfies $$\label{eq:point-depth}
 \operatorname{depth}(x,y)=\min\{t\geq1:u_tx+v_ty\geq a\}.$$ If $C_a(t)=\#\{(x,y):\operatorname{depth}(x,y)\leq t\}$, then $C_a(0)=2$ and, for $t\geq1$, $$\begin{aligned}
 C_a(t)
 &=1+\#\{(x,y)\in Q_a:u_tx+v_ty\geq a\}                    \label{eq:cdf-set}\\
 &=1+\sum_{x=0}^{a}
 \left(a+1-\max\left\{0,
 \left\lceil\frac{a-u_tx}{v_t}\right\rceil\right\}\right).
 \label{eq:cdf-sum}\end{aligned}$$ The exact depth-$t$ shell is $C_a(t)-C_a(t-1)$.

For $t\geq1$, the second uncapped form in [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} dominates the first. Hence $T_a^t(x,y)=(a,a)$ exactly when the first form crosses $a$, which proves [\[eq:point-depth\]](#eq:point-depth){reference-type="eqref" reference="eq:point-depth"}. At positive time, the states already recurrent consist of $(0,0)$ plus the states that have reached $(a,a)$, giving [\[eq:cdf-set\]](#eq:cdf-set){reference-type="eqref" reference="eq:cdf-set"}. For fixed $x$, the admissible $y$ are the integers from $\max\{0,\lceil(a-u_tx)/v_t\rceil\}$ through $a$, proving [\[eq:cdf-sum\]](#eq:cdf-sum){reference-type="eqref" reference="eq:cdf-sum"}.

[\[cor:maxdepth\]]{#cor:maxdepth label="cor:maxdepth"} The maximum transient depth is $$\label{eq:maxdepth}
 D_a=1+\min\{k\geq0:F_k\geq a\}.$$ It is attained by $(1,0)$, and $D_a=\log_{\varphi}a+O(1)$, where $\varphi=(1+\sqrt5)/2$. Thus the depth staircase has Fibonacci plateau endpoints: it changes exactly when the cap crosses a Fibonacci number.

For any nonzero $(x,y)$, the first form in [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} is at least $F_{t-1}$ once $F_{t-1}>0$, because one of $x,y$ is at least one and $F_t\geq F_{t-1}$. Equality is realized by $(1,0)$. This proves the exact threshold. The asymptotic statement follows from the standard Binet bounds.

# Inverse fibres and Garden-of-Eden states

The inverse geometry is independent of the Fibonacci induction.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} The one-step image is the upper triangular half-square $$\label{eq:image}
 \operatorname{im}(T_a)=\{(u,v)\in Q_a:u\leq v\}.$$ For $(u,v)\in Q_a$, $$\label{eq:fibres}
 \#T_a^{-1}(u,v)=
 \begin{cases}
  0,&v<u,\\
  1,&u\leq v<a,\\
  u+1,&v=a.
 \end{cases}$$ Hence there are $a(a+1)/2$ Garden-of-Eden states and $(a+1)(a+2)/2$ image states.

If $T_a(x,y)=(u,v)$, then $y=u$ and $v=\min\{a,x+u\}$. When $v<a$, the unique possible preimage is $(v-u,u)$, which exists exactly when $v\geq u$. When $v=a$, the allowed values are $a-u\leq x\leq a$, giving $u+1$ preimages. The states below the diagonal are precisely the states with no preimage, and summing a triangular array gives both cardinalities.

The fibre formula also provides a global checksum: $$\sum_{(u,v)\in Q_a}\#T_a^{-1}(u,v)=(a+1)^2=\#Q_a.$$

# Independent exact control

The standard-library verifier enumerates every state for caps $1\leq a\leq
220$. Literal repeated application of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is compared at every registered time with [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}; the observed depth histogram is compared with both [\[eq:point-depth\]](#eq:point-depth){reference-type="eqref" reference="eq:point-depth"} and [\[eq:cdf-sum\]](#eq:cdf-sum){reference-type="eqref" reference="eq:cdf-sum"}. A separate reverse table counts every one-step fibre and checks [\[eq:fibres\]](#eq:fibres){reference-type="eqref" reference="eq:fibres"}, the image size, and the Garden-of-Eden count. The finite run is a hostile convention check, not an extrapolative proof.

# Conclusion

The cap does not destroy the linear recurrence; it converts it into a finite saturated dynamics whose exact iterates retain the Fibonacci matrix. That identity simultaneously controls attraction, every transient layer, and the logarithmic worst-case clock, while direct inversion exposes a triangular image with explicit fibres. The source and release boundary remains conservative pending specialist review.
