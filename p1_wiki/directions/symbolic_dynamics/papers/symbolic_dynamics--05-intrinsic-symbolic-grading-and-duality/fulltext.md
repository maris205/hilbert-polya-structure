---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--05-intrinsic-symbolic-grading-and-duality"
canonical_tex: "symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality/main.tex"
canonical_pdf: "symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality/main.pdf"
source_sha256: "e9d32bbf79c96ab8b06e43b2fca3605837dbd8ea0c94b88dcd3195c503099f76"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Tensor-Atom Exterior Transfer for Full Shifts: Möbius Supertrace and a Critical-Strip Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/05-intrinsic-symbolic-grading-and-duality/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give the tensor-prime full-shift transfer of SD-C07 an intrinsic factorization grading. For the open tensor-divisor interval of $F_n$, the reduced order complex has the homology of $S^{\omega(n)-2}$ when $n$ is squarefree and is contractible otherwise. Its supertrace is therefore $\mu(n)$. Placing tensor atoms in the resulting odd degree gives, for $\operatorname{Re}s>1$, $$\operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(\mathcal L_s)=\zeta(s)^{-1},
   \qquad
   \operatorname{Ber}_{V_{\bar1}}(I-\mathcal L_s)=\zeta(s).$$ This fixes the Euler determinant orientation, but it does not complete the zeta function. The honest equivariant Koszul resolution cancels its bosonic and fermionic factors to supertrace one. Natural symbolic reversal gives $s\mapsto s$, while tensor-group inversion gives $s\mapsto-s$. Even after granting a target-centered $s\leftrightarrow1-s$ pairing, the first common Schatten regularization is a paired $\det_3$ on $1/3<\operatorname{Re}s<2/3$; it is zero-free and deletes the prime and prime-square traces. An exact CPU audit checks all $511$ factorization complexes through $n=512$, with no chain, Möbius, or homology mismatch, and rejects random, Liouville, shifted-law, additive, and free-mixing controls. The stage reaches graded A2 but not A3: no new candidate is assigned and Route B remains locked.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Tensor-Atom Exterior Transfer for Full Shifts:\
  Möbius Supertrace and a Critical-Strip Obstruction
```

## Markdown 正文

# Introduction

The preceding symbolic construction in this project reached a precise but asymmetric Euler determinant. The tensor atoms of finite full shifts are the full $p$-shifts, their topological entropy is $\log p$, and a diagonal atom-loop suspension has weighted transfer $$\mathcal L_s e_p=p^{-s}e_p,\qquad
  \det(I-\mathcal L_s)=\zeta(s)^{-1}$$ for $\operatorname{Re}s>1$. The arithmetic source, primitive/repetition ledger, and Fredholm determinant all belong to one symbolic object. What remained missing was not another prime generator. It was an intrinsic orientation and a dual analytic structure capable of seeing the critical strip.

This paper makes the strongest source-locked version of that bet. We build gradings and dualities only from the symmetric monoidal skeleton of finite full shifts. The first construction works: factorization topology declares each tensor atom odd and recovers the Möbius coefficient. The other constructions fail in informative ways. The honest Koszul resolution cancels the entire Euler signal to the vacuum; symbolic time reversal preserves the spectral variable; and group inversion reflects it about zero rather than one half.

shows the resulting logic. The strongest adversarial escape is particularly useful. A paired regularized determinant can be defined in a strip around $\operatorname{Re}s=1/2$ once Schatten order three is allowed. It even has the desired reflection symmetry. Yet regularization removes the first two trace powers, exactly the prime and prime-square terms that carry the decisive arithmetic ledger. Visible symmetry therefore does not imply a Riemann divisor.

The contributions are:

1.  We derive the integral homology of every tensor-divisor order complex and identify its supertrace with $\mu(n)$. The empty prime interval places atoms in canonical odd degree.

2.  We separate three often-conflated objects: factorization homology, the zero-differential exterior transfer module, and the honest equivariant Koszul resolution. Their supertraces are respectively $1/\zeta(s)$, $1/\zeta(s)$, and $1$.

3.  We prove that stable/unstable reversal gives $s\mapsto s$, tensor inversion gives $s\mapsto-s$, and the first adversarial $s\leftrightarrow1-s$ Schatten determinant is zero-free and loses $r=1,2$.

4.  We certify the chain and coefficient statements exactly through $n=512$ and run controls designed to expose arbitrary parity and proves-too-much monoids.

The conclusion is deliberately forward-looking but not promotional. The A2 orientation problem is solved after choosing the exterior functor. The A3 problem is now a sharply posed search for a source-derived symbolic half-density or modular character. No SD-C08 is created by the present stage, and no zero data or Route-B mechanism is used.

# Related work and claim boundary

#### Full shifts, products, and zeta determinants.

For a finite-state shift, the Bowen--Lanford formula expresses the zeta function by a determinant [@bowenlanford1970]. Product structure and entropy of topological Markov shifts are classical [@lind1984]. The present paper inherits the full-shift tensor source from SD-C07 and does not claim these facts as new. Its question is narrower: whether functorial grading of that object monoid improves its Route-A analytic structure.

#### Exterior automata.

The closest same-family collision is Béal's exterior-power construction for deterministic automata [@beal1995]. Alternating determinants of exterior automata perform inclusion--exclusion among labeled presentations of a sofic shift. We therefore do not claim the first exterior power, superdeterminant, or alternating zeta in symbolic dynamics. Our exterior degree is indexed instead by finite subsets of categorical tensor atoms. It controls the squarefree factorization ledger rather than multiplicity of labeled paths.

#### Signed symbolic homology.

Putnam develops homology and a Lefschetz formula for Smale spaces [@putnam2014]; Deeley gives a signed theory and signed zeta [@deeley2018]. Product and Künneth structures for dynamical groupoid homology are also known [@proiettiyamashita2025]. Those theories show that graded trace formulas and monoidal homology are established subjects. They do not, however, attach the factorization-poset degree used here to the countable tensor-atom inventory. Indeed, signed SFT homology collapses to its degree-zero signed dimension group in the basic examples, whereas our nontrivial degree comes from object factorization before atom orbitification.

#### Möbius and Koszul algebra.

Poset Möbius functions and their Euler-characteristic interpretation go back to @rota1964; Koszul resolutions are standard [@priddy1970]. The divisor-lattice homology theorem below is thus a transport of known combinatorics through the full-shift tensor monoid, not a new theorem about arbitrary posets. The useful contribution is the distinction it forces: the exterior transfer module gives the Möbius Euler factor, while an honest equivariant Koszul resolution adds a symmetric algebra factor and cancels to the vacuum.

#### Reversal and stable/unstable duality.

Flip systems have their own zeta relations [@kimleepark2003], and shifts of finite type admit K-theoretic dualities [@kaminkerputnam1997]. These results motivate a stable/unstable test but do not assert a Riemann functional equation. At the elementary symbolic level, transposition or time reversal preserves the same entropy weight. The missing reflection center is therefore an additional datum, not a consequence of reversal alone.

Our defensible novelty claim is a synthesis and audit. We did not locate in these primary sources the exact combination of the finite-full-shift tensor monoid, factorization/exterior degree on its categorical atoms, and a Route-A test of the resulting Riemann Euler orientation and completion obstruction. We make no claim of analytic continuation, a Gamma factor, or a completed-$\xi$ determinant.

# Tensor-divisor factorization homology

Let $F_n=\{1,\ldots,n\}^{\mathbb Z}$ be the two-sided full $n$-shift and let $\mathsf{FSh}$ denote the symmetric monoidal skeleton generated by these shifts under Cartesian product. Coordinatewise pairing gives $$F_m\boxtimes F_n\cong F_{mn},
  \qquad
  h_{\mathrm{top}}(F_n)=\log n.$$ Thus $\operatorname{Iso}(\mathsf{FSh})\cong(\mathbb N_{\ge1},\times)$, and its nonunit tensor atoms are $F_p$.

For $n>1$, let $$P_n=(F_1,F_n)$$ be the open tensor-divisor interval and let $\Delta_n=\Delta(P_n)$ be its order complex. We use the augmented reduced chain convention: if $P_n$ is empty, $\widetilde C_{-1}(\Delta_n)=\mathbb Z$.

[\[thm:factorization-homology\]]{#thm:factorization-homology label="thm:factorization-homology"} For every $n>1$, $$\widetilde H_j(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,& n\text{ squarefree and }j=\omega(n)-2,\\
0,& n\text{ not squarefree}.
\end{cases}$$ Consequently $$\widetilde\chi(\Delta_n)=\mu(n).$$

Write $n=\prod_{i=1}^k p_i^{a_i}$. The closed divisor interval is the product $\prod_i[0,a_i]$. Use its atoms as a crosscut. If every $a_i=1$, the crosscut complex contains every proper subset of the $k$ atoms but not their full set; it is the boundary of a $(k-1)$-simplex and hence $S^{k-2}$. If some $a_i>1$, the join of all atoms is $F_{\operatorname{rad}(n)}<F_n$, so the crosscut complex is a full simplex and is contractible. The crosscut theorem gives the asserted homotopy types. The case $n=p$ is the empty complex $S^{-1}$.

The prime interval has its generator in degree $-1$, which is odd modulo two. A product of $k$ distinct tensor atoms contributes in degree $k-2$, with sign $$(-1)^{k-2}=(-1)^k=\mu(n).$$ Repeated atoms make the complex contractible rather than adding another signed occupation. This is precisely the exterior exclusion missing from the Liouville character $(-1)^{\Omega(n)}$.

[\[cor:homology-supertrace\]]{#cor:homology-supertrace label="cor:homology-supertrace"} Adjoin the tensor unit in even degree and define $$\mathcal H_{\mathrm{fac}}
=\mathbb C\mathbf 1\oplus
\bigoplus_{n\ge2}\widetilde H_\bullet(\Delta_n;\mathbb C).$$ Let $W_s$ act as $n^{-s}$ on the $n$-summand. For $\operatorname{Re}s>1$, $$\operatorname{Str}(W_s)
 =\sum_{n\ge1}\mu(n)n^{-s}
 =\frac1{\zeta(s)}.$$

The grading is invariant under relabeling tensor atoms. Simplex orientation is not a physical sign: changing an oriented basis conjugates adjacent boundary matrices by diagonal sign matrices and leaves both homology and supertrace unchanged. The intrinsic datum is chain degree, not a chosen orientation of each simplex.

# Exterior transfer and the Koszul cancellation

Let $$V=\bigoplus_{p}\mathbb C e_p,
 \qquad
 \mathcal L_s e_p=p^{-s}e_p.$$ The completion of $V$ is the same atom space used by SD-C07. The operator is trace class exactly for $\operatorname{Re}s>1$.

## The exterior transfer module

Place $V$ in odd degree and form the zero-differential exterior transfer module $\Lambda^\bullet V$. Once this functor is selected, the vacuum is even and tensor atoms are odd by [\[thm:factorization-homology\]](#thm:factorization-homology){reference-type="ref" reference="thm:factorization-homology"}.

[\[thm:exterior\]]{#thm:exterior label="thm:exterior"} For $\operatorname{Re}s>1$, $$\begin{aligned}
 \operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(\mathcal L_s)
 &=\det(I-\mathcal L_s)
 =\prod_p(1-p^{-s})
 =\zeta(s)^{-1}, \label{eq:exterior}\\
 \operatorname{Ber}_{V_{\bar1}}(I-\mathcal L_s)
 &=\det(I-\mathcal L_s)^{-1}
 =\zeta(s). \label{eq:berezinian}\end{aligned}$$

Finite exterior occupation gives a factor $1-p^{-s}$ for each atom. Absolute convergence in $\operatorname{Re}s>1$ identifies the product with the Fredholm determinant. With the convention $\operatorname{Ber}(A)=\det(A_{\bar0})/\det(A_{\bar1})$, a purely odd one-particle space places that determinant in the denominator.

Equations [\[eq:exterior\]](#eq:exterior){reference-type="eqref" reference="eq:exterior"} and [\[eq:berezinian\]](#eq:berezinian){reference-type="eqref" reference="eq:berezinian"} fix the orientation ambiguity of the ungraded object, but only after the exterior functor has been chosen. The bare commutative tensor monoid also admits the trivial grading; it does not force exteriorization. The accurate statement is therefore: selection of the functor is a modeling choice, while the parity inside that functor is canonical.

## The honest Koszul resolution

The phrase *Koszul determinant* can hide a different object. Let $$A=\mathbb C[M]\cong\mathbb C[x_p:p\in\mathbb P],
 \qquad I=(x_p),
 \qquad V\cong I/I^2.$$ The standard Koszul resolution is $$\mathcal K=A\otimes\Lambda^\bullet V$$ with $$d(x^\alpha\otimes e_{p_1}\wedge\cdots\wedge e_{p_k})
=\sum_{j=1}^k(-1)^{j-1}
x^{\alpha+e_{p_j}}\otimes
e_{p_1}\wedge\cdots\widehat e_{p_j}\cdots\wedge e_{p_k}.$$ Define the total-mass transfer $$T_s(x^\alpha\otimes e_S)
 =\bigl(N(\alpha)N(S)\bigr)^{-s}
   x^\alpha\otimes e_S.$$ Because the differential moves one atom from the exterior factor into the monomial factor, it preserves total mass and commutes with $T_s$.

[\[thm:koszul-cancel\]]{#thm:koszul-cancel label="thm:koszul-cancel"} For $\operatorname{Re}s>1$, $$\operatorname{Tr}(T_s)
 =\zeta(s)\prod_p(1+p^{-s})
 =\frac{\zeta(s)^2}{\zeta(2s)},
 \qquad
 \operatorname{Str}(T_s)=1.$$ Moreover $\operatorname{Str}(T_s^r)=1$ for every $r\ge1$, and $$\operatorname{sdet}(I-zT_s)=1-z.$$

The symmetric algebra contributes $\prod_p(1-p^{-s})^{-1}$, while the exterior supertrace contributes $\prod_p(1-p^{-s})$. They cancel factorwise. Replacing $s$ by $rs$ proves the power-supertrace identity. The logarithmic superdeterminant formula then reduces to $-\sum_{r\ge1}z^r/r=\log(1-z)$.

The honest equivariant resolution has only vacuum homology, exactly as its Lefschetz supertrace predicts. The Riemann Euler factor belongs to the exterior transfer module or the factorization-homology direct sum; it does not survive the standard Koszul resolution.

0.97L0.23L0.26X Object & Graded trace in $\operatorname{Re}s>1$ & Meaning\
Factorization homology & $\sum_n\mu(n)n^{-s}=1/\zeta(s)$ & Order-complex degree by tensor mass\
Exterior transfer module & $\operatorname{Str}\Gamma_-(\mathcal L_s)=1/\zeta(s)$ & Fermionic occupation of distinct atoms\
Odd one-particle space & $\operatorname{Ber}(I-\mathcal L_s)=\zeta(s)$ & A2 determinant orientation\
Equivariant Koszul resolution & $\operatorname{Str}T_s=1$ & Bosonic/exterior cancellation to vacuum\
Liouville character & $\sum(-1)^{\Omega(n)}n^{-s}=\zeta(2s)/\zeta(s)$ & Multiplicity parity, no exclusion\

# Three duality tests

The determinant orientation in [\[thm:exterior\]](#thm:exterior){reference-type="ref" reference="thm:exterior"} does not explain why a completed object should relate $s$ and $1-s$. We test three constructions that remain attached to the same symbolic source.

## Stable/unstable symbolic reversal

Let $V^s$ and $V^u$ be stable and unstable copies of the tensor-atom space, and let $J:V^s\to V^u$ be induced by reversal of the corresponding two-sided full shifts. Reversal preserves alphabet size and entropy.

[\[prop:reversal\]]{#prop:reversal label="prop:reversal"} The natural chain transfer is $$\mathcal L_s\oplus\mathcal L_s,
  \qquad J\mathcal L_s=\mathcal L_sJ.$$ Its ordinary determinant is $\zeta(s)^{-2}$ and its superdeterminant is one in $\operatorname{Re}s>1$. Replacing the unstable block by $\mathcal L_{1-s}$ breaks the chain identity except at $s=1/2$.

Both copies of $F_p$ have entropy $\log p$, so both diagonal weights are $p^{-s}$. Equality $J\mathcal L_s=\mathcal L_{1-s}J$ would require $p^{-s}=p^{-(1-s)}$ for every atom, which holds only at the center.

There is also no ordinary Fredholm overlap: $\mathcal L_s$ is trace class for $\operatorname{Re}s>1$, while $\mathcal L_{1-s}$ is trace class for $\operatorname{Re}s<0$. Time reversal therefore supplies the familiar transpose/reversal invariance of a symbolic determinant, not the Riemann reflection.

## Tensor group completion

The group completion of the object monoid is $$G=M^{\mathrm{gp}}\cong\mathbb Q_{>0}^{\times}
  \cong\bigoplus_p\mathbb Z.$$ Inversion sends $q^{-s}$ to $q^s=q^{-(-s)}$.

[\[prop:inversion\]]{#prop:inversion label="prop:inversion"} For every monoidal grading $\varepsilon:G\to\mathbb Z/2\mathbb Z$, $$\varepsilon(g^{-1})=-\varepsilon(g)=\varepsilon(g).$$ Thus group inversion cannot flip determinant parity and naturally implements $s\mapsto-s$, not $s\mapsto1-s$.

Centering $u=s-1/2$ rewrites $$p^{-s}=p^{-1/2}p^{-u},
 \qquad
 p^{-(1-s)}=p^{-1/2}p^u.$$ The shared factor $p^{-1/2}$ is a half-density character. Entropy permits one to write it, but the bare tensor skeleton contains no principle that selects the coefficient $1/2$. Choosing it because the target functional equation has that center would be circular.

## Adversarial Schatten regularization

We now grant the missing half-density pairing and ask whether regularized determinants could rescue the critical strip. This is an obstruction test, not a promoted candidate.

[\[thm:schatten\]]{#thm:schatten label="thm:schatten"} For $q\ge1$, $$\mathcal L_s\in\mathcal S_q\iff q\operatorname{Re}s>1,
 \qquad
 \mathcal L_{1-s}\in\mathcal S_q\iff q(1-\operatorname{Re}s)>1.$$ There is no common $\mathcal S_1$ or $\mathcal S_2$ domain. The first integer order with an overlap is $q=3$, on $$\frac13<\operatorname{Re}s<\frac23.$$

The $q$-th singular-value sum is $\sum_p p^{-q\operatorname{Re}s}$. It converges exactly when $q\operatorname{Re}s>1$. Applying the same calculation to $1-s$ gives the second condition. The common interval is $1/q<\operatorname{Re}s<1-1/q$, which is nonempty first for $q=3$.

[\[thm:det3\]]{#thm:det3 label="thm:det3"} On $1/3<\operatorname{Re}s<2/3$, define $$D_3(s)
 =\det\nolimits_3(I-\mathcal L_s)
  \det\nolimits_3(I-\mathcal L_{1-s}).$$ Then $D_3(s)=D_3(1-s)$, but $D_3$ is zero-free throughout this strip and $$\log D_3(s)
 =-\sum_{r\ge3}\frac1r
  \sum_p\left(p^{-rs}+p^{-r(1-s)}\right).$$

The regularized determinant identity starts at trace power $r=3$. Both diagonal blocks have spectral radius less than one in the open strip, so none of their regularized factors vanishes. Reflection swaps the two factors.

The symmetry is exact but sterile. It has removed the $r=1$ prime trace and the $r=2$ prime-square trace. Restoring them requires counterterms with no common nuclear definition near the critical line. The first regularization that enters the desired region therefore loses the arithmetic divisor it was meant to complete.

0.98L0.20L0.20X Construction & Natural involution & Decisive outcome\
Stable/unstable reversal & $s\mapsto s$ & Same entropy block; superdeterminant cancels\
Group completion & $s\mapsto-s$ & Inversion parity-even; no selected center\
Forced Fredholm pair & $s\mapsto1-s$ & Trace-class domains are disjoint\
Paired $\det_3$ & $s\mapsto1-s$ & Shared strip, but zero-free and omits $r=1,2$\

# Exact experiment and adversarial controls

The implementation constructs $\Delta_n$ from the tensor-divisibility relation for every $2\le n\le512$. Candidate-side code sees the registered full-shift objects, their tensor table, unit, and entropy norm. A separate factorization routine is used only after construction to score the predicted squarefree homology pattern. No prime or Riemann-zero table enters the candidate.

## Exact chain and coefficient census

All $511$ augmented complexes pass the integer identity $\partial^2=0$. Their reduced Euler characteristics and homology supertraces equal $\mu(n)$ without exception. The computed $\mathbb F_2$ Betti numbers match the integral theorem in [\[thm:factorization-homology\]](#thm:factorization-homology){reference-type="ref" reference="thm:factorization-homology"}: squarefree fibers have one generator in degree $\omega(n)-2$, and nonsquarefree fibers are reduced acyclic.

::: {#tab:complex-audit}
    $N$   objects   $\partial^2$   Euler $=\mu$   homology $=\mu$   simplices
  ----- --------- -------------- -------------- ----------------- -----------
     64        63          1.000          1.000             1.000         440
    128       127          1.000          1.000             1.000       1,441
    256       255          1.000          1.000             1.000       4,742
    512       511          1.000          1.000             1.000      15,629

  : Exact factorization-complex audit. Simplices include the augmented empty generator.
:::

At $N=512$, the construction recovers $97$ tensor atoms. The largest fiber is $n=480$, with $976$ simplices and maximum chain dimension seven. The odd one-particle Berezinian and exterior-Fock series reproduce all $512$ coefficients of $\zeta$ and $1/\zeta$, respectively.

## Parity controls

The controls are designed to distinguish homological degree from a useful looking sign:

-   A global nonunit parity flip matches only $199/512$ Möbius coefficients and breaks coprime multiplicativity in $740$ of $2347$ cases.

-   Across $32$ deterministic random simplex parities, only $0.500707$ of boundary incidences are odd on average; canonical chain degree gives $1.000$.

-   Sixty-four random atom characters stay multiplicative but achieve mean squarefree sign accuracy $0.492512$.

-   Liouville parity $(-1)^{\Omega(n)}$ leaves $198$ false nonzero coefficients at nonsquarefree masses and matches only $314/512$ entries.

-   Sixteen simplex orientation gauges preserve every boundary rank, Betti number, and supertrace. Orientation is a basis gauge, not an additional selector.

## Monoid and mixing controls

Shifted multiplication preserves abstract unique factorization but disagrees with the intrinsic full-shift entropy clock, reaching coefficient accuracy $0.26953125$. Exact recovery returns only after the forbidden post-hoc clock $\log(n-1)$ is installed. The additive monoid has a single atom of zero entropy, so its Euler factor vanishes.

Positive free mixing fails all $28$ pairs among the first eight atoms. Isolated loops give coefficient one at $pq$ in the zeta series and zero at $pq$ in its logarithmic derivative. Ordered mixed words give coefficient two and the spurious positive term $\log(pq)$. Word-length parity cannot cancel the two even words $pq$ and $qp$.

## Finite duality diagnostics

At atom cutoffs $31,127,257,509$, the finite ratio $$R_P(s)=\prod_{p\le P}\frac{1-p^{-(1-s)}}{1-p^{-s}}$$ satisfies $R_P(1-s)R_P(s)=1$ to residual $2.70\times10^{-15}$ and has unit modulus on the critical line to residual $7.77\times10^{-16}$. Its maximum adjacent-cutoff wrapped phase drift is nevertheless $3.10576$ radians. Finite algebra is exact; convergence is not.

The partial trace norms of the naive relative operator $$Q_s-I=\operatorname{diag}(p^{2s-1}-1)$$ grow at $s=1/2+i$ as $$11.3980,\quad45.6491,\quad86.2878,\quad114.2360.$$ Analytically, $Q_s-I$ is noncompact on every open domain and vanishes only at the isolated center $s=1/2$. These diagnostics support the theorem stop but do not replace the proof.

# Route-A outcome and the live frontier

The preregistered gates separate the stage-level theorem from the standing candidate evaluation.

0.96L0.12L0.18X Gate & Result & Reason\
G0 & PASS & One full-shift tensor source; all three branches defined before computation\
G1 & PASS & Factorization chain degree is functorial; orientation gauges leave it invariant\
G2 & PASS & Exact homology, Möbius, exterior, and Berezinian ledgers\
G3 & LIMITED & Ordinary determinant remains in $\operatorname{Re}s>1$; no relative nuclear open set\
G4 & FAIL & No intrinsic half-density, Gamma factor, continuation, or completed divisor\

The stage result is $$\boxed{\textsf{GO A2 GRADED ORIENTATION}
\quad/\quad
\textsf{STOP A3 COMPLETION}.}$$ Because G4 fails, the preregistration forbids assigning SD-C08. Paper05 is a graded enhancement and obstruction theorem for SD-C07.

The standing Route-A tuple remains $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\\
 &\texttt{A1\_PASS\_ANALYTIC},\\
 &\texttt{A2\_ANALYTIC\_DETERMINANT},\\
 &\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},\\
 &\texttt{A4\_FAIL}).
\end{split}$$ The overall candidate status is `ROUTE_A_ANALYTIC_CANDIDATE`. No coordinate is borrowed from the wheel sieve, the Gauss/Farey operator, the Knauf model, or any other system family.

## What has genuinely advanced

Paper04 left open whether the inverse Fredholm orientation was merely a bad choice of determinant. answers yes: factorization topology supplies an intrinsic odd atom degree and a canonical Berezinian orientation after exteriorization. The success is exact and selective against random, Liouville, shifted, additive, and mixing controls.

The advancement stops at the Euler boundary. The graded formulas do not create new operator holomorphy. The most obvious attempt to add homological content, the standard Koszul resolution, removes rather than completes the prime data. The most obvious dualities reflect the wrong variable. The first regularization entering the critical line removes the low-order trace terms.

## Bold next hypothesis

[\[conj:half-density\]]{#conj:half-density label="conj:half-density"} There exists a source-locked symbolic system with an entropy-normalized stable/unstable transfer pair and a canonical Jacobian character $\delta^{1/2}$ such that:

1.  its atom/repetition ledger reduces to SD-C07 in the Euler half-plane;

2.  the exponent $1/2$ is selected by a symbolic duality theorem rather than by the Riemann functional equation;

3.  the paired transfer acts on a common nonempty analytic function space without deleting trace powers $r=1,2$;

4.  its determinant contains an internally derived archimedean factor.

This is the smallest live same-family target. A factor $p^{-1/2}$ written down by hand, a copied Gamma function, or a regularized determinant repaired with fitted counterterms would falsify the conjecture's source lock. The next stage should either construct such a normalized symbolic Jacobian or prove a new obstruction for finite-state/local-potential candidates.

Route B remains locked. Geometric or operator-algebraic interpretations of a half-density are recorded only as a `ROUND2_CLUE`; they are not developed here.

# Conclusion

The tensor-prime full-shift construction admits a natural graded refinement. Factorization topology assigns odd degree to tensor atoms, kills repeated atoms homologically, and recovers the exact Möbius ledger. The associated exterior transfer and odd Berezinian put $1/\zeta(s)$ and $\zeta(s)$ on opposite sides of one canonical determinant convention in the Euler half-plane. This resolves the determinant-orientation question left by SD-C07.

The same analysis prevents an easy completion story. An honest Koszul resolution cancels to the vacuum. Symbolic reversal preserves $s$; tensor inversion sends it to $-s$. Adding the missing half-density by hand produces a paired $\det_3$ in the critical strip, but that determinant is zero-free and has already discarded the first two prime traces.

The project therefore moves forward with a more specific bet. The next symbolic object must derive its half-density center from a normalized stable/unstable Jacobian and must retain the full repetition ledger on a common analytic space. Until such an object exists, the correct status is a graded A2 success, an A3 theorem stop, no SD-C08, and no Route-B invocation.

# Proof, computation, and scope details

## Augmented boundary convention

For a nonempty simplex $\sigma=[d_0<\cdots<d_j]$, the signed boundary is $$\partial\sigma
 =\sum_{i=0}^j(-1)^i
 [d_0<\cdots<\widehat d_i<\cdots<d_j].$$ At degree zero, the augmented boundary sends each vertex to the unique empty generator. Pairwise deletion of indices proves $\partial^2=0$ over the integers. The prime interval contains no vertices, so its reduced homology is one-dimensional in degree $-1$. This convention is the source of odd atom parity and is fixed before any Euler comparison.

## Finite chain algorithm

For each $n$, the implementation enumerates all strict chains of proper divisors, groups them by dimension, and constructs signed boundary columns. It verifies $\partial^2=0$ over $\mathbb Z$. Boundary ranks and Betti numbers are computed exactly over $\mathbb F_2$ by bit-column elimination; the crosscut proof in [\[thm:factorization-homology\]](#thm:factorization-homology){reference-type="ref" reference="thm:factorization-homology"} supplies the integral classification. Reduced Euler characteristic is calculated directly from the augmented chain dimensions, while the poset Möbius coefficient is computed independently by its divisor recursion.

Every cutoff $64,128,256,512$ is a complete prefix; no best cutoff is selected. Result tables contain all $511$ fibers at the largest cutoff.

## Trace-class and Schatten criteria

Since $\mathcal L_s$ is diagonal, $$\|\mathcal L_s\|_{\mathcal S_q}^q
 =\sum_p|p^{-s}|^q
 =\sum_p p^{-q\operatorname{Re}s}.$$ The prime subseries converges for exponent greater than one and diverges at or below one. This proves [\[thm:schatten\]](#thm:schatten){reference-type="ref" reference="thm:schatten"} and also shows why no finite cutoff phase identity can establish an infinite determinant.

For the relative diagonal ratio, $$\mathcal L_{1-s}\mathcal L_s^{-1}-I
 =\operatorname{diag}(p^{2s-1}-1).$$ If $\operatorname{Re}s>1/2$, its entries grow; if $\operatorname{Re}s<1/2$, they tend to $-1$; and if $\operatorname{Re}s=1/2$ with nonzero imaginary part, their moduli do not tend to zero. Only $s=1/2$ makes every entry vanish. Thus the relative perturbation is compact at one isolated point and on no open set.

## Regularized determinant convention

For $A\in\mathcal S_3$, $$\det\nolimits_3(I-A)
 =\det\!\left((I-A)\exp(A+A^2/2)\right),$$ and $$\log\det\nolimits_3(I-A)
 =-\sum_{r\ge3}\frac{\operatorname{Tr}(A^r)}r.$$ This definition explains both properties in [\[thm:det3\]](#thm:det3){reference-type="ref" reference="thm:det3"}: the determinant is well defined in the shared Schatten strip, and the arithmetic trace powers $r=1,2$ have been subtracted by construction.

## Same-source audit

0.96L0.25X Coordinate & Frozen source\
Atoms & tensor indecomposability in finite full shifts\
Mass/clock & topological entropy $\log n$\
Factorization degree & reduced order complex of $(F_1,F_n)$\
Exterior transfer & finite subsets of the same tensor atoms\
Koszul differential & multiplication by those atom generators\
Reversal & time reversal of the corresponding two-sided full shifts\
Group completion & Grothendieck group of the same tensor monoid\
Function space & $\ell^2$ atom space and its stated graded completions\

No coordinate is imported from another symbolic candidate. The adversarial $1/2$-centering is explicitly denied source credit and is used only to prove the stronger regularization obstruction.

## Non-claims

The project does not claim a new general theorem about divisor lattices, Koszul resolutions, exterior automata, or Smale-space homology. It does not claim operator continuation, a Gamma factor, a functional equation, Riemann--von Mangoldt zero count, completed-$\xi$ divisor, natural Weil compression, or self-adjoint Hilbert--Pólya operator. No Riemann zero is read, fitted, or used as a diagnostic. Route B is not invoked.
