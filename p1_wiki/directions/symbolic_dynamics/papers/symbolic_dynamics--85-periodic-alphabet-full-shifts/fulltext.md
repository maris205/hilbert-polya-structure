---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--85-periodic-alphabet-full-shifts"
canonical_tex: "symbolic_dynamics/papers/85-periodic-alphabet-full-shifts/main.tex"
canonical_pdf: "symbolic_dynamics/papers/85-periodic-alphabet-full-shifts/main.pdf"
source_sha256: "a8a8edeefbdfa710c9da3bdd92df31f08de7f53140d4b8e16e739459efc572da"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Normal Forms and Chronology Collapse for Periodic-Alphabet Full Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/85-periodic-alphabet-full-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/85-periodic-alphabet-full-shifts/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/85-periodic-alphabet-full-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/85-periodic-alphabet-full-shifts/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/85-periodic-alphabet-full-shifts/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $A_0,\ldots,A_{p-1}$ be nonempty finite alphabets and consider the two-sided full shift whose alphabet at time $k$ is prescribed periodically by $A_{k\bmod p}$, with all $p$ phases included so that one time step is an autonomous homeomorphism. Put $q_j=|A_j|$ and $Q=\prod_jq_j\geq2$. We give an explicit conjugacy to the constant-height-$p$ suspension of the full $Q$-shift. Thus the entire ordered size schedule $(q_0,\ldots,q_{p-1})$ collapses to the two invariants $(p,Q)$. In particular, two such systems are conjugate exactly when their periods and alphabet products agree. The normal form yields $$\#\operatorname{Fix}(T^n)=
   \begin{cases}pQ^{n/p},&p\mid n,\\0,&p\nmid n,\end{cases}
   \qquad
   \zeta_T(z)=\frac1{1-Qz^p},
   \qquad
   h_{\rm top}(T)=\frac1p\log Q.$$ The system has a unique maximal-entropy measure, is transitive of exact period $p$, and is mixing only for $p=1$. This provides a complete and constructive classification of the scheduled full-shift subclass, while separating it from the more general theory of periodic nonautonomous zeta functions.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 28 August 2026'
title: 'Normal Forms and Chronology Collapse for Periodic-Alphabet Full Shifts'
```

## Markdown 正文

# Introduction

Periodic nonautonomous systems are often made autonomous by adjoining a finite clock. Their entropy and periodic-orbit zeta functions have been studied in broad settings; Alves and Málek, for example, treat periodic nonautonomous piecewise-monotone interval maps and the relation between entropy and periodic growth [@AlvesMalek2013]. Finite-type shifts have the classical determinant zeta formula of Bowen and Lanford [@BowenLanford1970].

Here we solve a deliberately elementary but structurally revealing symbolic subclass. At phase $j$, an unconstrained symbol is chosen from $A_j$, and the phase advances by one. It is tempting to regard the ordered vector of alphabet sizes as dynamical data. It is not: a block code moves information between consecutive phases and collapses every schedule to a cyclic suspension of a full shift on $Q=\prod q_j$ symbols.

The contribution is an explicit normal form and the resulting if-and-only-if conjugacy classification, together with its orbit, entropy, and maximal-law corollaries. General clock extensions, nonautonomous entropy, and rational zeta mechanisms are owned background. No claim is made for schedules with additional transition constraints.

# The scheduled shift

Fix $p\geq1$ and pairwise disjoint nonempty finite alphabets $A_0,\ldots,A_{p-1}$. Indices on alphabets are read modulo $p$. For a phase $r\in\mathbb Z/p\mathbb Z$, set $$X_r=\prod_{k\in\mathbb Z}A_{r+k}.$$ The compact phase-lifted space is the disjoint union $$X(\mathbf A)=\bigsqcup_{r\in\mathbb Z/p\mathbb Z}X_r.$$ Define $T:X_r\to X_{r+1}$ by $$(Tx)_k=x_{k+1}.$$ This is a homeomorphism. It is also the vertex shift of a finite directed graph: every vertex in $A_j$ has an edge to every vertex in $A_{j+1}$. Write $$q_j=|A_j|,\qquad Q=\prod_{j=0}^{p-1}q_j.$$ We assume $Q\geq2$ to exclude the single finite orbit with no symbolic branching.

Let $B=A_0\times\cdots\times A_{p-1}$, so $|B|=Q$, and let $\Sigma_B=B^\mathbb Z$ be the full two-sided shift. Its height-$p$ cyclic suspension is $$S_{Q,p}:\Sigma_B\times\{0,\ldots,p-1\}\longrightarrow
 \Sigma_B\times\{0,\ldots,p-1\},$$ $$\label{eq:suspension}
 S_{Q,p}(y,r)=
 \begin{cases}
 (y,r+1),&0\leq r<p-1,\\
 (\sigma y,0),&r=p-1.
 \end{cases}$$

# Explicit normal form

For $x\in X_r$, align $p$-blocks with phase zero and define $$\label{eq:block-code}
 \bigl(\Phi_r(x)\bigr)_k
 =\bigl(x_{kp-r},x_{kp-r+1},\ldots,x_{kp-r+p-1}\bigr)\in B.$$ Set $\Phi(x)=(\Phi_r(x),r)$ on the clopen component $X_r$.

[\[thm:normal\]]{#thm:normal label="thm:normal"} The map $\Phi$ is a topological conjugacy $$\Phi:(X(\mathbf A),T)\longrightarrow
 (\Sigma_B\times\mathbb Z/p\mathbb Z,S_{Q,p}).$$ Consequently the conjugacy type is independent of the ordered factorization $Q=q_0q_1\cdots q_{p-1}$.

For each fixed $r$, [\[eq:block-code\]](#eq:block-code){reference-type="eqref" reference="eq:block-code"} partitions every coordinate of $x$ into one and only one consecutive $p$-block. It is therefore a bijection $X_r\to\Sigma_B$, and both it and its inverse are finite-window block maps. Since the components $X_r$ are clopen, their union $\Phi$ is a homeomorphism.

If $r<p-1$, shifting $x$ and realigning the block boundary leaves the $B$-sequence in [\[eq:block-code\]](#eq:block-code){reference-type="eqref" reference="eq:block-code"} unchanged and advances the phase. If $r=p-1$, the realigned block with index $k$ is the old block with index $k+1$, so the $B$-sequence is shifted once. Thus $\Phi T=S_{Q,p}\Phi$ by [\[eq:suspension\]](#eq:suspension){reference-type="eqref" reference="eq:suspension"}. Explicitly, if $(\Phi_r(x))_{k,t}$ denotes entry $t\in\{0,\ldots,p-1\}$ of block $k$, then for $r<p-1$, $$(\Phi_{r+1}(Tx))_{k,t}
 =(Tx)_{kp-(r+1)+t}=x_{kp-r+t}=(\Phi_r(x))_{k,t},$$ whereas at the wrap, $$(\Phi_0(Tx))_{k,t}
 =(Tx)_{kp+t}=x_{kp+t+1}=(\Phi_{p-1}(x))_{k+1,t}.$$ These identities also fix the direction of the shift in [\[eq:suspension\]](#eq:suspension){reference-type="eqref" reference="eq:suspension"}.

The normal form is constructive. Given two schedules with the same $p$ and $Q$, choose any bijection between their product alphabets and insert it between their two block codes. This produces a finite-window conjugacy even when their individual phase sizes differ, for example $(q_0,q_1)=(2,6)$ and $(3,4)$.

# Classification and dynamical invariants

The suspension has exactly $p$ cyclic components and its $p$th power is the full $Q$-shift on each component. This already gives the classification.

[\[thm:classification\]]{#thm:classification label="thm:classification"} Let $X(\mathbf A)$ and $X(\mathbf A')$ be scheduled full shifts with $Q,Q'\geq2$ and clock lengths $p,p'$. They are topologically conjugate if and only if $$p=p'\quad\text{and}\quad Q=Q'.$$

Sufficiency follows from [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"} and a bijection between product alphabets of the same size. Conversely, the exact topological period of the transitive suspension is $p$, so conjugacy gives $p=p'$. The entropy is $(1/p)\log Q$ because the $p$th power on a cyclic component is the full $Q$-shift. Entropy invariance then gives $Q=Q'$.

Because the phase alphabets are disjoint and every successive phase is forced, the graph has closed walks precisely at multiples of $p$ and has a closed walk of length $p$. Thus the displayed clock length is already the intrinsic period of the irreducible graph shift; no presentation-minimality assumption is needed.

[\[thm:invariants\]]{#thm:invariants label="thm:invariants"} For every $n\geq1$, $$\#\operatorname{Fix}(T^n)=
 \begin{cases}
 pQ^k,&n=pk,\\
 0,&p\nmid n.
 \end{cases}$$ Moreover, $$\zeta_T(z)
 =\exp\left(\sum_{n\geq1}\frac{\#\operatorname{Fix}(T^n)}n z^n\right)
 =\frac1{1-Qz^p},
 \qquad
 h_{\mathrm{top}}(T)=\frac1p\log Q.$$

If $p\nmid n$, $T^n$ changes the phase and has no fixed point. If $n=pk$, then on each of the $p$ components the normal form identifies $T^n$ with $\sigma^k$ on the full $Q$-shift, which has $Q^k$ fixed points. Hence $$\log\zeta_T(z)
 =\sum_{k\geq1}\frac{pQ^k}{pk}z^{pk}
 =\sum_{k\geq1}\frac{(Qz^p)^k}{k}
 =-\log(1-Qz^p).$$ The entropy statement was already obtained from the $p$th power.

Equivalently, the adjacency spectrum has the following exact form.

[\[prop:charpoly\]]{#prop:charpoly label="prop:charpoly"} Let $C_{\mathbf q}$ be the block-cyclic adjacency matrix with an all-one rectangular block from phase $j$ to phase $j+1$. Then $$\label{eq:charpoly}
 \det(\lambda I-C_{\mathbf q})
 =\lambda^{\sum_jq_j-p}(\lambda^p-Q).$$ Thus its nonzero spectrum depends only on $(p,Q)$.

Write $V_j=\mathbb C^{A_j}$ and decompose $V=\bigoplus_jV_j=E\oplus W$, where $E$ is spanned by the phase-indicator vectors $e_j$ and $W=\bigoplus_jW_j$, with $W_j\subset V_j$ the subspace of vectors whose coordinates sum to zero. The all-one blocks annihilate $W$, so $C_{\mathbf q}|_W=0$ and $\dim W=\sum_jq_j-p$.

The subspace $E$ is invariant and, with indices modulo $p$, $$C_{\mathbf q}e_{j+1}=q_{j+1}e_j.$$ Hence $(C_{\mathbf q}|_E)^p=QI_E$. The vector $e_0$ is cyclic for this weighted cyclic shift because every $q_j$ is nonzero, so its minimal polynomial has degree $p$. It is therefore $\lambda^p-Q$, which, on the $p$-dimensional space $E$, is also the characteristic polynomial. Taking the product with the zero action on $W$ proves [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}.

# The maximal law and failure of mixing

Let $\nu_Q$ be the uniform Bernoulli measure on $B^\mathbb Z$ and let $u_p$ be the uniform measure on the clock. Transporting $\nu_Q\times u_p$ through $\Phi^{-1}$ yields the law that first chooses a uniform phase and then chooses every coordinate independently and uniformly from its scheduled alphabet.

[\[prop:mme\]]{#prop:mme label="prop:mme"} The measure above is the unique invariant probability measure of maximal entropy. The system is transitive and ergodic under this measure. It is mixing if and only if $p=1$. For $p>1$, the clock supplies every $p$th root of unity as a Koopman eigenvalue, while $T^p$ is Bernoulli on each of its $p$ components.

The presentation is an irreducible finite-type shift, so the Parry measure is unique; in the normal form it is exactly $\nu_Q\times u_p$. Transitivity and ergodicity follow from the cyclic suspension. If $p>1$, a nonconstant character of the clock is an eigenfunction of modulus one, preventing mixing. The remaining assertions are immediate from $S_{Q,p}^p(y,r)=(\sigma y,r)$.

# Controls and ownership boundary

The accompanying exact control builds the block-cyclic zero-one matrix for many schedules, compares direct traces with [\[thm:invariants\]](#thm:invariants){reference-type="ref" reference="thm:invariants"}, verifies [\[prop:charpoly\]](#prop:charpoly){reference-type="ref" reference="prop:charpoly"}, checks the coordinate alignment in the block code, and checks that all schedules in the same $(p,Q)$ class share the same periodic ledger. The explicit block code in [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"}, not finite enumeration, proves the conjugacy statement.

Periodic nonautonomous entropy and zeta functions are established subjects [@AlvesMalek2013]. The finite-type determinant mechanism is owned by Bowen and Lanford [@BowenLanford1970]. The residual statement here is the explicit normal form and complete classification for unconstrained periodic alphabet schedules. We make no result for constrained rectangular transition matrices, no priority claim, and no connection to arithmetic zeta functions.
