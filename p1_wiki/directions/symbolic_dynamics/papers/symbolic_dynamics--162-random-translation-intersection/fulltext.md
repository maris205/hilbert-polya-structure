---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--162-random-translation-intersection"
canonical_tex: "symbolic_dynamics/papers/162-random-translation-intersection/main.tex"
canonical_pdf: "symbolic_dynamics/papers/162-random-translation-intersection/main.pdf"
source_sha256: "98b54a3052dccb6168655e8f337921eef76547c73005d847338eb69fd5454e1d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Random Translation Intersections on Binary Vector Spaces: Sharp Span Clocks and Stabilizer-Weighted Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/162-random-translation-intersection>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/162-random-translation-intersection/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/162-random-translation-intersection/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/162-random-translation-intersection/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/162-random-translation-intersection/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $V=\mathbb F_2^d$ and repeatedly replace a subset $A\subseteq V$ by $A\cap(A+v)$, where $v$ is sampled uniformly from $V$. A length-$t$ history acts exactly as intersection by every translate in the span of its sampled vectors. We use this sufficient statistic to give the complete rank law and a sharp worst-non-full-source emptying clock, witnessed by $V\setminus
  \{0\}$. For every target $B$, every time, and every source size, we then enumerate source--history pairs by a polynomial determined by the translation stabilizer of $B$. Its one-step boundary separates targets with trivial stabilizer and recovers the stabilizer dimension once the phase dimension and target size are known. The forward erosion algebra and finite-field rank law are classical inputs; the contribution assessed here is the exact conjunction with the target-dependent inverse atlas. All release claims remain under `HOLD_EXTERNAL`.
author:
- Anonymous
bibliography:
- references.bib
title: 'Random Translation Intersections on Binary Vector Spaces: Sharp Span Clocks and Stabilizer-Weighted Fibres'
```

## Markdown 正文

# Process and theorem

Write $A+v=\{a+v:a\in A\}$. Starting from $A_0\in\mathcal P(V)$, sample independent uniform vectors $v_1,v_2,\ldots$ and set $$\label{eq:update}
 A_i=A_{i-1}\cap(A_{i-1}+v_i).$$ For a subspace $H\leq V$, define $$\mathsf E_H(A)=\bigcap_{h\in H}(A+h),
 \qquad H_t=\langle v_1,\ldots,v_t\rangle.$$ Let $$\label{eq:S}
 S(t,r)=\prod_{i=0}^{r-1}(2^t-2^i),$$ with the empty product equal to one, and put $S(t,r)=0$ for $r>t$. We write $\genfrac{[}{]}{0pt}{}{m}{r}_2$ for the Gaussian binomial coefficient.

For a target $B\subseteq V$, set $b=|B|$ and $$\operatorname{Stab}(B)=\{v\in V:B+v=B\},\qquad s=\dim\operatorname{Stab}(B).$$ The joint source-size/history polynomial is $$\label{eq:Fdef}
 F_t(B;z)=\sum_{A\subseteq V}\ \sum_{(v_1,\ldots,v_t)\in V^t}
 \mathbf 1\{A_t=B\}z^{|A|}.$$

[\[thm:main\]]{#thm:main label="thm:main"} For every $d,t\geq0$ the following statements hold.

1.  Every history satisfies the pointwise identity $$\label{eq:span}
     A_t=\mathsf E_{H_t}(A_0).$$ Moreover, $$\label{eq:rank}
     \Pr(\dim H_t=r)=
     \genfrac{[}{]}{0pt}{}{d}{r}_2\frac{S(t,r)}{2^{dt}}.$$

2.  The only states fixed by every possible sampled update are $\varnothing$ and $V$. Let $\sigma=\min\{t:H_t=V\}$. Every $A_0\neq V$ is empty by time $\sigma$, and this bound is attained by $A_\star=V\setminus\{0\}$. Thus the sharp worst-source emptying distribution is $$\label{eq:cdf}
     \Pr(\sigma\leq t)=
     \begin{cases}
     0,&t<d,\\[2pt]
     \displaystyle\prod_{i=0}^{d-1}(1-2^{i-t}),&t\geq d,
     \end{cases}$$ and $$\label{eq:mean}
     \mathbb E\sigma=\sum_{r=0}^{d-1}\frac{1}{1-2^{r-d}}.$$

3.  For every target $B$ and indeterminate $z$, $$\label{eq:fibre}
     F_t(B;z)=z^b\sum_{r=0}^{s}
     \genfrac{[}{]}{0pt}{}{s}{r}_2 S(t,r)
     \left((1+z)^{2^r}-z^{2^r}\right)^{2^{d-r}-b/2^r}.$$ For $r\leq s$, the exponent is a nonnegative integer. Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} includes $t=0$, $d=0$, and the empty and full targets. At one step its unweighted specialization is the boundary-safe formula $$\label{eq:one-step}
     F_1(B;1)=
     \begin{cases}
     1,&s=0,\\[2pt]
     1+(2^s-1)3^{2^{d-1}-b/2},&s\geq1.
     \end{cases}$$

4.  The phase cardinality $|\mathcal P(V)|=2^{2^d}$ determines $d$. At fixed $(d,b)$, the value in [\[eq:one-step\]](#eq:one-step){reference-type="eqref" reference="eq:one-step"} is strictly increasing over the feasible values of $s$, with value one occurring exactly at $s=0$. Consequently phase size, target size, and one-step inverse mass recover the target stabilizer dimension.

The clock in part (2) is a sharp universal bound, not an assertion that every non-full source empties exactly at $\sigma$. This distinction is important: individual sources may disappear earlier.

# History spans and the sharp clock

The algebra of erosions by translates is standard in mathematical morphology [@heijmans_ronse_1990; @heijmans_serra_1992]; stochastic morphological sampling is also established background [@sivakumar_goutsias_1996]. We record the short reduction needed for this particular process.

[\[lem:semigroup\]]{#lem:semigroup label="lem:semigroup"} For subspaces $H,K\leq V$, $\mathsf E_K(\mathsf E_H(A))=\mathsf E_{H+K}(A)$.

Distributing intersections over translation gives $$\mathsf E_K(\mathsf E_H(A))
 =\bigcap_{k\in K}\bigcap_{h\in H}(A+h+k)
 =\bigcap_{u\in H+K}(A+u).$$ Repeated factors do not affect an intersection.

Because $\langle v\rangle=\{0,v\}$ in characteristic two, one update is $\mathsf E_{\langle v\rangle}$. Lemma [\[lem:semigroup\]](#lem:semigroup){reference-type="ref" reference="lem:semigroup"} iterated over the history proves [\[eq:span\]](#eq:span){reference-type="eqref" reference="eq:span"}.

For a fixed $r$-subspace $H$, histories spanning $H$ are surjective linear maps $\mathbb F_2^t\to H$. Choosing the images dually as an ordered independent $r$-tuple in $\mathbb F_2^t$ gives [\[eq:S\]](#eq:S){reference-type="eqref" reference="eq:S"}. There are $\genfrac{[}{]}{0pt}{}{d}{r}_2$ choices of $H$, which proves [\[eq:rank\]](#eq:rank){reference-type="eqref" reference="eq:rank"}. This finite-field rank enumeration is classical; we do not claim it as a standalone increment [@balakin_1968].

If $A$ is fixed by every update, then $A\subseteq A+v$ for every $v$. Cardinalities force equality, so $A$ is invariant under all translations and hence is either $\varnothing$ or $V$.

When $H_t=V$, the set $\mathsf E_V(A)$ is $V$ for $A=V$ and is empty otherwise. Sharpness follows from the stronger identity $$\label{eq:witness}
 \mathsf E_H(V\setminus\{0\})=V\setminus H:$$ $x$ survives exactly when $x+h\neq0$ for every $h\in H$, equivalently when $x\notin H$. Therefore the witness empties exactly at full span.

Equation [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} is the full-rank probability in [\[eq:rank\]](#eq:rank){reference-type="eqref" reference="eq:rank"}. At rank $r<d$, a fresh uniform vector increases the rank with probability $1-2^{r-d}$. The independent geometric waiting times for the successive rank increments have means $(1-2^{r-d})^{-1}$, proving [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}.

# Stabilizer-weighted inverse fibres

The inverse enumeration uses information absent from the rank marginal: the specific target controls which history spans are possible.

[\[lem:fixed\]]{#lem:fixed label="lem:fixed"} Let $H\leq V$ have dimension $r$. There exists a source $A$ with $\mathsf E_H(A)=B$ if and only if $H\leq\operatorname{Stab}(B)$. In that case the source-size polynomial is $$\label{eq:fixed}
 \sum_{A:\,\mathsf E_H(A)=B}z^{|A|}
 =z^b\left((1+z)^{2^r}-z^{2^r}\right)^{2^{d-r}-b/2^r}.$$

The set $\mathsf E_H(A)$ is the union of precisely those $H$-cosets wholly contained in $A$. Hence it is $H$-invariant, proving necessity. Conversely, if $H\leq\operatorname{Stab}(B)$, then $B$ is a union of $b/2^r$ full $H$-cosets. A source with erosion $B$ must contain all of them. On each of the remaining $2^{d-r}-b/2^r$ cosets it may choose any proper subset, independently. One coset contributes $(1+z)^{2^r}-z^{2^r}$, which proves [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"}.

For a rank-$r$ history, Lemma [\[lem:fixed\]](#lem:fixed){reference-type="ref" reference="lem:fixed"} permits exactly the subspaces $H\leq\operatorname{Stab}(B)$. Their number is $\genfrac{[}{]}{0pt}{}{s}{r}_2$, and each is generated by $S(t,r)$ ordered histories. Summing [\[eq:fixed\]](#eq:fixed){reference-type="eqref" reference="eq:fixed"} proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

When $t=0$, only $r=0$ remains and the expression reduces to $z^b$, as it must. If $B=V$, the only source is $V$ and the rank sum gives $F_t(V;z)=2^{dt}z^{2^d}$. The empty target and $d=0$ require no exceptional convention beyond empty products.

At $t=1$, the zero history has rank zero and contributes one at $z=1$. Every nonzero vector of $\operatorname{Stab}(B)$ spans a rank-one subspace, and each outside two-point coset has three proper subsets. There are $2^s-1$ such histories. If $s\geq1$, then $B$ is a union of two-point orbits, so $b$ is even and the second line of [\[eq:one-step\]](#eq:one-step){reference-type="eqref" reference="eq:one-step"} follows. If $s=0$, there is no nonzero stabilizing history and the value is one. Keeping this branch separate is essential for odd $b$, where the other displayed exponent would not be an integer.

The map $d\mapsto2^{2^d}$ is injective. At fixed $(d,b)$ the power of three in the second line of [\[eq:one-step\]](#eq:one-step){reference-type="eqref" reference="eq:one-step"} is constant, while $2^s-1$ is strictly increasing. Its positive contribution also separates every $s\geq1$ from the value one at $s=0$.

The polynomial contains more than unweighted fibre sizes: its coefficient of $z^k$ counts all length-$t$ histories and $k$-point sources reaching the prescribed target. Thus target shape enters through $\operatorname{Stab}(B)$ even when target cardinality is held fixed.

# Source subtraction, controls, and scope

The update's erosion interpretation and composition algebra receive zero contribution credit [@heijmans_ronse_1990; @heijmans_serra_1992]; so do the generic stochastic-morphology setting [@sivakumar_goutsias_1996] and the finite-field rank distribution [@balakin_1968]. The bounded source audit found no primary source for the exact conjunction of the sharp witness [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"}, the arbitrary-target polynomial [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, and the recovery law [\[eq:one-step\]](#eq:one-step){reference-type="eqref" reference="eq:one-step"}. This non-hit is not a novelty, priority, or freedom-to-publish claim. Internally, the closest comparators use deterministic linear-subspace descent or random graph-cut signatures; neither transfers the affine-coset proper-subset fibre proof.

A paper-local, standard-library verifier applies every literal update and independently evaluates the span erosion over finite exhaustive boxes. It compares every target and source-size coefficient with [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, checks the rank census and full-rank boundary, tests the witness over all subspaces through dimension six, and exercises $d=0$, $t=0$, empty/full targets, odd-cardinality trivial stabilizers, and the repaired one-step branch. The frozen assertion total and transcript digest are recorded in the accompanying canonical file and build record. The run executes $1{,}712{,}974$ integer assertions; two fresh replays were byte-identical. The canonical transcript has SHA-256 (the following two lines concatenate):

`c31ec0a098bab52241eb2765bd6fef06`\
`69fdacdb4486ca69bea9dfc56fbab62b`.

Enumeration supplies counterexample pressure only; the all-parameter conclusions rest on the proofs above.

# Limitations {#limitations .unnumbered}

The process uses independent uniform translations of a binary vector space and begins from an arbitrary labelled subset. We do not treat biased or dependent histories, non-elementary finite groups, noisy observations, unlabelled targets, or asymptotic distributional limits. The source search was bounded, so a direct owner under different terminology would reopen the claim boundary.

# Data Availability {#data-availability .unnumbered}

No external data were used. The deterministic verifier and its canonical transcript provide the complete paper-local exact control.

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
