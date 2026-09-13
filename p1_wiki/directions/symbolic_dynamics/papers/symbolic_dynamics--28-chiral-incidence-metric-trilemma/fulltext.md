---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--28-chiral-incidence-metric-trilemma"
canonical_tex: "symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma/main.tex"
canonical_pdf: "symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma/main.pdf"
source_sha256: "e6bd13064e60a7374202f17f30d1e312836255bec015f3f2e3293d12deec2d27"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Chiral Completion Trilemma for Möbius-Incidence Atoms: Schatten-3 Motion versus Metric Collapse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/28-chiral-incidence-metric-trilemma/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study a canonical chiral completion of source-derived Möbius incidence idempotents on a weighted divisibility Hilbert space. The oblique atom family is boundedly similar to coordinate projections, so its Dirichlet operator $T_s$ belongs to $\mathcal S_q$ exactly when $q\Re s>1$. For the holomorphic reflected block $\mathcal B_s=\bigl(\begin{smallmatrix}0&T_s\\
  T_{1-s}^{\mathord{\sharp}}&0\end{smallmatrix}\bigr)$, the two legs give the sharp common strip $1/q<\Re s<1-1/q$; hence $q=3$ is the first integer order reaching the critical line. There $\mathcal B_{1/2+it}$ is compact self-adjoint but not Hilbert--Schmidt. We compute the native mixed Gram matrix exactly and prove that the fourth spectral moment has a positive isolated Fourier coefficient $4G_{pq}^2/(pq)$, so the self-adjoint spectrum genuinely moves with $t$. This motion is not arithmetically selective: exact mutated, composite-only, and generic poset controls reproduce it. Conversely, every bounded positive metric making the active idempotents self-adjoint has atom-diagonal conjugate $Z^*GZ$, forcing independent coordinate blocks and erasing all $t$-motion. Thus the canonical completions exhibit a precise trilemma between native motion, arithmetic selectivity, and metric orthogonality. The resulting third-regularized determinant is honest, but the construction is a $t$-dependent family rather than a fixed Hilbert--Pólya operator.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  The Chiral Completion Trilemma for Möbius-Incidence Atoms:\
  Schatten-3 Motion versus Metric Collapse
```

## Markdown 正文

# Introduction {#sec:introduction}

Incidence inversion offers a particularly transparent route from a locally finite relation to a family of primitive idempotents. For divisibility, the zeta matrix $Z$ and its Möbius inverse $M$ produce $$q_n=ZE_nM,\qquad q_nq_m=\delta_{nm}q_n.$$ The covers of the bottom element are the primes, so the associated Dirichlet family $$T_s=\sum_p p^{-s}q_p$$ has an honest Euler determinant in its trace-class half-plane. The same construction exposes its apparent weakness: the $q_p$ are oblique and globally similar to coordinate projections.

This paper asks whether the obliqueness can be turned into an asset. We join $T_s$ to a holomorphically reflected adjoint leg and study $$\mathcal B_s=
  \begin{pmatrix}0&T_s\\T_{1-s}^{\mathord{\sharp}}&0\end{pmatrix}.$$ The reflection is complex-linear away from the critical line and becomes the Hilbert adjoint on it. The resulting answer has a positive and a negative half.

#### Positive half.

The block belongs to $\mathcal S_q$ exactly on $$\frac1q<\Re s<1-\frac1q.$$ Thus $\mathcal S_3$ is the first integer Schatten ideal whose common strip contains $\Re s=1/2$. On that line the block is compact self-adjoint. Although the second trace is divergent, the fourth trace is honest, and unique factorization isolates a strictly positive Fourier coefficient. The native self-adjoint spectrum therefore really moves with $t$.

#### Negative half.

The motion is carried by mixed Hilbert--Schmidt Gram coefficients of the oblique idempotents. Exact computations reproduce it after mutating divisibility, replacing the prime atoms by composites, and replacing divisibility by a seeded finite DAG. The effect is therefore generic incidence geometry rather than an arithmetic selector. Moreover, every positive metric that makes the active idempotents self-adjoint is classified by their coordinate commutant. It forces the active family to become independent one-dimensional atom blocks, whose reflected eigenvalues $\pm p^{-1/2}$ do not move with $t$.

#### Contributions.

Our main results are:

1.  the exact Schatten threshold and the minimal $\mathcal S_3$ critical strip;

2.  closed formulas for the diagonal and mixed divisibility Gram coefficients;

3.  a positive, isolated fourth-moment frequency proving genuine spectral motion after the $\det\nolimits_3$ deletion;

4.  a complete classification of bounded positive common orthogonalizing metrics on the active sector;

5.  exact adversarial controls proving that native motion lacks arithmetic selectivity.

The result is deliberately not presented as a Hilbert--Pólya construction. The operator $\mathcal B_{1/2+it}$ depends on $t$; its third-regularized determinant is different from the original Euler determinant; and no target-zero information enters any definition or test. The strict route record is rejected.

#### Organization.

fixes the incidence and literature boundary. proves the Schatten threshold. derives the native Gram geometry. establishes the first honest spectral motion. proves metric rigidity. reports the exact adversaries, and [8](#sec:route){reference-type="ref" reference="sec:route"} states the completion trilemma and route decision.

# Source compiler and prior boundary {#sec:source}

## Weighted divisibility realization

Fix $\eta>1$ and let $$\mathcal H_\eta=
 \left\{x=(x_n)_{n\ge1}:
 \sum_{n\ge1}n^{2\eta}|x_n|^2<\infty\right\}.$$ The divisibility zeta operator and its Möbius inverse are denoted by $Z$ and $M=Z^{-1}$. In this range both are bounded and boundedly invertible. Let $E_n$ be the coordinate projection and define $$q_n=ZE_nM.$$ Then $$q_nq_m=\delta_{nm}q_n,\qquad
 \sum_nq_n=I$$ in finite cutoffs, and the individual $q_n$ extend as bounded rank-one idempotents in the countable realization.

For the atom set $A$ of covers of the bottom element, define $$D_s^A=\sum_{p\in A}p^{-s}E_p,
 \qquad
 T_s=ZD_s^AM=\sum_{p\in A}p^{-s}q_p.$$ In the unmutated divisibility relation, $A=\mathbb P$.

## Holomorphic reflection

Let $J$ be coordinate conjugation after normalizing the weighted coordinate basis. For source-real operators put $$X^{\mathord{\sharp}}=JX^*J.$$ This reflection is complex-linear, reverses products, and preserves all Schatten norms. In unnormalized coordinates it is $$X^{\mathord{\sharp}}=W_\eta^{-1}X^{\mathsf T}W_\eta,
 \qquad W_\eta=\operatorname{diag}(n^{2\eta}).$$ The reflected block $$\mathcal B_s=
 \begin{pmatrix}
 0&T_s\\T_{1-s}^{\mathord{\sharp}}&0
 \end{pmatrix}$$ is therefore holomorphic on every common Schatten domain. When $s=1/2+it$, the reflected leg equals $T_s^*$.

## Marker ownership {#subsec:marker}

The critical theorem in this paper is the arithmetic specialization $u=1$. The inherited digit marker could be retained formally as $$T_s(u)=\sum_pu^{\ell(p)}p^{-s}q_p.$$ Two firewalls are essential. First, the $r$-fold atom contribution is $u^{r\ell(p)}$, not $u^{\ell(p)}$. Second, when $|u|<1$ the Schatten sum becomes $$\sum_p|u|^{q\ell(p)}p^{-q\Re s},$$ so the threshold changes. This is a different regularized family, not analytic continuation of the $u=1$ critical object.

## Literature boundary

Rota's incidence-algebra framework supplies the Möbius source [@Rota1964]. Oblique projections and biorthogonal Riesz systems are classical operator geometry [@Tang2000], and compatibility with positive diagonal weights has been studied in the weighted projection setting [@AntezanaEtAl2004]. The square-root metric transfer is the operator form of symmetric orthogonalization [@Lowdin1950].

Schatten ideals and modified determinants are standard [@Simon2005]. Higher determinant product formulas require explicit correction terms [@BritzEtAl2020; @KoutsonikosLesch2022]; we therefore keep a power-by-power deletion ledger rather than treating $\det\nolimits_3$ as an ordinary determinant. Recent work on Möbius inversion over locally finite posets remains combinatorial rather than chiral-operator theoretic [@Goh2026].

The individual tools are classical. The new content is the exact source-locked synthesis: the minimal common strip, the divisibility Gram formula, the isolated fourth frequency, the non-arithmetic adversaries, and the full positive-metric collapse theorem.

# The exact Schatten-3 threshold {#sec:strip}

[\[thm:similarity\]]{#thm:similarity label="thm:similarity"} For every $q\ge1$, $$T_s\in\mathcal S_q
 \quad\Longleftrightarrow\quad
 \sum_{p\in A}p^{-q\Re s}<\infty.$$ For the prime atom set this is equivalent to $q\Re s>1$.

The identities $$T_s=ZD_s^AZ^{-1},\qquad D_s^A=Z^{-1}T_sZ$$ and the two-sided ideal property show that $T_s\in\mathcal S_q$ iff $D_s^A\in\mathcal S_q$. The latter is diagonal with singular values $p^{-\Re s}$. For primes, the corresponding series converges above exponent one, diverges at exponent one by Euler's prime harmonic theorem, and also diverges below it.

[\[thm:strip\]]{#thm:strip label="thm:strip"} For every $q\ge1$, $$\mathcal B_s\in\mathcal S_q
 \quad\Longleftrightarrow\quad
 \frac1q<\Re s<1-\frac1q.$$ The strip is nonempty exactly for $q>2$. In particular, $$\mathcal B_{1/2+it}\in\bigcap_{q>2}\mathcal S_q,
 \qquad
 \mathcal B_{1/2+it}\notin\mathcal S_2.$$

For $B=\bigl(\begin{smallmatrix}0&A\\C&0\end{smallmatrix}\bigr)$, $B^*B=\operatorname{diag}(C^*C,A^*A)$, so $B\in\mathcal S_q$ iff both legs belong to $\mathcal S_q$. gives $q\Re s>1$ for the first leg and $q(1-\Re s)>1$ for the reflected leg. Solving yields the stated strip.

[\[prop:selfadjoint\]]{#prop:selfadjoint label="prop:selfadjoint"} For every real $t$, $\mathcal B_{1/2+it}$ is compact self-adjoint.

The incidence idempotents are source-real, and $1-(1/2+it)=1/2-it=\overline{1/2+it}$. Therefore $T_{1-s}^{\mathord{\sharp}}=T_s^*$ on the line. Compactness follows from [\[thm:strip\]](#thm:strip){reference-type="ref" reference="thm:strip"}, for example with $q=3$.

makes the boundary obstruction explicit. The critical-line family is not Hilbert--Schmidt, so its second power is not trace class. This fact determines which spectral moment and which modified determinant are admissible.

[\[rem:family\]]{#rem:family label="rem:family"} does not construct a single operator with $t$ as spectral variable. It constructs a map $t\mapsto\mathcal B_{1/2+it}$ whose value is self-adjoint for each $t$. This is a positive analytic statement but fails the strict fixed- operator route gate.

# Native mixed-Gram geometry {#sec:gram}

The source formula for a primitive incidence idempotent is $$q_n(a,b)=\mathbf 1_{a\mid n}\,
 \mu(b/n)\mathbf 1_{n\mid b}.$$ Write $q_n=u_nv_n^{\mathsf T}$ and define $$G_{pq}=\operatorname{Tr}(q_pq_q^{\mathord{\sharp}}),\qquad
 C_\eta=\sum_{k\ge1}\frac{\mu(k)^2}{k^{2\eta}}
 =\frac{\zeta(2\eta)}{\zeta(4\eta)}.$$

[\[thm:gram\]]{#thm:gram label="thm:gram"} For primes $p,q$, $$G_{pp}=C_\eta(1+p^{-2\eta}),$$ and, if $p\ne q$, $$G_{pq}=
 C_\eta\,
 \frac{(pq)^{-2\eta}}
 {(1+p^{-2\eta})(1+q^{-2\eta})}>0.$$

The weighted rank-one contraction factors as $$G_{pq}=
 \left(\sum_a u_p(a)u_q(a)a^{2\eta}\right)
 \left(\sum_b v_p(b)v_q(b)b^{-2\eta}\right).$$ For $p=q$ the two factors are $1+p^{2\eta}$ and $p^{-2\eta}C_\eta$. For $p\ne q$, the primal overlap is the shared bottom coordinate $1$. A nonzero dual term has $b=pqk$, with $k$ squarefree and coprime to $pq$; the two Möbius signs multiply to $+1$. Removing the $p,q$ Euler factors from $C_\eta$ gives the formula. Details are recorded in [10.1](#app:gram){reference-type="ref" reference="app:gram"}.

[\[prop:b2\]]{#prop:b2 label="prop:b2"} For a finite atom set $F$ and $s=1/2+it$, $$\operatorname{Tr}\mathcal B_s^2
 =2\sum_{p\in F}\frac{G_{pp}}p+
 4\sum_{\substack{p<q\\p,q\in F}}
 \frac{G_{pq}}{\sqrt{pq}}
 \cos\left(t\log\frac qp\right).$$

Both diagonal blocks of $\mathcal B_s^2$ have the same trace. Expanding one of them gives $$\operatorname{Tr}\mathcal B_s^2
 =2\sum_{p,q\in F}
 p^{-1/2-it}q^{-1/2+it}G_{pq}.$$ Pair the ordered terms $(p,q)$ and $(q,p)$.

At $\eta=2$, $$C_2=\frac{105}{\pi^4},\quad
 G_{22}=\frac{1785}{16\pi^4},\quad
 G_{33}=\frac{2870}{27\pi^4},\quad
 G_{23}=\frac{105}{1394\pi^4}.$$ The exact two-atom cutoff is therefore $$G_{22}+\frac{2G_{33}}3+
 \frac{4G_{23}}{\sqrt6}
 \cos\left(t\log\frac32\right).$$ For atoms $2,3,5$, add the three pair frequencies, with $$G_{55}=\frac{105\cdot626}{625\pi^4},\quad
 G_{25}=\frac{105}{10642\pi^4},\quad
 G_{35}=\frac{105}{51332\pi^4}.$$

## The second-trace firewall

[\[prop:no-b2\]]{#prop:no-b2 label="prop:no-b2"} On the critical line, $\mathcal B_s^2$ is not trace class. Its diagonal cutoff contribution satisfies $$\sum_p\frac{2G_{pp}}p
 \ge2C_\eta\sum_p\frac1p=\infty.$$

Thus [\[prop:b2\]](#prop:b2){reference-type="ref" reference="prop:b2"} is an exact finite-cutoff diagnostic, not a conditionally interpreted infinite trace. The mixed terms decay rapidly for $\eta>1$, but their summability does not repair the missing full trace. The correct countable object begins with third regularization.

# Third regularization and surviving spectral motion {#sec:regularized}

On the strip $1/3<\Re s<2/3$, define the honest modified determinant $$\det\nolimits_3(I-z\mathcal B_s).$$ For small $z$ its logarithm is $$\log\det\nolimits_3(I-z\mathcal B_s)
 =-\sum_{m\ge3}\frac{z^m}{m}\operatorname{Tr}(\mathcal B_s^m).$$ The regularization deletes powers one and two. Odd powers of an off-diagonal block remain off diagonal, so every odd trace vanishes. Consequently $$\log\det\nolimits_3(I-z\mathcal B_s)
 =-\frac{z^4}{4}\operatorname{Tr}(\mathcal B_s^4)+O(z^6).$$ The second-trace Gram ledger is removed together with its harmonic divergence; the fourth moment is the first legal signal.

[\[thm:fourth\]]{#thm:fourth label="thm:fourth"} For every pair of distinct primes $p,q$, the coefficient of $$\cos\left(2t\log\frac qp\right)$$ in $\operatorname{Tr}\mathcal B_{1/2+it}^4$ is $$\frac{4G_{pq}^2}{pq}>0.$$ Hence the native compact self-adjoint spectrum is nonconstant in $t$, and $\det\nolimits_3(I-z\mathcal B_{1/2+it})$ is nonconstant in $t$ as an analytic germ in $z$.

Put $a_p=p^{-1/2-it}$. On the critical line, $$\operatorname{Tr}\mathcal B_s^4=2\operatorname{Tr}\bigl((T_sT_s^*)^2\bigr).$$ The tuple $(p,q,p,q)$ in the expansion contributes $$2a_p^2\overline{a_q}^{\,2}
 \operatorname{Tr}\bigl((q_pq_q^*)^2\bigr).$$ Since $q_pq_q^*$ has rank at most one, $$\operatorname{Tr}\bigl((q_pq_q^*)^2\bigr)
 =\operatorname{Tr}(q_pq_q^*)^2=G_{pq}^2.$$ Adding the conjugate tuple gives the stated cosine coefficient.

No other tuple can cancel it: a quotient of two products of two primes equals $q^2/p^2$ only when unique factorization forces the numerator multiset to be $\{q,q\}$ and the denominator multiset to be $\{p,p\}$. Prime cutoffs converge uniformly in $\mathcal S_4$ for all real $t$; continuity of the fourth trace moment passes the isolated coefficient to the countable limit. See [10.2](#app:fourier){reference-type="ref" reference="app:fourier"} for the continuity estimate.

For $(p,q,\eta)=(2,3,2)$, the isolated coefficient is exactly $$\frac{3675}{971618\pi^8}
 \cos\left(2t\log\frac32\right).$$

proves genuine spectral motion, not merely motion of eigenvectors. It does not restore the original Euler trace ledger: the determinant is third-regularized, its first visible term is fourth order, and its coefficients involve mixed Gram cycles. The adversaries in [7](#sec:audit){reference-type="ref" reference="sec:audit"} show that this surviving motion is not arithmetically selective.

# Positive metric rigidity and atom collapse {#sec:metric}

Could another positive metric remove the mixed Gram defect while retaining a coupled spectrum? The answer is no for the entire bounded positive class.

[\[thm:metric\]]{#thm:metric label="thm:metric"} Let $G$ be bounded, positive, and boundedly invertible. Then $$Gq_n=q_n^*G\quad\text{for every }n$$ if and only if $$Z^*GZ=D$$ for a positive bounded diagonal $D$ with bounded inverse. If the condition is imposed only for active atoms, $Z^*GZ$ is diagonal on the active coordinates, has no active--dormant coupling, and may have an arbitrary positive block on the dormant complement.

With $K=Z^*GZ$, conjugating $Gq_n=q_n^*G$ gives $$KE_n=E_nK.$$ The joint commutant of all coordinate projections is diagonal. Commutation with only the active $E_p$ annihilates the off-diagonal row and column at every active coordinate, leaving one arbitrary dormant block. Positivity and bounded invertibility are preserved under bounded congruence.

[\[cor:collapse\]]{#cor:collapse label="cor:collapse"} Let $S=G^{1/2}$, $K=Z^*GZ$, and $$U=SZK^{-1/2}.$$ Then $U$ is unitary and $$ST_sS^{-1}=UD_s^AU^*.$$ Thus every positive common metric that makes the active idempotents self-adjoint sends them to mutually orthogonal coordinate atoms.

The identity $U^*U=I$ is immediate. By [\[thm:metric\]](#thm:metric){reference-type="ref" reference="thm:metric"}, $K$ commutes with $D_s^A$, so the displayed conjugacy follows after inserting $K^{1/2}K^{-1/2}$.

In the orthogonal atom basis, the reflected block is the direct sum of $$\begin{pmatrix}
 0&p^{-s}\\p^{-(1-s)}&0
 \end{pmatrix}.$$ Each block squares to $p^{-1}I_2$, so its paired eigenvalues are $\pm p^{-1/2}$, independent of $s$. The third-regularized product is $$\det\nolimits_3(I-z\widehat{\mathcal B}_s)
 =\prod_p\left(1-\frac{z^2}{p}\right)
 \exp\left(\frac{z^2}{p}\right).$$ It converges because each logarithm is $O(p^{-2})$, but it is independent of $t$. Its auxiliary zeros $z=\pm\sqrt p$ are explicit atom values and have no target-zero interpretation.

is a scoped no-go. It classifies bounded positive common metrics; it does not classify indefinite or unbounded metric operators, whose domains and determinant theory would constitute a different problem.

# Deterministic exact adversarial audit {#sec:audit}

The exact prototype compiles every idempotent from a finite poset relation as $q_x=ZE_xZ^{-1}$. It does not supply a projector table or a primality oracle. All identities use integers, rational arithmetic, or exact symbolic radicals; floating point is used only to display common-$t$ samples.

L3.6cmL2.5cmcccc Fixture & active labels & mixed Gram & native $B^2$ & native $B^4$ & metric phase\
standard divisibility, $N=30$ & $2,3,5$ & yes & moves & moves & absent\
mutated divisibility, $N=12$ & $2,3,5,6$ & yes & moves & moves & absent\
composite-only subposet & $4,6,9$ & yes & moves & moves & absent\
seeded locally finite DAG & $10,14,21$ & yes & moves & moves & absent\

The mutated relation deletes $2<6$ and $3<6$, making $6$ an atom. The composite-only subposet has bottom covers $4,6,9$. The generic fixture is a deterministic DAG with seed $2801$. Exact witnesses include $$G_{23}^{(N=30)}=\frac{313}{405000},\qquad
 G_{4,6}^{(\mathrm{comp})}=\frac1{20736},\qquad
 G_{10,14}^{(\mathrm{DAG})}=\frac1{390625}.$$ These nonzero rational entries establish that the phase signal is not rounding noise.

## Representative common-$t$ samples

::: {#tab:samples}
  Fixture            $\operatorname{Tr}B^2(0)$   $\operatorname{Tr}B^2(1.3)$   $\operatorname{Tr}B^4(0)$   $\operatorname{Tr}B^4(1.3)$
  ---------------- --------------------------- ----------------------------- --------------------------- -----------------------------
  standard                        2.3055980793                  2.3053415717                1.0173068797                  1.0168511063
  mutated                         2.5967636512                  2.5966667902                1.0287302339                  1.0285865294
  composite-only                  1.1031574816                  1.1031514332                0.2215897527                  0.2215846316
  seeded DAG                      0.4773464242                  0.4773463427                0.0400704387                  0.0400704092

  : Displayed evaluations of exact symbolic expressions. The proof of nonconstancy uses nonzero exact Laurent coefficients, not the decimal differences.
:::

## Reproducibility and inference boundary

The frozen prototype has SHA-256

`e29553c5a04cb31393b6ef8f93d2718285bac52d956cffc04d4c8d53fc6cc737`,

and the result JSON has SHA-256

`118ae2e85e4ce8d403673f1d00725520c7137a3a032bb9201cda186a61cb5cfb`.

Two fresh executions were byte-identical and every exact control passed. The computation certifies finite formulas, control behavior, and metric identities. It does not replace the countable Schatten, Fourier-isolation, or metric-rigidity proofs.

# The completion trilemma and strict route {#sec:route}

The two canonical completions now admit a direct comparison.

L3.5cmYY Property & Native reflected metric & Positive common metric\
source incidence ownership & retained & retained under metric transfer\
critical self-adjointness & yes, as a $t$-dependent family & yes\
native mixed Gram & retained & removed\
fourth-order $t$-motion & exact and nonzero & erased\
arithmetic selectivity & fails aggregate controls & atom inventory only\
Euler determinant identity & not retained by chiral $\det\nolimits_3$ & phase-free atom product\
fixed spectral operator & no & no\

The native construction proves more than a formal analogy: it gives an analytic modified determinant and a compact self-adjoint spectrum whose fourth moment moves. Yet [\[tab:controls\]](#tab:controls){reference-type="ref" reference="tab:controls"} shows that the motion is generic. The metric construction removes this ambiguity only by reducing the active sector to independent coordinate atoms.

## Strict gate evaluation

L1.4cmL4.0cmY Gate & Status & Reason\
A0 & structural arithmetic relation & The compiler is derived from divisibility incidence and Möbius inversion.\
A1 & `FAIL` & The chiral completion does not preserve a pure Euler word/orbit ledger.\
A2 & analytic determinant & $\det\nolimits_3(I-z\mathcal B_s)$ is honest on $1/3<\Re s<2/3$.\
A3 & `FAIL` & Self-adjointness holds for a $t$-dependent family, not one fixed operator.\
A4 & `FAIL` & No continuation or target-zero equivalence theorem exists.\

No target-zero coordinates, fitting objective, or zero-labeled statistic appears in the construction or audit. The auxiliary zeros of the metric product are stated only as zeros in its $z$ variable.

# Conclusion {#sec:conclusion}

The reflected incidence construction clears a real analytic barrier. Its common Schatten domain is exact, the first integer order is $\mathcal S_3$, and on the critical line it gives a compact self-adjoint family. The fourth moment contains an isolated positive frequency, so native spectral motion is a theorem rather than a numerical impression.

That gain sharpens the obstruction. The exact motion is reproduced by mutated, composite-only, and generic locally finite posets. It comes from mixed Gram geometry, not from a demonstrated arithmetic selection rule. Every bounded positive metric that makes the active incidence idempotents self-adjoint is forced into their coordinate commutant. Its Hellinger/Löwdin transfer produces independent atom blocks and an $s$-independent modified product.

The resulting contribution is a canonical completion trilemma. The native metric retains motion but not selectivity; the positive metric retains orthogonality but not motion; neither gives a fixed Hilbert--Pólya operator. This is a strict route rejection, but it also identifies a focused next problem: classify source-natural renormalizations that subtract the diagonal prime-harmonic divergence without retaining a generic mixed-poset signal. A successful next step must distinguish global divisibility coherence, not merely pairwise obliqueness.

# Additional proof details

## Weighted rank-one contraction {#app:gram}

In unnormalized coordinates the weighted reflection is $X^{\mathord{\sharp}}=W_\eta^{-1}X^{\mathsf T}W_\eta$. For $q_p=u_pv_p^{\mathsf T}$, $$q_q^{\mathord{\sharp}}
 =W_\eta^{-1}v_qu_q^{\mathsf T}W_\eta.$$ Consequently $$\begin{aligned}
\operatorname{Tr}(q_pq_q^{\mathord{\sharp}})
&=\operatorname{Tr}\left(
u_pv_p^{\mathsf T}W_\eta^{-1}v_qu_q^{\mathsf T}W_\eta
\right)\\
&=(u_q^{\mathsf T}W_\eta u_p)
  (v_p^{\mathsf T}W_\eta^{-1}v_q).
\end{aligned}$$ This also makes symmetry and nonnegativity of the divisibility coefficients transparent.

For distinct primes, write $b=pqk$. If $k$ contains $p$ or $q$, one of $\mu(b/p),\mu(b/q)$ vanishes. If any other prime divides $k$ twice, both vanish. Otherwise $$\mu(qk)\mu(pk)=\mu(k)^2=1.$$ Thus $$\begin{aligned}
v_p^{\mathsf T}W_\eta^{-1}v_q
&=(pq)^{-2\eta}
\sum_{\substack{k\ {\rm squarefree}\\(k,pq)=1}}k^{-2\eta}\\
&=(pq)^{-2\eta}
\frac{C_\eta}
{(1+p^{-2\eta})(1+q^{-2\eta})}.
\end{aligned}$$

## Uniform fourth-moment passage {#app:fourier}

Let $F_N$ be increasing finite prime sets and $$T_{s,N}=Z\left(\sum_{p\in F_N}p^{-s}E_p\right)Z^{-1}.$$ On the critical line, $$\sup_{t\in\mathbb R}
 \|T_{1/2+it}-T_{1/2+it,N}\|_4
 \le
 \|Z\|\,\|Z^{-1}\|
 \left(\sum_{p\notin F_N}p^{-2}\right)^{1/4}
 \longrightarrow0.$$ The same estimate holds for the reflected leg, hence for $\mathcal B$. For $A,B\in\mathcal S_4$, the telescoping identity and Hölder's trace inequality give, on norm-bounded sets, $$|\operatorname{Tr}(A^4)-\operatorname{Tr}(B^4)|
 \le C\|A-B\|_4.$$ Therefore the finite trigonometric polynomials $t\mapsto\operatorname{Tr}\mathcal B_{1/2+it,N}^4$ converge uniformly. Their Bohr Fourier coefficients pass to the limit.

To isolate frequency $2\log(q/p)$, a term with indices $(a,b,c,d)$ would require $$\frac{bd}{ac}=\frac{q^2}{p^2}.$$ Both sides are quotients of products of two primes. Equality of prime exponent vectors forces $a=c=p$ and $b=d=q$. Thus the coefficient computed in [\[thm:fourth\]](#thm:fourth){reference-type="ref" reference="thm:fourth"} is unique.

## Active commutant

Suppose $KE_p=E_pK$ for an active coordinate $p$. For $i\ne p$, the $(i,p)$ entry of the left side is $K_{ip}$ and of the right side is zero, so $K_{ip}=0$. The $(p,i)$ entry similarly gives $K_{pi}=0$. Applying this to each active $p$ proves the active one-dimensional blocks in [\[thm:metric\]](#thm:metric){reference-type="ref" reference="thm:metric"}.

If $K$ is positive and boundedly invertible, functional calculus defines $K^{-1/2}$. Then $$U^*U=K^{-1/2}Z^*GZK^{-1/2}=I.$$ Since $K$ is block diagonal with scalar active blocks, it commutes with $D_s^A$. This completes the unitary-collapse calculation without assuming that the dormant block is diagonal.

## Modified atom product

For one orthogonalized atom, the chiral block has eigenvalues $\lambda_\pm=\pm p^{-1/2}$. The third modified factors for $I-zB$ are $$(1-z\lambda_\pm)
 \exp\left(z\lambda_\pm+\frac{z^2\lambda_\pm^2}{2}\right).$$ Multiplying the pair cancels the linear exponentials and yields $$\left(1-\frac{z^2}{p}\right)e^{z^2/p}.$$ Since $$\log(1-z^2/p)+z^2/p=O(p^{-2})$$ locally uniformly in $z$, the prime product converges normally.

# Scope and ownership declarations

1.  **Arithmetic specialization.** Every critical-line theorem uses $u=1$. If $T_s(u)=\sum_pu^{\ell(p)}p^{-s}q_p$ is retained, an $r$-fold atom contribution carries $u^{r\ell(p)}$. The altered threshold for $|u|<1$ is not continuation of the $u=1$ result.

2.  **Trace ownership.** The finite formula for $\operatorname{Tr}\mathcal B_s^2$ is a cutoff identity. The countable $\mathcal B_{1/2+it}$ is not Hilbert--Schmidt, so no ordinary second trace is asserted.

3.  **Determinant ownership.** The Euler determinant of $T_s$ on $\Re s>1$ and the chiral $\det\nolimits_3(I-z\mathcal B_s)$ on $1/3<\Re s<2/3$ are different objects. The latter deletes powers one and two.

4.  **Spectral ownership.** The compact self-adjoint operator depends on $t$. No fixed operator with spectral parameter $t$ is claimed.

5.  **Metric scope.** Metric rigidity covers bounded positive boundedly invertible common metrics. It does not classify indefinite or unbounded metrics.

6.  **Control inference.** Mutated, composite-only, and generic-poset controls reproduce the native motion. Their role is to reject arithmetic selectivity.

7.  **Target-zero firewall.** No target-zero position, label, fitting criterion, or comparison enters the definitions, the exact audit, or the route decision. Auxiliary zeros in $z$ are not identified with zeta zeros.

8.  **Route status.** The frozen tuple is $$\begin{gathered}
      (\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
       \texttt{ A1\_FAIL},\\
       \texttt{A2\_ANALYTIC\_DETERMINANT},
       \texttt{ A3\_FAIL},\texttt{ A4\_FAIL}).
      \end{gathered}$$ Overall status is `ROUTE_A_REJECTED`; Route B is locked.
