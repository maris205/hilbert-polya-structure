---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-magnetic-grushin-cylinder-route-a"
canonical_tex: "henon_dynamics/henon_magnetic_grushin_cylinder_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_magnetic_grushin_cylinder_route_a/paper/main.pdf"
source_sha256: "11cc9e96c52462e2a6a8cb057d30d7b458fc67b6e476aab32a89e55d40464e18"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Flux-Driven Compact-to-Continuous Transition for a Magnetic Grushin Cylinder

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_magnetic_grushin_cylinder_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_magnetic_grushin_cylinder_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_magnetic_grushin_cylinder_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_magnetic_grushin_cylinder_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a complete channel-level spectral atlas for the magnetic Baouendi--Grushin form on $\mathbb R\times S^1$. =0 The closed nonnegative form defines its Friedrichs realization, and Fourier--Hermite reduction gives every nonresonant level $(2n+1)|k+\alpha|$. \>0 Noninteger flux has compact resolvent. At integer flux exactly one angular channel becomes the free line Laplacian: its absolutely continuous spectrum coexists with embedded positive-integer oscillator eigenvalues, while the singular-continuous part is empty. \>1 We derive heat traces, exact odd-divisor multiplicities, a source-local spectral zeta factorization, and the two-term logarithmic Weyl law, with explicit flux and scope boundaries.
author:
- 'Route-A source-local certificate HCS-C293'
date: 2 September 2026
title: |
  A Flux-Driven Compact-to-Continuous Transition\
  for a Magnetic Grushin Cylinder
```

## Markdown 正文

trailerid \[\<C2932026090200000000000000000000\>\<C2932026090200000000000000000000\>\]

# Friedrichs realization and conventions

Use $L^2(\mathbb R\times S^1,\mathrm dx\mathrm d\theta/(2\pi))$ and write $D_\theta=-i\partial_\theta$. For $\alpha\in\mathbb R$, begin with $$\label{eq:form}
 q_\alpha[u]=\int_{\mathbb R\times S^1}
 \bigl(|\partial_xu|^2+x^2|(D_\theta+\alpha)u|^2\bigr)
 \frac{\mathrm dx\mathrm d\theta}{2\pi}.$$ The form domain is the completion of compactly supported smooth functions in $\lVert u\rVert_2^2+q_\alpha[u]$. Since [\[eq:form\]](#eq:form){reference-type="eqref" reference="eq:form"} is densely defined, nonnegative, and closable, its closure determines a unique nonnegative self-adjoint operator by the representation theorem. We call it $\mathsf G_\alpha$. Formally, $$\mathsf G_\alpha=-\partial_x^2+x^2(D_\theta+\alpha)^2.$$ This is a Friedrichs-form statement. We do not assert essential self-adjointness of a smaller differential core.

Boscain, Prandi, and Seri study spectral and magnetic effects on related almost-Riemannian Grushin manifolds [@BPS2016]; their geometric Laplace--Beltrami realization is not silently identified with the present Lebesgue-space form. Harakeh and Hillairet analyze Fourier-separated Baouendi--Grushin cylinder sectors and compact-resolvent mechanisms [@HH2023]. Our theorem is a self-contained source-model closure, not a claim that these classical mechanisms are newly discovered.

# Fourier--Hermite reduction

The unitary angular Fourier expansion $u(x,\theta)=\sum_{k\in\mathbb Z}u_k(x)e^{ik\theta}$ gives $$\label{eq:sum}
 \mathsf G_\alpha\cong\bigoplus_{k\in\mathbb Z}h_{k+\alpha},
 \qquad h_\omega=-\frac{\mathrm d^2}{\mathrm dx^2}+\omega^2x^2.$$ For $\omega\ne0$, scaling the Hermite basis yields $$\label{eq:levels}
 \lambda_{k,n}(\alpha)=(2n+1)|k+\alpha|,
 \qquad k\in\mathbb Z,\quad n\in\mathbb N_0.$$ For $\omega=0$, $h_0=-\mathrm d^2/\mathrm dx^2$ is the free line Laplacian.

[\[thm:dichotomy\]]{#thm:dichotomy label="thm:dichotomy"} If $\alpha\notin\mathbb Z$, then $\mathsf G_\alpha$ has compact resolvent and pure point spectrum given by [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"}, with multiplicities obtained by counting equal index pairs.

If $\alpha\in\mathbb Z$, exactly one resonant angular Fourier channel is unitarily equivalent to the free line Laplacian. It contributes absolutely continuous spectrum $[0,\infty)$ of almost-everywhere multiplicity two. The orthogonal nonresonant sector has compact resolvent and point spectrum equal to every positive integer. Those eigenvalues are embedded in the full continuum. The singular-continuous spectrum is empty.

If $\delta=\operatorname{dist}(\alpha,\mathbb Z)>0$, every channel is an oscillator and [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"} is complete. For fixed $L$, the inequality $(2n+1)|k+\alpha|\leq L$ permits only finitely many $k$ and, for each $k$, only finitely many $n$. Thus the eigenvalue list has finite multiplicities and tends to infinity, which is equivalent to compact resolvent.

At integer flux, a gauge shift reduces to $\alpha=0$. The $k=0$ summand in [\[eq:sum\]](#eq:sum){reference-type="eqref" reference="eq:sum"} is the free line Laplacian. Fourier transformation in $x$ shows that its spectrum is purely absolutely continuous on $[0,\infty)$; the two momentum branches $\xi=\pm\sqrt E$ give multiplicity two for almost every $E>0$. Every $k\ne0$ summand is an oscillator, and the same finite-list criterion makes their direct sum compact-resolvent. A direct sum of this pure-point part and the free absolutely continuous part has no singular-continuous component. Formula [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"} becomes $(2n+1)|k|$, so its values are positive integers and lie inside the free continuum. This proves coexistence, rather than incorrectly replacing the full integer-flux spectrum by either component alone.

Flux shifts $\alpha\mapsto\alpha+j$, $j\in\mathbb Z$, merely relabel $k$. Complex conjugation and $k\mapsto-k$ give reflection $\alpha\mapsto-\alpha$. Hence the spectral fundamental interval is $0\leq\delta\leq1/2$.

\>0

# Multiplicity and flux boundaries

At zero flux, a positive integer $N$ occurs when $N=(2n+1)|k|$. Let $d_{\rm odd}(N)$ count the positive odd divisors of $N$.

[\[prop:mult\]]{#prop:mult label="prop:mult"} On the zero-flux nonresonant sector, $$\label{eq:mult}
 \operatorname{mult}(N)=2d_{\rm odd}(N),\qquad N\geq1.$$

Choosing an odd divisor $j=2n+1$ fixes $|k|=N/j$. The two signs of $k$ give two orthogonal angular modes, and every index pair arises uniquely in this way.

If $\alpha$ is irrational, equality between two values $(2n+1)|k+\alpha|$ forces the two odd factors and signed channels to agree; otherwise it would make a nonzero integer multiple of $\alpha$ integral. Thus all off-integer-flux eigenvalues are simple for irrational flux. At rational flux the same equality is a finite Diophantine condition and may produce coincidences. Half flux has the systematic pairing $k\leftrightarrow-k-1$, so every level is at least double.

As $\alpha$ approaches an integer, the nearest-channel frequency $\delta=\operatorname{dist}(\alpha,\mathbb Z)$ tends to zero. Its levels $(2n+1)\delta$ collapse, compactness is lost in the limit, and the channel becomes the free Laplacian. This singular transition is not uniform in heat trace or resolvent norm.

# Heat traces

For $t>0$ and $\omega>0$, the oscillator trace is the geometric sum $$\label{eq:channelheat}
 \sum_{n\geq0}e^{-t(2n+1)\omega}
 =\frac1{2\sinh(t\omega)}.$$ Positive-term summation is legitimate throughout.

[\[thm:heat\]]{#thm:heat label="thm:heat"} For $\alpha\notin\mathbb Z$, $$\label{eq:heat}
 \operatorname{Tr}e^{-t\mathsf G_\alpha}
 =\sum_{k\in\mathbb Z}\frac1{2\sinh(t|k+\alpha|)}<\infty.$$ At integer flux the full heat operator is not trace class. On the orthogonal complement of the resonant channel, $$\label{eq:iheat}
 \operatorname{Tr}_{\perp}e^{-t\mathsf G_0}
 =\sum_{m\geq1}\frac1{\sinh(tm)}<\infty.$$ Moreover, as $\delta\downarrow0$, the closest-channel contribution is $(2\sinh(t\delta))^{-1}\sim(2t\delta)^{-1}$.

Sum [\[eq:channelheat\]](#eq:channelheat){reference-type="eqref" reference="eq:channelheat"} over all Fourier channels. Away from integer flux, $|k+\alpha|$ grows linearly in $|k|$, so the outer sum converges. At zero flux, remove $k=0$ and pair $k=\pm m$ to obtain [\[eq:iheat\]](#eq:iheat){reference-type="eqref" reference="eq:iheat"}. The final asymptotic follows from $\sinh z\sim z$.

\>1

# Source-local zeta series and logarithmic Weyl law

Only the compact nonresonant sector at zero flux enters this section. For $\Re s>1$, absolute convergence and [\[eq:levels\]](#eq:levels){reference-type="eqref" reference="eq:levels"} give $$\begin{aligned}
 Z_\perp(s)
 &=\sum_{k\ne0}\sum_{n\geq0}
   \bigl((2n+1)|k|\bigr)^{-s}\notag\\
 &=2\left(\sum_{m\geq1}m^{-s}\right)
   \left(\sum_{n\geq0}(2n+1)^{-s}\right)\notag\\
 &=2(1-2^{-s})\zeta(s)^2.\label{eq:zeta}\end{aligned}$$ This is a source-operator identity obtained from two separated indices.

Let $N_\perp(L)=\#\{\lambda\leq L\}$ count multiplicity.

[\[thm:weyl\]]{#thm:weyl label="thm:weyl"} For $L\geq1$, $$\label{eq:count}
 N_\perp(L)=2\sum_{\substack{j\leq L\\j\equiv1\pmod 2}}
 \left\lfloor\frac Lj\right\rfloor
 =2\sum_{r\leq L}d_{\rm odd}(r).$$ As $L\to\infty$, $$\label{eq:weyl}
 N_\perp(L)=L\log L+(2\gamma+\log2-1)L+O(\sqrt L).$$

Counting pairs $(j,m)$ with $j=2n+1$ odd and $jm\leq L$ gives the first formula; collecting products gives the second. The coefficient identity $d_{\rm odd}(r)=d(r)-\mathbf 1_{2\mid r}d(r/2)$ follows either by divisors or by removing the factor $2^{-s}$ in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. Apply the elementary hyperbola estimate $$\sum_{r\leq x}d(r)=x\log x+(2\gamma-1)x+O(\sqrt x)$$ at $x=L$ and $x=L/2$, subtract, and multiply by two. This yields exactly the constant in [\[eq:weyl\]](#eq:weyl){reference-type="eqref" reference="eq:weyl"}.

# Evidence, Route-A verdict, and disclosures

The receipt audits 165 rational channel levels, nine noninteger heat traces, three integer-flux nonresonant heat traces, 96 embedded multiplicities, six exact counts, four zeta values, and ten flux-symmetry cells. The independent checker sums individual Fourier--Hermite levels rather than copying the producer's hyperbolic-sine trace formula and reports 2,053 assertions. SymPy checks 750 identities, two isolated evidence replays are byte identical, and 75/75 hostile mutations are rejected: 54 evidence-JSON and 21 evaluation-YAML attacks, including a duplicate-key-rejecting evaluation YAML semantic lock and a repaired attempt to change the free line's absolutely continuous multiplicity from two to one. Finite cells audit indexing and constants; the proofs carry the all-flux operator statements.

The strict Route-A tuple is $$\begin{gathered}
 \texttt{(A0\_WEAK\_ARITHMETIC\_RELATION,A1\_FAIL,A2\_FAIL,}\\
 \texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE,}
 \texttt{A4\_NATURAL\_QUANTIZATION)}.
 \end{gathered}$$ The overall verdict remains `ROUTE_A_REJECTED`, and Route B is disabled. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the source-local odd-divisor multiplicity and [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} are explicitly not target arithmetic local data, target Euler factors, a target divisor or counting law, a target functional equation, a target zero correspondence, or a Hilbert--Pólya operator. No such interpretation is licensed.

All evidence, code, and deterministic build instructions are included. There are no personal data or human or animal subjects, so ethics approval is not applicable. The author reports no conflict of interest and no external funding. CRediT roles are conceptualization, formal analysis, software, validation, writing, and reproducibility curation. AI assistance was used in drafting and code generation; the final claims were checked against the proofs, exact schemas, independent calculations, and hostile tests recorded in the package.

2 U. Boscain, D. Prandi, and M. Seri, "Spectral analysis and the Aharonov--Bohm effect on certain almost-Riemannian manifolds," *Commun. Partial Differential Equations* 41 (2016), 32--50, [arXiv:1406.6578](https://arxiv.org/abs/1406.6578). M. Harakeh and L. Hillairet, "A spectral condition for the control of eigenfunctions of Baouendi--Grushin type operators," [arXiv:2312.04359](https://arxiv.org/abs/2312.04359) (2023).
