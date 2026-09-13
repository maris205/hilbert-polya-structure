---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--01-falsification-first-audit"
canonical_tex: "symbolic_dynamics/papers/01-falsification-first-audit/main.tex"
canonical_pdf: "symbolic_dynamics/papers/01-falsification-first-audit/main.pdf"
source_sha256: "592caadddf5e2a6b0b9cf73835260d0d5170b1ebcb043e9233ac322b66196553"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Falsification-First Symbolic Dynamics for Arithmetic Determinants: Six Audits and Seven Scoped Obstructions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We audit six source-locked symbolic-dynamics constructions as possible arithmetic determinants. The audit requires one object to supply five successive obligations: endogenous rational-prime arithmetic, a complete primitive-orbit and repetition ledger, a natural determinant, the required global analytic divisor, and a same-clock operator lift. We prove seven scoped obstructions. They include an $O(R)$ disk-divisor bound for every nonzero determinant built from a finite graph, positive finite-range roofs, finite-range weights, and a fixed finite-dimensional cocycle; periodic-point collapse for a squarefree admissible shift; inverse-design and mixed-orbit obstructions for shared-base renewal codes; a unary language obstruction; and acyclicity of an endogenous wheel-sieve prime recursion. Reproducible finite audits enumerate $63{,}319$ primitive Gauss necklaces, certify a $98{,}460$-vertex wheel directed acyclic graph, and evaluate $2^{22}$ states of a Knauf arithmetic recursion. These computations validate finite ledgers and expose controls; they do not establish analytic continuation. No frozen candidate passes all five obligations, and the subsequent operator route remains locked for every candidate. The conclusion is bounded: it rules out the six objects and the stated theorem classes, not symbolic dynamics as a whole.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 12, 2026'
title: |
  **Falsification-First Symbolic Dynamics for Arithmetic Determinants:**\
  Six Audits and Seven Scoped Obstructions
```

## Markdown 正文

# Introduction {#sec:introduction}

Dynamical zeta functions translate periodic data into analytic objects. For a map $T$, the Artin--Mazur series packages the fixed-point counts $\#\operatorname{Fix}(T^n)$ [@artin1965periodic]; for hyperbolic and expanding systems, transfer operators lead to determinant formulas with far richer analytic structure [@ruelle1976zeta]. This formal resemblance makes symbolic dynamics a natural place to look for arithmetic determinants. It also creates a serious identification problem: a determinant can display a chosen divisor because arithmetic data were inserted into its weights, because its grammar is flexible enough to encode almost any holomorphic germ, or because a finite plot hides missing repetitions and extra zeros.

An arithmetic-dynamical proposal therefore needs more than spectral resemblance. Its rational primes, clock, primitive objects, repetitions, operator, and analytic continuation must belong to one fixed construction. The phrase *one fixed construction* is essential. A prime generator in one system cannot certify the determinant of another, and a natural determinant cannot borrow a sign or a Hamiltonian from an unrelated carrier. We call this the same-object rule.

The analytic target is fixed throughout. We use the completed Riemann function $$\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),$$ and ask whether a declared dynamical determinant can satisfy $$\label{eq:target-divisor}
  D_{\mathrm{dyn}}(s)=e^{g(s)}\xi(s)$$ with $g$ entire. Equivalently, the two functions must have the same divisor: their orders of vanishing at every point agree, while the entire factor $e^g$ contributes no zero or pole. A candidate that is only meromorphic must also account for and remove every pole within its own declared convention.

This paper applies that rule to six frozen symbolic constructions: finite full shifts, a squarefree admissible shift, a weighted renewal shift, the Gauss continued-fraction shift, a wheel-sieve level shift, and Knauf's binary arithmetic recursion. Each object is evaluated through five gates: arithmetic origin (A0), primitive/repetition ledger (A1), determinant (A2), global analytic structure (A3), and same-clock lift (A4). The experiment protocol loads no Riemann-zero table and fits no parameter to target zeros.

![Frozen same-object outcomes, generated directly from the six Route-A YAML records. Supported (S), partial or weak (P), and failed or not-testable (F) cells are properties of a row and cannot be assembled across rows. No row completes A0--A4, and every Route-B flag is locked.](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit/figures/fig1_route_a_matrix.pdf>){#fig:route-a-matrix width="\\textwidth"}

gives the principal result. Several candidates possess real mathematical structure, but their strongest coordinates occur in different rows. The wheel recursion generates successive rational primes and the increments $\log p$ without a prime table, yet its strict level graph has no cycles. The Gauss/Mayer construction has a natural primitive ledger and an infinite-dimensional Fredholm determinant, yet its primitive species consists of periodic continued fractions and hyperbolic modular classes rather than rational primes. Knauf's recursion yields an exact zeta quotient in its proved half-plane, but the computed partition function is not an intrinsic primitive-orbit Fredholm determinant. Joining these facts would violate the same-object rule.

The paper makes four claims.

1.  We give a source-lock and adversarial-control protocol that separates arithmetic origin, orbit bookkeeping, determinant existence, global analysis, and operator realization.

2.  We derive seven scoped obstructions for finite-memory determinants, squarefree periodic points, shared-base renewal codes, unary return languages, finite unitary twists, and the wheel level shift.

3.  We record a candidate-by-candidate negative result: none of the six frozen objects passes A0--A4, so none is eligible for the operator route.

4.  We provide machine-readable evaluations and data-driven figures that distinguish exact identities, exhaustive finite certificates, floating observations, modeling choices, and open statements.

These claims are intentionally narrower than a universal no-go theorem. A countable-state system, an infinite-memory potential, or a genuinely infinite-dimensional operator may escape the finite-memory obstruction. Likewise, the Gauss trace collisions reported below do not exclude every conceivable word-to-prime map, and the wheel acyclicity theorem does not exclude every newly defined factor or recoding. Such an escape must be frozen as a new object and re-enter the audit at A0.

positions the six families. defines the audit gates and evidence labels. states the obstructions, [\[sec:candidates,sec:experiments\]](#sec:candidates,sec:experiments){reference-type="ref" reference="sec:candidates,sec:experiments"} apply them and report the finite audits, and [7](#sec:scope){reference-type="ref" reference="sec:scope"} records the precise boundary of the negative result.

# Context and Related Work {#sec:related}

#### Periodic-point and transfer determinants.

The Artin--Mazur zeta function begins with fixed-point counts and asks when the resulting formal series has analytic meaning [@artin1965periodic]. For finite shifts, the exact adjacency-matrix determinant and periodic-orbit Euler product are classical Bowen--Lanford theory [@bowen1970zeta]. Transfer-operator methods extend this connection beyond finite matrices: Ruelle's framework relates traces, periodic orbits, and zeta functions for expanding maps and Anosov flows [@ruelle1976zeta]. Meromorphic continuation for more general weights can require an infinite-dimensional operator even on a finite alphabet [@pollicott1986meromorphic]. That boundary matters here. Our finite-memory theorem applies only when the graph, memory/range, and cocycle dimension are finite; it is not a theorem that every finite-alphabet determinant has linear divisor growth.

#### Countable shifts and renewal flexibility.

Countable Markov shifts support a thermodynamic formalism with behavior not captured by finite adjacency matrices [@sarig1999thermodynamic]. A shared-base renewal graph gives the elementary determinant $D(z)=1-\sum_{n\ge1}a_nz^n$. This flexibility is useful, but it makes analytic matching non-identifying when the complex coefficients $a_n$ are free. Our renewal results isolate two different issues: coefficientwise inverse design can reproduce arbitrary normalized germs locally, while free concatenation creates mixed primitive necklaces. The point is not that countable shifts are unsuitable. It is that a countable grammar needs an independent arithmetic source and complete orbit bookkeeping before an analytic match becomes evidence.

#### Arithmetic subshifts.

$\mathscr B$-free systems provide a natural symbolic encoding of divisibility constraints and have a substantial dynamical theory [@elabdalaoui2015bfree]. We use the squarefree admissible system as a sharp distinction between arithmetic language complexity and periodic-orbit arithmetic. For the particular two-sided admissibility rule frozen here, a Chinese-remainder argument eliminates every nonzero periodic point. This claim concerns that periodic-point observable; it does not summarize the entropy, spectrum, or aperiodic structure of general $\mathscr B$-free systems.

#### Gauss and modular transfer operators.

Mayer's Gauss-map operator supplies the strongest natural analytic benchmark in the audit. Its holomorphic realization is nuclear in the source domain [@mayer1990gauss], and its signed Fredholm factors connect to the modular Selberg zeta function [@mayer1991selberg]. Periodic digit words determine quadratic irrationals and hyperbolic matrix products, with an intrinsic derivative roof. We retain this theorem as a same-object success at A1--A2. The blocking issue is arithmetic species: neither the grammar nor its primitive classes canonically produces the rational-prime von Mangoldt ledger.

#### Number-theoretical spin chains.

Knauf's binary recursion is a close prior-art collision because its unsigned thermodynamic limit is $\zeta(s-1)/\zeta(s)$ in the proved half-plane [@knauf2013adelic; @knauf1998spin; @knauf1999erratum]. The identity is stronger than a finite zero fit and receives full A0 credit in our analytic-arithmetic sense. Two additional obligations remain separate: the Liouville sign is an arithmetic observable unless derived from an intrinsic cocycle, and a Dirichlet partition function is not automatically a primitive-orbit Fredholm determinant.

#### Low-complexity length selection.

Parikh's theorem makes the length set of a unary context-free language semilinear, hence ultimately periodic in one dimension [@esparza2011parikh]. This yields one of our narrow stop rules: a unary regular or context-free return grammar cannot select exactly the rational primes. Binary encodings and more powerful computation shifts lie outside that statement; they must instead be judged by their description complexity, arithmetic controls, and determinant convention.

Relative to these lines of work, the present contribution is not a new zeta construction. It is an obligation audit that uses established positive theorems where applicable, derives elementary scoped stop rules for the frozen classes, and refuses to transfer a success between objects. No novelty claim is made for an obstruction without a separate precedence audit.

# A Same-Object Audit Protocol {#sec:protocol}

A candidate is a tuple $$\mathcal C=(X,T,\tau,\varphi,\mathcal B,D),$$ where $X$ is the phase space, $T$ the dynamics, $\tau$ the clock or roof, $\varphi$ the potential and cocycle data, $\mathcal B$ the function space, and $D$ the declared determinant convention. The source lock also records parameters, their provenance, numerical cutoffs, precision, allowed data, and forbidden data.

Changing any component that carries a failed obligation creates a new candidate. For example, adding reset edges to an acyclic level shift is not a numerical regularization; it changes $T$ and its periodic orbits. Likewise, assigning $\log p$ to an orbit after looking up $p$ changes the arithmetic source and clock.

#### Five gates.

The route decision is sequential: eligibility at a later gate requires the same row to retain every earlier obligation. The matrix nevertheless records *local structural support* at each gate. Thus an S in A2 means that the object has a valid determinant for its own declared ledger; it does not mean that an object which failed A0 or A1 has passed the Route-A target. Route eligibility is the row-wise conjunction, never a column-wise assembly.

A0: arithmetic origin.

:   Does the frozen rule generate the relevant rational-prime information and logarithmic scale without target-zero fitting or a prime-indexed lookup table? A classical arithmetic grammar may still receive a weak or modeling-choice label when the primes are direct inputs rather than outputs.

A1: primitive/repetition ledger.

:   Are primitive objects, orientations, powers, multiplicities, and completeness intrinsic to the same dynamics? A partition of finite states or a list of return atoms is insufficient unless it gives the declared periodic-orbit expansion.

A2: determinant.

:   Is a dynamical or Fredholm determinant defined on a named function space, with a trace expansion compatible with the A1 ledger? A Dirichlet series or an inverse-designed analytic germ does not pass merely because it has an interesting quotient.

A3: global structure.

:   Are analytic continuation, functional equation, completed factors, total divisor growth, extra zeros and poles, and any proposed compression established for the same determinant? A finite truncation cannot certify this gate.

A4: same-clock lift.

:   Is a Hilbert space, domain, and unitary, scattering, or self-adjoint construction defined while preserving the same clock, phases, and trace identity? Formal analogy earns at most a partial label.

#### Evidence labels.

We distinguish [proved]{.smallcaps}, [numerically certified]{.smallcaps}, [numerical observation]{.smallcaps}, [modeling choice]{.smallcaps}, [not testable]{.smallcaps}, and [open]{.smallcaps}. Exact symbolic algebra and a mathematical proof can receive the first label. Exhaustive enumeration at a frozen cutoff can certify the finite ledger it enumerates, but not an asymptotic statement. Floating-point orbit sums and cutoff trends remain observations even when a precision audit is excellent.

For legibility, the figures compress the exact evaluator enums into S, P, and F. The compression is explicit and fail-closed: only named supported verdicts map to S, only named weak/partial/formal verdicts map to P, and only named failed/not-testable verdicts map to F. An unrecognized enum stops figure generation rather than receiving support by default. also reports the first blocking gate and evidence type for each row.

#### Adversarial controls and stop rules.

Controls are chosen to test mechanism rather than visual similarity: neighboring alphabets and roofs, finite-modulus approximants, on-circle and off-circle polynomials, matched deletion rules, arithmetic and nonarithmetic sign fields, and points on both sides of a proved convergence boundary. If the same inverse-design mechanism reconstructs both desired and adversarial root geometries, the candidate stops as [proves too much]{.smallcaps}. If an early gate fails exactly, later attractive formulas are recorded but do not unlock the route.

#### Data separation.

No experiment loads a Riemann-zero table. The Riemann--von Mangoldt law is used only as a theorem-level growth benchmark [@dlmf2510]. Rational primes appear only when the candidate definition explicitly contains them or when the candidate recursion generates them. Every random seed is reported; there is no best-seed selection.

#### Route lock.

The subsequent operator evaluation, called [Route B]{.smallcaps}, is allowed only after the same source-locked object reaches A4 readiness. In the six records studied here, all [Route B]{.smallcaps} flags are false. This is a protocol outcome, not a judgment about the existence of a Hilbert--Pólya program outside the frozen objects.

# Seven Scoped Obstructions {#sec:obstructions}

The following statements are stop rules for specific classes, not universal claims about symbolic dynamics. Full proofs and edge cases appear in [9](#app:proofs){reference-type="ref" reference="app:proofs"}.

::: {#tab:obstructions}
  ID       Frozen class                                                                                        Exact conclusion                                             Not covered
  -------- --------------------------------------------------------------------------------------------------- ------------------------------------------------------------ -----------------------------------------------------------
  SD-O01   finite graph, positive finite-range roofs, finite-range weights, fixed finite-dimensional cocycle   determinant divisor has disk count $O(R)$                    countable state, infinite memory, or infinite dimension
  SD-O02   squarefree admissible two-sided shift                                                               only $0^{\mathbb{Z}}$ is periodic                            other $\mathscr B$-free observables or systems
  SD-O03   freely concatenable shared-base returns                                                             mixed primitive necklaces occur                              grammars without shared-base free concatenation
  SD-O04   unrestricted complex renewal coefficients                                                           every normalized holomorphic germ is locally representable   independently derived restricted weights
  SD-O05   unary regular/context-free return language                                                          accepted lengths cannot be exactly the primes                binary or stronger computational grammars
  SD-O06   fixed finite-dimensional unitary twist                                                              one mixed primitive factor cannot vanish identically         infinite-dimensional or differently sourced cancellations
  SD-O07   strict wheel level shift                                                                            endogenous prime recursion is acyclic                        a separately source-locked factor or recoding

  : The seven obstruction claims and their escape boundaries. Each row is conditional on the named class; none is a universal statement about symbolic dynamics.
:::

## Finite memory has the wrong divisor scale

Let $G=(V,E)$ be a finite directed multigraph. Finite-range symbolic data can first be recoded on a finite higher-block graph, so assume the data are edge-local. Assign each edge a positive roof $\tau_e$, a complex weight $w_e$, and a fixed matrix $A_e\in\operatorname{Mat}_d(\mathbb{C})$. The block transfer matrix is $$M(s)_{uv}=\sum_{e:u\to v} w_e e^{-s\tau_e}A_e,
  \qquad D(s)=\det(I-M(s)).$$

[\[thm:finite-memory\]]{#thm:finite-memory label="thm:finite-memory"} If $D\not\equiv0$, then $D$ is a finite exponential polynomial and the number $n_D(R)$ of its zeros in $\lvert s\rvert\le R$, counted with multiplicity, satisfies $$n_D(R)=O(R).$$ For any finite product or meromorphic quotient of nonzero determinants of this form, the zero-plus-pole divisor total variation in the disk is $O(R)$. Consequently it cannot have the completed Riemann divisor up to multiplication by a zero-free entire factor.

Every entry of $M(s)$ is a finite sum of exponentials. Expanding the finite determinant gives $$D(s)=\sum_{j=0}^{K}a_j e^{-\lambda_j s},$$ where the identity term permits $\lambda_0=0$. Thus $\lvert D(s)\rvert\le C e^{\Lambda\lvert s\rvert}$. Jensen's formula, centered at any $s_0$ with $D(s_0)\ne0$, gives a linear disk-zero bound. For a quotient, the zero-plus-pole count is bounded by the sum of the zero counts of its nonzero numerator and denominator factors. Finite products and quotients therefore retain $O(R)$ total variation. By contrast, Riemann--von Mangoldt gives $$N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
       -\frac{T}{2\pi}+O(\log T),$$ so the nontrivial Riemann zeros alone contribute $\Theta(R\log R)$ zeros in a comparable disk [@dlmf2510]. A zero-free factor changes no divisor.

Unitarity is not needed for this bound; only the fixed finite matrix dimension is used. The hypotheses are the content of the theorem. A finite alphabet with an infinite-memory Hölder potential or an infinite-dimensional transfer operator is not covered [@pollicott1986meromorphic].

## Arithmetic language need not yield arithmetic cycles

[\[prop:squarefree\]]{#prop:squarefree label="prop:squarefree"} Let $X_{\mathrm{sf}}\subset\{0,1\}^{\mathbb{Z}}$ consist of sequences whose support misses at least one residue class modulo $p^2$ for every rational prime $p$. The only periodic point is $0^{\mathbb{Z}}$. Hence $$\#\operatorname{Fix}(\sigma^n)=1,\qquad
  \zeta_{\mathrm{AM}}(z)=\frac{1}{1-z}.$$

If a period-$n$ point has an occupied position $a$, its support contains $a+n\mathbb{Z}$. Choose a prime $p\nmid n$. Multiplication by $n$ is invertible modulo $p^2$, so $a+n\mathbb{Z}$ meets every residue class modulo $p^2$, contrary to admissibility.

Finite families of prime-square exclusions may retain many cycles. They do not approximate the periodic ledger monotonically in a way that could replace the proposition.

## Unconstrained renewal determinants are non-identifying

For a shared-base renewal code, let $$F(z)=\sum_{n\ge1}a_nz^n,\qquad D_{\mathrm{ren}}(z)=1-F(z).$$

[\[prop:inverse-design\]]{#prop:inverse-design label="prop:inverse-design"} For every germ $H(z)=1+\sum_{n\ge1}h_nz^n$ holomorphic near zero, choosing $a_n=-h_n$ gives $D_{\mathrm{ren}}=H$ throughout their common disk of convergence.

The proof is coefficient matching. Its simplicity is the diagnostic: a determinant match carries no arithmetic information until the return weights are derived independently. The statement is local to the convergence disk and does not grant continuation.

[\[prop:mixed\]]{#prop:mixed label="prop:mixed"} If two distinct return atoms $a,b$ freely concatenate through one base, the renewal zeta contains the mixed primitive necklace represented by $ab$. Moreover, a finite-dimensional unitary cocycle cannot erase its individual factor identically.

With formal atom weights $x_a,x_b$, $$Z_{\mathrm{ren}}=\frac{1}{1-x_a-x_b}
  \quad\text{whereas}\quad
  Z_{\mathrm{ind}}=\frac{1}{(1-x_a)(1-x_b)}.$$ The coefficient of $x_ax_b$ is two in the first based-word expansion and one in the second; cyclically, the discrepancy is the primitive necklace $ab$. If the cocycle products are $U_a,U_b\in U(d)$, its factor contains $\det(I-tU_aU_b)$, $t=x_ax_b$. This degree-$d$ polynomial has nonzero leading coefficient $(-1)^d\det(U_aU_b)$, so it is not identically one.

## A unary low-complexity grammar cannot select the primes

[\[prop:unary\]]{#prop:unary label="prop:unary"} No unary regular or context-free language has the rational primes as its exact set of accepted lengths.

The length set is ultimately periodic by the unary specialization of Parikh's theorem [@esparza2011parikh]. If the primes had eventual period $m$, choose a sufficiently large prime $q$. Then $q(1+m)\equiv q\pmod m$ would also be classified as prime, although it is composite.

The proposition does not cover binary encodings, context-sensitive languages, or general computation shifts.

## The endogenous wheel clock lives on a DAG

Set $Q_0=1$, $q_1=2$, and $Q_1=q_1$. Given $Q_k$, take $q_{k+1}$ to be the least integer larger than $q_k$ and coprime to $Q_k$, set $Q_{k+1}=q_{k+1}Q_k$, and retain the unit residue branches modulo $Q_{k+1}$.

[\[prop:wheel\]]{#prop:wheel label="prop:wheel"} The recursion gives $q_k=p_k$, the $k$-th rational prime, and $$\log\frac{Q_{k+1}}{Q_k}=\log p_{k+1}.$$ The frozen path shift whose every edge raises the level by one has no positive-period point. Its formal Artin--Mazur series and inverse determinant are both $1$.

Assume $Q_k=\prod_{j\le k}p_j$. The next prime is an admissible coprime successor. A composite minimizer would have either a prime divisor already in $Q_k$, contradicting coprimality, or a smaller new prime divisor, contradicting minimality. Thus the minimizer is $p_{k+1}$. For the dynamical claim, a path beginning at level $k$ begins at level $k+n$ after $n>0$ shifts, so it cannot equal the original path.

Reset edges would create cycles but would define a new object. The proposition also leaves open a separately source-locked factor or observational recoding; it rules out only the frozen strict level shift.

# The Six Frozen Objects {#sec:candidates}

is generated from the evaluator records rather than transcribed into the manuscript. The label *supported* means supported for the candidate's own declared species and convention; it does not mean agreement with the completed Riemann divisor.

## `SD-C01`: finite-state arithmetic skeleton

For the full $q$-shift, primitive necklaces of length $n$ have count $$N_q(n)=\frac{1}{n}\sum_{d\mid n}\mu(d)q^{n/d},$$ which is also the count of monic irreducible degree-$n$ polynomials over $\mathbb{F}_q$. The repetitions are exact, and after the normalization $u=q^{-s}$ the inverse zeta is $$D_q(s)=1-q^{1-s}.$$ This is a complete function-field arithmetic skeleton, so A1 and A2 are supported for that species. It does not provide a canonical rational prime $p\mapsto\gamma_p$, and [\[thm:finite-memory\]](#thm:finite-memory){reference-type="ref" reference="thm:finite-memory"} blocks the broader finite-memory comparison class at A3. The candidate is rejected rather than enlarged by adding more finite states.

## `SD-C02`: squarefree admissibility

The phase space is the two-sided binary shift whose support misses a residue class modulo $p^2$ for every rational prime $p$. This is genuine arithmetic structure, but the primes occur explicitly in the grammar, so the strict emergence reading of A0 fails. More decisively, [\[prop:squarefree\]](#prop:squarefree){reference-type="ref" reference="prop:squarefree"} leaves only $0^\mathbb{Z}$ as a periodic point and gives $D_{\mathrm{AM}}(z)=1-z$. The candidate illustrates why rich aperiodic language structure and an arithmetic definition do not imply a useful primitive-orbit ledger.

## `SD-C03`: shared-base renewal inverse design

The renewal graph has a distinguished base vertex $b$. For each $n\ge1$, it has a first-return atom $r_n$: a length-$n$ directed path from $b$ back to $b$, with internal vertices disjoint from all other atoms and aggregate complex weight $a_nz^n$. At $b$, any atom may follow any other atom, and the first-return factorization is unique. Hence $$F(z)=\sum_{n\ge1}a_nz^n,\qquad
  Z_{\mathrm{ren}}(z)=\frac{1}{1-F(z)},\qquad
  D_{\mathrm{ren}}(z)=1-F(z).$$ Primitive cycles are cyclic necklaces in the return atoms. This gives a weak primitive expansion, but three exact failures intervene. The weights contain all analytic information ([\[prop:inverse-design\]](#prop:inverse-design){reference-type="ref" reference="prop:inverse-design"}); atom concatenation creates unwanted mixed primitive words; and finite unitary phases cannot remove their factors ([\[prop:mixed\]](#prop:mixed){reference-type="ref" reference="prop:mixed"}). The same degree-12 procedure reconstructs on-circle, off-circle, and generic controls exactly. The outcome is therefore [stop scoped / proves too much]{.smallcaps}; no Riemann target was fitted after that stop.

## `SD-C04`: Gauss words and the Mayer operator

For a continued-fraction digit $n$, write $$\phi_n(z)=\frac{1}{n+z},\qquad
  A_n=\begin{pmatrix}0&1\\1&n\end{pmatrix}.$$ For $w=(n_1,\ldots,n_m)$, take the ordered composition $\phi_w=\phi_{n_1}\circ\cdots\circ\phi_{n_m}$ and its matching Möbius product $M_w=A_{n_1}\cdots A_{n_m}$. (The experiment uses a fixed conjugate matrix convention, which preserves traces, eigenvalues, and roofs.) A primitive digit necklace determines an attracting fixed point $x_w$, and the derivative roof satisfies $$T_w=-\log\lvert\phi_w'(x_w)\rvert
      =2\log\lambda_+(M_w),\qquad T_{v^r}=rT_v.$$ Let $$D=\{z\in\mathbb{C}:\lvert z-1\rvert<3/2\},$$ and let $A_\infty(D)$ be the Banach space of functions holomorphic on $D$, continuous on its closure, with the supremum norm. For $\operatorname{Re}(s)>1/2$, Mayer realizes $$(\mathcal L_s f)(z)=\sum_{n\ge1}(z+n)^{-2s}
  f\!\left(\frac1{z+n}\right)$$ as a nuclear operator of order zero on $A_\infty(D)$ (and on a corresponding Hardy-space realization). In that source domain its Fredholm determinants satisfy $$D_{\mathrm{MG}}(s)
  =\det(I-\mathcal L_s^2)
  =\det(I-\mathcal L_s)\det(I+\mathcal L_s)$$ [@mayer1990gauss; @mayer1991selberg]. These are genuine A1--A2 successes and lie outside [\[thm:finite-memory\]](#thm:finite-memory){reference-type="ref" reference="thm:finite-memory"}.

The mismatch is not analytic naturalness but arithmetic species. Primitive continued fractions encode quadratic irrationals or hyperbolic modular classes, not rational primes. At the largest finite cutoff, many distinct non-reversal classes share a matrix trace, so trace is not an injective arithmetic label. That collision does not rule out every future map, but no map frozen here passes A0. A modular-surface interpretation is not imported to repair the same-object symbolic audit.

## `SD-C05`: wheel-sieve level shift

The recursive least-coprime rule supplies the strongest endogenous rational-prime origin among the six objects. With $Q_0=1$ and $q_1=Q_1=2$, level $k$ has vertices given by the unit residues $$R_k=\{0\le r<Q_k:\gcd(r,Q_k)=1\}.$$ The vertex $(k,r)$ has an edge to each unit lift $(k+1,r+jQ_k)$, with $0\le j<q_{k+1}$; exactly one lift is deleted because it is divisible by $q_{k+1}$. If $X_k$ is the set of one-sided path tails beginning at level $k$, then deleting the first edge defines $\sigma:\bigsqcup_{k\ge0}X_k\to\bigsqcup_{k\ge0}X_k$ with $\sigma(X_k)\subset X_{k+1}$.

proves both $q_k=p_k$ and the intrinsic scale increment $\log p_{k+1}$, so A0 is supported without a prime table. The same definition shows why this is not yet a zeta candidate: every edge raises the level, no positive-period orbit exists, and the formal determinant is $1$. The arithmetic coordinate cannot be transferred to `SD-C04`'s determinant. A stationary factor or recoding would be a new source lock, not an A1 result for the frozen DAG.

## `SD-C06`: Knauf's arithmetic recursion

On finite binary words set $h(\varnothing)=1$ and, for a prefix $u\in\{0,1\}^{k-1}$, define $$h(u0)=h(u),\qquad h(u1)=h(u)+h(\bar u),$$ where $\bar u$ is the bitwise complement. Let $h_k$ be the restriction to $\{0,1\}^k$, and group configurations by $$\varphi_k(n)=\#\{\sigma\in\{0,1\}^k:h_k(\sigma)=n\}.$$ Then $$Z_k(s)=\sum_n\varphi_k(n)n^{-s}.$$ The source construction defines $h$ on the finite-support direct union, identifies its full multiplicity with Euler's totient, and proves $0\le\varphi_k(n)\le\varphi(n)$ together with absolute convergence $$\lim_{k\to\infty}Z_k(s)
  =\sum_{n\ge1}\frac{\varphi(n)}{n^s}
  =\frac{\zeta(s-1)}{\zeta(s)},\qquad \operatorname{Re}(s)>2$$ [@knauf2013adelic; @knauf1998spin; @knauf1999erratum]. No universal finite-$k$ equality range is assumed here: the separately reported $k=22$ audit certifies only the finite statement $\varphi_{22}(n)=\varphi(n)$ for $1\le n\le23$. The exact limiting quotient is the strongest analytic-arithmetic collision in the audit.

The result does not supply A1 or A2. The finite configurations and their Dirichlet partition sum have no frozen orientation, repetition, monodromy, or complete primitive-cycle map. The Liouville-weighted refinement uses an extra arithmetic sign unless a symbolic symmetry derives it. Finite-depth values at $\operatorname{Re}(s)\le2$ remain continuation or boundary benchmarks, not evidence for the open signed-convergence region. In particular, the candidate supplies neither a completed-$\xi$ Fredholm divisor nor an operator lift.

# Reproducible Finite Audits {#sec:experiments}

The numerical work tests implementations, finite ledgers, and adversarial controls. It is not used to infer a Riemann divisor. Four frozen runners execute 29 tests in total: 12 across the three core candidates, five for the Gauss-word code, five for the wheel code, and seven for the Knauf recursion. All tests passed on fresh frozen reruns. Exact integer arithmetic, rational coefficients, decimal precision, and binary floating-point fields are labeled separately in the artifacts.

![Finite computations validate obligation-specific behavior rather than a Riemann divisor. (a) At the largest word cutoff, the Gauss primitive ledger grows with digit cutoff, while non-reversal matrix-trace collisions also grow. (b) At the largest wheel level, the arithmetic deletion rule recovers the unit residues exactly and matched controls do not, yet all eight frozen ledgers are acyclic. Random-control points show every seed and the blue segment shows their mean. (c) Knauf finite-depth benchmark errors are small deep in the Dirichlet region; the shaded continuation/boundary region is a benchmark only and supplies no convergence claim. The scripts read the frozen CSV files and cross-check their maxima against JSON summaries.](<../../../../../symbolic_dynamics/papers/01-falsification-first-audit/figures/fig2_finite_audits.pdf>){#fig:finite-audits width="\\textwidth"}

#### `SD-C01`: exact counts and a numerical theorem control.

For $q=2,3,5$, formula counts through degree 12 agree with independent primitive-necklace and irreducible-polynomial enumeration wherever brute-force cutoffs overlap. At degree 12 the formula gives $335$, $44{,}220$, and $20{,}343{,}700$, respectively. The finite determinant controls show linear, rather than $T\log T$, root-count behavior: the commensurable unitary example gives counts $7,14,28,56$ for $T=10,20,40,80$, while the nonlattice example gives $5,11,23,43$. These four-point controls illustrate [\[thm:finite-memory\]](#thm:finite-memory){reference-type="ref" reference="thm:finite-memory"}; they are not its proof.

#### `SD-C02`: finite approximants versus the infinite grammar.

The exact theorem gives one fixed point at every period. At period 30, a finite approximation using three prime-square moduli still has $4{,}501$ fixed points, while the golden-mean and full-binary controls have $1{,}860{,}498$ and $1{,}073{,}741{,}824$. The contrast prevents a finite-modulus census from being mistaken for the periodic structure of the full exclusion.

#### `SD-C03`: an adversarial identifiability check.

Degree-12 on-circle, off-circle, and generic rational polynomials are all reconstructed coefficientwise exactly by the same renewal inverse map. The on-circle control has 12 of 12 numerical roots on the unit circle, whereas the off-circle control has six roots inside and six outside. Maximum radius errors against exact factor geometry are below $4.1\times10^{-15}$. Good root reconstruction is therefore evidence for the algebraic flexibility, not for selective arithmetic dynamics.

#### `SD-C04`: exact word bookkeeping.

\(a\) reads the rows with the largest frozen word cutoff, $L=8$, from the 12-row cutoff table. At $D=5$, the code enumerates $63{,}319$ primitive necklaces. Cyclic-invariance, reversal-transpose, repetition-matrix, and reverse-completeness failure counts are all zero. There are $7{,}018$ non-reversal trace-collision groups. The latter result blocks trace as an injective label but does not challenge the continued-fraction orbit ledger itself. Recomputing orbit sums at 40 and 80 decimal digits changes them by at most $5.28\times10^{-42}$.

#### `SD-C05`: arithmetic separation and universal acyclicity.

The finite wheel audit reaches level 7 with multipliers $2,3,5,7,11,13,17$. It certifies $98{,}460$ vertices and $98{,}459$ edges. The arithmetic residue set has unit-set Jaccard score one at every level. At level 7, fixed, cyclic, and five random matched controls have the same residue count but Jaccard scores between approximately $0.14$ and $0.41$. Kahn traversal processes every vertex for all eight ledgers and finds no directed cycle. Thus the control separates the deletion rule but does not repair A1.

#### `SD-C06`: finite-depth domain audit.

The largest recursion has $2^{22}=4{,}194{,}304$ states, support size $28{,}863$, and complete totient multiplicities only through $n=23$. For the unsigned observable, absolute benchmark errors at $s=3$ and $s=4$ are $4.47\times10^{-3}$ and $6.92\times10^{-5}$; for the Liouville-weighted observable they are $1.46\times10^{-4}$ and $1.59\times10^{-6}$. Near the boundary, the errors remain much larger. Complex double precision agrees with a 100-decimal-digit direct sum to at most $7.85\times10^{-15}$.

The sign controls sharpen the claim boundary. The depth-coherent symbolic parity control has median successive-cutoff drift $0.001303$, below the Liouville value $0.004361$. Small finite-depth drift is therefore not selective evidence for the arithmetic sign. Random signs are keyed separately by depth, so their reported cross-level differences are not convergence diagnostics for one fixed observable.

#### Figure provenance.

is generated from the six YAML evaluations. is generated from the Gauss cutoff table, wheel level table, and Knauf final-grid table; its script verifies corresponding JSON summary and DAG-certificate fields before plotting. No plotted result is hard-coded in the generation scripts.

# What the Negative Result Does and Does Not Say {#sec:scope}

The audit finds no complete row in [1](#fig:route-a-matrix){reference-type="ref" reference="fig:route-a-matrix"}. That statement has three useful consequences.

#### First, attractive coordinates remain attributable.

`SD-C04` demonstrates that a symbolic grammar can support a natural infinite-dimensional determinant without free orbit-by-orbit weights. `SD-C05` demonstrates that a short recursion can generate rational primes and $\log p$ increments endogenously. `SD-C06` demonstrates that a binary arithmetic recursion can produce an exact quotient of zeta functions. Reporting these facts separately is stronger than calling all three *near misses*, because it specifies the missing mathematical map in each object.

#### Second, coordinatewise synthesis is invalid.

The Gauss determinant counts hyperbolic modular classes. Relabeling those classes with the wheel primes would replace A0 and the clock. Giving the wheel graph the Gauss determinant would replace its dynamics and periodic ledger. Adding Knauf's Liouville weight to either object would introduce a new arithmetic observable. None of these operations is a deduction from a frozen source lock.

#### Third, the stop rules reduce the next search space.

Adding finitely many states or a finite-dimensional phase cannot overcome [\[thm:finite-memory\]](#thm:finite-memory){reference-type="ref" reference="thm:finite-memory"}. Free complex renewal coefficients cannot establish arithmetic selectivity, and a unary context-free prime-length selector cannot work. Resetting the wheel hierarchy post hoc changes the candidate. These are reusable exclusions even though the six-object search is not exhaustive.

Several escape classes remain open: countable-state operators with a source-derived potential, finite alphabets with genuinely infinite memory, infinite-dimensional cocycles, or a newly defined observational factor of an arithmetic recursion. Their complexity cannot be hidden in a prime-indexed alphabet, an orbit table, a target-designed coefficient sequence, or a zero-selected phase. Any such proposal must name its function space and determinant before comparison.

The literature search likewise has a bounded interpretation. We did not find one low-description-complexity symbolic object that supplies all five obligations. A negative search is not a theorem of nonexistence. Ideas whose definition requires modular geometry, a quantum graph, scattering theory, or a Hamiltonian system belong to a different primary family and are not developed in this paper.

#### Threats to validity.

The candidate set was chosen to cover finite-state, arithmetic-subshift, renewal, countable continued-fraction, hierarchical sieve, and binary arithmetic-recursion mechanisms; it is broad but finite. Some evaluator labels necessarily compress qualitative distinctions. The manuscript therefore exposes the underlying verdict strings and source locks in machine-readable form. Finally, the finite experiments emphasize exact enumeration and adverse controls rather than statistical sampling. Their main threat is cutoff interpretation, addressed by labeling every continuation and near-boundary value as an observation.

# Conclusion {#sec:conclusion}

A convincing arithmetic determinant needs one symbolic object to carry its arithmetic source, primitive and repeated orbits, determinant, global analytic structure, and operator clock. The six frozen constructions studied here each miss at least one indispensable link. Seven scoped proofs explain why several tempting repairs fail, while the finite audits verify that the negative verdicts are not consequences of simple implementation errors.

The resulting contribution is a falsification discipline rather than a positive Hilbert--Pólya candidate. It prevents a function-field necklace ledger, a Gauss Fredholm determinant, a wheel prime generator, and a Knauf zeta quotient from being combined into a synthetic claim. It also marks clear escape boundaries: infinite-memory and genuinely infinite-dimensional symbolic models remain outside the strongest no-go theorem.

The next admissible step is therefore not a larger finite fit. It is a new, fully source-locked symbolic object whose arithmetic rule and function space are fixed before target comparison. Such an object must restart at A0; until it closes A0--A4 on its own, the operator route remains locked.

# Proof Details and Edge Cases {#app:proofs}

## Finite exponential polynomials {#app:finite-memory}

Let the cocycle dimension be $d$, so $M(s)$ is a $(d\lvert V\rvert)\times(d\lvert V\rvert)$ scalar matrix after choosing a basis. Each scalar entry is a finite sum of terms $c e^{-s\tau_e}$. The Leibniz determinant expansion contains finitely many finite products. After distributing and collecting equal exponents, $$D(s)=\sum_{j=0}^{K} a_j e^{-\lambda_j s},$$ where every $\lambda_j$ is a finite sum of positive roofs and the empty sum $\lambda_0=0$ accounts for the identity term when its collected coefficient is nonzero. If $\Lambda=\max_j\lambda_j$ and $C=\sum_j\lvert a_j\rvert$, then $$\lvert D(s)\rvert
  \le C e^{\Lambda\lvert\operatorname{Re}(s)\rvert}
  \le C e^{\Lambda\lvert s\rvert}.$$

Because $D\not\equiv0$, choose $s_0$ with $D(s_0)\ne0$ and define $F(z)=D(s_0+z)/D(s_0)$. Jensen's formula at radii $R$ and $2R$ implies $$n_F(R)\log 2
  \le \log\max_{\lvert z\rvert=2R}\lvert F(z)\rvert.$$ The exponential-type estimate bounds the right-hand side by $$\log C-\log\lvert D(s_0)\rvert
  +\Lambda(\lvert s_0\rvert+2R)=O(R).$$ Changing the disk center and radius by the fixed quantity $\lvert s_0\rvert$ gives $n_D(R)=O(R)$.

Any finite-range potential or roof on a finite graph becomes edge-local after passing to a finite higher-block presentation, so the same expansion applies. For a finite product, divisor multiplicities add. For a meromorphic quotient of nonzero factors, its zero-plus-pole divisor total variation is bounded by the sum of the zero counts of all numerator and denominator factors and remains $O(R)$. Multiplication by $e^{g(s)}$, with $g$ entire, adds no zero or pole. Since the nontrivial Riemann zeros lie in a bounded real strip and have vertical count $\Theta(T\log T)$, they already contradict the disk bound.

Two edge cases deserve emphasis. If all roofs are commensurable, $D(s)=P(e^{-hs})$ and the vertical strings of zeros make the linear count transparent. A nontrivial finite-group character can cancel a leading positive block, but every character block still has the displayed finite-exponential form; the regular representation also retains the trivial sector. The proof requires only fixed finite matrices, not unitarity. Neither observation extends the theorem to infinite-dimensional representations.

## Squarefree periodic-point collapse

Suppose $x\in X_{\mathrm{sf}}$ has period $n$ and nonempty support. Choose $a$ in its support. Periodicity gives $a+n\mathbb{Z}\subset\operatorname{supp}(x)$. Euclid's theorem supplies a prime $p\nmid n$. Since $n$ is a unit modulo $p^2$, the map $$k\longmapsto a+nk\pmod{p^2}$$ is a bijection. The support therefore meets every class modulo $p^2$, contradicting the frozen admissibility rule. Hence the support is empty. The zero sequence belongs to every $\operatorname{Fix}(\sigma^m)$, so every fixed-point count is exactly one and $$\exp\left(\sum_{m\ge1}\frac{z^m}{m}\right)=\frac{1}{1-z}.$$ Replacing the infinite set of exclusions by a finite prefix invalidates the choice of $p$ and does not prove the result.

## Renewal flexibility, positivity, and mixed factors

For inverse design, take a normalized germ $H(z)=1+\sum_{n\ge1}h_nz^n$ and set $a_n=-h_n$. Then $$1-\sum_{n\ge1}a_nz^n=H(z)$$ throughout the common convergence disk. No orbit inference occurs in this coefficient identity.

There is a complementary obstruction for nonnegative weights. If $a_n\ge0$, not all zero, then $F(r)=\sum_n a_nr^n$ is continuous and strictly increasing on the positive part of its convergence interval. If an explicit bracket satisfies $F(r_-)<1<F(r_+)$, the intermediate value theorem gives a unique positive determinant zero. Positivity alone makes no claim when the crossing condition fails.

For distinct atoms $a,b$, expand the two formal series: $$\frac{1}{1-x_a-x_b}
  =1+x_a+x_b+x_a^2+2x_ax_b+x_b^2+\cdots,$$ $$\frac{1}{(1-x_a)(1-x_b)}
  =1+x_a+x_b+x_a^2+x_ax_b+x_b^2+\cdots.$$ The coefficient difference is the based form of a mixed cyclic primitive. Prohibiting every switch between atoms would split the graph into atom-indexed components, which is a new and explicitly assembled model.

For a finite unitary twist, the mixed primitive contributes a polynomial $\det(I-tU_aU_b)$. Because $U_aU_b$ is invertible, its leading coefficient is nonzero. The polynomial cannot be identically one, regardless of cancellations at isolated values of $t$.

Finally, a unary regular or context-free language has an ultimately periodic length set. If that set equaled the primes beyond a threshold with period $m$, a prime $q$ beyond the threshold and the composite $q(1+m)$ would receive the same classification. The contradiction proves [\[prop:unary\]](#prop:unary){reference-type="ref" reference="prop:unary"}. This argument depends on the unary and context-free hypotheses.

## Wheel induction and the path-space convention

The base case is $q_1=p_1=2$, with $Q_0=1$ and $Q_1=2$. Assume inductively that $q_j=p_j$ for $j\le k$ and $Q_k=\prod_{j\le k}p_j$. The next rational prime $p_{k+1}$ is coprime to $Q_k$, so the least admissible successor $q_{k+1}$ is no larger. If $q_{k+1}$ were composite, let $r$ be its least prime factor. When $r\le p_k$, one has $r\mid Q_k$, contradicting coprimality. When $r>p_k$, the smaller integer $r<q_{k+1}$ is itself coprime to $Q_k$, contradicting minimality. Therefore $q_{k+1}=p_{k+1}$, and $Q_{k+1}/Q_k=p_{k+1}$.

Let $X_k$ be the one-sided paths whose first edge begins at level $k$, and set $X=\bigsqcup_{k\ge0}X_k$. Deleting the first edge gives $\sigma(X_k)\subset X_{k+1}$. Consequently $\sigma^n(X_k)\subset X_{k+n}$, and the disjointness of the components precludes $\sigma^n x=x$ for $n>0$. This phase-space convention is noncompact but explicit. Adding predecessor or reset structure changes the object and lies outside the proposition.

# Reproducibility and Evidence Ledger {#app:reproducibility}

## Frozen commands

All six evaluator records bind the experiment code to the full source commit recorded in the accompanying test report (prefix `7c059754141b`). The relocation and paper generation do not alter that experiment-code provenance. A fresh frozen rerun from the Stage-01 root used

    python -m pytest -q

and returned $29/29$ passing tests. The stage-manifest entry for the test report binds the command, output, and Python/package versions.

From the Stage-01 root, the four experiment entry points are:

    python finite_state_arithmetic_skeleton/experiments/run_session4_core.py
    bash farey_gauss_transfer/experiments/run.sh
    bash wheel_sieve_level_shift/experiments/run.sh
    bash knauf_spin_chain_audit/experiments/run.sh

The first command runs the `SD-C01`--`SD-C03` core. Candidate directories retain their frozen configurations, run logs, machine-readable results, and tests.

From the paper directory, regenerate all paper figures and the candidate table with:

    python figures/generate_all.py

The figure scripts resolve the Stage-01 root from their own file locations. They read YAML, CSV, and JSON inputs and fail if cross-format summary fields do not agree.

## Cutoffs, precision, and seeds

  Object     Frozen finite protocol
  ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------
  `SD-C01`   $q=2,3,5$, formula degree 12; determinant rectangles $T=10,20,40,80$; exact integers and 80 decimal digits; unitary seed 20260815.
  `SD-C02`   Brute periods through 14, exact census through 30, binary window length 4096; shuffle seed 20260816.
  `SD-C03`   Degree-12 rational controls; 80-digit positive-root bracketing; seeds 20260813--20260814 plus master control seed 20260812.
  `SD-C04`   Digit cutoffs $D=2,3,4,5$, word cutoffs $L=4,6,8$, 80 decimal digits and an independent 40-digit audit.
  `SD-C05`   Levels 0--7; arithmetic, fixed, cyclic, and five random deletion controls with seeds 20260812--20260816; exact integer graph certificates.
  `SD-C06`   Depths $k=8,10,\ldots,22$, 16 frozen real/complex points, complex double precision and independent 50/100-digit direct sums; every random seed is reported.

## Claims to artifacts

  Claim                                        Primary artifact classes
  -------------------------------------------- ----------------------------------------------------------------
  Finite-memory $O(R)$ obstruction             and exact count JSON/CSV.
  Squarefree periodic collapse                 and periodic census CSV.
  Renewal inverse design and mixed words       , result JSON, and control CSV.
  Gauss ledger and collisions                  , cutoff CSV, compressed orbit ledger, and summary JSON.
  Wheel prime recursion and DAG                , level CSV, compressed edge ledger, and DAG certificate JSON.
  Knauf quotient and finite-depth boundaries   , , final-grid and precision CSV files, and summary JSON.
  Route-A matrix and Route-B lock              Six append-only YAML files under .

The Stage-01 manifest records artifact hashes. The paper itself does not embed a Riemann-zero table, prime-indexed fitted parameters, or a best-seed selection.
