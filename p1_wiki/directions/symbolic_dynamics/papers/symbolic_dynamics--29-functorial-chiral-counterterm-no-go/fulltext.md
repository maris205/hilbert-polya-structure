---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--29-functorial-chiral-counterterm-no-go"
canonical_tex: "symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go/main.tex"
canonical_pdf: "symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go/main.pdf"
source_sha256: "c3f6d15d610765d1091f80512828e554e51ef2c00101c7e32bf2260e63ede4a0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Functorial Counterterms at the Hilbert--Schmidt Boundary: Finite-Scheme Ambiguity and Generic Mixed-Gram Residues

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/29-functorial-chiral-counterterm-no-go/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the critical line of a Möbius-incidence chiral family, the finite-cutoff quadratic ledger splits into a divergent diagonal prime-harmonic term and an absolutely summable mixed Gram phase. We freeze a category of finite pointed posets with transported decorations and order-ideal cutoff embeddings, and classify reference-independent natural quadratic counterterms. Divergence cancellation fixes only a germ: every convergent diagonal scheme has coefficient $C_\eta+r_p$ with $\sum_p|r_p|/p<\infty$, while summable natural mixed kernels remain free. Full-diagonal and leading-only subtraction are both admissible and differ by the finite shift $2C_\eta\sum_pp^{-1-2\eta}$. Sharp Mertens and Abel/prime-zeta finite parts differ by $-2C_\eta\gamma$. Every diagonal scheme preserves the mixed frequencies. More generally, no quadratic, additive, pair-local rule linear in the native Gram contraction can preserve the divisibility mechanism while cancelling matched non-arithmetic controls. This theorem is scoped: bare naturality still permits nonlocal filtered-tower invariants. We keep the nonexistent ordinary quadratic trace, the honest third-regularized Fredholm determinant, and a new scheme-dependent renormalized functional under separate ownership. A scheme change is a zero-free exponential and does not alter the auxiliary determinant divisor. Exact relabel, cutoff, mutated, composite-only, generic-DAG, and random-inventory controls support the bounded no-go. The strict arithmetic-spectral route remains rejected.

  **Keywords:** symbolic dynamics; incidence algebra; Möbius inversion; counterterm; finite-part ambiguity; modified Fredholm determinant; naturality.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Functorial Counterterms at the Hilbert--Schmidt Boundary:\
  Finite-Scheme Ambiguity and Generic Mixed-Gram Residues
```

## Markdown 正文

# Introduction {#sec:introduction}

The Hilbert--Schmidt boundary separates two kinds of determinant argument. Above it, an ordinary or modified Fredholm determinant is backed by a proved operator ideal. At the boundary, an attractive finite-cutoff trace formula may still exist even though the corresponding countable trace does not. Conflating these levels replaces an analytic obstruction with notation. The third-regularized determinant avoids that error by removing the first two logarithmic powers whenever the operator belongs to $\mathcal S_3$ [@Simon2005; @BritzEtAl2021]. For the chiral incidence family studied here, however, the removed quadratic cutoff coefficient has a particularly simple form: a divergent prime-harmonic diagonal plus an absolutely summable mixed phase. This raises a narrower question. Can the divergent diagonal be subtracted by a rule intrinsic to the source while the mixed phase is retained as an arithmetic invariant?

The scalar subtraction is easy. Its claimed naturality and selectivity are not. Prime-harmonic sharp cutoffs and prime-zeta/Abel regulators already carry different constants [@Mertens1874; @Froberg1968]. At the categorical level, incidence algebras are not functorial for arbitrary poset maps; interval and finiteness hypotheses are essential [@Rota1964; @ContentLemayLeroux1980; @GalvezKockTonks2018]. At the dynamical level, graph zeta theory does possess a source-local cancellation: the Ihara--Hashimoto non-backtracking operator removes immediate inverse-edge returns by changing the admissible word system [@Hashimoto1989; @Bass1992]. That mechanism is a useful warning, not a solution. The divisibility Hasse diagram has no native edge-reversal involution, and changing the operator does not preserve the mixed Gram ledger.

This paper freezes the categorical and analytic choices before classifying counterterms. The base objects are finite pointed locally finite posets. Pointed isomorphisms transport the Hilbert weight and the all-object coefficient mark. Compatible cutoff embeddings have order-ideal image, so old intervals and Möbius coefficients are preserved. The infinite divisibility result uses a fixed ambient incidence compilation followed by finite active-atom restriction. It does not identify Gram matrices obtained by recompiling each finite source with compressions of the ambient Gram kernel. This distinction prevents "cutoff naturality" from hiding two different operations.

Within that category, the exact answer has two parts. First, the divergent germ is rigid but the finite part is not. If $K=(k_{pq})$ is a reference-independent natural quadratic counterterm, absolute exhaustion-independent convergence holds exactly when $$k_{pp}=C_\eta+r_p,
 \qquad \sum_p\frac{|r_p|}{p}<\infty,
 \qquad
 \sum_{p<q}\frac{|k_{pq}|}{\sqrt{pq}}<\infty.
 \label{eq:intro-classification}$$ The first condition fixes the diagonal divergent germ. Both conditions leave arbitrary summable equivariant finite shifts. In particular, removing only $2C_\eta\sum p^{-1}$ and removing the full diagonal $2\sum G_{pp}/p$ are admissible. Their finite parts differ by $2C_\eta\sum_pp^{-1-2\eta}>0$.

Second, the retained mixed term proves too much. Every diagonal counterterm leaves every pair frequency unchanged. If the class is enlarged to quadratic counterterms that are additive over atoms and unordered pairs, local on one or two atoms, and linear in the native Gram contraction, a matched nonzero pair presents an exact preserve-or-cancel contradiction. Preservation forces the local mixed coefficient $\beta=0$; cancellation forces $\beta=1$. Mutated-cover, composite-only, generic-DAG, and random-inventory controls all contain nonzero mixed pairs and positive fourth-order descendants. The obstruction is generic oblique Gram geometry, not a prime selector.

The restriction in the previous paragraph is load-bearing. Isomorphism naturality alone permits a coefficient to inspect a nonlocal invariant of an entire filtered tower. One can even recognize a predeclared tower isomorphism class without consulting printed labels. Such a construction is formally natural but acts as an inventory oracle. We do not prove that every nonlocal tower invariant is generic, and we do not claim a universal naturality no-go. Whether an independently motivated, cutoff-compatible divisibility-coherence invariant exists remains open.

We also preserve determinant ownership. The countable critical operator is not Hilbert--Schmidt, so its ordinary quadratic trace and $\det_2$ are absent. The honest $\det_3$ deletes the complete quadratic power. After declaring a finite-part scheme $\mathcal R$, one may define a new functional $$\mathfrak D_{\mathcal R}(s,z)
 :=\det\nolimits_3(I-z\mathcal B_s)
 \exp\!\left[-\frac{z^2}{2}
  \operatorname{FP}_{\mathcal R}\operatorname{Tr}(\mathcal B_s^2)\right].
 \label{eq:intro-dren}$$ This is neither an ordinary Fredholm determinant nor $\det_2$. A finite scheme change multiplies it by a zero-free exponential, so it does not alter the auxiliary-$z$ divisor. Reflection symmetry survives exactly for a reflection-symmetric finite part, but symmetry supplies no missing selectivity.

The contribution is consequently a scoped classification and stop theorem. The subtraction technology is classical; the bounded primary-source audit found no exact collision for the combined decorated-incidence classification and exact-control no-go. The route record does not improve: `A2_ANALYTIC_DETERMINANT` remains owned solely by the inherited honest $\det_3$, while the fixed-operator and selectivity gates fail. Route A is rejected, Route B remains locked, and no target-zero datum enters the argument.

# Decorated source category and prior boundary {#sec:category}

## Pointed objects and compatible embeddings

Let $\mathsf{CutPos}_*$ have finite locally finite posets $(P,\le,\bot)$ with a unique least element as objects. Its isomorphisms are pointed order isomorphisms. An incidence-compatible cutoff embedding $i:P\hookrightarrow Q$ is an injective pointed order embedding whose image is an order ideal.

The order-ideal condition is stronger than an arbitrary induced-subposet inclusion. If two old elements bound an interval in $Q$, every element of that interval lies below the old upper endpoint and therefore remains in the image. Restriction consequently preserves the old zeta and Möbius coefficients: $$i^*\zeta_Q=\zeta_P,
 \qquad
 i^*\mu_Q=\mu_P,
 \qquad
 i^*q^Q_{i(x)}=q^P_x.
 \label{eq:incidence-restriction}$$ This morphism choice follows the classical lesson that incidence functoriality requires conditions beyond monotonicity [@ContentLemayLeroux1980; @AguiarFerrer2000; @GalvezKockTonks2018].

The positive Hilbert weight $w:P\to(0,\infty)$ and coefficient mark $\nu:P\to(0,\infty)$ are transported fibers. Under a pointed isomorphism $\phi$, $$w'(\phi x)=w(x),\qquad \nu'(\phi x)=\nu(x).
 \label{eq:transported-decorations}$$ They may weight every object; they may not determine which objects are active. Activity is fixed by the source cover predicate $$A(P)=\{x\in P:\bot\prec x\}.
 \label{eq:cover-predicate}$$ For integer divisibility, $\nu(n)=n$ and $A(P)$ is the set of prime covers. No primality lookup is used.

The unequal critical coefficients $p^{-s}$ cannot be natural on the bare integer-divisibility poset.

Every permutation of the prime generators extends multiplicatively to an automorphism of $(\mathbb N_{\ge1},\mid,1)$. All covers of $1$ lie in one automorphism orbit. A scalar natural on the bare poset must be constant on that orbit, while $p^{-s}$ is not. The uniformly transported all-object mark $\nu(n)=n$ is therefore coefficient data, not a recovered poset invariant.

## Source cutoff versus active cutoff

Two operations are easily confused. A *source cutoff* replaces the ambient source by a finite order ideal and recompiles the incidence idempotents. An *active cutoff* retains the ambient compilation and restricts the finite cover set in the operator sum. Equation [\[eq:incidence-restriction\]](#eq:incidence-restriction){reference-type="eqref" reference="eq:incidence-restriction"} preserves the old incidence coefficients, but a weighted Hilbert--Schmidt Gram contraction can acquire new upper-tail terms when the source grows. It need not be constant under finite-source recompilation.

The main theorem follows the active-cutoff convention. The countable divisibility realization is compiled once, and finite sets $F\nearrow A(P)$ restrict its ambient Gram kernel. Finite mutated and generic posets are standalone control objects. Their directly compiled Gram matrices are not asserted to be compressions of the infinite divisibility Gram.

## Regularization terminology

Hadamard finite parts retain a constant only after a singular or cutoff asymptotic and its scale convention have been specified [@BlanchetFaye2000; @EstradaKanwal1989]. Weighted or canonical traces in pseudodifferential analysis likewise depend on a proved symbol calculus and, outside special order or parity classes, can have residue-controlled weight or commutator defects [@KontsevichVishik1994; @Grubb2005; @CardonaEtAl2003]. Nothing in Schatten membership alone imports that machinery. We therefore use *sharp-cutoff finite part of the diagonal ledger*; "Hadamard-type" refers only to the displayed $X$-asymptotic.

Relative determinants make the reference explicit and impose trace-class heat-difference hypotheses [@Muller1998]. They do not select a diagonal reference from a bare poset. Similarly, the ordinary $\det\nolimits_3$ theory is available on its Schatten domain but removes the quadratic power in full [@Simon2005; @BritzEtAl2021].

The closest combinatorial collision is non-backtracking graph zeta theory. The directed-edge rule excludes an edge followed by its inverse, and Bass's formula expresses the resulting determinant through adjacency and degree data [@Hashimoto1989; @Bass1992]. This is genuinely graph-natural local cancellation. It changes the word system, however, and a divisibility DAG has no native inverse edge. It does not preserve the coefficient $G_{pq}\cos(t\log(q/p))$ audited below.

Finally, standard symbolic-dynamical zeta constructions first establish a finite or nuclear transfer operator and then take an honest determinant [@BowenLanford1970; @Ruelle1976]. Their analytic order is the opposite of declaring a finite trace for a non-trace-class square. The present result is not a new zeta regularization. Its novel target, in the bounded search, is the counterterm classification and exact local no-go for this decorated incidence source.

# Exact Gram geometry at the quadratic boundary {#sec:gram}

Let $Z$ be the zeta matrix of a finite pointed poset, let $M=Z^{-1}$, and let $E_x=e_xe_x^{\mathsf T}$. The incidence idempotent $$q_x=ZE_xM
 \label{eq:qx}$$ has the rank-one factorization $q_x=u_xv_x^{\mathsf T}$, where $$u_x(a)=\mathbf 1_{a\le x},
 \qquad
 v_x(b)=\mu(x,b)\mathbf 1_{x\le b}.
 \label{eq:uv}$$ For $W=\operatorname{diag}(w(a))$, put $$X^\sharp=W^{-1}X^*W,
 \qquad
 G_{xy}=\operatorname{Tr}(q_xq_y^\sharp).
 \label{eq:sharp-gram}$$

[\[prop:general-gram\]]{#prop:general-gram label="prop:general-gram"} For every finite weighted pointed poset, $$G_{xy}
 =\bigl(u_y^{\mathsf T}Wu_x\bigr)
  \bigl(v_x^{\mathsf T}W^{-1}v_y\bigr).
 \label{eq:general-gram}$$ The matrix $G$ is real symmetric and positive semidefinite for source-real data, and it is invariant under transported pointed isomorphisms.

The first factor in [\[eq:general-gram\]](#eq:general-gram){reference-type="eqref" reference="eq:general-gram"} measures overlap of lower cones; the second measures overlap of weighted Möbius upper tails. This factorization is the only incidence input needed for the counterterm theorem.

## Divisibility coefficients

Fix $\eta>1$ and $w(n)=n^{2\eta}$. Define $$C_\eta=\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
 =\frac{\zeta(2\eta)}{\zeta(4\eta)}.
 \label{eq:Ceta}$$

[\[thm:atom-gram\]]{#thm:atom-gram label="thm:atom-gram"} For divisibility covers $p,q$, $$G_{pp}=C_\eta(1+p^{-2\eta}),
 \label{eq:Gdiag}$$ and, for $p\ne q$, $$G_{pq}=C_\eta
 \frac{(pq)^{-2\eta}}
 {(1+p^{-2\eta})(1+q^{-2\eta})}>0.
 \label{eq:Gmixed}$$

The proof is in [11](#app:proofs){reference-type="ref" reference="app:proofs"}. The off-diagonal positivity is important: it makes a nonzero mixed pair a generic two-atom mechanism rather than a numerical accident.

## The finite quadratic ledger

For a finite active cover set $F$, set $$T_{s,F}=\sum_{p\in F}p^{-s}q_p,
 \qquad
 \mathcal B_{s,F}=
 \begin{pmatrix}
 0&T_{s,F}\\ T_{1-s,F}^\sharp&0
 \end{pmatrix}.
 \label{eq:finite-block}$$ Finite-dimensional cyclicity gives $$Q_F(s):=\operatorname{Tr}\mathcal B_{s,F}^2
 =2\sum_{p,q\in F}p^{-s}q^{s-1}G_{pq}.
 \label{eq:QFs}$$ This is an exact finite ledger. It is not notation for the nonexistent countable critical quadratic trace.

At $s=1/2+it$, symmetry of $G$ yields $$\begin{aligned}
 Q_F(t)&=D_F+M_F(t),\label{eq:Qsplit}\\
 D_F&=2\sum_{p\in F}\frac{G_{pp}}p,\label{eq:DF}\\
 M_F(t)&=4\sum_{p<q\in F}\frac{G_{pq}}{\sqrt{pq}}
 \cos\!\left(t\log\frac qp\right).
 \label{eq:MF}\end{aligned}$$

[\[thm:mixed-summability\]]{#thm:mixed-summability label="thm:mixed-summability"} For $\eta>1$, the limit $$M_\eta(t)=4\sum_{p<q}\frac{G_{pq}}{\sqrt{pq}}
 \cos\!\left(t\log\frac qp\right)
 \label{eq:Meta}$$ converges absolutely and uniformly for real $t$. For $F_X=\{p:p\le X\}$, $$\sup_{t\in\mathbb R}|M_\eta(t)-M_{F_X}(t)|
 =O_\eta(X^{1/2-2\eta}).
 \label{eq:mixed-tail}$$ Moreover, $$M_\eta(s)=2\sum_{p<q}G_{pq}
 \left(p^{-s}q^{s-1}+q^{-s}p^{s-1}\right)
 \label{eq:mixed-holo}$$ is holomorphic on $1-2\eta<\Re s<2\eta$ and obeys $M_\eta(1-s)=M_\eta(s)$.

[\[thm:diagonal-germ\]]{#thm:diagonal-germ label="thm:diagonal-germ"} The diagonal ledger satisfies the exact identity $$D_{F_X}
 =2C_\eta\sum_{p\le X}\frac1p
 +2C_\eta\sum_{p\le X}p^{-1-2\eta}.
 \label{eq:diagonal-decomposition}$$ Only the first term diverges. The second converges to $2C_\eta P(1+2\eta)$ with tail $O_\eta(X^{-2\eta})$. Consequently, $$Q_{F_X}(t)=2C_\eta\log\log X
 +2C_\eta\bigl(\mathfrak B_1+P(1+2\eta)\bigr)
 +M_\eta(t)+o(1),
 \label{eq:sharp-asymptotic}$$ uniformly in real $t$.

Theorem [\[thm:diagonal-germ\]](#thm:diagonal-germ){reference-type="ref" reference="thm:diagonal-germ"} is the analytic core of the paper. It licenses a finite part, while the distinction visualized in [\[fig:quadratic-decomposition\]](#fig:quadratic-decomposition){reference-type="ref" reference="fig:quadratic-decomposition"} prevents that finite part from being called canonical without another axiom.

# Classification of natural quadratic counterterms {#sec:classification}

For a finite active set $F$, write $V_F=\mathbb C^F$. A real counterterm homogeneous of bidegree $(1,1)$ in the coefficient vector is uniquely $$C_{P,F}(a)=2a^*K_{P,F}a,
 \label{eq:quadratic-kernel}$$ where $K_{P,F}$ is Hermitian. We first classify naturality itself and only then impose convergence.

[\[thm:natural-kernels\]]{#thm:natural-kernels label="thm:natural-kernels"} The counterterm [\[eq:quadratic-kernel\]](#eq:quadratic-kernel){reference-type="eqref" reference="eq:quadratic-kernel"} is natural under transported pointed isomorphisms and compatible ambient active cutoffs if and only if $$\begin{aligned}
 K_{P',\phi F}&=U_\phi K_{P,F}U_\phi^*,
 \label{eq:kernel-equivariance}\\
 K_{P,F}&=K_{P,F'}|_{F\times F}
 \qquad(F\subset F').
 \label{eq:kernel-prefix}\end{aligned}$$ Equivalently, a natural quadratic counterterm is a compatible Hermitian kernel on ordered active-atom pairs, constant on pointed decorated isomorphism orbits.

This theorem is deliberately non-rigid. Its diagonal entries may be any equivariant real one-atom density. Its off-diagonal entries may be any equivariant Hermitian pair density. Naturality supplies transport and prefix rules, not a preferred density.

On the critical line, write a reflection-symmetric kernel as $k_{pq}=k_{qp}\in\mathbb R$. Its value on the native coefficient field is $$C_F(t)=2\sum_{p\in F}\frac{k_{pp}}p
 +4\sum_{p<q\in F}\frac{k_{pq}}{\sqrt{pq}}
 \cos\!\left(t\log\frac qp\right).
 \label{eq:critical-counterterm}$$

[\[thm:scheme-classification\]]{#thm:scheme-classification label="thm:scheme-classification"} The net $Q_F(t)-C_F(t)$ over arbitrary finite active subsets $F\nearrow\mathbb P$ converges absolutely and independently of the exhaustion order if and only if $$k_{pp}=C_\eta+r_p,
 \qquad
 \sum_p\frac{|r_p|}{p}<\infty,
 \label{eq:diag-classification}$$ and $$\sum_{p<q}\frac{|k_{pq}|}{\sqrt{pq}}<\infty,
 \label{eq:mixed-classification}$$ in addition to [\[eq:kernel-equivariance\]](#eq:kernel-equivariance){reference-type="eqref" reference="eq:kernel-equivariance"}--[\[eq:kernel-prefix\]](#eq:kernel-prefix){reference-type="eqref" reference="eq:kernel-prefix"}.

The diagonal condition fixes $C_\eta$ only modulo $\ell^1(p^{-1})$. The mixed condition leaves the complete weighted $\ell^1$ space as finite-scheme freedom. The native mixed kernel is already in that space by [\[thm:mixed-summability\]](#thm:mixed-summability){reference-type="ref" reference="thm:mixed-summability"}; no mixed subtraction is needed for convergence.

The phrase means independence of the enumeration or cofinal finite subsets inside the fixed ambient marked divisibility realization. It does not mean independence of every source recompilation, comparison object, or regulator. The Gram recompilation defect described in [2](#sec:category){reference-type="ref" reference="sec:category"} remains open.

A symmetric scalar function of the entire decorated Gram matrix is invariant under relabeling. One may also multiply a local counterterm by the indicator of a predeclared filtered-tower isomorphism class. These constructions can be formally natural without satisfying pair locality, additivity, or an independent source-normalization principle. Hence [\[thm:scheme-classification\]](#thm:scheme-classification){reference-type="ref" reference="thm:scheme-classification"} classifies the quadratic compatible-kernel class; it does not prove that every conceivable natural functional has local form.

# Explicit finite-scheme ambiguity {#sec:schemes}

The classification becomes concrete through two atomwise schemes. The *leading-only* counterterm is $$C_F^{\mathrm{lead}}
 =2C_\eta\sum_{p\in F}\frac1p.
 \label{eq:lead-counterterm}$$ It removes exactly the divergent prime-harmonic germ and leaves $$R_\eta^{\mathrm{lead}}(t)
 =2C_\eta P(1+2\eta)+M_\eta(t).
 \label{eq:lead-fp}$$ The diagonal tail is absolutely summable and carries no cutoff-order ambiguity.

The *full-diagonal* counterterm is $$C_F^{\mathrm{full}}
 =2\sum_{p\in F}\frac{G_{pp}}p.
 \label{eq:full-counterterm}$$ It is defined on every finite realized source and leaves $$R_\eta^{\mathrm{full}}(t)=M_\eta(t).
 \label{eq:full-fp}$$ It removes more than the divergence, but it violates neither transported isomorphism naturality nor active-prefix compatibility.

[\[cor:scheme-shift\]]{#cor:scheme-shift label="cor:scheme-shift"} The two counterterms and finite parts differ by $$\begin{aligned}
 C_F^{\mathrm{full}}-C_F^{\mathrm{lead}}
 &=2C_\eta\sum_{p\in F}p^{-1-2\eta},
 \label{eq:finite-shift-cutoff}\\
 R_\eta^{\mathrm{lead}}-R_\eta^{\mathrm{full}}
 &=2C_\eta P(1+2\eta)>0.
 \label{eq:finite-shift-limit}\end{aligned}$$ Therefore pointed-isomorphism naturality, active-cutoff compatibility, and absolute convergence fix the divergent germ but not a finite part.

The experiment specializes to $\eta=2$, where the normalized difference is $2\sum_pp^{-5}$. It also preregisters summable shifts $2\sum_pp^{-(5+k)}$, $k=0,1,2$, and rational combinations fixed before the controls. These examples are not needed for existence, but they demonstrate constructively that the ambiguity is a family rather than a binary choice.

## Sharp and Abel constants

An additional scheme choice appears when one subtracts an asymptotic rather than the atomwise harmonic sum. Mertens' theorem gives $$\sum_{p\le X}\frac1p
 =\log\log X+\mathfrak B_1+o(1)
 \label{eq:mertens}$$ [@Mertens1874]. Thus the sharp-$X$ convention is $$\operatorname{FP}_{\mathrm{sharp}}Q(t)
 =2C_\eta\bigl(\mathfrak B_1+P(1+2\eta)\bigr)+M_\eta(t).
 \label{eq:sharp-fp}$$

The prime-zeta expansion at $1$ satisfies $$P(1+\varepsilon)=\log(1/\varepsilon)+\mathfrak B_1-\gamma+o(1)
 \label{eq:prime-zeta-expansion}$$ [@Froberg1968]. Applying this Abel regulator to the diagonal while using dominated convergence for the absolutely summable pieces gives $$\operatorname{FP}_{\mathrm{Abel}}Q
 -\operatorname{FP}_{\mathrm{sharp}}Q=-2C_\eta\gamma.
 \label{eq:abel-sharp}$$ The discrepancy is a constant, so both schemes preserve the mixed phase and reflection. It nevertheless rules out regulator-independent canonicity.

The atomwise leading scheme [\[eq:lead-counterterm\]](#eq:lead-counterterm){reference-type="eqref" reference="eq:lead-counterterm"}, the sharp convention [\[eq:sharp-fp\]](#eq:sharp-fp){reference-type="eqref" reference="eq:sharp-fp"}, and the Abel convention are three different statements. Only the first is independent of the numerical ordering of active cutoffs after the marked tower has been fixed. The latter two explicitly use a cutoff/regulator coordinate.

# Generic mixed-Gram residues and the local no-go {#sec:no-go}

The mixed series is analytic surplus rather than analytic debt: it already converges absolutely. A diagonal subtraction cannot change it.

[\[thm:diagonal-invariance\]]{#thm:diagonal-invariance label="thm:diagonal-invariance"} Let $C_F^{\mathrm{diag}}$ be any diagonal quadratic counterterm. For real $t_1,t_2$, $$(Q_F-C_F^{\mathrm{diag}})(t_1)
 -(Q_F-C_F^{\mathrm{diag}})(t_2)
 =M_F(t_1)-M_F(t_2).
 \label{eq:diagonal-invariance}$$ In particular, a diagonal scheme cannot make a nonconstant control ledger constant or zero.

A diagonal term has no unordered-pair phase and is independent of the mixed frequencies. It cancels from the difference.

The obstruction is already visible on two atoms. For distinct positive marks and $G_{xy}\ne0$, the mixed ledger contains $$\frac{4G_{xy}}{\sqrt{\nu(x)\nu(y)}}
 \cos\!\left(t\log\frac{\nu(y)}{\nu(x)}\right).
 \label{eq:two-atom-frequency}$$ Nothing in [\[eq:two-atom-frequency\]](#eq:two-atom-frequency){reference-type="eqref" reference="eq:two-atom-frequency"} requires divisibility. It is a weighted overlap of two oblique source idempotents.

One might use a mixed counterterm to remove controls. Because such a term is not required for convergence, it must be justified by selectivity. We test the minimal class in which that justification could be local.

[\[thm:pair-local-no-go\]]{#thm:pair-local-no-go label="thm:pair-local-no-go"} Assume a counterterm is

1.  quadratic in the active coefficient vector;

2.  additive over diagonal atoms and unordered atom pairs;

3.  local to the pointed induced one-/two-atom datum;

4.  linear in the native Gram contraction on each pair;

5.  invariant under transported relabeling and forbidden to branch on printed numerical atom names.

Then no such rule can preserve the divisibility mixed mechanism while cancelling every matched nonzero mutated, composite-only, generic-DAG, and random-inventory control mechanism.

On one local pair type, write the mixed counterterm as $\beta G_{xy}$ times the native phase factor. The residual multiplier is $1-\beta$. Exact preservation of a nonzero baseline pair forces $1-\beta=1$, hence $\beta=0$. Exact cancellation of a nonzero control pair with the same transported local datum forces $1-\beta=0$, hence $\beta=1$. Local naturality applies the same $\beta$ to both. The requirements are incompatible.

The theorem is not a statistical claim. The exact suite enumerates the preregistered coefficient grid $$\{-2,-1,-\tfrac12,0,\tfrac12,1,2\}^2
 \label{eq:coefficient-grid}$$ and finds zero selective solutions among 49 combinations. The symbolic $\beta=0$ versus $\beta=1$ contradiction proves the result beyond that grid.

## The open nonlocal case

Bare naturality does not force a counterterm to be pair-local. A global coefficient may inspect an isomorphism invariant of the complete filtered tower. Formally, it may even multiply $M_P$ by the indicator of the tower isomorphism class of standard divisibility. This construction is label-blind after the class has been hard-coded, yet it merely repackages the complete inventory as an oracle.

We therefore distinguish three statements:

-   diagonal-only selectivity is refuted by [\[thm:diagonal-invariance\]](#thm:diagonal-invariance){reference-type="ref" reference="thm:diagonal-invariance"};

-   quadratic additive pair-local linear-Gram selectivity is refuted by [\[thm:pair-local-no-go\]](#thm:pair-local-no-go){reference-type="ref" reference="thm:pair-local-no-go"};

-   the existence of a nonlocal, independently motivated, cutoff-compatible divisibility-coherence functional is open.

Excluding the third class requires an axiom such as locality, descent, continuity, or controlled additivity that is motivated before the control outcomes.

# Ordinary trace, modified determinant, and a new functional {#sec:ownership}

The critical countable family satisfies $\mathcal B_{1/2+it}\in\bigcap_{r>2}\mathcal S_r$ but $\mathcal B_{1/2+it}\notin\mathcal S_2$. Hence $\mathcal B_s^2$ is not trace class on the critical line. The expression $Q_F$ remains an exact finite diagnostic; its renormalized limit is not an ordinary operator trace.

The third-regularized Fredholm determinant is an honest and separate object: $$\log\det\nolimits_3(I-z\mathcal B_s)
 =-\sum_{m\ge3}\frac{z^m}{m}\operatorname{Tr}(\mathcal B_s^m).
 \label{eq:det3-log}$$ It removes powers one and two in full. The chiral block has zero odd traces, so the first visible logarithmic coefficient is $$-\frac{z^4}{4}\operatorname{Tr}(\mathcal B_s^4).
 \label{eq:first-visible}$$ This fourth-order coefficient remains owned by $\det\nolimits_3$. Its generic control motion does not make the renormalized quadratic finite part selective.

For a declared finite-part scheme $\mathcal R$, define $$\mathfrak D_{\mathcal R}(s,z)
 :=\det\nolimits_3(I-z\mathcal B_s)
 \exp\!\left[-\frac{z^2}{2}
 \operatorname{FP}_{\mathcal R}\operatorname{Tr}(\mathcal B_s^2)\right].
 \label{eq:Dren}$$

Equation [\[eq:Dren\]](#eq:Dren){reference-type="eqref" reference="eq:Dren"} defines a new functional. It is not the ordinary Fredholm determinant, is not $\det_2$, and is not an alternative definition of $\det\nolimits_3$.

[\[prop:divisor\]]{#prop:divisor label="prop:divisor"} Suppose two finite parts differ by a holomorphic function $h(s)$ on the honest $\det\nolimits_3$ strip. Then $$\frac{\mathfrak D_{\mathcal R_2}(s,z)}{\mathfrak D_{\mathcal R_1}(s,z)}
 =\exp[-z^2h(s)/2].
 \label{eq:scheme-ratio}$$ The ratio is entire and zero-free in $z$. Therefore scheme changes do not alter the auxiliary-$z$ divisor, including multiplicities.

For leading-only and full-diagonal schemes, $h(s)=2C_\eta P(1+2\eta)$ is constant. The ratio is nontrivial, so the functionals differ, but it is zero-free, so their divisors agree. This agreement is analytic bookkeeping. It supplies no identification of those auxiliary zeros with any external target set.

The finite ledgers satisfy $Q_F(1-s)=Q_F(s)$, and $M_\eta(1-s)=M_\eta(s)$. Thus both minimal finite parts obey reflection. More generally, $$\mathfrak D_{\mathcal R}(1-s,z)=\mathfrak D_{\mathcal R}(s,z)
 \label{eq:Dren-reflection}$$ if and only if the chosen finite part is reflection symmetric. Reflection does not remove the weighted-$\ell^1$ scheme freedom in [\[thm:scheme-classification\]](#thm:scheme-classification){reference-type="ref" reference="thm:scheme-classification"}.

Standard singular traces do not fill the ownership gap. From the inherited similarity theorem and the prime number theorem, the partial singular-value sums of $\mathcal B^2$ grow only as $O(\log\log N)$. The usual Dixmier $1/\log N$ normalization therefore yields zero. A custom $\log\log$ normalization would introduce a new ideal and generalized limit; it would record a leading coefficient rather than the finite mixed functional. No Wodzicki, heat, or zeta-trace terminology is used without a source-native calculus.

# Exact preregistered audit {#sec:audit}

The exact artifact freezes $\eta=2$, factors out the common $C_\eta$, and uses the analytic divisibility Gram $$g_{pp}=1+p^{-4},
 \qquad
 g_{pq}=\frac1{(p^4+1)(q^4+1)}\quad(p\ne q).
 \label{eq:frozen-gram}$$ Finite control Grams are compiled directly from their own zeta, Möbius, and weight data. The code never queries primality or branches on printed numeric atom names; covers determine the active set.

L0.37rrrr Object & Atoms & Pairs & Mixed $\ne0$ & $B^4>0$\
Divisibility, cutoff 12 & 5 & 10 & 10 & 10\
Divisibility, cutoff 18 & 7 & 21 & 21 & 21\
Divisibility, cutoff 30 & 10 & 45 & 45 & 45\
Mutated cover & 8 & 28 & 3 & 3\
Composite-only inventory & 3 & 3 & 2 & 2\
Seeded generic DAG & 4 & 6 & 4 & 4\
Seeded random inventory & 5 & 10 & 9 & 9\

The baseline cutoffs contribute 76 pair rows, all with nonzero mixed coefficient and positive fourth-order descendant. The four control classes contribute 47 pair rows; 18 are nonzero mixed pairs and the same 18 have positive fourth-order coefficient $$\frac{4G_{pq}^2}{\nu(p)\nu(q)}>0.
 \label{eq:B4-pair}$$

The finite-scheme gate verifies the identity $$D_N/C_\eta
 =2\sum_{p\le N}p^{-1}+2\sum_{p\le N}p^{-5}
 \label{eq:experimental-shift}$$ at every baseline cutoff. The shift is positive and has a rational vanishing tail certificate. Five preregistered rational combinations of each of $S_0,S_1,S_2$ across the three cutoffs are atom-local, relabel-invariant, and prefix-additive. At least two residuals are exactly distinct.

Relabeled baseline copies at all three cutoffs reproduce the canonical analytic ledgers after transport. A separately relabeled generic DAG reproduces its directly compiled projector, Gram, mixed, and fourth-order ledgers. Compatible-prefix checks compare every old projector and every local counterterm increment. These gates detect hidden array-order or printed-label dependence.

The coefficient grid [\[eq:coefficient-grid\]](#eq:coefficient-grid){reference-type="eqref" reference="eq:coefficient-grid"} contains 49 combinations and returns zero selective solutions. The independent symbolic gate records the stronger contradiction: preservation requires $\beta=0$, while cancellation of a same-type nonzero control requires $\beta=1$.

The final evaluator reports 602/602 exact checks and 23/23 unit tests. The authority tables contain 76 baseline-pair rows, 47 control-pair rows, 15 scheme rows, 49 coefficient-grid rows, four determinant-power rows, five route-gate rows, seven comparison rows, and seven raw counterterm rows. Two fresh runs compare 30 artifacts and are byte-identical. The double-run certificate has SHA-256

7d788be24f16d7efbe52c25d199d9cb5815d096c3e30394dbc36f9e416195ec6.

The integrity audit passes with SHA-256

d7cf8bd141407f4e814569d9af762c831f2e93b344914c186f9057fe8cd5faa6.

All 32 entries in the canonical authority SHA ledger verify; that ledger has SHA-256

c146a7f3b8deb26a4eafa494ddfcb9269987b6898c197d2fb32768d7b6aae1df.

These exact checks validate the finite identities and the bounded control claim. They do not prove a no-go for arbitrary global functionals, do not turn a finite ledger into an ordinary trace, and do not evaluate any target-zero correspondence.

# Route decision, limitations, and open obligations {#sec:route}

The scoped theorem is a mathematical GO and an arithmetic-spectral STOP. It constructs and classifies finite parts, but it shows that the most natural retained phase is generic within the tested local class.

L0.20L0.19Y Gate & Status & Reason\
A0 structural arithmetic relation & A0: structural arithmetic relation & The cover predicate and Möbius incidence compiler are source-derived.\
A1 fixed self-adjoint operator & A1: fail & The critical construction remains a parameter-dependent family, not one fixed operator carrying the parameter as spectrum.\
A2 analytic determinant & A2: analytic determinant & The inherited $\det\nolimits_3$ is honest on its proved Schatten strip. The new $\mathfrak D_{\mathcal R}$ is scheme-dependent and receives no separate gate.\
A3 target equivalence & A3: fail & No equivalence to an external target-zero condition is stated or tested.\
A4 arithmetic selectivity & A4: fail & The mixed and fourth-order pair mechanisms survive every preregistered control class.\

The resulting tuple is

(A0\_STRUCTURAL\_ARITHMETIC\_RELATION, A1\_FAIL,\
A2\_ANALYTIC\_DETERMINANT, A3\_FAIL, A4\_FAIL).

Thus `ROUTE_A_REJECTED`. Route B is locked and has not been opened.

## What has been stopped

The result supports four stop decisions:

-   `STOP_POSITIVE_DIAGONAL_SUBTRACTION_CLAIM`: subtraction exists, but it does not produce a selective positive completion;

-   `STOP_CANONICAL_FINITE_PART_CLAIM`: explicit summable natural shifts and the sharp/Abel discrepancy prevent canonicity;

-   `STOP_PAIRWISE_MIXED_ARITHMETIC_SELECTIVITY`: local Gram motion survives the controls;

-   `STOP_INCIDENCE_ROUTE_AFTER_NO_GO`: another same-object local completion is not justified.

The positive result is `GO_SCOPED_RENORMALIZATION_RIGIDITY_PAPER`.

## Limitations

#### Nonlocal tower invariants.

The main no-go assumes a quadratic, additive, pair-local rule linear in the native Gram contraction. Bare isomorphism naturality permits nonlinear and nonlocal invariants of an entire filtered source. Their existence, useful normalization, and exclusion remain open.

#### Finite-source recompilation.

The main theorem uses an ambient compiled Gram kernel and active cutoffs. Recompiling inside a growing finite source can change upper-tail Gram terms. The resulting embedding defect may have a useful cocycle description, but no such theorem is claimed here.

#### Control towers.

A standalone finite control has no canonical asymptotic constant equal to $C_\eta$. The controls test local mixed mechanisms and transported finite schemes. They do not inherit the divisibility leading germ by declaration.

#### Regulators and trace properties.

Sharp and Abel finite parts are named schemes. No heat kernel, elliptic weight, meromorphic incidence zeta family, cyclic extension, or relative reference-independence theorem has been constructed. Standard pseudodifferential or singular-trace terminology would exceed the proof.

#### Search and experiments.

The primary-source audit is bounded by its named mathematical neighborhoods and date. Exact finite controls expose the pair-local mechanism but do not sample every finite pointed poset or establish a universal empirical law.

## Minimum obligation for a successor

Any successor must preregister either a nonlocal divisibility-coherence functor or a theorem excluding its entire motivated class. A positive functor must be independent of printed labels, compatible with every declared cutoff comparison, exhaustion/reference independent, and exactly absent on mutated, composite-only, generic-DAG, and random-inventory controls. A negative theorem must state the locality, continuity, descent, or additivity axioms that exclude tower inventory oracles. Another block completion, positive metric, or tuned global predicate does not meet this obligation.

# Conclusion {#sec:conclusion}

The critical incidence quadratic ledger can be renormalized, but its finite part is not selected by the naturality available here. The exact Gram formula separates one diagonal prime-harmonic divergence from an absolutely summable diagonal tail and an absolutely summable mixed phase. Natural quadratic counterterms are compatible equivariant pair kernels. Absolute exhaustion independence fixes the diagonal coefficient only modulo $\ell^1(p^{-1})$ and leaves a weighted-$\ell^1$ mixed-kernel freedom. Leading-only and full-diagonal schemes realize this ambiguity explicitly; sharp and Abel conventions add a second exact scheme discrepancy.

The retained mixed phase is analytically valid and arithmetically nonselective. Diagonal schemes leave it untouched. In the quadratic, additive, pair-local linear-Gram class, the same local coefficient cannot preserve a divisibility pair and cancel a matched control pair. Exact mutated, composite-only, generic-DAG, and random-inventory fixtures realize the generic mechanism.

Restoring a chosen finite part beside $\det\nolimits_3$ defines a useful new functional, but it does not repair determinant ownership. Scheme changes are zero-free quadratic exponentials and leave the auxiliary divisor unchanged. The ordinary quadratic trace and $\det_2$ remain absent.

The correct endpoint is therefore a scoped rigidity theorem and a stop rule. The local chiral-incidence counterterm route is exhausted. The only open same-source direction is a genuinely global divisibility-coherence invariant with an independent normalization and exact control separation, or a theorem excluding that class under motivated axioms.

# Proof details {#app:proofs}

## Rank-one factorization and transport

Since $E_x=e_xe_x^{\mathsf T}$, $$q_x=ZE_xM=(Ze_x)(e_x^{\mathsf T}M)=u_xv_x^{\mathsf T}.$$ The definitions of $u_x,v_x$ follow from the entries of $Z$ and $M$. Moreover, $$q_y^\sharp=W^{-1}v_yu_y^{\mathsf T}W,$$ and hence $$\begin{aligned}
 q_xq_y^\sharp
 &=u_x(v_x^{\mathsf T}W^{-1}v_y)u_y^{\mathsf T}W,\\
 \operatorname{Tr}(q_xq_y^\sharp)
 &=(v_x^{\mathsf T}W^{-1}v_y)(u_y^{\mathsf T}Wu_x).\end{aligned}$$ This proves [\[prop:general-gram\]](#prop:general-gram){reference-type="ref" reference="prop:general-gram"}. If $U_\phi$ is the permutation matrix of a transported pointed isomorphism, then $$q'_{\phi x}=U_\phi q_xU_\phi^{-1},
 \qquad
 W'=U_\phi WU_\phi^*,$$ so $G'_{\phi x,\phi y}=G_{xy}$.

## Divisibility Euler factors

For a cover $p$, the lower-cone factor is $1+p^{2\eta}$. The upper-tail factor is $$\sum_{p\mid b}\frac{\mu(p,b)^2}{b^{2\eta}}
 =p^{-2\eta}\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
 =p^{-2\eta}C_\eta.$$ Their product is [\[eq:Gdiag\]](#eq:Gdiag){reference-type="eqref" reference="eq:Gdiag"}.

For $p\ne q$, the only common lower bound is $1$. A common upper-tail term with nonzero Möbius factors is $b=pqk$, where $k$ is squarefree and coprime to $pq$. The two Möbius signs have product $+1$, so $$\begin{aligned}
 G_{pq}
 &=(pq)^{-2\eta}
   \sum_{\substack{k\ge1\\(k,pq)=1}}
   \frac{\mu(k)^2}{k^{2\eta}}\\
 &=C_\eta\frac{(pq)^{-2\eta}}
 {(1+p^{-2\eta})(1+q^{-2\eta})}.\end{aligned}$$ This proves [\[thm:atom-gram\]](#thm:atom-gram){reference-type="ref" reference="thm:atom-gram"} without a numeric prime list.

## Normal convergence

Equation [\[eq:Gmixed\]](#eq:Gmixed){reference-type="eqref" reference="eq:Gmixed"} implies $$0<G_{pq}\le C_\eta(pq)^{-2\eta}.$$ With $\alpha=2\eta+1/2>1$, $$\sum_{p<q}\frac{4G_{pq}}{\sqrt{pq}}
 \le2C_\eta\left(\sum_pp^{-\alpha}\right)^2<\infty.$$ The Weierstrass test gives uniform convergence on the critical line. If at least one atom exceeds $X$, replace the corresponding prime tail by $\sum_{n>X}n^{-\alpha}=O(X^{1-\alpha})$. This proves [\[eq:mixed-tail\]](#eq:mixed-tail){reference-type="eqref" reference="eq:mixed-tail"}.

For complex $s$, the two terms in [\[eq:mixed-holo\]](#eq:mixed-holo){reference-type="eqref" reference="eq:mixed-holo"} are dominated by products with exponents $2\eta+\Re s$ and $2\eta+1-\Re s$. Both exceed one on compact subsets of $1-2\eta<\Re s<2\eta$. Normal convergence gives holomorphy, and exchanging $p,q$ gives reflection.

## Kernel classification

Polarization gives the unique Hermitian $K_{P,F}$ in [\[eq:quadratic-kernel\]](#eq:quadratic-kernel){reference-type="eqref" reference="eq:quadratic-kernel"}. Under an isomorphism, the transported vector is $U_\phi a$. Equality $$a^*K_{P,F}a=(U_\phi a)^*K_{P',\phi F}(U_\phi a)$$ for every $a$ is equivalent, after polarization, to [\[eq:kernel-equivariance\]](#eq:kernel-equivariance){reference-type="eqref" reference="eq:kernel-equivariance"}. Equality on every vector supported in an old set $F\subset F'$ is likewise equivalent to [\[eq:kernel-prefix\]](#eq:kernel-prefix){reference-type="eqref" reference="eq:kernel-prefix"}.

Absolute convergence of the residual diagonal is $$\sum_p\frac{|G_{pp}-k_{pp}|}{p}<\infty.$$ Because $G_{pp}-C_\eta=C_\eta p^{-2\eta}$ is already in $\ell^1(p^{-1})$, this condition is equivalent to [\[eq:diag-classification\]](#eq:diag-classification){reference-type="eqref" reference="eq:diag-classification"}. The native mixed kernel belongs to the weighted $\ell^1$ space by [\[thm:mixed-summability\]](#thm:mixed-summability){reference-type="ref" reference="thm:mixed-summability"}; triangle inequalities then make residual mixed convergence equivalent to [\[eq:mixed-classification\]](#eq:mixed-classification){reference-type="eqref" reference="eq:mixed-classification"}. Absolute convergence removes dependence on the enumeration of finite active sets.

## Sharp--Abel discrepancy

The sharp finite part uses the constant $\mathfrak B_1$ in [\[eq:mertens\]](#eq:mertens){reference-type="eqref" reference="eq:mertens"}. The Abel regulator uses the constant $\mathfrak B_1-\gamma$ in [\[eq:prime-zeta-expansion\]](#eq:prime-zeta-expansion){reference-type="eqref" reference="eq:prime-zeta-expansion"}. The diagonal tail and mixed series are absolutely summable, so dominated convergence carries them unchanged between the two limits. Multiplication by the coefficient $2C_\eta$ proves [\[eq:abel-sharp\]](#eq:abel-sharp){reference-type="eqref" reference="eq:abel-sharp"}.

## Scheme-independent divisor

If two finite parts differ by $h(s)$, cancellation of the common $\det\nolimits_3$ factor gives [\[eq:scheme-ratio\]](#eq:scheme-ratio){reference-type="eqref" reference="eq:scheme-ratio"}. The complex exponential never vanishes. Therefore its product with a holomorphic function preserves the zero divisor in $z$, including multiplicity. This statement concerns only the auxiliary determinant variable and supplies no external spectral identification.

# Scope, reproducibility, and declarations {#app:scope}

## Claim boundary

The proved no-go covers quadratic, reference-independent counterterms and, for arithmetic selectivity, the additional additive pair-local linear-Gram class. It does not cover arbitrary nonlinear or nonlocal invariants of an entire filtered tower. Pointed isomorphisms transport decorations; printed numeric names are not source data. Compatible embeddings have order-ideal image and the main limit uses ambient active restriction, not repeated finite-source recompilation.

The finite expression $Q_F$ is not an ordinary countable trace. The new $\mathfrak D_{\mathcal R}$ is not an ordinary Fredholm determinant or $\det_2$. No auxiliary-$z$ zero is identified with an external target zero. Route B is locked, and no target-zero locations, labels, counts, or statistics are used.

## Data and code availability

The paper uses exact finite symbolic artifacts rather than empirical or personal data. The frozen experiment package, its per-artifact SHA ledger, and its double-run certificate are identified in the source lock associated with this manuscript. No new human-subject, animal-subject, or sensitive dataset was created or analyzed.

## Ethics statement

Ethics approval and informed consent are not applicable because the work is mathematical and uses no human participants, animals, or private records.

## Author contributions

The anonymous authors are responsible for conceptualization, formal analysis, methodology, validation, visualization, and writing. All authors approved the manuscript and accept responsibility for its claims.

## Funding and competing interests

No external funding is declared. The authors declare no competing interests.

## AI-use disclosure

AI-assisted research and writing tools were used for source-search strategy, proof organization, exact-artifact integration, drafting, and formatting. All mathematical claims, citations, and scope boundaries were checked against the frozen proof, experiment, and primary-literature artifacts. The authors take responsibility for the accuracy and integrity of the manuscript.

## Review policy

At the request governing this batch, no manuscript review loop was run. Formula, source, citation, route, exact-evidence, compilation, font, metadata, control-byte, and visual audits were retained. The absence of a review loop does not relax any ownership or scope declaration above.
