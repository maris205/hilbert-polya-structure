---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--4-arith-flow"
canonical_tex: "flow_systems/papers/4-arith-flow/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/4-arith-flow/paper/paper.pdf"
source_sha256: "da04db49fc641c938f0ca2ecee7d9b4ad89b78a7fc6adebe871280b434ba8041"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# One Clock, One Characteristic: A Frobenius-Suspension Positive Control for Arithmetic Flow Zeta Functions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/4-arith-flow>)
- [规范 TeX](<../../../../../flow_systems/papers/4-arith-flow/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/4-arith-flow/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/4-arith-flow/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/4-arith-flow/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An exact match between an orbit product and an Euler product is informative only when the primitive objects and their clocks arise from a frozen arithmetic dynamics. We construct a positive control from arithmetic Frobenius on the geometric points of $\mathbb P^1_{\mathbb{F}_2}$, equipped with the explicitly disclosed discrete topology, and suspend it with constant roof $\log 2$. Closed points, primitive Frobenius cycles, and primitive suspension orbits are then in bijection, and the orbit attached to $x$ has least period $\deg(x)\log 2=\log N(x)$. We prove, first as a formal identity and then analytically on $\Re s>1$, that $$\zeta_{\mathrm{orb}}(s)
    =Z(\mathbb P^1_{\mathbb{F}_2},2^{-s})
    =\frac{1}{(1-2^{-s})(1-2^{1-s})}.$$ The repetition coefficient $1/r$ and logarithmic weight $\log N(x)$ follow from the primitive factor and differentiation; neither is inserted as a potential. The same construction gives a sharp transfer boundary. If $Q=\ell^f$ and $n\log Q=r\log p$, unique factorization forces $p=\ell$, so one finite-field clock cannot produce rational-prime periods across characteristics. A disjoint union of circles of lengths $\log p$ does reproduce the Riemann Euler product, but the identical construction compiles any prescribed locally finite length multiset and therefore fails the arithmetic-origin gate. Cohomological Frobenius determinants are kept distinct from any transfer determinant of the neutral circle flow. The result is an exact native finite-field Route-A calibration, a proved rejection for the Riemann target, and no Route-B or Hilbert--Pólya claim.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 13 August 2026
title: |
  **One Clock, One Characteristic:**\
  A Frobenius-Suspension Positive Control for Arithmetic Flow Zeta Functions
```

## Markdown 正文

**摘要**

轨道乘积与 Euler 乘积的精确相等，只有在本原对象及其时钟由预先冻结的 算术动力系统产生时才具有判别力。本文取 $\mathbb P^1_{\mathbb F_2}$ 几何点上的算术 Frobenius，明确赋予其离散 拓扑，并以 $\log 2$ 为常值屋顶构造悬挂流。由此，闭点、本原 Frobenius 循环与本原流轨道一一对应；闭点 $x$ 的最小周期为 $\deg(x)\log2=\log N(x)$。本文先在形式幂级数层面、再在 $\Re s>1$ 的绝对收敛域内证明轨道 zeta 恰为 $Z(\mathbb P^1_{\mathbb F_2},2^{-s})
=((1-2^{-s})(1-2^{1-s}))^{-1}$。重复系数 $1/r$ 来自本原因子的 对数展开，$\log N(x)$ 则来自对悬挂时间参数求导，二者均非外加权重。 同一模型也给出严格的迁移边界：若 $Q=\ell^f$ 且 $n\log Q=r\log p$，唯一分解迫使 $p=\ell$，故一个有限域时钟不能 跨特征生成全部有理素数周期。虽然逐个赋予长度 $\log p$ 的互不相交 圆周能够精确写出 Riemann Euler 乘积，但该方法同样能够编译任意预设的 局部有限长度集合，因而在算术来源门槛处失败。本文严格区分上同调 Frobenius 行列式与中性圆周流可能具有的转移算子行列式。最终结论是： 该模型构成有限域原生目标的精确 Route-A 正控；对于 Riemann 目标则被 严格拒绝；本文不启动 Route B，也不提出 Hilbert--Pólya 声明。

**Keywords:** arithmetic dynamics; Frobenius suspension; Hasse--Weil zeta function; primitive orbit; constant roof; Euler-product compiler; Route-A audit.

# Introduction {#sec:intro}

Periodic-orbit formulas make arithmetic and dynamics look unusually close. For a map with finitely many fixed points of each iterate, the Artin--Mazur construction packages the fixed-point counts in an exponential generating function [@ArtinMazur1965]. In finite characteristic, the same fixed points are rational points over extension fields, while closed points are Frobenius orbits and the resulting product is the Hasse--Weil zeta function [@Deligne1974; @Milne2013]. Suspending a return map turns discrete cycles into closed flow orbits whose periods are roof sums, a standard bridge between maps and flows [@ParryPollicott1990]. These facts provide a rare setting in which arithmetic source, primitive objects, clock, and zeta can all be audited exactly.

Exact scalar agreement is nevertheless too weak to certify an arithmetic flow. Given a list of positive numbers $L_j$, one may place a translation flow on one circle of circumference $L_j$ for each index $j$. Its primitive-orbit product is automatically $\prod_j(1-\mathrm{e}^{-sL_j})^{-1}$. Choosing $L_p=\log p$ therefore writes the Riemann Euler product into a phase space without discovering either primes or their periods. A useful positive control must succeed for a reason that this universal compiler does not share.

This paper asks a deliberately narrow question. For a fixed variety over a finite field, does constant-roof Frobenius suspension give an exact, locally compact continuous-time realization of its closed-point Euler product, and what prevents the same one-clock construction from generating the rational-prime divisor of $\operatorname{Spec}\mathbb{Z}$? The concrete object is frozen before analysis: $$X=\mathbb P^1_{\mathbb{F}_2},\qquad
  S=X(\overline{\mathbb{F}}_2)_{\mathrm{disc}},\qquad
  F(a)=a^2,\qquad \tau=\log2.$$ The subscript "disc" matters. The arithmetic set and Frobenius action are intrinsic, but the locally compact Hausdorff topology used for the suspension is an imposed modeling choice.

Four theorem-level results follow. First, closed points of $X$, primitive Frobenius cycles on $S$, and primitive suspension orbits are in bijection; the period is exactly $\deg(x)\log2=\log N(x)$. Second, the unweighted orbit product equals the Artin--Mazur and Hasse--Weil zeta functions, and the coefficients $1/r$ and $\log N(x)$ have explicit internal provenance. Third, the Euler product converges absolutely exactly for $\Re s>1$, while the rational expression gives a separate meromorphic continuation with a single-clock imaginary period. Fourth, a fixed clock $\log Q$, where $Q=\ell^f$, can meet a rational-prime-power clock only for $p=\ell$. The construction is consequently exact for its native finite-field target and incompatible with the rational-prime target.

The contribution is a source-locked synthesis and falsification audit, not a claim that the classical component identities are new. It keeps three determinant notions separate: the primitive-orbit Euler product, the Artin--Mazur fixed-point zeta, and the $\ell$-adic cohomological Frobenius determinant. Their scalar values agree because they share an arithmetic source. No operator conjugacy or trace theorem identifies the last object with a transfer operator of the neutral circle flow.

The Route-A consequence is correspondingly split. Against the native Hasse--Weil target, the object is an exact positive control through the controlled-continuation layer. Against Riemann $\zeta/\xi$, it fails the arithmetic support and determinant layers. The disjoint-prime repair is rejected even though its product is exact, because it reads the target divisor and roof lengths into the phase space. No Route-B layer is opened.

# Source lock, conventions, and research design {#sec:lock}

## The frozen object

Let $F:S\to S$ be the permutation induced by the square map. We use the term *arithmetic Frobenius* for the point action $a\mapsto a^2$, in the convention recorded by the Stacks Project [@Stacks03SL]. Some cohomological sources formulate trace identities using geometric Frobenius or an inverse Galois convention. We do not identify those actions by notation: the return map in the flow is always the displayed square map. Replacing it by its inverse reverses each finite cycle but changes neither the cycle length nor the unweighted orbit product.

Give $S$ the discrete topology and let $\mathbb{Z}$ act on $S\times\mathbb{R}$ by $$n\cdot(a,u)=(F^n a,u-n\tau),\qquad \tau=\log2.
  \label{eq:action}$$ The mapping torus and vertical flow are $$M_F=(S\times\mathbb{R})/\mathbb{Z},
  \qquad
  \phi^t[a,u]=[a,u+t].
  \label{eq:suspension}$$ This is the constant-roof version of the standard suspension construction [@ParryPollicott1990 Chap. 6]. The reference supplies the convention; the topology of this noncompact countable-discrete base is proved directly in Section [3](#sec:orbits){reference-type="ref" reference="sec:orbits"}.

The primitive-orbit zeta is frozen as $$\zeta_{\mathrm{orb}}(s)
    :=\prod_{\gamma\in\mathcal{P}(M_F)}
      \left(1-\mathrm{e}^{-s\ell_\gamma}\right)^{-1}.
  \label{eq:orbit-zeta}$$ Primitive multiplicity is one and orientation is positive vertical time. There is no potential, phase, half-shift, stability denominator, fitted prefactor, orbit cutoff, or numerical parameter.

::: {#tab:lock}
  Field               Frozen value                                        Status
  ------------------- --------------------------------------------------- --------------------------------
  Arithmetic scheme   $\mathbb P^1_{\mathbb{F}_2}$                        intrinsic
  Return map          $F(a)=a^2$                                          intrinsic
  Base topology       discrete topology on $X(\overline{\mathbb{F}}_2)$   [MODELING CHOICE]{.sans-serif}
  Roof and clock      constant $\tau=\log2$                               base-field norm
  Orbit weight        one unweighted primitive factor                     frozen convention
  Target, native      $Z(\mathbb P^1_{\mathbb{F}_2},2^{-s})$              tested
  Target, Riemann     $\zeta(s)$ or $\xi(s)$                              not assumed
  Data use            exact algebra and deterministic controls            no zeros or fitting

  : Candidate lock and provenance. The discrete topology is the main additional modeling choice; the roof and orbit-zeta normalization are also explicitly frozen.
:::

## Evidence and falsification design

The primary sources were checked through 13 August 2026. Artin and Mazur provide the fixed-point zeta definition and its finite-field power-map example [@ArtinMazur1965]. Deligne supplies the closed-point product, Frobenius orbit dictionary, fixed-point counts, cohomological determinant, and native functional-equation framework [@Deligne1974]. Parry and Pollicott supply standard suspension and orbit-zeta conventions [@ParryPollicott1990]; the Stacks Project fixes Frobenius terminology and finite residue-field facts [@Stacks01TF; @Stacks03SL]; and Milne provides an independent authoritative check of point-count and cohomological formulas [@Milne2013].

The source scope is deliberately asymmetric. Hyperbolic suspension results are not transferred to the present neutral, disconnected flow. Conversely, the cohomological rationality theorem is not called a transfer-operator theorem for the circle suspension. Statements about the topology, circle decomposition, exact convergence boundary, clock obstruction, and universal compiler are established below by direct proof.

Ten obligations were frozen before manuscript composition: completeness of the closed-point dictionary; topological legitimacy; separation of primitive and repeated orbits; agreement of the three native zeta conventions; provenance of weights; separation of convergence and continuation; the one-clock test; a non-tautology gate; target-specific Route-A verdicts; and exclusion of Riemann-zero information. The strongest adversarial controls are exact rather than statistical: inverse Frobenius, same-cycle-type permutations, base-field change, the arbitrary-length circle compiler, and the disjoint $\log p$ construction.

# Closed points become primitive flow circles {#sec:orbits}

## The Frobenius ledger

Closed points of the affine chart $\mathbb A^1_{\mathbb{F}_2}$ correspond to monic irreducible polynomials. The point at infinity supplies one additional rational closed point. This concrete description agrees with the general theorem that closed points over a finite field are Frobenius orbits on the geometric points [@Deligne1974 Sec. 1.4].

[\[lem:cycle\]]{#lem:cycle label="lem:cycle"} Let $f\in\mathbb{F}_2[T]$ be monic and irreducible of degree $d$, and let $a$ be one of its roots. The points $$a,a^2,a^{2^2},\ldots,a^{2^{d-1}}$$ are distinct, form the full root set of $f$, and constitute an $F$-cycle of least length $d$.

The residue field $\mathbb{F}_2[T]/(f)$ is $\mathbb{F}_{2^d}$, hence $F^d(a)=a$. If $F^n(a)=a$, then $a\in\mathbb{F}_{2^n}$. The subfield $\mathbb{F}_2(a)=\mathbb{F}_{2^d}$ embeds in $\mathbb{F}_{2^n}$, which forces $d\mid n$. Thus no smaller positive iterate fixes $a$, and its $d$ conjugates are exactly the roots of $f$.

Let $a_d$ denote the number of degree-$d$ closed points of $\mathbb P^1_{\mathbb{F}_2}$. Lemma [\[lem:cycle\]](#lem:cycle){reference-type="ref" reference="lem:cycle"} gives $$a_1=3,
  \qquad
  a_d=\frac1d\sum_{e\mid d}\mu(e)2^{d/e}\qquad(d>1).
  \label{eq:closed-count}$$ Every geometric point is defined over a finite extension, so every element of $S$ lies in one finite cycle. If $N_n=\#\mathbb P^1(\mathbb{F}_{2^n})=2^n+1$, a cycle of exact size $d$ contributes all its $d$ points to $\operatorname{Fix}(F^n)$ precisely when $d\mid n$. Therefore $$N_n=2^n+1=\sum_{d\mid n}d\,a_d.
  \label{eq:fixed-ledger}$$ This is the complete primitive-versus-repetition ledger on the discrete base.

## Circle decomposition and topology

[\[thm:dictionary\]]{#thm:dictionary label="thm:dictionary"} For the frozen object there is a flow-preserving homeomorphism $$M_F\cong
  \coprod_{x\in|\mathbb P^1_{\mathbb{F}_2}|}
  \mathbb{R}/(\deg(x)\log2)\mathbb{Z}.
  \label{eq:circle-decomp}$$ Consequently closed points, primitive Frobenius cycles, and primitive suspension orbits are in bijection. The orbit $\gamma_x$ has least period $$\ell_x=\deg(x)\log2=\log(2^{\deg x})=\log N(x),
  \label{eq:period}$$ and its $r$-fold traversal has period $r\ell_x$. Every flow point is periodic, and the primitive ledger is locally finite by length.

Choose a root $a$ in the cycle $C_x$ and put $d=\deg(x)$. On the suspension of that cycle define $$\Psi_x([F^j a,u])=u+j\log2\pmod{d\log2}.$$ Equation [\[eq:action\]](#eq:action){reference-type="eqref" reference="eq:action"} replaces $(F^j a,u)$ by $(F^{j+n}a,u-n\log2)$; both representatives have the same image. Thus $\Psi_x$ is well defined. It is a continuous bijection with the evident continuous inverse and intertwines vertical translation. Its coordinate depends on the chosen root, but the component orbit and its period do not. The least positive return requires exactly $d$ base iterates, proving [\[eq:period\]](#eq:period){reference-type="eqref" reference="eq:period"}.

Distinct Frobenius cycles are disjoint open-and-closed subsets because $S$ is discrete. Below a length bound $T$, only degrees $d\leq T/\log2$ occur, and there are finitely many closed points in each such degree. This proves completeness and local finiteness.

The quotient also passes the elementary topological checks. The $\mathbb{Z}$-action is free because equality of real coordinates in [\[eq:action\]](#eq:action){reference-type="eqref" reference="eq:action"} forces $n\log2=0$. It is properly discontinuous: the real projection of a compact subset is bounded, and only finitely many translates by $n\log2$ can meet that bounded interval. Hence the quotient is locally compact and Hausdorff. It is second countable because it is a countable disjoint union of second-countable circles, and it is noncompact because it has infinitely many open-and-closed components.

These positive properties should not be confused with chaotic dynamics. The flow has no nonzero transverse tangent direction, no stable or unstable multiplier, no mixing, and no interaction between primitive components. A Poincaré section is zero-dimensional. This degeneracy is central to the later determinant distinction.

# Exact native zeta and endogenous weights {#sec:zeta}

Artin and Mazur define the fixed-point zeta by $$\zeta_{AM}(z)
   =\exp\!\left(\sum_{n\geq1}\frac{N_n}{n}z^n\right)
  \label{eq:am}$$ when the fixed-point counts are finite [@ArtinMazur1965 p. 84]. For a finite-field power map they identify this with the classical zeta. The following proof records exactly how the primitive cycle ledger enters.

[\[thm:zeta\]]{#thm:zeta label="thm:zeta"} As formal power series in $z$, $$\begin{aligned}
  \zeta_{AM}(z)
   &=\prod_{d\geq1}(1-z^d)^{-a_d}\\
   &=\prod_{x\in|\mathbb P^1_{\mathbb{F}_2}|}
       (1-z^{\deg x})^{-1}\\
   &=Z(\mathbb P^1_{\mathbb{F}_2},z)
    =\frac1{(1-z)(1-2z)}.
\end{aligned}
\label{eq:three-zeta}$$ After $z=2^{-s}$, the identity becomes $$\boxed{
  \zeta_{\mathrm{orb}}(s)
  =Z(\mathbb P^1_{\mathbb{F}_2},2^{-s})
  =\frac1{(1-2^{-s})(1-2^{1-s})}.}
  \label{eq:boxed-zeta}$$ It holds analytically by the Euler product on $\Re s>1$, and the rational expression supplies a meromorphic continuation beyond that domain.

Using [\[eq:fixed-ledger\]](#eq:fixed-ledger){reference-type="eqref" reference="eq:fixed-ledger"}, formal reindexing gives $$\begin{aligned}
 \sum_{n\geq1}\frac{N_n}{n}z^n
  &=\sum_{n\geq1}\frac{z^n}{n}\sum_{d\mid n}d a_d
    =\sum_{d\geq1}a_d\sum_{r\geq1}\frac{z^{rd}}r\\
  &=-\sum_{d\geq1}a_d\log(1-z^d).
\end{aligned}$$ Each coefficient uses only finitely many divisors, so no analytic rearrangement is hidden in this step. Exponentiation gives the first two equalities in [\[eq:three-zeta\]](#eq:three-zeta){reference-type="eqref" reference="eq:three-zeta"}. The closed-point product is the Hasse--Weil definition [@Deligne1974 Sec. 1.1]. Finally, $$\exp\!\left(\sum_{n\geq1}\frac{(2^n+1)z^n}{n}\right)
  =\exp[-\log(1-2z)-\log(1-z)],$$ which proves the rational expression. Theorem [\[thm:dictionary\]](#thm:dictionary){reference-type="ref" reference="thm:dictionary"} converts $z^{\deg x}$ into $\mathrm{e}^{-s\ell_x}$.

[\[cor:weights\]]{#cor:weights label="cor:weights"} On the absolute-convergence half-plane, $$\begin{aligned}
  \log\zeta_{\mathrm{orb}}(s)
   &=\sum_x\sum_{r\geq1}\frac{N(x)^{-rs}}r,
  \label{eq:logzeta}\\
  -\frac{d}{ds}\log\zeta_{\mathrm{orb}}(s)
   &=\sum_x\sum_{r\geq1}\log N(x)\,N(x)^{-rs}.
  \label{eq:logderivative}\end{aligned}$$ Thus $1/r$ is forced by the logarithm of a primitive factor, while $\log N(x)=\ell_x$ is forced by differentiation with respect to suspension time.

The result is positive but tightly scoped. No sign, complex phase, $N(x)^{-r/2}$ amplitude, or stability denominator appears in [\[eq:logderivative\]](#eq:logderivative){reference-type="eqref" reference="eq:logderivative"}. Introducing a half-shift in $s$ would change the frozen normalization rather than reveal a latent term. Replacing $F$ with $F^{-1}$ leaves [\[eq:boxed-zeta\]](#eq:boxed-zeta){reference-type="eqref" reference="eq:boxed-zeta"} unchanged, so orientation reversal cannot supply such a phase.

::: {#tab:ledger}
    $d$   affine irreducibles   $a_d$ on $\mathbb P^1$   $2^d+1$   $\sum_{e\mid d}e a_e$
  ----- --------------------- ------------------------ --------- -----------------------
      1                     2                        3         3                       3
      2                     1                        1         5                       5
      3                     2                        2         9                       9
      4                     3                        3        17                      17
      5                     6                        6        33                      33
      6                     9                        9        65                      65
      7                    18                       18       129                     129
      8                    30                       30       257                     257

  : The first eight rows of the exact closed-point ledger. The finite table is a regression control; Equation [\[eq:fixed-ledger\]](#eq:fixed-ledger){reference-type="eqref" reference="eq:fixed-ledger"} is the proof.
:::

# Convergence, continuation, and determinant types {#sec:analytic}

[\[thm:convergence\]]{#thm:convergence label="thm:convergence"} The logarithmic orbit expansion and primitive Euler product converge absolutely exactly for $\Re s>1$.

Put $\sigma=\Re s$. For $\sigma>0$, positivity and [\[eq:am\]](#eq:am){reference-type="eqref" reference="eq:am"} reduce absolute convergence to $$\sum_{n\geq1}\frac{(2^n+1)2^{-\sigma n}}n.
  \label{eq:convseries}$$ The first part is $\sum_n2^{(1-\sigma)n}/n$. It converges for $\sigma>1$, becomes the harmonic series at $\sigma=1$, and fails the term test for $0<\sigma<1$. The second positive part cannot repair that divergence. For $\sigma\leq0$, the primitive factors do not approach one in the required manner (and may be singular), so absolute Euler-product convergence also fails.

The rational function in [\[eq:boxed-zeta\]](#eq:boxed-zeta){reference-type="eqref" reference="eq:boxed-zeta"} continues meromorphically to all $s\in\mathbb{C}$. This does not mean that the defining Euler product converges after continuation. It also makes the single clock visible: $$\zeta_X\!\left(s+\frac{2\pi i k}{\log2}\right)=\zeta_X(s),
  \qquad k\in\mathbb{Z}.
  \label{eq:imag-period}$$ The poles lie on the two lattices $$s=\frac{2\pi i k}{\log2},
  \qquad
  s=1+\frac{2\pi i k}{\log2}.$$ Writing $Z(t)=((1-t)(1-2t))^{-1}$, direct algebra gives $$Z\!\left(\frac1{2t}\right)=2t^2Z(t),
  \qquad
  \zeta_X(1-s)=2^{1-2s}\zeta_X(s).$$ This is the native $\mathbb P^1$ functional relation, not the completed Riemann functional equation.

The scalar equality in Theorem [\[thm:zeta\]](#thm:zeta){reference-type="ref" reference="thm:zeta"} passes through three logically different constructions, summarized in Table [\[tab:determinants\]](#tab:determinants){reference-type="ref" reference="tab:determinants"}. Deligne's cohomological formula has the form $$Z(X,t)=\prod_i
  \det\!\left(I-t\Phi_{\mathrm{coh}}\mid
  H_c^i(X_{\overline{\mathbb{F}}_Q},\mathbb Q_\ell)\right)^{(-1)^{i+1}}.
  \label{eq:cohom-det}$$ Here $\Phi_{\mathrm{coh}}$ denotes the cohomological Frobenius in the convention of the cited trace formula, commonly geometric Frobenius in Galois notation. It is deliberately not denoted by $F$: the suspension return map is the arithmetic point action $a\mapsto a^Q$. The two point permutations are inverse and have the same finite cycles and fixed-point counts, but their operator actions must not be conflated. For $\mathbb P^1/\mathbb{F}_2$, the cohomological determinant factors are $1-t$ and $1-2t$. It provides rational continuation, and Poincaré duality supplies the native functional equation in the proper smooth setting [@Deligne1974 Secs. 1.5 and 2.6]; see also [@Milne2013 Secs. 26--29]. Equation [\[eq:cohom-det\]](#eq:cohom-det){reference-type="eqref" reference="eq:cohom-det"} acts on $\ell$-adic cohomology. It is not the determinant of a Poincaré return derivative or a trace-class transfer operator of the circle flow.

\@L0.24Y L0.25@ Construction & Defined from & What is proved\
Primitive-orbit Euler product & one factor per suspension circle & equals the native closed-point product\
Artin--Mazur zeta & fixed-point counts $N_n$ & equals the same formal series\
Cohomological Frobenius determinant & $\Phi_{\mathrm{coh}}$ on compactly supported $\ell$-adic cohomology & rationality and native analytic structure\
Circle-flow transfer determinant & an operator and trace ideal not supplied here & [NOT TESTABLE]{.sans-serif}\

The equality of the first three scalar functions is explained by their common arithmetic ledger. An operator equivalence between the second or third and a flow transfer operator would require a separately defined space, action, domain, trace, and intertwining theorem. None is implicit in the circle decomposition.

# One clock cannot cross characteristics {#sec:clock}

The fixed-field construction extends without parameter fitting to any fixed variety over $\mathbb{F}_Q$: arithmetic Frobenius cycles yield primitive periods $\deg(x)\log Q$. Changing the variety alters multiplicities, but every period remains in the lattice $(\log Q)\mathbb{N}$. The following elementary theorem locates the exact characteristic-zero obstruction.

[\[thm:clock\]]{#thm:clock label="thm:clock"} Let $Q=\ell^f$, where $\ell$ is a rational prime and $f\geq1$. If positive integers $n,r$ and a rational prime $p$ satisfy $$n\log Q=r\log p,
  \label{eq:clock-equality}$$ then $p=\ell$ and $fn=r$. If $n\log Q=\log p$, then $Q=p=\ell$ and $f=n=1$.

Exponentiating [\[eq:clock-equality\]](#eq:clock-equality){reference-type="eqref" reference="eq:clock-equality"} gives $\ell^{fn}=p^r$. Unique factorization in $\mathbb{Z}$ forces $p=\ell$, after which equality of exponents yields $fn=r$. When $r=1$, positivity of $f$ and $n$ forces $f=n=1$.

The obstruction is an equality statement, not a rank or density comparison. One may have accidental numerical proximity between unrelated logarithms, but an exact period identity across distinct prime bases is impossible. Passing from one finite field to all rational primes therefore requires a new global clock mechanism or an object that genuinely couples residue characteristics. No larger variety over the same $\mathbb{F}_Q$ can remove the lattice restriction.

There is also a purely analytic signature. Every rational function of $Q^{-s}$ has the nonzero imaginary period $2\pi i/\log Q$. The rational Euler product has no such fixed imaginary period on $\Re s>1$. Indeed, if its absolutely convergent Dirichlet series were periodic by $iT$, uniqueness would force both $2^{-iT}=1$ and $3^{-iT}=1$. Hence $T\log2,T\log3\in2\pi\mathbb{Z}$, which for nonzero $T$ would imply an equality $2^a=3^b$ with positive integers $a,b$, contradicting unique factorization. This distinguishes the analytic clocks without consulting Riemann zeros.

# The exact repair that proves too much {#sec:compiler}

The most tempting repair is to abandon one clock and give each rational prime its own component. It is better to state the universal theorem first.

[\[thm:compiler\]]{#thm:compiler label="thm:compiler"} Let $J$ be countable and let $\{L_j:j\in J\}\subset(0,\infty)$ be locally finite in length. The translation flow on $$M_L=\coprod_{j\in J}\mathbb{R}/L_j\mathbb{Z}
  \label{eq:compiler-space}$$ is locally compact, Hausdorff, and second countable, with exactly one primitive orbit of length $L_j$ on each component. Wherever it converges, $$\zeta_{M_L}(s)=\prod_{j\in J}(1-\mathrm{e}^{-sL_j})^{-1}.
  \label{eq:compiler-product}$$

The topological properties hold componentwise for the countable coproduct. Local finiteness of $\{L_j\}$ gives a finite primitive ledger below every length cutoff. Translation on one circle has the whole circle as one primitive orbit, whose repetitions give the geometric factor in [\[eq:compiler-product\]](#eq:compiler-product){reference-type="eqref" reference="eq:compiler-product"}. Multiplication over components proves the identity.

Taking $J$ to be the rational primes and $L_p=\log p$ produces $$M_{\mathbb{Z}}^{\mathrm{taut}}
   =\coprod_p\mathbb{R}/(\log p)\mathbb{Z},
  \qquad
  \zeta_{M_{\mathbb{Z}}^{\mathrm{taut}}}(s)=\zeta(s)
  \quad(\Re s>1).
  \label{eq:prime-compiler}$$ The invariant-looking notation $$\coprod_{x\in|\operatorname{Spec}\mathbb{Z}|}\mathbb{R}/(\log N(x))\mathbb{Z}$$ does not alter the information flow. Every target closed point and its norm are queried before the corresponding component exists. There is no coupled return map whose periodic points generate the divisor.

Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"} works equally for composite-only lengths, quadratic-irrational lengths, a randomized locally finite list, or a divisor chosen from an unrelated function. It therefore establishes an exact proves-too-much control. In Route-A language, the prime-circle flow has an exact primitive ledger and an exact orbit product, but it fails A0 because both the target labels and the $\log p$ roofs are inputs.

The same-cycle-type control exposes a second limitation. Let $G$ be a permutation of a countable discrete set for which every point is periodic and whose number of cycles of each finite length equals that of $F$. Then $G$ is conjugate to $F$ as a discrete dynamical system: match cycles one-by-one and preserve cyclic order. Its constant-roof suspension is therefore flow-conjugate to $M_F$ and has the same orbit zeta. The periodicity hypothesis is essential: additional infinite orbits would be additional components not present in the frozen Frobenius system. The bare flow topology remembers the sequence $(a_d)$, but it does not recover the algebraic geometry or $\ell$-adic cohomology that generated those counts.

# Target-specific Route-A assessment {#sec:route}

A verdict without a named target would merge two incompatible claims. The native finite-field zeta and the Riemann zeta are therefore evaluated in separate columns, with the compiler retained as an adversarial control.

\@L0.075YYY@ Layer & Native $Z(\mathbb P^1/\mathbb{F}_2)$ & Same flow, Riemann target & Disjoint-prime compiler\
A0 & `ANALYTIC_ARITHMETIC_ORIGIN` & `FAIL`: one characteristic & `FAIL`: target encoded\
A1 & `PASS_ANALYTIC` & exact flow ledger, wrong support & `PASS_ANALYTIC`\
A2 & `ANALYTIC_DETERMINANT` & `FAIL`: wrong product and clock & exact only tautologically\
A3 & `CONTROLLED_CONTINUATION` & `FAIL`: incompatible global structure & `FAIL`: no dynamical provenance\
A4 & `FAIL / NOT_TESTABLE` & `FAIL / NOT_TESTABLE` & `FAIL / NOT_TESTABLE`\
Overall & `SUCCESS_ROUTE_B_NOT_READY`, native calibration only & `ROUTE_A_REJECTED` & `REJECTED / PROVES_TOO_MUCH`\

For the native target, A0 is analytic because the scheme and its Frobenius generate the closed-point ledger before the zeta is evaluated. A1 is analytic because primitive cycles, repetitions, orientation, multiplicity, completeness, and local finiteness are exact. A2 records an exact orbit-zeta identity, not a trace-class operator theorem. A3 records native rational continuation and the functional relation with their cohomological source named. A4 fails because no natural quantization, unitary completion, or scattering lift has been defined.

For the Riemann target, A0 fails by Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}. The orbit ledger still exists, but it carries the wrong primitive support. A2 fails because the determinant is the wrong Euler product and has the wrong single-clock periodicity. A3 lacks the Riemann gamma factor, pole removal, counting law, and an intrinsic Weil-form compression. A4 again has no candidate lift. The overall status is `ROUTE_A_REJECTED`.

For the compiler, A1 and the formal orbit product are exact only because the desired index set and lengths were supplied as input. The construction receives `A0_FAIL` and `STOP_SCOPED / PROVES_TOO_MUCH`. This is precisely why scalar zeta matching is subordinate to arithmetic provenance.

No object in this paper has `route_b_invocation_allowed: true`. No B1--B5 evaluation is performed, and no self-adjoint or Hilbert--Pólya claim is inferred from the finite-field calibration.

# Deterministic controls {#sec:controls}

The companion Python program checks the proof ledger with exact integer and finite-polynomial arithmetic. A polynomial over $\mathbb{F}_2$ is encoded by its coefficient bits. Monic polynomials through degree 12 are enumerated, and irreducibility is certified by the Frobenius--Rabin criterion: for a monic degree-$d$ polynomial $f$, the program checks $T^{2^d}\equiv T\pmod f$ and the required gcd conditions for prime divisors of $d$. It then adds the point at infinity in degree one.

The run examined 8190 monic polynomials, found 747 affine irreducibles, and therefore recorded 748 projective closed points through degree 12. Every enumerated count equals the Möbius formula, and every fixed-point count $2^n+1$ is recovered from primitive cycles. The formal orbit product and $1/((1-z)(1-2z))$ have identical coefficients through the frozen order; the coefficient at $z^n$ is $2^{n+1}-1$. A separate ledger records each pair $(d,r)$, retaining $1/r$ and $d\log2$ as distinct sources.

Further controls evaluate finite partial Euler logs on both sides of $\Re s=1$, verify [\[eq:imag-period\]](#eq:imag-period){reference-type="eqref" reference="eq:imag-period"} to floating-point tolerance, and exhaust a finite grid of clock equalities generated at runtime. All 90 grid solutions use the same characteristic and satisfy the exponent identity $fn=r$. Finally, composite-only, integer-log, and quadratic-irrational circle profiles reproduce their encoded products just as the prime-circle construction does.

\@L0.29L0.20Y@ Control & Result & Interpretation\
Unit tests & 13/13 pass & implementation integrity\
Möbius versus enumeration & all degrees 1--12 match & finite exact regression\
Fixed points from cycles & all degrees 1--12 match & primitive/repetition separation\
Formal zeta coefficients & orders 0--12 match & finite check of an independently proved identity\
Clock grid & 90/90 solutions same-characteristic & finite check of Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}\
Imaginary periodicity & maximum displayed error below $3.0\times10^{-14}$ & floating-point software check\
Unrelated circle profiles & encoded and orbit products agree & proves-too-much control\

These computations do not upgrade a theorem's evidence status. They use no Riemann-zero locations, fitted scale or shift, random seed, network data, or hard-coded rational-prime table. Primes needed for the finite same-characteristic grid are generated by trial division at runtime. From the paper directory, the full suite is reproduced with

    bash experiments/reproduce.sh

# Discussion {#sec:discussion}

The Frobenius suspension succeeds at the interface that failed for less structured orbit proposals: it has one primitive arithmetic object per primitive flow orbit, an exact return clock, endogenous repetitions, and a closed-form zeta. Nothing is inferred from a fitted spectral statistic. This makes it a clean finite-field calibration for evaluating more ambitious arithmetic flows.

The calibration also exposes a boundary. The statement that closed points resemble periodic orbits is not yet a characteristic-zero construction. Over one finite field, every norm is a power of one base $Q$. A constant roof converts degree into $\log N(x)$ because $N(x)=Q^{\deg x}$. Over $\operatorname{Spec}\mathbb{Z}$, closed-point norms have different prime bases. Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"} says that the difference is not repaired by increasing degree, changing multiplicities, or choosing a larger variety over the same field.

The hostile objection to the positive control is valid: after imposing the discrete topology, the suspension is an orbit ledger in geometric dress. An arbitrary permutation with the same cycle counts produces the same bare flow. The construction does not retain Zariski incidence, a transverse derivative, or cohomology as intrinsic topology of the circle union. Its value lies in making every normalization decision visible and exact, not in supplying dynamical complexity.

The determinant taxonomy sharpens the next problem. The orbit product and the cohomological determinant agree as functions because both read the same closed-point counts. A same-object operator bridge would have to explain how the circle dynamics acts on a trace domain whose fixed-point coefficients recover the cohomological expression. Equality of scalar outputs alone does not construct that bridge. In particular, no stability factor or signed phase can be borrowed from $\ell$-adic cohomology and then described as a return derivative of a zero-dimensional transverse section.

The universal compiler gives a practical falsification rule for future proposals. If replacing the purported arithmetic objects by any locally finite length list leaves the proof unchanged, the proof establishes realizability, not arithmetic emergence. The next construction must therefore couple residue characteristics before its primitive ledger is known. It must derive $\log N(x)$ as a return time from one global mechanism, and it must possess a topology or trace framework that does more than take a coproduct of already labeled circles.

One precise next theorem obligation is consequently available: construct a single non-disjoint arithmetic phase space across residue characteristics with (i) an intrinsic return map generating its primitive closed objects, (ii) an emergent norm clock, (iii) a locally compact or otherwise trace-controlled global structure, and (iv) an exact test that distinguishes it from Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"}. Determinant or quantum analysis should wait until those four clauses are satisfied.

# Limitations {#sec:limitations}

The discrete topology on $X(\overline{\mathbb{F}}_2)$ is imposed. It is useful because it makes the suspension locally compact and completely explicit, but it suppresses algebraic adjacency and does not arise as the usual topology of the scheme. The resulting flow is disconnected and neutral: every component is one periodic circle, all points are periodic, and there is no transverse hyperbolicity or mixing.

Equation [\[eq:orbit-zeta\]](#eq:orbit-zeta){reference-type="eqref" reference="eq:orbit-zeta"} defines an orbit Euler product, not a trace-class flow operator. This paper constructs no transfer space, nuclear operator, wave trace, or Lefschetz complex for the suspension. The cohomological determinant in [\[eq:cohom-det\]](#eq:cohom-det){reference-type="eqref" reference="eq:cohom-det"} belongs to the algebraic variety and Frobenius action. An operator-level identification with the flow remains [NOT TESTABLE]{.sans-serif}.

The native finite-field continuation and functional relation do not provide a Riemann gamma factor, Riemann--von Mangoldt counting law, Weil compression, unitary lift, self-adjoint generator, or spectral determinant. The one-clock theorem rejects this frozen candidate for rational-prime support, but it is not a no-go theorem for every possible arithmetic dynamics across characteristics. The computation cutoff at degree 12 is only a software regression bound; none of the exact conclusions depends on it.

# Conclusion

Arithmetic Frobenius on $\mathbb P^1/\mathbb{F}_2$, after a disclosed discrete-topology choice and constant-roof suspension, gives an exact native finite-field positive control. Closed points are primitive flow orbits, their periods are $\log N(x)$, and the orbit, Artin--Mazur, and Hasse--Weil zetas agree with internally derived repetition and logarithmic weights.

The same proof determines the boundary. A single $Q$-clock sees only its own characteristic, while disjoint $\log p$ circles merely compile the target Euler product. The native control therefore passes Route A only in its stated finite-field scope; the Riemann target is rejected, and no Route-B or Hilbert--Pólya conclusion follows.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

#### Data and code availability.

All source-audit notes, proof records, deterministic Python code, tests, generated tables, checksums, TikZ figure sources, bibliography, and manuscript source are included in the directory. No external dataset or Riemann-zero dataset was created or analyzed.

#### Ethics statement.

This theoretical and computational study involves no human participants, animals, intervention, personal data, or identifiable information. No institutional ethics review was required.

#### CRediT authorship contribution statement.

Liang Wang: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Data curation, Visualization, Writing---original draft, and Writing---review and editing.

#### Funding.

No project-specific external funding source was declared for this work.

#### Conflict of interest.

The author declares no financial or non-financial conflict of interest relevant to this study.

#### AI-assistance disclosure.

OpenAI Codex assisted with source triage, deterministic implementation, source-to-claim auditing, adversarial proof checking, figure preparation, and manuscript drafting. No generative system is credited as an author. The named author is responsible for source verification, mathematical claims, artifact release, and the final text.

# Finite-polynomial control

The implementation represents $f(T)=\sum_jc_jT^j\in\mathbb{F}_2[T]$ by the integer whose $j$-th bit is $c_j$. Addition and subtraction are bitwise exclusive-or. Multiplication is the shift-and-exclusive-or algorithm, followed by polynomial long division when a modulus is present. For a monic polynomial of degree $d$, the Frobenius--Rabin criterion used in the control suite is $$T^{2^d}\equiv T\pmod f,
  \qquad
  \gcd\!\left(f,T^{2^{d/q}}-T\right)=1
  \quad\text{for every prime }q\mid d.$$ This supplies an independent constructive enumeration of the primitive affine closed points. The code also compares the count against Equation [\[eq:closed-count\]](#eq:closed-count){reference-type="eqref" reference="eq:closed-count"}; agreement is required at every degree, so a bug in either enumeration or number-theoretic counting is exposed rather than averaged away.

The formal product is multiplied coefficientwise through order 12. For $(1-z^d)^{-a_d}$, the coefficient of $z^{rd}$ is $\binom{a_d+r-1}{r}$. Truncated polynomial multiplication then gives the orbit-product series. The independent rational-function coefficient is $2^{n+1}-1$ at order $n$. The proof in Theorem [\[thm:zeta\]](#thm:zeta){reference-type="ref" reference="thm:zeta"} remains logically prior to this finite comparison.

# Claim-to-evidence ledger

\@L0.38L0.18L0.36@

\
Claim & Evidence & Basis\
Claim & Evidence & Basis\
closed points are Frobenius cycles & [PROVED]{.sans-serif}& primary source plus Lemma [\[lem:cycle\]](#lem:cycle){reference-type="ref" reference="lem:cycle"}\
cycle size equals residue degree & [PROVED]{.sans-serif}& Lemma [\[lem:cycle\]](#lem:cycle){reference-type="ref" reference="lem:cycle"}\
suspension component is a circle of length $d\log2$ & [PROVED]{.sans-serif}& Theorem [\[thm:dictionary\]](#thm:dictionary){reference-type="ref" reference="thm:dictionary"}\
quotient is LCH, Hausdorff, and second countable & [PROVED]{.sans-serif} after [MODELING CHOICE]{.sans-serif}& direct topology proof\
orbit, Artin--Mazur, and Hasse--Weil zetas agree & [PROVED]{.sans-serif}& Theorem [\[thm:zeta\]](#thm:zeta){reference-type="ref" reference="thm:zeta"}\
$1/r$ and $\log N(x)$ are endogenous & [PROVED]{.sans-serif}& Corollary [\[cor:weights\]](#cor:weights){reference-type="ref" reference="cor:weights"}\
absolute convergence is exactly $\Re s>1$ & [PROVED]{.sans-serif}& Theorem [\[thm:convergence\]](#thm:convergence){reference-type="ref" reference="thm:convergence"}\
one fixed finite-field clock covers all rational primes & [REFUTED]{.sans-serif}& Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}\
disjoint circles compile any locally finite length product & [PROVED]{.sans-serif}& Theorem [\[thm:compiler\]](#thm:compiler){reference-type="ref" reference="thm:compiler"}\
circle flow is operator-equivalent to $\ell$-adic cohomology & [NOT TESTABLE]{.sans-serif}& no operator map or trace theorem\
construction supplies a Riemann gamma factor or half-weight & [REFUTED]{.sans-serif} for frozen object & absent from source lock\
natural quantum lift exists & [NOT TESTABLE]{.sans-serif}& no Hilbert space, operator, or domain defined\

# Artifact map

\@L0.39L0.53@ Relative path & Purpose\
Relative path & Purpose\
& frozen question, obligations, evidence vocabulary, and controls\
& verified primary-source corpus and claim boundaries\
& immutable object, clock, topology, zeta convention, and target split\
& theorem proofs, adversarial controls, and dual Route-A verdict\
& source-to-claim map and manuscript architecture\
& deterministic polynomial, zeta, clock, and compiler controls\
& 13 regression tests\
& one-command reproduction entry point\
& degree counts, fixed-point reconstruction, and periods\
& finite formal-series identity\
& primitive-versus-repeated contribution ledger\
& finite convergence regressions\
& software check of the single imaginary clock\
& generated finite instances of the one-clock theorem\
& unrelated target-encoding controls\
& parameters, interpretation boundary, verdicts, and SHA-256 hashes\
& source-native TikZ diagrams\
