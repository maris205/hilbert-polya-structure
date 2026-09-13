---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--13-character-resolved-holonomy"
canonical_tex: "symbolic_dynamics/papers/13-character-resolved-holonomy/main.tex"
canonical_pdf: "symbolic_dynamics/papers/13-character-resolved-holonomy/main.pdf"
source_sha256: "0944f978957389fed0484c5e3c41fe72d9deb893ed5f8e617dd6a6b11d7f1c2b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Character-Resolved Holonomy over Tensor-Prime Symbolic Loops: Exact Euler Zero Mode and a Reversal Trilemma

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/13-character-resolved-holonomy>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/13-character-resolved-holonomy/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/13-character-resolved-holonomy/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/13-character-resolved-holonomy/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/13-character-resolved-holonomy/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a character-resolved determinant from one positive-cocycle $\mathbb Z$-extension of the tensor-prime symbolic loop system. The base graph is recurrent, but every cross edge increases the lift coordinate. Consequently its periodic lifted orbits, modulo deck translation, are exactly the tensor-prime loops and their repetitions. Fourier transformation in the lift coordinate gives trace-class Bloch fibers $L_s(w)=D_s+wA_s$ for $\Re s>1$. We prove that the zero Fourier coefficient of $\log\det(I-zL_s(w))$ is $\sum_p\log(1-zp^{-s})$, while positive coefficients record charged mixed base returns. Thus the formerly averaged-out sector becomes visible inside the same Fredholm family without changing the Euler mode. A two-vertex formula shows immediate nontrivial character motion. Three exact obstructions then stop the proposed RH mechanism: entropy coboundaries are gauge, an entropy-roof character only translates $s$, and inverse labels on reversed edges return the mixed two-cycle to Fourier degree zero. Moreover composite, random, and random-charge controls reproduce the transverse response. The result is a same-parent equivariant analytic advance and a sharp holonomy trilemma. No individual unitary Bloch fiber retains the Euler ledger, so the construction is not a completed zeta determinant or Hilbert--Pólya operator.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Character-Resolved Holonomy over Tensor-Prime Symbolic Loops:\
  Exact Euler Zero Mode and a Reversal Trilemma
```

## Markdown 正文

# Introduction {#sec:introduction}

The tensor product of finite full shifts satisfies $F_m\otimes F_n\cong F_{mn}$, while topological entropy satisfies $h(F_n)=\log n$ and is additive under this product [@lind1984; @delvenne2019]. The tensor atoms are therefore precisely $F_p$. Placing one symbolic loop of roof $\log p$ on each atom gives the exact Euler determinant $$\det(I-zD_s)=\prod_p(1-zp^{-s}),\qquad \Re s>1.       \tag{1.1}$$ The difficulty is no longer the arithmetic ledger. It is to add recurrent, phase-bearing symbolic structure that is visible within the *same parent* equivariant Fredholm family without inserting mixed composite orbits into its neutral coefficient.

The preceding Haar-fiber construction showed that an infinite diffuse sector can preserve every power trace and yet cancel coefficientwise from the scalar trace-log. SD-C15 reverses that averaging step. We keep the full dual-character family of a single $\mathbb Z$-skew extension. Its base has loops and both adjacent returns, while every cross edge advances the lift coordinate by one. The base is strongly connected, but a mixed base return never closes upstairs. After Fourier transformation in the lift coordinate, the same operator decomposes into $$L_s(w)=D_s+wA_s,\qquad w=e^{i\theta}.                 \tag{1.2}$$

This construction makes the hidden sector analytically visible. For small $z$, closed-word expansion gives $$[w^0]\log\det(I-zL_s(w))
  =\sum_p\log(1-zp^{-s}),                              \tag{1.3}$$ whereas every mixed base return occurs in positive Fourier degree. The zero mode and the moving modes now belong to one parent Fredholm family, not to a Fredholm determinant patched to a singular-value or Fuglede--Kadison object. They remain different readouts: no individual unitary character fiber equals the neutral Euler coefficient.

The positive result is sharp but insufficient. For two masses $x,y$ and $a=(x+y)/2$, $$\det(I-zL(w))=(1-zx)(1-zy)-z^2a^2w^2.                \tag{1.4}$$ Thus character motion appears immediately, but it appears for every positive inventory. If reversed edges instead receive inverse charges, the $w^2$ term becomes degree zero and corrupts the target ledger at power two. If the phase is a vertex coboundary it is removed by diagonal conjugacy; if it is the entropy character it merely sends $s$ to $s-i\theta$.

The paper makes four contributions.

1.  It constructs the positive-cocycle lift and proves its exact primitive ledger modulo deck translation.

2.  It proves trace-class holomorphy and the all-order Euler zero-mode identity for the resolved Fredholm family.

3.  It proves a local holonomy trilemma between zero-mode exactness, inverse reversal, and character motion.

4.  It subjects the motion to exact path, gauge, random-charge, and matched inventory controls before assigning Route-A credit.

Symbolic Dynamics remains the only primary system family. Character and operator language describes the Fourier decomposition of the symbolic lift; it does not initiate a separate graph-spectral or operator-algebra route.

# Character zeta functions and claim boundary

Character twists of periodic-orbit zeta functions are classical. @adachisunada1987 developed twisted Perron--Frobenius theory and $L$-functions, and @parrypollicott1990 [Chs. 8 and 12] treated compact group extensions as well as $\mathbb Z^d$ skew extensions and their dual-torus characters. Character families for closed-orbit homology classes are central in @katsudasunada1990. Graph coverings similarly lead to Artin--Ihara factors and character determinants [@starkterras1996], while $\mathbb Z$-actions and periodic graph determinants are treated by @clair2009 and @guidoisolalapidus2008. The identity-sector zeta of amenable group extensions and its group-trace formulation are especially close to our neutral coefficient [@sharp2020]. Accordingly, neither Bloch decomposition nor a character-twisted determinant is claimed as new.

The narrower synthesis tested here is different. The character and group trace machinery itself is prior art. The loop weights here are not generic symbolic periods: they come from tensor-indecomposable full shifts, and their roof is the same object's entropy. The cocycle is chosen before any spectral computation, its zero mode has a full all-order Euler theorem, and the nonzero modes are challenged by matched arithmetic controls. We did not locate this exact Route-A audit in the primary literature.

There are two further boundaries. First, the positive-cocycle skew product is not an invertible $\mathbb Z$-cover: it is an autonomous one-sided group extension whose deck coordinate only increases on cross edges. Second, Livšic-type periodic data characterize coboundaries in much broader hyperbolic settings [@kalinin2011]. Our finite graph gauge lemma is elementary and is not presented as a new Livšic theorem.

The neutral coefficient $[w^0]$ is not the trivial Bloch character (which is $w=1$). It is the deck-neutral conditional expectation, equivalently the Haar Fourier coefficient; its equality with evaluation at $w=0$ uses analytic continuation in a noncharacter variable. This distinction is essential to the claim boundary.

The determinant baseline is the standard Fredholm/periodic-orbit expansion behind SFT zeta functions [@bowenlanford1970]. Typical full-shift extensions can exhibit broad zeta behavior [@ward1999]; this is precisely why the nonprime and random controls are decisive rather than optional.

# The positive-cocycle symbolic lift

Let $p_1<p_2<\cdots$ be the tensor atoms in entropy order. The base graph $G$ has a loop $\ell_n$ at every vertex $n$ and adjacent arrows in both directions. Define $$\kappa(\ell_n)=0,\qquad \kappa(e)=1
 \quad\text{for every cross edge }e.                   \tag{3.1}$$ The skew graph $\widetilde G$ has vertices $(n,k)\in\mathbb N\times\mathbb Z$ and an edge $(n,k)\to(m,k+\kappa(e))$ above every base edge $e:n\to m$.

[\[thm:lift-ledger\]]{#thm:lift-ledger label="thm:lift-ledger"} Modulo translation in the second coordinate, the primitive periodic paths of $\widetilde G$ are exactly the atom loops $\gamma_p$. Their $r$th traversals have roof $r\log p$ and weight $p^{-rs}$.

A lifted closed path has total cocycle charge zero. Every cross edge has strictly positive charge, so a charge-zero word contains no cross edge. It is therefore a power of one vertex loop. Primitive reduction and deck translation give the stated list.

The base graph itself is strongly connected and aperiodic; recurrence has not been deleted from the grammar. It has instead been separated by an intrinsic displacement ledger. The lift is noncompact and contains infinitely many deck translates of every loop, so counting is always performed per deck cell or, equivalently, in Fourier space. This convention is part of the object, not an after-the-fact normalization.

Set $$d_n(s)=p_n^{-s},\qquad
 a_n(s)=\frac{d_n(s)+d_{n+1}(s)}2.                     \tag{3.2}$$ The endpoint average is a frozen symmetric modeling choice. It supplies cross dynamics but receives no arithmetic credit. On $\ell^2(\mathbb N)\otimes\ell^2(\mathbb Z)$ the transfer commutes with deck translation. It is not ordinary trace class there: deck translations have infinite multiplicity. It belongs instead to the semifinite algebra $B(\ell^2\mathbb N)\,\bar\otimes\,L(\mathbb Z)$ with trace $\operatorname{Tr}\bar\otimes\tau_{\mathbb Z}$. Fourier transform in the second coordinate gives ordinary trace-class fibers $$L_s(w)=D_s+wA_s,\quad
 A_s=\sum_{n\ge1}a_n(s)
 (E_{n+1,n}+E_{n,n+1}),\quad w\in\mathbb T.                \tag{3.3}$$ Complex $w$ off the unit circle is used only as an analytic continuation of this family, not as a deck character.

# The resolved Fredholm determinant

[\[thm:trace-class\]]{#thm:trace-class label="thm:trace-class"} For $\Re s>1$, $L_s(w)$ is trace class, locally holomorphic in $(s,w)$ for $|w|$ bounded, and $$\mathcal D(s,z,w)=\det(I-zL_s(w))                            \tag{4.1}$$ is locally holomorphic in $(s,w)$ and entire in $z$.

The diagonal trace norm is $\sum_np_n^{-\Re s}$. Each directed weighted shift in $A_s$ has singular values $|a_n(s)|$, and $\sum_n|a_n(s)|\le\sum_np_n^{-\Re s}$. Local uniform summability also gives trace-norm holomorphy. Standard Fredholm theory then gives (4.1).

[\[thm:zero-mode\]]{#thm:zero-mode label="thm:zero-mode"} On the common trace-log germ at $z=0$, $$[w^0]\log\mathcal D(s,z,w)
 =\sum_p\log(1-zp^{-s}).                               \tag{4.2}$$ Consequently $[w^0]\mathcal D(s,z,w)=\prod_p(1-zp^{-s})$.

Expand $\operatorname{Tr}L_s(w)^r=\sum_{m\ge0}c_{r,m}(s)w^m$. Matrix trace closes the base word; the exponent is its cocycle displacement. Degree zero therefore contains only the loop at each vertex, so $c_{r,0}=\sum_pp^{-rs}$. Substitution into $\log\det(I-zL)=-\sum_{r\ge1}z^r\operatorname{Tr}(L^r)/r$ gives (4.2). Every remaining term has positive $w$ degree, so exponentiation preserves the constant coefficient.

For sufficiently small $z$, (4.2) is also the Haar average of a continuous local logarithm over $w=e^{i\theta}$. We do not infer a global logarithm through fiber zeros. At $z=1$, the scalar right-hand side is the reciprocal Euler product on its honest half-plane; this equality does not continue the full resolved family across the critical strip.

The smallest fiber already moves. With two masses $x,y$ and $a=(x+y)/2$, $$\det\!\begin{pmatrix}1-zx&-zaw\\-zaw&1-zy\end{pmatrix}
 =(1-zx)(1-zy)-z^2a^2w^2.                              \tag{4.3}$$ Thus the hidden recurrent return becomes visible at character degree two while the target coefficient stays exact.

[\[cor:no-fiber\]]{#cor:no-fiber label="cor:no-fiber"} At the frozen real points and every $|w|=1$, $$\operatorname{Tr}L_s(w)^2=\sum_n p_n^{-2s}+2w^2\sum_na_n(s)^2.     \tag{4.4}$$ No unitary character fiber has the pure Euler all-order ledger. Exactness belongs to the deck-neutral coefficient; $w=0$ recovers it algebraically but is not a character and deletes the cross grammar.

# Gauge, reversal, and the holonomy trilemma

If the edge charge has the form $\kappa(i\to j)=\psi_j-\psi_i$, then for $|w|=1$ $$L_s(w)=U_\psi(w)L_s(1)U_\psi(w)^{-1},\qquad
 U_\psi(w)e_j=w^{\psi_j}e_j.                           \tag{5.1}$$ The resolved determinant is independent of the character.

Entropy and rank vertex potentials therefore give no holonomy. A different natural-looking twist is equally sterile: attaching the character to the entropy roof yields $$p^{-s}e^{i\theta\log p}=p^{-(s-i\theta)},              \tag{5.2}$$ which is only a vertical reparameterization of the original family.

[\[thm:trilemma\]]{#thm:trilemma label="thm:trilemma"} Let the two orientations of an adjacent edge have integer charges $q$ and $\bar q$. The mixed two-cycle stays outside Fourier degree zero exactly when $q+\bar q\ne0$. Inverse time reversal requires $\bar q=-q$ and therefore places this mixed return in degree zero at power two. Hence the following three requirements cannot hold simultaneously:

1.  recurrent adjacent returns in the base;

2.  an exact pure-loop zero Fourier ledger;

3.  inverse labels on reversed edges.

The character weight of the two-edge return is $w^{q+\bar q}$. It contributes to the target coefficient precisely when the exponent is zero. Edge inversion makes that equality automatic.

The primary choice $q=\bar q=1$ therefore buys visibility and ledger exactness by giving up inverse reversal. This is not cosmetic. On a strongly connected graph, a nonnegative coboundary must vanish on every edge: each edge lies on a directed cycle whose nonnegative charges sum to zero. Positive holonomy cannot simultaneously be an exact reversible gauge.

Finally, none of these arguments uses primality once a positive summable inventory has been supplied. Every two positive masses satisfy (4.3), every positive random charge keeps mixed paths out of degree zero, and every forward DAG can carry determinant-invisible phase data. Arithmetic specificity must therefore come from more than character resolution itself.

# Exact and numerical falsification audit

The preregistered experiment has four layers. First, exact path enumeration checks all closed words through power twelve on the smallest graphs, recording their cocycle degree before any scalar character evaluation. Second, continuant polynomials compute finite resolved determinants without Fourier aliasing. Third, direct character grids and selected high-precision points audit the polynomial evaluation, gauge similarity, and roof translation. Fourth, the identical protocol is run on composite, shuffled, random, DAG, inverse-label, and positive-random-charge controls.

The source lock fixes cutoffs $N=2,3,4,8,16,32,64,128$, four source points, three determinant radii, all $1024$ characters, and all random seeds. The specificity statistic is the normalized nonconstant coefficient energy $$E_N(s,z)=\frac{\bigl(\sum_{m\ge1}|d_m|^2\bigr)^{1/2}}
 {|d_0|},\qquad
 \det(I-zL_s(w))=\sum_m d_mw^m.                         \tag{6.1}$$ The preregistered arithmetic GO requires nonzero prime response but exact collapse on every matched control. This is intentionally stronger than merely observing different amplitudes after changing the mass scale.

#### Frozen outcome.

The run contains $384$ frozen determinant rows. Exact path census for $N=2,\ldots,5$ through power twelve finds no positive-cocycle mixed word of charge zero; inverse labels first leak at power two. Continuant, dense character, trace-power, and selected 80-digit evaluations agree to at most $6.09\times10^{-16}$, while the gauge and roof controls have residual at most $6.21\times10^{-17}$.

At the preregistered summary point $(N,s,z)=(32,1.5,0.35)$, the coefficient energy (6.1) is $$\begin{array}{c|cccc}
\text{inventory}&\text{tensor primes}&\text{composites}&\text{shuffled}
 &\text{random increasing}\\ \hline
E&1.49110\times10^{-2}&2.35352\times10^{-3}&5.02776\times10^{-5}
 &3.19709\times10^{-5}.
\end{array}                                               \tag{6.2}$$ All $32$ positive random-charge controls are also nonzero, with $E\in[1.15221,1.42214]\times10^{-2}$. These values audit a theorem-level failure: the exact $w^2$ coefficient is nonzero for every positive inventory, so no larger cutoff can make all matched controls collapse. The response passes character visibility but fails arithmetic selectivity. All $25$ unit tests pass. No Riemann zeros, target crossings, or selected characters are computed.

Numerical values in the final artifact are checks of exact identities. They are not promoted to analytic continuation, divisor matching, or asymptotic zero-count evidence.

# Route-A conclusion

SD-C15 advances the program in one precise sense: the Euler target mode and the recurrent moving modes now live in one character-resolved Fredholm family. The candidate receives analytic A0--A2 credit, but A3 fails because no moving unitary fiber owns the target ledger: $$\begin{gathered}
 (\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
  \texttt{A1\_PASS\_ANALYTIC},
  \texttt{A2\_ANALYTIC\_DETERMINANT},\\
  \texttt{A3\_FAIL},
  \texttt{A4\_FAIL}).
\end{gathered}                                           \tag{7.1}$$

The overall verdict is `ROUTE_A_REJECTED` for the proposed RH mechanism. Three missing properties are decisive.

-   There is no arithmetic selection rule for a distinguished nonzero character; matched inventories reproduce the motion.

-   Inverse time reversal returns mixed adjacent cycles to the target mode, whereas intrinsic entropy twists are gauge or translations.

-   The construction supplies no critical-strip continuation, Gamma factor, functional equation, Riemann--von Mangoldt law, Weil compression, or fixed self-adjoint generator.

The stage status is

`GO_CHARACTER_RESOLUTION`

`GO_EQUIVARIANT_EULER_LEDGER / STOP_UNIFIED_BLOCH_FIBER`

`STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`

`STOP_INVERSE_TIME_REVERSAL / ROUTE_B_LOCKED`.

Route B remains locked. The next same-family question is narrower: can a finite-description symbolic cocycle derive a nontrivial character from tensor factorization itself, rather than from a generic edge counter, while keeping the target coefficient and inverse symmetry? Absent such a selector, more character scans only enlarge a proves-too-much family.

# Proof details and scope ledger

#### Trace-norm holomorphy.

On every compact subset of $\Re s>1$, the series $\sum_np_n^{-\Re s}$ is uniformly convergent. The same majorant controls the diagonal and both weighted shifts, including all local $s$ derivatives after the usual logarithmic factor. This supplies the trace-norm holomorphic family used in [\[thm:trace-class\]](#thm:trace-class){reference-type="ref" reference="thm:trace-class"}.

#### Coefficient extraction.

At finite cutoff the determinant is a polynomial in $w$. At infinite cutoff, the trace-log is a normally convergent power series for sufficiently small $z$, and coefficient extraction commutes with the trace and repetition sums. The scalar Euler identity then extends in its own honest half-plane. We do not assert that a single logarithm branch survives every resolved fiber zero.

#### Periodicity convention.

The one-sided skew product is autonomous but not an invertible covering. Primitive lifted paths are counted modulo deck translation using the canonical semifinite trace per cell. The lifted operator is not ordinary trace class. Calling the strongly connected base "recurrent" is a graph statement; no positive-recurrence theorem for the countable lifted shift is claimed.

#### Evidence labels.

The lifted ledger, trace-class theorem, zero-mode identity, two-atom formula, gauge lemma, and reversal trilemma are proved analytically. Finite computations are labeled `NUMERICAL_OBSERVATION` or exact implementation certificates. Arithmetic specificity is `REFUTED` for the frozen statistic and controls. Analytic continuation, a target divisor, and a Hilbert--Pólya operator remain `OPEN` or absent, not numerically supported.

#### Round-two boundary.

Any geometric magnetic flux, scattering phase, or Hamiltonian carrier is recorded only as a `ROUND2_CLUE`. No such system is used in the candidate, proof, experiment, or Route-A tuple.
