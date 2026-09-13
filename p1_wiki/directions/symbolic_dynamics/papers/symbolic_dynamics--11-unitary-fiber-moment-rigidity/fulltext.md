---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--11-unitary-fiber-moment-rigidity"
canonical_tex: "symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity/main.tex"
canonical_pdf: "symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity/main.pdf"
source_sha256: "873f4102a92a30286cb1adf9b25bd3d54763517ea56b0d3dac1b2febb4d43d9f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite Positive Unitary-Fiber Rigidity for Tensor-Prime Symbolic Zeta Functions: Exact Repetition Ledgers versus Bloch Motion

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/11-unitary-fiber-moment-rigidity/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test whether a finite unitary, or Bloch, fiber can add determinant-visible phase motion to tensor-prime symbolic loops without changing their Euler repetition ledger. For a fiber $U_p\in U(d)$ over the atom of entropy $\log p$, the $r$th repeated loop is weighted by the positive normalized trace $\tau_d(U_p^r)$. The resulting block-diagonal transfer has an exact analytic tracial determinant on $\operatorname{Re}s>1$. Its apparent freedom is rigid: $\tau_d(U)=1$ already implies $U=I_d$, and ordinary-trace equality for the first $d$ moments forces $d=1$ and $U=1$. We also prove that a finite positive fiber cannot erase every repetition of an isolated mixed primitive cycle. A directed triangle with holonomy $W$ leaves a mixed monomial at some repetition no later than the number of distinct eigenvalues of $W$. Root-of-unity fibers attain this delay but do not remove the defect. A matched graded sector preserves all supertraces only because its moving part cancels from the superdeterminant. Nine finite-control tests verify the formulas; all 96 prime, 96 composite, and 96 random-clock Bloch trials move, so phase motion alone proves too much. The outcome is a finite-positive moment-rigidity theorem and a scoped stop for the proposed Bloch escape, not a completed zeta divisor or spectral realization.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Finite Positive Unitary-Fiber Rigidity for Tensor-Prime Symbolic Zeta Functions:\
  Exact Repetition Ledgers versus Bloch Motion
```

## Markdown 正文

# Introduction {#sec:introduction}

A unitary fiber is an attractive way to add phase without changing a symbolic alphabet. In a periodic-orbit determinant, however, a holonomy is not used once. The $r$th traversal sees its $r$th power. For a tensor-prime atom $F_p$ with entropy $h(F_p)=\log p$, a finite fiber therefore changes the loop coefficient from $p^{-rs}$ to $$p^{-rs}\tau_d(U_p^r),\qquad
 \tau_d=\frac1d\operatorname{Tr}.                                      \tag{1.1}$$ The question is exact and unforgiving: can $U_p$ vary nontrivially while $\tau_d(U_p^r)=1$ for every $p$ and every repetition $r$?

SD-C13 answers no for every finite faithful positive fiber. The obstruction appears before asymptotics, analytic continuation, or zero comparison. The first normalized moment alone gives $$\tau_d\bigl((I-U)^*(I-U)\bigr)
 =2-\tau_d(U)-\tau_d(U^*) .                              \tag{1.2}$$ If the target first-loop coefficient is retained, the right side vanishes; faithfulness forces $U=I$. The ordinary Fredholm determinant is even less permissive. Its coefficients are $\operatorname{Tr}(U^r)$, and matching one copy of the Euler factor through the first $d$ repetitions forces a one-dimensional trivial fiber.

One might try to move the phase from isolated atom loops into recurrent symbolic paths. That branch fails differently. A mixed primitive cycle with monomial $M$ and holonomy $W$ contributes $$\sum_{k\ge1}\frac{M^k}{k}\tau_d(W^k)                  \tag{1.3}$$ up to the determinant sign convention. A finite positive spectral measure cannot have all of its positive moments zero. Hence some repeated mixed cycle survives. Uniform roots of unity can delay visibility to a prescribed finite order, but the first surviving order then carries the full mixed monomial. Parallel paths have the same problem: cancellation at one order returns at another, and independent path variables prevent even accidental coefficient collisions.

The paper makes four falsifiable claims.

1.  The frozen block transfer belongs to the tracial Schatten class $L^q$ exactly when $q\operatorname{Re}s>1$, and its trace-log defines an exact twisted determinant in the honest Euler half-plane.

2.  Exact normalized positive moments force $U_p=I_d$ atom by atom; exact ordinary moments force $d=1$ as well.

3.  Every finite positive triangle or finite positive family of parallel primitive paths exposes a mixed repetition at finite order.

4.  Nonfaithful and graded controls evade the algebraic conclusion only by hiding or cancelling the moving sector from the determinant that owns the target ledger.

Finite computations are used only as exact-formula and adversarial controls. The cyclic-fiber identities are reproduced to machine precision, and all nine frozen tests pass. Bloch determinant motion also appears in every one of 288 matched-clock trials: 96 tensor-prime, 96 composite, and 96 random increasing inventories. This uniformity is negative evidence. Motion comes from the finite fiber topology, not from the arithmetic inventory.

The result is scoped. It does not exclude infinite diffuse tracial fibers, arbitrary virtual representations, or a different symbolic determinant. Nor does it provide continuation, a functional equation, a completed divisor, or a fixed self-adjoint operator. It establishes the exact boundary for one natural attempt: finite positive Bloch phase cannot remain visible while every prime repetition coefficient stays unchanged.

# Twisted symbolic zeta functions and the claim boundary {#sec:related}

The use of unitary representations in periodic-orbit functions is classical. @adachisunada1987 developed twisted Perron--Frobenius operators and $L$-functions for topological graphs. In the symbolic setting, @parrypollicott1990 [Chapter 8] start from a subshift of finite type, a compact group in $U(d)$, and a finite-dimensional unitary representation; the representation character weights periodic holonomy, and the trivial one-dimensional character recovers the untwisted zeta. Repetition therefore produces $\operatorname{Tr}(U_\gamma^r)$ in the established formalism. SD-C13 does not claim a new twisted transfer operator or character-weighted orbit product.

The untwisted finite-state determinant baseline goes back to @bowenlanford1970. Multivariable edge and path zeta functions provide a particularly useful audit device: independent variables separate closed paths before any numerical specialization [@starkterras1996]. We use that principle for the triangle and parallel-path obstruction. It prevents two different primitive cycles from appearing to cancel merely because their weights were prematurely set equal.

Group extensions also warn against reading too much from a twisted zeta. @boyleschmieding2017 exhibit substantial periodic-data and classification subtleties for finite group extensions of shifts of finite type, including nonconjugate extensions with the same zeta data. @ward1999 shows that isometric extensions of full shifts can change dynamical zeta functions sharply and can produce nonalgebraic behavior. These works support neither an exact tensor-prime ledger nor an arithmetic divisor conclusion; they establish that nontrivial fibers naturally alter periodic data.

Fredholm determinant background is standard [@simon1977]. The project-specific question is narrower than this literature: once a tensor-prime loop has coefficient one at every repetition, can a finite-dimensional positive unitary character move without changing that coefficient? The answer follows from elementary faithfulness, Newton, and Vandermonde arguments. We make no priority claim for those tools. The contribution is their source-locked synthesis into a no-go theorem for the SD-C13 ledger.

# SD-C13: source lock and analytic determinant {#sec:source}

Let $\mathcal P$ be the tensor-indecomposable full-shift atoms. Entropy identifies them with primes by $F_p\in\mathcal P$ and $$h(F_p)=\log p.                                             \tag{3.1}$$ Each atom has one primitive loop $\gamma_p$; the $r$th traversal is $\gamma_p^r$ and has roof $r\log p$. This grammar and clock predate the fiber and are not fitted to a target zero list.

Fix $d<\infty$. For a Bloch parameter $\theta$, attach $U_p(\theta)\in U(d)$ with $U_p(0)=I_d$. On $$\mathcal H=\ell^2(\mathcal P)\otimes\mathbb C^d$$ define the diagonal symbolic transfer $$T_s(\theta)=\bigoplus_{p}p^{-s}U_p(\theta).                \tag{3.2}$$ The relevant algebra is the block diagonal direct sum with faithful semifinite trace $$\Phi(A)=\sum_p\tau_d(A_p),\qquad \tau_d=\frac1d\operatorname{Tr}.        \tag{3.3}$$ The ordinary Hilbert-space trace is retained as a distinct control.

[\[prop:ideals\]]{#prop:ideals label="prop:ideals"} Put $\sigma=\operatorname{Re}s>0$. The transfer $T_s(\theta)$ is bounded and $\Phi$-compact. For $q\ge1$, $$T_s(\theta)\in L^q(\Phi)
 \quad\Longleftrightarrow\quad q\sigma>1.                  \tag{3.4}$$ For every integer $r\ge1$ in its trace domain, $$\Phi(T_s(\theta)^r)
 =\sum_pp^{-rs}\tau_d(U_p(\theta)^r).                       \tag{3.5}$$

Unitarity gives $|T_s|=\bigoplus_pp^{-\sigma}I_d$ in the tracial algebra. Thus its $L^q(\Phi)$ norm to the $q$th power is $\sum_pp^{-q\sigma}$, which converges exactly when $q\sigma>1$. The block norms tend to zero for $\sigma>0$, so finite atom cutoffs prove compactness. Taking powers blockwise gives [\[prop:ideals\]](#prop:ideals){reference-type="ref" reference="prop:ideals"}.

For $\sigma>1$ and $|z|2^{-\sigma}<1$, define the normalized analytic trace-series determinant by $$\begin{aligned}
 D_\tau(s,z;\theta)
 &:=\exp\left[-\sum_{r\ge1}\frac{z^r}{r}
          \Phi(T_s(\theta)^r)\right]                         \tag{3.6}\label{eq:dtau}\\
 &=\exp\left[-\sum_p\sum_{r\ge1}
       \frac{z^rp^{-rs}}r\tau_d(U_p(\theta)^r)\right].       \tag{3.7}\end{aligned}$$ Absolute local convergence follows from $|\tau_d(U^r)|\le1$. At a finite atom cutoff it is the branch at $z=0$ of $$\prod_p\det(I_d-zp^{-s}U_p(\theta))^{1/d}.                 \tag{3.8}$$ Equation [\[eq:dtau\]](#eq:dtau){reference-type="eqref" reference="eq:dtau"}, rather than an unqualified fractional product, is the determinant convention. At the trivial fiber, $$D_\tau(s,z;0)=\prod_p(1-zp^{-s}),                           \tag{3.9}$$ so $D_\tau(s,1;0)=\zeta(s)^{-1}$ in the honest Euler half-plane.

The ordinary Fredholm determinant is another object: $$D_{\rm ord}(s,z;\theta)
 =\det_{\!F}(I-zT_s(\theta))
 =\prod_p\det(I_d-zp^{-s}U_p(\theta)).                      \tag{3.10}$$ It exists for $\sigma>1$, but its repetition coefficient is $\operatorname{Tr}(U_p^r)$, not $\tau_d(U_p^r)$. Coordinatewise mixing of [\[eq:dtau\]](#eq:dtau){reference-type="ref" reference="eq:dtau"} and [\[eq:dtau\]](#eq:dtau){reference-type="eqref" reference="eq:dtau"}--[\[eq:dtau\]](#eq:dtau){reference-type="eqref" reference="eq:dtau"} with the ordinary determinant is forbidden; the two rigidity statements below audit them separately.

# Positive moment rigidity {#sec:rigidity}

The intended Bloch escape asks a finite unitary fiber to move while leaving every coefficient of the untwisted Euler ledger unchanged. In the positive tracial convention this demand is already rigid at the first repetition.

[\[thm:positive-rigidity\]]{#thm:positive-rigidity label="thm:positive-rigidity"} Let $U\in U(d)$ and let $\tau_d=d^{-1}\operatorname{Tr}$. If $\tau_d(U)=1$, then $U=I_d$. Consequently $$\tau_d(U^r)=1\quad(r\geq1)
 \qquad\Longleftrightarrow\qquad U=I_d .                 \tag{4.1}$$ For a general positive state $\phi$, the equality $\phi(U)=1$ forces only the $\phi$-visible spectral measure to equal $\delta_1$; faithfulness again forces $U=I$.

Positivity and traciality give $$\tau_d((I-U)^*(I-U))=2-\tau_d(U)-\tau_d(U^*)=0.$$ Faithfulness implies $I-U=0$. In a general GNS representation the same identity gives $(\pi_\phi(U)-I)\xi_\phi=0$, which is precisely the stated visible-measure conclusion.

The ordinary determinant convention is even more restrictive.

[\[thm:ordinary-rigidity\]]{#thm:ordinary-rigidity label="thm:ordinary-rigidity"} If $U\in U(d)$ and $\operatorname{Tr}(U^r)=1$ for $1\leq r\leq d$, then $d=1$ and $U=1$.

Newton's identities applied to the first $d$ power sums yield $e_1=1$ and $e_k=0$ for $2\leq k\leq d$. If $d\geq2$, then $\det U=e_d=0$, contradicting unitarity. Thus $d=1$, and the first moment fixes the sole eigenvalue.

These theorems separate two legitimate branches. The trivial fiber retains the exact tensor-prime determinant but supplies no new phase. Every state-visible nontrivial Bloch fiber changes at least one repetition coefficient and therefore fails A1 for the promoted object.

There are two apparent escapes, neither determinant-visible. A nonfaithful state can ignore a summand containing arbitrary $V\in U(k)$, but the ordinary determinant still sees $\det(I-zV)$. Alternatively take even fiber $1\oplus V$ and odd fiber $V$. Then for every $r$, $$\operatorname{Str}(U^r)=1,
 \qquad
 \operatorname{Ber}(I-zU)=\frac{(1-z)\det(I-zV)}{\det(I-zV)}=1-z.       \tag{4.2}$$ The moving sector cancels exactly from the promoted invariant.

# Recurrent Bloch flux leaves a mixed repetition {#sec:mixed}

A genuine Bloch flux requires at least one recurrent cross-atom circuit or two inequivalent return paths. Independent edge variables make the resulting ledger defect visible before specializing $x_p=p^{-s}$.

[\[thm:mixed-visibility\]]{#thm:mixed-visibility label="thm:mixed-visibility"} Let a recurrent primitive path have independent monomial $M$ and unitary holonomy $W\in U(d)$. With normalized positive trace, some $1\leq k\leq d$ satisfies $\tau_d(W^k)\ne0$. Hence the mixed term $M^k\tau_d(W^k)$ survives at a finite repetition. The same conclusion holds for any finite positive family of parallel primitive returns.

Write the distinct eigenvalues of $W$ as $\lambda_j$ with positive normalized multiplicities $w_j$. If the first $m$ moments vanished, where $m$ is the number of distinct eigenvalues, then $\sum_j w_j\lambda_j^k=0$ for $1\leq k\leq m$. The corresponding Vandermonde matrix is invertible, so every $w_j$ would vanish, a contradiction. Summing finitely many positive spectral measures proves the parallel-path statement.

For a directed triangle with monomial $M=xyz$, the three cyclic starting points give coefficient $$3M^k\tau_d(W^k)                                           \tag{5.1}$$ in the $3k$th trace. An $m$-cycle permutation fiber illustrates the sharp failure mode: $$\tau(P_m^r)=\begin{cases}1,&m\mid r,\\0,&m\nmid r.
 \end{cases}                                                \tag{5.2}\label{eq:cycle-moment}$$ It can postpone a defect, never remove it. In the frozen experiment the first triangle leak occurs at transfer powers $3m=6,9,\ldots,24$ for $m=2,\ldots,8$.

Two paths with phases $+1$ and $-1$ do not cancel coefficientwise either: with independent monomials $a,b$ their $r$th repeated contribution is $$a^r+(-1)^rb^r.                                             \tag{5.3}$$ Specializing edge variables too early can disguise this failure; unique factorization restores it once atom weights are inserted. Thus finite positive fibers face a strict alternative: without recurrent cross paths, [\[thm:positive-rigidity\]](#thm:positive-rigidity){reference-type="ref" reference="thm:positive-rigidity"} trivializes visible phase; with such paths, [\[thm:mixed-visibility\]](#thm:mixed-visibility){reference-type="ref" reference="thm:mixed-visibility"} corrupts the primitive ledger.

# Exact controls and claim boundaries {#sec:controls}

The executable audits repetitions through $r=32$. Scalar phases reproduce $e^{ir\theta}$, conjugate Bloch pairs reproduce $\cos(r\theta)$, and cycle permutations of orders $2$ through $8$ satisfy [\[eq:cycle-moment\]](#eq:cycle-moment){reference-type="eqref" reference="eq:cycle-moment"} with zero symbolic residual. The faithful-state identity and ordinary Newton reconstruction are checked in dimensions up to eight.

The hidden-sector control preserves state moments but changes the ordinary determinant by as much as $0.088829$ on the frozen grid. The graded matched sector has exact supertrace ledger and Berezinian residual at most $2.22\times10^{-16}$, but its moving spectrum cancels from the invariant. Triangle and parallel-return expansions certify the finite mixed leaks described in [5](#sec:mixed){reference-type="ref" reference="sec:mixed"}.

Arithmetic selectivity fails decisively. For each of prime, composite, and matched random increasing clocks, all $96/96$ nontrivial Bloch controls show determinant motion and all fail the exact ledger by repetition $r=d$. Block sizes two, three, and four behave alike. This is a `PROVES_TOO_MUCH` result: finite Bloch response is a fiber property, not a rational-prime discriminator.

The theorem is deliberately finite-fiber and positive. It does not exclude diffuse infinite-dimensional traces, rank-dependent virtual coefficients, or another determinant convention. It does exclude promoting a finite unitary character family to the unchanged Riemann Euler product. No target zeros, crossing census, fitted phase, or cross-family repair appears in the protocol.

# Route-A outcome and Route-B lock {#sec:route}

The source remains arithmetic: tensor indecomposability gives $F_p$ and entropy gives $\log p$. The promoted nontrivial-Bloch object nevertheless fails its primitive ledger. Its conservative tuple is $$\begin{gathered}
 (\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\texttt{A1\_FAIL},\\
 \texttt{A2\_ANALYTIC\_DETERMINANT},\texttt{A3\_FAIL},
 \texttt{A4\_FAIL}).
\end{gathered}                                               \tag{7.1}$$ Here A2 certifies the exact twisted determinant in its honest half-plane; it does not certify the target Euler determinant for nontrivial holonomy. The overall verdict is $$\boxed{\texttt{ROUTE\_A\_REJECTED}}                         \tag{7.2}$$ with stage labels $$\texttt{GO\_POSITIVE\_MOMENT\_RIGIDITY}/
 \texttt{STOP\_BLOCH\_ESCAPE}/
 \texttt{STOP\_SCOPED}/\texttt{PROVES\_TOO\_MUCH}.          \tag{7.3}$$

There is no fixed self-adjoint generator, compact-resolvent theorem, completed functional equation, Gamma mechanism, Weil compression, or target counting law. Hence $$\mathtt{route\_b\_invocation\_allowed=false}.              \tag{7.4}$$

# Conclusion

SD-C13 closes the finite positive Bloch branch. Exact prime repetition moments force each visible unitary fiber to be trivial; ordinary determinant exactness even forces a one-dimensional fiber. Recurrent finite flux cannot evade the result because some mixed repetition survives, while graded or nonfaithful escapes merely hide their motion from the promoted determinant.

The negative result is useful: it identifies diffuseness as the next minimal same-family loophole. An infinite tracial unitary can have all nonzero moments zero, so an added diffuse sector might coexist with the base Euler ledger. The next paper tests whether that sector becomes analytically visible or whether moment cancellation makes it another determinant-invisible ghost.

# Proof scope and reproducibility

All algebraic claims use finite unitary matrices, positive normalized trace, and independent formal variables for recurrent paths. Numerical controls only verify frozen finite instances and are not used to infer the all-order theorems. The code generates its arithmetic inventories internally, reads no Riemann-zero data, and performs no parameter fitting. The exact theorem does not cover infinite diffuse traces or indefinite functionals; these are explicitly separated rather than silently imported into SD-C13.
