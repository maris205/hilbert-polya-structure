---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dihedral-chronology-obstruction"
canonical_tex: "henon_dynamics/henon_dihedral_chronology_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dihedral_chronology_obstruction/paper/main.pdf"
source_sha256: "91a97f6e5a98604bb4bd9334fe783c048163fac87a19f295fb9b9d9977de9fbb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Invariant-Sector Limits of Coarse Dihedral Quotients in the Area-Preserving Hénon Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dihedral_chronology_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dihedral_chronology_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dihedral_chronology_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dihedral_chronology_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_dihedral_chronology_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We evaluate a proposed arithmetic upgrade of the area-preserving Hénon map: retain the map parameter, form the exact-period cover, quotient by time translation and reversal, and use the resulting curve's Frobenius cohomology as a spectral object. Three gates reject this object as a new global Route-A mechanism. First, after the exact scaling $x=Aq$, the recurrence is the Hamiltonian Hénon family whose parameter-dependent orbital polynomials and diagonal/non-diagonal/chiral decomposition were constructed in 2002--2007. Second, the coarse dihedral quotient is the invariant representation sector, so it retains no non-trivial joint Hénon--Frobenius isotypic data; this is a scope limit, not an objection to the standard use of unmarked cycles in an autonomous scalar zeta. Third, there is no cross-period determinant, prime clock, or target divisor. We also give an exact low-period certificate. Period six has nine cyclic orbits but eight dihedral classes; its squarefree marker has components of degrees $1,2,5$. The degree-five component is quadratic in the parameter and has discriminant $16(\sigma-6)(\sigma+2)(3\sigma^2-8\sigma-12)^2$, making its normalization a rational conic. All period-six components have genus zero and no weight-one $H^1$. Exact code reproduces the class counts through arbitrary cutoff. The result is a scoped rejection of the registered global mechanism, not a no-go for ordinary autonomous orbit zeta or equivariant covers with non-trivial dihedral coefficient systems.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 6, 2026'
title: |
  Invariant-Sector Limits of Coarse Dihedral Quotients\
  in the Area-Preserving Hénon Family
```

## Markdown 正文

# Introduction

Replacing a finite set of periodic points by a parameter-varying family seems to evade an elementary obstruction in arithmetic dynamics. At a fixed period, Frobenius acts on only finitely many points, so its local zeta function is a finite permutation determinant. If the parameter is retained, the same periodic-point equations define a curve; its compactification may carry weight-one cohomology and Weil eigenvalues. This observation motivated a specific proposal for the area-preserving Hénon map: pass to exact period, identify time translates and reversal partners, and study the $H^1$ of the coarse dihedral quotient.

The proposal has three limitations. Its algebraic orbit marker is already present in the orbital-polynomial literature. Its coarse quotient retains only invariant functions, so it cannot carry the non-trivial joint Frobenius--dihedral representation sectors of the marked cover. Finally, a collection of unrelated fixed-period curve factors supplies neither a global dynamical determinant nor a prime-like clock or target divisor. The second point must be interpreted carefully: autonomous scalar dynamical zeta functions normally identify cyclic choices of starting point, and the period label remains available. What the coarse quotient loses is marked phase, reversal orientation, and non-trivial isotypic data, not the legitimacy of unmarked periodic orbits.

We prove and document the following claims.

1.  The recurrence used in the motivating Hénon model [@wang2026henon] is exactly conjugate, away from one parameter value, to the Hamiltonian Hénon recurrence studied by Endler and Gallas. Their polynomial $S_n(\sigma)$ and its chiral factorization already implement the proposed low-period cyclic and reversal-class orbit marker [@endler2002; @endler2004; @endler2006chiral; @gallas2007].

2.  For every discriminant-free exact-period cover, the coarse quotient projects its permutation local system onto the trivial dihedral representation. We give the resulting trace identity and state exactly which marked and isotypic data are lost. We do not use this identity as a generic objection to autonomous scalar orbit zeta.

3.  At the first period with a chiral pair, $n=6$, every component of the squarefree quotient marker has genus zero. An exact symbolic certificate factors the relevant discriminant and supplies a rational parametrization.

The conclusion is deliberately scoped. Non-trivial isotypic local systems on the unquotiented cover retain the omitted joint action. They require a different candidate definition, however, and they do not yet provide a compatible tower over periods, a prime-like clock, or a target determinant. The negative result therefore prevents a low-period curve computation from being misreported as a Hilbert--Pólya mechanism while leaving the genuinely equivariant problem open.

Section [2](#sec:setup){reference-type="ref" reference="sec:setup"} fixes the map and the prior-art boundary. Section [3](#sec:chronology){reference-type="ref" reference="sec:chronology"} proves the invariant-sector identity. Section [4](#sec:period6){reference-type="ref" reference="sec:period6"} gives the period-six certificate, and Section [5](#sec:routea){reference-type="ref" reference="sec:routea"} records the dynamical-zeta consequences.

# Exact setup and source boundary {#sec:setup}

## The map, reversor, and parameter scaling

The motivating recurrence is $$\label{eq:paper-map}
q_{t+1}=1-Aq_t^2-q_{t-1}.$$ For $A\ne0$, set $x_t=Aq_t$. Multiplication of [\[eq:paper-map\]](#eq:paper-map){reference-type="eqref" reference="eq:paper-map"} by $A$ gives $$\label{eq:ham-henon}
x_{t+1}=A-x_t^2-x_{t-1}.$$ Thus no limiting procedure or fitted rescaling separates the proposed family from the Hamiltonian ($b=-1$) Hénon family of @endler2002 [@endler2004; @endler2006chiral]. In phase-space form, write $$H_A(x,y)=(A-x^2-y,x),\qquad R(x,y)=(y,x).$$ A direct calculation yields $$\label{eq:reversor}
R^2=1,\qquad RH_AR=H_A^{-1}.$$

For completeness, the period-$n$ fixed scheme has the cyclic presentation $$\operatorname{Spec}\mathbb Z[A,x_0,\ldots,x_{n-1}]/
\bigl(x_i^2+x_{i-1}+x_{i+1}-A\bigr)_{i\bmod n},$$ where repeated neighbors for $n=1,2$ are counted with multiplicity. Under a degree-compatible monomial order, the leading monomials are the pairwise coprime monomials $x_i^2$. The monic Buchberger product criterion gives the free basis $\prod_i x_i^{e_i}$, $e_i\in\{0,1\}$, and hence rank $2^n$ over $\mathbb Z[A]$.

Fix $n$ and pass to the characteristic-zero parameter line. Remove the intersections with all proper divisor periods and the discriminant locus where the remaining algebra is non-reduced. On the resulting open set $U_n$, let $$\pi_n:\mathcal P_n\longrightarrow U_n$$ denote the finite étale exact-period cover. Its generic degree is $$\label{eq:nu}
\nu(n)=\sum_{d\mid n}\mu(n/d)2^d.$$ Möbius inversion gives [\[eq:nu\]](#eq:nu){reference-type="eqref" reference="eq:nu"} on the generic reduced fiber. The map $H_A$ acts freely on every exact-period fiber. Equation [\[eq:reversor\]](#eq:reversor){reference-type="eqref" reference="eq:reversor"} then supplies a fiberwise action of $$\mathsf D_n=\langle H,R\mid H^n=R^2=1,\ RHR=H^{-1}\rangle.$$ We make no finite-flat exact-period assertion at the excluded parameters or in residue characteristics that interfere with period separation.

## What the orbital-polynomial program already contains

For an $n$-cycle with coordinates $x_1,\dots,x_n$, Endler and Gallas use the cyclic invariant $\sigma=\sum_i x_i$. They construct an orbital polynomial $P_n(x,\sigma)$ and a constraint $S_n(\sigma)$ whose roots select individual cyclic orbits. In the Hamiltonian family, their key factorization is $$\label{eq:CDN}
S_n(\sigma)=C_n(\sigma)^2D_n(\sigma)N_n(\sigma).$$ The factors $D_n,N_n$ select self-conjugate cycles, while $C_n^2$ records pairs of distinct cycles exchanged by $R$ and sharing the same $\sigma$ [@endler2006chiral]. At period six, the source formulas state that the roots select all nine cyclic cycles; squarefree reduction leaves eight markers and therefore separates the eight generic dihedral classes. We do not claim the unproved all-period function-field identity $\mathbb Q(\mathcal P_n)^{\mathsf D_n}=\mathbb Q(A,\sigma)$.

::: {#tab:prior}
  ---------------------------------------------------------------------------------------------------------------------------------------------
  Source              Exact object                                                Boundary established here
  ------------------- ----------------------------------------------------------- -------------------------------------------------------------
  @endler2002         Parameter-dependent period-four orbital polynomial          Orbit-marker curves are not new at period four

  @endler2004         Nine-root $S_6(\sigma;a,b)$ for genuine period-six cycles   A cyclic orbit marker is explicit at period six

  @endler2006chiral   $S_n=C_n^2D_nN_n$ and periods 6--8                          Squarefree reduction identifies reversal partners

  @gallas2007         All-period Möbius formulas for the three classes            Burnside degrees and the first chiral period are prior work

  @endler2006sums     Low-period sums, discriminants, and number fields           Ordinary low-period elimination/Galois data are prior work
  ---------------------------------------------------------------------------------------------------------------------------------------------

  : Primary-source equivalence boundary. The sources directly collide with the proposed orbit-marker novelty; an all-period equality with the scheme-theoretic coarse quotient is not asserted.
:::

General dynatomic-cycle language also predates this proposal [@hutz2010]. That theory cannot be copied verbatim to a birational compactification of a plane Hénon automorphism, but it reinforces the need to state exact-period conventions at bad fibers. Table [1](#tab:prior){reference-type="ref" reference="tab:prior"} separates these established ingredients from the invariant-sector identity proved next.

# The coarse quotient retains the invariant sector {#sec:chronology}

Let $\ell$ be any prime and set $$\mathcal V_n=(\pi_n)_*\mathbb Q_\ell.$$ On a geometric fiber, $\mathcal V_n$ is the vector space of functions on the finite exact-period set, and $\mathsf D_n$ permutes its coordinate basis. After spreading the cover and the action over $\mathbb Z[1/N]$ for a suitable $N$, every good closed point of residue characteristic $p\nmid N\ell$ has a geometric Frobenius action on the corresponding stalk.

[\[thm:chronology\]]{#thm:chronology label="thm:chronology"} Let $\mathcal C_n=\mathcal P_n/\mathsf D_n$ be the coarse orbit-set cover over $U_n$. Then $$\label{eq:invariants}
(\mathcal C_n\to U_n)_*\mathbb Q_\ell\simeq\mathcal V_n^{\mathsf D_n}.$$ The generator $H$ acts identically on the right-hand side. If $F^r$ is any endomorphism commuting with $\mathsf D_n$---including geometric Frobenius at a good closed point---then $$\label{eq:average}
\operatorname{Tr}(F^r\mid\mathcal V_n^{\mathsf D_n})
=\frac1{2n}\sum_{g\in\mathsf D_n}\operatorname{Tr}(F^rg\mid\mathcal V_n).$$

Functions on a finite orbit set are exactly the functions on the original set that are constant on every group orbit. This proves [\[eq:invariants\]](#eq:invariants){reference-type="eqref" reference="eq:invariants"}. Every vector in $\mathcal V_n^{\mathsf D_n}$ is fixed by every group element, including $H$. Since $\mathbb Q_\ell$ has characteristic zero, the Reynolds projector is $$P_{\mathrm{inv}}=\frac1{2n}\sum_{g\in\mathsf D_n}g.$$ Commutation of $F^r$ with this projector gives $$\begin{aligned}
\operatorname{Tr}(F^r\mid\mathcal V_n^{\mathsf D_n})
&=\operatorname{Tr}(F^rP_{\mathrm{inv}}\mid\mathcal V_n)\\
&=\frac1{2n}\sum_{g\in\mathsf D_n}\operatorname{Tr}(F^rg\mid\mathcal V_n),\end{aligned}$$ which is [\[eq:average\]](#eq:average){reference-type="eqref" reference="eq:average"}.

The theorem distinguishes unmarked orbit identity from equivariant data. The intermediate invariants $\mathcal V_n^{\langle H\rangle}$ remember cyclic Hénon orbits while distinguishing a chiral orbit from its reversal partner. Taking the remaining reversal invariants identifies that pair: $$\mathcal V_n^{\mathsf D_n}=\bigl(\mathcal V_n^{\langle H\rangle}\bigr)^{\langle R\rangle}.$$ The final quotient therefore does not remember a marked phase, reversal orientation, any non-trivial $\mathsf D_n$ representation, or an unaveraged joint Frobenius--Hénon trace.

This statement does not invalidate ordinary autonomous dynamical zeta functions. Such zeta functions intentionally sum cycles modulo cyclic starting phase, and the period $n$ remains an external label. They do, however, count both members of a chiral pair. An unweighted squarefree dihedral marker counts that pair once; a scalar orbit zeta built from it must restore multiplicity two or an equivalent representation weight.

Ordinary constant-$\mathbb Q_\ell$ cohomology of the quotient stack also computes the invariant sector: higher finite-group cohomology vanishes in characteristic zero. This does not mean that the stack forgets all equivariant information. Its sheaf category can retain the omitted sectors after one specifies non-trivial equivariant coefficients or an inertia-type construction. A candidate invoking non-trivial joint Hénon--Frobenius action must make that additional structure explicit.

# The first chiral quotient has genus zero {#sec:period6}

The all-period counting formulas of @gallas2007 provide a useful consistency check. Let $M_n=\nu(n)/n$ and define $$A_n=\sum_{d\mid n}\mu(n/d)2^{\lfloor(d+1)/2\rfloor},\qquad
Q_n=\sum_{d\mid n}\mu(n/d)2^{\lfloor(d+2)/2\rfloor}.$$ Then $$D_n=\begin{cases}A_n,&n\text{ odd},\\A_n/2,&n\text{ even},\end{cases}
\qquad
N_n=\begin{cases}0,&n\text{ odd},\\Q_n/2,&n\text{ even},\end{cases}$$ and the number of chiral cyclic orbits is $C_n=M_n-D_n-N_n$. Since chiral orbits occur in reversal pairs, the coarse quotient degree is $$\label{eq:burnside-degree}
D_n+N_n+C_n/2=\frac{M_n+D_n+N_n}{2}.$$

::: {#tab:counts}
    $n$   exact points   cyclic orbits   self-conjugate   chiral doublets   dihedral classes
  ----- -------------- --------------- ---------------- ----------------- ------------------
      1              2               2                2                 0                  2
      2              2               1                1                 0                  1
      3              6               2                2                 0                  2
      4             12               3                3                 0                  3
      5             30               6                6                 0                  6
      6             54               9                7                 1                  8
      7            126              18               14                 2                 16
      8            240              30               18                 6                 24

  : Exact class counts reproduced from the all-period formulas. Period six is the first time reversal identifies two distinct cyclic orbits.
:::

At $n=6$, the source factorization is $$S_6(\sigma)=C_6(\sigma)^2D_6(\sigma)N_6(\sigma),$$ where $$C_6=\sigma-2,\qquad D_6=\sigma^2+4\sigma-4A$$ and $$\begin{aligned}
N_6={}&\sigma^5+2\sigma^4-4(5A+4)\sigma^3+8A\sigma^2\notag\\
&+4(16A^2+12A+9)\sigma+128A^2-96A+72.
\label{eq:N6}\end{aligned}$$ The squarefree marker has degrees $1+2+5=8$, agreeing with Table [2](#tab:counts){reference-type="ref" reference="tab:counts"}.

[\[lem:marker-bridge\]]{#lem:marker-bridge label="lem:marker-bridge"} Shrink the period-six parameter open set so that the source orbital polynomials are separable and reconstruct the cycles they label. The map $\sigma=\sum_{i=1}^6x_i$ then induces a generically bijective map from the coarse dihedral orbit-set cover to the squarefree marker $C_6D_6N_6=0$. Their componentwise normalizations are birational.

The orbital reconstruction theorem associates one cyclic cycle to each simple root of $D_6N_6$ and two distinct cyclic cycles to the double root selected by $C_6$; the latter two are exchanged by $R$ [@endler2004; @endler2006chiral]. Thus the nine cyclic cycles map to eight distinct squarefree markers, exactly one for each of the eight dihedral classes in Table [2](#tab:counts){reference-type="ref" reference="tab:counts"}. A finite generically degree-one map of curves induces an equality of function fields after normalization.

[\[prop:genus0\]]{#prop:genus0 label="prop:genus0"} The smooth projective normalizations of the three affine components $C_6=0$, $D_6=0$, and $N_6=0$ all have genus zero. In particular, their weight-one $H^1$ vanishes. Under Lemma [\[lem:marker-bridge\]](#lem:marker-bridge){reference-type="ref" reference="lem:marker-bridge"}, this is also the componentwise genus statement for the generic coarse period-six quotient.

The first component is the parameter line $\sigma=2$. The second is rational because $A=(\sigma^2+4\sigma)/4$. For the third, regard [\[eq:N6\]](#eq:N6){reference-type="eqref" reference="eq:N6"} as a quadratic $c_2(\sigma)A^2+c_1(\sigma)A+c_0(\sigma)$. Exact factorization gives $$\label{eq:disc}
\operatorname{Disc}_A(N_6)=16(\sigma-6)(\sigma+2)
(3\sigma^2-8\sigma-12)^2.$$ On the generic locus, the substitution $$Y=\frac{2c_2(\sigma)A+c_1(\sigma)}
{4(3\sigma^2-8\sigma-12)}$$ identifies its function field with that of $$Y^2=(\sigma-6)(\sigma+2).$$ This conic is rational; one parametrization is $$\sigma=2+2(t+t^{-1}),\qquad Y=2(t-t^{-1}).$$ The inverse parameter is $t=(\sigma-2+Y)/4$, while $A=(4(3\sigma^2-8\sigma-12)Y-c_1)/(2c_2)$. The discriminant in [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"} is not a square in $\mathbb Q(\sigma)$, so this is the generic quadratic function field rather than a collapsed linear component. All three normalizations therefore have genus zero.

Singular gluing among rational components can contribute weight-zero dual-graph cohomology. It cannot supply the proposed weight-one curve spectrum. Proposition [\[prop:genus0\]](#prop:genus0){reference-type="ref" reference="prop:genus0"} is a low-period witness, not a claim that every higher-period component is rational.

# Route-A assessment and conclusion {#sec:routea}

The formal Route-A input gate is [not testable]{.smallcaps}: the candidate never defines a cross-period Euler product or Fredholm determinant, its repetition law, normalization, or target divisor. Table [3](#tab:routea){reference-type="ref" reference="tab:routea"} records only screening ceilings for the four layers, not formal layer verdicts for a complete candidate.

::: {#tab:routea}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Layer   Verdict      Reason
  ------- ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A1      weak         Exact unmarked primitive cycles are intrinsic, but there is no prime-like clock or arithmetic repetition weight; reversal orientation and non-trivial isotypic data are absent.

  A2      fail         No frozen cross-period dynamical determinant or target divisor exists; a fixed curve's Hasse--Weil factor is not diagnostic.

  A3      fail         There is no $\xi$ functional equation, gamma factor, global zero count, or continuation mechanism.

  A4      fail         Frobenius is not a natural self-adjoint Hilbert--Pólya operator here, and period six has no weight-one $H^1$.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Route-A screening ceilings after the formal input gate returns [not testable]{.smallcaps}.
:::

Three conclusions should not be conflated. The direct prior-art collision concerns the orbital marker and reversor classes, not a proved all-period function-field equality for the scheme quotient. The invariant-sector theorem says that a higher-period coarse quotient retains only trivial dihedral isotypic data; this is compatible with an ordinary unmarked scalar orbit zeta. The Route-A rejection comes from the missing global arrows: no cross-period determinant, prime-like clock, target divisor, functional equation, or natural discrete operator follows from these curves. Computing one more genus or local factor does not supply those arrows.

An equivariant replacement remains mathematically coherent. It would keep $\mathcal P_n$, decompose $\mathcal V_n$ into non-trivial $\mathsf D_n$-isotypic local systems, and track the full joint Frobenius--Hénon action. Before such a replacement becomes a dynamical-zeta candidate, it must define a canonical weighted Euler product or operator determinant across all primitive periods, including its clock, repetition law, and target divisor. Geometric tower maps are one possible mechanism, not a formal requirement. None of this structure follows from positive genus alone.

We therefore stop the registered C12C object at scoped triage and recommend a system-level pivot rather than another low-period elimination. A useful next system should possess a reversible polynomial dynamics and a canonical self-adjoint operator from the outset, so that the first experiment can test an exact dynamics--spectrum bridge instead of fitting a finite zero list.

# Exact computation and source-table check

The accompanying script uses integer Möbius inversion and SymPy polynomial arithmetic. From the project root, run

    python code/c12c_audit.py --max-period 35 --out-dir results
    python code/test_c12c_audit.py

No floating-point calculation occurs. The JSON certificate contains the factorization [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"}, the conic parametrization, the low-period count ledger, and the invariant-projector statement. The CSV file lists all counts through the requested cutoff.

The code also detects a small internal typo in the displayed period-14 row of @gallas2007. The paper's own formulas give $$M_{14}=1161,\quad D_{14}=56,\quad N_{14}=119,$$ so there are $$(1161-56-119)/2=493$$ chiral doublets. The displayed value 500 would imply $2(500)+56+119=1175$ cyclic orbits. This tabular inconsistency does not alter the prior-art boundary because the all-period formulas are explicit.
