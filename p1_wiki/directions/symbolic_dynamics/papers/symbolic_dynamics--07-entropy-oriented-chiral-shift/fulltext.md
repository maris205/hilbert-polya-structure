---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--07-entropy-oriented-chiral-shift"
canonical_tex: "symbolic_dynamics/papers/07-entropy-oriented-chiral-shift/main.tex"
canonical_pdf: "symbolic_dynamics/papers/07-entropy-oriented-chiral-shift/main.pdf"
source_sha256: "e6c773edd824f0929e588ddf7a7b45607bdc4993b3719a0b7e9ab374a0ba29eb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Entropy-Oriented Couplings of the Tensor-Prime Shift: Exact Euler Ledgers, Chiral Spectral Motion, and Divisor Invisibility

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/07-entropy-oriented-chiral-shift>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/07-entropy-oriented-chiral-shift/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/07-entropy-oriented-chiral-shift/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/07-entropy-oriented-chiral-shift/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/07-entropy-oriented-chiral-shift/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The tensor-prime symbolic shift gives the exact Euler product but isolates its prime atoms; a previous Hellinger chiral pairing consequently had no critical-axis spectral motion. We prove first that the obstruction was stronger than stated: every one-sided phase family $A_t=G^{1/2+it}K$ is gauge-equivalent to $A_0$, whether or not $K$ commutes with mass. We then define SD-C09. Order the tensor atoms intrinsically by entropy, let $D_se_n=p_n^{-s}e_n$, let $Se_n=e_{n+1}$, and set $$L_s=\tfrac12\{D_s,I+S\}.$$ Its graph has one loop at every atom and two endpoint-weighted parallel successor edges. The successor edges cannot lie on a periodic word, hence $\operatorname{Tr}L_s^r=\sum_pp^{-rs}$ and $\det(I-zL_s)=\prod_p(1-zp^{-s})$ for $\operatorname{Re}s>1$, despite $[D_1,L_s]\ne0$. More generally, an exact scalar Euler ledger forces every off-diagonal recurrent component to be acyclic. The holomorphic chiral double $\mathcal B_s=\left(\begin{smallmatrix}0&L_s\\L_{1-s}^{\mathsf T}&0\end{smallmatrix}\right)$ belongs to $S_3$ on $1/3<\operatorname{Re}s<2/3$, satisfies exact $s\mapsto1-s$ determinant symmetry, and is self-adjoint at $s=1/2+it$. Its fourth trace is strictly maximal at $t=0$, proving genuine non-gauge spectral motion. An exact two-atom model exhibits infinitely many zero-data-free critical-axis crossings. Nevertheless the triangular coupling changes singular values but neither periodic traces nor the Euler Fredholm divisor; all-order graded cancellation is likewise determinant-invisible. Thus the stage advances the symbolic chiral mechanism while stopping at divisor motion.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Entropy-Oriented Couplings of the Tensor-Prime Shift:\
  Exact Euler Ledgers, Chiral Spectral Motion, and Divisor Invisibility
```

## Markdown 正文

# Introduction {#sec:introduction}

The symbolic program begins with the symmetric monoidal family of full shifts $F_n$. Its tensor law and entropy are $$F_m\boxtimes F_n\cong F_{mn},\qquad h_{\rm top}(F_n)=\log n.$$ The nonunit tensor atoms are therefore precisely $F_p$, with the correct logarithmic clock emerging from entropy. An atom-loop transfer then gives one primitive loop per prime and its iterates give prime powers. Paper06 added a canonical binary Parry fluctuation sector and obtained the Gaussian Mellin factor $\pi^{-s/2}\Gamma(s/2)$, but its first chiral completion was spectrally constant on the critical axis.

The next proposed move was to mix distinct atom masses while cancelling all mixed primitive cycles. That formulation hides two different questions: must cross-atom edges be recurrent, and must cancellation be the mechanism? The answer to both is no. The atom source already has a strict total order, because the entropies $\log p$ are distinct. Transitions may be oriented toward increasing entropy. Such edges genuinely mix masses, yet no periodic word can traverse them. The prime-power ledger then remains exact by grammar, rather than by a fitted sign cancellation.

This observation leads to SD-C09, the entropy-oriented anticommutator shift. Write the tensor atoms as $p_1<p_2<\cdots$, let $S$ be the unilateral successor shift, and average the endpoint weights: $$L_s=D_s+\frac12(D_sS+SD_s),
 \qquad D_se_n=p_n^{-s}e_n.                 \tag{1.1}$$ The two successor summands have the same directed symbolic edge but record the source and target roof conventions. Their equal average is selected by endpoint symmetry; it is not fitted to any Riemann zero.

The construction succeeds in two exact senses. First, $L_s$ is lower bidiagonal, so its powers have diagonal entries $p_n^{-rs}$. Its Fredholm determinant in the Euler half-plane is exactly the old product. Second, the endpoint average prevents the vertical phase from being factored from only one side. The chiral double $$\mathcal B_s=
 \begin{pmatrix}0&L_s\\L_{1-s}^{\mathsf T}&0\end{pmatrix}$$ is self-adjoint for $s=1/2+it$, and a fourth-Schatten calculation proves that its spectrum changes with $t$.

The same argument also reveals the ceiling. Exact scalar Euler ledgers force the support of the off-diagonal coupling to be a directed acyclic graph. For SD-C09 this coupling lies in the triangular radical: it changes singular values and the chiral spectrum but not eigenvalues, periodic traces, or the Euler Fredholm determinant. Replacing ordinary trace by a supertrace does not fix the issue. If every mixed power supertrace cancels, the entire mixed superdeterminant is one. Exact cancellation makes the moving sector divisor-invisible.

The contributions are:

1.  a universal correction showing that one-sided Hellinger phases are gauge-trivial even for mass-noncommuting couplings;

2.  a directed-acyclic rigidity theorem for exact scalar Euler ledgers;

3.  the source-locked, mass-noncommuting transfer $L_s$ with the exact prime-power trace and Fredholm product;

4.  a holomorphic $S_3$ chiral determinant with exact conjugation and $s\mapsto1-s$ symmetry;

5.  a strict fourth-trace theorem establishing genuine critical-axis spectral motion;

6.  an exact two-atom crossing formula and a proves-too-much boundary;

7.  a determinant-invisibility theorem for all-order graded cancellation.

All primary objects remain countable symbolic shifts, weighted symbolic transfers, and their natural operator pencils. Ideas requiring an external geometric carrier are not developed here.

# Cyclic languages, triangular realizations, and symbolic determinants {#sec:related}

Finite-state symbolic zeta functions admit determinant presentations going back to @bowenlanford1970; transfer operators extend this language to far richer dynamical systems [@ruelle1976]. Our Euler half-plane identity is elementary, but its interpretation depends on the tensor-prime source: the diagonal weights and their clock are outputs of the full-shift monoidal structure, not an arbitrary prime-labelled graph.

The pure-power cyclic language $$\{a_i^r:i\ge1,\ r\ge1\}$$ is closely related to the theory of zeta functions of formal languages. Regular cyclic languages have virtual-character descriptions [@berstelreutenauer1990], and finite-monoid character theory explains why trace data see the semisimplification while nilpotent radicals may remain invisible [@masudaquoossteinberg2015]. Exterior-power automata yield alternating determinant formulas for sofic zeta functions [@beal1995]. These results prohibit a broad novelty claim about signed or virtual-character cancellation. The present point is narrower: an entropy-oriented radical coupling is selected inside the tensor-prime symbolic source, preserves its entire Euler ledger, and produces a moving chiral singular spectrum.

Compact-group extensions and twisted symbolic $L$-functions are classical [@parrypollicott1990]. A finite-dimensional unitary cocycle cannot delete one mixed primitive factor at all repetitions: some power of a finite group element is the identity, while the powers of an element of a compact group accumulate at the identity. Continuity then prevents a finite virtual character from vanishing on every mixed power while remaining nonzero at the identity. This is why the successful finite mechanism below is triangular and nonsemisimple rather than unitary.

There is a live infinite-dimensional symbolic alternative. The canonical trace of the left regular representation of a free group extracts the identity coefficient, and free-group matrix zeta functions exploit exactly this rule [@kasselreutenauer2014]. Analytic determinants and $L^2$ zeta functions on periodic graphs provide related precedents [@clairmokhtari2002; @guidoisolalapidus2009]. A free-group label could make a fully connected base grammar while preventing positive mixed words from closing in the extension. However, chiral self-adjointization adds inverse-labelled edges, and the positive term $gg^{-1}=e$ returns in the quadratic trace. The infinite tensor-atom analytic domain is also open. We therefore record this as the next same-family branch, not as part of SD-C09.

Signed graph zeta functions and matrix-weighted graph zeta functions modify primitive factors rather than generically deleting them [@lihou2024; @ohtasakaiwagatsuma2022]. Trace monoids organize partial commutation but do not by themselves supply the required divisor-visible cancellation [@cartierfoata1999]. Homological signed constructions can remove redundant symbolic sectors, but a contractible sector is invisible to the associated alternating determinant. This agrees with our direct supertrace theorem.

The literature supports every ingredient but, in the primary-source search performed for this stage, we found no work combining tensor-prime atoms, entropy-oriented radical mixing, an exact Riemann Euler ledger, and a moving critical-axis chiral singular spectrum in one Route-A audit. This finite search is not evidence of absolute priority, so no first-ever claim is made.

# Source lock and exact-ledger rigidity {#sec:rigidity}

Let $\operatorname{At}=\{F_{p_n}:n\ge1\}$ be the tensor atoms of the full-shift monoid, listed by increasing topological entropy. Unique factorization and strict monotonicity of $\log n$ give the same order as $2=p_1<p_2<p_3<\cdots$. This is an intrinsic enumeration; no external prime table is part of the definition.

The phase space of SD-C09 is the countable directed graph with vertex set $\operatorname{At}$. It has a loop at every vertex and two parallel edges from $p_n$ to $p_{n+1}$. The loop has roof $\log p_n$. The two successor edges carry, respectively, the source roof $\log p_n$ and target roof $\log p_{n+1}$, each with scalar potential $-\log2$. There are no decreasing edges. The function space is $\ell^2(\operatorname{At})$; its transfer is defined in [4](#sec:coupling){reference-type="ref" reference="sec:coupling"}. This freezes the object, grammar, roof, potential, function space, and determinant convention before any spectral comparison.

## A universal one-sided gauge theorem

We first correct and strengthen the previous stage's no-motion theorem. Let $G$ be any positive injective diagonal mass operator and let $K$ be bounded. No commutation is assumed.

[\[thm:one-sided-gauge\]]{#thm:one-sided-gauge label="thm:one-sided-gauge"} For $$A_t=G^{1/2+it}K,
 \qquad
 B_t=\begin{pmatrix}0&A_t\\A_t^*&0\end{pmatrix},$$ one has $$B_t=U_tB_0U_t^*,
 \qquad U_t=\operatorname{diag}(G^{it},I).$$ Thus the spectrum, singular values, and every unitarily invariant regularized determinant are independent of $t$, even when $[G,K]\ne0$.

Functional calculus gives $A_t=G^{it}A_0$. Substitution into the two chiral blocks yields the asserted conjugacy.

Mass noncommutation is therefore necessary only after the phase has been placed at both endpoints in a way that cannot be factored unitarily from one side.

## Exact Euler ledgers force directed acyclicity

The next result locates every scalar one-step escape. For independent commuting variables $x=(x_1,\ldots,x_N)$ put $D(x)=\operatorname{diag}(x_1,\ldots,x_N)$.

[\[thm:dag\]]{#thm:dag label="thm:dag"} Let $K\in M_N(\mathbb C)$ and assume $$\det(I-zD(x)K)=\prod_{j=1}^N(1-zx_j)             \tag{3.1}$$ as a polynomial identity in $z,x_1,\ldots,x_N$. Then $K=I+N_0$, and the directed support of $N_0$ contains no directed cycle. Conversely, after a permutation of the vertices, every strictly triangular $N_0$ satisfies [\[eq:dag-converse\]](#eq:dag-converse){reference-type="ref" reference="eq:dag-converse"}: $$\det(I-zD(x)(I+N_0))=\prod_j(1-zx_j).
 \label{eq:dag-converse}$$ The conclusion also follows from equality of all Dirichlet coefficients after $x_j=p_j^{-s}$ for distinct tensor atoms.

Expanding the determinant by principal minors and comparing the coefficient of $z^{|S|}\prod_{j\in S}x_j$ gives $\det K_{S,S}=1$ for every $S$. In particular $K_{jj}=1$. Write $K=I+N_0$ with zero diagonal. The identity $$\det(I+(N_0)_{S,S})=
 \sum_{T\subseteq S}\det (N_0)_{T,T}$$ and induction on $|S|$ imply $\det(N_0)_{S,S}=0$ for every nonempty $S$.

If the support of $N_0$ contained a directed cycle, choose one of shortest length with vertex set $C$. It has no directed chord: a chord followed by one of the two directed portions of the cycle would produce a shorter cycle. The determinant of $(N_0)_{C,C}$ then contains exactly one nonzero permutation term, the product around the cycle, contradicting its vanishing. The support is a DAG and hence admits a topological ordering making $N_0$ strictly triangular. The converse follows from triangularity. Finally, unique factorization makes distinct prime multisets linearly independent as Dirichlet monomials, so the same coefficient comparison applies.

The theorem covers arbitrary scalar signs and complex phases: exactness does not leave a hidden recurrent signed solution. A finite-dimensional unitary cocycle does not evade it at the primitive-factor level, because a mixed cycle labelled by an invertible $U$ contributes $\det(I-wU)$, which is nonconstant.

## All-order graded cancellation is divisor-invisible

[\[thm:trace-invisible\]]{#thm:trace-invisible label="thm:trace-invisible"} Let $T=T^+\oplus T^-$ be a trace-class graded operator. If $\operatorname{Str}T^r=0$ for every $r\ge1$, then $$\operatorname{Ber}(I-zT)=1$$ throughout its Fredholm domain. More generally, if $T^\pm\in S_q$ and $\operatorname{Tr}(T^+)^r=\operatorname{Tr}(T^-)^r$ for every $r\ge q$, their relative $q$-regularized determinant is one.

Use the convergent logarithmic expansions $$\log\operatorname{Ber}(I-zT)=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Str}T^r,$$ and, after the first $q-1$ subtractions, the analogous expansion beginning at $r=q$. Analytic continuation on the connected determinant domain preserves the identity.

Thus a chain-level sector may move spectrally while exactness cancels every mixed trace, but that motion cannot generate zeros of the determinant whose logarithm uses those same traces. This is the precise ceiling that motivates the acyclic rather than homological construction below.

# The entropy-oriented anticommutator transfer {#sec:coupling}

On $\mathcal H=\ell^2(\operatorname{At})$ let $S e_n=e_{n+1}$ and $D_se_n=p_n^{-s}e_n$. Define $$L_s=\frac12\{D_s,I+S\}
     =D_s+\frac12(D_sS+SD_s).                \tag{4.1}$$ With the basis ordered by entropy, $L_s$ is lower bidiagonal: $$L_se_n=p_n^{-s}e_n+
 \frac{p_n^{-s}+p_{n+1}^{-s}}2e_{n+1}.       \tag{4.2}$$ This is exactly the transfer of the source-locked graph in [3](#sec:rigidity){reference-type="ref" reference="sec:rigidity"}: the two parallel successor edges contribute their source- and target-roof weights. Endpoint exchange swaps the edges and fixes their equal scalar potential.

[\[thm:euler-ledger\]]{#thm:euler-ledger label="thm:euler-ledger"} For $\operatorname{Re}s>1$, $L_s$ is trace class and, for every $r\ge1$, $$\operatorname{Tr}L_s^r=\sum_p p^{-rs},                    \tag{4.3}$$ $$\det(I-zL_s)=\prod_p(1-zp^{-s}).             \tag{4.4}$$ Moreover $[D_1,L_s]\ne0$.

Both $D_s$ and the weighted shift terms have singular values bounded by a constant multiple of $p_n^{-\operatorname{Re}s}+p_{n+1}^{-\operatorname{Re}s}$, so they are trace class for $\operatorname{Re}s>1$. The diagonal of a power of a lower triangular matrix is the corresponding power of its diagonal. This proves [\[eq:euler-trace\]](#eq:euler-trace){reference-type="ref" reference="eq:euler-trace"}: $$(L_s^r)_{nn}=p_n^{-rs}.
 \label{eq:euler-trace}$$ The trace and logarithmic Fredholm expansion give $$\log\det(I-zL_s)
 =-\sum_{r\ge1}\frac{z^r}{r}\sum_pp^{-rs}
 =\sum_p\log(1-zp^{-s})$$ initially for small $z$, and then on the Fredholm domain. Finally, the successor coefficient between two unequal masses is nonzero, so the commutator with $D_1$ is nonzero.

The primitive/repetition ledger is transparent. Every successor step strictly raises entropy, so a periodic word can use only one loop. The primitive objects are the atom loops $\gamma_p$, their repetitions are $\gamma_p^r$, their lengths are $r\log p$, and their scalar weights are one. There are no mixed primitive words to cancel.

## What the radical can and cannot change

The strictly lower-triangular part of $L_s$ is a nonsemisimple radical. On every finite prefix, $L_s$ has the same characteristic polynomial as $D_s$. It changes singular values, eigenvectors, and pseudospectral behavior, but it does not change eigenvalues or the ordinary Fredholm determinant. This is not an accidental cancellation at a chosen $s$: it is the exact language statement that increasing-entropy edges cannot close.

# A symmetric chiral determinant with genuine motion {#sec:chiral}

The one-sided gauge theorem requires an endpoint-symmetric alternative. Define the holomorphic operator pencil $$\mathcal B_s=
 \begin{pmatrix}
 0&L_s\\ L_{1-s}^{\mathsf T}&0
 \end{pmatrix}.                              \tag{5.1}$$ The transpose is taken in the entropy basis; it is linear rather than antilinear in $s$.

[\[prop:strip\]]{#prop:strip label="prop:strip"} One has $L_s\in S_q$ whenever $q\operatorname{Re}s>1$. Hence $\mathcal B_s\in S_3$ on $$\frac13<\operatorname{Re}s<\frac23,$$ where $$\Delta_3(s,z):=\det{}_3(I-z\mathcal B_s)            \tag{5.2}$$ is holomorphic. It satisfies $$\Delta_3(1-s,z)=\Delta_3(s,z),
 \qquad
 \Delta_3(\bar s,\bar z)=\overline{\Delta_3(s,z)}. \tag{5.3}$$ For $s=1/2+it$, $\mathcal B_s$ is self-adjoint.

The diagonal and weighted-shift singular values are controlled by the $\ell^q$ sequence $(p_n^{-\operatorname{Re}s})_n$. Both off-diagonal blocks are in $S_3$ precisely in the displayed common strip. Furthermore $\mathcal B_{1-s}=\mathcal B_s^{\mathsf T}$, and regularized determinants are invariant under transpose. Real coefficients give conjugation symmetry. On the critical line $L_{1-s}^{\mathsf T}=L_s^*$.

The regularization deletes powers one and two. Odd chiral traces vanish, so the first retained coefficient is the fourth trace. Unlike the Paper06 block-preserving pair, it moves.

Put $u_n=p_n^{-1}$ and, on $s=1/2+it$, define $$x_n(t)=\frac14\left(u_n+u_{n+1}
 +2\sqrt{u_nu_{n+1}}
 \cos\left(t\log\frac{p_{n+1}}{p_n}\right)\right). \tag{5.4}$$ This is the squared modulus of the $n$th successor coefficient of $L_s$.

[\[thm:motion\]]{#thm:motion label="thm:motion"} For the infinite SD-C09 transfer, $$\|L_{1/2+it}\|_4^4
 =\sum_n(u_n+x_n(t))^2+2\sum_nu_{n+1}x_n(t), \tag{5.5}$$ and $$\|L_{1/2+it}\|_4^4<\|L_{1/2}\|_4^4
 \qquad(t\ne0).                              \tag{5.6}$$ Consequently $\mathcal B_{1/2+it}$ is not unitarily gauge-equivalent to a constant family and $$\operatorname{Tr}\mathcal B_{1/2+it}^{,4}=2\|L_{1/2+it}\|_4^4$$ varies with $t$.

For a lower bidiagonal $L$, the diagonal of $L^*L$ is $u_n+x_n$ and its nearest off-diagonal squared modulus is $u_{n+1}x_n$. Squaring and tracing gives [\[eq:s4\]](#eq:s4){reference-type="ref" reference="eq:s4"}: $$\operatorname{Tr}(L^*L)^2=\sum_n(u_n+x_n)^2+2\sum_nu_{n+1}x_n.
 \label{eq:s4}$$ Every summand is strictly increasing in its $x_n\ge0$, and $x_n(t)\le x_n(0)$. Equality would require $t\log(p_{n+1}/p_n)\in2\pi\mathbb Z$ for every $n$. In particular, for the successive ratios $3/2$ and $5/3$, there would be integers $k,\ell$ with $$(3/2)^\ell=(5/3)^k.$$ Unique factorization forces $k=\ell=0$, and then $t=0$. Thus at least one $x_n$ is strictly smaller for every nonzero $t$, proving the claim.

Near $z=0$, the $\det_3$ expansion begins with $$\log\Delta_3(1/2+it,z)
 =-\frac{z^4}{4}\operatorname{Tr}\mathcal B_{1/2+it}^{,4}+O(z^6)
 =-\frac{z^4}{2}\|L_{1/2+it}\|_4^4+O(z^6). \tag{5.7}$$ Thus the moving spectrum is visible to the chiral regularized determinant. It is not visible to the Euler Fredholm determinant of $L_s$. The two determinants have overlapping symbolic ancestry but are not an analytic continuation of one another.

# Exact finite models and falsification controls {#sec:experiment}

The smallest prefix already separates eigenvalue ledger from singular-value motion. For atoms $2,3$, $$L_s^{(2)}=
 \begin{pmatrix}
 2^{-s}&0\\[1mm]
 \dfrac{2^{-s}+3^{-s}}2&3^{-s}
 \end{pmatrix}.                              \tag{6.1}$$ For every $r\ge1$ and every complex $s$, $$\operatorname{tr}(L_s^{(2)})^r=2^{-rs}+3^{-rs},
 \qquad
 \det(I-wL_s^{(2)})=(1-w2^{-s})(1-w3^{-s}). \tag{6.2}$$

On $s=1/2+it$, let $$c(t)=\cos\left(t\log\frac32\right).$$ A direct calculation gives $$\det\left(I-(L_s^{(2)})^*L_s^{(2)}\right)
 =\frac{3-2\sqrt6\,c(t)}{24}.                \tag{6.3}$$ Therefore the self-adjoint chiral block has an eigenvalue $+1$ or $-1$, equivalently its $z=1$ regularized determinant vanishes, exactly at $$t=\frac{2\pi k\pm\arccos(\sqrt6/4)}{\log(3/2)},
 \qquad k\in\mathbb Z.                             \tag{6.4}$$ No Riemann zero, scale fit, or numerical root search enters this formula.

This success is also an adversarial warning. Every adjacent pair $(p_n,p_{n+1})$ has an analogous elementary oscillation, and the two-atom crossings have linear periodic counting rather than the Riemann--von Mangoldt $T\log T$ law. The mechanism therefore proves too much if one mistakes "self-adjoint critical-axis crossings" for a completed-zeta divisor.

The frozen computational audit uses tensor atoms recovered from full-shift indecomposability, not a prime input file. It checks:

1.  exact lower-triangular power traces through the frozen power cutoff;

2.  ordinary Fredholm-prefix equality with the loop product;

3.  the one-sided gauge theorem for random mass-noncommuting controls;

4.  the $S_4$ identity [\[eq:s4\]](#eq:s4){reference-type="ref" reference="eq:s4"} and strict motion at nonzero heights;

5.  chiral transpose, functional-equation, conjugation, and self-adjointness residuals;

6.  the exact two-atom crossing formula;

7.  recurrent reverse-edge failures, arbitrary forward phases, random DAGs, shuffled masses, and non-atom inventories.

The frozen run confirms the exact formulas sharply. For a dense random mass-noncommuting $7\times7$ control, the largest chiral-gauge, singular-value, and eigenvalue residuals were respectively $8.56\times10^{-16}$, $8.88\times10^{-16}$, and $2.67\times10^{-15}$. On the $N=8$ atom prefix and $0\le t\le40$, the endpoint placements had no motion at scale $10^{-15}$, whereas the symmetric average had fourth-Schatten range $1.395631$. The recurrence/determinant identities had residual at most $4.03\times10^{-16}$.

      height bound $T$       20   40   80   160   320
  ------------------------ ---- ---- ---- ----- -----
   sign-changing brackets     3    5   11    21    41

These counts were identical for every cutoff $N=2,\ldots,128$ tested and stable under step halving. At 150-digit precision the first-root shifts for $N=8\to16\to32\to64$ were $3.516\times10^{-13}$, $3.66\times10^{-38}$, and $1.73\times10^{-100}$. This is strong cutoff stability, but the census is only a positive-axis sign-change scan, not an argument-principle root count. Its observed growth is $O(T)$-like, not a $T\log T$ law.

The controls expose the limit. Adding a reverse successor edge creates a two-cycle and already breaks the ledger at $r=2$, confirming [\[thm:dag\]](#thm:dag){reference-type="ref" reference="thm:dag"}. In contrast, arbitrary phases on forward edges remain triangular: they preserve *all* power traces and the full determinant, not merely a finite prefix, while typically retaining chiral motion. All 24 frozen random forward-DAG controls had both an exact ledger and spectral motion. Shuffled atom orders, composites, and matched random integers behave similarly. These are the strongest `PROVES_TOO_MUCH` controls: SD-C09's A0 credit comes from the intrinsic tensor-entropy source, while acyclic ledger preservation plus motion is broadly nonselective.

Numerics test the formulas and cutoff stability. They do not establish analytic continuation, global root counts, or an RH-like divisor.

# Route-A outcome and Route-B lock {#sec:route}

The source lock is complete: the tensor-prime atom set, entropy order, directed grammar, endpoint roofs, equal edge potentials, $\ell^2$ function space, transfer $L_s$, chiral pencil $\mathcal B_s$, and the Fredholm/$\det_3$ conventions are fixed before interpretation. The construction is assigned candidate identifier SD-C09.

## Route-A layers

0.99L0.08L0.25X Layer & Verdict & Evidence\
A0 & analytic arithmetic origin & tensor indecomposables generate primes, entropy orders them and gives $\log p$, without prime or zero tables\
A1 & analytic pass & only atom loops are periodic; their repetitions give the exact $p^r$ ledger, while successor edges are acyclic\
A2 & analytic determinant & $\det(I-zL_s)=\prod_p(1-zp^{-s})$ on $\operatorname{Re}s>1$; signed cancellations are unnecessary\
A3 & partial analytic structure & $\det_3(I-z\mathcal B_s)$ is holomorphic on $1/3<\operatorname{Re}s<2/3$, symmetric under $s\mapsto1-s$, and moves on the critical axis, but it is not the Euler determinant continued\
A4 & formal hint & a canonical self-adjoint critical-axis pencil exists; no fixed generator, quantization, domain theorem, or target counting law is supplied\

The tuple is

  -----------------------------------------------------------
      `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC,`
   `A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE,`
                      `A4_FORMAL_HINT).`
  -----------------------------------------------------------

with overall verdict $$\boxed{\texttt{ROUTE\_A\_ANALYTIC\_CANDIDATE}.}$$ The stage status is $$\boxed{\textsf{GO A3 CHIRAL MOTION}
 \;/\;
 \textsf{STOP UNIFIED DIVISOR}.}$$

## Adversarial boundary

The argument does not certify RH-like behavior for controls. Arbitrary DAG orders and phases, matched nonprime masses, and randomized positive diagonal masses all retain the all-order triangular determinant mechanism; all 24 frozen random DAGs also show chiral motion. Only recurrent reverse edges break the ledger. Two-state prefixes have periodic linearly counted crossings. Thus "exact diagonal ledger plus moving chiral singular values" is not sufficient for a Riemann divisor. The arithmetic source remains selective at A0, but the chiral inference stops at A3/A4.

## Why Route B is locked

$\mathcal B_{1/2+it}$ is a compact self-adjoint operator for each $t$, but it is an operator pencil whose parameter is the proposed spectral height. It is not a single self-adjoint operator $H$ with eigenvalue parameter $E$. No dense domain or boundary condition problem has been posed, no compact-resolvent $T\log T$ counting theorem exists, no exact von-Mangoldt trace formula is derived from this pencil, and no spectral determinant equals completed $\xi$. The Euler and chiral determinants remain distinct data types. Route B therefore cannot be used to combine their best coordinates, and $$\mathtt{route\_b\_invocation\_allowed=false}.$$

The next smallest same-family test is a relative-determinant theorem: either derive a source-internal bridge between the Euler Fredholm determinant and the chiral $\det_3$ without fitted counterterms, or prove that the deleted low-order traces obstruct every such bridge.

# Conclusion: motion exists, but not yet divisor motion {#sec:conclusion}

SD-C09 answers the sharp question left by Paper06. A symbolic coupling can mix distinct tensor-atom masses, preserve every prime-power coefficient, and produce genuine critical-axis chiral spectral motion. The mechanism is neither a fitted sign table nor a cancellation miracle. The tensor source already orders its atoms by entropy, and an increasing edge cannot belong to a periodic word.

This success changes the frontier. The correct obstruction is no longer "exact Euler ledgers forbid noncommuting coupling." They forbid recurrent scalar coupling. Directed-acyclic radical coupling survives and can move singular values. Endpoint-symmetric placement then defeats the universal one-sided phase gauge and yields an exact fourth-trace signal.

The construction also proves its own limitation. The moving radical does not change the Euler Fredholm divisor, while a graded sector whose mixed traces cancel at all orders has superdeterminant one. Hence $$\boxed{
 \text{exact ledger}+\text{noncommuting spectral motion}
 \not\Rightarrow \text{divisor motion}.}$$ The remaining task is not to create motion; it is to make one natural determinant see both the arithmetic ledger and the moving sector.

One same-family escape remains live. A free-group extension with its canonical identity-coefficient trace can suppress mixed positive words in a fully recurrent base grammar. Its self-adjoint double, however, restores positive $gg^{-1}$ terms and its infinite-atom analytic domain is unresolved. That precise branch, rather than a generic phase search, is the next symbolic experiment.

No geometric system is constructed. If a future bridge requires local turning phases or a fixed generator supplied by a geometric carrier, that is a second-round clue rather than a coordinate to splice into SD-C09. Route B remains locked until one compatible object owns the arithmetic trace, critical-axis spectral parameter, and completed divisor.

# Proof details, determinant conventions, and scope {#app:proofs}

## Operator-ideal estimates

The singular values of $D_s$ are $p_n^{-\operatorname{Re}s}$. For a weighted unilateral shift $W_se_n=w_n(s)e_{n+1}$, the singular values are $|w_n(s)|$. Here $$|w_n(s)|\le\tfrac12
 (p_n^{-\operatorname{Re}s}+p_{n+1}^{-\operatorname{Re}s}).$$ Consequently $L_s\in S_q$ whenever $\sum_np_n^{-q\operatorname{Re}s}<\infty$, namely when $q\operatorname{Re}s>1$. Applying the same argument to $L_{1-s}^{\mathsf T}$ gives the common $S_q$ strip $$\frac1q<\operatorname{Re}s<1-\frac1q.$$ The first integer $q$ with a nonempty strip is $q=3$.

## Regularized determinant convention

For $A\in S_3$ we use $$\det{}_3(I-A)
 =\det\bigl((I-A)e^{A+A^2/2}\bigr),$$ so near the origin $$\log\det{}_3(I-zA)
 =-\sum_{r\ge3}\frac{z^r}{r}\operatorname{Tr}A^r.$$ For the chiral $\mathcal B_s$, every odd trace vanishes. The first visible term is $r=4$. This is a genuine determinant theorem in the $S_3$ strip, but the subtracted $r=2$ term is the divergent Hellinger trace. We do not restore it by an ad hoc counterterm.

## Finite-prefix determinant

Let $P_N$ project onto the first $N$ entropy-ordered atoms. Then $P_NL_sP_N$ is triangular and $$\det(I-zP_NL_sP_N)=\prod_{n\le N}(1-zp_n^{-s}).$$ For $\operatorname{Re}s>1$, $P_NL_sP_N\to L_s$ in trace norm. Continuity of the Fredholm determinant proves the infinite product identity independently of the logarithmic trace expansion.

## Source and data firewall

The construction uses the multiplication law of full shifts, topological entropy, the induced order on tensor atoms, and endpoint roof evaluation. It loads no Riemann-zero table. Finite computations may generate indecomposables of the multiplication table algorithmically; no list of primes is an input to the candidate.

The following implications are explicitly forbidden: $$\begin{aligned}
 \Delta_3(1-s,z)=\Delta_3(s,z)
   &\not\Rightarrow \text{Riemann functional equation},\\
 \mathcal B_{1/2+it}=\mathcal B_{1/2+it}^*
   &\not\Rightarrow \text{Hilbert--P\'olya operator},\\
 \text{critical-axis crossings}
   &\not\Rightarrow \text{Riemann zeros},\\
 \text{moving singular spectrum}
   &\not\Rightarrow \text{moving Euler divisor}.\end{aligned}$$

Any plan requiring a separate geometric, graph-theoretic physical, or Hamiltonian system is outside the primary family and may appear only as a `ROUND2_CLUE`.
