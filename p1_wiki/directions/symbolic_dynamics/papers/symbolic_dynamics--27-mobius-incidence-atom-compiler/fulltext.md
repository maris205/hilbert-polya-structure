---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--27-mobius-incidence-atom-compiler"
canonical_tex: "symbolic_dynamics/papers/27-mobius-incidence-atom-compiler/main.tex"
canonical_pdf: "symbolic_dynamics/papers/27-mobius-incidence-atom-compiler/main.pdf"
source_sha256: "50189808940af036eaba3041bd4dd6081bc5c7b6010e9bc438e25c4e2aa663d8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Möbius-Compiled Atom Loops in Integer Symbolic Dynamics: Exact Necklace Selection and Oblique-Projector Collapse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/27-mobius-incidence-atom-compiler>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/27-mobius-incidence-atom-compiler/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/27-mobius-incidence-atom-compiler/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/27-mobius-incidence-atom-compiler/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/27-mobius-incidence-atom-compiler/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An arithmetic symbolic system should identify its primitive orbit labels from its own grammar, rather than receive the desired atoms as a projector table. We implement that requirement for the integer divisibility poset. Covers of $1$ are exactly its source atoms, and incidence conjugation $q_n=\zeta\varepsilon_n\mu$ compiles every source coordinate into an oblique primitive idempotent. Filtering the uniform family by the cover predicate yields a wordwise cyclic selector: a nonempty word has trace one exactly when it is a temporal repetition of one source atom; mixed words and composite source letters vanish. The original Elias-gamma marker appears as $u^{r\ell(p)}$ at repetition $r$. We prove a complementary collapse theorem. Every finite complete lift is unitriangularly conjugate to the coordinate projectors, while on an explicit weighted Hilbert space the countable family is boundedly similar to them for $\eta>1$. Individual atom idempotents are rank-one trace class already for $\eta>1/2$, with an exact trace-norm formula. The marked transfer and both inherited holomorphic de Rham degrees are trace class on a proved common domain, and their graded Fredholm ratio is the atom Euler product. At $u=1$, its eigenvalues impose the sharp barrier $\operatorname{Re}s>1$. Thus source-derived atom selection passes the analytic orbit gate, but ordinary cyclic observables still reduce to atom blocks; continuation and a critical-line mechanism remain absent, so Route A is rejected.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Möbius-Compiled Atom Loops in Integer Symbolic Dynamics:\
  Exact Necklace Selection and Oblique-Projector Collapse
```

## Markdown 正文

# Introduction {#sec:introduction}

There are two very different ways to obtain an Euler product from symbolic loops. One may first specify the desired labels, allocate one invariant line to each label, and then read the product from their diagonal weights. Or one may begin with a fixed symbolic grammar and demand that the grammar identify its own primitive labels before any cyclic trace is formed. The first method is exact but inventory dependent. The second is the structural requirement needed by the present exploratory program.

The distinction becomes sharp for integer labels. A table indexed by rational primes already contains the desired arithmetic selection. By contrast, the locally finite poset $$P=(\mathbb N_{\ge1},\mid)$$ contains only objects and the divisibility relation. Its atoms are the covers of $1$. Their identification with rational primes is a theorem of the fixed factorization grammar, not a separately supplied mask. The first question of this paper is whether that intrinsic predicate can be promoted to an exact cyclic selector that acts before trace, respects every temporal repetition, and keeps the duration of the underlying binary code.

The answer is yes. Let $\zeta$ be the incidence zeta element, $\mu=\zeta^{-1}$, and $\varepsilon_n$ the uniform diagonal coordinate at the source object $n$. The formula $$q_n=\zeta\varepsilon_n\mu
\label{eq:intro-compiler}$$ produces a complete family of primitive idempotents. It is important that [\[eq:intro-compiler\]](#eq:intro-compiler){reference-type="eqref" reference="eq:intro-compiler"} is defined for *every* source integer. Only after the uniform compilation do we apply the cover predicate. The resulting letter actions annihilate every mixed word and every composite source letter, while a temporal repetition of one source atom has trace one at every order.

This positive result resolves a recurring orbit-level problem. Scalar Möbius inversion can extract aggregate arithmetic coefficients, but it does not by itself distinguish a composite source letter from a repetition of an atom loop. Here the two objects are separated before cyclic trace. If $p$ is an atom, the word $p,p,\ldots,p$ survives; the single source label $p^r$ is composite and dies. The return marker $z$ counts completed codewords, while the independent marker $u$ records original binary digit steps. Consequently the $r$-fold traversal carries $$u^{r\ell(p)}p^{-rs},
\qquad
\ell(p)=2\lfloor\log_2p\rfloor+1,$$ and not a duration that has been silently reset at induction.

The same algebra that makes the selector exact also proves its limitation. At a finite cutoff, $$q_n=\zeta\varepsilon_n\zeta^{-1}.
\label{eq:intro-similarity}$$ More generally, every complete primitive lift with the same diagonal labels is conjugate to the coordinate family by a unit in the nilpotent radical. Thus incidence geometry changes the basis but not any ordinary power trace or determinant. We call this the *oblique-projector collapse*.

The countable realization makes both sides of the conclusion analytic. On the weighted Hilbert space $$H_\eta=\left\{x:\sum_{n\ge1}n^{2\eta}|x_n|^2<\infty\right\},$$ each source-atom $q_p$ is a rank-one trace-class idempotent for $\eta>\tfrac 12$. We compute its trace norm exactly and obtain a bound uniform in $p$. For $\eta>1$, the countable zeta and Möbius transforms themselves are bounded inverses, so the full compiled family is boundedly similar to the coordinate projectors. No such global claim is needed, or made, in the remaining interval $\tfrac 12<\eta\le1$.

With the source-fixed Elias gamma code [@elias1975universal], define $$T_\eta(s,u)=\sum_{p\in\operatorname{At}(P)}
u^{\ell(p)}p^{-s}q_p.$$ This family converges in trace norm whenever $$\sum_p|u|^{\ell(p)}p^{-\Re s}<\infty.$$ Every power trace is the expected atom sum and the Fredholm determinant is the atom product. Tensoring with the inherited holomorphic zero- and one-form sectors removes the local affine fixed-point denominator. Both degrees remain honest trace-class operators on one common domain; the final object is their graded determinant ratio, not an ordinary determinant of an ungraded direct sum.

At $u=1$, the construction has a sharp analytic stop. The vectors $e_1+e_p$ are eigenvectors with eigenvalues $p^{-s}$. Absolute summability of eigenvalues is necessary for trace class, so the operator cannot cross $\Re s=1$. A scalar continuation of the familiar product does not continue this operator family. Nor does ordinary incidence conjugacy produce a divisor-moving spectral law or a critical-line carrier.

#### Contributions.

The paper makes five scoped contributions.

1.  It gives a source-internal atom predicate and a uniform incidence compiler, with no prime/color inventory, prime mask, prime-power table, or target spectrum.

2.  It proves exact wordwise and necklace-resolved selection at every repetition, with the binary digit marker retained.

3.  It classifies the finite compiler up to radical conjugacy and proves determinant collapse, including scalar-Möbius and no-filter no-gos.

4.  It constructs an honest countable weighted realization, proves the exact rank-one trace norm, and establishes bounded global similarity for $\eta>1$.

5.  It couples the selector to the holomorphic de Rham sector, proves the full graded Fredholm product on a trace-class domain, and proves the sharp $u=1$ barrier.

The strict result is therefore positive at the orbit gate and negative overall: $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
\ \texttt{A1\_PASS\_ANALYTIC},\\
&\texttt{A2\_ANALYTIC\_DETERMINANT},
\ \texttt{A3\_FAIL},\ \texttt{A4\_FAIL}).
\end{split}$$ Route A is rejected and Route B remains locked. The purpose of the paper is not to disguise that rejection. It is to isolate exactly what an endogenous incidence selector can accomplish, and exactly which obstruction remains after it succeeds.

# Frozen source and literature boundary {#sec:source-literature}

## The arithmetic symbolic source

All new structure is derived from the countable locally finite poset $$P=(\mathbb N_{\ge1},\mid).$$ Its finite models are the divisibility downsets $P_N=\{1,\ldots,N\}$. Every interval is finite, so incidence convolution is algebraically well-defined without a summability convention.

Write $\delta$ for the incidence identity and $\bar\zeta=\zeta-\delta$. The atom predicate is $$\operatorname{At}(P)
=\{n>1:(1,n)=\varnothing\}
=\{n>1:(\bar\zeta*\bar\zeta)(1,n)=0\}.
\label{eq:atom-predicate}$$ The second expression is intrinsic: $(\bar\zeta*\bar\zeta)(1,n)$ counts strict intermediate divisors. An integer $n>1$ has no such divisor exactly when it is prime, and hence $$\operatorname{At}(P)=\mathbb P.
\label{eq:atoms-primes}$$ Equation [\[eq:atoms-primes\]](#eq:atoms-primes){reference-type="eqref" reference="eq:atoms-primes"} is a consequence of the source relation. A modified relation may have different covers; the construction must follow them.

The symbolic time convention is inherited from the prefix-coded affine renewal system. For the Elias gamma length $$\ell(n)=2\lfloor\log_2n\rfloor+1,
\label{eq:gamma-length}$$ the marked return weight is $$a_n(s,u)=u^{\ell(n)}n^{-s}.
\label{eq:marked-weight}$$ The variable $z$ counts completed returns, whereas $u$ counts original digit steps. These markers have different ownership and are never merged.

## What is classical

Incidence algebras, their zeta elements, and Möbius inversion are foundational material due to @rota1964foundations. Möbius-generated idempotent decompositions occur classically in Burnside and Möbius algebras [@solomon1967burnside; @greene1973mobius]. The structure and automorphisms of incidence algebras, including the role of primitive systems and inner conjugacy, are established background [@stanley1970incidence; @baclawski1972automorphisms]. Semigroup representation theory supplies further direct precedents for Möbius decomposition and character formulas [@steinberg2006mobius; @steinberg2008mobius], while incidence Hopf algebras provide broader primitive-structure prior art [@schmitt1994incidence].

Scalar extraction of prime series by Möbius inversion is also classical [@froberg1968prime]. Möbius and primitive-necklace structures meet in the Witt-vector theory of @metropolis1983witt. Therefore neither *Möbius idempotents*, *Möbius extraction of primes*, nor a generic *Möbius/necklace correspondence* is a safe novelty claim.

The analytic machinery is likewise established. Dynamical zeta functions and transfer operators go back to @ruelle1976zeta; countable-state thermodynamic formalism is developed by @sarig1999thermodynamic; holomorphic trace-ideal estimates are represented by @bandtlow2008eigenvalue; and the determinant identities used below are standard trace-class theory [@simon1977determinants].

L38mm L39mm Y ingredient & primary boundary & safe use here\
incidence zeta and Möbius inversion & Rota (1964) & fixed source algebra; no novelty claim\
primitive/idempotent decompositions & Solomon (1967), Greene (1973), Stanley (1970) & exact cyclic coupling and collapse application\
inner/character structure & Baclawski (1972), Steinberg (2006, 2008) & elementary finite conjugacy theorem with labels fixed\
scalar prime extraction & Fröberg (1968) & contrast with wordwise pre-trace selection\
necklace Möbius theory & Metropolis--Rota (1983) & source atoms label loops; period alone does not\
trace-class transfer determinants & Ruelle (1976), Simon (1977), Bandtlow--Jenkinson (2008) & marker-preserving countable realization and domain audit\

## Novelty-safe claim

The project-specific synthesis has five linked parts: covers of the integer divisibility grammar derive the atom labels; a uniform incidence conjugation compiles them into wordwise selectors; a weighted countable model gives an exact trace norm; finite and countable similarity results prove collapse; and the selector couples to the inherited gamma-coded holomorphic de Rham complex without losing the digit marker. The closed primary-source audit found no exact collision with that complete package. This is a scoped literature finding, not an absolute priority assertion.

The boundary also dictates the rhetoric. The paper does not offer a new representation of $1/\zeta$ in isolation. It offers a source-derived orbit selector and then proves that its ordinary determinant contains no more semisimple information than a coordinate atom product.

# The incidence atom compiler {#sec:compiler}

Let $I(P;\mathbb C)$ denote the locally finite incidence algebra. Its product is $$(f*g)(a,b)=\sum_{a\mid c\mid b}f(a,c)g(c,b).
\label{eq:incidence-product}$$ The zeta and Möbius elements are $$\zeta(a,b)=\mathbf 1_{\{a\mid b\}},
\qquad
\mu=\zeta^{-1},
\qquad
\mu(a,b)=\mu_{\mathrm{arith}}(b/a).
\label{eq:zeta-mobius}$$ For every source object $n$, including composites, introduce the uniform coordinate idempotent $$\varepsilon_n(a,b)=\mathbf 1_{\{a=b=n\}}.
\label{eq:coordinate-idempotent}$$

[\[def:compiler\]]{#def:compiler label="def:compiler"} The compiled source coordinate is $$q_n=\zeta*\varepsilon_n*\mu.
\label{eq:compiler}$$

No factorization or primality test is used in [\[def:compiler\]](#def:compiler){reference-type="ref" reference="def:compiler"}. Directly expanding the two convolutions gives $$q_n(a,b)
=\mathbf 1_{\{a\mid n\mid b\}}\mu_{\mathrm{arith}}(b/n).
\label{eq:kernel}$$ This formula will later yield the countable rank-one representation.

[\[thm:primitive-system\]]{#thm:primitive-system label="thm:primitive-system"} For every finite cutoff $P_N$, and intervalwise in the countable incidence algebra, $$q_nq_m=\delta_{nm}q_n,
\qquad
\sum_n q_n=\delta.
\label{eq:complete-idempotents}$$ Each $q_n$ is primitive.

Using $\mu\zeta=\delta$, $$q_nq_m
=\zeta\varepsilon_n\mu\zeta\varepsilon_m\mu
=\zeta\varepsilon_n\varepsilon_m\mu
=\delta_{nm}q_n.$$ At finite cutoff, $\sum_n \varepsilon_n=\delta$, whence $$\sum_n q_n
=\zeta\left(\sum_n \varepsilon_n\right)\mu
=\zeta\delta\mu=\delta.$$ The countable sum has only finitely many contributions on every interval. Each $\varepsilon_n$ is primitive in the finite incidence algebra and conjugation by the unit $\zeta$ preserves primitivity. The countable claim is the compatible intervalwise statement.

The compiler itself does not select primes: it produces one idempotent for every integer. Selection enters through the fixed source predicate.

[\[def:letter-action\]]{#def:letter-action label="def:letter-action"} For a positive-integer return letter $n$, define $$A_n=\mathbf 1_{\operatorname{At}(P)}(n)q_n,
\label{eq:letter-action}$$ where membership in $\operatorname{At}(P)$ is evaluated by [\[eq:atom-predicate\]](#eq:atom-predicate){reference-type="eqref" reference="eq:atom-predicate"}.

[\[thm:word-selector\]]{#thm:word-selector label="thm:word-selector"} For every nonempty word $w=n_1\cdots n_r$, $$\operatorname{Tr}(A_{n_1}\cdots A_{n_r})
=
\begin{cases}
1,&n_1=\cdots=n_r=p\in\operatorname{At}(P),\\
0,&\text{otherwise}.
\end{cases}
\label{eq:word-selector}$$ The coefficient is invariant under cyclic rotation. The selected primitive cyclic classes are precisely the one-letter source-atom loops, and their $r$-fold temporal repetitions have weight $$u^{r\ell(p)}p^{-rs}
\label{eq:repetition-weight}$$ with multiplicity one.

If a letter is not an atom, its action is zero. If all letters are atoms but two differ, [\[thm:primitive-system\]](#thm:primitive-system){reference-type="ref" reference="thm:primitive-system"} makes the product zero. A monochromatic atom word equals $q_p^r=q_p$. At a finite cutoff $q_p$ is similar to the rank-one coordinate idempotent and has trace one. The countable trace-one statement is proved directly in [\[thm:rank-one\]](#thm:rank-one){reference-type="ref" reference="thm:rank-one"}. Cyclic invariance follows either from the trace or directly from the dichotomy.

[\[rem:source-time\]]{#rem:source-time label="rem:source-time"} The single source letter $p^r$ is a composite integer and is killed by [\[eq:letter-action\]](#eq:letter-action){reference-type="eqref" reference="eq:letter-action"}. The word with $r$ copies of $p$ is the temporal repetition of the primitive loop and survives. The exponent in [\[eq:repetition-weight\]](#eq:repetition-weight){reference-type="eqref" reference="eq:repetition-weight"} records both distinctions: $p^{-rs}$ comes from $r$ traversals, and $u^{r\ell(p)}$ records all underlying digit steps.

This is the analytic A1 advance. It is stronger than an equality obtained only after commuting letter variables or aggregating endpoints: mixed and composite-letter products vanish before the cyclic trace is taken.

# Finite similarity and the oblique-projector no-go {#sec:similarity}

Let $J_N\subset I(P_N;\mathbb C)$ be the ideal of incidence functions with zero diagonal. It is nilpotent, and $$I(P_N;\mathbb C)/J_N\cong\mathbb C^{P_N}.
\label{eq:incidence-semisimple}$$ The quotient records the coordinate characters. Off-diagonal incidence data live in the radical.

[\[thm:finite-conjugacy\]]{#thm:finite-conjugacy label="thm:finite-conjugacy"} Let $\{e_x:x\in P_N\}$ and $\{f_x:x\in P_N\}$ be complete orthogonal primitive-idempotent families satisfying $$f_x\equiv e_x\pmod{J_N}$$ for every $x$. Then there is a unit $v\in1+J_N$ such that $$f_x=ve_xv^{-1}\qquad(x\in P_N).
\label{eq:lift-conjugacy}$$

Set $$v=\sum_x f_xe_x.$$ Modulo $J_N$, one has $$v\equiv\sum_x e_x=1.$$ Thus $v$ is invertible because $J_N$ is nilpotent. Orthogonality and completeness give $$f_xv=f_xe_x=ve_x.$$ Right multiplication by $v^{-1}$ proves [\[eq:lift-conjugacy\]](#eq:lift-conjugacy){reference-type="eqref" reference="eq:lift-conjugacy"}.

For the canonical family, the conclusion is visible without classification: $$q_n=\zeta\varepsilon_n\zeta^{-1}.
\label{eq:canonical-conjugacy}$$ Because $\zeta-\delta\in J_N$, this is exactly a unitriangular change of basis. If labels are retained, [\[thm:finite-conjugacy\]](#thm:finite-conjugacy){reference-type="ref" reference="thm:finite-conjugacy"} exhausts the freedom in a complete lift. If labels are forgotten, a compatible relabeling may additionally permute the coordinate characters.

[\[cor:finite-determinant\]]{#cor:finite-determinant label="cor:finite-determinant"} For arbitrary scalars $b_n$ and every $r\ge1$, $$\operatorname{Tr}\left(\sum_n b_nq_n\right)^r=\sum_n b_n^r,
\label{eq:finite-power-trace}$$ and $$\det\left(I-z\sum_n b_nq_n\right)=\prod_n(1-zb_n).
\label{eq:finite-determinant}$$

Either use pair annihilation and $\operatorname{Tr}q_n=1$, or conjugate the operator to $\sum_n b_n\varepsilon_n$ using [\[eq:canonical-conjugacy\]](#eq:canonical-conjugacy){reference-type="eqref" reference="eq:canonical-conjugacy"}.

## Why scalar Möbius inversion is not the selector

The two uses of Möbius structure must not be conflated. In [\[eq:compiler\]](#eq:compiler){reference-type="eqref" reference="eq:compiler"}, the incidence inverse is part of a conjugation that orthogonalizes a complete coordinate family. The scalar arithmetic function $\mu_{\mathrm{arith}}(n)$ is not itself an atom indicator: $$\mu_{\mathrm{arith}}(2)=-1,\qquad \mu_{\mathrm{arith}}(6)=1,\qquad \mu_{\mathrm{arith}}(4)=0.$$ It fails idempotence at $2$, accepts the squarefree composite $6$, and vanishes for a reason unrelated to primality at $4$.

The von Mangoldt function has a different limitation. Its prime-power support appears after scalar endpoint convolution and does not define a primitive word action. Likewise, prime-zeta inversion acts after commutative aggregation. Neither distinguishes the source letter $p^r$ from the temporal word $p,p,\ldots,p$ at the operator level.

The unfiltered compiler gives the complementary ablation. If one defines $A_n=q_n$ for every $n$, every composite coordinate survives as an idempotent. Möbius conjugation makes coordinates orthogonal; it does not say which coordinates are atoms. That ownership belongs entirely to the cover predicate [\[eq:atom-predicate\]](#eq:atom-predicate){reference-type="eqref" reference="eq:atom-predicate"}.

L37mm L43mm Y ablation & exact outcome & ownership lesson\
scalar $\mu_{\mathrm{arith}}(n)$ & $\mu_{\mathrm{arith}}(2)=-1,\ \mu_{\mathrm{arith}}(6)=1$ & scalar inversion is neither an atom predicate nor an idempotent weight\
$\zeta\varepsilon_n$ without $\mu$ & distinct columns need not annihilate & the inverse is required to compile a complete orthogonal family\
all $q_n$, no cover filter & every composite coordinate survives & inversion compiles coordinates; covers select atoms\
mutated relation with $6$ covering $1$ & the compiler selects $6$ & selection is equivariant with the supplied grammar and proves too much\
coordinate relabeling & output is conjugately relabeled & numeric prime names are not hidden in the formula\

## The exact negative conclusion

The no-go does not say that every $q_n$ is literally diagonal in the original Hilbert metric. It says that their ordinary cyclic character is coordinate-like and, at finite cutoff, that the entire family is explicitly similar to the coordinate table. Radical extensions and obliqueness cannot alter [\[eq:finite-power-trace\]](#eq:finite-power-trace){reference-type="eqref" reference="eq:finite-power-trace"} or [\[eq:finite-determinant\]](#eq:finite-determinant){reference-type="eqref" reference="eq:finite-determinant"}.

This conclusion is stronger than determinant equivalence discovered only after computation. It is a classification statement with an explicit conjugating unit. It also points to the only datum not tested here: $q_p^*q_q$ depends on the chosen Hilbert geometry and need not vanish even when $q_pq_q=0$. That adjoint question is not used to repair the present route.

# An honest countable weighted realization {#sec:countable}

The intervalwise incidence identities are algebraic. To form Fredholm determinants we now realize the selected atom family on a Hilbert space and prove the required operator ideals directly.

[\[def:weighted-space\]]{#def:weighted-space label="def:weighted-space"} For $\eta>\tfrac 12$, let $$H_\eta=
\left\{x=(x_n)_{n\ge1}:
\lVert x\rVert_\eta^2=\sum_{n\ge1}n^{2\eta}|x_n|^2<\infty\right\}.
\label{eq:weighted-space}$$

For a source atom $p$, the kernel [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} gives the explicit action $$q_px
=\left(\sum_{k\ge1}\mu_{\mathrm{arith}}(k)x_{pk}\right)(e_1+e_p).
\label{eq:rank-one-action}$$ Thus the incidence idempotent is not merely an intervalwise formal element: it is a concrete rank-one operator.

[\[thm:rank-one\]]{#thm:rank-one label="thm:rank-one"} For every $\eta>\tfrac 12$ and source atom $p$, the operator $q_p$ belongs to $\mathcal S_1(H_\eta)$, satisfies $$q_p^2=q_p,\qquad \operatorname{Tr}q_p=1,$$ and has trace norm $$\lVert q_p\rVert_1
=\sqrt{(1+p^{-2\eta})C_\eta},
\qquad
C_\eta
=\sum_{k\ge1}\frac{\mu_{\mathrm{arith}}(k)^2}{k^{2\eta}}
=\frac{\zeta(2\eta)}{\zeta(4\eta)}.
\label{eq:trace-norm}$$ In particular, $$\lVert q_p\rVert_1\le\sqrt{2C_\eta}
\label{eq:uniform-trace-norm}$$ uniformly in $p$, and $q_pq_q=0$ for distinct source atoms.

Write [\[eq:rank-one-action\]](#eq:rank-one-action){reference-type="eqref" reference="eq:rank-one-action"} as $$q_p=|r_p\rangle\langle v_p|,
\qquad
r_p=e_1+e_p.$$ The range vector has $$\lVert r_p\rVert_\eta^2=1+p^{2\eta}.$$ The squared dual norm of the functional is $$\lVert v_p\rVert_\eta^2
=\sum_{k\ge1}\frac{\mu_{\mathrm{arith}}(k)^2}{(pk)^{2\eta}}
=p^{-2\eta}C_\eta.$$ The trace norm of a rank-one operator is the product of these norms, giving [\[eq:trace-norm\]](#eq:trace-norm){reference-type="eqref" reference="eq:trace-norm"}. The Euler product for the squarefree indicator gives $$C_\eta
=\prod_{\ell\in\mathbb P}(1+\ell^{-2\eta})
=\frac{\zeta(2\eta)}{\zeta(4\eta)}.$$ The functional in [\[eq:rank-one-action\]](#eq:rank-one-action){reference-type="eqref" reference="eq:rank-one-action"} evaluates to one on $e_1+e_p$, proving idempotence and trace one. If $p\ne q$, neither $1$ nor $q$ is a positive multiple of $p$; the cross evaluation vanishes and hence $q_pq_q=0$.

The condition $\eta>\tfrac 12$ is exactly what is needed for $C_\eta<\infty$. The uniform estimate [\[eq:uniform-trace-norm\]](#eq:uniform-trace-norm){reference-type="eqref" reference="eq:uniform-trace-norm"} will control the infinite marked transfer.

## Bounded similarity of the whole family

Individual trace-class projectors do not automatically imply a bounded global change of basis. The stronger similarity statement has a narrower domain.

[\[thm:global-similarity\]]{#thm:global-similarity label="thm:global-similarity"} For $\eta>1$, the incidence zeta and Möbius transforms extend to bounded mutually inverse operators $Z_\eta,M_\eta$ on $H_\eta$, and $$q_p=Z_\eta\varepsilon_pM_\eta.
\label{eq:countable-similarity}$$ Their norms satisfy $$\lVert Z_\eta\rVert\le\zeta(\eta),
\qquad
\lVert M_\eta\rVert
\le\sum_{k\ge1}\frac{|\mu_{\mathrm{arith}}(k)|}{k^\eta}
=\frac{\zeta(\eta)}{\zeta(2\eta)}.
\label{eq:similarity-bounds}$$

Apply the unitary reweighting $U_\eta x=(n^\eta x_n)_n$. In unweighted $\ell^2$ coordinates, $$(U_\eta Z_\eta U_\eta^{-1}X)_a
=\sum_{k\ge1}k^{-\eta}X_{ak},
\qquad
(U_\eta M_\eta U_\eta^{-1}X)_a
=\sum_{k\ge1}\mu_{\mathrm{arith}}(k)k^{-\eta}X_{ak}.
\label{eq:downsampling-series}$$ Every downsampling map $X\mapsto(X_{ak})_a$ has norm at most one. The two operator series therefore converge absolutely in norm for $\eta>1$, with the bounds in [\[eq:similarity-bounds\]](#eq:similarity-bounds){reference-type="eqref" reference="eq:similarity-bounds"}. On finitely supported vectors the incidence identities give $Z_\eta M_\eta=M_\eta Z_\eta=I$; continuity and density extend them to all of $H_\eta$. Equation [\[eq:countable-similarity\]](#eq:countable-similarity){reference-type="eqref" reference="eq:countable-similarity"} follows from the finite-support kernel identity.

[\[rem:intermediate-eta\]]{#rem:intermediate-eta label="rem:intermediate-eta"} For $\tfrac 12<\eta\le1$, every selected $q_p$ remains an honest rank-one trace-class idempotent and pair annihilation remains exact. A bounded global zeta similarity is neither needed for the determinant theorem nor asserted there. Choosing any $\eta>1$, however, leaves every symbolic coefficient unchanged and proves that the canonical whole family can be put in coordinate form by a bounded similarity.

The countable theorem therefore sharpens the finite no-go. Oblique incidence geometry is not a cutoff artifact, but neither does it supply a new ordinary cyclic character. On a perfectly legitimate common space it is a bounded change of basis from the coordinate atom family.

# Trace-class transfer and holomorphic de Rham coupling {#sec:holomorphic}

## Marked atom transfer

Fix $\eta>\tfrac 12$ and define $$T_\eta(s,u)
=\sum_{p\in\operatorname{At}(P)}u^{\ell(p)}p^{-s}q_p.
\label{eq:atom-transfer}$$ The summation index is derived by the cover predicate, not read from a prime table.

[\[thm:trace-class-transfer\]]{#thm:trace-class-transfer label="thm:trace-class-transfer"} Whenever $$\sum_{p\in\operatorname{At}(P)}
|u|^{\ell(p)}p^{-\Re s}<\infty,
\label{eq:absolute-domain}$$ the series [\[eq:atom-transfer\]](#eq:atom-transfer){reference-type="eqref" reference="eq:atom-transfer"} converges in trace norm, locally uniformly in $(s,u)$. For every $r\ge1$, $$T_\eta(s,u)^r
=\sum_p u^{r\ell(p)}p^{-rs}q_p,
\qquad
\operatorname{Tr}T_\eta(s,u)^r
=\sum_p u^{r\ell(p)}p^{-rs}.
\label{eq:all-power-traces}$$ Its Fredholm determinant is $$\det(I-zT_\eta(s,u))
=\prod_p \left(1-zu^{\ell(p)}p^{-s}\right).
\label{eq:atom-fredholm}$$

The uniform bound [\[eq:uniform-trace-norm\]](#eq:uniform-trace-norm){reference-type="eqref" reference="eq:uniform-trace-norm"} and [\[eq:absolute-domain\]](#eq:absolute-domain){reference-type="eqref" reference="eq:absolute-domain"} prove absolute trace-norm convergence, locally uniformly on compact subsets of the domain. Holomorphy as an $\mathcal S_1$-valued map follows. Pair annihilation from [\[thm:rank-one\]](#thm:rank-one){reference-type="ref" reference="thm:rank-one"} gives the operator identity in [\[eq:all-power-traces\]](#eq:all-power-traces){reference-type="eqref" reference="eq:all-power-traces"}; tracing uses $\operatorname{Tr}q_p=1$.

For small $z$, the trace-class determinant identity $$\log\det(I-zT)
=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}T^r$$ and absolute convergence give $$\log\det(I-zT_\eta)
=\sum_p \log\left(1-zu^{\ell(p)}p^{-s}\right).$$ Both sides of [\[eq:atom-fredholm\]](#eq:atom-fredholm){reference-type="eqref" reference="eq:atom-fredholm"} are entire in $z$, so equality extends globally.

For $\rho=|u|>0$, the gamma duration has the two-sided comparison $$\rho^{\ell(n)}
\asymp_\rho n^{2\log_2\rho}.
\label{eq:gamma-asymptotic}$$ The prime series therefore gives the exact threshold $$\Re s>1+2\log_2\rho.
\label{eq:marker-half-plane}$$ At $u=0$ the transfer is identically zero. A common, marker-transparent safe domain is $|u|\le1$ and $\Re s>1$.

At $u=z=1$, [\[eq:atom-fredholm\]](#eq:atom-fredholm){reference-type="eqref" reference="eq:atom-fredholm"} becomes $$\det(I-T_\eta(s,1))
=\prod_p(1-p^{-s})
=\frac1{\zeta(s)},
\qquad \Re s>1.
\label{eq:reciprocal-zeta}$$ Equation [\[eq:reciprocal-zeta\]](#eq:reciprocal-zeta){reference-type="eqref" reference="eq:reciprocal-zeta"} is a consequence of the source-derived loop theorem. It is not advertised as a new scalar identity.

[\[prop:trace-barrier\]]{#prop:trace-barrier label="prop:trace-barrier"} The realization $T_\eta(s,1)$ cannot be trace class when $\Re s\le1$.

For each source atom $p$, the vector $r_p=e_1+e_p$ satisfies $$T_\eta(s,1)r_p=p^{-s}r_p.$$ These vectors are linearly independent. The eigenvalues of a trace-class operator, with algebraic multiplicity, are absolutely summable. Their absolute values here include $p^{-\Re s}$, whose sum over primes diverges for $\Re s\le1$.

The marker may shift the absolute half-plane when $|u|<1$, but this does not continue the $u=1$ arithmetic operator. In particular, a scalar continuation of the right side of [\[eq:reciprocal-zeta\]](#eq:reciprocal-zeta){reference-type="eqref" reference="eq:reciprocal-zeta"} is not a same-object continuation of $T_\eta(s,1)$.

## Two honest holomorphic degrees

We now couple the incidence selector to the inherited prefix-coded affine renewal sector. Let $U_{p,0}$ and $U_{p,1}$ denote its zero- and one-form pullbacks on the fixed holomorphic cylinder space. The prior construction provides a common degreewise trace-norm bound on the absolute domain and, for every branch word $w$, the local Lefschetz identity $$\operatorname{Tr}U_{w,0}-\operatorname{Tr}U_{w,1}=1
\label{eq:local-lefschetz}$$ after removing the scalar branch weight. Concretely, if the derivative of the affine word is $\vartheta_w$, the two local traces are $$\frac1{1-\vartheta_w},
\qquad
\frac{\vartheta_w}{1-\vartheta_w},$$ whose difference is one. This is the canonical de Rham cancellation of the fixed-point denominator.

Define the degreewise operators $$\mathcal T_k(s,u)
=\sum_p u^{\ell(p)}p^{-s}q_p\otimes U_{p,k},
\qquad k=0,1.
\label{eq:degreewise-transfer}$$

[\[thm:graded-determinant\]]{#thm:graded-determinant label="thm:graded-determinant"} On the common absolute trace-class domain, both operators in [\[eq:degreewise-transfer\]](#eq:degreewise-transfer){reference-type="eqref" reference="eq:degreewise-transfer"} are trace class and, for every $r\ge1$, $$\operatorname{Tr}\mathcal T_0(s,u)^r-\operatorname{Tr}\mathcal T_1(s,u)^r
=\sum_p u^{r\ell(p)}p^{-rs}.
\label{eq:graded-power-trace}$$ Consequently $$D_{\mathrm{gr}}(s,u,z)
:=\frac{\det(I-z\mathcal T_0(s,u))}
        {\det(I-z\mathcal T_1(s,u))}
=\prod_p \left(1-zu^{\ell(p)}p^{-s}\right).
\label{eq:graded-ratio}$$

The common local trace-norm bound, [\[eq:absolute-domain\]](#eq:absolute-domain){reference-type="eqref" reference="eq:absolute-domain"}, and [\[eq:uniform-trace-norm\]](#eq:uniform-trace-norm){reference-type="eqref" reference="eq:uniform-trace-norm"} give degreewise trace-norm convergence. In an $r$-fold product, the incidence factor annihilates every mixed atom word before the holomorphic trace is taken. A monochromatic word contributes $\operatorname{Tr}q_p=1$, and [\[eq:local-lefschetz\]](#eq:local-lefschetz){reference-type="eqref" reference="eq:local-lefschetz"} removes its local stability factor. This proves [\[eq:graded-power-trace\]](#eq:graded-power-trace){reference-type="eqref" reference="eq:graded-power-trace"}. Taking the difference of the two ordinary trace-log expansions yields [\[eq:graded-ratio\]](#eq:graded-ratio){reference-type="eqref" reference="eq:graded-ratio"}.

[\[rem:ordinary-graded\]]{#rem:ordinary-graded label="rem:ordinary-graded"} The numerator and denominator in [\[eq:graded-ratio\]](#eq:graded-ratio){reference-type="eqref" reference="eq:graded-ratio"} are separately defined ordinary Fredholm determinants. Their quotient is the graded relative determinant. It is not the ordinary determinant of $\mathcal T_0\oplus\mathcal T_1$, which would multiply rather than divide the two degreewise determinants.

The two cancellations also have separate ownership. Incidence pair annihilation removes mixed source labels. The de Rham difference removes a local holomorphic stability denominator. After both steps, one scalar class remains per source-derived atom, so the final determinant is again the atom product.

# Exact finite controls and evidence ownership {#sec:exact}

The infinite claims above are proofs. A deterministic exact suite checks their finite algebra, marker bookkeeping, determinant identities, and failure controls independently. Integer arithmetic and rational fractions are used for every gating check; high precision appears only in one non-gating trace-log sanity line.

The finalized integration passes all $61/61$ regression tests and records 2,384 exact ledger rows: 2,379 scientific, control, and comparison rows plus five strict-route gates. The row ownership is $$\begin{gathered}
4\ \text{incidence inverse},\quad
30\ \text{primitive},\quad
900\ \text{pair},\quad
256\ \text{cover},\\
1016\ \text{necklace},\quad
80\ \text{marker},\quad
8\ \text{power trace},\quad
4\ \text{Fredholm/de Rham},\\
24\ \text{weighted Hilbert},\quad
3\ \text{bounded similarity},\quad
2\ \text{source mutation},\\
30\ \text{stability/equivariance},\quad
13\ \text{ablation},\quad
9\ \text{analysis comparison},\quad
5\ \text{route}.
\end{gathered}$$

## Compiler census

At the downset cutoff $N=30$, the cover relation derives $$2,3,5,7,11,13,17,19,23,29$$ as the atoms of $1$. This displayed list is output, not input. The suite checks both products $Z\mu=\mu Z=I$, every entry of [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"}, all $30^2$ identities $$q_nq_m=\delta_{nm}q_n,$$ completeness, exact rank and trace, and the obliqueness of every selected atom idempotent. Restriction from $P_{30}$ to $P_{18}$ reproduces the smaller compiler exactly. A deterministic nontrivial relabeling reproduces conjugate relabeling, ruling out hidden use of numeric prime names.

## Words, necklaces, and markers

For the four source-derived atoms $2,3,5,7$, every word through length six is checked. The cyclic-class census is shown in [1](#tab:necklace-census){reference-type="ref" reference="tab:necklace-census"}. At every length, the only selected classes are the four monochromatic repetitions.

::: {#tab:necklace-census}
    word length $r$   all cyclic classes   selected classes
  ----------------- -------------------- ------------------
                  1                    4                  4
                  2                   10                  4
                  3                   24                  4
                  4                   70                  4
                  5                  208                  4
                  6                  700                  4

  : Exact cyclic-class census over the four source-derived atoms $2,3,5,7$.
:::

Every word through length five over the alphabet $2,3,4,5$ supplies a separate composite-letter control. In particular, a monochromatic $4$-word is rejected even though a temporal repetition of $2$ survives. Marker exponents are checked through repetition eight and always equal $r\ell(p)$.

## Determinant fixtures

At the exact rational point $$(s,u,z)=(2,\tfrac12,\tfrac13),$$ the $30\times30$ incidence determinant is $$\frac{
13032061231684147510264082032595569214375
}{
13239391670016285360628993515288344395776
},
\label{eq:exact-incidence-determinant}$$ equal to the finite source-atom product. All power traces through order eight agree with the corresponding atom sums.

The suite also constructs separate finite zero- and one-form matrices and computes their ordinary determinants before taking the ratio. The exact graded result is $$\frac{9217800049}{9364045824},
\label{eq:exact-graded-ratio}$$ again equal to the finite atom product. The order-30 trace-log residual is approximately $3.95\times10^{-42}$; it is recorded only as a numerical sanity check and does not gate any theorem.

L37mm L45mm Y control & exact observed outcome & conclusion\
mutated source relation & covers become $\{2,3,5,6\}$, and $6$ is selected & compiler is faithful to the source and has no independent primality oracle\
scalar Möbius ablation & nonzero at $6$, value $-1$ at $2$ & scalar inversion cannot replace the cover predicate\
zeta without inverse & the $2$- and $4$-columns fail cross-annihilation & Möbius inversion is required for orthogonal compilation\
no cover filter & every integer coordinate survives & incidence inversion alone has no atom selectivity\
relabeling & recompiled matrices equal conjugate relabeling & numeric names are not hard-coded\
cutoff restriction & every retained kernel entry stabilizes exactly & finite checks respect the locally finite infinite formula\

## What the computation does not prove

The exact suite corroborates finite identities, catches marker mistakes, and tests the ownership firewalls. It does not prove convergence of the countable operator series, boundedness of the global similarity, the sharp trace-class barrier, or the holomorphic determinant theorem. Those statements are owned by [\[thm:rank-one,thm:global-similarity,thm:trace-class-transfer,%
prop:trace-barrier,thm:graded-determinant\]](#thm:rank-one,thm:global-similarity,thm:trace-class-transfer,%
prop:trace-barrier,thm:graded-determinant){reference-type="ref" reference="thm:rank-one,thm:global-similarity,thm:trace-class-transfer,%
prop:trace-barrier,thm:graded-determinant"}. No Riemann zero, target spectrum, private dataset, or fitted loss enters either the proofs or the exact suite.

The canonical runner starts from a fresh result directory, fixes `PYTHONHASHSEED=0`, and executes the generator, tests, and analyzer twice. All 30 compared code/generated-result artifacts are byte identical, the 32-entry SHA-256 ledger passes, and the integrity audit reports no local cache or CRLF CSV artifact. This certificate covers code and generated results; it does not cover the manuscript or documentation.

# Strict route evaluation {#sec:route}

The route record evaluates the construction that was actually proved. A positive orbit theorem does not force a positive overall decision.

L42mm L27mm Y gate & status & reason\
`A0_ANALYTIC_` `ARITHMETIC_ORIGIN` & [source-derived]{style="color: passgreen"} & divisibility derives atomhood; the fixed gamma code derives duration; no prime table or target spectrum enters\
`A1_PASS_ANALYTIC` & [pass]{style="color: passgreen"} & [\[thm:word-selector\]](#thm:word-selector){reference-type="ref" reference="thm:word-selector"} selects only source-atom loops, with multiplicity one and weight $u^{r\ell(p)}p^{-rs}$ at every repetition\
`A2_ANALYTIC_DETERMINANT` & [pass]{style="color: passgreen"} & both holomorphic degrees are honest trace-class operators on one common domain and [\[thm:graded-determinant\]](#thm:graded-determinant){reference-type="ref" reference="thm:graded-determinant"} proves their graded ratio\
`A3_FAIL` & [fail]{style="color: stopred"} & at $u=1$, [\[prop:trace-barrier\]](#prop:trace-barrier){reference-type="ref" reference="prop:trace-barrier"} stops the operator at $\Re s=1$; no same-object continuation or canonical regularization is built\
`A4_FAIL` & [fail]{style="color: stopred"} & similarity makes ordinary incidence geometry determinant invisible, and no critical-line carrier or divisor-moving spectral law exists\

## Why A1 genuinely passes

The compiler is not handed a prime-only state space. It is defined uniformly over all source integers, and the source relation derives the cover predicate. The word theorem acts before trace and survives every repetition. These facts meet the analytic orbit gate even though the final product is familiar.

The mutated-source control does not undo the pass. It establishes the precise scope: the selector is faithful to the frozen factorization grammar. It also prevents an inflated interpretation. The compiler has no grammar-independent oracle for rational primality.

## Why A3 and A4 do not move

There are two independent stops. Analytically, the eigenvalues $p^{-s}$ prevent the $u=1$ family from remaining trace class at or left of $\Re s=1$. Replacing the operator by a scalar continuation of its product would change the object and therefore cannot earn A3.

Structurally, [\[thm:finite-conjugacy,thm:global-similarity\]](#thm:finite-conjugacy,thm:global-similarity){reference-type="ref" reference="thm:finite-conjugacy,thm:global-similarity"} reduce the ordinary cyclic family to coordinate projectors at every finite cutoff and on a canonical countable space. There is no derived motion of zeros, no self-adjoint critical-line family, and no RH criterion. That is an A4 failure even though A0--A2 are strong.

The associated stop records are $$\begin{gathered}
\texttt{GO\_SOURCE\_DERIVED\_ATOM\_ORBITS},\\
\texttt{STOP\_INCIDENCE\_SIMILARITY\_COLLAPSE},\\
\texttt{STOP\_CRITICAL\_STRIP\_CONTINUATION}.
\end{gathered}$$

## Minimum Paper28 obligation {#sec:paper28-obligation}

Ordinary products exhaust the information studied here, but adjoint products need not vanish. With $q_p=|r_p\rangle\langle v_p|$, the ranges $r_p=e_1+e_p$ share the $e_1$ direction, and generally $$q_p^*q_q\ne0\qquad(p\ne q).$$ The next admissible question is therefore a canonical chiral completion of $$T_{\sigma+it,u}
=\sum_p u^{\ell(p)}p^{-\sigma-it}q_p,$$ not another ordinary selector.

Any such study must derive the exact mixed Gram kernel, prove the common Schatten domain, retain the digit marker, and compare the oblique family with both coordinate and mutated-poset controls. The adjoint is not holomorphic in $s$, so a two-variable holomorphic/antiholomorphic family must precede any restriction to real $t$. A fitted subtraction, reference-dependent regularization, or target-zero comparison is forbidden.

If the chiral spectrum is generic rank-one Gram geometry or becomes trivial after canonical orthogonalization, the required stop is $$\texttt{STOP\_ADJOINT\_GRAM\_COLLAPSE}
\quad\text{and}\quad
\texttt{STOP\_INCIDENCE\_ROUTE}.$$

# Conclusion {#sec:conclusion}

The integer divisibility grammar can compile its own atom loops. Covers of $1$ identify the source atoms without a prime inventory, and $q_n=\zeta\varepsilon_n\mu$ turns the uniform source coordinates into exact primitive word actions. Every mixed word and composite source letter vanishes before trace; every temporal repetition of one atom survives with coefficient one and the full gamma-code duration. This is a genuine analytic pass of the orbit gate.

The compiler also closes its own loophole. Finite primitive lifts are unitriangularly conjugate to coordinate projectors. In the countable weighted model, individual atom idempotents are rank-one trace class for $\eta>\tfrac 12$, and the whole family is boundedly similar to coordinate projectors for $\eta>1$. The marked transfer and both holomorphic degrees have honest Fredholm determinants on a proved domain, but their graded ratio is exactly the atom product. Obliqueness creates no new ordinary cyclic observable.

At $u=1$, the eigenvalue sequence gives a sharp trace-class stop at $\Re s=1$. No same-object continuation, critical-line carrier, or RH mechanism follows. The final route is therefore rejected despite the A1 and A2 advances.

The conceptual gain is precise: source derivation and spectral mechanism are different obligations. Paper27 solves the first and proves that ordinary incidence conjugacy cannot solve the second. Only the adjoint mixed-Gram geometry remains untested, and it must survive diagonal, mutated-source, and generic controls before receiving any further arithmetic interpretation.

# Expanded proof details {#app:proofs}

## The cover formula and locally finite completion

For $n>1$, $$(\bar\zeta*\bar\zeta)(1,n)
=\sum_{1\mid c\mid n}\bar\zeta(1,c)\bar\zeta(c,n).$$ The factors require $1<c<n$, so the value is the number of strict intermediate divisors. It is zero exactly for a cover of $1$. If $n=ab$ with $1<a<n$, then $a$ is such an intermediate divisor. Conversely, an intermediate divisor supplies a nontrivial factorization. This proves [\[eq:atoms-primes\]](#eq:atoms-primes){reference-type="eqref" reference="eq:atoms-primes"} without any scalar prime coefficient.

The intervalwise countable statement in [\[thm:primitive-system\]](#thm:primitive-system){reference-type="ref" reference="thm:primitive-system"} requires no topological completion. For fixed $a\mid b$, only the finite interval $[a,b]$ can contribute to an incidence convolution, and only $n\in[a,b]$ can contribute to $\sum_n q_n(a,b)$. Every finite identity therefore stabilizes on that interval.

## Matrix orientation and rank one

With rows and columns indexed by source integers, the kernel [\[eq:kernel\]](#eq:kernel){reference-type="eqref" reference="eq:kernel"} factors as $$q_n(a,b)
=\mathbf 1_{\{a\mid n\}}\,
  \mathbf 1_{\{n\mid b\}}\mu_{\mathrm{arith}}(b/n).$$ Thus every finite $q_n$ has rank one. For an atom $p$, its range vector is exactly $e_1+e_p$, because the only divisors of $p$ are $1$ and $p$. Its functional is $$x\longmapsto\sum_{k\ge1}\mu_{\mathrm{arith}}(k)x_{pk}.$$ The evaluation of this functional on $e_1+e_p$ is $\mu_{\mathrm{arith}}(1)=1$. Hence the rank-one trace formula gives $\operatorname{Tr}q_p=1$ and the same evaluation proves $q_p^2=q_p$.

For distinct atoms $p$ and $q$, the functional associated with $p$ vanishes on both nonzero coordinates of $e_1+e_q$: neither $1$ nor $q$ is a positive multiple of $p$. This gives pair annihilation directly on $H_\eta$, independently of the global similarity theorem.

## The radical conjugating unit

The proof of [\[thm:finite-conjugacy\]](#thm:finite-conjugacy){reference-type="ref" reference="thm:finite-conjugacy"} uses only completeness, orthogonality, and a nilpotent radical. To verify the intertwining step in detail, write $$v=\sum_y f_ye_y.$$ Then $$f_xv
=\sum_y f_xf_ye_y
=f_xe_x,$$ whereas $$ve_x
=\sum_y f_ye_ye_x
=f_xe_x.$$ Thus $f_xv=ve_x$. Since $v=1+j$ for $j\in J_N$, the finite geometric series $$v^{-1}=1-j+j^2-\cdots$$ terminates and proves $f_x=ve_xv^{-1}$. This proof does not assert that $v$ is unitary or that the $f_x$ are orthogonal in a Hilbert metric.

## Exact weighted dual norm

The dual of $H_\eta$ identifies the coefficient functional $\lambda(x)=\sum_n b_nx_n$ with squared norm $$\lVert\lambda\rVert^2=\sum_{n\ge1}n^{-2\eta}|b_n|^2.$$ For $b_{pk}=\mu_{\mathrm{arith}}(k)$ and all other coefficients zero, $$\lVert\lambda_p\rVert^2
=p^{-2\eta}\sum_{k\ge1}\frac{\mu_{\mathrm{arith}}(k)^2}{k^{2\eta}}.$$ The squarefree Dirichlet series is absolutely convergent for $2\eta>1$, and prime-by-prime expansion gives $$\sum_{k\ge1}\frac{\mu_{\mathrm{arith}}(k)^2}{k^{2\eta}}
=\prod_{\ell\in\mathbb P}(1+\ell^{-2\eta})
=\prod_{\ell\in\mathbb P}
  \frac{1-\ell^{-4\eta}}{1-\ell^{-2\eta}}
=\frac{\zeta(2\eta)}{\zeta(4\eta)}.$$ Multiplying by $\lVert e_1+e_p\rVert_\eta^2=1+p^{2\eta}$ gives [\[eq:trace-norm\]](#eq:trace-norm){reference-type="eqref" reference="eq:trace-norm"}.

## Downsampling convergence

Let $S_kX=(X_{ak})_{a\ge1}$. Then $$\lVert S_kX\rVert_{\ell^2}^2
=\sum_{a\ge1}|X_{ak}|^2
\le\sum_{n\ge1}|X_n|^2,$$ so $\lVert S_k\rVert\le1$. The series in [\[eq:downsampling-series\]](#eq:downsampling-series){reference-type="eqref" reference="eq:downsampling-series"} therefore converge absolutely in operator norm when their scalar coefficients lie in $\ell^1$. For zeta this requires $\eta>1$. For Möbius, $$\sum_{k\ge1}\frac{|\mu_{\mathrm{arith}}(k)|}{k^\eta}
=\prod_{\ell\in\mathbb P}(1+\ell^{-\eta})
=\frac{\zeta(\eta)}{\zeta(2\eta)}.$$ Inversion on finite-support vectors extends because both limits are bounded.

## The gamma-marker half-plane

Put $j=\lfloor\log_2n\rfloor$, so $2^j\le n<2^{j+1}$ and $\ell(n)=2j+1$. For fixed $\rho>0$, with $\alpha=2\log_2\rho$, $$\min(\rho,\rho^{-1})n^\alpha
\le \rho^{\ell(n)}
\le \max(\rho,\rho^{-1})n^\alpha.$$ This proves [\[eq:gamma-asymptotic\]](#eq:gamma-asymptotic){reference-type="eqref" reference="eq:gamma-asymptotic"}. The prime sum in [\[eq:absolute-domain\]](#eq:absolute-domain){reference-type="eqref" reference="eq:absolute-domain"} therefore has the same convergence as $$\sum_p p^{-(\Re s-2\log_2\rho)}.$$ The prime Dirichlet series converges exactly when its real exponent is greater than one, proving [\[eq:marker-half-plane\]](#eq:marker-half-plane){reference-type="eqref" reference="eq:marker-half-plane"}. At equality the divergence of the prime harmonic series supplies the sharp boundary.

## Trace-log and degreewise ownership

On compact subsets of [\[eq:absolute-domain\]](#eq:absolute-domain){reference-type="eqref" reference="eq:absolute-domain"}, the transfer series is uniformly summable in trace norm. For sufficiently small $z$, the trace-log series is absolutely convergent and the sums over $r$ and $p$ may be interchanged. The resulting product is entire in $z$, so analytic uniqueness extends the identity to every $z$.

For the holomorphic tensor, each degree is formed and shown trace class before a quotient is taken. Write $$d_r=\operatorname{Tr}\mathcal T_0^r-\operatorname{Tr}\mathcal T_1^r.$$ Then $$\log\frac{\det(I-z\mathcal T_0)}{\det(I-z\mathcal T_1)}
=-\sum_{r\ge1}\frac{z^r}{r}d_r.$$ Incidence pair annihilation reduces $d_r$ to monochromatic atom words, and the local de Rham identity makes their fiber contribution one. This yields [\[eq:graded-ratio\]](#eq:graded-ratio){reference-type="eqref" reference="eq:graded-ratio"} without interpreting a formal superdeterminant whose degreewise factors have not been defined.

# Scope, reproducibility, and declarations {#app:scope}

## Claim and ownership ledger

L39mm Y Y boundary & licensed statement & excluded substitution\
source atom / supplied inventory & covers of $1$ derive the labels & prime-only coordinate table as input\
compiler / selector & $\zeta\varepsilon_n\mu$ compiles all coordinates & incidence inversion alone called prime selective\
source power / temporal repetition & $p^r$ dies, while $p,\ldots,p$ survives & endpoint prime-power support used as a word theorem\
wordwise / aggregate & mixed products vanish before trace & commuting scalar variables before verification\
ordinary / graded determinant & quotient of two honest degreewise determinants & ordinary determinant of an ungraded block sum\
individual / global countable claim & $q_p\in\mathcal S_1$ for $\eta>\tfrac 12$ & bounded global similarity below its $\eta>1$ proof domain\
digit / return marker & $u^{r\ell(p)}$ and $z^r$ have distinct owners & one codeword silently counted as one digit\
scalar / operator continuation & trace class on the proved half-plane & scalar continuation of the product called the same operator\
ordinary / adjoint geometry & ordinary cyclic observables collapse & universal claim about $q_p^*q_q$\

## Data and code availability

The exact evidence is generated by deterministic source/evaluator-separated code stored with the paper project under independently owned code, experiment, and result paths. The artifact set includes an exact result ledger, environment lock, per-file SHA-256 ledger, double-run certificate, and integrity audit. The double-run certificate applies to code and generated results, not to manuscript or documentation files. It compares 30 artifacts from two fresh runs; the 32-entry frozen ledger and all 61 regression tests pass. No external dataset, target-zero file, private service, or stochastic seed is required.

## Limitations

The source theorem is specific to the fixed integer divisibility grammar and its cover relation. The finite conjugacy theorem assumes a finite incidence algebra and complete primitive lifts with fixed diagonal labels. The countable rank-one theorem treats the explicit weighted spaces $H_\eta$; the global bounded similarity is asserted only for $\eta>1$. The analytic determinant is proved only on the absolute trace-class domain.

The paper does not construct scalar or operator continuation across $\Re s=1$ at $u=1$, a canonical regularized determinant there, a self-adjoint critical-line family, or an RH criterion. Odd super-operators, unbounded similarities, arbitrary von Neumann traces, non-type-I representations, and adjoint mixed-Gram spectra lie outside the theorem.

## Ethics statement

This is a mathematical and exact-computation study. It uses no human participants, animals, personal data, surveillance data, or consequential automated decisions. No ethics-board approval was applicable.

## Author contributions

The anonymous authors jointly contributed conceptualization, formal analysis, methodology, software specification, validation, visualization, writing, and artifact curation. Individual names are withheld in this research draft.

## Funding

No external funding is declared for this research artifact.

## Conflict of interest

The authors declare no competing financial or nonfinancial interests. The standing instruction excluded a manuscript-review loop; source, proof, formula, citation, exact, build, and visual audits were retained.
