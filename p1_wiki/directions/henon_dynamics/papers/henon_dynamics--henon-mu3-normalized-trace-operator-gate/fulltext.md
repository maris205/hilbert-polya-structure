---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-normalized-trace-operator-gate"
canonical_tex: "henon_dynamics/henon_mu3_normalized_trace_operator_gate/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_normalized_trace_operator_gate/paper/main.pdf"
source_sha256: "4030d3c1e445a6dca221d3e508cc553adf50e8fd47832a23ff3985ad04804435"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Fourth-Order Regularized Graded Determinant for a Hénon Euler Germ

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_normalized_trace_operator_gate>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_normalized_trace_operator_gate/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_normalized_trace_operator_gate/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_normalized_trace_operator_gate/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_normalized_trace_operator_gate/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an operator realization of the field-degree-normalized Hénon Euler germ previously shown to converge on $\operatorname{Re}s>1/2$. At each split prime we assemble all Galois-conjugate $\mu_3$ sectors in a graded finite algebra with field-degree-normalized positive trace and associated supertrace. The global prime block $X_s$ satisfies the sharp criterion $X_s\in L^q$ if and only if $q\operatorname{Re}s>2$. It is not $\tau$-trace class near the Riemann critical abscissa, but it lies in $L^4(\mathcal M,\tau)$ throughout the proved half-plane. We show exactly that the Hénon germ equals a fourth-order regularized graded determinant multiplied by three explicit local chronological counterterm series. Order four is minimal for this positive-ideal realization. A positive Fuglede--Kadison determinant retains only modulus and cannot replace the analytic superdeterminant. This upgrades the germ to a genuine regularized operator determinant while leaving continuation, a functional equation, and a self-adjoint generator open.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: 13 August 2026
title: 'A Fourth-Order Regularized Graded Determinant for a Hénon Euler Germ'
```

## Markdown 正文

# Introduction

The normalized Galois root of the full finite-field Hénon kernel has two apparently conflicting properties. Its prime product is canonical and holomorphic on $\operatorname{Re}s>1/2$, yet its first local factor has exact fractional divisor orders. Ordinary finite-dimensional determinants cannot have such orders. Finite and semifinite algebras, by contrast, carry traces that assign fractional dimensions to projections [@FugledeKadison1952; @DeLaHarpe2013; @HochsKaadSchemaitat2018].

We show that this is the correct operator category, with an important qualification: the relevant analytic object is a graded fourth-order regularized determinant, not a positive Fuglede--Kadison determinant.

[\[thm:main\]]{#thm:main label="thm:main"} There is a canonical graded semifinite block operator $X_s$ such that $$X_s\in L^q\quad\Longleftrightarrow\quad q\operatorname{Re}s>2
 \qquad(q>0).$$ On $\operatorname{Re}s>1/2$, the normalized Hénon Euler germ satisfies $$\mathcal G(s)=
 \exp\!\left(-\ell_1(s)-\frac{\ell_2(s)}2-\frac{\ell_3(s)}3\right)
 \operatorname{Det}_{4,\tau,\mathrm{gr}}(I-X_s),$$ where the three counterterms are the convergent Dirichlet series of the first three exact local chronological supertraces. Order four is the least fixed integer Schatten order valid on the entire half-plane.

The theorem resolves the operator-category gate positively without hiding the cost. $X_s$ is $\tau$-trace class only on $\operatorname{Re}s>2$; cancellation in a supertrace never improves positive trace-norm summability. This is not a classical Hilbert-space Fredholm determinant. Near $\operatorname{Re}s=1/2$, the head counterterms and the fourth-order determinant are both essential.

# The graded Galois-sector algebra

Fix a split prime $p$ and write $$d=(p-1)/2,\qquad d_0=(p+2)/3,\qquad d_1=d_2=(p-1)/3.$$ For $[a]\in\mathbf F_p^\times/\{\pm1\}$, let $\mathcal H_{a,k}$ be the sector space on which the two-step unitary Hénon operator $T_{a,k}$ acts. Define the graded spaces $$\begin{aligned}
 \mathcal H_{p,[a]}^+
 &=\mathcal H_{a,0}^{\oplus2}\oplus\mathcal H_{-a,0}^{\oplus2},\\
 \mathcal H_{p,[a]}^-
 &=\mathcal H_{a,1}\oplus\mathcal H_{a,2}
   \oplus\mathcal H_{-a,1}\oplus\mathcal H_{-a,2},\end{aligned}$$ and let $W_{p,[a]}^\pm$ be the corresponding direct sums of the $T_{a,k}$, with two copies in the positive grade. Since both $a$ and $-a$ occur, the construction is independent of the representative of $[a]$. Set $$\mathcal H_p^\pm=\bigoplus_{[a]}\mathcal H_{p,[a]}^\pm,
 \qquad
 W_p^\pm=\bigoplus_{[a]}W_{p,[a]}^\pm,
 \qquad W_p=W_p^+\oplus W_p^-.$$ Then $W_p$ is unitary. Put $$\mathcal M_p=B(\mathcal H_p^+)\oplus B(\mathcal H_p^-),
 \qquad \Gamma_p=I\oplus-I.$$ The positive field-degree-normalized trace and signed supertrace are $$\tau_p(A_+\oplus A_-)=d^{-1}(\operatorname{Tr}A_++\operatorname{Tr}A_-),
 \qquad
 \operatorname{Str}_p(A)=\tau_p(\Gamma_pA).$$ The trace is faithful and positive, but it is not a tracial state because $\tau_p(I)$ grows with $p$. Direct dimension counting gives $$\label{eq:dimension}
 \tau_p(I)=4(d_0+d_1)=\frac{8p+4}{3}.$$

[\[prop:moment\]]{#prop:moment label="prop:moment"} For every $n\ge1$, $$\operatorname{Str}_p(W_p^n)=c_{p,n},$$ where $c_{p,n}$ is the field-degree-normalized chronological moment from the Galois norm construction. Hence, for $|z|<1$, $$G_p(z)=\exp\operatorname{Str}_p\operatorname{Log}_0(I-zW_p).$$

The proof is the block expansion in [7](#sec:traceproof){reference-type="ref" reference="sec:traceproof"}. The positive trace controls ideals; the supertrace encodes the virtual augmentation. These two roles must not be interchanged.

# Sharp Schatten thresholds

Form the product algebra $$\mathcal M=\prod_{p\equiv1\ (3)}\mathcal M_p,$$ represented on $\mathcal H=\bigoplus_p(\mathcal H_p^+\oplus\mathcal H_p^-)$. On positive elements $A=(A_p)_p$, set $\tau(A)=\sum_p\tau_p(A_p)$; this is a faithful normal semifinite trace. Form the block Dirichlet family $$X_s=\bigoplus_{p\equiv1\ (3)}p^{-s}W_p,
 \qquad \Gamma=\bigoplus_p\Gamma_p.$$ Because $W_p$ is unitary, $|p^{-s}W_p|=p^{-\operatorname{Re}s}I$. Therefore $$\label{eq:lq}
 \tau(|X_s|^q)
 =\sum_{p\equiv1\ (3)}\frac{8p+4}{3}p^{-q\operatorname{Re}s}.$$ For every $q>0$, the prime series in [\[eq:lq\]](#eq:lq){reference-type="eqref" reference="eq:lq"} converges exactly when $q\operatorname{Re}s>2$; at equality it contains the divergent prime harmonic series. More explicitly, convergence for $q\operatorname{Re}s>2$ follows by comparison with the integer series of exponent $q\operatorname{Re}s-1>1$. In the other direction the summand dominates a constant multiple of $1/p$, and the Euler--Dirichlet theorem gives $\sum_{p\equiv1\ (3)}p^{-1}=\infty$.

Thus $$\begin{array}{c|c}
\toprule
\text{ideal}&\text{exact domain}\\
\midrule
L^1&\operatorname{Re}s>2\\
L^2&\operatorname{Re}s>1\\
L^3&\operatorname{Re}s>2/3\\
L^4&\operatorname{Re}s>1/2\\
\bottomrule
\end{array}$$ As a bounded operator on $\mathcal H$, $X_s$ is compact exactly when $\operatorname{Re}s>0$; it is bounded and noncompact at $\operatorname{Re}s=0$, and unbounded for $\operatorname{Re}s<0$. Since $|\Gamma X_s|=|X_s|$, the grading cannot improve any positive ideal threshold. This excludes an unregularized $\tau$-determinant on most of the C45 half-plane.

The canonical Hilbert-space trace gives a different threshold. Since $$\dim(\mathcal H_p^+\oplus\mathcal H_p^-)
 =d\,\tau_p(I)=\frac{(p-1)(4p+2)}3,$$ one has $$\operatorname{Tr}_{\mathcal H}(|X_s|^q)
 =\sum_p\frac{(p-1)(4p+2)}3p^{-q\operatorname{Re}s},
 \qquad X_s\in S^q(\mathcal H)\Longleftrightarrow q\operatorname{Re}s>3.$$ Thus standard Hilbert trace class begins only at $\operatorname{Re}s>3$, and its graded moments are $C_{p,n}=d_pc_{p,n}$: they encode the ordinary Galois norm, not the field-degree-normalized root.

# The fourth-order determinant

For a graded $X=X^+\oplus X^-$ in $L^4$ with $\|X\|<1$, define the two trace-associated regularized determinants $$\operatorname{Det}_{4,\tau_\pm}(I-X^\pm)
 =\exp\!\left(-\sum_{n\ge4}
       \frac{\tau_\pm((X^\pm)^n)}n\right)$$ and their graded ratio $$\operatorname{Det}_{4,\tau,\mathrm{gr}}(I-X)
 =\frac{\operatorname{Det}_{4,\tau_+}(I-X^+)}
        {\operatorname{Det}_{4,\tau_-}(I-X^-)}
 =\exp\!\left(-\sum_{n\ge4}\frac{\operatorname{Str}(X^n)}n\right).$$ Here the global supertrace is applied only to trace-class powers. Hölder's inequality puts $X^4$ in $L^1$, and for $n\ge4$, $$|\operatorname{Str}(X^n)|\le\tau(|X|^n)
 \le\|X\|^{n-4}\tau(|X|^4).$$ For $X=X_s$ on a compact subset of $\operatorname{Re}s>1/2$, both $\|X_s\|<1$ and $\tau(|X_s|^4)$ are uniformly controlled. Thus the defining series is locally normally convergent and the determinant is holomorphic and nonzero. This is the fourth-order trace-ideal regularization specialized to the graded semifinite trace setting [@Simon2005].

For $n=1,2,3$, put $$\ell_n(s)=\sum_pc_{p,n}p^{-ns}.$$ The exact first moment gives convergence of $\ell_1$ on $\operatorname{Re}s>0$. The uniform Hénon moment bounds give convergence of $\ell_2$ on $\operatorname{Re}s>1/2$ and $\ell_3$ on $\operatorname{Re}s>1/3$. Hence all three are holomorphic in the fourth-order half-plane.

These are sums of finite-dimensional *local* supertraces. When $X_s^n\notin L^1$, the notation $\ell_n(s)$ is not an application of the global semifinite trace to $X_s^n$; the cancellation has already occurred inside each prime block. This is precisely why the three counterterms must remain explicit.

Expanding the canonical local logarithms and separating repetitions below four proves the equality in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The counterterms are not fitted: they are the exact first three local chronological-supertrace series. Since $L^3$ only holds for $\operatorname{Re}s>2/3$, no regularized determinant of fixed integer order at most three covers the entire half-plane by positive Schatten membership.

Finally, all $c_{p,n}$ are rational. Normal convergence therefore gives $\mathcal G(\overline s)=\overline{\mathcal G(s)}$ on the proved half-plane. The displayed counterterm exponential is holomorphic and nowhere zero there, so it introduces no hidden divisor.

# Three determinant notions

On $\operatorname{Re}s>2$, $X_s$ is $\tau$-trace class. The $\tau$-trace-associated analytic determinants in the two grades exist, and their ratio has logarithm $$-\sum_{n\ge1}\operatorname{Str}(X_s^n)/n=\log\mathcal G(s).$$ This is the unregularized region for the normalized semifinite trace, not the classical Fredholm region. The latter starts at $\operatorname{Re}s>3$ for the same Hilbert blocks and gives the unnormalized Galois norm.

On $\operatorname{Re}s>1/2$, the fourth-order regularized graded determinant is the appropriate analytic object. It retains complex phase through the supertrace and requires the three disclosed counterterms.

Where a positive Fuglede--Kadison determinant, or its semifinite relative version on $I+L^1$, is defined, it uses $\tau(\log|A|)$ and is positive [@FugledeKadison1952; @DeLaHarpe2013; @HochsKaadSchemaitat2018]. On the ordinary domain, the ratio in the two grades can encode $\operatorname{Re}\log\mathcal G=\log|\mathcal G|$, but not the analytic phase. On the $L^4$ domain one would first need a fourth-order positive regularization. Neither positive object replaces the analytic determinant in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. This distinction also prevents signed cancellation from being misreported as positive trace-class summability.

# Route-A conclusion

The normalized Hénon germ now has a reproducible operator algebra, exact trace identity, and canonical regularized determinant on its full proved half-plane. This substantially strengthens the dynamical-zeta layer. The primes remain arithmetic fibers, and the analytic-structure layer still lacks continuation, a Gamma factor, a functional equation, and a Riemann divisor. The quantization remains intrinsic but is not a self-adjoint Hilbert--Pólya operator.

The strict tuple is $$\begin{aligned}
 \mathrm{A1}&=\mathrm{WEAK},
 &\mathrm{A2}&=\mathrm{ANALYTIC\_DETERMINANT},\\
 \mathrm{A3}&=\mathrm{PARTIAL\_ANALYTIC\_STRUCTURE},
 &\mathrm{A4}&=\mathrm{NATURAL\_QUANTIZATION}.\end{aligned}$$ Overall: `ROUTE_A_EXPLORATORY`, with scoped descriptor `REGULARIZED_GRADED_DETERMINANT`. Route B is not authorized.

The next large step is to improve the low counterterms rather than increase a finite matrix cutoff. The second chronological trace admits a projective geometric interpretation as a genus-four curve count. Its Weil bound may supply enough extra prime decay to continue the Euler germ to $\operatorname{Re}s>1/3$. It cannot, however, put the present block in $L^3$ there: the threshold $q\operatorname{Re}s>2$ would require a sixth-order determinant on the full new half-plane, with five explicit counterterms. A lower determinant order would require a genuinely different compressed operator.

# Trace expansion {#sec:traceproof}

For one real Galois class $[a]$, the signed trace of the $n$th power is $$\begin{aligned}
&2\operatorname{Tr}T_{a,0}^n+2\operatorname{Tr}T_{-a,0}^n\\
&\quad-\operatorname{Tr}T_{a,1}^n-\operatorname{Tr}T_{a,2}^n
      -\operatorname{Tr}T_{-a,1}^n-\operatorname{Tr}T_{-a,2}^n.\end{aligned}$$ This is exactly the sum of the augmentation moment for $\psi_a$ and its inverse character. Summing over all $[a]$ takes the field trace from $\mathbf Q(\zeta_p)^+$ to $\mathbf Q$. Dividing by $d=(p-1)/2$ gives $c_{p,n}$, proving [\[prop:moment\]](#prop:moment){reference-type="ref" reference="prop:moment"}.
