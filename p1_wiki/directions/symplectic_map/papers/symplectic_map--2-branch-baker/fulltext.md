---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--2-branch-baker"
canonical_tex: "symplectic_map/papers/2-branch-baker/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/2-branch-baker/paper/manuscript.pdf"
source_sha256: "be36bf3ac1cf3e0236dcf9cc90c8f2c5dbabe12d212d0ded349ec64c247d4c78"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Rank Obstructions for Locally Constant Multiplier Clocks: An Audited PCF Markov--Baker Note

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/2-branch-baker>)
- [规范 TeX](<../../../../../symplectic_map/papers/2-branch-baker/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/2-branch-baker/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/2-branch-baker/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/2-branch-baker/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove an exact obstruction for multiplier clocks on finite symbolic models. For one fixed finite-state system with a finite-memory, locally constant, nonzero scalar multiplicative cocycle, every periodic instability length lies in a finite-dimensional rational vector space. Since logarithms of distinct rational primes are rationally linearly independent, such a clock cannot realize all prime logarithms term by term. We certify the obstruction on a three-state post-critically finite Markov factor and its compact labeled Markov--baker realization. The carrier is almost everywhere invertible and exact symplectic on every affine branch interior. Two independent primitive-cycle enumerations, an all-period boundary-quotient proof, and an independent 100-digit parent audit verify the construction. There are 226 primitive symbolic cycles through period 20, but every period $2k$ orbit has unstable multiplier modulus $2^k$ and length $k\log2$; hence the rational-prime intersection is only $\log2$, and the multiplier product is $(1-2^{1-s})^{-1}$. The carrier therefore passes its structural checks while the arithmetic gate fails; the intrinsic orbit ledger is formally weak because it has no arithmetic labels. The theorem concerns exact termwise containment for locally constant scalar clocks, not variable roofs, countable-state models, matrix spectral radii, or approximate prime resemblance.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology (HUST)\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: August 2026
title: |
  **Finite-Rank Obstructions for Locally Constant\
  Multiplier Clocks: An Audited PCF Markov--Baker Note**
```

## Markdown 正文

# Introduction {#sec:intro}

A finite symbolic model may carry every orbit exactly and still carry too little metric information to support an arithmetic correspondence. This distinction matters whenever primitive periodic orbits are compared with the rational primes. A symbolic language supplies primitive objects and their repetitions; an arithmetic model also needs an intrinsic clock whose primitive lengths can support the proposed labels. Neither a rational dynamical zeta nor reciprocal symplectic multipliers establish that second property by themselves.

Arithmetic--spectral analogies motivate exact tests of this separation [@berry1999riemann]. Here the requested clock is the instability length $L(C)=\log|\Lambda_u(C)|$ of a periodic orbit. The question is deliberately termwise: can one fixed dynamical model contain $\log p$ for every rational prime $p$, without inserting a prime table into local weights? This paper does not compare a fitted spectrum with Riemann zeros. Instead, it identifies an assumption class for which the termwise question is settled before any target data are opened.

The frozen band-merging parameter and its prime-symbolic motivation are inherited from the author's earlier non-autonomous Logistic-map study [@wang2026prime]. The present paper neither revalidates that study's prime-sieve claims nor imports its prime data. It asks the different, autonomous question of whether an exact branch-history carrier supplies an adequate periodic multiplier clock, and it permits a negative answer.

Our main observation is elementary but restrictive. Higher-block presentations, locally constant weights, and periodic-orbit sums are standard symbolic-dynamics tools [@lind2021symbolic; @parry1990zeta; @marcus1991weight]; we make no priority claim for finite-span containment by itself. The point of the note is its arithmetic design consequence. A finite graph with a finite-memory locally constant scalar cocycle has only finitely many local log-multipliers. All closed-walk lengths therefore lie in their finite $\mathbb{Q}$-span, whereas distinct prime logarithms are $\mathbb{Q}$-linearly independent. We give the complete argument, sharpen the bound to the span generated by closed walks, and record a sharp finite-rank example. The result does not extend to a point-dependent derivative merely because its symbolic coding is finite.

The worked case is a post-critically finite (PCF) quadratic map with a three-state Markov factor. Perron--Frobenius geometry realizes its two-sided branch history as a compact disjoint union of three labeled rectangles. Each allowed branch expands and contracts by reciprocal factors $\sqrt2$ and $1/\sqrt2$, with simultaneous coordinate reversal on a decreasing parent branch. The resulting baker is exact symplectic on branch interiors and almost everywhere invertible. Generalized baker and natural-extension constructions are classical [@bose1989generalized; @bruin2014natural]; the construction is used here as an auditable certificate, not presented as a new formalism.

The exact orbit calculation exposes the obstruction in its simplest form. Every closed word has even period $2k$, so $$|\Lambda_u(C)|=2^k,
  \qquad L(C)=k\log2,
  \qquad
  Z_u(s)=\frac{1}{1-2^{1-s}}.$$ Direct canonical-word enumeration and trace/Möbius inversion agree on 226 primitive symbolic cycles through period 20. A single symbolic period-two boundary orbit is replaced by a parent fixed point. The corresponding parent zeta is treated as a reproduction baseline rather than a novelty claim; the broader $RLR^\infty$ kneading setting is discussed in [@alseda2025realteapot].

The contributions are therefore narrow and falsifiable:

1.  We prove the finite-rank obstruction for one fixed finite-state, finite-memory, locally constant scalar multiplier clock, including the sharper closed-walk rank bound and its finite-rank sharpness.

2.  We give a convention-safe PCF Markov--baker certificate that separates the unsigned orbit zeta, parent boundary quotient, inherited factor orientation, Lefschetz convention, and multiplier product.

3.  We verify the rank-one corollary with exact algebra, two orbit ledgers, an independently implemented high-precision parent audit, three locked implementation splits, and six matched controls.

The formal outcome is `A0_FAIL / STRUCTURAL_ONLY` and `A1_WEAK`: the carrier is a structural positive control, but its orbit ledger has no all-prime arithmetic labeling. Downstream determinant fitting and quantization remain outside the declared scope. Figure [1](#fig:carrier-obstruction){reference-type="ref" reference="fig:carrier-obstruction"} summarizes the verified carrier geometry and the rank-one clock obstruction without identifying the factor-orientation signs with symplectic orientation.

![Carrier validity does not imply arithmetic adequacy. (a) The three-state Markov factor has four edges; the solid and dashed styles encode inherited one-dimensional factor signs. (b) Perron--Frobenius areas tile a compact labeled carrier whose branch Jacobians preserve $\Omega$ and have determinant one. (c) Every period-$2k$ instability length belongs to $\mathbb{Q}\log2$, while the full rational-prime logarithm family does not. Thus the carrier passes its structural gate and fails the exact arithmetic clock gate.](<../../../../../symplectic_map/papers/2-branch-baker/paper/figures/fig1_carrier_obstruction.pdf>){#fig:carrier-obstruction width="\\linewidth"}

Section [2](#sec:prior){reference-type="ref" reference="sec:prior"} fixes the prior-art boundary. The general obstruction is proved in Section [3](#sec:theorem){reference-type="ref" reference="sec:theorem"}. Sections [4](#sec:carrier){reference-type="ref" reference="sec:carrier"} and [5](#sec:ledger){reference-type="ref" reference="sec:ledger"} construct and solve the PCF case. Section [6](#sec:audit){reference-type="ref" reference="sec:audit"} reports the certification protocol, and Section [7](#sec:discussion){reference-type="ref" reference="sec:discussion"} gives the formal stopping decision and limitations.

# Prior work and claim boundary {#sec:prior}

#### PCF interval maps, kneading, and boundary corrections.

Periodic-point zetas originate in the finite-orbit counting framework of @artin1965periodic; finite Markov presentations lead to determinant formulas familiar from symbolic and hyperbolic dynamics [@bowen1970zeta]. Kneading theory organizes analogous information for piecewise monotone interval maps [@milnor1988iterated]. Generating partitions for smooth unimodal maps can be checked using the homterval lemma, the no-wandering-interval theorem, and the negative-Schwarzian basin theorem [@demelo1993one Chapter II, Lemma 3.1 and Theorems 6.1--6.2]. Periodic coding at a monotonicity boundary need not be one-to-one: Hofbauer's Markov-diagram framework already treats the resulting period discrepancies [@hofbauer1985periodic], and weighted kneading theory provides a broader setting for convention-sensitive determinants [@rugh2015kneading]. The $RLR^\infty$ kneading family is part of the setting studied in *The Real Teapot* [@alseda2025realteapot]. We use that paper only as nearby kneading context: the particular determinant identity below is derived directly here and is not attributed to that source. We conservatively treat both the parent formula and the one-orbit boundary correction as reproduction baselines.

#### Locally constant weights and symbolic recoding.

Higher-block presentations and finite-state codes are standard [@lind2021symbolic]. Locally constant suspension data and weighted periodic-orbit formalisms likewise belong to the established symbolic and hyperbolic-dynamics toolkit [@parry1990zeta; @marcus1991weight]. The finite-span step in Theorem [\[thm:finite-rank\]](#thm:finite-rank){reference-type="ref" reference="thm:finite-rank"} is therefore presented as an elementary lemma with a rational-prime consequence, not as a claim of priority over this literature. The contribution is the explicit design certificate, its sharp scope boundary, and the convention-safe audited example.

#### Natural extensions and generalized bakers.

Passing from a one-sided noninvertible map to a two-sided branch history is a standard way to recover past information. Generalized baker transformations give piecewise-affine geometric realizations [@bose1989generalized], and Hofbauer-tower methods construct natural extensions for broad classes of piecewise-affine maps [@bruin2014natural]. Our finite baker represents a branch code on a labeled disjoint union. We do not claim that this zero-dimensional symbolic system is homeomorphic to the full topological inverse-limit continuum of the quadratic map, or that the factor is a smooth coordinate projection.

#### Signed weights and quantized bakers.

Weighted symbolic determinants can encode branch orientation, but the meaning of a sign depends on the chosen operator and boundary convention. The matrix $W$ used here records the orientation of one-dimensional parent branches; it is neither two-dimensional symplectic orientation nor a Maslov phase. Quantized baker maps also have a substantial independent literature [@balazs1989quantized; @saraceno1990classical]. The existence of a generic baker quantization supplies no arithmetic clock and is not evidence for a canonical quantization of the present candidate.

#### Arithmetic scope.

The motivating comparison is with rational primes, not with the generic "prime orbit" terminology used for primitive dynamical cycles. Our theorem asks only whether all numbers $\log p$ can occur exactly as periodic instability lengths in a fixed clock. It neither asserts a new Hilbert--Pólya construction nor proves that two analytically continued zeta functions must differ. Phase cancellation and analytic continuation require additional hypotheses in a common convergence domain. Thus the PCF determinant, boundary mechanism, baker platform, and finite-state weighted-orbit machinery are prior-art baselines; only the explicit arithmetic certificate and its audited specialization are advanced here.

There is also a directly relevant smooth-dynamical contrast. For every non-exceptional rational map of degree at least two, Ji, Xie, and Zhang prove that the $\mathbb{Q}$-span of periodic finite characteristic exponents is infinite-dimensional and use the resulting length spectrum to characterize post-critical finiteness [@ji2026space]. Their exponents are normalized by period, whereas [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"} below is an unnormalized closed-orbit sum. The present theorem is not a competing general length-spectrum result: it is the elementary finite-locally-constant complement, packaged as a design certificate. In particular, a finite symbolic coding alone never implies a finite-rank derivative clock.

# Finite-memory clocks and the finite-rank obstruction {#sec:theorem}

Let $G$ be a finite directed graph defining a subshift of finite type. Fix an integer $m\geq1$, let $\mathcal{B}_m$ be the finite set of allowed length-$m$ blocks, and assign each block a nonzero scalar $\mu_b\in\mathbb{C}^\times$. For a periodic orbit $C$, blocks are counted with cyclic multiplicity and the modulus-based instability length is $$L(C)=\sum_{b\in C}\log|\mu_b|.
 \label{eq:length}$$ Define $$V=\operatorname{span}_{\mathbb{Q}}
 \{\log|\mu_b|:b\in\mathcal{B}_m\},
 \qquad
 V_{\mathrm{cyc}}=\operatorname{span}_{\mathbb{Q}}\{L(C):C\text{ periodic}\}.
 \label{eq:spaces}$$ The finite-memory hypothesis includes an edge-local cocycle as $m=1$ and does not require the multipliers to be algebraic.

[\[thm:finite-rank\]]{#thm:finite-rank label="thm:finite-rank"} Every periodic length in [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"} belongs to $V$, and $$\dim_{\mathbb{Q}}V_{\mathrm{cyc}}\leq\dim_{\mathbb{Q}}V\leq|\mathcal{B}_m|<\infty.$$ Moreover, $$\#\{p:\ p\text{ is a rational prime and }
       L(C)=\log p\text{ for some }C\}
 \leq \dim_{\mathbb{Q}}V_{\mathrm{cyc}}.
 \label{eq:rank-bound}$$ In particular, one fixed clock satisfying these hypotheses cannot contain $\log p$ for every rational prime.

First recode the finite-memory rule on the standard higher-block graph [@lind2021symbolic]. Its vertices are allowed words of length $m-1$, and an allowed length-$m$ block is an edge from its prefix to its suffix. When $m=1$, retain the original edge presentation. The graph remains finite, and the original block weight becomes an edge-local weight. Periodic sequences and cyclic block multiplicities are unchanged.

For an orbit $C$, let $N_b(C)\in\mathbb Z_{\geq0}$ count occurrences of $b$. Then $$L(C)=\sum_{b\in\mathcal{B}_m}N_b(C)\log|\mu_b|\in V.$$ Thus $V_{\mathrm{cyc}}\subseteq V$, while $V$ is spanned by the finite family of local lengths. This proves the dimension inequalities. Blocks with $|\mu_b|=1$ contribute zero and do not affect the argument; complex phases do not enter because the clock was defined using modulus.

It remains to bound prime logarithms. Distinct rational-prime logarithms are linearly independent over $\mathbb{Q}$. Indeed, if $\sum_{i=1}^{r}q_i\log p_i=0$, choose a positive common denominator $D$ and set $n_i=Dq_i\in\mathbb Z$. Exponentiation gives $\prod_i p_i^{n_i}=1$. Moving negative exponents to the other side yields an equality of positive integers whose two sides use disjoint prime sets. Unique factorization forces every $n_i$, hence every $q_i$, to vanish.

Every prime logarithm realized by a periodic orbit lies in $V_{\mathrm{cyc}}$. Such logarithms form a linearly independent subset of that finite-dimensional space, so their number is at most $\dim_{\mathbb{Q}}V_{\mathrm{cyc}}$. This proves [\[eq:rank-bound\]](#eq:rank-bound){reference-type="eqref" reference="eq:rank-bound"} and the all-prime obstruction.

The rank bound is sharp as an abstract finite-graph statement. A one-vertex graph with $r$ self-loops weighted by distinct primes $p_1,\ldots,p_r$ realizes the independent lengths $\log p_1,\ldots,\log p_r$. This example explicitly inserts a finite prime list; it is not an arithmetic-origin construction.

::: {#tab:scope}
  ----------------------------------------------------------------------------------------------------------------------------------
  Clock class                               Finite rank forced?   Theorem applies?   Reason
  ----------------------------------------- --------------------- ------------------ -----------------------------------------------
  Fixed finite, locally constant scalar     Yes                   Yes                Finite local length set

  Finite memory on a finite graph           Yes                   Yes                Finite higher-block recoding

  Finite prime-weight loop example          Yes                   Yes                Sharp at its inserted finite rank

  Point-dependent / Hölder roof             --                    No                 Periodic values need not share a finite span

  Countable-state or infinite memory        --                    No                 Local length set can be infinite

  Growing sequence of finite models         Per model             No union claim     Ranks may grow with the model

  Matrix spectral radius / singular value   --                    No                 Generally not a scalar multiplicative cocycle

  Approximate or density matching           --                    No                 Statement is exact and termwise
  ----------------------------------------------------------------------------------------------------------------------------------

  : Scope of Theorem [\[thm:finite-rank\]](#thm:finite-rank){reference-type="ref" reference="thm:finite-rank"}. A dash means that the theorem makes no assertion, not that the indicated model can realize an all-prime clock.
:::

The locally constant and scalar assumptions are essential. A smooth map with a finite Markov partition can still have a point-dependent derivative and infinitely many rationally independent orbit lengths; the rational-map result of @ji2026space makes this contrast precise for normalized periodic characteristic exponents of non-exceptional maps. Likewise, spectral radii and largest singular values of matrix products are not generally multiplicative local scalars. Theorem [\[thm:finite-rank\]](#thm:finite-rank){reference-type="ref" reference="thm:finite-rank"} is therefore an elementary design-class certificate, not a no-go theorem for arbitrary smooth symplectic dynamics and not a finite-rank assertion about the nonlinear quadratic parent below.

# A compact PCF Markov--baker carrier {#sec:carrier}

## The parent and its finite Markov factor

Consider $$f_u(x)=1-u x^2,
 \qquad
 p(u)=u^3-2u^2+2u-2,
 \label{eq:parent}$$ where $u$ is the unique root of $p$ in $(3859/2500,15437/10000)$, and set $d=u-1$. Exact reduction modulo $p(u)$ gives $$0\longmapsto1\longmapsto-d\longmapsto d\longmapsto d.
 \label{eq:pcf-orbit}$$ Thus the postcritical core is partitioned into $I_0=[-d,0]$, $I_1=[0,d]$, and $I_2=[d,1]$. Their endpoint images, in the displayed orientation, are $$(f(-d),f(0))=(d,1),\quad
 (f(0),f(d))=(1,d),\quad
 (f(d),f(1))=(d,-d).
 \label{eq:endpoint-images}$$ The unsigned adjacency matrix and the *factor-orientation matrix* are therefore $$A=\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix},
 \qquad
 W=\begin{pmatrix}0&0&1\\0&0&-1\\-1&-1&0\end{pmatrix}.
 \label{eq:AW}$$ Equivalently, the allowed signed edges are $0\to2$ with sign $+1$, and $1\to2$, $2\to0$, $2\to1$ with sign $-1$. These signs record monotonicity of the one-dimensional factor; they do not record symplectic orientation.

The Perron--Frobenius eigenvalue is $\lambda=\sqrt2$. We use the normalized left and right vectors $$\ell=r=(1/2,1/2,1/\sqrt2)^{\mathsf T},
 \quad Ar=\lambda r,
 \quad \ell^{\mathsf T}A=\lambda\ell^{\mathsf T},
 \quad \ell^{\mathsf T}r=1.
 \label{eq:pf}$$ The labeled carrier is the compact disjoint union $$\mathcal R=\bigsqcup_{i=0}^{2}
 R_i,\qquad R_i=\{i\}\times[0,r_i]\times[0,\ell_i],
 \label{eq:carrier}$$ with rectangle areas $(\ell_i r_i)_i=(1/4,1/4,1/2)$. Labels are part of the state, even when two rectangles have equal dimensions.

For each allowed edge $i\to j$, allocate a vertical source strip of width $r_j/\lambda$ in $R_i$ and a horizontal destination strip of height $\ell_i/\lambda$ in $R_j$. The two eigenvector identities in [\[eq:pf\]](#eq:pf){reference-type="eqref" reference="eq:pf"} say exactly that these strips tile every source and destination rectangle. Ordering equal-source or equal-target edges by label gives offsets $$s_{ij}=\sum_{j'<j}\frac{A_{ij'}r_{j'}}{\lambda},
 \qquad
 t_{ij}=\sum_{i'<i}\frac{\ell_{i'}A_{i'j}}{\lambda}.
 \label{eq:offsets}$$ Write $\sigma_{ij}=W_{ij}$ on an allowed edge. In local rectangle coordinates the branch map is $$B_{ij}(x,y)=
 \begin{cases}
 (\lambda(x-s_{ij}),\ t_{ij}+y/\lambda),&\sigma_{ij}=+1,\\[2pt]
 (r_j-\lambda(x-s_{ij}),\ t_{ij}+(\ell_i-y)/\lambda),&\sigma_{ij}=-1.
 \end{cases}
 \label{eq:branch-map}$$ The simultaneous reversal in the second line is essential: reversing only one coordinate would make the branch anti-symplectic.

[\[prop:carrier\]]{#prop:carrier label="prop:carrier"} On every branch interior, $B_{ij}$ is an exact symplectic affine diffeomorphism from its source strip to its destination strip. The deterministic half-open realization is one-to-one and onto away from the finite union of strip-boundary faces. Retaining all closed strip faces instead defines a forward/inverse relation whose two directions agree.

The derivative on an allowed branch is $$DB_{ij}=\operatorname{diag}
 (\sigma_{ij}\sqrt2,\sigma_{ij}/\sqrt2).
 \label{eq:jacobian}$$ It has determinant one and therefore, in dimension two, $(DB_{ij})^{\mathsf T}\Omega DB_{ij}=\Omega$ for $\Omega=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. This proves preservation of $dx\wedge dy$, but exactness requires one more calculation. With the Liouville primitive $\alpha=x\,dy$, every branch has the affine form $B_{ij}(x,y)=(a x+b,a^{-1}y+c)$, where $a=\sigma_{ij}\sqrt2$. Hence $$B_{ij}^{*}\alpha-\alpha
 =(a x+b)a^{-1}dy-x\,dy
 =\frac{b}{a}\,dy
 =d\!\left(\frac{b}{a}y\right).
 \label{eq:exactness}$$ Thus the preserved symplectic form and the primitive difference are exact on each branch interior.

The right PF identity tiles every source rectangle by the vertical strips; the left identity tiles every destination rectangle by the horizontal strips. Formula [\[eq:branch-map\]](#eq:branch-map){reference-type="eqref" reference="eq:branch-map"} maps each such strip bijectively onto its paired strip, and solving its two affine coordinates gives its inverse. Choose strips left-closed and right-open, except for the last outer endpoint; make the analogous deterministic choice for destination strips. Then each nonboundary point selects exactly one edge in either direction. If all faces are closed instead, a shared face may select two adjacent edges, and the same affine equations show equality of the resulting forward and inverse relations. The exceptional faces have area zero.

Proposition [\[prop:carrier\]](#prop:carrier){reference-type="ref" reference="prop:carrier"} is deliberately local. The map is piecewise affine on branch interiors, not a global $C^1$ symplectomorphism. It is a compact labeled realization of two-sided branch history, not a homeomorphism with the full inverse-limit continuum of $f_u$, and the factor to the interval is not asserted to be a smooth submersion. Appendix [8](#app:parent){reference-type="ref" reference="app:parent"} records the root certificate, while Appendix [9](#app:branches){reference-type="ref" reference="app:branches"} makes the half-open and closed-boundary conventions explicit.

# Periodic ledger, boundary quotient, and the candidate clock {#sec:ledger}

## Unsigned cycles and the parent quotient

Let $N_n=\operatorname{tr}(A^n)$ count points fixed by the $n$th shift iterate, and let $P_n$ count primitive orbits of least period $n$. The standard trace/Möbius relation [@lind2021symbolic; @bowen1970zeta] is $$N_n=\sum_{q\mid n}qP_q,
 \qquad
 P_n=\frac1n\sum_{q\mid n}\mu(q)N_{n/q}.
 \label{eq:mobius}$$ Since the eigenvalues of $A$ are $0,\sqrt2,-\sqrt2$, $$N_n=\begin{cases}0,&n\text{ odd},\\2^{k+1},&n=2k.\end{cases}
 \label{eq:fixed-counts}$$ Trace/Möbius inversion and a second algorithm that directly enumerates closed words, rejects proper repetitions, and takes the least cyclic rotation agree through period 20. Their common primitive-count vector is $$(P_1,\ldots,P_{20})=
 (0,2,0,1,0,2,0,3,0,6,0,9,0,18,0,30,0,56,0,99),
 \label{eq:primitive-vector}$$ whose entries sum to 226.

[\[lem:sole-boundary\]]{#lem:sole-boundary label="lem:sole-boundary"} For the endpoint-split Markov coding defined by $I_0,I_1,I_2$, the coding of parent periodic orbits is one-to-one and period-preserving except at the fixed point $d$. Its symbolic preimage is the single primitive period-two orbit $1\leftrightarrow2$. Consequently no other primitive-period correction occurs at any period.

We first verify that the partition is generating, rather than assuming this from its transition graph. For an admissible one-sided sequence $\omega=(\omega_j)_{j\geq0}$, define the nested closed cylinders $$K_N(\omega)=\bigcap_{j=0}^{N} f_u^{-j}(I_{\omega_j}),
 \qquad K(\omega)=\bigcap_{N\geq0}K_N(\omega).
 \label{eq:nested-cylinders}$$ The endpoint images in [\[eq:endpoint-images\]](#eq:endpoint-images){reference-type="eqref" reference="eq:endpoint-images"}, monotonicity on each partition element, and the Markov property show inductively that every finite admissible word has a nonempty compact interval as its cylinder (obtained by following the corresponding monotone inverse branches). Hence every $K(\omega)$ is nonempty.

For $x\ne0$, the parent has $$S f_u(x)=-\frac{3}{2x^2}<0,
 \label{eq:schwarzian}$$ and its quadratic critical point is nonflat. Moreover, the critical point and both endpoints of the invariant core eventually land on the fixed point $d$: $$0\mapsto1\mapsto-d\mapsto d,
 \qquad -d\mapsto d,
 \qquad 1\mapsto-d\mapsto d.$$ This fixed point is repelling, since the frozen isolating interval gives $$|f'_u(d)|=2u(u-1)>
 \frac{5244381}{3125000}>1.
 \label{eq:repelling-d}$$ The negative-Schwarzian basin theorem therefore rules out an attracting or neutral periodic basin: such a basin must capture the critical point or a core endpoint, while all three displayed orbits instead terminate at the repelling point $d$. The no-wandering-interval theorem and homterval lemma for a smooth nonflat unimodal map now rule out a nontrivial itinerary fibre [@demelo1993one Chapter II, Lemma 3.1 and Theorems 6.1--6.2]. Indeed, if some $K(\omega)$ contained a nondegenerate interval, its interior would be a homterval for the coarser monotonicity partition $[-d,0],[0,1]$: every iterate follows one monotone branch. The homterval lemma makes such an interval either wandering or contained in a periodic attracting basin, and both alternatives have just been excluded. Thus every nested cylinder in [\[eq:nested-cylinders\]](#eq:nested-cylinders){reference-type="eqref" reference="eq:nested-cylinders"} shrinks to one point, apart from the choice of symbolic name at a shared endpoint; each named fibre itself remains a singleton.

If $\omega$ is periodic of period $n$, the points represented by $\omega$ and its $n$-shift are the same singleton, so its point is fixed by $f_u^n$. Conversely, every parent periodic orbit has an admissible itinerary. Off the endpoints this itinerary is unique. If a primitive word of period $n$ represented an off-endpoint point of smaller period $r<n$, uniqueness would give $\sigma^r\omega=\omega$, contradicting primitivity. It remains only to identify periodic endpoint names, the standard finite exception in piecewise-monotone coding [@hofbauer1985periodic].

Here the endpoint set is $$E=\{-d,0,d,1\}.$$ If a periodic parent orbit meets $E$, the endpoint it meets must itself be periodic. The displayed endpoint dynamics shows that $d$ is the only such point. Since $d\in I_1\cap I_2$, only labels 1 and 2 are available there. Restricting the adjacency matrix [\[eq:AW\]](#eq:AW){reference-type="eqref" reference="eq:AW"} to these labels leaves exactly the transitions $1\to2$ and $2\to1$; neither $1\to1$ nor $2\to2$ is allowed. Thus the only symbolic orbit over $d$ is the primitive two-cycle $1\leftrightarrow2$. Every other periodic orbit avoids the endpoint ambiguity and keeps its least period.

Lemma [\[lem:sole-boundary\]](#lem:sole-boundary){reference-type="ref" reference="lem:sole-boundary"} replaces the symbolic period-two boundary ghost by the parent fixed point $d$. Thus the parent minus symbolic primitive-count delta is $(+1,-1,0,\ldots)$ for all periods, not merely through the audit cutoff. At the Euler-product level the ratio is $$\frac{1-z^2}{1-z}=1+z.
 \label{eq:boundary-factor}$$ Directly, $$\det(I-zA)=1-2z^2,
 \quad
 \zeta_A(z)=\frac1{1-2z^2},
 \quad
 \zeta_f(z)=\frac{1+z}{1-2z^2}.
 \label{eq:unsigned-parent-zeta}$$ Equivalently, the parent fixed-point counts are $1$ for odd $n$ and $2^{k+1}-1$ for $n=2k$. These all-period statements follow from Lemma [\[lem:sole-boundary\]](#lem:sole-boundary){reference-type="ref" reference="lem:sole-boundary"}; the period-20 parent audit below is only an independent implementation check. The correction mechanism and the parent formula are used as prior-art reproduction baselines, not as novelty claims. Figure [2](#fig:orbit-lattice){reference-type="ref" reference="fig:orbit-lattice"} displays the exact primitive ledger, the single boundary replacement, and the resulting rank-one instability-length lattice.

![Two independent exact enumerations give 226 primitive symbolic cycles through period 20. The interval-factor quotient changes only one primitive boundary pair: it adds the fixed point $d$ at period one and removes the symbolic orbit $1\leftrightarrow2$ at period two. All higher primitive-count differences vanish. Candidate instability lengths occupy the rank-one lattice $\{k\log2:k\geq1\}$, whose rational-prime intersection is only $\log2$.](<../../../../../symplectic_map/papers/2-branch-baker/paper/figures/fig2_orbit_lattice.pdf>){#fig:orbit-lattice width="\\linewidth"}

## Factor orientation and determinant conventions

The *factor-orientation matrix* $W$ in [\[eq:AW\]](#eq:AW){reference-type="eqref" reference="eq:AW"} satisfies $$W^2=\begin{pmatrix}-1&-1&0\\1&1&0\\0&0&0\end{pmatrix},
 \qquad W^3=0.
 \label{eq:W-nilpotent}$$ Consequently every positive-period signed trace vanishes and $$\det(I-zW)=1,
 \qquad \zeta_{W}(z)=1.
 \label{eq:W-zeta}$$ This factor-orientation-weighted SFT product is separate from the unsigned orbit zeta. After the frozen parent boundary convention, two still different objects are $$D_{\mathrm{or,parent}}(z)=1-z,
 \qquad
 \zeta_{\mathrm{Lef}}(z)=\frac1{1-z}.
 \label{eq:orientation-conventions}$$ The first is a parent factor-orientation object; it is not a Lefschetz zeta. Neither object supplies a two-dimensional symplectic orientation or a Maslov/quantum phase. An all-positive-sign null leaves $A$, the carrier areas, unsigned cycles, and symplectic branch determinants unchanged while destroying the nilpotent cancellation.

[\[cor:candidate\]]{#cor:candidate label="cor:candidate"} For every primitive period-$2k$ orbit of the constant-slope Markov--baker, $$|\Lambda_u(C)|=2^k,
 \qquad L(C)=k\log2.
 \label{eq:candidate-length}$$ The only rational prime $p$ for which $L(C)=\log p$ is $p=2$. The unsigned constant-slope multiplier product is $$Z_u(s):=\prod_{C\ \mathrm{primitive}}
       \left(1-e^{-sL(C)}\right)^{-1}
 =\det\!\left(I-2^{-s/2}A\right)^{-1}
 =\frac1{1-2^{1-s}}
 =\frac{2^s}{2^s-2},
 \quad \operatorname{Re}s>1,
 \label{eq:multiplier-product}$$ followed by the elementary meromorphic continuation of the displayed rational expression in $2^s$.

The graph is bipartite, with parts $\{0,1\}$ and $\{2\}$, so every closed walk has even period $2k$. Each edge has unstable multiplier modulus $\sqrt2$, hence a $2k$-edge product has modulus $2^k$ and logarithm $k\log2$. If this equals $\log p$, exponentiation gives $p=2^k$, which is prime exactly when $k=1$; period-two primitive orbits exist by [\[eq:primitive-vector\]](#eq:primitive-vector){reference-type="eqref" reference="eq:primitive-vector"}. Finally the standard weighted-graph Euler product uses edge weight $2^{-s/2}$, so $Z_u(s)=\det(I-2^{-s/2}A)^{-1}$. Substitution into $\det(I-zA)=1-2z^2$ proves [\[eq:multiplier-product\]](#eq:multiplier-product){reference-type="eqref" reference="eq:multiplier-product"}. Absolute convergence holds when the spectral radius $\sqrt2\,|2^{-s/2}|$ is below one, namely $\operatorname{Re}s>1$.

Corollary [\[cor:candidate\]](#cor:candidate){reference-type="ref" reference="cor:candidate"} concerns the source-locked Parry-affine branch cocycle. It does not compute the point-dependent derivative cocycle of the nonlinear parent [\[eq:parent\]](#eq:parent){reference-type="eqref" reference="eq:parent"}. The latter lies outside Theorem [\[thm:finite-rank\]](#thm:finite-rank){reference-type="ref" reference="thm:finite-rank"}; finite PCF symbolic structure does not make its derivative locally constant. This distinction is consistent with the infinite-dimensional rational-map characteristic-exponent theorem of @ji2026space.

# Certified verification and matched controls {#sec:audit}

The proofs above settle the mathematical claims; computation checks that the implemented object is the declared one. The candidate, conventions, scales, controls, stopping rule, and forbidden-data policy were source-locked before validation. A version-2 amendment repaired only a mechanically mistranscribed development seed before any split was opened. No external prime or Riemann-zero table, target fitting, or target unfolding was used. All six exact preflight gates and all 89 unit/integration tests passed. The complete protocol, amendment, hashes, and access chain are recorded in Appendix [11](#app:repro){reference-type="ref" reference="app:repro"} and the accompanying machine-readable passport.

An independent parent audit did not import the exact ledger generator. At 100 decimal digits it recovered parent periodic points through monotone inverse branches and reproduced the period-20 ledger and sole boundary duplicate; its maximum periodic residual was $9.706\times10^{-98}<10^{-75}$. This supports implementation consistency, not interval certification and not the all-period proof, which is Lemma [\[lem:sole-boundary\]](#lem:sole-boundary){reference-type="ref" reference="lem:sole-boundary"}.

Development, validation, and test each performed $65{,}536\times256=16{,}777{,}216$ identified per-step forward/inverse checks. Every split had zero edge mismatch and zero boundary failure, and the common maximum roundtrip error was $1.388\times10^{-16}$, below the frozen $2\times10^{-13}$ threshold. These are deterministic software checks, not independent statistical observations. Six one-feature controls separately tested enumeration, paired reversal, dissipation, label loss, anti-symplectic rejection, and factor-sign cancellation. Their exact outcomes and inference limits are tabulated in Appendix [11](#app:repro){reference-type="ref" reference="app:repro"}; Figure [3](#fig:computational-audit){reference-type="ref" reference="fig:computational-audit"}, placed with that passport, is the compact visual summary.

# Discussion and conclusion {#sec:discussion}

The case study separates two questions that are easy to conflate. The three-rectangle carrier is compact, almost everywhere invertible, and exact symplectic on branch interiors; its intrinsic symbolic and parent ledgers are fully auditable. Yet its frozen multiplier clock has rank one. It therefore cannot provide an exact termwise all-prime ledger, regardless of further sampling or determinant manipulation.

The mathematical conclusion is that the carrier succeeds as a geometric and symbolic construction but fails as an exact all-prime multiplier clock; its primitive ledger is structural evidence only. For traceability, the source-locked project records this conclusion under the internal tags $$\texttt{PRE\_A0\_STRUCTURAL\_PASS},\qquad
 \texttt{A0\_FAIL / STRUCTURAL\_ONLY}{},\qquad \texttt{A1\_WEAK}{}.$$ Here `A1_WEAK` means that the intrinsic orbit ledger is exact but contains no A0 arithmetic labels; it is not an `A1_PASS`. Stages A2--A4 are `STOP_SCOPED`, Route B is `FORBIDDEN`, and the overall candidate decision is `ROUTE_A_REJECTED`. The model remains useful as a structural positive control and an arithmetic negative control. Classical baker quantizations [@balazs1989quantized; @saraceno1990classical] do not change this gate: generic quantizability supplies neither missing arithmetic origin nor a canonical quantization of this clock.

The obstruction is exact but narrow. It does not cover point-dependent or Hölder roofs, countable-state or infinite-memory systems, growing sequences of finite models, nonmultiplicative matrix spectral radii or singular values, approximate/density matching, or signed analytic cancellation under additional convergence hypotheses. It also does not apply to the nonlinear parent derivative; indeed, the infinite-rank theorem for characteristic exponents of non-exceptional rational maps [@ji2026space] shows why finite coding and finite derivative rank must not be identified. Any independently motivated variable-roof, smoothed, countable-state, coupled, or higher-dimensional construction is a new candidate requiring a new source lock and an arithmetic-origin audit, not a post-hoc modification of this one.

The parent determinant and boundary-period discrepancy, generalized-baker platform, natural-extension strategy, higher-block recoding, locally constant weight framework, and generic baker quantization all have direct prior context. Accordingly, this paper is a specialist note: its contribution is the explicit rational-prime design certificate, the all-period boundary proof, and a convention-safe audited worked example. A valid carrier answers a geometric question; only an intrinsic clock can answer the arithmetic one.

# Data, code, and assistance disclosure {#data-code-and-assistance-disclosure .unnumbered}

All exact and numerical artifacts, source locks, audit scripts, figure generators, and frozen reports accompany this manuscript. No external prime or Riemann-zero data were used. Computation used only CPU resources. AI tools assisted code and manuscript review; all definitions, proofs, calculations, citations, and final claims were checked against the locked artifacts by the author. Any venue-specific disclosure wording should supersede this generic statement.

# Exact parent algebra {#app:parent}

The isolating interval in [\[eq:parent\]](#eq:parent){reference-type="eqref" reference="eq:parent"} is an exact certificate. Its endpoint evaluations are $$p(3859/2500)=-\frac{4136221}{15625000000}<0,
 \qquad
 p(15437/10000)=\frac{32678453}{10^{12}}>0.
 \label{eq:root-signs}$$ Moreover $p'(u)=3u^2-4u+2$ has negative discriminant and positive leading coefficient, hence is positive on $\mathbb R$. Thus $p$ is strictly increasing and the interval contains its unique real root.

All PCF identities follow in $\mathbb{Q}[u]/(p)$. Clearly $f_u(0)=1$ and $f_u(1)=1-u=-d$. Since $$f_u(d)-d=1-u(u-1)^2-(u-1)=-p(u),
 \label{eq:pcf-reduction}$$ we have $f_u(d)=d$; evenness also gives $f_u(-d)=d$. This proves [\[eq:pcf-orbit\]](#eq:pcf-orbit){reference-type="eqref" reference="eq:pcf-orbit"} and the endpoint pairs [\[eq:endpoint-images\]](#eq:endpoint-images){reference-type="eqref" reference="eq:endpoint-images"}. On the interval interiors, $f'_u(x)=-2ux$ is positive on $I_0$ and negative on $I_1,I_2$. Combining these orientations with the endpoint images yields precisely the four entries of $A$ and $W$ in [\[eq:AW\]](#eq:AW){reference-type="eqref" reference="eq:AW"}. This establishes the exact parent algebra independently of decimal root approximation.

# Branch formulas and boundary relation {#app:branches}

Table [2](#tab:strips){reference-type="ref" reference="tab:strips"} expands the offsets [\[eq:offsets\]](#eq:offsets){reference-type="eqref" reference="eq:offsets"}. All coordinates are local to the labeled source or destination rectangle. Write $b_*=1/(2\sqrt2)$.

::: {#tab:strips}
    Edge     $\sigma$   $s_{ij}$   Source $x$-range   $t_{ij}$   Destination $y$-range
  --------- ---------- ---------- ------------------ ---------- -----------------------
   $0\to2$     $+$         0          $[0,1/2]$          0             $[0,b_*]$
   $1\to2$     $-$         0          $[0,1/2]$        $b_*$       $[b_*,1/\sqrt2]$
   $2\to0$     $-$         0          $[0,b_*]$          0             $[0,1/2]$
   $2\to1$     $-$       $b_*$     $[b_*,1/\sqrt2]$      0             $[0,1/2]$

  : Closed strip allocation. Half-open ownership is specified below.
:::

For an image point $(X,Y)\in R_j$ on the strip assigned to $i\to j$, the complete inverse of [\[eq:branch-map\]](#eq:branch-map){reference-type="eqref" reference="eq:branch-map"} is $$B_{ij}^{-1}(X,Y)=
 \begin{cases}
 (s_{ij}+X/\lambda,\ \lambda(Y-t_{ij})),&\sigma_{ij}=+1,\\[2pt]
 (s_{ij}+(r_j-X)/\lambda,\ \ell_i-\lambda(Y-t_{ij})),&\sigma_{ij}=-1.
 \end{cases}
 \label{eq:inverse-map}$$ The deterministic forward implementation assigns the internal vertical face $x=b_*$ in $R_2$ to edge $2\to1$; the inverse implementation assigns the internal horizontal face $y=b_*$ in $R_2$ to edge $1\to2$. Equivalently, earlier strips are closed on the lower side and open on the upper side, while the last strip includes the outer upper endpoint. This choice affects only faces of zero area. The closed-boundary relation instead uses every closed range in Table [2](#tab:strips){reference-type="ref" reference="tab:strips"}; formulas [\[eq:branch-map\]](#eq:branch-map){reference-type="eqref" reference="eq:branch-map"} and [\[eq:inverse-map\]](#eq:inverse-map){reference-type="eqref" reference="eq:inverse-map"} are then mutually inverse on each edge, including its faces.

For completeness, the exactness generator in [\[eq:exactness\]](#eq:exactness){reference-type="eqref" reference="eq:exactness"} can be read off edge by edge. If the first coordinate is $X=a x+b$, then $B^*\alpha-\alpha=dG_{ij}$, with $$(G_{02},G_{12},G_{20},G_{21})
 =\left(0,-\frac y2,-\frac{y}{2\sqrt2},-\frac{y}{\sqrt2}\right).
 \label{eq:branch-generators}$$ These are branch-local primitives; no global smooth gluing across strip faces is claimed.

# Cycle and determinant ledger {#app:cycles}

The characteristic polynomial of $A$ is $t(t^2-2)$, which immediately gives [\[eq:fixed-counts\]](#eq:fixed-counts){reference-type="eqref" reference="eq:fixed-counts"} and $\det(I-zA)=1-2z^2$. For a direct check independent of traces, enumerate all closed state words of length $n$, retain a word only if no proper divisor of $n$ is a rotational period, and represent its orbit by the lexicographically least cyclic rotation. The trace/Möbius and direct procedures give the following complete count ledger.

::: {#tab:full-ledger}
       $n$          1    2    3    4    5    6    7    8    9   10
  -------------- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    SFT $P_n$       0    2    0    1    0    2    0    3    0    6
   Parent $P_n$     1    1    0    1    0    2    0    3    0    6
       $n$         11   12   13   14   15   16   17   18   19   20
    SFT $P_n$       0    9    0   18    0   30    0   56    0   99
   Parent $P_n$     0    9    0   18    0   30    0   56    0   99

  : Primitive orbit counts through the frozen maximum period.
:::

The parent ledger is obtained only after the declared quotient and should not be substituted for the unquotiented baker ledger in Corollary [\[cor:candidate\]](#cor:candidate){reference-type="ref" reference="cor:candidate"}.

The signed convention is also transparent at the Euler-factor level. The removed symbolic two-cycle has factor-orientation product $({-1})({-1})=+1$, whereas the added parent fixed point $d$ lies on a decreasing branch and has factor sign $-1$. Starting from the unquotiented weighted product one, the replacement contributes $$(1-z^2)(1+z)^{-1}=1-z,
 \label{eq:signed-boundary-factor}$$ which is the frozen object $D_{\mathrm{or,parent}}$ in [\[eq:orientation-conventions\]](#eq:orientation-conventions){reference-type="eqref" reference="eq:orientation-conventions"}. This derivation also shows why it must not be called the Lefschetz zeta. Likewise, substituting edge weight $2^{-s/2}$ into $A$, but not into $W$, produces the unsigned multiplier-clock product [\[eq:multiplier-product\]](#eq:multiplier-product){reference-type="eqref" reference="eq:multiplier-product"}; substitution into the nilpotent $W$ instead gives the factor-orientation multiplier product one.

# Reproducibility passport {#app:repro}

![Frozen implementation and control audit. (a) Each of three splits completed $16{,}777{,}216$ identified per-step forward/inverse checks with no boundary failure or edge mismatch. (b) Their common maximum roundtrip error was $1.388\times10^{-16}$, below the predeclared threshold. (c) Independent 100-digit parent residuals were below the $10^{-75}$ target; this was not interval certification. (d) Six matched controls separately test enumeration/symplecticity, paired reversal, dissipation, label loss, anti-symplectic rejection, and dependence of signed cancellation on factor signs.](<../../../../../symplectic_map/papers/2-branch-baker/paper/figures/fig3_audit_panel.pdf>){#fig:computational-audit width="\\linewidth"}

## Evidence and matched controls {#evidence-and-matched-controls .unnumbered}

Table [4](#tab:evidence){reference-type="ref" reference="tab:evidence"} records the inference boundary. Here "exact" means exact algebra or integer enumeration, not merely a passing tolerance.

::: {#tab:evidence}
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Audit                     Observed result                                                                                                                  Supports / does not support
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------
  PCF, PF, branch algebra   All symbolic residuals zero                                                                                                      Declared carrier / no global smoothness

  Two primitive ledgers     Vector [\[eq:primitive-vector\]](#eq:primitive-vector){reference-type="eqref" reference="eq:primitive-vector"}, total 226        Exact SFT counts / no arithmetic labels

  Boundary quotient         Lemma [\[lem:sole-boundary\]](#lem:sole-boundary){reference-type="ref" reference="lem:sole-boundary"}; audit through period 20   All-period parent quotient / not novel boundary theory

  Factor orientation        $W^3=0$, $\det(I-zW)=1$                                                                                                          Convention check / no quantum phase

  Parent audit              100 digits; max residual $9.706\times10^{-98}$                                                                                   Independent consistency / no interval proof

  Three floating splits     $3\times16{,}777{,}216$ checks; max error $1.388\times10^{-16}$                                                                  Stable implementation / no sampling inference

  Six controls              Every intended gate passed                                                                                                       Failure-mode specificity / no A2--A4 evidence

  Static isolation          Zero forbidden-data violation                                                                                                    Data discipline / no external target comparison
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : Evidence and inference boundary.
:::

The six controls alter one structural feature at a time. A dyadic baker is the positive enumeration/symplecticity control and has 747 primitive binary necklaces through period 12. A folded-tent baker verifies paired stable and unstable reversal with determinant $+1$. A matched dissipative map keeps the future graph but has determinant $1/2$ and a non-surjective image. Erasing labels breaks unique past reconstruction; reversing only one coordinate gives determinant $-1$ and is rejected. Finally, replacing all factor signs by $+1$ preserves the unsigned carrier but removes the nilpotent cancellation. These controls separate enumeration, coding, invertibility, symplecticity, and sign convention.

## Artifact and execution record {#artifact-and-execution-record .unnumbered}

All computations refer to candidate `pcf_markov_baker_v1`, source lock version 2, with source-lock SHA-256

`20473ff34b1f9258281483f47b9db915eb2680d2a71e9e1e6e9f3cf3d6fc07c8`

and frozen code-tree SHA-256

`ad7f6637a90e6f5cfc4933b89adc70c543c0d0f259f295ea84da10c6fa5f0b11`.

The pre-test verification manifest has SHA-256

`e3e79e94e1e7ec684cd66748498c7aba238eb25bbef629c778a069b755640c54`.

and records that the test had not been accessed before it was created. The final manifest contains hashes for every result artifact. Figure generators and their exact JSON inputs are separately recorded with the figure package; PDF creation timestamps preclude a claim of byte-identical rerendering.

The split seed rule takes the unsigned big-endian integer represented by the first eight bytes of $\operatorname{SHA256}(\texttt{pcf\_markov\_baker\_v1:split})$. It gives $$\begin{aligned}
 s_{\rm dev}&=9296786003925294372,\\
 s_{\rm val}&=6299270948367439428,\\
 s_{\rm test}&=17469014571681933606.
\end{aligned}
\label{eq:seeds}$$ Version 1 transcribed the development value as 18394334463172922998. The version-2 amendment repaired this mismatch before any run. A post-test development rerun to a temporary path was byte-identical to the frozen file; the sealed test was not rerun.

The recorded environment was Python 3.12.3 on Linux 5.4.0-155-generic x86\_64 (glibc 2.35), with NumPy 2.4.4, SymPy 1.14.0, mpmath 1.3.0, SciPy 1.16.1, and pytest 9.0.3. No GPU was used. The principal machine-readable outputs are , , , the three files, and . The source lock and access chain are under .

For a clean copy with fresh output paths, the documented entry-point order is

    python -m pytest
    python code/scripts/run_exact_preflight.py
    python code/scripts/run_ledger.py
    python code/scripts/audit_ledger.py
    python code/scripts/run_float_stress.py --split development
    python code/scripts/analyze_carrier.py --split development
    python code/scripts/freeze_splits.py validation
    python code/scripts/run_float_stress.py --split validation
    python code/scripts/analyze_carrier.py --split validation
    python code/scripts/freeze_splits.py test
    python code/scripts/run_float_stress.py --split test
    python code/scripts/analyze_carrier.py --split test

This is a reconstruction from the non-overwriting command-line entry points and frozen artifact order, not a claim that a literal historical shell transcript was retained. The entry points refuse to overwrite frozen JSON. Validation and test execution must follow their hash/unlock gates.
