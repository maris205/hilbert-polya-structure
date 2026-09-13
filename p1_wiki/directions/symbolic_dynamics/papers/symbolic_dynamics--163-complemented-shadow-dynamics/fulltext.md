---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--163-complemented-shadow-dynamics"
canonical_tex: "symbolic_dynamics/papers/163-complemented-shadow-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/163-complemented-shadow-dynamics/main.pdf"
source_sha256: "bb18ae1fbe2f9b7994efc3bdbe69917783e5e5e2acc539bbc8dcb37fbbb79e8f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Complemented-Shadow Dynamics on Set Families: Atomic Kernels and Support-Resolved Deepest Shells

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/163-complemented-shadow-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/163-complemented-shadow-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/163-complemented-shadow-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/163-complemented-shadow-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/163-complemented-shadow-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix $n\geq2$ and map a set family to the complements of all members of its lower shadow. We determine every atomic iterate: even times are closed balls in a Johnson graph, while odd times satisfy a dual intersection threshold. These kernels give a parity-sensitive clock for every mixed-rank family and a recurrent core governed by an involution on rank support. The central result classifies the full phase-space shell at maximum depth. For $n\geq3$, a family has tail $n-1$ exactly when its rank-$\lceil n/2\rceil$ slice contains one set. Hence the shell has $\binom{n}{\lceil n/2\rceil}2^{2^n-\binom{n}{\lceil n/2\rceil}}$ members. We refine this count by the rank support inherited by the eventual cycle and factor the shell into eventual periods one and two. The exceptional case $n=2$ has twelve deepest states, split six and six. Shadow, Johnson-ball, Boolean-relation, and covering ingredients are treated as owned background; the artifact remains `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Complemented-Shadow Dynamics on Set Families:\
  Atomic Kernels and Support-Resolved Deepest Shells
```

## Markdown 正文

# The literal map and main contracts

Let $[n]=\{1,\ldots,n\}$, $\mathcal B_n=2^{[n]}$, and let the phase space be $2^{\mathcal B_n}$. Complements are taken in $[n]$. The deterministic map is $$\label{eq:map}
 \mathsf S_n(\mathcal F)=
 \{\,\overline{A\setminus\{a\}}:A\in\mathcal F,\ a\in A\,\}.$$ Thus the empty set is a silent atom and [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} distributes over unions. For $A\neq\varnothing$, define $\mathsf K_t(A)=\mathsf S_n^t(\{A\})$ and $\phi(k)=n-k+1$ on the nonzero ranks.

For a family $\mathcal F$, write $\mathcal F_k=\mathcal F\cap\binom{[n]}k$ and $R(\mathcal F)=\{k\geq1:\mathcal F_k\neq\varnothing\}$. When $\mathcal F_k$ is nonempty, put $$\begin{aligned}
 e_k(\mathcal F)&=\max_{B\in\binom{[n]}k}\min_{A\in\mathcal F_k}
   \bigl(k-|A\cap B|\bigr),\label{eq:e}\\
 o_k(\mathcal F)&=\max_{C\in\binom{[n]}{\phi(k)}}\min_{A\in\mathcal F_k}
   \bigl(|A\cap C|-1\bigr).\label{eq:o}\end{aligned}$$ Let $e(\mathcal F)$ and $o(\mathcal F)$ be the maxima over $k\in R(\mathcal F)$. The tail $\mu(\mathcal F)$ is the least time at which the orbit enters its eventual cycle.

[\[thm:forward\]]{#thm:forward label="thm:forward"} For $n\geq2$, the following hold.

1.  If $A$ has rank $k\geq1$, then for every $s\geq0$, $$\begin{aligned}
     \mathsf K_{2s}(A)
     &=\left\{B\in\binom{[n]}k:k-|A\cap B|\leq s\right\},\label{eq:even}\\
     \mathsf K_{2s+1}(A)
     &=\left\{C\in\binom{[n]}{\phi(k)}:|A\cap C|\leq s+1\right\}.
     \label{eq:odd}\end{aligned}$$ The silent atom satisfies $\mathsf K_0(\varnothing)=\{\varnothing\}$ and $\mathsf K_t(\varnothing)=\varnothing$ for $t\geq1$, and $\mathsf S_n^t(\mathcal F)=\bigcup_{A\in\mathcal F}\mathsf K_t(A)$.

2.  If $R(\mathcal F)\neq\varnothing$, then $$\label{eq:clock}
     \mu(\mathcal F)=\max\left\{\mathbf1_{\{\varnothing\in\mathcal F\}},
     \min\{2e(\mathcal F),\,2o(\mathcal F)+1\}\right\}.$$ The empty family has tail zero and $\{\varnothing\}$ has tail one. The global height is $n-1$.

3.  For $R\subseteq\{1,\ldots,n\}$, let $$\label{eq:UR}
     U_R=\bigcup_{k\in R}\binom{[n]}k.$$ The recurrent states are exactly the $2^n$ families $U_R$, with $\mathsf S_n(U_R)=U_{\phi(R)}$. There are $2^{\lceil n/2\rceil}$ fixed states; all other recurrent states lie in strict two-cycles. Hence $$\label{eq:fix}
     |\operatorname{Fix}(\mathsf S_n^j)|=
     \begin{cases}2^{\lceil n/2\rceil},&j\text{ odd},\\2^n,&j\text{ even},
     \end{cases}$$ and the Artin--Mazur zeta function is $$\label{eq:zeta}
     \zeta_{\mathsf S_n}(z)=
     (1-z)^{-2^{\lceil n/2\rceil}}
     (1-z^2)^{-(2^n-2^{\lceil n/2\rceil})/2}.$$

The full phase space is much larger than the recurrent core. The next theorem resolves which of its $2^{2^n}$ states occupy the last transient shell.

[\[thm:deep\]]{#thm:deep label="thm:deep"} For a nonempty rank-$k$ atom, the singleton family $\{A\}$ has depth $$\label{eq:delta}
 \delta_n(k)=\min\{2\min(k,n-k),\,2\min(k-1,n-k)+1\}.$$ Every $d\in\{0,\ldots,n-1\}$ is realized by exactly one rank, $$\label{eq:rank-depth}
 k_n(d)=
 \begin{cases}n-d/2,&d\text{ even},\\(d+1)/2,&d\text{ odd},\end{cases}$$ so exactly $\binom n{\lceil d/2\rceil}$ nonempty atomic singleton families have depth $d$.

Assume now $n\geq3$, and set $$\label{eq:middle}
 k_\star=\lceil n/2\rceil,\qquad M_n=\binom n{k_\star}.$$ Then $$\label{eq:iff}
 \mu(\mathcal F)=n-1\quad\Longleftrightarrow\quad |\mathcal F_{k_\star}|=1,$$ and therefore $$\label{eq:deep-total}
 D_n:=|\{\mathcal F:\mu(\mathcal F)=n-1\}|=M_n2^{2^n-M_n}.$$ More precisely, for each endpoint rank support $R\subseteq\{1,\ldots,n\}$, $$\label{eq:deep-support}
 D_n(R)=
 \begin{cases}
 0,&k_\star\notin R,\\[2pt]
 \displaystyle 2M_n\prod_{k\in R\setminus\{k_\star\}}
   \left(2^{\binom nk}-1\right),&k_\star\in R.
 \end{cases}$$ Here $R=R(\mathcal F)$ labels one endpoint of the eventual support cycle $R\leftrightarrow\phi(R)$.

Let $\Omega_n$ be the orbit set of $\phi$ on the ranks, put $w_k=2^{\binom nk}-1$, and define $$\label{eq:qO}
 q_O=
 \begin{cases}
 \displaystyle\prod_{j\in O\setminus\{k_\star\}}w_j,&k_\star\in O,\\[6pt]
 \displaystyle1+\prod_{j\in O}w_j,&k_\star\notin O.
 \end{cases}$$ The numbers of deepest states with eventual periods one and two are $$\begin{aligned}
 D_n^{(1)}&=2M_n\prod_{O\in\Omega_n}q_O,\label{eq:period-one}\\
 D_n^{(2)}&=M_n2^{2^n-M_n}-D_n^{(1)}.\label{eq:period-two}\end{aligned}$$ At $n=2$, the height is one and all twelve nonrecurrent states are deepest; six have eventual period one and six have eventual period two. Condition [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"} selects only eight states, so [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"}--[\[eq:period-two\]](#eq:period-two){reference-type="eqref" reference="eq:period-two"} are not asserted at this boundary.

# Johnson kernels and the mixed-rank clock

Lower shadows and their extremal theory are classical [@kruskal1963; @katona2009]. The exact identity between a shadow followed by an upper shadow and closed-neighbourhood dilation in a Johnson graph is also recorded directly in the Johnson-graph literature [@diego2018]. It supplies the owned forward primitive used below.

[\[lem:square\]]{#lem:square label="lem:square"} On rank $k\geq1$, $\mathsf S_n^2$ is closed-neighbourhood expansion in the Johnson graph $J(n,k)$.

The one-step images of $A$ are $\bar A\cup\{a\}$ for $a\in A$. From this set, choosing $a$ returns $A$, while choosing $b\in\bar A$ returns $(A\setminus\{a\})\cup\{b\}$. These are exactly $A$ and its Johnson neighbours.

Iterating Lemma [\[lem:square\]](#lem:square){reference-type="ref" reference="lem:square"} gives the closed Johnson ball [\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"}. A rank-$\phi(k)$ set $C$ has one-step predecessors $\bar C\cup\{c\}$ for $c\in C$. Since every rank-$k$ set $A$ meets $C$, the minimum Johnson distance from $A$ to these predecessors is $|A\cap C|-1$. Applying one further step to [\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"} proves [\[eq:odd\]](#eq:odd){reference-type="eqref" reference="eq:odd"}. Union preservation proves the arbitrary-family formula.

At time $2s$, a nonempty rank slice fills its layer exactly when $s\geq e_k$; at time $2s+1$, its image fills the dual layer exactly when $s\geq o_k$. The map $\phi$ is bijective, so all occupied slices must fill at the same parity. The earlier of these two saturation times, together with the one-step loss of the silent atom, proves [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}.

A periodic family cannot contain the silent atom. Lemma [\[lem:square\]](#lem:square){reference-type="ref" reference="lem:square"} also makes every rank slice inflationary under $\mathsf S_n^2$, so periodicity forces that square to fix the family. Each nonempty slice is then invariant under closed-neighbourhood expansion in the connected graph $J(n,k)$, hence is either empty or the whole layer. This gives precisely [\[eq:UR\]](#eq:UR){reference-type="eqref" reference="eq:UR"}. Rank support follows the involution $\phi$, proving the recurrent and fixed counts, [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"}, and [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. The height statement follows from Theorem [\[thm:deep\]](#thm:deep){reference-type="ref" reference="thm:deep"}, including its $n=2$ branch.

For a singleton rank-$k$ source, the even covering radius is $\min(k,n-k)$. The largest odd defect is $\min(k,n-k+1)-1=\min(k-1,n-k)$. Substitution into [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} proves [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"}; separating even and odd depths gives [\[eq:rank-depth\]](#eq:rank-depth){reference-type="eqref" reference="eq:rank-depth"} and its binomial census.

# Central equality rigidity and support products

Suppose $n=2m$. Every occupied slice has $e_k\leq m$ and $o_k\leq m-1$. Tail $2m-1$ therefore requires $e(\mathcal F)=m$ and $o(\mathcal F)=m-1$. Only rank $m$ can attain the even equality. In $J(2m,m)$, the sole point at distance $m$ from a fixed vertex is its complement. Thus a rank-$m$ slice has covering radius $m$ exactly when it is a singleton, and such a singleton also attains the odd bound.

Now suppose $n=2m+1$. Both radii are at most $m$, and tail $2m$ forces $e(\mathcal F)=o(\mathcal F)=m$. Only rank $m+1$ can attain the odd equality. Equality means that some $(m+1)$-set $C$ satisfies $|A\cap C|-1=m$ for every $A\in\mathcal F_{m+1}$, forcing every such $A$ to equal $C$. Conversely, a singleton central slice attains both bounds. This proves [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"} in both parities.

There are $M_n$ choices for the central atom. Every one of the other $2^n-M_n$ atoms, including the silent atom, is unrestricted. This proves [\[eq:deep-total\]](#eq:deep-total){reference-type="eqref" reference="eq:deep-total"}.

Fix $R$. The central slice contributes $M_n$ choices. Each other occupied rank $k$ contributes any nonempty slice, hence $w_k$ choices; an absent rank is forced, and the silent atom is optional. This gives [\[eq:deep-support\]](#eq:deep-support){reference-type="eqref" reference="eq:deep-support"}, whose sum over $R$ is [\[eq:deep-total\]](#eq:deep-total){reference-type="eqref" reference="eq:deep-total"}.

The eventual period is one precisely when $R=\phi(R)$. On a $\phi$-orbit not containing $k_\star$, invariant support is either absent on the whole orbit or occupied at every rank, contributing $1+\prod_{j\in O}w_j$. The orbit containing $k_\star$ is forced occupied and contributes $\prod_{j\in O\setminus\{k_\star\}}w_j$. Including the central choice and the optional silent atom proves [\[eq:period-one\]](#eq:period-one){reference-type="eqref" reference="eq:period-one"}; subtraction proves [\[eq:period-two\]](#eq:period-two){reference-type="eqref" reference="eq:period-two"}. Direct enumeration of the sixteen phase states gives the stated $n=2$ exception.

# Inverse completeness and claim boundary

The atomic description also yields a complete inverse formula, although its proof is ordinary cover inclusion--exclusion and is not used as a residual contribution axis. For $t\geq1$ and a target family $\mathcal G$, define $$c_t(\mathcal G)=|\{A\in\mathcal B_n\setminus\{\varnothing\}:\mathsf K_t(A)\subseteq\mathcal G\}|.$$

[\[prop:inverse\]]{#prop:inverse label="prop:inverse"} For $t\geq1$, $$\label{eq:inverse}
 |\mathsf S_n^{-t}(\mathcal G)|=
 2\sum_{\mathcal J\subseteq\mathcal G}(-1)^{|\mathcal J|}2^{c_t(\mathcal G\setminus\mathcal J)}.$$ The target is in the image exactly when $$\label{eq:image}
 \mathcal G=\bigcup_{A\neq\varnothing:\ \mathsf K_t(A)\subseteq\mathcal G}\mathsf K_t(A).$$ For $t\geq n-1$, only recurrent targets occur, and $$\label{eq:stable-fibre}
 |\mathsf S_n^{-t}(U_R)|=
 2\prod_{k\in\phi^t(R)}\left(2^{\binom nk}-1\right).$$ In particular, the empty target has two preimages at every positive time.

A source consists of admissible nonempty atoms whose kernels lie in $\mathcal G$ and whose union covers $\mathcal G$. Inclusion--exclusion over missed target atoms gives the sum in [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}; the optional silent atom supplies the factor two. Taking the union of all admissible kernels gives [\[eq:image\]](#eq:image){reference-type="eqref" reference="eq:image"}. After time $n-1$, every occupied rank slice has saturated, so each required source rank may be any nonempty slice. The source support is $\phi^t(R)$, which proves [\[eq:stable-fibre\]](#eq:stable-fibre){reference-type="eqref" reference="eq:stable-fibre"}.

The owner subtraction is substantial. Shadow extremality and Johnson dilation receive zero contribution credit [@kruskal1963; @katona2009; @diego2018]. Representing a union-preserving powerset map by a Boolean relation, and using relation powers to describe its eventual behaviour, are also established frameworks [@rosenblatt1957; @gregory1993; @akin2024]. Formula [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} is standard cover inclusion--exclusion. The assessed residual is only the integrated parity clock, atomic depth census, and central-slice deepest-shell classification with its support and period products. The bounded source audit does not establish originality, precedence, or publication safety.

The internal comparison makes the same subtraction. P97 removes generic union-driven subset growth; P110 and P115 already contain deepest-shell formats on different carriers; P143 removes generic Boolean-relation and eventual-period language. None of those arguments transfers the simultaneous even/odd radius optimization or central-slice equality condition used in [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"}.

# Exact controls, limitations, and declarations

A paper-local standard-library verifier constructs [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} literally and compares it with both atomic kernel formulas through $n=9$. It exhausts all phase states and all audited targets through $n=4$, including mixed-rank clocks, union iterates, recurrent and fixed states, image criteria, inverse fibres, deepest support counts, and the $n=2$ split. Central singleton and pair controls extend through $n=12$. The run executes $1{,}430{,}898$ integer assertions. Two fresh replays were byte-identical; the canonical transcript has SHA-256 (the following two lines concatenate):

`21d2dc8e66580e7b78ef9c4bd2bda3ea`\
`a393757ee466497a62defb0f15700434`.

Enumeration supplies counterexample pressure only. The all-parameter claims rest on the preceding proofs.

# Limitations {#limitations .unnumbered}

The theorem is restricted to complementation after the ordinary lower shadow on labelled subsets of a fixed $[n]$. It does not cover weighted families, biased deletion, other rank-selected shadows, quotienting by relabelling, or perturbations of the Boolean union rule. The phase-space shell is counted by labelled states. The source audit was bounded, so a direct conjunction owner under different terminology would require the claim boundary to be reopened.

# Data Availability {#data-availability .unnumbered}

No external data were used. The deterministic verifier and frozen transcript provide the complete paper-local exact control.

# Ethics Statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, animals, personal data, or field intervention.

# Author Contributions {#author-contributions .unnumbered}

The anonymous author performed the derivation, proof, exact checks, source-boundary audit, and manuscript preparation.

# Conflict of Interest {#conflict-of-interest .unnumbered}

The author declares no conflict of interest.

# Funding {#funding .unnumbered}

No external funding is declared.

# External Status {#external-status .unnumbered}

This anonymous internal artifact remains `HOLD_EXTERNAL`. It is not cleared for posting, submission, circulation, or author contact.
